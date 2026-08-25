# Content Map — 内容地图

Purpose: make sure the agent and the inventor see the **same territory** before any patent judgment. A content map is a faithful, neutral summary of what the content says — not what the patent should say.

## When to build

Every mining-mode run builds one `内容地图.md` under `patents/<patent-name>/.patent/exploration/` (case-root-relative `.patent/exploration/`). Socratic-only runs can skip it, but if any document was ingested, build it.

## Structure

```markdown
# 内容地图 — <content title or short label>

来源: <archived path> | 摄入时间 | 摄入方式
形态: 论文 / 交底材料 / 现有专利 / 笔记 / 混合

## 1. 一句话梗概 (one sentence)
<what this content is about, in the user's domain language>

## 2. 结构速览 (structure at a glance)
- §1 <section> — <one-line gist>
- §2 <section> — <one-line gist>
...

## 3. 技术事实 vs 论文主张 vs 待验证 (only for paper-like sources)
| 技术事实 (reproducible) | 论文主张 (claim) | 待验证 (gap) |
|---|---|---|
| ... | ... | ... |

For non-paper sources, collapse to two columns: `已明确` / `待明确`.

## 4. 关键术语表 (glossary)
| 术语 | 内容中的含义 | 备注 |
|---|---|---|
| ... | ... | 是否与专利常用语冲突 |

## 5. 已识别的附图/表格/公式清单
- 图1: <what it shows>
- 表2: <what it compares>
- 公式(3): <what it computes>

## 6. 初步疑问 (questions for discussion)
1. ...
2. ...
```

## Rules

- **Faithful, not inventive**: do not add patent vocabulary ("其特征在于", "所述") here. Use the content's own language.
- **No paper structure leakage**: the map's headings are about the content, not about patent sections. Never create "背景技术/发明内容" headings at this stage.
- **One map per content thread**: if the user gives two unrelated papers, create `内容地图-1.md` and `内容地图-2.md`; discuss whether they share a lineage before merging.
- **Length**: aim for 1–2 pages; if the source is 20 pages, the map is still 1–2 pages. It is an index, not a translation.
- **Honesty**: every bullet traces to a page/section of the archived source. Mark `推断` explicitly if you inferred.

## Done when

- An inventor who has not read the source can understand what it does after reading the map.
- Every major section of the source has a corresponding map entry or an explicit "已略过(非技术)" note.
- The `初步疑问` list has 2–5 items that seed the Socratic loop.

## Anti-pattern

Do not produce a "专利交底书初稿" at this stage. The map is not a disclosure — it is a shared reading note.
