# Skills map (grouped source layout, ADR-0011)

```text
skills/
├── self-service/     自助组:发明人自助链路(6 技能,包主体)
├── professional/     专业组:CN 授权链路(入口 + 5 discipline, 6 技能)
├── tools/            工具组:conversion(材料摄入)、word-delivery(Word 交付,按需)、patents-search(委托检索,可选)
└── patent-standards/ 跨组共享:分型法律锚点(两组均依赖)
```

**分组 = 安装单元**(实测 2026-08-13):

```bash
npx skills add transmit-bug/patentwritter                        # 整包(推荐,15 技能引用全通)
npx skills add transmit-bug/patentwritter/skills/self-service    # 只装自助组 6 技能
npx skills add transmit-bug/patentwritter/skills/professional    # 只装专业组 6 可见技能
```

子路径安装后,跨组引用需一并补装共享与工具:`skills/patent-standards`(两组都需要)、`skills/tools/conversion`(材料摄入)、`skills/tools/word-delivery`(Word 交付,按需)、`skills/tools/patents-search`(可选)。也支持 `-s <names>` 按名选择。

另有一条**分组安装面**:仓库根的 `.claude-plugin/marketplace.json` 声明四个分组,self-service / professional / tools / standards,供 Claude Code 插件市场按组安装。注意两种安装几何不同:skills CLI 恒按技能名拍平(上面命令),marketplace.json 才保留分组;它列出的是 15 个技能,路径必须与源树同步,技能增删改名时一并更新。

The **self-service chain** is the package's core; the professional chain lives under `professional/`, see package-repo `docs/guide/README.md`.

`patent-intake` is the front door and orchestrator of the self-service chain; the disciplines below it each own one artifact. The workspace is hierarchical in the inventor's project: one directory per application under `patents/<patent-name>/` (case root; directory name = target product, frozen at routing), each holding `drafts/`, `figures/`, `deliverables/` plus the case-local `.patent/` support layer — a **workspace name, not a skill name**.

## Skill roles

| Skill | Role | Owns |
|---|---|---|
| `self-service/patent-intake` | front door + orchestrator | routing (source × deliverable × type), interview, stage checklist, back edges, assembly handoff; shared `references/` |
| `self-service/patent-exploration` | content lab | 内容研讨：任何形态材料→内容地图→技术拆解→可专利点矩阵→Socratic 研讨→保护方向，向 intake 移交 |
| `self-service/patent-drafting` | discipline | 说明书(可读技术 prose 先行) → 权利要求书(从说明书提炼) + 摘要, voice wall 语体边界,支撑链单一所有者 |
| `self-service/patent-drawings` | discipline | drawings, figure-type routing, numeral consistency, abstract figure |
| `self-service/patent-compliance` | discipline | 递交前自检(仅 filing 轨), report at `drafts/check-report.md`, back-end claim formalities owner |
| `self-service/patent-filing` | discipline | filing / rectification guidance, 👤 steps marked |
| `patent-standards` | shared service | standards index and on-demand anchors |
| `tools/conversion` | service | material ingestion DOCX/PPTX → Markdown (pipeline head, ingestion only) |
| `tools/word-delivery` | service | Word delivery md → docx (pipeline tail, on demand, disable-model-invocation, single-source rule) |
| `tools/patents-search` | service | delegated prior-art search (optional) |

Merge rationale (ADR-0009): a skill survives only if it passes one of four tests — independent re-entry, distinct tool surface / failure mode, checker independence from drafter, load budget. router+application and claims+specification failed all four and were merged into `patent-intake` / `patent-drafting`.

## Three flows (the whole relationship model)

**Control flow** — who drives whom; strictly downward, back edges owned by the orchestrator:

```text
patent-exploration (optional content lab, before intake)
  └─ handover ──► patent-intake (cold start / resume from stage checklist)
├─ source intake ──► conversion (ingestion only) / environment fetch
├─ interview ──────► references/interview.md · design-points.md · type-decision.md
├─ dispatch ───────► patent-drafting (spec → claims → abstract) → patent-drawings
├─ gate ───────────► patent-compliance (filing track only) ── critical? ── back edge ──► drafting/drawings
├─ deliver ────────► word-delivery (Word 交付,按需触发, delivery form = application-info.md word-export field)
└─ on request ─────► patent-filing (weeks later, independent re-entry)
```

**Data flow** — artifacts decide the order; disciplines communicate only through artifact files and the orchestrator:

```text
materials → .patent/materials/ (archive contract, five flags)
application-info.md (route record + stage checklist + word-export) ──► 说明书.md ──► 权利要求书.md + 摘要.md
      ──► figures/ (source/ preview/ embed/ + abstract figure) ──► drafts/check-report.md (filing track only, critical=0 is the gate)
      ──► deliverables/application/*.docx + deliverables/disclosure.docx (only when word-export is agreed or the inventor asks in-turn, via word-delivery)
```

**Knowledge flow** — single-source pointers, read-only; use read-only pointers:

```text
drafting/drawings/compliance/filing ──► patent-standards/references/<per-type anchor>
any consumer of the design branch ───► patent-intake/references/design-points.md (single executable version)
intake (source handling) ────────────► patent-intake/references/source-modes.md
drafting Part B (honesty) ───────────► source-modes.md paper delta
search ──────────────────────────────► patent-intake/references/search-guide.md + patents-search/
```

## Route ownership

- **Intake** owns source handling (archive contract + ingestion channel + extract-confirm-fill), the four routing axes, interview sequencing, stage progression, back-edge routing, and assembly handoff.
- **Disciplines** own only their artifact and update their own stage in the checklist.
- **Standards** owns legal source locations; downstream skills point, they do not reproduce.
- **Conversion** owns material intake at the pipeline head; **word-delivery** owns Word acceptance at the tail (on-demand trigger, single-source rule: drafts/ is the only editable truth, deliverables/ are regenerable exports).

Case facts, papers, formulas, citations, and experimental data belong to the project support workspace and drafts, never to this package's skills.
