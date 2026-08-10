# Patent Writing Skill Hub

A hub of agent skills (`.agents/skills/`) for writing patent applications, built **delegation-first**: the set owns only authoring/decision logic; every legal assertion traces to a declared authoritative source, every prior-art reference comes from an external search tool — never model improvisation.

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
