# Writing Rules (Best Paper shared reference)

Hard rules for writing, revising, compressing, and organizing experiments across a whole manuscript. This file is the single source of truth for every rule numbered here. Other files cite the numbers and must not restate the content; conversely, this file does not copy rules that belong elsewhere.

Rules owned by other files: abstract, introduction, and contribution bullets in `abstract-intro.md`; figures, tables, and captions in `figures.md`; the de-AI checklist, final-pass polishing, and terminology unification in `polish.md`; audit method and process gates in `audit-method.md`. Chapter 7 of this file keeps a pointer only; chapter 4 keeps the title rules and points away for the rest.

## H.1 Author-wide hard rule: no em-dash anywhere in the manuscript

The ban targets the em-dash exactly: Unicode `—` (U+2014) and its LaTeX source form `---`.

**Not covered by the ban, and never to be deleted or altered in the name of enforcing it**: the hyphen `-`, and LaTeX `--` together with its rendered en-dash `–` (U+2013). The latter is normal syntax for numeric ranges (e.g. `2--6\%`), page ranges, year ranges, and compound ranges. Verify character by character, never by "it looks like a horizontal line".

This rule is numbered H.1; audit findings cite that number under A.10.

## Preamble G: the reader's stepwise understanding has the highest priority

Every rule in this file is subordinate to this preamble. Academic correctness, evidential honesty, and reproducibility are the floor and are never traded away. Above that floor, as long as the truth of the conclusions, the meaning of the evidence, and the reproducibility of the method are unchanged, brevity, completeness, formalization, style, defensiveness, layout, and author preference all yield to a stranger's single-pass understanding.

### G.1 A paper is a path to understanding, not an inventory of knowledge

A paper must not lay out related objects, conditions, and conclusions in the order they already occupy in the author's head. That the author knows these things are related does not mean the reader knows why they must be adjacent, still less that the reader can derive the next sentence from the previous one.

The unit of writing is not "what content have I not written yet" but "what problem does the reader face right now, and what necessary information does the next sentence add to solve it". Every new concept, distinction, comparison, condition, and conclusion must be produced by a problem the text has already raised. Content that is merely on topic but answers no current question must be moved later, deleted, or given a reason to appear.

### G.2 Always maintain the reader's current knowledge state

Assume a reader who knows the general background of the target field but not this paper's internal terminology, notation, taxonomy, comparison scheme, writing plan, or later conclusions. The author must not substitute their own whole-paper knowledge for what the reader has actually received at this point.

Check every sentence:

1. Are the objects and terms it uses already established by earlier text?
2. Do pronouns, superordinate terms, and generic names have a unique and clear antecedent?
3. Must the reader read further ahead to work out what this sentence is saying?
4. Does this sentence require the reader to hold several unexplained new concepts at once?
5. If everything after it were deleted, could the reader still restate this sentence accurately?

Any concept that can only be understood by reading ahead is a forward-comprehension failure. Defining it later, explaining it again, or adding a summary does not repair the break that already happened at first occurrence.

### G.3 A new concept must earn the right to appear

Before introducing any term, symbol, taxonomy, comparison, or formal object, all four questions must have answers:

1. What concrete problem in the earlier text makes the reader need it now?
2. Which already-visible ambiguity does it remove, or which two already-introduced objects does it separate?
3. What judgment can the reader make after it is introduced that they could not make before?
4. Will later text actually use it to carry argumentative work?

If any of the four has no answer, the object must not be written into the current paragraph merely because it exists in the research plan, the code table, the formal model, or the author's notes. Simple objects also need a reason to appear; complex objects especially cannot substitute "we will use it later" for an explanation now.

### G.4 Consecutive paragraphs must stand in a derivation relation

Sharing a topic is not being logically connected. Two paragraphs about the same field, system, or set of terms may belong in the same paper, but that does not show the second was produced by the first.

Each paragraph advances one main question. It opens by taking up a fact, contradiction, or open question the text has already established; it does the necessary explaining or arguing; and it ends on an intermediate conclusion the reader can restate, which creates a definite need for the next paragraph. Any sudden announcement that "several cases are needed", "several categories exist", "we now compare", or "this yields a framework" must first say why one comparison, one category, or the existing formulation is insufficient, and what each added structure answers.

Connectives cannot fake a derivation. Adding "therefore", "moreover", "next", or a vague transition improves surface cohesion only; it does not supply the missing causal, comparative, identifying, or argumentative relation.

### G.5 Separate the domain model from the reading model

The domain model answers which objects exist in the research and how they really relate. The reading model answers in what order a reader can come to understand them. The former may be a network, a cycle, or high-dimensional; the latter must be a path that can be entered step by step.

Writing is not serialization of the domain model. Fix the question the reader needs answered, choose the fewest objects sufficient for it, then order definitions, evidence, and conclusions. Completeness is not displaying every component of the domain model at once; it is having each load-bearing component appear in time to carry its load.

