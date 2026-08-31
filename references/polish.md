# Polishing Rules (Best Paper shared reference)

This is the shared **style rulebook**, covering three things: stripping AI tells
out of academic prose, the last rhetorical pass after the content is frozen, and
terminology unification. The numbered hard-rule system (general principles,
non-negotiable audit clauses, launch principle, defensive writing, deletion
safety, figures, citations) lives in `writing-rules.md`; this file cites it by
number and never copies its articles.

Two sources:

- **Source 1**: the `academic-humanizer` skill for de-AI academic editing (AI-tell
  patterns and their fixes). **It is a separate skill that must be installed
  separately and does not ship with Best Paper**; when it is absent, §1 still
  works standalone, since §1 is its distillation: it covers the pattern list and
  the main fixes, but not every fix or every genre branch.
- **Source 2**: *How Can Rhetoric Reward-Hack AI Reviewers? Dissecting
  Rhetorical Sensitivity in AI-Based Peer Review* (Li, Wang et al.,
  arXiv:2608.08975). Not a style manual but an empirical study of which
  rhetorical dimensions move AI reviewer scores; its executable part is
  distilled here as post-freeze polishing heuristics.

**Authority**: Source 1 is a pattern-recognition checklist whose enforcement is
bounded by the numbered hard rules; Source 2 is empirical evidence and **may only
rank priorities among implementations that both the hard rules and Source 1
already allow**. It must never be used to relax a hard rule. Conflicts and their
rulings: §3.

**Genre- and venue-specific content stays out of this file**: rules that hold
only for one genre (SoK, theory paper, grant proposal) and the target venue's
word limits, layout, template, and house style are produced in Setup, when the
style baseline is built from that venue's actual past papers.

---

## 0. Execution premise

Everything in this file is bounded by hard rules **G.8 / A.14** (conflicts
escalate upward only: truth and reproducibility → a stranger understands in one
pass → a complete and forceful argument chain → and only last, concision,
rhythm, style, and length). Style, rhythm, and rhetorical scoring sit at that
last level and must never override the first three.

---

## 1. De-AI pattern checklist (Source 1)

Source 1's core premise: academic writing already has a correct human voice:
neutral, precise, first-person plural `we`, every claim bound to evidence. The
task is to strip the AI tells without making the text colloquial, and to enforce
that **every claim earns its own number, figure, or citation, and no verb is
stronger than its evidence**. **Never alter any number, formula, or citation.**

Workflow: read (including the author's own writing samples, to tell a paper from
a grant proposal) → review without editing (list every pattern's location and
proposed fix, plus the evidence status of each empirical claim) → rewrite
(structure and content unchanged, all claims and citations preserved) → report a
change log.

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
the ban see `writing-rules.md` H.1.

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
  hard rule in `abstract-intro.md` §3.8.)
- **2.8 Citation dumping.** Cite the one or two that actually matter and say why;
  do not hand over a bracketed list. (Consistent with `writing-rules.md`
  chapter 8.)
- **2.9 Hedging by vagueness.** **Watch**: somewhat, relatively, fairly, to some
  extent, quite. Quantify or delete.
- **2.10 Boilerplate emphasis.** **Watch**: `It is worth noting that`, `It should
  be emphasized that`, `Notably,`, `Importantly,`. If it truly matters, the
  sentence shows it.
- **2.11 Long, clause-stacked sentences. Author-wide hard rule:** a sentence
  longer than about 30 words, or containing more than three subordinate clauses
  is **flagged for the forward cold read G.7 defines**, and the length settles
  nothing on its own: G.7 names a shorter sentence as one of the proxies that
  never shows the text can be understood in one pass. Split it only where that
  read records a break inside it, and split at the break: one idea per sentence,
  with non-load-bearing clauses deleted, but never into telegraphic fragments. A
  flagged sentence the reader restates in one pass stays as it stands, since
  splitting it anyway degrades term binding and manufactures verbatim repetition
  across chapters (`audit-method.md` §3). **The word threshold is [English
  manuscripts]**: Chinese has no matching word count, so Chinese manuscripts
  convert it to clause count and comprehension load. The verdict belongs to
  G.2 / G.7 (see §3 item 1).

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
  it states nothing this paragraph produced. **Boundary**: `writing-rules.md`
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
- **Formal definitions, named methods and metrics, technical terms, formulas and
  notation** are preserved verbatim.
- **Never invent, delete, or alter any number, formula, or citation**; all cite
  keys are preserved.

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
- Vague magnitude → give a number or a **range** with attribution. **Prefer a
  range** (e.g. `2--6%`) over a single mean unless the averaging is stated; bind
  every number to its method, metric, and baseline; **compare against the
  strongest competitor first**, not the trivial baseline.

### Layer 5: matching the author and the venue

