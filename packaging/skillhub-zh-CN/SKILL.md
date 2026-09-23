---
name: card-creator
slug: card-creator
displayName: 卡面生成器
version: 0.3.2
description: 用一句话或参考图生成 AirCard、银行卡、交通卡卡面。用图片生成工具完成整张图，Logo 图片只供参考，可随画面风格变化。
summary: 一句话生成完整卡面，参考图按需读取。
homepage: https://github.com/juju-w/card-creator-skill
license: MIT
metadata:
  version: 0.3.2
  author: JuJu
  tags:
    - image-generation
    - card-design
    - transit
  openclaw:
    emoji: "🎴"
    homepage: https://github.com/juju-w/card-creator-skill
---

# 卡面生成器

“鲤鱼王 × ICOCA，简洁，右下角 ICOCA”就够了。使用当前可用的图片生成工具，一次创作包含 Logo 的完整卡面。不得用代码绘制卡面，也不要先生成背景再贴 Logo。没有图片生成工具就说明情况，不用脚本替代。

1. 阅读简短的[卡面规则](references/card-rules.md)。提到 Logo 时，从[参考图索引](references/logo-reference-index.md)取对应图片交给图片生成工具，只取这张卡需要的图，优先使用用户附件。没有可用图片就依靠模型知识；仅在用户要求搜索或确实无法辨认时搜索。不为出图检查整个图库或追查来源历史。
2. 按用户的主题、风格、位置生成。Logo 可以配合画面变成烫金、单色、线稿。按卡面惯例选择标志（例如银联通常用短款），不要把所有品牌都强制缩成短款。让模型自己平衡 Logo 大小、留白与插画，不设固定位置框或大小上限。
3. 返回生成图片，检查主体和 Logo 是否可辨认、排版是否协调；明显错误再修正，不扩展成制作流水线。

钱包截图只参考卡面设计，不带上周围界面。默认不添加无关文字、号码、芯片、二维码、感应/NFC 标记。第三方标志属于非官方艺术诠释，不代表品牌授权或卡片具有实际功能。未经允许不公开用户私人参考图。
