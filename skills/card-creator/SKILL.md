---
name: card-creator
description: Create print-ready AirCard, NFC-card, and transit-card faces quickly from short visual briefs. Use one-pass stylized marks by default; use verified transparent stickers only when the user explicitly asks for exact logos.
---

# Card Creator

Prefer the shortest route that satisfies the request. A brief such as “Magikarp × ICOCA, simple, ICOCA
at lower right” is enough; do not turn it into an asset-research project.

## Choose one route

### Fast artistic mode — default

Use for ordinary card requests and for style-matched marks such as “make the Octopus logo purple.”

- Generate the artwork and requested marks together in one ImageGen call.
- Use the user's reference or model knowledge. Do not browse, inspect the sticker manifest, extract Alpha,
  or compare logo variants.
- Treat generated payment, transit, bank, and city-card marks as one-off non-official stylized
  interpretations. Mention that briefly when delivering; never add them to the `ready` sticker pack.
- Make at most one focused retry when the composition is clearly unusable. A stylized mark differing from
  official geometry is not by itself a reason to research or restart.

### Exact-overlay mode — explicit opt-in

Use only when the user asks for an “exact,” “official,” “original,” or local transparent logo/sticker.

- Read [sticker catalog](references/sticker-catalog.md) and the
  [manifest](assets/stickers/manifest.json), then composite only `status: ready` assets.
- If the exact mark is absent, report it immediately. Search or extract a new asset only when the user
  explicitly asks to find, search, collect, or cut one out; then read
  [sticker research](references/sticker-research.md).
- Keep exact source geometry. A requested color/material treatment may use the compositor's
  `foil-gold`, `monochrome`, or `outline` treatment.

## Fast workflow

1. Default to one card face. Use the user's short brief directly; do not ask for details that can be
   inferred safely.
2. Generate flat landscape artwork containing the subject, style, requested marks, and placement. Avoid
   hands, devices, mockups, perspective, watermarks, functional card numbers, QR codes, and barcodes.
   Do not add a contactless/NFC symbol unless requested.
3. Check only the essentials: requested subject and marks are present, the hierarchy is readable, and
   important content is not accidentally cropped. Do not perform a mandatory second art-direction pass.
4. Run `scripts/prepare_card.py` for the deterministic 300 DPI exports. The default `cover` mode suits
   full-bleed art; use `--fit-mode contain` when embedded edge content would otherwise be cut.
5. Return the trim file path and a short disclosure for any generated third-party mark.

## Fixed boundaries

- Dimensions and coordinates live in [card rules](references/card-rules.md); the export script produces
  `1011 × 638 px` trim and `1081 × 708 px` bleed files.
- Private user images remain local unless the user explicitly asks to publish them.
- Do not claim brand accuracy, authorization, interoperability, sponsorship, or endorsement.
- Do not create credentials or a design intended to pass as a functional payment, access, transit, or
  government-issued card.

## Read references only when needed

- Read [prompt guide](references/prompt-guide.md) only when drafting or debugging a prompt.
- Read [reference-card remix](references/reference-remix.md) only for a variation based on an existing
  card, photo, or wallet screenshot.
- Read the sticker catalog and manifest only in exact-overlay mode.
- Read sticker research only after an explicit asset-search request.
