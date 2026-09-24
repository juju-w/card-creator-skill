# SkillHub 简体中文分发包

本目录只维护 `entry.md` 的中文元数据、简短介绍及中文界面文案。构建时从
`skills/card-creator` 复制主包，将同一份 Skill 正文接在中文介绍之后；卡面规则不覆盖、不翻译。
网页指南也来自相同源文件，三个入口不各自维护执行规则。

中英文包都只用图片生成，不包含卡面绘制、拼贴或导出脚本。

## 构建

```bash
python3 packaging/skillhub-zh-CN/build.py /tmp/card-creator-skillhub-zh-CN
```

输出目录可交给 SkillHub CLI。本仓库目前发布文本分发包：构建器移除参考图片，
把索引改成固定到源 Git 提交的原图直链；这不代表 CLI 预检验证过服务端的图片支持。
链接不可访问时遵循共享规则的参考图处理方式。GitHub 主包保留本地图片。
输出入口记录源提交和规则摘要，便于核对实际安装版本；构建过程也会清理缓存文件。

普通用户无需安装 Python 或任何绘图依赖；宿主需具备图片生成能力。本目录的构建脚本仅供发布维护。

## 校验与发布

```bash
skillhub --skip-self-upgrade publish /tmp/card-creator-skillhub-zh-CN --dry-run

skillhub --skip-self-upgrade publish /tmp/card-creator-skillhub-zh-CN \
  --changelog "统一执行规则，增加自动标志搭配与局部改图，优化网页复制入口。"
```

版本只维护在 `entry.md` 顶层。正式构建前先提交并推送源码，确保固定提交的图片链接能访问。
本机 CLI 的 `--dry-run` 仅校验元数据，不能证明包文件可发布或远程素材可用。

发布后用 `skillhub --skip-self-upgrade install card-creator --namespace indiv-juju-w --dir <全新临时目录>`
重新安装，比较正文、版本、源提交、规则摘要和完整索引；再验证代表性图片链接。
若平台仍返回旧版本，不将本地构建成功或发布接受响应当成安装验证成功。
发布前须运行根目录 README 中的 Skill 校验与分发包、参考图完整性测试。
