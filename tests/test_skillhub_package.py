from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import hashlib
import re
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPOSITORY / "packaging" / "skillhub-zh-CN" / "build.py"
CANONICAL_SKILL = REPOSITORY / "skills" / "card-creator"


class SkillHubPackageTests(unittest.TestCase):
    def test_build_shares_rules_and_pins_remote_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "card-creator"
            subprocess.run(
                [sys.executable, str(BUILD_SCRIPT), str(output)],
                check=True,
                capture_output=True,
                text=True,
            )

            skill_text = (output / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("displayName: 卡面生成器", skill_text)
            entry = BUILD_SCRIPT.with_name("entry.md").read_text(encoding="utf-8")
            self.assertEqual(re.search(r"^version: (.+)$", skill_text, re.M)[1], re.search(r"^version: (.+)$", entry, re.M)[1])
            canonical = (CANONICAL_SKILL / "SKILL.md").read_text(encoding="utf-8").split("\n---\n", 1)[1].strip()
            shared = skill_text.split("## Shared workflow\n", 1)[1].strip()
            self.assertEqual(shared, canonical.split("# Card Creator\n", 1)[1].strip())
            rules = (CANONICAL_SKILL / "references/card-rules.md").read_text(encoding="utf-8")
            self.assertEqual((output / "references/card-rules.md").read_text(encoding="utf-8"), rules)
            digest = hashlib.sha256((canonical + "\n" + rules.strip()).encode()).hexdigest()
            self.assertIn(f"rules sha256: {digest}", skill_text)
            self.assertNotIn("精确贴纸模式", skill_text)
            self.assertFalse(output.joinpath("references/reference-remix.md").exists())
            self.assertFalse(output.joinpath("references/prompt-guide.md").exists())
            self.assertFalse(
                output.joinpath("references/bank-issuer-catalog.md").exists()
            )
            self.assertFalse(any(output.rglob("*.py")))
            self.assertFalse(any(output.rglob("requirements.txt")))
            self.assertFalse(output.joinpath("assets/logo-references").exists())
            index = output.joinpath("references/logo-reference-index.md").read_text(encoding="utf-8")
            revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPOSITORY, text=True).strip()
            self.assertIn(f"Source revision: {revision}", skill_text)
            canonical_index = (CANONICAL_SKILL / "references/logo-reference-index.md").read_text(encoding="utf-8")
            expected = canonical_index.replace("../assets/logo-references/", f"https://raw.githubusercontent.com/juju-w/card-creator-skill/{revision}/skills/card-creator/assets/logo-references/")
            self.assertEqual(index, expected)
            self.assertNotIn("../assets/logo-references/", index)
            for reference in ("banks/china/cmb.png", "banks/usa/chase.png", "overseas/japan/suica.png", "overseas/canada/presto.png", "overseas/usa/ventra.png", "overseas/italy/venezia-unica-citypass.jpg", "overseas/south-korea/tmoney-card.jpg"):
                self.assertIn(reference, index)
            self.assertFalse(any(output.rglob("SOURCES.md")))
            self.assertFalse(output.joinpath("references/sticker-catalog.md").exists())
            self.assertFalse(output.joinpath("references/sticker-research.md").exists())
            self.assertFalse(output.joinpath("scripts/render_stickers.py").exists())
            self.assertFalse(any(output.rglob("*.png")))
            self.assertFalse(any(output.rglob("*.svg")))
            self.assertFalse(any(output.rglob(".DS_Store")))


if __name__ == "__main__":
    unittest.main()
