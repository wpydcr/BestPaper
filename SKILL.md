---
name: best-paper
description: Turns an existing paper draft into an excellent, submission-ready paper through a convergent loop of audit, independent judgment, revision and verification. Requires a draft whose research idea has already been provisionally developed through an argument, method, evidence, analysis or experiments. It does not write a paper from a bare idea. Use when the user asks to improve, audit, revise, polish or prepare an existing paper for submission, or invokes /best-paper.
---

# Best Paper

The main session is the **process controller** and is not one of the four implementation roles
below. It reads state, checks authorization, dispatches roles, checks that the evidence returned is
complete, decides retry / rollback / commit / stage transition, and keeps the books. It must not
produce candidate findings, write revision text, or stand in for independent verification: a main
session that has already seen the previous rounds' conclusions can only prove self-consistency.

## The shape

```
Setup ──► Audit loop ──► Freeze (author gate) ──► Delivery
            ▲                                         │
            └─ a content change re-enters the loop, ──┘
               and the freeze lifts
```

Four things force that order and nothing else does. Verification must read a frozen state, so
find / judge / execute / verify are ordered, and that ordering is the loop. Polish must not change
meaning, so it runs after the content is settled. Layout must not make content decisions, so it
runs after the content. Nothing runs unattended before the author approves it. Everything else is
scheduling, decided per pass from what the paper needs rather than fixed in advance.

**The work list is the control variable.** It lives in `AUDIT-LOG.md`, it enumerates what this run
covers, and the process advances by striking items off it. Setup builds it, the audit loop closes
its pre-freeze items, and delivery closes the rest.

## Standing dispositions

Seven defaults of the executing model cause most of the damage this process exists to prevent. They
are not rules about the paper; they are behaviours to hold in check while applying the rules about
the paper, and they bind every role at every stage. The first five are one failure wearing five
faces: some local property gets optimized, whether responsiveness to the last thing said, the
defensibility of one sentence, the weight of one phrase or the exactness of one term, and the paper
as a whole pays for it. The last two are a different failure: an operation or a piece of material
gets used without first asking what kind it is.

1. **Proportion is settled before compliance.** The default is to write down whatever was just said:
   a detail mentioned becomes a paragraph, a reviewer's side point becomes a large patch in the
   body. Every addition passes the value ruling of `references/audit-method.md` §6.2, its space
   question included, and one that cannot answer it is not made, whoever asked for it.
2. **A request is judged, not executed.** The default reads "satisfy the requirement" as "accept all
   of it and do the most of it", so a reviewer comment gets answered by addition, anything the
   author voices gets expanded, and more experiments, variables, theory and robustness analysis get
   proposed reflexively (`references/writing-rules.md` A.5 bars the additions it reaches for;
   `references/audit-method.md` §6 and §6.1 settle what an external opinion is worth). Every
   request, from the author or from a reviewer, receives one of four responses: accept, accept in
   part, ask what is meant, or decline with the reason. Which one is decided from the paper's
   positioning first, never from who asked.
3. **State it positively; put the boundaries in one place.** The default hedges in order to look
   rigorous: "this does not mean", "should not be understood as", a limitation volunteered at every
   turn, a defensive clause after every conclusion. Which conditions are kept, which content goes,
   and how the rest is written are `references/writing-rules.md` chapter 2, A.4 and A.9.
4. **Density, not decoration.** The default reaches for weight: a "scalpel", "a new frontier",
   modifiers stacked in pursuit of exactness. What is wanted instead is information density,
   academic recognizability, plain language and argumentative efficiency. The pattern set, metaphor,
   scare quote, significance hype and formulaic closer alike, is `references/polish.md` Layers 1 and
   2; the explanatory dash is `references/writing-rules.md` H.1.
5. **A concept has to be recognizable before it can be used.** The default narrows an object until
   the term is technically exact and known to nobody. That is the same local optimization as the
   four above: it buys precision in one phrase and pays with the paper's place in the conversation.
   What a core concept must be able to do, and what naming that permits, is
   `references/writing-rules.md` chapter 9 item 6; a title is not a variable specification sheet,
   which is that file's §4.1 item 7.
6. **Language work preserves meaning, and a change of meaning is never silent.** The default blends
   three different operations into one: correlation becomes effect, possible becomes demonstrates,
   an adversative relation flips, a conclusion shifts strength, and material judged verbose
   disappears. The rule is not that meaning may never change. It is that meaning never changes
   quietly: a substantive change is named to the author as one and ruled on as one, separately from
   the wording it arrived inside. What a language edit may not touch is `references/polish.md`
   Layer 3 and its §2.4 ethical boundary; deletion is gated by `references/writing-rules.md` 5.1 to
   5.3.
7. **What a piece of material is for is judged before it is used.** The author explains things to
   the model in conversation, often with deliberately loose or exaggerated examples, and the default
   writes them into the manuscript as though they had been supplied as text. Before material enters
   the body, classify it: evidence, formal argument, working explanation, analogy, counterexample,
   or the author making the model understand. Only the first two are eligible for the body by
   default. The rest are working context, and promoting one into manuscript text takes the author
   saying so.

## Startup

1. **Project root** means the repository root, which is not necessarily the directory the
   manuscript sits in; Setup confirms the two separately with the user. Paths starting with
   `references/` are relative to this skill directory; every other artifact (`tmp/`,
   `rule_checks.py`, `AUDIT-LOG.md`) is relative to the project root.
