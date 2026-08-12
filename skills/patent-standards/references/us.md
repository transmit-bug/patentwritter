# United States — 核实锚点

> 消费方:专业组(`skills/professional/` 的 patent-application-creator-us / patent-claims-analyzer-us,当前隐藏)。
> 核实:2026-08-10 对官方源逐条核实(逐条来源见 `../../../docs/research/standards-catalog.md`)。

## 完整纪律(declare / consume / cite / fail loud / never invent)

专业组消费本目录时按下方五条执行(来源契约:`../../../docs/prototype/delegation-contract.md`;索引侧指针见 `../SKILL.md`):

1. **Declare** — 法律断言前先声明需要:`[STANDARD] <jurisdiction> <topic>`。按本文件锚点确定管束材料,再由环境读取该材料;技能自身不抓取、不持 key、不越出目录声明的 URL。
2. **Consume** — 只依据实际读到的材料;没有读到就没有断言。
3. **Cite** — 输出中的每条断言带锚点:`(per 35 U.S.C. §112 — uscode.house.gov)` / `(per MPEP §2106 — uspto.gov)` / `(per 37 CFR §1.75 — ecfr.gov)`。
4. **Fail loud** — 材料读不到时,发出「无法获取依据」块并停止起草该部分,不硬写:

```
无法获取依据: [STANDARD] <jurisdiction> <topic>
缺少: <tool or material>
请提供: <concrete options — enable a retrieval tool, supply the material as a file, or waive>
```

5. **Never invent** — 绝不凭记忆重述法律;本文件锚点与契约是唯一权威。

## 35 U.S.C. — Title 35, United States Code

| 条文 | 主题 |
|---|---|
| §100 | 定义 |
| §101 | 可获得专利的发明(客体适格) |
| §102 | 新颖性 |
| §103 | 非显而易见性 |
| §105 | 外层空间中的发明 |
| §111 | 申请 |
| §112 | 说明书(书面描述/能够实现/清楚性) |
| §251 | 再颁 |

## 37 C.F.R. — Title 37, Part 1 (Rules of Practice in Patent Cases)

| 条文 | 主题 |
|---|---|
| §1.57 | 援引并入 |
| §1.71 | 详细描述与说明书 |
| §1.72 | 标题与摘要 |
| §1.75 | 权利要求 |
| §1.77 | 申请文件排列 |
| §1.97/1.98 | 信息披露声明(IDS) |
| §1.104 | 审查的性质 |
| §1.121 | 修改 |

## MPEP — Manual of Patent Examining Procedure (9th Ed., Rev. 01.2024)

| 章节 | 主题 |
|---|---|
| §608 | 公开内容/权利要求格式(§608.01 说明书、§608.01(g) 详细描述、§608.01(i)-(o) 权利要求) |
| §706 | 驳回(§706.02 现有技术) |
| §2106 | 客体适格(§2106.03-.07) |
| §2163 | 书面描述 |
| §2164 | 能够实现 |
| §2171-2176 | 35 U.S.C. 112(b) 清楚性(§2171 两项独立要求、§2173 清楚性/引用基础) |
