# Abstract and Introduction (Best Paper shared reference)

This is the sole rulebook for the two entry sections of the manuscript:
structure, opening, gap formulation, closing loop, contributions, citation
density, and typesetting.

**Scope (strict)**: abstract- and introduction-specific rules only.
Whole-manuscript rules (launch principle, defensive writing, deletion safety,
page pressure, final checklist) live in `writing-rules.md` and are cited here by
number only, never copied. Also elsewhere: **title rules in `writing-rules.md`
§4.1**; figures and tables in `figures.md`; the AI-tell checklist and
post-freeze polishing in `polish.md`.

Three sources:

- **Source A**: a per-paper empirical analysis of the abstracts of a batch of
  accepted papers in one genre. **This is form induction, not a hard rule**:
  acceptance shows that a form can exist, not that it is optimal, still less
  that it caused acceptance.
- **Source B**: the same analysis for the introductions of that batch; same
  status.
- **Source C**: the abstract- and introduction-specific articles of the numbered
  hard-rule system, owned by this file and cited by its § numbers. The
  whole-manuscript article 1.11 lives in `writing-rules.md` and is only cited
  here. **These articles are hard rules**, judged `PASS`/`FAIL`, and must not be
  softened.

**Authority**: Source C is a hard gate. Sources A and B supply form references
only; they may rank priorities among the compliant implementations Source C
already allows, and must never cancel or relax any article of Source C.
Conflicts among the three sources are listed in §4, which gives a ruling for
each.

> **Out of scope: genre, venue, and corpus statistics.** Rules that hold only for
> one genre (SoK, survey, benchmark study), the target venue's word limits,
> layout, template and house style, and every count drawn from a past-proceedings
> corpus (word-count distributions, item-count distributions, per-form paper
> shares) are deleted here or lifted into genre-independent principles.
> **Those regularities are produced by each project's Setup (style baseline)
> from the target venue's actual past papers**; take them from the Setup's
> output, not from this file.

---

## 1. Shared entry principles

### The two global hard rules that apply (cited only; text in `writing-rules.md`)

- **1.11** governs the launch-talk opening of the abstract and the introduction,
  including what "like a launch talk" does not mean and the test that catches a
  hook only the author can read.
- **0.4** governs the entrance test: what a stranger must be able to answer
  before brevity, rhythm, hooks, or counterintuitiveness are discussed at all.

Read both there before judging an opening. This file only ranks priorities among
the implementations those two allow; it neither restates nor relaxes them.

### The argument spine shared by strong entry sections (Source A)

> Get the reader to grant a real problem; show why existing knowledge cannot
> support some important judgment; state what new analytical capability this
> paper builds; prove that capability with the strongest result; convert that
> result into a new judgment for research, evaluation, or deployment.

Real "elevation" is not making the claim bigger. It answers: **who can now make
what judgment that could not be made reliably before.**

---

## 2. Abstract

### 2.1 The stranger test (Source C, hard rule)

An abstract does not remind readers who have already read the paper; it helps a
reader decide whether to keep reading. The stranger here is **a peer at the
target venue**, not a lay audience: assume domain-general concepts, assume no
knowledge of this paper's problem setting, internal taxonomy, or conclusions.
The abstract must be self-contained enough for a peer from an adjacent subfield
to understand the main findings and judge, on the evidence, why they matter.

- Importance must follow from consequences, results, and impact, and **must not
  be declared with adjectives such as `important`, `novel`, `significant`**
  (word examples [English manuscripts]).
- If the opening uses a term only a reader of the full paper would know (a
  coined compound, an internal category name, a common word given a
  paper-specific meaning), you must either explain it immediately in language a
  peer already understands, or cut it. Concepts that are stable and standard at
  the target venue may be used directly; **familiarity built up over months of
  the authors' own use must not be mistaken for community consensus** (test:
  can the term be found in the field's existing literature with the same sense,
  as opposed to "everyone in our group says it this way").
- Run **G.2**'s per-sentence check over the abstract, where nothing later can
  repair a break: a sentence understandable only after later text needs its
  definition moved forward or the sentence rewritten, and **readers must not be
  expected to re-read**.
