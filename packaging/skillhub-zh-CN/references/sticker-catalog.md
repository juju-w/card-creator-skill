# 贴纸目录

先用本目录选择贴纸类别，再从 `../assets/stickers/manifest.json` 读取准确路径和来源记录。
清单是贴纸能否使用的唯一权威：只有 `status: ready` 的条目可以合成。

支付卡组织、钱包、非接触受理标志和交通卡代表不同含义，不要把它们统称为“卡组织”。

## 已就绪：支付卡组织和网络

- `visa` — Visa
- `mastercard` — Mastercard 红橙双色标志
- `american-express` — American Express
- `unionpay` — UnionPay / 银联完整横版标志
- `unionpay-compact` — UnionPay / 银联紧凑卡角标志，不带右侧字样
- `jcb` — JCB
- `discover` — Discover
- `diners-club` — Diners Club International 完整字标
- `diners-club-symbol` — Diners Club 紧凑图形，不带右侧字样
- `rupay` — RuPay
- `mir` — MIR；必须保留清单中的署名与相同方式共享说明

## 已就绪：日本全国交通 IC 互通体系

- `suica` — JR 东日本
- `pasmo` — 关东私铁与巴士
- `icoca` — JR 西日本
- `toica` — JR 东海
- `manaca` — 名古屋地区
- `sugoca` — JR 九州
- `nimoca` — 西日本铁道集团
- `hayakaken` — 福冈市交通局
- `pitapa` — 关西地区后付费交通 IC

`kitaca` 已收集但仍为 `pending`：当前可追溯 SVG 带不透明米色底，尚未核验单独的透明字标来源。

这些系统参与日本全国 IC 互通体系，但服务规则并不完全相同。贴纸包只提供装饰性标志；不得声称
自制卡由任何运营方发行、受理或认可。

## 研究队列：内地和大湾区城市交通卡

以下条目有明确的清单记录以及运营方或官方信息页，但仍是 `pending`。可以在背景中预留位置，
不可以合成：

- `china-t-union` — 交通联合
- `beijing-yikatong` — 北京一卡通
- `shanghai-public-transport-card` — 上海公共交通卡
- `tianjin-city-card` — 天津城市卡
- `guangzhou-yangchengtong` — 羊城通
- `lingnan-pass` — 岭南通
- `shenzhen-tong` — 深圳通
- `hangzhou-tong` — 杭州通
- `nanjing-jinling-tong` — 金陵通
- `chengdu-tianfu-tong` — 天府通
- `chongqing-city-card` — 重庆畅通卡
- `wuhan-tong` — 武汉通
- `xian-changan-tong` — 长安通
- `hong-kong-octopus` — 香港八达通 / Octopus
- `macau-pass` — 澳门通 / Macau Pass

`assets/stickers/research/cities/` 保存的是官方网页提供的来源样本，不是可用贴纸。
`research_file` 绝不能当成 `file`。羊城通和岭南通的研究 PNG 是不透明的合作方目录图，不能手工
去底；北京文件是白色官网页头版本；深圳是单独图形；杭州和重庆是运营方标志，尚未确认等同于
对应交通卡产品标志。上海和武汉目前只记录了官网页面横幅地址。

八达通是明确的硬性停止项：其官方品牌指引要求书面认可。即使存在 AI/JPG 官方下载包，也不得
因此把它提升为 `ready`。

## 研究队列：支付、钱包与其他交通体系

以下标志仍不可调用：

- 支付和银行网络：Maestro、Cirrus、PLUS、V Pay、Interac、Bancontact、Cartes Bancaires
  (CB)、BC Card、Elo。
- 钱包、数字货币和受理标志：Apple Pay、e-CNY / 数字人民币、EMV 非接触标志、Rakuten Edy、
  T-money。
- 中国内地和日本之外的交通储值系统：EZ-Link。

除非用户明确要做拼贴或戏仿，不要把不同类型的标志堆在一起。贴纸是否可用始终以 manifest 为准。
