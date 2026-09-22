---
name: card-creator
description: Create print-ready AirCard, NFC-card, bank-card, and transit-card faces quickly from short visual briefs. Always generate the complete artwork with ImageGen; repository logo PNGs are optional visual references, not compositing layers.
---

# Card Creator

A short brief such as “Magikarp × ICOCA, simple, ICOCA at lower right” is complete. Start creating;
do not turn it into logo research or a vector-graphics task.

## Required workflow

1. **Call ImageGen first.** Generate one flat landscape card face containing the subject, style, requested
   marks, and placement in a single image-generation pass. Never substitute SVG, HTML, Canvas, or code-drawn
   artwork for ImageGen.
2. A brand name, the word “Logo,” a placement such as “lower right,” or a request for trim/bleed downloads
   does **not** request a deterministic overlay. Do not inspect SVG files, a manifest, or compositing options.
3. For each requested mark, check the small [logo reference index](references/logo-reference-index.md). If a
   matching PNG exists, open only that PNG and pass it to ImageGen; do not redraw the mark from memory. If no
   reference exists, use model knowledge or a user attachment without starting web research. The PNG guides
   appearance; it is not pasted onto the finished card.
4. Do not add unrequested text, card numbers, chips, QR codes, barcodes, or contactless/NFC symbols. Avoid
   hands, devices, wallet UI, perspective, mockups, watermarks, shadows, and baked corner masks.
5. Check only that the requested subject and marks are present, visual hierarchy works, and important content
   is not accidentally cropped. Make at most one focused retry when the card is clearly unusable.
6. Run `scripts/prepare_card.py` only after generation to produce deterministic 300 DPI trim, bleed, and guide
   files. Use default `cover` for full-bleed art; use `--fit-mode contain` when edge content would otherwise be
   cut. The export script resizes and checks artwork; it does not add logos.

## Output

Return the trim file first, followed by bleed and guide files when useful. Mention briefly that generated
third-party marks are non-official stylized interpretations. Do not claim brand accuracy, authorization,
interoperability, sponsorship, or endorsement.

## Fixed boundaries

- Dimensions and coordinates live in [card rules](references/card-rules.md): `1011 × 638 px` trim and
  `1081 × 708 px` bleed.
- Private user images remain local unless the user explicitly asks to publish them.
- Do not create credentials or a design intended to pass as a functional payment, access, transit, or
  government-issued card.
- Contactless/payment indicators are opt-in only.

## Read references only when needed

- Read [prompt guide](references/prompt-guide.md) only when drafting or debugging a prompt.
- Read [logo reference index](references/logo-reference-index.md) when the request names a brand or transit mark.
- Read [reference-card remix](references/reference-remix.md) only for a variation based on an existing card,
  photo, or wallet screenshot.
