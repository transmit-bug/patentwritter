---
name: patent-drafting
description: "Draft and revise the CN patent text documents in Chinese — claims (权利要求书), five-part specification (说明书), abstract; claims first, the support chain owned in one place. Use when the user asks to write or revise claims or the specification; direct entry needs existing drafts or a complete four-element record."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Patent Drafting (claims → specification → abstract)

Role: **discipline** of the self-service group. Input: the four elements (technical problem / technical solution / distinguishing feature / technical effect) + application type (invention / utility model), plus the route record from `../patent-intake/SKILL.md`. If any input is missing, go back to the interview — never write on guesswork. This skill does not interview the inventor; when a fact is missing, return it as a blocker to patent-intake.

Order is fixed: **claims first, then the specification** — the specification is the support structure for the claims. The support chain is owned here in one place; a gap found while writing Part B is fixed by re-entering Part A, not by papering over it.

On completion, update the 权利要求 and 说明书 stages in `草稿/申请信息.md` (✓, or `blocked: <reason>`).

## Type differences (settle the template first)

| Dimension | Invention | Utility model |
|---|---|---|
| Independent-claim subject | Product / method / system | **Product only** (shape / construction / combination) |
| Method features | Algorithm / process allowed | **No method steps as main features**; only known method names as qualifiers |
| Reference numerals | Allowed, in parentheses | Same |
| Typical claim count | 8-15 | 5-10 |

---

## Part A — Writing the claims (权利要求书)

Standards pointer: `../patent-standards/references/cn-invention-utility.md`.

### A1 Pin down the essential features → Done when: every retained feature passes the deletion test

For every feature in the solution ask: **if deleted, is the technical problem still solved?** Yes → non-essential, demote to a dependent claim or drop it. The independent claim keeps only the features without which the problem cannot be solved.

- Essential features come from the **problem**, not from implementation detail: to solve "unreliable recognition", the essential thing is a "recognition mechanism", not "camera mounted in the top-left corner".
- Effect — distinguishing vs enhancing: a feature that only boosts an effect without affecting problem-solving is not essential.

### A2 Write the independent claim → Done when: single paragraph, preamble + characterizing portion, one full stop

Format:

```
一种<上位主题名称>,包括:<与最接近现有技术共有的必要特征>;其特征在于:<区别于现有技术的特征>。
```

- Preamble: subject name + shared features. The X in "一种<X>" uses a **generic/upper-level term** (see A3), not the product name.
- Characterizing portion: introduced by "其特征在于". If the distinguishing feature is not yet clear, go back to the interview — don't force it.
- Place the independent claim before dependent claims and keep the claim set internally consistent.

### A3 The generalization ladder (上位化) → Done when: every term passed the three questions

Abstract the concrete implementation level by level along "the essence of the problem", ordered narrow → broad:

```
层1 具体实现  手机APP通过蓝牙连接手环,读取心率
层2 中间概括  客户端与可穿戴设备通信,获取生理数据
层3 功能概括  第一终端与第二终端通信,获取用户状态数据
```

**The three-question test** (every level up must pass):
1. Does the generalization **still solve the original technical problem**? → No: step back one level.
2. Is it **supported by an embodiment in the specification**? claims shall be supported by the description → No: either add an embodiment or step back.
3. Is it a **pure functional limitation**? (only states "what it does", not "how it does it") → Yes: at least one implementation path must be disclosed, otherwise unsupported/unclear.

- The generalization direction is set by the essence of the problem: if the problem is about "interaction between the user and a data service", app→client holds; if it is about "Bluetooth low-energy power saving", app→client fails and that limitation must be kept.
- Use levels 2-3 for the independent claim; all level-1 implementation detail sinks into dependent claims.

### A4 Fallback dependent claims → Done when: every embodiment has a matching fallback, and the citation rules are respected

