# 模式 D（审查答复案例 RAG）— 吸收评估报告

> 用途：为未来 A 组（专业代理人，`skills/en/professional/`）的「审查意见答复（OA 答复）」技能提供事实依据——评估外部仓库 patent-disclosure-skill 的**模式 D** 提供什么、与本包委托优先/薄技能哲学冲突什么。对应 ADR-0005 决策 6（OA 归档为 professional/ 方向参考）。
> 方法：**以外部仓库源码为准**（非其 README）；只读评估，未移植任何代码。源提交 `ff43eb7`（2026-08-12 本地克隆，与 ADR-0005 同源同提交）。对照对象：本包 ADR-0003（delegation-first）、ADR-0004（self-service 包定位、A 组未来接入）、ADR-0005（零脚本收编纪律）、CONTEXT.md 词表（Delegated search / Thin skill / Grounded output / Fail loud / Declared external source / Document-only capability / Archived reference / `.patent/`）、`docs/prototype/delegation-contract.md`。
> 评估日期：**2026-08-13**。

## 结论速览

- **模式 D 是什么**：一个默认关闭、显式触发、须人审的「审查答复辅助」旁路。两条半流程——(a) 历史通知书/答复**脱敏入库**成案例笔记 + 可选向量库；(b) 通知书 PDF → 抽取 → 结构化 → **自建案例库检索**（标签过滤 + 可选向量 Top-K）→ 策略勾选 → 逐条答复草稿 → 人审闸门。
- **可复用**：工作流纪律（PDF-first、先检索再生成、逐条对应、空库禁糊弄、人审闸门、脱敏）、案例笔记合同（`oa_case.schema.yaml` 的分类法：statutes / defect_types / strategy / outcome / compare_refs）、五条 guardrails、案例笔记中**隐含**的创造性反驳模板（确认区别特征 → 功能相互支持/非简单叠加 → 说明书出处 → 效果论证）。
- **冲突**：① 整套**自建检索基建**（sqlite-vec + embedding 客户端 + Obsidian 语料管线，`tools/oa/` 共 3,341 行 Python / 144 KB）——正是 ADR-0003 否决的形态；② **API Key 管理**（`config.py`，850 行，`embedding.secrets.yaml`）——ADR-0003「never manages keys」；③ **零脚本**纪律（ADR-0005 决策 1 与线稿工具否决先例）；④ 语料耦合 Obsidian 库结构 + sqlite DB，与本包 `.patent/` 纯目录工作区不相容；⑤ **三步法并未被编码**（全仓 grep「三步法」= 0 命中）——论证逻辑仅以案例模板隐式存在，A 组须从 `patent-standards` 锚点（指南 第二部分第四章）重建。
- **吸收形态建议**：纯文档纪律收编进 `skills/en/professional/` 新技能（OA 答复），检索环节改写成「用户提供的脱敏案例档案（目录）+ 环境自带检索能力」，零脚本零密钥；三步法论证从本包 standards 锚点构建。

---

## 一、来源与边界

- 外部仓库：`/tmp/patent-disclosure-skill`（handsomestWei/patent-disclosure-skill，MIT，`LICENSE` 全文 MIT，Copyright (c) 2026 handsomestWei），HEAD = `ff43eb798c3fbde5fd22a532aed8fb62930851ce`。
- 模式 D 子集（本报告只评估这部分）：`prompts/oa/`（6 个 md，约 11 KB）、`tools/oa/`（12 个 Python 文件 + `requirements-oa.txt`，共 3,341 行 / 144 KB）、`docs/oa/`（配置模板种子）、`examples/example_oa_response/`（冒烟样例）、`tests/oa/test_oa_store.py`（422 行，9 个测试类）、`references/schemas/oa_case.schema.yaml`（案例笔记合同）。合计 30 个文件。
- 与本包边界：外部仓库整体（211 文件、4 模式、~60 个 Python 工具）曾按 ADR-0005 评估；**转换能力**（模式 A 附带的 5 个转换脚本）已纯文档化收编，**OA 模式 D** 当时仅归档为 professional/ 参考、未评估。本报告补上这一评估。

## 二、模式 D 全貌：输入 → 检索 → 论证 → 输出

### 2.1 定位与触发

