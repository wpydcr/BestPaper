# Optional background on polishing studies

These historical notes preserve the source context of the method. They are not an acceptance score, a mandatory optimization target, or evidence that a particular manuscript will improve. Follow the active author task and actual reader outcome.

### 2.1 The six dimensions and their positive definitions

> **Numbering namespace**: two `G.x` schemes appear in this file. Unprefixed
> `G.x` (G.2, G.7, G.8) always means the general principles in
> `../argument.md`; the rewriting prompts in Source 2's appendix are always
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
