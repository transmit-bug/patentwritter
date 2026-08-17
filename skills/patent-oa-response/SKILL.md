---
name: patent-oa-response
description: "Draft a grounded response to a CN substantive-examination office action (审查意见答复, OA 答复) — parse the notice (type / deadline / itemized defects / legal basis / cited references), classify each rejection, rebuild inventive-step argumentation on the three-step method (三步法, 指南 II-4 3.2.1.1), choose the response strategy (opinion only / amend claims / amend spec / correction) with amendment-scope and estoppel checks, and produce an item-by-item opinion-statement draft for human review. Pure document discipline — no scripts, no keys, no in-package search; prior art comes from delegated / external sources and the user's own de-identified case archive. Use when the user asks to answer an office action, write an 意见陈述书, respond to a rejection on novelty / inventive step / clarity / support, or amend claims in response to an OA. Model-invoked discipline of the professional group (entry: patent-prosecution)."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Responding to a CN Office Action (审查意见答复)

Professional-group discipline skill (ADR-0007 decision 1). Owns the response logic only; every legal assertion traces to a declared anchor, every prior-art reference to a real delegated-search result or user-supplied material, every case reference to the user's own de-identified archive. **Input = 审查意见通知书 + 申请文件 (claims + specification, as filed and as amended).** If any input is missing, fail loud — never draft on guesswork.

## Read first

1. **Discipline**: `../patent-standards/references/professional-discipline.md` — declare / consume / cite / fail loud / never invent (shared, jurisdiction-neutral). Follow it.
2. **Anchors**: `../patent-standards/references/cn-professional.md` — the patent-oa-response row of the stage anchor map: 法22 / 26.4 / 33 / 37; 细则57.3 / 58 / 59; 指南 II-3 3.1 (单独对比), II-4 3.2.1.1 (三步法), II-8 4.10.3 / 4.11.3.2 (期限), II-8 5.1.1 / 5.2 (答复与修改). Cite these anchors, never renumber from memory.
3. **Honesty red line**: prior art only from real search-tool results or user-supplied material (`(prior art: <title>, <pub. no.>, <URL>)` / `(provided: <file or patent number>)`). Never invent references, dates, or experimental data.
4. **Workspace**: `.patent/` support layer — `sources/` `materials/` `queries/` + case archive (see below); drafts land in `.patent/oa/<case>/` (suggest gitignored).

## Workflow

### Step 0 — Input gate (fail loud)

- **PDF-first**: the notice is given as a file path (PDF preferred). Never ask the user to hand-paste or hand-copy the notice text. If the PDF has no extractable text (scan), state exactly that and offer OCR or a text-bearing PDF — still no hand-typing.
- **申请文件**: claims + specification needed to judge support (法33) and amendment direction (细则57.3). Missing → say what is missing, stop that part.
- No notice at all → stop. No output is better than an unverified response.

### Step 1 — Structured parsing (通知书结构化解析)

Extract and record, per notice item, into `.patent/oa/<case>/notice_struct.md`:

| Field | Meaning |
|---|---|
| `notice_kind` | 第一次审查意见通知书 / 再次审查意见通知书 / 补正通知书 / 驳回前通知 |
| `response_period` | **the period stated in the notice** (指定期限) — never assume |
| `patent_type` | invention / utility model |
| `defects[]` | per item: `item_no` (通知书条目编号), `statute` (法条, e.g. 法22.3), `examiner_view` (审查员观点), `compare_refs` (对比文件号), `claim_refs` (涉及的权利要求) |
| `defect_types` | novelty / inventiveness / clarity / support / disclosure / unity / formality / other |
| `domain` | technical domain — if inferred, mark `(推断)` |

Parsing is judgment, not transcription: the skill reads the notice text and structures it; anything inferred is explicitly marked. `notice_struct.md` is the skeleton the draft must answer **item by item** (逐条对应).

### Step 2 — Search before drafting (先检索再生成)

Search is mandatory and comes before any argument is written:

