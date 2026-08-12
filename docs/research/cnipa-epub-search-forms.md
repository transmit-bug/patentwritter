# CNIPA 公布公告系统 (epub.cnipa.gov.cn) — 可用检索形态调研

调研对象：国知局 **公布公告系统** `http://epub.cnipa.gov.cn/` 的可用检索形态，以及
"声明外部源 (declared external source)" 框架下本包应如何呈现它。

- Scope：本包不建检索（CONTEXT.md `Delegated search`，见下）前提下，评估三种呈现形态 —
  (a) 纯文档指引 / (b) 薄封装脚本 / (c) 不采用。
- 证据方法：**一手证据为主** — 第三方爬虫源码（`/tmp/patent-disclosure-skill/tools/crawl/`，已 clone 仓库，
  其内部实现 = 站点端点的最直接证据）、2026-08-12 对本机 curl 实测（多次重试、浏览器 UA、短超时）、
  Valyu 官方文档（docs.valyu.ai，2026-08-12 抓取）。网络不稳时以源码为准并明示。
- Verified on 2026-08-12（curl 实测 + 文档抓取）。

> 结论速览：epub 站入口被**动态 JS 反爬网关**（瑞数风格 WAF）保护，实测无稳定公开查询 URL / 官方 API 可直连；
> 第三方爬虫用 Playwright 真浏览器 + 轮询等待 #searchStr 的方式通过，正是本包 `Delegated search` 明令禁止的
> "in-repo harness"。**推荐 (a) 纯文档指引**：把 CNIPA 声明为一个"人工操作的外部源"，文档只写源信息与
> 检索/引用规则，不随包带任何爬取代码；(b) 无稳定查询 URL 可构造，不成立；(c) 作为退路保留。

---

## 1. 第三方爬虫如何工作（/tmp/patent-disclosure-skill/tools/crawl/）

仓库布局（已 clone 至 `/tmp/patent-disclosure-skill`）：

| 文件 | 作用 |
|---|---|
| `tools/crawl/cnipa_epub_search.py` (191 行) | 一步「检索+解析」CLI；`EPUB_HITS_JSON:` 单行 JSON 输出约定 |
| `tools/crawl/cnipa_epub_crawler.py` (337 行) | Playwright 抓取核心；`fetch_epub_result_html` / `search_epub_keyword` |
| `tools/crawl/cnipa_epub_parse.py` (260 行) | 结果页 HTML → 命中列表（标题/公开号/详情链接/摘要） |
| `tools/crawl/requirements-cnipa.txt` | 仅一行：`playwright>=1.40.0` |

**技术栈：HTTP？HTML 解析？Playwright？** — 三者都有，但**渲染必须走 Playwright**。

- 站点入口 `EPUB_BASE = "http://epub.cnipa.gov.cn/"`（crawler L77，注意是 **http** 非 https）。
- 检索框是首页表单 `#indexForm` / `#searchStr`（crawler L3）。流程：
  1. `page.goto(EPUB_BASE, wait_until="load")`（L119-123）；
  2. **轮询等待 #searchStr 出现** — 每 3 秒一次，上限 `EPUB_WAF_MAX_WAIT_SEC` 默认 180s
     （L124-131；docstring L14 明言：站点先过「前端脚本/WAF 一类逻辑」，未通过前不出现检索框，
     **不是用 requests 直接 POST 能等价替代的步骤**）；
  3. 勾选类型复选框（`fmgb` 发明公布 / `fmsq` 发明授权 / `xxsq` 实用新型 / `wgsq` 外观设计，
     patent_type.py L27-34）后 `page.fill("#searchStr", kw)` + 对 `#indexForm` 执行 `el.submit()`
     （crawler L194-207），等结果页导航 **commit**；
  4. 等结果页 DOM 就绪：title 为「专利查询结果展示」或「无查询结果」（L79-80，注释指明结果页为
     **`/Dxb/IndexQuery`**）且 `#result` 出现列表/零结果文案（L84-92 `_RESULT_PAGE_READY_JS`）；
  5. `page.content()` 取整页 HTML（`_safe_page_content` 防导航竞态重试，L134-151）。
