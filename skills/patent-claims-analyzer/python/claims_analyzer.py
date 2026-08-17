#!/usr/bin/env python3
"""claims_analyzer.py — antecedent basis, definiteness, and structure analysis of patent claims.

Dependency-free (stdlib only). Runs on a claims text and emits the JSON shape
documented in the patent-claims-analyzer SKILL.md.

Usage:
    python3 claims_analyzer.py [path-to-claims.txt]   # reads stdin if no path
"""

import json
import re
import sys

# ---- Indefinite / relative / ambiguous term lexicons (MPEP 2173.05) ----
INDEFINITE_TERMS = [
    "substantially", "about", "approximately", "essentially", "roughly",
    "virtually", "around",
]
RELATIVE_TERMS = [
    "large", "small", "thin", "thick", "high", "low", "fast", "slow",
    "near", "far", "close", "wide", "narrow", "strong", "weak",
]
AMBIGUOUS_PHRASES = ["and/or", "optionally", "such as", "etc.", "or the like"]
SUBJECTIVE_PHRASES = [
    "aesthetically pleasing", "user friendly", "as needed", "as desired",
    "when necessary", "substantially similar",
]

# MPEP citation anchors per issue category (within catalog-declared MPEP 2171-2176).
MPEP_CITES = {
    "antecedent_basis": "MPEP 2173.05(e)",
    "definiteness_indefinite": "MPEP 2173.05(b)",
    "definiteness_relative": "MPEP 2173.05(b)",
    "definiteness_ambiguous": "MPEP 2173.01",
    "structure_means_plus_function": "MPEP 2181",
    "structure_no_preamble": "MPEP 2173.05(a)",
    "structure_bad_dependency": "MPEP 608.01(n)",
}

STOP_WORDS = {
    "a", "an", "the", "said", "of", "for", "to", "in", "on", "with", "and",
    "or", "configured", "adapted", "operable", "comprising", "consisting",
    "wherein", "whereby", "claim", "claims", "according", "as", "that", "which",
    "at", "from", "by", "into", "such", "when", "is", "are", "be", "being",
}

CLAIM_START_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
DEPENDENT_RE = re.compile(
    r"\b(according to claim\s+\d+|of claim\s+\d+|as claimed in claim\s+\d+|"
    r"as in claim\s+\d+|claim\s+\d+|the method of claim\s+\d+|the system of claim\s+\d+)\b",
    re.I,
)
TRANSITION_RE = re.compile(r"\b(comprising|consisting of|consisting essentially of)\b", re.I)
MEANS_FOR_RE = re.compile(r"\bmeans for\b", re.I)
INTRO_RE = re.compile(r"\b(?:a|an)\s+([a-z][a-z0-9\-]+(?:\s+[a-z][a-z0-9\-]+)?)", re.I)
USAGE_RE = re.compile(r"\b(said|the)\s+([a-z][a-z0-9\-]+(?:\s+[a-z][a-z0-9\-]+)?)", re.I)
STRUCTURE_WORDS_RE = re.compile(
    r"\b(circuit|module|unit|processor|engine|mechanism|component|assembly|"
    r"pump|valve|sensor|actuator|motor|driver|controller|interface|device|apparatus)\b",
    re.I,
)


def parse_claims(text: str):
    """Return {number: body} for each numbered claim. One claim per line-start number."""
    claims = {}
    current = None
    buf = []
    for line in text.splitlines():
        m = CLAIM_START_RE.match(line)
        if m and not re.match(r"^\s*\d+\.\d", line):
            if current is not None:
                claims[current] = " ".join(buf)
            current = int(m.group(1))
            buf = [m.group(2)]
        elif current is not None:
            buf.append(line.strip())
    if current is not None:
        claims[current] = " ".join(buf)
    return claims


def head_of(phrase: str) -> str:
    """Normalize a candidate noun phrase to its head — the first content word.

    Single-word heads keep introduction/usage matching stable across claims
    (e.g. 'a pump controlled by' introduces 'pump', later 'the pump' matches).
    """
    for w in phrase.lower().split():
        if w not in STOP_WORDS and not re.fullmatch(r"\d+", w):
            return w
    return ""


def introduced_heads(body: str) -> set:
    heads = set()
    for m in INTRO_RE.finditer(body):
        h = head_of(m.group(1))
        if h:
            heads.add(h)
    return heads


def is_dependent(body: str) -> bool:
    return bool(DEPENDENT_RE.search(body))


def referenced_claims(body: str) -> list:
    return [int(n) for n in re.findall(r"claim\s+(\d+)", body, re.I)]


