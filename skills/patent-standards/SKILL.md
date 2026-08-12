---
name: patent-standards
description: The standards catalog (专利标准/资料目录) for the patent-writing skill set — a thin index declaring which authoritative CN/US texts exist, where they live, and which per-type anchor file governs each patent type. 内容按类型拆分在 references/(发明/实用新型、外观设计、US、目录),锚点条号均对 CNIPA/USPTO 官方全文实测核实(2026-08-11 发明/实用新型,2026-08-12 外观设计)。Consumed by the self-service skills (patent-application, patent-claims, patent-specification, patent-drawings, patent-compliance, patent-filing) and the professional US skills. Declares WHAT exists and where — never fetches, never holds keys, never prescribes how to retrieve.
---

# Patent Standards (专利标准/资料目录)

The catalog of authoritative texts governing patent drafting and examination in CN and US, plus the citation discipline every writing skill follows. This skill is a **declaration**, not a retrieval tool: it says what exists and where; the environment's tools do the actual reading.

## 引用文件(按类型取用,不整包加载)

| 文件 | 内容 | 消费方 |
|---|---|---|
| `references/cn-invention-utility.md` | 发明/实用新型锚点:专利法(第2/9/22/24/26/33/42条)、细则(第17/20-26/43/46/47条)、指南(第一部分第二章、第二部分第二/三/四/五/九章) | patent-application(发明/实用新型)、patent-claims、patent-specification、patent-drawings(附图部分)、patent-compliance(检查1-7)、patent-filing(发明/实用新型部分) |
| `references/cn-design.md` | 外观设计锚点:专利法(第2条第4款/23/27/31条第2款/33条第2款/42条)、细则(第30/31/32/40/43/44/53/57条第2款/58条第2款)、指南(第一部分第三章 4.2-4.5) | patent-application(外观分支)、patent-drawings(外观附图节)、patent-compliance(检查项8)、patent-filing(外观要点) |
| `references/us.md` | US 锚点:35 U.S.C.(§100-112/251)、37 CFR Part 1(§1.57-1.121)、MPEP(§608/706/2106/2163/2164/2171-2176) | 专业组(professional/US 技能,当前隐藏) |
| `references/catalog.md` | CN/US 权威文本目录(官方位置、版本、版次摘要)+ 声明外部源(CNIPA 公布公告系统) | 需要源信息/外部源条目时 |

锚点核实:发明/实用新型 2026-08-11、外观设计 2026-08-12 对 CNIPA 官方全文实测;US 2026-08-10 对官方源核实。证据见 `../../docs/research/standards-catalog.md` 与 `../../docs/research/design-patent-anchors.md`。**Skills must cite the per-type anchors — not chapter-level approximations — and never renumber from memory.**

## How writing skills invoke this skill

Two consumption modes (ADR-0004):

- **自服务组(`skills/self-service/`)**:按类型读对应 references 文件,引用其中的条号作为锚点(如 `细则第20条`),需要向发明人解释时说明来源。不声明 `[STANDARD]` 需求、不强求环境检索法条;现有技术按诚实红线(三类素材)处理,见 `../../docs/prototype/delegation-contract.md` 的"自服务组简化变体"节。
- **专业组(`skills/professional/`,US 技能,当前隐藏)**:读 `references/us.md`(内含完整纪律 declare/consume/cite/fail loud/never invent),按其中纪律执行。

## The discipline — four clauses, one prohibition (专业组完整版)

> 专业组完整纪律(declare/consume/cite/fail loud/never invent)执行版在 `references/us.md`,来源契约 `../../docs/prototype/delegation-contract.md`。

## 自服务组纪律(简化版)

自服务技能引用本目录时遵守:

1. **锚点**:按类型读 `references/cn-invention-utility.md` / `references/cn-design.md`,引用其中实测核实的条号,不凭记忆编号。
2. **诚实红线**:现有技术只写三类素材 — 发明人已知方案 / 客观通用问题 / 检索工具真实返回。绝不编造专利号、文献、实验数据。
3. **Fail loud**:缺输入(如四要素不齐)、缺工具(如无 dot)时明说缺什么,不硬写。
4. **范围外**:OA 答复等专业工作不在本包。

## Scope guard

- CN + US only. EP/PCT, other jurisdictions: out of scope of this skill set.
- This skill declares what exists; it is not a search tool, not a corpus, not a knowledge base.
