# Audit Method (shared across papers)

## 1. Anchors and independence

- There are only two anchors: the **core storyline** and the **stable criteria**, both
  given by the author. No single round's verdict is a gold standard, the previous
  round's included: a previous fix may itself be wrong, and being overturnable is
  exactly why the loop exists.
- Keep no permanent "rejected" list and never suppress this round with "we said no last
  time". Anti-oscillation comes from hanging every finding back onto an anchor;
  **a finding that cannot be hung onto one is not a finding and is dropped** (this is
  also how "do not nitpick" is executed).
- "Not a gold standard" licenses **reversal**, not **relitigation every round**. A
  reversal needs new evidence or a new dimension; without one, leave it alone. That is
  convergence.
- The main session controls process only: it checks authorization and evidence
  completeness and decides retries, rollbacks, commits and stage transitions. It does
  not produce candidate findings, write revision text, or stand in for independent
  verification. A mind that has already seen the previous rounds' conclusions can only
  prove self-consistency.

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

- **Convergence is judged by blocking risk; its conditions are defined once, in
  `SKILL.md` under the audit loop's Termination section, and are not restated here.** "N consecutive rounds
  with no P1" is not by itself convergence evidence: it only proves that those N
  rounds' path set failed to cover it. Every late-arriving true P1 came from a new path;
  re-running the same path has diminishing returns.
- **A new path resets the count**: a new independent verification dimension, a new
  evidence source or a new failure mechanism is a new path. Changing only the sample,
  the entry point or the attack while the verification target and failure mechanism stay
  the same is a mutation path, usable inside a consecutive verification round without a
  reset; a mutation that exposes a new mechanism is promoted to a new path. Registration
  and counting are per the audit loop's Termination section in `SKILL.md`.
- **Convergence is a verdict on one text state, not a permanent property of the paper**:
  after convergence, **every substantive edit to the body voids that verdict**, and
  convergence may be reclaimed only after a regression sweep over all hunks of that
  edit. Start the next round with `git log <convergence commit>..HEAD` to see what moved
  after convergence. Commits nobody re-audited after convergence are the richest P1
  seam, and are the easiest to mistake for "already audited last round".
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
- **"Simulated review" and content audit catch two disjoint error classes.** Audit roles
  catch **false beliefs inside the text** (sentence vs. sentence, table vs. proposition,
  body vs. record). A reviewer catches **the gap between the paper's claims and the
  delivered artifacts** (open the supplementary material and what you see does not match
  what the paper says). No path of the first kind ever reaches the second: the first
  run of simulated review surfaced problems that thirty-plus consecutive content-audit
  rounds had never touched.
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
- **When external opinion is fed in, always dispatch a blind agent that cannot see it**:
  only items hit independently are trustworthy. Without the blind pass there is no way
  to tell "the report was right" from "the agent was carried by its phrasing".
- **Checking external opinion does not stop at right-or-wrong**: where an external
  opinion points in the wrong direction is often exactly where a more serious real
  problem sits.

## 4. Exhaustiveness

- **The moment a failure form is found, sweep the whole text for its family** instead of
  fixing that one point and stopping. After fixing, ask: how many other instances of
  this form exist? (Family sweeps authorize family *location* only, never family
  *modification*. See the gate in §7.)
