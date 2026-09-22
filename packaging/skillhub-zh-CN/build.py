#!/usr/bin/env python3
"""Build the localized SkillHub/WorkBuddy distribution package."""

from __future__ import annotations

import argparse
import base64
import json
import shutil
from pathlib import Path


LOCALIZED_FILES = (
    Path("SKILL.md"),
    Path("agents/openai.yaml"),
    Path("references/card-rules.md"),
    Path("references/prompt-guide.md"),
    Path("references/reference-remix.md"),
    Path("references/sticker-catalog.md"),
    Path("references/sticker-research.md"),
)


def remove_junk(output: Path) -> None:
    for path in sorted(output.rglob("*"), reverse=True):
        if path.is_file() and (path.name == ".DS_Store" or path.suffix == ".pyc"):
            path.unlink()
        elif path.is_dir() and path.name == "__pycache__":
            shutil.rmtree(path)


def encode_binary_stickers(output: Path) -> None:
    manifest_path = output / "assets" / "stickers" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    for item in manifest["items"]:
        raster_file = item.get("file")
        if item.get("status") == "ready" and raster_file:
            raster_path = manifest_path.parent / raster_file
            encoded_relative = f"{raster_file}.base64.txt"
            encoded_path = manifest_path.parent / encoded_relative
            encoded_path.write_text(
                base64.b64encode(raster_path.read_bytes()).decode("ascii") + "\n",
                encoding="ascii",
            )
            raster_path.unlink()
            item["file"] = encoded_relative

        research_file = item.pop("research_file", None)
        if research_file:
            research_path = manifest_path.parent / research_file
            if research_path.exists():
                research_path.unlink()
            item["distribution_note"] = (
                "Binary research sample omitted from the SkillHub text-only package; "
                "see the canonical GitHub repository."
            )

    for path in (manifest_path.parent / "research").rglob("*.png"):
        path.unlink()
    for path in manifest_path.parent.rglob("*.png"):
        path.unlink()

    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


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

    encode_binary_stickers(output)
    remove_junk(output)
    print(f"Built SkillHub zh-CN package: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
