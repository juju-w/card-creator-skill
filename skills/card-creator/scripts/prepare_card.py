#!/usr/bin/env python3
"""Create deterministic 300 DPI card exports from a background and optional sticker PNGs."""

from __future__ import annotations

import argparse
import base64
import io
import json
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required. Install scripts/requirements.txt.") from exc


BLEED = 35
TRIM_SIZE = (1011, 638)
BLEED_SIZE = (1081, 708)
SAFE_INSET = 59
MARK_INSET = 35
STICKER_ANCHORS = {
    "top-left",
    "top-center",
    "top-right",
    "center-left",
    "center-center",
    "center-right",
    "bottom-left",
    "bottom-center",
    "bottom-right",
}
STICKER_STYLES = {"original", "foil-gold"}


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_sticker_spec(spec: str) -> tuple[str, str | None]:
    if "@" not in spec:
        return spec, None
    sticker_id, anchor = spec.rsplit("@", 1)
    if not sticker_id or anchor not in STICKER_ANCHORS:
        choices = ", ".join(sorted(STICKER_ANCHORS))
        raise SystemExit(f"Invalid sticker placement: {spec}; choose one of: {choices}")
    return sticker_id, anchor


def parse_sticker_styles(specs: Iterable[str]) -> dict[str, str]:
    styles: dict[str, str] = {}
    for spec in specs:
        if "=" not in spec:
            raise SystemExit(
                f"Invalid sticker style: {spec}; expected ID=original, "
                "ID=foil-gold, ID=monochrome:#RRGGBB, or ID=outline:#RRGGBB"
            )
        sticker_id, style = spec.split("=", 1)
        if not sticker_id or not is_valid_sticker_style(style):
            raise SystemExit(f"Invalid sticker style: {spec}")
        styles[sticker_id] = style
    return styles


def parse_sticker_widths(specs: Iterable[str]) -> dict[str, int]:
    widths: dict[str, int] = {}
    for spec in specs:
        if "=" not in spec:
            raise SystemExit(f"Invalid sticker width: {spec}; expected ID=PIXELS")
        sticker_id, value = spec.split("=", 1)
        try:
            width = int(value)
        except ValueError as exc:
            raise SystemExit(f"Invalid sticker width: {spec}; expected ID=PIXELS") from exc
        if not sticker_id or width < 1:
            raise SystemExit(f"Invalid sticker width: {spec}; width must be positive")
        widths[sticker_id] = width
    return widths


def is_valid_sticker_style(style: str) -> bool:
    if style in STICKER_STYLES:
        return True
    family, separator, color = style.partition(":")
    if family not in {"monochrome", "outline"} or separator != ":":
        return False
    return len(color) == 7 and color.startswith("#") and all(
        character in "0123456789abcdefABCDEF" for character in color[1:]
    )


def resolve_stickers(
    manifest_path: Path, specs: Iterable[str]
) -> list[tuple[dict, Path, str | None]]:
    manifest = load_manifest(manifest_path)
    index = {item["id"]: item for item in manifest["items"]}
    resolved = []
    for spec in specs:
        sticker_id, anchor = parse_sticker_spec(spec)
        item = index.get(sticker_id)
        if not item:
            raise SystemExit(f"Unknown sticker id: {sticker_id}")
        if item.get("status") != "ready" or not item.get("file"):
            raise SystemExit(f"Sticker is not approved/ready: {sticker_id}")
        file_path = (manifest_path.parent / item["file"]).resolve()
        if not file_path.exists():
            raise SystemExit(f"Sticker file is missing: {file_path}")
        resolved.append((item, file_path, anchor))
    return resolved


def open_sticker(path: Path) -> Image.Image:
    if path.name.endswith(".base64.txt"):
        try:
            data = base64.b64decode(path.read_text(encoding="ascii").strip(), validate=True)
        except (OSError, ValueError) as exc:
            raise SystemExit(f"Invalid base64 sticker asset: {path}") from exc
        return Image.open(io.BytesIO(data)).convert("RGBA")
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


def logo_ink_mask(sticker: Image.Image) -> Image.Image:
    """Return the exact non-white logo geometry as a grayscale mask."""
    red, green, blue, alpha = sticker.convert("RGBA").split()
    darkest_channel = ImageChops.darker(red, ImageChops.darker(green, blue))
    non_white = darkest_channel.point(lambda value: 0 if value >= 245 else 255)
    return ImageChops.multiply(alpha, non_white)


