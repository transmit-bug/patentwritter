---
name: patent-claim-strategy
description: Professional claim strategy for CN patents — design the protection scope (essential-feature weighing, generalization, claim tiers, fallback positioning), choose the response amendment strategy under an OA (argue vs amend, amendment ladder, estoppel-aware drafting), and decide when to divide (分案, 细则48-49) or claim priority (优先权, 法29-30) with their deadlines. Strategy discipline only — mechanical claim drafting stays in the self-service group (patent-claims); enforcement / portfolio-level layout (专利布局), FTO and licensing are out of scope (ADR-0007 decision 7). Grounded output: every legal assertion cites the verified anchors; never number from memory. Use when the user asks about claim scope, protection breadth, 保护范围, amendment strategy in an OA, whether to divide or claim priority, or 分案 / 优先权. Model-invoked discipline of the professional group (entry: patent-prosecution).
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Claim Strategy (权利要求策略 — 保护范围 / 答复修改 / 分案 / 优先权)

Professional-group discipline skill (ADR-0007 decisions 1-2): the **strategy layer** over claim drafting. Mechanical drafting (claims text, 上位化 mechanics, dependent-claim structure) stays in the B 组 self-service skill (`patent-claims`); this skill decides **what scope to pursue and how to defend it**. Every legal assertion traces to a verified anchor — never number from memory.

## Read first

1. **Discipline**: `../../patent-standards/references/professional-discipline.md` — declare / consume / cite / fail loud / never invent. Follow it.
2. **Anchors**: `../../patent-standards/references/cn-professional.md` — patent-claim-strategy row: 法33, 法22.3, 法29-30 (优先权), 细则48-49 (分案), 细则57.3, 指南 II-4 3.2.1.1; plus `cn-invention-utility.md` for drafting mechanics (法22 / 26.4, 细则22-25).
3. **Honesty red line**: prior art from real delegated-search results / user-supplied material only; strategy is argued against the actual cited references, never against imagined ones.
4. **Workspace**: strategy notes in `.patent/strategy/<case>/` (suggest gitignored).

## 1. Protection-scope design (保护范围设计)

Professional-grade scope decisions, from the four elements up:

- **必要技术特征拿捏 (essential-feature weighing)**: apply the 删除测试 — remove a feature: does the technical problem still get solved? Solved → not essential, demote to a dependent claim. The independent claim carries only the essential set (细则23); every non-essential feature is fallback material, not a self-inflicted limit.
- **上位化 (generalization)**: walk the three-rung ladder (具体实现 → 中间概括 → 功能概括), each rung gated by: still solves the original problem / supported in the specification (法26.4) / not a pure functional limitation.
- **Claim tiers (独权/从权层级)**: independent claim = the commercial core; dependent claims = 退路布防 in three directions — 细化 (narrowing specifics), 变体 (alternative implementations), 增强 (additional-function features), ordered by commercial importance. The dependent tier is the amendment ammunition for the whole prosecution life (OA → 复审 → 无效).
- **禁止反悔-aware drafting**: at drafting time, pre-judge which words would become concessions if the claim is narrowed later — a limitation drafted only for breadth (e.g. an unnecessary 优选 feature in the independent claim) is a hostage; keep the independent claim lean and put breadth-reducing detail in dependents.
- **保护范围与商业价值匹配**: scope is chosen against the actual prior-art landscape from the delegated search (撰写前必要检索, 指南 II-7), not in a vacuum — a claim that ignores a close reference is a claim that will be rejected or invalidated.

## 2. Response amendment strategy (答复修改策略)

Given an OA (or a rejection decision), decide the response shape before drafting:

1. **argue vs amend vs both**: pure argument preserves scope but risks the finding; amendment trades scope for allowability; the default is both — argue the disputed finding, amend only what is truly indefensible.
2. **Amendment ladder**: prefer the *lowest* rung that overcomes the defect while keeping the broadest defensible scope — a specific rung of the 上位化 ladder, a 细化 feature, or a 变体/增强 combination from the fallback tier. Never jump straight to the narrowest embodiment.
3. **细则57.3 discipline**: amendments are directed to the defects the notice points out (OA response); in 复审 they are limited to removing the rejection decision's defects (细则66 — narrower); in 无效 the limits are stricter still (细则73 — claims only, no broadening). The amendment power shrinks down the pipeline — spend the broad-amendment capital while the OA is still open.
4. **法33 red line**: every amendment checked against the original specification + claims; a feature with no original-disclosure support is inadmissible — prefer the supported rung, mark 「待发明人指认段落」 if the location is uncertain.
5. **禁反悔 review**: after choosing amendments, re-read the final claim set for what it concedes (a narrowed feature set is a public record); if a concession buys nothing, argue instead.
6. **分案 pressure valve**: when unity (法31.1 / 细则39-40) is objected or multiple inventions compete in one application, division (细则48-49) preserves the dropped subject matter as a separate application instead of abandoning it — decide division *before* the 细则60.1 deadline (细则48).

