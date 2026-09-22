# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

一个用于生成 AirCard、NFC 卡片和交通卡卡面的 Codex Skill。仓库当前只维护三类内容：

- 标准卡面尺寸、出血区和安全区规则。
- 有来源记录的透明交通/支付贴纸素材。
- 将 AI 背景图裁切、缩放并叠加贴纸的确定性脚本。
- 用户明确选择时，把可追溯 Logo 参考融入烫金、单色、线稿等非官方风格化卡面。

它不包含在线编辑器。默认使用准确贴纸；只有用户明确要求风格匹配时，才让图像模型参考 Logo
做艺术化诠释，并明确标注为非官方版本。

## 安装

推荐使用 Vercel 的开源 `skills` CLI，从 GitHub 安装国际版：

```bash
npx skills add juju-w/card-creator-skill
```

也可以手动把技能目录复制到 Codex skills 目录：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

脚本依赖：

```bash
python3 -m pip install -r skills/card-creator/scripts/requirements.txt
```

常规裁切和 PNG 贴纸合成只依赖 Pillow。只有维护者需要从 SVG 重新生成透明 PNG 衍生文件时，
才安装 `requirements-render.txt` 以及系统原生 Cairo 库。

之后可以这样调用：

```text
Use $card-creator to create a quiet Guangzhou morning card face,
reserve the upper-right for the China T-Union sticker, and export print-ready PNGs.
```

SkillHub/WorkBuddy 使用维护中的简体中文分发包。可复现源码、构建和发布命令位于
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。GitHub/skills.sh 默认包保持英文，
两个版本共享同一套脚本、卡面规则和素材清单，不会各自维护一份易漂移的资产库。

SkillHub 中文版审核上架后可直接安装：

```bash
skillhub install card-creator
```

## 输出规格

- 成品裁切尺寸：`1011 × 638 px`，300 DPI，对应 `85.60 × 53.98 mm`。
- 含出血尺寸：`1081 × 708 px`，四边各 `35 px` 出血。
- 重要内容安全边距：裁切线内缩 `59 px`。
- 输出包含 `bleed`、`trim` 和 `guides` 三张 PNG。

## 直接在 ChatGPT / Gemini 网页版使用

把参考图上传到当前对话后，复制下面这段，把方括号内容换成你的主题和贴纸名称。即使模型无法
访问 GitHub，Prompt 里也包含了关键尺寸和边界：

```text
请参考 https://github.com/juju-w/card-creator-skill 的卡面规范，并结合我在当前对话上传的参考图（参考图如上），为我生成一张 [主题] 卡面。

画面要求：横向平面画稿，宽高比 1.58577:1，最终裁切规格为 1011 × 638 px、300 DPI；背景铺满整个画布，所有人物、建筑和其他重要元素都留在中央安全区，四周保留充足裁切空间。只输出卡面正视图，不要生成手持效果、实体卡样机、透视、圆角遮罩、边框或阴影。不要生成卡号、二维码、条形码、水印或无关文字。

贴纸要求：为 [贴纸名称] 在 [位置] 留出干净空间。如果我同时上传了对应透明 PNG，请把它作为不可变贴纸使用，保持原始比例、颜色和透明度，不要让 AI 重画、改字或近似 Logo；如果没有收到可验证贴纸，就只保留空位并告诉我缺少素材。

请先生成一张完整卡面预览，并同时给出你实际使用的最终 Prompt。不要添加我没有要求的文字。
```

### 根据现有卡面做风格化变化

参考图是手机钱包截图也没关系，Skill 会把卡面和余额、读卡提示等界面元素分开。下面这段适合
“保留设计气质，但不要照抄原卡”的需求：

```text
请遵循 https://github.com/juju-w/card-creator-skill 的卡面规则，并参考我在当前对话上传的图片（参考图如上）。参考图可能是手机钱包截图：请只分析卡面区域，忽略余额、币种、读卡提示、应用界面、样机圆角、阴影和水印。

不要照抄原卡。请先提取它的设计语法，包括配色关系、留白、构图区、线条粗细、纹样密度和整体气质，再用这些关系创作一个明显不同的 [目标主题] 风格化版本。可以借鉴“角色服装吸收品牌色”“传统纹样转译成新线稿”“大面积留白配一个小型叙事场景”等方法，但不要复制参考图里的专有插画。

输出横向平面卡面，宽高比 1.58577:1，目标裁切尺寸 1011 × 638 px、300 DPI，所有重要内容位于中央安全区。不要复制卡号、掩码数字、姓名、芯片、余额、二维码、条形码、发卡方文字或不可用 Logo。

为 [所需贴纸] 预留干净位置；如果我上传了已验证的透明贴纸，请保持比例、颜色、文字和透明度，把它作为不可变图层使用，否则保持空位。只输出卡面画稿，不要手、设备、样机、透视、圆角遮罩、边框或阴影。请生成一张完整预览，并附上最终使用的 Prompt。
```

