# Background Prompt Guide

The generation prompt describes artwork, not the physical card product.

Include:

- `flat edge-to-edge landscape artwork, 1.58577:1 composition`
- subject, visual style, palette, mood, and focal placement
- `important content centered within a generous safe area`
- the desired empty region for later sticker placement
- `no logo, no brand mark, no card number, no QR code, no barcode, no watermark`
- `no card mockup, no hand, no perspective, no rounded-corner mask, no shadow`

When the user requests a known sticker, describe only its reserved location in the ImageGen prompt. Add
the actual sticker afterward with `prepare_card.py`.

When the user supplies an existing card face or a mobile-wallet screenshot and asks for a style
variation, read [reference-card remix](reference-remix.md) before writing the prompt.

Example:

```text
Create flat edge-to-edge landscape artwork in a 1.58577:1 composition. A quiet ink-and-gouache city
morning with a train crossing the lower third, warm paper texture, pine green and vermilion palette.
Keep the central title area calm and all important subjects inside a generous safe area. Leave clean
negative space in the upper-right for a later transparent transit sticker. No logo, brand mark, card
number, QR code, barcode, watermark, card mockup, hand, perspective, border, rounded-corner mask, or
shadow.
```
