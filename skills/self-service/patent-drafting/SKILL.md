---
name: patent-drafting
description: "Draft and revise the CN patent text documents in Chinese — five-part specification (说明书) written first as readable technical prose, claims (权利要求书) then distilled from it, plus abstract; the support chain owned in one place. Use when the user asks to write or revise claims or the specification; direct entry needs existing drafts or a complete four-element record."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Patent Drafting (specification → claims → abstract)

Role: **discipline** of the self-service group. Input: the four elements (technical problem / technical solution / distinguishing feature / technical effect) + application type (invention / utility model), plus the route record from `../patent-intake/SKILL.md`. If any input is missing, go back to the interview — never write on guesswork. This skill does not interview the inventor; when a fact is missing, return it as a blocker to patent-intake.

Order is fixed: **the specification comes first**, written as readable technical prose; **claims are then distilled from the specification**; the abstract closes. Rationale: the disclosure's content quality is the one thing that cannot be repaired later — form can be fixed in prosecution, missing content cannot. A gap found while distilling Part B is fixed by re-entering Part A, not by papering over it.

## The voice wall (语体边界 — applies to every part of this skill)

Two registers live in this skill and must not leak into each other. This section is the **single source of truth** for the boundary; other skills point here by the token "voice wall / 语体边界":

- **Specification register (Part A)**: natural technical prose an engineer can read — the inventor should recognize their own invention in it. Use "所述" only when referring back to an already-introduced component in the same document; **never copy claim syntax ("其特征在于", feature chains, "所述X…所述Y") into narrative paragraphs**. The 发明内容 and 具体实施方式 sections describe how the invention works, they do not recite claim limitations.
- **Claims register (Part B)**: statutory claim language is legitimate here only. Formality details (citation rules, antecedent basis, single full stop, parenthetical numerals, leading phrases) are **not drafted against inline** — write naturally within the register, then let `../patent-compliance/SKILL.md` 检查2 run the formal sweep.

Term consistency spans both registers: once Part A names a component 传感器, no document in this set may call it 感应器.

On completion, update the claims and specification stages in drafts/application-info.md (✓, or `blocked: <reason>`).

## Type differences (settle the template first)

| Dimension | Invention | Utility model |
|---|---|---|
| Independent-claim subject | Product / method / system | **Product only** (shape / construction / combination) |
| Method features | Algorithm / process allowed | **No method steps as main features**; only known method names as qualifiers |
| Reference numerals | Allowed, in parentheses | Same |
| Typical claim count | 8-15 | 5-10 |

---

## Part A — Writing the specification (说明书, five parts)

Standards pointer: `../patent-standards/references/cn-invention-utility.md`.

### A1 Technical field → Done when: one sentence lands on the claimed subject

Example shape: "本发明涉及<宽领域>技术领域，特别涉及<窄领域>。" The narrow field echoes the eventual independent-claim subject name. One sentence — it is a label, not prose to polish.

### A2 Background art → Done when: every fact has an owner, zero fabrication

**Honesty red line** (the hardest rule in this skill): every background-art statement must answer "where did this come from" — a prior solution the inventor knows (describe truthfully; include a patent number/reference if one exists, leave out if not), an objective problem generally recognized in the field, or a real search-tool result. For a paper-source case, the paper's related-work section belongs here (see `../patent-intake/references/source-modes.md`). Inventing patent numbers, references, company names, or "某公司公开了…" is forbidden — if you cannot source it, cut it or rephrase as a common problem.

Structure: what the prior solution is → what specific problem its implementation has → the consequences → close with "因此，亟需一种<方案>…" leading into the summary of invention. Deficiencies are stated against the implementation process, not as empty assertions.

### A3 Summary of invention → Done when: problem/solution/effect correspond three ways, in readable prose

For algorithm/control/signal/optimization inventions, run the **core-formula gate**. Filing track: 2-5 equations + variable/边界 + embodiment mapping；交底书 track: 推荐≥1 equation + variable table + boundary + 10-30行伪代码（见 `patent-intake/references/disclosure-document.md` 分型豁免与 `references/8-points.md`⑤⑥⑦），规范描述与公式互指，不以描述替代定义；未覆盖项在 `application-info.md` 豁免说明，不编造。If unknown, return a blocker; never invent.