完整判定规则见 [reference-remix.md](skills/card-creator/references/reference-remix.md)。

## 卡面示例与 Prompt

默认精确模式中，ImageGen 只负责背景，`card-creator` 再叠加 `status: ready` 的透明贴纸；
用户明确选择风格化模式时，ImageGen 可以参考可追溯 Logo 做非官方材质化诠释。下面的预览限制
为 `600 px` 宽，仓库仍保留完整
`1011 × 638 px` 裁切图。第 1、3 张使用 `ready` 透明贴纸精确合成；第 2、4 张是用户明确选择的
非官方风格化诠释。非接触感应标志不会默认加入任何示例。

### 1. Chiikawa × Suica

<p align="center">
  <img src="examples/chiikawa-suica.png" width="600" alt="非官方 Chiikawa × Suica 卡面示例">
</p>

贴纸：`suica`（`ready`）。非官方、非商业同人示例；不代表角色或交通卡权利方授权、合作或认可。

直接复制给 ChatGPT / Gemini（先上传你喜欢的构图参考图；需要精确 Suica 标志时，同时上传仓库中的
`suica.png`）：

```text
请参考 https://github.com/juju-w/card-creator-skill 的尺寸与安全区规则，并结合我在当前对话上传的参考图（参考图如上），生成一张清新可爱的 Chiikawa × Suica 非官方个人同人卡面。画面是春日浅绿色草地、淡蓝天空、圆润白云和柔和水彩水粉质感；Chiikawa 单独坐在画面偏左位置，表情开心，手里拿着四叶草。右下角留出干净空间。

输出横向平面画稿，宽高比 1.58577:1，目标裁切尺寸 1011 × 638 px、300 DPI。背景必须铺满画布，人物和重要细节避免非预期裁切；蓝色安全线只是小字和功能信息参考。不要生成卡片样机、手、透视、圆角遮罩、边框、阴影、卡号、二维码、条形码、水印或无关文字。

如果我上传了 Suica 透明 PNG，请把它原样放在右下自然卡角位置，保持比例、颜色和透明度，不要重画、改字或风格化；由 Skill 自动检查它与角色的视觉重量和实体裁切边距。如果没有收到贴纸文件，就只保留空位，不要生成近似 Suica Logo。请直接生成一张完整卡面预览，并附上最终使用的 Prompt。
```

<details>
<summary>高级：查看背景层原始 Prompt</summary>

```text
Use case: illustration-story
Asset type: print-ready transit card background artwork
Primary request: Create a fresh, cute Chiikawa-themed card-face illustration featuring Chiikawa alone, with a gentle happy expression, sitting in a tiny spring meadow with a few small clover leaves and soft rounded clouds.
Scene/backdrop: airy pale mint-green meadow fading into a clear powder-blue sky, subtle watercolor-and-gouache texture, very clean and uncluttered.
Subject: one recognizable Chiikawa character, full body visible, placed slightly left of center and comfortably inside the central safe area.
Style/medium: polished kawaii Japanese character illustration, soft hand-painted watercolor and gouache, simple rounded shapes, delicate texture, crisp clean edges.
Composition/framing: flat edge-to-edge landscape artwork, 1.58577:1 composition; important content centered within a generous safe area; leave calm clean negative space in the lower-right for a later transparent Suica transit sticker; background extends fully to every edge.
Lighting/mood: bright soft morning light, fresh, calm, cheerful, adorable.
Color palette: pale mint, soft grass green, powder blue, cream white, tiny touches of warm peach.
Text: none.
Constraints: background artwork only; no logo, no brand mark, no Suica text, no Japanese text, no lettering, no card number, no QR code, no barcode, no watermark; no extra characters; no card mockup, no hand, no perspective, no border, no rounded-corner mask, no shadow; keep the lower-right negative space free of important elements.
```

</details>

### 2. 北京水墨 × 市政交通一卡通 × 交通联合

<p align="center">
  <img src="examples/beijing-ink-transit-background.png" width="600" alt="北京水墨交通卡背景示例">
</p>

这张图使用显式风格化模式：左上保留市政交通一卡通常见的正常组合标，右下使用交通联合卡角
标志，并把两者转成与宣纸水墨一致的矿物蓝、朱砂与晕染边缘。它们仍分别是 `reference-only`
和 `blocked`，因此这是标注清楚的非官方艺术化诠释，不会进入精确 `ready` 贴纸包。

