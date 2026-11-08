# Sentence, terminology and final-polishing methods

Writing requirements are owned by writing-guide; execution is owned by audit/routing. This file provides methods to use when relevant.

Basic sentence understanding, terminology, evidence visibility and necessary logical repair belong to ordinary substantive revision. They do not wait for a final-polishing authorization. Only the final round of rhetorical optimization after substantive convergence requires the author's explicit decision. A repair that changes scientific meaning returns to the relevant content verification under the existing authorization.
Background sources:

- Source 1 labels earlier academic-humanizer material. The methods below are self-contained; another skill is not an installation requirement.
- Source 2 labels the prior notes on *How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review* (Li, Wang et al., arXiv:2608.08975). The detailed notes are optional background, not an executable dependency, a rule authority or proof of benefit for a new manuscript.

Genre, venue, official limits and house style come from current task evidence. Apply patterns to actual reader difficulties; a score or source label does not decide what the paper must say.
## 0. Scope and application

Use the patterns below to find concrete reading problems, not to score text by word frequencies. Inspect actual clauses and their reader duties. Preserve correct facts, necessary conditions and effective contrasts; if a substantive error is found, use the authorized revision and verification workflow rather than silently changing it during polishing.

## 1. De-AI pattern methods

Locate candidates, read their context and propose a complete improved sentence or paragraph. Verify both meaning and readability. This file does not add a separate proposal/approval/report cycle.

### Layer 1: general AI tells

Word lists and sentence examples below are [English manuscripts]; Chinese
manuscripts identify the same patterns in their own language.

Inflated significance (`marking a pivotal moment`); pseudo-depth `-ing` tails
(`..., highlighting...`); promotional or rhetorical diction (`rich`, `vibrant`,
`groundbreaking`); vague attribution with no source (`experts argue`); AI
vocabulary (*delve, underscore, intricate, tapestry, testament, landscape*
[abstract sense]*, pivotal, showcase, foster, leverage* [filler sense]*, realm,
seamless*); evasive copulas (`serves as` → `is`); negative parallelism (`not just
X, but Y`); rule-of-three padding; elegant variation (the same referent renamed
across sentences); filler (`it is worth noting that`, `in order to`); **sentences
with stacked clauses (flag them, see 2.11)**; **em-dashes: delete all**, using
commas, colons, parentheses, or a sentence split, whichever matches the relation the dash was
carrying; for the exact scope of
the ban see `argument.md` H.1.

### Layer 2: academic AI tells

Each item's **Watch** list and examples are [English manuscripts]; Chinese
manuscripts identify the same patterns in their own language.

- **2.1 Overclaiming verbs.** Empirical work `shows` or `provides evidence`; it
  does not `prove` or `demonstrate` universal truths. **Watch**: demonstrate,
  prove, establish, confirm, guarantee; `significantly` with no test or number.
  **Disciplinary exemption**: in theorem-driven work (mathematics, theoretical
  computer science, cryptography, formal methods), `prove`, `guarantee`, and
  `establish` are accurate when they point at an actual formal proof or formal
  guarantee, are not AI tells, and must not be downgraded. This item targets only
  **empirical results written as universal truths**.
- **2.2 Significance hype.** **Watch**: paves the way for, a crucial/pivotal step
  toward, has the potential to revolutionize, opens new avenues, sheds light on,
  of paramount importance, bridges the gap.
- **2.3 Hollow intensifiers.** **Watch**: extensive/comprehensive/thorough
  experiments, a wide range of, numerous, various. Fix: replace the hollow
  quantifier with what it actually refers to (**illustrative, not universal**: an
  experimental ML paper names its three datasets; other genres substitute their
  own concrete referent: the propositions proved, the sample source, the case
  set).
- **2.4 Novelty padding.** **Watch**: more than one `novel` per section; `to the
  best of our knowledge`; `for the first time`.
- **2.5 Formulaic openers.** **Watch**: `In recent years, X has attracted
  increasing attention`; `With the rapid development of...`; `Despite recent
  advances,...`.
- **2.6 Connective overload.** Do not begin consecutive sentences with Moreover /
  Furthermore / Additionally / In particular; let the logic carry itself.
- **2.7 Contribution-list clichés.** Every contribution names a **concrete
  result**, not a restatement of the abstract. (Consistent with the contribution
  hard rule in `entry.md` §3.8.)
Choose citations that directly and sufficiently support the claim. Do not impose a one-or-two-source cap or keep extra citations solely for appearance; inspect each source’s distinct contribution to support.
- **2.9 Hedging by vagueness.** **Watch**: somewhat, relatively, fairly, to some
  extent, quite. Quantify or delete.
- **2.10 Boilerplate emphasis.** **Watch**: `It is worth noting that`, `It should
  be emphasized that`, `Notably,`, `Importantly,`. If it truly matters, the
  sentence shows it.
Long sentences and deeply nested clauses are candidates for inspection, not automatic failures. Identify the main actor, action, objects and independent propositions. Remove zero-increment repetition before splitting; preserve necessary logical dependencies. Judge the revised sentence in context, not by a universal word or subordinate-clause count.

