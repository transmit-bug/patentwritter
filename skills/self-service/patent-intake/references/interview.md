# Disclosure Interview Question Bank (交底访谈问题库)

The interview optimizes **content, not legal form**: what makes or breaks the later application is a complete, implementable, honestly-sourced description of the invention — formal defects are repairable downstream, missing content is not. The seven content principles this bank serves: state the prior art and its concrete deficiencies; keep problem → solution → effect complete; write to reproducible depth (no hidden parameters); keep the inventor's own words; one term per thing; source the background art; declare technical-reservation points explicitly. Answers stay verbatim in the inventor's engineering register — the **voice wall (语体边界)** defined in `../../patent-drafting/SKILL.md` owns that boundary; statutory claim language is applied downstream by patent-drafting / patent-compliance.

Grouped by the four elements. Ask the groups in order; skip a question when the inventor's answer already covers it. At most 4 questions per AskUserQuestion. Record the answers into drafts/application-info.md.

## A. Technical problem (what is being solved)

1. What does this thing do? In what scenario is it used? (→ technical field)
2. Without it, what trouble would the user/system run into? (→ technical problem — must be a **technical** trouble, not a business / marketing one)
3. How widespread is this trouble? Who hurts most? (→ problem importance, for the background art)
4. Has anyone tried to solve it before? How, and why didn't it work? (→ distinguishing-feature material + background-art material)

## B. 技术方案访谈（实施级规范描述，推荐8要点完整）

本组为 §四的单文件可复现做准备，推荐按 `8-points.md` 8要点提问，未覆盖项按分型在 `申请信息.md` 注明豁免理由，不编造。覆盖：①总体 ②设计构思 ③分步实施描述（输入/处理/输出与流向） ④可自编程度 ⑤必要源码摘录 ⑥物理变量释义 ⑦推导 ⑧硬件与实施例。

5. 总体：系统的总体架构是什么？输入输出边界与整体数据/信号流向如何？（→ ①总体）
6. 设计构思：核心发明构思与技术原理是什么？为什么这样设计能解决技术问题？（→ ②设计构思）
7. 分步实施描述：按技术逻辑分步说明——每步的输入是什么、处理逻辑是什么、输出给谁/用于哪一步？用规范技术语言描述，不用 `S1→Sn / M1→Mn` 符号堆砌，3-8步，标题自描述如 `分步实施描述（6步）`。（→ ③分步实施描述）
8. 可自编程度：该方案的可自编/可复现程度如何？哪些环节可完全自编，哪些依赖外部库/平台？工程化落地需要哪些适配？（→ ④可自编程度）
9. 必要源码摘录：关键算法/流程的核心伪代码或源码片段是什么？（可贴10-30行，标注语言与关键行含义）（→ ⑤必要源码摘录）
10. 物理变量释义：涉及的所有物理量/符号/变量的含义、量纲、取值范围与边界条件分别是什么？（→ ⑥物理变量释义）
11. 推导：核心公式的来源与推导过程是什么？有无等价变形或替代形式？（→ ⑦推导）
12. 硬件：硬件组成、部署形态与软硬件分工如何？系统部署在何种硬件/环境上？（→ ⑧硬件）
13. 实施例：能否给出一个完整实施例（参数取值+执行轨迹+输出结果）以验证可复现性？（→ 实施例收束）
14. 数据/信号流补充：各模块间数据/信号如何流转？谁发给谁？（→ 连接关系与附图依据，补 ③⑧）
15. 关键参数：关键阈值/数量/维度/超参如何选取？有何依据？（→ 支撑链与充分公开，补 ④⑥）

