# Patent Writing Skill Hub

Agent skills for writing patent applications (专利申请), installable as a single package:

```bash
npx skills add transmit-bug/patentwritter
```

Built **delegation-first**: the set owns only authoring/decision logic. Every legal assertion traces to a declared authoritative source (the standards catalog), every prior-art reference comes from an external search tool — never model improvisation.

## Skills

| Skill | Purpose |
| --- | --- |
| [`patent-architect`](skills/patent-architect/SKILL.md) | Chinese patent application forms (专利申请表), grounded in delegated prior-art search + standards catalog |
| [`patent-application-creator`](skills/patent-application-creator/SKILL.md) | End-to-end USPTO application creation — prior art, claims, specification, diagrams, compliance |
| [`patent-claims-analyzer`](skills/patent-claims-analyzer/SKILL.md) | Automated 35 USC 112(b) compliance analysis of claims (antecedent basis, definiteness, structure) |
| [`patent-diagram-generator`](skills/patent-diagram-generator/SKILL.md) | Patent-style diagrams (flowcharts, block diagrams, architecture) via Graphviz with reference numbering |
| [`patent-standards`](skills/patent-standards/SKILL.md) | Standards catalog (专利标准/资料目录): which authoritative CN/US texts govern drafting, where they live, citation anchors |
| [`patents-search`](skills/patents-search/SKILL.md) | Delegated prior-art search over global patents (Valyu) |

## Design principles

- **Thin skills** — each writing skill owns only its authoring/decision logic; it consumes the catalog (`patent-standards`) and delegated search, and produces grounded output or refuses.
- **Fail loud** — if no retrieval tool is available, a skill refuses to draft and states exactly which grounding it could not obtain.
- **No vendored law** — the catalog declares *what* exists and where; it never restates law from memory.

## Repository layout

```
skills/                     # ← package source (npx skills discovery root)
  <skill>/SKILL.md          #    each skill: YAML frontmatter (name + description) + body
CONTEXT.md                  # domain glossary (delegation-first vocabulary)
docs/
  adr/                      # architectural decision records
  prototype/                # delegation-contract prototype
  research/                 # standards-catalog research
  agents/                   # issue tracker, triage labels, domain-doc conventions
```

`.agents/` and `skills-lock.json` are consumer-side install state (gitignored); regenerate with the install command above. Note: this repo is also used as a working project — `docs/` and `CONTEXT.md` document the design process, not the package itself.

## Standards

Follows the [skills.sh / Agent Skills](https://www.skills.sh/docs) package convention: each skill is a directory containing `SKILL.md` with `name` and `description` in YAML frontmatter, discovered from the `skills/` container.
