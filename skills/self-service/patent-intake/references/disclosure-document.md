# 技术交底书 Assembly — brief-tight 交底

A 技术交底书 is the **brief-tight** consolidated disclosure handed to an agency for drafting or internal review. Leading word **brief-tight** = 紧凑态：让代理人据此独立起草申请文件。One 交底书 = one file `草稿/技术交底书.md`；三件套 filing docs stay separate `成品/申请文件/`。

Assembled at Stage-5 by `patent-intake`: merge tracked sources into `草稿/技术交底书.md`. The `.md` is the truth; docx export is a separate user-invoked step via `../../word-delivery/SKILL.md`.

## Leading word

**brief-tight** recruits the prior "tight loop" — small, checkable. Every run the agent reaches for the same budget: **1–3 core formulas, 2–3 figures, template six rows**. Repeated as token `brief-tight` in pointers and checks.

## Rule tracks — one trigger per branch

| Track | When to load this file | Rule set |
|---|---|---|
| **brief-tight track** | deliverable = 交底书 / 两者（any run that must produce `技术交底书.md`） | This file alone — the complete disclosed reference |
| filing track | deliverable = 申请文件套件 | `../../patent-drafting/SKILL.md` (spec-first + voice wall + full sufficient-disclosure gate) |

Patent law is handled downstream in filing track. On brief-tight track, this file is the authority; keep filing gates in `patent-drafting` there.

## Steps — what the agent does, in order

Each step ends on a checkable completion criterion.

### 1 Verify source → Done when: source map is closed
Confirm `草稿/申请信息.md` four elements + `.patent/materials/` provenance. When an element is marked `blocked`, pause that part and ask the inventor for the missing piece; proceed only with confirmed material.

### 2 Map template → Done when: one template slot per交底章节
Bind `examples/技术交底书模板.doc` slots to the six rows below. List any template slot without source and any source without slot as `待补图/待补式` for the inventor to confirm.

### 3 Assemble sections → Done when: every paragraph traces to `申请信息.md` or confirmed material and paper chapter structure is absent
Copy verbatim per the table. Write clean prose as the default. Append a single `[S#]` at sentence end only where the sentence directly quotes paper data, a table value, or a figure; otherwise rely on traceability via `申请信息.md` + `.patent/sources`. Budget: whole document ≤5 `[S#]` tags total.

### 4 Embed brief-tight figures → Done when: 2–3 figures embedded as `../附图/嵌入/figN.png` with caption `图N …`, files present in both `附图/嵌入/` and `附图/源文件/` (route via `../../patent-drawings/SKILL.md`)
When inventor material supplies an architecture or flow original, integrate it as-is to both directories. When no supply exists, create a brief dot-flow with ≤8 nodes, LR direction, 4:3–16:9 tight canvas that traces the inventive step.

### 5 Tight formula check → Done when: 1–3 core formulas each show variable map and boundary handling on the same page, and body reads as engineering prose
Tight gate is a budgeted pointer to `../../patent-drafting/SKILL.md` A3: retain only the relation that makes the distinguishing feature work, show meaning/units/in-out/boundary alongside it, and present non-core derivations as a single `[S#]` citation. Keep body in engineering register with ordinary prose and sentence-end citations only.

## Reference — assembly table (flat peer-set, template-aligned)

Six rows only — every row is a disclosure need.

| 交底章节 | 来源 | 写法 |
|---|---|---|
| 基本信息 + 模板适配 | `申请信息.md` | 照抄；模板占位文字保留在来源，不复制进正文 |
| 一、技术领域 | 四要素定位 | 写成一句话技术领域陈述 |
| 二、背景技术 | 发明人已知现有方案 / 客观通用问题 / 检索真实返回 | 保留发明人原话，只写可溯源的内容；仅对直接引用的对比数据或文献结论加一句尾 `[S#]` |
| 三、要解决的技术问题 | `申请信息.md` 四要素·技术问题 | 照抄 |
| 四、技术方案（含 brief-tight 图式） | 四要素·技术方案 + 确认的实施例（≤2个真实变体）+ 2–3图 + 1–3式 | 图文式 co-located：文字讲流程，图显结构/流向，式给判据；每式紧跟变量表与边界处理 |
| 五、技术效果 / 六、区别特征 / 七、替代方案 | `申请信息.md` 对应四要素 | 数据写明条件，机理写清因果 |
| 八、附图说明 + 附录 S | `附图/嵌入/` 实际内嵌图 + `.patent/sources|queries/` | 一图一句话编号；附录 S 为唯一附录，≤5 条可省略，未引用则留空 |

**Co-location rule**: Keep a concept's definition, its figure, and its formula under one heading (`§四`). Reading `§四` brings all three together.

**Single source of truth**: Four elements live once in `申请信息.md`; copy from there. Keep claims and abstract in their filing files `权利要求书.md`/`摘要.md` on filing track; write disclosure as four elements + figures + formulas within the six rows above, with rights drafting produced on filing track via `patent-drafting B`.

## Completion — brief-tight bar (both checkable and exhaustive)

- [ ] 2–3 figures embedded, each with caption and paired files `附图/嵌入/*.png` + `附图/源文件/*`
- [ ] 1–3 core formulas, each with variable map + I/O + boundary, tight gate satisfied; remaining formulas consolidated to `[S#]`
- [ ] §四 stays free of paper deep tower and full parameter tables; whole document traces to 申请信息 or `[S#]`
- [ ] Engineering register: ordinary prose, single stable file `技术交底书.md`
- [ ] 附录 S ≤5 条，按需可省略；全文 ` [S#]` ≤5 处且仅在直接引用句尾
