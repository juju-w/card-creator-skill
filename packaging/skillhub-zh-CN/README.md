# SkillHub 简体中文分发包

本目录保存 SkillHub/WorkBuddy 中文版本的可维护源文件。默认安装入口
`skills/card-creator` 继续使用英文，方便 GitHub、skills.sh 和国际 Agent Skill 市场收录；
构建时复制默认 Skill，再用本目录中的中文入口、界面文案和参考文档覆盖对应文件。

中英文包都只用图片生成，不包含卡面绘制、拼贴或导出脚本。

## 构建

```bash
python3 packaging/skillhub-zh-CN/build.py /tmp/card-creator-skillhub-zh-CN
```

输出目录是可直接交给 SkillHub CLI 的完整 Skill 包。SkillHub 不接受图片二进制附件，因此构建器
会移除 PNG/JPG 文件，把参考图索引改成 GitHub 原图直链。只取当前请求所需的图片；链接不可访问时
使用用户参考图或模型知识。GitHub 主包保留本地图片。构建过程也会清理缓存文件。

普通用户无需安装 Python 或任何绘图依赖；宿主需具备图片生成能力。本目录的构建脚本仅供发布维护。

## 校验与发布

```bash
skillhub publish /tmp/card-creator-skillhub-zh-CN --dry-run \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"

skillhub publish /tmp/card-creator-skillhub-zh-CN \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"
```

发布新版本时，同时更新 `SKILL.md` 顶层和 `metadata.version` 中的版本号。发布前必须运行
根目录 README 中的 Skill 校验与分发包、参考图完整性测试。