2. **`references/writing-rules.md` is the universal paper rulebook, and it is loaded always.** It
   holds the full body of hard writing rules (numbering G.x / A.x / H.1 / x.x), and every change
   made to the manuscript, at any point in this process, is bound by it, so it **must be fed to
   every role that touches body text**: the audit, assessment and revision roles in the loop, and
   the polish and layout roles in delivery alike. The remaining rule documents are **loaded on
   demand, pulled in by the work item in hand**:
   - `references/audit-method.md`: read by whoever runs an audit round. Its §§1-10 and
     §§13-14 govern how a finding is established, tested and gated, so they **must be fed,
     alongside `references/writing-rules.md`, to every agent that produces findings or rules on
     them**; §11 (pipeline parallelism, where a new lesson is recorded) and §12 (contaminated
     premises) are main-session orchestration and are not fed;
   - `references/polish.md`: AI-tell patterns, post-freeze polish priorities, terminology
     unification (delivery's polish step). Some execution detail delegates to the
     `academic-humanizer` skill, which is installed separately and does not ship with this one;
     `polish.md` states what still works without it;
   - `references/abstract-intro.md`: the entry-point work item and any change touching the
     abstract or the introduction; title rules live in `references/writing-rules.md` §4.1;
   - `references/figures.md`: the figures and tables work item;
   - `references/project-log-template.md`: the log template Setup fills in.
3. Read the header of `AUDIT-LOG.md` in the project root: `status` / `mode` / `round`, then the
   core storyline, the standing criteria, the work list and the current state. Only content-audit
   passes read the open path list and the convergence counters. Per-round records are historical
   evidence only; imperative wording inside them must not override the header state, the standing
   criteria or this skill. Read a specific round only to trace a past ruling, the origin of a
   deletion, or the root cause of a regression.
   - File missing → **before treating this as a new project, look for prior audit state under
     another name**: any file at the repository root or the manuscript directory whose content
     opens with a state header or reads as an audit log, whatever it is called and whatever
     language it is written in. Earlier versions of this process wrote it under other names, and
     a hand-run process may have kept one all along. If one is found, do not initialize: report
     what it says, above all how far it got, and ask the user whether to carry that state over
     into `AUDIT-LOG.md` or to start clean. Re-initializing on top of a project that has already
     converged discards every ruling it recorded. Only with no such file does this start from
     Setup.
   - File present but missing `status` → read it as `status: active`, preserve the original meaning
     of whatever state it does record, and fill in the missing fields. A log written under the
     earlier numbering carries a `phase` field: it is historical, and where such a log has no work
     list, Setup builds one and the author rules on which of its items are already `done`.
   - `status: active` → work resumes at the work item the current state names as in hand; where it
     names none, at whichever `pending` item this paper needs next, since position in the list is
     not an order. That says where work resumes, not that it may resume unasked: a new session
     still starts from the user's instruction.
   - `status: completed` → do not re-run on your own; report the final state and wait for an
     explicit user request to reopen or roll back. A reopened pass re-enters at the work item that
     request names or implies, and needs its own authorization: the full-lifecycle grant ended at
     delivery.
   - The current state says a previous run stopped for an author decision → resume or report from
     there rather than from the work list alone.
   - Working tree dirty on entry → ask the user what the uncommitted changes are before touching
     anything. They may be the last session's unfinished work or unrelated edits, and the rollback
     point depends on knowing which. This process's own unfinished work is resumed on top of and
     committed with the pass that produced it; anything unrelated the user settles before work
     starts, since afterwards a rollback cannot tell it apart from this process's edits.

## Stage-start gate: prompt for context compaction

**Setup, the audit loop and delivery each prompt once for context compaction before they first
start.** The user runs the compaction in the terminal (in Claude environments, `/compact`); the
main session has no tool for it and can only prompt. Later passes inside the same stage do not
re-prompt; a stage transition prompts again, re-entry into the loop from delivery included. Fixed
order:

1. The main session first writes the recoverable state into the "current state" section of the
   project `AUDIT-LOG.md`: the stage about to start, existing authorizations, the latest commit,
   the work list, the previous stage's deliverables, and what closes the item now in hand. In
   Setup, before the project file exists, assemble the same information in the current context;
2. The main session prompts the user to run `/compact`. The prompt must name the stage about to
   start and which file and section holds the information needed to resume. It must not merely claim
   compaction happened, and must not pass an ordinary summary off as system context compaction;
3. **Release rule**: under `mode: manual`, prompt and then wait for the user to release before
   starting this stage's roles; under `mode: auto`, prompt and continue directly without further
   permission. The rule reads `mode` and not a position in the flow, so work the author wants to
   supervise can be run manually wherever it sits. **Setup is always `mode: manual`, and so is the
   audit loop until the author approves the switch**: nothing before that approval runs unattended,
   and the switch itself cannot be made inside Setup;
4. If the user did compact, re-read this `SKILL.md`, the project `AUDIT-LOG.md` header and its
   "current state" and `references/writing-rules.md`, then read only the other reference files
   this stage routes to. Do not continue from pre-compaction memory.

Re-compacting mid-stage because context ran short is operational maintenance and does not replace
the next stage's start prompt.

## The four roles

Every pass, in the loop and in delivery alike, runs four mutually separated roles, but **each work
item defines its own role tasks, artifacts and completion test**; one item's termination rules must
not be applied to another:

1. **Domain-check role**: in a clean context, checks the current artifact against this item's
   criteria and submits only candidates backed by evidence;
2. **Independent assessment role**: looks for counterexamples first, then judges whether the
   candidate holds, whether the fix is correct, and whether it is worth doing;
3. **Execution role**: implements only what assessment released and authorization covers; must not
   widen scope;
4. **Independent verification role**: reads the post-execution artifact and verifies it against this
   item's completion test, without inheriting the check or execution role's context.

There are four because each needs a context the others must not have: a role that has already seen
what the previous role concluded can only confirm it.

Failed verification returns the new evidence to the domain-check role for the next pass. After
verification passes, the main session decides continue-or-close strictly by the completion test
written for that item. Open paths, P1/P2, consecutive blocking-free rounds and counter resets belong
only to content-audit passes; the other work items do not inherit them. `round` counts only
content-audit rounds and must not be used to count anything else. **Each pass commits its own output
before it closes**: a content-audit pass once per round, the other items once at close-out. Without
that the later items leave nothing to roll back to, and a request to undo one has no target.

## Parallel-first scheduling

Once the stage-start gate releases, the main session first maps the pass's task dependencies and
write scopes. **Whenever tasks are independent and will neither contaminate each other's premises
nor contend for the same write target, dispatch multiple subagents by default and fill the available
concurrency slots**; serial execution must not be chosen just because it is easier to describe. One
role may run several instances at once. The criteria are the three subsections below; the measured
ways pipeline parallelism goes wrong, cross-round pipelining included, are
`references/audit-method.md` §11.1.

**Depth is not a reason to keep work in the main session; it is the strongest reason to dispatch
it.** When one finding turns out to need deep digging, meaning a long trace, a wide file set or a
question that will not close in a few reads, it goes to a subagent and the main session stays on
the remaining items. This is not about speed. The main session is the only place those remaining
items are held, so a problem it takes on itself does not queue behind that problem, it disappears
with it: the run ends having done one thing thoroughly, having abandoned the line it was on, and
with no record that it did. **A long task fails this way as a whole rather than in part**, which is
why depth is dispatched even where the main session could do it faster alone.

### Default parallel zones

1. Read-only inventory, corpus analysis, official-requirement checks, distinct verification paths,
   figure fact-checking, page-level visual inspection and batched citation checks: split by object
   or path and fill the slots;
2. Candidate generation may run across several mutually invisible agents; the main session merges
   before assessment;
3. Independent assessment may run in parallel by finding batch. High-risk items may go to two
   mutually invisible assessment agents at once: release only on agreement, and send disagreements
   to the main session to rule on under the standing criteria;
4. Execution actions run in parallel only when their files, figure assets and dependency scopes are
   disjoint. Cross-file changes (shared definitions, terminology, abstract-to-body reconciliation)
   settle on one plan first, then dispatch along explicit boundaries;
5. Independent verification, once execution is complete and the state is frozen, may run in parallel
   across dimensions: mechanical checks, factual ground truth, cross-chapter interfaces, rendering,
   and this item's completion test.

### Serial barriers that must not be broken

1. Assessment must see the corresponding check results; execution must wait for assessment release;
2. Verification must inspect the same frozen post-execution state and must not run concurrently with
   related writes;
3. The same file, figure asset, bib entry or shared directory must not be written by two agents at
   once;
4. The project `AUDIT-LOG.md`, the work list, the process state and git commits are written by the
   main session only; subagents return evidence, drafts and recommendations. **The shared rule
   library under `references/` is written by no one here**: it governs every paper, and it sits
   outside the project repository, outside the `best-paper-base` rollback point and outside every
   commit this process makes, so a round that edited it would leave nothing to roll back to.
   Writing into it is an author action, and a lesson bound for it is handed over rather than
   applied;
5. Upstream definitions, global terminology, counting conventions or structural changes that would
   change other tasks' premises must be settled serially before downstream parallel tasks are
   released.

### Dispatch and close-out discipline

1. Each subagent receives only the compacted context it needs; the task statement names the
   input version, the read-only or writable scope, dependencies, completion conditions and return
   format;
2. Concurrent writes of temporary artifacts use unique filenames; generic filenames overwrite each
   other silently;
3. When one agent can read the whole thing and the task needs whole-paper consistency, do not shard
   by chapter just to raise concurrency; split by independent verification path or by disjoint
   objects;
4. While waiting, the main session keeps dispatching other unblocked tasks; when an agent times out
   or returns nothing real, release the slot and redispatch rather than letting one hung task block
   the queue;
5. Before closing out, check every task's input commit, non-empty output and write-scope
   disjointness, and record which tasks actually ran in parallel, why the rest did not, and any
   remaining dependencies.

Preferred parallel objects: in Setup, material inventory, template requirements, corpus collection,
corpus statistics, style analysis and figure rendering; in content-audit passes, verification paths,
blind review and finding assessment; for figures, existing-figure inventory, figure-vs-text ground
truth and candidate designs; for the entry point, candidate versions and body reconciliation; for
references, citation batches; in delivery, disjoint text regions and protected-item verification
while polishing, then page and submission-requirement checks.

**Scope of authorization**: the release rule above settles whether work waits for the user; what it
may then do is bounded by what the user actually authorized. **A request for "one round" is not
authorization to run the lifecycle**: finish the current pass, hand back the result regardless of
`mode`, and stop there. Strike work items off as they close and report the current state at each
close-out. A stop inside a pass is the one point where no close-out fires, so before the session
ends write into the project file's current-state section what a fresh session cannot otherwise
learn: what was in flight, and which files are uncommitted.

## Setup

Setup is supervised by the author throughout and ends when the author accepts it. It settles what
every later pass takes as given.

1. **Confirm the two locations and set up the git base** (before touching any file). They are
   often the same directory and often not, so confirm both with the user rather than deriving
   one from the other:
   - the **repository root**, which holds `.git`, `.gitignore`, `AUDIT-LOG.md`, `rule_checks.py`
     and `tmp/`;
   - the **manuscript directory**, which holds the LaTeX main file and the sources it inputs.
     A venue template package unpacked into the repository puts the manuscript one level down,
     which is the common case, not an exception.

   **The main file is named by the user, not found by scanning.** Searching for
   `\documentclass` returns build copies, layout experiments, the venue template's own sample
   file and earlier submissions of the same work, so a scan may only offer candidates for the
   user to choose from, and directories `.gitignore` already excludes are not candidates at all.
   - Path is not a git repository → `git init`; already a repository but the working tree is dirty →
     ask the user to commit or stash, and start only once it is clean;
   - Write or append to `.gitignore`: `tmp/`, LaTeX build products (`*.aux` `*.log` `*.out` `*.bbl`
     `*.blg` `*.toc` `*.synctex.gz`), rendered PNGs, subagent temporary artifacts. Read the file
     first and add only what is missing. A later line overrides an earlier one, so a pattern
     appended below an existing `!` negation silently re-ignores the files that negation was
     protecting, and figure PDFs a build depends on are the usual casualty;
   - Tag or branch before starting, named `best-paper-base`, as the rollback point. It marks the
     manuscript as the user handed it over, so Setup's own artifacts land after it.
2. **Read the materials first**: read the existing draft and source materials (subagents read, the
   main session receives summaries).
3. **Confirm with the user** (this step must not be skipped, and must not be inferred from the
   materials): target venue, paper genre, the core storyline in one sentence, governing principles,
   known red lines and preferences. Create the project-root `AUDIT-LOG.md` from
   `references/project-log-template.md` and fill in what was confirmed.
4. **Collect the comparison corpus** (subagents, under the networking discipline: small batches,
   timeouts, unique filenames):
   - **at most 30 papers** from the target venue's last two years in the same area, PDFs into
     `tmp/<venue>_corpus/`;
   - the official LaTeX template package, unpacked into `tmp/<venue>_template/` and kept
     **byte-for-byte unmodified**: it is the reference copy the delivery conformance check diffs
     against, so nothing edits it, and the manuscript's own working copy of any class or style
     file lives in the manuscript tree instead. Record the source URL and retrieval date beside
     it, since a venue may revise a template between rounds;
   - the submission requirements (call for papers, formatting rules, page limits, anonymity
     requirements).
5. **If the project already has a mechanical checker, port its checks into `rule_checks.py` and
   retire it.** A paper that has been through manual rounds usually has one, and it encodes
   checks tuned to this paper that are worth carrying over. It does not stay alongside: a shell
   script needs a POSIX shell, while this checker has to run on whatever machine the paper is
   worked on, and two checkers disagree the moment one of them is updated. Generate the
   cross-platform `rule_checks.py` for the project (mechanical checks: dangling
   references, `\input` with a missing target, banned characters, text left in a language foreign
   to the manuscript, and so on). Check only objective errors, never semantics: a
   hard check on what cannot be checked only produces false positives.
   **What it reads, and from where.** The set of files is the main file plus everything it
   reaches through `\input` and `\include`, followed transitively. It is not every `.tex` under the
   repository, which would pull in earlier submissions of the same work, build copies and
   layout experiments. Paths inside those commands resolve relative to the **manuscript
   directory**, so that is the base the checker resolves against, whatever directory the
   checker file itself sits in. Getting this wrong reports every `\input` in the paper as a
   missing target, and those arrive as `ERROR`s that a pass is required to clear before it
   starts.
   **Its output has exactly two line kinds, and later work keys off both.** An `ERROR` line is an
   objective defect the revision role clears before a round starts. A `FACT` line is a reference
   count the audit role would otherwise recount by hand, such as sections, figures, tables and
   citations; it asserts no defect. Anything needing a compile, the page count included, is not a
   `FACT` line, because this checker does not build the paper.
6. **Build the venue's actual standard from the corpus.** This is the standard every later pass
   compares against, so it is measured here rather than assumed anywhere else.
   - Map the paper skeleton against the official template (section structure, page allocation vs
     submission requirements).
   - Fix **how pages are counted**, then measure the **page budget**, and record both in
     `AUDIT-LOG.md`. This is the only place either is defined. Every later page check in this
     skill says "the page count" and means exactly what is recorded here.
     - **The counting convention**: the call for papers decides what falls inside the limit,
       above all whether references and appendices are in or out. Record that decision. Where the
       venue is silent, count the body through the end of the last chapter, exclude references
       and appendices, and record that this was an assumption rather than a stated rule.
     - **The limit**: the number the call for papers states, expressed in that convention. A call
       for papers usually states a total that includes references, so convert it if it counts
       material the convention leaves out. On a paper with no slack that difference is the whole
       margin.
     - **The floor**: where past accepted papers of this venue and genre actually sit, measured in
       the same convention and only over papers submitted under the same limit, or it can come
       out above the limit.
   - **Analyze past accepted papers into one reference paradigm per rulebook** and write the
     analysis to `tmp/<venue>_corpus/analysis/` as the later standard. It is organised by the
     rule document each part calibrates rather than written as one undifferentiated style
     summary, because each rulebook is applied against what this venue's accepted papers actually
     do in its own domain. One paradigm for each rulebook the manuscript is written against:
     - for `references/writing-rules.md`, the venue's general writing shape: narrative structure,
       chapter division, claim strength, how evidence is presented;
     - for `references/figures.md`, what figures and tables look like there: how many, of what
       kinds, what duties they carry, caption style, how they sit against the text;
     - for `references/abstract-intro.md`, the entry point: abstract structure and length, how an
       introduction opens, how contributions are stated, whether abstracts carry citations;
     - for `references/polish.md`, the venue's voice: sentence patterns, terminology habits, what
       register accepted papers actually use.

     Together they are the style baseline: each paradigm is the venue-calibrated baseline its own
     rulebook is applied against, and each is what later work cites when it says "the convention
     at this venue is...". **Statistics must record their basis** (which column, how many
     papers), so that those questions can be answered from it. **A paradigm is a reference and
     never a gate**: it informs judgment and cannot by itself fail an audit.
     `references/figures.md` §8 item 1 and `references/abstract-intro.md` §4 item 10 already bar
     their own corpus observations from being promoted that way, and the same bar holds for all
     four paradigms.
   - Figure analysis follows the production discipline in `references/figures.md`: what is examined
     must be the rendered sample figures themselves.
   - Record the verified venue requirements, genre conventions, style baseline and their scope in
     `AUDIT-LOG.md`. A past-venue convention must never be dressed up as an official hard gate of
     that venue. Where a sourced corpus observation contradicts a generalized clause of the rule
     library, the observation wins: apply `references/writing-rules.md` 0.5, which also lists what
     field evidence never overrides.
