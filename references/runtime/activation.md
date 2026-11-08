# BestPaper 提醒运行方式

提醒辅助当前已授权的论文工作，不能保证模型遵守规则，也不能替代真实改稿及独立核验。提醒正文在reminder.md；只有一个正文版本。

## Claude Code

Claude版本采用技能级PostToolBatch hook；不修改用户全局settings。需要正式调用 `/BestPaper` 或Skill工具，单独Read技能文件不会注册hook。新安装若当前会话已缓存旧技能，重新正式调用并检查是否出现实际启用确认；仍无确认则在新会话调用，不能报“已启用”。

首次工具批后，脚本会把session_id与cwd绑定并确认启用。之后默认1800秒阈值，只在下一工具批结束、下一模型请求之前注入正文；未到期静默。纯思考、没有工具或长工具尚未返回时，不保证按时钟到点触发。原生Cron只在空闲时触发，不作为这里的替代。

新用户消息先暂停本会话旧提醒，提示中给出真实会话ID和目录。确认仍属于同一已授权论文任务时显式运行arm恢复，其他任务保持暂停。同一会话重新调用技能时，旧inactive状态不会自行开启，也应在确认本轮授权后运行arm；首次自动启用不是恢复动作的替代。子代理不启用本机制。暂停、完成或转任务时显式停用；SessionEnd也做静默停用。状态在系统临时目录，按会话与项目隔离，不保存论文正文。

需要Python 3，并让hook中的command解析到实际解释器。仓库默认使用PATH中的python；如果环境仅提供python3，则将hook command改为python3。本地可使用已确认的解释器绝对路径，但不要把个人机器路径提交到共享配置。

下面的<skill-directory>替换为实际技能目录；ID和cwd取真实hook确认，不能猜：

```text
python "<skill-directory>/scripts/reminder.py" status --session-id '实际会话ID' --cwd '实际绝对项目目录'
python "<skill-directory>/scripts/reminder.py" arm --session-id '实际会话ID' --cwd '实际绝对项目目录'
python "<skill-directory>/scripts/reminder.py" disarm --session-id '实际会话ID' --cwd '实际绝对项目目录'
```

正式Skill调用会替换 `${CLAUDE_SESSION_ID}` 为当前会话ID；若读到的仍是占位字符串，说明只是读取文件，不能当作真实ID运行。激活未注册、管理策略拒绝hook或脚本错误时，报告实际限制，不修改安全策略绕过。

如只有停用时间或重启后的接续需要确认，status只说明状态，不证明提醒已经被模型收到。验收要看真实会话的additionalContext及之后的行为。测试可显式传入短间隔，正式默认不得因此改成秒级，也不能把加速测试称为真实30分钟验收。

## Codex desktop

使用当前可用的automation_update工具创建或更新绑定当前论文聊天的heartbeat。间隔30分钟，名称“BestPaper执行纠偏”，prompt使用reminder.md全文并加上本项目/当前稿/已授权范围及状态文件路径。不要创建独立cron任务，不要向别的聊天发送提醒。

先检查当前聊天是否已有同类heartbeat；已有则复用或更新。记录返回的automation ID和实际状态，再说已启用。没有实际成功返回就不能声称提醒已运行。不要手写automation.toml，使用工具当前schema；保存的提示要保持“无偏离安静继续，只有重要进展/实际失败/作者决定才汇报”的意图。

作者新消息改变任务、暂停等待决定或论文交付后，用同一工具暂停本次heartbeat。后续恢复仍按当前授权，不因定时唤醒重开已停止的工作。当前环境没有调度工具时，继续执行动作节点检查并说明没有自动提醒，不用后台sleep或UI按键冒充。

Codex的heartbeat与Claude的工具边界hook不是同一种时序机制；按各自真实工具返回报告，不承诺中途打断模型生成。本次技能维护不等于开启一个论文写作任务，不应给维护聊天挂永久论文提醒。
