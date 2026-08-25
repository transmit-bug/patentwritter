# Novelty Search Guide (查新指南, optional, before drafting the background art)

The novelty search is an **optional, recommended** step: run one pass before drafting the background art; write only the actual results (honesty red line; executable version in `../../patent-drafting/SKILL.md` Part B). Execute after the routing stage and before drafting (stage checklist). Search records follow the `.patent/` three-tier convention (see the "Workspace layout" section of patent-intake/SKILL.md): **search records and results land in `.patent/queries/`**, materials in `materials/`, citation lists in `sources/`.

## Main path: delegated search tool (Valyu)

Invoke `../../patents-search/SKILL.md` (script-path resolution / API-key config / output format / error handling all live in that file, not repeated here):

```bash
"$PATENTS_SCRIPT" "<natural-language query>" <maxResults>   # returns results[].title/url/content/relevance_score
```

- First run hits `"setup_required": true`: ask the user for the Valyu API key (https://platform.valyu.ai) → `scripts/search setup <key>` → retry.
- **CN coverage warning**: Valyu's patent sources per the official list cover only **US (USPTO) + EP (EPO)**; CN hits are not guaranteed.
- When CN prior art is needed, supplement with the CNIPA manual search below.

## Supplement path: CNIPA manual search (declared external source)

The CNIPA Publication & Announcement System is a declared external source (catalog entry in `../../patent-standards/references/catalog.md`); only the source info and citation anchors are referenced — no crawler code ships in the package. Manual browser steps:

1. Open http://epub.cnipa.gov.cn/ in a browser, wait for the anti-crawl check to pass (the site has a dynamic JS anti-crawl gateway; **on captcha, switch path directly — don't force through**);
2. Enter keywords, tick the types (invention publication / invention grant / utility model / design);
3. Record hits one by one: title + **publication / announcement number** (e.g. CN209861402U) as the citation anchor; when writing the background art, note "retrieved from the CNIPA Publication & Announcement System";
4. Optional: run the above with a real-browser automation tool such as agent_browser (a real browser passes the gateway naturally; results still handled under the honesty red line);
5. Blocked / timed out: fall back to Google Patents (add `country:CN`) or WebSearch.

## Landing on disk

Write the search records into `.patent/queries/` each time (Valyu raw JSON output, manual-search hit tables), kept separate from materials (`materials/`) and citation lists (`sources/`) so that background-art citations of real publication numbers can be reconciled.
