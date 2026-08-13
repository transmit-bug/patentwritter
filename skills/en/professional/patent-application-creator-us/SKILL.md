---
name: patent-application-creator
description: Reserved Group A asset, hidden from discovery by default. US utility patent application creation workflow — prior art, claims, specification, diagrams, compliance. To be redone when the A direction (professional agent) restarts.
disable-model-invocation: true
metadata:
  internal: true
tools: Bash, Read, Write
model: sonnet
---

# Patent Application Creator Skill

Complete end-to-end patent application creation from invention disclosure to USPTO-ready filing.

## When to Use

Invoke this skill when users ask to:
- Create a complete patent application
- Draft a provisional patent application
- Prepare a utility patent application
- Write patent claims and specification
- Generate a full patent filing package

## What This Skill Does

Orchestrates the complete patent creation workflow as follows. The skill owns the authoring logic; all retrieval is delegated:

1. **Prior Art Search (delegated)** → Identify existing patents via delegated search
2. **Claims Drafting** → Write independent and dependent claims
3. **Specification Writing** → Create detailed description
4. **Diagram Generation** → Produce technical figures
5. **Abstract Creation** → Write concise summary
6. **Compliance Checking** → Validate USPTO requirements against catalog standards

## Retrieval & citation (read first)

This skill follows the delegation contract (`docs/prototype/delegation-contract.md`) and the patent-standards catalog (`skills/en/patent-standards/references/us.md`):

1. **Declare** — before any novelty or legal assertion, name the need: `[PRIOR-ART] <technology description>` / `[STANDARD] US <topic>`.
2. **Consume** — work only from what retrieval returned (search results with real patent numbers/URLs; standards read from catalog-declared materials).
3. **Cite** — every assertion in the output carries its anchor: `(prior art: <title>, <pub. no.>, <URL>)`; `(per 35 U.S.C. §112; MPEP §2106 — uspto.gov)`.
4. **Fail loud** — a needed grounding that cannot be obtained (no search tool, no material access) stops that portion with a 无法获取依据/blocked block; the rest still delivers grounded.
5. **Never invent** — no prior art from memory, no law from memory. User-supplied prior art (patent numbers, PDFs) counts as grounding: `(provided: <file or patent number>)`.

Before delivering, scan the output: any legal or prior-art assertion without a citation must be cited or failed loud.
7. **IDS Preparation** → List prior art for disclosure

## Complete Workflow

### Phase 1: Discovery & Research (15-30 min)

1. **Invention Interview**:
   - Get detailed invention description from user
   - Extract key features and novel aspects
   - Identify problem being solved
   - List all components/steps

2. **Prior Art Search (delegated)**:
   - Declare `[PRIOR-ART] <technology description>`; resolve via the **patents-search** skill (Valyu) or any search tool the environment exposes, or user-supplied material
   - Find 10-20 most relevant patents; each cited in output as `(prior art: <title>, <pub. no.>, <URL>)`
   - Document key differences
   - Assess patentability
   - No search tool and no user-supplied prior art → fail loud for this portion; do not draft novelty assertions

3. **Technology Landscape**:
   - Identify CPC classifications
   - Review competing approaches
   - Find terminology used in field

**Output**: Research summary with prior art analysis

---

### Phase 2: Claims Drafting (20-40 min)

1. **Claim Strategy**:
   - Define claim scope based on prior art
   - Identify distinguishing features
   - Plan independent/dependent structure
   - Choose claim types (system, method, etc.)

2. **Independent Claims**:
   - Draft 1-3 broad independent claims
   - Use preamble-transition-body structure
   - Include all essential elements
   - Distinguish from prior art

3. **Dependent Claims**:
   - Add 10-20 dependent claims
   - Cover specific implementations
   - Add fall-back positions
   - Include preferred embodiments

4. **Claim Review**:
   - Use **Patent Claims Analyzer** skill
   - Check antecedent basis
   - Fix definiteness issues
   - Validate dependencies

**Output**: Complete claims section (20-25 claims)

---

### Phase 3: Specification Writing (40-90 min)

1. **Title**:
   - Clear, descriptive (< 500 characters)
   - Matches invention scope
   - Includes key technology terms

2. **Field of the Invention**:
   - 1-2 paragraphs
   - Describe technical field
   - Reference relevant classifications

3. **Background**:
   - Problem statement (2-3 paragraphs)
   - Limitations of existing solutions
   - Need for invention
   - Cite prior art from search, each with `(prior art: <title>, <pub. no.>, <URL>)`

