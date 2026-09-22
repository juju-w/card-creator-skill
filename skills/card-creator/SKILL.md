---
name: card-creator
description: Generate print-ready AirCard and transit-card face images from a visual brief, enforcing the standard card ratio, bleed, safe area, local-only processing, exact logo overlays, and explicitly requested non-official logo reinterpretations. Use for new card faces or card-face variations.
---

# Card Creator

Support two clearly separated mark modes:

- **Exact mode (default):** AI generates the background and the compositor adds a `ready` manifest asset.
- **Stylized mode (explicit opt-in):** when the user asks for a mark to match the artwork, ImageGen may
  reinterpret a traceable or user-supplied logo reference as foil, monochrome, line art, ink, jade, or
  another requested material. Label it as non-official, retain the reference source and final prompt,
  and never add the generated mark to the exact `ready` sticker pack.

## Automatic layout direction

Run an art-direction pass automatically whenever a card contains two or more marks, or one mark shares
the face with a visually dense hero scene. The user does not need to request layout optimization.

- Judge marks by optical weight, not identical numeric dimensions. A symbol-only mark, a bilingual
  lockup, and a compact payment mark usually need different physical sizes to feel balanced.
- Establish a clear hierarchy between hero artwork, issuer mark, institution/transit mark, and payment
  mark. Marks should remain readable at card size without overpowering the main illustration.
- Give corner marks consistent optical breathing room from the physical trim. Do not push them against
  an edge merely because their bounding boxes technically fit.
- Treat the blue safe-area guide as advisory. Do not shrink logos or artwork just to fit it; large
  corner marks, repeated-icon patterns, intentional crops, and full-face marks are valid compositions.
- Choose each mark's conventional card-face variant from its category and official reference; do not
  apply one global compact/full rule. Variant choice and rendered size are independent.
- Prefer an unconstrained art-direction instruction over brittle pixel coordinates. Preserve the chosen
  hero composition and ask ImageGen to rebalance only the marks when the first layout feels crowded,
  tiny, edge-bound, or inconsistent.
- After any AI layout pass, verify every required word and character against the reference. Correct or
  reject hallucinated, traditional-vs-simplified, missing, or malformed lettering before delivery.

## Workflow

1. Read [card rules](references/card-rules.md) before generating.
   When the input is an existing card face or a wallet screenshot, also read
   [reference-card remix](references/reference-remix.md). Isolate the card artwork, ignore the
   surrounding interface, and translate its design grammar into a distinct new composition.
2. Read [sticker catalog](references/sticker-catalog.md) when choosing among payment and transit
   sticker families. Then read [sticker manifest](assets/stickers/manifest.json) and use only entries whose status is `ready`.
   Select the variant conventionally used on cards: payment networks often use a card-acceptance mark,
   while issuer banks and cultural institutions normally use their primary symbol-plus-name lockup.
   Do not force every brand into either a compact symbol or a full horizontal wordmark. User direction
   overrides convention.
   When the request names a bank issuer, also read
   [bank issuer reference catalog](references/bank-issuer-catalog.md) and keep the issuer mark distinct
   from its payment-network mark.
   If a requested sticker is not ready, generate the background without it and report the missing asset.
   This restriction applies to exact mode. An explicit stylized-mode request may instead use the
   traceable source only as an ImageGen reference and must disclose that the result is not an exact logo.
   Never add a contactless/NFC mark by default. Only consider one when the user explicitly requests
   it, and do not substitute a generic icon for an exact licensed card-side indicator.
   When the user asks to research a missing mark or supplies a card-face image, read
   [sticker research](references/sticker-research.md). Card-face extraction is a research fallback,
   never an automatic way to promote a mark to `ready`.
3. Default to one card face. Ask about front/back only when the request clearly requires a paired design.
4. In exact mode, use the built-in image generation tool to create only the background artwork. In
   explicit stylized mode, provide the mark as a labeled reference and ask ImageGen to integrate the
   requested material treatment into the flat artwork. In both modes, avoid a device, card mockup,
   watermark, border, or shadow. Treat the blue safe-area guide as advisory: ordinary small text and
   functional data stay clear of trim, while logos and artwork may fill corners, repeat, cross the guide,
   or run into bleed when that is the requested composition.
5. Copy the selected generation into the working project, then run `scripts/prepare_card.py` to crop it,
   create 300 DPI bleed and trim exports, and overlay approved transparent PNG stickers. Use original
   sticker colors by default. When the user explicitly asks for a style-matched mark, choose a
   geometry-locked render treatment: `foil-gold` for heritage/luxury artwork, `monochrome:#RRGGBB`
   for a single-color palette, or `outline:#RRGGBB` for line-art compositions. Use
   `--sticker-width ID=PIXELS` when the intended logo should dominate a corner or the card face.
6. When the composition meets the automatic-layout trigger above, perform one art-direction review and,
   if needed, one focused ImageGen layout pass that changes mark scale, spacing, and hierarchy without
   redesigning the approved hero artwork.
7. Inspect the final bleed, trim, and guide preview. Reject outputs with cropped focal subjects, distorted
   text, incorrect sticker placement, missing transparency, or accidental clipping. Do not reject an
   intentional oversized, cropped, repeated, corner-filling, or full-bleed mark for crossing the blue guide.
8. Return the final file paths, dimensions, sticker sources used, and the final background prompt.

## Non-negotiable rules

- Standard trim: `1011 × 638 px` at 300 DPI, representing `85.60 × 53.98 mm`.
- Full-bleed master: `1081 × 708 px`; the outer `35 px` on each side is bleed.
- The `59 px` blue safe-area inset is an advisory guide for conventional small text and functional data,
  not a hard limit on logos, artwork, or intentional full-bleed composition.
- Exact mode keeps sticker geometry, proportions, lettering, color, and transparency derived from the
  traceable source. Stylized mode may depart from those properties only after explicit user opt-in and
  must be described as a non-official artistic interpretation rather than a verified logo asset.
- `reference-only` and `blocked` manifest entries are terminal non-compositable records, not a
  queue of almost-ready stickers.
- Use the conventionally expected card-side variant. For example, use `unionpay-compact` for the usual
  UnionPay card-corner acceptance mark; keep a bank or institution's normal primary lockup unless the
  supplied reference or user request calls for symbol-only treatment.
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
- For mainland Chinese, Hong Kong, and international bank issuer marks, read
  [bank issuer reference catalog](references/bank-issuer-catalog.md).
- For sourcing or extracting a missing mark from an official card face, read
  [sticker research](references/sticker-research.md).
- Sticker assets and provenance live under `assets/stickers/`.
- Run `python3 scripts/prepare_card.py --help` for deterministic export options.
