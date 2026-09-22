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
- `prepare_card.py --fit-mode contain --contain-inset 20` preserves an edge-bound source composition
  inside trim and extends a sampled paper/background color into bleed. Use it when cover-cropping would
  cut embedded marks or focal artwork; the default `cover` mode remains appropriate for true full-bleed
  backgrounds.

## Composition

- Background artwork must extend through the full bleed.
- The safe area is advisory, not a rejection boundary. Logos, mascots, patterns, architecture, and other
  artwork may cross it, fill a corner, repeat across the face, or intentionally run through the trim into
  bleed when that is the requested composition.
- Keep small text, card numbers, and other conventional functional data away from trim by default.
  For logos and focal art, reject only accidental clipping; deliberate cropping or full-bleed use is valid.
- ImageGen may reinterpret a reference mark's geometry, lettering treatment, color, and material as a
  disclosed non-official artwork. PNG logo files are references, not deterministic overlays.
- Do not rasterize rounded corners. Printers and card manufacturers apply the physical corner cut.
- Avoid unnecessary generated text. Short text that is integral to a requested mark may remain part of the
  generated artwork.

## Export acceptance

- PNG in sRGB.
- No alpha is required for the generated card artwork.
- No metadata containing private source paths or user identifiers.
- Inspect the guide preview before delivering the clean files.