When samples of the author's prior papers exist, read them first and record
sentence rhythm, connective habits, the degree and placement of hedging, section
openings, notation and stock phrasing, then match them. Venue register varies
widely (some terse, direct, results-first; others expansive); **which one applies
is determined in Setup from that venue's actual past papers and is not assumed
here**. Without samples, default to clean, precise, venue-appropriate prose
rather than the opinionated voice of a generic rewriter.

---

## 2. Post-freeze polishing (Source 2, empirical evidence)

**Source caveat**: Source 2 is an empirical study of real submissions, rewritten
along six rhetorical dimensions in both directions and re-scored by five LLM
reviewers under two protocols. It measures **AI reviewers'** sensitivity to
rhetoric-only changes with content held fixed, not human reviewers and not
writing norms. Its use here is to say which dimensions are worth adjusting after
the content is frozen and which are wasted effort.

### 2.1 The six dimensions and their positive definitions

> **Numbering namespace**: two `G.x` schemes appear in this file. Unprefixed
> `G.x` (G.2, G.7, G.8) always means the general principles in
> `writing-rules.md`; the rewriting prompts in Source 2's appendix are always
> written **`Source-2 Prompt G.x`**. They are unrelated and must not be conflated.

| Dimension | Positive rewrite | Negative rewrite |
|---|---|---|
| Novelty stance | Where the evidence already supports it, state claims, novelty, positioning, and contributions more confidently and decisively | More cautious, more qualifiers, softened verbs |
| Scope framing | Within the boundary the evidence allows, widen the wording of datasets, tasks, domains, model classes, assumptions, and application settings | Bind more tightly to the specific evidence and setup |
| Evidence framing | Present existing comparisons, metrics, and quantitative findings more clearly, visibly, and favorably; state which method against which baseline, on which dataset and metric | Downplay empirical advantage, add context, explain more conservatively |
| Contribution salience | Contributions explicitly labeled, front-loaded, skimmable, reviewer-facing | Contributions folded into ordinary narrative, less labeling |
| Technical register | Describe mechanisms, procedures, assumptions, and protocols in a more formal, precise, technical register | Plainer and more direct |
| Lexical complexity | More advanced academic vocabulary and denser syntax | Shorter, plainer sentences and more common words |

Shared floor for every positive rewrite (Source-2 Prompt G.7 / G.8): **no new
experiments, data, baselines, numbers, or unsupported conclusions; no change to
any reported value, comparison direction, ranking, qualifying condition, or
evidence boundary; no turning limited, conditional, mixed, or setting-specific
evidence into universal certainty; no removal of qualifiers that define a claim
substantively; no adding a mechanism, assumption, or derivation that was not
there in order to sound more technical.**

### 2.2 Measured effects (basis for the priority order)

- **Sensitivity concentrates in three dimensions**: evidence framing is
  strongest, novelty stance next, scope framing a weaker second tier; technical
  register, contribution salience, and lexical complexity are small or unstable.
- Magnitudes: positive evidence framing raises Overall Assessment by up to
  **0.93**; negative novelty stance lowers it by up to **0.73**. Swing in
  weak-accept probability (OA ≥ 6), positive vs. negative: evidence **13.0**
  points, novelty **12.0**, scope **9.0**.
- **Novelty and scope effects are penalty-driven** (writing too narrowly or too
  cautiously loses points; writing wider does not gain symmetrically), while
  **evidence framing is bidirectional** (clarity gains, murkiness loses).
- OA movement tracks contribution and soundness, and barely tracks presentation:
  the AI reviewer reads rhetorical confidence and evidence emphasis as a signal
  of scientific value.
- **The pattern holds across human-quality strata**: strong papers are no more
  resistant to rewriting, weak papers no more sensitive.
- **The starting score strongly determines the direction of movement**: low
  initial AI scores move up, high ones move down. The authors note this may
  partly reflect scale boundaries and regression to the mean.
- **More elaborate rewriting pipelines are unreliable**: gains from joint
  six-dimension rewriting depend heavily on the rewriting model; feeding reviewer
  feedback back in and rewriting again averages **worse** than a second pass
  without feedback; recursive rewriting gains concentrate in round two, with
  almost no round-three increment.
- **The strict protocol only lowers scores across the board and does not make
  reviewers more immune to rhetoric** (rewrite effects correlate barely at all
  across protocols).

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
   boundaries are kept and stated once, accurately and positively, not re-tightened
   chapter by chapter.
4. **Do not spend effort on lexical complexity or technical register**: Source 2
   measures the effects as small and unstable, while Layer 2.11 and hard rule G.7
   require the opposite direction (lower load, splitting where the cold read finds
   a break). The positive
   rewrites of these two dimensions are **not adopted** in this system.
5. **Do not iterate for score**: there is no reliable gain past the second pass,
   and feeding reviews back in averages worse. Polishing converges within two
   passes.
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

## 3. Conflicts and boundaries

