---
name: patent-invalidation
description: "Draft CN invalidation pleadings (无效宣告, both directions): the 无效宣告请求书 with grounds inside the closed 细则69.2 list and the evidence register, or the patentee's 答辩意见陈述书 rebutting grounds (incl. reverse three-step method) and amending claims within the narrow 细则73 limits — with the oral-hearing, deadline, estoppel, and withdrawal procedure embedded. Use when the user asks to request invalidation, respond to an invalidation request, draft an 无效宣告请求书 or 答辩意见陈述书, or assess whether a ground is admissible."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Invalidation (无效宣告 — 请求方与答辩方)

Professional-group discipline skill. Two directions, one skill: **请求方** (request invalidation) and **答辩方** (patentee responding). Owns the pleading logic only. **Input = 专利文件 (claims + spec as granted) + the other side's material (patent for the requester; 无效宣告请求书 + 证据 for the respondent).** Missing input → fail loud.

## Read first

1. **Discipline**: `../patent-standards/references/professional-discipline.md`. Follow it.
2. **Anchors**: `../patent-standards/references/cn-professional.md` — patent-invalidation row: 法45-47; 细则69-76; 指南 IV-3 (incl. 4.6 amendment), IV-4 (oral hearing), IV-8 (evidence). Cite anchors.
3. **Honesty red line**: every piece of evidence is a real document (patent publication, 公知常识 carrier, internet evidence with disclosure date); no invented references, dates, or data.
4. **Workspace**: drafts + evidence register land in `.patent/invalidation/<case>/` (suggest gitignored).

## The two directions

### Direction A — 请求方: 无效宣告请求书

**Trigger**: from the grant announcement, any entity or individual may request invalidation (法45). Request form + necessary evidence, in duplicate (细则69.1); 请求费 (细则110).

**Grounds = the closed list of 细则69.2** — grounds outside it are inadmissible (细则70 not-accepted cases include insufficient grounds / evidence, same grounds + evidence re-request). The admissible set:

| Source | Grounds |
|---|---|
| 专利法 | 第2条 (subject matter), 第19.1条, 第22条 (novelty / inventive step / utility), 第23条 (design), 第26.3条 (disclosure), 第26.4条 (support / clarity), 第27.2条 (design pictures), 第33条 (amendment scope) |
| 细则 | 第11条, 第23.2条, 第49.1条 |
| 专利法 | 第5条 / 第25条 (excluded subject matter), 第9条 (double patenting) |

For each ground: 条、款、项 are independent grounds; pick the most persuasive and argue it in depth rather than listing everything. **三步法反向** for inventive-step grounds (法22.3): argue that the claimed invention *is* obvious to a person skilled in the art — (1) closest prior art among the cited references; (2) distinguishing features and the actually-solved technical problem; (3) technical teaching in the prior art as a whole makes the combination obvious (the reverse of the OA-response direction; same anchor 指南 II-4 3.2.1.1). When several combinations are possible, argue the strongest combination first.

**Evidence register (证据清单)** — the core record, one entry per piece:

| Field | Meaning |
|---|---|
| `ev_no` | evidence number |
| `source` | where it came from (patent pub. / 公知常识工具书 / 互联网) |
| `publication_date` | disclosure date — the basis for whether it counts as prior art |
| `proves` | what fact it establishes (feature disclosed / teaching / common knowledge) |
| `filed` | whether it was filed with the request or added later |

Evidence: 证据一式两份 with the request (细则69.1); grounds may be added / evidence supplemented **within 1 month of the request** (细则71) — the evidence-deadline discipline. 公知常识 and internet evidence follow 指南 IV-8 (disclosure-time proof).

**Draft structure**: 当事人信息 / 专利信息 (专利号、授权公告日) / 请求宣告无效的范围与理由 (逐项: 法条、款、项 + 论述) / 证据清单 / 请求结论. Draft to `.patent/invalidation/<case>/无效宣告请求书_<date>.md`.

**Procedure**: 口审 (细则74; 指南 IV-4) — attend; failure to attend without cause → 视为撤回. The request may be withdrawn before the decision (细则76).

### Direction B — 答辩方: 意见陈述书 (对无效宣告请求的答复)

**Trigger**: 转送文件通知书 (细则72) — the requester's 请求书 + evidence are transferred to the patentee, who states opinions.

**First pass — grounds & evidence audit** (before drafting anything):

1. **理由范围**: is each asserted ground inside the closed list of 细则69.2? A ground outside it is inadmissible — say so, anchored.
2. **证据核实**: for each piece of evidence — 真实性 (is it a real document?), 公开时间 (is it prior art against the patent? disclosure date), 公开内容 (what does it actually disclose?). Read the evidence; never accept the requester's characterization.
3. **证据与理由的因果关系**: does the evidence actually support the ground as pleaded? (e.g. a novelty ground needs a single reference disclosing every feature.)

**Response strategy**: 针对证据论述 (distinguishing features not disclosed in the cited reference / no technical teaching / combination not obvious — three-step method in defense); 提供反证 (counter-evidence, incl. evidence that the alleged prior art was not public before the filing date); 据理反驳. When necessary, amend claims to **partially maintain** the patent — under the narrow invalidation limits of 细则73:

