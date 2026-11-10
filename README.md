[English](README.md) | [简体中文](README.zh-CN.md)

# BestPaper

Improve a developed academic manuscript so its readers understand the research contribution and can trust the argument and evidence. Start with [SKILL.md](SKILL.md).

## Scope and execution

The [audit router](references/audit/routing.md) preserves 82 detailed checkpoints within 26 specialist tasks, three judgment stages, and three operational check packages. These are a catalog, not 32 or 82 agents on every revision. Verify mechanical edits locally; use dependency-based regression for ordinary revisions; inspect applicable coverage at initial diagnosis, major restructuring, and submission readiness. Reuse requires a valid version and unchanged dependencies.

Mathematical validity, nontrivial insight, whole-paper logic, and basic readability cannot substitute for one another. Coupled checks such as terminology necessity, consistency, first use, symbols, and density are assessed jointly with separate findings. Manuscript and reader outcomes matter more than scores, report counts, or green checklists.

## Files

| Location | Responsibility |
|---|---|
| SKILL.md / SKILL.codex.md | Platform entry points with identical workflow bodies |
| references/writing-guide.md | Normative writing principles |
| references/audit/routing.md | Task selection, scope, evidence reuse and invalidation |
| references/audit/specialties/ | Research, writing and workflow task cards |
| references/audit/checks.json | Checkpoint actions, ownership, triggers and verification |
| references/audit/methods.md | Optional verification techniques |
| references/writing/ | Argument, entry, figure and language methods; optional background is separate |
| references/review/protocol.md | Staged cold reading, comparison review and feedback handling |
| references/project/ | Working-state and project-specific lesson templates |
| references/runtime/ | Activation, stopping and the single reminder prompt |
| scripts/ / tests/ | Standard-library reminder implementation and behavioral tests |

Load only the task-specific details needed. Method references do not create competing rule hierarchies. Keep project-specific lessons in that project; transfer only substantiated general mechanisms into the shared skill.

## Reminders and stopping

Enable the reminder only when entering an authorized autonomous revision loop, and disable it when the loop ends. Reading the skill, registering hooks, a single edit, or a tool call does not start the timer. Claude requires explicit `arm` at loop entry and `disarm` at exit; Codex creates or resumes the thread heartbeat only at loop entry and pauses it at exit.

Claude registers skill hooks on formal Skill or slash-command invocation. The 30-minute check is injected at the next tool-batch boundary, not as a guaranteed interruption of reasoning or a running tool. Codex uses an available native heartbeat, as described in [activation](references/runtime/activation.md). Verify actual activation rather than assuming it.

The model may stop on supported substantive convergence and return the current complete manuscript, reasons, and verification coverage. Final polishing requires the author's explicit decision. Basic readability and substantive repairs are not deferred to that final stage. Disable reminders when complete, paused, waiting for the author, or changing tasks.

## Installation and validation

Claude uses root SKILL.md, including its skill-scoped hooks. For Codex, install the repository under skills/best-paper and replace that installation's SKILL.md with SKILL.codex.md. The bodies match; Codex does not use Claude hooks.

The reminder needs Python 3 on PATH and no third-party package. Run `python -m unittest discover -s tests -v` for behavioral checks. These tests do not establish end-to-end delivery inside a real client; confirm the activation receipt in the actual manuscript session.
