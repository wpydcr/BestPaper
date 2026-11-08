# Verification methods

This reference supplies methods, not a second execution workflow. Use writing-guide for principles and audit/routing for task selection, independence, reuse and stopping. Apply the relevant method to the current scope; do not run every section for every edit.

## 1. Anchors and independence

- The **core storyline** and **stable criteria** anchor the authorized work.
  They do not replace source evidence or make an old factual judgment true.
  Check whether a ruling still applies to the current version, goal and premises.
  Surface new evidence that challenges the storyline and handle positioning changes
  within the author's authority. No round's verdict is a gold standard.
- Keep no permanent "rejected" list and never suppress analysis with "we said no
  last time". Before adopting a finding, identify the affected claim, reader judgment
  or active criterion and its evidence. An opinion outside the present scope is still
  analyzed under section 6; its analysis may justify no change or reveal a premise
  that needs reconsideration. Scope controls execution, not whether evidence is read.
- "Not a gold standard" licenses **reversal**, not **relitigation every round**. A
  reversal needs new evidence or a new dimension; without one, leave it alone. That is
  convergence.
- The main session controls authorization, dispatch, retries, rollbacks, commits and
  stage transitions, and remains responsible for substantive adoption decisions.
  It checks the source, evidence, reasoning and expected reader benefit of consequential
  changes; agreement between agents is not proof. This informed review cannot replace
  independent verification or a blind read, which require uncontaminated inputs.

## 2. Everything handed over by the previous sub-agent is untrusted; the evaluation step re-proves it item by item

- **Line numbers are untrusted**: audit agents locate by semantics and write line
  numbers as an afterthought. Re-verify every range independently before acting, or
  deleting by the stated range will cut a sentence in half or miss the target.
- **Proposed fixes are untrusted, and go wrong more often than the findings do**: the
  proposer is immersed in their own diagnosis and will not go check the word's other
  uses. The independent evaluation role rules separately on whether the finding holds,
  whether the fix is correct, and whether the change is worth making; a finding that
  holds with a defective fix must come back with a corrected version. **Accepting the
  finding ≠ accepting the fix.**
- **Self-reported word counts are untrusted**: word count is an input to the adoption
  ruling, so the evaluation step counts for itself. **[Language unit]** For manuscripts
  in Chinese, Japanese or other languages not delimited by spaces, count **characters**;
  every later mention of "words" in this file converts the same way.
- **When an agent asserts "searched one by one, found nothing" and its intermediate work
  cannot be re-inspected, the main session must re-prove by hand any fork that changes a
  number or a conclusion.** "It happens to match" is not verification.
- **Quotations are untrusted**: before writing "reuse the wording at X verbatim", open X and
  read the sentence yourself; a quotation arriving inside another agent's report is as
  untrusted as an upstream list. Copying an agent's paraphrase produces a **third** phrasing
  of the same thing, which is the disease the consistency edit existed to cure. A quotation
  used only to locate ("roughly that paragraph in §5") needs no verbatim check; only one
  about to enter the body does.

## 3. Independence comes from different verification paths, not from more rounds

- **Completion follows substantive acceptance**, as defined in `SKILL.md` under
  "独立阅读、送审与停止": established issues are resolved, the key value is correctly
  understood, and required checks cover the current artifact. Neither a fixed
  number of clean rounds nor an empty path list proves that result.
- **A new path updates coverage, not a counter.** A new verification dimension,
  evidence source or failure mechanism identifies what now needs checking.
  Changing only the sample or entry point may strengthen an existing check; if it
  reveals a new failure mechanism, assess that risk and its affected scope.
  Record actual coverage, evidence and unresolved work without resetting a
  consecutive-round count or requiring unrelated checks to repeat.
- **Convergence is a verdict on one text state, not a permanent property of the paper**:
  after convergence, **every substantive edit to the body voids that verdict**, and
  convergence may be reclaimed only after a regression sweep over all hunks of that
  edit. Compare the current files with the recoverable accepted baseline; if the
  project uses git, `git log <accepted commit>..HEAD` can locate intervening changes.
  Otherwise use the saved version and full diff. Unverified later changes must not
  inherit acceptance from an older version.
  **Readability rewrites are the most dangerous**: they systematically change sentence
  structure (grouping markers, repeated subordinating conjunctions, term-name
  anaphora), and those are precisely what carries the logical relations. One measured
  "improve readability" full-text rewrite introduced four regression classes at once:
  numeric mismatch, garden-path sentences, degraded term binding, and verbatim
  cross-chapter repetition created by sentence splitting.
