# 查新指南(可选,撰写背景技术前)

查新是**可选、建议**步骤:撰写背景技术前跑一轮,结果只写真实返回(诚实红线,执行版见 `../../patent-specification/SKILL.md` 段2)。在阶段2 类型判断后、阶段3 撰写前执行。检索记录按 `.patent/` 三档约定落盘(见 patent-application/SKILL.md 的「.patent/ 支撑层工作目录」节):**检索记录与结果落 `.patent/queries/`**,素材落 `materials/`,引用清单落 `sources/`。

## 主路径:委托检索工具(Valyu)

调用 `../../../tools/patents-search/SKILL.md`(脚本路径解析/API key 配置/输出格式/错误处理全在该文件,不在此重复):

```bash
"$PATENTS_SCRIPT" "<自然语言查询>" <maxResults>   # 返回 results[].title/url/content/relevance_score
```

- 首次运行遇 `"setup_required": true`:向用户要 Valyu API key(https://platform.valyu.ai)→ `scripts/search setup <key>` → 重试。
- **CN 覆盖警示**:Valyu 专利数据源按官方清单仅覆盖 **US (USPTO) + EP (EPO)**,CN 命中不保证。
- 需要 CN 现有技术时,用下面的国知局人工检索补充。

## 补充路径:国知局人工检索(声明外部源)

CNIPA 公布公告系统是声明外部源(目录条目见 `../../../patent-standards/references/catalog.md`),只引用源信息与引用锚点,包内不带爬虫代码。人工浏览器步骤:

1. 浏览器打开首页 http://epub.cnipa.gov.cn/,等待反爬校验放行(该站有动态 JS 反爬网关;**遇验证码直接切路径,不硬闯**);
2. 输入关键词,勾选类型(发明公布/发明授权/实用新型/外观设计);
3. 逐条记录命中:标题 + **公开号/公告号**(如 CN209861402U)为引用锚点;写背景技术时注明"CNIPA 公布公告系统检索所得";
4. 可选:用 agent_browser 等浏览器自动化工具代跑上述步骤(真浏览器天然过网关,结果同样按诚实红线处理);
5. 被拦/超时:改用 Google Patents(加 `country:CN`)或 WebSearch。

## 落盘

每次查新把检索记录写入 `.patent/queries/`(Valyu 原始 JSON 输出、人工检索命中表),与素材(`materials/`)、引用清单(`sources/`)分治,便于背景技术引用真实公开号时对账。