### G.6 Structural feedback must not be patched locally

"Abrupt", "I do not follow", "I had to read it several times", and "I do not see why this is being analyzed" are usually not a problem with one word or one connecting sentence: the reader's path of understanding has broken. On such feedback, restore the reader's knowledge state from the start of the section or paragraph and re-check how the problem arises, why the concept appears, and how the conclusion follows. Adding one more sentence at the point of complaint is not a fix.

If the problem keeps migrating among definitions, paragraph links, abstract wording, and comparison relations, the method that generated the passage is wrong. Rebuild the logical chain instead of eliminating the newest symptom. Effort already invested in the previous round is not a reason to keep the current structure.

### G.7 Proxy metrics must not stand in for real readability

A successful compile, a lower word count, shorter sentences, complete notation, consistent terminology, a reasonable number of paragraphs, a reviewer who eventually guesses the author's intent: none of these shows that the text can be understood in one pass. Each verifies only its own local property.

Readability verification must use a forward cold read: the reader starts from a blank state and restates the text sentence by sentence in order, without using later text to complete earlier text and without guessing at omissions from the author's plan. The check records the first sentence that cannot be restated immediately, the missing premise, and whether the break is an undefined object, a missing motivation, an unestablished relation, or a single overloaded sentence.

When using an independent reader, confirm they are reading the current version and ask them to look for breaks in understanding rather than deliver a general verdict. Their comments are themselves checked item by item against the current text; a reader's judgment is not an exemption from verification.

### G.8 Order of adjudication when rules conflict

When rules conflict, adjudicate in this order:

1. Do not change the truth of the conclusions, the meaning of the evidence, or the reproducibility of the method
2. Ensure a stranger can understand the text in one forward pass
3. Keep the argumentative chain complete and strong
4. Only then optimize brevity, rhythm, style, visual form, length, and defensive explanation

Do not pile up conditions the reader does not yet need in the name of rigor, and do not delete a qualifier that changes the conclusion in the name of readability. Real clarity means the necessary condition appears, in an understandable form, at the moment the reader needs it.

## Audit clauses A: non-negotiable

This section is the enforcement protocol for the whole file. Except where content is explicitly marked RECOMMENDED or non-mandatory, every rule here is a hard constraint. The auditor may only check whether a rule is satisfied. The auditor has no authority to renegotiate a rule, add balancing conditions, or lower the strength of enforcement to fit personal writing preference.

### A.1 No softening of rules

The auditor must not perform any of these conversions:

1. Reading "must" as "recommended"
2. Reading "must not", "cannot", or "prohibited" as "usually not advisable"
3. Reading "delete" as "could be kept"
4. Reading "keep only" as "may also be added for completeness"
5. Reading "do not raise this" as "still discuss it briefly to appear balanced"
6. Reading "organize around strengths" as "present strengths and weaknesses in full and equally"
7. Reading "do not concede defeat" as "honestly emphasize every result where we do not win"
8. Reading "must not answer questions the paper never raised" as "better to pre-empt likely reviewer comments"
9. Reading "structural problems must be rebuilt" as "one transition sentence may be enough"

Any such conversion makes the audit itself non-compliant.

### A.2 Only explicitly marked rules may be relaxed

Only clauses carrying a RECOMMENDED or non-mandatory marker may be adopted or not depending on paper type and target venue. The single other route is 0.5, and it is not discretion. What this clause forbids is an auditor relaxing a rule on judgment alone, which no amount of corpus evidence turns into.

In the body text, "must", "must not", "cannot", "prohibited", "keep only", "never", and "no skipping levels" all constitute hard gates.

"Should" and "prefer" state a mandatory direction of execution, not permission to skip. The auditor may choose among compliant implementations; the auditor may not use these words to cancel the rule.

### A.3 The academic floor must not be reused as a defense argument

Truth of conclusions, meaning of evidence, and reproducibility of method are guaranteed once, by the preamble. Having completed those three checks, the auditor must not again demand added defensive text on grounds of "rigor", "completeness", "balance", "reviewer risk", or "avoiding misunderstanding".

Any finding that asks to add or keep a qualifier, weakness, negation, disclaimer, or counter-argument must state explicitly:

1. Which core proposition's truth value it changes
2. Which piece of evidence's meaning it changes
3. Which method step's reproducibility it affects

If none of the three can be named, the finding is void and the content must not enter the manuscript.

### A.4 Defensive content is deleted by default

Defensive content enjoys no presumption of retention. The burden of proof lies with whoever wants to keep or add it.

If the auditor cannot show that a passage directly determines the truth of a conclusion, the interpretation of evidence, the reproducibility of the method, or the scope of applicability of a claim, that passage must be deleted, moved later, or rewritten as a positive statement of capability.

"A reviewer might ask", "this is more complete", "this looks objective", "just in case of misreading", and "better to mention it" are not reasons to keep it.

### A.5 No manufacturing of audit problems