def analyze_claims(text: str) -> dict:
    claims = parse_claims(text)
    if not claims:
        return {
            "claim_count": 0,
            "independent_count": 0,
            "dependent_count": 0,
            "compliance_score": 0,
            "total_issues": 0,
            "critical_issues": 0,
            "important_issues": 0,
            "minor_issues": 0,
            "issues": [],
            "error": "no claims parsed — expected numbered claims like '1. A system comprising:'",
        }

    issues = []
    introduced = set()

    for number, body in sorted(claims.items()):
        dep = is_dependent(body)

        # 1) register this claim's introductions first (same-claim usage is valid)
        introduced |= introduced_heads(body)

        # 2) antecedent basis — 'said/the X' where X was never introduced
        for m in USAGE_RE.finditer(body):
            head = head_of(m.group(2))
            if not head or head.startswith("claim") or head in ("same", "like"):
                continue
            if head not in introduced:
                issues.append({
                    "category": "antecedent_basis",
                    "severity": "critical",
                    "claim_number": number,
                    "term": m.group(0).strip(),
                    "description": (
                        f"'{m.group(1).lower()} {m.group(2).strip()}' used before '{head}' "
                        "was introduced with 'a/an'"
                    ),
                    "mpep_cite": MPEP_CITES["antecedent_basis"],
                    "suggestion": (
                        f"Introduce '{head}' with 'a/an' on first use, then reference it as "
                        f"'the {m.group(2).strip()}' afterwards"
                    ),
                })

        # 3) definiteness
        for phrase in SUBJECTIVE_PHRASES:
            if phrase in body.lower():
                issues.append({
                    "category": "definiteness_indefinite",
                    "severity": "important",
                    "claim_number": number,
                    "term": phrase,
                    "description": f"Subjective term '{phrase}' without objective definition",
                    "mpep_cite": MPEP_CITES["definiteness_indefinite"],
                    "suggestion": "Define the term objectively in the specification or replace with measurable criteria",
                })
        for term in INDEFINITE_TERMS:
            if re.search(rf"\b{re.escape(term)}\b", body, re.I):
                issues.append({
                    "category": "definiteness_indefinite",
                    "severity": "important",
                    "claim_number": number,
                    "term": term,
                    "description": f"Indefinite term '{term}' without boundary or definition",
                    "mpep_cite": MPEP_CITES["definiteness_indefinite"],
                    "suggestion": f"Define '{term}' in the specification or use a precise numerical/structural criterion",
                })
        for term in RELATIVE_TERMS:
            if re.search(rf"\b{re.escape(term)}\b", body, re.I):
                issues.append({
                    "category": "definiteness_relative",
                    "severity": "important",
                    "claim_number": number,
                    "term": term,
                    "description": f"Relative term '{term}' without a reference point",
                    "mpep_cite": MPEP_CITES["definiteness_relative"],
                    "suggestion": f"Anchor '{term}' to a measured quantity or comparative reference",
                })
        for phrase in AMBIGUOUS_PHRASES:
            if phrase in body.lower():
                issues.append({
                    "category": "definiteness_ambiguous",
                    "severity": "minor",
                    "claim_number": number,
                    "term": phrase,
                    "description": f"Ambiguous language '{phrase}' blurs claim boundaries",
                    "mpep_cite": MPEP_CITES["definiteness_ambiguous"],
                    "suggestion": "Replace with an explicit enumeration or a definite alternative structure",
                })

        # 4) structure
        if not dep and not TRANSITION_RE.search(body):
            issues.append({
                "category": "structure_no_preamble",
                "severity": "important",
                "claim_number": number,
                "term": "transition",
                "description": "Independent claim lacks a transition (comprising / consisting of)",
                "mpep_cite": MPEP_CITES["structure_no_preamble"],
                "suggestion": "Add 'comprising', 'consisting of', or 'consisting essentially of' after the preamble",
            })
        if MEANS_FOR_RE.search(body):
            # structure must appear within the means-for clause itself
            # (clause ends at the next ';' / '.' / end, capped at 120 chars)
            clause = None
            for m in MEANS_FOR_RE.finditer(body):
                tail = body[m.start():m.start() + 120]
                cut = re.search(r"[;.]", tail)
                clause = tail[:cut.start()] if cut else tail
                break
            if clause is None or not STRUCTURE_WORDS_RE.search(clause):
                issues.append({
                "category": "structure_means_plus_function",
                "severity": "important",
                "claim_number": number,
                "term": "means for",
                "description": "Means-plus-function limitation without disclosed structure",
                "mpep_cite": MPEP_CITES["structure_means_plus_function"],
                "suggestion": "Recite the structure performing the function and disclose it in the specification",
            })
        if dep:
            refs = referenced_claims(body)
            if not refs or any(r not in claims for r in refs):
                issues.append({
                    "category": "structure_bad_dependency",
                    "severity": "critical",
                    "claim_number": number,
                    "term": "dependency",
                    "description": "Dependent claim references a claim number that is missing",
                    "mpep_cite": MPEP_CITES["structure_bad_dependency"],
                    "suggestion": "Point the dependency at an existing claim number",
                })

    # dedupe
    seen = set()
    deduped = []
    for issue in issues:
        key = (issue["category"], issue["claim_number"], issue["term"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(issue)
    issues = deduped

    counts = {"critical": 0, "important": 0, "minor": 0}
    for issue in issues:
        counts[issue["severity"]] += 1
    penalty = sum({"critical": 6, "important": 3, "minor": 1}[i["severity"]] for i in issues)
    score = max(0, min(100, 100 - penalty))

    independents = sum(1 for c in claims.values() if not is_dependent(c))

    return {
        "claim_count": len(claims),
        "independent_count": independents,
        "dependent_count": len(claims) - independents,
        "compliance_score": score,
        "total_issues": len(issues),
        "critical_issues": counts["critical"],
        "important_issues": counts["important"],
        "minor_issues": counts["minor"],
        "issues": issues,
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else None
    text = open(path, encoding="utf-8").read() if path else sys.stdin.read()
    print(json.dumps(analyze_claims(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
