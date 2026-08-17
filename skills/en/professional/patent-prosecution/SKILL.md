---
name: patent-prosecution
description: "Entry point for the professional (professional, A 组) prosecution pipeline — route the user's situation to the right discipline skill of the 授权链路 (OA 答复 / 复审 / 无效 / 评价报告 / 权利要求策略), check the input gate each skill requires, and dispatch. User-invoked orchestrator only — it carries no pleading logic itself (that lives in the five discipline skills). Trigger with /skill:patent-prosecution, or when the user asks to respond to an office action, request re-examination, invalidate / defend a patent, request or use a patent evaluation report, or work out claim scope / amendment / division / priority strategy. Out of scope: 授权后业务 (FTO / 布局 / 维权 / 许可) and US prosecution (ADR-0007 decision 7)."
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion
---

# Professional Prosecution Pipeline (授权链路编排入口)

Professional-group **entry** skill (ADR-0007 decisions 1 & 5): user-invoked, orchestrates the five discipline skills of `skills/en/professional/` — the discipline skills carry the pleading logic and are model-invoked; this skill only routes and gates. No statute text is repeated here; every discipline skill reads the shared discipline and its anchors itself.

## Boundaries

- Scope: the 授权链路 core — OA 答复 (`patent-oa-response`), 复审 (`patent-re-exam`), 无效 (`patent-invalidation`), 评价报告 (`patent-evaluation-report`), 权利要求策略 (`patent-claim-strategy`).
- Out of scope (ADR-0007 decision 7): FTO / 专利布局 / 维权 / 许可 (授权后业务); US prosecution (US 组重做另起); 专利通俗解读 / 政策嗅探.
- Mechanical claim drafting for a fresh application: not this entry — route to the self-service `patent-intake` entry (B 组).

## Route (dispatch table)

| User situation | Skill | Input gate |
|---|---|---|
| Received an 审查意见通知书 (OA) — draft a response / 意见陈述书 | `patent-oa-response` | notice (PDF-first) + 申请文件 (claims + spec) |
| Rejected (驳回决定) — request re-examination / draft 复审请求书 | `patent-re-exam` | 驳回决定 + 申请文件 + OA history |
| Want to invalidate a granted patent (请求无效) | `patent-invalidation` (Direction A) | granted claims + spec + evidence (delegated search / user-supplied) |
| Received an 无效宣告请求 — respond (答辩) | `patent-invalidation` (Direction B) | 无效请求书 + evidence + granted claims + spec |
| Need a 专利权评价报告 (维权前 / 应对侵权指控 / 开放许可) | `patent-evaluation-report` | utility-model / design patent text + purpose |
| Claim scope / amendment strategy / 分案 / 优先权 questions | `patent-claim-strategy` | claim text + spec + prior art (as available) |
| Fresh application drafting | → self-service `patent-intake` (B 组) | — |
| FTO / 布局 / 维权 / 许可 / US prosecution | out of scope — state so, per ADR-0007 decision 7 | — |

## Flow

1. **Intake** — ask what the user has and what they want (max 4 questions via AskUserQuestion): the material in hand (通知书 / 驳回决定 / 无效请求 / 专利文本 / 目的), the patent type, and any deadlines (e.g. the OA 指定期限 / 复审 3-month window). Record the deadline at the top of the handoff — the discipline skills re-verify it, but the entry never lets a deadline go unnoticed.
2. **Route** — use the dispatch table; when the situation spans stages (e.g. OA 答复 + 无效 readiness from a negative evaluation report), route the primary task and name the follow-on skill explicitly.
3. **Gate check** — before dispatch, confirm the input the target skill needs (the "Input gate" column) is present or obtainable; anything missing is stated to the user (fail loud) rather than dispatched half-blind.
4. **Dispatch** — hand off to the discipline skill with the material paths; the discipline skill runs its own workflow (read-first → parse → search → argue → draft → 人审闸门).

## Honesty red line (entry-level)

- Prior art and evidence come only from real delegated-search results / user-supplied material — never invented.
- Deadlines are read from the notice / decision, never assumed from memory; when the user doesn't know the deadline, the skill states what is needed, not a guess.
- Every discipline skill ends with a 人审闸门 — the entry reminds the user that drafts are drafts until a human (agent / inventor) reviews and files them.

## Fail loud (网关)

- No material at all (no notice, no decision, no patent text, no purpose) → list exactly what is missing and stop; do not invent a stage to work on.
- The user's situation does not match any in-scope stage → state the boundary (ADR-0007 decision 7) and what would be needed to help.
