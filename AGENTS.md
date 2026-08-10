# AGENTS.md

A hub of agent skills for patent writing (专利撰写). The skills live in `.agents/skills/`, installed via `npx skills` (see `skills-lock.json`). The user's working concern: the current skill set is too descriptive and not retrieval-grounded — skills must ground output in real retrieved sources (patent databases, law/standard texts), not model improvisation.

## Agent skills

### Issue tracker

Issues are tracked as GitHub issues via the `gh` CLI (repo: `pony-zhang/patentwritter`). See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout: root `CONTEXT.md` + `docs/adr/`. See `docs/agents/domain.md`.
