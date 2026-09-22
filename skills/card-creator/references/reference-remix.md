# Reference-Card Remix

Use this mode when the user supplies an existing card face, product photo, or mobile-wallet screenshot
and asks for a new design inspired by it. Default to a recognizably new composition rather than a
pixel-close replica.

## Separate the card from the screenshot

Identify the card rectangle before analyzing style. Ignore the wallet balance, currency, phone-reader
guide, surrounding application interface, rounded mockup corners, drop shadows, reflections, and any
social-media watermark outside the card. If the photographed card is perspective-distorted, use it for
style analysis but do not copy its geometry.

## Extract design grammar

Summarize the reference in six fields before prompting:

1. **Palette relationship** — dominant field color, accent colors, contrast, and whether brand color is
   echoed in clothing, line work, or architecture.
2. **Composition zones** — quiet area, illustration area, lower band, and reserved logo corners.
3. **Line and shape language** — monoline, outlined character art, engraved line work, flat blocks,
   watercolor, or another visible system.
4. **Motif density** — sparse single character, repeated pattern, narrative scene, or architectural
   centerpiece.
5. **Mood and material** — playful, premium, civic, heritage, wintry, paper-like, metallic, and so on.
6. **Mark reference** — use a user-supplied or matching repository PNG as an ImageGen visual reference
   when helpful; otherwise use model knowledge.

Transfer these relationships, not exact artwork. Useful transformations include giving a character one
garment in the transit brand color, translating a heritage motif into new line art, or reusing the
reference's balance between a large quiet field and one small narrative scene.

## Do not carry over

- card numbers, masked digits, balances, currencies, names, chips, QR codes, barcodes, or functional
  acceptance claims;
- issuer, bank, museum, transit, payment, or contactless marks that the user did not request;
- proprietary illustrations copied from the source;
- wallet UI, device instructions, mockup shadows, rounded-corner masks, or screenshot watermarks.

Generate requested marks as part of the complete ImageGen composition. When a reference PNG exists, use it
to guide the mark rather than pasting it afterward. Label third-party marks as non-official stylized
interpretations.

## Direct web prompt template

```text
Use the card-face rules in https://github.com/juju-w/card-creator-skill and the reference image I uploaded above. The reference may be a mobile-wallet screenshot: analyze only the card artwork and ignore the balance, currency, reader instructions, interface, mockup corners, shadows, and watermark.

Do not copy the card literally. First extract its design grammar—palette relationships, whitespace, composition zones, line weight, motif density, and mood—then create a clearly new [target theme] variation using those relationships. Create a flat 1.58577:1 landscape card face targeting a 1011 × 638 px trim at 300 DPI; allow intentional full-bleed elements while avoiding accidental clipping.

Do not reproduce card numbers, masked digits, names, chips, balances, QR codes, barcodes, or unrequested marks. Generate [requested marks] inside the complete artwork; use any uploaded logo image only as an ImageGen visual reference. Output artwork only, with no hand, device, card mockup, perspective, rounded-corner mask, border, or shadow. Generate one complete preview and include the final prompt you used.
```
