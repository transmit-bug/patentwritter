---
name: patent-compliance
description: "Pre-filing self-check of the drafted CN patent deliverables — support chain, claim clarity, title and figure consistency, formula provenance. Reports severity, location, and repair guidance to 草稿/检查报告.md; checks existing drafts and never drafts or silently repairs content itself."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Pre-Filing Self-Check

Role: **discipline** of the self-service group, independent from the drafters by design — the checker and the drafter never share a file. On completion, update the 自检 stage in `草稿/申请信息.md`.

Standards pointer: `../patent-standards/`. Use the relevant anchor when a check needs a legal interpretation; this skill owns the executable check, not a reproduction of the standards.

Input: the drafts and supplied figures for the selected branch. Output a report at `草稿/检查报告.md` with `critical`, `important`, or `minor`, a location, the observed problem, and a repair instruction.

## Invention / utility-model checks

### 1. Support chain

Split every claim into features and locate each feature in the specification's solution or embodiments. Missing landing points are critical. Check generic claim terms, dependent additions, core formulas, parameters, and alternatives.

### 2. Claim clarity

Scan for:

- undefined "所述" terms;
- leading phrases such as “优选”“例如”“最好” in claims;
- claims that rely on figure-only or specification-only language;
- mixed claim subjects;
- inconsistent terminology;
- multiple-dependent claims that create an invalid citation chain;
- numerals used as limitations rather than parenthetical references.

### 3. Title and subject consistency

Compare the route record, title, independent claim subject, dependent-claim citation parts, specification, abstract, and filenames. Any mismatch is critical.

### 4. Figure consistency

Compare the specification's reference-numeral set, figure labels, and brief description in both directions. Check figure numbering, missing images, embedded paths, and the designated abstract figure.

### 5. Formula and provenance hygiene

For formula-bearing cases, verify each core equation or logic predicate has:

- confirmed notation and variable meanings;
- units/ranges where meaningful;
- initialization, thresholds, and boundary handling;
- an embodiment and claim landing point;
- a source or inventor confirmation.

Model-inferred core relations are critical blockers. Scan the clean body for inline author/year citation prose. Replace it with an approved `[S#]` marker and a source appendix or support-layer record. Markdown is acceptable in drafts but not in a finished DOCX.

### 6. Abstract and effect

Check that the abstract states the subject, field, problem, solution gist, and use without marketing language. Check that every claimed effect is supported by data or an explicit mechanism explanation; never accept fabricated numbers.

## Design checks

Run only the design branch when the route says design:

- product name, use, design points, color choice, and similar/basic-design relationship are recorded;
- supplied views show the same product/version and cover the claimed design points;
- view scale, orientation, background, and labels are consistent;
- omitted views and designated view are recorded;
- the brief description describes appearance, not performance or internal structure;
- all required pictures/photographs are present and readable.

Use the design standards pointer for questions not answered by these checks.

## Rectification checks

When this is a rectification task, compare each amended feature with the original disclosure and figures. Flag newly introduced subject matter as critical and do not silently broaden the draft.

## Report format

```markdown
# 检查报告
| 级别 | 位置 | 问题 | 修复指引 |
|---|---|---|---|
| critical | 权利要求1 / 说明书实施例 | … | … |

## 修复建议
1. …
```

## Completion standard

- [ ] Only applicable branch checks were run
- [ ] Every critical has a location and repair instruction
- [ ] Support chain and formula checks are complete where applicable
- [ ] Figures, titles, terminology, and deliverable files are consistent
- [ ] Word delivery is separately passed through `../conversion/SKILL.md`
- [ ] 自检 stage updated in `草稿/申请信息.md`
