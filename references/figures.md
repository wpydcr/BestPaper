# Figure and Table Rules (Best Paper shared reference)

**Scope**: the single rulebook for figures and tables (commissioning, selection,
encoding, layout, acceptance, readability checks, caption rules and the output pipeline).
No other file repeats figure or table rules.

**Provenance**: the morphological generalizations here come from one pass the author made
over accepted papers from a **single venue and a single genre**, and that analysis is not
shipped with this skill, so no reader can trace the evidence behind them. **They must
therefore never be promoted to hard gates**; §8 item 1 gives the test for which of them
*are* hard gates.

**Corpus statistics do not live here**: see §0.

---

## 0. Principle: imitate the visual hierarchy, not the surface parameters (author ruling)

> **Do not learn "how many colors and icons" prior papers used; learn their visual
> hierarchy. Build a paper-level visual rhythm.**

This governs how everything else in this file is used, in three layers:

1. **Primary vs. secondary encoding.** Within one visual object, which dimension carries
   the primary information, which are auxiliary, and which should not be encoded at all.
   This transfers; the number of colors and icons does not.
2. **Reading order.** Where the reader's eye lands first, what path it follows, and where
   it stops and gets the conclusion. The design of that path transfers; specific line
   widths and color values do not.
3. **Paper-level visual rhythm.** How figures and tables are distributed across the whole
   paper, what duty each carries at which stage of the argument, and how density rises
   and falls. This is the highest layer of imitation and the one most often missed.

**Promotion and demotion rules (hard)**:

- **Never enter this file, are measured on site in Setup when needed, and may never
  serve as a quota or an acceptance item**: figure and table counts, the Figure-to-Table
  ratio, per-paper means, medians and quantiles, positional distribution, number of
  colors, number of icons, style uniformity. These are surface parameters; matching
  them produces no argumentative value.
- **Always promoted to the main line**: primary/secondary encoding, reading order,
  division of duties, number of encoding layers, evidence-status semantics, visual
  grammar reuse, whole-paper distribution rhythm.
