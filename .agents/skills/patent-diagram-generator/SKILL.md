---
name: patent-diagram-generator
description: Create patent-style technical diagrams including flowcharts, block diagrams, and system architectures using Graphviz with reference numbering
tools: Bash, Read, Write
model: sonnet
---

# Patent Diagram Generator Skill

Create patent-style technical diagrams including flowcharts, block diagrams, and system architectures using Graphviz.

## When to Use

Invoke this skill when users ask to:
- Create flowcharts for method claims
- Generate block diagrams for system claims
- Draw system architecture diagrams
- Create technical illustrations for patents
- Add reference numbers to diagrams
- Generate patent figures

## What This Skill Does

1. **Flowchart Generation**:
   - Method step flowcharts
   - Decision trees
   - Process flows with branches
   - Patent-style step numbering

2. **Block Diagram Creation**:
   - System component diagrams
   - Hardware architecture diagrams
   - Software module diagrams
   - Component interconnections

3. **Custom Diagram Rendering**:
   - Render Graphviz DOT code
   - Support multiple formats (SVG, PNG, PDF)
   - Multiple layout engines (dot, neato, fdp, circo, twopi)

4. **Patent-Style Formatting**:
   - Add reference numbers (10, 20, 30, etc.)
   - Use clear labels and connections
   - Professional formatting for USPTO filing

## Retrieval & citation (read first)

This skill follows the delegation contract (`docs/prototype/delegation-contract.md`) and the patent-standards catalog (`.agents/skills/patent-standards/SKILL.md`):

1. **Declare** — before asserting a patent *figure requirement* (reference-number rules, drawing format), name the need: `[STANDARD] CN 附图` / `[STANDARD] US drawings`.
2. **Consume / Cite** — ground each stated requirement in the catalog: CN 附图内容在 说明书 之下 `(依据: 实施细则 第20条 — gov.cn)`; US drawing format `(per 37 CFR §1.84 — ecfr.gov)`.
3. **Fail loud** — a stated requirement that cannot be read from the declared material is marked `ungrounded` rather than asserted.
4. **Never invent** — reference-number conventions and drawing rules come from the catalog anchors, not recollection. The diagram craft itself (Graphviz shapes, layouts) needs no citation — it is not a legal assertion.

## Required Dependencies

This skill requires the Graphviz **`dot` binary** (not a Python plugin path):

```bash
dot -V   # verify; e.g. brew install graphviz / apt install graphviz / choco install graphviz
```

The `graphviz` Python package is optional; all examples below use the `dot` CLI directly.

## How to Use

When this skill is invoked:

1. **Verify Graphviz**: `dot -V` — if missing, install it (see above) or fail loud about the missing dependency.
2. **Write the DOT source** for the diagram (templates below), with patent-style reference numbers in labels, e.g.:
   ```dot
   digraph PatentSystem {
       rankdir=LR;
       node [shape=box, style=rounded];
       Input [label="User Input\n(10)"];
       Processor [label="Processing Unit\n(20)"];
       Output [label="Display\n(30)"];
       Input -> Processor [label="data"];
       Processor -> Output [label="result"];
   }
   ```
3. **Render** with the `dot` CLI:
   ```bash
   dot -Tsvg method_flowchart.dot -o method_flowchart.svg   # svg / png / pdf
   ```
4. **Reference numbers**: keep the numbering consistent with the 说明书文字部分 — CN: 附图标记应与文字部分描述一致 `(依据: 实施细则 第20条 — gov.cn)`; US: drawing format `(per 37 CFR §1.84 — ecfr.gov)`.

## Diagram Templates

Build DOT directly from these shapes (Graphviz-native; no wrapper needed):

- **simple_flowchart**: `digraph { start [shape=ellipse]; step1 [shape=box]; decision [shape=diamond]; }`
- **system_block**: `digraph { rankdir=LR; node [shape=box, style=rounded]; }`
- **method_steps**: sequential `rankdir=TB` chain with numbered step labels `S1..Sn`
- **component_hierarchy**: `digraph { rankdir=TB; }` with parent→child edges

## Shape Types

### Flowchart Shapes
- `ellipse`: Start/End points
- `box`: Process steps
- `diamond`: Decision points
- `parallelogram`: Input/Output operations
- `cylinder`: Database/Storage

### Block Diagram Types
- `input`: Input devices/sensors
- `output`: Output devices/displays
- `process`: Processing units
- `storage`: Memory/storage
- `decision`: Control logic
- `default`: General components

## Layout Engines

- `dot`: Hierarchical (top-down/left-right)
- `neato`: Spring model layout
- `fdp`: Force-directed layout
- `circo`: Circular layout
- `twopi`: Radial layout

## Output Formats

- `svg`: Scalable Vector Graphics (best for editing)
- `png`: Raster image (good for viewing)
- `pdf`: Portable Document Format (drawing format per 37 CFR §1.84 — ecfr.gov)

## Patent-Style Reference Numbers

Convention:
- Main components: 10, 20, 30, 40, ...
- Sub-components: 12, 14, 16 (under 10)
- Elements: 22, 24, 26 (under 20)

Example labeling:
```
"Input Sensor (10)"
"  - Detector Element (12)"
"  - Signal Processor (14)"
"Central Unit (20)"
"  - CPU Core (22)"
"  - Cache (24)"
```

## Presentation Format

When creating diagrams:

1. **Describe what will be generated**:
   "Creating a flowchart for the authentication method with 5 steps..."

2. **Generate the diagram**:
   Run Python code to create SVG/PNG/PDF

3. **Show file location**:
   "Diagram created: <output path>.svg (next to the DOT source)"

4. **List reference numbers** (if added):
   ```
   Reference Numbers:
   - Input Module (10)
   - Processing Unit (20)
   - Output Interface (30)
   ```

## Common Use Cases

1. **Method Claims** → Flowcharts
   - Show sequential steps
   - Include decision branches
   - Number steps (S1, S2, S3...)

2. **System Claims** → Block Diagrams
   - Show components and connections
   - Use reference numbers
   - Indicate data flow directions

3. **Architecture Diagrams** → Custom DOT
   - Complex system layouts
   - Multiple interconnections
   - Hierarchical structures

## Error Handling

If Graphviz is not installed:
1. Check installation: `dot -V`
2. Install for your OS (see above)
3. Verify the `dot` binary is on PATH: `which dot`
4. Re-render the DOT source; a missing dependency is reported loudly, never silently skipped

## Tools Available

- **Bash**: To run Python diagram generation
- **Write**: To save DOT code or diagrams
- **Read**: To load existing diagrams or templates