- 旁路，**默认关**，须显式触发：`SKILL.md:19`「D · 审查答复辅助 | 案例脱敏入库；通知书 → 标签+向量检索 → 答复草稿 | `prompts/oa/`（**默认关**；须人审）」；`SKILL.md:69` 触发词「审查意见、意见陈述、OA、补正通知书、案例入库、`/oa`、`/审查答复` → **仅此时**进入模式 D」；`SKILL.md:223` 自检清单「模式 D：已显式触发」。
- 产出定位为**草稿**：`prompts/oa/guardrails.md` 定位节「**不**替代专利代理签字与正式递交；产出为草稿」。
- 主流程（`SKILL.md:187-198`）：① Read `guardrails.md` → `intake.md`；② 首次/改向量：`configure_embedding.md` 对话问清 → `config.py`（selftest）→ 人确认后 `rebuild_vectors.py --confirm`；③ 入库 `ingest_case.py`（支持 `--pdf`）；④ 答复 `search_cases.py --pdf` → 策略勾选 → 草稿 → 人审；⑤ 仅刷新 Obs：`refresh_vault.py`。

### 2.2 输入（PDF-first，禁止手贴）

`prompts/oa/respond_office_action.md:7`「**审查意见通知书 / 补正通知书 PDF**（用户给路径即可）」；可选：本申请权要/说明书 PDF、专利类型、已知法条/缺陷标签。工具层强制自动抽取：`pdf_text.py`（158 行，pymupdf）「优先路径，禁止让用户手贴」（`SKILL.md:141`）；扫描件几乎无字时 `WARN extracted_text_too_short`，告知用户换可复制文字的 PDF 或先 OCR，「**仍不要**让用户手抄通知书」（`respond_office_action.md:26-28`）。

### 2.3 检索：自建案例语料库（核心冲突点，详见第三节）

检索**必须**先做（`respond_office_action.md:40`「### 2. 检索（必做）」），但对准的是**技能自建的案例库**，不是任何外部委托源：

- 语料 = 用户所在机构**历史 OA 案**，经 `ingest_case.py` 脱敏后写入 Obsidian 笔记（`{vault}/oa/cases/history/`，方案 C，`ingest_case.md:40-47`）+ sqlite-vec 向量库（`{Documents}/…/oa/data/oa_vectors.sqlite`）。
- 检索 = `search_cases.py`（205 行）：标签/字段过滤（statutes / defect_types / patent_type / domain / tags）优先，向量可用时再 Top-K，超时/失败自动回退标签（`search_cases.py` 的 `mode`：`vector` / `tags_only` / `tags_fallback`；`SKILL.md:59`「标签检索始终可用，向量超时则回退」）。
- 检索实现：`tools/oa/store.py:294` `def search`「先元数据过滤；有向量则 KNN，否则标签检索」；`store.py:255` `search_by_tags` 纯标签路径；`store.py:36` `init_db` 建 sqlite-vec 表（`store.py:30` 依赖 `pip install -r tools/oa/requirements-oa.txt`，内含 `sqlite-vec>=0.1.6`、`numpy`、`pymupdf`、可选 `sentence-transformers`）。
- 向量：`tools/oa/embed.py:34` `class Embedder`（多厂商适配：zhipu / dashscope / minimax / local / openai，`embed.py` docstring「多厂商适配（可选；失败可回退标签检索）」）；配置与密钥由 `config.py`（850 行）管理（`docs/oa/embedding.config.yaml` 模板种子：`api_key_env: ZHIPUAI_API_KEY`、`base_url: https://open.bigmodel.cn/api/paas/v4`；密钥落 `embedding.secrets.yaml`「仅本机」）。
- 案例入库 / 重建 / 刷新配套：`ingest_case.py`（369 行）、`rebuild_vectors.py`（168 行）、`refresh_vault.py`（55 行）、`vault_layout.py`（759 行，Obsidian 目录布局 + `_OA索引` / `_OA看板.base` / `_OA关联.canvas` 生成）、`case_md.py`（82 行，frontmatter 解析 + `chunk_case` 分块）、`redact.py`（62 行，规则型脱敏：公司名/申请号正则，入库前仍须人审）。

### 2.4 结构化解析与论证逻辑

