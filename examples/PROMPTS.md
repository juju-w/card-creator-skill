# Gallery image-generation prompts

These are the full prompts used for the named gallery images below, preserved for provenance. They are longer than the one-line prompts shown to visitors and are **not** instructions required to use the `card-creator` Skill. The outputs were created with the built-in image-generation tool from the specified visual reference images. Generated brand marks are non-official artistic interpretations.

## 二次元系列（2026-09-23 新增）

以下均为非官方 AI 二创，图片生成模型绘制整张卡面，标志未以脚本贴图。最终八张均为不含 alpha 通道的完整矩形 PNG。试稿中的写实五条悟、利姆露史莱姆和佐佐木／田山双人版未入库；《胆大党》的第一稿有手部错误，画廊使用的是修正版。

### 祢豆子 × ICOCA

- Output: [`anime-nezuko-icoca.png`](anime-nezuko-icoca.png)
- Character reference: model knowledge; [Demon Slayer official character page](https://kimetsu.com/anime/yukakuhen/character/?id=02) was used to verify identity. ICOCA was rendered by the model, not overlaid from a local file.

```text
Use case: stylized-concept. Create one finished downloadable flat rectangular card-face image, landscape 1.586:1, fully opaque from edge to edge. A refined nonofficial fan-art transit card inspired by Demon Slayer: Nezuko Kamado unmistakably recognizable with long dark hair fading copper, pink kimono geometric pattern and small bamboo muzzle, shown in a graceful half-body portrait on the LEFT. Art direction: premium modern Japanese woodblock print, dark indigo night, muted sakura pink, a few crisp bamboo leaves and a single soft moon disk; intentional depth and generous uncluttered dark field on RIGHT. Add one modest, legible style-matched ICOCA wordmark at lower-right as part of the whole generated illustration, not a pasted sticker. Do not add Demon Slayer title, other text, chip, number, payment wave, NFC, QR, border, corner rounding, card mockup, device, watermark, shadows outside canvas, or transparent pixels. Avoid gore, keep restrained sophisticated hierarchy.
```

### 高专同学 Q 版 × Visa

- Output: [`anime-jujutsu-high-chibi-visa.png`](anime-jujutsu-high-chibi-visa.png)
- Character reference: model knowledge; no image file passed. This replaces a discarded realistic Gojo concept.

```text
Use case: stylized-concept. Make one finished fully opaque flat landscape collectible card face, 1.586:1, a nonofficial chibi fan-art interpretation of Jujutsu Kaisen's Tokyo Jujutsu High classmates: Yuji Itadori (short pink hair and dark uniform with red hood), Megumi Fushiguro (spiky dark hair, serious), Nobara Kugisaki (short orange-brown bob, confident), and Panda (friendly black-and-white panda teammate). Draw exactly these four, unmistakable as a playful cohesive group, each as a neat chibi full-body figure with short arms and simple hands; avoid extra fingers or anatomy glitches. No Satoru Gojo and no death/finale imagery. Art direction: polished Japanese enamel pin / sticker-sheet illustration ON A SOLID WARM IVORY BACKGROUND, clean ink outlines, dark navy, brick red, muted gold accents, subtle abstract cursed-energy swirls, refined spacing not crowded. Small compact VISA mark in lower-right, style-matched and generated as part of composition. No series title, extraneous text, chip, card number, NFC/contactless, QR, border, rounded card mask, mockup, device, watermark, gore or transparency. Every pixel including every edge opaque.
```

### 桃与厄卡伦 × PASMO

- Output: [`anime-dandadan-momo-okarun-pasmo.png`](anime-dandadan-momo-okarun-pasmo.png)
- Character references: [Momo](https://anime-dandadan.com/_assets/images/char/detail/momo_pc.png), [Okarun](https://anime-dandadan.com/_assets/images/char/detail/ken_pc.png) from the [official character page](https://anime-dandadan.com/character/). The image inputs were temporary references, not redistributed.

Initial prompt:

```text
Use case: stylized-concept. Reference images 1 and 2 show the official visual appearances of Momo Ayase and Okarun from Dandadan; use them for character identity ONLY, never copy the poses or page layout. Generate one complete nonofficial fan-art card face, flat edge-to-edge opaque landscape 1.586:1. Hero composition: Momo on LEFT, confident expression, brown hair, green earrings, pink top; Okarun on RIGHT, messy dark hair and round glasses, black school outfit; dynamic but clearly readable pair in the middle distance. A single large graphic UFO ellipse arcs behind them, with a few white-and-orange paranormal sparks. Art direction: striking 1970s Japanese screenprint poster, magenta, tangerine, acid mint and deep midnight navy, halftone texture but not messy. A compact style-matched PASMO wordmark in the lower-right, integrated in the whole generated image; no series title or stray letters. No chip, number, NFC, QR, border, rounded corners, mockup, device, watermark or transparency. All pixels opaque.
```

Final edit prompt (input: first generated card image):

```text
Use case: precise-object-edit. Input is the card face to repair. The oversized foreshortened hands in front of Momo and Okarun are anatomically wrong: Momo's hand has reversed handedness and too few fingers. Remove BOTH giant foreground hands entirely and recompose both characters as relaxed upper-body portraits with their hands out of frame. Preserve both recognizable faces, hair, clothing, green earrings, the striking magenta/orange/mint retro screenprint UFO background, and the PASMO mark in lower right. Preserve all other artwork as much as possible. Flat opaque edge-to-edge landscape card face 1.586:1; no added lettering, card number, chip, NFC, QR, border, rounded corners, device, mockup or transparent pixels. This is an anatomy/layout repair, not a wholesale redesign.
```

### 山田／田山 × Suica

- Output: [`anime-yamada-tayama-suica.png`](anime-yamada-tayama-suica.png)
- Visual references: [official character-announcement lineup](https://yanisuu.com/news/post-100), [official Tayama standing image](https://yanisuu.com/assets/img/character/chara2/stand.webp?ver=1.41). Images were used only temporarily to understand the two looks and were not redistributed.

```text
Use case: stylized-concept. Reference image 1 is the OFFICIAL character lineup of Smoking Behind the Supermarket with You; the same adult woman appears as Tayama in black leather jacket / white dress / burgundy hair (second figure) AND as Yamada in red supermarket apron / olive blouse / burgundy bob (third figure). Reference image 2 is Tayama's official standing appearance. Create one new nonofficial fan-art landscape card face, fully opaque flat rectangular 1.586:1. The central artistic idea is TWO SIDES OF THE SAME WOMAN: Yamada on LEFT, friendly smiling red-apron supermarket worker in warm daylight cream and coral; Tayama on RIGHT, cool subtle smile, burgundy hair, black leather jacket and white dress in rainy after-hours indigo. A vertical soft light seam or thin sliding door divides the two worlds, with the same facial features on both sides. No male protagonist, no extra people. Add a delicate small curl of smoke only on the night side, but no cigarette advertising feel. Cinematic yet graphic clean art with strong side-by-side contrast and enough room for faces; do not copy the source lineup layout. Place one modest ivory SUICA wordmark bottom-right on dark side. No series title, labels, additional text, chip, number, NFC, QR, border, rounded corners, device, mockup, watermark or transparency. Every pixel fully opaque.
```

### 克罗诺亚 × Mastercard

- Output: [`anime-chronoa-mastercard.png`](anime-chronoa-mastercard.png)
- Visual reference: [official Chronoa page](https://www.ten-sura.com/character/chronoa), [official character image](https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/assets/images/character/chronoa/character-image.png?v=6), used as a temporary visual input only. Replaces a discarded Rimuru concept.

```text
Use case: stylized-concept. Image 1 is official Chronoa character appearance reference from That Time I Got Reincarnated as a Slime; use it for identity only, NOT as a cutout or existing layout. Generate a fresh complete nonofficial fan-art card face, flat fully opaque edge-to-edge landscape 1.586:1. Chronoa is a mysterious black-haired girl with blue-violet eyes and dark armor, elegant long cape and a gold-accented sword. Place her slightly LEFT of center, poised and composed; make a large circular fractured CLOCK / time-halo behind her, gold hour markers and violet-blue magical trails sweeping toward a spacious right half. Art direction: premium fantasy art nouveau with midnight navy, antique gold, muted violet and subtle mica gloss, detailed yet carefully composed. A small readable style-matched Mastercard two-circle symbol at lower right, silver line treatment, no wordmark needed. No other characters, blue slime, title, card number, chip, contactless icon, QR, border, rounded corners, device, mockup, watermark or transparency. Opaque dark background all the way to every edge.
```

### 爱蜜莉雅 × Visa

- Output: [`anime-emilia-visa.png`](anime-emilia-visa.png)
- Character reference: model knowledge and [official Re:Zero character page](https://re-zero-anime.jp/tv/character/); no image file passed.

```text
Use case: stylized-concept. Generate a finished nonofficial Re:Zero fan-art card face as one flat fully opaque landscape rectangle, about 1.586:1. Emilia is the unmistakable heroine: long silver hair, violet eyes, white-and-lavender fantasy outfit, delicate flower hair ornament; three-quarter portrait left of center, elegant and kind, not generic idol. Puck, a tiny gray cat-like spirit, appears discreetly by her shoulder. Art direction: ethereal snow-crystal stained glass with soft amethyst and pearl, blue twilight, restrained luminous frost geometries leading into open negative space on the right. This should feel like a high-end collectible card, not a screenshot or busy game UI. Include only a modest style-matched Visa wordmark in lower-right, comfortably away from trim. No series title, card number, chip, NFC/contactless icon, QR, border, rounded-corner mask, mockup, device, watermark or transparency. Image must have a solid opaque background to all edges.
```

### 乔鲁诺 × Mastercard

- Output: [`anime-giorno-mastercard.png`](anime-giorno-mastercard.png)
- Character reference: model knowledge and [official JoJo animation site](https://wwws.warnerbros.co.jp/jojo-animation/); no image file passed.

```text
Use case: stylized-concept. Make one complete nonofficial JoJo's Bizarre Adventure fan-art card face, fully opaque flat rectangular landscape 1.586:1. Hero: Giorno Giovanna, recognizable blond hair with three rolled curls at forehead, confident calm gaze and purple outfit with heart-shaped chest opening and gold trim, elegantly posed left of center. Art direction: bold 1960s Italian fashion screenprint meets lavish Art Deco graphic design, gold foil geometry, amethyst purple, dusty rose, small ladybug motifs and a single diagonal sunbeam; sophisticated fashion illustration rather than a fight scene. Place a small style-matched gold-outline Mastercard overlapping-circle emblem in lower-right, comfortably inset, no brand wordmark needed. Strong clear hierarchy and some negative space on right; avoid distorted limbs and extra hands. No series title, other lettering, chip, number, NFC/contactless icon, QR, border, rounded corners, device, mockup, watermark or alpha transparency. Every edge solid and opaque.
```

### 利威尔 × Visa

- Output: [`anime-levi-visa.png`](anime-levi-visa.png)
- Character reference: model knowledge and [official Attack on Titan character page](https://shingeki.tv/season1/character/); no image file passed.

```text
Use case: stylized-concept. Create a fully opaque flat landscape card-face illustration, 1.586:1 rectangular edge-to-edge, nonofficial fan art inspired by Attack on Titan. Hero: Levi Ackerman, recognizable short black undercut hair, stern gray eyes and olive Survey Corps cloak, shown from the waist up on the LEFT in a poised quiet profile, no giant/gore. Background: layered monumental walled city fading into dawn mist, two tiny birds and a restrained wing-shaped abstract motif; no Titan attack or violent scene. Art direction: premium vintage lithograph/etching, graphite, moss green and warm aged ivory with limited antique silver light, sober dramatic atmosphere with clean room on the RIGHT. Put a small readable muted-silver VISA mark at lower-right, painted as part of the whole image. No series title or extra readable text, chip, card number, NFC/contactless icon, QR, border, rounded-corner mask, device, mockup, watermark or transparency. Solid opaque texture to every edge.
```

## 牛来 × American Express（非官方玩梗）

- Output: [`niu-lai-amex-parody.png`](niu-lai-amex-parody.png)
- Visual references: [American Express's card-structure guide](https://www.americanexpress.com/content/dam/amex/za/network/documents/merchant-prevent-fraud-2014.pdf), [centered Platinum card layout](https://travelafterwork.azureedge.net/uploads/2019/08/Amex-Plat.png), [《牛来》 film still](https://news.ifeng.com/c/8vcLKbjIKad). The card and movie still were used only as visual references, not republished here.

```text
Use case: stylized-concept. Asset type: one non-official parody card-face image for the Card Creator gallery, flat edge-to-edge 1.586:1 landscape artwork, opaque rectangular canvas. Image 1 is ONLY a composition reference: classic American Express Platinum charge card, with centered engraved Centurion cameo, top-centered brand lettering, symmetric guilloché field and delicate border; do not copy its chip, cardholder text, or card details. Image 2 is ONLY a character identity reference from the animated movie 牛来: use the SMALL yellow-orange calf at left, not the tall adult or leopard. Preserve its deliberately awkward little horns, half-lidded sideways eyes, broad mauve-purple muzzle, and recognizable deadpan expression. Create a refined but genuinely funny parody by replacing the traditional human Centurion portrait with a centered, elegantly engraved cameo bust of that calf inside a single oval medallion. Make the calf head and oval the dominant CENTRAL focal point, optically centered across the entire card (not off to one side), with ample balanced open space left and right. Restrained platinum-silver, soft ice blue and pale gold security-engraving / banknote linework; a tiny hint of the calf's warm ochre and muted purple can remain. Symmetrical ornate fine-line border and subtle repeating guilloché, but the centered cow face stays readable at thumbnail size. At the top, only one modest, centered, clean two-line inscription exactly 'AMERICAN EXPRESS'; do not place giant lettering on the right. No other text anywhere, no 'PLATINUM', no card number, no name, no date, no chip, no NFC/contactless icon, no barcode, no QR, no fake account details, no extra characters, no official/real-card implication, no physical mockup, no shadows, no white margins, no rounded-corner cutout. Generate as an artistic fan parody, not an official payment card. Output ONE finished image.
```

## 奶龙捧腹大笑 × 黄色 Suica（非官方玩梗）

- Output: [`laughing-nailong-suica.png`](laughing-nailong-suica.png)
- Visual references: [经典 Suica 卡外观](https://i.ebayimg.com/images/g/yrMAAOSwjoNoFYxa/s-l1200.jpg), [奶龙捧腹大笑表情包](https://imgheybox.max-c.com/bbs/2026/01/15/b2651cd314d13862f5eb928ea8d2fc13/thumb.png), [`../skills/card-creator/assets/logo-references/overseas/japan/suica.png`](../skills/card-creator/assets/logo-references/overseas/japan/suica.png). The source photos were used as visual references, not republished. An earlier friendly-wave draft was discarded after the user clarified the meme.

Initial composition prompt (reference images: classic Suica card, ordinary Nai Long character, Suica logo):

```text
Create ONE finished, flat, edge-to-edge LANDSCAPE card-face illustration, aspect ratio about 1.586:1, full opaque image. A witty high-quality nonofficial fan-art reinterpretation of the classic Suica transit-card layout. Reference 1 is ONLY the classic Suica card design layout: broad left trapezoid with slanted right edge, pale right field, large simple 'Suica' word on the left, penguin at right. Reference 2 is the Nai Long (奶龙) character identity: round sunny yellow cartoon dinosaur, white belly, tiny horns, green-black eyes, adorable awkward grin. Reference 3 is only a visual reference for Suica identity; DO NOT paste any reference screenshot, wood surface, border, device, watermark or text from it. Replace the Suica penguin entirely with one recognizable Nai Long on the right, charmingly leaning into the diagonal edge. Recolor the strong left trapezoid to warm vivid marigold yellow; use creamy ivory and pale lemon as the surrounding palette; retain the iconic diagonal composition and a clean large 'Suica' word on the yellow area in white, plus only a restrained tiny style-matched Suica identity symbol near the upper right. Premium minimal Japanese transit-card design, playful but impeccably composed, generous breathable space, crisp shapes, soft tactile printed finish, no collage. No other characters, no chips, card numbers, NFC/contactless symbol, QR, slogan, arbitrary letters, wallet UI, rounded-card mockup or shadow. The complete artwork including all text and marks must be image-generated, not overlaid.
```

Final image-generation edit prompt (input 1: initial card; input 2: specific laughing meme reference):

```text
Edit image 1, a finished yellow Suica fan-art card face. Keep the entire card layout, large marigold left trapezoid, big white Suica word, pale cream field and upper-right small Suica identity exactly as they are. Replace ONLY the cute waving dinosaur on the right with the exact absurd '奶龙捧腹大笑' meme pose shown in reference image 2: a long-bodied pale yellow creature bent forward laughing uncontrollably, eyes squeezed shut in curved slits, HUGE dark wide-open mouth, both hands clasping its round belly, distorted ungainly posture and gray hands. It must read immediately as the specific belly-laugh meme, not as a friendly wave or gentle smile. Make the whole laughing figure visible on the right, slightly large, with enough margin; harmonize its lighting into the premium card illustration without making the expression less absurd. Keep this a flat fully opaque 1.586:1 card-face raster, no wood, screenshot, mockup, border, chip, card number, NFC icon or new words. This is a targeted character replacement, not a full redesign.
```

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

The lion version is retained for provenance but no longer featured in the gallery.

## 蓝晶猫影 × 汇丰（当前画廊版）

- Output: [`hsbc-crystal-cat.png`](hsbc-crystal-cat.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png`](../skills/card-creator/assets/logo-references/banks/hong-kong/hsbc.png). The previous lion card and the user's example image were not passed to the generator.

```text
Use case: stylized-concept. Asset type: finished downloadable card-face artwork for a noncommercial fan-art gallery. Image 1 is ONLY the HSBC logo visual identity reference; do not use any previous lion-card image as a layout reference. Make a new original flat edge-to-edge opaque landscape card face, approximately 1.586:1. Subject: an unmistakably domestic CAT, not a lion: a graceful seated cat in three-quarter profile with pointed ears, slim muzzle, small paws and an elegant curved tail. Design language: sophisticated midnight-blue and icy-cyan crystalline origami, broad angular mineral-glass facets flowing from the cat into an abstract quiet background, delicate pearlescent glints; refined and slightly playful, not cartoon mascot, not a royal guardian animal. Composition different from a close-up lion portrait: show the full cat silhouette slightly left of center, ample spacious dark-blue field at right. A small recognizable red-and-white HSBC hexagon plus clean white 'HSBC' wordmark sits comfortably in the upper-right, painted as part of the complete image, nonofficial artistic interpretation. No lion mane, no HSBC stone lion, no skyline, no second oversized hexagon, no chip, card number, contactless symbol, payment network mark, slogans, other text, rounded corners, border, shadow, device, mockup or watermark. Output fully opaque at every pixel.
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

The line-art Guangzhou version is retained for provenance but no longer featured in the gallery.

## 广州 · 彩窗夜河 × 羊城通（当前画廊版）

- Output: [`guangzhou-arcade-yangchengtong.png`](guangzhou-arcade-yangchengtong.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/guangzhou-yangchengtong-official-opaque.png`](../skills/card-creator/assets/logo-references/cities/guangzhou-yangchengtong-official-opaque.png)

```text
Use case: stylized-concept. Asset type: finished downloadable Guangzhou city transit-card face for a noncommercial fan-art gallery. Image 1 is ONLY a visual identity reference for the 羊城通 / YANG CHENG TONG mark, not a composition reference. Make a completely new, premium, flat edge-to-edge OPAQUE landscape card artwork, about 1.586:1, replacing an ugly sparse line-art card. Art direction: contemporary Lingnan enamel and architectural stained-glass, sophisticated rather than tourist-poster. A single graceful arch inspired by old Guangzhou arcade windows frames a distant, unmistakable slender Canton Tower across the Pearl River at blue hour; luminous river reflections form broad flowing bands. Deep peacock teal, warm coral-orange, ivory and restrained brass-gold; translucent enamel glow and fine grain. Clear hierarchy: architecture and river are the art; a modest, readable style-matched 羊城通 mark based on image 1 sits at the upper-left with generous breathing room, integrated into the artwork. Do NOT add the 交通联合 mark, 岭南通 mark, flower, row of skyline icons, card number, chip, NFC/contactless mark, QR, watermark, border, rounded corners, mockup, device, fake signs or any other text. Nonofficial artistic logo interpretation. Refined, atmospheric, memorable, fully opaque rectangular canvas.
```

## 大湾区 · 海上相连 × 虚构「大湾区通」/ 交通联合

- Output: [`greater-bay-sea-bridge-concept.png`](greater-bay-sea-bridge-concept.png)
- The fictional 大湾区通 mark was made for this concept only. The prior [`guangzhou-minimal-lingnantong-tunion-v2.png`](guangzhou-minimal-lingnantong-tunion-v2.png) was passed to the final edit only as a visual reference for the 交通联合 mark, **not** as a composition reference or official logo source.

Initial bridge artwork:

```text
Use case: stylized-concept. Asset type: finished downloadable Greater Bay Area themed concept card face for a noncommercial art gallery. Create ONE premium flat edge-to-edge fully OPAQUE landscape image, about 1.586:1. This is an artistic regional concept, NOT a real interoperable transit card and NOT an official brand. Scene: seen from above at first light, a single long elegant sea bridge curves gently between a few pearl-like islands across the broad estuary, with delicate wakes and bands of tidal current suggesting connected shores. No rows of city skylines. Art direction: quiet contemporary Japanese-style printmaking meets premium cartography, large balanced shapes, engraved water textures, luminous nacre and pale champagne reflections over deep marine indigo and sea-glass green; restrained, sophisticated, spacious. The bridge is the hero, with the sea taking most of the canvas and a calm upper area. Do not add any logo, fictional operator mark, text, place labels, map pins, card number, chip, NFC/contactless symbol, QR, badge, border, rounded corner, mockup, device, shadow or watermark. Make it feel like an art card, not a tourism poster. Output a complete opaque rectangular card face.
```

Branding edit requested by the user:

```text
Use case: precise-object-edit. Image 1 is the EDIT TARGET: a finished elegant Greater Bay Area sea-bridge concept card. Image 2 is ONLY a visual reference for the short red-and-blue '交通联合 / China T-Union' mark located at the upper-right of that old Guangzhou card; do NOT copy its composition, tower, flowers, lines, or Lingnan Tong logo. Preserve image 1's bridge, islands, tides, blue-green water, champagne sunrise, composition and full landscape framing. Add exactly TWO tasteful small marks, painted as part of the same scene: (A) at the upper-left in the quiet pale sky, create an ORIGINAL, clearly fictional '大湾区通' concept logo: three clean interlocking bay/bridge arcs in sea-glass blue, deep navy and muted gold, with the exact Chinese words '大湾区通' below or beside it in elegant dark-navy type; no claim it is an existing operator. (B) at the lower-right over a quiet dark-water area, add a modest recognizable short-form red-and-blue '交通联合' / China T-Union style mark inspired by image 2, rendered legibly as a nonofficial stylized interpretation. Keep both marks balanced and separated, not oversized, and do not let either obscure the bridge. No other words, station names, card number, chip, NFC/contactless icon, QR, border, device, shadow, rounded mask, mockup, or watermark. Fully OPAQUE rectangular card face. This is a precise branding addition, not a redesign.
```

## 佛山 · 赤金醒狮 × 广佛通

- Output: [`foshan-lion-dance-guangfo-tong.png`](foshan-lion-dance-guangfo-tong.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/guangfo-tong-reference.png`](../skills/card-creator/assets/logo-references/cities/guangfo-tong-reference.png)

```text
Use case: stylized-concept. Asset type: finished downloadable Foshan city transit-card face for a noncommercial fan-art gallery. Image 1 is ONLY a visual identity reference for the 广佛通 / Guangfo Tong mark, not a card composition reference. Create a new flat edge-to-edge OPAQUE landscape card artwork, approximately 1.586:1. Central subject: an elegant Foshan lion-dance HEAD in dynamic three-quarter profile, with expressive round eyes and layered fabric details, not a real lion animal and not a cartoon mascot. Art direction: high-end Lingnan lacquer and hand-cut paper collage, dramatically simplified into a few strong shapes; deep cinnabar red, muted antique gold, ink-black and warm ivory paper, tiny jade accents. Let the lion-dance ribbons sweep from left-center toward the lower edge with breathing room on the right. Include one modest clear style-matched 广佛通 mark based on image 1 in a quiet right-hand area; preserve its arcing colored band and Chinese name as recognizable, but integrate it into the palette rather than pasting a white box. The image model paints the whole composition. No fictional station names, extra lettering, chip, card number, payment-network mark, NFC/contactless icon, QR, border, rounded corners, shadow, device, mockup or watermark. Refined, festive but not kitschy; fully opaque rectangular card face.
```

## 西安 · 石色钟楼 × 长安通（新版）

- Output: [`xian-changan-tong-bell-tower.png`](xian-changan-tong-bell-tower.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/xian-changan-tong.png`](../skills/card-creator/assets/logo-references/cities/xian-changan-tong.png)

```text
Use case: stylized-concept. Image 1 is only a visual identity reference for the 长安通 / CHANG'AN CARD logo, not a composition reference. Create a completely NEW Xi'an transit-card face with a lighter, more contemporary and premium visual direction than a heavy red woodblock print. Flat fully opaque edge-to-edge landscape card artwork, approximately 1.586:1, no mockup or rounded-corner mask. Art direction: understated museum-editorial illustration inspired by the architecture of Xi'an Bell Tower and Tang-era stone and ceramic materials. Airy warm limestone/ivory field with spacious negative space; the recognizable Bell Tower forms a graceful detailed but simplified architectural silhouette across the lower-right two-thirds, rendered in refined terracotta and dark slate-blue fine linework, sparse muted gold accents, subtle mineral-paper texture. No giant red sun disk, no dense black city wall, no distressed poster/grunge look. Integrate one moderately sized, clearly readable style-matched 长安通 / CHANG'AN CARD mark in the upper left based on image 1; keep it in balance with the tower rather than making it the hero. No other text, chip, card number, QR, contactless/NFC mark, payment network logo, border, shadow, device or fake signs. Image model paints the whole composition, including the nonofficial artistic brand interpretation.
```

The first output accidentally had a transparent background. An image-generation edit made the warm limestone field fully opaque while preserving the composition:

```text
Use case: precise-object-edit. Image 1 is the EDIT TARGET, a new Xi'an Chang'an Card face illustration. Repair only its unintended transparent background. Replace every transparent or partially transparent background pixel with a smooth, fully OPAQUE warm limestone/ivory paper tone, edge to edge; all visible architectural art, the Bell Tower, soft mountains, thin clouds and the readable 长安通 / CHANG'AN CARD logo must be preserved in exactly the same positions, shapes and proportions. Remove the black/transparent void at the top and the blocky alpha-edge transition; make the parchment field continuous and natural. Preserve the airy museum-editorial terracotta/slate/gold aesthetic. Flat rectangular landscape card face, no mockup, no rounded corners. No extra text, chip, NFC, card number, other mark or new objects. This is only a technical background-opacity correction, not a redesign.
```

## 深圳 · 海湾流线 × 深圳通符号

- Output: [`shenzhen-bay-tong-symbol.png`](shenzhen-bay-tong-symbol.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/shenzhen-tong-symbol.png`](../skills/card-creator/assets/logo-references/cities/shenzhen-tong-symbol.png). The reference is symbol-only, so no wordmark was invented.

```text
Use case: stylized-concept. Asset type: finished flat transit-card face for a free noncommercial fan-art gallery. Input image 1 is a visual identity reference for the multicolor Shenzhen Tong SYMBOL ONLY, not a wordmark or an exact compositing asset. Create a distinctly Shenzhen card face in refined, forward-looking graphic minimalism. Opaque edge-to-edge landscape composition about 1.586:1. Pearl-white and pale aqua backdrop, one flowing translucent cyan arc evoking Shenzhen Bay Bridge, a restrained blue-green waterfront silhouette in the distance and a few crisp sunlit geometric planes; generous clean negative space. Use the attached colorful asymmetric symbol once, rendered legibly as part of the artwork at a comfortable corner scale; do not add or invent any 深圳通 text because the provided reference is symbol-only. The palette should harmonize with its lime, blue and magenta accents without becoming a rainbow poster. Editorial sophistication, precise linework, subtle satin-paper sheen. No fake signs or slogans, no card numbers, chip, QR, contactless/NFC mark, payment network logo, border, rounded mask, device or mockup. Model paints the whole design; output fully opaque.
```

Logo-size correction (input 1: first card; input 2: same symbol reference):

```text
Use case: precise-object-edit. Image 1 is the EDIT TARGET: a finished flat Shenzhen city card face. Image 2 is the visual identity reference for the colorful Shenzhen Tong symbol only. Change ONE thing: the symbol in the upper-left is much too large. Remove the oversized symbol cleanly and repaint it in the same upper-left area at roughly one third of its current width and height, with comfortable margin from the edges. Keep its recognizable asymmetric yellow, lime, navy, magenta and gray geometry based on image 2. Preserve everything else from image 1: pale aqua/white palette, sweeping translucent bridge arc, Shenzhen Bay Bridge, distant skyline, water, subtle geometric planes, full edge-to-edge landscape framing and every other visual detail. No Shenzhen Tong text, no other text, chip, contactless icon, border, card mockup or rounded corners. Output a fully opaque rectangular card-face raster. This is a surgical logo-size correction, not a redesign.
```

## 杭州 · 西湖瓷青 × 市民卡运营方

- Output: [`hangzhou-west-lake-citizen-card.png`](hangzhou-west-lake-citizen-card.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/hangzhou-citizen-card-operator.png`](../skills/card-creator/assets/logo-references/cities/hangzhou-citizen-card-operator.png). Operator identity, not a verified 杭州通 product sticker.

```text
Use case: stylized-concept. Asset type: finished flat city-card face for a free noncommercial art gallery. Input image 1 is a visual identity reference for the 杭州市民卡 / Hangzhou Citizen Card OPERATOR mark; it is NOT proof of a separate '杭州通' card logo. Create one distinctly Hangzhou artwork, opaque edge-to-edge landscape about 1.586:1. Art direction: contemporary Song-dynasty-inspired celadon glaze and fine silk-screen linework, spacious and quiet. One graceful, recognizable West Lake Broken Bridge crosses pale celadon water in the middle distance; a few willow fronds and lotus leaves draw the eye without turning into a souvenir collage. Palette of misty celadon green, warm porcelain white, very restrained tea-brown ink; subtle ceramic crackle/pearl sheen only in light. Include one clean readable style-matched Hangzhou Citizen Card operator logo based on the input, comfortably inside a corner; preserve its meaning as an operator mark, do not invent '杭州通' lettering. The mark may be green and teal, but should feel harmonized with the lake. No other text, card numbers, chip, QR, contactless/NFC mark, payment network logo, border, rounded mask, device or mockup. The image model paints the whole design; fully opaque.
```

## 重庆 · 山城轨道 × 城市通卡运营方

- Output: [`chongqing-city-card-monorail.png`](chongqing-city-card-monorail.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/cities/chongqing-city-card-operator.png`](../skills/card-creator/assets/logo-references/cities/chongqing-city-card-operator.png). Operator identity, not a verified 畅通卡 product sticker.

```text
Use case: stylized-concept. Asset type: finished flat city-card face for a free noncommercial art gallery. Input image 1 is a visual identity reference for 重庆城市通卡 OPERATOR mark; it is NOT a verified '畅通卡' product sticker. Create a distinctly Chongqing card-face artwork, opaque edge-to-edge landscape about 1.586:1. Art direction: sophisticated contemporary screenprint poster of Chongqing's layered mountain city at blue hour. One slender, unmistakable monorail passes through the middle of a single terraced hillside building (a stylized Liziba scene); silhouettes of stacked stairways and river cliffs recede behind it. Dramatic but orderly diagonal composition, deep indigo and midnight blue with warm coral-orange window lights and a few magenta accents inspired by the reference mark. Keep sufficient calm space for one legible 重庆城市通卡 operator logo based on the attached reference, painted by the image model and harmonized with the palette. Do not add or imply any separate '畅通卡' product logo. No fake signs or slogans, no card numbers, chip, QR, contactless/NFC mark, payment network logo, border, rounded mask, device, shadow or mockup. Premium, readable, fully opaque.
```

Chongqing opacity-preserving text correction (input 1: first generated card; input 2: the same operator reference):

```text
Use case: precise-object-edit. Image 1 is the EDIT TARGET, an otherwise finished Chongqing city-card face. Image 2 is the visual reference for the operator logo. Make ONE small correction only: REMOVE the fabricated Latin/English subtitle beneath the large Chinese 重庆城市通卡 mark in the upper-left, including the nonsensical 'CHONGQING PAYEASY' lettering. Leave a clean dark-blue background in that narrow strip. Retain the colorful emblem and the Chinese title 重庆城市通卡 clearly, based on image 2. Preserve all other pixels and composition as closely as possible: same blue-hour layered city, rail train passing through building, distant bridge and river, warm lights, blue/coral palette, camera framing, full opaque rectangular canvas. Do not add any text, payment marks, chip, NFC icon, border or card mockup. This is a surgical text-removal correction, not a new design.
```

## 海外城市交通卡面（2026-09-24 入选）

下面四张均为非官方图像生成创作。参考图只供识别标志，不作为图层贴入；伦敦雨夜旧稿未上架。

### 伦敦 · 春日厚涂 × Oyster

- Output: [`london-oyster-impasto-v2.png`](london-oyster-impasto-v2.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/overseas/uk/oyster-card.png`](../skills/card-creator/assets/logo-references/overseas/uk/oyster-card.png)

```text
Use case: stylized-concept. Asset type: non-official London Oyster transit-card face candidate. Create ONE flat full-bleed landscape artwork at approximately 1.586:1, a FULLY OPAQUE RECTANGLE with color and oil paint reaching every corner. Replace the previous gloomy London rain-night mood with a bright, uplifting, sophisticated London spring afternoon. The main visual is a deliberately artful, contemporary oil painting of a London street near an Underground entrance: graceful curving station architecture, a small red bus as a distant accent, softly suggested city rooftops, sunlight across pavement. Extremely tactile heavy impasto and palette-knife painting, physically thick ridges of cobalt, turquoise, cream, coral and buttery gold paint with visible cast shadows from raised brushstrokes. Rich artistic materiality, refined high-end gallery quality; still simple enough to read as a card, with clear focal hierarchy and negative space. Add only the recognizable lowercase 'oyster' wordmark, compact and tastefully integrated at lower right in a deep blue that contrasts with the light paint. Use the attached Oyster card only as a visual reference for the wordmark, not as a source image layer or card layout. No other text, no route numbers, no card number, no chip, no NFC/contactless icon, no QR code, no frame, no physical mockup, no rounded-corner cutout, no shadow outside the artwork, NO transparency or white/empty margins. Non-official artistic interpretation.
```

### 纽约 · 地铁版画 × OMNY

- Output: [`new-york-omny-graphic.png`](new-york-omny-graphic.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/overseas/usa/omny.png`](../skills/card-creator/assets/logo-references/overseas/usa/omny.png)

```text
Use case: stylized-concept. Asset type: candidate artwork for a non-commercial card-face gallery. Make ONE polished, complete, flat, edge-to-edge landscape transit-card face, approximately 1.586:1. Concept: New York OMNY as a collectible urban graphic design card, aimed at young people living abroad. Sharp but playful editorial composition: diagonal MTA-style subway tile geometry, a single orange subway train slipping into a tunnel, energetic layered transit-line ribbons, hints of Manhattan's ironwork and street-grid pattern. Distinct from cinematic illustrated landscapes: use bold clean geometric forms, sophisticated cream, subway orange, ink black, and restrained electric blue; slight printed-paper texture. Keep a spacious clean lower-right corner for a recognizable 'OMNY' mark, based on the supplied logo picture as visual reference. Brand mark can be style-matched but should read OMNY clearly; do not paste the reference as a layer. No people, no other words or lettering, no route numbers, no QR code, no chip, no contactless/NFC symbol, no mockup, no rounded-corner cutout, no border or drop shadow. This is non-official artistic fan concept, not a functioning fare card.
```

### 悉尼 · 蓝花楹海湾 × Opal

- Output: [`sydney-opal-jacaranda.png`](sydney-opal-jacaranda.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/overseas/australia/opal.png`](../skills/card-creator/assets/logo-references/overseas/australia/opal.png)

Base generation prompt:

```text
Use case: stylized-concept. Asset type: candidate artwork for a non-commercial card-face gallery. Make ONE complete flat, edge-to-edge landscape transit-card face, approximately 1.586:1. Concept: Sydney Opal card reimagined for a young overseas resident. The mood is fresh, serene and quietly luxurious: jacaranda blossoms drifting across a luminous pale lavender-to-sky-blue harbor morning, abstract ferry wake and soft Sydney harbor-bridge arches in the far distance, with plenty of breathing room. Use refined contemporary gouache and subtle pearlescent paper texture, not photo realism and not tourist-poster cliché. Compose blossoms mainly at left and top; retain a calm pale area at lower right for a small but readable 'opal' mark. Use the supplied Opal logo picture as visual reference only; integrate a color-harmonized recognizable opal wordmark as part of the generated artwork rather than pasting a layer. No other text or symbols, no numbers, QR code, chip, contactless/NFC icon, device, mockup, border, rounded-corner cutout or shadow. Non-official artistic interpretation, not a working transit card.
```

Final edge-repair prompt (input: first generated image):

```text
Use case: precise-object-edit. Edit target: the provided Sydney Opal card artwork. Preserve the jacaranda blossoms, Sydney harbor, bridge, ferry wake, soft gouache style, palette, and the readable 'opal' wordmark. CHANGE ONLY THE FOUR OUTER CORNERS AND EDGES: remove the rounded-card silhouette and any transparent or white cutout outside it; extend the existing sky, blossoms and water naturally all the way to every pixel of a full opaque rectangular canvas, especially top-left, top-right, bottom-left, bottom-right. The artwork must be one solid edge-to-edge 1.586:1 rectangle with no alpha/transparency anywhere, no rounded-corner mask, no background beyond the card. Do not add text, chip, numbers, NFC icon, border, shadow, mockup or UI. Keep the current composition otherwise.
```

### 威尼斯 · 石狮泻湖 × Venezia Unica

- Output: [`venice-venezia-unica-marble-lion.png`](venice-venezia-unica-marble-lion.png)
- Visual reference: [`../skills/card-creator/assets/logo-references/overseas/italy/venezia-unica-citypass.jpg`](../skills/card-creator/assets/logo-references/overseas/italy/venezia-unica-citypass.jpg)

```text
Use case: stylized-concept. Asset: ONE non-official Venezia Unica City Pass transit-card face for the Card Creator gallery. Generate a complete flat, opaque, edge-to-edge rectangular landscape artwork around 1.586:1 (no physical-card mockup or rounded-corner mask). Visual reference image: the attached official Venezia Unica City Pass logo, used ONLY to understand its distinctive CITYPASS / VENEZIA / UNICA lettering and red accent; generate the entire image together, do not paste the logo image or its white background. Art direction: an Italian Renaissance-inspired sculptural relief from Venice. A magnificent but graceful winged Lion of Saint Mark carved in warm ivory marble occupies the left-center as the unmistakable hero, with finely chiseled feathers and soft realistic stone depth; behind it, pale Venetian Renaissance arcades, a quiet turquoise lagoon and a hint of sunlit reflections. Restrained palette of ivory limestone, antique parchment, lagoon blue-green and tiny touches of oxidized terracotta red; luminous late-afternoon light, luxurious museum-quality composition, poised and spacious rather than busy or tourist-poster cliché. Keep the winged lion and sculpture tactile; leave balanced breathing room for one compact, legible, style-matched 'VENEZIA UNICA' City Pass identity in the lower right, with a small dark-red accent inspired by the reference. Only text allowed is 'VENEZIA UNICA' (optional smaller 'CITYPASS' above if perfectly spelled). The mark is an artistic, non-official interpretation. No other words, no route number, card number, barcode, QR, chip, NFC/contactless symbol, watermark, border, drop shadow, white/transparent margins, or device UI. No fake functionality or official endorsement.
```
