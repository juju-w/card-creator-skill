# Live Skill acceptance scenarios

Maintainer checks, not instructions loaded during ordinary card creation. Use the current Skill with the host's image tool. Keep drafts and execution notes outside the repository; do not publish QA images automatically.

| Request | Observable acceptance |
|---|---|
| 生成一张伦敦春日厚涂交通卡 | Chooses a relevant transit-product mark without asking the user to pick one; bright impasto, recognizable London, no unrelated payment indicators. |
| 鲤鱼王 × ICOCA，简洁，右下角 ICOCA | Recognizable character and requested mark, correct placement; only matching reference opened if needed. |
| On that image: 只把 ICOCA 改成深蓝，主体和背景不动 | Uses the previous image as the edit target; only the requested mark should materially change. Record any drift rather than claiming pixel-perfect preservation. |
| 无标志莫兰迪静物卡面 | No mark or added text despite the automatic-logo default. |
| 做一张竖版卡面，主体、文字和标志都朝上 | Generates portrait artwork near 1:1.586, with a native upright composition and important details intact; no sideways landscape or forced crop. Record actual dimensions rather than promising 969 × 1536. |
| 做一张无标志的文殊菩萨竖版纪念卡 | Portrait composition keeps crown, raised sword and lotus pedestal visible; no payment mark, fabricated script or transparent corners. Inspect hands and attributes rather than treating packaging tests as visual validation. |
| Repeat a short request with image tools unavailable | Explains the capability limitation; no script, SVG drawing or pretend image. |
| Named mark with inaccessible reference URL | No download loop or library audit; uses an available user reference or confident knowledge, otherwise resolves genuine uncertainty. |

For returned images, record actual dimensions and inspect actual alpha pixels, corners and unintended pale borders. An opaque light background is not itself a white-border failure. Do not resize, crop or composite to make a test pass. Inspect subject details and logo readability visually; make at most the one targeted correction allowed by the Skill.

Record the short request, source Skill revision, image tool result, opened references, output paths and visual findings. A tool rejection, missing image or unavailable capability is **blocked**, not a visual pass. Syntax, packaging and frontmatter validation do not substitute for these scenarios.
