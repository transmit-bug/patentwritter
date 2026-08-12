# Patent Writing Skill Hub

Agent skills for patent writing (专利申请), installable as a single package:

```bash
npx skills add transmit-bug/patentwritter
```

**方向(2026-08-11 重构后)**:面向**发明人/非专业人士的自助申请向导**,只覆盖专利申请全流程(交底 → 类型判断 → 撰写 → 自检 → 递交与补正;发明/实用新型/外观设计)。专业代理人方向(OA 答复、三步法论证等)留待未来以独立技能组接入,见 `docs/adr/0004-self-service-package.md`。

**`.patent/` 支撑层工作目录**:发明人项目根目录下三档分级(`sources/` 引用清单、`materials/` 素材、`queries/` 检索记录),与申请文件草稿 `patent-application/` 分治;建议加入发明人项目的 gitignore(留痕可自行取消)。

**诚实红线**:不编造现有技术、专利号、文献、实验数据。背景技术只写发明人已知的、客观通用问题、检索工具真实返回的三类素材。

## 布局(skills.sh 类别目录标准)

```
skills/
├── self-service/                  # B 组:发明人自助(本包主体)
│   ├── patent-application/        # 入口(user-invoked):交底访谈+类型判断+编排(含外观设计分支)
│   ├── patent-claims/             # 权利要求撰写(独权/从权/上位化/退路布防)
│   ├── patent-specification/      # 说明书五段式+摘要
│   ├── patent-drawings/           # 附图+附图标记一致性+摘要附图+外观视图清单
│   ├── patent-compliance/         # 递交前自检(支撑链/清楚性/形式)
│   └── patent-filing/             # 递交与补正指引
├── professional/                  # A 组(未来):当前只寄放保留的 US 技能,默认不参与发现
│   ├── patent-application-creator-us/
│   └── patent-claims-analyzer-us/
├── tools/
│   ├── patents-search/            # 委托检索(可选工具,流程不依赖)
│   └── conversion/                # 纯文档转换纪律:Word 交付/材料摄入(零脚本,可选依赖)
└── patent-standards/              # 共享目录:CN/US 权威文本+实测核实的条文锚点+声明外部源
```

## 技能关系(依赖化/层级化)

- **入口**(`patent-application`,disable-model-invocation)编排全流程,调用 model-invoked discipline 技能;入口不调用入口。
- **Discipline 技能**(claims/specification/drawings/compliance/filing)承载可复用撰写纪律,模型按需自动加载,也被入口调用。
- **法律锚点单一来源**:`patent-standards` 的"Verified rule anchors"节(2026-08-11 对 CNIPA 全文实测核实),各技能只引用锚点,不重复条文。

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

遵循 [skills.sh / Agent Skills](https://www.skills.sh/docs) 包约定:技能 = 含 `SKILL.md`(frontmatter 有 `name`+`description`)的目录,从 `skills/` 容器发现,支持 `skills/<category>/<name>/` 类别布局。
