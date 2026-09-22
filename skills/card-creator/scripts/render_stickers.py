#!/usr/bin/env python3
"""Render ready SVG sticker assets to transparent PNG previews."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import cairosvg


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).parents[1] / "assets/stickers/manifest.json")
    parser.add_argument("--width", type=int, default=1200)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rendered = []
    for item in manifest["items"]:
        if item.get("status") != "ready" or not item.get("file"):
            continue
        source = (manifest_path.parent / item["file"]).resolve()
        if source.suffix.lower() != ".svg":
            continue
        target = source.with_suffix(".png")
        cairosvg.svg2png(url=str(source), write_to=str(target), output_width=args.width)
        rendered.append(str(target))
    print(json.dumps({"rendered": rendered}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
