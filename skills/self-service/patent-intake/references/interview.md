# Disclosure Interview Question Bank (交底访谈问题库)

The interview optimizes **content, not legal form**: what makes or breaks the later application is a complete, implementable, honestly-sourced description of the invention — formal defects are repairable downstream, missing content is not. The seven content principles this bank serves: state the prior art and its concrete deficiencies; keep problem → solution → effect complete; write to reproducible depth (no hidden parameters); keep the inventor's own words; one term per thing; source the background art; declare technical-reservation points explicitly. Answers stay verbatim in the inventor's engineering register — the **voice wall (语体边界)** defined in `../../patent-drafting/SKILL.md` owns that boundary; statutory claim language is applied downstream by patent-drafting / patent-compliance.

Grouped by the four elements. Ask the groups in order; skip a question when the inventor's answer already covers it. At most 4 questions per AskUserQuestion. Record the answers into drafts/申请信息.md.

## A. Technical problem (what is being solved)

1. What does this thing do? In what scenario is it used? (→ technical field)
2. Without it, what trouble would the user/system run into? (→ technical problem — must be a **technical** trouble, not a business / marketing one)
3. How widespread is this trouble? Who hurts most? (→ problem importance, for the background art)
4. Has anyone tried to solve it before? How, and why didn't it work? (→ distinguishing-feature material + background-art material)

## B. Technical solution (how it is solved)

5. What is the minimal set of parts/steps your solution needs? List them in order. (→ essential-technical-feature candidates)
6. What does each step / part do? (→ functional role of each feature)
7. Is there any step that "works without it"? (→ reverse-pin the essential features: can the problem still be solved if it is deleted)
8. What are the key parameters? (values / thresholds / counts / dimensions — → dependent-claim material and sufficient disclosure)
9. How does data / signal flow? Who sends to whom? (→ connection relationships, for the drawings and embodiments)

## C. Core formula and implementation gate (formula-bearing cases only)

Ask this group for algorithm, control, signal-processing, image-processing, optimization, and scheduling inventions. Write answers only from inventor-confirmed material; when uncertain, mark the gap as blocked and ask the inventor to clarify.

19. What exact quantity is calculated or judged at the inventive step? Write the equation or logic predicate in your own notation. (→ core formula)
20. What does every symbol mean, what are its units/range, and what are the input/output signals? (→ variable semantics and physical meaning)
21. How are initialization, thresholds, empty sets, ties, saturation, and boundary cases handled? (→ implementability and edge conditions)
22. Where did the relation come from: your derivation, an experiment, a known formula, or a design choice? What alternative relation also works? (→ derivation/provenance and fallback)

Completion gate: the core formula/logic is written, all variables are defined, boundary handling is known, and at least one embodiment and claim feature are linked to it. If any item is missing, record a blocker in drafts/申请信息.md and pause only the affected core feature.

## D. Distinguishing feature (what differs from existing practice)

10. How is this step usually done on the market / in existing products? (→ closest prior art)
11. Compared with that, what did you add? Which step did you change? (→ distinguishing feature, the core of the claims)
12. Is this difference "never done by anyone", or "done but not done well"? (→ inventive-step argument material)
13. Have you thought of other approaches achieving the same effect? (→ variants, fallback-deployment material)

## E. Technical effect (how it is proven)

14. What's the benefit of doing it this way? (→ beneficial effects)
15. How do you prove these benefits? Is there test / comparison data? What are the numbers? (→ data if available; otherwise mechanism reasoning only)
16. Any side effects / costs? (→ honestly state the weaknesses, to avoid being caught in examination)

## F. Disclosure and risk (triggers the grace-period reminder)

17. Has this been disclosed before — published, exhibited, sold, open-sourced, posted, or shown to a third party?
18. Could anyone else know the solution through colleagues, partners, outsourcing, or an unauthorized disclosure?

When either answer is yes, record the date, channel, audience, evidence, and whether the inventor claims a statutory exception. Point to `../../patent-standards/references/cn-invention-utility.md` for the current disclosure/grace-period treatment; do not paste legal explanations into the interview record.

## Closing check (are the four elements complete)

| Element | Test | What happens if missing |
|---|---|---|
| Technical problem | can state in one sentence "what is solved" | cannot write the summary of invention; the independent claim has no anchor |
| Technical solution | can name the minimal part/step set | claims become hollow, only fillable by fabrication |
| Distinguishing feature | can say "what was added / changed vs existing practice" | the characterizing portion has nothing to write |
| Technical effect | has data or mechanism basis | the effect paragraphs can only be padded |
