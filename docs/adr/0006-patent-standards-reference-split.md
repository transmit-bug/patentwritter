# ADR-0006: patent-standards 重组为薄索引 + 分型 references

- 状态:Accepted (2026-08-12)
- 取代/关联:ADR-0004(self-service 包定位;本决策细化其「法律锚点单一来源」的落盘形态);ADR-0005(吸收整合;外观锚点由此前单表扩展而来)

## 背景

ADR-0005 实施后,`patent-standards/SKILL.md` 的 Verified rule anchors 表把 发明/实用新型/外观设计 与 US 的锚点平铺在一份文件(专利法 10 行、细则 18 行、指南 8 行,外加权威文本目录与声明外部源)。用户指出两点:

1. patent-standards **名为技能、实为资料目录**(frontmatter 自称 "a declaration, not a retrieval tool")——内容应作为被技能引用的参考,而不是一个"能力"。
2. **不同专利类型的标准不同**(发明/实用新型/外观设计/US 各适用不同条文),平铺表无类型标注,消费者容易引错锚点;每次加载也带上本类型用不到的分支内容。

## 决策

- patent-standards 重组为**薄 SKILL.md 索引 + references/ 分型锚点文件**(保留为可发现技能,不降级为纯 reference 目录——模型在需要法律锚点时仍可按 description 加载索引):
  - `references/cn-invention-utility.md` — 发明/实用新型锚点(专利法/细则/指南相关行)
  - `references/cn-design.md` — 外观设计锚点(2026-08-12 核实)
  - `references/us.md` — US 锚点(35 USC/37 CFR/MPEP,专业组消费)
  - `references/catalog.md` — 权威文本目录(官方位置/版本/版次)+ 声明外部源(CNIPA 公布公告系统)
- SKILL.md 保留:声明定位、引用文件表(文件→内容→消费方映射)、两种消费模式(自服务简化/专业完整)、完整纪律与自服务纪律、scope guard。
- **跨类型共用条文**(如专利法第24条宽限期、第42条保护期、细则第43条申请日)以「主表 + 指针」处理:主行留在 cn-invention-utility.md,cn-design.md 内只放跨引用说明与类型特有事实(如外观 15 年),不复制同义行。
- 各消费技能按类型指向对应 references 文件:patent-application(发明/实用新型→cn-invention-utility,外观→cn-design)、patent-drawings(附图→cn-invention-utility,外观节→cn-design)、patent-compliance(检查8→cn-design)、professional US 技能→us.md。

## 后果

- **渐进披露**:每次只加载本类型锚点(外观/US 分支内容后置到指针),符合 writing-for-agents 的信息层级。
- **单一来源保持**:每条锚点只存在于一个文件,不因拆分产生重复。
- 包布局:`skills/patent-standards/` 由单文件变为目录;README/AGENTS.md/CONTEXT.md 已同步;ADR-0004 的「法律锚点单一来源」表述由此决策细化。
- 无新增依赖、无脚本;检索仍委托(声明外部源不变)。

## 未来(非本次范围)

- 若专业组(professional/)正式启用,US 锚点可再按审查阶段细分;当前 us.md 一个文件足够。
- 若引入其他法域(EP/PCT),按同构新增 `references/ep.md` 等,并更新 SKILL.md 引用表。
