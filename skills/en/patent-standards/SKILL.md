---
name: patent-standards
description: The standards catalog (专利标准/资料目录) for the patent-writing skill set — a thin index declaring which authoritative CN/US texts exist, where they live, and which per-type anchor file governs each patent type. Content is split by type under references/ (invention / utility model, design, US, catalog); anchor article numbers were verified against the official CNIPA/USPTO full texts (2026-08-11 invention / utility model, 2026-08-12 design). Consumed by the self-service skills (patent-application, patent-claims, patent-specification, patent-drawings, patent-compliance, patent-filing) and the professional US skills. Declares WHAT exists and where — never fetches, never holds keys, never prescribes how to retrieve.
---

# Patent Standards (专利标准/资料目录)

The catalog of authoritative texts governing patent drafting and examination in CN and US, plus the citation discipline every writing skill follows. This skill is a **declaration**, not a retrieval tool: it says what exists and where; the environment's tools do the actual reading.

## Reference files (consume per type, never load the whole package)

| File | Content | Consumers |
|---|---|---|
| `references/cn-invention-utility.md` | Invention / utility-model anchors: 专利法 (第2/9/22/24/26/33/42条), 细则 (第17/20-26/43/46/47条), 指南 (第一部分第二章, 第二部分第二/三/四/五/九章) | patent-application (invention / utility model), patent-claims, patent-specification, patent-drawings (drawings part), patent-compliance (checks 1-7), patent-filing (invention / utility-model parts) |
| `references/cn-design.md` | Design anchors: 专利法 (第2条第4款 / 23 / 27 / 31条第2款 / 33条第2款 / 42条), 细则 (第30/31/32/40/43/44/53/57条第2款 / 58条第2款), 指南 (第一部分第三章 4.2-4.5) | patent-application (design branch), patent-drawings (design drawings section), patent-compliance (check 8), patent-filing (design points) |
| `references/us.md` | US anchors: 35 U.S.C. (§100-112 / 251), 37 CFR Part 1 (§1.57-1.121), MPEP (§608 / 706 / 2106 / 2163 / 2164 / 2171-2176) | professional group (professional / US skills, currently hidden) |
| `references/catalog.md` | CN/US authoritative-text catalog (official location, edition, edition summary) + declared external source (CNIPA Publication & Announcement System) | when source info / external-source entries are needed |

Anchor verification: invention / utility model 2026-08-11, design 2026-08-12, both tested against the official CNIPA full texts; US 2026-08-10 verified against official sources. Evidence: `../../../docs/research/standards-catalog.md` and `../../../docs/research/design-patent-anchors.md`. **Skills must cite the per-type anchors — not chapter-level approximations — and never renumber from memory.**

## How writing skills invoke this skill

Two consumption modes (ADR-0004):

- **Self-service group (`skills/en/self-service/`)**: read the corresponding reference file per type, cite its article numbers as anchors (e.g. `细则第20条`), and state the source when explaining to the inventor. Do not declare `[STANDARD]` requirements, do not force the environment to fetch statutes; prior art follows the honesty red line (three kinds of material), see the "self-service simplified variant" section of `../../../docs/prototype/delegation-contract.md`.
- **Professional group (`skills/en/professional/`, US skills, currently hidden)**: read `references/us.md` (it contains the full discipline declare / consume / cite / fail loud / never invent) and follow it.

## The discipline — four clauses, one prohibition (professional full version)

> The executable version of the professional discipline (declare / consume / cite / fail loud / never invent) lives in `references/us.md`; source contract `../../../docs/prototype/delegation-contract.md`.

## Self-service discipline (simplified version)

Self-service skills referencing this catalog follow:

1. **Anchors**: read `references/cn-invention-utility.md` / `references/cn-design.md` per type, cite the verified article numbers, never number from memory.
2. **Honesty red line**: prior art only from the three kinds of material — known prior solutions / objective common problems / real search-tool results. Never invent patent numbers, references, or experimental data.
3. **Fail loud**: when input is missing (e.g. incomplete four elements) or a tool is missing (e.g. no dot), state exactly what is missing — don't force output.
4. **Out of scope**: professional work such as OA responses is not in this package.

## Scope guard

- CN + US only. EP / PCT, other jurisdictions: out of scope of this skill set.
- This skill declares what exists; it is not a search tool, not a corpus, not a knowledge base.