- Standing verification paths (add or drop by paper genre): summary-layer flattening
  sweep (chapter lead-ins, concluding sentences, etc. vs. the body they summarize;
  look for branches flattened into a single path and premises silently dropped);
  appendix-vs-body proof-scope pairing (**RECOMMENDED, and only for papers containing
  theorems or formal proofs**. Empirical, measurement and qualitative work has no such
  path: the strongest form the proof's own steps support vs. the conclusion as written);
  cross-chapter term-binding sweep (every "Section X defines Y" promise vs. where it is
  redeemed); reverse supply chain (work back from conclusions/prescriptions to check the
  body actually supplies them: a prescription issued in one chapter is a natural source
  of counterexamples to abstract claims); table cell vs. proposition, cell by cell;
  numeric panorama (table row/column sums, ratio conversions, funnel counts);
  readability sweep for long, tangled sentences and rare words;
  **simulated review at the target venue** (open the delivered artifacts as a reviewer
  would and look for gaps between what the paper claims and what is actually there).
- **Reviewer-perspective and content checks have overlapping but complementary purposes.** Audit roles
  catch **false beliefs inside the text** (sentence vs. sentence, table vs. proposition,
  body vs. record). A reviewer catches **the gap between the paper's claims and the
  delivered artifacts** (open the supplementary material and what you see does not match
  what the paper says). Explicitly opening delivered artifacts can expose gaps missed by text-only review. Internal audits may also check these artifacts; define actual coverage rather than claiming the error classes are disjoint.
- **Reviewer-perspective and attacker-perspective roles manufacture defensive suggestions by
  construction**: their value function is "could a reader raise a doubt", which does not
  point where the paper's delivery surface points, so "valid" from them is not "necessary".
  Whatever they produce that **proposes adding a qualification, a disclosure or an
  explanation** passes the §7 gate before it reaches evaluation; skip that and defensive
  edits collect an apparently independent endorsement while the prose drifts,
  monotonically, toward defensive verbosity. The attacker role additionally invents its own
  burden of proof (a claim the paper never made) and reports the gap as a defect; adopting
  it outsources the paper's burden of proof to an imagined adversary. **Boundary**: both
  roles remain the most effective path for **factual, arithmetic, referential and
  delivery-surface** defects and are neither weakened nor retired here; only their "add a
  qualification / disclosure / explanation" output is constrained.
- **When external opinion is fed in, use an independent check that first reads the
  relevant source without the opinion's proposed diagnosis.** Then assess every
  received opinion against the source, evidence and reasoning. Failure to rediscover
  an issue does not refute it; a second agent's agreement does not prove it.
  Record the independent basis for adoption or rejection.
- **Checking external opinion does not stop at right-or-wrong**: where an external
  opinion points in the wrong direction is often exactly where a more serious real
  problem sits.

## 4. Exhaustiveness

Git commands below are examples for projects that already use git. With another
versioning method, use the saved baseline, changed-file list and archived originals
to perform the same checks. Missing history is reported as an unchecked range;
do not invent a commit or initialize a repository just to satisfy these examples.

- **The moment a failure form is found, sweep the whole text for its family** instead of
  fixing that one point and stopping. After fixing, ask: how many other instances of
  this form exist? (Family sweeps authorize family *location* only, never family
  *modification*. See the gate in §7.)
- **Before writing any exhaustiveness claim ("only X left", "the only one in the
  paper"), verify it by grep.** An unverified exhaustiveness claim is a mine laid for
  the next round: it makes later rounds believe this area is already clean.
- **An edit batch is a family by construction; always hunt for the misses** (use its
  changed-file list, or `git show <sha> --stat` when the batch is committed):
  - Renames: the miss is an orphan symbol, hiding wherever sequential reading is least
    likely to reach (in theorem papers, typically the theorem's formal premises).
  - Deletions: the miss is a proper name **defined in the deleted file and used
    elsewhere**: run `git show <sha>:<path>` on the deleted file, list the proper names
    it defined, and grep each against the current text (a filename grep will not catch
    them).
  - Global word swaps: check five seams (the replacement word colliding with a formal
    term, a noun's head being deleted, wording from earlier rulings being overwritten,
    the agentive subject being carried off along the way, the appendix not being swept).
- **Git history is the live archive of deleted data**: source data absent from the
  current tree should be looked up in the initial/historical commits first.
- **A family's boundary is not just literal word form; it includes the support surface
  of the same assertion.** A **literally true** contrastive sentence such as "X does not
  hold" is the support for the false claim "Y holds", and belongs to the same family;
  delete only the false claim and leave the support, and the reader reconstructs it from
  the contrast anyway. Building the family by word form always misses this layer,
  because the supporting sentence does not contain the word. `git show` will often
  confirm the two were **written together in the same commit**.
- **Edits create new gaps in the same family**: after changing the annotation at A, go
  back and check **its cognate at B**. Family sweeps do not happen only before the edit;
  after the edit, sweep **the family the edit itself just created**.
- **A "to-fix list" from upstream is not a decision basis** (the list form of §2): the
  executor must re-sweep the whole range **by the decision rule**; the list only narrows
  the range and never decides. In one measured case a 7-item list missed 4 same-family
  instances, recovered by the executor's rule-based re-sweep.
- **A root cause that reappears in a new form each round is not an exhaustible
  word-form family; it is a check dimension.** "Resolved" in the ledger can only be read
  as "resolved within the dimension swept this round", and the dimension must be named.

## 5. Bookkeeping discipline

- **When rejecting a finding, separate rejecting the *problem* from rejecting the
  *fix*.** Rejecting only the fix may be recorded only as "this fix is unusable";
  recording it as "there is no problem here" manufactures an exempt zone.
- **A rejection rationale is itself a falsifiable factual assertion**: verify it before
  writing it down (often one grep falsifies it), and re-check next round whether it
  still holds.
- **A positional or formal proxy may narrow what to check; it may never issue the verdict.**
  Proxies: sitting inside some environment, a literal-string grep returning zero, frequency
  above N, which section it is in, a word count over N, the instruction obeyed to the
  letter. They mispredict wherever proxy and criterion diverge, and worse, they yield
  entries whose **conclusion happens to be right for the wrong reason**: a wrong rationale
  in the ledger becomes next round's exemption. Narrowing by proxy is fully legitimate
  (family location, sampling entry points); the verdict must return to the semantics of the
  criterion itself. Where the criterion is itself formal (a banned character, a dangling
  reference), the formal check **is** the verdict and this item does not apply.
- Build no permanent exclusion list and grant no location exemption. Without new
  evidence or a new dimension, do not re-file; when something resurfaces, rule on the
  current text and evidence, and read the project's per-round records and git history
  when an old decision must be traced.
- **A semantic criterion cannot be falsified by a word-list grep** (a word list always
  misses morphological variants); only full reading can falsify it. Conversely,
  **word lists for mechanical greps must be generated mechanically from the data's value
  domain** (enumerate the field's actual values), never listed from memory.

## 6. External opinion is a source of leads, not an agenda

Every received opinion is analyzed, including opinions outside scheduled paths and
opinions labelled non-substantive or previously settled. In a compact project record,
retain the source, original text, reviewer's reading, the manuscript's actual claim,
independent judgment and disposition. Merge duplicates without losing their sources.

Distinguish real errors or argument gaps, expression-induced misreading, reviewer
omission or faulty reasoning, and different standards or out-of-scope preferences.
Rejection needs a checked reason, not a prior verdict alone. Analysis does not imply
adoption or unlimited new work: changes still pass the validity, fix, value and
authorization gates. An opinion may reveal a new verification path; being outside
the scheduled paths is not grounds to ignore it.

### 6.1 Investigate the mechanism of a reported misreading

Check the exact reviewed version, input fidelity, quotation and context. A broken extraction, old file or omitted material can invalidate a specific criticism; demonstrate that causal link rather than treating a label as an exemption. A misleading abstract, ambiguous reference or poorly placed condition can still cause a real error even when the reviewer skimmed or paraphrased incorrectly.

Separate two decisions: whether the criticism is justified by the actual paper, and whether the current expression still creates a likely misunderstanding for the intended reader. Read the passage without the diagnosis first, then test the specific interpretation. Do not claim the whole paper is correct because one criticism came from corrupted input.

Use the representation required by the task, including rendered pages, accessible text or machine-readable material when relevant. If only an extraction pipeline is broken and the intended artifact is sound, repair the pipeline for review instead of distorting the scientific notation. Report which input and judgment remain unverified.

### 6.2 Value ruling: valid ≠ worth changing (the evaluation step's third ruling)

Check four questions before spending effort on a valid proposed fix:

1. Does it change a concrete reader judgment or prevent a substantive error, rather than merely tune wording?
2. Does its benefit justify the added work or explanatory burden?
3. Does its space and emphasis fit the role it serves?
4. Does the paper as a whole improve, with its genuine strengths preserved?

A negative answer calls for a better fix or retaining correct text, not a fabricated defect. A small edit can still be substantive when it prevents a false belief. Page constraints do not determine whether a finding is true.

The audit loop's most typical failure is not a wrong edit but a pile of individually
valid micro-adjustments: each one hangs back onto a criterion, each one passes the
first two gates, and together they do not make the paper better. This is **process
evidence substituting for the result**, projected into the audit setting: N edits is
process; the reader judging differently is the result.

**Decision signal**: the fix is only "add a qualifier / swap a connective / adjust one
phrase", and you cannot say **which reader's which concrete judgment changes because of
it** → local tuning, do not do it. Conversely, if you can state "not fixing this makes
the reader form which false belief, or miss which step of the argument", it is a
substantive contribution however few words it is.

**Division of labor with §7**: §7 (the over-auditing gate) stops **false problems**:
hypothetical obligations unsupported by the actual claim and task. This section stops **the real problems not worth fixing**: the problem
exists, but fixing it makes no observable difference to the paper. Both gates must be
passed.

### 6.3 Side-effect ruling: is the cure cheaper than the disease? (the fourth ruling)

- **Two questions the three rulings never ask**: is the fix's **side effect cheaper than the
  original defect**, and is **the original defect actually cured**? Validity, fix and value
  all interrogate the fix, never its cost. Replacing a weak antecedent (the reader bridges
  it) with a garden-path sentence (the reader must backtrack and re-parse) buys the dearer
  defect; the quieter form replaces an unparsable statement with one that parses and is
  false, which the next round is **less** likely to catch.
- **Scope**: changes across quality dimensions also need side-effect checks. Correcting a fact or supplying a definition may create ambiguity, bury the point or weaken a valid result. Inspect foreseeable risks before writing and actual effects afterwards. Use the relevant independent reviewer and affected scope; this is not a demand for another universal full-paper role.
- **Failing it has one outcome: the edit is rolled back**, either to the original defect or
  to a different fix that passes. It is recorded as "fix unusable" under §5, never as "no
  problem here", and the original finding stays open.

### 6.4 A score is a lead, not proof of reader benefit

Check concrete charges against the exact scored version and source evidence. If a decision genuinely depends on an unstable score, comparable re-sampling can help distinguish noise, within the authorized scope. It is not a mandatory new review cycle.

Stable low scores still do not prove that the scoring criterion measures the intended reader outcome. Inspect the actual interpretation and argument. Differences in prompts, models, opponents or input quality limit what a before/after score can establish.

## 7. The over-auditing gate (the audit loop's own most common disease)

- **Scope of this method**: diagnose unnecessary defensive prose and hypothetical obligations. It does not exempt actual mathematical counterexamples, factual errors, evidence gaps, required disclosures or necessary method information.
- **Reader-belief test**: identify what the target reader would reasonably conclude at the current point, using only available context. Repair a misleading claim at its source; do not rely on later text to undo it.
- **Qualifier placement**: keep a condition where it determines truth, scope or interpretation, including independently read abstracts and captions. Repeated wording is unnecessary only when it has no current function.
- **Checkability alone is not a reason to add material**. Necessary evidence, reproducibility information and verified submission requirements are different: inspect their actual role rather than dismiss them as defensive detail.
- **Repair choices**: remove misleading wording, rewrite the claim, place the minimal necessary fact where the reader needs it, or use a separate explanation when warranted. These are choices by effectiveness, not four compulsory gates.
- **Deletion boundary**: do not remove a fact or condition that another statement relies on without preserving its duty. Evidence that changes the central judgment must not be hidden for rhetorical advantage.
- **Before changing a headline's prose gloss, check whether the chapter it glosses makes
  an equally strong claim**: changing only the gloss and not the chapter trades one
  inconsistency for another.
- **Minimal edit**: change one word fewer wherever possible; a rewritten fix preserves
  the author's original sentence patterns and wording by default. Paragraphs the author
  wrote or rolled back by hand are the author's choice: wording-preference items may not
  be filed again there, though substantive defects may still be reported.

## 8. Fix gates

### 8.1 Wording gate (mechanically executable, defensive)

When a change introduces or reuses a potentially technical word, inspect its definitions, table headers and other relevant uses. A match is a reason to check meaning, not automatically to choose another word. Reuse a correct established term for the same object; distinguish different meanings and check local scope after replacement.

### 8.2 Whole-paper gate (constructive; takes priority over 8.1)

**The choice of fix must itself target the whole-paper optimum, not "the problem is gone
at the landing site".** 8.1 and the seam gates of §13 are defensive (do not break
something else). This one asks a different question: is this fix optimal at whole-paper
scale? Finishing only the defensive checks does not count as finished.

Four questions before any fix lands:

- **Does an accurate formulation already exist?** Use it as evidence for the intended object and scope. Reuse wording when its current rhetorical duty matches; adapt it when an abstract, definition or explanation needs a different form. Do not create gratuitous synonyms or mechanically duplicate text.
- **Can changing the upstream kill several downstream instances at once?** When one root
  cause is scattered across many places, changing the definition beats changing each use.
  Locate the layer of the root cause first, then decide which layer to touch.
- **Do several findings share a root cause?** If so, merge them into one edit. Fixing
  them separately is the surest way to create mutually unaware local dialects, the other
  mechanism behind "independently optimized chapters drift apart".
- **Read the new wording back in whole-paper context**: is it now more consistent with
  the cognate phrasings in the abstract, introduction and summary layer, or is there one
  more formulation that holds only here?

The local view's two failure modes: adding a qualifier in place (hits the
over-defensiveness gate), or rewriting in place (creates a new dialect). Asking "how is
this assertion phrased elsewhere" first often finds the correct version already exists,
degrading the fix to a zero-cost alignment. This matters most when an external reviewer
calls a sentence "too strong" or "unclear": **neither the location nor the diagnosis is automatically correct**. Check both against the actual passage before adopting a repair.

## 9. Strict separation of page budget from correctness/improvement

- **No tolerating a bug for the page budget**: the audit step must not downgrade or defer
  a report because "the fix adds words"; the evaluation step must not treat "net
  addition" as grounds for overturning. The page budget settles separately, after the
  revision step: fix it correctly first, then reclaim space from unrelated places.
- **No refusing an improvement for the page budget**: no suggestion may be withheld
  because "it adds words" or "we are already over". The only permitted response is to
  honestly annotate the word delta (characters for Chinese manuscripts, see §2). Write
  the page budget into an agent's instructions and the agent will use it as a screening
  gate: **the suggestions it blocks never appear in the output and cannot be recovered
  by asking**.
- **No padding to reach a page count**: being under the target is not a defect, and
  content written to reach a word count is necessarily filler, another entrance for
  over-defensiveness. An under-length paper is reported, not acted on.
- **Measure pages when the current layout or delivery task needs the measurement**,
  using the real submission rules and the relevant rendered version. Repeating a
  build for every content pass is not an acceptance condition. A content audit does
  not silently become a compression task; when compression is authorized, preserve
  meaning and assess deletion cost under writing-rules chapter 6. Execution scope is maintained in [routing.md](routing.md); no separate delivery-to-audit return loop is imposed here.
  Never add content merely to fill an observed shortfall.

## 10. Table criteria

- **Column-header subject test, in two steps**: first ask whether the cell plus the
  column header **parses as a proposition** (parsing comes before truth), then ask
  whether it is true. A cell without its own subject borrows the header's subject, and
  the header must be true of it; a cell with its own subject treats the header as a mere
  column label. **Before changing a header, count how many cells are borrowing their
  subject from it.**
- **Make joint conditions explicit**: a table can represent conjunction, alternatives or independent cases if headers, grouping and notes make the relation unambiguous. Do not let parallel rows imply independence when the claim requires several conditions together. Use prose when it communicates the relation more clearly.

- **Adding a block header appends an implicit subject to every subject-less cell below
  it**; re-run the subject test cell by cell before adding one.
- **A table finding must trigger a full-table family sweep on the spot**: when the finding
  lands on a cell / column / row pattern, the sweep attaches to the finding and not to the
  fix, so a finding ruled not worth doing is swept before it is closed. The revision
  instruction, where there is one, must also require
  "check **every** cell in the same column (row, pattern) against the same criterion,
  cell by cell", and the close-out report must state how many cells were swept, how many
  passed, how many failed. Fixing only the reported cell = not done. This is family
  *location*, not family *modification* (the latter hits the authorization boundary in
  §4). Every located cell still goes through evaluation individually.
  **Why tables need this more than prose does**: cells are independent and do not
  reference each other, so **no adjacent text can ever expose another cell's error**.
  Prose errors often self-expose through contextual conflict, table errors never do. In
  one measured case the same column of the same table failed four times across rounds more
  than twenty apart, because each round fixed only the reported cell. The typical failure
  form is **a cell filled with something adjacent to but different from what the header
  asks for** (the header asks for A; the cell holds B, which sat in the same source
  paragraph and was copied over in passing).

## 11. Content-check functions and pipeline parallelism

A revision batch needs distinct functions: proposing supported changes, independently
assessing validity and value, executing authorized changes, and independently checking
the revised artifact. These functions do not impose a fixed four-agent or repeated-round
schedule. Post-edit verification checks the full batch, affected interfaces and actual
reader effect against the current agreed scope. It is an informed regression check,
not a blind review. Failed verification keeps the affected issue open; passing requires
evidence of repair, preserved value and no unresolved required work.

### 11.1 Pipeline parallelism (how parallel execution goes wrong)

Dispatch boundaries, dependencies and post-edit checks follow [routing.md](routing.md) and the entrypoint revision loop. This section supplies concrete failure modes
for applying those nodes, not a second mandatory schedule.

- **Parallel preparation** may use a fixed version when its premises and write scope
  are independent of pending edits. Do not present it as acceptance of the future
  combined version. Checks that depend on the edited text wait for writes to finish
  and inspect the same frozen batch; dependent blind review waits for the acceptance
  node in `SKILL.md`. A commit is optional; a stable, identified version is not.
- **Multiple independent checks** can help on a critical risk when they use different
  evidence or reasoning paths. Agreement does not authorize adoption; the main session
  still checks the substantive basis. Choose the number of checks from the risk and
  the agreed scope, not a fixed two-agent prescription or a target round count.
- **Revision agents touching the same file must be dispatched serially**: if parallelism
  is genuinely needed, enumerate a **file-occupancy list** per agent before dispatch and
  confirm zero intersection, with the list written into the dispatch instructions rather
  than checked afterwards. One measured case where two revision agents edited the same
  file concurrently survived only because Edit matches exact strings and they happened to
  hit different paragraphs (**luck, not design**): with one overlapping line the later
  Edit either fails to match or silently swallows the earlier change, and **a successful
  Edit never reveals that it wrote onto an already-modified baseline**. The
  after-the-fact diff cannot show it either, since the final text is self-consistent and
  what is lost is the intermediate version.
- **Tiered agent reuse**: reconciliation, gate and record-checking work may reuse a warm
  agent via SendMessage; blind review and evaluation must be opened fresh, because
  accumulated familiarity kills first-read independence.

### 11.2 Where a new lesson is recorded

A paper-specific lesson belongs in that project's own lessons document. The working log records the current event and links the lesson; it does not duplicate the entire lessons file.
A transferable mechanism can be proposed for BestPaper with its evidence and applicability. Manuscript work does not itself authorize editing the shared skill or global instructions; an authorized skill-maintenance task does.

## 12. Contaminated premises mean restart

When a task used a wrong premise, file, scope or example, discard the affected execution and restart with corrected inputs. A correction message cannot reveal what was already suppressed or reinterpreted under the wrong premise.

An ordinary suspended task can resume when its inputs and premises remain valid. Lack of a visible output is not evidence that no contaminated reasoning occurred.

## 13. Seams and engineering details

- **Rewrite seam gate** (the dual of the deletion gate): after each round's edits, grep
  both the old and the new form of every word swapped this round, across all their other
  occurrences, and confirm no stale binding, duplicate attribution or forward reference
  is left behind. This is the actual mechanism behind "independently optimized chapters
  drift apart".
- **Intra-sentence seam gate** (the in-sentence dual of the rewrite seam gate): when
  rewriting **part** of a sentence, the rest of the same sentence must be re-checked. The
  half that was fixed creates the illusion that the sentence has been reviewed, and the
  unexamined half thereby gets an exemption: the diff marks the whole sentence
  "changed", the re-checker reads the fixed half, and naturally never suspects the other
  half of the same line. The rewrite seam gate looks for stale bindings across sentences
  and chapters; this one looks at **the part of the same sentence that was not
  replaced**. One measured unit error survived exactly this way, through a rewrite of the
  first half of its own sentence.
- **Deletion search**: locate the symbols, introductory promises and dependent references carried by the proposed deletion. Counts identify candidates, not whether a duty is unique or dispensable. Read the semantic dependency and identify its replacement. Where repository history exists, inspect relevant prior decisions rather than treating either a historical deletion or a historical retention as permanent authority.
- **Cross-line double check**: when the source file is hard-wrapped, a phrase grep misses
  occurrences that span lines. **The hard requirement is that the cross-line double check
  must be done**: first search the whole phrase on a single line, then search again in
  cross-line mode; missing either pass means it was not checked. The command is whatever
  tool is at hand: with ripgrep, `rg -U "word\s+phrase"` (Claude Code's built-in Grep tool
  is ripgrep. Pass `multiline: true` for cross-line; it does not accept `-Pzo`); with GNU
  grep, `grep -Pzo "word\s+phrase"` (`-P` needs PCRE support, which the BSD grep shipped
  with macOS lacks). Keep inserted key phrases on one line when reordering.
- **Three seam checks**: before a newly written sentence lands, check for a bare numeral
  at sentence start, repetition within ten lines above, and tense breaks at the insertion
  point.
- Unique filenames for concurrent writes, non-empty output checks and the networking
  discipline support the shared dispatch and post-edit checks: give each
  concurrent temporary artifact a unique path and verify actual returned content.

## 14. Boundaries for verifying records and supplementary material

**Applicability**: these items assume the paper delivers a checkable artifact (human
coding/review records, supplementary material, or archived data). Papers with no such
delivery surface (pure theory, pure method, short papers with no supplement) are out of
scope.

- Executed review/coding records are **traces**. Demanding extra data or rewriting records
  because "a reviewer cannot recompute it" is falsifying records. Whenever the urge to
  chase a data source arises, ask first: is this serving the reader, or serving the
  feeling of "I verified it"?
- **Keep two verification states separate**: an internally consistent chain of definitions may support a formal conclusion, but it cannot establish external events, dataset contents or execution records. If source records are unavailable, mark those factual checks unverified and state the effect on the claim. When records are available, compare the actual assertions with them; self-consistency is not a substitute.
- **The delivery-surface citation chain must be checked in both directions**: check both
  "does the artifact contain what the paper names" (missing = false statement, must fix)
  and "does the paper mention what the artifact contains". **A reverse-direction gap
  produces no false statement**, so every "claim vs. artifact" check is immune to it; its
  damage is different: **wasted delivery** (the reader opens material the paper never
  mentions and cannot place it in the evidence chain), and it makes two findings collide
  in the same place: "the named ones count correctly" and "there is a problem here" are
  each half right, and the next round easily uses the former as a shield to suppress the
  latter (the exempt-zone form of §5). **Only running both directions counts as checked.**
  Choose the reference location where the reader needs the material. A body claim may point directly to a supplement; an appendix may carry detailed navigation. Existing appendix and supplement files do not impose a mandatory body-to-appendix-to-supplement chain.
- **Archived data is a historical snapshot, not current truth**: writing back from an
  archive requires overlaying every ruling made after the archive, and re-checking each
  borderline instance against the rules.
