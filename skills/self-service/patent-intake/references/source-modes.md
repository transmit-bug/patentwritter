# Source Modes (统一来源处理)

Any material source — 口述, 文档 (docx / pdf / pptx), 网页, 对谈记录, 代码, or other technical material (paper, product material, publication) — is handled by **one protocol with two orthogonal parameters**: the source's *form* decides the ingestion channel; the source's *completeness* decides the interview strategy. There are no per-source branches, no per-source skills. Once the four elements are recorded, downstream skills never read the source kind — only the five cross-cutting flags.

## Archive contract (mandatory, every source)

Archive the source **as-is** under `.patent/materials/` and register provenance in `drafts/application-info.md` ((material-location field)): what it is, when obtained, how obtained, whose it is. This is the physical basis of the honesty red line — the user must always be able to say where a piece of content came from.

## Ingestion channel table (form → channel)

| Source form | Channel | Archived artifact |
|---|---|---|
| Document (docx / pdf / pptx) | `../../conversion/SKILL.md` ingestion chain | original + extraction notes |
| Web page | environment fetch / browsing tool + snapshot | URL + access date + snapshot |
| Dialogue / meeting record | archive the transcript directly | record + participants |
| Code | read the repository directly | code location + structure notes |
| Inventor's oral description | none — the interview itself is the channel | interview record |

## Extract-confirm-fill (completeness → interview strategy)

The interview mode **emerges** from material completeness; the question bank never changes:

1. **Extract**: from whatever material exists, draft the four elements (technical problem / minimal solution / distinguishing feature / technical effect) as a candidate record.
2. **Confirm**: show the draft to the inventor element by element — "this is what I read from your material; correct it where I read it wrong."
3. **Fill**: ask only the question-bank groups (`interview.md`) covering actual gaps.

Modes that emerge: oral description = empty extraction → full question bank (**mining**); a paper or complete draft = near-full extraction → only boundary conditions asked (**confirm**); a webpage or slide deck = partial extraction → gap-filling (**mixed**).

## Five cross-cutting flags (what downstream skills consume)

Set during extraction, written into `drafts/application-info.md`. Downstream skills read flags, never the source kind:

| Flag | Trigger | Consumer |
|---|---|---|
| 公开状态 | paper published / webpage accessible / shown to a third party | novelty go/no-go before drafting; grace-period check (`interview.md` group F) |
| 语言纯度 | material is marketing or colloquial language | regularization happens **only at the claims layer** during drafting (tables now in `../../patent-claim-strategy/references/claim-language.md`, claims register only); the disclosure and specification narrative keep the inventor's engineering words |
| 数据可用性 | material carries real experimental / test data | beneficial effects may cite it, with measurement conditions stated |
| 图可用性 | material carries figures | filing-track figures: dot-drawable types are **redraw source only** (never pasted), external types route per `../../patent-drawings/SKILL.md` Step 2 (integrated or requested); the disclosure track may embed confirmed figures as-is |
| 多贡献风险 | one material contains multiple independent inventive contributions | singleness check → split-application decision (record it; do not silently merge) |

## 披露层防火墙（交付物洁净）

工作区路径与检索过程（`res/`、`.patent/`、`figures/source`、`abstract_inverted_index`、`PII` 等内部路径与检索痕迹）严禁写入交底书正文；正文仅写技术内容本身。所有溯源与缺口仅在 `drafts/申请信息.md` 与 `.patent/sources/` 归档，附录 S 仅保留一行 DOI 极简登记。

## Paper-source delta (the one source with extra traps)

- **Two-column PDF text**: default `pdftotext` output interleaves the columns into unreadable text; extract per column (page width W: `pdftotext -x 40 -W W/2-30 -y 0 -H <pageheight>` for the left half, then `-x W/2+4` for the right) and concatenate — one faithful readable copy under `.patent/extract/`.
- **Published?** If the paper is already published, the novelty risk is a **go/no-go decision, not a routine question**: the grace period covers only statutory exceptions (see the disclosure/grace-period treatment in `../../patent-standards/references/cn-invention-utility.md`; never restate the law here). Unpublished → "file before publication" becomes a scheduling constraint.
- **Related work** belongs to the first legal category of background-art material ("prior solutions the inventor knows") — mine it honestly, with or without citation numbers.
- **Core formulas**: never inferred from the paper's abstract or from a familiar algorithm name (`interview.md` group C); every variable's engineering meaning, units/ranges, and boundary handling need the inventor's confirmation.
- **Figures** are redraw material only: paper figures are not CN filing drawings (black-white line art, reference numerals, no parameter annotations).
- **Experimental data** in the paper may be cited as real evidence for beneficial effects — stating measurement conditions; never fabricated, never embellished.
