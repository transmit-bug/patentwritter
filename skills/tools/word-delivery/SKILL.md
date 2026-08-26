---
name: word-delivery
description: Word delivery of application documents — converts the .md drafts under drafts/ into the two delivery sets under deliverables/ (three filing .docx plus one consolidated 技术交底书.docx), with environment-probed degradation chains, template filling (style inheritance / content fill), and a Word acceptance gate. Runs only on an explicit user request ("convert to Word", "generate docx", "export to Word", "use my Word template") or when the route record pre-agrees it — never as an automatic end-of-pipeline step. Revisions always go back to drafts/*.md first; the .docx is a regenerable artifact, never a source.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, Bash
---

# Word Delivery Discipline (纯文档)

This skill is a **document-only capability**: md→docx is generated inline by the AI at conversion time; no conversion script ships in the package. Probe the environment first on every conversion, take the first available path in the degradation chain; if none is available, fail loud (state exactly what is missing) rather than pretending to produce output.

## Trigger gate (read this first)

Run this skill **only** when one of these holds:

1. The user explicitly asks for Word output in the current turn ("转Word" / "generate docx" / "export to Word" / "fill my template"); or
2. `drafts/application-info.md` records `word-export: agreed` — agreed at interview or in an earlier turn.

Otherwise do nothing except point to the `.md` drafts under `drafts/`. Markdown-to-Word conversion is never an automatic end-of-pipeline step; the pipeline's own completion standard is finalized, self-checked `.md` drafts.

## Single-source rule (revision loop)

The `.md` drafts under `drafts/` are the **only editable truth**. Everything under `deliverables/` is a regenerable export.

- Any revision request — including complaints about a delivered `.docx` — is fixed in the owning draft (`权利要求书.md`, `说明书.md`, `摘要.md`, `技术交底书.md`), then this skill re-runs to regenerate. Keep `.docx` under `deliverables/` as regenerable exports; make all edits in the owning `drafts/*.md` draft and regenerate.
- When a revision touches claims / specification substance, re-run the applicable checks in `../patent-compliance/SKILL.md` before re-exporting.
- Regeneration is idempotent and cheap: re-export all deliverables after any substantive edit, so the sets never drift apart.

## Delivery degradation chain

Goal: turn the `.md` drafts under `drafts/` into the **two delivery sets** under `deliverables/` (layout in `../patent-intake/SKILL.md` "Workspace layout"). **Drafts and deliverables never mix**: everything under `deliverables/` is directly usable, nothing under `drafts/` is final.

1. **申请文件** (CNIPA 分文件递交用): three same-named `.docx`, one file per document, no timestamps.
2. **技术交底书** (交代理机构/内部评审用): one consolidated `.docx`.

**Step 0 — assemble `drafts/技术交底书.md` first**: merge the tracked sources per the route-aware assembly table in `../patent-intake/references/disclosure-document.md` — both: application-info / 说明书 / figures / 权利要求书 / 摘要 drafts; disclosure-only: the interview four-element record + confirmed materials (no filing drafts, no filing-track gates). Then convert every deliverable source the route actually produced — on a disclosure-only route that is `技术交底书.md` alone.

| Source file (drafts/) | Delivered file (deliverables/) |
|---|---|
| 权利要求书.md | 申请文件/权利要求书.docx |
| 说明书.md | 申请文件/说明书.docx |
| 摘要.md | 申请文件/摘要.docx |
| 技术交底书.md | 技术交底书.docx |

Figure references inside the `.md` drafts are written as relative paths `../figures/embed/figN.png` (figures live in `figures/embed/`, see `../patent-drawings/SKILL.md` Step 2). **Run all conversion commands from inside `drafts/`** so those `../` paths resolve against the case root `patents/<patent-name>/`.

### Probe (do this first; it decides the chain)

```bash
python3 -c "import docx" 2>/dev/null && echo docx-ok     # hit → chain ①
python3 -c "import latex2mathml" 2>/dev/null && echo latex2mathml-ok || true
pandoc --version 2>/dev/null | head -1                  # hit → chain ②
```

Before conversion, classify the source: plain prose, tables/figures, or **formula-bearing**. Treat LaTeX delimiters and equation-like Unicode text (for example `α`, `Δt`, `＝`, subscripts, or a line labelled “公式”) as formula candidates; Unicode typography alone is not an editable Word equation. Normalize confirmed equations to `$$...$$`/inline math in the draft, then prefer a path that produces editable Word math (OMML): `pandoc` math conversion, or `latex2mathml` → OMML during inline generation. If neither path is available, fail loud and deliver the Markdown draft plus a formula-blocker report; do not call a literal formula paragraph a finished Word deliverable.

### Chain ① python-docx available → generate inline

Write an inline Python script (python-docx): read each source from `drafts/`, resolve `../figures/embed/figN.png` **relative to the source file's directory** (not the working directory), map headings to Word's built-in heading styles, convert Markdown emphasis/links/blockquote/list/checklist/table syntax into native Word runs, paragraphs, list styles, and tables, embed the figures inline (keep aspect ratio; width at a clearly legible size), and write the output to `deliverables/application/` (three filing docs) or `deliverables/` (技术交底书). 封面/页眉/页脚写入中性 `技术交底书（供代理机构据此独立起草申请文件）`，不发射过程控制词；控制词仅在 `drafts/application-info.md` 跟踪。

When a `.docx` template is supplied, the modes and fill protocol in the "Template filling" section below govern. Chain ① is the only chain that can fill content into a template's own structure; it preserves page setup, headers/footers, styles, numbering, and table geometry where safe, and reports every unsupported feature.

- **Formulas**: convert every core formula to editable OMML; define variables in adjacent prose; preserve equation numbering if the template has it. Before conversion, verify that the source formula is semantically complete rather than merely a string containing Greek letters. Emit every core formula as editable OMML with variable definitions alongside; treat Markdown delimiters and raw LaTeX as source notation only.
- **PNG only**: Word inline embedding supports bitmaps only; the figure pipeline already produces both formats as PNG (see `../patent-drawings/SKILL.md` Step 2).
- **Native structure**: `**bold**`, headings, lists, checkboxes, blockquotes, and `---` become Word structure, never visible Markdown punctuation.

### Chain ② pandoc available → command conversion

```bash
cd drafts
pandoc 权利要求书.md -o ../deliverables/application/权利要求书.docx
pandoc 说明书.md -o ../deliverables/application/说明书.docx
pandoc 摘要.md -o ../deliverables/application/摘要.docx
pandoc 技术交底书.md -o ../deliverables/disclosure.docx
```

Run from inside `drafts/`: pandoc resolves the figure paths `../figures/embed/figN.png` against the working directory, so `../` steps up to the case root (`patents/<patent-name>/`). (Alternative: run from the root with `pandoc --resource-path=drafts drafts/xxx.md -o ...`.) `--reference-doc` is **style inheritance only** — it cannot place content into a template's structure; for content fill see the "Template filling" section. Spot-check after conversion for missing figures and formula conversion.

### Chain ③ neither available → deliver .md + manual save-as

Deliver the `.md` drafts from `drafts/` (the assembled `技术交底书.md` included) and give the inventor a one-line instruction: open the .md with WPS/Word (or copy-paste) and choose "Save As" → .docx.

### Title gate（复用 intake 规范）

`drafts/技术交底书.md` 的 `#` 标题即发明名称，须符合 `../patent-intake/references/disclosure-document.md` 发明名称规范（`一种…的…方法`，见上）。Word 封面/页眉中的标题与该 `#` 逐字一致；缺 `一种`、含英文缩写/ `之`、超长均在 acceptance gate 记 fail。Word 封面副标题与页眉/页脚统一发射中性 `技术交底书（供代理机构据此独立起草申请文件）`，不发射任何过程控制词；控制词仅保留于 `drafts/application-info.md` 与 skill 内跟踪，不进 Word 正文/封面/页眉/页脚/表格。

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

Scope: content fill applies to the 技术交底书. The three 申请文件 docx keep their statutory one-document structure — a template may style them, never restructure them.

Content-fill protocol:

1. **Ingest the template** → Done when: a section map is recorded — every heading, placeholder, and table in the template, with what belongs in each.
2. **Map drafts to slots** → Done when: every 交底书 section (assembly table in `../patent-intake/references/disclosure-document.md`) has a target slot; draft sections without a slot and template slots without a source are both listed — neither silently dropped nor filled.
3. **Fill** → Done when: each slot receives its content verbatim (assembly rules apply — copy, don't rewrite); template boilerplate (cover, headers/footers, numbering, fixed clauses) is preserved untouched; the template's own styles carry the inserted text.
4. **Verify** → Done when: zero unfilled placeholders remain (`{{...}}`, `【...】`, `____`); no template instructions copied into the body; the filled DOCX passes the acceptance gate above.

Degradation: without a docx-capable environment (chain ① unavailable), content fill is **impossible** — state it loudly and fall back to style inheritance or `.md` + paste instructions. Fill by writing into a copy of the template, keeping the supplied template file unchanged; map each draft section to its template slot without appending after the body.

Record back into drafts/application-info.md (template-adaptation note): which template was used, mode taken, inheritance scope, and any downgrade.

## Optional dependencies

See `requirements-optional.txt` in the same directory. All "optional, install on demand": not installing means taking the degradation chain, which does not block the flow. The probe commands above are the authority; no pre-installation required.

## Boundaries

- Only structured conversion of text / images / tables; layout beautification (headers / footers / page numbers / font sizes) follows the official filing requirements and is out of scope for this skill.
- This skill never edits the substance of the drafts — content revisions belong to the drafting disciplines via the single-source rule above.
- This skill is zero-script: any urge to "download a script / run a repo conversion tool" is out of bounds — generate inline or degrade.