- 解析纯正则（parse.py）：表格行 `<tr>` 优先（L63-98）；新版卡片布局 `div.item`/`h1.title`/
  二维码 `div.qrcode` 的 `title="http://epub.cnipa.gov.cn/patent/CN…"`（L101-149，L144 正则，
  L160 构造 `f"{base}/patent/{pub_number}"` 详情链接）；兜底抓 `<a href>` 中含 `/dxb/` `/sw/` `/patent/`
  `detail` `show` 的链接（L152-196，L210）。
- 浏览器指纹伪装：Chromium 无头 + `--disable-blink-features=AutomationControlled`（L262）+ 桌面 Chrome/120
  UA + `locale="zh-CN"` + 1280x900 视口（L270-272）。
- CLI（search.py）：默认按空白拆多词、**每词一次 Playwright 运行**，再按公开号去重合并（L58-75），
  `_MAX_TERMS = 8`（L40）；stdout 仅一行 `EPUB_HITS_JSON:`（L183），stderr 为 ASCII 提示，便于 Agent 抓取。

### 1.1 引用到的端点/URL（源码原文）

- 首页：`http://epub.cnipa.gov.cn/` — crawler L77 `EPUB_BASE = "http://epub.cnipa.gov.cn/"`
- 结果页：`/Dxb/IndexQuery` — crawler L78 注释 `# 国知局 /Dxb/IndexQuery 结果页 <title>；改版时须同步单测`
  （真实提交是浏览器内表单 submit，无公开可直连的查询串 URL）
- 详情页：`http://epub.cnipa.gov.cn/patent/CN…`（公开号形态）— parse L144 正则、
  L160 `link = f"{base}/patent/{pub_number}"`

### 1.2 脆弱点（自源码归纳）

1. **动态 JS 反爬网关（WAF）**：docstring 自述首页有「前端脚本/WAF 一类逻辑」，未通过不出现 `#searchStr`；
   轮询等待上限 180s，超时即失败（L14, L124-131）。`--disable-blink-features=AutomationControlled`
   只是"减弱暴露，效果因站点升级而变，非保证"（L25）。**我 2026-08-12 curl 实测证实**：首页交替返回
   HTTP 202（含瑞数风格动态 JS challenge，见 §2）与 HTTP 400 空体。
2. **页面结构改版**：三套解析路径（表格行/卡片 div.item/兜底 a-href）都依赖具体 DOM 结构与正则；
   L78 明言改版"须同步单测与 _RESULT_PAGE_READY_JS"，常量 `EPUB_TITLE_RESULT/NO_HIT` 是硬编码 title。
3. **反自动化特征对抗升级**：站点可升级检测 headless/自动化开关；脚本**不覆盖**图形/滑块验证码、
   短信验证、强制登录（L26），启用即失效，退路是人工 `PLAYWRIGHT_HEADED=1` 或 WebSearch。
4. 次要：多词每词一次浏览器启动，慢且易被限流；结果只取第一页（无翻页逻辑）；纯 HTTP/正则假设
   UTF-8 页面。

### 1.3 测试覆盖（tests/crawl/）

- `test_cnipa_epub_crawler.py` (130 行)：**全 Mock**（`MagicMock` page）— 类型复选状态、submit 流程
  （`expect_navigation(..., wait_until="commit")` + `wait_for_function`）、`_RESULT_PAGE_READY_JS`
  包含 `#result`/`div.item`/`h1.title`、title 常量。**无任何真实网络测试**。
- `test_cnipa_epub_chain.py` (48 行)：真实联调冒烟 — 直接调 `cnipa_epub_search.main`，默认关键词
  「知识图谱」，需已装 Playwright。属本地联调脚本，非 CI 级。

