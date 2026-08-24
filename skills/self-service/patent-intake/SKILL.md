---
name: patent-intake
description: "brief-tight disclosure assembly or filing-set routing for self-service Chinese patents — interview four elements, dispatch drafting/drawings, assemble disclosure. Use when the user wants a technical disclosure (交底书, brief-tight) or a filing set (权利要求书/说明书)."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Intake (front door + orchestrator)

Role: **front door + orchestrator** of the self-service group. This skill routes the task, runs the interview, owns the stage checklist, and dispatches the disciplines — `../patent-drafting/`, `../patent-drawings/`, `../patent-compliance/`, `../patent-filing/`. It does not draft claims, specifications, drawings, or filing instructions, and it does not repeat patent-law explanations.

Cold start always begins here. If a route record already exists, re-enter this skill and resume from the stage checklist instead of re-routing.

## Route inputs

Collect three axes:

1. **Material source** — 口述 / 文档 (docx, pdf, pptx) / 网页 / 对谈记录 / 代码 / 其他材料 (paper, product material, technical publication). Source handling is not a set of branches: follow the unified protocol in `references/source-modes.md` (archive contract → ingestion channel → extract-confirm-fill). A paper is technical input, not automatically prior art or a complete invention disclosure.
2. **Requested deliverable**
   - **disclosure only**: technical disclosure for an agent or internal review;
   - **filing set**: claims, specification, abstract, and applicable drawings/brief description;
   - **both**: disclosure plus filing set.
   Word/docx export is **not** an automatic deliverable. At interview, agree the delivery form with the inventor — finalized `.md` drafts only (default) / docx on request / docx per an agreed template — and record it in the route record's `Word导出` axis. Generating Word files is the separately user-invoked `../word-delivery/SKILL.md`; run it only when the inventor asks in the current turn or the route record pre-agrees it.
3. **Patent type** — invention / utility model / design / undecided or possible dual filing. Use `references/type-decision.md`. Decide type only when `references/type-decision.md` provides supporting evidence; when multiple independent contributions appear, apply the singleness check in `references/source-modes.md` and confirm with the inventor via AskUserQuestion before committing.

## Routing table — one trigger per branch

| Decision | Handoff |
|---|---|
| any supplied material | source intake `references/source-modes.md` (`../conversion/SKILL.md` ingestion), then interview |
| description incomplete | disclosure interview `references/interview.md` (four elements; formula-bearing runs C) |
| invention filing set | `../patent-drafting/` → `../patent-drawings/` (full) → `../patent-compliance/` |
| utility filing set | same chain, utility branch in drafting, structural drawings mandatory |
| design filing set | design branch `references/design-points.md` → `../patent-compliance/` |
| brief-tight disclosure only | assemble `references/disclosure-document.md` (brief-tight, ≤3 formulas, 2-3 figures) + `../patent-drawings/` Disclosure branch (brief-tight); no filing gates; docx via `../word-delivery/SKILL.md` on request |
| both | filing-set route first, then brief-tight assembly from filing drafts |
| filing/rectification | `../patent-filing/SKILL.md` |

## State record

Write and maintain `草稿/申请信息.md`. A route is selected only when source, deliverable, and type are recorded; if type or material meaning remains ambiguous, ask the inventor — do not draft by guessing.

Route record:

```text
材料来源: 口述 / 文档 / 网页 / 对谈记录 / 代码 / 其他材料
材料位置: …
交付目标: 交底书 / 申请文件套件 / 两者
Word导出: 未约定(按需,默认) / 已约定(时机/模板)
申请类型: 发明 / 实用新型 / 外观设计 / 一案两请 / 待确认
待确认事项: …
模板: 项目默认 / 指定模板 / 无
横切标志: 公开状态=… / 语言纯度=… / 数据可用性=… / 图可用性=… / 多贡献风险=…
```

`Word导出` records the delivery-form agreement: by default no Word files are generated — the pipeline completes at self-checked `.md` drafts and docx is exported only when the inventor asks (`../word-delivery/SKILL.md`).

Stage checklist (the resume mechanism — update it, never infer progress from which files exist):

```text
## 阶段清单
- [ ] 摄入  (materials archived under .patent/materials/ + source registry)
- [ ] 路由  (three axes recorded)
- [ ] 访谈  (four elements or design points recorded)
- [ ] 权利要求
- [ ] 说明书
- [ ] 附图
- [ ] 自检  (report at 草稿/检查报告.md)
- [ ] 交付  (.md 定稿；docx 仅当 Word导出 已约定或发明人当场要求)
- [ ] 递交
```

