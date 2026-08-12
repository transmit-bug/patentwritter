# 整合方案:吸收 patent-disclosure-skill 实用能力(分阶段执行)

> **执行状态:三阶段已于 2026-08-12 全部落地**,实施记录见 [ADR-0005](../adr/0005-absorb-external-patent-tools.md) 的「实施记录」节。本文件保留为方案原文,供追溯。

> 依据 [ADR-0005](../adr/0005-absorb-external-patent-tools.md)（2026-08-12 生效）。本文是地图终点的落地物：三块吸收的**分阶段执行计划**。每个阶段独立可交付、可验收；实现由**方案确认后另起 effort** 执行（地图本身只出决策，不实现）。

**执行前置**：本方案经用户确认后，按阶段顺序执行；每阶段完成标准达成即验收，再进入下一阶段。

---

## 阶段 1 · 转换/交付文档化（优先）

**目标**：Word 交付与既有材料摄入能力落地为纯文档技能，零脚本零依赖。

| 项 | 内容 | 完成标准 |
|---|---|---|
| 1.1 | 新增 `skills/tools/conversion/SKILL.md`：转换纪律（交付降级链 / 摄入降级链 / 公式 OMML 可选 / 附图 PNG 嵌入规则引用 patent-drawings） | SKILL.md 存在且被 patent-application 阶段 5 引用 |
| 1.2 | 新增 `skills/tools/conversion/requirements-optional.txt`（python-docx、mammoth、python-pptx、latex2mathml 可选清单） | 文件存在，SKILL.md 指明按需安装 |
| 1.3 | patent-application 阶段 5 组装：增「生成 Word 交付」完成标准（同名 .docx 分文件对应，固定文件名） | 阶段 5 文档更新 |
| 1.4 | patent-drawings 步骤 2：补双输出命令（`dot -Tsvg` + `dot -Tpng`），附图目录 figN.svg + figN.png 并存 | 步骤 2 与完成标准更新；完成标准补「Word 嵌入图已生成、无缺图」 |

**依赖**：无（#9/#10 决策）。**验收**：文档可循一条样例流程从 .md 产出 .docx（环境有 python-docx 或 pandoc 任一）。

---

## 阶段 2 · 查新外部源（.patent/ 分级 + CNIPA 声明）

**目标**：CN 权威查新通道可用（人工操作），检索记录分级落盘。

| 项 | 内容 | 完成标准 |
|---|---|---|
| 2.1 | patent-application 阶段 2 查新指引：补「补充路径：国知局人工检索」段落（源信息 / 浏览器步骤 / 引用锚点=公开号/公告号 / agent_browser 代跑可选） | 指引更新，引用 #11 决议与 research/cnipa-epub-forms 报告 |
| 2.2 | `.patent/` 三档结构（sources / materials / queries）：阶段 2 检索结果落 queries/，素材落 materials/，引用清单落 sources/ | 输出目录约定写入 patent-application；README/模板建议 gitignore `.patent/` |
| 2.3 | patent-standards 目录加「外部声明源」条目：CNIPA 公布公告系统（官方名 / URL / 管辖 / 引用锚点） | 目录表更新（沿用 2026-08-11 核实惯例标注） |

**依赖**：无。**验收**：文档含可直接照做的国知局检索步骤（人工或 agent_browser）。

---

## 阶段 3 · 外观设计轻量向导

**目标**：自助包覆盖发明 + 实用新型 + 外观设计三种类型。

| 项 | 内容 | 完成标准 |
|---|---|---|
| 3.1 | patent-application 加外观分支：类别 / 洛迦诺分类提示 / 设计要点 / 简要说明 / 相似设计 / 请求保护色彩与否访谈 | 阶段 1/2 分支逻辑与完成标准更新 |
| 3.2 | 新增外观撰写要点 reference（外观四要素不适用，改走类别+设计要点） | reference 文件存在并被分支引用 |
| 3.3 | type-decision.md 加外观分支 | 决策树更新 |
| 3.4 | patent-standards 补锚点：第 2 条第 4 款 / 第 23 条 / 第 27 条（核实实施细则/审查指南对应条文，按 CNIPA 全文核实惯例） | 目录表 3 条新增 + 核实日期 |
| 3.5 | patent-drawings 加「外观附图」节：六面正投影视图 + 立体图、视图命名、黑白/灰度实务、素材由发明人提供 | 节存在，dot 不适用已注明 |
| 3.6 | patent-compliance 加外观检查项；patent-filing 补外观电子申请要点（图片格式/大小规范） | 两技能更新 |

**依赖**：阶段 1（附图 PNG/交付约定已定，外观视图清单独立）。**验收**：按外观分支可走通「类别→要点→六视图清单→自检→递交指引」。

---

## 边界清单（不执行）

- 审查答复（OA）：归档 professional/ 参考，本包边界不动（ADR-0004）。
- 专利通俗解读 / 政策嗅探：out-of-scope。
- 任何 Python 脚本 / Node / Java 工具收编：不执行（零脚本决策）。
- 国知局爬虫 / 薄封装启动器：不执行（自建检索禁区）。

## 执行后动作

- 每阶段落地后，在 ADR-0005 追加实施记录（完成项 + 偏离说明）。
- 若阶段 2 的 `.patent/` 约定与现有发明人工作流冲突，回到地图 #6 复议（用户在场裁决）。
