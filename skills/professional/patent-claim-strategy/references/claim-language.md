# Claim Language Reference (权利要求语言参考)

On-demand tables for claim drafting and claim amendment. Consult while writing or amending claims (independent-claim wording, generalization, dependent-claim structure).

**Voice-wall application (语体边界, defined in `../../patent-drafting/SKILL.md`)**: these tables apply **only to the claims register (权利要求书)**. The specification narrative paragraphs and the 技术交底书 keep the inventor's engineering register; the conversion into statutory claim language happens once, here at the claims layer.

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
