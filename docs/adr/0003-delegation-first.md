# ADR-0003: Delegation-first — no in-repo retrieval infrastructure

- **Status**: Accepted (charting correction, 2026)
- **Context**: ADR-0001 (vendored corpus) and ADR-0002 (shared search harness) assumed the skill set should own retrieval infrastructure. The user corrected this mid-charting: 大而全 is wrong — "这些搜索的不应该声明哪些是核心、哪些是通用的,应该委托给外部去做" and "搜索的功能肯定不是我们这个来处理的". The set was headed toward maintaining a corpus, curating "core sections", and managing search keys — exactly the in-repo infrastructure the user rejected.
- **Decision**: The skill set owns only authoring/decision logic (claims, spec, abstract, claim/112(b) analysis, diagram conventions) plus a citation discipline. All retrieval is delegated:
  - Prior-art search runs on existing external tools (patents-search/Valyu, whatever the environment exposes). The set never builds a search tool and never manages keys.
  - Standards lookup runs through a thin pointer skill that **declares which materials exist and where** (a catalog of the official texts: 国家法律法规数据库, cnipa.gov.cn, uspto.gov, uscode.house.gov — what each governs, and its citation anchors). It does **not** prescribe how to fetch them — "我们只能声明哪些资料可以去查找,不应该负责具体如何去查找". The how belongs to the environment's tools.
  - When retrieval tooling is missing, skills fail loud instead of producing unverified patent text.
- **Consequences**: Supersedes ADR-0001 and ADR-0002. The set stays thin and portable; retrieval capability is whatever the host environment provides. Trade-off: output quality depends on the environment's tooling — mitigated by the fail-loud rule, which makes missing tooling visible instead of silent hollowness.
