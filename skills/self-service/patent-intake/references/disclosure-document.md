# 技术交底书 Assembly — 单篇闭合 饱满披露

A 技术交底书 is the **单篇闭合** consolidated disclosure handed to an agency for drafting or internal review. Leading word **单篇闭合** = 饱满态：单篇内可复现、无需外链补材料。以 8 要点为展开基准，不设字数/图/式上限。One 交底书 = one file `drafts/技术交底书.md`；三件套 filing docs stay separate `deliverables/application/`。

Assembled at Stage-5 by `patent-intake`: merge tracked sources into `drafts/技术交底书.md`. The `.md` is the truth; docx export is a separate user-invoked step via `../../word-delivery/SKILL.md`.

## Leading word

**单篇闭合** recruits the prior saturated loop — full, checkable, reproducible in one file. Every run the agent reaches for the same budget: **8 要点饱满展开，不设上限（图 ≥2、式 ≥2，上不封顶）**。Repeated as token `单篇闭合` in pointers and checks.

8 要点定义（按序展开于 §四）：
1. **总体** — 系统/方法总体架构与输入输出边界
2. **设计构思** — 核心发明构思与技术原理
3. **按时序分步** — 按时间/数据流顺序的分步物理过程（S1→Sn）
4. **可自编程度** — 可自编/可复现程度与工程化落地说明
5. **必要源码摘录** — 关键算法/流程的必要源码或伪代码摘录
6. **物理变量释义** — 全部物理量、符号、量纲、取值范围与边界
7. **推导** — 核心公式的来源、推导与等价变形
8. **硬件** — 硬件组成、部署形态与软硬件分工；末尾以实施例收束

## Rule tracks — one trigger per branch

| Track | When to load this file | Rule set |
|---|---|---|
| **单篇闭合 track** | deliverable = 交底书 / 两者（any run that must produce `技术交底书.md`） | This file alone — the complete disclosed reference |
| filing track | deliverable = 申请文件套件 | `../../patent-drafting/SKILL.md` (spec-first + voice wall + full sufficient-disclosure gate) |

Patent law is handled downstream in filing track. On 单篇闭合 track, this file is the authority; keep filing gates in `patent-drafting` there.

## 零过程元段落（hard ban）

正文严禁出现以下过程元内容（出现即 fail）：
- 开头 `> ` blockquote 引导段落
- `基本信息表` / `待补清单` / `Completion` / `Co-location` / `预算` / `法律指向解释`
- 文末 `*本交底书为…*` 定性句
- `见申请信息.md` / `详见申请信息` 等外链式引用（单篇必须自包含）

剩余待确认（Blockers）仅记 `drafts/申请信息.md`，不进正文。

## 自包含与单篇闭合纪律

- 所有变量含义、推导、边界条件、实施例、源码摘录在正文写全，不以“见申请信息.md”外链
- 附图与公式与文字 **co-located 于 §四**：读 §四即得定义+图+式
- 变量表与边界处理与对应公式同页呈现
- 背景技术只写三类可溯源素材（发明人已知方案/客观通用问题/检索真实返回），不编造

## Steps — what the agent does, in order

Each step ends on a checkable completion criterion.

### 1 Verify source → Done when: source map is closed
Confirm `drafts/申请信息.md` four elements + `.patent/materials/` provenance + `.patent/sources/` + 检索报告溯源。When an element is marked `blocked`, pause that part and ask the inventor for the missing piece; proceed only with confirmed material. 但正文不出现 blocker 清单。

### 2 Map template → Done when: one template slot per交底章节
Bind `examples/技术交底书模板.doc` slots to the eight rows below. 模板占位文字保留在来源，不复制进正文。

### 3 Assemble sections → Done when: every paragraph traces to `申请信息.md` or confirmed material and paper chapter structure is absent
Write clean prose as the default. 按 8 要点在 §四饱满展开；一、二、三各自 2-4 句以上饱满陈述，不以一句话应付。全文工程化 prose，无论文章节复刻。

### 4 Embed saturated figures → Done when: ≥2 figures embedded as `figures/embed/figN.png` with caption `图N …`, files present in both `figures/embed/` and `figures/source/` (route via `../../patent-drawings/SKILL.md`)
图按需展开，上不封顶（建议 2-6 图）。When inventor material supplies an architecture or flow original, integrate it as-is to both directories. When no supply exists, create dot-flow with LR direction, tight canvas that traces the inventive step；可按 8 要点分图（总体架构图、分步时序图、硬件部署图等）。

### 5 Saturated formula check → Done when: ≥2 core formulas each show variable map and boundary handling on the same page, and body reads as engineering prose
按 8 要点中的 ⑥⑦ 要求：每式紧跟变量表（含义/单位/输入输出/取值范围）与边界处理；推导写清来源与等价变形；必要源码摘录与式同页或紧邻。图/式/表 co-located 于 §四。