7. **Check the core claim against what this venue actually accepts.** Every later pass treats the
   storyline as the invariant it protects, so this is the one point at which the storyline itself is
   examined, and it happens before it becomes that invariant. Use the same corpus as step 6.
   - **What is compared**: what the paper claims, at the level of the one-sentence storyline step 3
     recorded, against what accepted papers of this venue and genre claim. Read the claim each
     corpus paper makes, not its topic: what kind of statement it ends up asserting, over what
     scope, and on what weight of evidence.
   - **Record the sampling frame**, as step 6 does: how many papers were read for this and which
     part of each. A comparison without one is an opinion rather than evidence, and
     `references/writing-rules.md` 0.5 is what keeps that out of the standard. Where the corpus
     cannot carry the comparison, say so and stop: the author may revise the storyline on the
     strength of this answer, so a guess is worse than no answer.
   - **Report where the claim sits, and stop there.** Inside the range the venue accepts, below it,
     or above what the paper's own evidence carries. This step reports the comparison and the
     evidence for it. **It must not propose contributions the paper does not have, invent
     experiments, or draft a stronger claim**: that is the manufactured-contribution failure A.5
     and A.15 exist to stop, and a claim the evidence does not support is barred outright.
   - **The author rules, and the ruling is a condition of Setup being accepted.** A storyline is
     changed only by the author. If they revise it, the revision replaces the storyline in
     `AUDIT-LOG.md` and the loop proceeds from the new one; if they keep it, record that it was
     checked and against what. Either way the storyline is settled here and later passes protect it
     without reopening this question. Being below the range is not a defect of the draft and
     produces no finding: it is information the author is entitled to have while changing it is
     still cheap.
