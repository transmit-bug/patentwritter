# 自助组技能法律内容浸透程度审计报告

- 审计对象: `/Users/pony/skillhub/patentwritter/skills/` 源码树（self-service 全量 + professional 概览 + patent-standards 引用面 + tools/conversion、tools/word-delivery）
- 审计性质: 只读，未修改仓库任何文件
- 设计方向（既定）: 交底阶段只留几条核心方向性准则；法律形式细节后移给专业代理机构 / 递交前阶段
- 日期口径: 以源码树当前 HEAD 为准

---

## 1. 法律内容密度表

统计口径：
- **法条/规则引用** = 法条号、实施细则/审查指南锚点、"Rule/statutory/法定"等字样
- **硬约束** = "不得/必须/禁止/never/must not/forbidden/violation/red line/红线"类语句

| 文件 | 行数 | 法律触点 | 硬约束 | 密度评级 | 主要位置 |
|---|--:|--:|--:|---|---|
| self-service/patent-drafting/SKILL.md | 179 | 2 | 8 | **高** | A2/A4/A5 权利要求句式与引用规则；B2 背景技术三来源；B6 摘要 |
| self-service/patent-filing/SKILL.md | 79 | 0 | 4 | **高**（但职责即递交） | 补正"不得超出范围"红线；费用/期限表 |
| self-service/patent-compliance/SKILL.md | 93 | 0 | 3 | **高**（但职责即自检） | 检查2 权利要求清楚性清单（所述/优选/单句号/多引多） |
| self-service/patent-drawings/SKILL.md | 112 | 1 | 4 | 中 | 实用新型必须有结构图；黑白线条图惯例；括号标记非限定 |
| self-service/patent-intake/SKILL.md | 134 | 2 | 6 | 低 | "不重复专利法解释"、交底轨不受申请轨闸门约束的声明 |
| self-service/patent-intake/references/source-modes.md | 48 | 1 | 8 | 中 | 公开状态→新颖性 go/no-go；宽限期只覆盖法定例外 |
| self-service/patent-intake/references/disclosure-document.md | 43 | 5 | 5 | 中 | 规则双轨声明；诚实红线 |
| self-service/patent-intake/references/interview.md | 58 | 1 | 1 | 低 | F 组公开/宽限期两问 + 指针不贴法条 |
| self-service/patent-intake/references/search-guide.md | 29 | 0 | 2 | 低 | 诚实红线引用；CNIPA 手工检索步骤 |
| self-service/patent-intake/references/design-points.md | 48 | 0 | 0 | 低 | 无法律触点，纯访谈/视图清单 |
| self-service/patent-intake/references/type-decision.md | 39 | 0 | 0 | 低 | 纯决策树 |
| self-service/patent-drafting/references/claim-language.md | 26 | 0 | 1 | 中 | 整文件即权利要求语言转换/纠错表（属 C 类形式规则） |
| tools/conversion/SKILL.md | 36 | 0 | 2 | 低 | 无法律内容，纯摄入纪律 |
| tools/word-delivery/SKILL.md | 121 | 1 | 10 | 低（硬约束多为工程纪律而非法律） | 触发门/单一真源/验收门均为流程纪律 |
| patent-standards/SKILL.md | 46 | 4 | 6 | （索引本身，不计入浸透） | 自助纪律简化版四条 |
| patent-standards/references/cn-invention-utility.md | 43 | 22 | 4 | （法定锚点库，按需读取） | 全文即法条表 |
| patent-standards/references/cn-design.md | 43 | 20 | 1 | 同上 | 全文即法条表 |
| 其余 standards references（cn-professional/us/catalog/professional-discipline） | — | — | — | 专业组消费，不在自助浸透范围 | — |

**结论速览**: 浸透集中在 `patent-drafting/SKILL.md` 一个文件（A 部分约 60 行为密集法律形式规则），其次是 compliance/filing 两份"本来就是合规岗位"的文件（其密度是职责使然，不算病灶）。intake 组整体干净——双轨制已把申请轨规则挡在 disclosure-document.md 一张表之后。

### 逐处摘录（自助组，每处 ≤2 行）

**patent-drafting/SKILL.md（高）**
- :42 (A2) `一种<上位主题名称>,包括:<…共有必要特征>;其特征在于:<区别于现有技术的特征>。` —— C 类句式模板
- :46 (A2) `Characterizing portion: introduced by "其特征在于".` —— C
- :67-77 (A4) 引用规则三条：`A multiple dependent claim must not serve as the basis of another multiple dependent claim` 等 —— C 类细则25条复述
- :83-95 (A5) 清晰度八项检查表：`"所述" has an antecedent`、`One claim, one full stop`、`Reference numerals in parentheses only`、`No leading phrases` —— C 类集中区
- :110-118 (B2) `Honesty red line … the background art may only contain three kinds of material` —— B+A 混合（防编造=A 类质量；三分类框架=B 类提示）
- :158 (B6) `the 2023 Implementing Regulations removed the 300-character statutory cap` —— 已自我修正的历史法条残留，可删

