# AGENTS.md

> 本仓库是「专利全生命周期 15 技能」的**技能工厂**，交付物是 `skills/`。消费方以 `npx skills add transmit-bug/patentwritter` 安装到自有项目后运行全链路。

## 定位

- **工厂**：按薄技能 + 委托 + 单一来源组织，定边界与质量门。
- **非工作区**：验证用例建于临时目录，跑通即清，不在仓库内留 `patents/`。
- 消费方手册见 `docs/usage/`，架构见 `docs/usage/architecture.md`。

## 结构

```
skills/self-service  6：intake(前门+编排) / exploration / drafting / drawings / compliance / filing
skills/professional  6：prosecution(入口) + 5 discipline
skills/tools         3：conversion / word-delivery / patents-search
skills/patent-standards  1：分型法律锚点单一来源
```

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

---

## Agent skills

### Issue tracker

`gh` 管理，见 `docs/agents/issue-tracker.md`。

### Triage labels

见 `docs/agents/triage-labels.md`。

### Domain docs

见 `docs/agents/domain.md`（`CONTEXT.md` + `docs/adr/`）。
