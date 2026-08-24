---
name: patent-filing
description: "Filing and rectification guidance for CN patent applications (发明/实用新型/外观设计) — e-filing steps, fees and fee reduction, post-filing process, rectification-notice protocol with the beyond-scope red line and deadlines. Marks the steps only the applicant can perform; amounts and deadlines follow the official system."
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Filing and Rectification Guidance (递交与补正指引)

Role: **discipline** of the self-service group. A re-entry point independent of drafting — filing and rectification happen weeks later, against the finished deliverables. On completion, update the 递交 stage in `草稿/申请信息.md`.

Standards pointer: `../patent-standards/`. Verify current amounts, deadlines, and portal prompts against the official system and the actual notice.

Input: the completed application file package + application type. This skill is a walk-through: step-by-step actions, with steps marked 👤 executable only by the applicant themselves (registration / payment / signature — identity and funds).

## Before filing

1. 👤 Confirm the applicant (individual / entity) and inventor list; information must match the ID documents.
2. Check the file package is complete. Drafts under `草稿/` (invention / utility model: 申请信息.md / 权利要求书.md / 说明书.md / 摘要.md / 附图说明.md + drawings in `附图/`; design: 简要说明.md + 视图清单.md + pictures or photographs in `图片/`). Word deliverables under `成品/` (invention / utility model: 申请文件/权利要求书.docx + 说明书.docx + 摘要.docx; design: brief description) — when the degradation chain was taken, the .md drafts themselves are the upload source. 技术交底书.docx is for the agency / internal review, never part of the CNIPA filing package — seeing it in `成品/` is not a missing-file finding.
3. 👤 Prepare the e-filing environment: visit the Patent Business Processing System (cponline.cnipa.gov.cn), register an account and apply for a **digital certificate** (real-name verification needed on first application; effective within days).

## Filing (e-filing)

1. 👤 Log in, create a new application → select invention / utility model / design.
2. 👤 Fill in the system form: title (consistent with the specification), applicant, inventors, contact, fee-reduction information.
3. 👤 Upload the claims / specification / abstract / drawing files, designate the **abstract figure** (the system prompts; for designs upload the pictures/photos and designate the image best showing the design points).
4. 👤 Submit → the system generates the application number → pay the application fee **the same day or the next day**.
   - Fees (subject to what the system shows; long-standing standard here): invention application fee 900 RMB + publication printing fee 50 RMB; utility model 500 RMB; design 500 RMB.
   - 👤 Fee-reduction filing: eligible parties (individuals / small businesses, per the official fee-reduction rules of the year) can file in advance; the reduction ratio follows the filing result. Late payment = deemed withdrawn — be sure to pay within the fee deadline.

## Post-filing process (explain to the user, set expectations)

- **Utility model**: acceptance → preliminary examination (formalities + obvious defects) → grant. Typical cycle: several months.
- **Design**: acceptance → preliminary examination (formalities + obvious defects) → grant. Typical cycle: several months (same as utility model).
- **Invention**: acceptance → preliminary examination → publication (18 months; early publication can be requested) → substantive examination (must be requested and paid within **3 years** of the filing date, otherwise deemed withdrawn) → grant. Typical cycle: 2-3 years.
- After grant: complete the registration procedures, pay annuities, receive the patent certificate.

## Design e-filing points

- A design filing uses the request, pictures or photographs, and brief description; it does not use invention/utility-model claims, specification, or abstract.
- Picture/photo format and size: follow the upload prompts of the Patent Business Processing System for current size and format requirements and ensure the protected appearance is clearly shown; treat any remembered legacy size rules as non-authoritative.
- Views: submit orthographic views for the faces involved by the design points (six views only when six faces are involved; view rules in `../patent-intake/references/design-points.md`), black-white/gray in practice; keep color only when color protection is claimed — then submit color pictures or photographs.
- Designate in the system the single image best showing the design points.

## Rectification-notice handling protocol (补正通知书)

On receiving a "Notice of Rectification" (formal defects at the preliminary-examination stage; possible for invention / utility model / design):

1. **Match first**: copy down the rectification items one by one and compare against the original application (common items in the table below).
2. **Amendment principle**: delete, don't change — **amendments must not go beyond the scope recorded in the original specification and claims**. New content = beyond scope = dead end. When unsure about a feature, rather delete it than "improve" it.
3. 👤 Submit the rectified documents through the system within the deadline stated in the notice (generally 2 months, per the notice), otherwise deemed withdrawn.
4. When amendments involve replacement pages of the specification / claims, submit them per the system's replacement-page requirements.

### Common rectification items

| Rectification item | Usual cause | Handling |
|---|---|---|
| Title inconsistency | request / specification / claims titles not aligned | unify to one title |
| Reference-numeral issues | text and drawing numerals inconsistent / not numbered "图1, 图2" | align numerals (patent-compliance check 4) |
| Missing abstract figure / not designated | drawings exist but no abstract figure designated | designate the figure best showing the technical features |
| Abstract contains marketing language | "首创""领先" etc. | delete |
| Claim format | multiple-dependent-claim citation violations / numerals as limitations | fix using the claims discipline and compliance check |
| Missing documents | abstract / drawings omitted | follow the system's late-document procedure and assess filing-date impact |
| Design: class / product-name mismatch | request inconsistent with brief description / images | unify the product name, verify the Locarno class |
| Design: insufficient views or omission not declared | views don't match the faces involved by the design points; omitted views not declared in the brief description | add views or add the omission statement |
| Design: brief description missing items | missing use / design points / designated image | complete the brief description |
| Design: missing color declaration | color protection claimed but not declared in the brief description | add the color declaration in the brief description |

## Boundaries

- **Office-action (OA) responses at the substantive-examination stage** are out of scope for this skill — that is the professional-agent direction (the `professional/` group of the repo).
- All amounts, deadlines, and processes follow the Patent Business Processing System and the actual notices; this skill gives structure, not number promises.

## Completion standard

- [ ] Filing step list given, all 👤 steps marked
- [ ] Post-filing process and key deadlines (3-year substantive-examination request / fee deadlines) explained
- [ ] Rectification protocol given: match → delete don't change → deadline → replacement pages
- [ ] "Amounts and deadlines per the official sources" reminder given
- [ ] 递交 stage updated in `草稿/申请信息.md`
