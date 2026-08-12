---
name: patent-application
description: 发明人自助申请专利(发明/实用新型/外观设计)的全流程向导:交底访谈、类型判断、生成申请文件、递交前自检、电子申请与补正指引。入口技能,用 /skill:patent-application 触发。
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Write, Edit, AskUserQuestion, Bash
---

# 专利自助申请向导(发明/实用新型/外观设计)

把发明人脑子里的技术(或产品外观),变成一套能递交的申请文件:发明/实用新型 = 权利要求书/说明书/附图/摘要;外观设计 = 图片或照片 + 简要说明。并指引递交。

## 边界

- 范围:交底 → 类型判断 → 撰写 → 自检 → 组装 → 递交与补正。
- 实审 OA 答复不在本包(那是专业代理人方向,仓库 `professional/` 组)。
- 发明人不熟行话:提问用大白话,输出用规范申请文件语言。

## 诚实红线

背景技术只写有出处的现有技术,拿不到就不写——定义(三类素材)单一来源:CONTEXT.md「诚实红线」;执行版(含"这处内容用户说得出出处吗"判断)见 `../patent-specification/SKILL.md` 段2。

## `.patent/` 支撑层工作目录(可选,建议)

发明人项目根目录建 `.patent/`,与申请文件草稿分治:

```
.patent/
├── sources/    # 声明性:专利-标准引用清单、外部源声明条目
├── materials/  # 资料性:发明人素材、检索命中文档副本(摄入的 docx/pptx 及抽图也在这)
└── queries/    # 联网查询过程:Valyu/CNIPA/Google Patents 检索记录与结果
```

- 检索结果落 `queries/`,素材落 `materials/`,引用清单落 `sources/`(阶段1 摄入、阶段2 查新都按此落盘)。
- 申请文件草稿保持可见的 `patent-application/`,不混入 `.patent/`。
- 建议把 `.patent/` 加入 gitignore(留痕可自行取消)。

## 流程:六个阶段,每阶段有完成标准

### 阶段1 交底访谈 → 完成标准:四要素齐全,写入 申请信息.md

四要素 = 技术问题 / 技术方案(最小可实施)/ 区别特征 / 技术效果。按 `references/interview.md` 的问题库逐组提问,每组用 AskUserQuestion 最多4问。

**外观设计走另一条访谈线**(发明人描述的是产品外观——形状/图案/色彩、美感为主,不涉及功能结构改进):改按 `references/design-points.md` 的外观访谈组提问(类别/设计要点/视图素材/相似设计/色彩),完成标准改为"类别 + 设计要点 + 视图素材齐全"。

提问纪律:
- 发明人先给描述,你提取四要素,**缺哪个问哪个**,不问已齐的。
- 产品名/品牌/UI 词当场记下,撰写阶段交给 patent-claims 的术语转换表。
- 效果必问"怎么证明":有数据写数据,没数据只写机理推理,不编。
- 问清是否已公开(文章/展会/售卖/泄露)→ 触发宽限期提示(专利法第24条,见 interview.md)。
- 发明人带来既有材料(.docx 交底书/设计说明/.pptx 评审稿):按 `../../tools/conversion/SKILL.md` 摄入降级链读取,素材与抽图落 `.patent/materials/`(见上)。

### 阶段2 申请类型判断 → 完成标准:类型 + 规则依据写入 申请信息.md

按 `references/type-decision.md` 的决策树判断 发明 / 实用新型 / 外观设计 / 一案两请。规则依据来自 patent-standards 的核实锚点,不凭印象。类型为外观设计时,继续按 `references/design-points.md` 收类别与洛迦诺分类提示。

**查新(可选,建议)**——撰写背景技术前跑一轮,结果只写真实返回(诚实红线):见 `references/search-guide.md`(Valyu 主路径 + 国知局人工检索五步)。

### 阶段3 撰写 → 完成标准:四个文件落盘,无占位符(外观设计:简要说明 + 视图清单)

**发明/实用新型**:依次读三个 discipline 技能全文并按之执行(路径相对本目录):
1. `../patent-claims/SKILL.md` — 权利要求书
2. `../patent-specification/SKILL.md` — 说明书 + 摘要
3. `../patent-drawings/SKILL.md` — 附图 + 摘要附图指定(实用新型必须;发明有图更稳)

输出到用户工作目录 `patent-application/`:
```
patent-application/
├── 申请信息.md       ← 四要素 + 类型 + 宽限期判断
├── 权利要求书.md
├── 说明书.md
├── 摘要.md
├── 附图/fig1.svg、fig1.png …   ← svg 预览 + png 供 Word 内联
└── 附图说明.md       ← 编号 + 标记清单 + 摘要附图指定
```

**外观设计**:读 `references/design-points.md` → 生成 `简要说明.md` + `视图清单.md`;视图素材(按设计要点涉及的面数,照片或线条图)由发明人提供,AI 只整理视图清单与合规核对,不代画。输出布局:

```
patent-application/
├── 申请信息.md       ← 类别 + 设计要点 + 色彩声明 + 相似设计
├── 简要说明.md       ← 名称/用途/设计要点/指定图/省略视图/色彩
├── 图片/主视图.png … ← 发明人提供(黑白/灰度,按设计要点涉及面数,见 references/design-points.md)
└── 视图清单.md       ← 六视图 + 立体图对应表
```

### 阶段4 自检 → 完成标准:critical 清零(最多两轮,两轮后仍有的明确列出)

读 `../patent-compliance/SKILL.md`,对产出文件跑全部检查项(发明/实用新型:权利要求书+说明书+附图;外观设计:简要说明+视图),输出检查报告。有 critical 问题返回阶段3修改;两轮后仍有 critical,列清单交用户决定。

### 阶段5 组装 → 完成标准:递交清单确认 + Word 交付(可选)

核对:名称一致、文件齐全、附图标记一致、摘要附图已指定。给出发明/实用新型/外观设计各自的申请文件清单(请求书由系统生成,提醒用户填)。

**生成 Word 交付(发明/实用新型,发明人需要 .docx 时)**:读 `../../tools/conversion/SKILL.md`,按交付降级链把 `权利要求书.md / 说明书.md / 摘要.md` 各出**同名 .docx**(固定文件名、分文件对应,无时间戳),附图以 `figN.png` 内联。完成标准:三个 .docx 已生成且无缺图;或明确走了降级链(交付 .md + 手动另存指引),并对用户说明当前产物格式。

### 阶段6 递交与补正指引 → 完成标准:分步指引给出,人可执行的步骤已标注

读 `../patent-filing/SKILL.md`,给出发明人可自己完成的电子申请步骤,标注哪些只有人能办(注册/缴费/签字)。用户收到补正通知书后回到本阶段,用 patent-filing 的补正协议处理。

## 技能关系

- 本入口只调用上述 model-invoked discipline 技能,不调用其他入口技能。
- 法律锚点统一在 `../../patent-standards/`(发明/实用新型 → `references/cn-invention-utility.md`;外观设计 → `references/cn-design.md`),本技能不重复条文内容,只在判断点引用。
