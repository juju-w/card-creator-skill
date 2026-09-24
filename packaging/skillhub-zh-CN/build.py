#!/usr/bin/env python3
"""Build the localized SkillHub/WorkBuddy distribution package."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from skill_text import card_rules, split_frontmatter, workflow


def remove_junk(output: Path) -> None:
    for path in sorted(output.rglob("*"), reverse=True):
        if path.is_file() and (path.name == ".DS_Store" or path.suffix == ".pyc"):
            path.unlink()
        elif path.is_dir() and path.name == "__pycache__":
            shutil.rmtree(path)


def omit_binary_references(output: Path, revision: str) -> None:
    """Keep a direct remote picture index in the text-only distribution."""
    references = output / "assets" / "logo-references"
    if references.exists():
        shutil.rmtree(references)
    logo_index = output / "references" / "logo-reference-index.md"
    if logo_index.exists():
        text = logo_index.read_text(encoding="utf-8")
        text = text.replace(
            "../assets/logo-references/",
            f"https://raw.githubusercontent.com/juju-w/card-creator-skill/{revision}/skills/card-creator/assets/logo-references/",
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

    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True,
    ).strip()
    frontmatter, intro = split_frontmatter((packaging_dir / "entry.md").read_text(encoding="utf-8"))
    rules_digest = hashlib.sha256((workflow() + "\n" + card_rules()).encode()).hexdigest()
    shared = workflow().replace("# Card Creator\n", "## Shared workflow\n", 1)
    (output / "SKILL.md").write_text(
        f"{frontmatter}\n\n<!-- Source revision: {revision}; rules sha256: {rules_digest} -->\n\n{intro}\n\n{shared}\n",
        encoding="utf-8",
    )
    shutil.copy2(packaging_dir / "agents/openai.yaml", output / "agents/openai.yaml")
    omit_binary_references(output, revision)
    remove_junk(output)
    print(f"Built SkillHub zh-CN package: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
