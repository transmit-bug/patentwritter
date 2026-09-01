# Skills map (grouped source layout, ADR-0011)

```text
skills/
├── self-service/     自助组:发明人自助链路(1 技能,精简一站式)
├── professional/     专业组:CN 授权链路(入口 + 5 discipline, 6 技能)
├── tools/            工具组:word-delivery(Word 交付,按需)、patents-search(委托检索,可选)
└── patent-standards/ 跨组共享:分型法律锚点(两组均依赖)
```

**分组 = 安装单元**(实测 2026-08-13):

```bash
npx skills add transmit-bug/patentwritter                        # 整包(推荐,10 技能引用全通: 1+6+2+standards)
npx skills add transmit-bug/patentwritter/skills/self-service    # 只装自助组 1 技能
npx skills add transmit-bug/patentwritter/skills/professional    # 只装专业组 6 可见技能
```

子路径安装后,跨组引用需一并补装共享与工具:`skills/patent-standards`(两组都需要)、`skills/tools/word-delivery`(Word 交付,按需)、`skills/tools/patents-search`(可选)。也支持 `-s <names>` 按名选择。

另有一条**分组安装面**:仓库根的 `.claude-plugin/marketplace.json` 声明四个分组,self-service / professional / tools / standards,供 Claude Code 插件市场按组安装。注意两种安装几何不同:skills CLI 恒按技能名拍平(上面命令),marketplace.json 才保留分组;它列出的是 10 个技能,路径必须与源树同步,技能增删改名时一并更新。

The **self-service chain** is the package's core — single skill `patent` (摄入→分型→四要素→撰写→自检); the professional chain lives under `professional/`, see package-repo `docs/guide/README.md`.

`patent` is the sole self-service skill; material ingestion is handled inline in its Step 0 (no separate `conversion` skill). The workspace is hierarchical in the inventor's project: one directory per application under `patents/<patent-name>/` (case root; directory name = target product, frozen at routing), each holding `drafts/`, `figures/`, `deliverables/` plus the case-local `.patent/` support layer — a **workspace name, not a skill name**.

## Skill roles

| Skill | Role | Owns |
|---|---|---|
| `self-service/patent` | 精简一站式 | 摄入→分型→四要素访谈→交底书/申请文件撰写→附图→自检，一站替代原 6 技能 |
| `patent-standards` | shared service | standards index and on-demand anchors |
## Three flows (精简一站式)

**Control flow** — `patent` 一站驱动：

```text
patent: 摄入(内联 docx/pptx→md) → 分型(A技术/B综述) → 四要素访谈 → 撰写(交底书/申请文件) → 附图(dot) → 自检(check-report.md)
  └─ 按需 → word-delivery (Word 交付, 仅用户显式要求或 word-export: agreed)
  └─ 可选 → patents-search (Valyu US/EP 语义检索, CN 走 CNIPA 手工)
```

**Data flow**:

```text
materials → .patent/materials/ → drafts/application-info.md + 技术交底书.md (+ 权利要求书/说明书/摘要) → figures/ → drafts/check-report.md
      ──► deliverables/*.docx (仅经 word-delivery 按需生成)
```

**Knowledge flow**: `patent` → `patent-standards/references/<per-type anchor>` (法律锚点单一来源)

## Route ownership

- **patent** 一站拥有全流程：摄入、分型、访谈、撰写、附图、自检。
- **Standards** 拥有法律锚点位置；下游只指针不复制。
- **word-delivery** 拥有 Word 验收与单源规则（drafts 唯一真相，deliverables 可再生）。

Case facts, papers, formulas, citations, and experimental data belong to the project support workspace and drafts, never to this package's skills.