- **2.12 Empty metaphor.** A metaphor earns its place only when it makes a
  mechanism easier to reason about than the literal statement does. Most
  metaphors in AI-assisted prose do the opposite: they replace a precise
  relation with an evocative one, and the reader has to translate back before
  they can check the claim. **Watch** (beyond the Layer 1 word list and beyond
  2.2, which already bans the significance-hype metaphors outright): journey,
  lens, unlock, cornerstone, `at the heart of`, `a double-edged sword`, `the tip
  of the iceberg`. **Test**: restate the sentence literally, then compare.
  Nothing lost, whatever the length: the metaphor carried no information and
  must go. Literal version longer *and* harder to follow: the metaphor is doing
  work and stays. Literal version longer but just as easy to follow: it goes.
  The burden of proof is on the metaphor, and being no worse than the literal
  statement does not discharge it. **Boundary**: a word that is the literal name
  of its object in this field is not a metaphor here, whatever its origin
  (pipeline, bottleneck, attack surface, threat model, overhead; backbone of a
  network; ecosystem of a package registry). Do not de-metaphor them, and do not
  count them against this rule. The same word used outside that sense (`an
  ecosystem of stakeholders`) is in scope.

- **2.13 Scare quotes.** Quotation marks around a term have three jobs: marking
  a real quotation, mentioning a term rather than using it (its first
  introduction as a name), and holding an established sense at a distance in a
  sentence that then says which sense is meant. Doing none of the three, they
  tell the reader the author will not stand behind the word while using it
  anyway. **Test**: delete the marks. If the sentence says the same thing they
  carried nothing and stay deleted; if it now says something the author does not
  mean, they were standing in for a missing word, so write that word.
  **Boundary**: verbatim quotation, string and identifier literals, and the
  venue's own citation and typographic conventions are not in scope.

- **2.14 Formulaic paragraph closers.** A closing sentence that reassembles what
  the paragraph already said, inside a frame that would fit unchanged under the
  neighbouring paragraphs, adds a sentence and no step. **Watch**: `Taken
  together, ...` is the type case, with `In summary`, `Overall`, and
  `Collectively, these results show` in the same family; what is flagged is the
  frame recurring paragraph after paragraph, not one occurrence of the words.
  **Test**: move the closer under the previous paragraph. If it fits there too,
  it states nothing this paragraph produced. **Boundary**: `argument.md`
  G.4 requires every paragraph to end on an intermediate conclusion the reader
  can restate, and that conclusion is what this item exists to protect. The
  defect is the formula, never the conclusion: a closer carrying something the
  paragraph earned and the next paragraph needs stays, whatever words it opens
  with, and an empty one is rewritten into the conclusion G.4 asks for rather
  than merely deleted.

### Layer 3: do not overcorrect (must be preserved)

- **Evidence-bound hedging is correct and required**: `suggests`, `is consistent
  with`, `we hypothesize that`, `may indicate`, `appears to` must stay wherever
  the claim genuinely is uncertain. **Wrong fix: turning `the results suggest X`
  into `the results prove X`**; that manufactures an overclaim.
- **The passive voice** is right when the agent is irrelevant (`Samples were
  normalized to total protein.`).
- **First-person plural `we`** is standard; do not rewrite to avoid it.
- **Semicolons and the occasional rule of three** are fine in moderation;
  em-dashes are the exception and are all deleted.
Preserve the intended scientific claim and accurate technical distinctions. A wrong or unnecessarily obscure term is not protected merely because it already appears in the manuscript. Correct substantive errors only within authorization and recheck the affected evidence, definitions and dependencies.

### Layer 4: claim-evidence alignment

For every empirical claim check two things: (a) is it backed by a number, figure,
table, or citation in the text; (b) does the verb's strength match the evidence's
strength.

The parenthetical examples below are from experimental ML papers and are
**illustrative, not universal**; English examples are [English manuscripts].
Other genres and languages apply the same test with their own evidence forms (a
theorem and its conditions, a sample size and statistic, a case and its source).

- Unsupported claim → add an evidence pointer or weaken it (`Our method is more
  robust.` → give the 2-point drop under distribution shift vs. the baseline's
  11-point drop, and point at Figure 3).
- Verb stronger than evidence → downgrade (`universally superior` → `On these
  three datasets, ... matches or exceeds the strongest baseline (Table 2)`).
Bind numerical claims to the correct method, metric, population and comparison. Choose a range, mean, uncertainty interval or baseline according to the research question and actual evidence; polishing alone does not authorize changing the statistical object or selecting a favorable comparator.

### Layer 5: matching the author and the venue

When samples of the author's prior papers exist, read them first and record
sentence rhythm, connective habits, the degree and placement of hedging, section
openings, notation and stock phrasing, then match them. Venue register varies
widely (some terse, direct, results-first; others expansive); **which one applies
is checked against relevant actual papers when needed and is not assumed here**. Without samples, default to clean, precise, venue-appropriate prose
rather than the opinionated voice of a generic rewriter.

