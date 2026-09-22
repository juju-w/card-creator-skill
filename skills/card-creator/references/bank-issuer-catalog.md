# Bank issuer reference catalog

Use this catalog when a requested card face includes a bank issuer mark. Bank issuers are a separate
layer from payment schemes and transit products:

- `issuer-bank` identifies the bank whose brand appears on the card, such as ICBC or HSBC;
- `payment` identifies a payment scheme or network, such as UnionPay, Visa, or Mastercard;
- `transit-ic` and `cities` identify a transit or stored-value product.

Never replace one layer with another. A card may legitimately reserve space for one issuer mark and
one payment-network mark, but their presence must not imply that the generated artwork is a genuine
bank-issued payment card.

All entries below are `blocked` as exact reusable overlays in `../assets/stickers/manifest.json`.
Exact mode reserves a clean area and names the missing asset. If the user explicitly selects stylized
mode and supplies or approves a traceable reference, ImageGen may create a disclosed non-official
interpretation for that artwork only. Never promote that generated result to `ready`.

## Mainland China

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

## Hong Kong and commonly requested international issuers

- `bank-of-china-hong-kong` — 中国银行（香港） / BOCHK; do not substitute the mainland BOC lockup
- `hsbc` — 汇丰 / HSBC
- `standard-chartered` — 渣打银行 / Standard Chartered
- `hang-seng-bank` — 恒生银行 / Hang Seng Bank
- `bank-of-east-asia` — 东亚银行 / Bank of East Asia
- `dah-sing-bank` — 大新银行 / Dah Sing Bank
- `cmb-wing-lung-bank` — 招商永隆银行 / CMB Wing Lung Bank
- `dbs-bank` — 星展银行 / DBS
- `ocbc` — 华侨银行 / OCBC; use the current post-2023 identity, not the legacy Wing Hang mark
- `uob` — 大华银行 / UOB
- `citi` — 花旗 / Citi

## Composition guidance

Treat issuer placement as part of the background brief even when the mark is unavailable. A small
horizontal lockup normally needs a calm area near the upper-left or upper-right; a compact symbol can
use a smaller corner zone. Do not infer a bilingual, symbol-only, monochrome, or reversed variant.
Reserve for the exact variant requested by the user or supplied as an approved transparent asset.

Issuer marks must never be combined with account numbers, names, expiration dates, security codes,
chips, magnetic stripes, or other details that could make the result pass as a functional bank card.