**patent-compliance/SKILL.md（高，职责使然）**
- 检查2: `undefined "所述" terms; leading phrases such as "优选""例如""最好"; multiple-dependent claims that create an invalid citation chain; numerals used as limitations` —— C 类检查项集合
- 检查5: `Model-inferred core relations are critical blockers` —— A 类（内容真实性）

**patent-filing/SKILL.md（高，职责使然）**
- 补正协议第2步: `amendments must not go beyond the scope recorded in the original specification and claims. New content = beyond scope = dead end.` —— C/B 类（递交期红线，位置合理）
- Filing 节: `substantive examination (must be requested and paid within 3 years … otherwise deemed withdrawn)` —— B 类一次性期限提示，位置合理

**patent-drawings/SKILL.md（中）**
- Utility model mandatory items: `A utility model must have drawings showing the shape / construction / combination` —— C 类形式要求（细则20），但作为交付阻断器有存在必要
- Step 3 图检: `black-white line art; no color figures, photos, or gray shading (practice)` —— C 类惯例

**patent-intake/SKILL.md（低）**
- Single pointers 末条: `no statutory text or Rule-basis tables copied here` —— 正向纪律声明，保留

**patent-intake/references/source-modes.md（中）**
- :44 `the grace period covers only statutory exceptions … never restate the law here` —— B 类，且已带指针，形态正确

**patent-intake/references/disclosure-document.md（中）**
- Rule tracks 表: `the filing-track gates (five-part structure, claims format, generalization, support chain, statutory openings) never apply here` —— 双轨隔离声明，是抗浸透的关键结构，保留

---

## 2. 三分类归类（A=写作工艺保留 / B=法律风险决策一次性提示 / C=形式合规细节应后移）

### patent-drafting/SKILL.md

| 小节 | 归类 | 说明 |
|---|---|---|
| A1 必要特征删除测试 | **A** | 上位化判断核心工艺，内容质量需要 |
| A2 独权两句式模板（包括/其特征在于） | **C** | 句式规则，纯权利要求书格式 → 后移或压成一行模板 |
| A3 概括阶梯三问 | **A**（含一条 C） | 问题导向概括是工艺；其中"supported by the description"一句是 C |
| A4 从权引用规则（先引在前/多引单一/多引不当基础） | **C** | 细则25条逐条复述 → 后移 compliance/filing |
| A5 清晰度八项表（所述先行基础、单句号、括号标记、禁引导词） | **C**（术语一致一条为 A） | 典型形式合规 → 后移 |
| B1 技术领域一句话 | **C**（轻） | "本发明涉及…"法定开头 → 可压成一行示例 |
| B2 背景技术诚实红线（三来源） | **B+A** | 防编造是内容质量底线（A）；"只能写三类材料"的分类学是法律框架（B），一次性提示即可 |
| B3 三方对应 + 核心公式门 | **A** | 支撑链与公式变量定义是内容质量本体 |
| B4 附图说明一句话一图 | **C**（轻） | 压成一行示例 |
| B5 充分公开五要素 + 支撑链 | **A** | "能再现"测试是内容质量本体 |
| B6 摘要四要素 + 300 字历史注 | **C**（轻）+ 可删残留 | 四要素保留；300 字法规注释删除 |

### 其他文件

| 文件/小节 | 归类 |
|---|---|
| compliance 检查2 全部子项（所述/优选/单句号/多引链/标记限定） | **C**（该文件职责就是合规，位置正确但应在瘦身时明确"仅申请轨触发"） |
| compliance 检查1/3/4/5/6 | **A**（支撑链/标题图号一致/公式溯源=质量检查） |
| filing 补正"删除不改动/不得超范围"、3 年实审期限、缴费期限 | **B/C**（递交阶段一次性提示，位置合理） |
| drawings 实用新型必须结构图、黑白线条 | **C**（但作为阻断器保留一句即可） |
| intake interview F 组公开状态两问、source-modes 公开状态 flag | **B**（一次性风险决策，现形态已是"记录+指针"，正确） |
| intake type-decision 一案两请 | **B**（一次性决策提示，正确） |
| claim-language.md 整文件 | **C**（产品词→专利词转换表 + 常见错误表；服务权利要求书语言，属形式规则集 → 后移或标注"仅 Part A 使用"） |

---

## 3. 法律腔根源分析

