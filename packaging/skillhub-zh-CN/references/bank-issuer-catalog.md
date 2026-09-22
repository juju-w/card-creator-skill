# 银行发行方参考目录

用户希望卡面出现银行标识时，先区分三个不同图层：

- `issuer-bank` 是发卡银行，如工商银行、招商银行、汇丰；
- `payment` 是支付卡组织或网络，如银联、Visa、Mastercard；
- `transit-ic` 与 `cities` 是交通或储值卡产品。

不要用其中一类代替另一类。一张卡面可以分别为银行和卡组织预留位置，但不得让成品看起来像
真实银行发行、可支付的银行卡。

下面所有条目在 `../assets/stickers/manifest.json` 中均为 `pending`，只用于识别需求和预留位置。
生成结果要说明缺少素材，不得要求图像模型重画或近似 Logo。只有取得可追溯透明母版，并核实
可再分发或商标使用条件后，才能提升为 `ready`。

## 中国内地

- `icbc` — 中国工商银行 / ICBC
- `agricultural-bank-of-china` — 中国农业银行 / ABC
- `bank-of-china` — 中国银行 / Bank of China
- `china-construction-bank` — 中国建设银行 / CCB
- `bank-of-communications` — 交通银行 / Bank of Communications
- `postal-savings-bank-of-china` — 中国邮政储蓄银行 / PSBC
- `china-merchants-bank` — 招商银行 / China Merchants Bank
- `china-citic-bank` — 中信银行 / China CITIC Bank
- `china-everbright-bank` — 中国光大银行 / China Everbright Bank
- `china-minsheng-bank` — 中国民生银行 / CMBC
- `industrial-bank-china` — 兴业银行 / Industrial Bank
- `shanghai-pudong-development-bank` — 浦发银行 / SPD Bank
- `ping-an-bank` — 平安银行 / Ping An Bank
- `china-guangfa-bank` — 广发银行 / China Guangfa Bank

## 香港与常见国际发行方

- `bank-of-china-hong-kong` — 中国银行（香港） / BOCHK；不要用内地中国银行组合标识代替
- `hsbc` — 汇丰 / HSBC
- `standard-chartered` — 渣打银行 / Standard Chartered
- `hang-seng-bank` — 恒生银行 / Hang Seng Bank
- `bank-of-east-asia` — 东亚银行 / Bank of East Asia
- `dah-sing-bank` — 大新银行 / Dah Sing Bank
- `cmb-wing-lung-bank` — 招商永隆银行 / CMB Wing Lung Bank
- `dbs-bank` — 星展银行 / DBS
- `ocbc` — 华侨银行 / OCBC；使用 2023 年后的当前识别，不使用旧永亨标识
- `uob` — 大华银行 / UOB
- `citi` — 花旗 / Citi

## 构图规则

即使银行贴纸尚不可用，也要在背景 Prompt 中明确留位。横向组合标识通常需要左上角或右上角的
安静区域；紧凑图形需要的角落空间更小。不要自行猜测双语、纯图形、单色或反白版本，只为用户
明确指定或已经提供的获准透明文件预留。

银行标识不得与卡号、姓名、有效期、安全码、芯片、磁条等元素组合成足以冒充真实银行卡的设计。
