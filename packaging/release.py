#!/usr/bin/env python3
"""Validate a release or build versioned packages from a committed Git snapshot."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from skill_text import ROOT, version


def check(repository: Path, tag: str | None = None) -> str:
    current = version(repository / "skills/card-creator")
    if tag is not None and tag != f"v{current}":
        raise ValueError(f"tag {tag!r} does not match Skill version v{current}")
    changelog = (repository / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"\n## [{current}] — " not in changelog:
        raise ValueError(f"CHANGELOG.md has no release entry for {current}")
    entry = (repository / "packaging/skillhub-zh-CN/entry.md").read_text(encoding="utf-8")
    if any(line.startswith("version:") for line in entry.splitlines()):
        raise ValueError("SkillHub entry must inherit the canonical version")
    return current


def archive_package(folder: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(folder).as_posix())


def build(repository: Path, ref: str, output: Path) -> dict:
    if output.exists():
        raise ValueError(f"output already exists: {output}")
    revision = subprocess.check_output(
        ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=repository, text=True,
    ).strip()
    paths = ["skills/card-creator", "packaging", "web/card-creator.md", "CHANGELOG.md", "LICENSE", "SOURCES.md", "DISCLAIMER.md"]
    snapshot = subprocess.check_output(
        ["git", "archive", "--format=zip", revision, *paths], cwd=repository,
    )
    with tempfile.TemporaryDirectory(prefix="card-creator-release-") as temporary:
        work = Path(temporary)
        source = work / "source"
        with zipfile.ZipFile(io.BytesIO(snapshot)) as archive:
            archive.extractall(source)
        current = check(source, ref if ref.startswith("v") else None)
        subprocess.run([sys.executable, str(source / "packaging/build_web_md.py"), "--check"], check=True)
        # All package inputs come from the commit, never the working directory.
        full = work / "full"
        full.mkdir()
        shutil.copytree(source / "skills/card-creator", full / "card-creator")
        zh = work / "zh-CN"
        zh.mkdir()
        subprocess.run([
            sys.executable, str(source / "packaging/skillhub-zh-CN/build.py"),
            str(zh / "card-creator"), "--revision", revision,
        ], check=True)
        manifest = {"version": current, "tag": f"v{current}", "source_revision": revision, "packages": {}}
        artifacts = work / "artifacts"
        artifacts.mkdir()
        for flavor, folder in (("full", full), ("zh-CN", zh)):
            for document in ("LICENSE", "SOURCES.md", "DISCLAIMER.md", "CHANGELOG.md"):
                shutil.copy2(source / document, folder / document)
            filename = f"card-creator-{current}-{flavor}.zip"
            archive_package(folder, artifacts / filename)
            manifest["packages"][flavor] = {
                "file": filename,
                "sha256": hashlib.sha256((artifacts / filename).read_bytes()).hexdigest(),
            }
        (artifacts / "release.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        sums = "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
            for path in sorted(artifacts.iterdir())
        )
        (artifacts / "SHA256SUMS").write_text(sums, encoding="utf-8")
        shutil.copytree(artifacts, output)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validation = commands.add_parser("check", help="validate working-tree version and changelog")
    validation.add_argument("--tag", help="expected Git tag, such as v0.5.0")
    package = commands.add_parser("build", help="build two ZIPs from a Git commit or tag, not local edits")
    package.add_argument("output", type=Path, help="new output directory")
    package.add_argument("--ref", default="HEAD", help="committed source revision; default HEAD")
    args = parser.parse_args()
    try:
        if args.command == "check":
            print(f"Release metadata valid: v{check(ROOT, args.tag)}")
        else:
            manifest = build(ROOT, args.ref, args.output.expanduser().resolve())
            print(json.dumps(manifest, indent=2))
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Release failed: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
