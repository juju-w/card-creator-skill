<p align="center"><img src="brand/icon.png" width="88" alt="Card Creator 图标"></p>

<h1 align="center">Card Creator</h1>

<p align="center"><strong>一句话，把脑海里的卡面做出来。</strong><br>用图片生成创作 AirCard、银行卡和交通卡卡面的 Skill。<br>给它主题、风格和想要的标志，其余交给画面。</p>

<p align="center"><a href="https://juju-w.github.io/card-creator-skill/">逛卡面画廊</a> · <a href="#30-秒开始">开始使用</a> · <a href="README_EN.md">English</a></p>

<p align="center">
  <a href="https://skills.sh/juju-w/card-creator-skill"><img src="https://skills.sh/b/juju-w/card-creator-skill" alt="skills.sh"></a>
  <a href="https://github.com/juju-w/card-creator-skill/stargazers"><img src="https://img.shields.io/github/stars/juju-w/card-creator-skill?style=flat-square&logo=github" alt="GitHub Stars"></a>
  <a href="https://github.com/juju-w/card-creator-skill/forks"><img src="https://img.shields.io/github/forks/juju-w/card-creator-skill?style=flat-square&logo=github" alt="GitHub Forks"></a>
  <a href="https://aiagentslisting.com/mcp/card-creator-skill"><img src="https://aiagentslisting.com/card-creator-skill/badge.svg?claim=1080f8ea087cc1881566e4ed826f8708" alt="Card Creator Skill on AI Agents Listing"></a>
</p>

## 先看作品，再动手

每张卡都从一个很短的想法出发。点击图片可去[画廊](https://juju-w.github.io/card-creator-skill/)浏览、查看 Prompt 和下载原图。

| 艺术 · 旋涡夜景 | 艺术 · 新艺术花卉 |
|:---:|:---:|
| [<img src="examples/post-impressionist-visa.png" width="320" alt="深蓝旋涡夜景 Visa 卡面">](https://juju-w.github.io/card-creator-skill/) <br> `后印象派夜空 · 哑金 Visa` | [<img src="examples/mucha-art-nouveau-octopus.png" width="320" alt="花卉人物八达通卡面">](https://juju-w.github.io/card-creator-skill/) <br> `新艺术花卉人物 · 古铜八达通` |
| 宝可梦 · 超能系粉色 | 城市 · 大湾区海桥 |
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="320" alt="沙奈朵招商银行银联卡面">](https://juju-w.github.io/card-creator-skill/) <br> `沙奈朵 · 招商银行 × 银联` | [<img src="examples/greater-bay-sea-bridge-concept.png" width="320" alt="大湾区海桥概念卡面">](https://juju-w.github.io/card-creator-skill/) <br> `海桥晨光 · 大湾区通概念标志` |
| 玩梗 · 牛来 | 现代 · 蓝晶猫影 |
| [<img src="examples/niu-lai-amex-parody.png" width="320" alt="牛来运通风格玩梗卡面">](https://juju-w.github.io/card-creator-skill/) <br> `经典运通构图 · 牛来居中肖像` | [<img src="examples/hsbc-crystal-cat.png" width="320" alt="蓝色晶面猫咪汇丰风格卡面">](https://juju-w.github.io/card-creator-skill/) <br> `蓝色晶面 · 猫咪 × 汇丰` |

> 沙奈朵示例由用户从 ChatGPT 网页版分享，无法确认当时是否加载了本 Skill。大湾区通是虚构概念标志；品牌与角色画面均为非官方二创。来源见 [SOURCES.md](SOURCES.md)。

## 30 秒开始

在支持 **Agent Skills** 和**图片生成**的客户端中安装，然后直接描述你想要的卡。Skill 本身不包含生图模型。

```bash
npx skills add juju-w/card-creator-skill
```

腾讯 SkillHub 中文版也可安装：

```bash
skillhub install card-creator --namespace indiv-juju-w
```

安装并确认当前会话已识别 `card-creator` 后，试试：

```text
使用 card-creator Skill，生成一张宝可梦沙奈朵的招商银行银联信用卡卡面：简洁，超能系粉色，不要芯片。
```

想换题材，只需改一句话：`故宫云母仙鹤 × 银联`、`伦敦春日厚涂 × Oyster`，或上传你喜欢的卡面当构图参考。默认不加卡号、芯片、二维码和感应支付标志；有明确需要再说。

### 在 ChatGPT 等网页界面使用

先选择界面的**创建图像**功能，再复制这一句；[网页单文件指南](web/card-creator.md)已包含工作流与卡面规则，不需要逐个打开仓库文档：

```text
请先读取并遵循 https://raw.githubusercontent.com/juju-w/card-creator-skill/main/web/card-creator.md ，然后用图片生成功能创作一张宝可梦沙奈朵的招商银行银联信用卡卡面：简洁，超能系粉色，不要芯片。
```

贴链接**不等于安装 Skill**，也不保证当前模型真的读到了网页。若读不到，请直接上传 [card-creator.md](web/card-creator.md)；需要精确辨认特定标志时，再上传对应[参考图](skills/card-creator/references/logo-reference-index.md)。`@创建图像` 是部分界面的工具入口，不是通用 Prompt 语法。

## 它怎么工作

1. 读你的主题、风格和位置要求；有参考图时只取相关图片，不遍历整个图库。
2. 用图片生成工具**一次创作整张卡面**，包括与画风协调的标志；不拿 SVG、脚本或图层事后拼贴。
3. 检查主体是否清楚、布局是否顺眼。默认返回生成器原图，不虚称精确 DPI 或印刷出血文件。

参考库涵盖中国内地与海外交通卡、常见中外银行、支付组织及 Wise、Apple Cash 等金融科技标志。可从[图片索引](skills/card-creator/references/logo-reference-index.md)按需选用；[比例与构图规则](skills/card-creator/references/card-rules.md)保持简短。Logo 可随画面变成烫金、单色或线稿，但生成结果只是**非官方风格化诠释**，不是可用的真实银行卡或交通卡。

## 关于这个项目

Card Creator 免费、非商业，用于创作交流与参考分享，不出售卡面或素材，也不代表品牌授权。第三方标志、角色和作品的权利归原权利人；**非盈利与注明来源不自动等于获得许可**。仓库的 MIT License 不覆盖第三方内容。完整说明、来源和移除联系方法分别见 [DISCLAIMER.md](DISCLAIMER.md)、[SOURCES.md](SOURCES.md)。

<details>
<summary>手动安装与维护者校验</summary>

仓库根目录下手动安装到 Codex：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

SkillHub 中文分发包的维护说明在 [`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。网页指南由 Skill 工作流和卡面规则自动生成，请勿手改。提交前可运行：

```bash
python3 packaging/build_web_md.py --check
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
```

</details>