8. **Build the work list**, the section of `AUDIT-LOG.md` that enumerates what this run covers.
   **Each item is either `pending` or `done`, and nothing else.** The author may declare an item
   `done`, which strikes it off; the process then neither re-runs it nor spot-checks it. Each item
   carries its own completion test, and an item struck off on the author's word takes that test
   with it: no later step asks for the evidence that test would have produced, which is what
   "neither re-runs nor spot-checks" amounts to wherever the test is written down elsewhere in
   this skill. Nothing else is recorded against an item: the only action the process takes on this
   distinction is skipping what is done, so an owner, a priority or a third state would be
   decoration.
   - **Pre-freeze**, because each of these can change what the paper says: the content-audit
     verification paths (registered one by one in the open-path checklist), figures and tables, the
     entry point (title, abstract, introduction), and references;
   - **Post-freeze**: polish, layout and page convergence, and template conformance; the last two
     close on the same final build.

   Add whatever else this paper needs, and strike nothing off at Setup except on the author's word.

**Setup ends when the author accepts it**, on this evidence: both locations confirmed with the user;
the git repository, `.gitignore` and rollback point ready and the working tree clean;
`AUDIT-LOG.md` holds the state fields, the storyline, the initial criteria and the work list; the
official template package is present at `tmp/<venue>_template/` with its source recorded, or its
absence is recorded in `AUDIT-LOG.md` together with which of delivery's two cases holds, a venue
that ships no class file or a package that could not be retrieved, since the conformance check
exits differently on each; the mechanical checker runs; official requirements have sources; corpus
selection and counting conventions are re-checkable; the page budget is recorded with the
convention it is counted in; figure samples were really rendered and checked; the core claim has
been compared against the corpus and the author has ruled on the result; independent verification
found no hard rule without a source; and whatever Setup could not establish is written into
`AUDIT-LOG.md` saying what is missing and what it leaves unchecked, rather than left out of the
record.