**判定原则**: "所述/其特征在于"句式在**权利要求书**中合法且必要（污染=无）；在**说明书叙事段、技术交底书、访谈记录**中出现即为法律腔蔓延。

### 根源 1（最强）：patent-drafting/SKILL.md A2 的句式模板被默认为全局文体
- A2 (:37-52) 把"包括…;其特征在于:…"定为独权格式——这对权利要求书是对的。但该 skill 同时负责说明书（Part B），且 B3 要求"expand the independent claim into paragraphs (feature-by-feature correspondence)"。模型执行时极易把权利要求的"所述X"链条原样展开进发明内容和实施例叙述段，产生"所述图像采集模块…所述识别模块…"式说明书。
- **证据链**: B3 的 feature-by-feature 展开指令 + A5 术语一致性检查要求"claims write 传感器 → specification must not write 感应器"——一致性检查只约束术语映射，没有反向豁免条款告诉模型"说明书叙事段不必使用所述句式"。缺口在此。
- **claim-language.md 加剧**: 词表标题是 "The inventor says → The claim writes"，作用域本应是权利要求书；但 source-modes.md 的 语言纯度 flag 写的是 "terminology regularization before claims (conversion table in `../../patent-drafting/SKILL.md`)"，指向含糊，模型可能在交底书组装阶段就提前做"专利腔转换"。
- **对照（已有的正确设计）**: disclosure-document.md 双轨表明确"statutory openings never apply here"、"照抄，不套法定句式"（技术领域行）。这说明设计者已经意识到问题并做了隔离——但该隔离只在**交底书轨**生效；**说明书叙述段（B3 发明内容、B5 实施例）没有任何对应豁免**。

### 根源 2：compliance 检查2 对说明书正文无差别扫描
- 检查2 列出 `undefined "所述" terms` 等权利要求检查项，但未显式声明这些只适用于 权利要求书.md。若模型把"说明书里出现未定义的'所述'"也当 critical 报出，会反过来倒逼起草者在说明书里补全所有"所述"先行词——法律腔被检查器制度化。

### 根源 3（轻微）：B1 的法定开头句示范
- "本发明涉及…技术领域,特别涉及…"作为 Done 条件给出，说明书第一段从第一句起就是法定腔。影响小（该段本来就该简短），但对发明人阅读体验是第一印象。

### 明确不是根源的部分
- interview.md、design-points.md、type-decision.md、search-guide.md：全程发明人语言，无句式传染。
- disclosure-document.md：唯一在文档级禁止法定腔的文件（"不套法定句式"），是正面样板。
- conversion/word-delivery：零法律腔风险（word-delivery 的硬约束全是工程纪律）。

---

## 4. 瘦身处置清单

档位：**删除 / 后移到 professional（或递交前）/ 压缩为一句提示 / 保留**

### self-service/patent-drafting/

| 目标 | 处置 | 具体动作 |
|---|---|---|
| SKILL.md A2 句式模板块 | **压缩为一句提示** | 保留一行模板代码块 + "句式细节见 compliance 检查2"；删去 preamble/characterizing 的逐条解释段 |
| SKILL.md A4 引用规则 4 条 | **后移** | 移入 compliance 检查2（或 filing 补正常见项表，已有对应行）；SKILL.md 只留一句"从权只能引用在前权利要求，详见自检" |
| SKILL.md A5 八项表 | **拆分** | "Terms consistent with the specification" 一条保留（A 类）；其余 7 条（所述先行、如图、括号标记、引导词、营销语、单句号、主题名一致）**后移** compliance，正文换成一句"写完跑一遍 compliance 检查2" |
| SKILL.md B1 法定开头 | **压缩为一句提示** | 降为例句，不作 Done 条件 |
| SKILL.md B6 300 字法规历史注 | **删除** | "2023 Implementing Regulations removed the cap" 是无人需要的立法史 |
| SKILL.md B2 三来源分类学 | **压缩为一句提示** | 保留诚实红线的本质："背景技术每个事实都要能回答出处；编造专利号/文献=红线"。三类材料的分类框架随红线一并压缩 |
| references/claim-language.md 整文件 | **后移 + 重新标注作用域** | 文件本身保留在 drafting 下可接受，但需加显式头注"本表仅适用于权利要求书.md；交底书与说明书叙事段禁止使用本表改写发明人语言"；或整目录后移交 professional 组 |
| 新增建议 | **新增一句豁免** | 在 B3/B5 加一条："说明书发明内容与实施例按自然技术散文书写，仅在指代已有部件时可用'所述'；禁止把权利要求句式复制为叙事段落"——这是根治法律腔的最小补丁 |
| A1/A3/B3/B5/修订循环/完成标准中的工艺项 | **保留** | 删除测试、概括阶梯、三方对应、公式门、支撑链闭环、充分公开五要素——全部是内容质量本体 |

