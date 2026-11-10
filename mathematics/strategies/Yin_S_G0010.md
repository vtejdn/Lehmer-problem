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
| disposition | paused |
| priority | Retain the completed sampling comparisons and exact fixed-cell exclusion; resume with a concrete change in integer supply or complete exterior-cost control and a discriminating bounded test. |
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
## Prior-strength mechanism and completed bounded live control

The [pair-prior calculation](../computations/programs/Yin_J_G0156/readme.md#prior-dilution) proves that the original 81 pseudocounts force the pair's expected absolute coefficient sum above its initial value, regardless of the elite data.
That coefficient statement is not a Mahler-measure probability theorem.
The separate [exact fixed-elite control](../computations/programs/Yin_J_G0156/readme.md#prior-strength-control) has now been executed on the 13 calibration batches.
Changing only the pair total pseudocount from 81 to 1 raises final target mass from 0.1171515 to 1.5507105 times its initial value on that same recorded path.
This identifies a mechanism change separately from the live proposals and elite sets evaluated below.

The separately labelled live control uses degree 14, new seeds 5 through 9 and three arms: the fixed bias, the unchanged original adaptive law O, and the reduced-strength adaptive law A.
For A, a pair frequency is \((c(s)+1/81)/(m+1)\); singleton pseudocounts remain one per state, and all other laws, batch rules, precision, certification, caching and duplicate conventions stay as in the first pilot.
Use 10 seconds per run on one worker, arms serially rotated by seed, for a total experimental ceiling of 150 seconds.
The separate implementation must preserve the frozen first-pilot source and identify its changed law explicitly.
The [separate live implementation](../computations/programs/Yin_J_G0156/readme.md#prior-strength-live) now implements this protocol while preserving the frozen first-pilot source.
Its bounded implementation controls and [complete fifteen-run comparison](../computations/programs/Yin_J_G0156/readme.md#prior-live-results) have now been executed.

Retain all five seed outcomes and the same primary target count and first-hit censoring conventions.
Before increasing its scope, require A to avoid a loss to the fixed arm in target count in at least four seeds, and to improve on O in at least four seeds either by a higher target count or, at equal positive target count, by an earlier first hit.
These are allocation screens for this small reused benchmark, not significance tests or claims about unknown degrees.
If either screen fails, retain the result and reassess the model or feedback before another prior-parameter trial.
The comparison returns to the main agent after all 15 runs or any execution stop; unfinished runs cannot establish a passing result.
Degree 14 is reused calibration data, and any later degree-18/20 evaluation is likewise a reused benchmark rather than a new unseen held-out test.
The fixed-elite control and this live comparison remain separate from the original 45-run pilot.

The complete live comparison has five nonlosses to fixed and five improvements on O by the declared rule.
One O/A time comparison precedes their first update and supplies no learning attribution; the other four seeds independently meet the improvement rule.
Every A and fixed run finds exactly one known target value, while O succeeds in only two of five runs.
A's large increase in raw hits comes with about seventy percent repeated proposals, so it does not establish greater target-value diversity than fixed bias.

<a id="degree-validation"></a>
## Completed bounded degree comparison

The next selected question is whether unchanged A improves recovery against fixed bias in the larger degree-18 and degree-20 boxes, beyond the degree-14 setting used to choose the prior strength.
Use only fixed and A, seeds 10 through 14, ten seconds per run, with a fresh law and cache for each degree, seed and arm.
Run the twenty identities serially on one worker, with the two arms' order rotated by degree index plus seed index, for an experimental ceiling of 200 seconds.
Keep the same full evaluator, arithmetic, exploration, batch, elite, duplicate and cost conventions; introduce no new prior strength or reference training.
The original O has already failed its declared screen and is not assigned another budget in this comparison.
The [separate degree implementation and completed comparison](../computations/programs/Yin_J_G0156/readme.md#degree-validation) retain all twenty valid runs and their original observations.

At each degree, report all five target-value counts and first-hit times, exact cores and value identities, raw and repeated hits, neutral mass, fresh evaluations, cache hits and wider-threshold counts.
Before increasing degree or runtime further, require A to avoid a target-count loss to fixed in at least four seeds at each degree, and to improve on fixed in at least four seeds at one degree by a larger target count or, at equal positive count, an earlier first hit.
A time comparison before any changed-law update remains an observation, without an attribution to adaptation.
All twenty valid runs are required for a passing screen; all-zero ties do not count as improvements.
Both degrees reuse inspected reference benchmarks, so this tests the procedure without claiming an unseen validation set or statistical significance.
If this screen fails, return to model and feedback design before another degree or prior-parameter trial.
Whether it passes or fails, known-value amplification remains separate from a new small measure or the arbitrary-radius existence obligation in S4.

The completed comparison has five nonlosses and four improvements at each degree, and therefore passes this screen.
A finds one target value in all ten runs; fixed bias does so in four degree-18 runs and one degree-20 run.
All 577 raw whole-polynomial target hits have the known Lehmer core, and all A first hits follow its first update boundary.
The gain establishes finite recovery performance under the declared rule, while leaving target-value diversity unchanged.

<a id="core-mass-follow-up"></a>
## Completed diagnostic: target mass by core

Before assigning a larger stochastic comparison, evaluate the initial and final laws of the ten completed A runs on the already inspected degree-18/20 target census.
Partition that census by exact normalized core, separating the Lehmer value from the second known value near 1.1883681475.
Compute the conditional probabilities as exact rationals from the actual committed final block weights, including the unchanged one-tenth uniform component.
Keep this offline calculation separate from proposal training, observed discoveries and estimates of an unknown population.
Preserve the exact target partition and final states needed to reproduce the calculation; no new live run or prior choice is part of this diagnostic.

If the second core loses probability while the Lehmer core gains it, revise the feedback or diversity mechanism before extending the search.
If both gain, quantify the remaining absolute probability and use it to choose a bounded test aimed at recovering distinct target values, without treating this finite benchmark as an arbitrary-radius existence result.
Any mixed result is assessed by degree and seed rather than pooled into an unsupported universal advantage.

The [completed exact diagnostic](../computations/programs/Yin_J_G0156/readme.md#core-mass-diagnostic) finds increased Lehmer mass and decreased second-core mass in all ten final laws.
At degree 18, the second-core final-to-initial ratio lies between 0.000494858 and 0.00155342; at degree 20 it lies between 0.00203085 and 0.0161242.
These are exact initial-to-final comparisons with decimal displays, without a claim of monotone change or a pathwise success probability.
The recovery screen therefore does not justify enlarging the current law: revise diversity feedback or the proposal representation first.
The next design must evaluate target-core coverage separately from recovery of the existing minimum, and must keep known reference data out of any experiment declared to learn only from its own proposals.

<a id="template-mutation-control"></a>
## Completed control of a template-preserving mutation mechanism

The [inspected nearest-reference method](../audits/literature/SEMR21/Yin_U001.md#sampling-comparison) supplies an existing way to preserve global coefficient correlations after a sparse random assignment.
Its bivariate domain, reference training, factor-inclusive outcomes and 1.37 threshold differ from the current whole-polynomial experiment; its unspecified sampling and tie choices are not silently imported.
The selected exact finite mechanism control is now complete, before implementation of another live learner.

At each degree 18 and 20, take the complete retained Lehmer-prefix class as an explicitly known reference library.
With probability one tenth draw uniformly from the original box; otherwise choose a library parent uniformly, choose \(k\) uniformly from \(1,2,3\), choose \(k\) distinct free coordinates uniformly and independently change each by \(+1\) or \(-1\) with equal probability.
If a changed coordinate leaves \([-4,4]\), return the unchanged parent.
Compute the exact mass on the second target core from the retained target partition and compare it with fixed bias and the observed A final laws.
This fully specified local kernel is a separate reference-seeded control, not a reproduction of the paper's algorithm or a claim about a learner without reference input.

The [completed control](../computations/programs/Yin_J_G0156/readme.md#mutation-kernel-control) gives second-core mass approximately \(5.131879125\cdot10^{-6}\) at degree 18 and \(1.514079067\cdot10^{-5}\) at degree 20, respectively 4.894863983 and 8.300145973 times the fixed-law mass.
Both probabilities also exceed the corresponding mass of every observed A final law.
The mutation component reaches both degree-18 target prefixes, but only four of the ten degree-20 prefixes; the uniform component supplies the remaining coverage.
The [independent offline-control finding](../audits/reviews/Yin_R_G1111_v7.md#mutation-controls-review) verifies these exact finite comparisons, which use the complete known Lehmer parent class rather than an actual live acquisition path.
They establish neither a live cost advantage nor a new value, and do not imply arbitrarily small positive measures.

The [source preparation on reciprocal descent](../audits/literature/RS03/Yin_U001.md#reciprocal-neighborhood) and [genetic search](../audits/literature/EMRS17/Yin_U001.md#genetic-mechanism) is complete at its stated text-inspection scope.
The former uses known low-measure seeds, and the latter uses a random ternary population; neither inspected algorithm specifies the complete neutral template closure below.
This is a comparison of mechanisms, not a historical novelty claim or evidence that larger degree improves the target probability.

<a id="cyclotomic-archive-comparison"></a>
## Frozen next comparison: diversity of template representations

The [actual-parent control](../computations/programs/Yin_J_G0156/readme.md#acquired-parent-control) shows why representation diversity needs testing independently of core recovery.
All five degree-18 acquired parent sets miss every compatible mutation parent for the second core, whereas the degree-20 acquired sets concentrate more second-core probability than the complete reference library.
The [exact closure construction](../computations/programs/Yin_J_G0156/readme.md#cyclotomic-closure) obtains the complete library from one core alone, but a uniform expanded library can dilute useful parents.
The selected experiment compares that tradeoff at degrees 24 and 30, beyond the already inspected degree-18/20 census.
The [existing source-backed reconstruction](../computations/programs/Yin_J_G0149/readme.md#core-coverage) already places these degrees within the published primitive-irreducible classification through degree 44.
This is therefore a bounded mechanism calibration within an externally classified range; that original exhaustive classification is not rerun here.
The [inspected primary minimum-search statement](../audits/literature/MV226/Yin_U001.md#mv226-secondary-results-and-updates) reports coverage through even degree 54, so a later counterexample campaign must address primitive noncyclotomic core degrees beyond that reported coverage.
Cyclotomic padding and substitutions preserve the seed measure and do not themselves supply that new-core step.
The [independent implementation finding](../audits/reviews/Yin_R_G1111_v8.md#archive-implementation-review) and [retention finding](../audits/reviews/Yin_R_G1111_v8.md#archive-retention-review) pass for the declared implementation and bounded controls.
The unchanged thirty-run protocol has now been executed, with observations retained in the [completed J156 comparison](../computations/programs/Yin_J_G0156/readme.md#archive-comparison-results).
The implementation findings supply no independent review of those later performance observations.

### Common domain, seed and proposal law

Use the same reciprocal height-four box \(\Omega_D\), complete-measure evaluator, 128-bit arithmetic, ranking tolerance, cache policy and strict whole-output target \(1<M<6/5\) as before, now with \(D\in\{24,30\}\).
Every run has the same explicitly supplied normalized Lehmer core as reference information.
This is a reference-seeded comparison, not an experiment learning without known inputs.
The supplied seed does not count as a discovery, and every evaluated proposal still goes through the common evaluator and cache rules.

The three arms are fixed bias, direct-template archive and cyclotomic-closure archive.
The fixed arm keeps the existing fixed coefficient law and does not use templates for generation.
The other two arms each draw uniformly from the whole box with probability \(1/10\); otherwise they choose a stored core uniformly, choose one of its stored distinct templates uniformly, and perform the previously specified uniform \(k\in\{1,2,3\}\), distinct-coordinate, independent \(\pm1\) mutation.
A box exit returns the unchanged parent, without rejection resampling.

For a core \(F\) of degree \(d\), the direct archive initially constructs every height-four sparse completion
\[
 F(\varepsilon z^k)(1+z^{D-kd})\quad(D>kd),
 \qquad F(\varepsilon z^k)\quad(D=kd),
\]
for \(\varepsilon=\pm1\) and \(1\le k\le\lfloor D/d\rfloor\), removing exact duplicate templates.
It also retains every distinct exact template actually encountered as a certified whole target for that core.
For a newly encountered core the successful template is retained even if none of its sparse completions meets the height bound.
The closure archive instead constructs the complete height-four class \(F(\varepsilon z^k)C(z)\), with all reciprocal cyclotomic products \(C\) at the remaining degree.
It verifies that each encountered target template belongs to its constructed class.
Only completed whole-target evaluations can add a core or an observed template; factor-only targets, approximate scores and incomplete work never update either archive.
Core selection stays uniform, so repeated hits cannot directly increase a core's selection weight.
Neither arm fits independent coordinate marginals or imports the second target's coefficients.

Charge initial template construction, later closure or direct-archive updates, all sampling, root certification, factorization, cache access and duplicate handling to the run budget.
Commit an evaluation and its archive update together; work still incomplete at the deadline cannot enter the measured yield or a retained final archive.
Do not load precomputed closure outputs to remove their cost from a run.
The deterministic preparation supplies 1170 and 5532 initial closure templates at degrees 24 and 30, respectively; it supplies no discovery credit or timing allowance.

### Allocation and decision rule

Run each degree, each of the three arms and seeds 20 through 24 once, for 20 seconds per run: 30 serial runs and 600 seconds of formal sampling budgets.
Within each degree and seed, rotate the arm order by the degree-index-plus-seed-index modulo three, using the base order fixed, direct, closure.
Preserve all failures, incomplete proposals and initialization overhead under the existing deadline contract.
Any separate implementation control is labelled as such and excluded from this formal comparison.

The primary comparison counts distinct certified whole-output values in \(1<M<6/5\) beyond the supplied Lehmer value, with the time to the first such value censored at the budget.
Report Lehmer recovery separately, the second locally known core separately, every other core relative to the actual local reference set, and every certified value strictly below the Lehmer seed enclosure.
For this classification, the explicit default local catalog is the two certified core groups in [the retained degree target partition](../computations/programs/Yin_J_G0156/inputs/degree_core_mass_states.json); it is used only for reporting, while the external classification scope remains with the source-backed reconstruction above.
Different cores count as distinct values only after the common certified separation or exact comparison; unresolved equality classes remain explicit.
An unfamiliar local core is not called a literature-new result before its actual comparison with published records.
Keep factor-only finds separate and retain their parent coefficients, whole measure and charged cost.
Also report distinct template counts by core, direct versus generated representation counts, archive-update costs, neutral fraction, repeated samples, unresolved evaluations, completed evaluations and wider-threshold yields.

The allocation screen requires all 30 runs to be valid, closure to be no worse than each comparator in at least four of five paired seeds at each degree, and to improve on both comparators in at least three of five paired seeds at at least one degree.
Here no worse means at least as many distinct nonseed target values; the three strict wins must occur against both comparators on the same paired seeds.
A strict improvement means more distinct nonseed target values, or the same positive count with an earlier first nonseed hit; a zero-zero comparison is never an improvement.
This is a finite exploratory allocation rule, not a statistical significance claim or an assumption that these previously inspected mechanisms generalize.
If the screen fails, retain its actual scope and diagnose the concrete representation or mutation limitation before increasing the same experiment's budget or degrees.
Even a passed screen establishes only a search mechanism at the tested degrees; the original Task still needs an integer family with arbitrarily small positive total measure, or a proof of a uniform positive gap.

All thirty runs are valid, and the observed screen passes: closure has five count nonlosses against each comparator at each degree, with three simultaneous strict wins at degree 24.
The three successful runs recover the same known degree-eighteen value, while all degree-30 nonseed yields are zero.
The [independent actual-result finding](../audits/reviews/Yin_R_G1111_v9.md#archive-results-review) verifies these observations, full retained evidence and the finite screen.
Preparation for the next search therefore concerns genuinely new primitive cores beyond the reused degree-54 minimum range, rather than further known-core recovery trials alone.
The separate [DP parent preparation](../computations/programs/Yin_J_G0156/parent_sampling.md) supplies a possible larger-degree generator; its unchanged-measure parents and finite feasibility observations do not yet supply a new-core mutation law or result.

<a id="primitive-core-comparison"></a>
## Frozen degree-56 primitive-core comparison

The next selected question is whether a larger range of neutral representations supplies useful mutations into genuinely primitive degree-56 integer polynomials, beyond the reused even-degree-through-54 minimum statement.
The [actual degree-24 transition](../computations/programs/Yin_J_G0156/readme.md#archive-comparison-results) changes the known core but retains a neutral factor and ends at degree eighteen.
It motivates checking each reduction explicitly instead of treating the proposed total degree as the discovered core degree.
The [independently reviewed DP law](../audits/reviews/Yin_R_G1111_v10.md#parent-law-review) removes complete-template enumeration as a prerequisite for generating larger parents, while leaving rejection cost and useful mutations unresolved.
The [dedicated implementation and bounded controls](../computations/programs/Yin_J_G0156/primitive_core_sampling.md) have passed the [independent composition finding](../audits/reviews/Yin_R_G1111_v11.md#primitive-implementation-review) and [corrected-retention finding](../audits/reviews/Yin_R_G1111_v11.md#primitive-retention-review).
The unchanged formal comparison has [completed all ten valid runs](../computations/programs/Yin_J_G0156/primitive_core_sampling.md#primitive-comparison-results), verified by its [independent actual-result finding](../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review) and separate [retention](../audits/reviews/Yin_R_G1111_v12.md#primitive-results-retention-review) and [interpretation](../audits/reviews/Yin_R_G1111_v12.md#primitive-results-interpretation-review) findings.

### Fixed proposal laws and budget

Use the reciprocal height-four box at \(D=56\), the same complete evaluator, 128-bit arithmetic, ranking tolerance and exact-polynomial cache size 4096.
The sole supplied core is the normalized Lehmer polynomial, freshly certified within each run.
The two arms are `direct` and `dp_closure`.
Both use probability one tenth for a uniform whole-box proposal and otherwise draw a parent, choose uniform \(k\in\{1,2,3\}\), choose a uniform set of distinct free coordinates, and assign independent uniform unit signs in the same order as the archive comparison.
An out-of-box mutation returns its unchanged parent without a redraw.
The direct parents are the distinct sparse completions already defined above, chosen uniformly.
The DP arm uses the reviewed raw multiset law and final height rejection, with at most 4096 raw attempts to obtain each parent.
Failure to obtain a parent within that cap is retained as an incomplete parent-supply stop, invalid for full-budget eligibility; it supplies no substitute parent, uniform fallback or discovery.
No core or template is added during this experiment, so the comparison isolates the initial parent-generation mechanisms without online feedback or a second known core.

Use seeds 30 through 34, twenty seconds per arm and seed, for ten serial runs and 200 seconds of formal sampling budgets.
At seed index \(j\), rotate the base order `direct`, `dp_closure` by \(j\bmod2\).
Charge startup, seed certification, initial direct construction or DP setup, every rejected raw parent, mutation, diagnostics, factorization, complete root certification, cache handling and retained-data writes to the same clock.
Preserve the hard supervisor and predeadline evaluation-commit boundary.
The ideal parent kernel and the hard-censored completed collection have distinct probability scopes; make no conditional-uniform claim for completions selected by the hard deadline.
Use separate labelled implementation controls before the formal identities, without changing the formal budgets or seeds from their results.

Retain the exact RNG and rank inputs for every started DP raw attempt, its acceptance or rejection if completed, and its actual pending state if interrupted before a parent is constructed.
Preserve final incomplete parent-generation work even when no full mutated polynomial was proposed.
For a generated whole proposal, preserve the exact coefficients, parent representation and mutation, whole/factor certificates and original charged cost at the applicable committed or incomplete scope.
Portable replay must reconstruct rejected and accepted parents, proposals and retained retry inputs without repeating historical timing.
Numerical uncertainty, arithmetic failure, parent-attempt exhaustion and an ordinary deadline remain distinguishable outcomes.

### Exact core diagnostics and discovery metrics

The primary discovery count is distinct certified whole-output values in \(1<M<6/5\) from polynomials that are themselves noncyclotomic and irreducible of degree 56 and have exponent gcd one.
Keep the existing conservative interval-separation rule and explicit unresolved value equalities.
The supplied Lehmer value is a reference in both whole and primary value ledgers and receives no discovery credit; distinct primitive coefficient cores and unresolved same-value cases remain separately visible.
Also retain all whole targets, known-core recoveries, values strictly below the Lehmer seed, and separate small factors with their complete parent measures and costs.
A whole target outside the primary degree-56 class is still an exact observation and cannot be discarded merely because it fails that class test.
The local two-core catalog is used only for post-run reporting, with literature novelty requiring the actual external comparison.

Record the smallest certified positive whole measure among the primitive degree-56 outputs, its exact witness and first occurrence, and distinct such cores with certified \(6/5\le M<13/10\).
A threshold overlap remains unresolved rather than being rounded into that near-miss interval.
Report raw and unique candidate counts, duplicate/cache/neutral rates, actual parent attempts and rejections, generation and evaluation costs, and the branch of each useful output.
No improvement in house, normalized log measure or aggregate noncyclotomic degree substitutes for these full-measure metrics.

For a template parent \(P=F(\varepsilon z^j)C\) and actual mutation \(\Delta\), retain the exact neutral polynomial \(C\) and \(G=\gcd(C,\Delta)\).
Since \(G\) divides both \(P\) and \(\Delta\), it divides the child, so the child's noncyclotomic total degree is at most \(56-\deg G\).
An unchanged-parent boundary return has \(\Delta=0\) and is covered by the same identity.
This is a diagnostic and does not reject or redraw a proposal; uniform whole-box draws have no supplied parent and record this diagnostic as inapplicable.
The condition \(G=1\) alone neither excludes newly occurring neutral factors nor ensures irreducibility or exponent gcd one.

Distinguish the noncyclotomic product with multiplicities, the existing compressed/sign-normalized whole core, and the individual irreducible factors after their own exponent compression and sign normalization.
The compressed whole core can be reducible, so its degree alone cannot establish the primary class.
The committed exact factorization determines whether a polynomial is genuinely noncyclotomic primitive irreducible degree 56.
Cyclotomic irreducible degree-56 outputs remain neutral observations and are excluded from that structural class as well as from positive-measure yields.
Report retained old neutral factors, additional neutral factors, exponent compression and noncyclotomic reducibility separately; these diagnostics can overlap and are not asserted to form a disjoint partition.

### Allocation after this bounded test

All ten declared identities must be valid before making a full-budget comparison, with incomplete or failed cases retained and diagnosed without automatic reruns or substituted seeds.
Compare the primary yields and certified primitive minima at their actual finite scope; a zero-zero outcome is not an improvement or a significance result.
Any certified below-Lehmer output or factor receives priority verification against the original exact input and full measure.
If primitive degree-56 near-misses below 13/10 occur, use their actual witnesses to select a separately bounded local-descent test before further degree enlargement.
If residual neutral factors or compression account for the failure to reach the primary class, the next possible revision is an explicitly defined necessary-condition mutation law whose changed parent weights and rejected costs are recorded.
If the primary class is reached but its measures remain large, merely enlarging the template collection, mutation radius or runtime is not the selected next step.
Neither a finite new value nor a successful search law supplies G0001's missing family with positive complete logarithmic measures tending to zero.

<a id="primitive-support-boundary"></a>
### Fixed-support boundary for degree extension

An extension of the direct sparse-parent branch that keeps the same nine-term Lehmer core, a two-term neutral completion and at most three reciprocal-coordinate mutations has at most \(9\cdot2+2\cdot3=24\) nonzero terms in every whole output.
Collisions or a central-coordinate move can only reduce this upper bound.
The accepted [DS17 fixed-support theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) therefore supplies a positive total-logarithmic-measure floor depending only on 24 for this branch across all degrees.
This is a direct application of the existing source input, not a new uniform-gap theorem or an effective exclusion at \(6/5\).
It excludes degree enlargement alone as a shrinking-positive-measure mechanism for that branch, while leaving finite new small values possible.
The uniform-box component and the DP branch with growing actual support are outside this fixed-support deduction.

<a id="primitive-root-cost-follow-up"></a>
### Selected follow-up after the formal outcome

The completed comparison produces 4521 direct and 2538 DP primary occurrences, but no primitive near-miss below \(13/10\) and no nonseed whole value below \(6/5\).
Its primitive minima are approximately 1.3606107463 and 1.6951471325 respectively, so the present failure is not simply an inability to reach a primitive degree-56 output.
The [independent actual-result finding](../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review) verifies these observations; the root-cost diagnostic below has its separate scope.
No automatic degree, mutation-radius or runtime enlargement is selected.

The completed diagnostic uses only the retained original parents, actual mutations and complete root certificates, without new sampling or root solves.
Within matching substitution index and actual nonzero mutation size, first examine \(j=1\), \(G=1\) strata and separate endpoint multiplicities and primary classification.
Compare internal neutral trace repetition, certified exterior and nonreal exterior root counts, complete measures and the contribution of the largest individual exterior roots.
Treat balls meeting modulus one as unresolved at that classification, not as proved circle roots, and keep uncommitted observations outside historical yield.
The comparison is a post-hoc mechanism diagnostic, with no new performance threshold or causal conclusion.
The [completed analysis](../computations/programs/Yin_J_G0156/primitive_root_diagnostics.md) preserves every committed denominator and finds that repeated neutral trace roots accompany larger nonreal exterior counts in its matched DP groups, while trace-simple parents also fail to reach a near-miss.
Its actual two arm minima retain respectively eight and eleven certified exterior roots, with the remaining unit-boundary classifications kept unresolved.
The [independent interface finding](../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-implementation-review) and [descriptive-result finding](../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-results-review) verify the full extraction, multiplicities, printing path, reported statistics and interpretation limits.
This association does not by itself select a squarefree-parent arm.

Removing neutral multiplicity alone is not a sufficient new mechanism: the direct completion already has simple uniformly spaced circle roots, while the attributed [Lehmer cyclotomic perturbation](../audits/literature/MPV98/Yin_U001.md#mpv98-u001) has a useful trace double root.
The [existing central-descent theorem](../claims/Yin_C_G0414_v1.md#statement) and [critical-value slice](../ledger/Yin_L_G0449_v1.md#constant-coefficient-critical-value-slice) retain the actual simultaneous sign and integer-step requirements.
Their source and proof scopes do not supply a nonzero integer mutation satisfying all those requirements at growing degree.
Any later sign-conditioned law must address that joint integer feasibility and full exterior cost on its actual inputs; a continuous neighborhood, one root radius or a larger parent collection is insufficient.

<a id="primitive-fixed-cell-test"></a>
## Selected fixed degree-56 root-cell test

The next bounded investigation asks whether joint changes of all 28 free reciprocal coefficients can preserve the required root configuration while leaving both known target-value fibers.
It reuses the interpolation and integer-search methods of [C876](../claims/Yin_C_G0876_v2.md#argument) and [J144](../computations/programs/Yin_J_G0144/readme.md#degree64-cell).
Their earlier exclusion concerns a different fixed degree-64 cell with a nonreal trace pair and supplies no exclusion of the cell selected here.
This is one finite root-position experiment under the existing route, not a new strategy or a new integer-supply theorem.

Use the actual parent of the DP seed-32 proposal-448 minimum, after applying \(z\mapsto-z\) to the whole product:
\[
 P_0(z)=F(-z)\Phi_6(z)\Phi_4(z)\Phi_{14}(z)
                 \Phi_{12}(z)\Phi_{15}(z)\Phi_{30}(z)\Phi_{60}(z),
\]
where \(F\) is the fixed canonical Lehmer polynomial in the [formal result](../computations/programs/Yin_J_G0156/primitive_core_sampling.md#primitive-comparison-results).
This post-hoc parent choice is fixed before the new search and is not an additional arm or preselected success metric of the completed comparison.
Its trace has 27 simple roots in \((-2,2)\) and one root in \((2,61/30)\).
Preparation must reconstruct the exact parent and this shape, choose rational separators by one declared deterministic rule, and freeze the resulting exact input before the formal test.

Use \(C_k(z+z^{-1})=z^k+z^{-k}\) for \(k\ge1\), with the constant basis element one, and
\[
 Q=C_{28}+a_1C_{27}+\cdots+a_{27}C_1+a_{28},
 \qquad a_i\in\mathbb Z\cap[-4,4].
\]
There are 26 internal separators between the 27 parent inner roots, together with \(s_0=-2\), \(s_{27}=2\) and \(s_{28}=61/30\).
Impose all 29 strict signs \((-1)^iQ(s_i)>0\), using exact integer rows after clearing denominators.
These signs place all 28 trace roots in disjoint open real intervals, with exactly one above two, and therefore guarantee the complete bound \(1<M(z^{28}Q(z+z^{-1}))<6/5\).
The existing interpolation argument gives an exact open simplex with vertices \(\prod_{j\ne i}(t-s_j)\), so joint coefficient bounds can use all of these vertices.
The input and sign controls must admit the original parent and reject the actually observed central \(+1\) child.

The finite question excludes divisibility of \(Q\) by each known positive-exterior trace core, of degrees five and nine respectively.
Determine both traces from the actual integer core polynomials and verify the sign convention during preparation.
Each nonzero-remainder condition is a finite disjunction of affine integer inequalities, with every introduced bound justified on the coefficient box.
Excluding only the original parent vector would leave its other neutral representations and does not answer this question.
The [fixed exact input and implementation](../computations/programs/Yin_J_G0144/trace56_cell.md) belong to J144, with exact references to the J156 parent input and complete evaluator.
Their [independent preparation finding](../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-preparation-review) and [implementation finding](../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-implementation-review) verify the complete mathematical reduction, fixed model, exact checks and candidate-retention boundary.
The [separate resultant bound](../computations/programs/Yin_J_G0144/trace56_resultant.md) fails to exclude the same cell at its independently checked finite scope, so it does not dispose of this integer-feasibility test.

The selected formal test has one 120-second total wall budget from prelaunch, one solver thread, seed 56003 and at most 100000 solver nodes.
Charge initialization, model construction, numerical search, candidate reconstruction, exact sign and remainder checks, factorization, complete-root certification and result writes to this clock.
Input preparation and bounded implementation controls precede this formal identity and receive no discovery or performance credit.
Do not move separators, switch parents, enlarge the box or automatically rerun or extend a failed or timed-out test.
Floating-point solver feasibility is only a candidate proposal; certify the exact integer input, all signs, both remainder conditions and complete original-polynomial measure before accepting a target.
Floating-point infeasibility and a timeout are unresolved outcomes unless a separate exact exhaustive certificate establishes the finite exclusion.
Keep any predeadline unverified candidate as an incomplete input; later verification supplies mathematical evidence without retrospective on-time yield.

A certified irreducible degree-56 output would establish one genuine primitive success of this root-position mechanism.
A certified output with a smaller unique noncyclotomic factor would establish a new value relative to the two-core reference, with the actual factor degree reported separately and literature novelty still requiring comparison.
An exact exclusion would close only this selected cell and box; an unresolved run would not justify automatic expansion.
Either outcome returns to the joint integer-feasibility question before another allocation.
For G0001, the first missing premise is still a nonneutral integer input in the desired region, and the decisive later premise is a family in growing degree whose permitted exterior bound tends to one.
A finite success, even below Lehmer, supplies neither that family nor the unrestricted zero-gap conclusion; failure of this Salem-shaped cell does not cover general nonreal trace configurations.

The [actual single numerical test](../computations/programs/Yin_J_G0144/trace56_cell.md#formal-result) returned `Infeasible` after 13013 reported MIP nodes and approximately 4.175 seconds from prelaunch, without an incumbent, returned candidate or complete-root call.
The [independent actual-result finding](../audits/reviews/Yin_R_G1111_v15.md#fixed-cell-result-review) verifies the full observation, native preservation and unresolved interpretation, separately from the adopted preparation and implementation findings.
The numerical result alone left the finite arithmetic question unresolved; the separate exact certificate below supplies its later exclusion.
No repetition or enlargement of the numerical experiment is selected.

<a id="primitive-cell-exact-certificate"></a>
### Selected exact verification of the same finite region

The numerical run reached its negative status well within both declared caps, but that status does not discharge the finite integer question.
The selected exact-certificate attempt used the already established [C876 prefix separation and coordinate bounds](../claims/Yin_C_G0876_v2.md#argument), with the same 29 vertices, original strict signs and height-four box.
This can distinguish an actual absence of new-value integer points in this region from a merely numerical negative answer.
It changes neither the parent nor the region and is not another performance arm, a repetition of the MIP run or credit within its original budget.

Use integer prefix enumeration with exact vertex extrema and box maxima.
Floating linear programming may suggest an integer separating normal or coordinate bound, but every pruning step must follow from the exact rational inequalities; an inadequate suggestion falls back to a valid wider branch.
At every complete coefficient vector, check the original strict integer sign rows and both exact remainder vectors.
An accepted integer vector stops the generation attempt and is retained for the separate complete-polynomial certification and actual factor-degree check.
Only complete coverage with every surviving strict-cell leaf in one of the two known-value fibers can establish the finite exclusion.

Authorize one generator attempt with at most 50000 internal prefixes, one thread and a 120-second total generation wall budget including initialization, LP suggestions, exact checks and writes.
Retain the fixed mathematical input, complete prefix records and any unfinished frontier so that an integer-only verifier can reconstruct the actual coverage without the numerical solver.
Use the remaining time for each LP and a hard supervisory boundary, preserving partial evidence on interruption or failure.
Preliminary small controls are separate from that one proof-generation identity.
There is no automatic second attempt or domain enlargement after a cap, failed hint, numerical error or incomplete certificate.
The existing [J144 computation group](../computations/programs/Yin_J_G0144/readme.md#degree56-cell) owns the program, certificate and actual result.
An independently verified complete exclusion would close this cell and coefficient box only, while an incomplete certificate would leave exactly its unprocessed region unresolved.

The [completed tree](../computations/programs/Yin_J_G0144/trace56_tree.md) has 1504 internal prefixes, one full leaf and an empty frontier.
The [independent mathematical finding](../audits/reviews/Yin_R_G1111_v16.md#fixed-cell-exact-tree-review) proves that the entire closed simplex in the height-four integer box contains exactly the original parent, which belongs to the Lehmer fiber.
The [independent evidence finding](../audits/reviews/Yin_R_G1111_v16.md#fixed-cell-exact-tree-evidence-review) checks the whole native tree and actual bounded generation separately from the earlier MIP.
Thus this joint-coefficient region supplies no new integer input; concentrating a different probability law on the same filtered cell cannot change that fact.
The exclusion covers only the declared fixed nodes and box.

<a id="allocation-after-fixed-cell"></a>
### Allocation after the completed finite tests

On 10 November 2026 the main agent deferred further sampling campaigns under S10 while S1 and S4 continue the unrestricted research.
The primitive comparison reached its intended degree class but did not control the complete exterior cost, and the subsequent fixed-cell test has now settled its local integer-supply question negatively.
The bounded strategy comparison found no developed replacement from the inspected interlacing, cyclotomic-delay or two-transvection mechanisms.
The [MS05 construction interface](../audits/literature/MS05/Yin_U001.md#ms05-arbitrary-distinct-prime-construction) retains the [positive exterior expense](../audits/literature/RY26/Yin_U001.md#exterior-root-measure-expense), and [L133 v2](../ledger/Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) already excludes the proposed boundary-log cancellation of two unrestricted cyclotomic blocks.
The [positive-lattice two-transvection theorem](../claims/Yin_C_G0885_v2.md#decision-positive-lattice-two-transvection-gap) separately closes that family as a source of positive measures tending to one, even when the positive integral lattice and its isometry vary.

Resume this sampling allocation when a concrete generator, arithmetic support or joint-root mechanism supplies a discriminating new question beyond changing degree, runtime, a nearby fixed cell or the representation count of known cores.
A finite discovery test need not first prove an asymptotic construction, but its evaluation must retain original complete measures, actual primitive degree, distinct values and all costs.
For any claimed shrinking-measure family, nonneutrality and a vanishing bound on the full exterior contribution remain separate obligations; original support growth alone does not rule out a bounded-support cyclotomic completion.
This is an allocation pause for the child strategy, not a pause or completion of G0001.
