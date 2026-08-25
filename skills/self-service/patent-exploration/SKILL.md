---
name: patent-exploration
description: "Explore patent content before drafting — deep-read any material (paper, disclosure, notes, existing patent), deconstruct the technology, mine patentable points, and discuss protection directions Socratically. Use when the user wants to understand, discuss, or research what is patentable in a piece of content before entering the intake/drafting pipeline."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Exploration — 内容研讨 (Content Lab)

Role: **content lab** of the self-service group. This skill sits **before** `../patent-intake/SKILL.md` and answers one question: *what in this content is worth patenting, and how?* It does not draft claims, specifications, or file anything — it produces understanding that makes the later intake interview fast and accurate.

Existing pipeline is `材料 → 四要素 → 说明书 → 权利要求` (normative). This skill inserts the missing loop: `内容 → 读懂 → 拆透 → 讨论 → 可专利点` (exploratory). When exploration is done, it hands a clean handover package to `patent-intake`.

## When to use

- User gives a paper, PPT, disclosure draft, existing patent, experiment log, or scattered notes and asks "这里面什么能申请专利？"
- User wants to discuss/research a technical idea before committing to a filing type or claim direction.
- User wants a patentability brainstorm without yet writing a formal disclosure.
- User says "先聊聊这个技术" / "帮我看看这篇论文的专利点" / "这个想法值得写吗"。

If the user already has a settled four-element record and wants to draft, go directly to `../patent-intake/SKILL.md`.

## The core distinction

| Normative (intake/drafting) | Exploratory (this skill) |
|---|---|
| 填对四要素、写对格式 | 读懂内容、拆透技术 |
| 收敛：一个答案 | 发散→收敛：多条路径再选最优 |
| 问"是什么" | 问"为什么是这个、还能是什么" |
| 产出：符合审查的文档 | 产出：判断与方向 |

This skill stays on the right column. It never enforces claim form, figure numerals, or filing deadlines — those belong to `../patent-drafting/SKILL.md` and `../patent-compliance/SKILL.md`.

## Inputs — any content form (内容不挑形态)

Any of these is a valid entry, single or combined:

- 论文 (paper, preprint, with or without code)
- 技术交底材料 (docx/pptx/pdf, even incomplete)
- 现有专利/申请 (yours or others')
- 实验记录、会议纪要、口述、网页、技术博客、代码片段

All sources follow one ingestion rule: see `references/source-handling.md`. Archive as-is under `.patent/materials/`, register provenance, then convert to Markdown for discussion. The skill never infers "this paper = prior art against you" — a paper is technical input first.

## Two modes — one skill

The user does not need to declare a mode upfront; the agent picks the entry point and can switch mid-session.

### Mode A — Mining (挖掘): material in → points out

For "我给你一份材料，帮我看看":

1. **Ingest** — archive + convert (via `../conversion/SKILL.md` discipline, zero scripts). See `references/source-handling.md`.
2. **Map** — build a content map so both sides see the same territory. See `references/content-map.md`.
3. **Deconstruct** — extract problem / means / effect triples and technical lineage. See `references/deconstruction.md`.
4. **Mine** — generate the patentable-point matrix: core / peripheral / defensive, each with generalizability. See `references/mining-matrix.md`.
5. **Gap** — optional prior-art gap pass: what does this content add beyond what is already known? Delegates to `../patents-search/SKILL.md` and `references/search-guide.md` in `../patent-intake/references/` when requested; never fabricates citations.
6. **Direction** — propose 1–3 protection directions with trade-offs; ask the user to pick. See `references/handover.md`.

Done when: `references/handover.md` handover package exists under `.patent/exploration/`.

### Mode B — Socratic (研讨): idea in → clarity out

For "我有一个想法，先聊聊":

Run the Socratic loop defined in `references/discussion.md`:

- Ask one question at a time (`AskUserQuestion`), challenge assumptions, offer counter-examples, propose alternatives.
- Never lecture; never dump a 10-point list without interaction.
- Each round ends with a one-sentence summary of what was agreed, so the user can see progress.
- Exit the loop when the user says "可以了" / "先到这里" or when the deconstruction stabilizes.

The loop can start from zero material (pure dialogue) or from a content map produced by Mode A.

## Workflow — the exploration loop

```text
ingest → map → deconstruct ⇄ discuss (Socratic) → mine → gap? → direction → handover → intake
              └─────────────── ask_user_question each turn ──────────────┘
```

- `ingest → map → deconstruct` is the fast path (one pass, ~1 turn each).
- `deconstruct ⇄ discuss` is the iterative core; expect 2–5 rounds.
- `mine → direction` converges; do not expand again after direction is agreed.
- `handover` is the gate to `patent-intake`: write `.patent/exploration/研讨纪要.md` and `.patent/exploration/可专利点清单.md`, then offer `是否现在进入 patent-intake 定四要素？`

## Output — handover package (not a filing set)

All outputs land under `.patent/exploration/` (exploration workspace, sibling to `.patent/materials/`):

| File | Purpose |
|---|---|
| `内容地图.md` | What the content says, in the user's language, section by section |
| `技术拆解.md` | Problem/means/effect triples + lineage + boundary conditions |
| `可专利点清单.md` | Patentable-point matrix with generalizability and fallback hints |
| `研讨纪要.md` | Socratic discussion log: questions asked, answers given, decisions made |
| `保护方向建议.md` | 1–3 directions with scope/breadth/risk trade-offs |

These are **exploration artifacts**, not `drafts/技术交底书.md`. The handover step in `references/handover.md` converts the agreed direction into the intake-ready four-element stub.

## Boundaries

- Does not draft `权利要求书` / `说明书` / `摘要` — dispatch to `../patent-drafting/SKILL.md` via `../patent-intake/SKILL.md`.
- Does not do compliance checks — that is `../patent-compliance/SKILL.md`.
- Does not file — that is `../patent-filing/SKILL.md`.
- Does not fabricate citations or prior-art conclusions. Every "known vs new" statement traces to archived material or a declared `patents-search` result; uncertain = mark as `待查新`.
- One exploration = one content thread. If the user brings a second unrelated paper, start a new `内容地图` rather than merging.

## Pointers — load only when the step fires

- `references/source-handling.md` — unified ingestion for any content form
- `references/content-map.md` — how to map content without copying paper structure
- `references/deconstruction.md` — problem/means/effect extraction
- `references/mining-matrix.md` — patentable-point matrix
- `references/discussion.md` — Socratic discussion protocol
- `references/handover.md` — handover gate to patent-intake

Cross-group pointers (flat install geometry, verify after `npx skills add`):

- `../conversion/SKILL.md` — document → Markdown discipline
- `../patents-search/SKILL.md` — optional delegated search
- `../patent-intake/references/search-guide.md` — search landing convention
- `../patent-intake/references/type-decision.md` — when type becomes clear during exploration
- `../patent-standards/references/cn-invention-utility.md` — standards anchor (read on demand, never copy into exploration artifacts)