### self-service/patent-intake/

| 目标 | 处置 | 具体动作 |
|---|---|---|
| SKILL.md 整体 | **保留** | 已是低密度；"no statutory text copied here" 纪律声明保留 |
| references/interview.md F 组 | **保留** | 公开状态两问 = B 类一次性风险决策，现形态（记录+指针+不贴法条）正确 |
| references/source-modes.md 五 flags | **保留** | B 类决策入口，形态正确 |
| references/source-modes.md 语言纯度 flag 的指向 | **修改一句** | 明确"regularization 仅用于权利要求书，交底书保留发明人语言"，切断提前专利腔转换 |
| references/disclosure-document.md 双轨表 | **保留** | 抗浸透的结构性资产；可把"不套法定句式"从技术领域一行提升为 assembly rules 总则 |
| references/type-decision.md、search-guide.md、design-points.md | **保留** | 低/零法律触点 |

### self-service/patent-drawings/

| 目标 | 处置 | 具体动作 |
|---|---|---|
| 实用新型必须结构图（mandatory items 节） | **压缩为一句提示** | 一句话保留（它是交付阻断器，不能删）；细则依据不留 |
| 黑白线条/无色彩/括号标记惯例 | **压缩为一句提示** | 合并为图检一行"黑白线条、标记加括号（CNIPA 惯例）" |
| Step 1-5 工作流、横版布局、双向核对 | **保留** | 全部是写作/绘图工艺 |

### self-service/patent-compliance/

| 目标 | 处置 | 具体动作 |
|---|---|---|
| 检查2 | **保留 + 收窄作用域** | 该文件是 C 类规则的正确归宿（承接 drafting 后移项）；须加一句"检查2 各项仅扫描 权利要求书.md，不适用于说明书/交底书正文" |
| 检查1/3/4/5/6、补正检查 | **保留** | A 类质量检查 |
| 整文件触发条件 | **新增** | 明确"仅申请轨（filing set）路由触发；交底书轨跳过本 skill"（intake 已有此意，此处宜自查声明） |

### self-service/patent-filing/

| 目标 | 处置 | 具体动作 |
|---|---|---|
| 补正协议、期限、费用表 | **保留** | 递交阶段职责所在；且文件已自带"金额以官方系统为准"免责 |
| 常见补正项表 | **保留**（作为 C 类规则的接收端） | drafting A4/A5 后移时可并入此表的 Claim format 行 |

### tools/ 与 patent-standards/

| 目标 | 处置 |
|---|---|
| conversion/SKILL.md | **保留**（零法律内容） |
| word-delivery/SKILL.md | **保留**（硬约束为工程纪律；"statutory one-document structure"一处措辞可中性化为"CNIPA 分文件结构"） |
| patent-standards/ 全部 | **保留**（锚点库 + on-demand 指针模式正是设计方向的实现，自助组正文已做到"给指针不贴法条"） |

---

## 最重要发现 Top 5

1. **浸透并非全局性，而是集中在 patent-drafting/SKILL.md 的 Part A（约 60 行）**。intake 全组已被"规则双轨"挡住（disclosure-document.md 明确"statutory openings never apply here"），standards 采用 on-demand 指针。瘦身主战场只有一个文件。

2. **法律腔的真正根源是一个缺口而非一条规则**：A2 把"其特征在于"句式定为独权格式（合理），B3 又要求把独权 feature-by-feature 展开进说明书，但**全文没有一句豁免告诉模型"说明书叙事段不必沿用权利要求句式"**；claim-language.md 的转换表作用域未标注，配合 source-modes 的"语言纯度"flag 可能提前污染交底书。最小补丁 = 在 B3/B5 和 claim-language.md 头部各加一句作用域声明。

3. **compliance 检查2 有把法律腔制度化的风险**：其"所述先行词"等检查项未声明仅适用权利要求书，若扫到说明书正文会倒逼叙事段补全"所述"。收窄作用域比删除更重要。

4. **A5 八项清晰度表和 A4 四条引用规则是最典型的可后移 C 类资产**（合计约 40 行细则复述）；compliance 检查2 与 filing 补正表已经是它们现成的接收端，后移成本极低。drafting 正文各留一句指针即可。

5. **B 类风险决策（公开状态/宽限期/一案两请）现状已接近目标形态**：interview F 组 + source-modes 五 flags 都是"一次提问 + 记录 + 法条指针"，不贴解释。这部分不需要动；反而要防止瘦身时误伤。另有一处纯垃圾可立即删：B6 的"2023 细则取消了 300 字上限"立法史注释。
