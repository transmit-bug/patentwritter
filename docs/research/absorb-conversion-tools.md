# Absorbing Conversion Tools — Adoption Feasibility Report

评估对象:是否从 `/tmp/patent-disclosure-skill`(monolithic 专利技能,MIT,已本地克隆)吸收 `tools/shared/` 下 9 个转换脚本,收编进本包。

- 范围:`docx_to_md.py`、`pptx_to_md.py`、`md_to_docx.py`、`mermaid_render.py`、`math_to_omml.py`、`math_render.py`、`iteration_dialog_log.py`、`formula_paradigms.py`、`check_formula_plan.py`。
- 方法:**以外部仓库源码为准**(非其 README)。源提交 `ff43eb7`(2026-08-12)。
- 对照对象:本包 `skills/self-service/` 六个技能(patent-application/claims/specification/drawings/compliance/filing)与 ADR-0003(delegation-first)、ADR-0004。
- 结论速览:核心 5 个转换脚本值得收编(其中 mermaid_render 需改造),公式规划 2 个与迭代日志 1 个不收编。

## 一、许可

MIT 确认。`LICENSE` 全文 MIT,Copyright (c) 2026 handsomestWei(`/tmp/patent-disclosure-skill/LICENSE`)。**脚本文件头无独立许可声明**(抽查 `md_to_docx.py` 头 5 行仅 docstring)。收编时建议在 `docs/` 或 NOTICE 中记录来源与版权行;不修改文件头也不违法,但注明出处更稳妥。

## 二、逐脚本评估

### 1. docx_to_md.py — 收编

| 项 | 内容 |
|---|---|
| 功能边界 | Word(.docx)→ Markdown + 抽图到磁盘(mammoth `convert_to_markdown` + `img_element` 回调)。图片默认存「{md 主名}_media/」,Markdown 内相对路径引用;输出 .md 头部写元信息注释;.doc 仅警告不转换。CLI:`-i/--input`(必填)、`-o/--output`(必填)、`--media-dir`(可选)(`docx_to_md.py:106-118`) |
| 依赖 | `mammoth>=1.6.0`(根 `requirements.txt:4`;脚本内 `_require_mammoth` 运行时检查,`docx_to_md.py:21-33`)。无外部命令 |
| 成熟度 | **无测试**。`tests/shared/` 无对应文件 |
| 对接点 | patent-application **阶段1 交底访谈**:发明人提供既有 Word 交底/设计说明/旧申请文件时扫描入库(外部仓库 `SKILL.md:78` 将 docx/pptx→md 归为「Word / PPT → Markdown」入口) |
| 收编成本 | 低。无路径/配置耦合;仅 usage 文案里的「技能根目录 requirements.txt」提示需改。media 目录命名约定可沿用 |

### 2. pptx_to_md.py — 收编

| 项 | 内容 |
|---|---|
| 功能边界 | PPTX/PPSX → 按页 Markdown + 抽图(python-pptx)。处理分组形状递归、表格、演讲者备注(「**备注**：」);图片命名 `slideNN_imgNNNN.ext`。CLI 同 docx_to_md(`pptx_to_md.py:140-145`) |
| 依赖 | `python-pptx>=0.6.21`(根 `requirements.txt:6`;脚本内 `_require_pptx` 运行时检查)。无外部命令 |
| 成熟度 | **无测试** |
| 对接点 | patent-application **阶段1 交底访谈**:评审材料/演示稿扫描 |
| 收编成本 | 低。同 docx_to_md |

### 3. md_to_docx.py — 收编(连带 math_to_omml / math_render)

