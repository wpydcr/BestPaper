# Audit Log Template (Setup initialization)

<!-- Usage: copy this file to the paper project root, rename it AUDIT-LOG.md,
     fill in every angle-bracket placeholder section by section, then delete this
     comment and every "How to fill this in" block.
     This template contains no paper-specific content; do not start the audit
     loop before it is filled in. -->

<!-- This file is the anchor of the audit loop. The first thing an audit agent
     does is read it; only then may it look at the manuscript.
     The anchor holds exactly two things: the core storyline and the stable
     criteria. No single round's verdict is the gold standard, including the
     last one's. -->

```
status: active         # active = resume at the item the current state names as in hand; completed = delivered, do not re-run unasked
mode: manual        # manual = list changes and wait for the author; auto = apply once the evaluation role clears them
round: 0             # content-audit rounds only; never incremented elsewhere
```

> **How to fill this in (delete when done)**: a new project always starts at
> `mode: manual`; switch to `auto` only after the author has confirmed the audit
> agents' judgment quality.
> Only content-audit rounds update `round`; annotate it with "commit of the previous round + this
> round's focus + where the count starts", so that a dropped session can resume
> without re-reading the whole manuscript.
> After a compaction, re-read the skill, this file's header and the current
> status before continuing; never continue from pre-compaction memory.

> **Normative precedence (keep this block)**: only the state header, the research
> origin and scope, the current stable criteria, the work list, the open-path
> checklist, and the current state are normative. The per-round records are
> historical evidence only; words like "must", "the only condition", or
> "supersedes" inside them describe that round's rules and never override the
> current stable criteria or the Best Paper skill. Read a past round only when
> tracing an old verdict, a deletion's origin, or a regression's root cause; do
> not feed the whole history to implementation roles by default.

---

## Audit prompt (hand to the audit agent verbatim each round)

We need a full sweep of the paper's content (`<manuscript source directory>`).
After many rounds of major revision, the paper may contain unclosed logic or
internal contradictions; the worst failure is chapters optimized in isolation
with no overall coordination, leaving the narrative fractured.

Do a deep evaluation. **Do not nitpick; find substantive problems.** I do not
want a report, and I do not want you to create any new file unless I ask.

The core metrics are: **the paper's core storyline must not drift, the story must
stay modest, the logic must close, and the prose must read smoothly.** Hold it to
the standard of the best `<genre>` paper at `<target venue>` (consult
`<past-proceedings corpus directory>` if useful, and update key findings into
this file).

Follow the rule files of the Best Paper skill itself, including any project rule
document this log records for this genre. The cross-project writing hard rules and
audit methodology load automatically and are not listed here.

> **How to fill this in (delete when done)**: do not change the skeleton of this
> prompt. Every sentence blocks a known failure mode:
> "do not nitpick, find substantive problems" blocks the agent's over-auditing
> tendency; "do not create any new file" blocks it from converting work into
> reports; "the storyline must not drift" blocks it from turning the paper into a
> different paper; "the story must stay modest" blocks defensive additions;
> "logic closes" and "prose reads smoothly" are two parallel acceptance faces,
> both required.
> Replace only the angle-bracket project-specific items.

---

## Research origin and scope

### Governing principle

> `<One sentence: the highest-level value judgment of the problem domain this
> research belongs to. It is not this paper's contribution; it is the premise the
> paper accepts and uses to decide what counts as a problem.>`

> **How to fill this in**: this constrains the audit agent's value system. If you
> cannot write it, ask "if someone said the paper's goal itself is wrong, how
> would I rebut them", and the rebuttal is this line.

### Core problem

> `<One sentence: what existing work reports, versus the different thing that
> actually needs to be judged. That mismatch is the paper's reason to exist.>`

> **How to fill this in**: it must read as "the mismatch between A and B", not "A
> is an important field". If the second half still stands after removing the
> "but", it is not there yet.

### Storyline

`<This paper is not a <the kind of paper it is most likely to be mistaken for>,
nor a <another such kind>. What it builds is:>`

1. `<Step 1: what the reader currently has>`
2. `<Step 2: what is actually needed>`
3. `<Step 3: what this paper uses to convert the former into the latter>`
4. `<... list the actual derivation chain, one restatable sentence per step>`

`<The full loop is therefore: X → Y → Z → ... → the judgment or capability finally
delivered>`

`<One sentence on why this loop is strong, i.e. where the paper's best-paper
potential comes from>`

**Invariant**: any change that pushes the paper toward `<the two to four things
this paper explicitly does not do>` is storyline drift.