Three-way correspondence:
- **Technical problem to be solved**: maps one-to-one to the background-art deficiencies; one sentence, optionally adding "本发明目的在于…".
- **Technical solution**: narrate how the invention works as connected paragraphs — what each part does, how data/signals flow, why the arrangement solves the problem. Write it so the inventor nods along; do not expand claim-style feature lists.
- **Beneficial effects**: written against the prior art. **If there is data, write the data (state the measurement conditions); if not, write the mechanism reasoning ("由于…，因此…")**. Fabricating experimental data is forbidden; real data from inventor material may be cited with its conditions (数据可用性 flag).

### A4 Brief description of drawings → Done when: one sentence per figure, numerals stay in bounds

"图1为本发明实施例提供的<X>的结构示意图；" — one sentence per figure, listing all figures. Figure numbers correspond one-to-one to the drawings.

### A5 Detailed description → Done when: a person skilled in the art can reproduce from it

The test for **sufficient disclosure**: an ordinary person skilled in the art, after reading it, can make the thing. Missing parameters, missing steps, missing data flows all fail.

Embodiment writing protocol — every embodiment must cover:
1. **Structure / connections**: parts list + connection relationships (written against the reference numerals).
2. **Working flow**: the complete process from input to output, with the key steps stated.
3. **Key parameters**: values / thresholds / counts / dimensions, as ranges or concrete values.
4. **Data flow**: how data/signals move between modules, who triggers whom.
5. **Core formulas and logic**: display the formula in editable math form in the Markdown source, define all symbols immediately after it, state threshold/initialization/boundary handling, and explain how the result changes the physical or system operation. A flowchart alone does not replace the formula when the formula is the inventive mechanism.

Embodiment quality requirements:
- At least 2-3 embodiments, and they must be **genuine variants** (real differences in deployment location / data flow / triggering), not the same paragraph re-templated with substitutions. If you cannot produce a genuine variant, one solid embodiment beats three watered-down ones.
- Every generic term that will later become a claim feature lands in at least one concrete embodiment; if a planned generalization has no landing point, either add the embodiment or narrow the plan — do not leave the gap for compliance to find.
- Narrative voice per the voice wall: prose first; "所述" only for back-references to introduced components.

Utility model notes:
- Structure / connection / fitting at the core, written against the drawings.
- State shape, construction, and positional relationships (above/below/connected/fitted) — these are the utility model's protection focus.

---

## Part B — Distilling the claims (权利要求书) from the specification

Input: the finished Part A draft. Every claim must be traceable to specification paragraphs or embodiments (support chain); distillation never introduces content Part A does not contain — if a needed feature is missing there, go back to Part A.

Standards pointer: `../patent-standards/references/cn-invention-utility.md`.

### B1 Pin down the essential features → Done when: every retained feature passes the deletion test

For every feature in the solution ask: **if deleted, is the technical problem still solved?** Yes → non-essential, demote to a dependent claim or drop it. The independent claim keeps only the features without which the problem cannot be solved.

- Essential features come from the **problem**, not from implementation detail: to solve "unreliable recognition", the essential thing is a "recognition mechanism", not "camera mounted in the top-left corner".
- Effect — distinguishing vs enhancing: a feature that only boosts an effect without affecting problem-solving is not essential.

### B2 Write the independent claim → Done when: single paragraph, preamble + characterizing portion

Format:

```
一种<上位主题名称>,包括:<与最接近现有技术共有的必要特征>;其特征在于:<区别于现有技术的特征>。
```

- Preamble: subject name + shared features. The X in "一种<X>" uses a **generic/upper-level term** (see B3), not the product name.
- Characterizing portion: introduced by "其特征在于". If the distinguishing feature is not yet clear, go back to the interview — don't force it.
- Place the independent claim before dependent claims and keep the claim set internally consistent.

### B3 The generalization ladder (上位化) → Done when: every term passed the three questions

Abstract the concrete implementation level by level along "the essence of the problem", ordered narrow → broad:

```
层1 具体实现  手机APP通过蓝牙连接手环,读取心率
层2 中间概括  客户端与可穿戴设备通信,获取生理数据
层3 功能概括  第一终端与第二终端通信,获取用户状态数据
```

**The three-question test** (every level up must pass):
1. Does the generalization **still solve the original technical problem**? → No: step back one level.
2. Is it **supported by an embodiment in the specification**? claims shall be supported by the description → No: either add an embodiment (back to Part A) or step back.
3. Is it a **pure functional limitation**? (only states "what it does", not "how it does it") → Yes: at least one implementation path must be disclosed, otherwise unsupported/unclear.

- The generalization direction is set by the essence of the problem: if the problem is about "interaction between the user and a data service", app→client holds; if it is about "Bluetooth low-energy power saving", app→client fails and that limitation must be kept.
- Use levels 2-3 for the independent claim; all level-1 implementation detail sinks into dependent claims.

### B4 Fallback dependent claims → Done when: every embodiment has a matching fallback

Dependent claims = **fallbacks**: when the over-broad independent claim is rejected, a dependent claim takes over. Defend in three directions, ordered by commercial importance:

| Direction | Technique | Example |
|---|---|---|
| Refinement | Fold implementation detail into a dependent claim | independent "处理单元" → dependent "所述处理单元包括特征提取模块和匹配模块" |
| Variants | One claim per alternative implementation | independent "第一通信方式" → dependent "所述第一通信方式为蓝牙" + "为Wi-Fi" |
| Enhancement | Add functional features | independent solution + dependent "还包括:根据用户反馈更新所述匹配模型" |

Citation mechanics (cite only earlier claims; a multiple dependent claim cites a single alternative and never serves as the basis of another multiple dependent claim; the citation part restates the full subject) are checked formally by `../patent-compliance/SKILL.md` 检查2 — follow them while writing, but do not draft against the rule text.

---

## Part C — Abstract (摘要) → Done when: name + field + problem + solution gist + main uses, no marketing language

State the name, technical field, technical problem, solution gist, and main uses. Keep it short — aim for brevity, not a character count. No commercial marketing language. If there are drawings, designate one in the request as the **abstract figure** (hand off to `../patent-drawings/`).

---

## Boundaries

- Owns the specification (five parts), claims, and abstract only; never interviews, never draws figures, never checks formally — those are `../patent-intake/`, `../patent-drawings/`, `../patent-compliance/` via artifact files.
- Never invents prior art, data, or core formulas; gaps return as `blocked` to intake.
- Honesty red line owns background-art sourcing; this skill normalizes confirmed material only.

## Revision loop (after delivery)

All review comments — the inventor's, the agency's, or complaints about a delivered Word file — land in the owning draft under `drafts/` (`权利要求书.md` / `说明书.md` / `摘要.md`). The delivered `.docx` files under `deliverables/` are regenerable exports produced by `../word-delivery/SKILL.md`; never edit them by hand. After a substantive revision, re-run the affected self-checks (`../patent-compliance/SKILL.md`) and re-export via `../word-delivery/`.

## Completion standard (before handover)

- [ ] Specification reads as coherent technical prose; the inventor can follow their own invention in it; voice wall respected (no claim syntax in narrative paragraphs)
- [ ] Five specification parts complete, headed, and in order; background art zero fabrication
- [ ] Three-way correspondence: problem ↔ background deficiencies, solution ↔ effect ↔ data or mechanism
- [ ] Core-formula gate passed where applicable; every core equation has variable meanings, conditions, and embodiment support
- [ ] Sufficient disclosure: paragraphs missing parameters/steps/flows are completed
- [ ] Independent claim passed the deletion test; generalization passed the three questions
- [ ] Every embodiment/variant has a fallback in the dependent claims
- [ ] Support chain: every claim feature has a source in the specification (in-skill loop closed)
- [ ] Term consistency across claims, specification, abstract, and figures
- [ ] Abstract contains the four elements' gist, no marketing language
- [ ] claims / specification stages updated in drafts/application-info.md
- [ ] No invented prior art, no fabricated data
