---
author: Yin
---

# Independent review of the completed sampling pilot and pair-pseudocount bound

## Review arrangement and retained inputs

At 2026-11-09T18:58, a reviewing agent acting for Yin completed the independent checks below after all 45 pilot runs and the selected native inputs were stable.
The reviewer did not implement the sampler, write its pilot summaries or develop the pair-pseudocount argument, and supplied no implementation repair.
The inputs were the frozen protocol and programs, actual completed run records, retained mathematical witnesses and the selected README statements.
Author-reported verification outcomes were not used as a substitute for the independent reproductions below.
The earlier [implementation and census findings](Yin_R_G1111_v1.md) and [diagnostic finding](Yin_R_G1111_v2.md#law-mass-diagnostic-review) are reused only at their unchanged applicable scopes.

The retained pilot inputs are [the complete observations](../../computations/programs/Yin_J_G0156/inputs/pilot_comparison.json), [1331 exact polynomial witnesses](../../computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json), and [15 post-run law-mass summaries](../../computations/programs/Yin_J_G0156/inputs/pilot_law_mass.json).
For the journal checks, the reviewer read all files `mathematics/computations/outputs/Yin_J_G0156/pilot_dD_ARM_sS.jsonl` and their `.json` summaries, for exactly \(D\in\{14,18,20\}\), `ARM` in `uniform,fixed,adaptive`, and \(S\in\{0,1,2,3,4\}\).
These fully specified 45 original journals remained available locally during the review.
The fixed observations preserve their reported finite outcomes; they do not claim to contain every original proposal event or to recreate wall-clock timing from a seed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Completed pilot](#pilot-results-review) | independently reviewed |
| [Completed-pilot law mass](#pilot-law-mass-review) | independently reviewed |
| [Pair pseudocount bound](#pair-pseudocount-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Completed pilot](#pilot-results-review) | [S10 metrics](../../strategies/Yin_S_G0010.md#metrics) | Whole-output measure, strict targets, distinct-value accounting, costs and censoring used by the actual experiment. |
| [Completed pilot](#pilot-results-review) | [S10 first experiment](../../strategies/Yin_S_G0010.md#first-experiment) | All 45 identities, fixed laws/settings, 60-second budgets, replication and held-out scope. |
| [Completed pilot](#pilot-results-review) | [S10 screen](../../strategies/Yin_S_G0010.md#decision-conditions) | The frozen four-of-five matched-seed continuation predicate and its failure in this pilot; no review of a separate new mechanism. |
| [Completed pilot](#pilot-results-review) | [Completed results](../../computations/programs/Yin_J_G0156/readme.md#pilot-results) | Entire completed first-pilot result section, both tables, all aggregate counts and the bounded screening conclusion. |
| [Completed pilot](#pilot-results-review) | [Timing explanation](../../computations/programs/Yin_J_G0156/readme.md#time-and-output-accounting) | Current counted-work and post-deadline contribution boundary, as applied to the actual journals and observed cleanup overhead. |
| [Completed pilot](#pilot-results-review) | [Fixed observations](../../computations/programs/Yin_J_G0156/inputs/pilot_comparison.json) | All 45 run records, preserved original comparison fields, added costs/rates, compact whole-output certificates, best inputs and separate factor records. |
| [Completed pilot](#pilot-results-review) | [Fixed witnesses](../../computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json) | All 1331 exact coefficient lists, exported roles and run memberships, with independent certificate reproduction. |
| [Completed pilot](#pilot-results-review) | [Frozen sampler](../../computations/programs/Yin_J_G0156/sampler.py) | Actual comparison_report/export_witnesses interfaces and unchanged evaluator/commit semantics reused from v1; not a repeated whole-implementation review. |
| [Completed pilot](#pilot-results-review) | [Earlier implementation finding](Yin_R_G1111_v1.md#sampler-implementation-review) | Applicable arithmetic, normalized cores, exact laws and valid-run interpretation. |
| [Completed pilot](#pilot-results-review) | [Earlier census finding](Yin_R_G1111_v1.md#baseline-census-review) | Exact finite-box reference target sets and the known complete-measure identities used for the observed recoveries. |
| [Completed-pilot law mass](#pilot-law-mass-review) | [Pilot diagnostic statements](../../computations/programs/Yin_J_G0156/readme.md#post-run-target-mass-on-the-completed-pilot) | Entire completed-pilot diagnostic section, its median/range table and approximate-arithmetic limits. |
| [Completed-pilot law mass](#pilot-law-mass-review) | [Fixed diagnostic summaries](../../computations/programs/Yin_J_G0156/inputs/pilot_law_mass.json) | All 15 degree/seed identities, update counts, initial/final conditional masses and ratios. |
| [Completed-pilot law mass](#pilot-law-mass-review) | [Diagnostic program](../../computations/programs/Yin_J_G0156/law_mass_diagnostic.py) | Unchanged conditional target-mass formula and committed-update interfaces applied to the completed pilot. |
| [Completed-pilot law mass](#pilot-law-mass-review) | [Earlier diagnostic finding](Yin_R_G1111_v2.md#law-mass-diagnostic-review) | Reused algorithmic and arithmetic scope; the v2 short calibration is not substituted for these 15 pilot histories. |
| [Pair pseudocount bound](#pair-pseudocount-review) | [Pair dilution statement and argument](../../computations/programs/Yin_J_G0156/readme.md#prior-dilution) | Complete mixture identity, elite/pseudocount weights, absolute-coefficient moment bound, first increment and 13-update numerical consequence. |
| [Pair pseudocount bound](#pair-pseudocount-review) | [Exact update implementation](../../computations/programs/Yin_J_G0156/sampler.py) | Law initialization/update, 81 pair states and the maximum of 26 elite representatives in a 256-proposal batch. |

<a id="pilot-results-review"></a>
## Completed-pilot finding

The verdict is **PASS for the reported finite pilot observations, their mathematical witness support and their stated interpretation**.
The experimental outcome is that the original adaptive law **fails the frozen S10 continuation screen**.
This review does not turn that finite outcome into a universal superiority claim or a resolution of the unrestricted research objective.

### Completeness, timing and original journals

The fixed data contain exactly one instance of every required degree/arm/seed identity, all with 60-second budgets and no proposal-count stop.
The original configurations agree on 128-bit certification, ranking radius \(10^{-12}\), batch size 256, the 4096-entry per-run cache and the declared initial laws.
All 45 runs reached their supervised caps, with no invalid run, unexpected worker failure or nonempty error output.
The worker return codes from planned deadline termination are not misclassified as independent failures.
The represented experimental ceiling is exactly 2700 seconds.

The reviewer independently streamed every original journal, checking sequential proposal/commit identities, coefficient-box membership, nondecreasing on-time completion timestamps and agreement with the stored configuration.
The replay rebuilt proposal and completed counts, cache membership under the declared LRU rule, repeated proposals and positive cores, neutral and unresolved counts, all four raw threshold totals, distinct whole values and separate factor values, and first-hit times.
It separately reconstructed conservative value ledgers from exact dyadic intervals and normalized cores, including equality and overlap handling.
Every rebuilt quantity matched the corresponding original run summary and retained observation.

There were 1906599 completed proposals and 43 unfinished proposals.
No completed evaluation had an unresolved ranking or threshold.
All counted completion timestamps were at most 60 seconds, and absent hits remain censored rather than being assigned a measured hit time of 60 seconds.
The observed supervisor excess was between approximately 0.0117119 and 0.0274178 seconds per run.
The checked boundary excludes post-deadline work from experimental yield; it does not assert an operating-system guarantee that every in-flight instruction stops at the exact deadline.
The final README wording about counted evaluations and post-deadline certification has been checked at this scope.

### Thresholds, values, witnesses and fixed retention

The reviewer independently recomputed all 1331 retained polynomial certificates through the already reviewed full-product evaluator.
Every retained whole-output certificate agrees with its exact coefficient list, canonical core, strict threshold decisions and fresh enclosing interval.
All original compact intervals used for a reported strict hit lie strictly above one and below the stated rational threshold.
Within each run, the intervals assigned distinct whole-value identifiers are pairwise disjoint, and their canonical cores are distinct.
The four distinct-value totals equal the corresponding counts of those certified representatives.
Small extracted factors remain in separate records and do not increase whole-output yield.

The fixed observations preserve the original comparison fields and additionally retain the actual per-run costs, rates, last completion time, compact discovery/equality certificates, best witness and separate factor records.
These additions match the corresponding original summary fields exactly at their selected mathematical scope.
Reconstructing the export selection from the per-run records gives exactly the 1331 retained coefficient lists, with matching role and run sets.
Per-run whole/factor use is available directly in the fixed observations, so no result depends on interpreting a cross-run union of witness roles as a per-run classification.
This is adequate retention of the reported observations and their selected mathematical witnesses.
The original ignored journals supplied the full proposal-level audit performed here; their continued availability is a separate scope from the compact native observation file.
Recorded wall-clock outcomes remain observations and are not promised to recur identically on rerunning a seed.

All 224 raw whole-polynomial hits in \(1<M<6/5\) recover the canonical core
\[
 (1,-1,0,1,-1,1,-1,1,0,-1,1)
\]
in ascending coefficient order.
It is the known Lehmer value, with complete measure approximately \(1.176280818259917506544070338474035051\).
No run recovered the second reference measure near 1.1883681475 as a whole-polynomial target.
The best reported complete positive measure and all relevant witness intervals are consistent with these facts.
The later certificate reproduction contributes no new stochastic discovery or additional charged pilot evaluation.

### Independent statistics and frozen screen

The reviewer recomputed the per-arm medians and ranges from the five retained seed observations and checked both README tables, including the displayed first-hit times and censoring marks.
The primary distinct-value vectors, in seed order zero through four, are:

| Degree | Uniform | Fixed | Adaptive |
| ---: | --- | --- | --- |
| 14 | 0, 1, 1, 0, 1 | 1, 1, 1, 1, 1 | 1, 1, 1, 1, 1 |
| 18 | 0, 0, 0, 0, 0 | 1, 1, 1, 1, 1 | 1, 0, 0, 0, 0 |
| 20 | 0, 0, 0, 0, 0 | 0, 1, 0, 0, 1 | 0, 0, 0, 0, 0 |

At degree 18 the adaptive arm wins strictly against both baselines in zero matched seeds and loses to at least one baseline in four.
At degree 20 the corresponding counts are zero and two.
The required four-of-five improvement condition is therefore false at both held-out degrees, so the frozen continuation screen fails without needing to resolve any ambiguity about a tie at the other degree.
This is the prescribed bounded resource-allocation comparison, not a significance test or an assumption that adaptive proposals are independent Bernoulli trials.
The wider-threshold tables are consistent with the fixed observations but do not replace the primary metric.

<a id="pilot-law-mass-review"></a>
## Completed-pilot law-mass finding

The verdict is **PASS for the 15 retained post-run diagnostic rows and their stated approximate interpretation**.
The raw-journal replay also reconstructed every adaptive update using only the eligible committed history, checking each exact elite/update record against the unchanged law implementation.
For every degree and seed, its update count, initial mass, final mass and final/initial ratio matched the retained diagnostic row and original generated diagnostic.
All 15 adaptive identities are present exactly once.
The reference target census enters only this later evaluation of a reconstructed law and does not enter the pilot's proposal or update process.

The independently recomputed ratio statistics agree with the README:

| Degree | Median final/initial mass | Minimum | Maximum |
| ---: | ---: | ---: | ---: |
| 14 | 0.03100497723 | 0.02483697216 | 0.03543130716 |
| 18 | 0.01139042937 | 0.01111700982 | 0.01360000926 |
| 20 | 0.004399791506 | 0.004293801495 | 0.004799365058 |

These are binary64 evaluations of the known finite target set under each final law.
The exact integer law update is reused, but no general rounding certificate for these 15 sums is claimed.
The rows describe endpoints of conditional one-proposal masses, not distinct-value yield, monotone decline, time-normalized performance or independent success probabilities along an adaptive trajectory.
They remain separate from the primary pilot observations and from the earlier short calibration diagnostic.

<a id="pair-pseudocount-review"></a>
## Pair-pseudocount algebra finding

The verdict is **PASS for the complete stated pair-component identity and moment bounds**.
The argument applies to the biased pair distribution before the global one-tenth uniform exploration mixture.
It does not purport to be the singleton update or a theorem about Mahler probabilities.

Each pair has 81 possible states.
A nonempty batch has at most 256 distinct eligible core representatives, so its elite size satisfies \(1\le m\le\lceil256/10\rceil=26\).
Adding one pseudocount to every pair state and retaining four fifths of the old law gives exactly
\[
 q'=\frac45q+\frac15\left(
       \frac{m}{m+81}\widehat q+\frac{81}{m+81}u_{81}\right).
\]
Consequently the elite contribution to the complete update is at most \(26/535\), while the uniform pseudocount contribution is at least \(81/535\).
The extrema use only the upper bound on \(m\), so variation of elite size between batches causes no gap.

For the initial one-coordinate law, the weights \((1,2,4,8,16,8,4,2,1)\) have total 46 and give expected absolute coefficient \(26/23\).
Thus \(\mathbb E_{q_0}(|a|+|b|)=52/23\).
The sum of \(|a|+|b|\) over all pair states is \(2\cdot9\cdot20=360\).
Nonnegative elite contributions and \(m+81\le107\) therefore imply
\[
 \mathbb E_{q'}W\ge\frac45\mathbb E_qW+rac15\frac{360}{107}.
\]
Iteration over nonempty updates gives the displayed lower bound in the README.
The first increase is exactly bounded below by
\[
 \frac15\left(\frac{360}{107}-\frac{52}{23}\right)
 =\frac{2716}{12305}>0,
\]
and the 13-update bound is approximately 3.303814027204, agreeing with the stated display.
An empty eligible batch leaves the law unchanged and does not increment this \(t\).

The resulting dilution statement is supported in the precise sense that this pair absolute-coefficient mean is forced above its initial value after any nonempty update sequence.
It does not establish stochastic dominance, monotonicity of the actual means, a Mahler-mass inequality or a unique causal explanation of the observed performance.
The README's stated limits are appropriate.

## Reproduction facts and remaining limits

The independent witness reproduction used the existing `verify-witnesses` command with the fixed pilot witness input and the separate output `mathematics/computations/outputs/Yin_J_G0156/independent_pilot_witness_verification.json`.
The [native review checker](../../computations/programs/Yin_J_G0156/checks/independent_pilot_review.py) retains the necessary fixed-data and streaming-journal checks first performed inline.
Both retained modes were then executed successfully with Python 3.14.7 and `python-flint==0.9.0`, reproducing the 45-run and 15-law-row checks above.
It reconstructs counts, rational-interval value identities and statistics directly, reusing the previously reviewed `Law.update` and diagnostic `target_mass` interfaces for exact updates and approximate endpoint masses.
The fixed mode checks the three native pilot inputs against separately generated witness certificates; it does not claim access to proposal events absent from those inputs.
The following are normalized reproduction commands from the repository root, with `python` denoting an interpreter having that package available through its environment or `PYTHONPATH`.

```powershell
python -B mathematics/computations/programs/Yin_J_G0156/sampler.py verify-witnesses mathematics/computations/programs/Yin_J_G0156/inputs/pilot_witnesses.json --output mathematics/computations/outputs/Yin_J_G0156/independent_pilot_witness_verification.json
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_pilot_review.py fixed
python -B mathematics/computations/programs/Yin_J_G0156/checks/independent_pilot_review.py journals
```

The optional `journals` command also requires the 45 original `.json`/`.jsonl` pairs specified above, the original generated `pilot_comparison.json`, the 15 corresponding `.law_mass.json` files, and `baseline_mass.json` in J156's output home.
The baseline and law-mass files use the existing [J156 reproduction interfaces](../../computations/programs/Yin_J_G0156/readme.md#reproduction) and [post-run diagnostic command](../../computations/programs/Yin_J_G0156/readme.md#post-run-law-diagnostic); missing original journals cannot be recreated by promising the same timed seed prefix.
The optional mode compares every retained observation with its original summary before streaming the journal and checking all committed updates.
The independently reconstructed fixed-data and journal results are written as `independent_pilot_summary_check.json` and `independent_pilot_journal_check.json` in that same output home.
The checker has explicit input, verification, original-output, reference and result-path options, and neither mode starts a sampling run.
The full 45-run pilot was not rerun; the checks used its actual completed observations and retained exact witnesses.
FLINT/Arb retain the trusted-library boundary recorded in v1.
No all-degree exclusion, new minimum, asymptotic positive-probability theorem or unrestricted Lehmer conclusion is established.

The later fixed-elite prior-strength control, its alternative update, new program and separate inputs are outside all three findings in this review.
They supply no additional first-pilot observations and receive no review coverage from this material.
