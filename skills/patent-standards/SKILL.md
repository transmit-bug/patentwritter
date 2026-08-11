---
name: patent-standards
description: The standards catalog (专利标准/资料目录) and citation discipline for the patent-writing skill set. Declares which authoritative texts govern CN and US patent drafting/examination, where they officially live, and their citation anchors. Consumed by the writing skills (patent-application-creator, patent-architect, patent-claims-analyzer, patent-diagram-generator) to ground every legal assertion. This skill declares WHAT exists and where — it never fetches, never holds keys, and never prescribes how to retrieve.
---

# Patent Standards (专利标准/资料目录)

The catalog of authoritative texts governing patent drafting and examination in CN and US, plus the citation discipline every writing skill follows. This skill is a **declaration**, not a retrieval tool: it says what exists and where; the environment's tools do the actual reading.

## The catalog

Verified against primary sources on 2026-08-10 (full per-fact provenance: `../../docs/research/standards-catalog.md` — read it for verification detail).

### China — the 2023 package (one body, effective 2024-01-20)

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 专利法 | As amended 2023-12-29 (8 chapters, 82 articles) | flk.npc.gov.cn (国家法律法规数据库) | 专利法 第X条 — drafting-relevant: 第2条(定义), 第22条(新颖性/创造性/实用性), 第25条(不授予专利权), 第26条(申请文件/说明书/权利要求书), 第59条(保护范围) |
| 专利法实施细则 | 2023年修订 (国务院令第769号, 13章149条) | gov.cn 令769号 / cnipa.gov.cn | 实施细则 第X条 — drafting-relevant: 第17条(申请文件), 第20条(说明书), 第26条(摘要), 第33条(宽限期) |
| 专利审查指南 | 2023 edition (局令第78号, six parts) | cnipa.gov.cn (局令第78号页 + 全文PDF) | 指南 第X部分第X章 — drafting-relevant: 第一部分第三章(权利要求书), 第二部分第二章(说明书和权利要求书), 第二部分第三章(新颖性), 第二部分第四章(创造性), 第二部分第五章(实用性), 第二部分第九章(计算机程序) |

### United States

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 35 U.S.C. | Current through Pub. L. 119-102 (2026-07-12); print 2024 Main Ed. | uscode.house.gov / govinfo.gov | 35 U.S.C. §101/§102/§103 (Ch.10), §112 (Ch.11) |
| 37 C.F.R. Title 37 | eCFR current (amended 2026-07-20) | ecfr.gov (Part 1) | 37 CFR §1.71(说明书), §1.75(权利要求), §1.77(申请文件排列), §1.104(审查), §1.121(修改) |
| MPEP | 9th Ed., Rev. 01.2024 (current to 2024-01-31) | uspto.gov (mpep/index.html) | MPEP §608(公开内容/权利要求格式), §706(驳回), §2106(客体适格), §2164(能够实现), §2171-2176(112(b) 清楚性) |

## The discipline — four clauses, one prohibition

Writing skills apply the delegation contract (`../../docs/prototype/delegation-contract.md`) when they consume this catalog:

1. **Declare** — before a legal assertion, name the need: `[STANDARD] <jurisdiction> <topic>`. Look up the governing material + anchor in this catalog, then have the environment read that material. Never fetch it yourself.
2. **Consume** — ground only on what was actually read.
3. **Cite** — every assertion in output carries the anchor: `(依据: 指南 第二部分第四章[创造性] — cnipa.gov.cn)` / `(per MPEP §2106 — uspto.gov)`.
4. **Fail loud** — if the material can't be read, emit the 无法获取依据 block and don't draft that portion.
5. **Never invent** — never restate law from memory; the catalog's material is the only authority.

## How writing skills invoke this skill

- Read this catalog for the material + anchor of any `[STANDARD]` need.
- Reference `../../docs/research/standards-catalog.md` for official URLs and verification.
- Do NOT ask this skill to fetch, download, or parse anything — the environment does that.

## Scope guard

- CN + US only. EP/PCT, other jurisdictions: out of scope of this skill set.
- This skill declares what exists; it is not a search tool, not a corpus, not a knowledge base.