`respond_office_action.md:30-37` 步骤 1 结构化解析：从抽取文本抽 `notice_kind`、答复期限、逐条缺陷（法条/审查员观点/对比文件号）、`defect_types`、`statutes`、`patent_type`、`domain`（推断须标注），可落 `outputs/oa/{案件}/notice_struct.yaml`。

论证逻辑（关键事实）：**「三步法」未以任何命名形式编码**——全仓 `grep -rn "三步法"` = 0 命中（含 `prompts/oa/`、`references/`、`examples/`）。创造性答复的论证只以**案例模板正文**隐式存在，可抽象为四步：① 确认审查员认定的区别特征是否属实；② 论证功能相互支持、非简单叠加（对应三步法的第二步「是否显而易见」）；③ 修改特征须指向说明书出处（或标「待指认段落」）；④ 强调组合带来的效果（含预料不到的效果，谨慎使用）。证据：
- `prompts/oa/case_note_template.md:33-37`（示例案）：「审查员认为权利要求1相对于对比文件1与公知常识的结合不具备创造性，认为区别技术特征仅为常规结构替换」「将说明书中记载的「限位配合 + 导向斜面」组合特征并入权利要求1；意见陈述中强调该组合解决的装配误差与卡滞问题及预料不到的效果」。
- `examples/example_oa_response/cases/history/hist-inventiveness-clamp.md` 陈述要点：「1. 对比文件1仅公开弹性卡扣，未公开限位凸起与导向斜面的组合。2. 二者功能相互支持，非简单叠加。3. 修改特征来自原说明书（示例：待指认段落）」。
- 清楚性案例 `hist-clarity-connector.md`：不修改权利要求，用说明书实施例 + 附图标记解释权利要求用语。

### 2.5 策略与输出

- `respond_office_action.md:58` 步骤 3 策略选项（人勾选）：至少给出「仅意见陈述 / 修改权利要求 / 修改说明书 / 补正形式」；附**超范围风险提示**（`guardrails.md:16`「修改超原申请记载范围却不标注风险」禁止项）。
- `respond_office_action.md:62-68` 步骤 4 草稿约束：**逐条**对应通知书条目编号；引用命中案例写 `case_id` + 为何可参考 + **差异**（`search_cases.py` 的 `diff_fields` 对每个 hit 输出 domain/statutes/defect_types/patent_type 差异）；每处修改须指向说明书可支持位置（未知则标「待发明人指认段落」）；落盘 `outputs/oa/{案件或日期}/意见陈述草稿_{时间戳}.md`（gitignore）。
- `respond_office_action.md:69` 步骤 5 人审闸门（`guardrails.md` 确认话术：「以下为审查答复【草稿】，须代理人/发明人复核后再递交」）。

### 2.6 冒烟样例与测试

- `examples/example_oa_response/`：README + `cases/history/` 两篇脱敏历史案（创造性卡扣、清楚性连接器）+ `pending/oa_notice_pending.md` 待答复通知书，可用于冒烟「入库 → 标签/向量检索 → 答复草稿」（README 给出完整命令序列）。
- `tests/oa/test_oa_store.py`（422 行，9 个测试类）：`RedactTests`、`CaseMdTests`、`StoreVecTests`、`TagOnlySearchTests`、`ConfigTests`、`EmbedderVendorTests`、`PdfExtractTests`、`SecretsAndSelftestTests`、`VaultLayoutTests`——覆盖入库 round-trip、标签检索、向量检索、配置/密钥/自检、PDF 抽取、脱敏。

## 三、核心冲突：自建案例 RAG vs 委托检索

### 3.1 逐条对照本包约束

