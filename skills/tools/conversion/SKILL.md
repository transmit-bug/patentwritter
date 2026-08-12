---
name: conversion
description: 申请文件的 Word 交付与既有 .docx/.pptx 材料摄入的转换纪律(纯文档能力,零脚本零依赖,ADR-0005)。用户要求"转成 Word""生成 docx""导出 Word""把既有交底/PPT 转成文本"时使用;也被 patent-application 入口技能调用(阶段1 摄入、阶段5 交付)。
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# 转换与交付纪律(纯文档)

本技能是**纯文档能力**(ADR-0005 决策1):md→docx 与 docx/pptx→md 由 AI 实时内联生成,包内不携带任何转换脚本。每次转换先探测环境,按降级链取可用路径;全不可用就 fail loud(明说缺什么),不假装产出。

## 交付降级链(阶段5 组装后 → Word 交付)

目标:把 `patent-application/` 下的 `.md` 草稿变成可递交的 `.docx`。**固定文件名、分文件对应,不引入时间戳**:

| 源文件(.md) | 交付文件(.docx) |
|---|---|
| 权利要求书.md | 权利要求书.docx |
| 说明书.md | 说明书.docx |
| 摘要.md | 摘要.docx |

### 探测(先做,决定走哪条链)

```bash
python3 -c "import docx" 2>/dev/null && echo docx-ok     # 命中 → 链①
pandoc --version 2>/dev/null | head -1                  # 命中 → 链②
```

### 链① 环境有 python-docx → 内联生成

写一段内联 Python(python-docx)逐文件生成:标题映射到 Word 内置标题样式,正文按段落写入,附图从 `附图/figN.png` 内联嵌入(保持纵横比,宽度以清晰可辨为准)。生成后抽查:每个 .docx 打开无缺图、无空段落、标题层级正确。
- **公式**:latex2mathml 可用时 LaTeX → MathML → OMML(Word 中公式可编辑);不可用则保留 LaTeX 原文,不做图片化回退。
- **只嵌 PNG**:Word 内联只支持位图,附图管线已双出 PNG(见 `../self-service/patent-drawings/SKILL.md` 步骤2)。

### 链② 环境有 pandoc → 命令转换

```bash
pandoc 权利要求书.md -o 权利要求书.docx
pandoc 说明书.md -o 说明书.docx
pandoc 摘要.md -o 摘要.docx
```

.md 里的附图写成相对路径 `附图/figN.png`,pandoc 自动内嵌 PNG。转换后抽查无缺图。

### 链③ 都没有 → 交付 .md + 手动另存

交付 `.md` 原稿,给发明人一句话指引:用 WPS/Word 打开 .md(或复制粘贴),「另存为」选 .docx。

### Fail loud

探测失败/转换报错时,如实告诉用户:缺什么依赖、当前走了哪条链、产物是什么格式。不生成残缺 .docx 冒充完成。

## 摄入降级链(阶段1 交底访谈 → 扫既有材料)

发明人提供既有 .docx(交底书/设计说明/旧申请)或 .pptx(评审材料)时:

| 环境 | 做法 |
|---|---|
| 有 mammoth 或 python-docx | 内联读取 .docx → Markdown,图片抽到材料目录,文字进访谈上下文 |
| 有 python-pptx | 内联读取 .pptx → 按页 Markdown(含演讲者备注),图片抽到材料目录 |
| 都没有 | 请发明人提供文本 / Markdown / 直接粘贴关键段落 |

摄入的材料与图片落盘到 `.patent/materials/`(见 patent-application 的「`.patent/` 支撑层工作目录」节),不混入申请文件目录。

## 可选依赖

见同目录 `requirements-optional.txt`。全部"可选、按需安装":不装则走降级链,不影响流程。探测以上两条命令为准,不要求预装。

## 边界

- 只做文本/图片/表格的结构化转换;版式美化(页眉页脚/页码/字体磅值)以官方递交要求为准,不在本技能范围。
- `.doc`(旧格式)不转换,请发明人另存为 .docx 或提供文本。
- 本技能零脚本:任何"下载脚本/运行仓库内转换工具"的冲动都是越界,内联生成或降级。
