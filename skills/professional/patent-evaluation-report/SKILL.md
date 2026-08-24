---
name: patent-evaluation-report
description: "Decide whether and how to use a CN patent evaluation report (专利权评价报告) for utility models and designs: who may request it and when, its evidentiary role in infringement disputes, the open-license obligation, and how to read the CNIPA's evaluation — the report itself is made by CNIPA, not drafted here. Use when the user asks about a 专利权评价报告 / 评价报告, whether to request one, 维权前评估, or how to respond to its findings."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Patent Evaluation Report (专利权评价报告 — 请求与使用)

Professional-group discipline skill. Unlike the pleading skills, the evaluation report is **made by CNIPA, not drafted by the agent** — this skill owns the decision logic around it: whether to request, by whom, when, and how to read and use the result. **Input = 实用新型 / 外观设计 专利文件 (claims or 图片/照片) + the purpose (维权前评估 / 应对侵权指控 / 开放许可).** Missing input → fail loud.

## Read first

1. **Discipline**: `../patent-standards/references/professional-discipline.md`. Follow it.
2. **Anchors**: `../patent-standards/references/cn-professional.md` — patent-evaluation-report row: 法50.2, 法66.2; 细则62-63; 指南 V-10. Cite anchors.
3. **Honesty red line**: any prior-art discussion in the skill's output traces to real search results or user-supplied material — the skill traces every prior-art discussion only to real search results or user-provided material.
4. **Workspace**: notes in `.patent/evaluation-report/<case>/` (suggest gitignored).

## When a report is needed (何时需要)

| Situation | Basis |
|---|---|
| Infringement dispute: the court / patent administrative department may require the report; it serves as evidence for deciding whether to suspend proceedings (中止诉讼) | 法66.2 |
| 维权前评估: assess the patent's validity (novelty / inventive step) before suing or licensing | 法66.2 (report covers search + evaluation of the utility model / design) |
| 应对侵权指控: an accused infringer evaluates the opposing patent before responding | 细则62 (2023 addition — the accused infringer is an explicit requester) |
| Open license: a 实用新型 / 外观设计 open-license declaration must be accompanied by a report | 法50.2 |
| 许可 / 交易前: an interested party (利害关系人) evaluates before licensing or transfer | 细则62 |

## Decision logic (是否请求、由谁请求)

1. **主体资格**: 专利权人 / 利害关系人 / **被控侵权人** may request (细则62) — confirm the requester falls in one of the three; only then proceed.
2. **时机**: after grant announcement (授权公告后); the applicant may also request at registration (办理登记手续时). The report is made **within 2 months** of the request (细则63) — the timeline matters when a dispute deadline looms.
3. **唯一性**: only one report per patent right regardless of how many requesters (细则63) — a later requester gets the existing report, not a new evaluation.
4. **查阅复制**: any entity or individual may inspect / copy (细则63) — assume the report is public to the other side in a dispute.
5. **成本**: 评价报告请求费 (细则110) — stated, follows the amount shown in the system at filing time.

## Request check (请求书核对)

Request form fields: 专利号、专利类型 (实用新型 / 外观设计)、请求人信息、与专利权的利害关系 (专利权人 / 利害关系人 / 被控侵权人 — attach the supporting basis). The skill fills the form data the user supplies and flags anything missing (fail loud) — it does not assert the report's conclusions in advance.

## Reading the report (报告解读框架)

The report (指南 V-10 3.2 内容 / 3.3 检索) evaluates the utility model / design against novelty and inventive step (实用新型) or 明显区别 (外观设计). Reading discipline:

- **检索范围**: what the CNIPA searched (databases, classifications) — a finding "未发现影响新颖性的对比文件" is grounded in that search, not an absolute guarantee.
- **逐项结论**: each evaluated claim (or design) and its conclusion (是否具备新颖性 / 创造性), with cited references. The skill re-reads any cited reference before commenting — re-reads each cited reference before commenting.
- **效力**: the report is **not an administrative decision and is not appealable** (指南 V-10); in litigation it is an evidentiary document, and the court may still independently assess validity (法66.2). When the user asks "can we appeal the report", answer 不可诉 with the anchor.

## Use cases (使用位置)

- **维权前**: a negative finding (评价报告认定不具备创造性) is a red flag before suing — the skill states the finding's implication and routes to 无效 readiness (`patent-invalidation`) or settlement thinking; it does not draft the strategy silently.
- **应对侵权指控**: an accused infringer's request buys a grounded validity picture before responding (细则62); a positive report for the patentee weakens that angle — the skill states what the report shows, nothing more.
- **开放许可**: the declaration must include the report (法50.2) — verify the condition before the user commits to open licensing.

## Fail loud (网关)

- No patent text (claims or 图片/照片) → stop.
- No purpose (which of the four situations) → ask, don't guess.
- Requesting party not one of the three 细则62 subjects → say so; a report cannot be requested by a non-subject.

## Boundaries

- In scope: request decision, request-form check, report-reading framework, evidentiary-role statements.
- Out of scope (sibling skills): 无效 → `patent-invalidation` (a negative report feeds it, it does not replace it); OA 答复 → `patent-oa-response`; 复审 → `patent-re-exam`; claim strategy → `patent-claim-strategy`; 侵权诉讼代理 → litigation, out of scope; drafting the report itself → CNIPA's function, remains CNIPA's function; the skill interprets and guides instead.
- Not a substitute for the agent's signature or formal filing.

## Minimal walkthrough (最小案例)

Input: 实用新型 专利文件 (授权公告后) + purpose 维权前评估.

1. **Decision**: requester = 专利权人 (细则62 ✅); 时机 = 授权后 (✅); report within 2 months (细则63) — timeline stated.
2. **Request check**: 请求书 fields from user data; nothing missing.
3. **Report reading**: when the report arrives, itemize each claim's 新颖性 / 创造性 conclusion (指南 V-10 3.2/3.3), re-read cited references, and state the evidentiary role (法66.2) + non-appealability — no invented conclusions in between.
4. **Use**: negative finding → flag validity risk, route to 无效 readiness (patent-invalidation); positive → proceed with the dispute plan.
5. **人审闸门**: 输出为评估与解读【草稿】，须代理人/当事人复核；报告结论以 CNIPA 出具文本为准。
