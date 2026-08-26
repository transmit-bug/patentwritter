# ADR-0014: 披露触发词统一为单篇闭合并止漏 Word

- 状态: Accepted (2026-08-15)
- 关联: ADR-0012(规则双轨)、`skills/self-service/patent-intake/references/disclosure-document.md`

## 背景

`disclosure-document.md` 已迁移为 `单篇闭合` 饱满态（8 要点、图≥2式≥2上不封顶、单篇可复现），但 `AGENTS.md`、`patent-intake`、`patent-drawings`、`patent-drafting`、`word-delivery` 仍保留 `brief-tight` 紧凑态词表（6 行表 + 1-3 式 + 2-3 图、≤5 `[S#]`），导致安装态暴露双触发（方差 bug）、上下文膨胀、单一事实源断裂，且过程控制词泄漏至 Word 封面/页眉/页脚，违背正文硬禁。

## 决策

1. **单触发词**：全链路统一为 `单篇闭合`；`brief-tight` 仅留 git 历史，不在任何常驻文件中出现（含 `AGENTS.md`、skill description、路由表、派发节、drawings Disclosure branch、drafting core-formula gate 注释）。
2. **Word 止漏**：`word-delivery` 封面副标题与页眉/页脚统一发射中性 `技术交底书（供代理机构据此独立起草申请文件）`，不含任何过程控制词；控制词仅保留于 `drafts/application-info.md` 与 skill 内跟踪，不进 Word 正文/封面/页眉/页脚/表格。
3. **预算统一**：`单篇闭合` = 8 要点饱满展开、图≥2式≥2上不封顶；`brief-tight` 预算不再作为现行规则。

## 迁移注记

`brief-tight (V1, tight: 1-3 式 / 2-3 图 / 六行表 / ≤5 [S#]) → 单篇闭合 (V2, saturated: 8 要点饱满展开, 图≥2式≥2上不封顶, 单篇自包含)`. 历史差异以 git diff 为准，本文件为唯一常驻迁移说明；不在 `skills/` 另立废弃引用文件以免再增方差。

## 后果

- 安装态 `grep -rn "brief-tight" skills/ AGENTS.md` 零命中；`grep -rn "单篇闭合" skills/` 仅 disclosure-document Leading word 与 intake/drawings/drafting 触发指针命中，Word 发射路径零命中。
- 披露链路单一预算、单一词表，复跑一致性提升；Word 交付语言纯净，代理机构审阅无过程元干扰。
- 后续披露相关改动以 `disclosure-document.md` 为单一事实源，薄技能纪律不变。

## 验证

`npx skills add . --skill '*' --agent '*' -y` 于临时空目录验证 `.agents/skills` 无 `brief-tight`；单篇闭合仅 disclosure-document/intake 触发指针；抽样 `drafts/技术交底书.md` 与 `deliverables/*.docx` header/cover 零过程词。
