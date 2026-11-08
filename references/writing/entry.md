# Title, abstract and introduction methods

Normative requirements are maintained in [writing-guide.md](../writing-guide.md); task selection and verification are maintained in [audit/routing.md](../audit/routing.md). This file supplies entry-specific methods for scope, structure, openings, gaps, closing judgments, contributions and evidence.

Whole-paper argument and deletion methods are in `argument.md`; visual methods are in `figures.md`; sentence and terminology methods are in `polish.md`. Load the relevant part rather than treating the attachments as competing rulebooks.

Source A and B refer to earlier analyses of abstract and introduction forms in a selected accepted-paper corpus. They are form observations, not universal requirements or evidence that a style caused acceptance. Source C labels earlier author guidance; it is provenance, not a second authority hierarchy.

Establish venue-specific regularities from actual comparable papers, keep the sampling frame, and follow verified current requirements. Reuse valid project evidence rather than creating a mandatory setup report.
## 1. Shared entry principles

### Two complementary entrance diagnostics (methods in `argument.md`)

- **1.11** examines the launch-talk opening of the abstract and the introduction,
  including what "like a launch talk" does not mean and the test that catches a
  hook only the author can read.
- **0.4** examines the entrance test: what a stranger must be able to answer
  before brevity, rhythm, hooks, or counterintuitiveness are discussed at all.

Use these methods to test whether the actual opening helps its reader. Active requirements remain in writing-guide; these methods do not create an additional authority hierarchy.

### The argument spine shared by strong entry sections (Source A)

> Get the reader to grant a real problem; show why existing knowledge cannot
> support some important judgment; state what new analytical capability this
> paper builds; prove that capability with the strongest result; convert that
> result into a new judgment for research, evaluation, or deployment.

Real "elevation" is not making the claim bigger. It answers: **who can now make
what judgment that could not be made reliably before.**

---

## 2. Abstract

### 2.1 The stranger test (method derived from prior guidance)

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

### 2.2 Structure and language (method derived from prior guidance)

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
  distributions come from relevant project corpus analysis, not from this file.
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
Use only setup that the reader needs to understand the problem and result. Remove repeated preparation; do not impose a universal one-sentence quota.
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
   prior-guidance method in §3.4).
3. **Express the contribution as a capability**, not "we propose a framework"
   (the prior-guidance method in §2.2 names the three capabilities to state).
4. **Use a headline result to show this is more than a tidy-up.** Restatable
   headline results look like:
   - No single factor independently explains the observed differences.
   - The existing simple method outperforms newer ones under realistic settings.
   - N% of real cases violate at least one of the criteria this paper gives.

   **Counter-form**: "important insights", "key factors", "guides future work"; the
   reader cannot restate the finding. Such abstracts get accepted; they are
   not the target.

### 2.5 Closing the result-to-meaning loop (method and source context)

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
citations follows verified target-venue requirements and relevant past practice. Either
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

### 3.1 The three duties of an introduction (method derived from prior guidance)

An introduction has three connected duties: establish the research problem and why it matters; explain what the work contributes and what evidence supports it; prepare the reader for the argument that follows. Order these duties according to information dependencies and the reader's current knowledge, not a compulsory paragraph template.

Show the result and its significance clearly. Put detailed mechanisms and proofs where they can be understood without overloading the entry. A closing paragraph is useful when it adds a needed judgment or orientation, not because every introduction must have the same ending.

**Final check is a four-way alignment**: the importance established by the
background, the gap named by the motivation, the method actually used, and the
results reported in the abstract and body must all point at the same problem.

### 3.2 The introduction must open on an evidence chain (method derived from prior guidance)

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
Measure proportions in a relevant target-venue sample when the decision needs them.

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

### 3.4 Write the gap as a task that cannot be completed (method derived from prior guidance)

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

For a claimed structural gap or a claim that systematization is necessary, apply the following test:
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

### 3.5 Evidence and citations in the introduction (method derived from prior guidance)

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

### 3.6 Concept order and paragraph load (method derived from prior guidance)

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

### 3.7 Core result and evidence status

Draft the introduction around the strongest result the available evidence actually
supports, explaining the problem, method, finding and reader benefit. Best Paper
improves a developed draft; it does not require an invented ideal end state.

If unfinished research is within the authorized task, distinguish observed results,
hypotheses and proposed analyses. A planning note may state which possible outcomes
would change the research judgment, with uncertainty and missing evidence explicit.
Keep that note separate from the manuscript. Do not invent future numbers, findings
or contributions to make a planning narrative look submission-ready, and do not
ban placeholders when they honestly identify missing evidence.

Update the abstract, introduction and contributions when evidence changes.
Unsupported claims are removed or rewritten, and the surrounding argument repaired.
**Every asserted result, number and conclusion in the manuscript must correspond
to evidence actually obtained.**

When introducing the work, state what material was analyzed, at what scale, by
what method, and how those choices address the gap just established. **The
headline result (the single most memorable result in the paper) must be
delivered before the contribution list**; the list must never be the first place
the paper's finding is explained.

### 3.8 Contributions at the end of the introduction

Follow the inherited contribution-format preference maintained in writing-guide G20, unless the current author changes it. Do not manufacture or split duplicate contributions to fill the format.

For each real contribution, ask what the work establishes, how it establishes it, what was not known or possible before, and which reader judgment changes. These are questions, not four mandatory slots: a theoretical finding or explanation need not invent a separate artifact.

Distinguish an existing component from the paper's contribution in showing why or how it applies. Do not describe repairing the manuscript's own earlier mistake as a research contribution. State the contribution directly, preserve its supported strength, and leave mechanism detail to the body. Check parallel presentation without forcing unlike contributions into identical sentences.
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

## 4. Source and method boundaries

Source A and B observations describe selected examples of accepted writing, not universal acceptance requirements. Source C preserves earlier author guidance; current requirements and the writing-guide are the operative rule source. Keep the sampling and evidence limits when using examples.

Resolved historical conflicts are not a second arbitration workflow. Apply current scope, evidence and reader duty through the shared audit routing. Character-level style preferences and contribution format are maintained once in writing-guide.