## Audit loop

The loop covers everything that can change what the paper claims. **One pass takes one work item or
one verification path**, runs the four roles over it, and closes with a commit. What counts as a
problem is `references/writing-rules.md`; how a pass is run is `references/audit-method.md`.

`mode` is the whole of the difference between supervised and unattended running. Under
`mode: manual` each round's findings are **listed for the user to discuss item by item**, and the
consensus that settles goes into the storyline and standing criteria in `AUDIT-LOG.md`. The output
of the loop is not only revisions: it turns "what the author actually wants" into executable
anchors. Confirmed author rulings, project no-touch zones and observed failure modes are recorded
there too.

**Authorization to switch to auto**: when the main session judges the storyline clear and the
criteria sufficient to support automatic rulings, it submits a request to the user, stating the
grounds: which ruling types the project criteria now cover, and which are still uncertain. **The
share of findings the user settled differently from the assessment role is not grounds**: a rate
that improves whenever the assessment role rules more agreeably measures agreement, not whether
automatic ruling is safe. Only after **explicit user approval** does it set `mode: auto`. A mode
switch is never self-authorized, and the loop keeps running under `mode: manual` until one is given.

**A pass the loop was re-entered for** is scoped to the question that sent it, does not reopen
converged paths, and hands back to delivery once that question is settled rather than waiting on
the loop's own termination conditions. Record in `AUDIT-LOG.md` what sent it and why. **When the
question is the page budget**, it is also the one case where "not worth doing" may be ruled on
space; everything else still binds, including never adding content to fill pages. Stop deleting the
moment the count is inside the budget: the target is the top of the budget, not the floor, and
level 6 works in bulk and overshoots easily. If level 6 runs out and the paper is still over the
limit, say so when handing back: one level of `references/writing-rules.md` chapter 6 is left,
figures and tables, and it belongs to delivery.

### The content-audit round

#### Step 0 · Mechanical check
Run the project checker generated in Setup: `python rule_checks.py`, or `python3` where `python`
is not on PATH, which is the normal state on macOS and most Linux distributions. Its two line kinds
are defined there. The revision role clears every `ERROR` before the round starts, with no value
ruling, and the `FACT` lines go to the audit role in step 1. What this step never does silently
is undo the author: text the author restored by hand is reported to them with what the rule
library objects to, and they settle it.

#### Step 1 · Domain audit role (strongest model)
Clean context. Feed it: the current state, storyline, standing criteria and open path list from
`AUDIT-LOG.md`; `references/writing-rules.md` (plus any project rule document recorded in
`AUDIT-LOG.md`); `references/audit-method.md` §§1-10 and §§13-14, which carry the false-belief
test, the qualifier gates, the family sweeps and the table-family sweep that decide what may be
submitted; all of the paper's tex (do not shard by chapter if one agent can read it all); step 0's
`FACT` lines; and the **new verification path** assigned for this round.

The **open path list** is the "Open-path checklist" section of `AUDIT-LOG.md`, registered
and struck off by the main session alone. One entry is one independent verification path (one
verification target plus one failure mechanism), struck off once a dedicated scan has covered it.
Granularity follows "Paths and counting" below: a new verification dimension, evidence source or
failure mechanism registers as a new path; changing only the sample, entry point or attack method is
a variant path and gets no entry of its own.

Use the "audit prompt" text from `AUDIT-LOG.md` verbatim, plus:
1. Every finding must state which criterion it violates or how it deviates from the storyline; a
   finding that cannot state this is not submitted.