- amendment confined to the claims;
- must not broaden the protection scope (不得扩大保护范围);
- must not change the subject-matter name (不改变主题名称);
- generally must not add features not present in the granted claims (一般不增加未包含在授权权利要求书中的技术特征);
- invention / utility model: the spec and drawings may not be amended;
- design: pictures / photos / brief explanation may not be amended;
- amendments must not exceed the original disclosure (法33).

**禁反悔审查**: any statement or amendment in the response becomes a concession in later infringement litigation — flag wording that narrows scope without need (same discipline as OA response, harsher here: the invalidation record is public).

**Draft structure**: 当事人信息 / 对请求书理由的逐项回应 (每项: 请求人理由 → 证据核实结论 → 我方论述/反证/修改) / 修改后的权利要求书(如修改) / 结论 (请求维持专利权有效 / 部分维持). Draft to `.patent/invalidation/<case>/答辩意见陈述书_<date>.md`.

**Decision & effects**: CNIPA examines, decides, registers and announces (法46.1); the invalidation decision is appealable within 3 months, the other party joins as third party (法46.2); an invalidated patent is deemed never to have existed, no retroactive effect, bad-faith damages exception (法47).

## Procedural discipline (程序纪律 — 内嵌)

- **口审 (细则74; 指南 IV-4)**: oral hearing on request / as arranged; absence consequences (请求方 → 视为撤回; 答辩方 → 缺席审理). Attendance and preparation are part of the pleading, not an afterthought.
- **举证期限 (细则71; 指南 IV-3 4.3)**: requester may add grounds / supplement evidence within 1 month of the request; the respondent's supplementary evidence follows the panel's schedule — evidence filed late is inadmissible unless justified.
- **修改限制 (细则73)**: narrowest amendment power of the whole pipeline — claims only, no broadening, no spec / drawings (invention / utility model), no design image changes. Re-read the anchor before proposing any amendment.
- **禁反悔**: every concession in the record is binding; review statements and amendments for downstream infringement-litigation exposure.
- **撤回 (细则76)**: requester may withdraw before the decision.

## Evidence retrieval (证据检索 — 委托式)

Same discipline as the B group and the OA skill: declare `[PRIOR-ART] <technology description>` / `[STANDARD] CN <topic>`, resolve via the **patents-search** skill (Valyu), the CNIPA 公布公告系统 (declared external source, manual steps in `../patent-standards/references/catalog.md`), or user-supplied documents. 公知常识 assertions require a carrier (教科书 / 技术词典 / 工具书) — cite it, don't assert from memory. The package ships no crawler, no search harness, no keys. No usable evidence → fail loud for that ground; a ground without evidence is not drafted.

## Fail loud (网关)

- No patent text (claims / spec as granted) → stop.
- No evidence obtainable for a ground → state the ground cannot be pleaded with grounding; do not draft it from memory.
- No extractable request text for the respondent → state what is missing.

## Boundaries

- In scope: 无效宣告请求书 (请求方) + 答辩意见陈述书 (答辩方), grounds audit, evidence register, amendment under 细则73, oral-hearing preparation.
- Out of scope (sibling skills): 复审 → `patent-re-exam`; OA 答复 → `patent-oa-response`; 评价报告 → `patent-evaluation-report`; claim strategy → `patent-claim-strategy`; mechanical drafting → the self-service group.
- 诉讼 / 行政处理代理 (法46.2 起诉、侵权诉讼): out of scope — the pleading ends at the CNIPA decision stage; litigation is not a patent-agency-only practice in this package.
- Not a substitute for the agent's signature or formal filing.

## Minimal walkthrough (最小案例 — 请求方, 创造性无效)

Input: granted patent (claims + spec) + 对比文件2 (delegated search result). Goal: 请求宣告专利权无效, 理由 = 法22.3 (inventive step).

1. **Audit**: ground 法22.3 is inside 细则69.2's closed list ✅; 对比文件2 publication date before filing date (verifiable) ✅.
2. **Three-step reverse**: closest prior art = 对比文件2; distinguishing features identified; argue the prior art as a whole teaches the combination — 区别特征 A 在对比文件2 中公开, 特征 B 属公知常识 (工具书出处), 结合显而易见 (指南 II-4 3.2.1.1).
3. **Evidence register**: 对比文件2 (专利文献, 公开日, 证明事项) + 公知常识载体; 一式两份.
4. **Draft**: 无效宣告请求书 — 逐项理由 + 证据清单, every assertion cited `(per 法22.3; 细则69.2; 指南 II-4 3.2.1.1 — cnipa.gov.cn)`.
5. **Procedure**: 1-month window to supplement evidence (细则71) noted; 口审 prepared (细则74).
6. **人审闸门**: 「以下为无效宣告请求书【草稿】，须代理人/当事人复核后再递交。」 + self-check (every ground in the closed list / every evidence real / every assertion cited / 禁反悔 reviewed).
