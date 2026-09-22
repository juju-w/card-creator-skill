#!/usr/bin/env python3
"""Validate ready sticker provenance, file presence, and PNG transparency."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


REQUIRED_READY_FIELDS = ("file", "vector_file", "source", "license", "usage")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path(__file__).parents[1] / "assets/stickers/manifest.json",
    )
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    seen_ids: set[str] = set()
    ready_count = 0

    for item in manifest.get("items", []):
        sticker_id = item.get("id", "<missing-id>")
        if sticker_id in seen_ids:
            errors.append(f"duplicate id: {sticker_id}")
        seen_ids.add(sticker_id)

        if item.get("status") != "ready":
            continue
        ready_count += 1

        missing = [field for field in REQUIRED_READY_FIELDS if not item.get(field)]
        if missing:
            errors.append(f"{sticker_id}: missing ready fields: {', '.join(missing)}")
            continue

        png_path = (manifest_path.parent / item["file"]).resolve()
        svg_path = (manifest_path.parent / item["vector_file"]).resolve()
        if not png_path.is_file():
            errors.append(f"{sticker_id}: missing PNG: {png_path}")
        if not svg_path.is_file():
            errors.append(f"{sticker_id}: missing SVG: {svg_path}")
        if svg_path.suffix.lower() != ".svg":
            errors.append(f"{sticker_id}: vector_file is not SVG: {svg_path}")

        if png_path.is_file():
            with Image.open(png_path) as image:
                if image.mode not in {"RGBA", "LA"}:
                    errors.append(f"{sticker_id}: PNG has no alpha channel: mode={image.mode}")
                else:
                    alpha = image.getchannel("A")
                    if alpha.getextrema()[0] == 255:
                        errors.append(f"{sticker_id}: PNG alpha channel is fully opaque")

    result = {"ready": ready_count, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
