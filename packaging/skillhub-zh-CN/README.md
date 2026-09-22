# SkillHub 简体中文分发包

本目录保存 SkillHub/WorkBuddy 中文版本的可维护源文件。默认安装入口
`skills/card-creator` 继续使用英文，方便 GitHub、skills.sh 和国际 Agent Skill 市场收录；
构建时复制默认 Skill，再用本目录中的中文入口、界面文案和参考文档覆盖对应文件。

脚本和素材只有一份权威来源：`skills/card-creator`。中文包不会复制维护另一套卡面尺寸、
贴纸清单或合成代码，因此 `status: ready` 的安全门不会因双版本而发生漂移。

## 构建

```bash
python3 packaging/skillhub-zh-CN/build.py /tmp/card-creator-skillhub-zh-CN
```

输出目录是可直接交给 SkillHub CLI 的完整 Skill 包。SkillHub 不接受 PNG 二进制附件，因此构建器
会把 `status: ready` 的透明 PNG 无损编码为 `*.base64.txt`；合成脚本在内存中解码，用户无需
手动处理。透明 SVG 原件仍保留，研究用 PNG 则只留来源记录并从中文分发包中移除。GitHub 主包
继续保存原始 PNG 衍生文件。构建过程也会清理 `.DS_Store`、`__pycache__` 和 `.pyc`。

普通用户只需安装 `scripts/requirements.txt` 中的 Pillow。只有维护者从 SVG 重新生成 PNG 时，
才需要 `scripts/requirements-render.txt` 与系统原生 Cairo 库。

## 校验与发布

```bash
skillhub publish /tmp/card-creator-skillhub-zh-CN --dry-run \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"

skillhub publish /tmp/card-creator-skillhub-zh-CN \
  --changelog "新增 Card Creator 中文 SkillHub/WorkBuddy 版本。"
```

发布新版本时，同时更新 `SKILL.md` 顶层和 `metadata.version` 中的版本号。发布前必须运行
根目录 README 中的 Skill 与贴纸校验；不得把 `reference-only` 或 `research_file` 当成可调用
贴纸。搜索失败的品牌不写入 manifest 占位记录。