| 模式 D 事实 | 本包约束（来源） | 判定 |
|---|---|---|
| 自建案例语料库 + 检索 harness：Obsidian 语料（`ingest_case.py` / `vault_layout.py`）+ sqlite-vec KNN（`store.py`）+ embedding 客户端（`embed.py`）+ 重建/刷新管线（`rebuild_vectors.py` / `refresh_vault.py`），`tools/oa/` 共 3,341 行 Python | ADR-0003「The set never builds a search tool and never manages keys」；CONTEXT.md「Delegated search」Avoid: in-repo harness, 自建搜索 | **冲突**——形态上是完整 in-repo 检索基建。注意一个**边界澄清**：语料是机构自己的历史 OA 案（内部分类知识），不是外部专利库/法条（委托检索管的那类外部知识）；但本包判据看的是**形态**：任何「自己建库、自己检索、自己管键」的脚本堆都不入包 |
| `config.py`（850 行）管理 embedding 厂商/模型/API Key（`docs/oa/embedding.config.yaml`、`embedding.secrets.yaml`；`SKILL.md:59` 推荐智谱 embedding-3） | ADR-0003「never manages keys」；CONTEXT.md「Delegated search」never declares which backend is core | **冲突**——选厂商 + 管密钥正是 ADR-0003 移交给环境的职责 |
| 10 个 Python 工具随包分发（`tools/oa/*.py`），`requirements-oa.txt` 声明 sqlite-vec/numpy/pymupdf/sentence-transformers | ADR-0005 决策 1「纯文档技能（零脚本零依赖）」；决策 5 线稿工具「不引入（零脚本决策）」；CONTEXT.md「Document-only capability」no script is committed to the package | **冲突**——违反零脚本纪律。注意先例：本包 `skills/en/professional/patent-claims-analyzer-us/` 现存一个隐藏的 `python/claims_analyzer.py`（11.4 KB），但 `disable-model-invocation: true` + `metadata.internal: true`，SKILL.md 标注「To be redone when the A direction restarts」——即保留的 A 组资产也只允许**隔离 + 标记重做**，不是脚本化常态 |
| 语料落 Obsidian 库结构（`_OA索引.md` / `.base` / `.canvas`）+ sqlite DB | CONTEXT.md「`.patent/` workspace」：`sources/`、`materials/`、`queries/` 纯目录分档，无库/DB 假设 | **冲突**（轻）——方案 C 的 Obsidian 耦合与本包工作区约定不同构；案例档案可平移到 `.patent/` 类目录（见第六节） |
| 模式 D 的检索只针对**自有案例库**；外部查新仍走模式 A 的 `tools/crawl/cnipa_epub_search.py`（`SKILL.md:73`） | ADR-0005 决策 3：CNIPA 公布公告系统 = 人工操作的外部声明源，「零代码，不移植爬虫（自建检索禁区）」 | 模式 D 本身无爬虫；但**同一仓库的检索哲学**含爬虫（`tools/crawl/cnipa_epub_crawler.py` 13.5 KB / `cnipa_epub_search.py` 5.4 KB），吸收时须只取 OA 纪律、不连带抓取工具 |
| 空库时禁止糊弄：`respond_office_action.md`「库为空：仅输出提纲 + 策略选项，禁止假装引用历史案」；`guardrails.md:15`「无检索命中（或未说明库为空）就长篇「糊弄」意见陈述」 | CONTEXT.md「Fail loud」；delegation-contract.md 第 4 条 | **对齐**——模式 D 已有本包 fail-loud 的同构纪律，是可复用资产 |
| 命中案例须带 `case_id` + 差异 + 为何可参考 | delegation-contract.md 第 3 条 cite 纪律；「Grounded output」每个先有技术引用指向真实检索结果 | **对齐**（需改锚点格式）——模式 D 要求引用命中案例并展示差异，与本包「每个断言带出处」一致；引用对象从「检索结果」换成「案例档案条目」即可 |

### 3.2 边界澄清（避免误判）

「自建检索禁区」的语义要拆开看：

1. **外部知识检索（先有技术、法条）**——本包绝对禁区：必须委托（ADR-0003）。模式 D 不碰这块（它不查外部专利库）。
2. **内部知识检索（机构历史 OA 案）**——模式 D 干的事。本包词表没有直接禁止「检索用户自己的资料」：delegation-contract.md 第 3 条明确「User-supplied grounding counts: (provided: <file or patent number>)」。所以**功能上**「检索历史案例」不违禁区；**形态上**违——模式 D 用 3.3K 行脚本 + 向量库 + 密钥管理来实现它，而不是「代理用环境工具读用户给的档案目录」。

结论：冲突不在「能不能检索案例」，而在「**包要不要自建检索基建**」。A 组吸收时，案例检索应降级为环境能力（Grep/Read/知识库工具扫 `.patent/` 类目录），包内零脚本。

