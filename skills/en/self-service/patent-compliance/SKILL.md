---
name: patent-compliance
description: Pre-filing self-check of application documents (Chinese, invention / utility model / design). Item-by-item checks — claims-specification support chain, clarity, citation basis, subject consistency, reference-numeral consistency, utility model formalities, design formalities (views / brief description / classification), abstract compliance, amendment beyond scope. Every check has an executable method; output is a check report with severity levels and repair guidance. Use when the user asks to "check the application documents", "self-check", "pre-filing check", "rectification check"; also invoked by the patent-application entry skill.
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Pre-Filing Self-Check (递交前自检)

Input: 草稿/权利要求书.md + 草稿/说明书.md + 草稿/摘要.md + 草稿/附图说明.md (+ the original application documents during a rectification phase). Output: a check report (severity + location + repair guidance).

## Check items, each with "how to check"

### 1 Support chain (claims ↔ specification) → find the source of every feature

How: split each claim into features; find a landing point for each feature in the specification (summary-of-invention solution paragraphs or embodiments). Not found = critical (专利法第26条第4款: claims shall be supported by the description).
- Independent-claim generic terms: the specification must have at least one concrete embodiment landing under them.
- Dependent-claim additional features: must be matched in the embodiments.

### 2 Clarity → mechanical scan

How: search the full text for these patterns —
- "所述 X": look backward for X's first introduction ("一种X" / "X"); not found = citation-basis error.
- "优选""例如""最好""可选的" appearing in a claim = leftover leading phrases.
- "如图…所示" / "如说明书…所述" in a claim = violation (细则第22条).
- Subject-name inconsistency: independent-claim subject vs dependent-claim citation part vs specification title.

### 3 Subject consistency → three-way table

How: build a table — request title (草稿/申请信息.md), independent-claim subject name, specification title. Any mismatch = critical (细则第20条: title consistent with the request).

### 4 Reference-numeral consistency → two-direction check

How: extract numeral set A from the specification text; numeral set B from the drawings / brief description. A−B (in text, not in figures) and B−A (in figures, not in text) must both be empty (细则第21条). One part carrying two numerals = critical.

### 5 Utility model formalities → three hard rules

How (utility models only):
- The independent claim is a product claim (subject like "装置/设备/系统"), without method steps as the main features → violation = critical (专利法第2条第3款).
- Has a structural figure (细则第20条).
- Reference-numeral consistency as above.

### 6 Abstract compliance → read it item by item

How: does the abstract contain the name, technical field, problem, solution gist, main uses (细则第26条)? Any marketing language? Is the abstract figure designated?

### 7 Amendment beyond scope (rectification phase only) → diff against the original

How: diff the revised draft against the original application documents feature by feature. Features newly added that the original did not record = beyond scope (critical, 专利法第33条). "Deleting" is not beyond scope; "changing a feature" needs care — changing is beyond scope unless the original supports it.

### 8 Design formalities → check views and brief description item by item

How (designs only):
- Views match the design points: a 3D product submits orthographic views of the faces its design points involve (six views only when all six faces are involved, 指南 第一部分第三章 4.2); omitted views → the brief description must carry an omission statement (missing statement = critical).
- Brief description complete: product name, use, design points, the image designated as best showing the design points; color protection requested and declared (if requested; claiming color requires submitting color pictures or photographs).
- Classification correct: product name consistent with the Locarno class direction (name-class mismatch = critical).
- Views consistent: all views at the same scale, showing the same product and the same version (two view forms for the same product = critical).
- Similar designs: one application containing multiple similar designs (≤10) → a basic design designated and declared (细则第40条).
- Image clarity: must clearly show the protected appearance (专利法第27条第2款).
- On rectification (rectification phase only): amendments must not go beyond the scope shown in the original pictures or photographs (专利法第33条第2款); picture/photo amendments submitted as replacement pages (细则第58条第2款).

## Report format

```markdown
# 检查报告
| 级别 | 位置 | 问题 | 修复指引 |
|------|------|------|----------|
| critical | 权利要求1 特征"识别模块" | 说明书无"识别模块"出处 | 在实施例补写识别模块结构 |
| important | … | … | … |

## 修复建议(按级别排序)
```

Severity definitions:
- **critical**: must fix; filing will otherwise hit problems (rejection / rectification / beyond scope).
- **important**: likely to be pointed out by the examiner; should fix.
- **minor**: quality improvement, optional.

## Completion standard

- [ ] All applicable check items executed (invention: 1/2/3/4/6/7; utility model: 1-7; design: 3/7/8)
- [ ] Report contains severity, location, repair guidance
- [ ] Every critical has a one-sentence repair plan
