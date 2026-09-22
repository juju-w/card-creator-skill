# Card Rules

## Physical standard

Use the ISO/IEC 7810 ID-1 footprint commonly used by transit and payment cards:

- Trim size: 85.60 × 53.98 mm.
- Aspect ratio: 1.58577:1.
- Corner radius: manufacturing concern; do not bake opaque corner masks into the artwork.

## 300 DPI raster outputs

| Output | Size | Purpose |
|---|---:|---|
| Trim | 1011 × 638 px | User preview and ordinary download |
| Full bleed | 1081 × 708 px | Print master with 35 px bleed on every edge |
| Safe area | 893 × 520 px | Essential content region inside the trim |

Coordinate system for the full-bleed master:

- Trim bounds: x 35–1045, y 35–672.
- Safe bounds: x 94–986, y 94–613.
- Sticker positions are expressed relative to the trim bounds, not the full-bleed canvas.

## Composition

- Background artwork must extend through the full bleed.
- Do not place faces, titles, or important landmarks in the bleed.
- Keep brand stickers entirely inside the safe area unless a verified production template says otherwise.
- Do not rasterize rounded corners. Printers and card manufacturers apply the physical corner cut.
- Text generated inside background artwork is discouraged. Add important text later as a deterministic
  editable layer when the caller provides a supported compositor.

## Export acceptance

- PNG in sRGB.
- No alpha is required for the background; transparent stickers retain alpha before compositing.
- No metadata containing private source paths or user identifiers.
- Inspect the guide preview before delivering the clean files.