---

## 2. Polishing after substantive convergence (Source 2, empirical evidence)

**Source caveat**: Source 2 is an empirical study of real submissions, rewritten
along six rhetorical dimensions in both directions and re-scored by five LLM
reviewers under two protocols. It measures **AI reviewers'** sensitivity to
rhetoric-only changes with content held fixed, not human reviewers and not
writing norms. Its use here is to say which dimensions are worth adjusting after
the content is frozen and which are wasted effort.

### 2.1 Useful dimensions and optional background

Evidence visibility, warranted confidence, readability, clear organization and accurate positioning are useful diagnostic dimensions. Apply the ones that improve the actual manuscript, without fabricating evidence, overstating novelty or imposing a fixed rhetorical template.

The original study conditions and numerical scoring notes are retained in [optional background](background/polish-study-notes.md). They are not mandatory priorities or a prediction of acceptance. Actual scientific and reader outcomes govern the revision.

### 2.3 Executable polishing priorities

**Applicability (read this before the order)**: the order comes from Source 2's
measurements, whose scope limits and no-promotion rule are §3 item 8's. These six
rank priorities among implementations the hard rules and Source 1 already allow,
and none of them is a reason to skip a polishing action.

1. **First priority is evidence framing**: make every comparison state which
   method against which baseline, on which dataset, metric, and evaluation
   condition; make figure and table captions and the results prose independently
   readable; put existing empirical patterns, margins, and consistency where they
   are visible. This runs with Layer 4 and hard rule 1.6 (an advantage must be
   stated, not left for the reviewer to discover); all three sources agree.
2. **Second priority is not undercutting the novelty stance**: where the evidence
   already supports a claim, do not phrase it hesitantly or indirectly. This
   permits removing unnecessary softening **only within what the evidence
   supports**; it never permits upgrading to a claim beyond the evidence (Layer
   2.1 and Layer 3 are hard constraints).
3. **Third priority is scope framing that is not over-narrow**: do not bind the
   conclusion tighter than the evidence. Consistent with hard rule A.9: necessary
   boundaries are kept accurately and positively where each claim's reader needs
   them, without repetitive tightening that changes no judgment.
4. **Do not spend effort on lexical complexity or technical register**: Source 2
   measures the effects as small and unstable, while Layer 2.11 and hard rule G.7
   require the opposite direction (lower load, splitting where the cold read finds
   a break). The positive
   rewrites of these two dimensions are **not adopted** in this system.
5. **Do not iterate for score**: Source 2's limited experiment found little gain
   after the second pass and worse average outcomes with review feedback. This
   observation sets no pass limit. Finish the agreed text coverage, check actual
   readability and semantic preservation, and stop when substantive polishing
   duties are met; neither two passes nor a higher score establishes completion.
6. **Touch a high-quality draft less**: high-scoring drafts tend to fall after
   rewriting, so the expected value of a large rewrite is negative. **This drop
   may partly be scale boundary and regression to the mean** (the authors' own
   caveat, §2.2). This item therefore forbids only **whole-draft rewriting done
   to chase a score**; it is not a reason to skip routine polishing. Problems
   identified by the hard rules and Source 1 are fixed regardless of how good the
   draft already is.

### 2.4 Ethical boundary (Source 2's explicit statement, binding)

The authors warn that the framework is dual-use: **a higher score must not be
read as higher scientific value, and these techniques must not be used to
manipulate a live review process**. This section exists only to keep a paper's
real value from being buried by how it is worded, with content and evidence
unchanged. Any "polish" that requires changing a number, a result, a comparison
direction, or an evidence boundary is forbidden (it also violates Layer 3,
Source-2 Prompt G.8, and Source 2's preservation contract).

---

## 3. Boundaries

Current author instructions, academic correctness and the writing-guide govern use of all methods. Source 1 patterns are candidate detectors, not a blacklist. Source 2 scoring observations do not establish that a wording change improves this manuscript or causes acceptance.

Preserve genuine strengths, warranted claims, necessary scope and the author's valid voice. Do not add false balance, generic disclaimers or empty praise. Do not suppress an actual evidence problem to preserve tone. For disagreements, inspect the concrete reader task and evidence through the shared audit workflow rather than a second source-precedence ladder.
## 4. Terminology unification

This section supplies the terminology check for `SKILL.md` "修改落地后" and
"独立阅读、送审与停止". It is the systematic form of the elegant-variation item
in Layer 1.

Determine the intended object and its accurate field meaning from current definitions, source evidence and context. Abstract/introduction wording is a useful candidate, not automatic authority.

Build both object-to-name and name-to-object mappings. Keep genuinely different concepts distinct. For replacements, inspect each occurrence and its sentence role; do not mechanically replace all matches or pick a term by majority frequency.

After changes, check first-use understanding, local scope, long descriptive substitutes, symbol references and actual sentence meaning. Terminology consistency and direct comprehension are separate outcomes within the joint concept task.
