# Handover — 向 patent-intake 移交

Purpose: the gate between exploration and the normative pipeline. This file defines when exploration is "done" and what the handover package contains.

## Gate condition

Exploration is done when **all** of:

- `内容地图.md` exists (if material was given)
- `技术拆解.md` has triples with problem/means/effect separated, no mixed triples
- `可专利点清单.md` has at least one `核心` point or an explicit "暂无核心点" conclusion
- `研讨纪要.md` has a `本轮研讨结论` (even if brief)
- `保护方向建议.md` proposes 1–3 directions with trade-offs, and the user has picked one (or explicitly deferred)

If any item is missing, do not handover — continue the loop.

## Protection-direction proposal (保护方向建议.md)

For each direction, write:

```markdown
### 方向 A — <label> (推荐/备选)
- 核心点: P1 (+ P2)
- 一句话构思: <prose, not claim language>
- 保护形态: 方法 / 系统 / 产品 / 多形态
- 上位化潜力: 高/中/低 + 一句话理由
- 证据状态: 充分/部分/缺口 + 需补充什么
- 风险: 单一性 / 公开风险 / 实现难度
- 适合的申请类型 hint: 发明 / 实用新型 / 外观(若涉及) — 最终由 intake 的 type-decision 定
```

1–3 directions, not more. Always include trade-offs; never present a single direction as "唯一正确".

## Writing the handover stub

Create `.patent/exploration/移交-intake.md` (handover stub) with:

```markdown
# 移交 patent-intake

探索结论: <方向 A/B/C + 一句话理由>
目标产物: <从 discussion.md 的产品锚定提炼，一句话>
核心 triple: T1/T2
核心专利点: P1 (+ P2)

四要素草稿 (intake 可直接确认/修正):
- 技术问题: <from T1 问题>
- 技术方案: <from T1 手段, prose>
- 区别特征: <from lineage 本内容的不同>
- 技术效果: <from T1 效果 + 证据>

待 intake 访谈确认:
- [ ] 申请类型 (invention/utility/design/dual) — 见 ../../patent-intake/references/type-decision.md
- [ ] 证据缺口: ...
- [ ] 单一性: 是否多件
- [ ] 公开风险: ...
- [ ] 交付形态: md only / docx on request — 记录到 申请信息.md Word导出 轴

附件: 内容地图 / 技术拆解 / 可专利点清单 / 研讨纪要 / 保护方向建议
```

## How intake consumes it

`patent-intake` starts its interview from this stub: the four-element draft is pre-filled, the remaining checks are explicit. The inventor confirms or corrects — no re-asking from scratch. The five cross-cutting flags from `source-handling.md` are carried over.

If the user chose "暂不进入 intake" (explore only), just archive the package and stop — a valid end state. The exploration artifacts remain useful as a standalone research memo.

## What handover is not

- Not a `技术交底书.md` — that is assembled by `patent-intake` at stage 5.
- Not a `权利要求书` — that is drafted by `patent-drafting`.
- Not a filing decision — that is the inventor's, with `patent-claim-strategy` advice if needed.

## Done when

- The stub exists under `.patent/exploration/` and the user has been asked: "是否现在进入 patent-intake 定四要素？(是 / 先存档 / 再聊一轮)".
- The user's choice is recorded.

No silent auto-dispatch. Always ask.
