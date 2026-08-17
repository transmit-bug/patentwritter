# ADR-0010: 技能源树拍平——取消语言命名空间与类别目录

- 状态:Accepted (2026-08-13)
- 取代/关联:取代 2026-08-13 的语言命名空间约定与 ADR-0004 决策 2 的类别目录布局(`skills/<category>/<name>/`);ADR-0009 的技能合并与引用几何不受影响;issue #25 后续修正

## 背景

ADR-0009 重构后暴露源树结构问题:技能间是**依赖图而非类别分区**——`patent-intake`(自助)依赖 `conversion`(工具)与 `patent-standards`(共享);`patent-claim-strategy`(专业)反向引用 B 组 `patent-drafting`;standards 被所有方向消费。三层源树 `skills/en/<category>/<name>/` 把互相依赖的技能切进不同目录,带来:

1. **组数开销**:语言层 `en/` + 类别层(self-service / professional / tools)= 每个技能路径三层深,单一语言下 `en/` 是纯开销;
2. **安装与源树不一致**:安装副本一直是 flat 的 `<agent-skills-dir>/<skill-name>/`,正文引用按安装几何书写,导致源树中跨技能引用悬空("属预期"的错位);
3. **依赖误读**:目录分组暗示组内自治,实际上 B 组/A 组/工具/共享之间的引用横跨所有类别边界。

## 决策

1. **源树拍平为 `skills/<skill-name>/`**(skills.sh 基础形态):16 个技能目录(5 自助 + 1 共享 + 2 工具 + 6 专业可见 + 2 隐藏 US)全部直挂 `skills/` 下;`en/` 与类别目录删除。
2. **语言信息退到文档**:正文本就全英文、交付物中文;语言不再是目录层,由根 README 说明。
3. **引用几何统一**:正文引用(安装几何 flat)在源树与安装副本**均真实解析**;"源树悬空属预期"的错位条款作废。
4. **组别词汇保留为概念**:"自助(B 组)/专业(A 组)/工具/共享"仍是文档中的角色词汇(ADR-0007/0009 沿用),但不再是目录结构。
5. 隐藏 US 技能(`metadata.internal: true`)平移至 `skills/` 直下,隐藏机制不变。

## 后果

- 安装行为零变化(安装器本就拍平);`npx skills add` 发现路径变浅一层。
- `skills/en/self-service/README.md` 上移为 `skills/README.md`(包级技能关系图,路径改为相对 `skills/`);组内三流模型内容不变。
- AGENTS.md 引用约定简化:源树与安装副本同构,逐条解析验证覆盖两处。
- 历史文档(ADR-0004/0007/0009、docs/research、docs/review、docs/plan)保留旧路径表述,不改写历史。
