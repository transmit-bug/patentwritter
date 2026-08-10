# Patent Writing Skill Hub

A hub of agent skills (`.agents/skills/`) for writing patent applications, being rebuilt to be **retrieval-grounded**: every legal assertion in a skill's output must trace to a vendored authoritative text, and every prior-art reference to a real search result — never model improvisation.

## Language

**Retrieval corpus (检索库)**:
The vendored, section-curated markdown files in the repo (`patent-retrieval` skill's corpus) holding the authoritative texts that skills read from. Searched with ripgrep; the ground truth for standards.
_Avoid_: 知识库, knowledge base, 资料库

**Patent standards (专利标准)**:
The authoritative legal/regulatory/guideline texts governing drafting and examination — 专利法, 专利法实施细则, 审查指南 (CN); 35 USC, 37 CFR, MPEP (US). The corpus is a curated subset of these. Skills cite standards; they never restate them from memory.
_Avoid_: rules, best practices

**Prior art (先有技术)**:
Existing patents and publications that a claim must be novel and non-obvious over. Sourced exclusively through the search harness; never invented or recalled.
_Avoid_: 已有技术, references

**Search harness**:
The shared script (in the `patent-retrieval` skill) that queries prior-art backends — SerpAPI/Google Patents, USPTO PatentsView, Valyu — behind one interface and one key-management story. The only sanctioned way to get prior art.
_Avoid_: per-skill scraping, ad-hoc API calls

**Thin skill (薄技能)**:
A writing skill rewritten to consume the retrieval layer (corpus + search harness) instead of carrying its own guidance prose. Produces **grounded output**.
_Avoid_: monolithic skill

**Grounded output**:
Skill output where each standards assertion cites its corpus section (e.g. 审查指南 II.3, MPEP 2106) and each prior-art reference points to a real search result.
_Avoid_: uncited output, plausible-sounding law

**Citation convention**:
The agreed format for referencing corpus sections and search results inside skill output — fixed by the prototype ticket; every writing skill follows it.
_Avoid_: informal references, no anchors