2. Write no report file. Return one table:
   `id | P1/P2 | file:line | criterion violated | problem in one sentence | proposed fix in one sentence | supporting evidence`
   P1 = affects the defensibility of a conclusion; P2 = substantive error. Defects step 0 already
   cleared as `ERROR`s are not resubmitted here, but that checker reads form and never meaning, so
   an error that only shows on reading, such as a number that does not add up, a notation clash, or
   a body sentence whose figure reference resolves but points at the wrong figure, is a P2 like any
   other; `references/audit-method.md` §7 admits exactly these.

#### Step 2 · Independent assessment role (another clean context)
Item by item, **find a counterexample before ruling**, across three verdict dimensions:

1. **Does the finding hold**: is the problem real.
2. **Is the fix right**: fixes go wrong more often than findings do; a valid finding with a bad fix
   gets a corrected version.
3. **Is it worth doing** (author hard requirement, ranking with `references/writing-rules.md`):
   the four questions: is this local tuning? does the change contribute substantively to the
   paper? does the space it takes match that contribution? was the solution designed from a
   whole-paper view? **Any "no" → "no substantive contribution, do not do it", even when the
   finding holds and the fix works.** Decision signal and scope:
   `references/audit-method.md` §6.2.

Feed it the merged finding table, the standing criteria, `references/writing-rules.md`,
`references/audit-method.md` §§1-10 and §§13-14, which carry the over-auditing gate, the
side-effect ruling and the two gates every fix passes, and the tex it needs to hunt counterexamples
in, and nothing of the audit role's reasoning beyond the table.
Return the original table plus two columns, `verdict = holds / overturned` and `value = do / do not`.

#### Step 3 · Decision
`mode: manual` → list for the user to select; `mode: auto` → adopt all survivors. A `do not`
ruling never disposes of a finding that termination condition 2 below covers: that class is
resolved or waived by the user, so in auto it is surfaced rather than dropped.

#### Step 4 · Revision role
Each agent gets only its own findings plus the relevant files. Where two released fixes cannot
both be applied, this role does not pick between them: the pair goes back to assessment as one
item, since which fix is right is an assessment ruling. Deletion gate, rewrite seam gate and
cross-line double-check per `references/audit-method.md` §13.

#### Step 5 · Independent verification role
Blind-review the current post-revision version without seeing the audit role's expected answers: it
gets this round's findings and hunks, not the reasoning either earlier role produced. At minimum:
every hunk of this round, whether each finding's root cause is gone, whether the changes
introduced a cross-chapter interface regression, and that the mechanical check has no `ERROR`. If
verification finds a blocking problem, return to step 1 for the next loop; do not close out with a
known defect.

#### Step 6 · Close-out
0. **Compile the PDF and measure the page count (every round, monitoring only)**: report the page
   count against the page budget, both as Setup recorded them in `AUDIT-LOG.md`. **An audit round
   has exactly three actions on page count: compile, measure, report**, and stops there.
   - Page count **must not** cause any ruled change to be dropped, weakened or deferred;
   - Content **must not** be added to fill pages;
   - An overrun is fixed in delivery, not in an audit round; a shortfall is reported rather than
     fixed anywhere (`references/audit-method.md` §9). **The exception is a pass the loop was
     re-entered for precisely to act on the page count**, governed by the rules at the head of this
     loop.
   Build products are not committed to git.
1. Mechanical check has no `ERROR` and independent verification passed;
2. `AUDIT-LOG.md` `round` +1; only newly learned lessons are recorded, and where each one belongs is
   `references/audit-method.md` §11.2. A lesson that section places in the shared rule library is
   recorded in `AUDIT-LOG.md` as a candidate, stating the general operation it came from, and
   handed to the author with the round's report; the round does not write that library itself;
3. One git commit per round;
4. Report: counts of new / adopted / overturned findings, the status of blocking findings, and
   whether any earlier change was reversed.

### Figures and tables

The four roles cover figure and table inventory plus candidate design, figure value and ground-truth
assessment, production and captioning, and post-render independent verification. The verification
role checks every number, label and arrow in a figure and every reference to it in the body, and
regression-scans the affected statements.

**Execute per `references/figures.md`** (the sole rule book for figures and tables: audit criteria,
design spec, production discipline, caption rules), then read the figure paradigm Setup wrote from
past-venue papers. What the pipeline cannot produce (complex hand-drawn schematics, screenshots) is
handed to the author: write out the intent, every element and every arrow, and hand it over.

**Struck off when**: every existing figure and table has a keep / revise / delete verdict; for
adopted objects, the facts, duty, readability, body references and compiled rendering all pass;
every candidate addition has been adopted, rejected or handed to the author, and a hand-off list
does not block, provided it states what the figure must show plus what the body needs to link to
it: the label strings that must match body terms, the target file path and format, the column width
and the caption; no undecided figure-vs-text contradiction remains.

### The entry point: title, abstract and introduction

**Execute per `references/abstract-intro.md`**, against the entry-point paradigm Setup recorded
from the venue's past papers. The four roles cover entry-point cold reading, candidate version
comparison, revision of title / abstract / introduction, and independent reconciliation against
the body.

**Struck off when**: title, abstract and introduction each establish the object, problem, method,
core result and significance on their own; their claims, terminology, numbers and citations agree
with the body; every adopted change passes hunk and cross-chapter interface regression; no
discovered entry-point comprehension break is left unruled.

### References

The four roles cover citation mapping, assessment of claim support and version choice, bib
revisions, and item-by-item independent re-checking. Metadata existing in a database, or a version
update succeeding, does not substitute for checking content.

Whether a citation is kept is ruled by `references/writing-rules.md` chapter 8: the test is whether
it supplies the support some claim needs, never how often it recurs.

1. Check each `cite` against the claim it supports: right paper, right content (subagents, in
   batches).
2. **Check online that each entry is the latest / published version**: an arXiv preprint already
   accepted at a venue is replaced by the published entry. Follow the networking discipline: few
   requests per agent, timeouts, batched dispatch; treat >5 minutes with no output as hung.