def stylize_sticker(sticker: Image.Image, style: str) -> Image.Image:
    """Apply a material treatment while keeping the source logo geometry fixed."""
    if style == "original":
        return sticker

    mask = logo_ink_mask(sticker)
    if style == "foil-gold":
        gradient = Image.linear_gradient("L").resize(sticker.size)
        smooth_gold = ImageOps.colorize(
            gradient,
            black=(139, 91, 25),
            white=(249, 226, 157),
        )
        grain = Image.effect_noise(sticker.size, 9).convert("L")
        grain_gold = ImageOps.colorize(
            grain,
            black=(158, 104, 29),
            white=(239, 205, 119),
        )
        result = Image.blend(smooth_gold, grain_gold, 0.18).convert("RGBA")
    else:
        family, _, color = style.partition(":")
        rgb = tuple(int(color[index : index + 2], 16) for index in (1, 3, 5))
        result = Image.new("RGBA", sticker.size, (*rgb, 255))
        if family == "outline":
            outside = mask.filter(ImageFilter.MaxFilter(5))
            inside = mask.filter(ImageFilter.MinFilter(5))
            mask = ImageChops.subtract(outside, inside)
    result.putalpha(mask)
    return result


def composite_sticker(
    canvas: Image.Image,
    sticker_path: Path,
    slot: int,
    anchor: str | None,
    style: str,
    width: int | None,
) -> None:
    sticker = open_sticker(sticker_path)
    if width is None:
        sticker.thumbnail((300, 140), Image.Resampling.LANCZOS)
    else:
        height = max(1, round(sticker.height * width / sticker.width))
        sticker = sticker.resize((width, height), Image.Resampling.LANCZOS)
    sticker = stylize_sticker(sticker, style)
    mark_right = BLEED + TRIM_SIZE[0] - MARK_INSET
    mark_left = BLEED + MARK_INSET
    mark_top = BLEED + MARK_INSET
    mark_bottom = BLEED + TRIM_SIZE[1] - MARK_INSET
    if anchor is None:
        x = mark_right - sticker.width
        y = mark_bottom - sticker.height - slot * (sticker.height + 18)
    else:
        vertical, horizontal = anchor.split("-")
        if horizontal == "left":
            x = mark_left
        elif horizontal == "right":
            x = mark_right - sticker.width
        else:
            x = mark_left + (mark_right - mark_left - sticker.width) // 2
        if vertical == "top":
            y = mark_top
        elif vertical == "bottom":
            y = mark_bottom - sticker.height
        else:
            y = mark_top + (mark_bottom - mark_top - sticker.height) // 2
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
    parser.add_argument(
        "--sticker",
        action="append",
        default=[],
        help="Approved sticker id, optionally ID@ANCHOR; repeatable",
    )
    parser.add_argument(
        "--sticker-style",
        action="append",
        default=[],
        help=(
            "Explicit render treatment: ID=original, ID=foil-gold, "
            "ID=monochrome:#RRGGBB, or ID=outline:#RRGGBB; repeatable"
        ),
    )
    parser.add_argument(
        "--sticker-width",
        action="append",
        default=[],
        help=(
            "Explicit rendered width in pixels, for example ID=420. This may cross the advisory "
            "safe-area guide when the composition intentionally uses an oversized or full-corner mark."
        ),
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    background = cover(Image.open(args.input), BLEED_SIZE).convert("RGBA")
    used = resolve_stickers(args.manifest.resolve(), args.sticker)
    styles = parse_sticker_styles(args.sticker_style)
    widths = parse_sticker_widths(args.sticker_width)
    requested_ids = {item["id"] for item, _, _ in used}
    unknown_style_ids = set(styles) - requested_ids
    if unknown_style_ids:
        raise SystemExit(
            "Sticker style supplied for unused id(s): "
            + ", ".join(sorted(unknown_style_ids))
        )
    unknown_width_ids = set(widths) - requested_ids
    if unknown_width_ids:
        raise SystemExit(
            "Sticker width supplied for unused id(s): "
            + ", ".join(sorted(unknown_width_ids))
        )
    for slot, (item, sticker_path, anchor) in enumerate(used):
        style = styles.get(item["id"], "original")
        composite_sticker(
            background,
            sticker_path,
            slot,
            anchor,
            style,
            widths.get(item["id"]),
        )

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
        "stickers": [item["id"] for item, _, _ in used],
        "sticker_placements": [
            {
                "id": item["id"],
                "anchor": anchor or "bottom-right-stack",
                "style": styles.get(item["id"], "original"),
                "width": widths.get(item["id"], "default"),
            }
            for item, _, anchor in used
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