| 项 | 内容 |
|---|---|
| 功能边界 | Markdown → Word。标题 `#`–`######` 映射 Word 内置「标题 1–9」(黑体/宋体);正文宋体 10.5;连续多行正文**逐行成段**(保「(1)…(2)…」换行);支持粗体/行内代码/列表/围栏代码/GFM 表格/引用/水平线/图片(**等比缩放**,上限 5.5in×8.2in,`md_to_docx.py:36-37`)。**mermaid 围栏:Word 只嵌 PNG,不写源码块**(`md_to_docx.py:933-941`)。LaTeX 公式三级回退:**OMML**(`_PREFER_OMML=True`,`md_to_docx.py:57`;`_try_append_omml:60-78`)→ **PNG**(`_maybe_render_math_md:306` 调 math_render)→ **原文等宽**。CLI:`-i`、`-o`、`--base-dir`(图片相对路径根)、`--image-max-width-inches`(5.5)、`--image-max-height-inches`(8.2)、`--no-math-render`、`--no-omml`(`md_to_docx.py:1141-1173`) |
| 依赖 | 硬:`python-docx>=1.1.0`(根 `requirements.txt:2`)。可选:`latex2mathml>=3.77.0`(OMML,`requirements.txt:3`)、`matplotlib>=3.8.0`(PNG 回退,`requirements.txt:7`)。兄弟模块 math_to_omml / math_render(import 双路径容错:`from math_to_omml import …` → `from tools.shared.math_to_omml import …`,`md_to_docx.py:65-70,311-316`) |
| 成熟度 | 部分。`test_md_to_docx_table.py`(3 用例,仅 `_parse_table_row` 表格列拆分,含 `\|` 转义与隐藏图注释);`test_math_omml.py` 覆盖 OMML 块级写入 + 无 OMML 降级(4 用例,缺 latex2mathml 时 skip)。**无端到端 CLI 测试、无 mermaid/图片嵌入测试** |
| 对接点 | patent-application **阶段5 组装**(Word 版交付)+ patent-filing 递交(CNIPA 电子申请系统上传 docx)。本包当前交付物全是 `.md`/`.svg`,Word 交付是新增能力 |
| 收编成本 | 中。须连同 math_to_omml.py + math_render.py 一并收编(否则公式降级为原文);usage 文案;图片**只嵌 PNG** 的约束会牵动 patent-drawings(见 gotcha 1)。尺寸/字体默认值(5.5in 宽、宋体/黑体)本就面向 CN 交底,可直接沿用 |

### 4. math_to_omml.py — 收编

| 项 | 内容 |
|---|---|
| 功能边界 | LaTeX → MathML(`latex2mathml`)→ OMML(`m:oMath`/`m:oMathPara`)挂到 python-docx 段落。`display=True` 块级、False 行内;`try_latex_to_omml` 失败返 `None`(不抛);`normalize_latex_for_omml` 做常见简写替换(`\le→\leq` 等)。**纯库,无 CLI** |
| 依赖 | `python-docx`(OxmlElement/qn)+ `latex2mathml>=3.77.0`(运行时检查 `math_to_omml.py:163-175`;`omml_available()` 探测) |
| 成熟度 | 有测试:`test_math_omml.py`(2 用例:oMath 存在性、怪输入优雅返 None;缺 latex2mathml skip) |
| 对接点 | 与 md_to_docx 联用——Word 可编辑公式(代理人侧刚需,公式不转图片) |
| 收编成本 | 低。无路径耦合、无外部命令、无 CLI |

### 5. math_render.py — 收编

| 项 | 内容 |
|---|---|
| 功能边界 | Markdown 内 LaTeX → PNG(matplotlib mathtext),**保留原文** + 在公式后追加 HTML 注释 `<!-- ![公式](路径) -->`;块级 `$$…$$`(可跨行)/`\[…\]`、行内 `$…$`/`\(…\)`;失败保留原文不中断;已带注释引用则跳过(可重复跑);围栏代码内不处理。CLI:`-i`、`-o`、`--assets-dir`(默认 `math_figures`)、`--dpi`(220)、`--block-fontsize`(12)、`--inline-fontsize`(11)(`math_render.py:376-388`) |
| 依赖 | `matplotlib>=3.8.0`(根 `requirements.txt:7`;`math_render.py:115,396`)。无外部命令 |
| 成熟度 | 有测试:`test_math_render.py`(3 用例:嵌套括号 `\(…\)` 整段匹配、块/行内混合渲染、坏 LaTeX 保留原文;缺 matplotlib skip;测试**有副作用**写 `ROOT/tmp/`) |
| 对接点 | md_to_docx 的 PNG 回退路径;也可独立用于不需要可编辑公式的场景 |
| 收编成本 | 低。`--assets-dir` 与 md_to_docx 的 `math_figures` 目录约定互相咬合(定稿 .md 与 .docx 同目录时) |

### 6. mermaid_render.py — 改造后收编(或暂缓)

