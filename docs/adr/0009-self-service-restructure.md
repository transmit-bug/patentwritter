# ADR-0009: 自助组重构——7→5 技能、显式分层与统一来源处理

- 状态:Accepted (2026-08-13)
- 取代/关联:ADR-0004(B 组布局,决策 3 的"router + application"拆分被本 ADR 收回);ADR-0007(A 组边界,不受影响);ADR-0008(目录分层,工作区目录名不变);issue #25(决策溯源)

## 背景

对 `skills/en/self-service/` 的层级审查发现:技能间关系不清、无法层级化处理。

1. **router/application 拆分只有交接成本**:路由记录落定后立刻整体移交,不存在"只要路由不要访谈"的再入场景;入口层反向引用编排层 references(入口层破层),两次 handoff 全是开销。
2. **claims/specification 之间是最紧的契约**(支撑链、"先权项后说明书"、术语一致),却被切成两个技能靠散文衔接;自服务场景几乎不存在"只写说明书不碰权项"的独立需求。
3. **层级约束全是散文**:七技能全部 model-invoked、全带直连触发词,回边(自检 critical → 回改)只在文字里;`草稿/申请信息.md` 只记路由四要素、不记阶段进度,会话中断后只能靠"哪些草稿文件存在"隐式推断。
4. **来源轴只活在前十行路由记录里**:router 列了来源,之后无人消费;网页/对谈/代码没有摄入通道;访谈只有"挖掘模式"一种。
5. **命名撞名**:`patent-application` 同时撞交付物("申请文件套件")、专业组保留技能(`patent-application-creator`)、发明人工作区目录(`patent-application/`,ADR-0008)。

## 决策

### 1. 合并判据(存续测试)

一个技能值得独立存在,须过四测之一:(a) 独立再入场景存在;(b) 工具面/失败模式不同;(c) 检查者须独立于起草者;(d) 合并后单次加载超预算。

- **router + application → `patent-intake`**:四测全不过(合并)。原 application 名下五个 references(interview / type-decision / design-points / disclosure-document / search-guide)整体迁入 intake;design-points.md 仍是外观分支唯一执行版。
- **claims + specification → `patent-drafting`**:紧契约由跨技能衔接变技能内阶段,"先权项后说明书"成为技能内顺序,支撑链单一所有者(合并)。
- **drawings / compliance / filing 保留**:分别过测试 (b)(dot 依赖、缺依赖 fail loud)、(c)+(a)(补正比对再入)、(a)(递交后独立再入,👤 手工步骤)。

### 2. 四层角色 + 三流分离

- 层级:L1 前门+编排(intake)→ L3 执行(drafting / drawings / compliance / filing)→ L0 服务(standards / conversion / patents-search / intake 名下共享 references)。组内 README 的树形图改为**三流描述**:控制流管线(含回边)、产物数据流 DAG、知识指针流(单一出处原则)。
- 每个 SKILL.md 开头声明角色(front door / discipline / service)。
- **回边规则**:自检 critical 由 intake 路由回 drafting/drawings 对应产物;discipline 之间零横向调用,只通过产物文件衔接。conversion 双角色(首端摄入/末端交付)在三流图中显式表达。

### 3. 阶段清单状态机

`草稿/申请信息.md` 增加"阶段清单"段,枚举:摄入 / 路由 / 访谈 / 权利要求 / 说明书 / 附图 / 自检 / 交付 / 递交。每个技能完成产物时自更新为 ✓;受阻记 blocked 加原因。续跑依据清单,不靠文件存在性推断。自检报告固定落 `草稿/检查报告.md`。

### 4. 统一来源处理(一份文件,不开技能分支)

来源是 intake 阶段的两个正交参数:**形态 → 摄入通道**(文档→conversion;网页→环境 fetch+快照;对谈→记录归档;代码→直读;口述→即访谈),**完整度 → 访谈策略**(提取-确认-补齐三步协议,访谈模式按材料完整度自然涌现:挖掘/确认/混合;问题银行不变)。

- 归档契约:任何来源原样落 `.patent/materials/` + 来源登记。
- 五横切标志(公开状态 / 语言纯度 / 数据可用性 / 图可用性 / 多贡献风险)写入申请信息,下游技能只读标志、不读来源种类。
- 论文特有 delta(已发表判定接宽限期核查、related work 归入"发明人已知的现有方案"、单一性拆案门、论文图只作重绘素材、实验数据可引用须注明条件)收进同一文件。
- 载体:新增 `patent-intake/references/source-modes.md`,不建 per-source 技能或 per-source 文件。

### 5. 命名

- 合并技能定名 `patent-intake` / `patent-drafting`;drawings / compliance / filing 保留原名。
- 发明人工作区目录 `patent-application/`(草稿/附图/成品)保持不变(存量项目兼容),组内 README 显式区分"工作区目录 vs 技能名"。三重撞名随改名消除。
- 引用一律按安装几何书写(flat:`../<skill-name>/`);顺带修复两个存量断链(`../tools/conversion/`、`../tools/patents-search/`)。

## 后果

- 自助组可发现技能 7 → 5;状态机交接点 6 → 4;"入口层反向引用编排层 references"的破层随合并结构性消失。
- 退役技能名 `patent-router` / `patent-claims` / `patent-specification` 在安装副本零残留;`patent-application-creator`(专业组隐藏保留)与工作区目录 `patent-application/` 不是退役对象。
- A 组指向 B 组的引用(`patent-prosecution` / `patent-claim-strategy` 中的 patent-application / patent-claims)同步更新为 patent-intake / patent-drafting。
- 旧技能名消失后,依赖旧名的会话由 intake 前门重路由;重装即迁移(`npx skills add` 幂等覆盖),磁盘存量草稿不受影响。
- ADR-0004 决策 3 中"router 与 application 分立"的描述由本 ADR 取代;其余(法律锚点单一来源、内容原则、删除清单)不变。
