---
name: patent-intake
description: "disclosure assembly or filing-set routing for self-service Chinese patents — interview four elements, dispatch drafting/drawings, assemble a self-contained disclosure in appropriate engineering prose. Use when the user wants a technical disclosure (交底书) or a filing set (权利要求书/说明书)."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Intake (front door + orchestrator)

Role: **front door + orchestrator** of the self-service group. This skill routes the task, runs the interview, owns the stage checklist, and dispatches the disciplines — `../patent-drafting/`, `../patent-drawings/`, `../patent-compliance/`, `../patent-filing/`. It does not draft claims, specifications, drawings, or filing instructions, and it does not repeat patent-law explanations.

Cold start always begins here. A project may hold several applications: each lives in its own directory under `patents/`, named after the application (see "Workspace layout"). If a route record already exists in one of them, re-enter that case and resume from the stage checklist instead of re-routing; if several case directories exist, ask the inventor via AskUserQuestion whether to resume an existing case or open a new one.

## Route inputs

Collect four axes (source × deliverable × type × target product):

1. **Material source** — oral / document (docx, pdf, pptx) / web page / conversation transcript / code / other material (paper, product material, technical publication). Source handling is not a set of branches: follow the unified protocol in `references/source-modes.md` (archive contract → ingestion channel → extract-confirm-fill). A paper is technical input, not automatically prior art or a complete invention disclosure.
2. **Requested deliverable**
   - **disclosure only**: technical disclosure for an agent or internal review;
   - **filing set**: claims, specification, abstract, and applicable drawings/brief description;
   - **both**: disclosure plus filing set.
   Word/docx export is **not** an automatic deliverable. At interview, agree the delivery form with the inventor — finalized `.md` drafts only (default) / docx on request / docx per an agreed template — and record it in the route record's `word-export` axis. Generating Word files is the separately user-invoked `../word-delivery/SKILL.md`; run it only when the inventor asks in the current turn or the route record pre-agrees it.
3. **Patent type** — invention / utility model / design / undecided or possible dual filing. Use `references/type-decision.md`. Decide type only when `references/type-decision.md` provides supporting evidence; when multiple independent contributions appear, apply the singleness check in `references/source-modes.md` and confirm with the inventor via AskUserQuestion before committing.
4. **Target product — constrained output** — the concrete product/method/system the patent protects (e.g., "application-aware scheduling method", "UAV onboard system", "scheduling framework"). This constrains the entire drafting: every claim, embodiment, and figure must trace to this product; vague "AI technology" is not a product. **Title rule**: record it verbatim as `一种<基于/面向><核心手段>的<对象+效果>方法`（及系统可选），15–30字，不用`之`、不用英文缩写，详见 `references/disclosure-document.md` 发明名称规范；该字符串即 `application-info.md` 的发明名称与 `drafts/技术交底书.md` 的 `#` 标题，二者逐字一致。When unclear, ask via AskUserQuestion and block drafting until confirmed.

## Routing table — one trigger per branch

| Decision | Handoff |
|---|---|
| any supplied material | source intake `references/source-modes.md` (`../conversion/SKILL.md` ingestion), then interview |
| description incomplete | disclosure interview `references/interview.md` (four elements; formula-bearing runs C) |
| invention filing set | `../patent-drafting/` → `../patent-drawings/` (full) → `../patent-compliance/` |
| utility filing set | same chain, utility branch in drafting, structural drawings mandatory |
| design filing set | design branch `references/design-points.md` → `../patent-compliance/` |
| disclosure only | assemble `references/disclosure-document.md` (推荐按 `references/8-points.md` 8要点完整展开，未展开需豁免说明) + `../patent-drawings/` disclosure branch + `../patent-compliance/` 轻量门禁（标题白名单+洁净）; docx via `../word-delivery/SKILL.md` on request |
| both | filing-set route first, then disclosure assembly from filing drafts |
| filing/rectification | `../patent-filing/SKILL.md` |

## State record

Write and maintain `drafts/application-info.md`. A route is selected only when source, deliverable, type, **and target product** are recorded; if type, target product, or material meaning remains ambiguous, ask the inventor — do not draft by guessing.

Route record:

```text
material-source: oral / document / web page / transcript / code / other
material-location: …
deliverable: disclosure / filing-set / both
word-export: not-agreed(on-demand,default) / agreed(timing/template)
patent-type: invention / utility-model / design / dual-filing / undecided
target-product: …(constrained output, e.g. application-aware scheduling method/system for UAV navigation)
open-questions: …
template: project-default / specified / none
cross-cutting flags: 公开状态=… / 语言纯度=… / 数据可用性=… / 图可用性=… / 多贡献风险=…
```

The `word-export` field records the delivery-form agreement: by default no Word files are generated — the pipeline completes at self-checked `.md` drafts and docx is exported only when the inventor asks (`../word-delivery/SKILL.md`).

Stage checklist (the resume mechanism — update it, never infer progress from which files exist):

```text
## Stage checklist
- [ ] intake   (materials archived under .patent/materials/ + source registry)
- [ ] route    (four axes recorded)
- [ ] interview (four elements or design points recorded)
- [ ] claims
- [ ] specification
- [ ] drawings
- [ ] self-check (report at drafts/check-report.md)
- [ ] delivery (.md finalized; docx only when word-export is agreed or the inventor asks in-turn)
- [ ] filing
```

Each discipline updates its own stage to ✓ when its completion standard passes, and to `blocked: <reason>` when it stops. Disclosure-only routes mark intake/route/interview/delivery; design routes mark intake/route/interview(design-points)/self-check/delivery/filing. Blockers are explicit: when a core fact is missing (e.g. an undefined formula boundary), record it and pause only the affected part — never fill by invention.

