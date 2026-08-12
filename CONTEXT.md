# Patent Writing Skill Hub

A skills **package** (`skills/`) for writing patent applications, installable via `npx skills add transmit-bug/patentwritter`. Built **delegation-first**: the set owns only authoring/decision logic; every legal assertion traces to a declared authoritative source, every prior-art reference comes from an external search tool — never model improvisation.

> **方向(2026-08-11,ADR-0004)**:面向发明人自助的专利申请向导(发明+实用新型,全流程)。专业代理人方向(A 组)未建,仅预留 `skills/professional/`。

> Install state (`.agents/`, `skills-lock.json`) is consumer-side and gitignored — regenerate it with `npx skills add transmit-bug/patentwritter`.

## Self-service 撰写词表

**四要素**:交底访谈必得的四个要素 — 技术问题 / 技术方案(最小可实施)/ 区别特征 / 技术效果。缺一不可进入撰写。

**删除测试**:判定必要技术特征的判据 — 删掉该特征,技术问题还解决吗?能解决 = 非必要,下沉从权或删。

**阶梯**:上位化概括的三层(具体实现 → 中间概括 → 功能概括),每上一层过三问(仍解决原问题 / 说明书有支撑 / 非纯功能限定)。

**退路**:从权 = 独权被驳时的退路;布防三方向(细化 / 变体 / 增强),按商业重要度排序。

**诚实红线**:背景技术只写三类素材 — 发明人已知的现有方案、客观通用问题、检索工具真实返回的结果。绝不编造专利号/文献/数据。

**支撑链**:每条权利要求特征在说明书有出处(专利法第26条第4款:权利要求以说明书为依据)。

**标记一致**:附图标记与说明书文字双向一致(细则第21条)。

## Language

**Patent standards (专利标准)**:
The authoritative texts governing drafting and examination — 专利法, 专利法实施细则, 审查指南 (CN); 35 USC, 37 CFR, MPEP (US). The set declares which of these exist and where they live; it never vendors them and never restates them from memory.
_Avoid_: rules, best practices

**Standards catalog (资料目录)**:
The core content of the patent-standards skill — a table declaring each authoritative material: official name, edition, official location, what it governs, citation anchors. It declares **what** to look up, never **how** ("我们只能声明哪些资料可以去查找,不应该负责具体如何去查找").
_Avoid_: retrieval instructions, fetch commands

**Delegated search (委托搜索)**:
Prior-art lookup performed by external tools — patents-search/Valyu or whatever the environment exposes. The set consumes search results and cites them; it never builds search, never manages keys, never declares which backend is core.
_Avoid_: in-repo harness, 自建搜索

**Prior art (先有技术)**:
Existing patents and publications that a claim must be novel and non-obvious over. Sourced exclusively from delegated search results or user-supplied material; never invented or recalled.
_Avoid_: 已有技术, made-up references

**Thin skill (薄技能)**:
A writing skill that owns only its authoring/decision logic and consumes the catalog + delegated search. Produces **grounded output** or refuses.
_Avoid_: monolithic skill

**Grounded output**:
Skill output where each standards assertion cites the declared source (e.g. 审查指南 Part II, MPEP 2106) as retrieved, and each prior-art reference points to a real delegated search result.
_Avoid_: uncited output, plausible-sounding law

**Fail loud**:
When no retrieval tool is available in the environment, a skill refuses to draft and states exactly which grounding it could not obtain. No output is better than unverified patent text.
_Avoid_: drafting with made-up grounding

**Citation convention**:
The agreed format for referencing catalog sources and search results in skill output — fixed by the prototype ticket; every writing skill follows it.
_Avoid_: informal references, no anchors

**Declared external source (声明外部源)**:
A human-operated source the set documents but never automates — e.g. CNIPA 公布公告系统 (epub.cnipa.gov.cn), Google Patents. The docs state source info, manual search steps, and citation anchors (公开号/公告号); the set never ships crawler code for it. Peer-level with delegated tools (Valyu), not a fallback ladder.
_Avoid_: in-repo crawler, thin wrapper scripts, 爬虫

**Document-only capability (纯文档能力)**:
A capability delivered as skill prose + inline-generation guidance rather than vendored scripts — e.g. Word delivery, docx/pptx intake. The agent probes the environment (python-docx → pandoc → manual save) and degrades; no script is committed to the package.
_Avoid_: vendoring conversion scripts, hard tool dependencies

**Archived reference (归档参考)**:
External design kept as reference material for a future skill group without changing the current package boundary — e.g. 审查答复 (OA case-RAG) archived for the future professional/ group.
_Avoid_: expanding current scope with archived designs

**`.patent/` workspace (支撑层工作目录)**:
The tiered support layer under the inventor's project root: `sources/` (declarations, citation lists), `materials/` (inventor materials, retrieved documents), `queries/` (search records and results). Draft application files stay in the visible `patent-application/`; `.patent/` is suggested gitignored.
_Avoid_: mixing support layer into draft directory
