# Gallery image-generation prompts

These are the full prompts used for the named gallery images below, preserved for provenance. They are longer than the one-line prompts shown to visitors and are **not** instructions required to use the `card-creator` Skill. Both outputs were created with the built-in image-generation tool from the specified visual reference images. Generated brand marks are non-official artistic interpretations.

## 折面之城 × 汇丰

- Output: [`hsbc-geometric-hong-kong.png`](hsbc-geometric-hong-kong.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png`](../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png)

```text
Use case: stylized-concept. Asset type: finished downloadable bank-card face artwork for a noncommercial fan-art gallery. Use the attached HSBC logo image only as a visual identity reference, not as an exact composited asset. Create one complete flat edge-to-edge landscape card image, approximately 1.586:1 ratio. Art direction: exceptionally elegant HSBC-inspired red-and-ivory geometric modernism, with large folded-paper diamond and triangular facets radiating outward from a calm off-center focal point, a faint suggestion of Hong Kong architecture integrated in the geometry, disciplined crimson/ivory/ink-charcoal palette, subtle paper grain and embossed highlights, high-end editorial design, intentional negative space. Include a legible small HSBC hexagon-plus-'HSBC' logo as a tasteful style-matched mark in the upper right, rendered by the image model as part of the whole artwork. Do not add a lion, character, slogans, card number, payment network mark, chip, NFC/contactless icon, border, mockup, device, rounded corner mask, shadow, or extra text. Balance the brand mark with the artwork; do not crowd edges.
```

## 虹彩流线 × Apple Cash

- Output: [`apple-cash-iridescent-ribbon-opaque.png`](apple-cash-iridescent-ribbon-opaque.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/fintech/apple-cash.png`](../skills/card-creator/assets/logo-references/fintech/apple-cash.png)

```text
Use case: stylized-concept. Asset type: finished downloadable digital-cash card face artwork for a noncommercial fan-art gallery. Use the attached Apple Cash mark only as a visual identity reference, not as an exact composited asset. Create one complete flat edge-to-edge landscape card image, approximately 1.586:1 ratio. Art direction: refined Apple Cash-inspired minimalism on deep near-black obsidian, one broad luminous translucent ribbon sweeping diagonally across the card with soft pearlescent mint, silver, lavender and a restrained peach edge; optical-glass depth, extremely smooth gradients, subtle metallic light, spacious high-end composition, not gaudy or rainbow-striped. Include only a clean readable white Apple symbol and 'Cash' wordmark at lower right, style-matched and image-generated as part of the composition. No other letters, slogans, card number, chip, NFC/contactless icon, border, mockup, device, rounded corner mask, or shadow. Keep the wordmark comfortably inside the edge and preserve a strong card silhouette.
```

Opacity-repair edit prompt (input: first generated card image):

```text
Use case: precise-object-edit. Input image 1 is the EDIT TARGET. Repair only the unintended transparency in this finished Apple Cash card face. The near-black obsidian background must become completely opaque deep black across the entire flat rectangular canvas (full alpha 255 at every pixel), with no translucent pixels, alpha haze, pale smoky streaks or checkerboard when shown on a white webpage. Preserve exactly the current 1.586:1 landscape composition, the single smooth pearlescent mint/silver/lavender ribbon's silhouette and lighting, and the clean white Apple symbol plus 'Cash' lettering at lower right. No new design elements, no additional text, no chip, no border, no rounded corners, no mockup. This is a technical opacity correction, not a redesign.
```
