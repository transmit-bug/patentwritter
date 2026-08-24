# ADR-0013: Word 导出拆分为用户主动调用的 word-delivery 技能

日期: 2026-08-14
状态: 已采纳

## 背景

ADR-0005/0008 起,`tools/conversion` 同时承担流水线两端:首端材料摄入(docx/pptx → md)与末端 Word 交付(md → docx),且交付降级链是 Stage-5 的默认终点。实际使用暴露两个问题:

1. **流程定死、无商量**:intake 阶段清单把「交付」列为必经阶段,agent 每次跑完自检就直接生成 docx,交付形态没有与发明人协商的闸门。
2. **docx 改动不便**:发明人拿到 docx 后最自然的动作是直接改 docx,但草稿真相在 `草稿/*.md`,手改产物导致源与产物漂移。

## 决策

1. **技能拆分**:`tools/conversion` 只保留摄入纪律(docx/pptx → md,model-invoked);新建 `tools/word-delivery` 承接全部 Word 交付内容(交付降级链、验收闸门、模板填充、fail loud)。
2. **Word 导出 = 用户主动调用**:`word-delivery` frontmatter 加 `disable-model-invocation: true`(先例:professional 组入口 `patent-prosecution`)。触发条件仅两个:用户当轮明确要求;或路由记录 `Word导出: 已约定`。
3. **访谈协商点**:intake 路由记录新增 `Word导出` 轴(未约定(按需,默认)/ 已约定(时机/模板)),访谈时确认并记入 `草稿/申请信息.md`;阶段清单「交付」语义改为「md 定稿;docx 仅按约定」。
4. **修订回路(单一真相)**:`草稿/*.md` 是唯一可编辑真相,`成品/*.docx` 是可再生导出。任何修改意见——包括对已交付 docx 的抱怨——回到对应 md 修改 → 重跑受影响自检(`patent-compliance`)→ 经 `word-delivery` 重导出;永不手改已交付 docx。规则写入 `word-delivery`(single-source rule)与 `patent-drafting`(Revision loop 一节)。

## 后果

- 流水线默认完成点是**自检清零的 md 草稿**,不再是 docx;`patent-compliance` 完成标准相应改为条件式。
- `disclosure-document.md` 的组装语义不变(md 组装恒做),docx 转换一句改为按需指向 `../../word-delivery/SKILL.md`。
- 可见技能数 14 → 15;`marketplace.json` tools 分组、`skills/README.md`(树形图/角色表/三流图)、`AGENTS.md`、`docs/guide/README.md` 同步更新;子路径安装需 Word 交付时补装 `skills/tools/word-delivery`。
- `requirements-optional.txt` 按 skill 目录拆分:conversion 留 mammoth/python-docx/python-pptx(摄入);word-delivery 留 python-docx/latex2mathml/pandoc(交付)。顺带修复合规问题:旧 conversion 的 requirements 内含仓库侧溯源注释(`research/absorb-conversion-tools.md`),违反安装侧自包含硬规则,已删除。
- 历史文档(ADR-0005/0008/0009/0012)描述的是当时状态,不回改。

## 验证

安装副本验证同既有流程:`npx skills add .` 装临时目录 → 逐条解析 `..` 引用 → 对全部安装文件 grep 禁词(`ADR-|docs/(research|prototype|adr|plan)|CONTEXT\.md|package-repo|A 组|B 组`)零命中。
