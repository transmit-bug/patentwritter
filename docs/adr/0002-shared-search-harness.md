# ADR-0002: One shared search harness with pluggable backends

- **Status**: Accepted (settled in charting, 2026)
- **Context**: Prior-art search was scattered — patents-search (Valyu) and patent-architect (SerpAPI) each carried their own backend and key story. The charting session decided a single retrieval layer serving thin writing skills.
- **Decision**: One `patent-retrieval` skill owns a shared search harness script with pluggable backends — SerpAPI/Google Patents (global, incl. CN), USPTO PatentsView (free, no key), Valyu (semantic). API keys live in environment variables, documented once in the skill. All writing skills call the harness; none call backends directly.
- **Consequences**: Keys and result shapes are managed in one place; a new backend means changing one file. Trade-off: skills depend on the harness existing — acceptable because they already depend on the retrieval layer.
- **Why not the alternatives**: Keeping per-skill backends perpetuates the scattered-key duplication this effort exists to fix; free-sources-only (HTML scraping) is brittle and has no semantic search.
