# card-creator-skill

<img src="brand/icon.png" width="72" alt="Card Creator 图标">

[简体中文](README.md) | [English](README_EN.md)

[![skills.sh](https://skills.sh/b/juju-w/card-creator-skill)](https://skills.sh/juju-w/card-creator-skill)
[![GitHub Stars](https://img.shields.io/github/stars/juju-w/card-creator-skill?style=flat-square&logo=github)](https://github.com/juju-w/card-creator-skill/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/juju-w/card-creator-skill?style=flat-square&logo=github)](https://github.com/juju-w/card-creator-skill/forks)
[![Card Creator Skill on AI Agents Listing](https://aiagentslisting.com/card-creator-skill/badge.svg?claim=1080f8ea087cc1881566e4ed826f8708)](https://aiagentslisting.com/mcp/card-creator-skill)

一个用一句话生成 AirCard、银行卡和交通卡卡面的 Skill。图片生成工具一次完成画面与标志；
参考图库帮助模型理解 Logo，也允许烫金、单色、线稿等风格变化。无需 Python，不含在线编辑器。

## 先看作品

[打开卡面画廊：按艺术风格、宝可梦、城市、二次元、玩梗等系列浏览与下载](https://juju-w.github.io/card-creator-skill/)。每张作品只归入一个主系列；画廊保存短 Prompt、来源说明与原始文件，新作品主要在那里更新。

| 梵高风格旋涡夜景 × Visa | 新艺术人物 × 八达通 |
|---|---|
| [<img src="examples/post-impressionist-visa.png" width="420" alt="梵高风格的深蓝旋涡夜景 Visa 卡面">](https://juju-w.github.io/card-creator-skill/) | [<img src="examples/mucha-art-nouveau-octopus.png" width="420" alt="左侧人物肖像的新艺术八达通卡面">](https://juju-w.github.io/card-creator-skill/) |

| 沙奈朵 × 招商银行／银联 | 大湾区海桥 × 大湾区通概念标志 |
|---|---|
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="420" alt="粉色沙奈朵卡面">](https://juju-w.github.io/card-creator-skill/) | [<img src="examples/greater-bay-sea-bridge-concept.png" width="420" alt="海桥与大湾区通概念标志卡面">](https://juju-w.github.io/card-creator-skill/) |

| 牛来 × American Express | 蓝晶猫 × 汇丰 |
|---|---|
| [<img src="examples/niu-lai-amex-parody.png" width="420" alt="牛来替代经典运通肖像的玩梗卡面">](https://juju-w.github.io/card-creator-skill/) | [<img src="examples/hsbc-crystal-cat.png" width="420" alt="深蓝色水晶折面猫咪汇丰卡面">](https://juju-w.github.io/card-creator-skill/) |

沙奈朵与巨金怪图由用户从 ChatGPT 网页版分享，**无法确认当时是否加载了 Skill**。大湾区通是虚构概念标志，牛来和品牌标志都是非官方二创；图片来源见 [SOURCES.md](SOURCES.md)，权利说明见 [DISCLAIMER.md](DISCLAIMER.md)。

## 使用方式

### 已安装 Skill：Codex 或兼容应用

应用需要同时支持 **Skill 加载**和**图片生成**。本仓库提供创作说明和参考图片，不自带生图模型；
仅仅是本地 App 或安装成功，并不代表当前会话能生图。没有图片生成工具时，不应用代码画图替代。

在支持 Agent Skills 的客户端中，使用 Vercel 开源 `skills` CLI 安装并选择对应客户端：

```bash
npx skills add juju-w/card-creator-skill
```

或下载本仓库后，在仓库根目录手动安装到 Codex：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

腾讯 SkillHub 简体中文版的源码与发布说明位于
[`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。安装已发布的版本：

```bash
skillhub install card-creator --namespace indiv-juju-w
```

确认客户端已识别 `card-creator` 后，直接使用短 Prompt：

```text
使用 card-creator Skill，生成一张宝可梦沙奈朵的招商银行银联信用卡卡面：简洁，超能系粉色，不要芯片。
```

### 网页版：链接与参考图

**在聊天框贴 GitHub 链接，不等于安装了 Skill，也不保证模型读到了说明和 PNG。**
未通过平台 Skill 入口安装时，把仓库当作参考资料使用。是否能访问链接、读取图片，以当前会话实际能力为准。

先在界面中选择图片生成功能，再发送下面这句。你的界面如果显示 `@创建图像`，选择该工具即可；
它不是需要在所有平台照抄的文字命令。ChatGPT 的图片入口见[官方说明](https://help.openai.com/en/articles/11084440)。

```text
参考 https://github.com/juju-w/card-creator-skill 中的 card-creator 说明，用图片生成功能生成一张宝可梦沙奈朵的招商银行银联信用卡卡面：简洁，超能系粉色，不要芯片。
```

读不到仓库时，直接粘贴 [SKILL.md](skills/card-creator/SKILL.md) 与简短的
[卡面规则](skills/card-creator/references/card-rules.md)，并上传需要的 Logo／角色参考图即可，不用让模型遍历仓库。
例如本例可上传[招商银行](skills/card-creator/assets/logo-references/banks/china/cmb.png)和
[短款银联](skills/card-creator/assets/logo-references/payment/unionpay-compact.png)，在 Prompt 后加“参考图如上”。

如果你的平台／工作区已经提供 Skill 安装入口，安装后按上一节使用；并非只有本地应用才能加载 Skill。
ChatGPT 的相关能力以[官方 Skill 说明](https://openai.com/academy/skills/)及账户实际入口为准。

两种用法都让图片生成工具完成整张卡面，PNG 只供参考，不用脚本绘制或事后拼贴 Logo。

## 图片与参考

默认横向卡片比例，返回图片生成工具的原始成图，不自动裁切、不附加印刷导出流程。
简短规则见 [card-rules.md](skills/card-creator/references/card-rules.md)。

- 交通参考按地区整理：中国内地、香港、日本、台湾、韩国、新加坡、美国、加拿大、英国、法国、意大利、德国、澳洲。Suica 与 ICOCA 等统一放在日本目录。
- 银行参考共 30 家：包含四大行及常见商业银行、香港常用银行，以及美国、英国、新加坡、德国和澳洲银行。
- 数字钱包与金融科技：Wise、Bybit、Apple Cash、X Money，包含品牌字标／符号及 X Card 官网卡面参考。不局限于动漫角色，也可做纯排版、抽象、城市或材质主题。
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
