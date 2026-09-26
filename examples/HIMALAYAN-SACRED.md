# 山野与唐卡卡面 · 2026-09-26

本轮按用户确认发布四张，使用内置 ImageGen。等高线采用疏朗 V2；文殊保留交通联合；黄财神只将标志改成银联。图像没有脚本绘制、标志拼贴、拉伸、裁切、圆角遮罩或另行导出。

| 下载 | 实际像素 | SHA-256 |
|---|---|---|
| [文殊 · 青绿雪山](manjushri-mineral-landscape.png) | 996×1579 | b95ac710657e60078e6cad122e0214d0c8c019084a16fc9379290bda46a955df |
| [黄财神 · 碧水莲境](yellow-jambhala-mineral-unionpay.png) | 980×1605 | e84f8d01c2de12fad3be9b213cb14ff3d7b0bb7db72432dba66cc77f5f7b91f0 |
| [珠峰与洛子峰](everest-lhotse-contours.png) | 1578×996 | eb3ac57740c2a5a7a94255fa0f1cc48a5a89718b56c0bc0f8797f76c8c082962 |
| [鱼尾峰 MBC](machhapuchhre-mbc-abc-contours.png) | 1578×996 | 114e3c66d971800c7fd559e0ae6dab5d82566c00ca8c45a8148776e47e532bd5 |

Alpha 检查均为255–255。竖图按原比例展示；黄财神高宽比约1.638，略窄于推荐比例，不用裁切强行凑尺寸。手机与桌面预览不改变下载文件。

## 输入索引与来源

