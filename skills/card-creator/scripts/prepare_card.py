#!/usr/bin/env python3
"""Create deterministic 300 DPI trim, bleed, and guide exports from generated card artwork."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required. Install scripts/requirements.txt.") from exc


BLEED = 35
TRIM_SIZE = (1011, 638)
BLEED_SIZE = (1081, 708)
SAFE_INSET = 59


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(
        image.convert("RGB"),
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )


def estimate_border_fill(image: Image.Image) -> tuple[int, int, int]:
    """Estimate a light neutral fill from the source border for contain-mode padding."""
    rgb = image.convert("RGB")
    width, height = rgb.size
    x_step = max(1, width // 32)
    y_step = max(1, height // 32)
    samples = [
        rgb.getpixel((x, y))
        for x in range(0, width, x_step)
        for y in (0, height - 1)
    ]
    samples.extend(
        rgb.getpixel((x, y))
        for y in range(0, height, y_step)
        for x in (0, width - 1)
    )
    light = [pixel for pixel in samples if sum(pixel) >= 630]
    selected = light or samples
    return tuple(
        sorted(pixel[channel] for pixel in selected)[len(selected) // 2]
        for channel in range(3)
    )


def contain_within_trim(image: Image.Image, inset: int) -> Image.Image:
    """Preserve the full source inside trim and extend the surrounding paper into bleed."""
    if inset < 0 or inset * 2 >= min(TRIM_SIZE):
        raise SystemExit(
            "--contain-inset must be non-negative and smaller than half the trim size"
        )
    source = image.convert("RGB")
    available = (TRIM_SIZE[0] - inset * 2, TRIM_SIZE[1] - inset * 2)
    contained = ImageOps.contain(source, available, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", BLEED_SIZE, estimate_border_fill(source))
    x = BLEED + (TRIM_SIZE[0] - contained.width) // 2
    y = BLEED + (TRIM_SIZE[1] - contained.height) // 2
    canvas.paste(contained, (x, y))
    return canvas


def guide_preview(clean: Image.Image) -> Image.Image:
    preview = clean.copy()
    draw = ImageDraw.Draw(preview, "RGBA")
    draw.rectangle(
        (BLEED, BLEED, BLEED + TRIM_SIZE[0] - 1, BLEED + TRIM_SIZE[1] - 1),
        outline=(230, 75, 65, 230),
        width=3,
    )
    safe = (
        BLEED + SAFE_INSET,
        BLEED + SAFE_INSET,
        BLEED + TRIM_SIZE[0] - SAFE_INSET,
        BLEED + TRIM_SIZE[1] - SAFE_INSET,
    )
    draw.rectangle(safe, outline=(25, 145, 190, 230), width=3)
    return preview


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Generated card artwork")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--name", default="card-face", help="Output filename stem")
    parser.add_argument(
        "--fit-mode",
        choices=("cover", "contain"),
        default="cover",
        help="cover fills bleed by cropping; contain preserves the whole source inside trim",
    )
    parser.add_argument(
        "--contain-inset",
        type=int,
        default=0,
        help="Extra trim inset in pixels for contain mode; useful for edge-bound content",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    source = Image.open(args.input)
    if args.fit_mode == "contain":
        clean = contain_within_trim(source, args.contain_inset)
    else:
        if args.contain_inset:
            raise SystemExit("--contain-inset requires --fit-mode contain")
        clean = cover(source, BLEED_SIZE)

    bleed_path = args.output_dir / f"{args.name}-bleed.png"
    trim_path = args.output_dir / f"{args.name}-trim.png"
    guide_path = args.output_dir / f"{args.name}-guides.png"

    clean.save(bleed_path, dpi=(300, 300), optimize=True)
    clean.crop(
        (BLEED, BLEED, BLEED + TRIM_SIZE[0], BLEED + TRIM_SIZE[1])
    ).save(trim_path, dpi=(300, 300), optimize=True)
    guide_preview(clean).save(guide_path, dpi=(300, 300), optimize=True)

    print(
        json.dumps(
            {
                "bleed": str(bleed_path.resolve()),
                "trim": str(trim_path.resolve()),
                "guides": str(guide_path.resolve()),
                "dimensions": {"bleed": BLEED_SIZE, "trim": TRIM_SIZE},
                "fit": {"mode": args.fit_mode, "contain_inset": args.contain_inset},
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
