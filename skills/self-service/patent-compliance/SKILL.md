---
name: patent-compliance
description: "Pre-filing self-check of the drafted CN patent deliverables — support chain, claim clarity, title and figure consistency, formula provenance. Reports severity, location, and repair guidance to drafts/check-report.md; checks existing drafts and never drafts or silently repairs content itself."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Pre-Filing Self-Check

Role: **discipline** of the self-service group, independent from the drafters by design — the checker and the drafter never share a file. On completion, update the self-check stage in drafts/application-info.md.

This skill is the **backend gate that owns claim-formality rules** — they were deliberately moved out of `../patent-drafting/SKILL.md` so drafting can stay in content mode. 它在两条轨道均运行：递交轨运行全量检查（1-6），披露轨运行轻量门禁（仅第3项标题白名单+洁净 + 第5项溯源收敛 + 第4项图一致），未过不标 `self-check ✓`。

Standards pointer: `../patent-standards/`. Use the relevant anchor when a check needs a legal interpretation; this skill owns the executable check, not a reproduction of the standards.

Input: the drafts and supplied figures for the selected branch. Output a report at `drafts/check-report.md` with `critical`, `important`, or `minor`, a location, the observed problem, and a repair instruction.

## Invention / utility-model checks

### 1. Support chain

Split every claim into features and locate each feature in the specification's solution or embodiments. Missing landing points are critical. Check generic claim terms, dependent additions, core formulas, parameters, and alternatives.

### 2. Claim clarity

**Scope: scan 权利要求书.md only.** These are claims-register checks; the specification's narrative paragraphs and any 技术交底书 are exempt — do not flag "所述" usage or statutory phrasing there (the specification is deliberately written in engineering prose per the voice wall in patent-drafting).

Scan for:

- undefined "所述" terms;
- leading phrases such as “优选”“例如”“最好” in claims;
- claims that rely on figure-only or specification-only language (e.g. "如图…所示");
- mixed claim subjects;
- inconsistent terminology;
- multiple-dependent claims that create an invalid citation chain;
- a dependent claim citing a later claim; a multiple dependent claim citing more than one alternative or serving as the basis of another multiple dependent claim; a citation part that does not restate the full subject;
- numerals used as limitations rather than parenthetical references;
- more than one full stop in a single claim.

### 3. Title and subject consistency

Compare the route record, title, independent claim subject, dependent-claim citation parts, specification, abstract, and filenames. Any mismatch is critical.

**Title rule gate**: `drafts/技术交底书.md` 的 `#` 标题与 `drafts/application-info.md` 的 `target-product`/发明名称须为 `一种<基于/面向><核心手段>的<对象+效果>方法`（及系统可选，见 `../patent-intake/references/disclosure-document.md` 发明名称规范），15–30字为佳、不超35字、用`的`不用`之`、英文缩写不上标题；缺`一种`前缀或含`VAE/MDFA/ROM`等缩写、含`之`字、超长均记 `critical` 并给出按规范的重命名建议。

**Disclosure heading gate（交底书标题干净检查，披露轨必跑，两级白名单）**: 扫描 `drafts/技术交底书.md`：
- H2 外框必须逐字命中 `../patent-intake/references/disclosure-document.md` 的外框白名单（`一、技术领域` / `二、背景技术` / `三、要解决的技术问题` / `四、技术方案` / `五、技术效果` / `六、区别特征` / `七、替代方案` / `八、附图说明` / `附录 S — 溯源登记`），缺 `一、技术领域`/`二、背景技术`/`三、要解决的技术问题`/`五、技术效果` 中任一即 `critical`；
- `四、技术方案` 内 H3 必须逐字命中方案内白名单（`（一）总体架构` / `（二）设计构思` / `（三）分步实施描述（N步）` / `（四）实施条件与可复现性说明` / `（五）关键算法伪代码` / `（六）符号与参数说明` / `（七）公式推导与等价形式` / `（八）硬件组成与部署形态` / `（九）具体实施例`），旧式 `一、总体架构` 作 H2 即 `critical`（应为 H3 且括号序号）；
- 正文外框 8 章（不含附录 S）出现工作区路径（`res/`、`.patent/`、`figures/source`）或过程性说明句式即 `critical`；
- 正文出现免责分散句式（每步/每式/每表末尾重复免责）即 `important`，提示收敛到 `application-info.md` 的 `blocked` 记录与附录 S 一行极简登记；
- 分步每步机械填表 `输入：/处理：/输出：` 三行且无连贯段落即 `important`，提示按 `8-points.md` 去填表化改写。

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

**Provenance convergence check（披露轨亦必跑）**: 诚实标注不得散落在每步/每式/每表末尾；应收敛到 `drafts/申请信息.md` 的 `blocked` 记录与附录 S 一行极简登记。扫描正文前八章（不含附录 S），出现重复免责句式即 `important`。

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

## Boundaries

- Owns checks only; never drafts or repairs content — reports severity/location/repair guidance, routes back via `../patent-intake/SKILL.md` Stage 4 back edges.
- Never invents prior art or data; gaps stay as `critical: blocked`.
- Claim-formality checks own the register; drafting owns the voice wall — do not flag specification prose for "所述".

## Rectification checks

When this is a rectification task, compare each amended feature with the original disclosure and figures. Flag newly introduced subject matter as critical and do not silently broaden the draft.

## Report format

```markdown
# Check report
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
- [ ] If Word output was requested, it is separately passed through `../word-delivery/SKILL.md` (user-invoked; md drafts are the completion point otherwise)
- [ ] self-check stage updated in drafts/application-info.md
