"""Shared document assembly for maintainers; never shipped inside the Skill."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "card-creator"


def split_frontmatter(content: str) -> tuple[str, str]:
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        raise ValueError("expected YAML frontmatter")
    end = content.index("\n---\n", 4) + len("\n---\n")
    return content[:end].rstrip(), content[end:].strip()


def workflow() -> str:
    return split_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))[1]


def version(skill: Path = SKILL) -> str:
    """Read the single stable release version without a YAML dependency."""
    frontmatter, _ = split_frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))
    metadata = re.search(r"^metadata:\n((?:[ \t]+[^\n]*\n?)*)", frontmatter, re.M)
    match = re.search(r'^  version: "((?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*))"$', metadata[1], re.M) if metadata else None
    if not match:
        raise ValueError('SKILL.md must declare metadata.version as a quoted MAJOR.MINOR.PATCH')
    return match[1]


def card_rules() -> str:
    return (SKILL / "references/card-rules.md").read_text(encoding="utf-8").strip()
