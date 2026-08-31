[English](README.md) | [简体中文](README.zh-CN.md)

# Best Paper

Turn an existing research draft into a stronger paper through a convergent revision loop.

> "Like a whole paragraph of caveats and disclaimers and hedging. Sick of it." ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/1uzslsj/chat_gpt_is_becoming_exceedingly_cautious/))

> "It will say 'this one is no good' and when I say 'I think that's the best one' it will reply 'you're right, that's the best'." ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/1vivmzq/how_do_you_make_chatgpt_stop_being_a_yesman/))

> "I am feeding it scientific academic journal materials and it comes with stuff like 'intricate dance' all the time." ([from Reddit](https://www.reddit.com/r/ChatGPT/comments/16ykd9e/how_to_get_chatgpt_to_stop_writing_in_superfluous/))

> "It invents concepts without defining them and bakes them into specs and plans." ([from Reddit](https://www.reddit.com/r/ClaudeAI/comments/1uok58g/claudes_self_invented_technical_jargon_complex/))

> "It corrects that area, but then regresses to worse results in other areas." ([from Reddit](https://www.reddit.com/r/ChatGPTPro/comments/1icbbmz/a_frustrating_limitation_of_chatgpt/))

> "So clearly it is impossible to provide a revision of the draft which will not get a new comment." ([from Reddit](https://www.reddit.com/r/academia/comments/1t6msy8/rant_im_so_fcking_tired_of_my_supervisor_using/))

> "At this point, it feels more work to get ChatGPT to write something than writing myself everything from scratch." ([from Reddit](https://www.reddit.com/r/academia/comments/1siehpx/how_does_anyone_even_rely_on_ai_for_writing/))

AI is genuinely useful for papers. It can read a full draft, trace claims across sections, inspect figures and references, compare versions, and work directly with local files. But ordinary chat puts review, judgment, revision, and self-approval in the same model. That is where defensive writing, yesmanship, inflated prose, invented jargon, regressions, and endless comments come from.

Best Paper separates those decisions and closes them with evidence.

## The loop

```text
audit -> independent judgment -> revision -> independent verification -> repeat
```

The audit must show evidence. Independent judgment looks for counterexamples before accepting a finding. Revision applies only approved changes. Verification reads the changed paper without inheriting the earlier reasoning and checks the whole manuscript for side effects.

This structure prevents the most common failure modes:

* Caveats survive only when the evidence requires them.
* Author, supervisor, and reviewer requests are evaluated, not obeyed automatically.
* Decorative language and private terminology must earn their place.
* Local improvements cannot silently damage claims elsewhere.
* The loop stops when registered checks converge, not when a model runs out of imagination.

## Before you use it

Best Paper needs an existing draft. The research idea must already be developed into some combination of argument, method, evidence, analysis, or experiments.

It does not create a contribution from a bare idea, invent results, or guarantee acceptance.

The manuscript can be LaTeX, Word, Markdown, or another editable local format. The loop is format independent. The final verification always inspects the artifact a reviewer will receive.

## Installation

```powershell
# Windows PowerShell
Copy-Item .\best-paper "$env:USERPROFILE\.claude\skills\best-paper" -Recurse
```

```bash
# macOS or Linux
cp -R ./best-paper ~/.claude/skills/best-paper
```

Restart Claude Code or reload skills after installation.

## Start a paper

Point Best Paper to the real manuscript. Do not ask it to scan a crowded project and guess.

```text
Use Best Paper on this existing draft.

Project root: <path>
Manuscript files: <path or paths>
Canonical editable file: <path>
Target venue: <venue, or unknown>
Paper genre: <research article, survey, theory paper, thesis chapter, ...>

Run Setup only. Wait for my approval before starting the audit loop.
```

## What Setup establishes

Setup gives the loop a stable definition of "better" before any revision begins.

| Setup establishes | Why it matters |
| --- | --- |
| Canonical manuscript files and the render or export path | Prevents edits to stale copies and makes the final artifact verifiable |
| A clean Git baseline | Makes every pass inspectable and reversible |
| The manuscript's actual evidence and source materials | Keeps chat explanations and invented support out of the paper |
| Venue, genre, core storyline, red lines, and no-touch areas | Stops helpful suggestions from turning it into a different paper |
| Current venue rules and comparable accepted papers | Replaces generic model preferences with relevant evidence |
| Page or word-count convention | Keeps length decisions consistent |
| Mechanical checks, work items, and verification paths | Separates objective errors from judgment and gives the loop a stopping condition |
| `AUDIT-LOG.md` | Makes decisions, authorization, and current state resumable across sessions |

Setup ends with author approval. A request for one round authorizes one round, not the full lifecycle.

## What is included

| File | Purpose |
| --- | --- |
| `SKILL.md` | Controls Setup, the four-role loop, authorization, freeze, rollback, and delivery |
| `references/writing-rules.md` | Whole-paper logic, claims, evidence, defensive writing, terminology, citations, and compression |
| `references/audit-method.md` | Counterexample-first assessment, finding quality, side effects, regressions, and convergence |
| `references/abstract-intro.md` | Abstract, introduction, contribution statements, and the paper's entry path |
| `references/figures.md` | Figures, tables, captions, visual hierarchy, and final-size checks |
| `references/polish.md` | Post-freeze language work, AI writing patterns, author voice, and terminology consistency |
| `references/project-log-template.md` | Template for the resumable project state in `AUDIT-LOG.md` |

These references are loaded only when relevant. The README explains the product; the files above contain the operating rules.

## When it stops

Content work closes when all registered verification paths have run, accepted changes are implemented, regressions are clear, and independent verification converges on one candidate version. The author then freezes the content.

Only after that does Best Paper polish language, check figures and layout, fit the venue's length limit, and verify the final submission artifact. Any change that would alter meaning returns to the audit loop.