结论：爬虫对站点改版/WAF 的防护能力**完全无自动化回归保障**，任何站点侧变更都可能静默失败。

---

## 2. 端点实测（2026-08-12，本机 curl）

探测条件：浏览器式 UA（Chrome/120）、`Accept-Language: zh-CN`、`--connect-timeout 8 --max-time 20`，
每 URL 多轮重试（网络不稳）。

| URL | 结果 | 说明 |
|---|---|---|
| `http://epub.cnipa.gov.cn/` | 交替 **HTTP 202**（~2.7 KB challenge 页）与 **HTTP 400**（6 字节空体） | 202 响应体含动态 JS 挑战：`<meta id="K5MK4FPPNWrv" content="…">` 指纹 + 某次抓取含 `$_ts.nsd/$_ts.cd` 变量 + 随机名 HttpOnly cookie（`NOh8RTWx6K2dS=…`）与 `WEB=` cookie、`Server: ******` — **瑞数 (RiverSecurity) 风格动态 JS 反爬网关签名**；挑战须由浏览器 JS 引擎执行后回写 cookie 才能放行 |
| `https://epub.cnipa.gov.cn/` | **全部失败** `rc=35 SSL unexpected eof while reading`（3/3 次） | 该主机 https 握手不可用（与此前站点仅 http 的认知一致） |
| `http://epub.cnipa.gov.cn/Dxb/IndexQuery`（GET） | HTTP 400（6 字节） | 无 WAF 会话时直连被拒 |
| `http://epub.cnipa.gov.cn/patent/CN102334155A`（GET） | HTTP 400（6 字节） | 同上 |

**判定：不存在可由普通人类/瘦脚本直接使用的稳定公开查询 URL 或官方 API。**
查询必须是浏览器内表单提交（首页 #indexForm → `/Dxb/IndexQuery`），前置条件是先通过 JS 挑战；
`/patent/CN…` 详情 URL 形如 crawler 所述，但直连同样被 WAF 拦。若后续网络恢复，值得复核的点：
（i）202 挑战的 cookie 是否可被纯脚本求解；（ii）是否存在面向移动端/App 的未公开 API 域名。
就当前证据，**「薄封装打开一个查询 URL」在技术上无 URL 可打开** —— 只能打开首页让人类自己搜。

---

## 3. Valyu 对中国 CN 专利的覆盖（未持有 key，以官方文档为准）

- 本包委托检索工具：`skills/tools/patents-search/` — SKILL.md 声称 "Search the complete global patent
  database"（L17）、"Comprehensive Coverage: Access to global patent data across jurisdictions"（L25）；
  端点 `https://api.valyu.ai/v1/search`，`X-API-Key` 头（L157-159）。
- `scripts/search.mjs`：key 来源 = 环境变量 `VALYU_API_KEY` 或 `~/.valyu/config.json`（L12-37）；
  请求固定 `included_sources: ['valyu/valyu-patents']`、`search_type: 'proprietary'`（L84-93）。
- **实测环境无 key**：`VALYU_API_KEY` 未设置，`~/.valyu/config.json` 不存在 → 未做 API 实测，
  以下为官方文档证据。
- **官方数据源清单（2026-08-12 抓取 docs.valyu.ai/guides/datasources.md）中，专利源仅两个**：

  | Source id | Description | Unlocks on |
  |---|---|---|
  | `valyu/valyu-patents` | **USPTO (US)**, full text with figures. Index updated weekly | Serious Business |
  | `valyu/valyu-patents-epo` | **EPO (Europe)**, full text with figures | Serious Business |

  （`valyu-datasources` 索引，docs.valyu.ai/guides/datasources.md "Data Sources" 表；另见
  docs.valyu.ai/concepts/data-coverage.md "Patents & IP" 节。SKILL.md 的 "global patents"
  表述与官方数据源清单不一致。）
