---
author: Yin
---

# Independent review of the reduced-pair-prior live control

## Arrangement and exact inputs

At 2026-11-09T19:42, a reviewing agent acting for Yin completed the implementation, actual-result and retention checks below.
The reviewer did not develop the live wrapper, its update law, exporter or result prose, and supplied no repair to those programs.
The review began from the actual fixed programs and S10 protocol, with bounded controls completed before the formal experiment.
After the experiment, the reviewer formed the result findings directly from its 15 original summaries and journals before checking the final native export and README interpretation.
Author-reported successes were not substituted for those reproductions.

The implementation inputs are [prior_strength_live.py](../../computations/programs/Yin_J_G0156/prior_strength_live.py), [its bounded controls](../../computations/programs/Yin_J_G0156/prior_strength_live_checks.py), and the unchanged [sampler.py](../../computations/programs/Yin_J_G0156/sampler.py).
The exact-law control dependency is limited to `initial_law` and `update_law` in [prior_strength_control.py](../../computations/programs/Yin_J_G0156/prior_strength_control.py), with the [13 elite batches](../../computations/programs/Yin_J_G0156/inputs/prior_strength_elites_d14.json) used as finite arithmetic control data.
This does not independently adopt the whole earlier fixed-elite mechanism experiment or its probability conclusions.
The full-root evaluator and unchanged original-worker interfaces reuse the applicable [v1 implementation finding](Yin_R_G1111_v1.md#sampler-implementation-review).

The actual original data are every `mathematics/computations/outputs/Yin_J_G0156/s10_prior_live_d14_VARIANT_sSEED.json` and corresponding `.jsonl`, for exactly `VARIANT` in `fixed,O,A` and `SEED` in `5,6,7,8,9`, together with `s10_prior_live_live_comparison.json`.
The retained inputs are [prior_live_comparison.json](../../computations/programs/Yin_J_G0156/inputs/prior_live_comparison.json) and [prior_live_witnesses.json](../../computations/programs/Yin_J_G0156/inputs/prior_live_witnesses.json).
The reviewer read the actual [exporter](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py) and checked its completed export against those original data.
All of these inputs belong to the separate degree-14 live control, not the original 45-run pilot.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Live implementation](#live-implementation-review) | independently reviewed |
| [Completed live evidence](#live-results-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Live implementation](#live-implementation-review) | [S10 live protocol](../../strategies/Yin_S_G0010.md#prior-strength-follow-up) | Degree 14, seeds 5 through 9, fixed/O/A, the pair update, unchanged worker conventions, 15 ten-second budgets and the original continuation predicate. |
| [Live implementation](#live-implementation-review) | [Live wrapper](../../computations/programs/Yin_J_G0156/prior_strength_live.py) | Entire wrapper: exact changed law, actual child-process dispatch, run validation, timing/failure handling, rotating serial schedule, aggregation and completeness-gated screen. |
| [Live implementation](#live-implementation-review) | [Native controls](../../computations/programs/Yin_J_G0156/prior_strength_live_checks.py) | Source inspection and independent execution of the bounded controls under the separate `independent_live_preflight` label. |
| [Live implementation](#live-implementation-review) | [Fraction reference functions](../../computations/programs/Yin_J_G0156/prior_strength_control.py) | Only `initial_law` and `update_law` as directly checked arithmetic dependencies; no new review of that program's complete fixed-elite experiment. |
| [Live implementation](#live-implementation-review) | [Control elite input](../../computations/programs/Yin_J_G0156/inputs/prior_strength_elites_d14.json) | Actual vectors used for the 13-snapshot exact-arithmetic control; no inference of new live outcomes from those vectors. |
| [Live implementation](#live-implementation-review) | [Frozen sampler](../../computations/programs/Yin_J_G0156/sampler.py) | Reused `Law`, worker, evaluator, journal, LRU, summary and run-validity interfaces; changed dispatch and ten-second eligibility checked here. |
| [Live implementation](#live-implementation-review) | [Earlier implementation finding](Yin_R_G1111_v1.md#sampler-implementation-review) | Unchanged complete-measure certification, normalized cores, conservative value accounting and original worker semantics. |
| [Live implementation](#live-implementation-review) | [Live description](../../computations/programs/Yin_J_G0156/readme.md#prior-strength-live) | Entire description of the separate implementation, controls, 150-second schedule and fixed screen. |
| [Completed live evidence](#live-results-review) | [S10 live protocol and result](../../strategies/Yin_S_G0010.md#prior-strength-follow-up) | The unchanged declared screen and its actual completed degree-14 outcome; the following degree-validation plan is excluded. |
| [Completed live evidence](#live-results-review) | [Completed result prose](../../computations/programs/Yin_J_G0156/readme.md#prior-live-results) | Entire result section, all three tables, seed-five timing qualification, repeat/cache interpretation and fixed retention claims. |
| [Completed live evidence](#live-results-review) | [Native observations](../../computations/programs/Yin_J_G0156/inputs/prior_live_comparison.json) | All 15 observations, original configurations/counts/times, compact complete-output certificates, separate factors, committed parent outputs and witness references. |
| [Completed live evidence](#live-results-review) | [Native witnesses](../../computations/programs/Yin_J_G0156/inputs/prior_live_witnesses.json) | All 449 exact polynomials, distinct witness IDs, roles, run memberships and complete-measure certificate support. |
| [Completed live evidence](#live-results-review) | [Exporter](../../computations/programs/Yin_J_G0156/prior_strength_live_export.py) | Interfaces used for this actual completed export, including joins to committed factor parents and the distinction between a single factor's measure and its multiplicity in the parent. |
| [Completed live evidence](#live-results-review) | [Live implementation](#live-implementation-review) | Checked proposal/update, timing, validity, deduplication and screening semantics applied to the actual histories. |

<a id="live-implementation-review"></a>
## Live implementation finding

The verdict is **PASS for the specified separate live implementation and its bounded controls**.
This finding was sufficient to permit the declared experiment; it supplied no performance conclusion before the actual runs.

### Exact update and child process

For a pair block, let its old integer weights be \(w_s\), with total \(W\), and let \(c_s\) count the selected elite states in a nonempty elite set of size \(m\).
A constructs \(b_s=81c_s+1\), whose total is \(B=81(m+1)\), and replaces the weights by \(4w_sB+b_sW\), followed only by a common gcd reduction.
Their total before reduction is \(5WB\), so the represented probabilities are exactly
\[
 q'_s=\frac45q_s+\frac15\frac{c_s+1/81}{m+1}.
\]
For the singleton block the counts remain \(c_s+1\) with total \(m+9\), exactly the original singleton rule.
Empty eligible batches leave the distribution unchanged.
Initialization, the one-tenth global uniform exploration mixture, pair/singleton block layout and integer categorical draw method are inherited unchanged.
The elite selection still deduplicates eligible normalized cores, applies the same score/tuple ordering, and selects \(\lceil u/10\rceil\) representatives from \(u\le256\) eligible cores.

`run_once` dispatches this file's `_worker` with the actual variant and seed.
Inside that child, the selected law class replaces `sampler.Law` before the frozen worker constructs its law.
A configuration label is therefore not the only evidence of the changed implementation.
The reviewer executed three 257-proposal controls, one per variant, and replayed their actual child proposals and update records.
O and A agreed through proposal 256 and differed at proposal 257 exactly as their reconstructed laws prescribed.
All 13 fixed-data A update snapshots also matched the directly inspected Fraction reference.
Additional reviewer-owned Fraction controls checked empty, one-, two- and 26-elite updates, positive normalization, singleton behavior, representative ties and the maximum elite count.

### Budgets, failure and aggregation

The wrapper has its own seeds 5 through 9, fixed/O/A identities, serial rotation, ten-second limit and fifteen-run completeness test.
It does not invoke the original pilot's seed enumeration or 45-run completeness rule.
Each new worker has a fresh law and cache, and its startup, proposal generation, evaluation, normalization, duplicate handling, update and journal work share the supervised cap.
Only committed on-time evaluations enter the reported yield.
As with the frozen implementation, supervisor cleanup can extend physical wall-clock duration slightly; no guarantee that every in-flight machine instruction stops at exactly ten seconds is asserted.

The reviewer independently executed the 0.75-second deadline control and an injected failure after the first proposal.
The failed run retained one proposal and no completed evaluation, and its absent-hit censor was its actual observed duration, approximately 0.257389 seconds, rather than the requested two seconds.
Independent in-memory checks also covered clean early exit, proposal-count termination, a short valid deadline, wrong protocol/degree/seed, and a controlled-failure configuration.
The short controls remain ineligible for the formal live comparison.
The actual report excludes their outcomes from live comparison statistics and cannot give an incomplete control a passing screen.
Missing identities, duplicate identities, three-versus-four qualifying seeds, zero-hit ties and equal-positive-count timing cases were checked at the declared predicate.

<a id="live-results-review"></a>
## Completed live evidence finding

The verdict is **PASS for the completed finite comparison, its retained mathematical witnesses and its qualified interpretation**.
The actual comparison **passes its predeclared resource-allocation screen**.
It establishes recovery behavior on the reused degree-14 benchmark, not a new target value, statistical significance, unseen-degree performance or an unrestricted Lehmer result.

### Actual journals, laws and certificates

All 15 required identities have valid deadline termination, ten-second budgets and no proposal-count stop.
The original configurations match the declared 128-bit evaluator, \(10^{-12}\) ranking radius, 256-proposal batches and 4096-entry per-run LRU cache.
There were 284130 completed proposals and 14 unfinished proposals.
No completed evaluation had an unresolved ranking, threshold or numerical failure.
The represented experimental ceiling is 150 seconds.
All counted completion timestamps are at most ten seconds; observed supervisor excess ranges from approximately 0.0099341 to 0.0236533 seconds.

The reviewer streamed all 15 original journals and replayed every readable proposal from its actual seeded law, including the readable unfinished proposals.
Sequential identities, coefficient-box membership, on-time commits, repeated proposals and cores, cache membership, stage totals, raw thresholds, distinct whole values, separate factor values, best retained outputs and first-hit times were checked against the original summaries.
Conservative value identities were independently reconstructed with exact rational endpoints and normalized cores.
All 866 committed adaptive updates were checked against the recorded elite metadata and, state by state, against an independent Fraction update calculation.
The resulting summaries, original comparison statistics and native observations all agree.

The reviewer first recomputed the 366 selected complete-output and factor witnesses available from the original summaries and first-hit records.
The final export additionally retains full parents of the selected factor discoveries.
Its 83 additional polynomial inputs were then certified, reusing the already checked 366 certificates, for 449 checked polynomials in total.
The complete evaluator includes every root with multiplicity and all exterior factors under the unchanged v1 arithmetic contract.
Every compact whole/factor interval agrees with a fresh enclosing certificate, every strict hit is certified above one and below its rational threshold, and the claimed separated whole-value representatives have disjoint intervals.

The native observations preserve the original configuration, count, cost, rate, timing and validity fields.
All 799 retained factor-parent outputs were matched to their actual committed journal events, and all 896 retained factor associations matched the original factors, timestamps and fresh parent factorizations, including multiplicity.
Each factor certificate describes that single factor's measure; its exponent records the factor's multiplicity in the complete parent.
All 449 witness IDs, exact coefficient arrays, role sets and run memberships were reconstructed from the per-run records and agree with the witness input.
Separate-factor discoveries never increase whole-output yield.
This is adequate retention of the reported finite observations and their selected mathematical evidence.
It does not claim to retain every proposal event or to reconstruct the same wall-clock prefix from a seed without the original journals.

### Screen, timing and mechanism limits

The primary distinct-value outcomes, in seed order 5 through 9, are:

| Variant | Distinct values in \(1<M<6/5\) |
| --- | --- |
| Fixed | 1, 1, 1, 1, 1 |
| O | 1, 1, 0, 0, 0 |
| A | 1, 1, 1, 1, 1 |

A has five target-count nonlosses to fixed and five improvements on O under the exact declared count/time predicate.
The comparison is complete, so both four-of-five requirements hold.
The reviewer independently recomputed all displayed seed times, censored outcomes, median/range statistics and aggregate counts in the README's three result tables.
Medians computed only among observed hits remain conditional descriptive summaries; censored misses are not measured ten-second first hits.

At seed 5, O and A first hit at the same proposal 122 with the same free coefficients \((-1,0,-1,0,0,1,0)\), before the first adaptive update.
Their recorded completion times are approximately 0.348519200023 and 0.346241299994 seconds, respectively.
That approximately 0.002278-second difference counts under the prescribed literal time rule but provides no evidence attributable to the changed prior.
The other four seeds already meet the improvement requirement: at seed 6 A first hits at proposal 581 while O first hits at proposal 1188, and at seeds 7 through 9 A has one target value while O has none within its budget.
Thus the stated passing conclusion does not depend on a learning interpretation of seed 5, without changing or retrospectively tuning the screen.

All 5890 raw whole-target hits have the same known normalized Lehmer core
\[
 (1,-1,0,1,-1,1,-1,1,0,-1,1)
\]
in ascending order, with complete measure approximately 1.176280818259917506544070338474035051.
A and fixed find exactly one target value in each run; no new target measure was observed.
Their completed/fresh/cache/raw-target totals are:

| Variant | Completed | Fresh complete evaluations | Cache hits | Raw target hits |
| --- | ---: | ---: | ---: | ---: |
| Fixed | 60825 | 58834 | 1991 | 29 |
| O | 57240 | 57126 | 114 | 2 |
| A | 166065 | 49676 | 116389 | 5859 |

A's per-run repeated-proposal fractions range from approximately 70.64 to 71.31 percent, cache-hit fractions from 69.69 to 70.45 percent, and neutral fractions from 9.05 to 9.59 percent, with completed proposals as the denominator.
The much larger raw throughput and repeated recovery count therefore do not establish greater target-value diversity than fixed bias.
The results support the stated bounded recovery comparison and retain the distinction between repeated known-value recovery and a new small measure.

## Native reproduction and limits

The reviewer-owned sources are [independent_live_review.py](../../computations/programs/Yin_J_G0156/checks/independent_live_review.py) for the pre-run arithmetic/eligibility checks and [independent_live_results.py](../../computations/programs/Yin_J_G0156/checks/independent_live_results.py) for the actual histories, witnesses and export bindings.
The latter reuses the rational interval/ledger helpers in [independent_pilot_review.py](../../computations/programs/Yin_J_G0156/checks/independent_pilot_review.py), at their unchanged scope.
Both new reviewer programs were actually executed successfully.
Their generated records are `independent_live_preflight_review.json`, `independent_live_results_review.json` and `independent_live_witness_verification.json` under `mathematics/computations/outputs/Yin_J_G0156/`.
The original bounded control outputs use the separate `independent_live_preflight` label and are not formal live observations.

The following normalized commands use Python 3.14.7 with `python-flint==0.9.0` available through the environment or `PYTHONPATH`, from the repository root.
The first control command requires a fresh label if the named control outputs already exist; use that same selected label in the following preflight-check command.

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/prior_strength_live_checks.py --label independent_live_preflight
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_live_review.py --label independent_live_preflight
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_live_results.py --native-comparison mathematics/computations/programs/Yin_J_G0156/inputs/prior_live_comparison.json --native-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/prior_live_witnesses.json
```

The last command requires the original 15 JSON/JSONL pairs and original comparison output identified above; it starts no sampling run.
Its default calculation recomputes the selected certificates, while the explicit `--reuse-verification` option permits reuse of a selected prior certificate calculation for identical coefficient arrays and certifies missing inputs.
That option was used for the actual 366-plus-83 certificate check described above.
Without the ignored original journals, the fixed 449-polynomial input remains sufficient for standalone mathematical certificate replay through the existing sampler's `verify-witnesses` command, but not for regenerating the historical proposal-level timing observations.

FLINT/Arb remain trusted libraries at the v1 boundary.
No formal 15-run experiment was rerun by the reviewer, no screen threshold was changed, and the distinct original 45-run pilot remains separate.
The later S10 `#degree-validation` plan, any new degree-generalized wrapper and any subsequent experiment are outside both findings.
