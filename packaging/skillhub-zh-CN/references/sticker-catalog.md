# 贴纸目录

精确合成以 `../assets/stickers/manifest.json` 为唯一依据。manifest 只保存仓库里实际存在的文件：

- `ready`：有准确透明来源和衍生文件，可以合成；
- `reference-only`：保留了可追溯研究文件，但不能合成。

缺失品牌只在用户真正请求时研究，不再写入空的 `blocked` 占位记录。

## 已就绪支付标志

- Visa、Mastercard、American Express、JCB、Discover、RuPay、MIR
- 银联：卡角默认 `unionpay-compact`，明确要求时使用完整 `unionpay`
- Diners Club：默认紧凑 `diners-club-symbol`，明确要求时使用完整字标

## 已就绪日本交通 IC 标志

- Suica、PASMO、ICOCA、TOICA、manaca
- SUGOCA、nimoca、Hayakaken、PiTaPa

这些只是装饰素材，不得声称自制卡由运营方发行、受理或认可。

## 已保留研究文件

manifest 中的 `reference-only` 包括北京、杭州、西安、广州、岭南通、深圳、天津、成都、重庆
的来源样本，以及带不透明底的 Kitaca 源文件和 Material 通用感应图标。它们是证据，不是贴纸。

## 缺失标志如何处理

1. 精确模式读取[按需素材研究与 Alpha 提取](sticker-research.md)，现场查找可追溯来源。
2. 无法建立精确素材时，保持空位并报告缺失，不新增 manifest 占位行。
3. 用户明确要求风格匹配或重新诠释时，可以搜索参考图，或基于模型先验生成只用于当前卡面的
   非官方版本；记录参考决策与最终 Prompt，绝不提升为 `ready`。

银行发行方、支付网络、钱包、交通产品和受理标志仍要区分；只有用户明确要做拼贴或戏仿时才混排。

## 感应标志

感应/NFC 标志仅在用户明确要求时加入。`generic-contactless-material` 是 `reference-only`，并非
标准卡面受理标志。精确授权标志必须来自可追溯且允许使用的来源，不能用通用图标代替。