- **判定：Valyu 专利数据源按官方清单仅覆盖 US (USPTO) + EP (EPO)，无列出的 CN 数据源。**
  CN 公开号的命中只能寄望于：(i) 泛 web 检索（`web` 源/Google Patents 索引的中文页面）；
  (ii) `patents-search` 技能之外，本包 patent_type.py（第三方仓库 tools/shared）给出的
  Google Patents `country:CN` 查询提示。**CN 覆盖率未知、且官方清单不支持"CN 专列"** —
  这正是 CNIPA 作为补充声明源的价值所在。

---

## 4. 三种呈现形态对比

### (a) 纯文档指引 — 文档只声明源 + 人工浏览器检索步骤（推荐）

形态：在 `patent-standards` 风格的声明目录或检索技能文档中，新增一条"外部声明源"：
CNIPA 公布公告系统（官方名、URL `http://epub.cnipa.gov.cn/`、管辖区 CN、管辖内容=公布/公告的著录+全文+法律状态、
引用锚点=公开号/公告号如 `CN209861402U`），并附**人工操作步骤**（浏览器打开首页 → 等待挑战放行 →
输入关键词 → 勾选类型 → 记录命中公开号/标题 → 引用时注明"CNIPA 公布公告系统检索所得"）。
不随包带任何抓取/解析代码。

- 可行性：**高**。真人浏览器天然通过 JS 挑战；步骤即 crawler 的 docstring 流程（crawler L8-26）转写为人工版。
- 风险：文档会随站点改版过时（步骤/勾选框 id/结果页形态）；依赖用户诚实记录真实命中（本包
  CONTEXT.md L19 诚实红线要求"检索工具真实返回的结果"——人工记录同样适用）；站点若启用滑块/短信
  （crawler L26 明示未覆盖场景）人工流程也会卡住，文档需给退路（改用 WebSearch/Google Patents）。
- 收益：零代码零 key 零维护成本；**完全符合 "声明外部源" 框架** —— 声明"哪些资料可以查"与"如何查"，
  不负责"在仓库里实现怎么查"（对照 CONTEXT.md L32-33 的 patent-standards 原则，与 L35-37
  "never builds search" 边界一致）。
- 契合度：**最高**。这与包内既有 `patent-standards`（声明目录）模式同构，是唯一不触碰红线且能
  让 CN 权威查新通道可用的形态。

### (b) 薄封装 — 脚本只构造/打开公开查询 URL（不成立）

形态：一个瘦脚本，构造 CNIPA 查询 URL 并在默认浏览器打开，不做结果解析/抓取。

- 可行性：**低 → 不成立**。§2 实测证明：**不存在可直连的查询 URL**。`/Dxb/IndexQuery` 需要 WAF 会话 +
  浏览器内表单提交；裸 GET 返回 400。脚本退化为"打开 `http://epub.cnipa.gov.cn/` 首页"——
  那只是一个启动器，且首页 URL 本身是 http + 挑战页，打开后人类仍需手动操作，与 (a) 相比
  不省任何步骤，却多一个需维护的脚本。
- 风险：容易滑向"再进一步就解析了"的爬虫化（正是 CONTEXT.md L37 "in-repo harness, 自建搜索" 红线）；
  脚本给了 Agent 一个"看起来能查"的入口，实则仍要人类完成全部工作，产生错误预期。
- 收益：几乎为零（唯一收益是少打一次 URL）。
- 契合度：**差**。没有稳定 URL 可构造，框架上也处于声明源与自建检索的模糊地带。

### (c) 不采用 — 包内完全不提 CNIPA

- 可行性：**高**（什么都不做）。
- 风险：包内唯一委托检索工具 Valyu 的官方清单不含 CN 数据源（§3），故 CN 先有技术检索只能依赖
  Valyu 泛 web 结果或用户提供材料；「背景技术」写作的 CN 权威查新通道缺失，诚实红线下的素材池变窄。
- 收益：零维护；边界最干净。
- 契合度：可接受，作为 (a) 不可行时的安全退路。

### 推荐