## Workspace layout

Multi-case projects are hierarchical — **one directory per application under `patents/`, named after the application**: use the target product recorded at routing as the directory name. Path-hostile characters (`/` `\` `:` and similar) are dropped or collapsed so the name stays one directory segment (e.g. target product "…scheduling method/system" → directory `…scheduling-method-system`). The name **freezes once routing completes**; later title revisions change `drafts/application-info.md` only, never the directory name.

All case paths below resolve against this **case root** `patents/<patent-name>/`. Inside it: drafts under `drafts/`, figures under `figures/` (`source/` .dot sources + original external figures as received, `preview/` svg, `embed/` png), deliverables under `deliverables/`; support layer `.patent/` (`sources/` citation lists, `materials/` inventor materials, `queries/` search records) lives **inside the case root**, so each case directory is self-contained and can be archived or handed over as a unit. Keep `drafts/` for editable drafts and `deliverables/` for regenerable exports as separate directories.

Create the case root at the end of the routing stage, when all four axes are recorded; until then keep working notes outside `patents/`. The `.patent/` support workspace belongs to its case — never share materials or sources across case roots.

## Sequence

### 1. Source intake → archived material → Done when: source archived under `.patent/materials/` with provenance in `drafts/application-info.md` and five cross-cutting flags set

Follow `references/source-modes.md`: archive the source as-is, register provenance, run the extract-confirm-fill protocol, and set the five cross-cutting flags in the route record. Documents are ingested through `../conversion/SKILL.md`.

### 2. Interview → four elements (or design points) complete → Done when: four elements (or design points) recorded in `drafts/application-info.md` with no invented core formula, disclosure status preserved, and search-guide optionally consulted

For invention / utility model, read `references/interview.md` and record the four elements: technical problem; minimally implementable technical solution; distinguishing feature; technical effect and its evidence. For a formula-bearing case, complete the core-formula questions in that reference — the model may normalize confirmed material, but must not invent a core formula or experimental result. For design, use `references/design-points.md` instead of the four-element interview.

Ask about disclosure status and preserve the inventor's source trail. Prior-art search is optional: `references/search-guide.md` + `../patents-search/` before drafting the background art.

### 3. Dispatch — only the requested branch → Done when: only the route-record branch ran and each discipline updated its stage in `drafts/application-info.md` (✓ or `blocked: <reason>`)

- Filing set, invention/utility: `../patent-drafting/SKILL.md` (spec-first) → `../patent-drawings/SKILL.md` full routing.
- Design: `references/design-points.md`.
- disclosure only: `references/disclosure-document.md` (推荐按 `references/8-points.md` 8要点完整展开，未展开需豁免说明) + `../patent-drawings/SKILL.md` disclosure branch + `../patent-compliance/SKILL.md` 轻量门禁（标题白名单+洁净）。No `patent-drafting` on this branch; rights and abstract stay in filing track.

Each discipline owns its own completion standard and updates the stage checklist.

### 4. Self-check → zero unresolved criticals → Done when: `drafts/check-report.md` exists with 0 `critical` (or all `critical` routed back and re-checked) and `self-check` stage updated

Read `../patent-compliance/SKILL.md`. 递交轨运行全量检查，披露轨运行轻量门禁（标题白名单+洁净+溯源收敛+图一致）；报告落 `drafts/check-report.md`。未过不标 `self-check ✓`。**Back edges are this skill's job**: route each unresolved critical back to the discipline that owns the artifact (`../patent-drafting/` for claims/specification support chains, `../patent-drawings/` for numeral/figure mismatches, 披露轨标题/洁净问题回 `references/disclosure-document.md` 组装), then re-check. Return blockers to the inventor instead of silently filling them.

### 5. Assemble and deliver → Done when: `drafts/技术交底书.md` (or filing-set drafts) finalized, passed `patent-compliance` 3/5 gate, and `delivery` stage marked (Word only if `word-export: agreed` or in-turn request via `../word-delivery/SKILL.md`)

The pipeline's default completion point is **finalized `.md` drafts**: assembly per `references/disclosure-document.md` (for the consolidated disclosure) plus zero unresolved criticals from step 4（含披露轨轻量门禁）。交付前执行洁净门禁：`drafts/技术交底书.md` 须通过 `../patent-compliance/SKILL.md` 第3/5项检查，未过不标 `delivery ✓`。Confirm the delivery form with the inventor. Generate Word files **only** when the inventor asks in the current turn or the route record says `word-export: agreed` — then read `../word-delivery/SKILL.md` for conversion chains, template reuse, formula conversion, and the acceptance gate.

Revision requests after delivery follow the single-source rule: edits land in the owning draft under `drafts/`, affected checks re-run, then `../word-delivery/SKILL.md` regenerates — never hand-edit a delivered `.docx`.

### 6. Filing guidance, only when requested → Done when: `patent-filing` guidance loaded iff route requested filing, otherwise track closed without filing

Hand off to `../patent-filing/SKILL.md`. Load filing guidance from `../patent-filing/SKILL.md` when the route record marks filing as requested; otherwise keep drafting focused on the current track.

## Single pointers — disclosed references (load only when branch fires)

- disclosure assembly: `references/disclosure-document.md` (实施级规范描述，推荐按 `references/8-points.md` 8要点完整展开)
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
- [ ] Delivery form agreed with the inventor and recorded (`word-export` axis); if Word was requested, output passed the acceptance gate in `../word-delivery/SKILL.md`, or the degradation/blocker report was delivered
