#!/usr/bin/env python3
"""Build the localized SkillHub/WorkBuddy distribution package."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


LOCALIZED_FILES = (
    Path("SKILL.md"),
    Path("agents/openai.yaml"),
    Path("references/card-rules.md"),
)


def remove_junk(output: Path) -> None:
    for path in sorted(output.rglob("*"), reverse=True):
        if path.is_file() and (path.name == ".DS_Store" or path.suffix == ".pyc"):
            path.unlink()
        elif path.is_dir() and path.name == "__pycache__":
            shutil.rmtree(path)


def omit_binary_references(output: Path) -> None:
    """Keep a direct remote picture index in the text-only distribution."""
    references = output / "assets" / "logo-references"
    if references.exists():
        shutil.rmtree(references)
    logo_index = output / "references" / "logo-reference-index.md"
    if logo_index.exists():
        text = logo_index.read_text(encoding="utf-8")
        text = text.replace(
            "../assets/logo-references/",
            "https://raw.githubusercontent.com/juju-w/card-creator-skill/main/skills/card-creator/assets/logo-references/",
        )
        logo_index.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="new output directory")
    args = parser.parse_args()

    packaging_dir = Path(__file__).resolve().parent
    repository = packaging_dir.parents[1]
    source = repository / "skills" / "card-creator"
    output = args.output.expanduser().resolve()

    if output.exists():
        parser.error(f"output already exists: {output}")
    if not source.is_dir():
        parser.error(f"canonical skill directory is missing: {source}")

    shutil.copytree(source, output)

    for relative in LOCALIZED_FILES:
        localized = packaging_dir / relative
        if not localized.is_file():
            parser.error(f"localized file is missing: {localized}")
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(localized, destination)

    omit_binary_references(output)
    remove_junk(output)
    print(f"Built SkillHub zh-CN package: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
