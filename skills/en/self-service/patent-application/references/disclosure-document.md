# 技术交底书 Assembly (技术交底书组装)

A 技术交底书 (invention disclosure) is the **single consolidated document** handed to a patent agency for drafting, or used for internal patentability review. It is not a filing document — no statutory five-part structure, no formal layout. It leads with the invention itself: problem → solution → effect → distinguishing features, then the draft claims as an appendix. One 交底书 = one document; the three filing documents stay separate (their .docx are `成品/申请文件/`, for CNIPA 分文件递交).

Assembled at Stage-5 (before Word delivery) by the patent-application entry skill: merge the 草稿/ drafts into `草稿/技术交底书.md`, then convert it to `成品/技术交底书.docx` (delivery chain in `../../conversion/SKILL.md`).

## Structure and assembly table

| 交底书章节 | 来源（草稿/） | 说明 |
|---|---|---|
| 基本信息（发明名称 / 申请类型 / 申请人 / 发明人 / 日期） | 草稿/申请信息.md | 照抄 |
| 一、技术领域 | 说明书.md §技术领域 | 照抄 |
| 二、背景技术 | 说明书.md §背景技术 | 照抄；诚实红线不变 — 只写发明人已知的现有方案 / 客观通用问题 / 检索工具真实返回的结果 |
| 三、要解决的技术问题 | 草稿/申请信息.md 中记录的四要素·技术问题 | 照抄，不重写 |
| 四、技术方案 | 说明书.md §发明内容的技术方案部分 | 照抄，并在对应处**内嵌附图** `../附图/嵌入/figN.png`，每图配图注「图N …」与 附图说明 一致 |
| 五、技术效果 | 草稿/申请信息.md 中记录的四要素·技术效果 | 照抄（数据或机理，不新造） |
| 六、与现有技术的区别特征 | 草稿/申请信息.md 中记录的四要素·区别特征 | 照抄 |
| 七、附图说明 | 附图说明.md | 照抄（编号 + 标记清单 + 摘要附图） |
| 附录 A：权利要求草案（全文） | 权利要求书.md | 全文照抄 |
| 附录 B：摘要 | 摘要.md | 照抄 |

## Assembly rules

- **This is an assembly, not a redraft**: copy every section verbatim from its source; do not rewrite, generalize, or "improve". The four elements stay exactly as recorded in 草稿/申请信息.md.
- **Figures**: reference `../附图/嵌入/figN.png` (the png bitmaps under `附图/嵌入/`, see `../../patent-drawings/SKILL.md` Step 2). The md lives in 草稿/, so the `../` steps up to the project root.
- **Do not duplicate 具体实施方式**: it stays in 说明书.md / 说明书.docx; the 交底书's 附录 and the companion `成品/申请文件/说明书.docx` together give the agency the full picture.
- **Honesty red line applies unchanged**: no invented prior art, patents, literature, or experimental data anywhere in the assembled document.
- **One file**: the whole disclosure is one `技术交底书.md` → one `技术交底书.docx` (ADR-0008). Never split it, never add timestamps.