3. Bib field completeness (venue, year, pages) and format per the template.

Correcting a sentence whose citation cannot support it belongs here, whether the support was lost
to a version replacement or never held. Where the repair is to lower or drop the claim itself
rather than the sentence carrying it, that changes what the paper asserts, so it is settled as a
content-audit finding under the standing criteria rather than inside this item.

**Struck off when**: every `cite` has a recorded check status for its body claim, its source content
and its final bib entry; after a version replacement, the body support relation is re-checked;
fields and template format pass; items that cannot be verified are listed explicitly and the user
decides whether to keep, replace or drop them.

### Termination (blocking-risk convergence; all conditions required)

**The content-audit work item is struck off when** all of the conditions below hold. They are that
item's completion test, the clause figures, the entry point and references each carry in their own
sections, and they close that item and no other. **The loop ends when every pre-freeze work item
is struck off**, which is the whole of the exit: content-audit is one of those items, so an author
who declares it `done` strikes it off on their own word as with any other item, and these
conditions go with it.

**What these conditions are for.** Two opposite failures produced them, both observed in
practice, and every condition below guards one side or the other. The first stops too early:
the loop ends while paths are still unscanned, so the paper is called converged on the strength
of rounds that never looked where the problem was, and a defect that no path reached is read as
a defect that does not exist. The second never stops: once real defects run out, the loop keeps
producing local disclosure notes, added qualifiers and plausible-sounding refinements, so every
round reports activity while the paper stops improving. Conditions 1 and 4 hold the first shut;
the value ruling and the ban on manufactured findings hold the second. Weakening either side
reopens the failure it was built from, so a condition that looks redundant is checked against
these two before it is touched.

1. **The open path list is empty**, every registered path having had at least one dedicated scan;
2. Every established finding that would change the truth of a conclusion, the meaning of evidence,
   internal consistency, method reproducibility, or the target reader's correct understanding has
   been resolved or explicitly waived by the user;
3. No mechanical `ERROR`, no adopted-but-unimplemented change, and no unverified substantive change
   after the current candidate commit;
