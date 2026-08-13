---
name: patent-specification
description: Write the five-part specification (说明书) and abstract for CN invention patents and utility models, in Chinese. Technical field / background art (honesty protocol) / summary of invention (problem-solution-effect three-way correspondence) / brief description of drawings / detailed description (sufficient disclosure + support chain), plus the abstract and abstract figure. Use when the user asks to "write the specification", "how do I write the background art", "detailed description", "abstract"; also invoked by the patent-application entry skill.
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Writing the Specification (说明书, five parts)

Input: the four elements + the claims (write the claims first, then the specification — the specification is the support structure for the claims). The five-part structure is a statutory requirement (细则第20条); each part has a heading.

## Part 1 Technical field → Done when: one sentence "本发明涉及…技术领域,特别涉及…"

Broad category first, then the narrow one: "The present invention relates to the technical field of <broad>, and in particular to <narrow>". The narrow field must land on the claimed subject matter and echo the independent claim's subject name.

## Part 2 Background art → Done when: only the three kinds of material, no fabricated references

**Honesty red line** (the hardest rule in this skill): the background art may only contain three kinds of material —

1. **Prior solutions the inventor knows**: describe them truthfully (structure / practice / deficiencies); include a patent number or reference if there is one, and leave numbers out if there isn't.
2. **Objective common problems**: no specific reference; describe the problem state generally recognized in the field ("现有技术中,<问题>是普遍存在的…").
3. **Results actually returned by a search tool**: cite real publication numbers.

Forbidden: inventing patent numbers, references, company names, or "某公司公开了…". **Test: can the user tell you where this content came from? If not, cut it or rephrase as a common problem.**

Structure: what the prior solution is → what problem it has (objective, specific) → the consequences of that problem → close with "因此,亟需一种<方案>…" leading into the summary of invention.

## Part 3 Summary of invention → Done when: problem/solution/effect correspond three ways, and the solution paragraphs cover every claim

Three-way correspondence (细则第20条: state it against the prior art):
- **Technical problem to be solved**: maps one-to-one to the background-art deficiencies; one sentence, optionally adding "本发明目的在于…".
- **Technical solution**: expand the independent claim into paragraphs (feature-by-feature correspondence), then summarize the dependent claims with "进一步地…可选地…". **Every claim feature must have a source in the solution paragraphs or the embodiments** (support chain, 专利法第26条第4款).
- **Beneficial effects**: written against the prior art. **If there is data, write the data (state the measurement conditions); if not, write the mechanism reasoning ("由于…,因此…")**. Fabricating experimental data is forbidden.

## Part 4 Brief description of drawings → Done when: one sentence per figure, numerals stay in bounds

"图1为本发明实施例提供的<X>的结构示意图;" — one sentence per figure, listing all figures. Figure numbers correspond one-to-one to the drawings (细则第21条).

## Part 5 Detailed description → Done when: a person skilled in the art can reproduce from it

The test for **sufficient disclosure** (专利法第26条第3款): an ordinary person skilled in the art, after reading it, can make the thing. Missing parameters, missing steps, missing data flows all fail.

Embodiment writing protocol — every embodiment must cover:
1. **Structure / connections**: parts list + connection relationships (written against the reference numerals).
2. **Working flow**: the complete process from input to output, with the key steps stated.
3. **Key parameters**: values / thresholds / counts / dimensions, as ranges or concrete values.
4. **Data flow**: how data/signals move between modules, who triggers whom.

Support-chain requirements:
- Every generic concept in the claims lands in at least one concrete embodiment (指南 第二部分第二章).
- Every additional feature of a dependent claim is matched in the embodiments.
- At least 2-3 embodiments, and they must be **genuine variants** (real differences in deployment location / data flow / triggering), not the same paragraph re-templated with substitutions. If you cannot produce a genuine variant, one solid embodiment beats three watered-down ones.

Utility model notes:
- Structure / connection / fitting at the core, written against the drawings.
- State shape, construction, and positional relationships (above/below/connected/fitted) — these are the utility model's protection focus.

## Abstract → Done when: name + field + problem + solution gist + main uses, no marketing language

细则第26条: state the name, the technical field, reflect the technical problem to be solved, the gist of the technical solution, and the main uses. **Keep it short** (practice: ~300 characters; the 2023 Implementing Regulations removed the 300-character statutory cap — aim for brevity, not character count). No commercial marketing language. If there are drawings, designate one in the request as the **abstract figure** (hand off to patent-drawings).

## Completion standard (before handover)

- [ ] Five parts complete, headed, in order (细则第20条)
- [ ] Background art zero fabrication; only the three kinds of material
- [ ] Three-way correspondence: problem ↔ background deficiencies, solution ↔ claims, effect ↔ data or mechanism
- [ ] Support chain: every claim feature has a source in the specification
- [ ] Sufficient disclosure: paragraphs missing parameters/steps/flows are completed
- [ ] Abstract contains the four elements' gist, no marketing language
