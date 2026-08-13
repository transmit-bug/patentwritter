---
name: patent-claims-analyzer
description: Reserved Group A asset, hidden from discovery by default. US 112(b) claim compliance lint (English-only). To be redone when the A direction (professional agent) restarts.
disable-model-invocation: true
metadata:
  internal: true
tools: Bash, Read, Write
model: sonnet
---

# Patent Claims Analyzer Skill

Automated analysis of patent claims for USPTO compliance with 35 USC 112(b) requirements, grounded in the standards catalog.

## When to Use

Invoke this skill when users ask to:
- Review patent claims for definiteness
- Check antecedent basis in claims
- Analyze claim structure
- Find claim drafting issues
- Validate claims before filing
- Fix USPTO office action issues related to claims

## Retrieval & citation (read first)

This skill follows the delegation contract (`docs/prototype/delegation-contract.md`) and the patent-standards catalog (`skills/en/patent-standards/references/us.md`):

1. **Declare** — `[STANDARD] US claim definiteness` etc.; the catalog declares the governing material (MPEP §2171-2176 for 112(b); §2164 enablement; §608 claim format; §2181 means-plus-function).
2. **Consume** — each reported issue carries the anchor it is grounded on; never assert an MPEP rule that was not read from the declared material.
3. **Cite** — every issue in the report carries `(per MPEP §2173.05(e) — uspto.gov)` style citations.
4. **Fail loud** — if the relevant MPEP section cannot be read in this environment, say so and mark the affected findings `ungrounded` rather than citing from memory.
5. **Never invent** — MPEP citations come from the catalog's declared anchors, never from recollection.

## What This Skill Does

Runs the bundled analyzer (`python/claims_analyzer.py`, stdlib-only, in this skill's directory) which performs:

1. **Antecedent Basis Checking**:
   - Finds terms used with "said/the" before first introduction
   - Tracks term references across claims
   - Anchored: `(per MPEP §2173.05(e) — uspto.gov)`

2. **Definiteness Analysis** (35 USC 112(b)):
   - Identifies subjective/indefinite terms
   - Detects relative terms without reference
   - Finds ambiguous claim language
   - Anchored: `(per MPEP §2173.05(b), §2173.01 — uspto.gov)`

3. **Claim Structure Validation**:
   - Parses independent vs. dependent claims
   - Validates claim dependencies and numbering
   - Checks transitions and means-plus-function
   - Anchored: `(per MPEP §2173.05(a), §608.01(n), §2181 — uspto.gov)`

4. **Issue Categorization**:
   - **Critical**: Must fix before filing
   - **Important**: May cause rejection
   - **Minor**: Best practice improvements

## How to Use

When this skill is invoked:

1. **Locate the analyzer** (in this skill's directory — not a plugin path):
   ```bash
   ANALYZER="$(dirname "$0")/python/claims_analyzer.py"   # or resolve relative to the skill dir
   ```
2. **Run it** on the claims text (file or stdin):
   ```bash
   python3 "$ANALYZER" /path/to/claims.txt
   # or: cat claims.txt | python3 "$ANALYZER"
   ```
3. **Present analysis**:
   - Show compliance score (0-100)
   - List issues by severity (critical, important, minor), each with its MPEP anchor citation
   - Suggest specific fixes

## Analysis Output Structure

```json
{
  "claim_count": 20,
  "independent_count": 3,
  "dependent_count": 17,
  "compliance_score": 85,
  "total_issues": 12,
  "critical_issues": 2,
  "important_issues": 7,
  "minor_issues": 3,
  "issues": [
    {
      "category": "antecedent_basis",
      "severity": "critical",
      "claim_number": 1,
      "term": "said processor",
      "description": "'said processor' used before 'processor' was introduced with 'a/an'",
      "mpep_cite": "MPEP 2173.05(e)",
      "suggestion": "Introduce 'processor' with 'a/an' on first use, then reference it as 'the processor'"
    }
  ]
}
```

## Grounding rule for the report

The analyzer's `mpep_cite` field is the anchor; the presented report appends the source: `(per MPEP §2173.05(e) — uspto.gov)`. When the environment cannot read the declared MPEP material (no web access, no user-supplied file), the report marks those findings `ungrounded` and says exactly what is missing (fail loud). Uncited fixes and unverified "examiner guidance" are never produced.

## Common Issues Detected

1. **Antecedent Basis Errors** — "said/the" before "a/an" introduction; terms in dependent claims never introduced in the chain.
2. **Definiteness Issues** — subjective terms ("substantially", "about"), relative terms ("large", "fast") without reference, ambiguous language ("and/or").
3. **Structure Issues** — means-plus-function without disclosed structure; bad dependencies; missing transition.

## Integration with MPEP

MPEP anchoring is real and catalog-declared, not asserted:

- **§2171-2176** — claim rejection under 35 U.S.C. 112(b): two separate requirements (§2171), definiteness (§2173, incl. 2173.01 ambiguous, 2173.05(b) relative/indefinite, 2173.05(e) antecedent basis)
- **§2164** — enablement
- **§608 / §608.01** — claim format and disclosure content
- **§2181** — means-plus-function limitations
- **§706** — rejection practice context

Catalog: `skills/en/patent-standards/references/us.md`; full provenance: `docs/research/standards-catalog.md`.

## Tools Available

- **Read**: To load claims from files
- **Bash**: To run the bundled Python analyzer (`python/claims_analyzer.py`)
- **Write**: To save analysis reports
