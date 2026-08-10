# ADR-0001: Retrieval corpus is markdown files searched by ripgrep

- **Status**: Accepted (settled in charting, 2026)
- **Context**: The writing skills were "hollow" — they told the agent to comply with 专利法/审查指南/MPEP without ever reading them. The fix vendors the authoritative texts. The format decision: plain markdown files in the repo, searched with ripgrep, vs a structured JSON/YAML knowledge base vs an FTS5 semantic index (context-mode).
- **Decision**: The corpus is a directory of markdown files (one file per law/guideline, section-numbered for citation anchors), retrieved by ripgrep under a citation convention. Optional later enhancement: index into the context-mode knowledge base when running under pi — the markdown stays canonical.
- **Consequences**: Portable to any harness (Claude Code, Gemini, pi) with zero runtime dependencies; git-diffable so edition updates are reviewable; humans can read it. Trade-off: no semantic retrieval and no machine-enforced citation structure — we accept this for maintainability and portability.
- **Why not the alternatives**: A structured KB is heavy to author and hard for humans to review; an FTS5 index only exists in environments with the context-mode plugin, breaking portability.

# ADR-0002: One shared search harness with pluggable backends

- **Status**: Accepted (settled in charting, 2026)
- **Context**: Prior-art search was scattered — patents-search (Valyu) and patent-architect (SerpAPI) each carried their own backend and key story. The charting session decided a single retrieval layer serving thin writing skills.
- **Decision**: One `patent-retrieval` skill owns a shared search harness script with pluggable backends — SerpAPI/Google Patents (global, incl. CN), USPTO PatentsView (free, no key), Valyu (semantic). API keys live in environment variables, documented once in the skill. All writing skills call the harness; none call backends directly.
- **Consequences**: Keys and result shapes are managed in one place; a new backend means changing one file. Trade-off: skills depend on the harness existing — acceptable because they already depend on the retrieval layer.
- **Why not the alternatives**: Keeping per-skill backends perpetuates the scattered-key duplication this effort exists to fix; free-sources-only (HTML scraping) is brittle and has no semantic search.