> **How to fill this in**: the storyline is the governing authority for every
> audit verdict; if it is not clear, do not open the loop.
> Write the **invariant** as "pushing in direction X is drift", because the audit
> agent's most common overreach is not a wrong word fix but helpfully pushing the
> paper toward "doing a bit more". Two to four explicit non-goals is enough.

---

## 1. Stable criteria (in force every round; may grow as audits validate them; not findings)

> **This section holds paper-specific criteria only.** Cross-paper methodology
> criteria (anchoring and independence, upstream distrust, verification paths,
> exhaustiveness, bookkeeping, over-audit gates, fix-wording gates, separating
> layout from correctness, table criteria, figure methodology, parallelism,
> premise contamination, seams, record-verification boundaries) are loaded
> automatically by the skill flow; **do not copy them here**.
> Write only what would not hold for a different paper: this paper's page limit,
> its no-touch zones, the nature of its material, and the final verdicts the
> author has issued for this paper.
>
> **Every criterion has one of three origins, and the origin must be written
> down**: (1) a verdict the author issued directly (mark "author's verdict, hard
> rule"); (2) a lesson measured in one round (mark "measured in round N" and
> record what went wrong and what it cost); (3) a constraint derived from the
> paper's own setup. **A criterion with no origin must not be written down**; a
> few rounds later someone will read it as a negotiable suggestion.
>
> Numbers are never reassigned once allocated, because other records point back
> by number. A retired criterion keeps its number and is annotated "retired
> (round N, reason)".

<!-- The three entries below are shape examples of what a criterion looks like.
     They are deliberately unnumbered so that they cannot occupy criterion
     numbers 1-3. Replace or delete them at initialization according to this
     paper, and number the real criteria from 1. -->

- **`<hard factual constraint example>`**: the page budget is a limit of `<N>` pages with a floor of `<M>` measured over `<K>` past papers, both counted as `<the convention recorded in Setup>`,
   `<work-item-specific constraint, e.g. "figures not started yet, placeholders
   are fine">`. Content unrelated to the storyline must therefore not be added
   freely.

