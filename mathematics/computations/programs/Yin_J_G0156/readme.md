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

## Files

| File | Role |
| --- | --- |
| [sampler.py](sampler.py) | Exact sampling laws, full-root certificates, bounded worker/supervisor, summaries, and separate replay. |
| [check_failure_boundary.py](check_failure_boundary.py) | Regression checking that failed or early runs stay visible and cannot become a complete pilot or enter valid-run comparisons. |
| [checks/independent_pilot_review.py](checks/independent_pilot_review.py) | Retained reviewer checks of fixed pilot observations and witnesses, with a separate optional reconstruction of the original journals. |
| [law_mass_diagnostic.py](law_mass_diagnostic.py) | Separate post-run replay of committed updates and approximate conditional target probabilities under the resulting laws. |
| [prior_strength_control.py](prior_strength_control.py) | Exact fixed-elite comparison changing only the pair pseudocount total from 81 to 1, with no new proposals or root calculations. |
| [baseline_mass.py](baseline_mass.py) | Exact offline box counts and uniform/static-law target probabilities, using the [J147 cover](../Yin_J_G0147/newton.cjs) and the [J144 Graeffe transform](../Yin_J_G0144/pilot.py). |
| [inputs/calibration_witnesses.json](inputs/calibration_witnesses.json) | Exact degree-14 polynomial recovered during the short adaptive implementation check, retained for independent replay. |
| [inputs/pilot_comparison.json](inputs/pilot_comparison.json) | All 45 observed run summaries, times, costs, compact whole-value certificates, separate factor records and unresolved equalities. |
| [inputs/pilot_witnesses.json](inputs/pilot_witnesses.json) | The 1331 exact polynomial inputs needed to replay the retained pilot discoveries, best outputs and unresolved equality cases. |
| [inputs/pilot_law_mass.json](inputs/pilot_law_mass.json) | The 15 post-run conditional target-mass diagnostics, explicitly approximate and separate from discovery yield. |
| [inputs/prior_strength_elites_d14.json](inputs/prior_strength_elites_d14.json) | The 13 checked elite batches from the separate 3432-proposal calibration prefix, retaining 337 seven-coefficient vectors and their native source parameters. |
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

## Results and limits

The implemented laws, evaluator and failure boundary have passed the stated controls and the linked independent implementation review.
The offline census establishes the stated finite-box counts and fixed-law probabilities subject to its reused complete-cover reduction and the arithmetic checks described above.
The short controls demonstrate executable throughput and successful reference recovery, but establish no adaptive advantage and no new small measure.
The completed pilot gives no adaptive advantage under its frozen screen and no new value below \(6/5\).
The pair-pseudocount calculation identifies a concrete update mechanism to test separately before any larger search.
Finite comparison cannot resolve the unrestricted Lehmer gap.
