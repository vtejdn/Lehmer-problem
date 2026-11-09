---
author: Yin
---
# Adaptive integer sampling for small Mahler measure

## Task associations

| Task | Scope |
| --- | --- |
| [Unrestricted Lehmer gap](../tasks/Yin_T_G0001_v1.md#contract) | Improve finite search for integer polynomials with small positive total Mahler measure and return certified candidates and useful distributional evidence to the unrestricted counterexample direction. |

<a id="route"></a>
## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Test reduced pair-prior strength in a separate small live comparison, retaining full-measure certification and the fixed-biased baseline. |
| parent | [Arithmetic constructions](Yin_S_G0004.md#route) |

The [explicit G0001 resumption](../tasks/Yin_T_G0001_v1.md#decision-resume-adaptive-sampling-2026-11-09) selects implementation and execution of this bounded comparison under the main research agent.
The first protocol below was prepared while research was paused and has now been completed without changing its sampling laws.
The existing Task limits continue to govern the work.

<a id="question"></a>
## Question and contribution

Can a distribution learned from complete Mahler-measure feedback find more useful integer candidates per unit of computation than uniform sampling or a fixed structural bias?
The immediate target is \(1<M(P)<6/5\).
A certified value below the Lehmer number would improve the known minimum; refuting the unrestricted positive-gap statement still requires arbitrarily small positive logarithmic measures.
Finite calibration and empirical enrichment alone supply neither conclusion.

S4 retains integer constructions, necessary conditions and any argument proving positive mass in arbitrarily small shells.
This child owns the sampling laws, comparisons and finite search efficiency.
Its successful candidates and recurrent features return to S4 for mathematical investigation.
The initial comparison uses a common reciprocal coefficient box; subsequent trace-grid or central-deformation generators require a separate, explicitly bounded comparison on their stated supports.

<a id="inputs"></a>
## Reused inputs and limitations

- [J146](../computations/programs/Yin_J_G0146/readme.md#finite-shell) supplies an existing finite circular-unit law and four values between \(6/5\) and \(13/10\), with exact probabilities.
  Those fixed supports and results provide comparison experience, without an adaptive update or a hit below \(6/5\).
- [J147](../computations/programs/Yin_J_G0147/readme.md#whole-shell) supplies complete fixed-degree reference shells at degrees 14, 18 and 20.
  Its [nonunit control](../computations/programs/Yin_J_G0147/readme.md#unique-input) has measure between 1.18836814 and 1.18836815 and absolute resultant 4313.
  A unit-resultant restriction would omit that control.
- [C870](../claims/Yin_C_G0870_v2.md#amplification) shows that a fixed-threshold conditional probability can tend to one by reproducing one existing value.
  Repeated samples, cyclotomic padding and power substitutions must therefore remain separate from distinct-value discovery.
- [J155](../computations/programs/Yin_J_G0155/readme.md#factorization-measure) supplies an integer point satisfying its two moments, strict signs and endpoint, with complete measure about 2.6206.
  Those structural conditions may guide proposals, but the evaluation uses the full measure.
- [L464 v9](../ledger/Yin_L_G0464_v9.md#rare-shell) bounds success for uniformly light-tailed coefficient laws on its specific logarithmic-cut family.
  The finite box below tests an algorithm at fixed degrees; it supplies no asymptotic sampling claim and imposes no fixed-height restriction on later research.

<a id="metrics"></a>
## Evaluation and duplicate handling

For every proposed monic polynomial retain the exact integer coefficients and evaluate \(M(P)=\prod_j\max(1,|\alpha_j|)\), with multiplicity.
The objective is the whole polynomial's measure.
A small irreducible factor extracted from a larger-measure output is a separately reported discovery, with its own verification and costs.

| Metric | Convention |
| --- | --- |
| Primary discovery yield | Distinct certified values in \(1<M<6/5\) found within each fixed wall-clock budget; report the time to the first such value, censored at the budget when absent. |
| Best certified measure | Smallest certified positive measure, with an enclosing interval and the exact polynomial; include all exterior roots. |
| Recovered core classes | Remove cyclotomic factors, repeatedly compress an exact \(F(z^k)\) representation for \(k>1\), then choose the lexicographically smaller monic coefficient list under \(z\mapsto-z\) before counting classes. |
| Exploration diagnostics | Report raw hit rate, neutral mass, repeated proposals, repeated normalized cores, unresolved numerical cases and yields at \(5/4,13/10,7/5\). |
| Computational cost | Charge generation, rejected proposals, scoring, distribution updates, factorization, certification and duplicate handling to the same budget; report proposal and completed-evaluation counts as well. |

Different normalized cores can have the same measure.
Count values as distinct only after disjoint certified intervals or an exact algebraic comparison separates them.
Leave unresolved equality classes explicit instead of counting them as new values.
Recovery of a known value measures search performance; novelty requires comparison with the actual retained reference data and applicable published records.
No improvement in average \(\log M(P)/\deg P\), maximum root radius or moment fit substitutes for the primary metric.

<a id="first-experiment"></a>
## First controlled experiment

The following is the frozen first-pilot specification.
Its finite scope calibrates search performance in degrees with existing reference data; it is not a new exhaustive search or an attempt to evade those degree results.

### Common integer space and evaluation

For \(D=2n\in\{14,18,20\}\), use
\[
 \Omega_D=
 \left\{
 z^{2n}+1+\sum_{i=1}^{n-1}a_i(z^i+z^{2n-i})+a_nz^n:
 a_i\in\{-4,-3,\ldots,4\}
 \right\}.
\]
All three arms use this same space and the same evaluator.
The degree-20 nonunit control lies in this box.
There is no hard unit-resultant, irreducibility, Salem-root-type or single-cut-chamber restriction.
Record chamber membership as an optional diagnostic whose cost is charged equally.
J147's unrestricted-height counts are not counts for this box; reference comparisons must intersect the actual coefficient domain.

Use the existing exact polynomial and complete-measure routines where adequate.
Exact cyclotomic detection identifies the neutral outputs.
A fixed numerical precision and tolerance, selected during the degree-14 calibration, may rank positive candidates by the approximate complete \(\log M(P)\).
All reported threshold hits and best measures require certification; approximate scores and unresolved cases cannot establish a hit.
An unresolved score does not enter the adaptive elite set.
Any numerical rejection used to save work must either be a proved exclusion at the relevant threshold or remain explicitly unresolved.

### Three sampling arms

1. **Uniform.**
   Draw the \(n\) free coefficients independently and uniformly from the nine-element alphabet.
2. **Fixed bias.**
   With probability \(1/10\), use the uniform arm.
   Otherwise draw independent coefficients with \(p(k)=2^{-|k|}/\sum_{j=-4}^{4}2^{-|j|}\).
   This fixed small-coefficient preference is a baseline whose usefulness is to be tested.
3. **Adaptive bias.**
   Keep the same \(1/10\) uniform exploration component throughout.
   The remaining component is a product of categorical laws on adjacent pairs \((a_1,a_2),(a_3,a_4),\ldots\), with one singleton when \(n\) is odd.
   Initialize each block with the corresponding product of the fixed-bias probabilities.
   After each 256-proposal batch, collapse resolved positive candidates to one representative per normalized core, then use the lowest-scoring ten percent of those representatives, rounded up.
   Add one pseudocount to every possible block state, form the block frequencies, and update each block law to four fifths of its old law plus one fifth of those frequencies.
   A batch with no eligible positive candidate leaves the laws unchanged.

Pair blocks permit a first limited test of learned coefficient correlations.
They do not assert that the relevant arithmetic correlations are local or captured by this model.
All arms start without inserting a known small-measure polynomial or its coefficient pattern.
The adaptive arm learns only from its own earlier proposals.
The reference census and special control coefficient lists are used by the verifier and final evaluator, not to fit proposal probabilities.
Reference replay is reported separately from stochastic discoveries.

### Budget, replication and held-out evaluation

Use seeds 0 through 4, one run per seed, arm and degree.
Each run has at most 60 seconds of wall-clock time on one worker, including all costs in the metrics table.
The 45 runs have a total experimental ceiling of 2700 seconds, subject to any stricter resumed Task limit.
Do not run this pilot while the Task is paused.

Use degree 14 first to check the shared evaluator, numerical ranking settings and the implementation of the declared laws.
Freeze the resulting program and all settings before inspecting the degree-18 and degree-20 comparison outcomes.
A changed sampling law or tuned parameter starts a separately identified comparison and cannot be pooled with the original one.
Each degree and seed starts from the declared initial distribution; the held-out degrees test the same procedure, not transfer of a fitted coefficient vector across dimensions.

Run arms serially in a rotating order to reduce machine-load bias.
Use the same cache policy and evaluator configuration for every arm, and report shared setup costs separately.
Stop at the time cap without an uncharged certification tail; retain unfinished cases as unresolved.
Compare results by independent run, with the median, range and all five seed outcomes visible.
Do not treat adaptive proposals within a run as independent Bernoulli trials.
Different sampling laws have different hit probabilities; estimating a probability under the uniform law additionally requires the actual likelihood ratios and their appropriate statistical analysis.

<a id="decision-conditions"></a>
## Continuation and redirection

The [J156 evaluator and sampling laws](../computations/programs/Yin_J_G0156/readme.md) have been implemented and checked, including complete measure certification and failed-run accounting.
The [completed frozen comparison](../computations/programs/Yin_J_G0156/readme.md#pilot-results) contains all 45 valid runs; J156 owns the native program, exact discoveries, costs and retained observations.
Its exact offline probabilities for the two fixed laws are separate calibration evidence and do not train the adaptive arm.
The adaptive arm won against both baselines in zero of five matched seeds at each held-out degree, losing to a baseline in four seeds at degree 18 and two at degree 20.
It fails the continuation screen below, so the original law is not enlarged in degree or runtime.
Every whole-polynomial hit below \(6/5\) recovered the known Lehmer value.

Continue bounded validation when the adaptive arm improves distinct-value discovery below \(6/5\) against both baselines in at least four of the five matched seeds at a held-out degree, without a corresponding loss at the other held-out degree.
This is a screening rule for resource allocation, not a statistical significance theorem.
A separately certified new smaller measure is direct mathematical feedback regardless of that screening rule.

When only the wider thresholds improve, retain that evidence and identify the missing change needed to reach \(6/5\) before increasing degree or runtime.
When gain comes mainly from neutral outputs, repeated cores or certification backlogs, revise the proposal law or evaluator within a new bounded comparison.
When all methods have zero target hits, report the comparison as inconclusive at the stated budget; it establishes no absence of integer candidates.
Evidence for a finite gain does not justify an arbitrary-radius positive-probability claim.
S4 retains that separate integer-existence obligation and decides whether a discovered feature supports a new construction or count.

<a id="prior-strength-follow-up"></a>
## Prior-strength mechanism and next bounded live control

The [pair-prior calculation](../computations/programs/Yin_J_G0156/readme.md#prior-dilution) proves that the original 81 pseudocounts force the pair's expected absolute coefficient sum above its initial value, regardless of the elite data.
That coefficient statement is not a Mahler-measure probability theorem.
The separate [exact fixed-elite control](../computations/programs/Yin_J_G0156/readme.md#prior-strength-control) has now been executed on the 13 calibration batches.
Changing only the pair total pseudocount from 81 to 1 raises final target mass from 0.1171515 to 1.5507105 times its initial value on that same recorded path.
This identifies a useful mechanism change, while alternative live proposals and elite sets remain untested.

The main agent's next discriminating investigation is a separately labelled live control at degree 14, with new seeds 5 through 9 and three arms: the fixed bias, the unchanged original adaptive law O, and the reduced-strength adaptive law A.
For A, a pair frequency is \((c(s)+1/81)/(m+1)\); singleton pseudocounts remain one per state, and all other laws, batch rules, precision, certification, caching and duplicate conventions stay as in the first pilot.
Use 10 seconds per run on one worker, arms serially rotated by seed, for a total experimental ceiling of 150 seconds.
The separate implementation must preserve the frozen first-pilot source and identify its changed law explicitly.
This next live control is specified but has not been implemented or run.

Retain all five seed outcomes and the same primary target count and first-hit censoring conventions.
Before increasing its scope, require A to avoid a loss to the fixed arm in target count in at least four seeds, and to improve on O in at least four seeds either by a higher target count or, at equal positive target count, by an earlier first hit.
These are allocation screens for this small reused benchmark, not significance tests or claims about unknown degrees.
If either screen fails, retain the result and reassess the model or feedback before another prior-parameter trial.
The comparison returns to the main agent after all 15 runs or any execution stop; unfinished runs cannot establish a passing result.
Degree 14 is reused calibration data, and any later degree-18/20 evaluation is likewise a reused benchmark rather than a new unseen held-out test.
The fixed-elite control and this next live comparison remain separate from the original 45-run pilot.
