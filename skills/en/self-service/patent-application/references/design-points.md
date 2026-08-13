# Design Application Points (外观设计申请要点: design interview group + drafting points)

A design protects the **product appearance itself** (shape, pattern, color and their combinations, aesthetically pleasing and fit for industrial application), not a technical solution. Therefore the invention/utility-model **"four elements" (technical problem / technical solution / distinguishing feature / technical effect) do not apply** — designs run on: **class + design points**. Rule basis: `../../../patent-standards/references/cn-design.md` (专利法第2条第4款 / 第23条 / 第27条 / 第31条第2款 / 第33条第2款; 细则第30/31/40条; 指南 第一部分第三章 4.2-4.5).

## Design interview group (Stage-1 disclosure interview, replaces the four-element questioning)

Ask in order, skip when covered, at most 4 questions per AskUserQuestion:

1. What is this product? What is it called? (→ product name, determines the class)
2. Is this product selling mainly on "good-looking shape / pattern" or on "functional structure"? (→ determine whether it is truly a design; functional-structural improvement → back to type-decision for invention / utility model)
3. Compared with products on the market, where does your appearance **differ**? (→ design points, the core of the brief description and the protection scope)
4. What view materials do you have? Photos or line drawings? Complete or not (front / back / left / right / top / bottom + perspective)? (→ view list; materials provided by the inventor, the AI never draws)
5. Any similar designs to file together? (→ similar designs: multiple similar designs of the same product can be one application, **up to 10** (细则第40条), with one designated as the basic design)
6. Do you want to **claim protection of color**? (→ color declaration; once claimed, color becomes a limitation of the protection scope; when unsure, usually don't claim)
7. Any prior disclosure (sale / exhibition / publication / leak)? (→ 专利法第24条 grace-period determination, same as invention)

## Class and Locarno classification (hint after Stage-2 type determination)

- The Locarno Classification (international design classification) is for **classification and search**, not a boundary of the protection scope; the class follows the product name and use.
- When stating the product's class, use the design-product classification table published by the patent administrative department of the State Council (细则第53条).
- Give directional hints on the class / subclass only; exact class numbers come from the official text of the International Design Classification table — never renumber from memory.
- Wrong class = rectification / examination risk; verify at self-check (patent-compliance design item).

## Brief description (Stage 3 generates 简要说明.md)

Per 细则第31条 it must contain:
- product name (consistent with the request and the views);
- use (state the use that helps determine the product class; for parts also state the product applied to);
- design points (the shape, pattern or combination differing from prior designs, or the combination of color with shape/pattern, or the part), and **designate one image or photograph best showing the design points**;
- omitted-view statement (e.g. "左视图与右视图对称,省略左视图");
- color-protection statement (if claimed; claiming color protection requires submitting color pictures or photographs, 细则第30条).

**Forbidden**: commercial marketing language; describing the product's performance (细则第31条第4款).

## Similar designs and sets

- **Similar designs**: multiple similar designs of the same product can be filed as one application, up to 10 items, with one designated as the basic design (细则第40条); whether designs are "similar" is the inventor's call — the AI states the rules but never merges on its own.
- **Sets of products**: same broad class, habitually sold or used together, with the same design concept (细则第40条).
- When multiple designs are in one application, number them in order and prefix each picture / photo name (e.g. "设计1主视图", "套件2主视图").

## View rules (single executable version)

> Materials are provided by the inventor (photos or line drawings); the AI only organizes the view list, checks naming and compliance, **never draws, never applies filters**. This section is the **single executable version** of the view rules — patent-drawings' "design drawings" section has been collapsed into a redirect to this section, with no separate rules.

- **View kinds follow the number of faces involved by the design points** (审查指南 第一部分第三章 4.2): all six faces involved → submit six orthographic views; only one or several faces involved → submit orthographic views of those faces (other faces may be submitted as a perspective view).
- Flat products: one face involved → that face's view alone may suffice; two faces involved → both views required.
- Omitted views: symmetrical / identical faces and faces not easily or not at all visible in use may be omitted, but the reason must be stated in the brief description (e.g. "左视图与右视图对称,省略左视图").
- Six-view names: front / back / left / right / top / bottom view, marked directly below each view (指南 4.2.1); the front view corresponds to the face usually facing the consumer in use or best reflecting the overall design.
- Photos or line drawings; black-white / gray in practice (color kept only when color protection is claimed, then submit color pictures or photographs).
- All views follow orthographic projection at a consistent scale, clearly showing the protected appearance (专利法第27条第2款; photographing / drawing details in 指南 4.2.2 / 4.2.3).
- View naming corresponds one-to-one with the design points in the brief description.

## Protection scope and amendments (explain to the inventor)

- Protection scope is defined by the appearance shown in the pictures or photographs; the brief description may be used to interpret (专利法第64条第2款) — the views themselves decide the scope, so treat them with care.
- Amendments must not go beyond the scope shown in the original pictures or photographs (专利法第33条第2款); a design may be voluntarily amended within 2 months of the filing date (细则第57条第2款); picture / photo amendments submitted as replacement pages (细则第58条第2款).
- Partial design (optional hint): when only part of a product is changed, a partial design can be filed — submit overall-product views and show the protected part with dashed and solid lines (细则第30条).

## Boundaries

- Line-tracing tools (auto-outline / vectorization) are not shipped with the package: zero-script decision (ADR-0005); materials stay as provided by the inventor.
- Designs have no specification / claims / abstract; patent-claims / patent-specification do not participate in the design branch.
