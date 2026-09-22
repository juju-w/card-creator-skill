# card-creator-skill

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)

一个用一句话生成 AirCard、银行卡和交通卡卡面的 Skill。图片生成工具一次完成画面与标志；
参考图库帮助模型理解 Logo，也允许烫金、单色、线稿等风格变化。无需 Python，不含在线编辑器。

## 先看作品：10 种卡面与一句话 Prompt

在支持图片生成的 ChatGPT / Gemini 等工具中使用。安装或让模型读取本仓库的 Skill 后，
复制一句话即可；有参考图时同时上传并写“参考图如上”。

| 简洁角色卡 · 鲤鱼王 × ICOCA | 紫色科技感 · 耿鬼 × 八达通 |
|---|---|
| <img src="examples/gemini-magikarp-icoca.jpeg" width="420" alt="简洁鲤鱼王与 ICOCA 卡面"> | <img src="examples/gemini-gengar-octopus.jpeg" width="420" alt="紫色耿鬼与八达通卡面"> |
| `使用 card-creator Skill，生成一张鲤鱼王 × ICOCA 卡面：简洁，右下角 ICOCA。` | `使用 card-creator Skill，生成一张耿鬼 × 八达通卡面，让八达通 Logo 变成与画面匹配的紫色。` |

| 华山水墨 · 交通联合 | 广州极简线条 · 岭南通 × 交通联合 |
|---|---|
| <img src="examples/huashan-ink-tunion.png" width="420" alt="华山水墨与交通联合卡面"> | <img src="examples/guangzhou-minimal-lingnantong-tunion.png" width="420" alt="广州极简线条岭南通与交通联合卡面"> |
| `使用 card-creator Skill，生成一张华山水墨画风格的交通卡面，右下角交通联合。` | `使用 card-creator Skill，生成一张广州极简线条卡面，包含岭南通和交通联合。` |

| 高级艺术 · 维也纳分离派 × Diners Club | 后印象派 · 旋涡夜景 × Visa |
|---|---|
| <img src="examples/vienna-secession-diners.png" width="420" alt="维也纳分离派黑金人物与哑金 Diners Club 卡面"> | <img src="examples/post-impressionist-visa.png" width="420" alt="后印象派旋涡夜景与哑金 Visa 卡面"> |
| `使用 card-creator Skill，生成一张维也纳分离派风格的黑金高级艺术卡面，右下角哑金 Diners Club。` | `使用 card-creator Skill，生成一张深蓝旋涡夜空的后印象派卡面，右下角哑金 Visa。` |

| 清新水彩 · Chiikawa × Suica | 极简线条 · Mastercard |
|---|---|
| <img src="examples/chiikawa-suica.png" width="420" alt="Chiikawa × Suica 清新水彩卡面"> | <img src="examples/minimal-mastercard.png" width="420" alt="极简线条 Mastercard 卡面"> |
| `使用 card-creator Skill，生成一张清新水彩风 Chiikawa × Suica 卡面，右下角 Suica。` | `使用 card-creator Skill，生成一张暖象牙白的极简线条 Mastercard 卡面，右下角 Mastercard。` |

| 故宫典藏 · 云母祥云与仙鹤 | 上海装饰艺术 · 夜景 × 银联 |
|---|---|
| <img src="examples/palace-museum-cranes-unionpay.png" width="420" alt="云母祥云仙鹤与故宫主题卡面"> | <img src="examples/shanghai-art-deco-unionpay.png" width="420" alt="上海装饰艺术夜景与哑金银联卡面"> |
| `使用 card-creator Skill，生成一张故宫典藏风卡面，使用云母祥云、仙鹤、宫殿和哑金风格化标志。` | `使用 card-creator Skill，生成一张深翡翠与古金配色的上海装饰艺术卡面，右下角哑金短款银联。` |

鲤鱼王与耿鬼两张是用户提供并授权发布的 Gemini 成图原样展示，其中生成图内的 ICOCA、
JR-West 与紫色八达通标志均为非官方风格化诠释。华山、广州与故宫示例中的标志也是由 AI
结合参考图生成的非官方风格化版本。所有示例均为个人、非商业创作演示，不代表品牌、角色、交通
运营方或金融机构授权、合作或认可。图库示例保留各自的原始尺寸与比例。

## 安装

使用 Vercel 开源 `skills` CLI：

```bash
npx skills add juju-w/card-creator-skill
```

或手动安装：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

SkillHub / WorkBuddy 简体中文版的源码与发布说明位于
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。审核上架后可运行：

```bash
skillhub install card-creator
```

## 使用

默认且唯一的创作路径是图片生成：一次生成完整画面与风格化标志。不会用 SVG、HTML 或脚本画
卡面，也不会把任务拆成“先生成背景、再贴 Logo”。Prompt 只需要“主题 + 风格 + Logo/位置”：

```text
使用 card-creator Skill，生成一张鲤鱼王 × ICOCA 卡面：简洁，右下角 ICOCA。
```

PNG 只供模型参考，不是最后贴上去的图层。只读取本次需要的图，缺图时使用用户附件或模型知识。
钱包截图只参考卡面，忽略余额、读卡提示等界面元素。Logo 的大小、留白、配色由模型结合画面调整。

## 图片与参考

默认横向卡片比例，返回图片生成工具的原始成图，不自动裁切、不附加印刷导出流程。
简短规则见 [card-rules.md](skills/card-creator/references/card-rules.md)。

- 交通参考按地区整理：中国内地、香港、日本、美国、英国、德国、澳洲。Suica 与 ICOCA 等统一放在日本目录。
- 银行参考共 30 家：包含四大行及常见商业银行、香港常用银行，以及美国、英国、新加坡、德国和澳洲银行。
- [参考图索引](skills/card-creator/references/logo-reference-index.md)直接链接实际图片；
  [完整来源与署名](SOURCES.md)在仓库外层供维护查阅，不放入 Skill。
- 感应支付标志默认不添加。仓库 MIT License 不覆盖第三方标志、角色及示例素材。

## 免责声明

本项目仅为免费、非商业的收集分享与创作交流，不出售素材，不代表品牌授权或合作。
第三方内容权利归原权利人；非盈利不构成无侵权保证。权利人可联系移除或更正，
详见[使用与权利声明](DISCLAIMER.md)。

## 验证

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
```

核心入口：[SKILL.md](skills/card-creator/SKILL.md)