直接复制给 ChatGPT / Gemini（上传可追溯的“市政交通一卡通”和“交通联合”卡面参考）：

```text
请参考 https://github.com/juju-w/card-creator-skill 的尺寸与构图规则，并结合我在当前对话上传的参考图（参考图如上），生成一张北京主题的现代水墨交通卡卡面。用暖象牙色宣纸铺满画布，左侧绘制天坛，远处是薄雾中的长城和山势，整体留白克制、安静、有现代编辑感。

输出横向平面画稿，宽高比 1.58577:1，目标裁切尺寸 1011 × 638 px、300 DPI。建筑和水墨可以自然出边，但不得非预期裁断天坛主体。不要生成卡片样机、手、透视、圆角遮罩、边框、阴影、卡号、二维码、条形码、水印或无关文字。

根据参考卡面，把市政交通一卡通常见的图形＋名称组合放在左上，把紧凑交通联合标志放在右下；两者都转换成与水墨画统一的矿物蓝、少量朱砂和晕染纸纹，并标注为非官方风格化诠释。由 Skill 自动复核两个标志的视觉重量和光学边距，不加入感应支付标志。如果缺少任一参考，就保留该位置，不要凭空补画。请直接生成一张完整卡面预览，并附上最终使用的 Prompt。
```

<details>
<summary>高级：查看背景层原始 Prompt</summary>

```text
Use case: stylized-concept
Asset type: print-ready transit card background artwork
Primary request: Create a refined Beijing-themed Chinese ink-wash card-face background, calm, contemporary, and fully printable edge to edge.
Scene/backdrop: the entire rectangular canvas is filled with warm ivory rice paper; misty layered ink landscape with a restrained Temple of Heaven and a distant Great Wall, broad atmospheric blank paper on the right.
Subject: one complete Temple of Heaven painted in elegant black and gray ink wash, scaled modestly and placed in the left third with at least 12% clear paper margin from the left and bottom edges so the entire building and roof remain visible; the Great Wall runs softly through the middle distance; no people.
Style/medium: traditional Chinese shui-mo ink painting with modern editorial restraint, visible dry-brush texture, soft ink diffusion, subtle handmade paper grain.
Composition/framing: flat edge-to-edge landscape artwork, 1.58577:1 composition; keep the complete Temple of Heaven and all important landmarks inside a generous central safe area; reserve two calm clean warm-white negative-space zones along the right side for later transparent China T-Union and Beijing transit stickers; rice-paper background reaches every canvas edge.
Lighting/mood: quiet early morning mist, dignified, spacious, poetic.
Color palette: warm rice-paper ivory, charcoal black, soft gray, one small muted cinnabar sun.
Text: none.
Constraints: opaque rectangular background artwork only; no cropped architecture, no black voids, no transparent areas, no circular ink frame, no vignette, no heavy border; no logo, no brand mark, no transit symbol, no Chinese characters, no lettering, no card number, no QR code, no barcode, no watermark; no card mockup, no hand, no perspective, no rounded-corner mask, no shadow; keep both right-side reserved zones free of important elements.
```

</details>

### 3. 极简线条 × Mastercard

<p align="center">
  <img src="examples/minimal-mastercard.png" width="600" alt="极简线条 Mastercard 卡面示例">
</p>

贴纸：红橙双色 `mastercard`（`ready`）。ImageGen 返回透明底时，只将背景修正为不透明暖象牙白；
Mastercard 双圆标志仍由 Skill 使用已核验 PNG 叠加，不让模型重画。

直接复制给 ChatGPT / Gemini（需要精确标志时，同时上传仓库中的 `mastercard.png`）：

```text
请参考 https://github.com/juju-w/card-creator-skill 的尺寸与安全区规则，并结合我在当前对话上传的参考图（参考图如上），生成一张极简线条风格的 Mastercard 卡面。背景为不透明暖象牙白，使用极少量的炭黑、珊瑚红和琥珀橙单线条形成抽象弧线，构图安静、现代、克制，右下角留出干净空间。

输出横向平面画稿，宽高比 1.58577:1，目标裁切尺寸 1011 × 638 px、300 DPI。背景铺满画布，重要线条交点位于中央安全区。不要生成芯片、卡号、二维码、条形码、水印、无关文字、卡片样机、手、透视、圆角遮罩、边框或阴影，也不要用背景圆形近似 Mastercard 标志。

如果我上传了 Mastercard 透明 PNG，请保持其红橙配色、比例和透明度，将它原样放在右下自然卡角位置，不要重画、改色或风格化；由 Skill 自动检查它与抽象线条的视觉重量和实体裁切边距。如果没有收到贴纸文件，就只保留空位。请直接生成一张完整卡面预览，并附上最终使用的 Prompt。
```

