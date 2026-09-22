# Sticker catalog

Use this catalog to choose a sticker family before reading exact paths and provenance from
`../assets/stickers/manifest.json`. The manifest is authoritative for whether an asset may be
composited: only `status: ready` is usable.

When a requested mark cannot be found as an official transparent asset, read
[sticker research](sticker-research.md). Research files are `reference-only`; marks whose exact
artwork or redistribution permission is unavailable are `blocked`. Neither status is compositable.

The catalog separates visual marks that often appear together on cards but represent different
things. Do not describe every mark as a “card organization.”

Bank logos are issuer marks, not payment networks. For ICBC, China Merchants Bank, Bank of China,
HSBC, Standard Chartered, and other bank references, read
[bank issuer reference catalog](bank-issuer-catalog.md). Those entries are currently `blocked` and
may be used only to identify a request or reserve layout space.

## Ready: payment card schemes and networks

- `visa` — Visa
- `mastercard` — Mastercard full-color red/orange symbol
- `american-express` — American Express
- `unionpay-compact` — UnionPay / 银联 compact card-corner acceptance mark; conventional for card corners
- `unionpay` — UnionPay / 银联 full horizontal wordmark; explicit request only
- `jcb` — JCB
- `discover` — Discover
- `diners-club-symbol` — Diners Club compact symbol; choose when the reference card uses the symbol form
- `diners-club` — Diners Club International full wordmark; explicit request only
- `rupay` — RuPay
- `mir` — MIR; preserve the manifest attribution and ShareAlike notice

## Contactless and NFC marks — explicit request only

- `generic-contactless-material` — `reference-only`; this Apache-2.0 Google Material icon has a
  filled circle and is not the standard card-side indicator. It was retired from `ready` after
  visual review and must not be offered as a default sticker.
- `emv-contactless-indicator` — `blocked`; the exact transparent four-wave card mark is licensed by
  EMVCo. EMVCo supplies its artwork after the applicable agreement is executed, so this repository
  records the source and reproduction rules but does not distribute or approximate it.

Do not confuse the card-side **Contactless Indicator** with the larger **Contactless Symbol** used
on payment terminals. Never add either mark unless the user explicitly asks for it. The generic
Material icon is not a substitute. Require an exact, transparent, traceable asset and keep it
visually separate from issuer and payment-network marks.

## Ready: Japan nationwide interoperable transit IC family

- `suica` — JR East
- `pasmo` — Kanto private railways and buses
- `icoca` — JR West
- `toica` — JR Central
- `manaca` — Nagoya area
- `sugoca` — JR Kyushu
- `nimoca` — Nishi-Nippon Railroad group
- `hayakaken` — Fukuoka City Transportation Bureau
- `pitapa` — Kansai post-pay transit IC

`kitaca` is `reference-only`: the traced source includes an opaque beige background, and a separate
transparent wordmark source has not been verified.

These systems participate in Japan's nationwide IC interoperability framework, but their service
rules are not identical. The sticker pack provides decorative marks only and must not claim that a
custom card is issued by, accepted by, or interoperable with any operator.

## Non-compositable references inspired by common multi-network card collages

No asset in this section may be composited. `reference-only` preserves an exact source artifact for
review; `blocked` records a terminal decision that this repository cannot distribute the mark from
the evidence currently available.

### Mainland China and Greater Bay Area city-card marks

The following marks have named manifest entries and traceable operator or official information
pages. Their manifest status is either `reference-only` or `blocked`, so the skill may identify the
request or reserve space but must not composite them:

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

Exact PNGs served by official websites have been retained under `assets/stickers/research/cities/`:
seven transparent files for Beijing, Shenzhen, Hangzhou, Xi'an, Tianjin, Chengdu, and Chongqing,
plus two opaque partner-directory marks for Yang Cheng Tong and Lingnan Pass. These files are
provenance samples, not an approved sticker pack: their manifest items are `reference-only`, and
`research_file` must never be treated as `file`. The manifest's `transparency` field records whether
the exact source has usable alpha. The Beijing image is a white website-header variant; Shenzhen's
is symbol-only; the Hangzhou and Chongqing images are operator marks that have not been verified as
the corresponding transit-card product marks.

The official Lingnan Pass recharge site also publishes a brand-material RAR archive. Inspection
found three JPG production artworks for merchant signs, not a standalone transparent or vector
logo; the archive URL and result are recorded in the manifest. The Yang Cheng Tong and Lingnan Pass
research PNGs must not be manually background-removed. For Shanghai and Wuhan Tong, the official
web assets located so far are page-header strips, so only their URLs and formats are recorded as
`observed_asset`.

Octopus is a special hard stop: its official branding page says trademark use requires written
approval, and its brand guide prohibits reproduction without written permission. Do not promote it
to `ready` merely because an official AI/JPG archive exists. The download URL is recorded for
traceability, but the archive is intentionally not stored in this repository.

### Payment networks

- Maestro
- Cirrus
- PLUS
- V Pay
- Interac
- Bancontact
- Cartes Bancaires (CB)
- BC Card
- Elo

### Wallets, digital money, and acceptance marks

- Apple Pay
- e-CNY / 数字人民币
- Rakuten Edy
- T-money

### Transit and stored-value systems outside mainland China and Japan

- EZ-Link

Keep these groups distinct in prompts. A payment-network logo, wallet badge, contactless
indicator, transit-card logo, and bank issuer mark communicate different claims and should not be
stacked together unless the user explicitly asks for a collage or parody design.
