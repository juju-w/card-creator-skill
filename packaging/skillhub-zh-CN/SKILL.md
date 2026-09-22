---
name: card-creator
slug: card-creator
displayName: 卡面生成器
version: 0.1.2
description: 根据用户描述生成可印刷的 AirCard、NFC 卡或交通卡卡面。严格执行标准比例、出血区和安全区规则；图像模型只生成背景，支付与交通标志只从有来源记录且状态为 ready 的透明贴纸包中叠加。适合制作新卡面、修改卡面风格和导出印刷 PNG，不用于伪造功能卡或让 AI 重画品牌 Logo。
summary: 用 AI 画背景，再用可追溯透明贴纸确定性合成标准尺寸卡面。
homepage: https://github.com/juju-w/card-creator-skill
license: MIT
metadata:
  version: 0.1.2
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

把卡面拆成两个图层：AI 生成的背景，以及由脚本确定性叠加的透明贴纸。支付卡组织、交通卡
或城市卡标志必须来自素材清单；绝不让 ImageGen 重画、近似、风格化或修补 Logo。

## 工作流

1. 生成前先读取[卡面规则](references/card-rules.md)。输入是已有卡面或手机钱包截图时，同时读取
   [参考卡面风格化改造](references/reference-remix.md)：只分析卡面区域，忽略外部界面，再把
   设计语法转化为明显不同的新构图。
2. 选择支付或交通贴纸时读取[贴纸目录](references/sticker-catalog.md)，再读取
   [贴纸清单](assets/stickers/manifest.json)。只有 `status: ready` 的条目可以叠加。
   如果用户要的贴纸尚未就绪，只生成并交付预留好位置的背景，同时明确报告缺少的素材；
   不得静默漏贴，也不得用近似图替代。
   用户要求继续研究缺失标志，或提供了具体卡面原图时，读取
   [贴纸研究与卡面提取](references/sticker-research.md)。从卡面抠图只能产生研究候选，不能
   自动把条目提升为 `ready`。
3. 默认只做一个卡面。只有用户明确需要正反面组合时，才确认成套设计要求。
4. 使用内置图像生成工具只创建背景。要求平视、横向、满版，不出现设备、卡片样机、Logo、
   水印、边框或阴影。重要主体远离安全区边缘，并为之后的贴纸留出干净负空间。
5. 把选定的生成图复制到工作项目，运行 `scripts/prepare_card.py` 完成裁切、300 DPI 出血与
   裁切导出，并叠加已批准的透明 PNG 贴纸。
6. 检查最终的出血图、裁切图和辅助线预览。主体被裁切、文字变形、贴纸位置错误、透明度异常
   或重要内容超出安全区时必须退回修正。
7. 返回最终文件路径、尺寸、使用的贴纸来源，以及最终背景 Prompt。

## 不可违反的规则

- 标准裁切尺寸为 `1011 × 638 px`、300 DPI，对应 `85.60 × 53.98 mm`。
- 含出血主文件为 `1081 × 708 px`，四边各 `35 px` 出血。
- 重要内容至少位于裁切线内侧 `59 px`。
- 贴纸是不可变的透明覆盖层；保持比例、颜色和透明度，不得描摹或重制。
- 用户私人图片默认只在本地处理，除非用户明确要求上传或发布。
- 不得声称出现品牌名称就代表赞助、授权或官方合作。
- 不得生成卡号、支付凭据、二维码、条形码，或足以冒充真实支付卡、门禁卡、交通卡、证件的设计。
- 参考卡面只用于提取配色关系、留白、线条、纹样密度和构图区，不代表可以复制卡号、钱包余额、
  发卡方文字、专有插画或尚未就绪的 Logo。

## 文件

- 精确尺寸与坐标系统见[卡面规则](references/card-rules.md)。
- Prompt 写法见[背景 Prompt 指南](references/prompt-guide.md)。
- 根据已有卡面或手机钱包截图做风格变化时，读取
  [参考卡面风格化改造](references/reference-remix.md)。
- 贴纸类别与研究队列见[贴纸目录](references/sticker-catalog.md)。
- 缺失标志的来源检索与卡面像素提取见[贴纸研究与卡面提取](references/sticker-research.md)。
- 贴纸文件与来源记录位于 `assets/stickers/`。
- 确定性导出参数运行 `python3 scripts/prepare_card.py --help` 查看。