- After drafting, have someone unfamiliar with the paper read it once and answer
  five questions: what does the paper study; what is inadequate about current
  evaluation; what did the paper do; what is the core conclusion; why does that
  conclusion matter. If they cannot answer accurately the abstract fails, and
  **"it becomes clear once you read the paper" must not be used as an excuse**.

**Overall test (Source A)**: if the value adjectives are deleted and the reader
can still derive the paper's importance from the consequences, the analytical
capability, and the headline result, the abstract holds.

### 2.2 Structure and language (Source C, hard rule)

There is no single fixed abstract template among accepted papers. Common
orderings, average lengths, and frequent sentence patterns show only that a form
exists. Structure must follow from the central judgment the paper needs to
establish, subject to:

- **Length and format follow the target venue's official requirements**; this
  file sets no cross-venue word law. Absent a venue specification, use a
  single-paragraph short abstract. **That fallback comes from computing and
  engineering practice and does not hold across disciplines**: biomedicine,
  clinical medicine, and some engineering journals default to structured
  abstracts (Background / Methods / Results / Conclusions), and those fields
  follow their own default rather than the single-paragraph form. Actual length
  distributions are measured in Setup, not taken from this file.
- **Zero undefined symbols; preferably zero symbols.** A reader deciding whether
  to continue needs the pain point, the gap, the idea, the conclusion, and the
  value, and no symbols at all. **Exception**: in theory, cryptography, and
  information theory, where a bound or parameter is itself the main result,
  stating it in the abstract is standard and "preferably zero" does not apply;
  "zero undefined" still does: any symbol that appears must be understandable
  to the target reader from within the abstract.
- Treat the abstract as an extremely short paper. **Minimum functional chain**:
  necessary background and problem → gap or difficulty → approach or method →
  main finding and its evidence → the theoretical, evaluative, design, or
  practical judgment that finding changes. This is an argument function, not a
  fixed sentence count.
- **Grant current practice its legitimate use first**, then say what it cannot
  support. State what current practice or existing knowledge measures and why it
  is useful; do not write prior work as obviously wrong. The value comes from
  "the existing evidence cannot support a stronger judgment", not from "this
  area is important".
- **When the core contribution is reorganizing or re-evaluating existing
  evidence rather than adding one isolated result, the abstract must carry one
  extra layer of methodological necessity**: which missing definitions,
  conflicting evidence, heterogeneous results, or inconsistent conventions leave
  researchers or practitioners **currently unable to make** some comparison,
  inference, prediction, or decision; and what this paper's organizing view
  makes comparable, testable, or supportable. State the material analyzed, its
  scale, and the unit of analysis.
- **An artifact type is not automatically a value claim.** A framework,
  taxonomy, ontology, benchmark, database, or tool is only an artifact; say what
  previously heterogeneous evidence it makes comparable, what claim it makes
  testable, or what decision it makes supportable.
- **Main findings must be concrete.** Give the result, relation, or number that
  best supports the claim; never substitute "significant results were obtained",
  "important insights", or "key factors were revealed".
- Title and abstract should naturally contain the terms readers actually search
  for, without turning a keyword list into a noun pile.
- **Setup sentences are normally at most one.** If three or four consecutive
  opening sentences describe facets of the same thing, merge them; keep a second
  only when it introduces a new fact that changes the nature of the problem.
- **The abstract must not open on a stakeholder's situation, investment, or need
  alone.** "Practitioners face...", "vendors are investing..." is grant-proposal
  padding when it merely reports a situation; **it is a valid opening if that
  situation immediately, in the same sentence, forms a well-defined, verifiable
  proposition with security or scientific consequences**. The test is not who
  the subject is, but whether the sentence has already established the problem
  the paper solves.
- The opening should tell a reviewer the object of study, the key question, and
  the stakes as fast as possible. The ending must rest on results the abstract
  has actually delivered, but the last sentence is not mechanically required to
  report evidence.