## 四、可复用资产（纪律层，非脚本层）

### 4.1 工作流纪律（直接可写成 SKILL.md + 提示词）

1. **PDF-first 摄入**：通知书 PDF 自动抽取，禁止让用户手贴/手抄（`respond_office_action.md:7,26-28`；`pdf_text.py` 用 pymupdf 只读抽取——这是「Document-only capability」式的环境探测，可保留为文档描述，不随包带脚本）。
2. **先检索再生成**：检索是必做步骤（`respond_office_action.md:40`），无命中禁糊弄（空库只出提纲 + 策略选项）。
3. **结构化解析**：通知书 → `notice_kind` / 期限 / 逐条缺陷（法条、审查员观点、对比文件号）/ `defect_types` / `statutes`（推断须标注），可落 notice_struct。
4. **逐条对应**：草稿按通知书条目编号逐条答复（`respond_office_action.md:64`）。
5. **策略选项 + 超范围风险标注**：仅意见陈述 / 改权利要求 / 改说明书 / 补正；每处修改须指向说明书支持位置，未知标「待发明人指认段落」。
6. **人审闸门**：草稿 ≠ 已递交；确认话术固定（`guardrails.md`）。
7. **脱敏先于入库**：客户名/电话/未公开参数，入库前脱敏 + 人审（`redact.py` 是规则型辅助，纪律是「人审」本身）。

### 4.2 案例笔记合同（`references/schemas/oa_case.schema.yaml`）

结构化 frontmatter 分类法可直接复用作 A 组「案例档案」格式：`case_id` / `status`（history | pending | draft）/ `patent_type` / `statutes` / `defect_types`（novelty | inventiveness | clarity | support | disclosure | formality | other）/ `domain` / `notice_kind` / `outcome`（granted | rejected | pending | amended_then_granted | …）/ `strategy`（argue_only | amend_claims | amend_spec | correction | other）/ `compare_refs` / `related_cases` / `redacted` / `tags`。正文建议结构：通知书要点 → 策略 → 陈述要点 → 修改摘要 → 结果 → 关联案 → 对比文件。

### 4.3 隐含论证模板（需升级为显式三步法）

案例模板中的创造性答复论证（确认区别特征 → 功能相互支持 → 说明书出处 → 效果）是**三/四步法论证的胚子**，但未命名、未锚定法条。A 组吸收时应把它显式化为「指南 第二部分第四章[创造性·三步法]」支撑的论证纪律——本包 `skills/en/patent-standards/references/cn-invention-utility.md:41` 已锚定「第二部分第四章 | inventive step (three-step method)」，法条锚点（专利法 第22条第3款）也已就位。**论证纪律从本包 standards 重建，不从模式 D 导入**。

### 4.4 对齐点小结（模式 D 与包哲学一致的机制）

- Fail loud 同构：空库禁糊弄。
- 人审闸门：草稿 ≠ 递交。
- 诚实红线同构：引用命中案例须带差异，不得无检索空写（`oa_case.schema.yaml`「生成答复须引用命中案例并展示差异；不得无检索空写」）。
- 脱敏纪律：先于入库、人审确认。

## 五、模式 D 不提供什么（A 组要自己补的）

1. **三步法本身**：全仓 0 命中「三步法」；论证只是案例模板的隐式惯例。
2. **法条 grounding**：案例笔记把法条当标签写（如 `专利法第22条第3款`），但没有「对照声明源核实条文」机制——本包 patent-standards 锚点 + delegation-contract 的 declare/consume/cite 补上这块。
3. **claim 修改策略引擎**：`strategy` 只是枚举，没有「布防三方向（细化/变体/增强）」式的修改决策逻辑（本包 self-service 词表已有「退路」概念可升级）。
4. **引用格式**：模式 D 的 `case_id` 引用不能直接进答复正文；按 delegation-contract 第 3 条，A 组输出须用本包 citation convention（条号即锚点 + 出处）。

## 六、吸收形态建议（professional/ A 组）

以 **纯文档纪律** 收编为 `skills/en/professional/` 新技能（例：`patent-oa-response`），与 ADR-0005 决策 6「归档为 professional/ 方向参考」接续，落地四件事：

