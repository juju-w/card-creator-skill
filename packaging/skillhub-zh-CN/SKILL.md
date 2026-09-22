---
name: card-creator
slug: card-creator
displayName: 卡面生成器
version: 0.2.0
description: 根据一句简短描述快速生成 AirCard、NFC 卡、银行卡或交通卡卡面。始终用 ImageGen 一次生成完整卡面，不使用 SVG 或脚本拼贴 Logo。
summary: 用一句话和 ImageGen 快速生成完整卡面。
homepage: https://github.com/juju-w/card-creator-skill
license: MIT
metadata:
  version: 0.2.0
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

“鲤鱼王 × ICOCA，简洁，右下角 ICOCA”这样的一句话已经完整。直接开始生成，不要把普通卡面
请求变成 Logo 研究、SVG 绘图或贴图工程。

## 必须遵循的流程

1. **首先调用 ImageGen。** 一次生成包含主体、风格、所需标志和位置的完整横向卡面。不得使用
   SVG、HTML、Canvas 或代码绘图代替 ImageGen。
2. 品牌名、“Logo”、位置要求以及裁切/出血下载要求都不表示需要精确贴图。不要读取 SVG、
   manifest 或合成参数。
3. 用户提供 Logo 参考图时，必须将它交给 ImageGen，而不是凭记忆重画或贴到成品上。中文分发包
   不附带二进制参考图库；没有用户参考时再使用模型知识，不要自动联网研究。
4. 不添加用户未要求的文字、卡号、芯片、二维码、条形码或感应/NFC 标志。避免手、设备、钱包
   界面、透视样机、水印、阴影和烘焙圆角。
5. 只检查主体与标志是否出现、层级是否清楚、重要内容是否意外裁切。只有成品明显不可用时，
   最多进行一次聚焦重试。
6. 图片生成完成后，才运行 `scripts/prepare_card.py` 输出 300 DPI 的 trim、bleed 和 guides。
   `cover` 用于满版；边缘内容可能被裁切时使用 `--fit-mode contain`。导出脚本不添加 Logo。

## 输出与边界

- 优先返回 `1011 × 638 px` trim，再按需提供 `1081 × 708 px` bleed 与检查版。
- 生成的第三方标志属于非官方风格化诠释，不得声称品牌规范准确、授权、互通、赞助或认可。
- 用户私人图片默认只在本地处理，除非用户明确要求发布。
- 不得创建支付凭据，或足以冒充真实支付卡、门禁卡、交通卡、证件的设计。
- 感应/支付指示图标默认不添加。

## 仅在需要时读取参考文件

- 只有编写或调试 Prompt 时读取[Prompt 指南](references/prompt-guide.md)。
- 只有根据已有卡面、照片或钱包截图做变化时读取
  [参考卡面改造](references/reference-remix.md)。
- 尺寸与坐标以[卡面规则](references/card-rules.md)为准。
