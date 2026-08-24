# Materials Catalog — CN/US authoritative texts + declared external source (资料目录)

> Pointed to by `../SKILL.md` (thin index). Declares **which materials exist, where they officially live, and what the citation anchors are**; not responsible for how to retrieve (retrieval is done by environment tools / humans). Per-type verification notes live in each reference file's header.

## China — the 2023 package (one body, effective 2024-01-20)

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 专利法 | As amended 2023-12-29 (8 chapters, 82 articles) | flk.npc.gov.cn (国家法律法规数据库) | 专利法 第X条 — drafting-relevant: 第2条 (definitions), 第22条 (novelty / inventive step / practical applicability), 第25条 (non-patentable subject matter), 第26条 (application documents / specification / claims), 第59条 (protection scope) |
| 专利法实施细则 | 2023年修订 (国务院令第769号, 13 chapters, 149 articles) | gov.cn 令769号 / cnipa.gov.cn | 实施细则 第X条 — drafting-relevant: 第17条 (application documents), 第20条 (specification), 第26条 (abstract), 第33条 (grace period) |
| 专利审查指南 | 2023 edition (局令第78号, six parts) | cnipa.gov.cn (局令第78号 page + full-text PDF) | 指南 第X部分第X章 — drafting-relevant: 第一部分第三章 (design preliminary examination), 第二部分第二章 (specification and claims), 第二部分第三章 (novelty), 第二部分第四章 (inventive step), 第二部分第五章 (practical applicability), 第二部分第九章 (computer programs) |

## United States

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 35 U.S.C. | Current through Pub. L. 119-102 (2026-07-12); print 2024 Main Ed. | uscode.house.gov / govinfo.gov | 35 U.S.C. §101 / §102 / §103 (Ch.10), §112 (Ch.11) |
| 37 C.F.R. Title 37 | eCFR current (amended 2026-07-20) | ecfr.gov (Part 1) | 37 CFR §1.71 (specification), §1.75 (claims), §1.77 (application arrangement), §1.104 (examination), §1.121 (amendments) |
| MPEP | 9th Ed., Rev. 01.2024 (current to 2024-01-31) | uspto.gov (mpep/index.html) | MPEP §608 (disclosure / claim format), §706 (rejection), §2106 (subject-matter eligibility), §2164 (enablement), §2171-2176 (112(b) clarity) |

## Edition summary (at a glance)

| Jurisdiction | Material | Current edition | Effective / currency date |
|---|---|---|---|
| CN | 专利法 | As amended 2023-12-29 (last amend. 2020-10-17; 2023 decision eff. 2024-01-20) | 2024-01-20 (2023 amendment) |
| CN | 专利法实施细则 | 2023年修订 (国务院令第769号, 3rd revision) | 2024-01-20 |
| CN | 专利审查指南 | 2023 edition (局令第78号) | 2024-01-20 |
| US | 35 U.S.C. | Online current through Pub. L. 119-102; print: 2024 Main Ed. | July 12, 2026 (online) |
| US | 37 C.F.R. | eCFR current (Title 37) | amended 2026-07-20 |
| US | MPEP | 9th Ed., Rev. 01.2024 | January 31, 2024 |

**Cross-system note for citation practice:** CN patent writing citations point to article numbers of 专利法 and 实施细则 (e.g., 专利法第26条第3款 — claims; 实施细则第20条 — specification) and 指南 part/chapter/section (e.g., 指南 第二部分第二章 — specification and claims). US citations point to statute section (35 U.S.C. §112), rule (37 CFR §1.71), and MPEP section (MPEP §2106, §2164, §2171-2176). The 2023 CN package (专利法 decision + 实施细则修订 + 审查指南2023 + 过渡办法) took effect as one body on 2024-01-20.

---

## Declared external sources (声明外部源)

Human-operated sources the set **documents for manual lookup; automation stays in delegated tools and environment**. Peer-level with delegated tools, not a fallback ladder: skills only reference the source info and citation anchors; no crawler / thin-wrapper code ships in the package.

### CNIPA Publication & Announcement System (国家知识产权局 公布公告系统)

| Item | Content |
|---|---|
| Official name | 国家知识产权局 公布公告系统 (epub.cnipa.gov.cn) |
| URL | http://epub.cnipa.gov.cn/ (note: **http, not https**; direct access is protected by a dynamic JS anti-crawl gateway; no stable public query URL/API) |
| Jurisdiction | CN |
| Governs | bibliographic data, full text, legal status of patent publication / announcement (invention publication / invention grant / utility model / design) |
| Citation anchor | publication / announcement number, e.g. CN209861402U; detail pages like http://epub.cnipa.gov.cn/patent/{公开号} |
| Search form | manual browser (steps in `../../patent-intake/references/search-guide.md`); real-browser automation like agent_browser can run it; on captcha fall back to Google Patents (country:CN) / WebSearch |
| Verification | 2026-08-12 curl-tested + third-party source cross-check |
