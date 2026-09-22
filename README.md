# card-creator-skill

一个用于生成 AirCard、NFC 卡片和交通卡卡面的 Codex Skill。仓库当前只维护三类内容：

- 标准卡面尺寸、出血区和安全区规则。
- 有来源记录的透明交通/支付贴纸素材。
- 将 AI 背景图裁切、缩放并叠加贴纸的确定性脚本。

它不包含在线编辑器，也不会让图像模型重画品牌 Logo。

## 安装

把技能目录复制到 Codex skills 目录：

```bash
cp -R skills/card-creator ~/.codex/skills/
```

脚本依赖：

```bash
python3 -m pip install -r skills/card-creator/scripts/requirements.txt
```

之后可以这样调用：

```text
Use $card-creator to create a quiet Guangzhou morning card face,
reserve the upper-right for the China T-Union sticker, and export print-ready PNGs.
```

## 输出规格

- 成品裁切尺寸：`1011 × 638 px`，300 DPI，对应 `85.60 × 53.98 mm`。
- 含出血尺寸：`1081 × 708 px`，四边各 `35 px` 出血。
- 重要内容安全边距：裁切线内缩 `59 px`。
- 输出包含 `bleed`、`trim` 和 `guides` 三张 PNG。

## 贴纸状态

当前已准备透明 SVG 与 PNG：Visa、Mastercard、American Express、UnionPay、Suica。

交通联合、北京一卡通、上海公共交通卡、杭州通、长安通、羊城通和岭南通已经进入素材清单，但在找到可验证的官方或可再分发源文件前保持 `pending`，Skill 不会使用近似图替代。

完整来源、许可备注和状态见 [manifest.json](skills/card-creator/assets/stickers/manifest.json)。品牌与商标仍可能受各司法辖区的商标规则约束；本项目不代表相关机构授权或合作。

## 验证

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/card-creator

python3 skills/card-creator/scripts/render_stickers.py
```

核心入口：[SKILL.md](skills/card-creator/SKILL.md)
