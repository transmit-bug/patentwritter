---
name: patents-search
description: Search patents with natural language queries via Valyu's semantic search API (patents prior art). Official Valyu patent sources are USPTO (US) and EPO (EP) only — CN coverage is not guaranteed.
keywords:
  - patents
  - patent-search
  - prior-art
  - semantic-search
license: MIT
---

# Patents Search

Search patents with natural language queries powered by Valyu's semantic search API. Invoked by the self-service flow (patent-intake optional novelty search, see `patent-intake/references/search-guide.md`) as the delegated-search main path; results are consumed as real prior art under the honesty red line — never invented.

## CN coverage warning

Per the official list, Valyu's patent sources cover only **US (USPTO)** and **EP (EPO)**: `valyu/valyu-patents` (USPTO, full text with figures), `valyu/valyu-patents-epo` (EPO, full text with figures). **CN hits are not guaranteed** — when CN prior art is needed, use the CNIPA manual search (see search-guide.md).

## Requirements

1. Node.js 18+ (uses built-in fetch)
2. Valyu API key from https://platform.valyu.ai ($10 free credits)

## CRITICAL: Script Path Resolution

The `scripts/search` commands in this documentation are relative to this skill's installation directory.

Before running any command, locate the script (works for both this repo's layout and installed plugins):

```bash
# this repo: scripts live at patents-search/scripts/search
PATENTS_SCRIPT="$(dirname "$0")/scripts/search"          # when invoked from inside the skill dir
# or resolve by name from anywhere:
PATENTS_SCRIPT=$(find . -name search -path "*/patents-search/*/scripts/*" -type f 2>/dev/null | head -1)
```

Then use the full path for all commands:

```bash
"$PATENTS_SCRIPT" "CRISPR gene editing methods" 15
```

## API Key Setup Flow

When you run a search and receive `"setup_required": true`, follow this flow:

1. **Ask the user for their API key:**
   "To search patents, I need your Valyu API key. Get one free ($10 credits) at https://platform.valyu.ai"
2. **Once the user provides the key, run:**
   ```bash
   scripts/search setup <api-key>
   ```
3. **Retry the original search.**

Key sources (in priority order): environment variable `VALYU_API_KEY`, then `~/.valyu/config.json`.

## Output Format

```json
{
  "success": true,
  "type": "patents_search",
  "query": "CRISPR gene editing methods",
  "result_count": 10,
  "results": [
    {
      "title": "Patent Title",
      "url": "https://patents.google.com/...",
      "content": "Patent claims, description, technical details...",
      "source": "patents",
      "relevance_score": 0.95,
      "images": ["https://example.com/diagram.png"]
    }
  ],
  "cost": 0.025
}
```

## Error Handling

All commands return JSON with `success` field:

```json
{
  "success": false,
  "error": "Error message"
}
```

- `"setup_required": true` — API key not configured; run the setup flow above.
- Exit codes: `0` - Success; `1` - Error (check JSON for details).

## API Endpoint

- Base URL: `https://api.valyu.ai/v1`
- Endpoint: `/search`
- Authentication: X-API-Key header

## Architecture

```
scripts/
├── search          # Bash wrapper (--path / --script-dir for discoverability)
└── search.mjs      # Node.js CLI
```

Direct API calls using Node.js built-in `fetch()`, zero external dependencies.

## Source and license

Vendored third-party skill (Valyu Patents Search, skills.sh ecosystem), MIT license. Trimmed to this package's consumption kernel — the SDK integration sections were removed; see https://docs.valyu.ai for full integration examples.