- **Before writing any exhaustiveness claim ("only X left", "the only one in the
  paper"), verify it by grep.** An unverified exhaustiveness claim is a mine laid for
  the next round: it makes later rounds believe this area is already clean.
- **A batch commit is a family by construction; always hunt for the misses** (start with
  `git show <sha> --stat` for the file list):
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

External audit reports get no ledger, no per-round re-adjudication duty, and no place in
the termination conditions. To decide whether to chase an item, ask only: would a
verification path already scheduled for this round reach it independently? Yes → handle
as an ordinary finding, and keep the source out of the rationale. No → it is a special
request, and is not done. The agenda is set only by the core storyline, the stable
criteria and the scheduled paths.

### 6.1 An external misreading must first pass the "reproducible by the target reader" test (before any discussion of fixes)

**A reviewer misread ≠ the paper is wrong.** The first step in judging any external
misreading is fixed: **would this misreading mechanism occur in a target reader?**
No → not a defect, ruling is "overturned", discussion ends there.

The most common non-reproducible mechanism is a **reading-pipeline difference**: LLM
reviewers read the PDF through **text extraction**, human reviewers read the **rendered**
version. Extraction artifacts (inline subscripts split onto their own line, misplaced
super/subscripts, normalized apostrophes and hyphens) simply do not happen in the
rendered version. Same family: the reviewer read only the abstract and conclusion; the
reviewer read an old version; the reviewer's paraphrase does not match the source
(misquotation). None of these are the paper's problem.

**Watch for this inversion**: after confirming "source correct + rendering correct +
extraction alone broken", **that evidence proves the paper is not wrong**, yet it reads
extremely easily as "so change it, to stop it being misread". The moment you argue about
eliminating the cause, you are optimizing the proxy metric "stop the review tool
misreading" instead of the user outcome "let real readers understand correctly". The cost
is real: reshaping formulas or notation to suit an extraction pipeline consumes page
budget and can introduce a one-off convention unique in the paper.

**Boundary**: extraction robustness is a real requirement only when the target channel
explicitly uses LLM-assisted first-pass screening. Even then it is handled as a
submission-engineering item (compile-time check); it does not enter the content audit
and does not consume page budget.

### 6.2 Value ruling: valid ≠ worth changing (the evaluation step's third ruling)

The evaluation step makes **three** independent rulings, not two: does the finding hold
→ is the fix right → **is it worth it**. Four questions for value: is this change
**local tuning**? does it make a **substantive contribution** to the paper? does the
**space it takes match that contribution**, measured against the paper as a whole? was
the solution **designed from a whole-paper view**? **Any "no" means do not do it, even
if the finding holds and the fix is usable.** The space question asks about proportion
inside the paper and never about the page budget: §9 still bars withholding a finding or
a suggestion because it adds words.

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
counterexamples only a formalist could construct, defensive additions in the name of
transparency. This section stops **the real problems not worth fixing**: the problem
exists, but fixing it makes no observable difference to the paper. Both gates must be
passed.

### 6.3 Side-effect ruling: is the cure cheaper than the disease? (the fourth ruling)

- **Two questions the three rulings never ask**: is the fix's **side effect cheaper than the
  original defect**, and is **the original defect actually cured**? Validity, fix and value
  all interrogate the fix, never its cost. Replacing a weak antecedent (the reader bridges
  it) with a garden-path sentence (the reader must backtrack and re-parse) buys the dearer
  defect; the quieter form replaces an unparsable statement with one that parses and is
  false, which the next round is **less** likely to catch.
- **Boundary**: only substitution **within one quality dimension** is gated (readability for
  readability, precision for precision, naming for naming); cross-dimension repair (a fact
  corrected, a missing definition supplied) has predictable side effects and needs no
  separate ruling. Both questions belong to the **independent verification role that took no
  part in the three rulings**: proposer and evaluator are already immersed in their own
  diagnosis. This ruling necessarily runs **after** the edit lands, because a side effect
  cannot be read off a prediction, only off the new text.
- **Failing it has one outcome: the edit is rolled back**, either to the original defect or
  to a different fix that passes. It is recorded as "fix unusable" under §5, never as "no
  problem here", and the original finding stays open.

### 6.4 An external scorer's score change is not a quality signal

- **Any scoring function orthogonal to the dimension you optimize is this case** (LLM
  review, readability scores, grammar-checker scores alike): the core failure is letting a
  function that does not measure your quality dimension drive content rulings. Before
  editing on a score, re-sample the **same** version several times to see the spread, and
  check sentence by sentence whether the criticised text is present verbatim in the version
  that scored well.
- **Failure form**: one system, two runs, accept and borderline reject; attributed item by
  item, the prose bore no real responsibility for the drop, and the wording attacked in the
  low run stood word for word in the high-scoring version, listed there as a core
  contribution. Correct prose then gets rewritten for sampling noise, with page budget and
  content rulings handed to that function. **Boundary**: concrete checkable charges (a
  number that does not add up, a claim contradicting the artifact, a wrong citation) are
  settled on the facts, score aside; a score that stays low across re-samples of one version
  is a true signal.

## 7. The over-auditing gate (the audit loop's own most common disease)

- **False-belief test** (the execution criterion for hard rule A.5, "do not manufacture
  audit problems"): without the qualifier, would a reader reading linearly in compiled
  order form a **false belief** that adjacent text does not correct → real finding.
  Merely "a formalist could construct a counterexample" → not a finding.
- **Qualifier-count gate** (the operationalization of hard rule A.9, "state the
  applicability domain in exactly one place"): stop as soon as one qualification needs to
  be inserted in more than one place. Once a fix grows into "insert the same word N
  times", rule it over-auditing and roll the whole thing back. A same-shaped sentence in
  a headline position is prose gloss; its truth value is set by the evidence frame of
  the chapter it sits in, **not by the universal form of the formal statement it
  glosses** (in a theorem paper that formal statement is the theorem; in empirical,
  measurement or qualitative work it is the glossed result statement and its
  applicability domain).
- Two exceptions: **removing an internal contradiction** (change only the side that
  genuinely collides), and **reference, arithmetic, notation or factual errors** (judged
  by ordinary standards).
- **"The reader cannot recompute it" is not a defect criterion**: only a gap that makes a
  body-only reviewer form a **false** belief counts. Leave alone places that lack detail
  but where the belief is true. Nothing may be added on the grounds of "improving
  checkability".
- **Absolutely no over-defensiveness under the interface of "honest disclosure" (author
  ruling, hard rule)**: adding disclosure sentences, disclaimers or limitation notes in
  the name of honesty, transparency or keeping the reader informed is over-defensiveness
  through another entrance. A disclosure is allowed only when **omitting it would make
  the reader form a specific false belief** (you must be able to state what that false
  belief is and why adjacent text cannot correct it), and the same fact is disclosed once
  only, where the information belongs. Any disclosure sentence for which no specific
  false belief can be stated must not be added, and existing ones must be deleted. No
  step may add one on the grounds that "one more disclosure is safer".
- **A disclosure finding that survives the false-belief test still has a fixed repair
  order**, with a standalone disclosure sentence as the last resort. Four mechanical gates,
  any one of them empty voiding the finding: you can name the specific false belief, you can
  point at the text that triggers it, the information **carries truth-value
  responsibility**, and repair in place has been shown insufficient. Order, highest first:
  delete the misleading wording; rewrite the sentence that makes the claim; state the
  minimal fact once where that information belongs; a standalone disclosure sentence.
- **Reverse boundary: a disclosure that carries truth-value responsibility may not be
  deleted.** The dividing line is **whether some statement in the body becomes false once it
  is gone**, not whether the reader would like to know. In quantitative work this shows up as
  arithmetic: an overlap count that lets a total reconcile stays, while which particular item
  overlapped can go. Elsewhere it shows up as a stated condition a theorem, a definition or a
  qualitative claim silently depends on. Distortions of the "claims something exists that
  does not" kind are always fixed and stand outside this order.
- **Before changing a headline's prose gloss, check whether the chapter it glosses makes
  an equally strong claim**: changing only the gloss and not the chapter trades one
  inconsistency for another.
- **Minimal edit**: change one word fewer wherever possible; a rewritten fix preserves
  the author's original sentence patterns and wording by default. Paragraphs the author
  wrote or rolled back by hand are the author's choice: wording-preference items may not
  be filed again there, though substantive defects may still be reported.

## 8. Fix gates

### 8.1 Wording gate (mechanically executable, defensive)

For every word in the fix that was not copied verbatim from the original sentence, grep
the whole repository: is it a term defined in italics somewhere, a column header of some
table, a value of some state machine? On a hit, pick another word. Whoever proposes the
fix will not check this themselves.

### 8.2 Whole-paper gate (constructive; takes priority over 8.1)

**The choice of fix must itself target the whole-paper optimum, not "the problem is gone
at the landing site".** 8.1 and the seam gates of §13 are defensive (do not break
something else). This one asks a different question: is this fix optimal at whole-paper
scale? Finishing only the defensive checks does not count as finished.

Four questions before any fix lands:

- **Does a correct version already exist elsewhere in the paper?** If so, reuse it
  verbatim; inventing a third phrasing is not allowed. When the same assertion appears N
  times and only one is off, the fix is to align that one to the other N−1, not to
  rewrite it in place.
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
calls a sentence "too strong" or "unclear": **the reviewer's location is usually right and
the diagnosis usually wrong**, so fixing by the reviewer's diagnosis fixes the wrong thing.

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
- **In audit rounds the page count is a monitoring metric, not an action target**: the
  per-round compile-and-check exists only to measure and report. An overrun is fixed in
  delivery; a shortfall is reported, as above. **Writing a monitoring metric in
  as an action target** (e.g. a criterion saying "below the floor, add content")
  immediately induces decisions that sacrifice content for layout; it is the page-budget
  projection of "proxy metric substitutes for user outcome". Audit rounds have exactly
  three actions on page count: compile, measure, report. The one exception is a round
  delivery sends back specifically to act on the budget, whose scope and exits are
  defined in `SKILL.md`; it still may not add content, and everything above still binds it.

## 10. Table criteria

- **Column-header subject test, in two steps**: first ask whether the cell plus the
  column header **parses as a proposition** (parsing comes before truth), then ask
  whether it is true. A cell without its own subject borrows the header's subject, and
  the header must be true of it; a cell with its own subject treats the header as a mere
  column label. **Before changing a header, count how many cells are borrowing their
  subject from it.**
- **A conjunction cannot be tabulated row by row**: if the truth of the row or column to
  be added depends on several other rows holding simultaneously, its place is prose.
  Table rows are parallel by construction, and "A and B and C" crammed into one row loses
  the "and".
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

## 11. The four-role loop for content audit, and pipeline parallelism

A content-audit round uses four mutually separated roles: domain audit produces
candidates; independent evaluation rules on validity, fix and value; the revision role
implements only cleared items; the independent verification role blind-checks hunks,
cross-chapter interfaces and the content-audit exit conditions on the current, revised
version. A failed verification carries new evidence into the next lap; without independent
verification there is no close-out.

### 11.1 Pipeline parallelism (how parallel execution goes wrong)

Which tasks may run in parallel, which serial barriers must not be broken, and the
dispatch and close-out discipline are orchestration, defined once in `SKILL.md`
"Parallel-first scheduling" and not restated here. This section carries only the failure
forms and the measured lessons.

- **Cross-round pipelining**: during round N's revision and blind review, start round
  N+1's audit paths that do **not** intersect this round's edit regions (partition the
  regions at dispatch time; intersecting paths must wait for the commit).
- **Two adversarial agents instead of serial evaluation**: dispatch two mutually invisible
  agents on a critical path; adopt on agreement, adjudicate only on divergence.
  **Independence comes from different paths, not from ordering**: running the same
  evaluation twice in sequence buys rounds, not independence.
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

A lesson that holds only for this paper goes into the project `AUDIT-LOG.md`; a lesson
that comes from a general operation reproducible across papers, and that no rule here
already covers, is written into this rule library directly.

## 12. Contaminated premises mean restart

When the premise given to a sub-agent is wrong, **restart on discovery; do not send a
correction and let it continue**. A correction can only constrain the reasoning that
follows the message; what it already discarded, downgraded or rewrote under the wrong
premise is neither in its output nor recoverable by asking. The cost of a restart is
visible, the cost of contamination is not, so take the visible one. An agent that has hung
but **produced no conclusions yet** may be woken and resumed; that is not contamination,
because there is no reasoning done under the wrong premise for a correction to arrive after.

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
- **Deletion gate**: grep once each for the symbol names inside the text to be deleted,
  the original phrases that redeem promises made in the introduction, and the anaphoric
  nouns in the following three sentences. If any hit count is 1 (the text to be deleted is
  the only place it is redeemed), deletion is forbidden. Before deleting pre-existing
  text, run `git log -S "<fragment>"` to check whether it was deliberately kept in earlier
  rounds.
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
  discipline are dispatch orchestration: see `SKILL.md` "Parallel-first scheduling".

## 14. Boundaries for verifying records and supplementary material

**Applicability**: these items assume the paper delivers a checkable artifact (human
coding/review records, supplementary material, or archived data). Papers with no such
delivery surface (pure theory, pure method, short papers with no supplement) are out of
scope.

- Executed review/coding records are **traces**. Demanding extra data or rewriting records
  because "a reviewer cannot recompute it" is falsifying records. Whenever the urge to
  chase a data source arises, ask first: is this serving the reader, or serving the
  feeling of "I verified it"?
- **Verification has two levels**: with the records out of reach, settle the case using the
  paper's own chain of definitions (the paper is a closed formal system, and most "we must
  look it up externally" questions are answered by its own state machine); with the records
  in hand, a self-consistent definition chain is only a necessary condition: **verbatim
  checking is the verification**, and any body assertion citing the records must be checked
  against the record text.
- **The delivery-surface citation chain must be checked in both directions**: check both
  "does the artifact contain what the paper names" (missing = false statement, must fix)
  and "does the paper mention what the artifact contains". **A reverse-direction gap
  produces no false statement**, so every "claim vs. artifact" check is immune to it; its
  damage is different: **wasted delivery** (the reader opens material the paper never
  mentions and cannot place it in the evidence chain), and it makes two findings collide
  in the same place: "the named ones count correctly" and "there is a problem here" are
  each half right, and the next round easily uses the former as a shield to suppress the
  latter (the exempt-zone form of §5). **Only running both directions counts as checked.**
  The fix location for a reverse-direction gap is constrained by the citation hierarchy
  (body → appendix → supplementary material; the introduction point can only be on the
  appendix side). **That hierarchy holds only when both an appendix and supplementary
  material exist**; short papers with no appendix (journal letters, workshop papers) do not
  fit it, and the location is judged by whatever levels actually exist.
- **Archived data is a historical snapshot, not current truth**: writing back from an
  archive requires overlaying every ruling made after the archive, and re-checking each
  borderline instance against the rules.
