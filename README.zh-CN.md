[English](README.md) | [简体中文](README.zh-CN.md)

# BestPaper

改进已有且已形成论证或证据的论文，让读者看懂真实价值并信任研究。执行入口是[SKILL.md](SKILL.md)。

## 先按当前任务选择范围

[审计安排](references/audit/routing.md)将81个检查点映射到26个可选专业专项、2个判断环节和3组操作核验。这是任务目录，不是每轮31次或81次审计。纯机械微改核实际差异；普通修订沿受影响对象和依赖回归；首次诊断、大重构及送审前检查适用范围。复用须有版本与依赖依据，不能只凭旧版通过。

数学证明、平凡推理、整篇逻辑和基本易读性不能互相代替。术语、句式等需要一起权衡的检查联合执行，分项留证。实际作品与读者效果决定是否完成，不以报告数、绿灯或胜场验收。

## 文件职责

```text
SKILL.md / SKILL.codex.md       执行入口（正文一致，运行环境不同）
references/writing-guide.md    写作规则主源
references/audit/              专项选择、80检查点、核验方法
  routing.md                  完整检查/增量回归/证据复用
  specialties/                研究、写作、流程专项卡
  checks.json                 逐项动作、归属、触发和复核
  methods.md                  证明、反例、删除、表格等方法
references/writing/            论证、入口、图表、语言方法
  background/                 可选来源背景，不作为执行规则
references/review/protocol.md   冷读、三级盲审与意见处理
references/project/            工作状态与项目经验模板
references/runtime/            激活、停止与唯一提醒正文
scripts/reminder.py            Claude工具边界提醒器
tests/test_reminder.py         提醒器行为测试
```

规则只在[写作指南](references/writing-guide.md)维护；[执行安排](references/audit/routing.md)决定任务和复用；专项卡与检查点提供具体动作；写作和核验附件提供按需方法，不另立硬规则体系。每个项目自己的经验文档保存具体事故，只有可迁移机制进入BestPaper。

## 提醒与停止

提醒只在进入已授权自动循环时启用，循环结束即停用；读技能或单次改稿不启动。Claude正式调用Skill或`/BestPaper`只注册hook，进入循环时由主会话显式arm，之后每满30分钟，在下一工具批结束时向当前模型注入[纠偏提醒](references/runtime/reminder.md)。不保证中断纯思考或尚未结束的长工具。Codex按[运行说明](references/runtime/activation.md)使用可用的原生heartbeat，工具不可用须如实说明。提醒不保证模型永远遵守，也不替代实际验证。

有依据判断实质性收敛可以停止并交回当前稿、理由与检查范围。最后润色由人工明确决定；基础理解障碍和必要论证修复不等待最后润色。完成、暂停、等待作者或切换任务时关闭提醒。

## 安装与检查

Claude使用根目录SKILL.md（含技能级hooks）。Codex将仓库安装到skills/best-paper后，用SKILL.codex.md替换该安装的SKILL.md；两份正文一致，Codex不使用Claude hooks。

提醒器只用Python标准库。确认`python`指向Python 3；运行`python -m unittest discover -s tests -v`检查提醒器行为。命令行测试不等于真实客户端的端到端注入验证，仍须在实际论文会话确认启用回执。
