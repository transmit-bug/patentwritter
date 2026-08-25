# Source Handling — 任何内容形态统一摄入

This file is the ingestion discipline for `patent-exploration`. It reuses the archive contract from `../../patent-intake/references/source-modes.md` but adds an exploratory lens: a source is first **understood**, not classified.

## Archive contract (mandatory, every source)

Same as `patent-intake`: archive the source **as-is** under `patents/<patent-name>/.patent/materials/` (case-root-relative `.patent/materials/`, see `../../patent-intake/SKILL.md` Workspace layout) and register provenance in `drafts/application-info.md` (material-location) or, if intake has not yet started, in `.patent/exploration/来源登记.md` (case-root-relative `.patent/exploration/`): what it is, when obtained, how obtained, whose it is.

No source is discarded. No source is pre-judged as "prior art" or "disclosure complete".

## Ingestion channel (form → channel)

| Form | Channel |
|---|---|
| docx / pptx / pdf | `../../conversion/SKILL.md` discipline (pure document, zero scripts) → Markdown under `patents/<patent-name>/.patent/materials/` (case-root-relative) |
| 网页 / 链接 | environment fetch → Markdown snapshot |
| 口述 / 对谈记录 | transcribe verbatim → Markdown |
| 代码 / 数据表 | archive as-is + Markdown summary of what it implements |
| 已有专利/申请 | archive as-is + Markdown extract of claims/spec lineage |

For docx/pptx, follow `conversion` degradation chain: if inline read fails, fall back to archived-file scan summary — never block exploration on a format error.

## The paper-source delta (exploration lens)

The intake source-modes file warns: paper structure ≠ disclosure structure. In exploration, go further:

- A paper's **contribution claim** is not necessarily a patentable point. Papers optimize for novelty narrative; patents optimize for reproducible technical effect.
- A paper's **evaluation section** is useful for effect evidence but rarely sufficient for patent enablement (边界条件、参数范围、失败模式 often missing).
- A paper's **related work** is not a prior-art search result — treat it as clues, not conclusions.

When ingesting a paper, always note in `内容地图.md`: `论文主张` vs `技术事实` vs `待验证` — three columns, never merged.

## Completeness does not gate exploration

In `patent-intake`, completeness decides interview strategy (extract-confirm-fill). In exploration, **incompleteness is the point**: the discussion exists to fill gaps. So:

- If the content is rich → mining mode can run end-to-end before Socratic.
- If the content is a one-sentence idea → skip map/deconstruction, enter Socratic immediately.
- If multiple sources conflict → keep them as parallel maps, discuss which lineage to follow.

## Five cross-cutting flags (shared with intake)

Downstream intake consumes these flags; exploration sets them early when possible:

1. `是否涉及核心公式/算法` — has a formula-bearing core?
2. `是否涉及附图类型` — what figure types would help?
3. `是否涉及产品形态` — is there a concrete product/method carrier?
4. `是否涉及公开/披露风险` — any publication/sale disclosure?
5. `是否涉及单一性风险` — multiple independent contributions?

Set what you can; leave the rest as `待确认` — the handover step will close them.
