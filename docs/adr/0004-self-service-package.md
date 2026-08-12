# ADR-0004: Self-service-first package (B 组优先,类别布局)

- 状态:Accepted (2026-08-11)
- 取代/关联:ADR-0003(delegation-first,仍有效);docs/review/skills-effectiveness-review.md(审查依据)

## 背景

对 `skills/` 全量审查(见 docs/review/)发现:原六技能"看起来很充实",实际内容层是流程脚手架——旗舰技能无权利要求书、教学样例编造现有技术、grounding 是表演、缺业务主循环。审查后与用户确认方向:**面向发明人/非专业人士的自助申请向导,发明+实用新型,只覆盖专利申请全流程**(交底→类型判断→撰写→自检→递交与补正;实审 OA 答复不在本包)。

## 决策

1. **包定位 = B 组(发明人自助)**。A 组(专业代理人:OA 答复、三步法论证、claim 策略)未来以独立技能组接入,现在不建。
2. **采用 skills.sh 类别目录布局**:`skills/<category>/<name>/SKILL.md`,为将来 A/B 分组预留(`professional/` 目录已建立,当前只寄放保留的 US 技能,`disable-model-invocation: true` + `metadata.internal: true`,不参与发现)。
3. **依赖化/层级化(参考 mattpocock/skills)**:入口技能 `patent-application`(user-invoked,`disable-model-invocation: true`)编排全流程;五个 model-invoked discipline 技能(claims/specification/drawings/compliance/filing)承载可复用纪律;入口只调用 discipline,不调用入口。
4. **法律锚点单一来源**:`patent-standards` 增加"Verified rule anchors"节,条文号于 2026-08-11 对 CNIPA 官方全文实测核实(专利法 2020 文本、实施细则 2023 修订全文)。技能只引用锚点,不重复条文。
5. **内容原则**:技能 = 判断逻辑 + 可检查完成标准,不是数量指标(废除"3个实施例/20+页/Top10专利"式质量门);诚实红线:不编造现有技术/专利号/文献/实验数据。
6. **删除**:`patent-architect`(被入口+claims+spec 取代,且其 examples.md 含编造的现有技术——保留它会继续教模型造假);`patent-diagram-generator`(重做为 `patent-drawings`)。

## 后果

- 包的可发现技能:6 个(self-service 6 个,其中入口 1 + discipline 5)+ 共享 patent-standards + 可选 tools/patents-search。
- US 技能从发现面移除,保留在 `professional/` 待 A 方向重做。
- 检索不是流程依赖:发明人无检索工具时,背景技术走"诚实协议"(三类素材),不编专利号。
- 摘要 300 字限制已在 2023 细则删除——技能按新法写(以简短为要,不以字数凑)。

## 未来(非本次范围)

- A 组技能(专业代理人):OA 答复三步法论证、修改策略、claim 战略。接入时放入 `skills/professional/`,与 B 组共存。
