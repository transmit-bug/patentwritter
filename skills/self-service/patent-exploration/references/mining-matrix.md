# Mining Matrix — 可专利点挖掘矩阵

Purpose: turn deconstructed triples into **ranked, generalizable patentable points**. Output is `可专利点清单.md`.

## Matrix structure

| # | 专利点 (label) | 来源 triple | 类型 | 可上位化? | 保护价值 | 实现成本 | 风险 |
|---|---|---|---|---|---|---|---|
| P1 | ... | T1 | 核心 | 高/中/低 | 高/中/低 | 高/中/低 | ... |
| P2 | ... | T1/T2 | 外围 | ... | ... | ... | ... |
| P3 | ... | T3 | 防御 | ... | ... | ... | ... |

### Types (类型)

- **核心 (core)**: the main inventive contribution; likely the independent claim subject. Usually 1–2 per exploration.
- **外围 (peripheral)**: meaningful improvement that depends on the core or stands as a secondary independent point; candidate for dependent claims or secondary independent claim.
- **防御 (defensive)**: alternative implementation or fallback that prevents design-around; low standalone value but high portfolio value.

### Generalizability (上位化潜力)

For each point, test three questions (borrowed from `patent-drafting` but exploratory, not drafting):

1. 如果把具体数值/具体结构去掉，效果还成立吗？(parameter → range → principle)
2. 如果把实现载体换了（软件/硬件/云边），手段还成立吗？
3. 有没有等效替换手段能达到同等效果？(if yes, the point needs broader wording)

Rate 高/中/低; 高 = worth exploring a broader claim scope later in `patent-claim-strategy`.

## Steps

### 1. Generate candidates from triples

Each `潜在专利点` triple yields 1–3 candidates; each `待研讨` yields 0–1 after discussion. Keep labels short and engineer-readable.

### 2. Rank by value vs cost

- 保护价值: how hard is it to design around? how central is it to the product?
- 实现成本: how much disclosure is needed to enable it? is experimental data available?

Use `AskUserQuestion` to confirm ranking when uncertain — inventors know product priority best.

### 3. Mark dependencies

Note which points depend on which: `P2 依赖 P1` or `P3 独立`. This prefigures claim dependency but does not draft claims.

### 4. Note evidence gap

For each point: `证据: 充分 / 部分 / 缺口` + `需补充: ...`. This becomes the intake interview's focus.

## Example row

```markdown
| P1 | 自适应阈值调度 | T1 | 核心 | 高 | 高 | 中 | 需补充突发流量下的对照数据 |
```

## Done when

- At least one `核心` point is identified, or an explicit "暂无核心点，建议先做 X 再评估" conclusion is recorded (also a valid outcome).
- Every row has 类型 + 上位化 + 价值/成本 + 证据 gap — no empty cells.
- The top 1–2 core points have a one-sentence "一句话保护构思" that will seed the later independent claim (but is not yet a claim).

## Non-goal

Do not draft claim language here. The one-sentence构思 is prose, not "一种...其特征在于...". Claim drafting belongs to `../../patent-drafting/SKILL.md`.

## Optional: portfolio view

If multiple points are independent (singleness risk), add a short note: `是否可能涉及多件申请/分案？` and point to `../../patent-intake/references/source-modes.md` singleness check + `../../patent-claim-strategy/SKILL.md` for later strategy. Do not decide filing count here.
