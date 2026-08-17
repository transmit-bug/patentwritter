---
name: patent-router
description: "Route a Chinese patent task by material source, requested deliverable, and patent type; then hand off to the smallest set of self-service skills."
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Patent Router

This is the **front door** for self-service patent work. It decides the route; it does not draft claims, specifications, drawings, or filing instructions. Ask only the questions needed to select a route, record the decision in `草稿/申请信息.md`, then hand off to the named skills.

## Route inputs

Collect three axes:

1. **Material source**
   - inventor description / interview;
   - user-supplied document, image, PDF, DOCX, PPTX, or code;
   - paper, product material, or other technical publication.
   Ingest supplied material through `../conversion/SKILL.md`; keep source files and extraction notes in `.patent/materials/`. A paper is technical input, not automatically prior art or a complete invention disclosure.

2. **Requested deliverable**
   - **disclosure only**: technical disclosure for an agent or internal review;
   - **filing set**: claims, specification, abstract, and applicable drawings/brief description;
   - **both**: disclosure plus filing set.
   Word output is a delivery choice handled by `../conversion/SKILL.md`, not a separate patent type.

3. **Patent type**
   - invention;
   - utility model;
   - design;
   - undecided / possible dual filing.
   Use `../patent-application/references/type-decision.md`. Do not force a type from the document format or from a product name.

## Routing table

| Decision | Handoff |
|---|---|
| Any supplied material | `../conversion/SKILL.md` → material intake, then interview |
| Inventor description or incomplete material | `../patent-application/SKILL.md` → disclosure interview |
| Invention, filing set | `../patent-claims/` → `../patent-specification/` → `../patent-drawings/` → `../patent-compliance/` |
| Utility model, filing set | claims/specification/drawings/compliance, with the utility-model branch in each discipline |
| Design, filing set | `../patent-application/references/design-points.md` → design brief/view list → compliance |
| Disclosure only | `../patent-application/references/disclosure-document.md` → `../conversion/SKILL.md` |
| Both | complete the filing-set route, then assemble the disclosure |
| Filing / rectification after documents exist | `../patent-filing/SKILL.md` |

## Handoff contract

Before handoff, write a compact route record:

```text
材料来源: 发明人描述 / 用户文件 / 论文或其他材料
材料位置: …
交付目标: 交底书 / 申请文件套件 / 两者
申请类型: 发明 / 实用新型 / 外观设计 / 一案两请 / 待确认
待确认事项: …
模板: 项目默认 / 指定模板 / 无
```

A route is selected only when source, deliverable, and type are recorded. If type or material meaning remains ambiguous, ask the inventor; do not draft by guessing.

## Boundaries

- The router does not repeat patent-law explanations. When a legal or standards question is reached, follow the single pointer in the receiving skill to `../patent-standards/`.
- The router does not copy a user's case, paper, formula, citation, or experimental result into a skill. Case facts remain in the project support workspace and drafts.
- The router does not run every discipline by default. It invokes only the branches required by the requested deliverable and type.

## Completion standard

- [ ] Source kind and material location recorded
- [ ] Deliverable selected
- [ ] Patent type selected or explicitly unresolved
- [ ] Template choice recorded, if any
- [ ] Only the required downstream skills handed off
