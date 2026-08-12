# Delegation Contract (委托契约)

The contract between a thin patent-writing skill and external retrieval. Every writing skill in this repo follows it. Four clauses — **declare**, **consume**, **cite**, **fail loud** — and one prohibition: **never invent**.

Status: prototype decision for wayfinder ticket #3. The catalog anchors below come from `docs/research/standards-catalog.md` (ticket #2).

## 1. Declare — 声明需要,不自行抓取

Before making any legal or prior-art assertion, the skill names what it needs grounded on. Two kinds of needs:

- `[STANDARD] <jurisdiction> <topic>` — a legal/standards assertion. Resolved via the patent-standards catalog (which material governs) + whatever tool the environment offers to actually read that material (web fetch, knowledge base, user-supplied file).
- `[PRIOR-ART] <technology description>` — a novelty/prior-art claim. Resolved via delegated search (patents-search/Valyu or any search tool the environment exposes).

The skill never fetches, never holds keys, never knows URLs beyond what the catalog declares.

## 2. Consume — 消费结果

The skill works only from what retrieval returned. Search results are real patents with numbers/URLs; standards text is what was actually read from the declared material. No result, no assertion.

## 3. Cite — 引用格式

Citation anchors follow the cross-system practice confirmed by the research ticket:

- CN: `专利法 第X条` / `实施细则 第X条` / `指南 第X部分第X章` (e.g. `指南 第二部分第四章[创造性]`, `专利法 第22条[新颖性/创造性/实用性]`, `实施细则 第20条[说明书]`)
- US: `35 U.S.C. §X` / `37 CFR §X` / `MPEP §X` (e.g. `MPEP §2106[subject matter eligibility]`, `35 U.S.C. §112`, `37 CFR §1.75[claims]`)

Every grounded assertion carries a citation in output:

- Standards: `(依据: <材料> §<锚点>[<topic>] — <官方来源URL>)` / `(per <material> §<anchor> — <official URL>)`
- Prior art: `(先有技术: <标题>, <公开号>, <URL>)` / `(prior art: <title>, <pub. no.>, <URL>)`
- User-supplied grounding counts: `(provided: <file or patent number>)`

A paragraph with a legal or prior-art assertion and no citation is a defect the skill fixes before delivering (clause 5).

## 4. Fail loud — 缺依据即停

When a needed grounding cannot be obtained — no search tool, no way to read the catalog material, tool error — the skill **stops that portion** and emits:

```
无法获取依据: [STANDARD] CN 创造性 / [PRIOR-ART] ...
缺少: <tool or material>
请提供: <concrete options — enable a search tool, supply the material as a file, or waive>
```

It does not draft the ungrounded portion. Partial output is allowed: grounded parts deliver, ungrounded parts are listed as blockers.

## 5. Self-check — 交稿前扫描

Before delivering, the skill scans its own output for legal/prior-art assertions lacking citations. Any found → either cite from what was retrieved, or fail loud for that portion.

## Worked example — claims-drafting excerpt

User: "一种手术机器人微量注射系统,包含压力反馈闭环"

1. **Declare**: `[PRIOR-ART] 手术机器人 微量注射 压力反馈` → delegated search returns 8 patents.
2. **Consume**: closest prior art = CN1xxxxxxxA (外科手术机器人注射控制); key difference = 压力反馈闭环 + 微量泵脉动抑制.
3. **Declare**: `[STANDARD] CN 创造性` → catalog: 审查指南 第二部分第四章 governs 创造性; environment reads the section.
4. **Draft** (grounded):
   - 技术问题段 cites the prior art: `(先有技术: 一种外科手术机器人注射系统, CN1xxxxxxxA, https://patents.google.com/patent/CN1xxxxxxxA)`
   - 区别特征段: "与 CN1xxxxxxxA 相比,本方案通过压力反馈闭环抑制微量泵脉动 (依据: 指南 第二部分第四章[创造性] — cnipa.gov.cn)"
   - 技术效果段: "…产生了预料不到的技术效果" only if the effect is shown; otherwise stated plainly.
5. **Self-check**: every legal/prior-art assertion above carries a citation → deliver.

## Fail-loud example

Environment has no search tool and the user supplied no prior art. `[PRIOR-ART]` unresolvable →

```
无法获取依据: [PRIOR-ART] 手术机器人 微量注射 压力反馈
缺少: 可用的专利检索工具 (patents-search/Valyu 或任何环境搜索)
请提供: 安装/启用一个检索工具,或直接提供相关专利号/文件,或明确放弃新颖性验证
```

The skill drafts only what it can ground (structural sections, embodiments from the disclosure) and lists the prior-art blocker.

## Conventions for consuming skills

- Never restate law from memory; if the catalog material can't be read, fail loud.
- Never list prior art without a search result or user-supplied provenance.
- Key handling, fetching, scraping: out of contract. The environment does it.
- `patents-search` (Valyu) is the canonical delegated search in this repo; any environment search tool may substitute when present.

## Status 与适用范围(2026-08-11 更新)

- **历史**:本契约是 wayfinder prototype 决策(ticket #3),旧包(CN/US 专业撰写)的架构基础;2026-08-11 之前所有 writing skill 遵循它。
- **现状(ADR-0004 重构后)**:完整版(declare/consume/cite)仍适用于 `skills/professional/` 组(US 技能,当前 `disable-model-invocation` 隐藏)。
- **自服务组(`skills/self-service/`)采用简化变体**:
  - 法律断言:直接引用 `patent-standards` 的 **Verified rule anchors**(2026-08-11 对 CNIPA 全文实测核实),不再声明 `[STANDARD]` 需求、不强求环境检索法条。
  - 现有技术:按**诚实红线**写背景技术(三类素材:发明人已知方案 / 客观通用问题 / 检索工具真实返回),不再声明 `[PRIOR-ART]`;拿不到就不写,绝不编造公开号。
  - **Fail loud 保留**:缺输入(四要素不齐)/缺工具(如无 dot)时明说缺什么,不硬写。
  - 引用格式:条号即锚点(如 `细则第20条`),需向用户解释时附 `patent-standards` 锚点来源。

## 旧版 Status(历史记录)

- **Accepted** (prototype ticket #3, 2026): shape confirmed, anchors verified against the research catalog. The patent-standards skill (ticket #4) implements the catalog + this contract; the four writing skills (ticket #5) consume it. (四技能已随 ADR-0004 重构:architect/diagram-generator 删除,application-creator/claims-analyzer 移至 professional 组隐藏。)