The auditor must not require the paper to answer a challenge merely because one is theoretically conceivable.

Only claims the text actually makes, work the evidence actually carries, capabilities the method actually declares, and content the target venue explicitly requires fall within audit scope.

The auditor must not:

1. Invent a stronger claim the paper never made
2. Require the paper to prove it did not make that stronger claim
3. Add a new comparison dimension
4. Add a new evaluation objective
5. Add a new experimental obligation
6. Add a new stakeholder question
7. Add an imagined opponent and require the text to pre-empt it

Findings that violate this clause are deleted and never enter the revision list.

### A.6 No demands for artificial balance

A paper has no obligation to give equal display to strengths and weaknesses, positive and negative results, or supporting and opposing evidence.

The auditor must not invoke "balance", "comprehensiveness", "objectivity", or "avoiding bias" to require:

1. Adding negative results that do not affect the core conclusion
2. Emphasizing dimensions where this work does not lead
3. Listing tasks this work did not complete
4. Pairing every positive claim with a negative note
5. Attaching a self-weakening limitation to every contribution

Objectivity is guaranteed by strict alignment among claims, evidence, and conclusions, not by equal counts of positive and negative content.

### A.7 The scope of comparison is set by the core claims

Audit scope is fixed by A.5: only the claims the text actually makes. Requiring a metric, dataset, baseline, scenario, or objective the core claims do not cover is barred by A.5 item 3 and A.6 item 2; treating "does not lead across the board" as a defect is barred by A.5 items 1 and 2, since it invents the claim first. 1.4 owns the author-side rule that the narrative is not built on a contest this work loses.

### A.8 Unfavorable material does not automatically earn a place in the main text

The test is A.4's, applied to unfavorable material rather than to defensive phrasing: the burden lies with whoever wants to keep it, and A.4 already rejects "this looks objective" and "a reviewer might ask" as reasons. 1.1 keeps what is not a strength out of the main line, 1.2 bars the progress report, A.6 blocks the balance argument, and 1.13 gives the priority order for the material once it is out.

### A.9 Scope of applicability is stated once, in one place

A scope condition that determines the truth of a conclusion must be kept, but it must be stated in one place, accurately, and positively.

The auditor must not require the same limitation to reappear in the abstract, introduction, theory, experiments, discussion, and conclusion. Except where a specific section carries an independent retrieval role, other locations stay aligned by accurate citation or consistent wording.

Repeating a limitation adds no rigor; it adds self-weakening and reader load.

### A.10 Every finding carries the burden of proof

Each valid audit finding must contain all four of:

1. The specific rule violated
2. The specific text location of the problem
3. The direct consequence for reader understanding or for the core argument
4. The minimal sufficient repair target

A finding missing any one of these must not enter the revision list.

"Could be more comprehensive", "suggest adding discussion", "might raise doubts", "the wording could be improved", and "better to be more cautious" are all void findings.

### A.11 The audit adds no evaluation criteria

This file is a closed audit standard. The auditor must not add personal preference, generic writing templates, conventions from other papers, or an imagined reviewer's taste to the mandatory standard.

External requirements enter the audit only when the target venue states them explicitly, and their source must be labeled; they must never be disguised as rules of this file.

### A.12 Structural feedback gets a structural fix

The trigger, the point the rebuild starts from, and the local patch that does not count as a fix are all G.6's; the connective and the vague transition are also G.4's, the later definition and the summary paragraph G.2's, and the shortened sentence and the reader who guesses from later text G.7's. A.1 item 9 bars the auditor from accepting a transition sentence in place of the rebuild, and the forward cold read of G.7 is the test of whether the break is gone.

### A.13 Audit verdicts must be hard verdicts

Each hard rule gets exactly one of:

1. `PASS`: the rule is satisfied
2. `FAIL`: the rule is not satisfied and must be fixed

Vague states such as "mostly satisfied", "acceptable in principle", "not a big deal", "could be kept", or "depends" must not be used to bypass a hard gate.

### A.14 Conflicts are adjudicated upward only

The order is set by G.8 and the goals that yield to it by the preamble to G; applying that order is what adjudicating upward means. The opening of section A already bars the auditor from putting balancing conditions in its place.

### A.15 Final veto clause

The audit fails outright if any of these occurs. Each item names the rule that owns it and adds no requirement of its own.

1. Any defense barred by A.5 and by 2.3 item 1 is added
2. Any negative content barred by A.6 item 1 is added for the sake of balance
3. Any dimension kept out of scope by A.6 item 2 and 1.4 is promoted to a core evaluation item
4. Any imagined reviewer comment barred by A.5 item 7 and A.11 is used to enlarge the paper's burden of proof
5. Any repetition barred by A.9 is used in place of claim-evidence alignment
6. Any local patch rejected by G.6 is used on a broken path of understanding
7. Any proxy named in G.7 is used in place of forward readability
8. Any hard rule in this file is read as an optional suggestion, against A.1 and A.2

