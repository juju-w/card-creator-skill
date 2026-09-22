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
| Advisory safe area | 893 × 520 px | Conservative guide for ordinary small text and functional data; not a hard composition boundary |

Coordinate system for the full-bleed master:

- Trim bounds: x 35–1045, y 35–672.
- Advisory safe bounds: x 94–986, y 94–613. The blue line in the guide preview visualizes this
  conservative zone; it does not constrain artwork or logo scale.
- Sticker positions are expressed relative to the trim bounds, not the full-bleed canvas.
- `prepare_card.py --sticker ID@ANCHOR` supports a complete 3 × 3 anchor grid: `top-left`,
  `top-center`, `top-right`, `center-left`, `center-center`, `center-right`, `bottom-left`,
  `bottom-center`, and `bottom-right`. Omitting `@ANCHOR` preserves the original bottom-right
  stacking behavior. The center column is useful for deliberate multi-logo collage layouts.
- `--sticker-style ID=foil-gold`, `ID=monochrome:#RRGGBB`, and `ID=outline:#RRGGBB` apply a
  material treatment inside the exact source-logo geometry. Omit the option for original colors.
- `--sticker-width ID=420` sets an explicit rendered width. Use it for intentionally oversized,
  corner-filling, repeated, or near-full-card marks instead of shrinking every mark into the blue guide.

## Composition

- Background artwork must extend through the full bleed.
- The safe area is advisory, not a rejection boundary. Logos, mascots, patterns, architecture, and other
  artwork may cross it, fill a corner, repeat across the face, or intentionally run through the trim into
  bleed when that is the requested composition.
- Keep small text, card numbers, and other conventional functional data away from trim by default.
  For logos and focal art, reject only accidental clipping; deliberate cropping or full-bleed use is valid.
- In exact compositor mode, a requested surface treatment must preserve the source geometry and may
  not repair or invent a mark. In explicit stylized mode, ImageGen may reinterpret the reference's
  geometry, lettering treatment, color, and material as a disclosed non-official artwork.
- Do not rasterize rounded corners. Printers and card manufacturers apply the physical corner cut.
- Text generated inside background artwork is discouraged. Add important text later as a deterministic
  editable layer when the caller provides a supported compositor.

## Export acceptance

- PNG in sRGB.
- No alpha is required for the background; transparent stickers retain alpha before compositing.
- No metadata containing private source paths or user identifiers.
- Inspect the guide preview before delivering the clean files.
