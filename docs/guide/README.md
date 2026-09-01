# Skills 指南:技能介绍与组合地图

> 本目录(package-repo `docs/guide/`)不随包安装分发,是仓库侧使用指南。实用案例见同目录 [use-cases.md](use-cases.md)。

本包是一套**专利撰写技能集**,一条命令安装:

```bash
npx skills add transmit-bug/patentwritter
```

安装后技能位于 `<agent-skills-dir>/<skill-name>/` 下(安装器拍平);源树按功能分组(`skills/<group>/<skill-name>/`,ADR-0011,分组即安装单元,见根 README「标准」一节)。技能正文为英文(2026-08-13 英文化),法律条文引用与发明人交付物保留中文。

## 两条独立链路,各有入口

技能集覆盖专利生命周期的两端,入口不互相调用(「入口不调入口」):

| 链路 | 入口 | 触发方式 | 覆盖 |
|---|---|---|---|
| **自助申请(B 组,self-service)** | `patent` | model-invoked(说到写专利即触发) | 论文→交底书主链路：摄入→分型→四要素→撰写→自检，兼申请文件；综述止步可专利点分析 |
| **专业授权(A 组,professional)** | `patent-prosecution` | user-invoked(`disable-model-invocation`,需显式 `/skill:patent-prosecution`) | OA 答复 / 复审 / 无效 / 评价报告 / 权利要求策略 |

入口只做路由与输入闸门检查,不承载任何撰写逻辑;拿到路线后转交对应 discipline 技能执行。

## 技能清单

### B 组:自助申请(`skills/self-service/`)

单技能精简一站式 `patent`（替代原 6 技能 intake/drafting/drawings/compliance/exploration/filing）：

| 阶段 | 职责 |
|---|---|
| Step 0 摄入 | 原文落 `.patent/materials/`，内联探测 mammoth/python-docx/python-pptx → Markdown，溯源一行 |
| Step 1 分型 | 技术论文(A)→进撰写；综述/案例(B)→止步 `可专利点分析.md` |
| Step 2 四要素 | 12问拿齐 技术问题/方案/区别特征/效果，缺一不写 |
| Step 3 撰写 | 单文件交底书 7节 + 申请文件分支(说明书→权利要求→摘要) |
| Step 4 附图 | 复用原图 + dot 流程图(≤8节点)，落 `figures/` |
| Step 5 自检 | 轻量3项(支撑/清楚性/一致性)落 `check-report.md` |

### A 组:专业授权(`skills/professional/`)

入口 `patent-prosecution`(user-invoked)按「你手里有什么材料」查表分发到五个 discipline(model-invoked,各自可独立被发现):

| 技能 | 触发情境 | 输入闸门 |
|---|---|---|
| `patent-oa-response` | 收到审查意见通知书,要写意见陈述书 | 通知书(优先 PDF)+ 申请文件(权利要求 + 说明书) |
| `patent-re-exam` | 收到驳回决定,要在 3 个月内提复审 | 驳回决定 + 申请文件 + OA 历史 |
| `patent-invalidation` | 无效双向:主动请求无效,或作为专利权人答辩 | 请求方向:授权文本 + 证据;答辩方向:无效请求书 + 证据 + 授权文本 |
**A 组边界(ADR-0007 决策 7)**:FTO / 专利布局 / 维权 / 许可(授权后业务)与 US 执业不在范围内;全新申请的机械撰写也不走 A 组——回到 B 组 `patent`。

### 工具组(`skills/tools/`)

| 技能 | 职责 | 关键约束 |
|---|---|---|
| `word-delivery` | Word 交付: md → docx (按需触发,单源规则) | 零脚本,探测 python-docx → pandoc → 手动,模板填充仅链①,全不可用则 fail loud |
| `patents-search` | 委托检索:Valyu 语义检索 API 查先有技术(USPTO/EPO 全文) | 可选工具,流程不依赖;CN 专利不在 Valyu 数据源内,CN 现有技术走 CNIPA 手动检索;需自备 API key |

### 跨组共享(`skills/patent-standards/`)

薄索引 + 按类型拆分的权威文本锚点(`references/`:CN 发明/实用新型、CN 外观、US、CN 专业执业、专业纪律、目录)。**单一来源**:所有技能的法律断言按需读取这里核实的条号,不在各自正文复制法条表格;它只声明**有什么、在哪里**,从不负责怎么检索。

## 三个贯穿性纪律

1. **诚实红线**:先有技术只来自真实检索结果或用户提供材料,绝不编造专利号、文献、实验数据;背景技术只写发明人已知方案、客观通用问题、检索真实返回三类素材。
2. **Grounded output**:每条法律断言引用声明来源(如审查指南 Part II),先有技术引用指向真实检索结果。
3. **Fail loud**:缺输入、缺工具(`dot`、转换依赖、检索 API)时明说缺什么、停下,不硬写。没有产出好过未经核实的专利文本。

## 支撑层工作目录 `.patent/`

发明人项目根下的三档分级,与申请文件草稿(`patent-application/` 下的 `草稿/` 与 `成品/`)分治:

- `sources/` — 声明与引用清单
- `materials/` — 发明人材料、检索所得文献
- `queries/` — 检索记录与结果

建议加入发明人项目的 gitignore。

## 延伸阅读

- 实用案例与组合链:[use-cases.md](use-cases.md)
- 包方向与架构决策:`docs/adr/0004-self-service-package.md`、`docs/adr/0007-professional-group-integration.md`
- 领域术语:根目录 `CONTEXT.md`
- 技能有效性审查:`docs/review/skills-effectiveness-review.md`