4. **Summary**:
   - High-level description (3-5 paragraphs)
   - Main features and advantages
   - How it solves the problem
   - Independent claims in prose

5. **Brief Description of Drawings**:
   - List each figure
   - One sentence per figure
   - Reference numbers introduced

6. **Detailed Description**:
   - Complete description of all embodiments
   - Multiple embodiments (preferred + variations)
   - Step-by-step for methods
   - Component-by-component for systems
   - Reference numbers throughout
   - Support ALL claim elements (35 USC 112(a))

7. **Examples/Embodiments**:
   - Specific implementations
   - Working examples
   - Alternative designs

8. **Advantages/Benefits**:
   - List key advantages
   - Explain improvements over prior art

9. **Specification Review**:
   - Run **patent-claims-analyzer** on the claims; verify every claim element is supported by the specification text
   - Check enablement (per 35 U.S.C. §112(a); MPEP §2164 — uspto.gov)
   - Validate completeness

**Output**: Complete specification (20-50 pages)

---

### Phase 4: Diagrams & Figures (15-30 min)

1. **Identify Figures Needed**:
   - System block diagrams
   - Method flowcharts
   - Component details
   - Alternative embodiments

2. **Generate Diagrams**:
   - Use **Patent Diagram Generator** skill
   - Create all required figures
   - Add reference numbers (10, 20, 30...)
   - Ensure clarity

3. **Figure Descriptions**:
   - Write detailed figure descriptions
   - Explain all reference numbers
   - Describe relationships between components

**Output**: 3-10 patent figures (SVG/PNG/PDF)

---

### Phase 5: Abstract & Front Matter (10-15 min)

1. **Abstract**:
   - 50-150 words (per 37 CFR §1.72 — ecfr.gov)
   - Single paragraph
   - No claim limitations
   - Broad technical description

2. **Title Page Info**:
   - Inventors
   - Assignee
   - Correspondence address
   - Prior applications (if any)

3. **Cross-References**:
   - Related applications
   - Priority claims
   - Provisional references

**Output**: Complete front matter

---

### Phase 6: Compliance & Validation (15-20 min)

Every check cites its catalog anchor; never assert compliance from memory. The catalog: `skills/en/patent-standards/references/us.md` (35 USC / 37 CFR / MPEP), provenance `docs/research/standards-catalog.md`.

1. **Formalities Check**:
   - Run **patent-claims-analyzer** on the claims
   - Abstract length: 50-150 words (per 37 CFR §1.72 — ecfr.gov)
   - Title: short and descriptive (per 37 CFR §1.72 — ecfr.gov)
   - Required sections present (per 37 CFR §1.77 — ecfr.gov)
   - Drawing references valid (per 37 CFR §1.84 — ecfr.gov)

2. **Claims Compliance**:
   - 35 USC 112(b) definiteness (per MPEP §2171-2176 — uspto.gov)
   - Antecedent basis correct (per MPEP §2173.05(e) — uspto.gov)
   - No indefinite terms (per MPEP §2173.05(b) — uspto.gov)
   - Proper dependencies

3. **Specification Compliance**:
   - 35 USC 112(a) written description (per MPEP §2163 — uspto.gov)
   - Enablement complete (per MPEP §2164 — uspto.gov)
   - All claims supported

4. **MPEP Guidance**:
   - Use the catalog's declared MPEP anchors for format requirements (MPEP §608 disclosure/claims format, §706 rejections) — read them via whatever the environment offers; if a section can't be read, mark the affected check `ungrounded` and say what is missing

**Output**: Compliance report with fixes, each finding carrying its citation

---

### Phase 7: Final Assembly (10-15 min)

1. **Document Assembly**:
   - Title page
   - Abstract
   - Drawings (brief description)
   - Specification
   - Claims
   - Abstract (at end)

2. **IDS Preparation**:
   - List all prior art from search
   - Include publication numbers
   - Add filing/grant dates
   - Note relevance

3. **Filing Package**:
   - Specification document
   - Claims document
   - Figures (separate files)
   - IDS form data
   - Assignment (if applicable)

**Output**: USPTO-ready filing package

---

## Document Templates

### Specification Structure