## 0. Meta-rules: ordering and precedence

Apart from the preamble, violating these causes the later rules to be misapplied. They fix the order of every other revision decision.

### 0.1 Establish the role before judging the quality

For any chapter, paragraph, equation, table, or figure, the first question is always:

> What role does it carry in the argument chain?

Only then comes the second:

> Does it fulfill that role?

Skipping the first step degrades judgment into "this is not how I would have written it", so every difference gets recorded as a defect and each round of edits grows larger than the last. Most wasted revision originates here.

### 0.2 Existence before optimality; counterexample before justification; conclusion-changing before prettier

The order cannot be reversed: a claim is shown to hold before it is discussed as the best phrasing, and an edit survives a counterexample check before it is argued for on its merits.

### 0.3 Edit size is set by the nature of the problem, not by the previous round

Local problems get local fixes. That the previous round was too conservative is not a reason to restructure chapters now; that the previous round overreached is not a reason to limit this round to punctuation. Each round judges independently.

### 0.4 Comprehension by a stranger first, appeal second

The title and the abstract are the paper's entrance, not the author's compression of the whole text. The reader is the one G.2 defines.

Before pursuing brevity, counterintuitiveness, rhythm, or a hook, show that this reader can answer four questions without reading the body, re-reading, or guessing at terms:

1. What object does the paper study?
2. How is it usually assessed by existing work?
3. What important problem does that assessment miss?
4. How exactly does this paper close that gap?

If any one is unanswerable, fix the order of information and the definitions first; do not discuss style. A title that only makes sense after reading the paper, and an abstract whose opening can only be reconstructed from its ending, are both entrance failures.

**Counterintuitiveness is not something the author declares, and tension is not manufactured by sentence structure.** It exists only once the reader understands two facts, sees the surface conflict between them, and knows why that conflict matters for the conclusion. A "hook" that skips these three steps is a slogan.

### 0.5 Field evidence outranks generalized guidance

When an observation from the target venue's own accepted papers contradicts a
generalized clause in this rule library, **the observation wins**. The library's
generalized clauses are derived from principle and from one author's experience;
the venue's accepted papers are what the venue actually rewarded. Record the
conflict and the ruling in `AUDIT-LOG.md` so later rounds do not re-litigate it.

Two conditions on the observation, both required:

