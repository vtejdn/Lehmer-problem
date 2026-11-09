---
author: Yin
---

# Independent review of adaptive integer sampling and its fixed-law reference census

## Review arrangement and fixed inputs

At 2026-11-09T17:52, a separately organized reviewing agent acting for Yin completed the implementation, arithmetic and evidence review recorded below.
The reviewer did not develop or repair the sampler or census and received no inherited development discussion or prior R conclusions about them.
The inputs were the frozen native programs, their fixed protocol and necessary dependencies, and the actual J156 documentation.
The documentation's author-reported ordinary controls were visible as part of those inputs but were not used as proof of their own success.
The reviewer independently inspected the code, performed the stated controls and reproduced the census.

The selected sampler input is the stable implementation after the failure-aggregation correction, including `run_validity`, the corrected supervisor and aggregate validity checks.
The reviewer identified that defect, supplied no repair code, and independently rechecked the actual repaired code and affected behavior.
The fixed mathematical and program locators below identify the checked scope; this review supplies no prospective coverage for later changes to the sampling laws, evaluator, timing semantics or census reduction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Sampler implementation](#sampler-implementation-review) | independently reviewed |
| [Exact baseline census](#baseline-census-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Sampler implementation](#sampler-implementation-review) | [S10 metrics](../../strategies/Yin_S_G0010.md#metrics) | Complete measure, distinct values, normalized cores, diagnostics and charged costs. |
| [Sampler implementation](#sampler-implementation-review) | [S10 first experiment](../../strategies/Yin_S_G0010.md#first-experiment) | Entire coefficient space, three laws, update rule, budgets, replication, rotation and held-out protocol. |
| [Sampler implementation](#sampler-implementation-review) | [Sampler source](../../computations/programs/Yin_J_G0156/sampler.py) | All functions, including the repaired run_validity, supervisor and aggregate path; whole-root certification, law generation/update, timing, summaries, witness retention and separate replay. |
| [Sampler implementation](#sampler-implementation-review) | [Failure regression](../../computations/programs/Yin_J_G0156/check_failure_boundary.py) | Entire focused regression, executed and supplemented by the reviewer's separate synthetic and live controls. |
| [Sampler implementation](#sampler-implementation-review) | [J156 arithmetic](../../computations/programs/Yin_J_G0156/readme.md#arithmetic-and-fixed-settings) | Declared arithmetic, precision, categorical weights, adaptation, normalization and interval separation. |
| [Sampler implementation](#sampler-implementation-review) | [J156 time and outputs](../../computations/programs/Yin_J_G0156/readme.md#time-and-output-accounting) | Final cap, commitment, failure, censoring, cache, aggregation and replay behavior. |
| [Sampler implementation](#sampler-implementation-review) | [J156 reproduction](../../computations/programs/Yin_J_G0156/readme.md#reproduction) | Runtime requirements, serial rotating pilot commands, separate controls/replay and declared 2700-second experimental ceiling. |
| [Exact baseline census](#baseline-census-review) | [Baseline source](../../computations/programs/Yin_J_G0156/baseline_mass.py) | Entire exact box intersection, neutral detection, strict threshold classification, full-product cross-check and fixed-law probability calculation. |
| [Exact baseline census](#baseline-census-review) | [J156 offline baseline](../../computations/programs/Yin_J_G0156/readme.md#exact-offline-baseline) | All three box counts, probabilities, core counts and distinct-value saturation statements. |
| [Exact baseline census](#baseline-census-review) | [J147 Newton cover](../../computations/programs/Yin_J_G0147/readme.md#newton-cover) | Complete necessary reciprocal coefficient cover, exact allowances, Newton recursion and JavaScript arithmetic bounds. |
| [Exact baseline census](#baseline-census-review) | [J147 measure reduction](../../computations/programs/Yin_J_G0147/readme.md#measure-and-chamber) | Only the neutral classification and strict whole-measure Graeffe bounds; no new chamber or resultant review. |
| [Exact baseline census](#baseline-census-review) | [J147 enumerator](../../computations/programs/Yin_J_G0147/newton.cjs) | Entire enumeration at degrees 14, 18 and 20, including the 32 necessary moment tests and exact rational allowances. |
| [Exact baseline census](#baseline-census-review) | [J144 Graeffe implementation](../../computations/programs/Yin_J_G0144/pilot.py) | The graeffe function only: exact integer transformation of every root to its square, retaining degree and multiplicity. |
| [Exact baseline census](#baseline-census-review) | [J156 full-product evaluator](../../computations/programs/Yin_J_G0156/sampler.py) | certify_polynomial, reciprocal_polynomial and normalized_core as the separate Arb cross-check of every strict census target. |

<a id="sampler-implementation-review"></a>
## Sampler implementation finding

The verdict is **PASS for implementation of the declared bounded protocol in the final reviewed code**.
The identified aggregation defect has been corrected and independently rechecked.
No remaining defect was found in the sampling laws, full-measure evaluation, strict threshold classification, core/value accounting or stopping and failure boundary at the inspected scope.
This is an implementation verdict, not a completed pilot or an empirical advantage finding.

### Probability laws and adaptive semantics

The reciprocal constructor maps the free vector bijectively to the stated coefficient box, with the central coefficient occurring once.
The categorical integer weights are \(2^{4-|k|}\), with sum 46, and cumulative integer sampling gives their exact normalized probabilities.
The fixed and adaptive arms use the same probability-\(1/10\) uniform mixture.
Adaptive pair weights initially equal the product weights, and an odd half-degree has exactly one final singleton.
No reference coefficient list or census is consulted by the drawing or update code.

For old integer weights \(w_j\), total \(W\), smoothed elite counts \(c_j\) and total \(C\), the implemented updated weights are \(4w_jC+c_jW\).
Their sum is \(5WC\), giving exactly \(\frac45w_j/W+\frac15c_j/C\).
The greatest-common-divisor reduction changes no probability.
Only resolved positive scores enter the current batch.
At each multiple of 256 proposals, the code chooses one representative per normalized core, orders by score with the declared deterministic tie break, takes the ceiling of ten percent, adds one pseudocount to every state and updates.
The empty eligible batch leaves the law unchanged.
Each run resets its random generator, block laws and cache, with no fitted state transferred to another seed or degree.

The reviewer's separate exact test used ten distinct core labels plus a second representative of one core with a lower score and a different free vector.
It verified the selected representative, one-member elite, all pair and singleton probabilities as rational numbers, and the no-change empty update.
Three separate degree-14, seed-2 controls completed 257 proposals for each arm under two-second caps.
Reconstruction from the retained proposal/evaluation events matched every proposal and the boundary update; the adaptive arm had exactly one update and the other arms had none.
These proposal-limited controls are not pilot outcomes.

### Whole-measure and duplicate verification

Exact integer factorization is reconstructed against the original monic polynomial before use.
All noncyclotomic factor roots returned as Arb complex balls are counted with their multiplicities, and the factor exponents are then applied to the whole product.
Exact cyclotomic factors contribute one.
For a modulus ball meeting one, union with \(\{1\}\) contains the true \(\max(1,|\alpha|)\), so the product remains a valid enclosure even for unit-circle roots or uncertain inside/outside classification.
The review inspected the installed python-flint 0.9.0 interface documentation for root multiplicities and exact outward-rounded interval endpoints.
The FLINT/Arb arithmetic and root-isolation implementation are trusted library inputs, not formally verified in this review.

The strict threshold test requires a certified lower bound above one and a certified upper bound below the rational threshold.
A ball failing to decide the comparison is retained as unresolved, not numerically rejected.
The log midpoint is used only for ranking after the stated radius test; it does not certify a threshold.
Small irreducible factors have their own ledger and never raise the whole-output yield.

The independent analytic controls included
\[
 (z-1)^4(z^2+z+1)^2,
 \qquad
 (z^2-3z+1)^2(z^4+3z^2+1),
 \qquad
 z^4-z^3-z^2-z+1.
\]
The first returned exact measure one and eight roots with multiplicity.
The second returned eight roots and a measure strictly between 17.94427 and 17.94428, agreeing with \(((3+\sqrt5)/2)^3\) and testing both repeated and nonreal exterior roots.
The third returned a measure strictly between 1.722 and 1.723 with two unit-circle modulus balls handled by the meeting-one branch.

Removing cyclotomic factors, compressing an exact power substitution and replacing a monic polynomial by its monic sign transform preserve its whole measure.
Thus equality of the normalized core is a valid equality test.
Different cores are counted as distinct values only after their dyadic certified intervals separate.
Overlapping intervals remain unresolved and can conservatively undercount values; they are never treated as new values merely because their coefficient lists differ.
The best field is a retained certified positive candidate, updated by strict interval separation; it is not an exact algebraic ordering of unresolved overlaps.

### Time, failure, aggregation and replay

The run clock starts before the child worker is launched.
Generation, certification, updates, cache operations, duplicate handling and evaluation-journal writes occur inside the supervised cap.
Only completed evaluation records with an on-time commit marker contribute to the summary.
The final unfinished proposal and a truncated final event are excluded from yields.
The per-run 4096-entry cache policy is identical in every arm.
Post-cap summarization does no new polynomial evaluation or certification.
The operator-facing comparison rotates arm order and reports independent seed outcomes, medians and ranges, without a Bernoulli assumption for adaptive proposals.

The initial code could declare 45 saved failed runs a complete pilot because its aggregate ignored failure metadata.
That exact case was reproduced with in-memory records before correction.
The final reviewed code preserves failure and supervision data, rejects failed or premature runs from valid statistics, excludes non-full runs from held-out matching, and requires all 45 distinct valid full-run identities for completion.
Its absent-hit censor uses the observed duration for an unsuccessful or early run.
The reviewer independently reproduced 45 failed records, a valid 45-record set, duplicate identities, a genuine deadline stop and a proposal-limited control after the correction.
The fixed focused regression also passed, including a single failed run with an artificially large yield that must not affect the statistics.

A separate 0.75-second live control committed through 0.749776 seconds, left one unfinished proposal and reported about 0.0123 seconds of supervisor cleanup beyond its cap.
The repaired supervisor also passed a new 0.5-second deadline control and a ten-proposal control, with the latter correctly excluded from full-pilot eligibility.
These timings verify the particular executions; they do not promise identical future throughput or eliminate operating-system termination overhead.

The journal retains exact proposed free coefficients and enough configuration to reconstruct the original polynomial.
Threshold discoveries, unresolved value equalities and selected best candidates retain certificates, and witness export retains exact polynomial inputs separately from generated logs.
Separate replay recomputed the retained certificates in all three 257-proposal controls without altering their original yields.
Replay is reproduction through the same evaluator, not an independent arithmetic algorithm or a new stochastic discovery.
The review did not independently reproduce every timing number or ordinary control listed in the author's calibration narrative.

<a id="baseline-census-review"></a>
## Exact baseline census finding

The verdict is **PASS for the complete stated finite-box counts and fixed-law probabilities**.
The reviewer inspected the full census and source cover, then reproduced degrees 14, 18 and 20 into the separate generated output `mathematics/computations/outputs/Yin_J_G0156/independent_baseline_mass.json`.
After removing elapsed-time fields, its mathematical payload agreed with the author's output.
The target vectors were independently checked for uniqueness, length and box membership, and their exact rational probability sums were recomputed from those vectors.

The J147 reduction covers every reciprocal monic integer polynomial with \(M\le6/5\), without imposing a height restriction before enumeration.
Pairing reciprocal roots bounds the radial moment error by \(R^k+R^{-k}-2\); the displayed superadditivity argument uses the sum of the exterior logarithms, so it applies to the complete measure with multiplicity.
The nonnegative trigonometric filters are necessary conditions, and omission of a zero-last-weight filter only weakens pruning.
Newton recursion enumerates every permitted next integer coefficient once, and reciprocity determines the remaining half.
All rational allowance floors are exact.
The stated coefficient and moment bounds keep the subsequent integer arithmetic below \(2^{42}\), and the prefix divisions cannot round across a required integer boundary.
The native code implements these interfaces through moment 32.

The box filter is then exactly \(\max_i|a_i|\le4\).
Neutrality is decided by exact cyclotomic factorization, and the remaining strict classifications use the whole-polynomial Graeffe bounds.
The imported transform is the integer polynomial \(E(x)^2-xO(x)^2\), which squares every root of the even-degree input and preserves its multiplicity.
The coefficient lower bound and squared-coefficient upper bound are compared to \((6/5)^{2^s}\) by strict integer inequalities.
An unresolved classification aborts rather than silently excluding a candidate.
Every strict target is additionally certified by the full-product Arb evaluator.

| Degree | Newton survivors in the box | Neutral | Above 6/5 | Strict targets | Exact uniform probability |
| ---: | ---: | ---: | ---: | ---: | --- |
| 14 | 1418 | 886 | 506 | 26 | \(26/9^7\) |
| 18 | 9621 | 2787 | 6658 | 176 | \(176/9^9\) |
| 20 | 27962 | 4674 | 22934 | 354 | \(354/9^{10}\) |

For half-degree \(n\), the independently checked static probability is
\[
 \frac{N}{10\,9^n}
 +\frac9{10\,46^n}\sum_{a\text{ target}}2^{\sum_i(4-|a_i|)}.
\]
The resulting probabilities agree with the documented approximately 0.0006508394871, 0.0001056313005 and 0.00005537943406.
The normalized target-core counts are 26 in degree 14, 174 and two in degree 18, and 344 and ten in degree 20.
The two core measures have disjoint certified intervals, while each common core preserves the original complete measure.
Thus the box has exactly one target value at degree 14 and two at degrees 18 and 20.
This distinction between polynomial counts and distinct values is essential for interpreting the pilot's saturation.

## Remaining scope

The inspected original-source interfaces are exact local programs and their explicit mathematical reductions; no unrelated chamber, resultant, historical census or source-priority claim is re-audited here.
The full 45-run comparison and all 60-second pilot runs remained unperformed in this review.
The ordinary short controls, deterministic census and separate replay are not pooled as pilot observations and supply no adaptive-performance conclusion.
Future pilot results require their own factual inspection, and any later changes to laws, settings, certification, output accounting or the cover need an appropriate recheck.
No novel minimum, asymptotic positive probability, arbitrary small shell or resolution of the unrestricted Lehmer problem follows from these findings.
