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
| **自助申请(B 组,self-service)** | `patent-intake` | model-invoked(说到写专利即触发) | 交底 → 类型判断 → 撰写 → 自检 → Word 交付 → 递交与补正 |
| **专业授权(A 组,professional)** | `patent-prosecution` | user-invoked(`disable-model-invocation`,需显式 `/skill:patent-prosecution`) | OA 答复 / 复审 / 无效 / 评价报告 / 权利要求策略 |

入口只做路由与输入闸门检查,不承载任何撰写逻辑;拿到路线后转交对应 discipline 技能执行。

## 技能清单

### B 组:自助申请(`skills/self-service/`)

| 技能 | 职责 | 不做什么 |
|---|---|---|
| `patent-intake` | 前门+编排(ADR-0009 合并原 router+application)。统一来源处理(归档契约+摄入通道+提取-确认-补齐+五标志)、按**材料来源 × 交付目标 × 专利类型**三轴问路、访谈四要素、阶段清单状态机、回边路由、组装交付 | 不写权利要求/说明书/附图,不复述法律条文 |
| `patent-drafting` | 权利要求书+说明书五段式+摘要,一个技能内先权项后说明书;必要特征判定(删除测试)、独权撰写、上位化阶梯、从权退路布防、背景技术诚实协议、三向对应、支撑链 | 不访谈发明人;缺输入回 intake,不自行发问 |
| `patent-drawings` | 附图。Graphviz(`dot`)画结构图/流程图,标记双向一致性,指定摘要附图 | 外观视图规则不在此(单一版本在 `patent-intake/references/design-points.md`);无 `dot` 时 fail loud |
| `patent-compliance` | 递交前自检。只查所请求的交付物,报告落 `草稿/检查报告.md`(严重度/位置/修复指引) | 不做递交操作指导;检查者独立于起草者 |
| `patent-filing` | 递交与补正。电子申请注册/缴费/流程,补正通知书处理协议(常见补正项 + 超范围红线 + 期限) | 不写申请文件本身 |

B 组内共享的判断逻辑放在 `patent-intake/references/` 下按需读取(来源模式 `source-modes.md`、访谈、类型判定 `type-decision.md`、外观要点 `design-points.md`、交底书结构、检索指引 `search-guide.md`)。

### A 组:专业授权(`skills/professional/`)

入口 `patent-prosecution`(user-invoked)按「你手里有什么材料」查表分发到五个 discipline(model-invoked,各自可独立被发现):

| 技能 | 触发情境 | 输入闸门 |
|---|---|---|
| `patent-oa-response` | 收到审查意见通知书,要写意见陈述书 | 通知书(优先 PDF)+ 申请文件(权利要求 + 说明书) |
| `patent-re-exam` | 收到驳回决定,要在 3 个月内提复审 | 驳回决定 + 申请文件 + OA 历史 |
| `patent-invalidation` | 无效双向:主动请求无效,或作为专利权人答辩 | 请求方向:授权文本 + 证据;答辩方向:无效请求书 + 证据 + 授权文本 |
| `patent-evaluation-report` | 实用新型/外观维权前评估、应对侵权指控、开放许可 | 专利文本 + 用途 |
| `patent-claim-strategy` | 保护范围权衡、OA 修改策略、分案/优先权决策 | 权利要求 + 说明书 + 可得的先有技术 |

**A 组边界(ADR-0007 决策 7)**:FTO / 专利布局 / 维权 / 许可(授权后业务)与 US 执业不在范围内;全新申请的机械撰写也不走 A 组——回到 B 组入口。

### 工具组(`skills/tools/`)

| 技能 | 职责 | 关键约束 |
|---|---|---|
| `patents-search` | 委托检索:Valyu 语义检索 API 查先有技术(USPTO/EPO 全文) | 可选工具,流程不依赖;CN 专利不在 Valyu 数据源内,CN 现有技术走 CNIPA 手动检索(search-guide);需自备 API key |
| `conversion` | 纯文档摄入: .docx/.pptx → Markdown (Stage-1) | 零脚本零依赖(ADR-0005),环境探测降级链(python-docx/pptx → 手动),全不可用则 fail loud |
| `word-delivery` | Word 交付: md → docx (Stage-5, 按需触发,单源规则) | 零脚本,探测 python-docx → pandoc → 手动,模板填充仅链①,全不可用则 fail loud |

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