1. **It carries its sampling frame**: which venue, which years, how many papers,
   which column of which tabulation. An impression ("past papers all seem to do
   X") is not evidence and outranks nothing. This is why Setup requires the
   corpus statistics to record their frame.
2. **The clause it overrides is generalized guidance.** Generalized guidance is
   this library's advice on **what a paper should look like**: shape, phrasing,
   arrangement, genre convention. It is not the library's rules on **what counts
   as a problem and how a verdict is reached**. Field evidence never overrides
   any of the following:
   - The venue's own mandatory requirements (page limits, anonymity, template).
   - Academic correctness and evidential honesty: truth of conclusions, meaning
     of evidence, reproducibility of method. A venue accepting a practice does
     not make that practice sound.
   - **The preamble and G.1 to G.8.** A stranger's single-pass comprehension is
     the standard the venue's readers are also subject to. Papers that were
     accepted despite a broken path of understanding are evidence about the
     review process, not licence to break it.
   - **A.1 to A.15.** These govern how the audit itself behaves, not how the
     paper looks. Nothing observed in published papers can tell you how to run
     an audit, and A.15.8 stays in force: reading any hard rule as an optional
     suggestion fails the audit outright.
   - Author-wide hard rules (H.1, and the hard rules carried in
     `abstract-intro.md`, `polish.md` and `figures.md`). These are the author's
     standing decisions across projects. Field evidence showing the venue
     tolerates otherwise is expected and does not loosen them.

Acceptance proves a practice is permissible at that venue. It never proves the
practice is optimal, and never proves it caused acceptance.

## 1. The launch-talk principle

Treat the paper as an academic launch talk, not a project report, an experiment log, or a self-review.

The task is not to present every aspect of the work evenly. It is to identify the value most worth publishing and to build the most favorable, most complete, and most convincing narrative around that value.

### 1.1 Organize the paper around strengths only

Look first for what this work genuinely leads in, is unique in, or is irreplaceable in: a new capability, a new problem, a new mechanism, a new perspective, wider applicability, lower cost, higher efficiency, better scalability, a more meaningful trade-off. Content that does not amount to a strength must not become the main line.

### 1.2 Do not write a progress report

Do not organize as "what we did first, what we tried next, which attempts failed". Keep only the logic that finally holds: why the problem matters, why existing methods fall short, what new solution this work provides, and how the evidence supports it.

### 1.3 Do not volunteer negative assessments

Do not summarize for the reviewer where this work is weak, where it loses, or where it falls behind. Do not use self-weakening phrasing such as "unfortunately", "merely", "still lags", "limited effect", or "a serious shortcoming". When a result is not a strength, do not distill it into a conclusion, and never help the reader escalate a local observation into a verdict on the whole method.

### 1.4 Do not enter a contest you lose

If this work does not lead on some metric, do not build the narrative on that metric. Re-select the task definition, evaluation dimension, application scenario, constraint set, or basis of comparison that better reflects this work's value. Do not fight for a championship that is not yours; make clear that this work wins a different and more meaningful contest.

### 1.5 Do not concede defeat; rewrite the comparison logic

Facing a result where the work does not lead, do not use direct failure phrasing such as "we are weaker than", "performance drops", or "fails to surpass". Judge in order: must this result be discussed at all; can it be explained by different objectives, constraints, or applicable scenarios; does it reflect a reasonable trade-off; can the claim be narrowed to avoid an unnecessary head-on comparison; should the main line be adjusted so that this result no longer carries the burden of proving the core contribution?

### 1.6 Strengths must be stated explicitly

Do not expect the reviewer to discover the contribution from a table or an equation. For every result that supports the value of this work, state actively: under which condition this work performs best; why that advantage arises; what practical problem it solves; and why this capability deserves attention compared with existing methods.

In particular, when this work delivers a stronger form of result than comparable work, for example an exact value rather than an interval, a directly usable conclusion rather than a qualitative judgment, or a measurable quantity rather than an existence statement, **the text must say explicitly why that difference is worth something**. This kind of advantage is the one authors most often assume the reader "will obviously see".

### 1.7 Control the scope of comparison

Do not pursue the unnecessary goal of leading on every dataset, every metric, and every setting. Make only the claims the evidence firmly supports, and choose the experiments and comparisons that fit those claims. Persuasiveness comes from tight alignment between claims and evidence, not from the number of comparisons.

### 1.8 Experiments are argumentative instruments, not a result warehouse

Every experiment must carry an explicit role, for example: showing the core method works; showing the advantage comes from the key mechanism; showing the method has value in the target scenario; ruling out the most likely alternative explanation. An experiment that cannot strengthen the main line, that distracts, or that invites unrelated disputes must be deleted, downplayed, moved, or redesigned.

### 1.9 Rebuilding the story from scratch is allowed

When the results cannot support the original narrative, do not defend the original narrative. Redefine the problem the paper actually solves, reorder the contributions, re-select the headline results, and redesign the title, abstract, introduction, and experimental structure. The story serves the strongest evidence, not the initial plan.

### 1.10 Do not hand the reviewer a knife

While writing, keep checking: does this sentence unintentionally enlarge the responsibility this work must carry; does it raise a question nobody asked; does it describe a local observation as a general defect; does it use a negative judgment broader than the evidence; could a more precise positioning avoid this pointless self-attack?

Do not manufacture audit problems, do not enlarge the attack surface, do not complete the opponent's argument for them.

### 1.11 The abstract and introduction must open like a launch talk

The opening must quickly establish: an important unsolved problem; the key gap in existing methods; this work's distinctive approach; and the most substantial result and its significance.

Do not start from implementation details, research process, or a large body of background, and do not discuss shortcomings before the contribution is established.

"Like a launch talk" does not mean slogans, suspense, puns, inflated adjectives, or unexplained counterintuitive statements. An effective opening first lowers the barrier to understanding, then establishes importance: the reader must know the object, the common practice, and the cost of failure before the gap can be felt. If the supposed hook depends on this paper's internal comparison scheme, terminology, or counterexample conditions, it is not an entrance but a private signal only the author can read.

### 1.12 The conclusion only reinforces what should be remembered

The conclusion is not a retrial of the paper. It makes the reader remember what this work solved, proposed, and proved, and why it matters. Do not add new self-negation or enlarged limitations in the final paragraph.

### 1.13 Default decision rule

For any unfavorable material, handle it in this priority order:

1. Delete content unrelated to the core claims
2. Narrow the claim to avoid a pointless head-on comparison
3. Switch to an evaluation dimension that better shows the value
4. Explain the result as a difference in objectives or a reasonable trade-off
5. Reorganize the experiments so the strength becomes the visual and narrative center
6. Redefine the paper's story
7. Only when it is unavoidable and genuinely affects the core conclusion, give the necessary statement

### 1.14 The end goal

Every chapter, paragraph, table, and sentence works toward one thing:

> Convince the reader that this work solves a problem worth solving, proposes a method worth attention, and already has clear enough evidence for its value.

Do not present evenly, do not volunteer weakness, do not write an experiment diary, do not attack yourself on the reviewer's behalf.

## 2. Defensive hedging

The point is not "delete all qualifiers". It is:

> Keep the conditions that decide whether the conclusion is true, delete the self-justification driven by imagined challenges, and rewrite the necessary boundaries as scope of applicability and statements of capability.

### 2.1 Why over-defense damages a paper

**It manufactures problems the reader did not have.** Repeatedly announcing what the paper does not prove, does not estimate, and does not validate leads the reader to infer that these things were supposed to be done and were not. In plugging one line of attack, the author generates the attack question for the reviewer.

**It shifts the burden of proof.** The paper only had to prove one precise proposition. After a long list of "what we do not prove", the reader assumes the paper is also answerable for those larger questions.

**It makes the contribution look weaker.** [English manuscripts] Phrasings such as `only a benchmark`, `merely descriptive`, `does not validate`, `cannot establish`, and `is not new` may each be correct in isolation; densely packed, the impression is not "the boundaries of the conclusion are precise" but "the author does not believe the contribution is strong enough either".

**It breaks the causal chain.** A good paper leaves the reader with: problem, key decomposition, formal result, evidence, design implication. Over-defense turns that into result, disclaimer, another result, disclaimer, imagined challenge, another explanation. Each part is locally rigorous while the whole reads like stitched-together rebuttal rounds.

**It spends the most expensive resource.** What is scarce is not word count but the reader's cognitive capacity for understanding the core contribution.

### 2.2 Qualifiers that must be kept

Keep only conditions that change the truth of a proposition or the meaning of evidence. Typically:

1. Quantifier conditions, for example whether the conclusion holds for one fixed value or for all admissible values
2. The target type of the conclusion, for example worst case versus average behavior
3. Object identification, for example whether a measured quantity and a theoretical quantity refer to the same object, and whether what the experiment can observe matches what the theory requires
4. What a strong word applies to, for example whether "exact" or "optimal" modifies an idealized baseline or a restricted implementation, and which half the restricted implementation inherits
5. The semantics of a variable, for example what the quantity actually measures and how it differs from the quantity a reader would easily mistake it for

These are not defense; they are part of the conclusion. They are the conclusion's coordinates, not an apology in front of the contribution.

### 2.3 Content to delete or move out of the main line

1. Answering questions the paper never raised
2. Explaining why some synthetic experiment, negative control, or mechanism comparison was not done
3. Listing five or six quantities in a row that were not identified
4. Repeating the same limitation across several chapters
5. Volunteering that the proof tools are simple or that a classical idea is not new
6. Pre-answering potential reviewer comments one by one
7. Spending a whole paragraph proving the author did not claim an obviously stronger conclusion

Test: **if deleting a sentence would not change the truth of a theorem, an experimental estimand, the interpretation of evidence, or the reproducibility of the method, it is probably not required in the main text.**

### 2.4 Paragraph audit

Ask five questions per paragraph:

1. What is the one claim this paragraph needs the reader to remember?
2. Does each condition directly change whether that claim is true?
3. Is it answering a question the paper never raised?
4. Does it repeat a boundary already stated elsewhere?
5. With all negative sentences removed, does the paragraph still state the contribution positively?

[English manuscripts] A paragraph containing more than two consecutive instances of `does not`, `cannot`, `only`, or `merely` is usually worth re-checking.

### 2.5 Whole-manuscript final check

1. Do the abstract, introduction, main results, and conclusion speak about the same central contribution?
2. Is each core claim qualified in exactly one place, with other locations kept consistent by citation?
3. Do the Limitations state the natural boundaries of the model and the evidence, rather than repeatedly disparaging results already reported?
4. After reading, is what the reader can most easily restate "what the paper found" or "what the paper did not do"?

If it is the latter, over-defense is still present.

> Precision is not obtained by enumerating every unsolved problem. It is obtained by aligning claims, conditions, evidence, and conclusions strictly.

## 3. Division of labor across chapters

**Every chapter can be stated in one sentence: the problem the reader enters with, and the conclusion they leave with.** A chapter that resists that sentence has no single job, so the type-specific duties below have nothing to attach to. G.4 asks this of a paragraph; at chapter scale it is the same test.

**A derivation chapter must deliver one uninterrupted derivation.** External material, literature evidence, and real-world calibration of parameters do not belong there. Placing them in a derivation chapter has two effects at once: the derivation is fragmented, and the evidence chapter is drained. (Derivation and evidence chapters appear in concrete papers as theory versus empirical chapters, method versus results chapters, and so on.)

**An evidence chapter must deliver a self-contained set of conclusions.** After reading it, the reader knows independently the status of **every object this chapter is responsible for settling** (the undetermined quantities, premises, parameters, or open judgments left by the derivation chapter), without going back to the derivation chapter to fill gaps.

**The two kinds of material must not be moved into each other.** If the evidence chapter looks thin or badly structured, there are exactly two correct fixes: pull back the evidence material scattered into the derivation chapter, or re-divide the sections inside the chapter so they correspond one to one with those undetermined objects. **Never move derivation into the evidence chapter, and never fold evidence into the derivation chapter.**

**Chapter-weight problems are solved by narrative pointing, not by splitting chapters.** If the most valuable result is buried in a mid-document subsection, the fix is to have the introduction point at it as soon as the problem is established and to make it the narrative destination, not to promote it to a top-level chapter and cut the derivation in half.

**A results chapter is organized in argument order, not written as an experiment log in execution order.** The main text keeps only results that support the core narrative; the rest moves to an appendix or supplementary material (applicability: the target venue accepts appendices or supplementary material). A results chapter explains only the method details needed to understand the results; full derivations, training strategies, and implementation details belong to the method chapter. When using benchmark results, say why those comparison targets were chosen and explain the practical use of the performance or insight; when reporting statistical tests, also say what the significance means for the claim.

**A discussion chapter does not repeat the abstract or the results.** It explains the broader theoretical or practical implications, states the natural boundaries of the method and the experiments in one place, and points out the remaining challenges and well-grounded next directions. New results and new core claims must not appear for the first time in the discussion.

## 4. Title, abstract, and introduction

This chapter covers the title only. All abstract, introduction, and contribution rules live in `abstract-intro.md`. This file does not copy them.

### 4.1 The title must be self-contained

The title's job is not to summarize every contribution, but to let someone who has not read the paper know immediately: what the object of study is, what key relation this work challenges or establishes, and why this paper differs from neighboring work. Foreground the primary finding, method, or resource, while keeping the core words readers in the field would actually search for.

The title must pass all of the following on its own:

1. **Clear object.** Not just an abstract result noun such as bound, evidence, or security; the reader must know whose problem this is and what the problem is.
2. **Clear relation.** Not two juxtaposed concepts, but what holds between them: distinction, condition, conflict, causation, upper bound, or evaluation gap.
3. **Recoverable claim.** From the title alone, the reader can say in one plain sentence what the paper most likely proves.
4. **No dependence on the body.** The title must not require the reader to already know this paper's notation, taxonomy, comparison world, theoretical counterexamples, or internal names.
5. **Strength matched to evidence.** Use `can` for an existence counterexample and `alone` when the evidence by itself is insufficient [English manuscripts]; do not inflate "cannot be derived under some conditions" into a general negation.
6. **Searchable.** Keep the object words and problem words readers actually search for; avoid metaphors that are meaningful only to the author.
7. **Clear but not oversimplified.** Avoid long compound noun phrases, non-standard abbreviations, and jargon, and do not pack in technical detail only experts need. Accuracy comes from stating the relation and the boundary, not from term density.

The following title forms usually fail:

1. Rhetorical questions, puns, or "where X ends, Y begins" constructions. A question weakens a definite claim; puns and metaphors mislead and hurt retrieval.
2. Elliptical forms such as "X remains unachieved", "the missing link", or "beyond metric Y", because what is elided is exactly the relation the paper needs to explain.
3. A method or framework name only, with no object of study and no result relation.
4. A broad question only, with no indication of the answer the paper gives.

A more reliable form writes the key relation out: the object of study, the observed fact, and the conclusion that does not follow automatically from that fact all appear in the title, joined by an explicit relational word (condition, limitation, conflict, causation, upper bound, distinction). This is a requirement on what the title states, not a template to fill in.

## 5. Deletion safety

This is where the compression stage most often goes wrong.

### 5.1 Three questions to answer before deleting

Before deleting any sentence, all three must be answerable:

1. Does it change the truth of a theorem, the definition of an estimand, the interpretation of a piece of evidence, or the reproducibility of the method?
2. **Is it the only place some symbol, concept, or condition is defined?**
3. **Is it the only place the paper answers a question raised by a claim the paper itself makes?**
   Scope is set by A.5: a claim actually in the text, evidence actually presented, a capability
   actually declared, or something the venue explicitly requires. A question no more than
   conceivable does not qualify, and under A.4 "a reviewer might ask" is never a reason to keep.

If any answer is yes, it cannot be deleted.

### 5.2 A successful compile is not evidence of deletion safety

The compiler does not check whether a symbol was ever defined, whether a scope declaration is still present, or whether a reviewer question still has an answer. "No cross-reference errors" only means no label broke; it says nothing about content integrity.

Typical failure: a sentence that looks redundant with the corollary after it is deleted, but that sentence was the only definition of a symbol which then appears undefined in the corollary's conditions. The compile reports nothing.

### 5.3 Demoting a result to a subordinate clause is deletion

Folding a numbered corollary into a clause inside a paragraph keeps the content formally, but the reviewer looking for it among the results will not find it and the scanning reader will skip it. **Anything that answers a foreseeable reviewer challenge must keep the form of a result** and must not be demoted to an incidental remark.

### 5.4 The dual role of Limitations

Conditions in Limitations come in two kinds:

- **Repeated disparagement**: already stated more strongly elsewhere, repeated here only as another self-deprecation. Delete.
- **Scope declaration**: states the range in which the main conclusion holds. It may also appear at a technical location in the body, but the reviewer scanning Limitations reads it here. **Do not delete it from Limitations on the grounds that "it is somewhere deep in the body".**

## 6. Fitting the page budget

> **Applicability**: the target venue sets a hard page or word limit. Journals with no page limit, and theses with a minimum length, do not trigger this chapter. Once triggered, the order inside this chapter is a hard gate.

**A page budget must not drive the priority of content decisions.** Follow this order strictly, with no skipping of levels:

1. **Pure restatement**: paragraphs whose proposition is already stated more strongly elsewhere
2. **Decorative data**: table columns, thresholds, secondary metrics, and auxiliary statistics that carry no argumentative role
3. **Non-load-bearing extensions**: corollaries or side results whose removal leaves no gap
4. **The conclusion chapter**: it mostly restates the body, so it compresses at the lowest cost of any chapter
5. **Related work**: compress it, keeping every citation that a claim in the body leans on
6. **Branch content of no value to the main storyline**: anything the storyline does not need is deleted or reduced to one sentence, without asking item by item. It comes before figures and tables because content the storyline does not need costs nothing to lose, while a figure is the hardest object in the paper to rebuild. It is also the only level that takes judgment rather than counting, and **deciding what has no value is content work, not layout work**, so this level is executed by a content-audit round rather than by whoever is compressing the layout; the routing is in `SKILL.md`
7. **Figures and tables, cautiously**: they cost the most per unit area, but they are also the hardest to rebuild and the easiest to break, which is why this level comes after every prose level rather than before them. Work down it in order: shrink the object with the highest unit cost of space, merge panels or columns that share a coordinate system, and only then consider dropping the one with the lowest information density. A table that carries no argumentative load may be dropped outright here. Deleting a whole figure is the last resort of this level, and never applies to one carrying evidence the text does not restate
8. **Stop here**

Truth-relevant content, symbol definitions, and scope declarations **are untouched under any page pressure**. Change a figure, change the basis of comparison, or narrow the claim before touching these.

Compressing space by enumerating disfluent short sentences is prohibited. A paper is reading material and must first be readable fluently.

### 6.1 The target is the top of the budget, not the shortest possible paper

The page budget has two bounds, the **limit** and the **floor**, both recorded in `AUDIT-LOG.md` in Setup along with the convention by which pages are counted. Overrun and shortfall are not symmetric, because their consequences are not. **Exceeding the limit is a hard failure and risks desk rejection; it is never delivered.** Sitting below the floor wastes room that was available for making the work understood, so it is a signal to investigate, not a failure to repair.

**A shortfall is never closed by adding content**, and whether the body explains enough is an audit question, not a page-count question. Padding, extra defensive text, decorative data, and restated conclusions are barred here by A.4 and A.5. Read the shortfall as a diagnosis instead, in this order:

1. **Did compression overshoot?** Restore load-bearing material cut at levels 1 to 7, most recent cut first. This repairs damage this process did; it is the only action a shortfall authorizes.
2. **Otherwise?** Leave the space unused. A shortfall that survives into delivery is **reported to the author there, not repaired**: at that point every remaining way to fill it is padding.

### 6.2 Costing a figure

The comparison is not "a new figure versus some pages of text" but "is each figure worth the space it takes".

A figure is not worth keeping if all of its content is already given in full in words in the abstract or introduction. Shrinking the figure with the highest unit cost of space (a full-width figure in a multi-column layout) is the cheapest concession available, and it is tried before any figure is dropped.

## 7. Figures and tables

All figure and table rules live in `figures.md`, including captions. This file does not copy them.

## 8. Citation rules

**The criterion for keeping a citation is whether it provides the support some claim needs, not whether it appears again later.**

Frequency of use is unrelated to the support relation. A citation that appears once must be kept if it is the sole basis for a modeling choice, a conceptual distinction, or a claim.

If a group of citations reads like a list, the correct fix is **to state what each one supports**, not to delete them. This usually costs a few dozen more characters and turns a pile of citations into a set of positions.

## 9. Measurement and reporting

1. **Do not report an estimate as a measurement.** When reporting a number, state how it was obtained
2. **Absolute page counts obtained with placeholder content (draft figures, lorem ipsum, substitute fonts for missing ones) are unreliable, and so are those from an approximate typesetting environment.** Only increments (character counts, line counts, area) transfer across typesetting environments
3. For any judgment about layout, measure before changing, not change and then explain
4. Say explicitly which parts cannot be verified, and give the other party a way to verify them
5. Keep exactly one formal name per concept, and do not dress a simple relation in obscure terminology
6. **A core concept must be able to enter the existing scholarly conversation.** Established superordinate terms, existing definitions, and moderate packaging are available for naming and framing the paper's central objects, provided nothing substantive is misrepresented: the object, its scope, and the strength of what is claimed about it stay what the evidence makes them. Narrowing a term until it is exact and recognized by nobody is item 5's failure taken from the other side, and the precision it buys does not repay it: a concept no one can place cannot be searched for, compared with neighboring work, or argued against. This is the whole-paper form, binding on the paper's own name for its central object, on chapter and section names, and on how the body frames them; the entrance-specific test is `abstract-intro.md` §2.1, and the title is 4.1.