- **Avoid the author's-compression abstract**: cramming every category, unit,
  comparison, condition, and contribution into one paragraph for coverage. The
  author knows how those words relate and so it reads complete; a stranger sees
  a noun pile. Keep only the decomposition needed to understand the central
  conclusion and leave the rest of the structure to the introduction.
- **"It has a hook" is not an evaluation on its own.** A hook must satisfy three
  conditions at once: it depends on no internal terminology; it names a gap that
  changes a conclusion; the reader sees the stakes immediately. Short sentences,
  parallelism, rhetorical questions, and a "counterintuitive" label satisfy none
  of them.

### 2.3 Effective opening forms (Source A; form reference, not a template)

Usable for selection, not a template. Each draws its force from the first two
moves of the §1 argument spine.

1. **Established success conflicts with a real decision**: a practice is
   successful or widely adopted, but current evaluation cannot answer what the
   decision actually turns on, so the paper re-examines its evidence.
2. **Results are incomparable, so build a common analytical language**: much
   prior work exists, but inconsistent definitions, data, assumptions, metrics,
   or setups make results unfair to compare. The point is not "we built a
   taxonomy" but **what could not be compared before and what unifying it
   revealed**.
3. **The object space grew and prior work covers isolated parts**: the paper
   rebuilds the full picture. The weak version says "first comprehensive
   survey"; the strong version says which shared mechanisms, omissions, or
   failure causes the new framework exposes.
4. **Correcting a field-wide default belief**: the community treats a metric,
   method, or motivation as sound, and systematic analysis shows it does not
   hold or holds only narrowly.
5. **A missing definition has stalled research**: the concept matters and work is
   plentiful, but consistent definitions, metrics, or comparison frameworks are
   absent. The value is **a judgment capability that was previously missing**,
   not "a more complete tidy-up".

### 2.4 Four forms of value evidence (Source A, form induction)

1. **Establish the problem's real scale**: adoption rate, defect share, number
   of studies, number of instances, coverage. The number's job is to answer "is
   this a real problem worth studying systematically", not to look rigorous.
2. **Write the gap as a task that cannot be completed** (consistent with the
   Source C hard rule in §3.4).
3. **Express the contribution as a capability**, not "we propose a framework"
   (the Source C hard rule in §2.2 names the three capabilities to state).
4. **Use a headline result to show this is more than a tidy-up.** Restatable
   headline results look like:
   - No single factor independently explains the observed differences.
   - The existing simple method outperforms newer ones under realistic settings.
   - N% of real cases violate at least one of the criteria this paper gives.

   **Counter-form**: "important insights", "key factors", "guides future work"; the
   reader cannot restate the finding. Such abstracts get accepted; they are
   not the target.

### 2.5 Closing the result-to-meaning loop (Source C hard rule; also Source A)

The final "elevation" is not raising the conclusion to a higher abstraction
level, and not replacing evidence with "advances the field", "lays a
foundation", or "is of great significance". The ending converts evidence into
judgment:

> concrete finding → the judgment revised or added → the researchers, designers,
> reviewers, or deployers who thereby gain a capability

The safest implementation closes the loop across the last two functions: the
penultimate sentence delivers the strongest result, the last states the
theoretical, evaluative, design, or practical judgment it changes. They may be
two sentences or fused into one when space is tight, **but a value slogan alone
must not be what remains**.

Three endings are acceptable:

1. End on the strongest finding, when that finding already changes the prior
   judgment plainly.
2. End on a recommendation, research agenda, or practical implication, **with
   the preceding sentence supplying the concrete result that supports it**.
3. End on a framework, tool, database, or other durable artifact, **stating what
   previously unreliable task it now supports**.

**Failure test**: if deleting `important`, `actionable`, `valuable`,
`foundation` (word examples [English manuscripts]) or "guides future research"
from the last sentence leaves no concrete change; or if the ending introduces a
new problem, stakeholder, limitation, or stronger claim the paper has not
established. Strong endings name a subject and an action (informs a class of
design, improves an evaluation method, supports a stricter decision); weak ones
say "lays the foundation for future research".

### 2.6 Citations in the abstract (boundary)

