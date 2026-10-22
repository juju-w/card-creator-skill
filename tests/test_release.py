from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "packaging"))
from release import build, check
from skill_text import version


class ReleaseTests(unittest.TestCase):
    def test_canonical_version_and_tag_must_agree(self):
        current = version()
        self.assertEqual(check(ROOT, f"v{current}"), current)
        with self.assertRaisesRegex(ValueError, "does not match"):
            check(ROOT, "v999.0.0")

    def test_archives_use_commit_and_share_version(self):
        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary) / "repository"
            repository.mkdir()
            shutil.copytree(ROOT / "packaging", repository / "packaging", ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(ROOT / "web", repository / "web")
            skill = repository / "skills/card-creator"
            (skill / "references").mkdir(parents=True)
            for file in ("SKILL.md", "references/card-rules.md"):
                shutil.copy2(ROOT / "skills/card-creator" / file, skill / file)
            shutil.copytree(ROOT / "skills/card-creator/agents", skill / "agents")
            (skill / "assets/logo-references").mkdir(parents=True)
            (skill / "assets/logo-references/example.png").write_bytes(b"committed reference")
            (skill / "references/logo-reference-index.md").write_text("[Reference](../assets/logo-references/example.png)\n")
            for file in ("LICENSE", "SOURCES.md", "DISCLAIMER.md", "CHANGELOG.md"):
                shutil.copy2(ROOT / file, repository / file)

            def git(*args):
                return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()

            git("init", "-q")
            git("add", ".")
            git("-c", "user.name=Release Test", "-c", "user.email=release-test@example.invalid", "commit", "-qm", "fixture")
            revision = git("rev-parse", "HEAD")
            current = version(skill)
            git("tag", f"v{current}")
            # A dirty tracked file and an untracked asset must not reach either ZIP.
            (skill / "assets/logo-references/example.png").write_bytes(b"private dirty replacement")
            (skill / "private-draft.png").write_bytes(b"private draft")
            (skill / "SKILL.md").write_text("private broken working tree")
            output = Path(temporary) / "release"
            manifest = build(repository, f"v{current}", output)
            self.assertEqual(manifest["source_revision"], revision)
            self.assertEqual(json.loads((output / "release.json").read_text()), manifest)
            for line in (output / "SHA256SUMS").read_text().splitlines():
                digest, filename = line.split("  ")
                self.assertEqual(hashlib.sha256((output / filename).read_bytes()).hexdigest(), digest)
            for flavor, artifact in manifest["packages"].items():
                path = output / artifact["file"]
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), artifact["sha256"])
                with zipfile.ZipFile(path) as archive:
                    self.assertNotIn("card-creator/private-draft.png", archive.namelist())
                    self.assertFalse(any(name.endswith((".py", ".pyc")) for name in archive.namelist()))
                    self.assertIn("SOURCES.md", archive.namelist())
                    self.assertNotIn("card-creator/SOURCES.md", archive.namelist())
                    text = archive.read("card-creator/SKILL.md").decode()
                    self.assertIn(f'version: "{current}"', text)
                    if flavor == "full":
                        self.assertEqual(archive.read("card-creator/assets/logo-references/example.png"), b"committed reference")
                    else:
                        self.assertFalse(any(name.endswith(".png") for name in archive.namelist()))
                        index = archive.read("card-creator/references/logo-reference-index.md").decode()
                        self.assertIn(f"/{revision}/skills/card-creator/assets/", index)
                        self.assertIn(f"Source revision: {revision}", text)
            with self.assertRaisesRegex(ValueError, "already exists"):
                build(repository, "HEAD", output)
            git("tag", "v999.0.0")
            with self.assertRaisesRegex(ValueError, "does not match"):
                build(repository, "v999.0.0", Path(temporary) / "bad-release")


if __name__ == "__main__":
    unittest.main()