- **Prior art (delegated / external)**: same discipline as the B group — declare `[PRIOR-ART] <technology description>`, resolve via the **patents-search** skill (Valyu) or whatever search tool the environment exposes, or user-supplied material. Verify the examiner's cited references by reading them where possible (环境检索, e.g. provided PDFs). No search tool and no user-supplied prior art → fail loud for that portion.
- **Case archive (user's own de-identified history)**: a user-supplied directory (e.g. `.patent/cases/history/`), format = the case-note contract below. Retrieval = **environment capability only** (Read / Grep / Glob over the directory) — the package ships zero scripts, zero vector DBs, zero keys.
- **空库禁糊弄**: if the archive is empty and search returned nothing usable, output only an outline + strategy options — never pretend to cite a historical case, never fabricate a reference.
- Every case hit is cited with `(案例 <case_id>: 差异 <diff_fields>)` — the difference vs the current case (statutes / defect_types / domain / patent_type), and why it is relevant.

### Step 3 — Defect classification & argumentation (理由分类 + 三步法)

Classify each item before arguing:

| Defect | Anchor | Argumentation direction |
|---|---|---|
| Novelty | 法22.2; 指南 II-3 3.1 (单独对比) | distinguishing feature not disclosed by the single reference; 惯用手段直接置换 doesn't hold |
| Inventive step | 法22.3; 指南 II-4 3.2.1.1 | three-step method (below) |
| Clarity / support / conciseness | 法26.4; 指南 II-2 3.2.1-3.2.3 | interpretation via spec embodiments / reference numerals; supported by original disclosure |
| Unity | 法31.1; 细则39 | same general inventive concept |
| Amendment scope | 法33 | red line on every amendment (Step 4) |
| Utility | 法22.4 | reproducible, industrially applicable |
| Subject matter | 法5 / 25 | statutory exclusions |
| Disclosure | 法26.3 | enablement from the spec as filed |
| Formality | 细则 / 指南 Part I | correction path (补正) |

**Creative argumentation — the three-step method, rebuilt from 指南 II-4 3.2.1.1** (the anchor file is the authority; case-library templates are only habits):

1. **最接近的现有技术** — identify the closest prior art (single reference with the most shared features / closest technical problem).
2. **区别特征与发明实际解决的技术问题** — state precisely what the claim does not share with that reference; from those distinguishing features, restate the technical problem actually solved.
3. **显而易见性判断** — argue whether a person skilled in the art would have been taught by the prior art as a whole to combine (技术启示): distinguishing features not disclosed, features mutually support each other rather than simple aggregation (非简单叠加), combination not obvious.

The four-part creative-argumentation habit (absorbed from the mode-D case practice, now explicitly anchored): ① verify the examiner's distinguishing-feature finding against the claim and the cited reference — read the reference, don't accept the finding on faith; ② argue mutual functional support, not simple superposition; ③ any proposed amendment points to a support location in the **original** spec (法33) — unknown location → mark 「待发明人指认段落」; ④ argue the effect (incl. unexpected effect — use cautiously, only with support). Every step carries its anchor citation.

### Step 4 — Strategy options (user picks)

Offer at minimum: **仅意见陈述 / 修改权利要求 / 修改说明书 / 补正形式**. For each option:

- **超范围风险标注** (per 法33): every amendment is checked against the original specification + claims scope; a risky amendment is labeled with the risk, never silently passed.
- **细则57.3**: amendments after an OA shall be directed to the defects pointed out in the notice; 全面适应性修改 keeps the text consistent (细则58 replacement pages).
- **禁反悔审查**: review statements and amendments for what they would concede in a later infringement dispute (禁止反悔原则) — flag any wording that narrows scope unnecessarily.

### Step 5 — Item-by-item draft (逐条草稿)

- Answer **every** numbered item of the notice; skip none.
- Each legal assertion carries its citation: `(per 法22.3; 指南 第二部分第四章 3.2.1.1 — cnipa.gov.cn)`.
- Case references carry id + difference; prior art carries real publication data.
- Deadline box at top: 指定期限 = <date from the notice>; background note 第一次 4 个月 / 再次 2 个月 (指南 II-8 4.10.3 / 4.11.3.2) — **never** a hard number, the notice governs.
- Output: `.patent/oa/<case>/意见陈述草稿_<date>.md`.

### Step 6 — Human review gate (人审闸门)

The draft is a **draft**, not a filing. Close with the fixed confirmation: 「以下为审查答复【草稿】，须代理人/发明人复核后再递交。」 Self-check before delivery:

- [ ] every legal assertion cited (else fail loud for that portion)
- [ ] every prior-art reference real and cited with publication data
- [ ] every case reference carries case_id + 差异
- [ ] every amendment points to an original-spec support location or 「待发明人指认段落」
- [ ] no item of the notice left unanswered
- [ ] no statement that over-commits under 禁止反悔

## Case archive contract (脱敏案例档案)

User-supplied directory (e.g. `.patent/cases/history/`), one file per case, frontmatter contract:

```yaml
case_id: <id>
status: history            # history | pending | draft
patent_type: invention     # invention | utility_model
statutes: [法22.3]         # legal bases at issue
defect_types: [inventiveness]   # novelty | inventiveness | clarity | support | disclosure | formality | other
domain: <technical domain>
notice_kind: first_OA      # first_OA | subsequent_OA | correction
outcome: amended_then_granted   # granted | rejected | pending | amended_then_granted | ...
strategy: amend_claims     # argue_only | amend_claims | amend_spec | correction | other
compare_refs: [<pub. no.>]
related_cases: []
redacted: true             # must be true on entry
tags: []
```

Body (suggested): 通知书要点 → 策略 → 陈述要点 → 修改摘要 → 结果 → 关联案 → 对比文件. **脱敏先于入库**: client names, application numbers, undisclosed parameters are removed before storing; redaction is human-reviewed (rules are helpers, the discipline is the human gate). An empty archive is fine — it triggers 空库禁糊弄, not silence or invention.

## Deadlines (期限纪律)

第一次审查意见 4 个月 / 再次 2 个月 (指南 II-8 4.10.3 / 4.11.3.2) — background for planning only. The operative deadline is the 指定期限 stated in the notice; it is extendable on request per 细则 — the skill states the mechanism, never hard-codes a number.

## Abstract note (摘要 300 字)

If the response touches the abstract: annotate the three-text inconsistency — 细则2023 第26条已删字数限制 vs 指南2023 第一部分第一章 4.5.1 仍要求 ≤300 字 vs 2025 大纲按 300 字表述. 按细则为准; 指南仍在初步审查执行 (超 300 字会被通知删节). See `cn-professional.md`.

## Boundaries

- In scope: OA response at substantive examination (invention) and preliminary-examination correction paths (补正).
- Out of scope (sibling skills, per ADR-0007): 复审 → `patent-re-exam`; 无效 (请求 + 答辩) → `patent-invalidation`; 评价报告 → `patent-evaluation-report`; professional claim strategy (答复修改策略 / 分案 / 优先权 / 布局) → `patent-claim-strategy`; mechanical drafting → B 组 self-service skills.
- Not a substitute for the agent's signature or formal filing; the draft exists for human review.

## Minimal walkthrough (最小案例 — verify the path)

Input: 第一次审查意见通知书 (PDF) + 申请文件. 审查员观点: 权利要求1 相对 对比文件1 与公知常识的结合不具备创造性 (法22.3), 区别技术特征仅为常规结构替换.

1. **Step 0-1**: read the notice PDF; notice_struct: `notice_kind=first_OA`, `response_period=<通知书载明>`, item 1: `statute=法22.3`, `compare_refs=[对比文件1]`, `defect_types=[inventiveness]`.
2. **Step 2**: declared prior-art search + user case archive scanned (Read/Grep). No usable hit → record 空库; draft proceeds on anchors + strategy only.
3. **Step 3**: three-step — closest prior art = 对比文件1; distinguishing features = 「限位配合 + 导向斜面」组合; argue 对比文件1 未公开该组合、二者功能相互支持非简单叠加 (指南 II-4 3.2.1.1); amendment candidate points to 原说明书实施例 (法33).
4. **Step 4**: strategy = 修改权利要求 + 意见陈述; 超范围风险 checked; 禁反悔 review (don't concede the combination is optional).
5. **Step 5**: item-by-item 意见陈述草稿, every assertion cited `(per 法22.3; 指南 第二部分第四章 3.2.1.1 — cnipa.gov.cn)`.
6. **Step 6**: 人审闸门 closing phrase + self-check.

(案例形态参照包仓库 `docs/research/pattern-d-oa-rag.md`(不随安装分发) 的创造性卡扣例; 论证纪律以本文件三步法为准, 不从案例模板导入.)
