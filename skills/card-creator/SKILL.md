---
name: card-creator
description: Generate print-ready AirCard and transit-card face images from a visual brief, enforcing the standard card ratio, bleed, safe area, local-only processing, and an approved transparent sticker pack. Use for new card faces or card-face variations; do not use to invent or redraw protected brand logos.
---

# Card Creator

Create the card artwork as two layers: an AI-generated background and deterministic sticker overlays.
Brand or transit marks must come from the approved asset manifest; never ask ImageGen to reproduce,
approximate, stylize, or repair a logo.

## Workflow

1. Read [card rules](references/card-rules.md) before generating.
2. Read [sticker manifest](assets/stickers/manifest.json) and use only entries whose status is `ready`.
   If a requested sticker is not ready, generate the background without it and report the missing asset.
3. Default to one card face. Ask about front/back only when the request clearly requires a paired design.
4. Use the built-in image generation tool to create only the background artwork. Prompt for a flat,
   straight-on landscape composition without a device, card mockup, logo, watermark, border, or shadow.
   Keep important subjects out of the safe-area edges and reserve negative space for requested stickers.
5. Copy the selected generation into the working project, then run `scripts/prepare_card.py` to crop it,
   create 300 DPI bleed and trim exports, and overlay approved transparent PNG stickers.
6. Inspect the final bleed, trim, and guide preview. Reject outputs with cropped focal subjects, distorted
   text, incorrect sticker placement, missing transparency, or content outside the safe area.
7. Return the final file paths, dimensions, sticker sources used, and the final background prompt.

## Non-negotiable rules

- Standard trim: `1011 × 638 px` at 300 DPI, representing `85.60 × 53.98 mm`.
- Full-bleed master: `1081 × 708 px`; the outer `35 px` on each side is bleed.
- Keep essential content at least `59 px` inside the trim edge.
- Treat stickers as immutable transparent overlays. Preserve their proportions, colors, and transparency.
- Private user images stay local unless the user explicitly asks to publish or upload them.
- Do not claim that included brand names imply sponsorship or official cooperation.
- Do not generate card numbers, payment credentials, QR codes, barcodes, or designs intended to pass as
  a functional payment, access, or government-issued card.

## Files

- For exact dimensions and coordinate systems, read [card rules](references/card-rules.md).
- For prompt construction, read [prompt guide](references/prompt-guide.md).
- Sticker assets and provenance live under `assets/stickers/`.
- Run `python3 scripts/prepare_card.py --help` for deterministic export options.
