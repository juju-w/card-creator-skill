# SkillHub 简体中文分发包

本目录保存 SkillHub/WorkBuddy 中文版本的可维护源文件。默认安装入口
`skills/card-creator` 继续使用英文，方便 GitHub、skills.sh 和国际 Agent Skill 市场收录；
构建时复制默认 Skill，再用本目录中的中文入口、界面文案和参考文档覆盖对应文件。

卡面尺寸与导出脚本只有一份权威来源：`skills/card-creator`。中文包不会复制维护另一套规则。

## 构建

```bash
python3 packaging/skillhub-zh-CN/build.py /tmp/card-creator-skillhub-zh-CN
```

输出目录是可直接交给 SkillHub CLI 的完整 Skill 包。SkillHub 不接受 PNG 二进制附件，因此构建器
会移除可选的 Logo 参考图库；中文 Skill 使用模型知识或用户上传的参考图。GitHub 主包继续保存
PNG 视觉参考。构建过程也会清理 `.DS_Store`、`__pycache__` 和 `.pyc`。

普通用户只需安装 `scripts/requirements.txt` 中的 Pillow。

## 校验与发布

```bash
skillhub publish /tmp/card-creator-skillhub-zh-CN --dry-run \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"

skillhub publish /tmp/card-creator-skillhub-zh-CN \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"
```

发布新版本时，同时更新 `SKILL.md` 顶层和 `metadata.version` 中的版本号。发布前必须运行
根目录 README 中的 Skill 与导出脚本测试。
