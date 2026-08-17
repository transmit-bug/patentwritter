# Design — Verified Anchors (外观设计 — 核实锚点)

> Consumers: patent-intake (design branch), patent-drawings (design drawings section), patent-compliance (check 8), patent-filing (design e-filing points). Invention / utility-model anchors in `cn-invention-utility.md`.
> Verification: 2026-08-12 tested against the official CNIPA full texts (2020 专利法 text + 2023 实施细则 full text + 2023 审查指南 PDF full text); per-item evidence in package-repo `docs/research/design-patent-anchors.md` (not shipped with the skill). **The 2023 细则 / 指南 have no mandatory six-view rule and no "3cm×3cm / 15cm×22cm" image-size numbers (2010 old rules deleted); views follow the number of faces involved by the design points.**

## 专利法 (2020 text; source: cnipa.gov.cn full text)

| Article | Gist (drafting-relevant) |
|---|---|
| 第2条第4款 | design definition: new design on the shape, pattern or combination thereof, or the combination of color with shape / pattern, of the whole or part of a product, aesthetically pleasing and fit for industrial application |
| 第23条 | grant conditions: not part of the prior design; clearly distinguishable from prior designs or their combinations; no conflict with prior legal rights of others (prior design = designs made available to the public before the filing date, at home or abroad) |
| 第24条 | grace period (four situations within 6 months before the filing date do not lose novelty) — same as invention / utility model, see cn-invention-utility.md |
| 第27条 | application documents: request + pictures or photographs + brief description; pictures / photographs must clearly show the protected appearance |
| 第31条第2款 | unity: one application limited to one design; two or more similar designs of the same product, or two or more designs of products in the same class habitually sold or used as a set, may be filed as one application |
| 第33条第2款 | amendments must not go beyond the scope shown in the original pictures or photographs |
| 第42条 | design term 15 years, from the filing date |

## 专利法实施细则 (2023 revision, 国务院令第769号; source: cnipa.gov.cn full text)

| Article | Gist (drafting-relevant) |
|---|---|
| 第30条 | pictures / photographs: submit per the content needing protection of each product; partial designs submit overall-product views showing the protected part with dashed / solid lines; claiming color protection requires submitting color pictures or photographs |
| 第31条 | brief description: name, use, design points, and designation of one image or photograph best showing the design points; omitted views or claimed color protection shall be stated; similar designs shall designate the basic design; no commercial marketing language, no performance description |
| 第32条 | samples or models: may be requested when necessary; volume ≤ 30cm×30cm×30cm, weight ≤ 15kg |
| 第40条 | similar designs (≤ 10 items, similar to the basic design) / sets of products (same broad class, habitually sold or used together, same design concept); multiple designs in one application numbered in order and prefixed to each picture / photo name |
| 第43条 | filing date: on receipt of the request, the pictures or photographs and the brief description (invention / utility-model scope in cn-invention-utility.md) |
| 第44条 | not accepted: application missing the request, the pictures / photographs, or the brief description |
| 第53条 | when stating the product's class, use the design-product classification table published by the patent administrative department of the State Council |
| 第57条第2款 | voluntary amendment within 2 months of the filing date |
| 第58条第2款 | amendments to pictures / photographs submitted as replacement pages as prescribed |

## 审查指南 (2023 edition, 局令第78号) chapter anchors (design preliminary examination; verified against the full-text PDF table of contents)

| Anchor | Topic |
|---|---|
| 第一部分第三章 4.2 | design pictures / photographs (views follow the number of faces involved by the design points: six orthographic views only when six faces are involved; one or several faces → views of those faces, other faces may be supplemented with a perspective view; omitted views must state the reason in the brief description) |
| 第一部分第三章 4.2.1 | view names and marking (front / back / left / right / top / bottom view, marked directly below the view; 套件N / 设计N / 组件N numbering) |
| 第一部分第三章 4.2.2 | drawing pictures (solid lines of even thickness for shape; no shading lines / leader lines / center lines / dimension lines / phantom lines; computer-rendered resolution meets the clarity requirement) |
| 第一部分第三章 4.2.3 | photographing photos (clear, single background, orthographic projection rules, avoid strong light / reflections / shadows / mirror images, avoid contents / support props) |
| 第一部分第三章 4.2.4 | defects in pictures / photographs (wrong view projection relationships, unclear or too-small graphics, lines to be removed, incomplete six faces, symmetrical-face omission rules, etc.) |
| 第一部分第三章 4.3 | brief description (name consistent with the request, use, design points, designate one image best showing the design points; claimed color protection / omitted views shall be stated; no marketing language or performance description) |
| 第一部分第三章 4.4 | partial designs (submit overall-product views, dashed / solid lines showing the protected part) |
| 第一部分第三章 4.5 | designs involving graphical user interfaces (two submission modes: whole or part) |