- **`<no-touch zone example>` (author's verdict, hard rule)**: `<some class of
   material>` is **a record of a process already executed**; rewriting it is
   falsifying the record. It must not be used as grounds to demand extra data,
   extra scripts, or a rewrite on the argument that "the reader cannot
   recompute it". **Test**: it is a problem only if the omission would make a
   reviewer who reads only the body form a **false** belief; where detail is
   missing but the belief is true, leave it alone.

- **`<measured-lesson example>` (measured in round N)**: `<what actually went
   wrong in one round: how many of how many findings were overturned, the shape
   of the failure, and what following them would have cost>`. Therefore
   `<the mechanically executable gate distilled from it for the next round>`.

> **How to fill this in**: entry 3, the lesson with measured numbers, is the most
> valuable shape, because it gives both the failure rate and the failure mode, so
> a later agent cannot read it as "just be careful". At the end of every round, if
> a finding was overturned, first ask which existing criterion it slipped past,
> and only then consider adding a new one.

## Work list

> **This section is the control variable**: it enumerates what this run covers,
> and the process advances by striking items off it. **Each item is either
> `pending` or `done`, and nothing else.** The author may declare an item `done`,
> which strikes it off; the process then neither re-runs it nor spot-checks it.
> Each item carries its own completion test, defined for it in `SKILL.md`, and an
> item struck off on the author's word takes that test with it: no later step
> asks for the evidence it would have produced.
> Nothing else is recorded against an item: the only action the process takes on
> this distinction is skipping what is done, so an owner, a priority or a third
> state would be decoration.

**Pre-freeze**, because each of these can change what the paper says:

- `pending` content-audit verification paths (registered one by one in the
  open-path checklist below)
- `pending` figures and tables
- `pending` the entry point: title, abstract, introduction
- `pending` references
- `pending` `<whatever else this paper needs before the freeze>`

**Post-freeze**:

- `pending` polish
- `pending` layout and page convergence
- `pending` template conformance
- `pending` `<whatever else this paper needs after the freeze>`

> **How to fill this in**: add whatever else this paper needs, and strike nothing
> off at Setup except on the author's word. Layout and page convergence and
> template conformance close on the same final build.

---

## 2. Open-path checklist

> **Applicability**: Setup registers this paper's paths here, content-audit
> passes strike them off, and this list standing empty is one clause of the
> content-audit work item's own completion test. No other work item and no stage
> outside the loop reads this section's P1/P2, paths, or consecutive counts to
> decide whether an item is struck off; each of those uses the completion test
> `SKILL.md` defines for it.

> **Blocking-risk convergence**: the conditions, the path-versus-mutation
> distinction, and the counter-reset rule are defined in `SKILL.md` under the
> audit loop's Termination section. Do not restate them here; read them there.

Tick the standing paths that apply to this paper's genre, then add its own:

- [ ] Summary-layer flattening sweep (chapter lead-ins, concluding sentences,
      etc. vs. the body they summarize; look for branches flattened into a single
      path and premises silently dropped)
- [ ] Appendix-versus-body convention check, pair by pair (the strongest form the
      proof's own steps support vs. the conclusion actually stated)
- [ ] Cross-chapter term-binding sweep (every "Section X defines Y" promise and
      where it is redeemed)
- [ ] Reverse supply chain (work backward from a conclusion or prescription to
      check the body actually supplies it)
- [ ] Table cells vs. propositional statements, cell by cell
- [ ] Whole-number sweep (row and column sums, ratio conversions, funnel counts)
- [ ] Long-sentence and rare-word readability sweep
- [ ] Simulated review at the target venue (open the delivered artifacts as a reviewer
      would and look for gaps between what the paper claims and what is there)
- [ ] `<paper-specific path 1>`
- [ ] `<paper-specific path 2>`

> **How to fill this in**: a tick means only "this path has had one dedicated
> run", never "this path is permanently clean". Record the round number and the
> result (blocking finding or not) next to each path that has been run. The
> moment a new failure mechanism appears, add a new path and reset the
> convergence count.

---

## 3. Current state

**Stage and item in hand**: `<the stage about to start or already running: Setup,
the audit loop, or delivery; and which item of the work list above is in hand.
The work list itself is that section; do not copy it here>`

**Authorization in force**: `<what the user actually granted, and when: the full
lifecycle through delivery, or one round or one work item only. A single-round
grant is discharged the moment that pass hands back its result; the full-lifecycle
grant ends at delivery, so a reopened pass needs a fresh one. Where this says
nothing, a resuming session holds no grant and asks before running anything>`

**Progress**: `<the most recent commit and what it contains; what is landed but
uncommitted>`

**Previous stage's deliverables**: `<what the stage before this one handed over:
its artifacts, the commit they landed in, and anything it left with the author>`

**Freeze**: `<not frozen; or the commit the author froze the content at, and when.
Until this says frozen, content may still change; after it, a content change re-enters
the audit loop and lifts the freeze>`

**This round's dispositions**: `<candidate count and grading; how many adopted,
how many rejected, and the shape of the rejection reasons>`

**Completion-test status for the work item in hand**: `<list each condition that
`SKILL.md` requires before that item is struck off, with its evidence>`

**Stage-start context compaction**: `<whether a system compaction has been
invoked for the current stage; which required files were re-read afterwards>`

**Parallel scheduling**: `<this loop's task dependencies, subagents dispatched,
each one's input commit, read-only or write scope, serial barriers, tasks not
parallelized and why>`

**Content-audit blockers**: `<content-audit passes only; unresolved blocking
findings, mechanical ERRORs, adopted-but-unimplemented items>`

**Content-audit convergence candidate commit**: `<content-audit passes only; the
candidate commit and whether any unverified substantive change follows it>`

**Content-audit convergence count**: `<content-audit passes only; the current
consecutive count and the reason for the last reset>`

**Shared-rule candidates**: `<lessons from this round that §11.2 of
references/audit-method.md places in the shared rule library, each with the general
operation it came from and the evidence. The round does not write that library; these
are handed to the author with the round's report and stay here until the author acts.>`

**Next loop's starting point**: `<what the next loop on the work item in hand
does, or which author verdict it is waiting on>`

**Terminal information**: `<when status=completed, the final_commit and the paths
of the final artifacts; while active, write "n/a">`

> **How to fill this in**: this section is the sole entry point for resuming a
> dropped session. A new session with no context must be able to read only this
> and know where things stand and what to do next. Update it every loop; do not
> append history; history goes in the per-loop records below.

---

## 4. Per-loop records

> One section per loop, newest first. Content-audit passes record paths,
> findings, reasons for overturning, and the net change; other work items record
> that item's artifacts, the verification result for its completion test, and the
> next loop's starting point.
> **A single loop's verdict is not the gold standard**: a later loop overturning
> an earlier conclusion is normal, and the grounds must be written down here.
> This section is always historical evidence only and must never use imperative
> wording that overrides the file header, the current stable criteria, or the
> skill.

<!-- `<N>` is this record's position among the records already written for work item
     `<W>`: count them and add one. -->

### work item `<W>` loop `<N>`: `<one sentence on this loop's focus and conclusion>`

`<content>`
