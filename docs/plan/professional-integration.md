# 整合方案：专业组（professional，A 组）接入（分阶段执行）

> **执行状态：执行中（阶段 0-2 完成）**。依据 [ADR-0007](../adr/0007-professional-group-integration.md)（2026-08-13 生效）。本文是 wayfinder 地图 [专业组（professional，A 组）接入：决策与整合方案 #19](https://github.com/transmit-bug/patentwritter/issues/19) 的终点落地物：专业组接入的**分阶段执行计划**。每阶段独立可交付、可验收；实现由**方案确认后另起 effort** 执行（地图只出决策，不实现）。

**执行前置**：本方案经用户确认后，按阶段顺序执行；每阶段完成标准达成即验收，再进入下一阶段。

---

## 阶段 0 · 结构基座（先行）

**目标**：专业组的基础结构先立起来，后续技能有处挂载。

| 项 | 内容 | 完成标准 |
|---|---|---|
| 0.1 | 纪律文件中立化：专业 full discipline（declare / consume / cite / fail loud / never invent）抽到共享位置（patent-standards SKILL.md 专业节或 `references/professional-discipline.md`） | `us.md` 不再独占纪律；两辖区引用同一纪律 |
| 0.2 | 新建 `references/cn-professional.md`：收 research 已核实锚点（法37 / 41 / 45-47 / 66.2；细则57.3 / 58 / 62-63 / 65-76；指南II-4 3.2.1.1、II-8 期限 4.10.3 / 4.11.3.2、IV、V-10） | 锚点文件存在，含核实来源与日期 |
| 0.3 | US 技能去 `-us` 后缀重命名（`patent-application-creator` / `patent-claims-analyzer`），保持 `metadata.internal: true` 隐藏 | 目录 / 命名更新，隐藏标记保留，patent-standards 索引同步 |
| 0.4 | patent-standards SKILL.md 索引更新（consumers 含 professional CN 组；引用新锚点文件）；README / AGENTS.md 同步专业组规划表述 | 索引与包说明更新 |

## 阶段 1 · patent-oa-response（旗舰，优先）

**目标**：审查意见答复技能落地；模式 D 纯文档收编（零脚本零密钥）。

| 项 | 内容 | 完成标准 |
|---|---|---|
| 1.1 | 新建 SKILL.md：输入 = 审查意见通知书 + 申请文件（独立为主；`.patent/` 可选消费）；结构化解析（通知书类型 / 期限 / 逐条缺陷 / 法条 / 对比文件号） | 流程文档化，含结构化解析步骤 |
| 1.2 | 模式 D 纯文档收编（源自 `docs/research/pattern-d-oa-rag.md`）：工作流纪律（PDF-first、先检索再生成、逐条对应、空库禁糊弄、人审闸门、脱敏）、案例笔记分类法（statutes / defect_types / strategy / outcome / compare_refs）、四步创造性反驳模板 | 收编为纪律文本；无 vendored 脚本 |
| 1.3 | 三步法论证从指南II-4 3.2.1.1 重建（锚点 `cn-professional.md`）；答复期限纪律（第一次 4 个月 / 再次 2 个月，指南II-8 4.10.3 / 4.11.3.2） | 锚点引用 + 期限内嵌 |
| 1.4 | 检索：委托 / 外部源（B 组同款纪律）；脱敏案例档案 = 用户提供目录 + 环境检索（Grep / Read） | 无自建检索、无密钥管理 |

## 阶段 2 · patent-invalidation（无效，双向）

| 项 | 内容 | 完成标准 |
|---|---|---|
| 2.1 | 请求书撰写（细则69.2）+ 答辩意见陈述书；三步法反向论证 | 双向流程文档化 |
| 2.2 | 程序纪律：口审（细则74）、举证期限、禁反悔 | 程序纪律内嵌 |
| 2.3 | 证据检索：委托 / 外部源 | 无自建检索 |

## 阶段 3 · patent-re-exam + patent-evaluation-report

| 项 | 内容 | 完成标准 |
|---|---|---|
| 3.1 | 复审请求书（法41、细则65-68；驳回后 3 个月内；前置审查 指南IV-2） | 流程文档化 |
| 3.2 | 评价报告（法66.2、细则62-63、指南V-10；开放许可须提供 法50.2；细则62 新增被控侵权人可请求） | 流程文档化 |

## 阶段 4 · patent-claim-strategy + 入口收口

| 项 | 内容 | 完成标准 |
|---|---|---|
| 4.1 | claim-strategy：保护范围设计 / 答复修改策略 / 分案 / 优先权 / 布局 | 策略纪律文档化 |
| 4.2 | 入口 `patent-prosecution`：编排五 discipline，user-invoked（`disable-model-invocation: true`） | 入口存在并引用全部 discipline |

## 验收口径

- 每技能：可循 research 锚点走通一个最小案例（如 OA 答复：输入通知书 + 申请文件 → 结构化 → 逐条草稿 → 人审闸门）。
- 网关：grounded output + fail loud——无检索 / 无材料时明确拒绝，不编造。
- 零脚本零密钥：全组无 vendored 脚本、无密钥管理。
- 摘要 300 字：标注三处文本不一致（细则已删 vs 指南 / 大纲保留），按细则为准。

## 执行主体与节奏

实现由方案确认后另起 effort；执行主体与节奏另议（参照 ADR-0005 先例）。