| 项 | 内容 |
|---|---|
| 功能边界 | 定稿管线:mermaid 围栏 → PNG(`mmdc`,`-b white`),保留围栏源码 + 追加 `<!-- ![图示](路径) -->` 注释;默认先跑 math_render(可 `--no-math` 关),写出 .md 后**默认再子进程调 md_to_docx 生成同名 .docx**(`try_write_docx`,`mermaid_render.py:292-341`;Word 失败不致命,打手动命令提示)。mmdc 检测顺序:本地 `tools/node_modules/.bin/mmdc` → PATH `mmdc` → `npx -y @mermaid-js/mermaid-cli`(`_find_mmdc_invocation`,`mermaid_render.py:39-69`)。视口 `-s 2 -w 1400 -H 1050`(`mermaid_render.py:71-86`) |
| 依赖 | Python 侧无硬依赖(可选 matplotlib)。外部命令:`mmdc` = Node + `@mermaid-js/mermaid-cli`(外部 `tools/package.json` pin `^11.4.0` + `puppeteer ^23.1.1`)。**当前环境:node 有、mmdc 无** → 收编后默认走 npx 拉包(需网络,puppeteer 体积大) |
| 成熟度 | **无测试** |
| 对接点 | 与本包 patent-drawings(Graphviz `dot` → SVG 黑白线条,细则第21条)是**两条平行绘图管线**:mermaid 管框图/流程图且出 PNG,dot 管结构图出 SVG。见 gotcha 1/2 的冲突说明 |
| 收编成本 | 高。① Node/mmdc 依赖与「thin package」取向冲突;② 与 dot 管线需定并存还是替代;③ 脚本把 math_render + md_to_docx 绑成一条链(`--no-math`/`--no-docx` 可关,但默认开);④ 子进程调用硬编码「同目录 md_to_docx.py」。改造点:抽掉 docx/math 强制耦合、mermaid 主题强制单色(若用于附图)、依赖说明写进 SKILL |

### 7. formula_paradigms.py — 不收编(当前)

| 项 | 内容 |
|---|---|
| 功能边界 | 加载/合并公式推荐范式配置:默认 `references/formulas/paradigms.yaml`(外部仓库,209 行)+ 案件目录覆盖 + 环境变量 `PATENT_FORMULA_PARADIGMS`(`formula_paradigms.py:60-73`)。CLI:`list`/`show`/`combos`/`paths` + `--case-dir`/`--json`(`formula_paradigms.py:122-152`) |
| 依赖 | PyYAML(运行时按需,`formula_paradigms.py:50-56`) |
| 成熟度 | 有测试:`test_formula_paradigms.py`(3 用例:默认库 ≥15 范式、案件覆盖合并、check_plan 联动) |
| 对接点 | **无直接对应**:本包 patent-specification 没有 formula_plan 工作流(不要求范式 id/禁装饰音/可算数值例)。它是外部仓库「交底书 3.4.1 公式规划」纪律的一部分 |
| 收编成本 | 高。`DEFAULT_PATH = ROOT/references/formulas/paradigms.yaml`(`formula_paradigms.py:20`,parents[2] 硬编码仓库根);需连带收编配置 + 在 patent-specification 引入公式规划纪律。**若未来给 patent-specification 加公式规划纪律,再整体评估** |

### 8. check_formula_plan.py — 不收编(当前)

| 项 | 内容 |
|---|---|
| 功能边界 | 校验 `formula_plan.yaml/json`:范式/combo 存在性、**禁装饰音**(默认 `\tilde \hat \bar \breve \vec`,`check_formula_plan.py:75-78`)、数值例(require_numeric_example)、符号数上限、`max(1,…)` 量纲启发;退出码 0/1。CLI:`-i/--input`、`--case-dir`(`check_formula_plan.py:122-133`) |
| 依赖 | PyYAML + 同包 formula_paradigms(硬耦合 import `from tools.shared.formula_paradigms import …`,`check_formula_plan.py:21-25`) |
| 成熟度 | 有测试(`test_formula_paradigms.py` 覆盖 check_plan 的 ok/禁 tilde 两路径) |
| 对接点 | 同 formula_paradigms:无对应工作流 |
| 收编成本 | 高。依赖 paradigms 配置 + formula_plan 纪律 + `tools.shared.` import 路径,三者本包都没有 |

### 9. iteration_dialog_log.py — 不收编

| 项 | 内容 |
|---|---|
| 功能边界 | 向案件目录追加「交底书修订对话记录.md」条目(本地/UTC 时间、类型 merge|correct、用户说明摘要、交付文件清单、合并/纠正摘要)。CLI:`--case-dir`、`--kind`、`--user`、`--summary`、`--artifacts`、`--log-name`(`iteration_dialog_log.py:25-56`) |
| 依赖 | 纯标准库(datetime/pathlib) |
| 成熟度 | **无测试** |
| 对接点 | **无**:本包没有外部仓库的「交底书迭代/合并/纠正」工作流(外部 `prompts/disclosure/invention/disclosure_builder.md:151-162`);本包补正流程在 patent-filing,不维护对话日志 |
| 收编成本 | 低但**无价值**。若将来需要,让 Agent 用 Write 直接追加即可(脚本本体约 80 行,重实现成本近零) |

## 三、顶层 gotchas

