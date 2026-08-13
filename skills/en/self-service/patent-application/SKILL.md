---
name: patent-application
description: Full-flow guide for inventors to file patents on their own (invention / utility model / design, CN) — disclosure interview, type determination, generating the application documents, pre-filing self-check, e-filing and rectification guidance. Entry skill; trigger with /skill:patent-application.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# Self-Service Patent Application Guide (发明/实用新型/外观设计)

Turn the technology (or product appearance) in the inventor's head into a filable application package: invention / utility model = claims / specification / drawings / abstract; design = pictures or photographs + brief description. Then guide the filing.

## Boundaries

- Scope: disclosure → type determination → drafting → self-check → assembly → filing and rectification.
- Substantive-examination OA responses are not in this package (the professional-agent direction, the `professional/` group of the repo).
- Inventors are not fluent in jargon: ask questions in plain language, produce output in formal application language.

## Honesty red line

The background art only contains prior art with a source; if none can be obtained, write nothing — definition (the three kinds of material) single source: CONTEXT.md「诚实红线」; the executable version (including the "can the user tell you where this came from" test) is in `../patent-specification/SKILL.md` Part 2.

## `.patent/` support workspace (optional, recommended)

Create `.patent/` under the inventor's project root, kept separate from the application drafts:

```
.patent/
├── sources/    # declarative: patent-standard citation lists, declared external-source entries
├── materials/  # documentary: inventor materials, copies of retrieved hits (ingested docx/pptx and extracted figures also land here)
└── queries/    # networked lookup process: Valyu / CNIPA / Google Patents search records and results
```

- Search results land in `queries/`, materials in `materials/`, citation lists in `sources/` (both Stage-1 ingestion and Stage-2 novelty search follow this).
- Application drafts stay in the visible `patent-application/`, never mixed into `.patent/`.
- Suggest gitignoring `.patent/` (keep the trail if you want).

## Process: six stages, each with a completion standard

### Stage 1 Disclosure interview → Done when: the four elements are complete, written into 申请信息.md

The four elements = technical problem / technical solution (minimally implementable) / distinguishing feature / technical effect. Ask group by group using the question bank in `references/interview.md`, at most 4 questions per group via AskUserQuestion.

**Designs run a different interview line** (the inventor describes the product appearance — shape / pattern / color, aesthetics-driven, no functional-structural improvement): ask the design interview groups in `references/design-points.md` instead (class / design points / view materials / similar designs / color), with the completion standard "class + design points + view materials complete".

Questioning discipline:
- The inventor gives the description first; you extract the four elements and **ask only for what's missing**, not what's already there.
- Record product names / brands / UI words on the spot; hand them to patent-claims' term conversion table at drafting time.
- Always ask "how do you prove the effect": data if there is data, mechanism reasoning only if not — never fabricate.
- Ask whether it has been disclosed (article / exhibition / sale / leak) → triggers the grace-period reminder (专利法第24条, see interview.md).
- If the inventor brings existing materials (.docx disclosure / design description / .pptx review deck): ingest via the degradation chain in `../../tools/conversion/SKILL.md`; materials and extracted figures land in `.patent/materials/` (above).

### Stage 2 Type determination → Done when: type + rule basis written into 申请信息.md

Use the decision tree in `references/type-decision.md` to determine invention / utility model / design / dual filing (一案两请). The rule basis comes from patent-standards' verified anchors, never from impression. For designs, continue with `references/design-points.md` for the class and Locarno classification hints.

**Novelty search (optional, recommended)** — run one pass before drafting the background art; write only the actual results (honesty red line): see `references/search-guide.md` (Valyu main path + CNIPA manual five-step search).

### Stage 3 Drafting → Done when: the four files are on disk, no placeholders (design: brief description + view list)

**Invention / utility model**: read the three discipline skills in full and execute per them (paths relative to this directory):
1. `../patent-claims/SKILL.md` — claims
2. `../patent-specification/SKILL.md` — specification + abstract
3. `../patent-drawings/SKILL.md` — drawings + abstract-figure designation (mandatory for utility models; an invention with figures is sturdier)

Output to the user's working directory `patent-application/`:
```
patent-application/
├── 申请信息.md       ← four elements + type + grace-period determination
├── 权利要求书.md
├── 说明书.md
├── 摘要.md
├── 附图/fig1.svg、fig1.png …   ← svg preview + png for Word inline embedding
└── 附图说明.md       ← numbering + numeral list + abstract-figure designation
```

**Design**: read `references/design-points.md` → generate `简要说明.md` + `视图清单.md`; view materials (by the number of faces the design points involve, photos or line drawings) are provided by the inventor — the AI only organizes the view list and checks compliance, never draws. Output layout:

```
patent-application/
├── 申请信息.md       ← class + design points + color declaration + similar designs
├── 简要说明.md       ← name / use / design points / designated image / omitted views / color
├── 图片/主视图.png … ← provided by the inventor (black-white/gray, by the faces the design points involve, see references/design-points.md)
└── 视图清单.md       ← six views + perspective view correspondence table
```

### Stage 4 Self-check → Done when: zero criticals (at most two rounds; anything still critical after two rounds gets listed explicitly)

Read `../patent-compliance/SKILL.md`, run all check items against the produced files (invention / utility model: claims + specification + drawings; design: brief description + views), output the check report. Critical issues → back to Stage 3 to fix; anything still critical after two rounds: list it and let the user decide.

### Stage 5 Assembly → Done when: filing checklist confirmed + Word delivery (optional)

Verify: title consistency, files complete, reference-numeral consistency, abstract figure designated. Give the filing document list for each type (the request form is generated by the system; remind the user to fill it).

**Generate Word delivery (invention / utility model, when the inventor needs .docx)**: read `../../tools/conversion/SKILL.md`, use the delivery degradation chain to produce **same-named .docx** files for `权利要求书.md / 说明书.md / 摘要.md` (fixed filenames, one file per document, no timestamps), with figures inlined as `figN.png`. Done when: the three .docx exist with no missing figures; or the degradation chain was explicitly followed (deliver .md + manual save-as guidance), telling the user the current artifact format.

### Stage 6 Filing and rectification guidance → Done when: step-by-step guidance given, human-only steps marked

Read `../patent-filing/SKILL.md`, give the inventor the e-filing steps they can do themselves, marking which only a human can do (registration / payment / signature). When the user receives a rectification notice, come back to this stage and use patent-filing's rectification protocol.

## Skill relations

- This entry invokes only the model-invoked discipline skills above; it never invokes another entry skill.
- Legal anchors live centrally in `../../patent-standards/` (invention / utility model → `references/cn-invention-utility.md`; design → `references/cn-design.md`); this skill does not repeat statute text, only cites at decision points.
