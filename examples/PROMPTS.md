# Gallery image-generation prompts

These are the full prompts used for the named gallery images below, preserved for provenance. They are longer than the one-line prompts shown to visitors and are **not** instructions required to use the `card-creator` Skill. The outputs were created with the built-in image-generation tool from the specified visual reference images. Generated brand marks are non-official artistic interpretations.

## 折面之城 × 汇丰

- Output: [`hsbc-geometric-hong-kong.png`](hsbc-geometric-hong-kong.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png`](../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png)

```text
Use case: stylized-concept. Asset type: finished downloadable bank-card face artwork for a noncommercial fan-art gallery. Use the attached HSBC logo image only as a visual identity reference, not as an exact composited asset. Create one complete flat edge-to-edge landscape card image, approximately 1.586:1 ratio. Art direction: exceptionally elegant HSBC-inspired red-and-ivory geometric modernism, with large folded-paper diamond and triangular facets radiating outward from a calm off-center focal point, a faint suggestion of Hong Kong architecture integrated in the geometry, disciplined crimson/ivory/ink-charcoal palette, subtle paper grain and embossed highlights, high-end editorial design, intentional negative space. Include a legible small HSBC hexagon-plus-'HSBC' logo as a tasteful style-matched mark in the upper right, rendered by the image model as part of the whole artwork. Do not add a lion, character, slogans, card number, payment network mark, chip, NFC/contactless icon, border, mockup, device, rounded corner mask, shadow, or extra text. Balance the brand mark with the artwork; do not crowd edges.
```

The red-and-ivory image above is retained for provenance but no longer featured in the gallery.

## 蓝晶狮影 × 汇丰（新版）

- Output: [`hsbc-crystal-lion.png`](hsbc-crystal-lion.png)
- Visual references: [`../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png`](../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png) for the mark; the user-supplied `IMG_9001.JPG` only for the low-poly blue visual rhythm and logo hierarchy. The user image itself is not published here.

```text
Use case: stylized-concept. Asset type: a finished downloadable, nonofficial HSBC-inspired bank-card face for a free fan-art gallery. Input image 1 is only the HSBC logo identity reference. Input image 2 is only a visual reference for the sophisticated deep-blue low-poly facet rhythm and clear logo hierarchy; do NOT copy its mascot, words, watermark, payment circles, or screenshot edges. Make an entirely NEW, elegant card artwork. Flat full-bleed opaque rectangular landscape canvas, about 1.586:1, no rounded-corner mask or mockup. Art direction: midnight teal and mineral-blue crystalline facets radiate outward from a single sculptural guardian-lion silhouette at left-center, as if carved from blue glass and paper; the lion is dignified and abstract, not a cartoon face. Dynamic geometry is integrated into its mane and the background, with a quiet dark-blue area on the right for visual breathing room. Restrained pearlescent highlights, subtle print texture, refined bank-card finish; tiny touches of HSBC red ONLY in the upper-right logo. Put one clean recognizable small red-and-white hexagon plus white 'HSBC' wordmark at upper right, comfortably inset, based on image 1. Image model paints the complete artwork, including the brand mark. No giant second hexagon, no Hong Kong skyline, no busy red/white triangles, no lion photorealism, no bank-card number, chip, NFC icon, payment network mark, 'world debit', any other words, border, shadow, device, or watermark. Premium, restrained, memorable.
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

## 上海装饰艺术 × 银联（新版）

- Output: [`shanghai-art-deco-unionpay-v2.png`](shanghai-art-deco-unionpay-v2.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/payment/unionpay-compact.png`](../skills/card-creator/assets/logo-references/payment/unionpay-compact.png)
- The previous gallery image is retained as [`shanghai-art-deco-unionpay.png`](shanghai-art-deco-unionpay.png), but is no longer featured.

```text
Use case: stylized-concept. Asset type: finished card-face artwork for a free noncommercial gallery. Input image 1 is a visual identity reference for the compact UnionPay 银联 mark, not an exact compositing asset. Make a completely NEW Shanghai city card face with much stronger art direction and calm hierarchy than a busy skyline poster. Flat opaque edge-to-edge landscape artwork, approx 1.586:1, no rounded-corner mask. A high-end 1930s Shanghai Art Deco interpretation: one confident stepped fan geometry frames a simplified Bund clock-tower silhouette and a single elegant line of river reflections; the distant Oriental Pearl appears only as a subtle small counterpoint, not a forest of towers. Deep ink-jade and muted malachite, warm ivory, very restrained antique-gold foil lines; tactile silkscreen paper and quiet negative space. One medium-sized compact UnionPay 银联 mark, style-matched in warm ivory and muted gold, clearly recognizable and visually balanced, placed comfortably inside a corner. Image model paints the whole image including the mark. No huge moon, no star field, no multiple fan decorations, no fake readable building signs. No other text, card number, chip, NFC/contactless icon, QR, border, shadow, device, or mockup. Make the image fully opaque, not transparent.
```

## 广州极简线条 × 岭南通 / 交通联合（新版）

- Output: [`guangzhou-minimal-lingnantong-tunion-v2.png`](guangzhou-minimal-lingnantong-tunion-v2.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/lingnan-pass-reference.png`](../skills/card-creator/assets/logo-references/cities/lingnan-pass-reference.png); the 交通联合 mark was painted from model knowledge, not a local logo asset.
- The previous gallery image is retained as [`guangzhou-minimal-lingnantong-tunion.png`](guangzhou-minimal-lingnantong-tunion.png), but is no longer featured.

```text
Use case: stylized-concept. Asset type: finished card-face artwork for a free noncommercial gallery. Input image 1 is a visual identity reference for the 岭南通 (Lingnan Pass) mark only, not an exact compositing asset or a card layout reference. Create a completely NEW Guangzhou city transit card, radically different from a dense panoramic skyline card. Flat opaque edge-to-edge landscape artwork, approximately 1.586:1, no rounded corner mask, no device or mockup. Design language: premium minimalist architectural linework, warm ivory paper, deep petrol-blue ink and one muted cinnabar-red accent. Let one elegant oversized continuous-line Canton Tower rise asymmetrically from the LEFT third; express the Pearl River as only three sweeping thin parallel curves across the lower half; place a single restrained kapok flower motif near the river. Leave substantial calm negative space, with a strong, professional editorial composition. Integrate TWO medium, comfortably inset, recognizable transit marks as part of the painted design: the 岭南通 mark based on the attached reference and a compact familiar red-and-blue China T-Union 交通联合 mark. Keep them crisp, proportionate, and harmonized with the line-art design, yet distinct. The image model paints the complete design; do not paste or composite. Do not include a row of buildings, ornate skyline, sun disc, chip, NFC/contactless indicator, card number, barcode, QR code, decorative border, shadow, fake signs, or any other text. Fully opaque, clean high-end card face.
```

Opacity-repair edit prompt (input: first generated card image):

```text
Edit the supplied Guangzhou transit card face, preserving its composition, linework, Canton Tower, kapok flower, river curves, and BOTH logos. Crucial correction: fill the ENTIRE current transparent background, from edge to edge, with SOLID OPAQUE warm ivory paper (#F5F1E9). The output must have no transparent pixels anywhere. Make the dark petrol linework and both logo texts fully legible on this light background, with natural antialiasing. Keep the overall restrained editorial minimalism. Do not add objects, card mockup, rounded corners, shadow, border, extra text, NFC icon, card number, or chip. Final raster should be one complete flat rectangular card face, opaque at every pixel.
```
