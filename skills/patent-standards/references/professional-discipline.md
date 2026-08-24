# Professional Discipline (专业组共享纪律 — declare / consume / cite / fail loud / never invent)

> Consumers: every skill in the professional group, jurisdiction-neutral — CN skills follow it via `cn-professional.md`, US skills via `us.md`.
> This file is the **single home** of the professional discipline. The per-jurisdiction anchor files (`us.md`, `cn-professional.md`) reference it and never maintain a second copy — keep the five clauses here only.

## The five clauses

1. **Declare** — before a legal assertion, declare the need: `[STANDARD] <jurisdiction> <topic>`. Determine the governing material from the per-jurisdiction anchor file (`us.md` for US, `cn-professional.md` for CN), then have the environment read that material; the skill itself never scrapes, never holds keys, never goes beyond the URLs declared in the catalog.
2. **Consume** — assert only from material actually read; no material read, no assertion.
3. **Cite** — every assertion in the output carries an anchor with its official source:
   - CN: `(per 专利法第22条第3款 — cnipa.gov.cn)` / `(per 细则第57条第3款 — cnipa.gov.cn)` / `(per 审查指南 第二部分第四章 3.2.1.1 — cnipa.gov.cn)`
   - US: `(per 35 U.S.C. §112 — uscode.house.gov)` / `(per MPEP §2106 — uspto.gov)` / `(per 37 CFR §1.75 — ecfr.gov)`
4. **Fail loud** — when a material cannot be read, emit a "cannot obtain basis" block and stop drafting that part; never force output:

````
无法获取依据: [STANDARD] <jurisdiction> <topic>
缺少: <tool or material>
请提供: <concrete options — enable a retrieval tool, supply the material as a file, or waive>
````

5. **Write only from declared sources and delegated-search results** — never restate the law from memory; the per-jurisdiction anchor files and the contract are the only authority.
