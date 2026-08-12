# Skills 有效性审查报告(2026)

> 审查对象:`skills/` 下六个技能是否满足实际专利编写业务。
> 审查方式:通读全部 SKILL.md 与支撑文件 + 对关键断言做可查证验证(下节)。
> 结论先行:**架构是干净的(委托检索、fail loud、目录引用),内容层是流程脚手架,不是专利撰写专业能力。** 最致命的证据是包自己的教学样例编造现有技术。

---

## 1. 验证记录(非印象流,可复现)

### 1.1 `patent-architect/examples.md` 的检索结果表是编造的

示例"Focus Period Recommendation System"的"检索结果"表格宣称三个真实专利号,逐号在 Google Patents 上查证(2026-08-11):

| 示例声称 | 实际标题(google patents) | 判定 |
|---|---|---|
| US10234567B2 "Calendar-based Task Scheduling System" | Location awareness apparatus, vehicle having the same and method for controlling the apparatus | **张冠李戴** |
| US9876543A1 "Context-Aware Notification System" | —(HTTP 404) | **不存在** |
| CN111222333A "智能日程推荐方法及装置" | 基于网络高阶结构与主题模型融合的关键词抽取方法 | **张冠李戴** |

影响:该文件是全包的教学范本,模型模仿的"高质量输出"本身就是编造品。它示范的正是包的第一戒律("never invent prior art")所禁止的行为;连同"检索结果分析"里"最接近的现有技术"整段论证,全部建立在虚构专利之上。**无论初衷是不是"示意",它都在教模型造假。**

### 1.2 `patent-claims-analyzer` 实测

用一段简单英文权利要求(1条独权+1条从权)运行 `python/claims_analyzer.py`:

- 能正确抓到真实的引用基础问题("the threshold" 未先行引入)— 作为 **lint 有价值**;
- 头词归一化粗糙("the stored instructions" 以 "stored" 为头词,建议语"Introduce 'stored' with 'a/an'" 无意义);
- 不看说明书,对 "substantially" 无条件报"important" — 而 MPEP 2173.05(b) 明确承认该词在说明书给出指引时可接受,存在系统性误报;
- 纯英文,对中文权利要求(本包主要市场)完全无效;
- "compliance_score" 是 100 减加权扣分的伪精度数字,无法律含义;
- `mpep_cite` 是**硬编码字符串**,不是检索结果;SKILL 声称"环境读不到 MPEP 就标 ungrounded",但分析器没有任何机制知道 MPEP 是否被读过,该标记永远不会触发。

### 1.3 工具链缺口(检索管道在声明层面即死)

- 本机无 `VALYU_API_KEY`、无 `~/.valyu/config.json` → `patents-search` 必然返回 setup_required;
- `patent-architect` 的 `allowed-tools` 为 Read/Grep/Glob/Write/Edit/AskUserQuestion — **无 Bash、无 web 工具**,在声明层面就跑不了检索脚本、也读不了目录声明的法条材料;
- `patent-architect` 模板要求"检索式"(布尔式),唯一脚本是 Valyu 语义搜索(自然语言),格式不匹配;`reference.md` 文档化的 SerpAPI / Exa 两个 API 无脚本、无 key 管理,是装饰性内容;
- 真实检索必需的 IPC/CPC 分类、引证链、同族、申请人检索:全部缺席。

### 1.4 standards-catalog 抽查

CNIPA 局令78号页、gov.cn 令769号页、USPTO MPEP index 抽查均 200,版本事实(2023 专利法修订、实施细则 国务院令769号、审查指南 局令78号,均 2024-01-20 生效;MPEP 9th Ed. Rev. 01.2024)核对无误。

**这是全包最扎实的一份资产,但它是"声明",不是"内容"** — 锚点停留在章级("指南 第二部分第四章"),没有节级锚点,也没有任何技能消费它去读原文。

---

## 2. 逐技能评估

| 技能 | 实际价值 | 空洞点 |
|---|---|---|
| patent-standards | 高(事实准、URL 可验证) | 只有目录,没有规则内容;章级锚点太粗,引用无法验证精度;没有消费机制 |
| patent-architect (CN 旗舰) | 低 | **无权利要求书**(模板=提案书/交底书,不是申请文件);检索分析是内部底稿却混入"申请文件";3 实施例=维度置换注水;检索式与工具脱节;allowed-tools 跑不了检索 |
| patent-application-creator (US) | 低 | 流程日程表而非技能;claims 指导是 boilerplate,无 101 (Alice/Mayo) 策略(美国最大驳回杀手);质量门全是数量("20+页""10-20条") |
| patent-claims-analyzer | 中(仅英文 lint) | 玩具级:硬编码 MPEP 标签、不看说明书、英文 only、伪精度分数;对 CN 无用 |
| patent-diagram-generator | 中(诚实的 Graphviz 包装) | 只加参考数字约定;无摘要附图指定、无 CN/US 附图形式要求自动化、无"附图标记与文字一致性"检查(实际最痛的补正项) |
| patents-search | 低-中(薄包装) | 依赖第三方 $10 服务+key;语义检索不能替代分类/引证/同族检索;对 CN 专利覆盖与中文查询质量未验证 |

