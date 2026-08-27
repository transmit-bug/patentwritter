# AGENTS.md

> 本仓库是一套**专利全生命周期生态**的技能工厂——**围绕专利构建一整套声明周期 skills**，覆盖 想法/材料 → 交底书 → 申请文件与附图 → 自检与交付 → 递交与补正 → 授权攻防。交付物是 `skills/` 16 技能，消费方以 `npx skills add transmit-bug/patentwritter` 安装到自有项目后运行全链路。

## 定位

- **工厂**：按薄技能 + 委托 + 单一来源组织，定边界与质量门；任务是让这套生态在别处好用。
- **非工作区**：验证用例建于临时目录，跑通即清，不在仓库内留 `patents/`。
- **目标（生命周期·生态）**：围绕专利声明周期，把发明人的碎片材料（口述/PPT/论文/代码/照片）收敛为可追溯、可分工、可验证的专利资产——交底书为底座枢纽，申请文件闭环支撑，授权链路可攻防，生态价值在于全链路可续跑可验证。
- 消费方手册见 `docs/usage/`，架构见 `docs/usage/architecture.md`。

## 结构

```
skills/self-service  6：intake(前门+编排) / exploration / drafting / drawings / compliance / filing
skills/professional  6：prosecution(入口) + 5 discipline
skills/tools         3：conversion / word-delivery / patents-search
skills/patent-standards  1：分型法律锚点单一来源
```

## 产出在消费方是什么（生命周期生态）

一句话链路：`任意材料 → 交底书底座(四要素+可复现+区别清晰) → 申请文件(支撑闭环) → 自检 gate → 交付/递交 → 授权攻防`，贯穿声明全周期。自助入口 `patent-intake`，授权入口 `patent-prosecution`，生态而非单点工具。

- **交底书底座**：四要素完整/单文件可复现（tight）/区别清晰/来源诚实，定义见 `patent-intake/references/disclosure-document.md`。
- **申请文件与附图**：撰写/附图各有质量门与产物，阶段清单 `drafts/application-info.md` 为状态机，可中断续跑。
- **诚实可验证**：背景技术只写三类素材，法律断言指向 `patent-standards` 分型锚点，缺依据 fail loud；五横切标志写入 `application-info.md` 供下游只读。
- 详情见 `docs/usage/README.md` 与 `docs/usage/writing-disclosure.md`。

## 如何改

1. **定边界**：判归属技能，各管一件产物、零横向调用、经产物文件衔接。
2. **改源码**：只改 `skills/<group>/<name>/SKILL.md` 及 `references/`，本地定义术语。
3. **守规则**：见下节。
4. **落点验证**：在临时空目录 `npx skills add .` 验拍平与引用，必要时跑最小链路验端到端。
5. **同步清单**：改名增删时更新 `.claude-plugin/marketplace.json`。

## 硬规则

- **以安装态为验收态**：以拍平到空白消费项目的体感为准——引用可解析、技能可发现、产出可追溯可续跑、异常可感知。源码自洽不算完成，安装态好用才算完成。
- **项目级安装**：始终在目标项目目录执行 `npx skills add .`，产物落于项目本地 `.agents/skills/`。本项目不使用全局目录。
- **拍平引用**：正文写 `../<skill>/`，`references/` 内再加一级 `../`，改后以安装副本逐条验证。
- **自包含**：正文与 `references/` 零 `ADR`/`CONTEXT`/`docs/`/`package-repo` 引用。
- **可复现与控量**：技能自包含、无外部上下文依赖；全新空会话 `npx skills add .` 后可复现，不经 `herdr` 等通道传递提示词；过程控制词、豁免与分型仅在 `application-info.md` 记录，交付物以模板槽位为准、无模板回退中性；清单可豁免、分型可变，符合最佳实践即默认干净。

---

## Agent skills

### Issue tracker

`gh` 管理，见 `docs/agents/issue-tracker.md`。

### Triage labels

见 `docs/agents/triage-labels.md`。

### Domain docs

见 `docs/agents/domain.md`（`CONTEXT.md` + `docs/adr/`）。
