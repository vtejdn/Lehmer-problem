---
author: Yin
---

# Independent review of finite mutation kernels and cyclotomic closure

## Arrangement and exact scope

At 2026-11-09T20:55, a separately organized reviewer acting for Yin completed the fixed offline-component review below.
The reviewer did not develop the author implementations, extract their original native inputs, or supply a repair to their mathematics or programs.
The inputs were the fixed source files, native data and three specified J156 README sections.
No development conversation or proposed future live algorithm was inspected.
The two earlier findings below were read and reused for their established input boundaries, rather than treated as prior conclusions about these new controls.

The [v5 degree-evidence finding](Yin_R_G1111_v5.md#degree-results-review) supplies the already checked degree-18/20 histories, committed-event semantics and complete-measure evidence.
The [v6 core-mass finding](Yin_R_G1111_v6.md#core-mass-review) supplies the exact retained target partition and final-law states, including the earlier complete-census and root-certification boundaries.
This review independently checks the new parent extraction, finite kernels, closure generator and their actual results.
It does not rerun the stochastic comparison, the census or numerical root certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Offline mutation controls](#mutation-controls-review) | independently reviewed |
| [Cyclotomic closure](#cyclotomic-closure-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Offline mutation controls](#mutation-controls-review) | [Reference kernel source](../../computations/programs/Yin_J_G0156/mutation_kernel_control.py) | Entire specified mixture, cross-pair counting, endpoint enumeration, boundary returns, rational comparisons, controls and command input/output behavior. |
| [Offline mutation controls](#mutation-controls-review) | [Reference kernel native result](../../computations/programs/Yin_J_G0156/inputs/mutation_kernel_control.json) | Both complete-parent kernels, every witness, branch count, boundary count, exact probability, ratio and numerical display. |
| [Offline mutation controls](#mutation-controls-review) | [Geometry source](../../computations/programs/Yin_J_G0156/target_geometry.py) | All four free-coordinate metrics, cross-class histograms, targetwise minima and nearest-parent witnesses. |
| [Offline mutation controls](#mutation-controls-review) | [Observed-parent source](../../computations/programs/Yin_J_G0156/acquired_parent_control.py) | Complete committed-history extraction, exact-prefix deduplication, LRU and repeat handling, certificate association, empty-set behavior and subsequent conditional kernel. |
| [Offline mutation controls](#mutation-controls-review) | [Observed parent states](../../computations/programs/Yin_J_G0156/inputs/acquired_parent_states.json) | All ten parent sets, first certificates and 569 selected occurrence records, independently matched to original journals. |
| [Offline mutation controls](#mutation-controls-review) | [Observed-parent native result](../../computations/programs/Yin_J_G0156/inputs/acquired_parent_control.json) | All ten finite probabilities, parent/target counts, witnesses, comparisons, cache/repeat totals and acquisition-time observations. |
| [Offline mutation controls](#mutation-controls-review) | [Degree observations](../../computations/programs/Yin_J_G0156/inputs/degree_comparison.json) | The ten A configurations, exact source names, counts, committed-time limits and target totals used by extraction. |
| [Offline mutation controls](#mutation-controls-review) | [Target partition and final laws](../../computations/programs/Yin_J_G0156/inputs/degree_core_mass_states.json) | Actual complete parent/target sets and final integer block weights used for every new comparison. |
| [Offline mutation controls](#mutation-controls-review) | [Earlier exact masses](../../computations/programs/Yin_J_G0156/inputs/degree_core_mass.json) | Second-core initial/final rational masses recomputed at the new ratio interfaces. |
| [Offline mutation controls](#mutation-controls-review) | [Reference-control description](../../computations/programs/Yin_J_G0156/readme.md#mutation-kernel-control) | The fixed law, finite geometry/counts, exact and displayed comparisons, reference-data assumption and interpretation limits. |
| [Offline mutation controls](#mutation-controls-review) | [Observed-parent description](../../computations/programs/Yin_J_G0156/readme.md#acquired-parent-control) | Actual history extraction, distinct-parent weighting, all ten outcomes, post hoc selection and conditional-probability limits. |
| [Offline mutation controls](#mutation-controls-review) | [Earlier degree review](Yin_R_G1111_v5.md#degree-results-review) | Reused complete-measure and original experiment provenance; no renewed performance review. |
| [Offline mutation controls](#mutation-controls-review) | [Earlier partition/mass review](Yin_R_G1111_v6.md#core-mass-review) | Reused complete target-census, exact-core grouping and final-state evidence at its actual scope. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Closure source](../../computations/programs/Yin_J_G0156/cyclotomic_closure.py) | Entire conditional generator, neutral-product enumeration, normalization interface, final height filtering, comparison separation, controls and deterministic preparation. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Closure description](../../computations/programs/Yin_J_G0156/readme.md#cyclotomic-closure) | Complete representation argument under the stated normalized-core hypotheses, degree-18/20 equalities, degree-24/30 counts and limits. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Frozen normalization](../../computations/programs/Yin_J_G0156/sampler.py) | Only reciprocal_polynomial and normalized_core, including cyclotomic removal, exponent compression and descending-coefficient sign normalization. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Neutral-product interface](../../computations/programs/Yin_J_G0147/readme.md#measure-and-chamber) | Even multiplicities at the two real unit roots, the complete cyclotomic factor list and the totient order bound. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Reference target partition](../../computations/programs/Yin_J_G0156/inputs/degree_core_mass_states.json) | Exact coefficient-set comparison after generation, without using the target census to construct templates. |
| [Cyclotomic closure](#cyclotomic-closure-review) | [Earlier partition review](Yin_R_G1111_v6.md#core-mass-review) | Reused core identities, full target partition and earlier measure-certification boundaries. |

<a id="mutation-controls-review"></a>
## Offline mutation-control finding

The finding is **PASS for both specified finite kernels, their actual parent provenance and their qualified interpretation**.
No mathematical or implementation correction to the author files was required.

### Exact law and complete reference class

An ordered parent-target pair contributes to the \(k\)-coordinate branch exactly when its nonzero coordinate differences consist of \(k\) values in \(\{-1,1\}\).
Equivalently, its Hamming and \(\ell^1\) distances both equal \(k\).
It then determines one coordinate subset and one sign assignment.
A difference of magnitude greater than one is correctly excluded even when its Hamming distance is small.

Conditional on using the mutation component, each such branch has probability
\[
 \frac{1}{3|L|\binom nk2^k}.
\]
The uniform component contributes \(|T|/(10\,9^n)\), because each free prefix uniquely determines its complete reciprocal polynomial.
The out-of-box rule returns the unchanged parent without conditioning or resampling.
Since the two exact-core classes are disjoint, these returns supply no target hits.
Multiplying the mutation probability by \(9/10\) and adding the uniform contribution gives the displayed complete probability, including all boundary mass.

The independent checker enumerated weighted mutation endpoints directly, independently of the author's cross-pair calculation.
It checked every witness, changed-coordinate/sign list, reachable target, total branch count and boundary return.
It also checked branch normalization and executed the author's hand-counted controls, including empty target sets, larger coordinate differences, all three branch sizes and the explicit undefined empty-parent case.

| Degree | Parent prefixes | Target prefixes | \((C_1,C_2,C_3)\) | Mutation-only mass | Complete mixture mass |
| ---: | ---: | ---: | --- | --- | --- |
| 18 | 174 | 2 | \((0,0,2)\) | \(1/175392\) | \(25830631/5033366993088\) |
| 20 | 344 | 10 | \((0,2,6)\) | \(5/297216\) | \(1162283483/76765045372416\) |

The complete-library enumeration covers 145116 branches at degree 18 and 399040 at degree 20, totaling 544156.
Its boundary-return counts for \(k=1,2,3\) are respectively \((76,1154,7680)\) and \((166,2886,22314)\).
The geometry calculation separately checks Hamming, \(\ell^1\), squared Euclidean and changed-pair-block distances, including each target's exact minima, nearest-parent count and displayed witness.
The minimum Hamming distances are three and two, respectively.
These are distances in free reciprocal coordinates; the middle coefficient is not silently counted as two independent coordinates.

The reviewer independently calculated the fixed-law probabilities by multiplying the coordinate fractions \(2^{4-|a|}/46\).
For each final A law, the reviewer separately formed tuple-keyed block probabilities and summed products of normalized Fractions over the second-core targets.
These calculations match the previously retained masses and every new kernel ratio, including all numerator/denominator and decimal fields.
The author's complete comparison function also reproduced the entire native result object.
The complete-reference mixture exceeds the fixed baseline by the stated approximate factors 4.894863983 and 8.300145973 and exceeds each of the ten specified final A masses.
This comparison uses the complete known parent library and remains conditional on that privileged input.

### Actual parent extraction and cache accounting

The reviewer independently streamed all ten original A journals and joined each committed proposal to its own evaluation.
The reconstruction checked sequential identities, degree/box membership, the original configuration, on-time commitment, seen-prefix membership and exact LRU membership.
The cache order was updated on every committed evaluation, including hits, and the original size bound was enforced.
The original worker may touch its cache during final unfinished work, but that suffix precedes no later committed evaluation and cannot affect any retained occurrence.
The counts, cache/repeat totals and last committed times agree with the existing degree observations.

For every selected target event, the exact reciprocal polynomial reconstructed from the proposal agrees with the full coefficient array in its certificate.
The checked certificate fields include degree with multiplicity, 128-bit precision, factor-product verification, resolved ranking, nonneutrality, exact core and strict dyadic interval \(1<\text{lower}\le\text{upper}<6/5\).
The original numerical certification is reused at the v5/v6 boundary, not recomputed.
In the separate evaluation phase, every distinct retained parent also belongs to the already certified complete Lehmer target class.

All 135269 committed A evaluations were inspected.
The 569 selected Lehmer target events produce 55 run-parent records: the per-run distinct counts are \((6,7,4,4,4)\) at degree 18 and \((6,6,5,6,7)\) at degree 20.
Every first certificate and all occurrence records agree with the native parent-state input.
The author's extraction function was independently executed and produced an object identical to that complete input.

There are 513 cached target hits and 514 repeated target hits.
The one fresh repeated target occurs at degree 18, seed 12, after its earlier prefix has left the cache.
The first encounter of each retained parent is neither cached nor repeated.
Subsequent cached and fresh repeated hits remain provenance only and do not increase that parent's weight.
The extraction source does not consult the complete reference partition; the partition is loaded only for the later subset and probability checks.
Known whole-target/core status nevertheless enters parent selection after the completed run, as the description explicitly states.

### Conditional masses for the observed sets

The independent endpoint calculation covers all 55650 branches from the ten retained parent sets.
Every compatible witness, boundary count and rational comparison agrees with the saved observed-parent result.
The author evaluation function also reproduced that entire native object.

All ten sets have \(C_1=C_2=0\).
At degree 18 every set has \(C_3=0\), so its complete mixture probability is exactly the uniform floor \(1/1937102445\).
This is below both the fixed probability and the corresponding final A probability in every run.
At degree 20, the five \(C_3\) values are \((2,2,1,2,4)\), and the numbers of reachable second-core prefixes are likewise \((2,2,1,2,4)\).
The complete probabilities, in seed order 10 through 14, are
\[
 \begin{gathered}
 \frac{1162264667}{11157710083200},\quad
 \frac{1162264667}{11157710083200},\quad
 \frac{3486800401}{55788550416000},\\
 \frac{1162264667}{11157710083200},\quad
 \frac{3486790001}{19525992645600}.
 \end{gathered}
\]
All their ratios to the complete library, fixed baseline and corresponding final A law were checked exactly.
The per-run first-parent and last-new-parent observations also agree with the original committed events.

The two degrees demonstrate that replacing a complete library by an observed subset can either reduce or increase this conditional target mass.
No uniform ordering follows.
These computations establish neither the probability of acquiring those parent sets, a pathwise success rate, nor a cost-normalized advantage.
They do not modify the original yield or timing observations.

The [SEMR21 source unit](../literature/SEMR21/Yin_U001.md#restoration-map) was read at its mechanism interface.
Its bivariate ternary nearest-reference completion is related motivation, with different proposal and restoration rules.
No empirical result or incompletely specified source probability law is imported into this univariate kernel calculation.

<a id="cyclotomic-closure-review"></a>
## Cyclotomic-closure finding

The finding is **PASS for the conditional complete generator and all stated finite coefficient-set/count results**.
Its output remains the representation class of an already supplied core.
It supplies no new core, new Mahler value or evidence about a later live algorithm.

### Normalization and completeness

The stated input is already in the frozen sign normalization.
It is monic reciprocal of positive even degree, has constant coefficient one, no cyclotomic factor and exponent gcd one.
The code checks its coefficient, degree, reciprocity and exponent-gcd interface.
The caller's noncyclotomic certification and normalized sign remain genuine preconditions; the function is not a replacement certificate for an arbitrary supplied polynomial.
Both actual seed cores have those properties under the reused source evidence, and their canonical sign was checked directly.

For any output polynomial in the stated class, remove all cyclotomic factors to obtain its monic reciprocal noncyclotomic part \(R\).
Its nonzero exponent gcd is some \(k\), so \(R(z)=G(z^k)\) with \(G\) of exponent gcd one.
The frozen sign normalization implies \(G(z)=F(z)\) or \(F(-z)\).
Thus
\[
 P(z)=F(\varepsilon z^k)C(z),\qquad
 \varepsilon\in\{-1,1\},\qquad 1\le k\le\lfloor D/d\rfloor.
\]
Conversely, a root of unity cannot be a root of \(F(\varepsilon z^k)\), since its image under that substitution would be a root of unity of \(F\).
Removing the cyclotomic product therefore leaves exactly that substituted core, whose compression and sign normalization return \(F\).
The substitution preserves the complete Mahler measure: the \(k\) roots above each root of \(F\) contribute its original factor \(\max(1,|\alpha|)\).
The multiplier has measure one.

The neutral product \(C\) has even degree \(r=D-kd\), is reciprocal and has constant coefficient one.
Its roots at \(1\) and \(-1\) have even multiplicities, as follows from the trace-lift representation of an even reciprocal polynomial.
All other cyclotomic factors have orders \(m\ge3\) and degree \(\varphi(m)\).
For a prime power,
\[
 \frac{\varphi(p^e)^2}{p^e}=p^{e-2}(p-1)^2.
\]
The sole factor below one is \(p=2,e=1\), where it equals \(1/2\).
Multiplication over distinct prime powers gives \(\varphi(m)^2\ge m/2\), so every needed order satisfies \(m\le2r^2\).
This verifies the finite factor list reused from J147, including the separate constant product for \(r=0\).

The author's forward degree layers allow every nonnegative multiplicity of every listed factor.
They apply no intermediate height test.
This is necessary because a later factor can cancel earlier coefficients.
The final height check, complete-degree check and conversion to free prefixes are correct.
Exponent gcd one also separates the two sign representatives and the different substitution indices; the actual accepted-count sums equal the distinct output counts.

### Independent generation and finite checks

The reviewer enumerated nondecreasing factor multisets recursively, using an independently calculated totient for the order filter.
This differs from the author's degree-layer construction.
Exact FLINT multiplication in the reviewer checker was compared with the author's integer convolution.
The complete neutral-product sets agree at every remainder degree needed below, through degree twenty.
The generated coefficient sets and every per-index constructed/accepted count agree exactly.

| Core degree | Output degree | Accepted templates by substitution index | Distinct templates |
| ---: | ---: | --- | ---: |
| 10, Lehmer | 18 | \(174\) | 174 |
| 10, Lehmer | 20 | \(342,2\) | 344 |
| 10, Lehmer | 24 | \(1140,30\) | 1170 |
| 10, Lehmer | 30 | \(5228,302,2\) | 5532 |
| 18, second core | 18 | \(2\) | 2 |
| 18, second core | 20 | \(10\) | 10 |

At degrees 18 and 20, equality was checked for the full prefix sets against the retained partition, not inferred from matching cardinalities.
The complete generator uses only its supplied core, degree and height.
Source inspection confirms that the comparison function finishes all four generations before opening the reference partition.
Neither the original target coefficients nor census counts are used to choose generated polynomials.

The author's small controls were actually executed.
They check the five degree-two neutral products, exact cyclotomic factorization through neutral degree ten and normalization of all 556 displayed representations across the selected small core/degree combinations.
This includes substitution index two at output degree twenty.
No Mahler roots are computed by these checks.

The existing closure and preparation outputs were compared with fresh deterministic source-function results.
Their complete mathematical payloads agree; volatile generation-time fields were excluded.
The reported preparation times remain descriptive observations and are not independently certified performance measurements.
No conclusion about useful discovery mass or amortized search cost is obtained from the larger template counts.

## Native verification and retained limits

The reviewer-owned program is [independent_offline_controls_review.py](../../computations/programs/Yin_J_G0156/checks/independent_offline_controls_review.py).
Its fixed-input mode reads the six retained native JSON inputs named above, performs the independent exact probability and closure checks, and executes the relevant author control functions.
It needs Python 3.14.7 and the existing python-flint 0.9.0 package for exact polynomial arithmetic.
It does not need an original journal, a census output or an earlier generated closure output in that mode.

The additional history mode requires the ten original A journals and the two existing author outputs, cyclotomic_closure.json and cyclotomic_closure_preparation.json, under the J156 output home.
It reconstructs all committed cache/parent provenance, executes the author's bounded extraction and compares the saved closure payloads.
The original seeded law and full-root certifications remain reused evidence at the v5/v6 scope.

From the repository root, normalized reproduction commands are:

~~~powershell
python3.14 -B mathematics/computations/programs/Yin_J_G0156/checks/independent_offline_controls_review.py --output mathematics/computations/outputs/Yin_J_G0156/independent_offline_controls_fixed_review.json
python3.14 -B mathematics/computations/programs/Yin_J_G0156/checks/independent_offline_controls_review.py --with-history
~~~

In the current environment, the package is supplied through PYTHONPATH pointing to mathematics/computations/outputs/Yin_J_G0156/packages.
Both fixed-input and history calculations were actually executed successfully.
The saved verification results are independent_offline_controls_fixed_review.json and independent_offline_controls_review.json in that output home.
The final reviewer source and saved material were inspected directly.

These findings cover only the three fixed offline components and the exact README scopes bound above.
They provide no review of a future online composition, its acquisition process, timing behavior, sampling performance or experimental protocol.
No stochastic run, unrelated historical recertification or new root calculation was performed.
The unrestricted Lehmer Task remains unresolved.
