---
name: patent-application
description: "Coordinate the invention/utility-model drafting flow after routing: interview, record the four elements, invoke claims/specification/drawings, self-check, and assemble the requested delivery."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Application Orchestrator

Use this skill **after** `../patent-router/` has recorded the source, deliverable, and type. This file owns sequencing and the inventor interview. It does not decide the route, repeat type rules, or duplicate the drafting disciplines.

## Inputs and outputs

Input: a route record in `草稿/申请信息.md`, inventor materials under `.patent/materials/`, and any declared template.

For invention / utility model:

- filing set: `草稿/权利要求书.md`, `草稿/说明书.md`, `草稿/摘要.md`, `草稿/附图说明.md`, applicable drawings, and the corresponding `成品/申请文件/*.docx` when Word is requested;
- disclosure only: `草稿/技术交底书.md` and, when requested, `成品/技术交底书.docx`;
- both: produce both sets without treating the disclosure as a filing document.

For design: use the design branch's brief description, view list, and supplied images; do not generate invention/utility-model claims or a five-part specification.

## Sequence

### 1. Intake interview → four elements complete

For invention / utility model, read `references/interview.md` and record:

- technical problem;
- minimally implementable technical solution;
- distinguishing feature;
- technical effect and its evidence.

For a formula-bearing case, complete the core-formula questions in that reference. The model may normalize confirmed material, but must not invent a core formula or experimental result. For design, use `references/design-points.md` instead of the four-element interview.

Ask about disclosure status and preserve the inventor's source trail. Put retrieved references and user materials in `.patent/`; keep the drafting body readable.

### 2. Draft only the requested branch

- Filing set, invention / utility model: read and execute `../patent-claims/SKILL.md`, then `../patent-specification/SKILL.md`, then `../patent-drawings/SKILL.md` when figures apply.
- Filing set, design: execute the design branch in `references/design-points.md`; images are inventor-supplied.
- Disclosure only: assemble according to `references/disclosure-document.md`; do not manufacture claims or statutory filing sections merely to fill space.

Each discipline owns its own completion standard. Every retained claim feature must have a specification landing point; every core formula must have confirmed variables, conditions, and embodiment support.

### 3. Self-check → zero unresolved criticals

Read `../patent-compliance/SKILL.md`. Run only the checks applicable to the selected type and deliverable. Return unresolved blockers to the inventor instead of silently filling them.

### 4. Assemble and deliver

Read `../conversion/SKILL.md` for Markdown-to-Word conversion, template reuse, formula conversion, and the acceptance gate. Read `references/disclosure-document.md` for the single consolidated disclosure structure. Never mix `草稿/` and `成品/`.

### 5. Filing guidance, only when requested

When the user requests filing or rectification guidance, hand off to `../patent-filing/SKILL.md`. Do not load filing procedure during drafting unless the route record asks for it.

## Single pointers

- Type choice: `references/type-decision.md`.
- Design interview and views: `references/design-points.md`.
- Prior-art search: `references/search-guide.md` and `../tools/patents-search/`.
- CN standards: `../patent-standards/SKILL.md` and the one relevant reference named there. Do not copy statutory text or long rule-basis tables into this orchestrator.
- Word and existing-material conversion: `../conversion/SKILL.md`.

## Completion standard

- [ ] Route record exists and is respected
- [ ] Only the selected type and deliverable branches ran
- [ ] Four elements or design points are recorded
- [ ] Requested drafts and figures exist, with no invented material
- [ ] Applicable self-check has no unresolved criticals
- [ ] Word output passed the conversion acceptance gate, or the degradation/blocker report was delivered
