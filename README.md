# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

一个为 AirCard、NFC 卡片和交通卡生成可打印卡面的 Codex Skill：AI 负责画面，Skill 负责尺寸、
裁切、排版、透明贴纸和 300 DPI 导出。仓库不包含在线编辑器。

## 先看作品：10 种卡面与一句话 Prompt

尺寸、出血、排版、圆角展示适配和导出规则都在 Skill 内部。复制一句话给 ChatGPT / Gemini
即可；有参考图时同时上传并写“参考图如上”。

| 清新水彩 · Chiikawa × Suica | 五迷应援 · 卜卜 × Mastercard |
|---|---|
| <img src="examples/chiikawa-suica.png" width="420" alt="Chiikawa × Suica 清新水彩卡面"> | <img src="examples/mayday-bubu-mastercard.png" width="420" alt="五月天卜卜五迷应援卡面"> |
| `使用 card-creator Skill，参考图如上，生成一张 Chiikawa × Suica 清新水彩卡面：春日四叶草草地，右下角 Suica。` | `使用 card-creator Skill，生成一张五月天五迷应援卡：卜卜 / MOJO CARROT 站在五束彩色舞台灯下，深蓝演唱会氛围，右下角 Mastercard。` |

| 梦幻鬼系 · 耿鬼 × PASMO | 浮世绘 · 鲤鱼王 × ICOCA |
|---|---|
| <img src="examples/gengar-pasmo.png" width="420" alt="梦幻紫色月夜耿鬼与 PASMO 卡面"> | <img src="examples/magikarp-icoca.png" width="420" alt="浮世绘巨浪鲤鱼王与 ICOCA 卡面"> |
| `使用 card-creator Skill，生成一张耿鬼 × PASMO 卡面：耿鬼悬浮在紫色月夜与云海中，梦幻俏皮，右下角 PASMO。` | `使用 card-creator Skill，生成一张鲤鱼王 × ICOCA 卡面：鲤鱼王跃出靛蓝巨浪，浮世绘与金箔质感，右下角 ICOCA。` |

| 高级艺术 · 维也纳分离派 × Diners Club | 后印象派 · 旋涡夜景 × Visa |
|---|---|
| <img src="examples/vienna-secession-diners.png" width="420" alt="维也纳分离派黑金人物与哑金 Diners Club 卡面"> | <img src="examples/post-impressionist-visa.png" width="420" alt="后印象派旋涡夜景与哑金 Visa 卡面"> |
| `使用 card-creator Skill，生成一张维也纳分离派高级艺术卡面：原创人物侧影、黑金马赛克与螺钿花卉，右下角哑金 Diners Club 短标。` | `使用 card-creator Skill，生成一张高级后印象派卡面：深钴蓝旋涡夜空、金色星光与柏树，右下角哑金 Visa。` |

| 北京水墨 · 一卡通 × 交通联合 | 极简线条 · Mastercard |
|---|---|
| <img src="examples/beijing-ink-transit-background.png" width="420" alt="北京水墨交通卡面"> | <img src="examples/minimal-mastercard.png" width="420" alt="极简线条 Mastercard 卡面"> |
| `使用 card-creator Skill，参考图如上，生成一张北京水墨交通卡面：天坛、长城、宣纸质感与风格匹配的北京交通标志。` | `使用 card-creator Skill，参考图如上，生成一张暖象牙白的极简线条 Mastercard 卡面，右下角红橙双色 Mastercard。` |

| 故宫典藏 · 云母祥云与仙鹤 | 上海装饰艺术 · 夜景 × 银联 |
|---|---|
| <img src="examples/palace-museum-cranes-unionpay.png" width="420" alt="云母祥云仙鹤与故宫主题卡面"> | <img src="examples/shanghai-art-deco-unionpay.png" width="420" alt="上海装饰艺术夜景与哑金银联卡面"> |
| `使用 card-creator Skill，参考图如上，生成一张故宫典藏风卡面：云母祥云、仙鹤、宫殿与哑金风格化标志。` | `使用 card-creator Skill，生成一张 1930 年代上海装饰艺术卡面：深翡翠外滩夜景与古金线条，右下角哑金短款银联。` |

其中北京水墨与故宫示例使用明确标注的非官方风格化标志；卜卜与宝可梦相关画面是非官方
AI 同人诠释；卡组织与交通标志只合成 manifest 中 `status: ready` 的精确透明贴纸。所有示例均为
个人、非商业创作演示，不代表品牌、角色、乐团、交通运营方或金融机构授权、合作或认可。

## 安装

使用 Vercel 开源 `skills` CLI：

```bash
npx skills add juju-w/card-creator-skill
```

或手动安装：

```bash
cp -R skills/card-creator ~/.codex/skills/
python3 -m pip install -r skills/card-creator/scripts/requirements.txt
```

SkillHub / WorkBuddy 简体中文版的源码与发布说明位于
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。审核上架后可运行：

```bash
skillhub install card-creator
```

## 使用

不需要把尺寸和排版规则重复写进 Prompt：

```text
使用 card-creator Skill，参考图如上，生成一张 [主题] 卡面，加入 [贴纸]，整体为 [风格]；不要添加感应支付标志和无关文字。
```

手机钱包截图也可以作为参考。Skill 只分析卡面区域，会忽略余额、币种、读卡提示、界面圆角、
阴影和水印，并把设计语言转化成新的构图，而不是复制原卡。完整规则见
[reference-remix.md](skills/card-creator/references/reference-remix.md)。

## 输出规格

- 裁切图：`1011 × 638 px`，300 DPI，对应 `85.60 × 53.98 mm`。
- 出血图：`1081 × 708 px`，四边各 `35 px`。
- `59 px` 蓝线仅是普通小字和功能信息的建议区域，不限制 Logo、插画和满版构图。
- 输出 `bleed`、`trim` 和 `guides` 三张 PNG；实体圆角或钱包展示圆角不烘焙进源图。
- 九宫格锚点支持多标志大集合；Skill 会按视觉重量复核层级与实体裁切边距。

尺寸与坐标的单一来源是 [card-rules.md](skills/card-creator/references/card-rules.md)。

## 素材与边界

- 可直接合成的 `ready` 素材包括 Visa、Mastercard、American Express、银联、JCB、Discover、
  Diners Club、RuPay、MIR，以及 Suica、PASMO、ICOCA 等日本交通 IC 标志。
- manifest 只保留仓库里实际存在的 `ready` 与 `reference-only` 文件，不再维护无法获取的空
  `blocked` 条目。缺失的城市交通、银行、钱包或支付标志会在用户请求时现场搜索、抠取 Alpha
  候选，或在明确风格化模式下由模型生成一次性的非官方诠释。详见
  [sticker-catalog.md](skills/card-creator/references/sticker-catalog.md)、
  [sticker-research.md](skills/card-creator/references/sticker-research.md) 和
  [manifest.json](skills/card-creator/assets/stickers/manifest.json)。
- 银联卡角默认选 `unionpay-compact`，Diners Club 默认按卡面惯例选紧凑标志；用户指定时可改用
  完整横版。Logo 可按构图占据角落或铺满画面，不会被蓝色建议线强制缩小。
- 感应支付标志默认不添加。EMVCo 四弧线版本需要相应许可，通用 Material 图标不能代替它。
- 仓库 MIT License 只覆盖原创代码与文档，不会重新授权第三方商标、角色、音乐或示例素材。

## 验证

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 skills/card-creator/scripts/validate_stickers.py
python3 -m unittest discover -s tests -v
```

核心入口：[SKILL.md](skills/card-creator/SKILL.md)