---

## 3. 根因分析(为什么"看起来很充实")

1. **内容 = 过程清单,不是专业知识**。技能的骨架是"先 X 再 Y 再 Z"的流程 + 数量指标(3 实施例、10-20 从权、20+页、Top 10 专利)。数量可以注水,所以输出"看起来很多"。真正值钱的判断逻辑缺席:创造性三步法的操作化、权利要求上位化/概括边界、公开充分与支持、从权布防、OA 答复论证。
2. **grounding 是表演**。declare/consume/cite/fail-loud 契约架构正确,但:无检索工具(1.3)、无内容可消费(章级锚点)、fail-loud 无触发机制(模型永远"有答案")。输出要求(背景技术必须引用现有技术)与 fail-loud(拿不到就停)自相矛盾,模型解决冲突的唯一出路是编造或默认用户放弃验证 — examples.md 已证明走了编造那条路。
3. **产出物与业务目标错位**。旗舰技能产出"专利申请表"里没有权利要求书,还混入永远不会进申请文件的检索底稿;US 技能与 CN 主体市场错配;业务主循环(OA 答复、修改、超范围、挖掘、策略)整体缺失。
4. **示例教学污染**。examples.md 是模型的模仿范本,而它展示的检索表是编造的 — 等于把违规行为写进了行为规范。

---

## 4. 修复建议(按优先级)

1. **[P0] 处理伪造样例**:删或重写 `examples.md` 检索结果表;真实检索前不得展示专利号;或明确标注为"示意格式,非真实检索结果"并去除具体公开号。
2. **[P0] 给 patent-architect 补权利要求书**:加入 独权/从权 生成 + 创造性三步法分析逻辑;把"检索式"表改为与语义检索匹配的真实输出格式;把"专利申请表"正名为"提案书(交底书)"或补齐申请文件结构。
3. **[P1] 新增审查意见答复(OA)技能**:三步法论证、修改权利要求策略、修改超范围判断 — 业务价值密度最高,目前空白。
4. **[P1] 修正 grounding 执行机制**:要么环境真正挂一个检索/读法条工具,要么把"未读"如实标记为 ungrounded;补节级锚点;删除"放弃验证"这种让模型自我豁免的条款。
5. **[P2] claims-analyzer 重定位**:降级为"英文权利要求结构 lint"并声明边界,或加中文支持(指南 第二部分第二章 清楚性规则)。
6. **[P2] diagram-generator 补 CN 形式要求**:摘要附图指定、附图标记一致性检查。

---

## 5. 保留资产

- standards-catalog:事实准确、URL 可验证 — 深化方向:节级锚点 + 把三步法/权利要求规则的实际内容接进来。
- 委托契约(fail-loud/不编造):架构正确 — 缺执行机制,见 4.4。
- diagram-generator:诚实包装,没装腔作势。

---

## 6. 方向决定与实施(2026-08-11)

用户拍板并已实施:`ADR-0004`(self-service-first,类别布局)。要点:

- **定位**:发明人/非专业人士自助申请向导,发明+实用新型,全流程(交底→类型判断→撰写→自检→递交与补正)。实审 OA 答复不在本包。
- **分组**:按 skills.sh 类别目录 `skills/<category>/<name>/`,参考 mattpocock/skills 的 user-invoked 入口 + model-invoked discipline 依赖化层级化。
- **已删除**:`patent-architect`(被取代 + 伪造样例)、`patent-diagram-generator`(重做为 patent-drawings)。
- **已隐藏**:US 两技能移至 `skills/professional/`,`disable-model-invocation` 不参与发现,待 A 方向重做。
- **新技能**:`patent-application`(入口)+ `patent-claims` / `patent-specification` / `patent-drawings` / `patent-compliance` / `patent-filing`。
- **实测 grounding**:2023 实施细则全文 + 专利法 2020 文本条文号经 CNIPA 官方全文核实,写入 patent-standards 的 Verified rule anchors 节;发现 2023 版已删摘要 300 字限制。
