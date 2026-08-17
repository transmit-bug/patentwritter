---
name: conversion
description: Conversion discipline for Word delivery of application documents and ingestion of existing .docx / .pptx materials (document-only capability, zero scripts zero dependencies, ADR-0005). Covers two template modes — style inheritance and filling content into an existing DOCX template. Use when the user asks to "convert to Word", "generate docx", "export to Word", "turn my existing disclosure / PPT into text", "use a Word template", or "fill my template"; also invoked by the patent-intake entry skill (ingestion at the pipeline head, delivery at the tail).
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# Conversion and Delivery Discipline (纯文档)

This skill is a **document-only capability** (ADR-0005 decision 1): md→docx and docx/pptx→md are generated inline by the AI at conversion time; no conversion script ships in the package. Probe the environment first on every conversion, take the first available path in the degradation chain; if none is available, fail loud (state exactly what is missing) rather than pretending to produce output.

## Delivery degradation chain (Stage-5 assembly → Word delivery)

Goal: turn the `.md` drafts under `草稿/` into the **two delivery sets** under `成品/` (layout in `../patent-intake/SKILL.md` "Workspace layout"). **Drafts and deliverables never mix**: everything under `成品/` is directly usable, nothing under `草稿/` is final.

1. **申请文件** (CNIPA 分文件递交用): three same-named `.docx`, one file per document, no timestamps.
2. **技术交底书** (交代理机构/内部评审用): one consolidated `.docx`.

**Step 0 — assemble `草稿/技术交底书.md` first**: merge 申请信息 / 说明书 / 附图 / 权利要求书 / 摘要 into one disclosure document per the assembly table in `../patent-intake/references/disclosure-document.md`. Then convert all four sources below.

| Source file (草稿/) | Delivered file (成品/) |
|---|---|
| 权利要求书.md | 申请文件/权利要求书.docx |
| 说明书.md | 申请文件/说明书.docx |
| 摘要.md | 申请文件/摘要.docx |
| 技术交底书.md | 技术交底书.docx |

Figure references inside the `.md` drafts are written as relative paths `../附图/嵌入/figN.png` (figures live in `附图/嵌入/`, see `../patent-drawings/SKILL.md` Step 2). **Run all conversion commands from inside `草稿/`** so those `../` paths resolve against the project root `patent-application/`.

### Probe (do this first; it decides the chain)

```bash
python3 -c "import docx" 2>/dev/null && echo docx-ok     # hit → chain ①
python3 -c "import latex2mathml" 2>/dev/null && echo latex2mathml-ok || true
pandoc --version 2>/dev/null | head -1                  # hit → chain ②
```

Before conversion, classify the source: plain prose, tables/figures, or **formula-bearing**. Treat LaTeX delimiters and equation-like Unicode text (for example `α`, `Δt`, `＝`, subscripts, or a line labelled “公式”) as formula candidates; Unicode typography alone is not an editable Word equation. Normalize confirmed equations to `$$...$$`/inline math in the draft, then prefer a path that produces editable Word math (OMML): `pandoc` math conversion, or `latex2mathml` → OMML during inline generation. If neither path is available, fail loud and deliver the Markdown draft plus a formula-blocker report; do not call a literal formula paragraph a finished Word deliverable.

### Chain ① python-docx available → generate inline

Write an inline Python script (python-docx): read each source from `草稿/`, resolve `../附图/嵌入/figN.png` **relative to the source file's directory** (not the working directory), map headings to Word's built-in heading styles, convert Markdown emphasis/links/blockquote/list/checklist/table syntax into native Word runs, paragraphs, list styles, and tables, embed the figures inline (keep aspect ratio; width at a clearly legible size), and write the output to `成品/申请文件/` (three filing docs) or `成品/` (技术交底书).

When a `.docx` template is supplied, the modes and fill protocol in the "Template filling" section below govern. Chain ① is the only chain that can fill content into a template's own structure; it preserves page setup, headers/footers, styles, numbering, and table geometry where safe, and reports every unsupported feature.

- **Formulas**: convert every core formula to editable OMML; define variables in adjacent prose; preserve equation numbering if the template has it. Before conversion, verify that the source formula is semantically complete rather than merely a string containing Greek letters. Do not emit Markdown delimiters, raw LaTeX, Unicode-only equations, or formula images as the only representation.
- **PNG only**: Word inline embedding supports bitmaps only; the figure pipeline already produces both formats as PNG (see `../patent-drawings/SKILL.md` Step 2).
- **Native structure**: `**加粗**`, headings, lists, checkboxes, blockquotes, and `---` become Word structure, never visible Markdown punctuation.

### Chain ② pandoc available → command conversion