## 发明名称规范 — Title rule (单一来源，跨项目复用)

**必选形态**：`一种<基于/面向><核心手段>的<对象+效果>方法`。如需同时保护系统，可写作 `一种…方法及系统`，但递交时 `patent-drafting B2` 会拆为方法独权 + 系统从权，标题主语以方法为准。

| 规则 | 要求 | 反例 → 正例 |
|---|---|---|
| 前缀 | 必须以 `一种` 起首 | `基于XXX的方法` → `一种基于XXX的方法` |
| 介词 | 用 `的`，不用文言 `之` | `一种XXX之方法` → `一种XXX的方法` |
| 手段 | 保留1个最核心手段，英文缩写不上标题 | `VAE混合检测方法` → `一种面向环境变异的桥梁早期损伤检测方法`（VAE下沉从权） |
| 长度 | 15–30字为佳，最长不超过35字 | 超长标题拆手段到从权 |
| 主题一致 | 与 `申请信息.md` 的 `target-product` 逐字一致 | — |

**层级**：文档包裹 `技术交底书 — <发明名称>` 与发明名称本体 `<一种…方法>` 分离。`drafts/技术交底书.md` 的 `#` 标题即发明名称；副标题另起一行写 `技术交底书（单篇闭合）·供代理机构据此独立起草申请文件`。

## Reference — assembly table (8 要点饱满展开)

| 交底章节 | 来源 | 写法 |
|---|---|---|
| 基本信息 + 模板适配 | `申请信息.md` | 照抄；`target-product`/发明名称须符合 Title rule，模板占位文字保留在来源，不复制进正文；**不出现基本信息表** |
| 一、技术领域 | 四要素定位 | 2-4 句饱满陈述技术领域与应用场景 |
| 二、背景技术 | 发明人已知现有方案 / 客观通用问题 / 检索真实返回 | 2-4 句饱满陈述，只写可溯源的内容；保留发明人原话 |
| 三、要解决的技术问题 | `申请信息.md` four-elements · technical-problem | 2-4 句饱满陈述，照抄并饱满展开 |
| 四、技术方案（8要点饱满展开） | 四要素·技术方案 + 实施例 + ≥2图 + ≥2式 | 按 8 要点展开：①总体→②设计构思→③按时序分步物理过程→④可自编程度→⑤必要源码摘录→⑥物理变量释义→⑦推导→⑧硬件→实施例；图文式 co-located，每式紧跟变量表与边界处理，源码与式同页 |
| 五、技术效果 | `申请信息.md` technical-effect | 数据写明条件，机理写清因果，饱满展开 |
| 六、区别特征 | `申请信息.md` distinguishing-feature | 饱满展开区别点 |
| 七、替代方案 | `申请信息.md` variants | 饱满展开等效替代 |
| 八、附图说明 + 附录 S | `figures/embed/` 实际内嵌图 + `.patent/sources|queries/` | 一图一句话编号；附录 S 按需展开（不设 5 条上限，但需精炼） |

**Co-location rule**: Keep a concept's definition, its figure, and its formula under one heading (`§四`). Reading `§四` brings all three together。变量表与边界与式同页。

**Single source of truth**: Four elements live once in `申请信息.md`; copy from there for 一/三/五/六/七。§四按 8 要点饱满展开，不依赖外链。

**Single-closed rule**: 正文自包含，严禁 `见申请信息.md`；所有 Blockers 仅在 `申请信息.md` 记录。

## Completion — 单篇闭合饱满 bar (both checkable and exhaustive)

- [ ] §一、§二、§三 各 2-4 句以上饱满陈述（非一句话）
- [ ] §四 按 8 要点饱满展开：总体→设计构思→分步物理过程→可自编/源码→变量释义→推导→硬件→实施例，单篇可复现
- [ ] ≥2 figures embedded, each with caption and paired files `figures/embed/*.png` + `figures/source/*`（上不封顶，按需 2-6 图）
- [ ] ≥2 core formulas, each with variable map + I/O + boundary + derivation on the same page（上不封顶，变量表与边界同页）
- [ ] 必要源码摘录与式同页或紧邻，硬件与软硬件分工写清
- [ ] 正文自包含，无 `见申请信息.md`，无零过程元段落（无开头blockquote/基本信息表/待补清单/Completion/文末*本交底书为…*/Co-location/预算/法律指向）
- [ ] 工程化 prose，单篇闭合，单一稳定文件 `技术交底书.md`
- [ ] 附录 S 按需展开，全文不设 [S#] 数量上限但需精炼，仅在直接引用句尾使用