| ID | 实际参考 | 角色及来源 |
|---|---|---|
| MANJUSHRI-V1 | 本项目青金蓝文殊旧稿 | 先由文字生成，再生成式缩小主体、加入山水。图像学文字参考 [The Met](https://www.metmuseum.org/art/collection/search/39420) 与 [Cleveland Museum](https://www.clevelandart.org/print/art/1964.370)，没有下载或使用馆藏照片 |
| JAMBHALA-V1/V2 | 本项目孔雀绿黄财神旧稿 → 山水版 | 文字参考 [The Robert Beer Archive: Five forms of Jambhala](https://tibetanart.com/artworks/405-five-forms-of-jambhala)，文字 Robert Beer、作品 Chewang Dorje；只核对两臂三眼、右手香橼、左手吐宝鼠、右足莲托，未输入该艺术家图片。V2 后仅修改标志 |
| T-UNION | [徐州地铁票卡说明](https://xzdtyy.xzdtjt.com/article/44/jnpzzs/3863.html)中的[江苏交通卡原图](https://pics.xzdtjt.com/upload/20251203111838.png) | 只参考右下角交通联合，不复制江苏名称、卡号或票面；非西藏独有 Logo。第三方商标与图片，再分发许可未核实 |
| UNIONPAY | `skills/card-creator/assets/logo-references/payment/unionpay-compact.png` | 已有紧凑银联标志；模型重绘为金线，既有来源见根目录 SOURCES |
| HIMALAYA-STYLE | 用户提供的 CardArt 小红书等高线截图 | 只参考风格；不发布截图，不复制水印，不声称原作者授权 |
| HIMALAYA-EVEREST | 临时 Esri 地形导出，北朝上，bbox 86.83,27.93,86.98,28.025 | [确切导出请求](https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/export?bbox=86.83,27.93,86.98,28.025&bboxSR=4326&size=1536,969&imageSR=4326&format=png&f=image)，只作地形位置参考，原始地图不再分发 |
| HIMALAYA-MBC | 临时 Esri 地形导出，北朝上，bbox 83.855,28.48,83.975,28.555 | [确切导出请求](https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/export?bbox=83.855,28.48,83.975,28.555&bboxSR=4326&size=1536,969&imageSR=4326&format=png&f=image)，只作地形位置参考，原始地图不再分发 |
| VISA / MASTERCARD | 已有 `payment/visa.png`、`payment/mastercard.png` | 标志外形参考，不是贴图；继承 SOURCES 中的记录 |

Esri 完整上游署名：Sources: Esri, HERE, Garmin, Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), (c) OpenStreetMap contributors, and the GIS User Community.

额外地理文字核对：[尼泊尔旅游部门](https://tourismdepartment.gov.np/pages/mountains1/)；[Seven Summit Treks 行程](https://sevensummittreks.com/page/annapurna-base-camp-abc-trek.html)。[OpenTopoMap](https://github.com/der-stefan/OpenTopoMap) 曾用于只读核对，未作为 ImageGen 输入或再分发：地图 © OpenTopoMap（CC BY-SA），数据 © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)（ODbL）、SRTM。

## 使用边界

等高线及 Deurali → MBC → ABC / EBC 路线都是 AI 艺术示意，不具 DEM 测绘精度，也不是用户去年徒步的 GPS 轨迹。不要用于导航、定位或登山安全决策。MBC 为营地，不是鱼尾峰顶。山峰间距与线条存在艺术化调整。

唐卡意象是当代数字艺术，矿物颜料和18K金均为视觉模拟，不宣称特定画派、仪轨正确、开光、祈福或招财效果。所有品牌是非官方重绘，无发卡、互通、赞助或授权含义；见 [使用声明](../DISCLAIMER.md)。

## 简短提示词

### 文殊 · 青绿雪山

> 使用 card-creator Skill，生成一张文殊菩萨竖版卡面：主体稍小，青绿雪山、溪流与花木，清新的藏式唐卡矿物色，局部暖金光泽，搭配金色交通联合。

### 黄财神 · 碧水莲境

> 使用 card-creator Skill，生成一张黄财神竖版银行卡面：主体稍小，碧水莲境与雪山，石青石绿矿物重彩、局部暖金光泽，右下角紧凑金色银联，不要芯片或卡号。

### 珠峰与洛子峰 · 银线

> 使用 card-creator Skill，生成珠峰与洛子峰主题卡面：灰蓝银白、疏朗清楚的等高线，标注珠峰与邻峰，保留 EBC 徒步终点示意和右下角 Visa；不作为导航图。

### 鱼尾峰 · MBC 徒步记忆

> 使用 card-creator Skill，生成鱼尾峰 MBC 徒步纪念卡：苔绿底、疏朗银白等高线，金线串起 Deurali、MBC、ABC，峰顶与营地分开标注，右下角线条 Mastercard；不作为导航图。

## 实际修改提示词

以下保留主要生成式修改的原文；最初文字成图及已退回版本不作为新作品重复发布。

### 文殊山水版

```text
Edit reference image 1 into an elegant, fresh, landscape-rich PORTRAIT thangka-inspired card. This is Nepal-made Tibetan-thangka inspiration, NOT Newari / Paubha styling; no dense architectural shrine, mandala lattice or ornate frame. Keep the single deity's identity, iconographic implements and pose from image 1, but reduce the whole figure and lotus to roughly three-quarters its former size. Build a genuinely spacious environment around the smaller central subject: softly layered Himalayan snowy ridges, malachite-green hills, an understated turquoise stream or pool, sparse delicate flowers and gently drifting pale cloud ribbons. The landscape occupies meaningful visible space above, beside and below the figure, not just a thin strip. Quiet sacred stillness, balanced breathing room.
Colour/material: opaque fine mineral-pigment painting on subtle cloth, luminous azurite blue, malachite green, pale turquoise, warm ivory and a few restrained vermilion accents. Fresh crystalline mineral colours rather than murky antique brown or bleached watery pastels. Fine human-drawn contour work, poised traditional two-dimensional painted form, NOT a photograph, 3D gold statue, anime or oil portrait. Selective warm 18K-gold-like metallic gleam on crown, jewelry, a slender halo rim and a few exquisitely thin painted details: subtle burnished foil reflections, not all-over glitter or a massive gold disc. The figure must remain clear and important; no added deities.
Image 2 is a whole Jiangsu transit card used ONLY for the small CHINA T-UNION / 交通联合 mark at its lower right. Ignore its Jiangsu name, city imagery, numbers and layout. Integrate ONE readable familiar T-Union mark in a calm lower-right corner of the new portrait, artistically redrawn in muted metallic gold and dark teal with comfortable inset. It is a discreet but legible non-official decorative interpretation, not an issued Tibet transit card. No other text, no invented Tibet brand, no bank logos.
Output finished upright portrait artwork about width:height 1:1.586, preferably 969 x 1536 if supported. Entire image opaque and edge-to-edge including four solid square corners. No outer frame, white border, rounded mask, mockup, device, shadow, chip, NFC or watermark. Never crop off crown, sword, hands or lotus.
Manjushri: preserve youthful peaceful golden face and TWO arms. Anatomical RIGHT hand (viewer LEFT) raises a flame-tipped wisdom sword; entire sword has sky breathing room above it. Anatomical LEFT hand (viewer RIGHT) holds the blue lotus stalk near the heart, lotus blossom at shoulder supporting a closed horizontal scripture manuscript, no letters. Seated cross-legged on lotus. A smaller soft turquoise nimbus with a gold rim, simplified graceful blue-green and coral silks. Surround with open pale-blue sky, distant ivory snow peaks, emerald hills and a quietly flowing river; airy spatial depth rendered entirely as flat mineral painting. Hands coherent, five digits, no extra arms. Preserve reverence without heavy brocade ornament.
```
### 黄财神山水版

```text
Edit reference image 1 into an elegant, fresh, landscape-rich PORTRAIT thangka-inspired card. This is Nepal-made Tibetan-thangka inspiration, NOT Newari / Paubha styling; no dense architectural shrine, mandala lattice or ornate frame. Keep the single deity's identity, iconographic implements and pose from image 1, but reduce the whole figure and lotus to roughly three-quarters its former size. Build a genuinely spacious environment around the smaller central subject: softly layered Himalayan snowy ridges, malachite-green hills, an understated turquoise stream or pool, sparse delicate flowers and gently drifting pale cloud ribbons. The landscape occupies meaningful visible space above, beside and below the figure, not just a thin strip. Quiet sacred stillness, balanced breathing room.
Colour/material: opaque fine mineral-pigment painting on subtle cloth, luminous azurite blue, malachite green, pale turquoise, warm ivory and a few restrained vermilion accents. Fresh crystalline mineral colours rather than murky antique brown or bleached watery pastels. Fine human-drawn contour work, poised traditional two-dimensional painted form, NOT a photograph, 3D gold statue, anime or oil portrait. Selective warm 18K-gold-like metallic gleam on crown, jewelry, a slender halo rim and a few exquisitely thin painted details: subtle burnished foil reflections, not all-over glitter or a massive gold disc. The figure must remain clear and important; no added deities.
Image 2 is a whole Jiangsu transit card used ONLY for the small CHINA T-UNION / 交通联合 mark at its lower right. Ignore its Jiangsu name, city imagery, numbers and layout. Integrate ONE readable familiar T-Union mark in a calm lower-right corner of the new portrait, artistically redrawn in muted metallic gold and dark teal with comfortable inset. It is a discreet but legible non-official decorative interpretation, not an issued Tibet transit card. No other text, no invented Tibet brand, no bank logos.
Output finished upright portrait artwork about width:height 1:1.586, preferably 969 x 1536 if supported. Entire image opaque and edge-to-edge including four solid square corners. No outer frame, white border, rounded mask, mockup, device, shadow, chip, NFC or watermark. Never crop off crown, sword, hands or lotus.
Yellow Jambhala: retain the mature substantial round-bellied golden yaksha, crown, small moustache and three eyes, TWO arms. Anatomical RIGHT hand (viewer LEFT) holds one citron fruit; anatomical LEFT hand (viewer RIGHT) holds the long-bodied mongoose with a modest stream of jewels from its mouth. Preserve royal-ease seated pose: his right leg (viewer LEFT) pendant on a small lotus footrest, other leg tucked. Keep all feet and pedestal comfortably in view. Benevolent firm protective expression rather than angry scowl. A restrained warm-ivory nimbus with a slender gold rim, clear jade/turquoise/red silk accents. Bright malachite foothills, a pale turquoise lotus pool, a little flowering foliage and distant clear ivory peaks surround the figure, leaving luminous sky above. A few jewels near the lotus, never heaps of gold coins or financial slogans. Hands coherent, five digits, no extra arms.
```

文殊／黄财神本轮山水图首次请求被输出审核拦截后，实际重试在上述提示中补充了完整衣饰与非色情宗教绘画要求；生成图保留传统披帛与部分上身，未完全执行全覆长袍要求。

### 黄财神换银联（发布版）

```text
Use case: precise-object-edit. Image 1 is the approved Yellow Jambhala mineral-pigment portrait card. Image 2 is the compact UnionPay logo shape reference only. CHANGE ONLY the lower-right transit mark: remove every part and text of China T-Union and replace it with the familiar compact UnionPay / 银联 mark from image 2, artistically drawn as warm 18K-gold lines and gold lettering against a deep jade field. Similar visual footprint and comfortable lower/right inset, harmonize with the existing fine gilding. Do not add any bank name, new text, numbers, chip or NFC. Preserve every other part: deity identity, face and three eyes, exact hands, citron, mongoose, pose, silks, lotus, gold halo, snowy peaks, sky, river, flowers, colour, scale and composition. Reverent non-sexual traditional religious illustration. Opaque upright portrait artwork, preserve original aspect ratio and full composition, no cropping, transparent corners, frame or mockup. Non-official artistic bank-card concept, no endorsement or real payment capability.
```

### 珠峰稀疏化

```text
Use case: precise-object-edit. Input image 1 is the existing Everest/Lhotse contour card to simplify. Keep its blue-grey colour family, north-up top-down terrain arrangement, Everest/Lhotse/Nuptse identity, existing text content, EBC hiking trace and white VISA in the lower right. The user finds the contour lines FAR too dense and illegible. Make a decisive cartographic generalization, not a mild cleanup: remove about four out of five contour levels, remove ALL tiny ridge hatching, zigzag microtexture, double-lines and wispy noise. Each main mountain should have only around 10–16 broadly spaced clean irregular nested contour paths. Keep branching ridges and saddles rather than generic concentric circles. Use smoothly simplified paths with generous visible blue-grey gaps, enough to remain individually distinct at a 400px-wide card preview. A few ivory index contours are clearly heavier, other retained lines thin but crisp; no fine noise between them. Flat solid matte slate-blue ground, no gradients, no faux-3D relief or paper noise. The image should breathe and be readable at a glance, never fill every gap with more lines.
Preserve the existing relative peak/camp positions and route meaning; use the prior map as approximate artistic geography, not survey data. Retain exactly these labels with comfortably sized dark-navy type on calm background: "EVEREST", "8848.86 m", "LHOTSE", "8516 m", "NUPTSE", "GORAK SHEP", "EBC". Keep the restrained warm-gold dotted trail from Gorak Shep to EBC on the west, ending at EBC, not a summit. Keep VISA the same visual size and corner, non-official artistic interpretation. Do not add a title, map legend, new route, or other words. Output only the finished full-bleed opaque rectangular landscape art, approximately 1.586:1, preferably 1536 x 969 if supported. All corners opaque. No card mockup, outer border, rounded mask, transparency, UI, watermark, chips or NFC. Generate the entire image with image generation.
```

### MBC 稀疏化

```text
Use case: precise-object-edit. Input image 1 is the existing MBC trekking card. Keep its muted moss-green palette, north-up terrain arrangement, exact existing labels, Deurali to MBC to ABC route, separately marked Machhapuchhre summit and lower-right line-only Mastercard double circles. The user says its contours are much too dense and unclear. Strongly simplify the contour drawing: remove about 80 percent of contour levels and ALL dotted stippling, fine hatching, micro-ridge noise and hairline tangles. Retain only around 10–16 broad smooth irregular contour paths on each major mountain mass, letting green negative space breathe between the curves. Preserve asymmetric branching ridges and the valley, not target-like concentric blobs. Sparse ivory contours with a few stronger index lines; clear spacing and contrast visible at 400px-wide preview. Flat uniform medium moss-green background, no 3D shaded terrain, grain or decorative shading.
The valley gold route must be readable immediately: retain the same delicate but clear line entering from the south at "DEURALI", passing "MBC" / "3700 m", then northwest to "ABC" / "4130 m". Existing ring markers remain. Preserve the separate southeast summit triangle and text "MACHHAPUCHHRE" / "6993 m"; route MUST NOT touch the summit. Type is comfortably readable and positioned in clear gaps, preserve spellings and elevation values. Keep the original lower-right small ivory outline Mastercard symbol, a non-official interpretation. Do not add text, extra peaks or icons. Geographic illustration only, no survey claims. Output only the finished full-bleed opaque rectangular landscape art, approximately 1.586:1, preferably 1536 x 969 if supported. All corners opaque. No card mockup, outer border, rounded mask, transparency, UI, watermark, chips or NFC. Generate the entire image with image generation.
```

### 两张等高线共同的一次修正

```text
Use case: precise-object-edit. Edit this sparse contour card. Keep its palette, all existing labels and numbers in the same positions, payment mark, gold trail, markers, landscape format and broad topographic arrangement unchanged. Make ONE correction to the white contour linework: remove the bright spiderweb/spoke-like branching ridge creases. Reconstruct them as clean, smooth, separately traceable topographic contour paths. A contour line must NEVER intersect, fork, join another line or taper into a spiderweb. Each curve either closes into an irregular nested loop around its summit or continues naturally off the image edge. Use broad smooth bends and generous clear gaps, not angular spokes or embossed bevels. Retain the low line density (around 10–16 contour levels around a main summit) and hierarchy of a few slightly stronger index contours. Do not replace the removed creases with extra fine detail. Flat minimalist cartography, sparse and legible; no 3D relief or shiny embossed outlines. Do not change any words, elevations, route, labels or logo, do not add any new content. Opaque flat edge-to-edge rectangular landscape PNG, same approximate 1.586:1 ratio; no border, rounding, mask, mockup, transparency or watermark. Non-official terrain-inspired artwork, not precise navigation.
```