```bash
cd 草稿
pandoc 权利要求书.md -o ../成品/申请文件/权利要求书.docx
pandoc 说明书.md -o ../成品/申请文件/说明书.docx
pandoc 摘要.md -o ../成品/申请文件/摘要.docx
pandoc 技术交底书.md -o ../成品/技术交底书.docx
```

Run from inside `草稿/`: pandoc resolves the figure paths `../附图/嵌入/figN.png` against the working directory, so `../` steps up to the project root. (Alternative: run from the root with `pandoc --resource-path=草稿 草稿/xxx.md -o ...`.) `--reference-doc` is **style inheritance only** — it cannot place content into a template's structure; for content fill see the "Template filling" section. Spot-check after conversion for missing figures and formula conversion.

### Chain ③ neither available → deliver .md + manual save-as

Deliver the `.md` drafts from `草稿/` (the assembled `技术交底书.md` included) and give the inventor a one-line instruction: open the .md with WPS/Word (or copy-paste) and choose "Save As" → .docx.

### Word acceptance gate

A DOCX is complete only when all applicable checks pass: zero Markdown tokens (`**`, leading `>`, raw list markers, `$...$`, backticks, `---`, `[ ]`); headings have native heading styles; tables and figures are present; core formulas are editable/readable OMML with variables defined; source citations are absent from the clean body except approved `[S#]` markers; and template placeholders/instructions are absent. In content-fill mode additionally: zero unfilled placeholders, and every unfilled template slot is reported (see "Template filling"). Reopen and inspect the generated DOCX structurally before handover. Record counts for paragraphs, tables, figures, formulas, and residual Markdown markers.

### Fail loud

When the probe fails or conversion errors, tell the user truthfully: which dependency is missing, which chain was taken, and what format the artifact is in. If a core formula cannot be converted to OMML, keep the task blocked or deliver Markdown with a blocker report; never produce a broken .docx and pass it off as done.

## Template filling (fill content into an existing DOCX template)

Two modes — decide before conversion. The route record's 模板 axis (项目默认 / 指定模板 / 无) says a template exists; this section decides which mode:

| Mode | What it does | Chain |
|---|---|---|
| Style inheritance | template supplies styles / page setup; content structure follows the drafts | any chain (pandoc `--reference-doc`, or python-docx style extraction) |
| **Content fill** | generated content is inserted **into the template's existing structure** — cover page, fixed sections, tables, headers/footers stay as the template designed them | chain ① only (python-docx inline) |

Scope: content fill applies to the 技术交底书. The three 申请文件 docx keep their statutory one-document structure (ADR-0008) — a template may style them, never restructure them.

Content-fill protocol:

1. **Ingest the template** → Done when: a section map is recorded — every heading, placeholder, and table in the template, with what belongs in each.
2. **Map drafts to slots** → Done when: every 交底书 section (assembly table in `../patent-intake/references/disclosure-document.md`) has a target slot; draft sections without a slot and template slots without a source are both listed — neither silently dropped nor filled.
3. **Fill** → Done when: each slot receives its content verbatim (assembly rules apply — copy, don't rewrite); template boilerplate (cover, headers/footers, numbering, fixed clauses) is preserved untouched; the template's own styles carry the inserted text.
4. **Verify** → Done when: zero unfilled placeholders remain (`{{...}}`, `【...】`, `____`); no template instructions copied into the body; the filled DOCX passes the acceptance gate above.

Degradation: without a docx-capable environment (chain ① unavailable), content fill is **impossible** — state it loudly and fall back to style inheritance or `.md` + paste instructions. Never fake a fill by appending generated content after a copied template body, and never overwrite the supplied template file itself — fill into a copy.

Record back into 草稿/申请信息.md (模板适配说明): which template was used, mode taken, inheritance scope, and any downgrade.

## Ingestion degradation chain (Stage-1 disclosure interview → scan existing materials)

When the inventor provides existing .docx (disclosure / design description / old application) or .pptx (review materials):

| Environment | Approach |
|---|---|
| mammoth or python-docx available | read the .docx inline → Markdown; extract images to the materials directory; text enters the interview context |
| python-pptx available | read the .pptx inline → per-slide Markdown (including speaker notes); extract images to the materials directory |
| none available | ask the inventor for text / Markdown / paste the key paragraphs directly |

Ingested materials and images land in `.patent/materials/` (see the "Workspace layout" section of patent-intake), never mixed into the application documents directory.

## Optional dependencies

See `requirements-optional.txt` in the same directory. All "optional, install on demand": not installing means taking the degradation chain, which does not block the flow. The probe commands above are the authority; no pre-installation required.

## Boundaries

- Only structured conversion of text / images / tables; layout beautification (headers / footers / page numbers / font sizes) follows the official filing requirements and is out of scope for this skill.
- `.doc` (legacy format) is not converted; ask the inventor to save as .docx or provide text.
- This skill is zero-script: any urge to "download a script / run a repo conversion tool" is out of bounds — generate inline or degrade.