1. **Word 只嵌 PNG,附图管线是 SVG**。`md_to_docx.py:933-941` 对 mermaid 围栏「只嵌 PNG,不写源码块」;`_embed_from_image_ref`/`_embed_picture` 全部按位图解析(`_image_pixel_size` 读 PNG/GIF/JPEG,`md_to_docx.py:105-160`)。而本包 patent-drawings 现状是 `dot -Tsvg fig1.dot -o fig1.svg`(`patent-drawings/SKILL.md:45`)。**Word 交付意味着整个附图管线必须出 PNG**(`dot -Tpng` 即可,或统一经 mermaid_render)。不协调这一点,收编 md_to_docx 后附图在 Word 里是缺失占位。

2. **mermaid_render 的 Node/mmdc 依赖与「黑白线条」纪律**。mmdc 检测链 `tools/node_modules → PATH → npx`(`mermaid_render.py:39-69`);当前机器无 mmdc,走 npx 需网络拉 `@mermaid-js/mermaid-cli` + puppeteer(体积大)。且 `-b white` 只保证白底,`-s 2 -w 1400 -H 1050` 默认**主题彩色输出**;若产出物是申请文件附图,不满足细则第21条黑白线条实务。外部仓库用它画的是**交底书内部框图/流程图**(3.2/3.4,`SKILL.md:51`),与本包「附图即申请文件一部分」的定位不同——收编前必须先定:mermaid 是只服务 Word 交付的框图,还是替代 dot。建议:专利-drawings 维持 dot 黑白线条结构图(dot 也补 `-Tpng`),mermaid_render 仅作交付侧框图,且强制单色主题。

3. **命名/路径约定错位**。外部仓库强制交付物主文件名 `{规范化案件名}_{YYYYMMDDHHmmss}.md/.docx`、落盘 `outputs/{案件标识}/`(`prompts/disclosure/invention/disclosure_builder.md` §7.3 第 5 点,`tools/README.md:148,170`);本包是固定文件名 `patent-application/申请信息.md、权利要求书.md、说明书.md、摘要.md、附图/fig1.svg`(`patent-application/SKILL.md` 阶段3)。脚本本身不强制时间戳(是外部 prompt 层要求),但 usage/报错文案硬编码 `tools/shared/` 与「技能根目录 requirements.txt」;mermaid_render→md_to_docx 子进程硬编码同目录脚本(`mermaid_render.py:292-341`)。收编需:① 定目录布局(建议 `skills/tools/conversion/` 或包根 `tools/`);② 决定是否引入时间戳交付命名;③ 改 usage 文案与子进程路径。

4. **与 ADR-0003 delegation-first 的张力**。ADR-0003(`docs/adr/0003-delegation-first.md`)明确「set owns only authoring/decision logic」、不持有检索/抓取基础设施;收编 6 个 Python 脚本(+可选 Node/mmdc)是本包第一批**重量工具**。严格讲这不算检索基础设施(检索仍委托外部),但属于新类别——建议先补一条 ADR(「交付/格式转换基础设施例外」)再动手。依赖清单:python-docx、mammoth、python-pptx、latex2mathml、matplotlib、PyYAML(+mmdc/puppeteer),已不是「thin」。测试基建也要新建:外部用 `python -m unittest discover -s tests -t .` 从仓库根跑(`tests/README.md`),脚本互导依赖 `sys.path` hack 与 `from tools.shared.*`(如 `check_formula_plan.py:21-25`),收编后路径约定必须重定。

## 四、收编建议(若采纳)

- **第一批(核心,低风险)**:docx_to_md.py、pptx_to_md.py、md_to_docx.py、math_to_omml.py、math_render.py。目标目录 `skills/tools/conversion/`(与现有 `skills/tools/patents-search` 并列,见 AGENTS.md)。md_to_docx 的兄弟模块 import 用 try/except 双路径,改一行 `tools.shared.` 前缀即可。
- **第二批(需决策)**:mermaid_render.py——先答「Word 交付是否要框图/流程图」「附图是否统一 PNG」「mmdc 依赖可接受吗」;改造后收编。
- **不收编**:formula_paradigms.py、check_formula_plan.py、iteration_dialog_log.py(与现有工作流无对接点)。
- 每脚本收编时:改 usage 文案中的依赖提示、删除/改写指向外部仓库路径的注释、在 `docs/research/` 或 NOTICE 记录来源提交 `ff43eb7` 与 MIT 版权。

## Context

Resolves feasibility research for absorbing `/tmp/patent-disclosure-skill` conversion tooling (2026-08-12, source commit `ff43eb798c3fbde5fd22a532aed8fb62930851ce`, MIT, Copyright (c) 2026 handsomestWei). Primary source = external repo source code, not its README. 本报告为只读评估,未修改任何项目代码。
