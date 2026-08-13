# ADR-0007: 专业组（A 组）接入：技能集与整合方案

- 状态:Accepted (2026-08-13)
- 取代/关联:ADR-0004(self-service 包定位,A 组未来接入 — 本 ADR 落实其方向);ADR-0005(模式 D 归档为 professional/ 参考 — 本 ADR 启用评估);ADR-0003(委托优先,仍有效);wayfinder 地图 [专业组（professional，A 组）接入：决策与整合方案 #19](https://github.com/transmit-bug/patentwritter/issues/19)
- 事实底座:`docs/research/professional-agent-practice.md`(branch `research/professional-practice`)、`docs/research/pattern-d-oa-rag.md`(branch `research/pattern-d-oa-rag`)

## 背景

ADR-0004 定义 A 组（专业代理人）方向（OA 答复、三步法论证、claim 策略），预留 `skills/en/professional/`（只寄放 2 个隐藏 US 技能），「接入时放入 `professional/`，与 B 组共存」。用户提出补充 professional 组内容；经 wayfinder 地图 #19 四轮 grilling + 两张 research 票（业务实践锚点核实、模式 D 评估），确定终点 = **决策记录 + 整合方案，实现另起**。

## 决策

### 1. 技能集 = 五 discipline + 一入口（票 #22）

- 入口 `patent-prosecution`（授权链路编排，user-invoked，`disable-model-invocation: true` 同 B 组入口）。
- 五个 discipline：`patent-oa-response`（审查意见答复，旗舰）、`patent-re-exam`（复审）、`patent-invalidation`（无效，请求+答辩双向）、`patent-evaluation-report`（评价报告）、`patent-claim-strategy`（权利要求策略：保护范围 / 答复修改策略 / 分案 / 优先权）。
- 依据：2025 大纲实务科 = 撰写 / 答复 / 无效；业务实践 = OA 答复（法37，期限 4/2 个月）→ 复审（法41）→ 无效（法45-47）→ 评价报告（法66.2）。

### 2. 撰写归属：复用 B 组（票 #22）

A 组不另建独立撰写 discipline；B 组撰写技能独立可用。claim-strategy 承载专业级策略（答复修改策略 / 分案 / 优先权 / 布局），机械撰写仍走 B 组。

### 3. 贯穿性能力内嵌（票 #22）

三步法论证、检索策略、程序纪律（期限 / 举证 / 口审 / 禁反悔）按业务阶段内嵌各技能，不抽独立技能；锚点挂 patent-standards。三步法从指南II-4 3.2.1.1 重建（模式 D 未编码三步法，见 research）。检索走委托 / 外部源（B 组同款纪律）。

### 4. 目录与命名：平铺 + 功能命名，无辖区后缀（票 #23）

CN 技能平铺 `skills/en/professional/<name>/SKILL.md`（skills.sh 三级发现，`professional/` 下不开 `cn/`/`us/` 子层）；命名按功能、不携带辖区后缀。现有 `patent-application-creator-us` / `patent-claims-analyzer-us` 在实现时**去 `-us` 后缀重命名**（`patent-application-creator` / `patent-claims-analyzer`）并保持隐藏标记。

### 5. 发现模式：与 B 组同级（grilling Q7 + 票 #23）

入口 user-invoked + discipline model-invoked；US 预留技能保持 `metadata.internal: true` 隐藏。

### 6. 纪律文件：中立化共享 + 锚点分辖区（票 #23）

专业 full discipline（declare / consume / cite / fail loud / never invent）与辖区无关，抽到共享位置（patent-standards SKILL.md 专业节或 `references/professional-discipline.md`）；新建 `references/cn-professional.md` 收已核实锚点（法37 / 41 / 45-47 / 66.2，细则57.3 / 58 / 62-63 / 65-76，指南II-4 3.2.1.1 等）；`us.md` 收敛回 US 锚点；不维护两套纪律。

### 7. 边界

授权链路核心（OA 答复 / 复审 / 无效 / 评价报告 / claim 策略）入范围；FTO、专利布局、维权、许可（授权后业务）、US 组重做、专利通俗解读 / 政策嗅探 out of scope（地图 #19）。

### 8. 落地：分阶段，实现另起

整合方案见 `docs/plan/professional-integration.md`；实现由方案确认后另起 effort 执行（地图只出决策）。

## 后果

- 包形态：`professional/` 从「预留 US 隐藏组」变为「CN 专业组（已规划）+ US 预留隐藏组」；可发现技能在实现后增加。
- 无新增硬依赖：零脚本零密钥（模式 D 基建不收编，纪律纯文档）。
- 检索保持委托式：模式 D 的自建案例库 / RAG 不收编；脱敏案例档案由用户提供、环境检索。

## 实施记录

- 2026-08-13 落盘(wayfinder 地图 #19 终点达成,`docs/plan/professional-integration.md` 同步落盘)。
- 2026-08-13 实现完成(阶段 0-4 全部落地,见 `docs/plan/professional-integration.md` 执行状态):阶段 0 结构基座(专业纪律中立化 `references/professional-discipline.md` + `references/cn-professional.md` + US 技能去后缀) → 阶段 1 `patent-oa-response`(模式 D 纯文档收编,三步法从指南 II-4 3.2.1.1 重建) → 阶段 2 `patent-invalidation`(双向) → 阶段 3 `patent-re-exam` + `patent-evaluation-report` → 阶段 4 `patent-claim-strategy`(分案/优先权锚点法29-30、细则48-49 对照 CNIPA 官方全文补核)+ 入口 `patent-prosecution`。

## 未来（非本次范围）

- US 专业组重做：另起一轮；US 技能实现时按决策 4 去后缀重命名。
- 2026 大纲（675 号公告）发布后复核锚点（本次以 2025 为基线，如实标注）。
- 摘要 300 字三处文本不一致（2023 细则已删 vs 2023 指南 4.5.1 / 2025 大纲保留）：技能落地时标注并按细则为准。
