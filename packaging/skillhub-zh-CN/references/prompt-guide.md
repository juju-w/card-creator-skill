# 背景 Prompt 指南

生成 Prompt 描述的是平面画稿，而不是实体卡产品或样机。

必须包含：

- `flat edge-to-edge landscape artwork, 1.58577:1 composition`；
- 主体、视觉风格、色板、氛围和焦点位置；
- `important content centered within a generous safe area`；
- 后续透明贴纸所需的干净留白位置；
- `no logo, no brand mark, no card number, no QR code, no barcode, no watermark`；
- `no card mockup, no hand, no perspective, no rounded-corner mask, no shadow`。

默认精确模式下，ImageGen Prompt 只描述留位，真实贴纸之后通过 `prepare_card.py` 叠加；
应根据标志类别和官方参考选择约定俗成的卡面版本，不能全局强制短款或完整横版。

用户明确选择风格化模式时，把可追溯标志作为注明用途的参考图，并写清材质、位置和披露：结果
是非官方艺术化诠释，不能进入精确贴纸包。两种模式都不得默认加入感应标志。

用户提供已有卡面或手机钱包截图并要求做风格变化时，先读取
[参考卡面风格化改造](reference-remix.md)，再编写 Prompt。

示例：

```text
Create flat edge-to-edge landscape artwork in a 1.58577:1 composition. A quiet ink-and-gouache city
morning with a train crossing the lower third, warm paper texture, pine green and vermilion palette.
Keep the central title area calm and all important subjects inside a generous safe area. Leave clean
negative space in the upper-right for a later transparent transit sticker. No logo, brand mark, card
number, QR code, barcode, watermark, card mockup, hand, perspective, border, rounded-corner mask,
or shadow.
```