1. **工作流 SKILL.md + 提示词**：模式 A 的 intake → 结构化解析 → 先检索再生成 → 逐条草稿 → 人审闸门，写成 `prompts` 式纪律文档（沿用本包 `prompts/oa/*.md` 的编排结构，语言英文化）。
2. **案例档案 = 用户提供的目录**：历史 OA 案按 `.patent/` 约定存放（如 `.patent/cases/history/`），格式采用 `oa_case.schema.yaml` 的 frontmatter 合同（可英文化、加本包 citation convention 字段）；**检索 = 环境能力**（代理用 Grep/Read/环境知识库工具扫目录），包内零脚本、零向量库、零密钥。
3. **三步法论证从 standards 重建**：以 `cn-invention-utility.md` 锚点（指南 第二部分第四章）为准，把模式 D 案例模板里的隐式四步升级为显式三步法论证纪律 + 修改策略（沿用 self-service「退路/布防」词表）。
4. **不吸收**：`tools/oa/*.py` 全部脚本、`config.py` 密钥管理、`tools/crawl/` 抓取工具、Obsidian `_OA索引`/Canvas/DB 结构。

若未来确需向量检索案例档案，也应由**环境知识库工具**（如已装好的 embeddings/BM25 服务）承担，包只声明「存在哪些案例、在哪里」，不随包带检索实现——与 ADR-0003「声明存在与位置、不负责如何检索」同一原则。

## 附：证据索引

| 事实 | 证据 |
|---|---|
| 模式 D 默认关、显式触发、须人审 | 外部 `SKILL.md:19,69,187,223` |
| 案例脱敏入库 + 通知书→标签/向量检索→答复草稿 | 外部 `SKILL.md:19,132-152` |
| 输入 PDF-first、禁止手贴 | 外部 `prompts/oa/respond_office_action.md:7,26-28` |
| 检索必做、空库禁糊弄 | 外部 `respond_office_action.md:40`；`guardrails.md:15` |
| 逐条对应、修改须指向说明书出处 | 外部 `respond_office_action.md:64-67` |
| 策略选项 + 超范围风险 | 外部 `respond_office_action.md:58-60`；`guardrails.md:16` |
| 五条禁止 | 外部 `guardrails.md:12-18` |
| 自建语料：Obsidian 方案 C + sqlite-vec | 外部 `ingest_case.md:40-47`；`store.py:1,36,255,294`；`requirements-oa.txt` |
| 向量厂商适配 + 密钥管理 | 外部 `embed.py:34`；`config.py`（850 行）；`docs/oa/embedding.config.yaml`（`api_key_env: ZHIPUAI_API_KEY`） |
| 案例笔记合同 | 外部 `references/schemas/oa_case.schema.yaml` |
| 隐含论证模板（非命名三步法） | 外部 `case_note_template.md:33-37`；`examples/example_oa_response/cases/history/hist-inventiveness-clamp.md`；全仓 grep「三步法」= 0 命中 |
| 测试覆盖 | 外部 `tests/oa/test_oa_store.py`（422 行，9 测试类） |
| 本包：never builds search / never manages keys | 本包 `docs/adr/0003-delegation-first.md` |
| 本包：A 组未来接入、professional/ 预留 | 本包 `docs/adr/0004-self-service-package.md`（决策 1、未来节） |
| 本包：零脚本收编纪律 | 本包 `docs/adr/0005-absorb-external-patent-tools.md`（决策 1、决策 5、决策 6） |
| 本包：OA 归档为 professional/ 参考 | 本包 `docs/adr/0005-absorb-external-patent-tools.md` 决策 6 |
| 本包：检索禁区词表 | 本包 `CONTEXT.md`（Delegated search / Declared external source / Document-only capability / Archived reference / `.patent/`） |
| 本包：契约四条款 + user-supplied grounding | 本包 `docs/prototype/delegation-contract.md` |
| 本包：指南 第二部分第四章 = 三步法锚点 | 本包 `skills/en/patent-standards/references/cn-invention-utility.md:41` |
| 本包：A 组现存资产仅隔离 + 标记重做 | 本包 `skills/en/professional/patent-claims-analyzer-us/SKILL.md:3-4`（`disable-model-invocation` / `metadata.internal` / 「To be redone」） |
