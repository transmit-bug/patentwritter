---
name: patent-intake
description: "Front door and orchestrator for self-service Chinese patent work — routing, inventor interview, stage checklist, discipline dispatch and back-edge routing. Use when the user wants to write a patent application, continue an interrupted one, or produce a technical disclosure."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Intake (front door + orchestrator)

Role: **front door + orchestrator** of the self-service group (ADR-0009). This skill routes the task, runs the interview, owns the stage checklist, and dispatches the disciplines — `../patent-drafting/`, `../patent-drawings/`, `../patent-compliance/`, `../patent-filing/`. It does not draft claims, specifications, drawings, or filing instructions, and it does not repeat patent-law explanations.

Cold start always begins here. If a route record already exists, re-enter this skill and resume from the stage checklist instead of re-routing.

## Route inputs

Collect three axes:

1. **Material source** — 口述 / 文档 (docx, pdf, pptx) / 网页 / 对谈记录 / 代码 / 其他材料 (paper, product material, technical publication). Source handling is not a set of branches: follow the unified protocol in `references/source-modes.md` (archive contract → ingestion channel → extract-confirm-fill). A paper is technical input, not automatically prior art or a complete invention disclosure.
2. **Requested deliverable**
   - **disclosure only**: technical disclosure for an agent or internal review;
   - **filing set**: claims, specification, abstract, and applicable drawings/brief description;
   - **both**: disclosure plus filing set.
   Word output is a delivery choice handled by `../conversion/SKILL.md`, not a separate patent type.
3. **Patent type** — invention / utility model / design / undecided or possible dual filing. Use `references/type-decision.md`. Do not force a type from the document format or from a product name. If the source carries multiple independent inventive contributions, run the singleness check in `references/source-modes.md` before committing to one application.

## Routing table

| Decision | Handoff |
|---|---|
| Any supplied material | source intake per `references/source-modes.md` (documents go through `../conversion/SKILL.md`), then interview |
| Inventor description or incomplete material | disclosure interview (this skill, `references/interview.md`) |
| Invention, filing set | `../patent-drafting/` → `../patent-drawings/` → `../patent-compliance/` |
| Utility model, filing set | same chain, with the utility-model branch in `../patent-drafting/` and mandatory structural drawings |
| Design, filing set | design branch in `references/design-points.md` → brief description/view list → `../patent-compliance/` (design checks) |
| Disclosure only | assemble per `references/disclosure-document.md` → `../conversion/SKILL.md` |
| Both | complete the filing-set route, then assemble the disclosure |
| Filing / rectification after documents exist | `../patent-filing/SKILL.md` |

## State record

Write and maintain `草稿/申请信息.md`. A route is selected only when source, deliverable, and type are recorded; if type or material meaning remains ambiguous, ask the inventor — do not draft by guessing.

Route record:

```text
材料来源: 口述 / 文档 / 网页 / 对谈记录 / 代码 / 其他材料
材料位置: …
交付目标: 交底书 / 申请文件套件 / 两者
申请类型: 发明 / 实用新型 / 外观设计 / 一案两请 / 待确认
待确认事项: …
模板: 项目默认 / 指定模板 / 无
横切标志: 公开状态=… / 语言纯度=… / 数据可用性=… / 图可用性=… / 多贡献风险=…
```

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
- [ ] 交付
- [ ] 递交
```

Each discipline updates its own stage to ✓ when its completion standard passes, and to `blocked: <reason>` when it stops. Disclosure-only routes mark 摄入/路由/访谈/交付; design routes mark 摄入/路由/访谈(设计要点)/自检/交付/递交. Blockers are explicit: when a core fact is missing (e.g. an undefined formula boundary), record it and pause only the affected part — never fill by invention.

## Workspace layout

In the inventor's project (ADR-0008; the directory is a **workspace name, not a skill name**): drafts under `patent-application/草稿/`, figures under `patent-application/附图/` (`源文件/` .dot sources, `预览/` svg, `嵌入/` png), deliverables under `patent-application/成品/`; support layer `.patent/` (`sources/` citation lists, `materials/` inventor materials, `queries/` search records). Never mix `草稿/` and `成品/`.

## Sequence

### 1. Source intake → archived material

Follow `references/source-modes.md`: archive the source as-is, register provenance, run the extract-confirm-fill protocol, and set the five cross-cutting flags in the route record. Documents are ingested through `../conversion/SKILL.md`.

### 2. Interview → four elements (or design points) complete

For invention / utility model, read `references/interview.md` and record the four elements: technical problem; minimally implementable technical solution; distinguishing feature; technical effect and its evidence. For a formula-bearing case, complete the core-formula questions in that reference — the model may normalize confirmed material, but must not invent a core formula or experimental result. For design, use `references/design-points.md` instead of the four-element interview.

Ask about disclosure status and preserve the inventor's source trail. Prior-art search is optional: `references/search-guide.md` + `../patents-search/` before drafting the background art.

### 3. Dispatch drafting — only the requested branch

- Filing set, invention / utility model: execute `../patent-drafting/SKILL.md` (claims → specification → abstract), then `../patent-drawings/SKILL.md` when figures apply.
- Filing set, design: execute the design branch in `references/design-points.md`; images are inventor-supplied.
- Disclosure only: assemble per `references/disclosure-document.md`; do not manufacture claims or statutory filing sections merely to fill space.

Each discipline owns its own completion standard and updates the stage checklist.

### 4. Self-check → zero unresolved criticals

Read `../patent-compliance/SKILL.md`. Run only the checks applicable to the selected type and deliverable; the report lands at `草稿/检查报告.md`. **Back edges are this skill's job**: route each unresolved critical back to the discipline that owns the artifact (`../patent-drafting/` for claims/specification support chains, `../patent-drawings/` for numeral/figure mismatches), then re-check. Return blockers to the inventor instead of silently filling them.

### 5. Assemble and deliver

Read `../conversion/SKILL.md` for Markdown-to-Word conversion, template reuse, formula conversion, and the acceptance gate; read `references/disclosure-document.md` for the consolidated disclosure structure.

### 6. Filing guidance, only when requested

Hand off to `../patent-filing/SKILL.md`. Do not load filing procedure during drafting unless the route record asks for it.

## Single pointers

- Type choice: `references/type-decision.md`.
- Source handling and the five flags: `references/source-modes.md`.
- Design interview and views: `references/design-points.md`.
- Disclosure assembly: `references/disclosure-document.md`.
- Prior-art search: `references/search-guide.md` and `../patents-search/`.
- CN standards: `../patent-standards/SKILL.md` and the one relevant reference named there — no statutory text or Rule-basis tables copied here.

## Boundaries

- Case facts, papers, formulas, citations, and experimental results belong to the project support workspace and drafts, never to this skill's files.
- Do not run every discipline by default; invoke only the branches required by the requested deliverable and type.
- Disciplines are never called sideways by each other — handoffs happen through artifact files and this orchestrator.

## Completion standard

- [ ] Route record exists and is respected; stage checklist kept current
- [ ] Source archived with provenance; five cross-cutting flags set
- [ ] Only the selected type and deliverable branches ran
- [ ] Four elements or design points recorded; no invented material
- [ ] Self-check report exists with no unresolved criticals; back edges routed and re-checked
- [ ] Word output passed the conversion acceptance gate, or the degradation/blocker report was delivered