```markdown
[TITLE]

FIELD OF THE INVENTION

[Technical field description]

BACKGROUND

[Problem statement and prior art]

SUMMARY

[High-level invention description]

BRIEF DESCRIPTION OF THE DRAWINGS

FIG. 1 illustrates...
FIG. 2 shows...
FIG. 3 depicts...

DETAILED DESCRIPTION

[Comprehensive description with reference numbers]

First Embodiment

[Detailed description of main embodiment]

Second Embodiment

[Alternative embodiment]

Examples

[Working examples]

ADVANTAGES

[Key benefits and improvements]

CONCLUSION

[Broad scope statement]

CLAIMS

[Claims section]
```

### Claims Structure

```
What is claimed is:

1. A [system/method/apparatus] for [purpose], comprising:
    a [first element];
    a [second element]; and
    wherein [novel relationship/function].

2. The [system/method/apparatus] of claim 1, wherein [additional limitation].

3. The [system/method/apparatus] of claim 1, wherein [alternative limitation].

...

[Continue through all claims]
```

## Quality Checklist

Before finalizing, verify:

- [ ] Prior art search completed (Top 10 documented, each cited `(prior art: …)`)
- [ ] Claims drafted (1-3 independent, 10-20 dependent)
- [ ] Specification written (20+ pages)
- [ ] All claim elements supported in specification
- [ ] Diagrams created (3+ figures with reference numbers)
- [ ] Abstract written (50-150 words, per 37 CFR §1.72)
- [ ] Title short and descriptive (per 37 CFR §1.72)
- [ ] Antecedent basis checked (no critical issues)
- [ ] Definiteness verified (no indefinite terms)
- [ ] Enablement complete (sufficient detail)
- [ ] Formalities compliant (per MPEP §608; 37 CFR §1.77/§1.84)
- [ ] IDS list prepared (all prior art included)
- [ ] Figures match description
- [ ] Reference numbers consistent
- [ ] No uncited legal or prior-art assertions remain (self-check)

## File Organization

```
patent-application/
├── 01-research/
│   ├── prior-art-search.md
│   ├── top-10-patents.md
│   └── patentability-assessment.md
├── 02-claims/
│   ├── claims-draft-v1.md
│   ├── claims-final.md
│   └── claims-analysis-report.md
├── 03-specification/
│   ├── specification-outline.md
│   ├── specification-full.md
│   └── specification-review.md
├── 04-diagrams/
│   ├── fig1-system-diagram.svg
│   ├── fig2-method-flowchart.svg
│   ├── fig3-component-detail.svg
│   └── figures-list.md
├── 05-front-matter/
│   ├── abstract.md
│   ├── title.md
│   └── bibliographic-data.md
├── 06-compliance/
│   ├── formalities-check.md
│   ├── claims-compliance.md
│   └── spec-compliance.md
└── 07-filing-package/
    ├── complete-specification.pdf
    ├── claims.pdf
    ├── drawings.pdf
    └── ids-list.md
```

## Integration with Other Skills

This skill delegates, it does not orchestrate. It composes with other skills in this repo as consumers:

- **patents-search** (delegated prior art, Phase 1) — or any environment search tool
- **patent-claims-analyzer** (claim compliance, Phase 2, 6)
- **patent-standards** (catalog of 35 USC / 37 CFR / MPEP anchors in `references/us.md` for all compliance claims, Phase 6)

> 注(ADR-0004 重构):本技能为 A 组保留资产(隐藏)。原引用的 patent-diagram-generator 已删除并重做为 self-service/patent-drawings;本技能重做前,附图阶段按"delegation or fail loud"自行完成。

No skill referenced here is expected to exist beyond this repo's set; where a named skill is absent from the environment, the phase still completes via delegation or fail loud — never via a phantom tool.

## Estimated Timeline

**Provisional Application** (Lighter requirements):
- Research: 15 min
- Claims: 20 min
- Specification: 40 min
- Diagrams: 15 min
- **Total: ~90 minutes**

**Utility Application** (Full formal requirements):
- Research: 30 min
- Claims: 40 min
- Specification: 90 min
- Diagrams: 30 min
- Compliance: 20 min
- **Total: ~3.5 hours**

## User Interaction Points

Throughout the workflow, pause to:

1. **After Research**: Present patentability assessment, ask if should proceed
2. **After Claims**: Show draft claims, get feedback on scope
3. **After Specification Outline**: Review structure before full writing
4. **After Diagrams**: Confirm figures match invention description
5. **After Compliance**: Show any issues found, make fixes
6. **Before Final**: Present complete package for review

## Tools Available

- **Bash**: Run the bundled claims analyzer (patent-claims-analyzer) and delegated search scripts
- **Write**: Save all documents and sections
- **Read**: Load user invention descriptions, prior art
- **Grep**: Search through generated content
