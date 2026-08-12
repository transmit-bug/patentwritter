# 资料目录 — CN/US 权威文本 + 声明外部源

> 由 `../SKILL.md`(薄索引)指向。声明**哪些资料存在、官方在哪、引用锚点是什么**;不负责如何检索(检索由环境工具/人工完成)。校验信息见 `../../../docs/research/standards-catalog.md`(逐条来源)与 `../../../docs/research/design-patent-anchors.md`(外观设计锚点)。

## China — the 2023 package (one body, effective 2024-01-20)

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 专利法 | As amended 2023-12-29 (8 chapters, 82 articles) | flk.npc.gov.cn (国家法律法规数据库) | 专利法 第X条 — drafting-relevant: 第2条(定义), 第22条(新颖性/创造性/实用性), 第25条(不授予专利权), 第26条(申请文件/说明书/权利要求书), 第59条(保护范围) |
| 专利法实施细则 | 2023年修订 (国务院令第769号, 13章149条) | gov.cn 令769号 / cnipa.gov.cn | 实施细则 第X条 — drafting-relevant: 第17条(申请文件), 第20条(说明书), 第26条(摘要), 第33条(宽限期) |
| 专利审查指南 | 2023 edition (局令第78号, six parts) | cnipa.gov.cn (局令第78号页 + 全文PDF) | 指南 第X部分第X章 — drafting-relevant: 第一部分第三章(外观设计初步审查), 第二部分第二章(说明书和权利要求书), 第二部分第三章(新颖性), 第二部分第四章(创造性), 第二部分第五章(实用性), 第二部分第九章(计算机程序) |

## United States

| Material | Edition | Official location | Citation anchor |
|---|---|---|---|
| 35 U.S.C. | Current through Pub. L. 119-102 (2026-07-12); print 2024 Main Ed. | uscode.house.gov / govinfo.gov | 35 U.S.C. §101/§102/§103 (Ch.10), §112 (Ch.11) |
| 37 C.F.R. Title 37 | eCFR current (amended 2026-07-20) | ecfr.gov (Part 1) | 37 CFR §1.71(说明书), §1.75(权利要求), §1.77(申请文件排列), §1.104(审查), §1.121(修改) |
| MPEP | 9th Ed., Rev. 01.2024 (current to 2024-01-31) | uspto.gov (mpep/index.html) | MPEP §608(公开内容/权利要求格式), §706(驳回), §2106(客体适格), §2164(能够实现), §2171-2176(112(b) 清楚性) |

## Edition summary (at a glance)

| Jurisdiction | Material | Current edition | Effective / currency date |
|---|---|---|---|
| CN | 专利法 | As amended 2023-12-29 (last amend. 2020-10-17; 2023 decision eff. 2024-01-20) | 2024-01-20 (2023 amendment) |
| CN | 专利法实施细则 | 2023年修订 (国务院令第769号, 3rd revision) | 2024-01-20 |
| CN | 专利审查指南 | 2023 edition (局令第78号) | 2024-01-20 |
| US | 35 U.S.C. | Online current through Pub. L. 119-102; print: 2024 Main Ed. | July 12, 2026 (online) |
| US | 37 C.F.R. | eCFR current (Title 37) | amended 2026-07-20 |
| US | MPEP | 9th Ed., Rev. 01.2024 | January 31, 2024 |

**Cross-system note for citation practice:** CN patent writing citations point to article numbers of 专利法 and 实施细则 (e.g., 专利法第26条第3款 — 权利要求书; 实施细则第20条 — 说明书) and 指南 part/chapter/section (e.g., 指南 第二部分第二章 — 说明书和权利要求书). US citations point to statute section (35 U.S.C. §112), rule (37 CFR §1.71), and MPEP section (MPEP §2106, §2164, §2171-2176). The 2023 CN package (专利法 decision + 实施细则修订 + 审查指南2023 + 过渡办法) took effect as one body on 2024-01-20.

---

## Declared external sources (声明外部源)

Human-operated sources the set **documents but never automates** (CONTEXT.md「Declared external source」)。与委托工具同级,不是降级梯:技能只引用源信息与引用锚点,包内不带任何爬虫/薄封装代码。

### CNIPA 公布公告系统(国知局公布公告系统)

| 项 | 内容 |
|---|---|
| 官方名 | 国家知识产权局 公布公告系统(epub.cnipa.gov.cn) |
| URL | http://epub.cnipa.gov.cn/(注意是 **http 非 https**;直连受动态 JS 反爬网关保护,无稳定公开查询 URL/API) |
| 管辖区 | CN |
| 管辖内容 | 专利公布/公告的著录项目、全文、法律状态(发明公布/发明授权/实用新型/外观设计) |
| 引用锚点 | 公开号/公告号,如 CN209861402U;详情页形如 http://epub.cnipa.gov.cn/patent/{公开号} |
| 检索形态 | 人工浏览器(步骤见 `../../self-service/patent-application/references/search-guide.md`);agent_browser 等真浏览器自动化可代跑;遇验证码改用 Google Patents(country:CN)/WebSearch |
| 核实 | 2026-08-12 curl 实测 + 第三方源码交叉,详见 `../../../docs/research/cnipa-epub-search-forms.md` |
