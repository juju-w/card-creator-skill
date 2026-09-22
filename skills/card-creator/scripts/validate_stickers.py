#!/usr/bin/env python3
"""Validate ready stickers and repository-backed reference assets."""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
from pathlib import Path

from PIL import Image


REQUIRED_READY_FIELDS = ("file", "vector_file", "source", "license", "usage")
NON_COMPOSITABLE_STATUSES = {"reference-only"}
REQUIRED_NON_READY_FIELDS = ("source", "license", "usage", "blocker", "resolution")


def open_raster(path: Path) -> Image.Image:
    if path.name.endswith(".base64.txt"):
        data = base64.b64decode(path.read_text(encoding="ascii").strip(), validate=True)
        return Image.open(io.BytesIO(data))
    return Image.open(path)


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
    status_counts: dict[str, int] = {}

    for item in manifest.get("items", []):
        sticker_id = item.get("id", "<missing-id>")
        status = item.get("status")
        status_counts[status] = status_counts.get(status, 0) + 1
        if sticker_id in seen_ids:
            errors.append(f"duplicate id: {sticker_id}")
        seen_ids.add(sticker_id)

        research_file = item.get("research_file")
        if research_file:
            if status != "reference-only":
                errors.append(
                    f"{sticker_id}: research_file must remain status=reference-only"
                )
            missing = [
                field
                for field in (
                    "source",
                    "source_asset",
                    "license",
                    "usage",
                    "sha256",
                    "transparency",
                )
                if not item.get(field)
            ]
            if missing:
                errors.append(f"{sticker_id}: missing research fields: {', '.join(missing)}")
            research_path = (manifest_path.parent / research_file).resolve()
            if not research_path.is_file():
                errors.append(f"{sticker_id}: missing research file: {research_path}")
            else:
                digest = hashlib.sha256(research_path.read_bytes()).hexdigest()
                if digest != item.get("sha256"):
                    errors.append(f"{sticker_id}: research SHA-256 mismatch")
                with Image.open(research_path) as image:
                    transparency = item.get("transparency")
                    if transparency not in {"transparent", "opaque"}:
                        errors.append(
                            f"{sticker_id}: invalid research transparency: {transparency}"
                        )
                    else:
                        alpha = image.convert("RGBA").getchannel("A")
                        alpha_min = alpha.getextrema()[0]
                        if transparency == "transparent" and alpha_min == 255:
                            errors.append(
                                f"{sticker_id}: research PNG transparency is fully opaque"
                            )
                        if transparency == "opaque" and alpha_min < 255:
                            errors.append(
                                f"{sticker_id}: research PNG is not fully opaque"
                            )

        if status in NON_COMPOSITABLE_STATUSES:
            missing = [
                field for field in REQUIRED_NON_READY_FIELDS if not item.get(field)
            ]
            if missing:
                errors.append(
                    f"{sticker_id}: missing non-ready fields: {', '.join(missing)}"
                )
            continue
        if status != "ready":
            errors.append(f"{sticker_id}: unsupported status: {status}")
            continue
        ready_count += 1

        missing = [field for field in REQUIRED_READY_FIELDS if not item.get(field)]
        if missing:
            errors.append(f"{sticker_id}: missing ready fields: {', '.join(missing)}")
            continue

        raster_path = (manifest_path.parent / item["file"]).resolve()
        svg_path = (manifest_path.parent / item["vector_file"]).resolve()
        if not raster_path.is_file():
            errors.append(f"{sticker_id}: missing raster asset: {raster_path}")
        if not svg_path.is_file():
            errors.append(f"{sticker_id}: missing SVG: {svg_path}")
        if svg_path.suffix.lower() != ".svg":
            errors.append(f"{sticker_id}: vector_file is not SVG: {svg_path}")

        if raster_path.is_file():
            try:
                image_source = open_raster(raster_path)
            except (OSError, ValueError) as exc:
                errors.append(f"{sticker_id}: invalid raster asset: {exc}")
                continue
            with image_source as image:
                if image.mode not in {"RGBA", "LA"}:
                    errors.append(f"{sticker_id}: PNG has no alpha channel: mode={image.mode}")
                else:
                    alpha = image.getchannel("A")
                    if alpha.getextrema()[0] == 255:
                        errors.append(f"{sticker_id}: PNG alpha channel is fully opaque")

    result = {"ready": ready_count, "statuses": status_counts, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
