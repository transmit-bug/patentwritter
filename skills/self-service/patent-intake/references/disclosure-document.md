# 技术交底书 Assembly (技术交底书组装)

A 技术交底书 (invention disclosure) is the **single consolidated document** handed to a patent agency for drafting, or used for internal patentability review. It is not a filing document. One 交底书 = one document; the three filing documents stay separate (their .docx are `成品/申请文件/`, for CNIPA 分文件递交).

Assembled at Stage-5 (before Word delivery) by the patent-intake entry skill: merge the tracked sources into `草稿/技术交底书.md`, then convert it to `成品/技术交底书.docx` (delivery chain in `../../conversion/SKILL.md`).

## Rule tracks (规则双轨 — which rules gate which document)

| Track | Gates | Rule set |
|---|---|---|
| **Disclosure track (交底轨)** | `技术交底书.md` / `.docx` only | This file's assembly table + assembly rules — the **complete** rule set |
| **Filing track (申请文件轨)** | 权利要求书 / 说明书 / 摘要 (`../../patent-drafting/SKILL.md`) | Statutory drafting gates — five-part structure, claims format / citation / clarity, 支撑链, 阶梯 |

The disclosure is written for a human reader (the agency, or internal review); patent law enters **downstream**, when the agency drafts the filing set. So the filing-track gates (five-part structure, claims format, generalization, support chain, statutory openings) never apply here. The reverse holds too: a rule not written in this file is not a disclosure requirement — do not import one. When a filing-track rule seems to conflict with the assembly rules below, the assembly rules win on this track.

## Structure and assembly table (route-aware sources)

交付目标=两者: the filing drafts exist and are the sources. 交付目标=交底书: the sources are the interview four-element record and confirmed materials — **never** documents that were not produced (do not run patent-drafting just to create them). It leads with the invention itself: problem → solution → core formulas/logic → embodiments/effect → distinguishing features → alternatives, then the appendices.

| 交底书章节 | 来源 · 两者 | 来源 · 仅交底书 | 说明 |
|---|---|---|---|
| 基本信息（发明名称 / 申请类型 / 申请人 / 发明人 / 日期 / 模板标识） | 草稿/申请信息.md | 同左 | 照抄 |
| 模板适配说明（使用的模板、继承范围、降级项） | 草稿/申请信息.md 或交付检查报告 | 同左 | 仅供内部审阅，不复制模板占位文字 |
| 一、技术领域 | 说明书.md §技术领域 | 四要素记录 / 已确认材料中的领域定位 | 照抄；一句话说清领域即可，不套法定句式 |
| 二、背景技术 | 说明书.md §背景技术 | 发明人已知的现有方案（访谈 / 已确认材料），可保留发明人原话 | 照抄；诚实红线不变 — 只写发明人已知的现有方案 / 客观通用问题 / 检索工具真实返回的结果 |
| 三、要解决的技术问题 | 草稿/申请信息.md 中记录的四要素·技术问题 | 同左 | 照抄，不重写 |
| 四、技术方案（含核心公式 / 逻辑 / 已确认实施例） | 说明书.md §发明内容的技术方案部分 | 已确认材料 / 访谈记录中的方案描述 | 照抄，并在对应处**内嵌附图** `../附图/嵌入/figN.png`，每图配图注「图N …」与 附图说明 一致 |
| 五、技术效果 | 草稿/申请信息.md 中记录的四要素·技术效果 | 同左 | 照抄（数据或机理，不新造） |
| 六、与现有技术的区别特征 | 草稿/申请信息.md 中记录的四要素·区别特征 | 同左 | 照抄 |
| 七、替代方案与保护退路 | 草稿/申请信息.md / 说明书实施例 | 访谈中确认的变体 | 照抄已确认的变体，不替发明人创造方案 |
| 八、附图说明 | 附图说明.md | 有图才写：按实际内嵌的图列图注；无图整节省略 | 照抄（编号 + 标记清单；摘要附图仅两者路由） |
| 附录 S：资料依据与来源清单 | `.patent/sources/` 与 `.patent/queries/` 的已确认记录 | 同左 | 正文保持清洁；仅列真实来源和检索记录 |
| 附录 A：权利要求草案（全文） | 权利要求书.md | **省略本附录** | 仅当权利要求书.md 已存在；绝不为凑附录起草权利要求 |
| 附录 B：摘要 | 摘要.md | **省略本附录** | 仅当摘要.md 已存在 |

## Assembly rules (the complete disclosure-track rule set)

- **This is an assembly, not a redraft**: copy every section verbatim from its tracked source; do not rewrite, generalize, or "improve" into statutory formats. The four elements stay exactly as recorded in 草稿/申请信息.md.
- The body is clean prose: do not place author/year/source-parentheses in the middle of technical paragraphs. Use `[S#]` only where needed, with the full entry in 附录 S. Markdown syntax is a source notation, not deliverable text.
- **Figures**: confirmed figures may be embedded in the disclosure as-is (copies land in `附图/嵌入/` for path stability, referenced `../附图/嵌入/figN.png`, figure workspace in `../../patent-drawings/SKILL.md`); the redraw / figure-type routing discipline is a filing-track requirement and does not block the disclosure. The md lives in 草稿/, so the `../` steps up to the project root.
- **具体实施方式 duplication** (两者路由 only): embodiments stay in 说明书.md / 说明书.docx — the 交底书's 附录 and the companion `成品/申请文件/说明书.docx` together give the agency the full picture. 仅交底书: confirmed embodiments belong in 四、技术方案, verbatim.
- **Honesty red line applies unchanged** (shared by both tracks): no invented prior art, patents, literature, or experimental data anywhere in the assembled document.
- **One file**: the whole disclosure is one `技术交底书.md` → one `技术交底书.docx`. Never split it, never add timestamps.
