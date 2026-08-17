# Patent Writing Skill Hub

Agent skills for patent writing (专利申请), installable as a single package:

```bash
npx skills add transmit-bug/patentwritter
```

**方向(2026-08-11 重构后;2026-08-13 ADR-0007 落地)**:面向**发明人/非专业人士的自助申请向导**,覆盖专利申请全流程(交底 → 类型判断 → 撰写 → 自检 → 递交与补正;发明/实用新型/外观设计)。专业代理人方向(A 组)已按 `docs/adr/0007-professional-group-integration.md` 分阶段实现并落地 `skills/en/professional/`(授权链路:OA 答复 / 复审 / 无效 / 评价报告 / 权利要求策略 + 入口),见 `docs/plan/professional-integration.md`。

**`.patent/` 支撑层工作目录**:发明人项目根目录下三档分级(`sources/` 引用清单、`materials/` 素材、`queries/` 检索记录),与申请文件草稿 `patent-application/` 分治;建议加入发明人项目的 gitignore(留痕可自行取消)。

**诚实红线**:不编造现有技术、专利号、文献、实验数据。背景技术只写发明人已知的、客观通用问题、检索工具真实返回的三类素材。

## 布局(skills.sh 类别目录标准)

```
skills/
├── en/                              # en 语言组(2026-08 起,内容英文化,语言作为顶层命名空间)
│   ├── self-service/                # B 组:发明人自助(本包主体)
│   │   ├── patent-router/           # 总入口:材料来源+交付目标+专利类型+模板路由
│   │   ├── patent-application/      # 访谈与编排(不再承担总路由)
│   │   ├── patent-claims/           # 权利要求撰写(独权/从权/上位化/退路布防)
│   │   ├── patent-specification/    # 说明书五段式+摘要
│   │   ├── patent-drawings/         # 附图+附图标记一致性+摘要附图+外观视图清单
│   │   ├── patent-compliance/       # 递交前自检(支撑链/清楚性/形式)
│   │   └── patent-filing/           # 递交与补正指引
│   ├── professional/                # A 组(ADR-0007 已实现):CN 授权链路技能集 + 入口 + 保留 US 技能(隐藏)
│   │   ├── patent-prosecution/          # 入口(user-invoked):授权链路编排路由
│   │   ├── patent-oa-response/          # OA 答复(旗舰:模式 D 纯文档收编 + 三步法)
│   │   ├── patent-re-exam/              # 复审请求书
│   │   ├── patent-invalidation/         # 无效(请求+答辩双向)
│   │   ├── patent-evaluation-report/    # 专利权评价报告(请求与解读)
│   │   ├── patent-claim-strategy/       # 权利要求策略(保护范围/答复修改/分案/优先权)
│   │   ├── patent-application-creator/  # 保留 US 资产(隐藏,待重做)
│   │   └── patent-claims-analyzer/      # 保留 US 资产(隐藏,待重做)
│   ├── tools/
│   │   ├── patents-search/          # 委托检索(可选工具,流程不依赖)
│   │   └── conversion/              # 纯文档转换纪律:Word 交付/材料摄入(零脚本,可选依赖)
│   └── patent-standards/            # 共享目录:薄索引 + 分型 references(发明/实用新型、外观、US 锚点 + CN 专业执业锚点 + 共享专业纪律 + 目录 + 声明外部源)
```

## 专业组(A 组)构成

- **入口**(`patent-prosecution`,user-invoked,disable-model-invocation)编排授权链路,路由到五个 discipline;入口不调用入口。
- **Discipline**(oa-response / re-exam / invalidation / evaluation-report / claim-strategy,model-invoked)承载可复用代理纪律(三步法、封闭列举、程序纪律、禁反悔),全部引用共享专业纪律与分辖区锚点。
- **专业纪律单一来源**:`patent-standards` 的 `references/professional-discipline.md`(declare/consume/cite/fail loud/never invent) + `references/cn-professional.md`(CN 授权链路锚点)。

## 技能关系(依赖化/层级化)

- **Router**(`patent-router`)先处理材料来源、交付目标、专利类型和模板选择，再转交最小技能集合。
- **Application orchestrator**(`patent-application`)只负责访谈、顺序和交付编排；不重复路由和类型规则。
- **Discipline 技能**(claims/specification/drawings/compliance/filing)只承载各自工件的撰写或检查纪律。
- **法律锚点单一来源**:`patent-standards` 的分型 references；self-service 技能只保留文件索引，法律细节按需读取，不把 Rule basis 表格复制进用户文稿。

## 设计原则

- **内容 = 判断逻辑,不是流程清单**:每个技能给可执行的判断(删除测试/三问判据/双向核对),质量门是可检查的完成标准,不是数量指标。
- **Grounding 诚实**:条文号来自实测核实,拿不到的如实说"以官方为准",不凭记忆引用。
- **Fail loud**:缺输入/缺工具时明说缺什么,不硬写。

## 仓库布局

```
skills/                     # ← 包源码(npx skills 发现根)
CONTEXT.md                  # 领域术语表
docs/
  adr/                      # 架构决策记录(0004 为本包方向)
  review/                   # skills 有效性审查(2026)
  research/                 # standards-catalog 研究底稿
  prototype/                # delegation-contract(历史,professional 组仍引用)
  agents/                   # issue tracker、triage labels、domain 约定
```

## 标准

遵循 [skills.sh / Agent Skills](https://www.skills.sh/docs) 包约定:技能 = 含 `SKILL.md`(frontmatter 有 `name`+`description`)的目录,从 `skills/` 容器发现,支持 `skills/<category>/<name>/` 类别布局。**语言组约定(2026-08-13)**:标准本身无语言概念,本包把语言作为顶层类别目录(`skills/en/<category>/<name>/SKILL.md`),发现机制 3 层遍历兼容;法律条文引用(专利法/细则/指南条号)与发明人交付物模板保留中文原文。
