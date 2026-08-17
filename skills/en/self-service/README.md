# Self-service patent skills

Use `patent-router` as the front door. It selects the material, deliverable, and patent-type route; it does not draft.

```text
patent-router
├── patent-application          interview + orchestration
│   ├── patent-claims           invention / utility-model claims
│   ├── patent-specification    invention / utility-model specification + abstract
│   ├── patent-drawings         technical drawings / abstract figure
│   ├── patent-compliance       selected-branch self-check
│   ├── patent-filing           filing / rectification guidance
│   └── references/             route-specific interview and assembly references
├── patent-standards            standards index and on-demand anchors
└── ../tools/conversion         material intake and Word delivery
```

## Route ownership

- **Router** owns source, deliverable, type, and template selection.
- **Application orchestrator** owns interview sequencing and handoffs.
- **Discipline skills** own only their artifact: claims, specification, drawings, compliance, or filing.
- **Standards** owns legal source locations. Downstream skills point to the relevant file; they do not reproduce long rule-basis explanations.
- **Conversion** owns DOCX/PDF/PPTX intake, template reuse, and Word acceptance.

Case facts, papers, formulas, citations, and experimental data belong to the project support workspace and drafts, never to this package's skills.
