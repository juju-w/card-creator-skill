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
画廊可按精选或最新发布浏览。打开作品，选择「网页直接使用／通过已安装的 Skill」，即可复制对应的提示词；原始 Prompt 也会保留。

| 艺术 · 旋涡夜景 | 艺术 · 新艺术花卉 |
|:---:|:---:|
| [<img src="examples/post-impressionist-visa.png" width="320" alt="深蓝旋涡夜景 Visa 卡面">](https://juju-w.github.io/card-creator-skill/) <br> `后印象派夜空 · 哑金 Visa` | [<img src="examples/mucha-art-nouveau-octopus.png" width="320" alt="花卉人物八达通卡面">](https://juju-w.github.io/card-creator-skill/) <br> `新艺术花卉人物 · 古铜八达通` |
| 宝可梦 · 超能系粉色 | 城市 · 大湾区海桥 |
| [<img src="examples/chatgpt-gardevoir-cmb-unionpay.png" width="320" alt="沙奈朵招商银行银联卡面">](https://juju-w.github.io/card-creator-skill/) <br> `沙奈朵 · 招商银行 × 银联` | [<img src="examples/greater-bay-sea-bridge-concept.png" width="320" alt="大湾区海桥概念卡面">](https://juju-w.github.io/card-creator-skill/) <br> `海桥晨光 · 大湾区通概念标志` |
| 玩梗 · 牛来 | 现代 · 蓝晶猫影 |
| [<img src="examples/niu-lai-amex-parody.png" width="320" alt="牛来运通风格玩梗卡面">](https://juju-w.github.io/card-creator-skill/) <br> `经典运通构图 · 牛来居中肖像` | [<img src="examples/hsbc-crystal-cat.png" width="320" alt="蓝色晶面猫咪汇丰风格卡面">](https://juju-w.github.io/card-creator-skill/) <br> `蓝色晶面 · 猫咪 × 汇丰` |

> 沙奈朵示例由用户从 ChatGPT 网页版分享，无法确认当时是否加载了本 Skill。大湾区通是虚构概念标志；品牌与角色画面均为非官方二创。来源见 [SOURCES.md](SOURCES.md)。

## 30 秒开始

### 网页直接使用

在 ChatGPT 等支持图片生成的界面选择**创建图像**，然后复制：

```text
请先读取并遵循 https://raw.githubusercontent.com/juju-w/card-creator-skill/main/web/card-creator.md ，然后用图片生成功能创作一张宝可梦沙奈朵的招商银行银联信用卡卡面：简洁，超能系粉色，不要芯片。
```

也可以去[画廊](https://juju-w.github.io/card-creator-skill/)选择作品，直接复制「网页直接使用」的提示词。单文件指南已经包含全部执行规则，不用逐个翻阅仓库。

链接**不等于安装 Skill**，也不保证当前模型读到了网页。读不到时，下载 [card-creator.md](https://juju-w.github.io/card-creator-skill/web/card-creator.md) 后上传到对话。`@创建图像` 不是通用 Prompt 语法，请以当前界面的工具入口为准。

### 安装 Skill

在支持 **Agent Skills** 和**图片生成／编辑**的客户端中安装。Skill 本身不包含生图模型。

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

想换题材，只需改一句话：`故宫云母仙鹤 × 银联`、`伦敦春日厚涂交通卡`。未指定标志时会自动搭配；想要纯插画就说「无标志」。默认不加卡号、芯片、二维码和感应支付标志。

### 上传参考图，或只改一点

在画廊点「参考这张创作」，下载图片并上传到绘图对话，再复制改图提示。已经生成过的图片可以直接继续说：

```text
只把八达通 Logo 改成紫色，角色和背景保持。
```

需要特定标志或角色版本时，附上对应参考图即可。复制文字不会自动附带图片；AI 局部编辑也不保证未修改区域逐像素一致。

## 它怎么工作

1. 理解主题与修改范围，未指定标志时按题材、卡片类型和地域搭配；只读取相关参考图。
2. 用宿主图片工具创作或编辑完整卡面，包括与画风协调的标志；不使用 SVG 绘画或脚本拼贴。
3. 检查主体、标志和意外透明白边。默认横版，也支持直接说「竖版卡面」；按方向重新构图，不旋转或裁切横图充当竖图。比例与推荐尺寸见[卡面规则](skills/card-creator/references/card-rules.md)，返回实际成图，不虚称尺寸、DPI 或出血文件。

参考库涵盖中国内地与海外交通卡、常见中外银行、支付组织及 Wise、Apple Cash 等金融科技标志。可从[图片索引](skills/card-creator/references/logo-reference-index.md)按需选用；[比例与构图规则](skills/card-creator/references/card-rules.md)保持简短。Logo 可随画面变成烫金、单色或线稿，但生成结果只是**非官方风格化诠释**，不是可用的真实银行卡或交通卡。

## 关于这个项目

Card Creator 免费、非商业，用于创作交流与参考分享，不出售卡面或素材，也不代表品牌授权。第三方标志、角色和作品的权利归原权利人；**非盈利与注明来源不自动等于获得许可**。仓库的 MIT License 不覆盖第三方内容。完整说明、来源和移除联系方法分别见 [DISCLAIMER.md](DISCLAIMER.md)、[SOURCES.md](SOURCES.md)。

<details>
<summary>手动安装与维护者校验</summary>

仓库根目录下手动安装到 Codex：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

SkillHub 中文分发包的维护说明在 [`packaging/skillhub-zh-CN`](packaging/skillhub-zh-CN/README.md)。中文包使用中文入口和共享执行规则，参考图片是远程链接；GitHub 安装包包含本地图片。网页指南也由同一源文件自动生成，请勿手改。提交前可运行：

```bash
python3 -m pip install -r requirements-dev.txt  # 仅维护端：检查图片实际透明度
python3 packaging/build_web_md.py --check
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/card-creator
python3 -m unittest discover -s tests -v
node --test tests/gallery-prompts.test.mjs
```

建议在虚拟环境中安装维护依赖；普通 Skill 用户不需要 Python 或 Node。真实生图验收用例见 [tests/skill-scenarios.md](tests/skill-scenarios.md)。

</details>
