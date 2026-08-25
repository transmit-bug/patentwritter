# Deconstruction — 技术拆解

Purpose: turn neutral content into **patent-relevant structure** without yet judging patentability. Output is `技术拆解.md`.

## The triple (三元组)

Every technical contribution is expressed as one or more triples:

> **问题 (Problem)** — 在什么约束下，什么做不好/做不到？
> **手段 (Means)** — 用了什么结构/步骤/参数/连接关系来解决？
> **效果 (Effect)** — 解决了到什么程度？如何证明？边界在哪？

One content may yield 1–5 triples. Each triple is numbered `T1, T2, ...` and stands alone.

## Steps

### 1. Extract raw triples from the content map

For each major contribution in `内容地图.md`, write a triple in plain engineering language:

```markdown
### T1 — <short label>
- 问题: <context + deficiency, one paragraph>
- 手段: <core mechanism, 2–4 bullets, include key parameters/ranges if present>
- 效果: <measurable effect + evidence location + known limits>
- 来源: 内容地图 §X / 论文 §Y / 口述 turn N
```

No claim language. "手段" is mechanism, not feature list.

### 2. Lineage (技术脉络)

For each triple, add:

- **前代做法**: how was this problem addressed before (content's related work + your general knowledge, but mark `待查新` if not in archived sources).
- **本内容的不同**: what changed — a new step? a removed constraint? a different parameter range? a new combination?
- **可替代性**: which part of 手段 could be swapped without losing 效果? (seeds generalizability).

### 3. Boundary conditions (边界)

For each triple, note:

- 必需条件 (must-have for the effect to hold)
- 可选条件 (nice-to-have, may become dependent points)
- 已知失效模式 (where it breaks, from content or inference — mark inference)

### 4. Distinguish "paper novelty" from "patent inventiveness"

Add a one-line tag per triple:

- `论文亮点` — interesting for publication but not necessarily patentable
- `潜在专利点` — reproducible technical improvement with identifiable effect
- `待研讨` — need Socratic discussion to decide

## Example (abstract, not domain-specific)

```markdown
### T1 — 动态阈值调度
- 问题: 高并发下固定阈值导致队列堆积，传统做法需人工调参
- 手段: 基于滑动窗口统计的阈值自适应 + 二级缓冲队列，阈值范围 [X, Y]
- 效果: 论文表3显示吞吐提升 18%，延迟 P99 降低 22%（测试集 A，N=10k）
- 前代做法: 固定阈值 / 手工分级
- 不同: 阈值由统计量驱动而非预设
- 可替代性: 滑动窗口可用指数加权替代；二级缓冲可用优先级队列替代
- 边界: 需连续请求流；突发零星请求下效果不显著
- 标签: 潜在专利点
```

## Done when

- Every major contribution has a triple, each with problem/means/effect cleanly separated.
- No triple mixes two independent problems — split them.
- Every 手段 bullet is concrete enough that an engineer could ask "如果我把 X 换成 Y，还行吗？" — that question will drive the mining matrix.
- Tags are assigned; nothing is left as "都挺重要".

## Handover

Triples tagged `潜在专利点` or `待研讨` feed `mining-matrix.md`. Pure `论文亮点` stays in the map but does not enter the matrix.
