[English](README.md) | [简体中文](README.zh-CN.md)

# Best Paper

通过一个能够收敛的修改 loop，把已有论文初稿推进到更好的投稿版本。

> "Like a whole paragraph of caveats and disclaimers and hedging. Sick of it."  
> 中文：整整一段都是限定、免责声明和闪烁其词，真的受够了。 ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/1uzslsj/chat_gpt_is_becoming_exceedingly_cautious/))

> "It will say 'this one is no good' and when I say 'I think that's the best one' it will reply 'you're right, that's the best'."  
> 中文：它刚说这个不行，我说我觉得这个最好，它马上又说你说得对，这个就是最好的。 ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/1vivmzq/how_do_you_make_chatgpt_stop_being_a_yesman/))

> "I am feeding it scientific academic journal materials and it comes with stuff like 'intricate dance' all the time."  
> 中文：我给它的是科学论文材料，它却总写什么“错综复杂的舞蹈”。 ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/16ykd9e/how_to_get_chatgpt_to_stop_writing_in_superfluous/))

> "It invents concepts without defining them and bakes them into specs and plans."  
> 中文：它凭空发明概念，又不下定义，然后直接塞进规范和计划里。 ([from Reddit](https://www.reddit.com/r/ClaudeAI/comments/1uok58g/claudes_self_invented_technical_jargon_complex/))

> "It corrects that area, but then regresses to worse results in other areas."  
> 中文：它修好了这一处，其他地方却退回到更糟的状态。 ([from Reddit](https://www.reddit.com/r/ChatGPTPro/comments/1icbbmz/a_frustrating_limitation_of_chatgpt/))

> "So clearly it is impossible to provide a revision of the draft which will not get a new comment."  
> 中文：看来根本不可能交出一个不会再招来新意见的版本。 ([from Reddit](https://www.reddit.com/r/academia/comments/1t6msy8/rant_im_so_fcking_tired_of_my_supervisor_using/))

> "At this point, it feels more work to get ChatGPT to write something than writing myself everything from scratch."  
> 中文：到这个地步，让 ChatGPT 写东西感觉比我从头自己写还费劲。 ([from Reddit](https://www.reddit.com/r/academia/comments/1siehpx/how_does_anyone_even_rely_on_ai_for_writing/))

AI 对论文工作确实很有用。它能通读初稿，追踪跨章节论断，检查图表和引用，对比版本，也能直接处理本地文件。问题在于，普通对话让同一个模型同时负责找问题、做判断、改稿和给自己验收。过度防御、迎合、华丽包装、自造术语、局部回归和永远改不完，往往就发生在这里。

Best Paper 把这些决定分开，再用证据让修改真正闭合。

## 核心 loop

```text
审计 -> 独立裁决 -> 修改 -> 独立验证 -> 重复
```

审计必须给出证据。独立裁决先找反例，再决定问题是否成立。修改只执行获准的项目。独立验证不继承前面的推理，直接阅读改后的论文，并检查改动对全文的影响。

这套结构针对的正是开头那些问题：

* 只有证据需要时才保留限定，不以严谨为名不断自我削弱。
* 作者、导师和审稿人的要求都要判断，不能自动服从。
* 华丽语言和私造概念必须证明自己确有必要。
* 局部改善不能悄悄破坏其他章节的主张。
* Loop 在登记的检查路径收敛后停止，不靠模型“再想一条意见”。

## 使用前提

Best Paper 需要一份已有初稿。研究 idea 必须已经落实为某种论证、方法、证据、分析或实验，而不是只有一个尚未展开的想法。

它不会凭空制造贡献，不会虚构结果，也不能保证录用。

稿件可以是 LaTeX、Word、Markdown 或其他可编辑的本地格式。内容 loop 与格式无关，最终验证会检查审稿人真正收到的成品。

## 安装

```powershell
# Windows PowerShell
Copy-Item .\best-paper "$env:USERPROFILE\.claude\skills\best-paper" -Recurse
```

```bash
# macOS 或 Linux
cp -R ./best-paper ~/.claude/skills/best-paper
```

安装后重启 Claude Code，或重新加载 skills。

## 开始处理一篇论文

直接告诉 Best Paper 哪些是真正的稿件文件，不要让它在混杂的项目目录里猜。

```text
使用 Best Paper 处理这份已有初稿。

项目根目录：<路径>
稿件文件：<一个或多个路径>
权威可编辑文件：<路径>
目标投稿场所：<名称，或尚未确定>
论文类型：<研究论文、综述、理论论文、学位论文章节等>

先只做初始化。等我确认后，再开始审计 loop。
```

## 初始化会确定什么

初始化先给“什么算改得更好”一个稳定答案，然后才允许进入修改 loop。

| 初始化内容 | 为什么需要 |
| --- | --- |
| 权威稿件文件和渲染或导出路径 | 防止改到旧副本，也让最终成品可以验证 |
| 干净的 Git 基线 | 让每一轮都能准确检查和回滚 |
| 论文实际拥有的证据与依据材料 | 防止把聊天解释或虚构支撑写进论文 |
| 投稿场所、论文类型、核心故事、红线和禁改区域 | 防止一条“好建议”把论文改成另一篇论文 |
| 当前投稿要求和同类已接收论文 | 用相关证据替代模型的通用偏好 |
| 统一的页数或字数口径 | 让篇幅判断前后一致 |
| 机械检查、工作项和验证路径 | 分开客观错误与主观判断，并给 loop 明确终点 |
| `AUDIT-LOG.md` | 让决定、授权和当前状态可以跨会话恢复 |

初始化以作者确认结束。请求执行一轮，只代表授权这一轮，不代表授权完整流程。

## 包含哪些文件

| 文件 | 内容 |
| --- | --- |
| `SKILL.md` | 控制初始化、四角色 loop、授权、冻结、回滚和交付 |
| `references/writing-rules.md` | 全文逻辑、论断、证据、防御性写作、术语、引用和压缩 |
| `references/audit-method.md` | 反例优先的裁决、问题质量、副作用、回归和收敛 |
| `references/abstract-intro.md` | 摘要、引言、贡献陈述和论文入口 |
| `references/figures.md` | 图、表、图注、视觉层级和最终尺寸检查 |
| `references/polish.md` | 内容冻结后的语言打磨、AI 写作模式、作者声音和术语统一 |
| `references/project-log-template.md` | 用于生成可恢复项目状态 `AUDIT-LOG.md` 的模板 |

这些附件只在相关阶段加载。README 负责说明这个 skill 是什么，具体执行规则留在对应文件中。

## 什么时候停止

所有登记的验证路径都已运行，采纳的修改已经落实，没有未处理的回归，并且独立验证在同一个候选版本上收敛后，内容阶段才结束。随后由作者冻结内容。

Best Paper 只在冻结后处理语言、图表、版式、篇幅和投稿规范。如果某项修改会改变论文含义，它必须回到审计 loop。
