# ADR-0001: Retrieval corpus is markdown files searched by ripgrep

- **Status**: **Superseded by ADR-0003** (charting correction ruled out in-repo retrieval infrastructure)
- **Context**: The writing skills were "hollow" — they told the agent to comply with 专利法/审查指南/MPEP without ever reading them. This ADR proposed vendoring the authoritative texts in-repo.
- **Decision**: (Superseded.) The corpus would be a directory of markdown files (one file per law/guideline, section-numbered for citation anchors), retrieved by ripgrep under a citation convention.
- **Consequences**: Superseded — see ADR-0003. The set does not vendor or curate texts at all; it declares which materials exist and delegates the fetching to environment tools.
