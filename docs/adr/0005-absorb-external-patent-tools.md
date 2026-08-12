# ADR-0005: 吸收 patent-disclosure-skill 实用能力（纯文档化，零脚本收编）

- 状态:Accepted (2026-08-12)
- 取代/关联:ADR-0003(delegation-first,仍有效);ADR-0004(self-service 包定位,仍有效);wayfinder 地图 [吸收外部专利工具：决策与整合方案 #6](https://github.com/transmit-bug/patentwritter/issues/6)
- 外部来源:[handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) @ `ff43eb7`(2026-08-12 本地克隆评估),MIT © 2026 handsomestWei。评估只读,未移植代码。

## 背景

用户提出把 [patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill)(211 文件,4 大模式,~60 个 Python 工具)的"实用性工具"吸收进本包。经 wayfinder 地图两轮 grilling + 两张 research 票 + 四张决策票(全部 HITL 用户在场),确定终点 = **决策记录 + 分阶段整合方案**,实现留待方案确认后单独执行。

关键张力:外部仓库是工具密集的 monolithic 技能;本包是委托优先/薄技能(ADR-0003/0004,CONTEXT.md「Delegated search」「Thin skill」)。裁决:**转换类能力纯文档化,不移植任何 Python 脚本;检索保持委托式,国知局作「人工操作的外部声明源」;外观设计以轻量向导分支进入**。

## 决策

### 1. 转换/交付能力 — 纯文档技能(零脚本零依赖)

外部仓库 `tools/shared/` 的 5 个转换脚本(docx_to_md / pptx_to_md / md_to_docx / math_to_omml / math_render)经 research 评估(分支 `research/absorb-conversion-tools`,报告 `docs/research/absorb-conversion-tools.md`)确认可用,但用户裁决:**md/docx 转换由 AI 实时内联生成,不随包携带脚本**。

- 新增 `skills/tools/conversion/SKILL.md`(纯文档):转换纪律 + 环境探测降级链。
- Word 交付降级链(patent-application 阶段 5 组装后):①环境有 python-docx → agent 内联生成片段,`说明书.md / 权利要求书.md / 摘要.md` 各出**同名 .docx**(固定文件名、分文件对应,不引入时间戳)②有 pandoc → 用 pandoc ③都没有 → 交付 .md + 指引用户 WPS/Word 另存;fail loud。
- 摄入降级链(阶段 1 交底访谈扫既有 .docx/.pptx):环境有 python-docx/mammoth/python-pptx 则内联读取;无则请发明人提供文本/MD/粘贴。
- 公式:latex2mathml 可用时内联转 OMML(可编辑公式);否则保留 LaTeX 原文。
- 附 `requirements-optional.txt`(可选依赖清单,按需安装,不装则走降级链)。

### 2. 附图 — Graphviz dot 单轨,不引入 mermaid / PlantUML

按 AI 适配度裁决(用户授权):dot 声明式语法简单、编译即校验、黑白天然合规(细则第 21 条)、无 Java/CJK 字体失败模式,已是 patent-drawings 前置依赖。

- SVG+PNG 双出:`dot -Tsvg`(预览/版本)+ `dot -Tpng`(Word 内联嵌入;python-docx/pandoc 原生支持 PNG,不嵌 SVG)。
- patent-drawings 步骤 2 补双输出命令;完成标准补「Word 嵌入图已生成、无缺图」。
- mermaid(Node/mmdc 重依赖、默认彩色)、PlantUML(Java 运行时、skinparam monochrome、CJK 字体风险)不进申请文件附图管线;交底内部复杂图(非申请文件)可现场 PlantUML,可选不落库。

### 3. 查新 — Valyu 核心委托 + 国知局「人工操作的外部声明源」

research 实测(分支 `research/cnipa-epub-forms`,报告 `docs/research/cnipa-epub-search-forms.md`):epub.cnipa.gov.cn 无稳定公开查询 URL/API(WAF 动态 JS 挑战,裸 GET 400);**Valyu 官方源仅 USPTO/EPO,无 CN 源** → CN 权威查新通道缺失。

- CNIPA 公布公告系统声明为「人工操作的外部源」:文档写源信息、人工浏览器检索步骤、引用锚点(公开号/公告号);零代码,不移植爬虫(自建检索禁区)。
- 可选描述 agent_browser 等浏览器自动化工具代跑人工步骤(真浏览器天然过 WAF)。
- 外部源同级:国知局 / Google Patents / Valyu 同级;不写细粒度降级叙事,AI 遇 WAF/验证码自提并切换。
- 诚实红线保持现状(「检索工具真实返回的结果」已覆盖人工检索)。

### 4. 工作目录 — `.patent/` 三档分级(支撑层)

发明人项目根目录下新增 `.patent/`(用户提出,确认采纳):

```
.patent/
├── sources/    # 声明性:专利-标准引用清单、外部源声明条目
├── materials/  # 资料性:发明人素材、检索命中文档副本
└── queries/    # 联网查询过程:Valyu/CNIPA/Google Patents 检索记录与结果
```

申请文件草稿**保持可见的 `patent-application/` 不动**(支撑层与申请文件分治)。默认建议 gitignore `.patent/`(技能文档说明,可自行留痕)。

### 5. 外观设计 — 轻量向导分支

- patent-application 内加外观分支:类别/洛迦诺分类提示/设计要点/简要说明/相似设计/请求保护色彩与否;不复制外部 design/ 全套模板与填表机制。
- type-decision.md 加外观分支;patent-standards 目录补锚点:专利法第 2 条第 4 款(外观定义)、第 23 条(外观新颖性)、第 27 条(外观申请文件),并核实实施细则/审查指南对应条文(2026-08-11 CNIPA 全文核实惯例)。
- patent-drawings 加「外观附图」节:六面正投影视图 + 立体图(照片或线条图,黑白/灰度实务),视图与简要说明对应;dot 不适用,素材由发明人提供,AI 只整理视图清单与合规核对。
- 线稿工具(design_lineart_gate)不引入(零脚本决策)。
- patent-compliance 加外观检查项(六视图齐全、简要说明与视图对应、类别正确、相似设计声明);patent-filing 补外观电子申请要点(图片文件格式/大小规范)。

### 6. 边界 — 归档与 out-of-scope

- **审查答复(OA)**:归档为 `professional/` 方向参考(外部仓库模式 D 案例 RAG 思路),当前自助包边界不动(ADR-0004)。
- **专利通俗解读(Obsidian 图谱)与政策嗅探**:判为超出本包目的地(out-of-scope),外部仓库整体可作参考。
- **许可**:未移植代码,无需 NOTICE 文件;来源与版权仅在本 ADR 与整合方案文档提及。

## 后果

- 包形态不变:6 个 self-service 技能 + patent-standards + 可选 tools/patents-search;新增纯文档 `skills/tools/conversion/` 与 `.patent/` 工作目录约定。
- 无新增硬依赖:Python 包(python-docx/mammoth/python-pptx/latex2mathml)均按「可选,按需安装」处理;Node/mmdc、Java 均不引入。
- 检索保持委托式:Valyu 核心 + 国知局/Google Patents 人工外部源。
- 附图管线补 PNG 双输出,Word 交付成为可能且合规。

## 实施记录(2026-08-12,三阶段执行完毕)

整合方案 `docs/plan/absorb-integration.md` 三阶段已按序落地(本次提交)。逐项状态:

### 阶段1 转换/交付文档化 — 完成
- 新增 `skills/tools/conversion/SKILL.md` + `requirements-optional.txt`(纯文档,零脚本):交付降级链(①python-docx 内联 → ②pandoc → ③.md+手动另存,固定文件名、分文件对应、无时间戳)、摄入降级链(.docx/.pptx 内联读取或请发明人提供)、公式 latex2mathml→OMML 可选、附图只嵌 PNG。
- patent-application 阶段5 补「生成 Word 交付」完成标准并引用 conversion;patent-drawings 步骤2 补 `dot -Tsvg` + `dot -Tpng` 双输出,完成标准补「figN.svg+figN.png 并存、Word 嵌入图无缺图」。
- 实测:本机 dot(2.43)/pandoc(3.10)可用;python-docx/mammoth/python-pptx/latex2mathml 均未安装 → 文档按「可选、探测降级」表述;dot 双输出与 pandoc PNG 内嵌均实测通过(阶段1 验收达成)。

### 阶段2 查新外部源 — 完成
- patent-application 阶段2 补「查新」小节:主路径 Valyu(注明官方清单仅 US/EP,CN 命中不保证)+ 补充路径 CNIPA 公布公告系统人工检索(浏览器步骤 / 引用锚点=公开号/公告号 / agent_browser 可选代跑 / 验证码退路 Google Patents country:CN)。
- `.patent/` 三档结构(sources/materials/queries)写入 patent-application(含 gitignore 建议);包 `.gitignore` 补 `.patent/`;README 与 AGENTS.md 包说明同步。
- patent-standards 新增「Declared external sources」节:CNIPA 公布公告系统条目(官方名 / URL=http 非 https / 管辖区 CN / 管辖内容 / 引用锚点 / 2026-08-12 核实)。

### 阶段3 外观设计轻量向导 — 完成
- patent-application 外观分支:阶段1 外观访谈线 / 阶段2 类型判断加外观+洛迦诺提示 / 阶段3 生成 简要说明.md+视图清单.md / 阶段5 外观文件清单。
- 新增 `references/design-points.md`(外观四要素不适用,改走类别+设计要点;相似设计≤10项、成套条件、简要说明内容与禁止项、保护范围与修改红线);type-decision.md 加外观分支与依据表。
- patent-standards 外观锚点 2026-08-12 后台 research 核实(报告 `docs/research/design-patent-anchors.md`):专利法 第2条第4款/第23条/第27条/第31条第2款/第33条第2款;细则 第30/31/32/40/44条、第57条第2款/第58条第2款;指南 第一部分第三章 4.2-4.5。
- patent-drawings 加「外观设计附图」节(dot 不适用、素材由发明人提供);patent-compliance 加检查项 8;patent-filing 加外观电子申请要点与补正对照表外观行。
- **偏离/修正(相对本 ADR 决策5)**:research 核实 2023 版细则与指南**无**固定六视图强制与「3cm×3cm/15cm×22cm」图片尺寸数值(2010 版旧规则已删);视图数量按「设计要点涉及的面数」决定(指南 第一部分第三章 4.2),省略视图须在简要说明写明原因。各技能外观文档均按核实结果表述,不写旧规则。

### 验收口径
- 阶段1:文档可循样例流程从 .md 产出 .docx(本机 pandoc 实测通过,PNG 内嵌验证)。
- 阶段2:patent-application 阶段2 含可直接照做的国知局检索步骤(人工或 agent_browser)。
- 阶段3:按外观分支可走通「类别→要点→视图清单→自检→递交指引」,四技能链路齐备。
- `.patent/` 约定未与现有发明人工作流冲突,无需回地图 #6 复议。

## 未来(非本次范围)

- 整合方案执行(见 `docs/plan/absorb-integration.md`)——每阶段完成后更新本 ADR 状态或追加补充记录。
- A 组(专业代理人)接入时,OA 归档参考可资借鉴;若外部仓库后续出官方 API,再评估 CNIPA 是否升级为可脚本化源。
