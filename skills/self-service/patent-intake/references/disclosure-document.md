# 技术交底书 Assembly — 单文件可复现（工程白话）

一份技术交底书是一份单文件可复现的披露材料，代理人据此可独立起草申请文件，无需外链补料。一份交底书对应一个文件 `drafts/技术交底书.md`，申请文件三件套另存于 `deliverables/application/`。
由 `patent-intake` 在 Stage-5 组装，`.md` 为准，docx 按需经 `../../word-delivery/SKILL.md` 另行导出。

## 语体与分层
以**工程白话**为合适语体：用“第一步做什么、数据传给谁”的自然表述，让同行能照着复现。默认以三块为底座——总体架构、白话分步、可复现说明配合一图一例；复杂案再按 `references/8-points.md` 按需展开八要点，上不封顶。

## 适用分支
| 分支 | 何时加载本文件 | 规则 |
|---|---|---|
| 交底书 | 交付物含交底书时 | 仅本文件 |
| 申请文件 | 交付物为申请文件套件时 | `../../patent-drafting/SKILL.md` |
专利法的审查口径在申请文件分支处理，本文件只负责把技术讲清楚。

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
### 3 Assemble → Done when: 每段可追溯、无论文章节复刻，图/式已按需处理
用工程白话书写，默认以三块为底座组装，复杂案按 `references/8-points.md` 展开八要点。图与式按需安排：简单案一图一例即可，复杂案上不封顶；无需时在 `application-info.md` 注明豁免。已嵌入的图带有 `图N …` 题注，成对存放于 `figures/embed/` 与 `figures/source/`（经 `../../patent-drawings/SKILL.md`），已呈现的公式每式紧跟变量表与边界，同页可读。发明名称按 `references/title-rule.md` 处理。

## Disclosed references — load only when branch fires
- 8 要点天花板（复杂案）：`references/8-points.md`
- 发明名称规范：`references/title-rule.md`

## Reference — assembly table（紧凑版）
| 章节 | 来源 | 写法 |
|---|---|---|
| 一、技术领域 | 四要素定位 | 2-4 句说清领域与场景 |
| 二、背景技术 | 可溯源三类素材 | 2-4 句说清，只写可溯源内容 |
| 三、要解决的技术问题 | `申请信息.md` technical-problem | 2-4 句照抄并展开 |
| 四、技术方案 | 四要素·方案 + 实施例 + 图/式按需 | 以工程白话三块为底座，复杂案按 `8-points.md` 按需展开 |
| 五、技术效果 | `申请信息.md` technical-effect | 数据写明条件，机理写清因果 |
| 六、区别特征 / 七、替代方案 | `申请信息.md` | 说清区别与等效替代 |
| 八、附图说明 + 附录 S | `figures/embed/` + `.patent/sources` | 一图一句话；附录 S 按需精炼 |

## 完成自检
- [ ] 已按工程白话三块（复杂案按 `8-points.md`）组装，单文件可复现，无外链
- [ ] 图与式已按需处理或在 `application-info.md` 注明豁免，附录 S 按需精炼
> 更细的校验按需由 `patent-compliance` 执行。
