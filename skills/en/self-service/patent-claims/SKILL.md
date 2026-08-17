---
name: patent-claims
description: Draft and revise the claims (权利要求书) for CN invention patents and utility models, written in Chinese. Start from the four elements — pin down the essential technical features, write the independent claim (preamble + characterizing portion), walk the generalization ladder (上位化), lay fallback dependent claims, and converge on clarity. Use when the user asks to "write claims", "how do I write claims", "independent vs dependent claims", "generalization"; also invoked by the patent-application entry skill.
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Writing the Claims (权利要求书)

Standards pointer: `../patent-standards/references/cn-invention-utility.md`.

Input: the four elements (technical problem / technical solution / distinguishing feature / technical effect) + application type (invention / utility model). If any input is missing, go back and ask — never write on guesswork.

## Type differences (settle the template first)

| Dimension | Invention | Utility model |
|---|---|---|
| Independent-claim subject | Product / method / system | **Product only** (shape / construction / combination) |
| Method features | Algorithm / process allowed | **No method steps as main features**; only known method names as qualifiers |
| Reference numerals | Allowed, in parentheses | Same |
| Typical claim count | 8-15 | 5-10 |

## Five drafting steps, each with a completion standard

### Step 1 Pin down the essential features → Done when: every retained feature passes the deletion test

For every feature in the solution ask: **if deleted, is the technical problem still solved?** Yes → non-essential, demote to a dependent claim or drop it. The independent claim keeps only the features without which the problem cannot be solved.

- Essential features come from the **problem**, not from implementation detail: to solve "unreliable recognition", the essential thing is a "recognition mechanism", not "camera mounted in the top-left corner".
- Effect — distinguishing vs enhancing: a feature that only boosts an effect without affecting problem-solving is not essential.

### Step 2 Write the independent claim → Done when: single paragraph, preamble + characterizing portion, one full stop

Format:

```
一种<上位主题名称>,包括:<与最接近现有技术共有的必要特征>;其特征在于:<区别于现有技术的特征>。
```

- Preamble: subject name + shared features. The X in "一种<X>" uses a **generic/upper-level term** (see Step 3), not the product name.
- Characterizing portion: introduced by "其特征在于". If the distinguishing feature is not yet clear, go back to Stage 1 and ask — don't force it.
- Place the independent claim before dependent claims and keep the claim set internally consistent.

### Step 3 The generalization ladder (上位化) → Done when: every term passed the three questions

Abstract the concrete implementation level by level along "the essence of the problem", ordered narrow → broad:

```
层1 具体实现  手机APP通过蓝牙连接手环,读取心率
层2 中间概括  客户端与可穿戴设备通信,获取生理数据
层3 功能概括  第一终端与第二终端通信,获取用户状态数据
```

**The three-question test** (every level up must pass):
1. Does the generalization **still solve the original technical problem**? → No: step back one level.
2. Is it **supported by an embodiment in the specification**? claims shall be supported by the description → No: either add an embodiment or step back.
3. Is it a **pure functional limitation**? (only states "what it does", not "how it does it") → Yes: at least one implementation path must be disclosed, otherwise unsupported/unclear.

- The generalization direction is set by the essence of the problem: if the problem is about "interaction between the user and a data service", app→client holds; if it is about "Bluetooth low-energy power saving", app→client fails and that limitation must be kept.
- Use levels 2-3 for the independent claim; all level-1 implementation detail sinks into dependent claims.

### Step 4 Fallback dependent claims → Done when: every embodiment has a matching fallback, and the citation rules are respected

Dependent claims = **fallbacks**: when the over-broad independent claim is rejected, a dependent claim takes over. Defend in three directions, ordered by commercial importance:

| Direction | Technique | Example |
|---|---|---|
| Refinement | Fold implementation detail into a dependent claim | independent "处理单元" → dependent "所述处理单元包括特征提取模块和匹配模块" |
| Variants | One claim per alternative implementation | independent "第一通信方式" → dependent "所述第一通信方式为蓝牙" + "为Wi-Fi" |
| Enhancement | Add functional features | independent solution + dependent "还包括:根据用户反馈更新所述匹配模型" |

Citation rules:
- A dependent claim may only cite an **earlier** claim.
- A multiple dependent claim must cite a single alternative: "根据权利要求1或2所述的…".
- A multiple dependent claim **must not** serve as the basis of another multiple dependent claim ("根据权利要求3或4所述的…" violates this if claim 3 is multiple).
- The citation part restates the full subject: "根据权利要求1所述的一种<主题>…".

### Step 5 Clarity convergence → Done when: every claim passes the table below, zero hits

| Check | Rule |
|---|---|
| Terms consistent with the specification | if the claims write "传感器", the specification must not write "感应器" for the same part |
| Subject name consistent | independent claim, dependent-claim citation parts, and the specification title must agree |
| "所述" has an antecedent | "所述处理器" must be preceded by "处理器" or "一种处理器" |
| No "as shown in the figures" | unless absolutely necessary, no "如图…所示" |
| Reference numerals in parentheses only | numerals go in parentheses, never as limitations |
| No leading phrases | "优选""例如""最好" are drafting words, not claim content |
| No marketing language | keep claim language technical and bounded |
| One claim, one full stop | Practice: each claim ends with a single period |

## Term conversion table (product words → patent words)

| The inventor says | The claim writes |
|---|---|
| 手机/平板 | 移动终端、便携式计算设备 |
| 服务器/云端 | 服务端、远程处理单元 |
| 按钮/页面/弹窗 | 输入控件、显示界面、提示信息 |
| 微信/支付宝/App | 应用程序、第三方应用接口 |
| 摄像头 | 图像采集装置 |
| 芯片/CPU | 处理单元 |
| "自动" | 根据…确定 / 响应于…(写明触发条件) |
| 口语连接词 | 响应于 / 根据 / 基于 / 配置为 |

## Common mistakes (wrong vs right)

| Mistake | Problem | Fix |
|---|---|---|
| "一种智能门锁,其特征在于:能够自动识别用户" | pure functional limitation, no implementation path | state the mechanism: "包括图像采集模块和与所述图像采集模块连接的识别模块,所述识别模块配置为…" |
| Putting "摄像头装在左上角" into the independent claim | implementation detail locks the protection scope | demote to dependent: "所述图像采集模块设于门体的上部" |
| Mixing "一种X的方法" with "一种X" apparatus claims | mixed subjects, rejected in examination | method claims state steps, apparatus claims state structure, keep separate |
| Multiple dependent claim citing another multiple dependent claim | violation | cite a single claim, or split |
| "优选地,摄像头为红外摄像头" in the independent claim | leading phrase, muddled limitation | delete "优选地"; that limitation goes into a dependent claim |

## Completion standard (before handover)

- [ ] Independent claim passed the Step-1 deletion test; not a pile of implementation detail
- [ ] Step-3 three questions all passed: generalization keeps the problem, specification supports it, no pure functional limitation
- [ ] Every embodiment/variant has a fallback in the dependent claims
- [ ] Step-5 checklist: zero hits
- [ ] No invented prior art, no fabricated data