**首选 (a) 纯文档指引**：声明 CNIPA 公布公告系统为"人工操作的外部声明源"，文档给出源信息 +
人工检索步骤 + 引用规范（引用锚点=公开号/公告号），明确不随包提供爬取能力；(b) 因无稳定公开查询
URL 而技术上不成立（§2 实测）；(c) 保留为退路。同时建议在文档中如实标注：
CNIPA 站有动态 JS 反爬网关、人工操作可能遇到验证码，并保留"改用 Google Patents / WebSearch"
的备选路径（patent_type.py 已提供 `country:CN` 查询提示，第三方仓库 tools/shared/patent_type.py L37-54）。

---

## Sources

**第三方爬虫（已 clone 仓库，路径即源码证据）**
- `/tmp/patent-disclosure-skill/tools/crawl/cnipa_epub_crawler.py` — L3, L14-15, L23-26, L37, L77-80,
  L84-92, L107, L119-131, L134-151, L194-207, L262, L270-272（EPUB_BASE、WAF 轮询、表单 submit、
  /Dxb/IndexQuery 注释、浏览器指纹、未覆盖场景）
- `/tmp/patent-disclosure-skill/tools/crawl/cnipa_epub_parse.py` — L15, L63-98, L101-149, L144, L160, L163, L152-196, L210
- `/tmp/patent-disclosure-skill/tools/crawl/cnipa_epub_search.py` — L10, L22, L40, L58-75, L119-127, L183
- `/tmp/patent-disclosure-skill/tools/crawl/requirements-cnipa.txt` — `playwright>=1.40.0`
- `/tmp/patent-disclosure-skill/tools/shared/patent_type.py` — L27-34（epub 复选框映射）, L37-54（Google Patents CN 提示）
- `/tmp/patent-disclosure-skill/tests/crawl/test_cnipa_epub_crawler.py`（130 行，全 Mock，无网络测试）;
  `test_cnipa_epub_chain.py`（48 行，真实联调冒烟）

**端点实测（2026-08-12，本机 curl）**
- `http://epub.cnipa.gov.cn/` → 交替 HTTP 202（动态 JS 挑战页：`<meta id="K5MK4FPPNWrv">`、
  `$_ts.*` 变量、随机名 HttpOnly cookie、`Server: ******`）与 HTTP 400（6 字节）
- `https://epub.cnipa.gov.cn/` → TLS 握手失败（`rc=35 unexpected eof`）
- `http://epub.cnipa.gov.cn/Dxb/IndexQuery`、`/patent/CN102334155A` → HTTP 400

**Valyu**
- https://docs.valyu.ai/guides/datasources.md — 专利源仅 `valyu/valyu-patents` (USPTO/US)、
  `valyu/valyu-patents-epo` (EPO/Europe)，无 CN 源（2026-08-12 抓取）
- https://docs.valyu.ai/concepts/data-coverage.md — "Patents & IP" 数据覆盖节
- https://docs.valyu.ai/llms.txt — 数据源索引（2026-08-12 抓取）
- `/home/weimou/skillhub/patentwritter/skills/tools/patents-search/SKILL.md` — L17, L25, L157-159
- `/home/weimou/skillhub/patentwritter/skills/tools/patents-search/scripts/search.mjs` — L12-37, L84-93
- 实测环境：`VALYU_API_KEY` 未设置、`~/.valyu/config.json` 不存在（未做 API 实测）

**本包约束**
- `/home/weimou/skillhub/patentwritter/CONTEXT.md` — L32-33（声明目录原则）、L35-37（Delegated search，
  "never builds search, never manages keys"）、L19（诚实红线）、L43-45（Thin skill）
- 风格参照：`docs/research/standards-catalog.md`（声明目录 + 官方位置 + 引用锚点 + Verified 日期）

## Context
调研先行于引入决策：CNIPA 公布公告系统是否/如何作为"声明外部源"进入本包。
对应委托检索工具 Valyu 无 CN 数据源（官方清单），CN 权威查新通道目前缺失。
