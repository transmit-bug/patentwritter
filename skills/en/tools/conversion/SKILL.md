---
name: conversion
description: Conversion discipline for Word delivery of application documents and ingestion of existing .docx / .pptx materials (document-only capability, zero scripts zero dependencies, ADR-0005). Use when the user asks to "convert to Word", "generate docx", "export to Word", "turn my existing disclosure / PPT into text"; also invoked by the patent-application entry skill (Stage-1 ingestion, Stage-5 delivery).
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# Conversion and Delivery Discipline (纯文档)

This skill is a **document-only capability** (ADR-0005 decision 1): md→docx and docx/pptx→md are generated inline by the AI at conversion time; no conversion script ships in the package. Probe the environment first on every conversion, take the first available path in the degradation chain; if none is available, fail loud (state exactly what is missing) rather than pretending to produce output.

## Delivery degradation chain (Stage-5 assembly → Word delivery)

Goal: turn the `.md` drafts under `patent-application/` into filable `.docx` files. **Fixed filenames, one file per document, no timestamps**:

| Source file (.md) | Delivered file (.docx) |
|---|---|
| 权利要求书.md | 权利要求书.docx |
| 说明书.md | 说明书.docx |
| 摘要.md | 摘要.docx |

### Probe (do this first; it decides the chain)

```bash
python3 -c "import docx" 2>/dev/null && echo docx-ok     # hit → chain ①
pandoc --version 2>/dev/null | head -1                  # hit → chain ②
```

### Chain ① python-docx available → generate inline

Write an inline Python script (python-docx) generating the files one by one: map headings to Word's built-in heading styles, write body text as paragraphs, embed the figures from `附图/figN.png` inline (keep aspect ratio; width at a clearly legible size). Spot-check after generation: each .docx opens with no missing figures, no empty paragraphs, correct heading hierarchy.
- **Formulas**: when latex2mathml is available, LaTeX → MathML → OMML (editable formulas in Word); otherwise keep the LaTeX source as-is, no image fallback.
- **PNG only**: Word inline embedding supports bitmaps only; the figure pipeline already produces both formats as PNG (see `../patent-drawings/SKILL.md` Step 2).

### Chain ② pandoc available → command conversion

```bash
pandoc 权利要求书.md -o 权利要求书.docx
pandoc 说明书.md -o 说明书.docx
pandoc 摘要.md -o 摘要.docx
```

Figures in the .md are written as relative paths `附图/figN.png`; pandoc embeds the PNGs automatically. Spot-check after conversion for missing figures.

### Chain ③ neither available → deliver .md + manual save-as

Deliver the `.md` drafts and give the inventor a one-line instruction: open the .md with WPS/Word (or copy-paste) and choose "Save As" → .docx.

### Fail loud

When the probe fails or conversion errors, tell the user truthfully: which dependency is missing, which chain was taken, and what format the artifact is in. Never produce a broken .docx and pass it off as done.

## Ingestion degradation chain (Stage-1 disclosure interview → scan existing materials)

When the inventor provides existing .docx (disclosure / design description / old application) or .pptx (review materials):

| Environment | Approach |
|---|---|
| mammoth or python-docx available | read the .docx inline → Markdown; extract images to the materials directory; text enters the interview context |
| python-pptx available | read the .pptx inline → per-slide Markdown (including speaker notes); extract images to the materials directory |
| none available | ask the inventor for text / Markdown / paste the key paragraphs directly |

Ingested materials and images land in `.patent/materials/` (see the "`.patent/` support workspace" section of patent-application), never mixed into the application documents directory.

## Optional dependencies

See `requirements-optional.txt` in the same directory. All "optional, install on demand": not installing means taking the degradation chain, which does not block the flow. The probe commands above are the authority; no pre-installation required.

## Boundaries

- Only structured conversion of text / images / tables; layout beautification (headers / footers / page numbers / font sizes) follows the official filing requirements and is out of scope for this skill.
- `.doc` (legacy format) is not converted; ask the inventor to save as .docx or provide text.
- This skill is zero-script: any urge to "download a script / run a repo conversion tool" is out of bounds — generate inline or degrade.
