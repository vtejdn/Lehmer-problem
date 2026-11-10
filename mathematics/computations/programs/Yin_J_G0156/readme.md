---
author: Yin
---
# A controlled comparison of integer sampling laws

## Question and scope

Implement the [S10 first experiment](../../../strategies/Yin_S_G0010.md#first-experiment) under the [resumed G0001 contract](../../../tasks/Yin_T_G0001_v1.md#decision-resume-adaptive-sampling-2026-11-09).
Compare uniform, fixed-biased and adaptive sampling in the same reciprocal integer coefficient boxes at degrees 14, 18 and 20.
The primary target is distinct certified values in \(1<M<6/5\), with complete computation costs and repeat handling.
The implementation has passed the controls and short degree-14 calibration below.
The [independent implementation review](../../../audits/reviews/Yin_R_G1111_v1.md#sampler-implementation-review) covers the frozen sampler, complete-measure arithmetic, timing and repaired failure accounting.
The [separate census finding](../../../audits/reviews/Yin_R_G1111_v1.md#baseline-census-review) independently reproduces the exact finite-box baseline.
The frozen 45-run pilot is complete, with all prescribed identities and budgets valid.
Its observed outcomes are retained separately from the shorter calibration and later mechanism controls below.
The [independent completed-pilot review](../../../audits/reviews/Yin_R_G1111_v3.md#pilot-results-review) verifies all 45 journal summaries and retained witnesses, the result tables and the failed continuation screen.
Its separate findings verify the [15 post-run mass diagnostics](../../../audits/reviews/Yin_R_G1111_v3.md#pilot-law-mass-review) and [pair-pseudocount bound](../../../audits/reviews/Yin_R_G1111_v3.md#pair-pseudocount-review); the later reduced-strength control remains outside those findings.
The subsequent [reference-seeded archive comparison](#archive-comparison-results) and [uniform-parent preparation](#uniform-parent-preparation) retain their own completed results and independent reviews.
The [degree-56 primitive-core protocol](../../../strategies/Yin_S_G0010.md#primitive-core-comparison) has an independently reviewed implementation and [completed formal results](primitive_core_sampling.md#primitive-comparison-results), verified by the [separate actual-result finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review).

## Files

| File | Role |
| --- | --- |
| [sampler.py](sampler.py) | Exact sampling laws, full-root certificates, bounded worker/supervisor, summaries, and separate replay. |
| [check_failure_boundary.py](check_failure_boundary.py) | Regression checking that failed or early runs stay visible and cannot become a complete pilot or enter valid-run comparisons. |
| [checks/independent_pilot_review.py](checks/independent_pilot_review.py) | Retained reviewer checks of fixed pilot observations and witnesses, with a separate optional reconstruction of the original journals. |
| [law_mass_diagnostic.py](law_mass_diagnostic.py) | Separate post-run replay of committed updates and approximate conditional target probabilities under the resulting laws. |
| [prior_strength_control.py](prior_strength_control.py) | Exact fixed-elite comparison changing only the pair pseudocount total from 81 to 1, with no new proposals or root calculations. |
| [prior_strength_live.py](prior_strength_live.py) | Separate degree-14 live comparison of fixed, original adaptive O and reduced-pair-prior A, with its own seeds, dispatch and completeness screen. |
| [prior_strength_live_checks.py](prior_strength_live_checks.py) | Exact update, actual child-process dispatch, deadline, failure and allocation-screen controls for the separate live comparison. |
| [prior_strength_live_export.py](prior_strength_live_export.py) | Retain actual live observations and compact certificates, with exact links from separate factors to their committed whole outputs. |
| [degree_validation.py](degree_validation.py) | Separate twenty-run degree-18/20 comparison of fixed bias and the unchanged A law. |
| [sampling_runtime.py](sampling_runtime.py) | Explicit degree/variant child dispatch and bounded observation bookkeeping for new comparisons, reusing the frozen evaluator. |
| [degree_validation_checks.py](degree_validation_checks.py) | Actual degree/seed/block dispatch, exact-law and completeness controls for the twenty-run comparison. |
| [checks/independent_degree_review.py](checks/independent_degree_review.py) | Independent checks of the new degree/runtime/identity/report interfaces, including startup failure. |
| [checks/independent_live_review.py](checks/independent_live_review.py) | Independent exact arithmetic, dispatch and validity checks before the live experiment. |
| [checks/independent_live_results.py](checks/independent_live_results.py) | Independent reconstruction of the actual live journals, sampling laws, counts and certified results. |
| [baseline_mass.py](baseline_mass.py) | Exact offline box counts and uniform/static-law target probabilities, using the [J147 cover](../Yin_J_G0147/newton.cjs) and the [J144 Graeffe transform](../Yin_J_G0144/pilot.py). |
| [inputs/calibration_witnesses.json](inputs/calibration_witnesses.json) | Exact degree-14 polynomial recovered during the short adaptive implementation check, retained for independent replay. |
| [inputs/pilot_comparison.json](inputs/pilot_comparison.json) | All 45 observed run summaries, times, costs, compact whole-value certificates, separate factor records and unresolved equalities. |
| [inputs/pilot_witnesses.json](inputs/pilot_witnesses.json) | The 1331 exact polynomial inputs needed to replay the retained pilot discoveries, best outputs and unresolved equality cases. |
| [inputs/pilot_law_mass.json](inputs/pilot_law_mass.json) | The 15 post-run conditional target-mass diagnostics, explicitly approximate and separate from discovery yield. |
| [inputs/prior_strength_elites_d14.json](inputs/prior_strength_elites_d14.json) | The 13 checked elite batches from the separate 3432-proposal calibration prefix, retaining 337 seven-coefficient vectors and their native source parameters. |
| [inputs/prior_live_comparison.json](inputs/prior_live_comparison.json) | All fifteen observed live outcomes, times, costs, compact whole certificates and separate-factor associations with their actual parent outputs. |
| [inputs/prior_live_witnesses.json](inputs/prior_live_witnesses.json) | The 449 exact polynomial inputs retained for whole-output, factor and parent-output replay in the live comparison. |
| `mathematics/computations/outputs/Yin_J_G0156/` | Ignored event journals, summaries, certificates, dependency installation, and replay results. |

The sampler never reads the baseline census, reference target lists, or retained witnesses when proposing or adapting.
The controls in `self-test` are available only through that separate command.

## Arithmetic and fixed settings

All native polynomial coefficient arrays are ascending.
The free list is \((a_1,\ldots,a_n)\), so the constructed array is `[1, *a, *reversed(a[:-1]), 1]`.
All three arms use the exact S10 box and their declared laws, with no chamber, resultant, irreducibility, or root-type filter.
The fixed categorical weights on \(-4,\ldots,4\) are \((1,2,4,8,16,8,4,2,1)\), whose sum is 46.
The exploration choice uses an exact integer draw with probability \(1/10\).
Adaptive pair and singleton distributions are represented by integer weights and sampled by exact integer cumulative sums.
The pseudocount and smoothing update uses rational arithmetic through common integer weights, so it implements \(4/5\) of the old law plus \(1/5\) of the smoothed empirical law without floating probability drift.
After each 256 proposals, only resolved positive scores from that batch are eligible, and one representative per normalized core is selected by score followed by lexicographic free-coefficient order.
The elite size is the ceiling of one tenth of the number of representatives.
An empty eligible batch leaves the law unchanged.

Every fresh candidate is factored exactly with FLINT, and the factor product is reconstructed and checked against the original polynomial.
Exact cyclotomic factors contribute measure one.
Every other irreducible factor is evaluated using all its Arb root balls and every multiplicity at 128-bit precision.
A root modulus ball meeting one contributes its union with \(\{1\}\), which encloses \(\max(1,|\alpha|)\); no uncertain root is dropped.
The complete product supplies certified whole-measure bounds, strict rational threshold decisions, and a binary64 midpoint approximation to \(\log M\) for ranking.
Ranking requires a log-measure ball radius below \(10^{-12}\) and a whole-measure ball strictly above one; otherwise the score is unresolved and cannot enter an elite.
Every reported threshold hit and best value therefore has a full-product certificate, without a preliminary floating exclusion.
Integer dyadic interval endpoints are retained as `[mantissa, exponent]`, meaning \(\text{mantissa}\,2^{\text{exponent}}\).
The certificate algorithm adapts the full-root treatment in [J155](../Yin_J_G0155/affine_milp.py), including multiplicities and root balls that meet the unit circle.

Core normalization removes all cyclotomic factors, repeatedly compresses exact power substitutions, and chooses the lexicographically smaller monic **descending** coefficient list under \(z\mapsto-z\).
The stored normalized array remains ascending.
Equal normalized cores prove equal measures through these operations.
Different cores count as different values only when their certified intervals are disjoint; an overlap remains an explicitly retained unresolved equality.
Small irreducible factors are reported separately and never increase a whole-output hit count.
A 4096-entry least-recently-used cache is reset at every run and is identical across arms.
Exact repeated-proposal and repeated-positive-core counts do not depend on cache retention.

## Time and output accounting

A supervisor starts the run clock before launching one worker and terminates that worker at the requested cap, which cannot exceed 60 seconds.
Worker initialization, proposal generation, rejected or unresolved work, exact factorization, root certification, normalization, caching, duplicate handling, adaptive updates, and result-journal writes all occur inside that cap.
The worker flushes each completed evaluation before writing its completion marker.
Only evaluations whose completion markers precede the deadline contribute to any reported yield.
A pending proposal or truncated final journal record remains incomplete; no post-deadline certification contributes to experimental yield.
Worker failures and premature exits remain explicit in persisted summaries and aggregate seed outcomes.
They are excluded from comparison statistics and matched-seed screening, and a pilot with any such run is incomplete.
An absent-hit censor for a failed or early run uses its observed duration, not the requested 60-second budget.
Process termination and post-run aggregation can add small separately reported wall-clock overhead, but that aggregation performs no polynomial evaluation, adaptation, or certification.
Dependency-import setup is reported separately, while the worker's own import/startup cost is included in its run budget.
Stage totals cover committed work; the full cap also charges interrupted work, unclassified overhead, and I/O.

Each journal records exact proposed coefficients, committed outcomes, update elites, retained certificates, and completion times.
The summary reports total proposals, completed proposals, fresh completed evaluations, cache hits, neutral mass, unresolved cases, repeated proposals and cores, raw hits, interval-separated values, and first-hit time or censoring.
Raw hit rates are supplied both per proposal and per completed proposal.
The separate factor table records factor discoveries without changing the whole-output table.
`report` aggregates independent runs into all seed outcomes, medians, ranges, and the held-out matched-seed comparisons; it makes no independent-Bernoulli assumption about adaptive samples.
Selected exact witnesses can be exported to the tracked input home for later verification.
`replay` and `verify-witnesses` are separate checks and never add discoveries to the original capped runs.

## Reproduction

Run from the repository root with Python 3.14.7 and `python-flint==0.9.0` available to the interpreter.
The tested local setup installs the single package under `mathematics/computations/outputs/Yin_J_G0156/packages` and makes it available through `PYTHONPATH`; a standard environment with that package is also sufficient.
The offline baseline additionally requires Node.js for the existing J147 enumerator.
The following are normalized reproduction commands, with `python` denoting the actual selected interpreter.

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py self-test
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/calibration_witnesses.json
python -B mathematics/computations/programs/Yin_J_G0156/baseline_mass.py 14 18 20
```

The two pilot comparison commands below have been executed under the active Task's continuing authorization and resource monitoring.
Run degree 14 first, review it, and keep the same program and settings before starting degrees 18 and 20.

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py compare --degrees 14 --seeds 0 1 2 3 4 --seconds 60 --label pilot
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py compare --degrees 18 20 --seeds 0 1 2 3 4 --seconds 60 --label pilot
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py report --label pilot
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py export-witnesses --label pilot --output mathematics/computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json
```

The two comparison commands represent 900 and 1800 seconds of capped experiment time, respectively.
For degree index \(j\in\{0,1,2\}\) and seed \(s\), arm order rotates the list `uniform, fixed, adaptive` by \((j+s)\bmod3\).
Every arm and seed starts from its declared initial law and an empty cache.
Existing run outputs are not overwritten; a different label is required for a distinct comparison.
The final two commands are separate replay preparation and verification, outside the experiment's discovery budget.
The optional `run --max-proposals` parameter is for implementation controls and must remain zero for the declared pilot.
With a wall-clock stopping rule, the random seed fixes the proposal process but does not fix the number of completed proposals; the exact retained coefficients support replay without pretending the runtime prefix is deterministic.

## Controls and calibration

The self-test passed exact neutral products including repeated cyclotomic roots, the Lehmer polynomial, J147's nonunit control, a repeated exterior-root control, cyclotomic padding, power substitution, sign normalization, conservative value overlap, singleton blocks, and exact adaptive pseudocount/smoothing arithmetic.
The repeated exterior-root control \((z^2-3z+1)^2\) has measure between 6.854 and 6.855, checking that multiplicities and all exterior factors enter the product.
Serial 512-proposal degree-14 checks at seed 1 completed for all three arms, and the adaptive arm performed exactly two updates.
Those controls exported 15 exact witnesses and successfully recomputed all 15 certificates.
A separate replay recomputed all 23 distinct retained polynomial certificates from the short adaptive timing check.

| Degree-14 timing control | Budget | Completed proposals | Fresh evaluations | Completed unresolved scores or thresholds | Incomplete at cap |
| --- | ---: | ---: | ---: | ---: | ---: |
| Uniform, seed 0 | 3 seconds | 3181 | 3180 | 0 | 1 |
| Fixed, seed 0 | 4 seconds | 4403 | 4307 | 0 | 1 |
| Adaptive, seed 0 | 3 seconds | 3432 | 3419 | 0 | 1 |

The controls establish approximately one thousand complete evaluations per second in the tested environment, not an arm-performance comparison.
Supervisor cleanup overhead in these timing controls was between 13 and 20 milliseconds and is separately recorded.
The short adaptive run recovered a cyclotomic/sign variant of the known Lehmer value at proposal 3028, with the exact polynomial retained in [the calibration input](inputs/calibration_witnesses.json).
Its complete certified measure is approximately \(1.176280818259917506544070338474035051\).
These implementation controls have shorter budgets and are excluded from the pilot comparison.

## Exact offline baseline

The offline baseline intersects J147's complete Newton necessary cover with the actual box \([-4,4]^{D/2}\), identifies neutral outputs exactly, and uses exact Graeffe inequalities for the whole-measure threshold.
Every strict target was independently recomputed with the Arb full-product evaluator.
This calculation is separate setup and supplies no examples to the sampler.

| Degree | Target polynomials in the box | Uniform one-proposal target probability | Fixed-mixture one-proposal target probability | Fixed/uniform ratio |
| --- | ---: | ---: | ---: | ---: |
| 14 | 26 | \(5.435954111\cdot10^{-6}\) | \(6.508394871\cdot10^{-4}\) | 119.7287 |
| 18 | 176 | \(4.542867633\cdot10^{-7}\) | \(1.056313005\cdot10^{-4}\) | 232.5212 |
| 20 | 354 | \(1.015262085\cdot10^{-7}\) | \(5.537943406\cdot10^{-5}\) | 545.4693 |

The exact uniform probabilities are \(26/9^7\), \(176/9^9\), and \(354/9^{10}\).
For each degree, the exact fixed-mixture probability is \(\frac1{10}\frac{N}{9^n}+\frac9{10}\sum_{a\text{ target}}\prod_i2^{4-|a_i|}/46^n\), and the generated JSON retains the exact rational values.
The certified core groups contain 26 Lehmer-value polynomials in degree 14, 174 Lehmer-value and two \(1.1883681475\ldots\)-value polynomials in degree 18, and 344 Lehmer-value and ten \(1.1883681475\ldots\)-value polynomials in degree 20.
These two complete-measure intervals are disjoint.
The target contains only one distinct measure in degree 14 and two in degrees 18 and 20, so raw polynomial recovery and the primary distinct-value metric have different saturation behavior.
These are finite box probabilities under two fixed laws, not probabilities for the adaptive law, distinct-value yields per second, or statements about arbitrarily high degree.

## Post-run law diagnostic

The separate diagnostic reads a completed adaptive journal and the offline target census, then replays only committed updates using the frozen law implementation.
Each reconstructed update must equal the journal's exact elite/update record.
For every reconstructed law it sums the probability of the finite target set, retaining the fixed uniform exploration component.
The updates use the exact integer weights; the probability sums are explicitly binary64 approximations for diagnosis, not arithmetic certificates.
This later reference calculation supplies no data to a live proposal or update and never changes experimental yield.

The original short calibration journal contains 3432 committed proposals and is a replaceable ignored output.
Its diagnostic can be reproduced from native programs and seed zero by regenerating the degree-14 reference and completing a separately labelled 3432-proposal control under a 60-second ceiling.
The following normalized commands were executed successfully with the runtime and dependency setup above:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/baseline_mass.py 14 --output mathematics/computations/outputs/Yin_J_G0156/diagnostic_reference_d14.json
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py run --degree 14 --arm adaptive --seed 0 --seconds 60 --max-proposals 3432 --label diagnostic_reproduction
python -B mathematics/computations/programs/Yin_J_G0156/law_mass_diagnostic.py mathematics/computations/outputs/Yin_J_G0156/diagnostic_reproduction_d14_adaptive_s0.jsonl --reference mathematics/computations/outputs/Yin_J_G0156/diagnostic_reference_d14.json --output mathematics/computations/outputs/Yin_J_G0156/diagnostic_reproduction_native_reference.law_mass.json
~~~

Use an unused label and corresponding journal filename when repeating the control in a checkout that retains its earlier outputs.
The reproduction completed all 3432 proposals normally, with no incomplete proposals and exactly 13 updates.
The 3432 proposed coefficient lists, every elite/update record, and all integer block weights at each of the 13 update snapshots matched the original calibration exactly despite differing wall-clock fields.
The regenerated degree-14 reference and the existing full `baseline_mass.json` gave identical diagnostic probability snapshots.
The control is separate calibration evidence and contributes no pilot data.
No copy of the original multi-megabyte journal is required in native inputs.
Its approximate conditional whole-target probability changes from 0.0006508394871 to 0.00007624683267, about 0.11715 of its initial mass.
Both diagnostic executions reproduced a final-to-initial ratio of 0.11715151613896259.
This identifies a distributional change in that short control, not a completed pilot outcome or a distinct-value comparison.
The declared first-pilot law remains unchanged.
The [separate independent diagnostic review](../../../audits/reviews/Yin_R_G1111_v2.md#law-mass-diagnostic-review) verifies the committed replay and probability formula, including an exact rational reconstruction of every calibration snapshot.
It does not supply a first-pilot performance verdict.

<a id="prior-dilution"></a>
## What the pair pseudocounts force

This direct calculation concerns the biased pair component, before mixing in the one-tenth uniform exploration law.
Let \(q\) be one pair law, let \(m\) be the number of elite representatives in a nonempty update, and write \(\widehat q\) for their empirical pair law.
Since a batch contains at most 256 proposals, \(1\le m\le26\).
The declared update is exactly
\[
 q'=\frac45q+\frac15\left(\frac{m}{m+81}\widehat q+
                              \frac{81}{m+81}u_{81}\right),
\]
where \(u_{81}\) is uniform on the 81 pair states.
The elite data therefore receive weight at most \(26/535\), whereas the uniform pseudocount contribution has weight at least \(81/535\).

For \(W(a,b)=|a|+|b|\), the initial fixed-bias product law has mean \(52/23\), and \(\sum_{a,b=-4}^4 W(a,b)=360\).
Nonnegativity of every elite value gives
\[
 \mathbb E_{q'}W
 =\frac45\mathbb E_qW+
   \frac15\frac{\sum_{\mathrm{elite}}W+360}{m+81}
 \ge\frac45\mathbb E_qW+\frac15\frac{360}{107}.
\]
After \(t\) nonempty updates, independently of which elites were selected,
\[
 \mathbb E_{q_t}W\ge
 \left(\frac45\right)^t\frac{52}{23}
 +\left[1-\left(\frac45\right)^t\right]\frac{360}{107}.
\]
The first update raises this mean by at least \(2716/12305\), and the bound after 13 updates is approximately 3.303814, compared with the initial 2.260870.
Empty batches leave the law unchanged and do not contribute to \(t\).
This author-checked algebra establishes dilution of the initial small-coefficient bias in every pair block.
It proves neither monotonicity of the actual means nor a theorem about Mahler-measure probabilities, and it does not identify the sole cause of any empirical performance difference.

<a id="pilot-results"></a>
## Completed first-pilot results

All 45 degree/arm/seed identities completed the prescribed 60-second budget, representing 2700 seconds of capped experimental time.
There were 1906599 completed proposals, 43 interrupted proposals and no unresolved score or threshold among the completed evaluations.
There were no invalid runs or failed workers.
Supervisor termination overhead ranged from 0.01171 to 0.02742 seconds per run and supplied no additional counted candidate evaluation.
The fixed native observations retain each run's actual completion count, stage costs, neutral and repeat counts, raw hit rates, separate factor outcomes and first-hit censoring.

Each vector below is ordered by seeds 0 through 4.
A dash means no hit before the 60-second censoring time; it is not a measured first-hit time of 60 seconds.

| Degree | Arm | Distinct values in \(1<M<6/5\), all seeds | Median [range] | First target hit, seconds, all seeds |
| ---: | --- | --- | --- | --- |
| 14 | Uniform | 0, 1, 1, 0, 1 | 1 [0, 1] | —, 50.302, 47.567, —, 52.482 |
| 14 | Fixed | 1, 1, 1, 1, 1 | 1 [1, 1] | 1.012, 1.076, 3.126, 0.681, 1.599 |
| 14 | Adaptive | 1, 1, 1, 1, 1 | 1 [1, 1] | 2.753, 9.512, 2.079, 13.782, 2.878 |
| 18 | Uniform | 0, 0, 0, 0, 0 | 0 [0, 0] | —, —, —, —, — |
| 18 | Fixed | 1, 1, 1, 1, 1 | 1 [1, 1] | 30.937, 7.051, 22.899, 10.728, 5.353 |
| 18 | Adaptive | 1, 0, 0, 0, 0 | 0 [0, 1] | 57.913, —, —, —, — |
| 20 | Uniform | 0, 0, 0, 0, 0 | 0 [0, 0] | —, —, —, —, — |
| 20 | Fixed | 0, 1, 0, 0, 1 | 0 [0, 1] | —, 18.409, —, —, 2.169 |
| 20 | Adaptive | 0, 0, 0, 0, 0 | 0 [0, 0] | —, —, —, —, — |

All 224 raw whole-polynomial target hits recover the known Lehmer value, with normalized core coefficients \((1,-1,0,1,-1,1,-1,1,0,-1,1)\) in ascending order.
The best complete positive measure is approximately \(1.176280818259917506544070338474035051\); exact dyadic enclosures and the actual integer witnesses remain in the native data.
No run recovered the second reference value near 1.1883681475 as a whole-polynomial target.
The separate verification command recomputed all 1331 retained polynomial inputs after the experiment; this adds no stochastic discoveries or charged pilot work.

The reviewer's native fixed-data checks can be reproduced from the tracked inputs by first producing fresh witness certificates:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/independent_pilot_witness_verification.json
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_pilot_review.py fixed
~~~

The optional `journals` mode additionally requires the original 45 JSON/JSONL run pairs, original comparison output, 15 generated law-mass files and the three-degree baseline output in their stated J156 output home.
It reconstructs the actual saved histories without starting another experiment.
Those ignored original histories were available for the completed review; the fixed-data mode does not claim to reconstruct every proposal or wall-clock time from the compact native inputs.

The wider-threshold distinct-value counts below are medians with ranges over the same five runs.

| Degree | Arm | \(1<M<5/4\) | \(1<M<13/10\) | \(1<M<7/5\) |
| ---: | --- | --- | --- | --- |
| 14 | Uniform | 1 [0, 2] | 2 [1, 7] | 5 [5, 14] |
| 14 | Fixed | 7 [7, 7] | 22 [21, 23] | 70 [69, 74] |
| 14 | Adaptive | 3 [3, 4] | 12 [8, 15] | 32 [27, 35] |
| 18 | Uniform | 0 [0, 0] | 0 [0, 0] | 0 [0, 1] |
| 18 | Fixed | 9 [8, 13] | 28 [25, 33] | 98 [86, 104] |
| 18 | Adaptive | 0 [0, 2] | 1 [0, 3] | 6 [4, 8] |
| 20 | Uniform | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] |
| 20 | Fixed | 6 [6, 10] | 21 [14, 28] | 78 [64, 89] |
| 20 | Adaptive | 0 [0, 1] | 1 [0, 4] | 3 [1, 5] |

At each held-out degree, the adaptive arm wins against both baselines in zero of five matched seeds.
It loses to at least one baseline in four seeds at degree 18 and two seeds at degree 20.
It therefore fails the frozen S10 continuation screen; the current law is not enlarged in degree or runtime on the strength of this pilot.
Five seeds provide a bounded allocation comparison, not a universal superiority or statistical-significance theorem.

## Post-run target mass on the completed pilot

The unchanged diagnostic successfully replayed every committed update in all 15 completed adaptive journals.
The ratio of final to initial conditional whole-target probability has the following median and range.

| Degree | Median final/initial mass | Range over five seeds |
| ---: | ---: | --- |
| 14 | 0.03100498 | [0.02483697, 0.03543131] |
| 18 | 0.01139043 | [0.01111701, 0.01360001] |
| 20 | 0.00439979 | [0.00429380, 0.00479937] |

These binary64 diagnostic values describe the final laws on the known finite target sets.
They do not assert monotone decrease, give distinct-value yields, or estimate independent Bernoulli success probabilities along an adaptive path.
The fixed inputs retain the 15 observed final summaries; the diagnostic source and each run's seed and completed prefix length specify their mathematical replay scope.

<a id="prior-strength-control"></a>
## Exact fixed-elite prior-strength control

The separate control compares the original update O with alternative A on the same 13 elite batches from the earlier degree-14 calibration at seed zero.
It generates no new proposals, scores or roots, and it does not replay the live pilot under a different law.
For a pair state with elite count \(c(s)\) and total elite size \(m\), A replaces \((c(s)+1)/(m+81)\) by
\[
                         \frac{c(s)+1/81}{m+1}.
\]
Thus only the pair pseudocount strength changes, from 81 to 1.
The uniform prior center, four-fifths retention, one-tenth uniform exploration, initial law and singleton pseudocount total of nine are unchanged.
The exact laws are reconstructed before the reference targets are read for evaluation.

The selected checkpoints were updates 1 and 13, without scanning strengths or choosing a favorable stopping point.
The preselected final comparison has three cases: \(H_{13}^A\le H_{13}^O\), \(H_{13}^O<H_{13}^A<H_0\), or \(H_{13}^A>H_{13}^O\) and \(H_{13}^A\ge H_0\).
All decisions, probability sums and block moments use exact rational arithmetic; the following decimals are displays.
The initial mass is exactly \(H_0=52995173298491/81425872817060715\).

| Update | Original \(H_t^O/H_0\) | Reduced-strength \(H_t^A/H_0\) |
| ---: | ---: | ---: |
| 1 | 0.8059852063407912 | 1.628944610941281 |
| 13 | 0.11715151613896257 | 1.550710530146340 |

The result enters the third case: the alternative restores and exceeds initial target mass on this fixed data path.
Extraction verified every original elite record and every rational O block probability against the frozen integer-weight law.
The control verifies normalized positive probabilities, unchanged singleton laws, the pair-difference identity and the original pair-moment lower bound at all 13 updates.
The initial mass agrees exactly with the independently checked finite reference.
The main agent also inspected the new source and repeated the rational control using the separately regenerated degree-14 reference, obtaining the same results.
These are ordinary computation checks, separate from the frozen sampler's earlier independent implementation review.

Use the retained elite input directly and regenerate only the degree-14 reference when needed:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/baseline_mass.py 14 --output mathematics/computations/outputs/Yin_J_G0156/diagnostic_reference_d14.json
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_control.py run --reference mathematics/computations/outputs/Yin_J_G0156/diagnostic_reference_d14.json
~~~

The first command requires the previously stated baseline dependencies; the second uses only Python's standard library and writes [prior_strength_control.json](../../outputs/Yin_J_G0156/prior_strength_control.json).
To check the elite source itself, first regenerate the separately labelled 3432-proposal calibration journal with the earlier commands, then run:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_control.py extract --journal mathematics/computations/outputs/Yin_J_G0156/diagnostic_reproduction_d14_adaptive_s0.jsonl --output mathematics/computations/outputs/Yin_J_G0156/prior_strength_elites_reproduced.json
~~~

The tracked native input makes the fixed-data calculation reproducible without a copy of that multi-megabyte journal.
Changing the law during actual sampling changes later proposals and elites, so this result is not a live-search performance gain.
Any subsequent degree-18/20 comparison reuses an inspected benchmark and is not a new unseen held-out evaluation, even with new seeds.

<a id="prior-strength-live"></a>
## Separate live prior-strength comparison

The [S10 follow-up protocol](../../../strategies/Yin_S_G0010.md#prior-strength-follow-up) uses degree 14, seeds 5 through 9, and fixed, original adaptive O and reduced-pair-prior A arms.
Each run has a ten-second wall-clock cap, with the arm order rotated by the seed index and all fifteen runs performed serially on one worker.
The experimental ceiling is 150 seconds.
A changes only the pair frequency to \((c(s)+1/81)/(m+1)\); the singleton prior, initialization, exploration fraction, selector, smoothing, full-root evaluator, cache and duplicate handling remain unchanged.
The new worker entry point selects the actual law in the child process before calling the frozen worker.
The report has its own seed range and fifteen-run completeness rule; failed, early, proposal-limited and missing runs cannot make the allocation screen pass.
This comparison is separate from the original forty-five-run pilot and reuses an inspected benchmark.

The implementation controls checked all thirteen exact fixed-elite updates and replayed each proposal in three 257-proposal child-process runs.
O and A generated the same first 256 proposals and different, correctly dispatched proposals after the first update.
A short deadline control and an injected worker failure checked completion cutoffs, invalid-run retention and censoring at the actual observed time.
Synthetic metric cases checked the four-of-five boundaries, equal positive counts with earlier first hits, zero-hit ties and incomplete comparisons.
These controls establish implementation behavior; the completed live experiment supplies the separate performance observations below.

Use a fresh output label for each explicitly selected reproduction, with the same runtime and dependency setup as above:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_live_checks.py --label independent_live_checks
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_live.py compare --label s10_prior_live
~~~

The second command is the complete declared schedule, not an instruction to repeat a failed or unfavorable comparison.
Before any expansion, A must avoid a target-count loss to fixed in at least four seeds and improve on O in at least four seeds by a larger count or, at equal positive count, an earlier first hit.
All fifteen valid runs are required.
This is a resource-allocation screen, with no statistical-significance or new-degree claim.
The [independent implementation finding](../../../audits/reviews/Yin_R_G1111_v4.md#live-implementation-review) covers the actual new child dispatch, exact update, deadline and failure behavior, and the complete fifteen-run allocation screen.

<a id="prior-live-results"></a>
### Completed live comparison

All fifteen declared runs completed with valid deadline termination, with 284130 completed proposals and fourteen unfinished proposals across the 150-second experimental budget.
No completed evaluation had an unresolved ranking or threshold decision.
The following table retains all five seed outcomes; a dash denotes no target hit, censored at ten seconds.

| Seed | Fixed distinct values below \(6/5\) | O distinct values | A distinct values | Fixed first hit (s) | O first hit (s) | A first hit (s) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 1 | 1 | 1 | 0.955750 | 0.348519 | 0.346241 |
| 6 | 1 | 1 | 1 | 4.619307 | 1.268227 | 0.727849 |
| 7 | 1 | 0 | 1 | 0.660690 | — | 0.503877 |
| 8 | 1 | 0 | 1 | 0.385270 | — | 0.499011 |
| 9 | 1 | 0 | 1 | 4.550654 | — | 0.931219 |

A has five nonlosses to fixed and five improvements on O under the declared screen, so the complete comparison passes.
At seed five, O and A hit the same polynomial at proposal 122, before any update; the approximately 0.00228-second timing difference cannot be attributed to learning.
The other four seeds still satisfy the improvement rule independently of that timing comparison: seed six first hits at proposal 581 for A and 1188 for O, and seeds seven through nine improve the target count.
This is a finite recovery result on the reused degree-14 benchmark.

| Arm | Completed proposals | Fresh complete evaluations | Cache hits | Raw whole-target hits | Distinct target values per run |
| --- | ---: | ---: | ---: | ---: | --- |
| Fixed | 60825 | 58834 | 1991 | 29 | 1, 1, 1, 1, 1 |
| O | 57240 | 57126 | 114 | 2 | 1, 1, 0, 0, 0 |
| A | 166065 | 49676 | 116389 | 5859 | 1, 1, 1, 1, 1 |

All 5890 raw whole-target hits recover the same known Lehmer core and measure as in the first pilot.
The target-value count of A equals that of fixed in every run; no new target value was found.
A's repeated-proposal fraction ranges from 70.64 to 71.31 percent, its cache-hit fraction from 69.69 to 70.45 percent, and its neutral fraction from 9.05 to 9.59 percent.
Its higher proposal throughput and raw target count therefore include substantial repetition and cannot be read as a comparable gain in distinct-value discovery.
The median wider-threshold distinct counts, with ranges over the same five runs, are as follows.

| Arm | \(1<M<5/4\) | \(1<M<13/10\) | \(1<M<7/5\) |
| --- | --- | --- | --- |
| Fixed | 7 [6, 7] | 17 [14, 20] | 59 [48, 59] |
| O | 2 [0, 4] | 5 [5, 9] | 17 [14, 22] |
| A | 6 [6, 7] | 19 [18, 19] | 62 [61, 64] |

The native comparison retains the non-reconstructible timing and complete observed summaries, while the witness input retains 449 exact polynomials for certificate replay.
Separate-factor records retain their actual committed whole-output parents and do not contribute to the primary metric.
To export a separately reproduced schedule, use explicit fresh destinations rather than overwriting these observations:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_live_export.py export --label s10_prior_live --comparison mathematics/computations/outputs/Yin_J_G0156/prior_live_export_check.json --witnesses mathematics/computations/outputs/Yin_J_G0156/prior_live_export_witnesses.json
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/prior_live_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/prior_live_witness_verification.json
~~~

The export command requires the fifteen actual JSON/JSONL run pairs; witness verification uses the retained input without those local journals and adds no stochastic discoveries.
The [independent results finding](../../../audits/reviews/Yin_R_G1111_v4.md#live-results-review) reconstructs all fifteen journals and 866 updates and checks all 449 retained polynomial inputs, the parent-factor associations and the result tables.
Its 449 certificate checks reuse the 366 inputs already certified in that review and add the 83 newly retained parent polynomials.

<a id="degree-validation"></a>
## Separate comparison at degrees 18 and 20

The [S10 degree protocol](../../../strategies/Yin_S_G0010.md#degree-validation) compares fixed bias with unchanged A at degrees 18 and 20, using seeds 10 through 14 and ten seconds per run.
The twenty identities run serially, first at degree 18 and then at degree 20, with arm order rotated by degree index plus seed index.
Each starts a fresh law and cache.
The new entry point explicitly passes degree, variant and seed to its own child process and imports the existing A class without changing it.
Degree 18 has four pair blocks and a singleton; degree 20 has five pair blocks and no singleton.
The complete measure, root precision, batch, exploration, duplicate and charged-cost conventions stay fixed.
All twenty formal runs have completed; the observations and scope are recorded below.

The bounded implementation controls completed four 257-proposal subprocesses and replayed every actual proposal and update.
They checked the full polynomial degree and both block layouts against exact Fraction updates.
A short deadline, an injected failure and independent startup-failure and identity controls checked the new runtime's actual behavior.
The independent pre-run check found no blocking defect; this supplies no performance result for the formal comparison.

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation_checks.py --label independent_degree_preflight
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation.py compare --label s10_degree_validation
~~~

The first command requires a fresh output label when reproducing existing controls.
The second command is the declared 200-second experiment and refuses to overwrite existing runs.
Its report requires all twenty valid identities, at least four target-count nonlosses for A at each degree, and at least four count-or-positive-first-hit improvements at one degree.
Zero-hit ties do not count as improvements.
The recorded first-hit proposal identifies any hit in A's initial batch, whose timing is not evidence of a learned-law change.
Both degrees are reused benchmarks, and all outcomes remain separate from the first pilot and the degree-14 live control.

### Completed degree comparison

All twenty declared identities ended with valid deadline termination, representing 200 seconds of capped experimental time.
They completed 209433 proposals and left twenty unfinished proposals, with 147858 fresh complete evaluations, 61575 cache hits, 61816 repeated proposals, 12308 neutral outputs and 525 A updates.
There were no unresolved completed scores or threshold decisions and no failed workers.
Supervisor termination overhead ranged from 0.00907 to 0.02404 seconds per run and added no counted candidate evaluation.
The following table gives every seed's distinct complete-polynomial target count and first-hit time; a dash denotes no hit, censored at ten seconds.

| Degree | Seed | Fixed values in \(1<M<6/5\) | A values | Fixed first hit (s) | A first hit (s) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 10 | 0 | 1 | — | 2.777177 |
| 18 | 11 | 1 | 1 | 6.049199 | 0.996976 |
| 18 | 12 | 1 | 1 | 6.076398 | 1.187771 |
| 18 | 13 | 1 | 1 | 6.777565 | 1.863692 |
| 18 | 14 | 1 | 1 | 2.811106 | 3.251588 |
| 20 | 10 | 0 | 1 | — | 2.495643 |
| 20 | 11 | 0 | 1 | — | 3.737657 |
| 20 | 12 | 1 | 1 | 1.969785 | 2.222744 |
| 20 | 13 | 0 | 1 | — | 3.587169 |
| 20 | 14 | 0 | 1 | — | 1.569018 |

A has five target-count nonlosses and four improvements at each degree, so the complete comparison passes the declared allocation screen.
At degree 18, seed 10 improves the count and seeds 11 through 13 improve the first-hit time at equal positive count; seed 14 has a later first hit.
At degree 20, seeds 10, 11, 13 and 14 improve the count, while seed 12 has a later first hit at equal positive count.
A's first-hit proposal indices are \((2150,620,778,1370,2635)\) at degree 18 and \((1559,2492,1377,2386,900)\) at degree 20, in seed order.
All exceed the first update boundary of 256 proposals; this temporal order alone does not isolate adaptation's causal effect.

The following aggregates sum the five runs within each degree and arm.
Repeat counts refer to completed proposals, while unfinished proposals remain separately charged at the deadline.

| Degree | Arm | Completed | Fresh complete | Cache hits | Repeated proposals | Neutral | Raw whole-target hits | Updates |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | Fixed | 40569 | 40515 | 54 | 70 | 123 | 7 | 0 |
| 18 | A | 77184 | 39551 | 37633 | 37821 | 6856 | 231 | 300 |
| 20 | Fixed | 33595 | 33592 | 3 | 3 | 37 | 1 | 0 |
| 20 | A | 58085 | 34200 | 23885 | 23922 | 5292 | 338 | 225 |

A's repeated-proposal fraction ranges from 47.75 to 50.15 percent at degree 18 and from 37.51 to 44.26 percent at degree 20.
Its neutral fractions range from 8.42 to 9.38 percent and from 7.96 to 10.62 percent, respectively.
The larger completed-proposal and raw-hit counts therefore include substantial reuse of previously evaluated polynomials.
Each wider-threshold cell below lists all five seed counts, followed by the median and range.
These are conservatively separated certified complete-polynomial values within each run; sums across runs are not a union of distinct values.

| Degree | Arm | \(1<M<5/4\): all seeds; median [range] | \(1<M<13/10\): all seeds; median [range] | \(1<M<7/5\): all seeds; median [range] |
| ---: | --- | --- | --- | --- |
| 18 | Fixed | 3, 3, 4, 4, 5; 4 [3, 5] | 8, 13, 13, 14, 13; 13 [8, 14] | 30, 40, 35, 40, 35; 35 [30, 40] |
| 18 | A | 13, 15, 15, 13, 13; 13 [13, 15] | 41, 42, 41, 38, 40; 41 [38, 42] | 131, 136, 133, 126, 125; 131 [125, 136] |
| 20 | Fixed | 3, 1, 2, 2, 2; 2 [1, 3] | 9, 6, 7, 5, 6; 6 [5, 9] | 20, 18, 18, 18, 19; 18 [18, 20] |
| 20 | A | 13, 15, 15, 14, 16; 15 [13, 16] | 44, 42, 40, 41, 40; 41 [40, 44] | 154, 162, 143, 156, 152; 154 [143, 162] |

All retained whole-target discoveries have normalized core \((1,-1,0,1,-1,1,-1,1,0,-1,1)\), the same known Lehmer value recovered earlier.
The 577 raw whole-target hits yield no additional distinct target value, and no whole output recovers the second reference value near 1.1883681475.
The best complete positive measure has the retained enclosure \([1.176280818259917506544070338474035051\mathbin{\pm}5.05\times10^{-37}]\); native certificates retain the exact dyadic endpoints.
The separate-factor collection has seventeen target records, all the Lehmer polynomial \(P(x)\) or \(P(-x)\), which have the same measure.
Five of those factor records occur in whole outputs outside the target interval and do not count toward the primary metric.
Thus this finite comparison demonstrates improved recovery of a known value on these reused boxes, without finding a new small measure or resolving the unrestricted Lehmer gap.
It supplies no statistical-significance or uninspected-benchmark claim.

### Retained degree observations and reproduction

[inputs/degree_comparison.json](inputs/degree_comparison.json) retains all twenty original configurations, counts, times, costs, censoring and validity fields, plus first-hit proposal and initial-batch fields.
It also retains 1691 per-run whole-value discovery records, each run's best output, 1849 separate-factor discoveries, 66 unresolved factor-value equality associations and their 1844 committed parent-output records.
There are no unresolved whole-value equality records.
The factor equality uncertainties concern value identity in the wider band, with none below \(13/10\); they are separate from the zero unresolved score and threshold decisions.
[inputs/degree_witnesses.json](inputs/degree_witnesses.json) contains 1575 distinct exact polynomial arrays covering the retained whole, best, factor and parent-output roles.
Those roles can overlap for one polynomial.
The complete measure and normalized core stay attached to each whole-output certificate, and each factor association retains its exact factor and whole-parent witness references.
Factor outcomes remain separate from complete-polynomial yield.

[degree_validation_export.py](degree_validation_export.py) uses only the new twenty-run identity enumeration and report, while reusing the checked certificate-compaction and committed-parent helpers from the live export.
It refuses existing destinations and requires explicit `--allow-partial` when fewer than twenty summaries are present.
Its bounded export check preserved the four 257-proposal controls and failed-worker control, verified all original observation fields and witness associations, and confirmed that partial controls cannot pass the allocation screen.
That check retained five witness arrays and one factor parent for the short controls, and zero witnesses for the failed control, without generating proposals or root certificates.
Use fresh labels and output destinations when reproducing controls or exporting an independently reproduced schedule:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation_export.py self-test --label independent_degree_export --short-label independent_degree_preflight_257 --failure-label independent_degree_preflight_failure
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation.py report --label s10_degree_validation
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation_export.py export --label s10_degree_validation --comparison mathematics/computations/outputs/Yin_J_G0156/degree_export_check.json --witnesses mathematics/computations/outputs/Yin_J_G0156/degree_export_witnesses.json
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/degree_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/degree_witness_verification.json
~~~

The export self-test requires the controls generated by the earlier `degree_validation_checks.py` command with the displayed label.
The report reads the twenty JSON summaries; export additionally reads their original JSONL journals to recover the committed factor parents.
The retained-input verification command needs no original run journals and adds no stochastic discoveries.
Recomputing certificates cannot reproduce historical wall-clock prefixes or timing from the compact inputs; these remain preserved observations.
The [independent implementation finding](../../../audits/reviews/Yin_R_G1111_v5.md#degree-implementation-review) and [completed-evidence finding](../../../audits/reviews/Yin_R_G1111_v5.md#degree-results-review) cover the actual twenty histories, 525 exact updates, retained certificate support and qualified result interpretation.
They do not cover the subsequent core-mass diagnostic below.

<a id="core-mass-diagnostic"></a>
## Exact post-run target mass by core

The [selected S10 diagnostic](../../../strategies/Yin_S_G0010.md#core-mass-follow-up) asks whether improved Lehmer recovery also increases coverage of the second known target near 1.1883681475.
[core_mass_diagnostic.py](core_mass_diagnostic.py) first replays the ten completed A journals, checking every recorded proposal and all 525 committed updates before reading any reference targets.
It then partitions the existing complete target census by exact factorization and the frozen normalized core, without new root calculations.
The degree-18 partition has 174 Lehmer prefixes and two second-core prefixes; the degree-20 partition has 344 and ten.
[inputs/degree_core_mass_states.json](inputs/degree_core_mass_states.json) retains these 530 prefixes and the final block states with 3690 positive integer weights, while referring to the existing degree comparison for original configurations and counts.
The final state is the state after the last committed update; an unfinished update contributes nothing.

For a target set \(T\), half-degree \(n\), block weights \(w_b\), and the block state \(s_b(a)\) of a prefix \(a\), the exact conditional next-proposal mass is
\[
 H(T)=\frac{|T|}{10\,9^n}
       +\frac{9\sum_{a\in T}\prod_b w_b(s_b(a))}
                    {10\prod_b\sum_s w_b(s)}.
\]
The separate evaluation uses only standard-library integer arithmetic and aggregate Fraction normalization on the fixed states and target partition.
The initial probabilities agree exactly with the independently checked fixed-law census.
Small controls compare this formula with separate Fraction products and cover empty sets, uniform laws and full small boxes.
[inputs/degree_core_mass.json](inputs/degree_core_mass.json) retains every initial and final probability, ratio and exploration floor as exact numerator and denominator strings.
The decimals below are displays of those rational results.

| Degree | Initial Lehmer mass | Initial second-core mass |
| ---: | ---: | ---: |
| 18 | 0.000104582879289539 | 0.000001048421190703135 |
| 20 | 0.000053555274498303 | 0.000001824159565782738 |

| Degree | Seed | Final Lehmer mass | Final / initial Lehmer | Final second-core mass | Final / initial second core |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 10 | 0.002695556721 | 25.77435943 | 5.447936784e-10 | 0.000519632456 |
| 18 | 11 | 0.001818287791 | 17.38609420 | 1.628638924e-9 | 0.001553420456 |
| 18 | 12 | 0.001946227635 | 18.60942870 | 6.440172387e-10 | 0.000614273390 |
| 18 | 13 | 0.003268918116 | 31.25672326 | 7.010388018e-10 | 0.000668661420 |
| 18 | 14 | 0.002644408411 | 25.28528980 | 5.188195576e-10 | 0.000494857947 |
| 20 | 10 | 0.010422744145 | 194.61657592 | 2.941305062e-8 | 0.016124165435 |
| 20 | 11 | 0.012412755051 | 231.77465090 | 1.788238331e-8 | 0.009803080632 |
| 20 | 12 | 0.019312878907 | 360.61581400 | 2.373667720e-8 | 0.013012390825 |
| 20 | 13 | 0.012446185337 | 232.39887113 | 3.704597846e-9 | 0.002030851859 |
| 20 | 14 | 0.013657233693 | 255.01192592 | 7.867002467e-9 | 0.004312672320 |

All ten final laws increase Lehmer mass and decrease second-core mass by exact comparison.
The initial-to-final comparison establishes neither a monotone trajectory nor an independent Bernoulli model along the adaptive path.
It supplies no stochastic discovery, new small value or uninspected-benchmark advantage.
The one-tenth uniform component preserves positive probability on this finite box, but the observed concentration substantially reduces coverage of its other known target.
The [independent diagnostic finding](../../../audits/reviews/Yin_R_G1111_v6.md#core-mass-review) verifies the actual committed-state provenance, exact target partition, all twenty core probabilities and the qualified interpretation.
Its scope excludes the subsequent mutation-kernel control and any future feedback design.

Use these commands from the repository root, with a fresh output path for an existing result:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/core_mass_diagnostic.py self-test
python -B mathematics/computations/programs/Yin_J_G0156/core_mass_diagnostic.py run --output mathematics/computations/outputs/Yin_J_G0156/degree_core_mass_recomputed.json
~~~

The probability recomputation needs only the retained states and degree comparison, with no FLINT, journal, root calculation or new sampling.
Reproducing the state extraction instead requires the original ten A journals and the reference census generated by `baseline_mass.py 18 20`:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/core_mass_diagnostic.py extract --seconds 60 --output mathematics/computations/outputs/Yin_J_G0156/degree_core_mass_states_replayed.json
~~~

The bounded extraction and subsequent exact evaluation have both been executed; existing fixed inputs are never overwritten.

<a id="mutation-kernel-control"></a>
## Target geometry and a reference-seeded mutation control

[target_geometry.py](target_geometry.py) computes exact distances between the retained Lehmer and second-core prefix classes.
The minimum free-coordinate Hamming distance is three at degree 18 and two at degree 20.
A free reciprocal coordinate can affect two coefficients of the complete polynomial; these distances concern the sampling coordinates, not all polynomial coefficients separately.
The [inspected SEMR21 restoration mechanism](../../../audits/literature/SEMR21/Yin_U001.md#restoration-map) supplies the related idea of retaining correlations from an existing reference template.
Its nearest-reference completion on a bivariate ternary domain is distinct from the fully specified univariate control below, and its reported results are not used as comparative evidence here.

[mutation_kernel_control.py](mutation_kernel_control.py) evaluates one fixed kernel using the complete retained Lehmer prefix class as its parent reference set.
With probability \(1/10\), it chooses uniformly from the whole box \(\{-4,\ldots,4\}^n\), where \(n=d/2\).
With probability \(9/10\), it chooses a uniform parent from that reference class, chooses \(k\) uniformly from \(\{1,2,3\}\), chooses a uniform \(k\)-element set of distinct free coordinates, and independently adds \(+1\) or \(-1\), each with probability one half, at those coordinates.
If any changed coordinate leaves the box, the outcome is the unchanged parent; no rejection or resampling is performed.
This control explicitly uses complete known reference data and fits no new law.

Let \(L\) be the parent class, \(T\) the second-core target class, and
\[
 C_k=\#\{(a,b)\in L\times T:
       d_H(a,b)=\lVert a-b\rVert_1=k\}.
\]
Each such ordered pair corresponds to exactly one coordinate subset and sign vector.
The mutation-only and complete mixture probabilities of a second-core hit are therefore
\[
 Q(T)=\sum_{k=1}^{3}\frac{C_k}{3|L|\binom{n}{k}\,2^k},
 \qquad
 H_{\mathrm{kernel}}(T)=\frac{|T|}{10\,9^n}+\frac9{10}Q(T).
\]
Boundary returns cannot hit \(T\), because the exact core classes are disjoint.
Small hand-counted controls check all three values of \(k\), empty targets, probability normalization, boundary returns and exclusion of a coordinate difference greater than one.
A separate exhaustive endpoint enumeration of all 544156 parent/subset/sign outcomes at the actual degrees agrees exactly with the cross-pair counts.
This enumeration performs no Mahler evaluation or stochastic search.

| Degree | Parent prefixes | Target prefixes | \(C_1\) | \(C_2\) | \(C_3\) | Target prefixes reachable by mutation |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 174 | 2 | 0 | 0 | 2 | 2 |
| 20 | 344 | 10 | 0 | 2 | 6 | 4 |

The following probabilities and ratios are exact in [inputs/mutation_kernel_control.json](inputs/mutation_kernel_control.json); displayed decimals are rounded.
The fixed baseline is the already checked mixture of uniform sampling and coefficient-wise fixed bias on the same box.

| Degree | Exact mutation-only \(Q(T)\) | Exact complete mixture \(H_{\mathrm{kernel}}(T)\) | Mixture probability, decimal | Kernel / fixed probability |
| ---: | --- | --- | ---: | ---: |
| 18 | \(1/175392\) | \(25830631/5033366993088\) | 0.000005131879125 | 4.894863983 |
| 20 | \(5/297216\) | \(1162283483/76765045372416\) | 0.000015140790673 | 8.300145973 |

The exact kernel-to-A comparisons use the final conditional second-core probabilities already retained by the core-mass diagnostic.
The kernel has no seed; the columns below identify the previously completed A paths used for comparison.

| Degree | Kernel / A seed 10 | Seed 11 | Seed 12 | Seed 13 | Seed 14 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 9419.858064 | 3151.023255 | 7968.543101 | 7320.392412 | 9891.452722 |
| 20 | 514.764377 | 846.687514 | 637.864792 | 4087.026798 | 1924.594626 |

Thus the specified template-preserving mutations assign greater one-step probability to the other known target class under this complete-reference assumption.
At degree 18, three simultaneous unit changes are necessary for every compatible pair; the one- and two-coordinate mutation branches cannot reach that class.
At degree 20, six of its ten target prefixes remain unreachable by the mutation branch and retain only the whole-box uniform contribution.
The native result preserves every compatible parent-target witness, its changed coordinates and signs, the boundary-return counts, and the exact comparisons with all ten A final states.
It reuses the existing target partition and does not create a new target or polynomial certificate.
The [independent offline-control finding](../../../audits/reviews/Yin_R_G1111_v7.md#mutation-controls-review) verifies the finite law, complete endpoint counts, geometry and exact comparisons.
They establish no ability to learn the complete parent class, no live success rate or cost-normalized advantage, and no novel Mahler value or arbitrary-radius conclusion.
The exact kernel control itself performs no live search.

The programs use only the standard library and retained native inputs; use fresh output destinations when reproducing them:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/target_geometry.py --output mathematics/computations/outputs/Yin_J_G0156/target_geometry_recomputed.json
python -B mathematics/computations/programs/Yin_J_G0156/mutation_kernel_control.py self-test
python -B mathematics/computations/programs/Yin_J_G0156/mutation_kernel_control.py run --output mathematics/computations/outputs/Yin_J_G0156/mutation_kernel_recomputed.json
~~~

<a id="acquired-parent-control"></a>
## Offline control with actually observed parent prefixes

[acquired_parent_control.py](acquired_parent_control.py) replaces the complete reference parent library in the preceding kernel by the distinct Lehmer prefixes actually encountered in each completed A history.
Extraction scans every committed whole-target evaluation, including later representations of a previously known core, and groups parents by their exact free-coordinate vector.
It reads no complete parent or target reference library.
The whole polynomial reconstructed from each prefix must match its saved certificate, whose exact core and dyadic measure interval verify the selected target status without a new root calculation.
The complete reference partition is read only in the later evaluation, where each observed parent set is checked to be a subset of its degree's Lehmer class.

[inputs/acquired_parent_states.json](inputs/acquired_parent_states.json) retains every distinct parent, its first certificate's core and interval, and all selected occurrence records as proposal number, committed time, cache flag and repeat flag.
Original configurations and full-run counts remain in the existing degree comparison.
The extraction reconstructed the exact polynomial LRU and seen-prefix flags over all 135269 committed A evaluations.
The 569 committed Lehmer hits give 55 run-parent records: 25 across the degree-18 runs and 30 across degree 20.
There are 513 cached target hits and 514 repeated target hits; the difference is one fresh reevaluation of an earlier target prefix at degree 18, seed 12.
Neither cached repetition nor fresh repetition increases a parent's weight in the subsequent uniform choice over distinct parents.
All ten actual parent sets are nonempty; the implementation separately checks that an empty parent set leaves the kernel undefined, without supplying a reference parent or silently switching to a fallback law.

The same one-tenth whole-box uniform component, uniform \(k\in\{1,2,3\}\), distinct-coordinate selection, signed unit changes and boundary-return rule are used without adjustment.
The formula in the preceding section applies with \(L\) replaced by the run's observed parent set.
A separate endpoint enumeration checks all 55650 mutation branches arising from those ten sets, agreeing exactly with the cross-pair counts.
The complete-library probability is also recomputed from the retained partition and agrees exactly with the previous control.
In every observed set \(C_1=C_2=0\); the following table retains all ten \(C_3\) and coverage outcomes.

| Degree | Seed | Raw Lehmer hits | Distinct parents | Cached target hits | \(C_3\) | Second-core prefixes reachable by mutation |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 10 | 31 | 6 | 25 | 0 | 0 |
| 18 | 11 | 36 | 7 | 29 | 0 | 0 |
| 18 | 12 | 50 | 4 | 45 | 0 | 0 |
| 18 | 13 | 52 | 4 | 48 | 0 | 0 |
| 18 | 14 | 62 | 4 | 58 | 0 | 0 |
| 20 | 10 | 42 | 6 | 36 | 2 | 2 |
| 20 | 11 | 40 | 6 | 34 | 2 | 2 |
| 20 | 12 | 111 | 5 | 106 | 1 | 1 |
| 20 | 13 | 65 | 6 | 59 | 2 | 2 |
| 20 | 14 | 80 | 7 | 73 | 4 | 4 |

[inputs/acquired_parent_control.json](inputs/acquired_parent_control.json) retains the exact probabilities, ratios, compatible parent-target witnesses and boundary counts.
The table displays the complete mixture's second-core probability and its ratio to the complete-library kernel, fixed bias and that run's original A final law.

| Degree | Seed | Observed-parent mixture probability | / Complete library | / Fixed bias | / A final |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | 10 | 5.162349583e-10 | 0.000100593749 | 0.000492392717 | 0.947578834 |
| 18 | 11 | 5.162349583e-10 | 0.000100593749 | 0.000492392717 | 0.316973241 |
| 18 | 12 | 5.162349583e-10 | 0.000100593749 | 0.000492392717 | 0.801585621 |
| 18 | 13 | 5.162349583e-10 | 0.000100593749 | 0.000492392717 | 0.736385714 |
| 18 | 14 | 5.162349583e-10 | 0.000100593749 | 0.000492392717 | 0.995018308 |
| 20 | 10 | 0.000104166953464 | 6.879888621 | 57.104079828 | 3541.521579 |
| 20 | 11 | 0.000104166953464 | 6.879888621 | 57.104079828 | 5825.115795 |
| 20 | 12 | 0.000062500286797 | 4.127940749 | 34.262510786 | 2633.068069 |
| 20 | 13 | 0.000104166953464 | 6.879888621 | 57.104079828 | 28118.289162 |
| 20 | 14 | 0.000178571715369 | 11.794081249 | 97.892595976 | 22698.825393 |

At degree 18, none of the five histories encountered either complete-library parent compatible with the second core under this mutation rule.
Every observed-parent probability therefore equals the unchanged uniform floor \(1/1937102445\), below the fixed baseline and each original A final probability.
At degree 20, the observed subsets contain one to three compatible parents and concentrate their uniform parent weight enough to exceed the complete-library average, while reaching at most four of the ten second-core prefixes.
The two degrees therefore do not support a general ordering between observed and complete parent libraries.

These sets were selected after each completed run using whole-target and known-core status.
The final new parent in each set was first encountered between 5.427636 and 9.714467 seconds into its original run, with exact individual provenance retained in the input.
The calculation gives conditional probabilities for those completed sets, not the success rate or cost of acquiring and using them in a live algorithm.
It neither changes the original observed yields nor provides a novel polynomial, new Mahler value or independent benchmark claim.
The [independent offline-control finding](../../../audits/reviews/Yin_R_G1111_v7.md#mutation-controls-review) verifies the actual journal extraction, distinct-parent and cache accounting, all ten conditional probabilities and their stated limitations.
The acquired-parent control itself performs no stochastic trial or live implementation.

Pure probability recomputation uses only the standard library and retained native inputs:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/acquired_parent_control.py self-test
python -B mathematics/computations/programs/Yin_J_G0156/acquired_parent_control.py run --output mathematics/computations/outputs/Yin_J_G0156/acquired_parent_recomputed.json
~~~

Reproducing the parent extraction additionally requires the original ten A JSONL journals and existing degree comparison:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/acquired_parent_control.py extract --seconds 60 --output mathematics/computations/outputs/Yin_J_G0156/acquired_parent_states_replayed.json
~~~

Both extraction and evaluation have been executed once for the retained observations, and the commands refuse existing output destinations.

<a id="cyclotomic-closure"></a>
## Constructing the complete template class from one core

[cyclotomic_closure.py](cyclotomic_closure.py) reverses the frozen core normalization using a supplied certified core, the required degree and coefficient height.
It does not need a census of low-measure parent polynomials.
Let \(F\) be a core in the frozen sign normalization, monic and reciprocal of positive even degree \(d\), with constant coefficient one, no cyclotomic factor and gcd one for its nonzero coefficient exponents.
Every degree-\(D\) polynomial with this normalized core has the form
\[
 P(z)=F(\varepsilon z^k)C(z),\qquad
 \varepsilon\in\{-1,1\},\quad 1\le k\le\lfloor D/d\rfloor,
\]
where \(C\) is a monic reciprocal cyclotomic product of degree \(D-kd\).
Indeed, removing the cyclotomic factors leaves exactly the polynomial whose exponent compression and sign normalization return \(F\); reversing those two operations gives \(F(\varepsilon z^k)\).
Conversely, this substitution introduces no cyclotomic roots, has the same whole measure as \(F\), and the product normalizes back to \(F\).
Thus filtering all these products by the final coefficient height enumerates exactly the desired template class, without creating a new core or measure.

The cyclotomic enumeration reuses [J147's complete neutral-product construction](../Yin_J_G0147/readme.md#measure-and-chamber).
At even remaining degree \(r\), its factors are \((z-1)^2,(z+1)^2\) and every \(\Phi_m\) with \(m\ge3\) and \(\varphi(m)\le r\).
The already justified inequality \(\varphi(m)^2\ge m/2\) bounds the inspected orders by \(2r^2\).
Dynamic programming lists every product at the required degree; no intermediate height restriction is used, because later multiplication may cancel coefficients.
The case \(r=0\) supplies the constant product one.
The program checks the core's coefficient, degree, reciprocity and exponent-gcd interface; the caller supplies its prior noncyclotomic certification.

The actual degree-18/20 comparison generated all templates before loading the reference target partition, and then compared the complete coefficient sets:

| Core | Output degree | Constructed products before height filtering | Accepted distinct templates | Exact census comparison |
| --- | ---: | ---: | ---: | --- |
| Lehmer | 18 | 330 | 174 | Equal sets |
| Lehmer | 20 | 838 at \(k=1\), 2 at \(k=2\) | 344 | Equal sets |
| Second known core | 18 | 2 | 2 | Equal sets |
| Second known core | 20 | 10 | 10 | Equal sets |

The retained [target partition](inputs/degree_core_mass_states.json) supplies only this subsequent equality check; it is not an input to the generator.
The two core coefficient lists themselves are explicitly supplied known seeds in this control.
The generated output is `mathematics/computations/outputs/Yin_J_G0156/cyclotomic_closure.json`.
Small controls check the five degree-two neutral products, exact cyclotomic factorization of every neutral product through degree ten, and reverse normalization of 556 generated representations across the selected core/degree combinations.
These controls pass, including the degree-twenty substitution index two.

A separate deterministic preparation constructs 1170 height-four Lehmer templates at degree 24 and 5532 at degree 30.
The degree-24 counts are 1140 from \(k=1\) and 30 from \(k=2\); the degree-30 counts are 5228, 302 and 2 from \(k=1,2,3\).
The final preparation invocation took approximately 0.043 and 0.550 seconds for those two constructions; these are descriptive generation times, not a controlled sampling comparison or an amortized cost allowance.
Its output is `mathematics/computations/outputs/Yin_J_G0156/cyclotomic_closure_preparation.json`.
The construction uses no additional Mahler evaluation, stochastic proposal or source of new values.
The [independent closure finding](../../../audits/reviews/Yin_R_G1111_v7.md#cyclotomic-closure-review) verifies the complete generator under its stated hypotheses and the actual finite coefficient sets and counts.
It does not establish that closure improves new-core discovery: the preceding acquired-parent control shows that uniform expansion can improve or dilute useful conditional mass depending on the actual parent set.

With Python 3.14.7 and the existing `python-flint==0.9.0` dependency, reproduce from the repository root using fresh output names:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_closure.py self-test
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_closure.py compare --output mathematics/computations/outputs/Yin_J_G0156/cyclotomic_closure_recomputed.json
python -B mathematics/computations/programs/Yin_J_G0156/cyclotomic_closure.py prepare --output mathematics/computations/outputs/Yin_J_G0156/cyclotomic_closure_preparation_recomputed.json
~~~

## Results and limits

The frozen first-pilot laws, evaluator and failure boundary have passed the stated controls and the linked independent implementation review.
The offline census establishes the stated finite-box counts and fixed-law probabilities subject to its reused complete-cover reduction and the arithmetic checks described above.
The short controls demonstrate executable throughput and successful reference recovery, but establish no adaptive advantage and no new small measure.
The completed pilot gives no adaptive advantage under its frozen screen and no new value below \(6/5\).
The reduced-pair-prior live control passes its finite recovery screen, while matching the fixed baseline's target-value count and producing many repeated hits of one known value.
The degree-18/20 comparison also passes its recovery screen, but the exact final-law diagnostic identifies amplification of the Lehmer core accompanied by reduced probability on the other known target core.
Finite comparison cannot resolve the unrestricted Lehmer gap.

<a id="archive-comparison-implementation"></a>
## Implementation of the reference-seeded archive comparison

[archive_sampling.py](archive_sampling.py) implements the [frozen S10 archive comparison](../../../strategies/Yin_S_G0010.md#cyclotomic-archive-comparison) in a separate entry point.
The formal allocation is degrees 24 and 30, arms `fixed`, `direct` and `closure`, seeds 20 through 24, and 20 seconds for each of the 30 serial runs.
Within each degree and seed, the arm order rotates by the degree-index-plus-seed-index modulo three.
The [independent implementation finding](../../../audits/reviews/Yin_R_G1111_v8.md#archive-implementation-review) and [retention finding](../../../audits/reviews/Yin_R_G1111_v8.md#archive-retention-review) pass for the checked implementation and bounded controls.
The unchanged formal protocol has been executed; its observations and current review scope are retained in the [completed comparison](#archive-comparison-results).
The [existing source-backed classification](../Yin_J_G0149/readme.md#core-coverage) covers these degrees, so this comparison calibrates a mechanism in a previously classified range and does not establish a new counterexample search range.

The worker reuses [sampler.py](sampler.py)'s full-measure evaluator, 128-bit arithmetic, threshold decisions, exact-polynomial cache, normalization, factor ledger and evaluation-commit boundary through the unchanged [sampling_runtime.py](sampling_runtime.py).
An explicit wrapper adds archive generation and a seed-aware value ledger before that same commit, without copying or changing the frozen evaluator.
Every run certifies the supplied Lehmer core inside its own deadline, records it as reference information and excludes it from the primary discovery count.
The configuration is flushed before this initialization, so a startup or construction interruption remains observable.
The fixed arm reproduces the old fixed law exactly and constructs no template archive.
The direct arm generates four initial sparse completions at degree 24 and six at degree 30; the closure arm calls the existing exact generator afresh and obtains 1170 and 5532 initial templates.
Neither worker reads a precomputed closure or the second local target core.

Both archive arms use probability one tenth for a uniform draw from the whole box and otherwise choose a core uniformly, a distinct stored template uniformly, and the specified one-to-three-coordinate unit mutation.
Generated templates begin in lexicographic order; new cores follow first committed whole-target encounter order, and newly observed direct templates are appended in encounter order.
Mutation coordinates are sampled without replacement and sorted before assigning independent uniform signs.
Any coefficient box exit returns the unchanged parent without resampling.
Only certified whole targets update an archive, and a new direct core retains its successful template even if its sparse completion set is empty.
Initial construction, later template construction, duplicate handling and seed-aware separation are timed within the run; an uncommitted evaluation cannot enter either the measured yield or the retained final archive.
Per-stage arithmetic and archive costs are retained alongside the overall deadline accounting; stage totals do not purport to equal all serialization, startup and supervision time.

The primary ledger starts with the supplied seed value and counts only additional certified, separated whole-target values.
A different core whose enclosure overlaps the seed or another retained value remains an explicit unresolved equality class.
Seed recovery, core observations and values strictly below the seed enclosure are reported separately.
The two-core [local catalog](inputs/degree_core_mass_states.json) is read only by post-run reporting; the sampler does not implement the separate external completeness argument.
An unrecognized core receives no literature-novelty label.
The allocation screen requires all 30 identities to be valid, closure nonloss by value count against each comparator in at least four paired seeds at each degree, and simultaneous strict improvement over both comparators on the same three or more seeds at one degree.
Equal positive counts use the first nonseed-hit time to determine strict improvement; zero-zero pairs never improve.

[archive_sampling_checks.py](archive_sampling_checks.py) checks the sparse formula independently with polynomial-ring multiplication, exact agreement of the fixed RNG stream, mutation endpoints and boundary returns, seed exclusion, interval-overlap uncertainty, new-core insertion and the empty-sparse-set case.
Mechanical callback controls confirm that factor-only targets do not train either archive and that uncommitted initialization or a computed but uncommitted new core contributes no final state or discovery.
Screen controls cover missing and duplicate identities, failed runs, zero-zero ties, and the distinction between joint wins on the same seeds and wins on different seeds.
Six actual child controls, each capped at two seconds and 257 proposals, completed all 257 proposals with the requested degree, arm and nonformal seed.
All 1542 proposal draws and every committed archive update in those controls reproduce from their journals.

| Control degree | Arm | Seed | Completed proposals | Initialization elapsed, seconds | Seed recoveries | Nonseed values |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 24 | fixed | 100 | 257 | 0.243243 | 0 | 0 |
| 24 | direct | 101 | 257 | 0.253007 | 0 | 0 |
| 24 | closure | 102 | 257 | 0.278741 | 15 | 0 |
| 30 | fixed | 100 | 257 | 0.254227 | 0 | 0 |
| 30 | direct | 101 | 257 | 0.245793 | 0 | 0 |
| 30 | closure | 102 | 257 | 0.799614 | 5 | 0 |

A separate degree-30 closure control with seed 103 reached its two-second deadline with 461 completed proposals and one incomplete proposal, 15 seed recoveries and zero nonseed values.
Its 462 proposal draws and 15 committed archive updates also replay exactly.
A deliberately failed degree-24 direct control with seed 104 stopped after its first proposal, retained zero completed proposals and remained an invalid worker failure.
These eight subprocess controls have 16 seconds of aggregate budget ceilings; the observed counts and initialization times are implementation evidence, not the formal equal-cost comparison.
The first actual check output is `mathematics/computations/outputs/Yin_J_G0156/control_archive_impl_v1_checks.json`.
The core report retains its first strictly-below-seed enclosure even when that core was already observed with a less decisive enclosure.
The final mechanism checks pass in `mathematics/computations/outputs/Yin_J_G0156/control_archive_mechanism_v2_checks.json`.

[archive_sampling_export.py](archive_sampling_export.py) uses only the new 30-run identity set for a formal export and refuses existing destinations.
Its default native outputs are `inputs/archive_comparison.json` and `inputs/archive_witnesses.json`.
It preserves all observed counts, time and configuration fields, seed/nonseed/best/unresolved whole certificates, every committed archive change, observed templates, and separate factor findings with complete parent associations, parent whole measures and charged stage costs.
Deterministic generated template arrays are represented by their exact generator, core, degree, height, ordering and count, so compact retained inputs suffice for RNG and archive reconstruction without the ignored journals.
Every distinct observed archive template is also an exact whole-polynomial witness.
Committed arithmetic errors, unresolved ranking or thresholds, and the final uncommitted proposal retain exact coefficients, proposal and time, reason, and any certificate actually present in the journal.
These retry inputs are separate from the certified witness list and create no extra discovery credit; an unresolved committed threshold retains its original threshold-specific scope.
Synthetic stream controls cover error inputs without a certificate, ranking and threshold uncertainty with an interval, uncommitted proposals with and without an evaluation, and a commit past the deadline.
The exporter has successfully retained and reconstructed the six proposal controls, the deadline control and the failed control in the J output directory, with respectively 75, 29 and 1 exact witnesses and 25, 7 and 0 factor parents.
These are separate export collections, so their witness counts are not asserted to be disjoint.
Partial-result and overwrite guards pass, and no new root certification or sampling is performed by export or archive replay.
The inspected final temporary exports use the `control_archive_export_v3` prefix under the J output directory.
Portable replay includes a retained final proposal even when its write timestamp exceeds the deadline, and reports within-budget proposals separately from reconstructed proposals.
It checks every unresolved or incomplete input's exact prefix and full coefficient vector; the independent retention finding verifies the repaired boundary and rejects altered retry inputs.

Use Python 3.14.7 with the existing `python-flint==0.9.0` dependency and run from the repository root.
Fresh `control_` labels reproduce the bounded controls and their temporary exports:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_checks.py --label control_archive_recheck
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_export.py self-test --label control_archive_export_recheck --control-label control_archive_recheck
~~~

The following commands execute the formal comparison, preserve its native inputs, replay its proposals and separately verify its witnesses:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling.py compare --label s10_archive_comparison
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling.py report --label s10_archive_comparison
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_export.py export --label s10_archive_comparison
python -B mathematics/computations/programs/Yin_J_G0156/archive_sampling_export.py replay-retained mathematics/computations/programs/Yin_J_G0156/inputs/archive_comparison.json
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/archive_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/archive_witness_verification.json
~~~

Archive replay reconstructs proposals and committed templates, while witness verification separately recomputes full measures; neither operation reproduces historical wall-clock timing or adds stochastic discoveries.
An incomplete formal dataset needs explicit `--allow-partial` for export and cannot pass the allocation screen.

<a id="archive-comparison-results"></a>
## Completed reference-seeded archive comparison

All thirty formal identities in [archive_comparison.json](inputs/archive_comparison.json) are valid twenty-second deadline runs, with 600 seconds of sampling budgets and the prescribed rotated serial order.
The separate [archive_witnesses.json](inputs/archive_witnesses.json) retains 3386 distinct exact coefficient vectors needed for whole outputs, cores and factor-parent associations.
These observations were acquired under `s10_archive_comparison`; the source programs and protocol remained those covered by the implementation finding above.
The [independent actual-result finding](../../../audits/reviews/Yin_R_G1111_v9.md#archive-results-review) verifies the complete histories, native evidence, certificate associations and finite screen.
The separate [transition finding](../../../audits/reviews/Yin_R_G1111_v9.md#archive-transition-review) checks the exact parent/child identity below and its actual proposal association.

The five entries in each row below follow seeds 20 through 24.
The supplied Lehmer value is excluded, and a missing first nonseed hit is censored at twenty seconds.

| Degree | Arm | Distinct nonseed target values | First nonseed hit, seconds |
| ---: | --- | --- | --- |
| 24 | fixed | 0, 0, 0, 0, 0 | all censored |
| 24 | direct | 0, 0, 0, 0, 0 | all censored |
| 24 | closure | 1, 1, 0, 1, 0 | 13.4579694, 17.9530574, censored, 3.7654560, censored |
| 30 | fixed | 0, 0, 0, 0, 0 | all censored |
| 30 | direct | 0, 0, 0, 0, 0 | all censored |
| 30 | closure | 0, 0, 0, 0, 0 | all censored |

Closure has five count nonlosses against each comparator at each degree, and three joint strict wins at degree 24 on the same seeds 20, 21 and 23.
It therefore passes the declared finite allocation screen.
All three first nonseed certificates have the already known degree-eighteen core and measure approximately 1.18836814750822358814.
The 183 raw nonseed target hits all recover that one value, while 3635 raw whole-target hits recover the Lehmer seed.
No whole target is absent from the supplied two-core catalog or strictly below the seed enclosure, and no target-value equality remains unresolved.
Separate factors below 6/5 normalize to these same two cores; factor-only hits provide no archive update or primary whole-output credit.
This is a finite representation-diversity gain at degree 24, with no observed nonseed gain at degree 30 and no literature-new measure.

| Degree | Arm | Completed evaluations | Fresh evaluations | Cache hits | Repeated proposals | Neutral outputs | Seed hits | Nonseed hits |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 24 | fixed | 47840 | 47839 | 1 | 1 | 12 | 1 | 0 |
| 24 | direct | 113874 | 51098 | 62776 | 68913 | 2796 | 30 | 0 |
| 24 | closure | 54087 | 52216 | 1871 | 2493 | 112 | 2153 | 183 |
| 30 | fixed | 33897 | 33897 | 0 | 0 | 0 | 0 | 0 |
| 30 | direct | 66747 | 38586 | 28161 | 29964 | 854 | 6 | 0 |
| 30 | closure | 36268 | 36129 | 139 | 174 | 16 | 1445 | 0 |

The total is 352713 completed evaluations, comprising 259765 fresh evaluations and 92948 cache hits, with 101545 repeated proposals and 3790 neutral outputs.
Each run retains one incomplete proposal, giving thirty exact retry inputs and no additional discovery credit.
There are no committed arithmetic-error, ranking-uncertainty or threshold-uncertainty inputs in this dataset.
The 56 separate unresolved factor-value equalities are all certified above 13/10; they concern equality accounting rather than an unresolved 6/5 threshold.
The native input retains 1181 run-level whole-discovery records, 1617 separated factor-discovery records, those 56 unresolved factor records and 1569 complete factor-parent outputs; these are associations within runs, not globally distinct value counts.
Wider-threshold yields, per-run neutral fractions, initialization and stage costs remain in the native rows.
The direct arm's larger completed count includes many cache hits, whereas its fresh count is close to closure's at each degree.
These observations alone do not establish a general throughput or probability ordering.

The degree-24 closure runs initially have 1170 templates and add a 62-template second-core class in the three successful runs.
At degree 30 every closure run retains the original 5532-template seed class alone.
The initial closure commit times range from 0.2861710 to 0.3290282 seconds at degree 24 and from 0.7896699 to 0.8241713 seconds at degree 30, including startup and seed certification as specified.
The actual native archive contains 2656 state-changing committed observations; repeated target hits without a state change have no extra template weight.

### One actual inter-core mutation

In degree 24, seed 20, proposal 7209, the closure arm selected
\[
 P(z)=z^{24}-z^{14}-z^{12}-z^{10}+1
\]
and changed free coordinate 2, indexed from zero, by minus one.
The evaluated child is \(Q(z)=P(z)-z^3-z^{21}\), with the second-core certificate and commit time 13.457969400013098 seconds.
Writing \(F\) for the normalized Lehmer polynomial and \(H\) for the normalized degree-eighteen polynomial in the retained catalog, direct coefficient multiplication gives
\[
 P(z)=F(-z^2)\Phi_{12}(z),\qquad
 Q(z)=H(z)\Phi_3(z)\Phi_{12}(z),
\]
where \(\Phi_3=1+z+z^2\) and \(\Phi_{12}=1-z^2+z^4\).
This parent belongs to the complete closure but is absent from the direct arm's initial sparse completions.
The mutation breaks the substitution symmetry while retaining the neutral divisor \(\Phi_{12}\); it reaches the known degree-eighteen core rather than a new degree-24 primitive core.
The exact coefficients, seed, proposal and archive replay preserve the observed transition without treating this retrospective example as a preselected training input or a universal explanation of every successful run.

### Retained replay and verification

Portable replay reconstructed all 352743 proposal vectors, all 2656 state changes and all thirty retry inputs from the native comparison, without the original journals or new root calculations.
The corresponding output is `mathematics/computations/outputs/Yin_J_G0156/archive_retained_replay.json`.
Separate recomputation of all 3386 witness measures completed and is retained in `mathematics/computations/outputs/Yin_J_G0156/archive_witness_verification.json`.
Those deterministic checks do not reproduce historical timing or constitute another stochastic experiment.
The actual-result finding also checks the certificates and every retained role, run and parent association against the original committed observations, within the previously reviewed complete-measure method's scope.

<a id="uniform-parent-preparation"></a>
## Preparation for larger closure classes

The separate [uniform-parent construction](parent_sampling.md) replaces full template enumeration by exact integer multiset counting, rank selection and a final coefficient-height rejection.
Its complete probability argument, attempt-boundary limits, author controls and degree-56/80 parent-only feasibility results remain at that linked home.
Its [independent law finding](../../../audits/reviews/Yin_R_G1111_v10.md#parent-law-review) and [finite-control finding](../../../audits/reviews/Yin_R_G1111_v10.md#parent-controls-review) cover the repaired standalone helper and actual parent-only evidence.
It is not part of the frozen archive comparison; the later degree-56 composition has its own [independent finding](../../../audits/reviews/Yin_R_G1111_v11.md#primitive-implementation-review).
Every accepted parent still represents the supplied core and has its unchanged Mahler measure; the construction supplies no new primitive core or counterexample.

<a id="primitive-core-implementation"></a>
## Degree-56 primitive-core implementation

The [dedicated implementation record](primitive_core_sampling.md) owns the composed worker, exact structural diagnostics, all-attempt retention, portable replay, actual five bounded controls and prepared formal commands.
The [independent composition finding](../../../audits/reviews/Yin_R_G1111_v11.md#primitive-implementation-review) checks the implementation and actual bounded controls, including completed, deadline-censored and deliberately failed cases.
The [independent retention finding](../../../audits/reviews/Yin_R_G1111_v11.md#primitive-retention-review) checks the corrected summary-versus-journal gate, all original inputs, portable replay and witness associations.
These findings establish no formal-comparison outcome or comparative discovery advantage.
The frozen direct-versus-DP comparison remains at [S10](../../../strategies/Yin_S_G0010.md#primitive-core-comparison), with irreducible noncyclotomic degree-56 whole outputs and their complete measures as the primary class.
Its [completed formal comparison](primitive_core_sampling.md#primitive-comparison-results) retains all ten valid runs, the zero target yields, primitive minima, exact witnesses, costs and full native evidence.
The [separate actual-result finding](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-review) verifies those formal observations, and its [retention](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-retention-review) and [interpretation](../../../audits/reviews/Yin_R_G1111_v12.md#primitive-results-interpretation-review) findings cover the native payload, storage extension, reported tables and fixed-support deduction.

The [post-hoc neutral-multiplicity and exterior-root diagnostic](primitive_root_diagnostics.md) reuses the original committed observations and root certificates to compare full-measure contributions within explicitly matched strata.
Its programs, native input, complete denominators, retained minimum witnesses and approximate-share conventions remain at that linked home.
Its [independent interface finding](../../../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-implementation-review) and [actual descriptive-result finding](../../../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-results-review) verify the full fixed extraction and reported statistics, including the actual decimal-printing path and all multiplicities.
It supplies neither a new frozen performance metric nor a validated replacement sampling law.
