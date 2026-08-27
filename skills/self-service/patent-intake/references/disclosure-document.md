# 技术交底书 Assembly — tight 单文件可复现

A 技术交底书 is the **tight** self-contained disclosure for an agency to draft from without extra material. One file `drafts/技术交底书.md`; filing docs stay separate `deliverables/application/`.
Assembled at Stage-5 by `patent-intake`; the `.md` is the truth, docx via `../../word-delivery/SKILL.md` on request.

## Leading word
**tight** recruits the pretrained tight loop — single file, reproducible, no external补料. Default budget: **工程白话三块即可过检**（①总体 ②白话分步3-5步“第一步做什么→数据给谁” ③可自编+1图1实施例），复杂案才展开天花板见 `references/8-points.md`。

## Rule tracks — one trigger per branch
| Track | When to load this file | Rule set |
|---|---|---|
| **tight track** | deliverable = 交底书 / 两者 | This file alone |
| filing track | deliverable = 申请文件套件 | `../../patent-drafting/SKILL.md` |
Patent law lives downstream; this file owns disclosure only.

## 正文内容 — 仅含可回溯段落
每段可追溯至 `申请信息.md` 或确认材料：
- 技术领域与应用场景（2-4 句说清领域与场景）
- 可溯源背景技术（发明人已知方案 / 客观通用问题 / 检索真实返回）
- 白话分步（第一步做什么→第二步做什么→数据给谁，3-5 步自然语言）
- 按需展开：源码/变量/推导/硬件/实施例（无公式/无硬件记 `N/A` 于 `申请信息.md`）
> 正文形态：单一稳定文件，无外链。待确认事项仅记 `drafts/申请信息.md`。校验：是否仅含上列四类段落。

## Steps — what the agent does, in order
Each step ends on a checkable completion criterion.
### 1 Verify source → Done when: 四要素与溯源均已归档且无 blocked
Confirm `drafts/申请信息.md` 四要素 + `.patent/materials/` + `.patent/sources/` 溯源完整；blocked 项暂停并向发明人追问，不进正文。
### 2 Map template → Done when: 每章已有对应模板槽位
Bind `examples/技术交底书模板.doc` 槽位到下表章节；模板占位文字保留在来源，不复制进正文。无模板时回退中性副标题（见 `references/title-rule.md`）。
### 3 Assemble → Done when: 每段可追溯且无论文章节复刻，图/式按需已处理
Write clean prose。默认按工程白话三块组装；复杂案按 `references/8-points.md` 展开 8 要点。图/式按需：简单案 1 图1例可过检，复杂案上不封顶，豁免记 `application-info.md`；已嵌入图含 `图N …` 题注且成对 `figures/embed/` + `figures/source/`（via `../../patent-drawings/SKILL.md`），已呈现公式每式紧跟变量表与边界同页。发明名称按 `references/title-rule.md`。

## Disclosed references — load only when branch fires
- 8 要点天花板（复杂案）：`references/8-points.md`
- 发明名称规范：`references/title-rule.md`

## Reference — assembly table（紧凑版）
| 章节 | 来源 | 写法 |
|---|---|---|
| 一、技术领域 | 四要素定位 | 2-4 句说清领域与场景 |
| 二、背景技术 | 可溯源三类素材 | 2-4 句说清，只写可溯源内容 |
| 三、要解决的技术问题 | `申请信息.md` technical-problem | 2-4 句照抄并展开 |
| 四、技术方案 | 四要素·方案 + 实施例 + 图/式按需 | 工程白话三块默认，复杂案按 `8-points.md` 展开 |
| 五、技术效果 | `申请信息.md` technical-effect | 数据写明条件，机理写清因果 |
| 六、区别特征 / 七、替代方案 | `申请信息.md` | 说清区别与等效替代 |
| 八、附图说明 + 附录 S | `figures/embed/` + `.patent/sources` | 一图一句话；附录 S 按需精炼 |

## Completion — tight bar
- [ ] 单文件可复现：工程白话三块（复杂案按 `8-points.md`）已组装，无外链
- [ ] 图/式按需已处理或已豁免（`application-info.md`），附录 S 按需精炼
> 详细校验（句数、题注成对、变量表同页等）由 `patent-compliance` 按需执行，不在交底书表面重复约束。
