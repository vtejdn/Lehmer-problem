---
author: Yin
---

# Independent review of the degree-18 and degree-20 sampling comparison

## Arrangement and exact inputs

At 2026-11-09T20:12, a reviewing agent acting for Yin completed the degree-specific implementation, actual-evidence and retention checks below.
The reviewer did not develop the new runtime, degree wrapper, exporter or result prose, and supplied no repair to those author programs.
The review began from the fixed sources and declared S10 protocol; bounded implementation controls were completed before the formal comparison.
After completion, the reviewer reconstructed the actual original journals and summaries, then checked their native export and the final result wording.
Author-reported counts and successes were not substituted for those checks.
The reviewer retained its own necessary checking programs and generalized their earlier degree-14 helpers through explicit parameters, without changing the author implementation or the earlier helpers' default degree-14 scope.

The implementation inputs are [degree_validation.py](../../computations/programs/Yin_J_G0156/degree_validation.py), [sampling_runtime.py](../../computations/programs/Yin_J_G0156/sampling_runtime.py), [degree_validation_checks.py](../../computations/programs/Yin_J_G0156/degree_validation_checks.py), and the degree-specific section of [S10](../../strategies/Yin_S_G0010.md#degree-validation).
The unchanged A law in [prior_strength_live.py](../../computations/programs/Yin_J_G0156/prior_strength_live.py) reuses the exact update finding in [v4](Yin_R_G1111_v4.md#live-implementation-review).
The unchanged [sampler.py](../../computations/programs/Yin_J_G0156/sampler.py) worker, complete-root evaluator, normalized cores and conservative value accounting reuse the applicable [v1 finding](Yin_R_G1111_v1.md#sampler-implementation-review).
The new degree dispatch, runtime failure handling, identity enumeration, aggregation and actual degree-18/20 evidence are checked here.

The original observations are every `mathematics/computations/outputs/Yin_J_G0156/s10_degree_validation_dDEGREE_VARIANT_sSEED.json` and corresponding `.jsonl`, for exactly `DEGREE` in `18,20`, `VARIANT` in `fixed,A`, and `SEED` in `10,11,12,13,14`, together with `s10_degree_validation_degree_comparison.json`.
The fixed native inputs are [degree_comparison.json](../../computations/programs/Yin_J_G0156/inputs/degree_comparison.json) and [degree_witnesses.json](../../computations/programs/Yin_J_G0156/inputs/degree_witnesses.json).
The reviewer read [degree_validation_export.py](../../computations/programs/Yin_J_G0156/degree_validation_export.py) and its directly reused compaction, committed-parent and reference interfaces in [prior_strength_live_export.py](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py).
These observations remain separate from the original 45-run pilot and the subsequent degree-14 live comparison.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Degree implementation](#degree-implementation-review) | independently reviewed |
| [Completed degree evidence](#degree-results-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Degree implementation](#degree-implementation-review) | [S10 degree protocol](../../strategies/Yin_S_G0010.md#degree-validation) | Degrees 18 and 20, fixed/A, seeds 10 through 14, fresh runs, rotating serial order, ten-second budgets and the exact two-level allocation screen. |
| [Degree implementation](#degree-implementation-review) | [Degree wrapper](../../computations/programs/Yin_J_G0156/degree_validation.py) | Entire new entry point, actual degree/variant/seed dispatch, configuration, degree validity, twenty-run schedule, statistics and completeness-gated screen. |
| [Degree implementation](#degree-implementation-review) | [Shared runtime](../../computations/programs/Yin_J_G0156/sampling_runtime.py) | Actual child invocation and law installation, frozen-worker reuse, supervised startup/cap/failure paths, retained configuration, failure evidence and actual absent-hit censor. |
| [Degree implementation](#degree-implementation-review) | [Native bounded controls](../../computations/programs/Yin_J_G0156/degree_validation_checks.py) | Source inspection and independent execution under `independent_degree_preflight`, including four actual 257-proposal subprocesses, deadline and injected-failure controls, exact law replay and screen boundaries. |
| [Degree implementation](#degree-implementation-review) | [Prior live implementation finding](Yin_R_G1111_v4.md#live-implementation-review) | The unchanged A pair/singleton update and exact integer sampling semantics; no new degree-14 performance review. |
| [Degree implementation](#degree-implementation-review) | [Frozen sampler](../../computations/programs/Yin_J_G0156/sampler.py) | Unchanged complete-measure evaluator, worker, per-run LRU, journals, normalized cores, elite selection, thresholds and conservative whole/factor ledgers. |
| [Degree implementation](#degree-implementation-review) | [Earlier implementation finding](Yin_R_G1111_v1.md#sampler-implementation-review) | Reused full-root certification and unchanged original-worker interfaces at their earlier checked scope. |
| [Degree implementation](#degree-implementation-review) | [Degree description](../../computations/programs/Yin_J_G0156/readme.md#degree-validation) | The new implementation, bounded controls, twenty-run schedule and declared screen, before the completed-result subsection. |
| [Completed degree evidence](#degree-results-review) | [S10 degree protocol and result](../../strategies/Yin_S_G0010.md#degree-validation) | Its unchanged screen and completed degree-specific outcome; the following core-mass diagnostic is excluded. |
| [Completed degree evidence](#degree-results-review) | [Degree results and retention prose](../../computations/programs/Yin_J_G0156/readme.md#degree-validation) | The completed comparison and retained-observation subsections, all seed and aggregate tables, exact-core interpretation, factor/whole separation and replay limits; the pending-review navigation sentence is not an adoption decision. |
| [Completed degree evidence](#degree-results-review) | [Native observations](../../computations/programs/Yin_J_G0156/inputs/degree_comparison.json) | All twenty original configurations, counts, times, validity/censor fields, first-hit proposal fields, compact whole/best/equality records, separate factors and committed parents. |
| [Completed degree evidence](#degree-results-review) | [Native witnesses](../../computations/programs/Yin_J_G0156/inputs/degree_witnesses.json) | All 1575 exact polynomial arrays, unique IDs, per-run memberships, role sets and complete-measure certificate support. |
| [Completed degree evidence](#degree-results-review) | [Degree exporter](../../computations/programs/Yin_J_G0156/degree_validation_export.py) | The actual full export, explicit partial-input boundary, original-field preservation and twenty-identity scope. |
| [Completed degree evidence](#degree-results-review) | [Shared export interfaces](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py) | Reused compaction, committed-parent joins, factor multiplicity and exact witness references in this export. |
| [Completed degree evidence](#degree-results-review) | [Degree implementation](#degree-implementation-review) | Checked proposal/update, timing, validity, deduplication and screen semantics applied to the actual twenty histories. |

<a id="degree-implementation-review"></a>
## Degree implementation finding

The verdict is **PASS for the new degree/runtime interfaces and their bounded controls**.
This finding permitted the declared comparison and supplied no performance conclusion before its actual runs.
No author-program repair was required during this review.

The degree entry point passes the actual degree, variant and seed to its own `_worker` subprocess.
The shared runtime installs the selected law before the frozen worker constructs it and uses the supplied degree in the actual worker arguments.
A retains its checked pair update
\[
q'_s=\frac45q_s+\frac15\frac{c_s+1/81}{m+1}
\]
for a nonempty elite set of size \(m\), with the original singleton update and unchanged empty-batch behavior.
Degree 18 has block widths \((2,2,2,2,1)\), and degree 20 has \((2,2,2,2,2)\).
The initialization, global exploration, exact integer categorical draws, batch size and elite selection are unchanged.
Each child constructs a fresh law and cache.

The reviewer executed all four degree/variant 257-proposal controls with seed 10 and replayed every actual proposal.
Both A controls made exactly one update, checked against independent Fraction arithmetic; fixed made none.
The controls checked the resulting complete polynomial degree as well as the different block layouts.
The actual 0.75-second deadline control and injected worker failure exercised the new runtime's supervision.
The failed degree-18 fixed control retained its first proposal but no completed evaluation, with actual absent-hit censor approximately 0.255506 seconds, below the requested two seconds.

The reviewer additionally checked all twenty unique identities and their exact degree-index-plus-seed-index rotation, foreign protocol/degree/variant/seed rejection, short and proposal-limited runs, controlled failures and clean early exits.
A separately mocked `Popen` startup failure verified the actual degree-20/A/seed-14 command and its invalid result with an actual short observed censor.
That mock started no child and created no experimental journal.
The actual short and failed controls are ineligible for the formal comparison and cannot pass either screen.
Missing or duplicate identities cannot make the comparison complete.
The four-versus-three boundary, zero-hit ties and equal-positive-count first-hit cases were checked against the declared predicate.

The experiment enumerates exactly twenty ten-second identities, first degree 18 and then degree 20, serially with the stated rotation.
Only valid full ten-second runs enter the degree comparison statistics and screen.
A passing report requires at least four nonlosses at each degree and at least four improvements at one degree, with all twenty valid identities present.
An improvement is a larger target count or, at equal positive count, an earlier first hit; two zero counts do not qualify.
Startup, proposal generation, evaluation, normalization, duplicate handling, update and journal work share the supervised cap.
Only committed on-time evaluations contribute yield.
Supervisor termination overhead can extend physical elapsed time slightly; the cap is not a claim that every in-flight machine instruction stops at precisely ten seconds.

<a id="degree-results-review"></a>
## Completed degree evidence finding

The verdict is **PASS for the completed finite comparison, its retained witnesses and its qualified interpretation**.
The actual comparison **passes its predeclared allocation screen**.
It establishes the stated recovery performance on the reused boxes, without establishing a new target value, statistical significance, unseen-benchmark performance or an unrestricted Lehmer result.

### Actual histories and complete-measure evidence

All twenty required identities have valid deadline termination, ten-second budgets, no proposal-count stop and no worker failure.
The configurations retain the declared 128-bit evaluator, \(10^{-12}\) ranking radius, 256-proposal batches and 4096-entry per-run LRU.
They completed 209433 proposals and left twenty unfinished proposals.
The completed totals are 147858 fresh evaluations, 61575 cache hits, 61816 repeated proposals, 12308 neutral outputs and 525 A updates.
There are no unresolved completed ranking scores or threshold decisions.
All counted completion timestamps are at most ten seconds, representing a 200-second experimental ceiling.
The observed supervisor excess ranges from approximately 0.009074900008 to 0.024042799982 seconds and adds no counted candidate evaluation.

The reviewer streamed all twenty original journals and replayed every readable proposal from its actual seeded law, including the readable unfinished proposals.
The checks covered sequential proposal/commit identities, integer-box membership, full reciprocal degree, cache/repeat membership, exact normalized cores, thresholds, stage totals, best outputs and first-hit times.
Distinct whole values and separate factor values were independently reconstructed with exact rational interval endpoints and conservative identity rules.
All 525 committed A updates agreed with the actual elite metadata and with an independent Fraction calculation for every state probability.
The reconstructed summaries agree with the original reports and all retained observation fields.
The first-hit proposal and initial-batch indicators were checked against actual first-hit journal events, independently of the report's discovery-list lookup.

All 1575 retained exact polynomial inputs have complete-measure certificate support.
The reviewer reused 658 previously checked certificates for identical coefficient arrays from the original-pilot and degree-14 live checks and computed the remaining 917 certificates in this degree review.
The complete evaluator includes all roots and their multiplicities, under the unchanged v1 arithmetic contract.
The retained exact intervals agree with the replayed certificates, normalized cores and threshold decisions.
Strict hits have certified lower endpoint above one and upper endpoint below their rational threshold.
The separated whole-value representatives have disjoint intervals; no unresolved whole-value equality was promoted to a new value.

### Screen and interpretation

The primary distinct-value outcomes, in seed order 10 through 14, are:

| Degree | Fixed counts in \(1<M<6/5\) | A counts |
| ---: | --- | --- |
| 18 | 0, 1, 1, 1, 1 | 1, 1, 1, 1, 1 |
| 20 | 0, 0, 1, 0, 0 | 1, 1, 1, 1, 1 |

Each degree has five target-count nonlosses and four improvements, so both levels of the complete comparison's screen hold.
At degree 18, seed 10 improves the count and seeds 11, 12 and 13 improve the first-hit time at equal positive count; seed 14 has a later A hit.
At degree 20, seeds 10, 11, 13 and 14 improve the count; seed 12 has a later A hit at equal positive count.
Missing fixed hits are censored at ten seconds and are not measured first-hit times of ten seconds.
The reviewer recomputed all displayed seed counts/times, median/range statistics and aggregate counts from the original summaries and journal reconstruction.

A's first-hit proposal indices are \((2150,620,778,1370,2635)\) at degree 18 and \((1559,2492,1377,2386,900)\) at degree 20.
Every one follows the first update boundary of 256 proposals.
This avoids a pre-update timing attribution for these actual hits, but temporal order alone does not isolate the causal contribution of adaptation.

The degree/arm totals are:

| Degree | Arm | Completed | Fresh complete | Cache hits | Repeated proposals | Neutral | Raw whole-target hits | Updates |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18 | Fixed | 40569 | 40515 | 54 | 70 | 123 | 7 | 0 |
| 18 | A | 77184 | 39551 | 37633 | 37821 | 6856 | 231 | 300 |
| 20 | Fixed | 33595 | 33592 | 3 | 3 | 37 | 1 | 0 |
| 20 | A | 58085 | 34200 | 23885 | 23922 | 5292 | 338 | 225 |

A's per-run repeated-proposal fractions range from approximately 47.75 to 50.15 percent at degree 18 and from 37.51 to 44.26 percent at degree 20, with completed proposals as denominator.
Its corresponding neutral fractions range from approximately 8.42 to 9.38 percent and from 7.96 to 10.62 percent.
The higher throughput and raw target-hit totals therefore include substantial repeat/cache reuse.

All 577 raw whole-target hits have the known normalized Lehmer core
\[
(1,-1,0,1,-1,1,-1,1,0,-1,1)
\]
in ascending order.
The best complete positive measure has retained enclosure
\[
[1.176280818259917506544070338474035051\mathbin{\pm}5.05\times10^{-37}],
\]
with exact dyadic endpoints in the native certificates.
No whole output supplies a second target value or the reference value near 1.1883681475.
The seventeen separate-factor target records are the Lehmer polynomial or its substitution \(x\mapsto-x\), with the same measure.
Five occur in complete outputs outside the target interval and contribute no primary whole-output hit.
The widened threshold tables report conservative within-run value counts, not an across-run union or a new lower-measure claim.
Both degrees are reused benchmarks.
The outcome supports bounded recovery of a known value and leaves target-value diversity and the unrestricted gap obligation unchanged.

### Native retention

The retained comparison contains 1691 whole-value discovery records, all twenty best-output records, 1849 separate-factor discovery records, 66 unresolved factor-value equality associations, and 1844 committed factor-parent outputs.
The 66 factor equality uncertainties all lie above \(13/10\); they concern value identity in the wider band and are distinct from unresolved score or threshold decisions.
All 1915 factor associations, including those uncertainties, were matched to their original factors, event times, exact committed parents and replayed parent factorizations with multiplicity.
A factor certificate describes the measure of that single factor, while its exponent records its multiplicity in the complete parent.
Separate-factor results never increase the whole-output yield.

All 1575 witness IDs, exact arrays, role sets and per-run memberships were reconstructed from the retained records and agree with the witness input.
The exporter preserves the new twenty-identity scope, explicit partial-input boundary and original observations.
The review checked the actual full export against the original data.
The separate author export self-test's source and saved result were inspected, including its four short controls and failed-worker control, but that self-test was not independently rerun.
The independent full-data association and certificate checks establish the completed export finding above.

The retained inputs are adequate to inspect the reported finite observations and replay their selected mathematical witnesses.
They intentionally do not contain every proposal event.
Without the original journals, the compact files do not regenerate historical wall-clock prefixes, seeded proposal/update histories or the same timing outcome.
Those timestamps remain retained observations rather than reproducible stochastic laws.

## Native reproduction and limits

The reviewer-owned preflight source is [independent_degree_review.py](../../computations/programs/Yin_J_G0156/checks/independent_degree_review.py).
The actual-history and retention source is [independent_degree_results.py](../../computations/programs/Yin_J_G0156/checks/independent_degree_results.py).
It reuses the committed-event and certificate helpers in [independent_live_results.py](../../computations/programs/Yin_J_G0156/checks/independent_live_results.py) with explicit degree, protocol, seed, variant, validity and expected-run parameters.
The earlier helper defaults remain degree 14 and fifteen runs.
The exact Fraction and rational-ledger dependencies remain [independent_live_review.py](../../computations/programs/Yin_J_G0156/checks/independent_live_review.py) and [independent_pilot_review.py](../../computations/programs/Yin_J_G0156/checks/independent_pilot_review.py).
The bounded preflight, full twenty-history reconstruction and final fixed-description mode were each actually executed successfully.
The final description-only addition was run separately after the full replay and does not alter its replay or certificate calculation.

Generated records are `independent_degree_preflight_review.json`, `independent_degree_results_review.json` and `independent_degree_witness_verification.json` under `mathematics/computations/outputs/Yin_J_G0156/`.
The independently executed bounded child controls use `independent_degree_preflight` and remain separate from the formal observations.

The following normalized commands use Python 3.14.7 with `python-flint==0.9.0` available through the environment or `PYTHONPATH`, from the repository root.
In the actual environment, FLINT is installed under `mathematics/computations/outputs/Yin_J_G0156/packages`.
The first command needs a fresh label if its control outputs already exist; use the same chosen label in the following preflight command.

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/degree_validation_checks.py --label independent_degree_preflight
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_degree_review.py --label independent_degree_preflight
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_degree_results.py --reuse-verification mathematics/computations/outputs/Yin_J_G0156/independent_pilot_witness_verification.json mathematics/computations/outputs/Yin_J_G0156/independent_live_witness_verification.json
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_degree_results.py --retained-description-only
```

The third command is the actual selected-certificate reuse command and requires the original twenty JSON/JSONL pairs, original comparison output and the two selected earlier verification files.
It starts no sampling run.
Omit `--reuse-verification` and its paths to recompute all selected certificates without those earlier verification files.
The fourth command needs only the native comparison and checks the final descriptive counts and per-seed wider-threshold data; it is not journal or certificate replay.

Without the ignored journals, standalone certificate replay remains available from the fixed witness input:

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/degree_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/degree_witness_verification.json
```

FLINT/Arb remain trusted libraries at the earlier v1 boundary.
The reviewer reran no formal twenty-run experiment and changed no implementation, sampling setting, screen threshold or author result.
The earlier pilot and degree-14 results remain governed by their own fixed reviews.
S10's subsequent `#core-mass-follow-up`, any new core-mass diagnostic and any later experiment are outside both findings here.