Each discipline updates its own stage to ✓ when its completion standard passes, and to `blocked: <reason>` when it stops. Disclosure-only routes mark 摄入/路由/访谈/交付; design routes mark 摄入/路由/访谈(设计要点)/自检/交付/递交. Blockers are explicit: when a core fact is missing (e.g. an undefined formula boundary), record it and pause only the affected part — never fill by invention.

## Workspace layout

In the inventor's project (the directory is a **workspace name, not a skill name**): drafts under `patent-application/草稿/`, figures under `patent-application/附图/` (`源文件/` .dot sources + original external figures as received, `预览/` svg, `嵌入/` png), deliverables under `patent-application/成品/`; support layer `.patent/` (`sources/` citation lists, `materials/` inventor materials, `queries/` search records). Keep `草稿/` for editable drafts and `成品/` for regenerable exports as separate directories.

## Sequence

### 1. Source intake → archived material

Follow `references/source-modes.md`: archive the source as-is, register provenance, run the extract-confirm-fill protocol, and set the five cross-cutting flags in the route record. Documents are ingested through `../conversion/SKILL.md`.

### 2. Interview → four elements (or design points) complete

For invention / utility model, read `references/interview.md` and record the four elements: technical problem; minimally implementable technical solution; distinguishing feature; technical effect and its evidence. For a formula-bearing case, complete the core-formula questions in that reference — the model may normalize confirmed material, but must not invent a core formula or experimental result. For design, use `references/design-points.md` instead of the four-element interview.

Ask about disclosure status and preserve the inventor's source trail. Prior-art search is optional: `references/search-guide.md` + `../patents-search/` before drafting the background art.

### 3. Dispatch — only the requested branch, brief-tight stays tight

- Filing set, invention/utility: `../patent-drafting/SKILL.md` (spec-first, tight not required) → `../patent-drawings/SKILL.md` full routing.
- Design: `references/design-points.md`.
- brief-tight disclosure only: `references/disclosure-document.md` (≤3 formulas, 2-3 figures, template structure) + `../patent-drawings/SKILL.md` Disclosure branch. No `patent-drafting`/`patent-compliance` on this branch; rights and abstract stay in filing track.

Each discipline owns its own completion standard and updates the stage checklist.

### 4. Self-check → zero unresolved criticals

Read `../patent-compliance/SKILL.md`. Run only the checks applicable to the selected type and deliverable; the report lands at `草稿/检查报告.md`. **Back edges are this skill's job**: route each unresolved critical back to the discipline that owns the artifact (`../patent-drafting/` for claims/specification support chains, `../patent-drawings/` for numeral/figure mismatches), then re-check. Return blockers to the inventor instead of silently filling them.

### 5. Assemble and deliver

The pipeline's default completion point is **finalized `.md` drafts**: assembly per `references/disclosure-document.md` (for the consolidated disclosure) plus zero unresolved criticals from step 4. Confirm the delivery form with the inventor. Generate Word files **only** when the inventor asks in the current turn or the route record says `Word导出: 已约定` — then read `../word-delivery/SKILL.md` for conversion chains, template reuse, formula conversion, and the acceptance gate.

Revision requests after delivery follow the single-source rule: edits land in the owning draft under `草稿/`, affected checks re-run, then `../word-delivery/SKILL.md` regenerates — never hand-edit a delivered `.docx`.

### 6. Filing guidance, only when requested

Hand off to `../patent-filing/SKILL.md`. Load filing guidance from `../patent-filing/SKILL.md` when the route record marks filing as requested; otherwise keep drafting focused on the current track.

## Single pointers — disclosed references (load only when branch fires)

- brief-tight disclosure assembly: `references/disclosure-document.md`
- type choice: `references/type-decision.md`
- source intake + five flags: `references/source-modes.md`
- design views: `references/design-points.md`
- search (optional, before background art): `references/search-guide.md` + `../patents-search/`
- standards (file index, not body): `../patent-standards/SKILL.md`

## Boundaries

- Case facts, papers, formulas, citations, and experimental results belong to the project support workspace and drafts, never to this skill's files.
- Invoke only the disciplines required by the deliverable and type recorded in the route; other branches remain dormant until the route asks for them.
- Disciplines are never called sideways by each other — handoffs happen through artifact files and this orchestrator.

## Completion standard

- [ ] Route record exists and is respected; stage checklist kept current
- [ ] Source archived with provenance; five cross-cutting flags set
- [ ] Only the selected type and deliverable branches ran
- [ ] Four elements or design points recorded; no invented material
- [ ] Self-check report exists with no unresolved criticals; back edges routed and re-checked
- [ ] Delivery form agreed with the inventor and recorded (`Word导出` axis); if Word was requested, output passed the acceptance gate in `../word-delivery/SKILL.md`, or the degradation/blocker report was delivered
