# ADR-0011: 技能源树按功能分组——分组即安装单元

- 状态:Accepted (2026-08-13)
- 取代:ADR-0010(拍平布局;其"依赖图不被目录切开"的观察成立,但结论错误——分组的价值在安装侧,不在依赖侧)
- 关联:ADR-0004(类别布局)、ADR-0009(技能合并)

## 背景

ADR-0010 把 `skills/en/<category>/<name>/` 拍平为 `skills/<name>/`,理由是依赖横跨分组。但分组的真正用途是**安装侧**:skills CLI 支持子路径安装(`skills add <repo>/skills/<group>`,实测 2026-08-13),分组目录就是消费者按功能选择性安装的单元——自助用户只装 self-service 组,代理人只装 professional 组。拍平后该能力丧失,且 16 个同级目录无法区分功能。

语言命名空间层(`en/`)在单一语言下是纯开销,维持移除。

## 决策

1. **源树 = 功能分组**:`skills/self-service/`(5 技能,自助链路)、`skills/professional/`(8 技能:入口+5 discipline+2 隐藏 US)、`skills/tools/`(conversion、patents-search)、`skills/patent-standards/`(跨组共享,两组均依赖)。
2. **分组即安装单元**:`npx skills add <repo>/skills/self-service` 只装 5 个自助技能;`/skills/professional` 只装 6 个专业可见技能(隐藏 US 不装);整包 `npx skills add <repo>` 全装。也支持 `-s <names>` 按名选择。
3. **共享依赖须一并安装**:子路径安装 self-service 后,`../patent-standards/`、`../conversion/` 等跨组引用需补装对应目录(README 安装一节给出完整命令);推荐普通用户直接整包安装(14 技能,开销小,引用全通)。
4. **正文引用仍按安装几何(flat)书写**:安装器把任何分组的技能都拍平到 `<agent-skills-dir>/<skill-name>/`,因此正文 `../<skill-name>/` 引用在安装副本恒解析;分组源树中跨组引用悬空属预期(组织结构 ≠ 引用深度)。验证以安装副本为准。

## 后果

- 恢复"源码分组、安装拍平"双层事实:分组服务人浏览与选择性安装;引用服务运行时解析,两者互不绑架。
- ADR-0010 的 flat 布局与"源树安装副本同构"条款作废;引用验证流程回到安装副本单侧。
- `skills/README.md` 承担分组地图 + 安装命令说明;各组职责词汇(B 组/A 组/工具/共享)重新对应真实目录。