<details>
<summary>高级：查看背景层原始 Prompt</summary>

```text
Use case: stylized-concept
Asset type: print-ready payment card background artwork
Primary request: Create an elegant ultra-minimal line-art card-face background designed to pair with a later full-color Mastercard symbol.
Scene/backdrop: smooth warm ivory field with a few precise continuous lines forming two large overlapping circular arcs and a subtle flowing path, abstract rather than illustrative.
Style/medium: premium Swiss-influenced minimal graphic design, crisp monoline geometry, restrained editorial composition, flat matte print finish.
Composition/framing: flat edge-to-edge landscape artwork, 1.58577:1 composition; thin lines sweep from the upper-left toward the center and dissolve gently; leave calm clean negative space in the lower-right for the later transparent Mastercard symbol; all important line intersections remain inside a generous safe area.
Lighting/mood: quiet, confident, modern, refined.
Color palette: warm ivory background, hairline charcoal, muted coral red, soft amber orange; very limited palette.
Materials/textures: almost flat, with only an extremely subtle uncoated-paper grain.
Text: none.
Constraints: background artwork only; no logo, no brand mark, no circles that exactly reproduce the Mastercard logo, no lettering, no card number, no chip, no QR code, no barcode, no watermark; no card mockup, no hand, no perspective, no border, no rounded-corner mask, no shadow; keep the lower-right sticker zone empty and clean.
```

</details>

### 4. 云母祥云仙鹤 × 中国银行 × 故宫博物院 × 银联

<p align="center">
  <img src="examples/palace-museum-cranes-unionpay.png" width="600" alt="云母祥云仙鹤与中国银行、故宫博物院和银联风格化标志卡面示例">
</p>

标记：左上使用中国银行正常行徽＋名称组合，右上使用故宫博物院正常院徽组合，右下使用卡角
惯例中的 `unionpay-compact`。三个标志均为哑金风格化版本；Skill 按类别与参考卡面的惯例选择
版本，而不是全局强制短款。
这组示例专门验证“大标志构图”：Logo 可以占据角落的大部分空间并跨过蓝色建议安全线，不会
因为安全线被强制缩小；只需避免非预期裁断。它们是基于可追溯参考制作的非官方艺术化诠释，
不是品牌规范母版，也不默认加入感应标志。

多标志卡面会自动触发 Skill 的美术指导复核，由 Skill 统一处理视觉重量、光学边距和主次层级；
用户不需要在 Prompt 里另外要求“优化排版”。

直接复制给 ChatGPT / Gemini（上传短款 `unionpay-compact.png`、中国银行官方标志参考和故宫
博物院院徽参考）：

```text
请参考 https://github.com/juju-w/card-creator-skill 的尺寸与构图规则，生成一张故宫博物院典藏气质的原创中式卡面。画面使用暖白宣纸、半透明云母质感祥云、三只展翅的丹顶鹤和位于下方的宫殿建筑；整体轻盈但具有大构图张力，配色以珍珠白、古金、朱砂红、炭黑和少量黛绿为主。不要为了蓝色建议安全线缩小仙鹤、宫殿或 Logo；安全线只用于普通小字和功能信息参考。

输出横向平面画稿，宽高比 1.58577:1，目标裁切尺寸 1011 × 638 px、300 DPI，背景必须不透明并铺满四边。装饰性祥云、建筑和仙鹤可以按构图出边。不要生成卡片样机、手、手机界面、透视、圆角遮罩、晕影、边框、阴影、芯片、卡号、二维码、条形码、水印或感应标志。

加入中国银行、故宫博物院与银联三个参考标志，并遵循 card-creator Skill 的惯例版本选择和自动排版规则。三个标志统一使用哑金烫金与细微云母质感。它们均为非官方风格化诠释；银联使用卡角短款，不要加入 ICBC 或感应标志。如果缺少任一参考，就保留该位置，不要凭空补画。请生成一张完整卡面预览，并附上最终使用的 Prompt。
```