The introduction requires a direct source for every externally verifiable fact;
**that density does not apply to the abstract**. Whether the abstract carries
citations follows the target venue's past practice, confirmed in Setup. Either
way, every external claim in the abstract must be directly supported in the body.

### 2.7 RECOMMENDED style preferences (non-binding)

1. Prefer opening on one accurate, restatable central judgment that brings the
   object of study and the key relation on stage together, rather than laying
   out domain common knowledge first.
2. Prefer positive claims. If deleting `not`, `rather than` (word examples
   [English manuscripts]), concessive clauses, and disclaimers does not change
   the truth value, state directly what the paper establishes.

---

## 3. Introduction

### 3.1 The three duties of an introduction (Source C, hard rule)

An introduction is not a longer abstract and not a warehouse for literature and
technical detail. It must, in order:

1. **Give the necessary background and establish importance.** Balance broad
   context against technical detail; keep only the context needed to understand
   the research problem and the stakes.
2. **Establish an explicit motivation.** State precisely what existing methods,
   data, or evidence lack and why that gap blocks the goal. **The motivation
   must pave the way directly to the research objective; "there is still room
   for improvement" must not stand in for it.**
3. **Announce how this paper occupies the gap.** A concise closing paragraph
   gives the objective, the main method, the key findings, and the impact.

**Final check is a four-way alignment**: the importance established by the
background, the gap named by the motivation, the method actually used, and the
results reported in the abstract and body must all point at the same problem.

### 3.2 The introduction must open on an evidence chain (Source C, hard rule)

Enter from domain facts the target reader already knows and the literature can
support, not from this paper's own terminology, taxonomy, notation, formal
counterexamples, or comparison worlds. A reliable general order:

> domain consensus and real-world context → current practice or evaluation →
> the conflict existing evidence exposes → the real cost of the wrong judgment →
> the key task existing research cannot complete → this paper's approach → core
> result → contributions

This fixes **information dependency**, not a paragraph count: each item must
rest on one a stranger can already understand. Four checks on the opening:

1. **Say why current practice is reasonable first.** Do not write prior work as
   obviously wrong; state accurately what problem it solved and what it measured.
2. **Then give a conflict strong enough to change the judgment.** After the
   turn, evidence or logic must show the prior results cannot support the
   stronger conclusion a reader would naturally draw.
3. **Severity comes from consequences.** Say what wrong comparison, wrong
   deployment, wrong guarantee, or misallocated resource a wrong inference
   causes; **do not substitute `important`, `critical`, `significant` for the
   argument** (word examples [English manuscripts]).
4. **The paper enters last.** Introduce the framework, taxonomy, method, or
   theoretical tool only after the problem, the consequences, and the gap stand.