- **The most common misuse is treating a mean as a quota** ("prior papers average N
  figures, so I need N"). Frequency proves commonness, never applicability.

---

## 1. Paper-level visual rhythm

> This section is derived from layer 3 of §0. The author's corpus pass left only
> scattered positional observations and no systematic "paper-level rhythm" dimension, so
> these items likewise must not be promoted to hard gates.

### 1.1 Distribution: the bulk of figures and tables sits in the argument's development zone, not at the two ends

**The bulk should grow where the framework is established and the systematization and
analysis unfold**, not piled into the introduction to "look substantial" and not piled at
the end to "look complete". A paper whose figures cluster at both ends usually means the
middle is not using visual objects to do any work.

**Position is set by cognitive dependency, not by aesthetic distribution.** An object
should appear **before it is first needed**, not after it is first cited.

### 1.2 Structural objects earlier, precise objects later

**Figures usually come earlier because readers need the shared structure first; Tables
usually come later because fields, objects and comparison scopes must be defined first.**
This is an inference about duty dependency, not a causal result, and it is not a
positional quota.

**Counterexamples hold**: if the body mainly relies on a table of discrete relations, an
early Figure is not required; conversely, if a complex role diagram is a prerequisite for
understanding the body, putting it on the last page adds jump cost, and that is a real
defect.

### 1.3 Division of duties between body text and numbered objects

Body text develops the reasoning and the explanation; numbered figures and tables reduce
the cost of recognizing structure, comparing, looking up, or checking precisely. When the
two repeat the same content and deleting one loses no independent duty, delete whichever
costs more in cognition or page budget. Key evidence must be addressable, and exact
counts, percentages and confidence intervals belong in a numbered object or the adjacent
body text.

### 1.4 Density: information density is not argument density

When many objects are individually complete but the main conclusion requires the reader to
stitch across tables and pages, overall argument density falls. Two typical failures: many
result tables preserve all the data but the main conclusion has to be assembled across
them; many highly similar curve plots are individually complete but add cross-page memory
load.

**Once objects multiply, three things must be added**: an overview object, a stable
cross-object encoding, and one cross-object synthesis conclusion. Without these three,
adding objects only adds noise.

---

## 2. What the visual hierarchy is made of

### 2.1 One object, one primary duty

**Every object present must have at least one clear and irreplaceable primary duty**, and
may additionally carry secondary duties that the body text explicitly uses.

If one Figure tries to show the taxonomy, the pipeline, all the citations, the results and
the recommendations at once, first check whether those duties are compatible, then split
or delete the encodings that cannot change the conclusion. **One giant figure carrying
overview, complete evidence, results and recommendations simultaneously is among the most
common failure forms.**

### 2.2 Encoding layers: color adds exactly one layer of semantics

- Critical states must carry **text, shape, texture or symbol redundancy**; color alone
  must not bear them.
- Color suits distinguishing a set of opposites, stages, states relative to a baseline, or
  evidence tiers. It **must not simultaneously carry object identity, state, magnitude and
  confidence**.
- Test: convert the figure to grayscale. Are the distinctions that would change the
  conclusion still legible?

### 2.3 Evidence status and relation type must be encoded explicitly

This is the layer of the visual hierarchy that collapses most easily and costs most when
it does.

- **Not reported, not applicable, not satisfied, partially satisfied, verified and refuted
  must not be flattened into the same blank or cross.** A single check/cross cannot express
  the difference between claimed / supported / derived / not reported / not applicable /
  refuted. Folding "not reported" into "non-compliant" is an error that changes the
  conclusion, and no amount of table completeness recovers it.
- **State semantics matter more than the palette**: define each state's decision threshold
  first, then choose symbols and colors.
- **Arrows must state the relation type**: mechanism, correlation, hypothesis, or direct
  evidence. A relation arrow with no evidence-strength encoding reads as established
  causation. That is visual overclaiming.
- **Never fabricate data when drawing an abstract object.** Do not invent concrete values
  to make it look like a measurement: the reader's first reaction is "where do these
  numbers come from", so the figure not only fails to help but creates a new attack
  surface. Draw the object's geometry schematically, label the axes as qualitative, and
  state in the caption that the coordinates are qualitative only (**[English
  manuscripts]** write `Axes are qualitative`; Chinese manuscripts use an equivalent
  phrasing).
- When a figure mixes evidence tiers (hypothesis, derivation, author synthesis, direct
  measurement, external validation), they **must be encoded explicitly** (solid vs. dashed
  lines, a dedicated Gap box, an explicit label saying the object is a hypothesis rather
  than an established finding; **[English manuscripts]** label form such as `Hypothesis,
  Not Established Finding`, with an equivalent phrasing in Chinese manuscripts). Readers
  must not be left to reconstruct the epistemic status from the body text. A visual object
  may actively take on the duty of **counteracting overclaiming**; that is one of its
  legitimate uses.

### 2.4 Visual grammar reuse

The same component, stage, risk, role or state should keep **consistent color, shape,
numbering and direction** across Figures.

Strong form: overlay several layers on one shared skeleton diagram (a base structure plus
two opposing mechanisms acting on it) so the reader learns the visual vocabulary once; or
use fully isomorphic coordinate encodings to compare two environments, so differences
visibly come from the data rather than from the drawing.

**This is the main carrier of "visual hierarchy" at whole-paper scale**, and the single
most transferable item in this file.

### 2.5 Density layering: compressed in the body, full draft in the appendix, stable cross-index

"First understanding" and "complete audit" are conflicting goals for a giant table and
cannot be carried by one object. The reliable arrangement is three pieces:

1. The body carries a compressed object retaining only **the dimensions that change the
   conclusion**.
2. The appendix carries the full draft: all fields, tools, parameters, sources, exceptions.
3. A stable cross-index links them (body Table N ↔ appendix Table M).

**Blocking condition**: objects needed for first understanding and for the core judgment
must stay in the body and **must not be moved to the appendix merely because they are
large**. Pushing key evidence back reduces the main text's judgeability.

---

## 3. Figure vs. Table: division and choice

### 3.1 The essential division

- **A Figure's primary duty is to reduce relational reasoning.** It suits paths,
  hierarchies, state transitions, temporal processes, distribution shapes, continuous
  trade-offs, visual quality and inference boundaries.
- **A Table's primary duty is to reduce lookup and checking cost.** It suits objects ×
  attributes, codebooks, evidence status, many-to-many mappings, exact values, sample
  denominators, configurations and provenance.

They are not two skins on the same information. The formal label is also not the visual
grammar: an object that looks like a table may legitimately be numbered as a Figure.

**Figures do not carry the argument for the body text.** A figure's duty is to make an
**already sound body argument** easier to see. If a claim can only be understood by looking
at the figure, the body text is underwritten: **fix the body text, not the figure**.

**Figures must use the paper's own vocabulary.** Do not introduce new instances, terms or
objects absent from the body "to aid understanding"; every label in a figure should be
traceable to the body text.

### 3.2 Selection order (four steps, judged in order)

1. Does the claim depend on topology, path, hierarchy, continuous shape or visual quality?
   If so, prefer a Figure.
2. Does the claim depend on exact cells, discrete attributes, many-to-many mappings or
   evidence status? If so, prefer a Table.
3. Do both kinds of information **independently change the conclusion**? If so, split the
   duties across an overview Figure and an evidence Table.
4. Neither applies and one or two sentences express it losslessly? Then **add no visual
   object**.

### 3.3 Borderline objects are decided by the reader's task

Heatmaps, symbol matrices and table-shaped summary Figures sit on the border. The criterion
**is not the formal number but the reader's primary task**: seeing the overall pattern
leans Figure, looking up an exact cell leans Table.

If a heatmap, symbol matrix or value-annotated plot **still supports both whole-view
reading and exact checking at final size**, and passes the deletion test, a single object
may carry both compatible duties.

### 3.4 When a Figure is needed (five triggers + minimum sufficient content)

1. **A process, path, state or trust boundary determines the conclusion.** Triggers:
   lifecycle, propagation path, data flow, role interaction, state transition, feedback,
   reachability. Minimum content: start, end, node semantics, arrow direction, stages or
   trust boundaries; a legend is required once there is more than one node or edge type.
   **Counterexample test: if rewriting it as two linear sentences loses nothing, the
   relation is too simple to deserve its own number.**
2. **A taxonomy needs to express hierarchy, overlap or composition.** Triggers: at least two
   levels of categories, or one object spanning categories, or composition changing the
   conclusion. Minimum content: root, levels, leaf definitions, exclusive or non-exclusive
   semantics, cross-category relations, object index. With one level and few categories, a
   body-text list is faster. **If an object must be repeated across several leaves,
   acknowledge multi-labeling or switch to an attribute matrix; repeated references must
   not paper over a broken taxonomy.**
3. **The conclusion depends on a continuous trend, threshold, crossing or trade-off.**
   Triggers: how it varies with scale, when it crosses the risk line, under which
   conditions the ranking flips, whether two objectives are simultaneously satisfiable.
   Minimum content: axes and units, baseline, legend, common scale, and the thresholds or
   acceptable regions that change the judgment. Sampling or repeated measurement also
   requires reporting the sample or run count and the uncertainty; theoretical curves,
   deterministic results or complete populations require stating the generation or counting
   scope. **Conditions being compared must use isomorphic coordinates and stable visual
   grammar; non-comparable panels must be labeled as such.**
4. **Visual quality or the error form is itself the evidence.** Triggers: reconstructed
   images, patches, interfaces, waveforms, artifacts, semantic detail. Minimum content
   depends on the claim: claims about typicality, frequency, severity or method superiority
   **require accompanying quantitative metrics or systematic coding**; explaining only where
   an error occurs or how a mechanism manifests need not be quantified, but the sample
   selection basis must be stated and **examples must not be extrapolated into typical
   phenomena**. Showing only the best example cannot establish typicality. Examples explain
   "what went wrong"; aggregate metrics answer "how often and how severe".
5. **An evidence chain or inference boundary must be shown.** Triggers: a synthesized
   conclusion spanning multiple sources, populations, methods or intermediate assumptions,
   easily misread as a direct finding. Minimum content: observed facts, inference steps,
   gaps, conclusion strength, and an explicit legend for solid vs. dashed.

### 3.5 When a Table is needed (five triggers + minimum sufficient content)

1. **Many objects × stable attributes.** Trigger: the reader needs to look up one object's
   value on several attributes. Minimum content: an explicit row unit, stable column
   definitions, a symbol legend, citations or sources, and **distinct semantics for
   missing, negative and not-applicable**.
2. **A concept must be executable by coders.** Trigger: later work must code or judge real
   analysis units item by item. Minimum content: code, definition, what to look at when
   judging, positive example, negative example, boundary example, conflict-resolution rule.
   Multi-coder work also needs agreement and disagreement handling. **The minimum is an
   applicability condition, an exclusion condition, a boundary example and a
   conflict-resolution rule per code.**
3. **Exact values, denominators, intervals or discrete conditions are needed.** Trigger: the
   conclusion depends on specific numbers rather than curve shape. Minimum content depends
   on the source: ratios need numerator and denominator; measurements need units, metric
   direction and baseline; discrete conditions need not-applicable values distinguished.
   Sampling or repeated measurement requires run counts and statistical uncertainty;
   deterministic enumerations, configuration constants or full-population counts require
   stating the scope. **Temporal processes prefer figures, final-value decompositions prefer
   tables; continuous parameter sensitivity prefers figures, a small cross of discrete
   experimental conditions prefers tables.**
4. **Evidence status must be recorded.** Trigger: the question is "has it been tested",
   "is it only the original authors' claim", "was it later broken", "is the evidence
   direct". Minimum content: the state set, each state's evidence threshold, source, time
   or version, and **"not reported" as its own state**.
5. **Reproduction, audit and provenance tracking are needed.** Trigger: version, input,
   configuration, sample filtering or the applicable denominator changes the result. May go
   in the appendix, but **the body must state how this information constrains the
   conclusion**.

---

## 4. The six core duties

1. **Define the shared objects and the reading contract.** Before the reader enters the
   details, fix the components, stages, actors, assets and basic flows. The duty is not "make
   the system look intuitive" but **to constrain every later term and judgment to land on the
   same objects**. Test: if the body cannot stably reuse the figure's nodes and numbering, the
   figure has not completed the reading contract.
2. **Establish a coordinate system that supports reasoning.** Preserve hierarchy,
   reachability, state transitions or formal relations, so later tables can refer back to its
   edges and nodes. **What separates it from an ordinary taxonomy diagram is that judgments can
   be derived from it**: a diagram that can only answer "which names exist" and not "when does
   it hold, how does it compose, where does it conflict" is usually better as a body list or a
   table.
3. **Operationalize a concept into decidable rules**, so different readers reach the same or
   an explainable judgment from the same source (see §3.5 item 2).
4. **Preserve systematic coverage and evidence tracking.** Rows are real analysis units;
   columns are attributes, states, conditions and sources that change the judgment. **A strong
   matrix surfaces blanks, conflicts and counterexamples** (empty cells directly generate
   unexplored combinations and drive follow-up experiments; a component table exposes that
   existing work is non-comparable and thereby generates a unified benchmark). **A weak matrix
   merely arranges known prose into cells.**
5. **Carry comparison, validation and diagnosis.** Result Figures suit trends, thresholds,
   crossings, variance, Pareto fronts and temporal processes; result Tables suit discrete
   conditions, exact values, denominators, confidence intervals and states. **Such objects must
   change the conclusion**: merely repeating "method A is higher" with no conditions,
   boundaries, anomalies or action implications has limited evidential value. Transferable
   strong forms: "show the anomaly first, then trace the root cause with a single-factor
   intervention plot", and "a cumulative-process plot showing the stage structure a final-value
   table hides, then a table decomposing the exact sources".
6. **Constrain claims and preserve epistemic boundaries.** See §2.3.

## 5. Decision and acceptance

### 5.1 Core criterion: deletion loss comes in five kinds, not all of which are "changes the conclusion"

Every candidate object must answer "what is lost if it is deleted", and the answer must land
in one of these:

1. **Loss of conclusion validity** (a pattern, counterexample or boundary the main conclusion
   needs) → must be kept.
2. **Loss of relational understanding** (path, hierarchy, state or overall shape) → a Figure
   has a reason to exist.
3. **Loss of audit completeness** (exact cells, provenance, denominators, reproduction
   conditions) → a Table has a reason to exist.
4. **Loss of reading convenience** (only navigation, motivation or scanning speed) →
   **subordinate to the page budget; does not count as new evidence**.
5. **Only aesthetics lost**, no independent cognitive duty → **must not be added**.

Only the first three normally justify a numbered object. One case sits outside the five: when
the body already retains the summary, key rows and boundaries needed to judge the conclusion,
deleting the full detail mainly reduces reproduction scope. Such drafts belong in the
appendix.

### 5.2 When not to add a figure or table (check item by item)

1. There is a single ratio, mean or simple comparison that one body sentence expresses fully.
2. Few categories, with no hierarchy, crossing or composition.
3. The figure just turns the table's discrete numbers into bars, adding no trend, threshold,
   anomaly or distribution shape.
4. The table just repeats the body sentence by sentence, adding no lookup, operationalization
   or audit capability.
5. **The data, taxonomy or coding does not yet really exist and the scope may still change**
   (unfinished results must not be drawn as a placeholder conclusion).
6. The visual encoding exceeds what is reliably legible at final size.
7. A figure and a table repeat the same evidence and deleting one loses no independent duty.
8. The sample is too small, yet percentages, bars or rankings manufacture an air of stability.
9. Relation arrows do not state whether they mean mechanism, correlation, hypothesis or direct
   evidence.
10. The body never uses the figure's encoding and never extracts cross-row patterns from the
    table.
11. A simple dichotomy or a few linear steps could be expressed losslessly in one sentence, and
    is numbered separately only because it "belongs to the complete taxonomy".
12. The object merely repeats one or two stable facts and purely serves motivation buildup,
    terminology onboarding or conclusion indexing, while its page cost exceeds the navigation
    benefit.

### 5.3 Counterexample test

Actively look for cases that would **flip a ranking, break a taxonomy, expose a missing state
or change the applicable scope**, and put those conditions into axes, facets, columns or a
separate diagnostic object: **they must not be buried in the caption**.

### 5.4 Body-text closure; pick the template by object type, do not apply it mechanically

- **Result Figure / result Table** use a four-sentence closure: what question this object
  answers; what the strongest pattern is; one counterexample or boundary; how this changes the
  later taxonomy, experiments, conclusions or recommendations.
- **Codebook Table**: state the applicable scope, decision rules, ambiguity handling and later
  use.
- **Structure Figure**: state node and edge semantics, the reading path, and where it is reused.
- **Audit Table**: state the sample boundary, key cells, missing-value semantics, and how it
  constrains the conclusion.

Failure forms: writing only "see Figure X" without telling the reader what to look at;
restating the maximum without explaining why; giving the reason but not the boundary, which
inflates the claim; giving the conclusion but not the action implication, which detaches the
object from the paper.

### 5.5 Caption self-sufficiency

A caption states, per object type: objects, variables, units, metric direction, symbols, panel
differences, sample or run scope, and the necessary evidence boundaries. **A conceptual figure
with no axes or values need not be padded with units and sample sizes.** One line is best.
**Hard gate, no exemption**: measured at the final typeset width, a narrow single-column
figure MUST NOT exceed 4 lines, and a wide or full-width figure MUST NOT exceed 3 lines.
When the necessary explanation exceeds the limit, move the non-self-sufficiency explanation
into the body, but never delete what determines truth value or evidence boundaries. Using
the caption to state explicitly that something is an inference rather than a direct
measurement is a legitimate use of epistemic constraint.

**A caption is a headline position: overstating it is a factual error.** Before the figure
lands, check every arrow and every number against the source; a schematic being approved does
not make the schematic true.

### 5.6 Size follows the task, and the judgment must be made at final size

- Single column suits local processes, small comparisons, few results and teaching examples.
- Full width suits a shared system model, the main taxonomy figure, the main evidence matrix,
  and small multiples needing a common x-axis.
- Full-page or rotated objects are justified only when splitting would break the relations.

**Fitting on the page is not the same as being readable.** The final judgment must be made at
the paper's actual typeset size, never on a zoomed-in PDF. Check font size, line width, color
redundancy, headers, legends, axis units and grayscale legibility. **If an object can only be
read after heavy zooming or rotation, split it into an overview and a draft.**

**A collision check is mandatory before delivery; readability must not be judged by
imagination.** Check at minimum: text against text, text against lines, text against axes, and
text being clipped. Bounding boxes of rotated text are loose estimates and produce false
positives; confirm with geometric distance or pixel-level checks.

### 5.7 Body vs. appendix layering

Objects needed for first understanding and the core judgment stay in the body (blocking
condition, see §2.5). Full corpus, configuration, secondary results, robustness and source
drafts go to the appendix. The body must explain how the appendix material constrains the
conclusion, and provide a stable cross-index.

**An object placed after the references is not automatically an appendix**; report positions
based on the explicit section headings.

### 5.8 Three fast, mechanically executable tests

- **3-second readability**: cover the caption; if a reader cannot say in 3 seconds what the
  figure is about, it is better left out. Drawing a structure the table already explains is
  just rearrangement.
- **Do not draw the mathematics, draw the consequence**: unfolding a formula into a flowchart,
  tree or node graph still leaves the reader looking at symbols. The test is "is this insight
  invisible in the symbols": visible only after substituting values → worth drawing; obvious
  once stated → do not draw. **An argument having a geometric form does not mean it deserves a
  figure.**
- **Numbers in a figure must have an intuitive reading**; if they do not, fall back to prose
  (normalized numbers over incommensurable dimensions have no intuitive reading).

---

## 6. Execution checklist (the order for adding a figure or table)

1. **Build the claim list first.** For each core claim record: the evidence object, the
   cognitive task the reader must complete, boundary conditions, counterexamples. **Do not
   start by listing figures you want to draw**, and certainly do not decide to draw a taxonomy
   figure and then look for material to fill it.
2. **Choose the visual grammar for the task** (the four steps of §3.2).
3. **Run the deletion test** (the five kinds in §5.1).
4. **Run the counterexample test** (§5.3).
5. **Check body-text closure** (§5.4, template by object type).
6. **Check at final size** (§5.6).
7. **Decide body vs. appendix layering** (§5.7).
8. **Look back at whole-paper rhythm** (§1): does the distribution sit in the argument's
   development zone, is the visual grammar reused, do the body and the numbered objects overlap
   in duty, and after the density increase were the overview and the synthesis conclusion added.

### 6.1 Production discipline (engineering side)

- **Before switching genre, look at the corpus; do not invent the form from inside the paper.**
  What must be looked at is **the rendered sample figures themselves** (render permission-locked
  PDFs to bitmaps first; PyMuPDF's `get_pixmap`, `pdftoppm`, `mutool draw` or any other renderer
  will do: the hard requirement is only "see the rendered result", not a specific
  implementation), not somebody's written description of the figures. Descriptions preserve the
  "duty" and lose exactly the "what it looks like" (size, orientation, density, palette, icon
  style).
- **When delegating "what figure should be drawn", always supply the sample image paths.**
  Otherwise the delegate inherits the delegator's blind spot and can only enumerate candidates
  from inside the paper.
- **Output pipeline (hard gate, no exemption)**: figures MUST be drawn with Python and with
  Python only: no other drawing pipeline is permitted, whatever the figure type. Anything
  Python cannot draw (complex hand-drawn schematics, screenshots) is described to the user
  (intent, elements, arrows) for the user to supply. **Scope of "zero bitmaps"**: it bans
  rasterizing what should have been vector, which is text, axes, lines, legends and icons. It
  does not reach raster content that *is* the evidence under §3.4 item 4 (reconstructed images,
  patches, interfaces, waveforms, artifacts); such a panel is placed at its native resolution
  and every label drawn around it stays vector. Vectorizable elements MUST use vector
  output; icons are downloaded as SVG (e.g. Bootstrap Icons, simple-icons) and parsed into
  vector paths; the PDF MUST contain no bitmap outside the carve-out just stated. Check it on
  the output with `pdfimages -list`: every image it reports must be an evidence panel under
  §3.4 item 4, and any other entry is a violation. Caption line limits: see §5.5.

---

## 8. Method and validity limits

1. The **morphological generalizations** in this file (provenance in the header) do not represent
   all years, all venues or the acceptance criteria, and **must never be promoted to hard gates**;
   they may only rank priorities among several compliant implementations. Acceptance proves only
   that a practice can exist, never that it is optimal or that it caused acceptance.
   **Which clauses those are is settled by what a clause rests on, not by a list**: one that reports
   how many, how often, how long or how commonly past papers did something is a morphological
   generalization; one that says what to do, what to check, or what must not be done is not, and is
   executed as written. Two rules here rest on neither and hold across papers whatever a corpus
   shows: figures are produced with Python and Python only (§6), and the caption line limits
   (§5.5). Both are author-level rulings, in the same class as H.1.
2. Beyond numbered Figures and Tables, algorithms, listings and equations do not enter the
   figure count, but must be evaluated separately when they carry a key visual duty.
3. Positional observations are based on physical PDF pages (including the cover), which is
   not the paper's printed page numbering. Two measurements taken under different
   conventions do not compare.
4. **Inferring a figure's existence from body citations alone inflates the count**: an appendix
   object cited in the body may not exist in the target venue's official PDF at all.
   Verification must go back to the actual pages. This is both a validity caveat and an
   operational discipline for Setup's corpus measurement.