参考来源：[中国银行官方标志说明](https://www.boc.cn/aboutboc/bi1/201110/t20111014_1556052.html)；
[故宫博物院院徽启用说明](https://www.dpm.org.cn/classify_detail/158858.html)。

## 贴纸状态

当前已准备透明 SVG 与 PNG：

- 支付卡组织/网络：Visa、红橙双色 Mastercard、American Express、UnionPay、JCB、Discover、Diners Club、RuPay、MIR。银联默认使用 `unionpay-compact`，Diners Club 默认使用 `diners-club-symbol`；完整横版只在用户明确指定时使用。
- 日本全国交通 IC 互通体系：Suica、PASMO、ICOCA、TOICA、manaca、SUGOCA、nimoca、Hayakaken、PiTaPa。

Kitaca 的可追溯 SVG 带有不透明米色底，已保留为 `reference-only`；不会手工去底或让 Skill 调用。

卡面右侧常见的“四道雷达波”准确名称是 EMVCo `Contactless Indicator`。它与支付终端上的
`Contactless Symbol` 不是同一个图形。EMVCo 要求先签署书面商标许可，并在签约后才提供官方
文件，因此精确四弧线版本在 manifest 中明确标为 `blocked`。原先的圆形 Google Material 图标
视觉并不相同，已从 `ready` 退役为 `reference-only`。除非用户明确要求，Skill 不提供任何感应标志。

交通联合与北京、上海、天津、广州、深圳、杭州、南京、成都、重庆、武汉、西安等城市交通卡标志，以及岭南通、香港八达通、澳门通，已经进入素材清单并记录运营方或官方信息来源。北京、深圳、杭州、西安、天津、成都、重庆官网提供的 7 份透明 PNG 原件，以及羊城通、岭南通官网合作方提供的 2 份不透明 PNG 原件，已收入 `research/cities/`，并记录原始 URL、透明状态、用途差异和 SHA-256；它们仍是研究样本，而不是可调用贴纸。上海、武汉目前只找到官网的不透明页面横幅，清单只记录地址，不会手工抠图。

岭南通官网网充平台另有公开的“品牌素材下载”，但压缩包里是三张门店标牌 JPG，没有独立透明或矢量 Logo。其页面、压缩包地址和内容检查结果均已写入 manifest。

这些城市条目已不再使用模糊的 `pending`：保留了准确来源样本但不适合作贴纸的标为
`reference-only`；缺少准确透明素材或所需许可的标为 `blocked`。Skill 不会使用近似图替代，
也不会把运营方 Logo 冒充具体卡产品标志。八达通官网虽然提供 AI/JPG 压缩包，但品牌指引明确
要求书面认可，因此保持 `blocked`。

梗图中常见的 Maestro、Cirrus、PLUS、V Pay、Interac、Bancontact、CB、BC Card、Apple Pay、e-CNY、非接触标志、EZ-Link、T-money 等已整理进 [sticker-catalog.md](skills/card-creator/references/sticker-catalog.md) 的研究队列；它们还不是可调用素材。

银行发行方已经单独建档，不再和 Visa、Mastercard、银联等支付网络混在一起。首批覆盖工商银行、
农业银行、中国银行、建设银行、交通银行、邮储、招商、中信、光大、民生、兴业、浦发、平安、
广发，以及香港和国际常见的中银香港、汇丰、渣打、恒生、东亚、大新、招商永隆、星展、华侨、
大华和花旗。完整名称、地区与官方来源见
[bank-issuer-catalog.md](skills/card-creator/references/bank-issuer-catalog.md)。这些银行条目目前全部为
`blocked`：精确模式只能为指定组合标识预留位置，不能调用或用另一个地区版本代替；用户明确
选择风格化模式时，可以从可追溯参考生成标注为非官方的艺术化版本，但不会进入 `ready` 贴纸包。

完整来源、许可备注和状态见 [manifest.json](skills/card-creator/assets/stickers/manifest.json)。品牌与商标仍可能受各司法辖区的商标规则约束；本项目不代表相关机构授权或合作。

如果官方透明素材确实找不到，可以把官方卡面或用户提供的卡面作为最后一级研究来源：AI 只生成
蒙版并移除背景，不能补画、改色或重构 Logo。权利条件未确认的原图和候选保存在本地
`output/research-cache/`，不上传公共图床、不进入自动合成；完整流程见
[sticker-research.md](skills/card-creator/references/sticker-research.md)。这段规则针对“精确贴纸入库”；
用户明确选择的一次性非官方风格化卡面不进入 manifest，按独立风格化流程处理。

仓库根目录的 MIT License 只覆盖本项目原创代码与文档，不会把第三方标志、角色形象或示例中的第三方元素重新授权为 MIT；每个贴纸仍按 manifest 中记录的来源、许可说明和商标限制处理。

## 验证

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/card-creator

python3 skills/card-creator/scripts/render_stickers.py
python3 skills/card-creator/scripts/validate_stickers.py
```

`render_stickers.py` 是素材维护命令，需要 `requirements-render.txt`；普通卡面生成不需要它。

核心入口：[SKILL.md](skills/card-creator/SKILL.md)