Each conflict carries a ruling; **execution follows the ruling**. For a new
conflict not covered here, first apply authority (hard rules > Source 1 > Source
2); at equal authority, or if still undecided, escalate in the §0 order. Either
way, record which source the decision rests on in the audit log.

1. **Sentence length and complexity**
   - Author-wide hard rule **2.11**: over-long, clause-stacked sentences are
     **flagged for the forward cold read**, and split where it finds a break.
   - Hard rules **G.2** and **G.7**: comprehension breaks caused by long
     sentences must be fixed, and that cold read is what establishes one. **Chapter 6** simultaneously forbids compressing
     space with disfluent enumerated fragments, so splitting must not produce
     telegraphese.
   - Source-2 Prompt G.6 positive pushes the opposite way (denser syntax, more
     nesting, more nominalization).
   - Ruling: §2.3 item 4 declines that direction; Source 2 itself measures the
     dimension as small and unstable.

2. **Confidence and assertion strength**
   - Source 1 Layers 2.1 / 2.4 mark `prove`, `demonstrate`, `establish`, `novel`,
     `for the first time` as overclaiming and novelty padding; Layer 3
     simultaneously requires evidence-bound hedging to stay.
   - Hard rules **1.3**, **1.5**, and **A.4**.
   - Source 2: positive novelty stance is the second-highest-yield dimension for
     AI reviewers.
   - Ruling: the intersection is "delete softening that has no evidential basis,
     but do not upgrade verb strength". The friction is that Source 1 actively
     downgrades strong verbs while Source 2 shows downgrading costs points; this
     system follows the hard rules and Source 1.

3. **Keeping or cutting hedges**
   - Source 1 Layer 3: `suggests`, `may indicate`, `appears to` must stay where
     the claim is genuinely uncertain, and rewriting them to `prove` is a wrong
     fix.
   - Hard rules **2.2**, **A.9**, and **2.4**.
   - Ruling: no direct contradiction, but the boundary slips in practice. Take the
     intersection: **if deleting the hedge would make the proposition false or
     change what the evidence means, keep it and keep it in one place only;
     otherwise delete it.**

4. **Repeating the contributions**
   - Hard rule `abstract-intro.md` §3.8 (no duplication between the contribution
     list and the adjacent prose) vs. Source-2 Prompt G.4 positive, which allows
     repeating contribution framing to help readers track the paper's value.
   - Ruling: hard gate wins over empirical heuristic.

5. **Contribution count and the "rule of three"**
   - Source 1 Layer 1 flags rule-of-three padding as an AI tell.
   - Author-wide hard rule `abstract-intro.md` §3.8 fixes the three-item
     contribution format.
   - Ruling: Source 1 targets contentless triads, while §3.8 requires each item to
     carry a concrete artifact and a changed judgment. Both hold at once, and an
     audit **must not** invoke Source 1 against the three-item format.

6. **Em-dashes**
   - Source 1 Layer 1 and the author-wide global ban agree. No conflict.
   - Scope of the ban: `writing-rules.md` H.1; the replacements for a deleted
     dash are Layer 1's. Neither is restated here.

7. **Where the style baseline comes from**
   - Source 1 Layer 5 uses the author's prior papers and the venue register as the
     baseline.
   - Hard rule **A.11**: an audit must not add evaluation criteria.
   - Ruling: venue matching is a choice among compliant implementations and cannot
     create a new hard gate; cite the venue requirement with its source.

8. **Scope limits of Source 2**
   - Its conclusions cover only one conference year, submissions with retrievable
     full source, five reviewer models, and two prompts; the authors state the six
     dimensions are not orthogonal, most configurations were scored once per
     paper, and the results do not extrapolate to human reviewers or other fields.
   - No item from Source 2 may be promoted to a `PASS`/`FAIL` gate; it may only
     rank priorities among implementations the hard rules and Source 1 already
     allow.

---

## 4. Terminology unification

This section is the sole body of the terminology-unification rule; delivery's
polish step in `SKILL.md` cites it. It is the systematic form of the
elegant-variation item in Layer 1.

**Canonical name**: for each concept that surfaces under more than one wording,
the canonical name is fixed by **the anchor already used in the abstract and the
introduction, combined with the field's mainstream term**. Frequency counts in
the body carry no authority: a variant used more often in later chapters does not
override the entry-section anchor.

Procedure:

1. Build a mapping table: concept → canonical name → every variant found in the
   manuscript.
2. **Before unifying a variant, grep the manuscript for it to check whether it is
   already a formal, defined term of this paper.** If it is, unifying would
   collapse two distinct concepts onto one name; keep them apart, or rename the
   canonical form, and record the case in the mapping table.
3. Apply the mapping mechanically across the whole manuscript, including figure
   and table captions, footnotes, and appendices.
4. The Layer 3 protected list applies unchanged: formal definitions, named
   methods and metrics, notation, numbers, formulas, and cite keys are never
   touched by a terminology pass.
