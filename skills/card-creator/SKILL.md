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
   When the input is an existing card face or a wallet screenshot, also read
   [reference-card remix](references/reference-remix.md). Isolate the card artwork, ignore the
   surrounding interface, and translate its design grammar into a distinct new composition.
2. Read [sticker catalog](references/sticker-catalog.md) when choosing among payment and transit
   sticker families. Then read [sticker manifest](assets/stickers/manifest.json) and use only entries whose status is `ready`.
   If a requested sticker is not ready, generate the background without it and report the missing asset.
   When the user asks to research a missing mark or supplies a card-face image, read
   [sticker research](references/sticker-research.md). Card-face extraction is a research fallback,
   never an automatic way to promote a mark to `ready`.
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
- A reference card is a source for palette relationships, spacing, line weight, motif density, and
  composition zones—not permission to copy its card number, wallet balance, issuer text, proprietary
  artwork, or unavailable logos.

## Files

- For exact dimensions and coordinate systems, read [card rules](references/card-rules.md).
- For prompt construction, read [prompt guide](references/prompt-guide.md).
- For a style variation based on an existing card face or wallet screenshot, read
  [reference-card remix](references/reference-remix.md).
- For sticker families and the research backlog, read [sticker catalog](references/sticker-catalog.md).
- For sourcing or extracting a missing mark from an official card face, read
  [sticker research](references/sticker-research.md).
- Sticker assets and provenance live under `assets/stickers/`.
- Run `python3 scripts/prepare_card.py --help` for deterministic export options.
