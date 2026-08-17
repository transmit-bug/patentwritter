# Skills map (flat source layout, ADR-0010)

All skills sit directly under `skills/` — the dependency graph crosses former group boundaries, so there are no category directories. The **self-service chain** below is the package's core; the **professional chain** (`patent-prosecution` entry + five prosecution disciplines + hidden reserved US skills) lives alongside, see package-repo `docs/guide/README.md`.

`patent-intake` is the front door and orchestrator of the self-service chain; the disciplines below it each own one artifact. The workspace directory in the inventor's project is `patent-application/` (草稿/附图/成品, ADR-0008) — a **workspace name, not a skill name**.

## Skill roles

| Skill | Role | Owns |
|---|---|---|
| `patent-intake` | front door + orchestrator | routing (source × deliverable × type), interview, stage checklist, back edges, assembly handoff; shared `references/` |
| `patent-drafting` | discipline | 权利要求书 + 说明书 + 摘要, the support chain as one owner (claims first, then specification) |
| `patent-drawings` | discipline | 附图, numeral consistency, abstract figure |
| `patent-compliance` | discipline | pre-filing self-check, report at `草稿/检查报告.md` |
| `patent-filing` | discipline | filing / rectification guidance, 👤 steps marked |
| `patent-standards/` | service | standards index and on-demand anchors |
| `conversion/` | service | DOCX/PDF/PPTX intake **and** Word delivery (one skill, two ends of the pipeline) |
| `patents-search/` | service | delegated prior-art search (optional) |

Merge rationale (ADR-0009): a skill survives only if it passes one of four tests — independent re-entry, distinct tool surface / failure mode, checker independence from drafter, load budget. router+application and claims+specification failed all four and were merged into `patent-intake` / `patent-drafting`.

## Three flows (the whole relationship model)

**Control flow** — who drives whom; strictly downward, back edges owned by the orchestrator:

```text
patent-intake (cold start / resume from stage checklist)
├─ source intake ──► conversion (ingestion) / environment fetch
├─ interview ──────► references/interview.md · design-points.md · type-decision.md
├─ dispatch ───────► patent-drafting → patent-drawings
├─ gate ───────────► patent-compliance ── critical? ── back edge ──► drafting/drawings
├─ deliver ────────► conversion (Word delivery)
└─ on request ─────► patent-filing (weeks later, independent re-entry)
```

**Data flow** — artifacts decide the order; disciplines never call each other sideways:

```text
材料 → .patent/materials/ (archive contract, five flags)
申请信息.md (route record + stage checklist) ──► 权利要求书.md ──► 说明书.md + 摘要.md
      ──► 附图/ (源文件/ 预览/ 嵌入/ + 摘要附图) ──► 检查报告.md (critical=0 is the gate)
      ──► 成品/申请文件/*.docx + 成品/技术交底书.docx
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
