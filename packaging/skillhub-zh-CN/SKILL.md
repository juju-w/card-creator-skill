---
name: card-creator
slug: card-creator
displayName: 卡面生成器
version: 0.1.8
description: 根据一句简短描述快速生成 AirCard、NFC 卡或交通卡卡面。默认一次生成画面与风格化标志；只有用户明确要求精确 Logo 时才读取并合成已核验透明贴纸。
summary: 用一句话快速生成卡面，需要精确 Logo 时再启用透明贴纸模式。
homepage: https://github.com/juju-w/card-creator-skill
license: MIT
metadata:
  version: 0.1.8
  author: JuJu
  tags:
    - image-generation
    - card-design
    - transit
    - print
  openclaw:
    emoji: "🎴"
    homepage: https://github.com/juju-w/card-creator-skill
---

# 卡面生成器

优先使用满足需求的最短路径。像“鲤鱼王 × ICOCA，简洁，右下角 ICOCA”这样的一句话已经足够；
不要把普通卡面生成变成素材研究任务。

## 选择模式

### 快速艺术模式（默认）

适用于普通卡面，以及“把八达通 Logo 变成紫色”一类风格匹配需求。

- 一次 ImageGen 调用同时生成画面和所需标志。
- 使用用户参考图或模型已有知识；不要联网搜索、读取贴纸清单、抠 Alpha 或比较不同 Logo 版本。
- 生成的支付、交通、银行与城市卡标志是一次性的非官方风格化诠释。交付时简短说明，绝不能
  加入 `ready` 精确贴纸包。
- 只有构图明显不可用时才做一次聚焦重试。风格化标志与官方几何不完全相同，不是自动研究或
  重做的理由。

### 精确贴纸模式（明确要求才启用）

只有用户说“精确”“官方”“原版”或明确要求使用本地透明 Logo/贴纸时使用。

- 读取[贴纸目录](references/sticker-catalog.md)和[清单](assets/stickers/manifest.json)，只合成
  `status: ready` 的素材。
- 缺少精确标志时直接报告。只有用户明确要求搜索、寻找、收集或抠图时，才读取
  [贴纸研究流程](references/sticker-research.md)并开展研究。
- 精确模式保持来源几何；用户要求变色或材质时，可使用 `foil-gold`、`monochrome` 或
  `outline` 的几何锁定处理。

## 快速流程

1. 默认只做一张卡面，直接使用用户的短描述；可安全推断的信息不要追问。
2. 生成包含主体、风格、标志与位置的平面横向画稿。不要出现手、设备、样机透视、水印、功能性
   卡号、二维码或条形码。除非用户要求，否则不加感应/NFC 标志。
3. 只检查关键结果：主体与标志是否出现、层级是否清楚、重要内容是否被意外裁切。不要强制执行
   第二轮美术指导。
4. 运行 `scripts/prepare_card.py` 输出确定性的 300 DPI 文件。满版画面用默认 `cover`；边缘已有
   Logo 或主体时用 `--fit-mode contain`。
5. 返回裁切图路径，并对生成的第三方标志做一句简短披露。

## 固定边界

- 尺寸与坐标以[卡面规则](references/card-rules.md)为准；脚本输出 `1011 × 638 px` 裁切图和
  `1081 × 708 px` 出血图。
- 用户私人图片默认只在本地处理，除非用户明确要求发布。
- 不得声称品牌准确性、授权、互通性、赞助或认可。
- 不得创建支付凭据，或足以冒充真实支付卡、门禁卡、交通卡、证件的设计。

## 仅在需要时读取参考文件

- 只有编写或调试 Prompt 时读取[Prompt 指南](references/prompt-guide.md)。
- 只有根据已有卡面、照片或钱包截图做变化时读取
  [参考卡面改造](references/reference-remix.md)。
- 只有精确贴纸模式才读取贴纸目录与清单。
- 只有用户明确要求素材搜索后才读取贴纸研究流程。
