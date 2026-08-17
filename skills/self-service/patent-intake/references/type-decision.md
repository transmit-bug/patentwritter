# Application Type Decision

Standards pointer: `../../patent-standards/references/cn-invention-utility.md` and `../../patent-standards/references/cn-design.md`.

Use this decision tree to choose the drafting branch. The pointer above is the standards source; do not copy its legal text into the interview record or the patent document.

## Decision tree

```text
Is the subject mainly a method, algorithm, process, formula, or control flow?
├─ Yes → invention
└─ No → is the improvement primarily the product's appearance?
    ├─ Yes → design
    └─ No → is it a product structure, construction, connection, or layout?
        ├─ Yes → ask whether the method also needs protection
        │   ├─ Yes → consider dual filing
        │   └─ No → choose invention or utility model after discussing scope and route
        └─ No → clarify the technical subject before drafting
```

## Clarification prompts

- **Invention**: use when the valuable contribution is a method, algorithm, process, material relation, control logic, or a broad product/system solution.
- **Utility model**: use when the valuable contribution is a product's physical shape, construction, connection, or combination. Keep the claims and disclosure on the product structure.
- **Design**: use when the protected contribution is the product's visual appearance. Use the design-point interview and supplied views; do not run the technical four-element interview.
- **Dual filing**: consider when the same product has a structural protection route and a separate method or broader technical route. Record this as a deliberate choice, not as an automatic default.

If the inventor cannot distinguish appearance from function, ask what a competitor would copy: the look, the construction, the method, or more than one of these. If the answer remains mixed, record the alternatives and route the unresolved part back to the inventor.

## Output record

Write only the decision and its plain-language explanation into `草稿/申请信息.md`:

```text
申请类型: 发明 / 实用新型 / 外观设计 / 一案两请 / 待确认
判断说明: …
判断依据索引: ../../patent-standards/references/cn-invention-utility.md 或 ../../patent-standards/references/cn-design.md
待确认事项: …
```