**Opening forms (Source B, form reference)**: the most robust entry is a domain
fact or accepted background (this object is infrastructure or a core component;
this practice is already successful; this class of risk is widespread; this
class of system is deployed at scale). **A specific incident, market figure, or
individual case is usually wrong as the first sentence**; it belongs in the
second half of the opening paragraph or the second paragraph, where it cashes
abstract importance into evidence. Special entries (a direct question, an
imagined scenario, a professional role's viewpoint, a short reversal judgment)
show only that such writing is possible, not that it beats a direct factual
entry; when the reader first needs to understand what current practice measures,
**an abstract counterexample or rhetorical question is the wrong opening**.
Actual proportions at the target venue are measured in Setup.

### 3.3 Seven argument types for introduction value (Source B, form induction)

Value rarely rests on "this is the first taxonomy of X" alone; strong papers
usually combine several of:

| Type | Core logic | Typical effect |
|---|---|---|
| Contradiction | Two established facts cannot both be explained by current understanding | Widely adopted, yet the key question is barely studied |
| Incomparability | Datasets, metrics, definitions, assumptions, or setups differ | Nobody can fairly judge which method is better |
| Illusion | Results hold under simplified conditions and fail under real ones | Reported high performance may be an artifact of the environment |
| Intractability | Object count, system heterogeneity, or design space is too large | Exhaustive experiments are infeasible; a model or common framework is required |
| Misalignment | The community optimizes the wrong target, or one already solved elsewhere | The contribution becomes a reordering of the research agenda |
| Scale | Study counts, adoption rates, defect or omission shares quantify the problem | The gap turns from an opinion into a citable result |
| Consequence | The gap causes wrong choices, wrong decisions, or false assurance | Explains why the problem is worth solving |

The strongest value chain is not "the field is important, therefore a survey is
needed" but: **current evaluation looks sound but supports wrong judgments under
some real conditions; existing research lacks a unified way to detect that; this
paper supplies it and shows which conclusions it changes.**

### 3.4 Write the gap as a task that cannot be completed (Source C, hard rule)

`existing work is fragmented`, `a unified understanding is lacking`, `there
remains room for improvement` (sentence examples [English manuscripts]) describe
a state and prove no necessity. An effective gap must answer: because which
definitions, evidence, setups, or comparison conventions are unaligned,
researchers or practitioners **currently cannot make** what judgment or take what
action. Common valid forms:

1. Cannot compare existing methods fairly.
2. Cannot tell whether experimental results transfer to real deployment.
3. Cannot separate real improvement from artifacts of data, environment, or
   evaluation setup.
4. Cannot infer the whole-system conclusion the paper or practice needs from
   local measurements.
5. Cannot predict new objects or scenarios without experimenting on each.
6. Cannot identify the common root cause of a class of failures.
7. Cannot reproduce experiments or determine the boundary of a conclusion.

The gap must then explain **why adding one more isolated experiment would not
resolve it**. If the root cause is inconsistent definitions, metrics,
assumptions, baselines, time ranges, or evidence objects, a common analytical
framework or systematic re-analysis is required. Four general arguments:

1. **Existing results are incomparable**: separate definitions, private data, and
   different metrics mean a new experiment adds one more coordinate rather than
   unifying the old ones.
2. **Exhaustive validation is infeasible**: too many combinations of objects,
   components, and paths; only abstraction from existing evidence scales.
3. **The literature's own volume is the obstacle**: hundreds of papers all claim
   improvement and practitioners cannot adjudicate them one by one.
4. **What is missing is a common language**: many local results exist, but
   definitions, assumptions, time ranges, and claim strengths share no
   coordinate system.

**Reverse gate**: if the root cause is simply a missing experiment, do not
package an ordinary experimental question as a structural gap.

### 3.5 Evidence and citations in the introduction (Source C, hard rule)

The goal is not that every sentence formally carries a reference, but that every
externally verifiable factual claim has **direct, sufficient, and precisely
placed** support.

Must cite: the state of the field, adoption trends, and community practice; real
incidents and their consequences; numbers, proportions, performance results, and
temporal trends; what prior work typically measures, covers, or ignores;
literature-scope judgments such as "existing results are incomparable" or "no
unified method exists".

Normally need no external citation: the research question, the authors'
definitions, this paper's method, this paper's results, and pure transitions.

**Citations must sit adjacent to the claim they support**; when one sentence
carries several independent facts, split it or attribute each separately. Do not
pile a block of references at the end of a long paragraph and leave the reader
guessing which supports what; do not use a local experiment to support a
stronger or broader conclusion.

### 3.6 Concept order and paragraph load (Source C, hard rule)

One paragraph advances one main level of abstraction and ends on a restatable
intermediate conclusion. **A single paragraph must not simultaneously define the
object of study, the system boundary, the taxonomy, the comparison baseline, the
time range, the stakeholders, and the formal conclusion.**

Write concrete objects, current practice, observable results, and real
consequences first, then abstract the common problem from those facts. **Do not
present a taxonomy or a counterexample first and ask the reader to guess what it
solves.**

A case or counterexample in the opening requires four conditions: the
proposition under test is already explicit; the key objects are already defined;
the causal or comparative relation can be recovered independently; the reader
can see which conclusion the example changes. If any fails, move the case later,
to intuition, framework exposition, or the body analysis.

### 3.7 Ideal target draft, core result, and evidence status (Source C, hard rule)

Research not being finished does not license an introduction without a core
result. Write early a complete, coherent, near-submission **ideal target
introduction** that names the material analyzed, its scale, the method, the
strongest headline result, three result-type contributions, and their field
impact. Write it for the most ideal yet still plausibly reachable end state;
**placeholders in brackets, blank paragraphs, and "results TBD" must not be used
to dodge the central narrative responsibility.**

The ideal target draft is first of all a **test of research value**: if, under
the best reasonable results, the paper still cannot establish an important
problem, change a substantive judgment, or produce a memorable contribution, the
research question, method, or contribution positioning must be restructured
immediately rather than executed mechanically.

The ideal target draft is a planning artifact, not a draft of the submission. It
lives in `AUDIT-LOG.md`, and the ban on placeholders applies to it alone: it has
to commit to a headline result precisely so that the commitment can be judged
before the work is done. Nothing licenses carrying an unearned result across
into the manuscript.

Complete narrative and evidence integrity are managed separately: the body stays
readable end to end, but **results not yet obtained must never be written as
obtained**. Update the introduction, abstract, and contributions with every new
round of real results instead of writing them once at the end; claims the
evidence does not support must be deleted and the surrounding narrative rebuilt;
claims whose direction or strength conflicts with the evidence must be rewritten
to the evidence. **In the final submitted version, every result verb, number,
and conclusion must correspond to evidence actually obtained.**

When introducing the work, state what material was analyzed, at what scale, by
what method, and how those choices address the gap just established. **The
headline result (the single most memorable result in the paper) must be
delivered before the contribution list**; the list must never be the first place
the paper's finding is explained.

### 3.8 Contributions at the end of the introduction (Source C, hard rule)

- **Author-wide hard rule: there must be exactly three contributions, each with
  a bold subheading, each of 30–50 words.** (Word counts [English
  manuscripts]; Chinese manuscripts convert to characters.)
- Each must state **the concrete artifact, the method or material, the key
  finding, and the judgment it changes**; empty verbs such as "we characterize"
  or "we analyze" are not enough. The full form is: what is delivered, how it
  was built or validated, what was found, and what the reader can now judge.
- **The prose paragraph and the list must not say the same thing twice.** The
  list carries the contribution statements; the prose only transitions.
- **A contribution must not stop at an artifact or a research action.** "We
  collect and classify prior work" or "we build a framework" does not qualify;
  say what the artifact or viewpoint makes comparable that was not, what
  inference it makes testable, or which new empirical results, theoretical
  results, and research directions it produces.

**A common division of the three (Source B, form reference)**: (1) a shared
structure or analytical view (definitions, taxonomy, framework, design
dimensions, evaluation model); (2) systematized material and empirical results
(corpus, benchmark, unified re-evaluation, case analysis, statistics); (3)
conclusions and actionability (recommendations, roadmap, research directions,
selection guidance). This division is a form reference and may be reordered to
fit the actual contributions; **the three-item count, the bold subheadings, and
the 30–50 words per item are an author-wide hard rule and do not depend on
whether the venue requires them.**

**Subheading wording**: most common is a searchable noun phrase; article plus
deliverable also occurs, and **conclusion-sentence subheadings are rarer but do
exist** (§4 item 6). The actual distribution at the target venue is measured in
Setup.

**Shortest fix for an overlong contribution item**: do not restructure the three
roles; keep the three-layer structure and compress the item to **one artifact,
one core result, one changed judgment**. The heaviest item is usually the one
carrying an overall verdict plus several cross-mechanism relations plus the
consequences of the taxonomy; compress that one first.

### 3.9 Typesetting the introduction (Source B, generalized)

**Applicability**: this section generalizes from papers that use the
"bold-subheading bullet contribution list at the end of the introduction"
convention, mainly in computing and engineering. Disciplines that do not use
that structure (mathematics, physics, medicine, humanities) follow their own
convention and this section does not apply.

Implementations frequent and effective in the Source B corpus: inline bold
paragraph leads via `\paragraph{}` or `\noindent\textbf{}`; `itemize` /
`enumerate`; `\textbf{}` contribution subheadings; `\emph{}` for key terms;
`\footnote{}` on the first page (terminology notes, equal-contribution notes);
and cross-references written as `Section~\ref{...}` with a non-breaking space so
the section word and number do not split across lines. The corpus contains only
published PDFs and no typesetting source (§4 item 10), so this is neither
exhaustive nor a prohibition on other implementations.

---

## 4. Three-source conflicts and boundaries

Each conflict below carries a ruling; **execution follows the ruling**. For a new
conflict the rulings do not cover, decide in two layers: first authority (Source
C hard rules outrank the form inductions of Sources A and B); at equal authority,
or if still undecided, escalate through the hard-rule arbitration order of
`writing-rules.md` G.8. Either way, record which source the decision rests on in the audit log.

**General ruling (read this before the individual items)**: **the existence of a
past-practice precedent grants no exemption from a hard rule**, and no past
practice may be promoted into one either. The Authority statement above and item
10 own both directions; the paper counts, proportions, and distributions any such
argument rests on are measured in Setup, per the scope note above.

1. **Abstract word budget.** Source C once gave a short working range while
   admitting it was not a cross-venue law; Source A shows the real distribution
   is far wider. **Ruling: no fixed range.** Word count follows the venue's
   official requirement; the distribution is measured in Setup.

2. **Ban on opening with a stakeholder's situation.** Apparent conflict only:
   Source A wants the ban made conditional, and the current Source C wording
   (§2.2) already is. The test is whether the problem has been established, not
   who the subject is.

3. **Must the ending rest on evidence?** Apparent conflict only: Source A's
   objection targets an earlier, stricter version. The current §2.5 wording,
   with its three valid endings, already matches the corpus.

4. **Must the headline result precede the contribution list?** Source C (§3.7)
   says yes, as a hard rule. Source B finds at least three orderings in past
   proceedings and notes this rule is **a deliberate stronger narrative design,
   not a summary of past practice**. The design reason is to keep the
   contribution list summarizing rather than first explaining the finding. The
   hard rule does not relax in the face of precedent.

5. **Contribution count and words per item.** Source B shows the count
   distribution in past proceedings is wider and that three is not any venue's
   format requirement. That only shows the rule is not externally imposed; it
   does not affect the author's decision to make it a hard rule for all projects
   (§3.8).

6. **Are noun-phrase subheadings the only option?** The claim "not one paper uses
   a conclusion-sentence subheading" was refuted by a Source B counterexample.
   Noun phrases are merely the most common form, not a hard rule. **This is also
   a methodological warning: before writing any "not one / all of them"
   exhaustive claim, you must be able to name the counting basis.**

7. **Citation density in abstract vs. introduction.** Source C (§3.5) requires a
   direct citation for every external fact in the introduction; Source A finds
   much lower density in abstracts. Apparent conflict only: it is a division of
   labor, and §2.6 states the abstract side of it in full.

8. **Priority claims.** Source B finds `first comprehensive` and `to the best of
   our knowledge` common in past proceedings; Source C and the novelty-padding
   item of the AI-tell checklist require priority claims to align strictly with
   the evidence and mark `to the best of our knowledge` and `for the first time`
   (word examples [English manuscripts]) for deletion. Per the general ruling,
   precedent grants no exemption.

9. **Defensive text and dashes.** Source B finds dedicated disclaimer boxes and
   frequent long dashes in past proceedings. Hard rule **A.4** and the global
   em-dash ban both apply; precedent grants no exemption. The
   exact scope of the em-dash ban is defined in `writing-rules.md` H.1 and is not
   restated here.

10. **External-validity limits of Sources A and B.** Both corpora come from one
    genre at a single conference across two recent editions, and contain only
    published PDFs and extracted text, no typesetting source (typesetting can be
    confirmed by appearance only, not by package). No item from Source A or B may
    therefore be promoted to a `PASS`/`FAIL` gate; they may only rank priorities
    among implementations Source C already allows. **Genre- and venue-level
    regularities must be regenerated in each project's Setup from that venue's
    actual past papers, and the form inductions in this file must not be carried
    over as facts.**
