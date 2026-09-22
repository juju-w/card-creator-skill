# Sticker catalog

Use this catalog to choose a sticker family before reading exact paths and provenance from
`../assets/stickers/manifest.json`. The manifest is authoritative for whether an asset may be
composited: only `status: ready` is usable.

The catalog separates visual marks that often appear together on cards but represent different
things. Do not describe every mark as a “card organization.”

## Ready: payment card schemes and networks

- `visa` — Visa
- `mastercard` — Mastercard full-color red/orange symbol
- `american-express` — American Express
- `unionpay` — UnionPay / 银联 full horizontal wordmark
- `unionpay-compact` — UnionPay / 银联 compact card-corner mark without the right-side wordmark
- `jcb` — JCB
- `discover` — Discover
- `diners-club` — Diners Club International full wordmark
- `diners-club-symbol` — Diners Club compact symbol without the right-side wording
- `rupay` — RuPay
- `mir` — MIR; preserve the manifest attribution and ShareAlike notice

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

`kitaca` is collected but remains pending: the traced source includes an opaque beige background,
and a separate transparent wordmark source has not yet been verified.

These systems participate in Japan's nationwide IC interoperability framework, but their service
rules are not identical. The sticker pack provides decorative marks only and must not claim that a
custom card is issued by, accepted by, or interoperable with any operator.

## Research backlog inspired by common multi-network card collages

No asset in this section may be composited until its official or freely reusable transparent
source and usage terms are recorded in the manifest.

### Mainland China and Greater Bay Area city-card marks

The following marks now have named manifest entries and traceable operator or official information
pages. They remain `pending`, so the skill may discuss or reserve space for them but must not
composite them:

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

Exact transparent PNGs served by official websites have been retained under
`assets/stickers/research/cities/` for Beijing, Shenzhen, Hangzhou, Xi'an, Tianjin, Chengdu, and
Chongqing. These files are provenance samples, not an approved sticker pack: their manifest items
remain `pending`, and `research_file` must never be treated as `file`. The Beijing image is a white
website-header variant; Shenzhen's is symbol-only; the Hangzhou and Chongqing images are operator
marks that have not been verified as the corresponding transit-card product marks.

For Shanghai, Yang Cheng Tong, Lingnan Pass, and Wuhan Tong, the official web assets located so far
are opaque rasters or page-header strips. Their exact URLs and formats are recorded as
`observed_asset` in the manifest, but the images are not copied into the sticker pack and must not
be manually background-removed.

Octopus is a special hard stop: its official branding page says trademark use requires written
approval, and its brand guide prohibits reproduction without written permission. Do not promote it
to `ready` merely because an official AI/JPG archive exists. The download URL is recorded for
traceability, but the archive is intentionally not stored in this repository.

### Payment and banking networks

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
- EMV contactless indicator
- Rakuten Edy
- T-money

### Transit and stored-value systems outside mainland China and Japan

- EZ-Link

Keep these groups distinct in prompts. A payment-network logo, wallet badge, contactless
indicator, and transit-card logo communicate different claims and should not be stacked together
unless the user explicitly asks for a collage or parody design.
