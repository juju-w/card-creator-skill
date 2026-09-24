"""Shared document assembly for maintainers; never shipped inside the Skill."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "card-creator"


def split_frontmatter(content: str) -> tuple[str, str]:
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        raise ValueError("expected YAML frontmatter")
    end = content.index("\n---\n", 4) + len("\n---\n")
    return content[:end].rstrip(), content[end:].strip()


def workflow() -> str:
    return split_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))[1]


def card_rules() -> str:
    return (SKILL / "references/card-rules.md").read_text(encoding="utf-8").strip()
