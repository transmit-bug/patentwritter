# Discussion Protocol — Socratic 研讨

Purpose: turn vague ideas into sharp triples through **guided dialogue**, not monologue. This is the interactive core of `patent-exploration`.

## Principles

1. **One question at a time.** Use `AskUserQuestion` with 2–4 options + free text. Never ask three questions in one turn.
2. **Challenge, don't lead.** Offer counter-examples, alternative framings, and "what if you removed X?" probes. The goal is to make the inventor think, not to make the agent sound smart.
3. **Summarize each round.** End every exchange with one sentence: "本轮确认：..." so progress is visible.
4. **Time-box.** Default 3–5 rounds; ask "是否继续深挖，还是先定方向？" when reaching 5.
5. **Stay technical.** Do not drift into claim drafting, filing strategy, or legal advice — those are downstream.

## Question bank (pick, don't dump)

Use when the relevant triple/point is unclear:

**A. 锚定问题 (problem anchoring)**
- 这个技术不做会怎样？最痛的场景是什么？
- 传统做法在哪一步卡住？是做不到、做不好、还是做得贵？

**B. 手段追问 (means probing)**
- 如果把 <关键步骤> 拿掉，效果还在吗？
- 这个参数范围是怎么定的？边界外会怎样？
- 有没有更笨但也能work的替代做法？

**C. 效果验证 (effect probing)**
- 这个效果是怎么测出来的？对照组是什么？
- 换一批数据/换一个环境，还成立吗？
- 失效模式是什么？什么时候不灵？

**D. 区分度 (distinctiveness)**
- 和 <现有做法/论文相关工作/竞品> 比，本质区别是一句话能说清吗？
- 如果竞争对手想绕开，最容易改哪一块？

**E. 产品锚定 (product anchoring)**
- 这个技术最终落在什么产品/方法/系统上？谁用？怎么用？
- 如果只保护一个点，你最不想被抄的是哪一个？

## Socratic moves (when the user is stuck)

- **反例**: "如果有人用固定阈值+更大队列，也能达到类似效果，那我们的本质区别还成立吗？"
- **归谬**: "如果把这个思想推到极端（全自适应/全固定），会怎样？"
- **类比**: "这和 <另一领域的类似技术> 的思路像吗？区别在哪？"
- **拆解**: "这个手段里，哪一步是必须的，哪一步只是实现细节？"

## Logging — 研讨纪要.md

After each round, append to `.patent/exploration/研讨纪要.md`:

```markdown
## Round N — <topic>
- 问: <question>
- 答: <user answer summary>
- 确认: <one-sentence agreement>
- 待定: <open items, if any>
```

The log is the audit trail for the handover package.

## Exit conditions

Exit the loop when any of:

- The user says "可以了/先到这里/进入下一步"
- All `待研讨` triples have been tagged `潜在专利点` or `论文亮点`
- The mining matrix has at least one agreed `核心` point

On exit, write a short `本轮研讨结论` (3–5 bullets) at the top of `研讨纪要.md` and proceed to `handover.md`.

## Anti-patterns

- Do not turn the discussion into a lecture ("我来给你讲讲专利法...").
- Do not ask "还有什么要补充的吗？" as a lazy close — always propose a concrete next question or a direction choice.
- Do not fabricate prior art to challenge the user — if you need a comparison, mark it `待查新` and offer to run `patents-search`.
