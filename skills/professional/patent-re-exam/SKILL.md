---
name: patent-re-exam
description: "Draft a re-examination request (复审请求书) for a CN patent application rejected at substantive examination — challenge the rejection decision item by item within the 3-month window (法41.1), limit amendments to removing the defects the rejection decision or re-exam notice points out (细则66), and lay out the re-exam procedure (形式审查 → 前置审查 → 合议审查 → 复审决定, 指南 IV-2; withdrawal 细则68; suit within 3 months 法41.2). Same discipline and grounding rules as patent-oa-response — the re-exam request re-argues the OA grounds (incl. three-step method, 指南 II-4 3.2.1.1) against the rejection decision. Use when the user asks to request re-examination, draft a 复审请求书, respond to a rejection decision (驳回决定), or challenge a 驳回. Model-invoked discipline of the professional group (entry: patent-prosecution)."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Re-examination (复审 — 对驳回决定不服)

Professional-group discipline skill (ADR-0007 decision 1). The OA-response skill answers the examiner; this skill answers the **rejection decision** (驳回决定, 法38 / 细则59). Owns the pleading logic only; every assertion traces to a declared anchor. **Input = 驳回决定 + 申请文件 (claims + spec, as amended at rejection) + the OA history leading to it.** Missing input → fail loud.

## Read first

1. **Discipline**: `../patent-standards/references/professional-discipline.md` — declare / consume / cite / fail loud / never invent. Follow it.
2. **Anchors**: `../patent-standards/references/cn-professional.md` — patent-re-exam row: 法41; 细则65-68; 指南 IV-2 (形式审查 / 前置审查 / 合议审查 / 复审决定). Cite anchors, never renumber from memory.
3. **Honesty red line**: prior art and evidence from real delegated-search results or user-supplied material only.
4. **Workspace**: drafts in `.patent/re-exam/<case>/` (suggest gitignored).

## Trigger and window

收到驳回决定之日起 **3 个月内**请求复审 (法41.1); 复审请求书 + 理由 + 证据 (细则65); 复审费 (细则110). Late filing → the rejection becomes final; the window is the first thing checked, stated at the top of the draft.

## Workflow

### Step 0 — Input gate (fail loud)

- 驳回决定 text (file path preferred; no hand-pasting). Missing → stop.
- 申请文件 as of the rejection (the text the decision rejected) + the OA exchange (前次答复 + 修改) — needed to argue what was already overcome and what the decision still objects to.

### Step 1 — Decompose the rejection decision

Parse the decision into items: each 驳回理由 (法条 + 事实认定 + 审查员结论), which claims it hits, which prior-art references it relies on, and whether the decision cites the applicant's prior response. The 复审请求书 must answer **each reason item by item** — the same 逐条 discipline as the OA skill, now against the decision rather than the notice.

### Step 2 — Argumentation (复用 OA 论证逻辑, 对驳回决定)

- **事实认定错误**: the decision misstates the claim features or the reference's disclosure — read the reference, verify, and rebut with citation.
- **法条适用错误**: e.g. a novelty finding under 法22.2 that violates 单独对比 (指南 II-3 3.1), or an inventive-step finding that skips a step of the three-step method (指南 II-4 3.2.1.1) — argue the method was misapplied.
- **新理由 (reasons not previously raised)**: a rejection reason the applicant never had the chance to answer in the OA exchange — point it out (前置审查 / 合议审查 is the applicant's first opportunity to respond to it).
- **修改以克服缺陷**: if amendment is chosen, it must be **限于消除驳回决定或复审通知书指出的缺陷** (细则66) — narrower than the OA amendment power; never introduce new subject matter (法33); 替换页 (细则58).

### Step 3 — Draft the 复审请求书

Structure: 当事人信息 / 申请信息 (申请号、驳回决定文号、收到日期 → 期限计算) / 请求 (请求撤销驳回决定) / 逐项理由 (每项: 驳回理由 → 事实与法律分析 → 结论) / 修改后的权利要求书 (如修改) / 证据 (如有). Draft to `.patent/re-exam/<case>/复审请求书_<date>.md`.

### Step 4 — Procedure brief (程序纪律)

- **形式审查 → 前置审查 → 合议审查 → 复审决定** (细则65; 指南 IV-2): 前置审查 is the original examining division's re-look — a strong case there can end the procedure; the request should be written to win at 前置审查, not just at the collegial panel.
- **复审决定**: 驳回复审请求 (维持驳回) or 撤销驳回、继续审查 (细则67).
- **修改**: only 消除驳回决定或复审通知书指出的缺陷 (细则66) — same narrow rule as noted.
- **撤回**: before the decision (细则68).
- **救济**: dissatisfied with the 复审决定 → suit within 3 months of receipt (法41.2) — note it, do not draft it (litigation is out of scope).

### Step 5 — Human review gate

「以下为复审请求书【草稿】，须代理人/发明人复核后再递交。」 Self-check: every reason item answered / every assertion cited / every amendment within 细则66 + 法33 / 3-month window stated / 前置审查 angle argued.

## Fail loud (网关)

- No rejection-decision text → stop.
- A reason that cannot be grounded (unreadable reference, no material) → fail loud for that item; do not argue from memory.
- No evidence for a factual claim → state the gap; a factual assertion without evidence is not drafted.

## Boundaries

- In scope: 复审请求书 against a substantive-examination rejection; procedure brief (前置审查 / 合议审查 / 修改限制 / 撤回 / 救济提示).
- Out of scope (sibling skills, per ADR-0007): OA 答复 → `patent-oa-response`; 无效 → `patent-invalidation`; 评价报告 → `patent-evaluation-report`; claim strategy → `patent-claim-strategy`; 行政诉讼 (法41.2 起诉) → litigation, out of scope.
- Not a substitute for the agent's signature or formal filing.

## Minimal walkthrough (最小案例)

Input: 驳回决定 (理由: 权利要求1 相对 对比文件1 结合公知常识不具备创造性, 法22.3) + 申请文件 + 前次答复记录.

1. **Step 0**: 驳回决定 read; 3-month window computed from the stated receipt date — stated at top.
2. **Step 1**: items = 法22.3 rejection of claim 1; decision relies on 对比文件1 + 公知常识 assertion.
3. **Step 2**: re-verify 对比文件1 (read it) — the distinguishing feature 「限位配合 + 导向斜面」组合 is not disclosed; the 公知常识 assertion has no carrier; three-step argument (指南 II-4 3.2.1.1): 区别特征确定 → 实际解决的技术问题 → 无技术启示, 组合非显而易见. Amendment candidate (限组合入权1) 限于消除驳回理由 (细则66), 指向原说明书 (法33).
4. **Step 3-5**: 逐项复审请求书, every assertion cited `(per 法22.3; 指南 第二部分第四章 3.2.1.1 — cnipa.gov.cn)`; 前置审查 angle argued; 人审闸门 closing phrase + self-check.