Dependent claims = **fallbacks**: when the over-broad independent claim is rejected, a dependent claim takes over. Defend in three directions, ordered by commercial importance:

| Direction | Technique | Example |
|---|---|---|
| Refinement | Fold implementation detail into a dependent claim | independent "处理单元" → dependent "所述处理单元包括特征提取模块和匹配模块" |
| Variants | One claim per alternative implementation | independent "第一通信方式" → dependent "所述第一通信方式为蓝牙" + "为Wi-Fi" |
| Enhancement | Add functional features | independent solution + dependent "还包括:根据用户反馈更新所述匹配模型" |

Citation rules:
- A dependent claim may only cite an **earlier** claim.
- A multiple dependent claim must cite a single alternative: "根据权利要求1或2所述的…".
- A multiple dependent claim **must not** serve as the basis of another multiple dependent claim ("根据权利要求3或4所述的…" violates this if claim 3 is multiple).
- The citation part restates the full subject: "根据权利要求1所述的一种<主题>…".

### A5 Clarity convergence → Done when: every claim passes the table below, zero hits

| Check | Rule |
|---|---|
| Terms consistent with the specification | if the claims write "传感器", the specification must not write "感应器" for the same part |
| Subject name consistent | independent claim, dependent-claim citation parts, and the specification title must agree |
| "所述" has an antecedent | "所述处理器" must be preceded by "处理器" or "一种处理器" |
| No "as shown in the figures" | unless absolutely necessary, no "如图…所示" |
| Reference numerals in parentheses only | numerals go in parentheses, never as limitations |
| No leading phrases | "优选""例如""最好" are drafting words, not claim content |
| No marketing language | keep claim language technical and bounded |
| One claim, one full stop | Practice: each claim ends with a single period |

While writing A2 / A3 / A5, consult `references/claim-language.md` (same directory as this skill): the term conversion table (product words → patent words) and the common-mistakes table (wrong vs right).

---

## Part B — Writing the specification (说明书, five parts) + abstract

Standards pointer: `../patent-standards/references/cn-invention-utility.md`.

Input: the four elements + the claims from Part A.

### B1 Technical field → Done when: one sentence "本发明涉及…技术领域,特别涉及…"

Broad category first, then the narrow one: "The present invention relates to the technical field of <broad>, and in particular to <narrow>". The narrow field must land on the claimed subject matter and echo the independent claim's subject name.

### B2 Background art → Done when: only the three kinds of material, no fabricated references

**Honesty red line** (the hardest rule in this skill): the background art may only contain three kinds of material —

1. **Prior solutions the inventor knows**: describe them truthfully (structure / practice / deficiencies); include a patent number or reference if there is one, and leave numbers out if there isn't. For a paper-source case, the paper's related-work section belongs here (see `../patent-intake/references/source-modes.md`).
2. **Objective common problems**: no specific reference; describe the problem state generally recognized in the field ("现有技术中,<问题>是普遍存在的…").
3. **Results actually returned by a search tool**: cite real publication numbers.

Forbidden: inventing patent numbers, references, company names, or "某公司公开了…". **Test: can the user tell you where this content came from? If not, cut it or rephrase it as a common problem.**

Structure: what the prior solution is → what problem it has (objective, specific) → the consequences of that problem → close with "因此,亟需一种<方案>…" leading into the summary of invention.

### B3 Summary of invention → Done when: problem/solution/effect correspond three ways, and the solution paragraphs cover every claim

For algorithm, control, signal-processing, image-processing, optimization, and scheduling inventions, run the **core-formula gate** before drafting is considered complete. Identify the equations or logic predicates that make the distinguishing feature work (not merely familiar textbook formulas), give every variable its engineering meaning, unit/range where applicable, input/output and boundary conditions, and map each formula to the corresponding process step and technical effect. If a core relation is unknown, pause that part and return a blocker to patent-intake; never invent a technically plausible formula.

