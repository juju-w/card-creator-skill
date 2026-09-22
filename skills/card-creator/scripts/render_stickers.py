#!/usr/bin/env python3
"""Render ready SVG sticker assets to transparent PNG previews."""

from __future__ import annotations

import argparse
import base64
import io
import json
from pathlib import Path

import cairosvg
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).parents[1] / "assets/stickers/manifest.json")
    parser.add_argument("--width", type=int, default=1200)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rendered = []
    for item in manifest["items"]:
        vector_file = item.get("vector_file")
        raster_file = item.get("file")
        if item.get("status") != "ready" or not vector_file or not raster_file:
            continue
        source = (manifest_path.parent / vector_file).resolve()
        if source.suffix.lower() != ".svg":
            continue
        target = (manifest_path.parent / raster_file).resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        raster = cairosvg.svg2png(url=str(source), output_width=args.width)
        image = Image.open(io.BytesIO(raster)).convert("RGBA")
        alpha_bounds = image.getchannel("A").getbbox()
        if not alpha_bounds:
            raise SystemExit(f"Rendered sticker is fully transparent: {source}")
        cropped = image.crop(alpha_bounds)
        if target.name.endswith(".base64.txt"):
            buffer = io.BytesIO()
            cropped.save(buffer, format="PNG", optimize=True)
            target.write_text(
                base64.b64encode(buffer.getvalue()).decode("ascii") + "\n",
                encoding="ascii",
            )
        else:
            cropped.save(target, optimize=True)
        rendered.append(str(target))
    print(json.dumps({"rendered": rendered}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
