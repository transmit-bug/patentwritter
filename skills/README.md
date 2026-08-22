# Skills map (grouped source layout, ADR-0011)

```text
skills/
├── self-service/     自助组:发明人自助链路(5 技能,包主体)
├── professional/     专业组:CN 授权链路(入口 + 5 discipline + 2 隐藏 US 保留)
├── tools/            工具组:conversion(材料摄入)、word-delivery(Word 交付,用户主动调用)、patents-search(委托检索,可选)
└── patent-standards/ 跨组共享:分型法律锚点(两组均依赖)
```

**分组 = 安装单元**(实测 2026-08-13):

```bash
npx skills add transmit-bug/patentwritter                        # 整包(推荐,15 技能引用全通)
npx skills add transmit-bug/patentwritter/skills/self-service    # 只装自助组 5 技能
npx skills add transmit-bug/patentwritter/skills/professional    # 只装专业组 6 可见技能
```

子路径安装后,跨组引用需一并补装共享与工具:`skills/patent-standards`(两组都需要)、`skills/tools/conversion`(自助组需要)、`skills/tools/word-delivery`(需要 Word 交付时)、`skills/tools/patents-search`(可选)。也支持 `-s <names>` 按名选择。

另有一条**分组安装面**:仓库根的 `.claude-plugin/marketplace.json` 声明四个分组,self-service / professional / tools / standards,供 Claude Code 插件市场按组安装。注意两种安装几何不同:skills CLI 恒按技能名拍平(上面命令),marketplace.json 才保留分组;它列出的是 15 个可见技能(隐藏 US 技能不在内),路径必须与源树同步,技能增删改名时一并更新。

The **self-service chain** is the package's core; the professional chain and reserved US skills live under `professional/`, see package-repo `docs/guide/README.md`.

`patent-intake` is the front door and orchestrator of the self-service chain; the disciplines below it each own one artifact. The workspace directory in the inventor's project is `patent-application/` (草稿/附图/成品, ADR-0008) — a **workspace name, not a skill name**.

## Skill roles

| Skill | Role | Owns |
|---|---|---|
| `self-service/patent-intake` | front door + orchestrator | routing (source × deliverable × type), interview, stage checklist, back edges, assembly handoff; shared `references/` |
| `self-service/patent-drafting` | discipline | 权利要求书 + 说明书 + 摘要, the support chain as one owner (claims first, then specification) |
| `self-service/patent-drawings` | discipline | 附图, figure-type routing, numeral consistency, abstract figure |
| `self-service/patent-compliance` | discipline | pre-filing self-check, report at `草稿/检查报告.md` |
| `self-service/patent-filing` | discipline | filing / rectification guidance, 👤 steps marked |
| `patent-standards` | shared service | standards index and on-demand anchors |
| `tools/conversion` | service | material intake only (docx/pptx → md for the interview); no Word delivery |
| `tools/word-delivery` | service (user-invoked) | md → docx Word delivery on explicit request; template filling; acceptance gate; regeneration after revisions (ADR-0013) |
| `tools/patents-search` | service | delegated prior-art search (optional) |

Merge rationale (ADR-0009): a skill survives only if it passes one of four tests — independent re-entry, distinct tool surface / failure mode, checker independence from drafter, load budget. router+application and claims+specification failed all four and were merged into `patent-intake` / `patent-drafting`.

## Three flows (the whole relationship model)

**Control flow** — who drives whom; strictly downward, back edges owned by the orchestrator:

```text
patent-intake (cold start / resume from stage checklist)
├─ source intake ──► conversion (ingestion) / environment fetch
├─ interview ──────► references/interview.md · design-points.md · type-decision.md
├─ dispatch ───────► patent-drafting → patent-drawings
├─ gate ───────────► patent-compliance ── critical? ── back edge ──► drafting/drawings
├─ deliver ────────► finalized .md drafts (default completion point)
├─ word export ────► word-delivery (user-invoked only)
└─ on request ─────► patent-filing (weeks later, independent re-entry)
```

**Data flow** — artifacts decide the order; disciplines never call each other sideways:

```text
材料 → .patent/materials/ (archive contract, five flags)
申请信息.md (route record + stage checklist) ──► 权利要求书.md ──► 说明书.md + 摘要.md
      ──► 附图/ (源文件/ 预览/ 嵌入/ + 摘要附图) ──► 检查报告.md (critical=0 is the gate)
      ──► 成品/申请文件/*.docx + 成品/技术交底书.docx (only via word-delivery, on request)
```

**Knowledge flow** — single-source pointers, read-only; never call paths:

```text
drafting/drawings/compliance/filing ──► patent-standards/references/<per-type anchor>
any consumer of the design branch ───► patent-intake/references/design-points.md (single executable version)
intake (source handling) ────────────► patent-intake/references/source-modes.md
drafting Part B (honesty) ───────────► source-modes.md paper delta
search ──────────────────────────────► patent-intake/references/search-guide.md + patents-search/
```

## Route ownership

- **Intake** owns source handling (archive contract + ingestion channel + extract-confirm-fill), the three routing axes, interview sequencing, stage progression, back-edge routing, and assembly handoff.
- **Disciplines** own only their artifact and update their own stage in the checklist.
- **Standards** owns legal source locations; downstream skills point, they do not reproduce.
- **Conversion** owns material intake at the pipeline head and Word acceptance at the tail.

Case facts, papers, formulas, citations, and experimental data belong to the project support workspace and drafts, never to this package's skills.