## 3. Division (分案)

Strategy view (anchors 细则48-49, verified against the official text):

- **When**: the application covers two or more inventions / utility models / designs; unity is objected; or a second inventive concept should survive separately. Division is possible before the 细则第60条第1款 deadline; **not** after rejection / withdrawal / deemed withdrawal (细则48).
- **Constraints**: 分案不得改变原申请类别 (细则48); the division retains the original filing date (and priority date if claimed) and must not exceed the original disclosure (细则49); the request states the original application number and filing date (细则49).
- **Strategy use**: a division is the escape hatch for subject matter the OA / rejection is squeezing out — the parent narrows, the division carries the broader variant. Decide early; the deadline is unforgiving.

## 4. Priority (优先权)

Strategy view (anchors 法29-30, verified against the official text):

- **Windows**: foreign priority — invention / utility model within 12 months of the first foreign filing, design within 6 months; domestic priority — same 12/6 months for same-subject filings in China (法29).
- **Formalities**: written declaration at filing + copy of the first application within 16 months (invention / utility model) or 3 months (design); missing either → 视为未要求优先权 (法30) — deadline discipline, not a detail.
- **Strategy use**: priority is the tool for claiming an earlier effective date for the same subject matter (incl. a 本国优先权 re-file incorporating improvements) — but every assertion about a specific priority claim's validity is grounded in the actual documents; no priority law beyond these anchors is asserted from memory.

## Grounded output & fail loud (网关)

- No claim text / specification → stop.
- A strategy recommendation that depends on unverified legal detail (e.g. 细则60 content beyond 细则48's citation, 指南 Part I filing rules) → declare `[STANDARD] CN <topic>` and read the material, or fail loud for that part; never fill from memory.
- No prior art for scope positioning → say the landscape is unknown and scope is argued without it (and recommend the search), rather than inventing a landscape.

## Boundaries

- In scope: scope design, response amendment strategy, division / priority strategy, estoppel-aware drafting, interplay with the prosecution pipeline.
- Out of scope (ADR-0007 decision 7): **专利布局 (portfolio-level layout across applications), FTO (自由实施), 维权 / 侵权诉讼, 许可** — these are 授权后业务; 分案/优先权 strategy *within a prosecution* is in scope, portfolio strategy is not.
- Out of scope (sibling skills): mechanical drafting → `patent-claims` (B 组); the actual OA response / 复审请求书 / 无效 pleadings → `patent-oa-response` / `patent-re-exam` / `patent-invalidation`.
- Not a substitute for the agent's judgment or signature.

## Minimal walkthrough (最小案例)

Input: claim 1 (独立权利要求) + 两份对比文件 from delegated search + 一次 OA 通知 (法22.3 创造性).

1. **Scope check**: 删除测试 on claim 1 — feature X fails the test → demoted to dependent (fallback tier: 细化), claim 1 stays lean.
2. **Response strategy**: argue the distinguishing feature (not disclosed in either reference) + amend one rung up the ladder? No — amend *down* one supported rung (细则57.3, 法33), preserving the rest as 变体/增强 dependents; 禁反悔 review: the narrowed rung concedes nothing beyond the actual distinction.
3. **Division check**: a second inventive concept in the spec (method embodiment) is currently unclaimed → 分案 candidate (细则48-49) before the 细则60.1 deadline; parent keeps the product scope, division carries the method.
4. **Priority check**: the user has a foreign filing within 12 months → 优先权声明 + copy deadline computed (法29-30); no assertion beyond the verified anchors.
5. **人审闸门**: strategy memo + 修改建议【草稿】, 须代理人复核; every recommendation carries its anchor citation.
