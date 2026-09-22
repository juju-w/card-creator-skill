# Prompt 指南

给用户看的 Prompt 保持简短。尺寸、导出规则和常规排除项由 Skill 自己处理。

## 单次 ImageGen 流程

一句话写明主体、风格和标志位置：

```text
使用 card-creator Skill，生成一张鲤鱼王 × ICOCA 卡面：简洁，右下角 ICOCA。
```

这个 Prompt 必须直接进入一次 ImageGen 调用。不得研究 Logo、读取 SVG、用代码绘图，也不得把
任务拆成“先生成背景、再贴 Logo”。内部只补充 ImageGen 真正需要的最少制作要求：平面横向
卡面、不要样机与功能性卡片数据、用户未要求时不加感应标志。用户上传的 Logo 图片只作为
ImageGen 视觉参考；所需 Logo 随整张卡面一起生成，并披露为非官方风格化诠释。