> 完成判定：8要点逐项均有发明人确认材料或已按分型豁免说明（机械/结构类无公式可记 `N/A — 无公式承载`；算法/控制/信号/优化/调度类⑤⑥⑦推荐具备，至少1式+1伪代码+变量表与边界），缺项在 `drafts/申请信息.md` 记 blocked，不进正文。
> 语体：不追问 `SLR/VOSviewer` 论文黑话，改问“该步骤的输入/处理/输出与流向是什么”；算法类追问“该步骤计算什么量、公式如何定义、变量含义与边界是什么”，规范描述与公式互指，不以描述替代定义；专业度由可复现深度体现，不在对话中强调语体标签。
>
> **交底书100分审美尺（防过简/防论文化双向）**：1可读性25（电梯2句+术语括号注解）/2完整性30（每步输入-处理-输出+异常分支）/3可实施性20（公式+变量表+伪代码+阈值范围）/4创新凸显15（对比表）/5结构合规10（背景2-4句三类素材）。算法类“公式≥1且变量表完整”未达标则可实施性扣15分，总分<60建议返工，60分以上可进入撰写但建议补齐推荐项。

## C. Core formula and implementation gate (formula-bearing cases only)

Ask this group for algorithm, control, signal-processing, image-processing, optimization, and scheduling inventions. Write answers only from inventor-confirmed material; when uncertain, mark the gap as blocked and ask the inventor to clarify.

19. What exact quantity is calculated or judged at the inventive step? Write the equation or logic predicate in your own notation. (→ core formula)
20. What does every symbol mean, what are its units/range, and what are the input/output signals? (→ variable semantics and physical meaning)
21. How are initialization, thresholds, empty sets, ties, saturation, and boundary cases handled? (→ implementability and edge conditions)
22. Where did the relation come from: your derivation, an experiment, a known formula, or a design choice? What alternative relation also works? (→ derivation/provenance and fallback)

Completion gate: the core formula/logic is written, all variables are defined, boundary handling is known, and at least one embodiment and claim feature are linked to it. If any item is missing, record a blocker in drafts/application-info.md and pause only the affected core feature.

> 注：C组与B组8要点中的⑥⑦互补，B组覆盖全量框架，C组对公式承载型做变量/边界/推导细化。算法类发明的交底书推荐过C组简化门（至少1个可计算公式+变量表+边界），机械类可豁免并注明理由。

## D. Distinguishing feature (what differs from existing practice)

16. How is this step usually done on the market / in existing products? (→ closest prior art)
17. Compared with that, what did you add? Which step did you change? (→ distinguishing feature, the core of the claims)
18. Is this difference "never done by anyone", or "done but not done well"? (→ inventive-step argument material)
19. Have you thought of other approaches achieving the same effect? (→ variants, fallback-deployment material)

## E. Technical effect (how it is proven)

20. What's the benefit of doing it this way? (→ beneficial effects)
21. How do you prove these benefits? Is there test / comparison data? What are the numbers? (→ data if available; otherwise mechanism reasoning only)
22. Any side effects / costs? (→ honestly state the weaknesses, to avoid being caught in examination)

## F. Disclosure and risk (triggers the grace-period reminder)

23. Has this been disclosed before — published, exhibited, sold, open-sourced, posted, or shown to a third party?
24. Could anyone else know the solution through colleagues, partners, outsourcing, or an unauthorized disclosure?

When either answer is yes, record the date, channel, audience, evidence, and whether the inventor claims a statutory exception. Point to `../../patent-standards/references/cn-invention-utility.md` for the current disclosure/grace-period treatment; do not paste legal explanations into the interview record.

## Closing check（四要素是否齐备）

| 要素 | 检验 | 缺失会怎样 |
|---|---|---|
| 技术问题 | 能一句话说清“解决了什么”，并有2-4句背景 | 发明内容无锚点，独权无从写起 |
| 技术方案 | 能说清最小可实施的部件或步骤集合，推荐按8要点完整呈现（未覆盖项已豁免说明） | 权利要求空洞，只能靠编造填补 |
| 区别特征 | 能说清“相对现有做法改了哪一步、加了什么” | 特征部分无内容可写 |
| 技术效果 | 有数据或机理依据，2-4句说清 | 效果段落只能空话填充 |

> 要求：技术方案在正文写全，推荐按8要点完整呈现（未覆盖项已豁免说明）；变量、推导、源码、硬件与实施例不外链到申请信息。