Three-way correspondence:
- **Technical problem to be solved**: maps one-to-one to the background-art deficiencies; one sentence, optionally adding "本发明目的在于…".
- **Technical solution**: expand the independent claim into paragraphs (feature-by-feature correspondence), then summarize the dependent claims with "进一步地…可选地…". **Every claim feature must have a source in the solution paragraphs or the embodiments** (support chain).
- **Beneficial effects**: written against the prior art. **If there is data, write the data (state the measurement conditions); if not, write the mechanism reasoning ("由于…,因此…")**. Fabricating experimental data is forbidden; real data from inventor material may be cited with its conditions (数据可用性 flag).

### B4 Brief description of drawings → Done when: one sentence per figure, numerals stay in bounds

"图1为本发明实施例提供的<X>的结构示意图;" — one sentence per figure, listing all figures. Figure numbers correspond one-to-one to the drawings.

### B5 Detailed description → Done when: a person skilled in the art can reproduce from it

The test for **sufficient disclosure**: an ordinary person skilled in the art, after reading it, can make the thing. Missing parameters, missing steps, missing data flows all fail.

Embodiment writing protocol — every embodiment must cover:
1. **Structure / connections**: parts list + connection relationships (written against the reference numerals).
2. **Working flow**: the complete process from input to output, with the key steps stated.
3. **Key parameters**: values / thresholds / counts / dimensions, as ranges or concrete values.
4. **Data flow**: how data/signals move between modules, who triggers whom.
5. **Core formulas and logic**: display the formula in editable math form in the Markdown source, define all symbols immediately after it, state threshold/initialization/boundary handling, and explain how the result changes the physical or system operation. A flowchart alone does not replace the formula when the formula is the inventive mechanism.

Support-chain requirements:
- Every generic concept in the claims lands in at least one concrete embodiment (support-chain check).
- Every additional feature of a dependent claim is matched in the embodiments.
- At least 2-3 embodiments, and they must be **genuine variants** (real differences in deployment location / data flow / triggering), not the same paragraph re-templated with substitutions. If you cannot produce a genuine variant, one solid embodiment beats three watered-down ones.
- **In-skill loop**: if a claim feature has no landing point here, go back to Part A (narrow the generalization, demote the feature, or add a dependent claim) — do not leave the gap to be found by compliance.

Utility model notes:
- Structure / connection / fitting at the core, written against the drawings.
- State shape, construction, and positional relationships (above/below/connected/fitted) — these are the utility model's protection focus.

### B6 Abstract → Done when: name + field + problem + solution gist + main uses, no marketing language

State the name, technical field, technical problem, solution gist, and main uses. **Keep it short** (practice: ~300 characters; the 2023 Implementing Regulations removed the 300-character statutory cap — aim for brevity, not character count). No commercial marketing language. If there are drawings, designate one in the request as the **abstract figure** (hand off to `../patent-drawings/`).

---

## Completion standard (before handover)

- [ ] Independent claim passed the deletion test; not a pile of implementation detail
- [ ] Three questions all passed: generalization keeps the problem, specification supports it, no pure functional limitation
- [ ] Every embodiment/variant has a fallback in the dependent claims
- [ ] A5 checklist: zero hits
- [ ] Five specification parts complete, headed, and in order; background art zero fabrication
- [ ] Three-way correspondence: problem ↔ background deficiencies, solution ↔ claims, effect ↔ data or mechanism
- [ ] Support chain: every claim feature has a source in the specification (in-skill loop closed)
- [ ] Sufficient disclosure: paragraphs missing parameters/steps/flows are completed
- [ ] Abstract contains the four elements' gist, no marketing language
- [ ] For formula-bearing technical fields: core-formula gate passed; every core equation has variable meanings, conditions, embodiment support, and a Word-editable OMML delivery path
- [ ] 权利要求 / 说明书 stages updated in `草稿/申请信息.md`
- [ ] No invented prior art, no fabricated data