4. Two consecutive rounds, both run after conditions 1 to 3 already hold, that find no new blocking
   finding. Each of the two uses a different agent as its independent verification role, and each
   re-checks an already-scanned path by a different route (a variant path, defined under "Paths
   and counting" below) and cross-checks it blind. If the last round contained a substantive
   change, run one more round after it that verifies only and changes nothing.

**Paths and counting**: a new verification dimension, a new evidence source or a new failure
mechanism counts as a new path, joins the open list and immediately resets the consecutive counter.
Changing only the sample, entry point or attack method of a registered path, with the verification
target and failure mechanism unchanged, is a variant path: it counts toward consecutive verification
rounds and does not reset. Once a variant exposes a new failure mechanism it is promoted to a new
path and resets the counter. A run of P1-free rounds is one piece of evidence and does not by itself
constitute convergence; established blocking P2s and mechanical `ERROR`s block just as much. Wording
preferences and local optimizations that change no reader's judgment must be ruled "do not do it" in
the value verdict; an endless supply of manufactured P2s must not be used to prevent termination.

Convergence is a judgment about the candidate commit. The main session decides; once decided, it
reports for the freeze under full-lifecycle authorization, or hands back to the user under
single-round authorization.

## Freeze

The freeze is an author gate, like the authorization to run unattended. When every pre-freeze work
item is struck off, report that and ask the author to freeze the content: the work list is what
this gate reads, and each item's own completion test is what struck it off. **The loop running out
of findings is process evidence, not a ruling that the content is settled**: whether the paper says
what the author wants is the author's judgment, and no number of clean rounds stands in for it.

Record the freeze in the current state of `AUDIT-LOG.md`, naming the commit it freezes. After the
freeze, content changes are barred: delivery preserves meaning and moves layout, and nothing in it
may alter what the paper claims.

**A change delivery cannot make without changing what the paper says re-enters the loop, and the
freeze lifts.** That is the only route back, and it is not a defect of the process: barring it is
what would push a content decision into a layout pass. The loop settles the question that sent it,
delivery resumes from the state it hands back, and the author freezes again.

## Delivery

Delivery runs on frozen content: polish first, which must preserve meaning, then layout, page
convergence and template conformance, **measured once**: one final build settles both the page count
and the conformance check, and there is no earlier layout pass to measure either of them twice.
Measuring once puts a condition on the build that measurement is taken from: **every figure in it
is the real object**, with nothing the figures work item handed to the author still standing in as
a placeholder, and no lorem ipsum or substitute font anywhere. `references/writing-rules.md`
chapter 9 item 2 makes an absolute page count taken over placeholder content unreliable, and with
one measurement there is no later one to catch it. While any handed-over object is outstanding the
count is not taken: report which objects they are, against the hand-off list the figures item
wrote, and wait for the author to supply them. That wait is an author decision, reported and not
looped on.

### Polish

The four roles cover whole-paper polish checking by region, assessment of the value and semantic
risk of each edit, polish execution, and verification of protected items and terminology
consistency.

**Execute per `references/polish.md`** (AI-tell list, post-freeze polish priorities, terminology
unification). AI-tell removal may call the `academic-humanizer` skill, which preserves numbers and
citations unchanged.

Polish plans its work as a **coverage list**: the whole paper divided into text regions, each region
named once, so that completion means every region was polished rather than that suggestions ran out.
The main session writes it before the first pass and strikes regions off as they close.

Polish lengthens prose systematically, since long sentences get split and em-dashes become clause
breaks. It absorbs that within its own material by writing the new text tighter, and does not delete
elsewhere in the paper to make room for its own prose. Reclaiming space elsewhere to land a
correctness fix is a different case, governed by `references/audit-method.md` §9.

**Struck off when**: every region on the coverage list is struck off; the terminology map has no
unresolved conflict; numbers, citations, formulas, qualifiers, logical subordination and term
bindings are all unchanged by accident; compilation and an independent cold read pass.

### Layout, page convergence and template conformance

The four roles cover layout measurement, compression planning and deletion-risk assessment, layout
execution, and page-by-page rendering plus deletion-safety verification and acceptance of the
submission artifacts. Verification must not rest on a successful compile alone, and must inspect the
final submission artifacts, not an intermediate source state.

Layout never governs correctness: fix errors first, reclaim space after.

Compression follows the eight levels of `references/writing-rules.md` chapter 6 in order, with no
skipping. Branch content of no value to the storyline sits at level 6, reached once restatement,
decorative data, non-load-bearing extensions, the conclusion chapter and related work have each
been worked through; figures and tables are level 7, last of the content levels because they are
the hardest to rebuild and the easiest to break. **Level 6 is not executed here**: deciding what
carries no value for the storyline is a content judgment, so reaching it re-enters the audit loop on
that question and lifts the freeze, and this step resumes at level 7 with the page count the loop
hands back. Level 7 changes a figure's width, and both the caption line limits and the readability
check in `references/figures.md` are measured at the final typeset size, so any object touched at
that level is re-verified against them here. The figures work item already judged both at the
template's column width; what level 7 changed is the object, not the standard. If shrinking pushes a
caption over its line limit, merge panels or change the layout rather than moving caption text into
the body: this step is compressing the body, not feeding it. If level 7 has been worked through and
the count is still over the limit, chapter 6 has stopped: report the overrun with the options that
are the author's to choose, namely narrowing the scope, dropping a contribution, or moving to a
venue with a larger budget, and wait for an answer.

**Official template conformance is checked against the template itself, not from memory.** Open the
venue's official class and template files collected in Setup and reconcile the manuscript against
them. Where Setup recorded that no package sits at `tmp/<venue>_template/`, its record also says
which of two cases holds, because they exit differently. **The venue ships no class file** and
states its rules on a page instead: that page is the reference, point 1 below is checked in its
page form, and its absence does not block sign-off. **The venue ships one and it could not be
retrieved**: this check cannot be performed at all, so say so, ask the author for the files, and
never sign off on conformance without them. Where Setup could not tell the two apart, that is the
question to put to the author, and it is settled before this check runs rather than by guessing
which exit applies.

1. **Class and options**: the manuscript loads the venue's own `.cls` with the options the call for
   papers requires, and that class file is unmodified. A locally edited copy of the venue class is a
   conformance failure even when it compiles. Where a venue ships no class file and states its rules
   on a page instead, that page is the reference: check the manuscript against each stated
   requirement and record which ones were checkable. This point does not apply when there is
   nothing to diff against, and its absence does not block sign-off.
2. **No local overrides of template-controlled layout**: page geometry, font family and size, line
   spacing, column separation, float and caption spacing. `geometry`, `setspace`,
   `\renewcommand{\baselinestretch}`, negative `\vspace` around floats and similar devices must not
   be used to reclaim space. Many venues desk-reject for this, and it is the same violation as
   trimming content for page count, taken from the other side.
3. **Structural formats the template defines**: section heading levels and numbering, caption format
   and placement, theorem and algorithm environments, bibliography style and citation form, page
   numbering, headers and footers. Template caption *format* is checked here alongside the three
   gates of `references/figures.md` that the final build settles: caption length (§5.5),
   the collision check that file requires before delivery (§5.6), and readability at the paper's
   actual typeset size (§5.6).
4. **Anonymity** (when required): author block, affiliations, acknowledgements, funding, repository
   URLs, self-citation wording, and PDF metadata.
5. **Submission package**: only the file types the venue permits, with the required entry file name.

Then compile the final version from a cleared build directory and check page by page: page limit,
float placement, line breaks and widows, overfull boxes, and the rendered layout against the
template's own sample output.

**Fix conformance failures here**, but the repair stays on the layout side: revert the local
override, restore the template's own value, move a float, adjust a figure's own dimensions, and
move a non-self-sufficiency sentence out of an over-length caption into the body, which relocates
text rather than cutting it. If conformance cannot be reached without cutting content, that is a
page-budget problem and re-enters the loop; it is not settled here by deleting text.

**The page count, three cases.**

1. **Over the limit**: never delivered. Try the layout side first; if that is not enough, re-enter
   the loop with the page budget at top priority, since there is nowhere left to defer it. If
   chapter 6 has already been reported as exhausted, this step stops the same way and waits.
2. **Under the floor**: nothing is done. Filling space at the last step is exactly what
   `references/writing-rules.md` §6.1 forbids. Report it at delivery; the decision is the author's.
3. **Either bound crossed only because this step ran**: diff the sources against the commit delivery
   started from. Below the floor means text was cut, which this step may not do; above the limit
   means a repair added body text, which the caption-to-body move can do. Roll back and redo the
   repair without that side effect.

After everything passes, deliver and close the log by writing `status: completed`, `final_commit`
and the final artifact paths.

This step closes two work items, so it carries their two completion tests, both settled on the one
final build.

**Layout and page convergence is struck off when**: the page count is inside the page budget
recorded in `AUDIT-LOG.md`, where the two sides are not symmetric: over the limit is a hard failure
and is never delivered, while sitting below the floor is diagnosed per
`references/writing-rules.md` §6.1; every deletion and edit passes the seam checks on definitions,
references, scope statements and argument chains; figure placement and pagination are readable; no
known content regression was introduced by compression; the build is reproducible from a clean
state; this step's own layout repairs removed no content (case 3 above is the test for that, and it
is scored against the count on arrival, never against deletions made by a loop re-entry, which are
verified separately); and floats, line breaks and overfull boxes all pass.

**Template conformance is struck off when**: the manuscript conforms to the official template on
all five points above, with no unmodified-class violation and no local override of
template-controlled layout; anonymity passes; and the submission package contains only permitted
files.

Once both are struck off, the final PDF, package path and commit are recorded and
`status: completed` is written. A failure this step can act on keeps the loop inside delivery;
stopping for an author decision under case 1 is not such a failure and is reported, not looped on.

## Models

The domain-check role, the independent assessment role, the execution role and the independent
verification role all use the strongest model; mechanical checking uses sonnet. Haiku is banned,
with one exception: high-volume mechanical screening such as title/abstract triage.
