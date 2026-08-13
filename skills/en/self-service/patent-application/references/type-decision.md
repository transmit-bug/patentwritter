# Application Type Determination Decision Tree (申请类型判断决策树)

Rule basis: `../../patent-standards/references/cn-invention-utility.md` (invention / utility model), `../../patent-standards/references/cn-design.md` (design).

## Decision tree

```
Is the technical solution mainly a method / algorithm / process / formula?
├─ Yes → invention only
└─ No (product / apparatus / structure / system) → judge the nature of the improvement:
    ├─ Improvement in appearance (shape / pattern / color, aesthetics-driven, no functional structure) → design
    │   (same shape both beautiful and functional: design and utility model / invention can be considered in parallel, filed separately)
    ├─ Improvement in shape / construction / connection / layout → ask: do you also want the method protected?
    │   ├─ Yes → dual filing (一案两请: same-day invention + utility model)
    │   └─ No → ask: fast or solid?
    │       ├─ Fast (grant in 6-12 months) → utility model
    │       └─ Solid (20-year protection / substantive examination) → invention
    └─ Improvement involves material formula / method steps → invention only (a utility model cannot protect methods)
```

> Design boundary: protection covers the product appearance itself (aesthetics), not functional structure. The inventor describing "good-looking shape / pattern, anti-copying appearance" → design; describing "a structural improvement solves some technical problem" → invention / utility model. When unsure, first clarify the nature of the improvement.

## Rule basis for each conclusion (explain to the user why)

| Determination | Basis |
|---|---|
| Utility models protect products only | 专利法第2条第3款: utility model = new technical solution for the shape, construction, or combination thereof of a product |
| Design protects the appearance itself | 专利法第2条第4款: design = new design on the shape, pattern or combination thereof, or the combination of color with shape/pattern, of the whole or part of a product, aesthetically pleasing and fit for industrial application |
| Design grant conditions | 专利法第23条: not part of the prior design; clearly distinguishable from prior designs or their combinations; no conflict with prior legal rights of others |
| Design application documents | 专利法第27条: request + pictures or photographs + brief description; pictures/photographs must clearly show the protected appearance |
| Methods can only be filed as invention | 专利法第2条第2款: invention = new technical solution for a product, a method, or an improvement thereof |
| Utility model: lower inventive-step bar, faster grant | 专利法第22条第3款 (substantive features and progress vs prominent substantive features and notable progress); preliminary examination only (细则第43条 et seq.) |
| Term: invention 20 / utility model 10 / design 15 years | 专利法第42条 |
| Utility model must have drawings | 细则第20条 / 第43条 |
| Dual filing | 专利法第9条: filing both utility model and invention for the same invention-creation on the same day; after the utility model grants first it can be abandoned to obtain the invention; 细则第47条: must declare separately at filing |

## Talking points for the inventor

- **Utility model fits**: product structural improvements, want protection fast, worried about cost. **Reminder**: the inventive-step examination bar is lower, but enforcement once granted is just as effective.
- **Invention fits**: has methods / algorithms, wants 20-year protection, possibly significant commercial value.
- **Dual filing fits**: product improvement but the method also matters, want fast-then-solid — file both on the same day; the utility model grants first for early enforcement; after the invention passes substantive examination, abandon the utility model. Note 细则第47条: declare separately at filing time.
- **Design fits**: the product's appearance (shape / pattern / color) itself is the selling point, mainly to stop others copying the look. Reminder: design protects the aesthetic appearance, not functional structure; functional improvements go to invention / utility model. Term 15 years (专利法第42条).
- **Design + utility model can be evaluated in parallel**: one product may have both functional-structural improvements and appearance improvements, filed separately (e.g., structure innovation → utility model, styling innovation → design).
- **Ask first**: any plans to go overseas? Overseas mainly looks at inventions (most countries have no utility-model counterpart); hint but don't elaborate.

## Output format (write into 申请信息.md)

```
申请类型:发明 / 实用新型 / 外观设计 / 一案两请
判断依据:专利法第X条 / 细则第X条 …
给用户的说明:一段大白话,解释为什么是这个类型
```

Design addition (see `design-points.md`):

```
类别:产品名称 + 洛迦诺分类提示
设计要点:…
色彩:是否请求保护色彩
相似设计:是否合并申请(基本设计)
```
