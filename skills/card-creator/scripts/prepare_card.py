#!/usr/bin/env python3
"""Create deterministic 300 DPI card exports from a background and optional sticker PNGs."""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required. Install scripts/requirements.txt.") from exc


BLEED = 35
TRIM_SIZE = (1011, 638)
BLEED_SIZE = (1081, 708)
SAFE_INSET = 59


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_stickers(manifest_path: Path, ids: Iterable[str]) -> list[tuple[dict, Path]]:
    manifest = load_manifest(manifest_path)
    index = {item["id"]: item for item in manifest["items"]}
    resolved = []
    for sticker_id in ids:
        item = index.get(sticker_id)
        if not item:
            raise SystemExit(f"Unknown sticker id: {sticker_id}")
        if item.get("status") != "ready" or not item.get("file"):
            raise SystemExit(f"Sticker is not approved/ready: {sticker_id}")
        file_path = (manifest_path.parent / item["file"]).resolve()
        if not file_path.exists():
            raise SystemExit(f"Sticker file is missing: {file_path}")
        resolved.append((item, file_path))
    return resolved


def open_sticker(path: Path) -> Image.Image:
    if path.suffix.lower() == ".svg":
        try:
            import cairosvg
        except (ImportError, OSError) as exc:  # pragma: no cover
            raise SystemExit(
                "CairoSVG and the native Cairo library are required to composite SVG stickers. "
                "Use the ready PNG derivative or install Cairo first."
            ) from exc
        raster = cairosvg.svg2png(url=str(path), output_width=1200)
        return Image.open(io.BytesIO(raster)).convert("RGBA")
    return Image.open(path).convert("RGBA")


def composite_sticker(canvas: Image.Image, sticker_path: Path, slot: int) -> None:
    sticker = open_sticker(sticker_path)
    max_width = 210
    max_height = 92
    sticker.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    safe_right = BLEED + TRIM_SIZE[0] - SAFE_INSET
    safe_bottom = BLEED + TRIM_SIZE[1] - SAFE_INSET
    x = safe_right - sticker.width
    y = safe_bottom - sticker.height - slot * (sticker.height + 18)
    canvas.alpha_composite(sticker, (x, y))


def guide_preview(clean: Image.Image) -> Image.Image:
    preview = clean.copy()
    draw = ImageDraw.Draw(preview, "RGBA")
    draw.rectangle((BLEED, BLEED, BLEED + TRIM_SIZE[0] - 1, BLEED + TRIM_SIZE[1] - 1), outline=(230, 75, 65, 230), width=3)
    safe = (BLEED + SAFE_INSET, BLEED + SAFE_INSET, BLEED + TRIM_SIZE[0] - SAFE_INSET, BLEED + TRIM_SIZE[1] - SAFE_INSET)
    draw.rectangle(safe, outline=(25, 145, 190, 230), width=3)
    return preview


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Generated background image")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--name", default="card-face", help="Output filename stem")
    parser.add_argument("--manifest", type=Path, default=Path(__file__).parents[1] / "assets/stickers/manifest.json")
    parser.add_argument("--sticker", action="append", default=[], help="Approved sticker id; repeatable")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    background = cover(Image.open(args.input), BLEED_SIZE).convert("RGBA")
    used = resolve_stickers(args.manifest.resolve(), args.sticker)
    for slot, (_, sticker_path) in enumerate(used):
        composite_sticker(background, sticker_path, slot)

    bleed_path = args.output_dir / f"{args.name}-bleed.png"
    trim_path = args.output_dir / f"{args.name}-trim.png"
    guide_path = args.output_dir / f"{args.name}-guides.png"

    clean = background.convert("RGB")
    clean.save(bleed_path, dpi=(300, 300), optimize=True)
    clean.crop((BLEED, BLEED, BLEED + TRIM_SIZE[0], BLEED + TRIM_SIZE[1])).save(trim_path, dpi=(300, 300), optimize=True)
    guide_preview(clean).save(guide_path, dpi=(300, 300), optimize=True)

    print(json.dumps({
        "bleed": str(bleed_path.resolve()),
        "trim": str(trim_path.resolve()),
        "guides": str(guide_path.resolve()),
        "dimensions": {"bleed": BLEED_SIZE, "trim": TRIM_SIZE},
        "stickers": [item["id"] for item, _ in used],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
