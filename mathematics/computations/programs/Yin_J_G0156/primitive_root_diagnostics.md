# Degree-56 neutral multiplicities and exterior-root contributions

This is a post-hoc diagnostic of the completed [fixed D56 comparison](../../../strategies/Yin_S_G0010.md#primitive-core-comparison), using its ten original `s10_primitive_core_comparison` journals and already computed root certificates.
Within matched substitution index, actual mutation size and old-neutral gcd strata, repeated neutral trace roots are associated with more certified nonreal exterior roots and larger measures in the principal DP comparison below.
They do not explain every failure: trace-simple parents also miss the primitive near-miss interval, and the DP arm's smallest primitive measure comes from a trace-simple parent.
The diagnostic has passed the [independent extraction and interface finding](../../../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-implementation-review) and [actual descriptive-result finding](../../../audits/reviews/Yin_R_G1111_v13.md#root-diagnostics-results-review).
It introduces no performance pass threshold and changes none of the frozen proposal laws, primary metrics or completed observations.

## Retained inputs and exact scope

[primitive_root_diagnostics.py](primitive_root_diagnostics.py) extracts committed observations, verifies neutral products by exact multiplication, reads original root enclosures and computes descriptive summaries.
It calls no sampling routine, polynomial factorization or numerical root solver.
The [native diagnostic input](inputs/primitive_root_diagnostics.json) contains the compact inputs and the resulting group summaries.
The [formal comparison](inputs/primitive_comparison.json.gz) remains the full coefficient, parent, mutation, cost and commit-scope reference for each `(arm, seed, proposal)` locator.
The diagnostic retains 20378 observation rows, 15612 distinct root-diagnostic payloads and 4834 distinct neutral-template payloads, rather than duplicating the raw journals.
A root-diagnostic payload is not a claim of a distinct polynomial or Mahler value.
Each payload retains the original whole-measure dyadic interval, threshold labels, root-region counts with multiplicities, factor-degree scopes, and original printed imaginary/modulus intervals for every certified exterior root.
Twenty selected lower-tail observations also retain their complete original whole root certificates, exact proposals, parent/Delta data and structural diagnostics.
These include every arm/seed primitive minimum and the selected primary minima of the principal repetition strata.
The selection uses the smallest certified upper endpoint and records a minimum enclosure, without asserting a uniquely minimizing polynomial when intervals overlap.

All ten original per-run completion and primary counts agree with the extracted commits.
The direct arm has 15014 committed observations and 4521 primary structural occurrences; the DP arm has 5364 and 2538 respectively.
There are no committed unresolved evaluation errors in these data.
All 7059 primary occurrences have original certificates excluding `M < 13/10`.
Rows count actual committed occurrences, including cached repeats, rather than independent trials or distinct polynomials.
The direct arm has 2417 cached/repeated proposals and the DP arm has none.
Every group retains its exact denominator, seed counts and cached/repeated count.
Quartiles are explicitly nearest-rank quartiles; medians use the usual middle-value average for even group sizes.

The following disjoint scope partition includes both primary and nonprimary outcomes:

| Arm | Uniform whole box | Actual Delta zero | Nonzero Delta, deg G positive | Nonzero Delta, G=1 | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 1568 | 0 | 3691 | 9755 | 15014 |
| dp_closure | 520 | 208 | 2398 | 2238 | 5364 |

Seven final whole proposals were uncommitted and excluded: one in each direct run and one in DP seeds 30 and 34.
Four of these seven have an observed but uncommitted certificate; none contributes to these statistics.
DP seeds 31, 32 and 33 ended with a further generation request that did not form a whole proposal.
Their actual generation counts remain in the diagnostic input, and their detailed pending inputs remain in the formal comparison.
No endpoint, root count or measure is invented for a generation request without a completed polynomial evaluation.

## Multiplicity and root-classification conventions

For the retained neutral part `C`, write its actual irreducible cyclotomic multiplicities as `e_m`.
The interior trace repetition count is

\[
B=\sum_{m\ge3}(e_m-1)_+\,\varphi(m)/2.
\]

The trace endpoint multiplicities are `e_1/2` at `+2` and `e_2/2` at `-2`.
The [DP helper's actual interface](parent_sampling.md#class-and-bijection) stores orders 1 and 2 as the squared atoms `(z-1)^2` and `(z+1)^2`.
Their recorded atom powers therefore already equal the trace endpoint multiplicities and must not be halved again.
The program stores both atom powers and the resulting irreducible cyclotomic powers and verifies their exact product against the observed `C`.
For a direct sparse completion `C=1+z^r`, the exact factors have orders dividing `2r` but not `r`, each with multiplicity one.
All ten direct degree-56 parents consequently have `B=0` and zero endpoint multiplicities.

“Trace simple” here means `B=0` and both endpoint multiplicities at most one.
“Endpoint repeated only” means `B=0` but at least one endpoint multiplicity greater than one.
“Interior repeated” means `B>0`; the exact endpoint multiplicities remain separate, including in the fully stratified native table.
Actual mutation size counts nonzero free-coordinate changes in the retained Delta, so an out-of-box self-return has size zero despite a requested size of one, two or three.
The central coordinate counts once.
The old-neutral gcd degree comes from the committed exact diagnostic; `G=1` does not itself assert that the whole output is primary.

The original evaluator distinguishes certified `outside`, certified `inside`, and `meets_one` modulus balls.
The last category remains unresolved at the unit-modulus boundary and is never renamed “on the circle.”
Exact cyclotomic factors have contribution one and their root counts are kept separately, without inventing individual root balls.
Within the certified exterior roots, a root is certified nonreal only when the retained imaginary decimal interval excludes zero; an exact zero imaginary interval certifies realness, and any remaining case is unknown.
The decimal enclosure convention is supported by the [FLINT decimal conversion documentation](https://flintlib.org/doc/arb/printing.html), which accounts for conversion error in the printed radius.
The independent interface finding checks the actual python-flint 0.9.0 and FLINT 3.6.0 wrapper and default printing path against matching source, together with fixed-ball endpoint controls.
The diagnostic parses these decimal endpoints as exact rational numbers.

Across all committed occurrences, including polynomial-factor and root multiplicities, the counts are 209896 certified exterior roots, 209896 certified interior roots, 631612 `meets_one` roots and 89764 exact cyclotomic roots.
Their sum is exactly `20378 * 56`.
Of the certified exterior roots, 189510 are certified nonreal, 20386 are certified real and none remains unknown in this dataset.
This zero unknown count says nothing about the `meets_one` category's unit-modulus classification.

## Log-contribution summaries

The top-one, top-two and top-four quantities refer to individual roots after expansion by both the root multiplicity and the containing irreducible factor's exponent.
A powered factor's aggregate contribution is never treated as a single root.
For each original certified exterior root, the program takes the center of its printed modulus interval and computes its nonnegative logarithm.
It orders these individual contributions and divides their partial sums by the logarithm of the center of the original complete whole-measure dyadic enclosure.
Thus the denominator is the full measure, not the house or the exterior-root maximum.
These ratios and displayed measures are descriptive floating-point center approximations, not certified ratio bounds or threshold decisions.
Possible positive contributions from `meets_one` roots remain enclosed by the original whole certificate and are not declared exactly zero.
For the available positive-measure payloads, the maximum observed discrepancy between the sum of exterior-root center contributions and the full log center, as a relative share, is approximately `2.0e-15`.
That numerical agreement is an arithmetic consistency observation, not proof that a `meets_one` root lies on the circle.

## Matched principal comparison

The principal table fixes `j=1`, actual nonzero Delta, `G=1`, both endpoint multiplicities zero, and the primary class.
It separates each actual mutation size before comparing interior repetition.
All displayed values below are descriptive centers; exact measure enclosures and all group denominators are retained in the native input.

| Arm | Actual size | B class | n | Median M | Mean nonreal exterior roots | Median top-two log share | Median top-four log share |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| direct | 2 | zero | 480 | 2.048358 | 6.883 | 0.4397 | 0.7052 |
| direct | 3 | zero | 247 | 2.245001 | 7.174 | 0.4497 | 0.7218 |
| dp_closure | 1 | zero | 60 | 2.594599 | 10.733 | 0.3169 | 0.5656 |
| dp_closure | 1 | positive | 75 | 2.929884 | 12.373 | 0.2895 | 0.5079 |
| dp_closure | 2 | zero | 56 | 2.742316 | 10.536 | 0.3411 | 0.5946 |
| dp_closure | 2 | positive | 48 | 3.069567 | 11.375 | 0.2946 | 0.5302 |
| dp_closure | 3 | zero | 55 | 3.102725 | 10.691 | 0.3434 | 0.6056 |
| dp_closure | 3 | positive | 60 | 3.296555 | 11.467 | 0.3608 | 0.5989 |

In these DP strata the positive-B groups have higher measure medians and more nonreal exterior roots at every matched mutation size.
The top-two shares do not show a universal monotone trend with B: at size three the positive-B median is slightly larger.
Their magnitudes also show why a single far exterior root cannot be the sole description of the full-measure cost in these groups.
The B-zero DP groups remain far above the desired primitive near-miss range and still carry roughly eleven nonreal exterior roots on average.
At sizes two and three the trace-simple direct strata have fewer nonreal exterior roots and lower median measures, but the neutral templates themselves differ between the arms.
This is not a controlled intervention on multiplicity alone.
There is no primary direct observation at `j=1`, size one and `G=1`; its absence is not represented as a zero-valued measure statistic.
The direct size-two row includes sixteen cached occurrences; the other rows of this table have none.

For clarity, before conditioning on primary status the `j=1`, nonzero-Delta, `G=1` denominators are:

| Arm | Actual size | Primary | Nonprimary |
| --- | ---: | ---: | ---: |
| direct | 1 | 0 | 461 |
| direct | 2 | 480 | 153 |
| direct | 3 | 247 | 379 |
| dp_closure | 1 | 689 | 43 |
| dp_closure | 2 | 264 | 16 |
| dp_closure | 3 | 756 | 46 |

The exact-B and exact-endpoint native table has 301 nonempty strata, with primary and nonprimary outcomes kept separate.
The general matched-j/mutation table has 47 nonempty strata and includes the observed larger substitution indices.
Sparse cells are retained as sparse observations and receive no fitted trend or significance claim.

Endpoint-only repetition is not folded into B-positive repetition.
For DP primary observations at `j=1`, `G=1`, nonzero Delta and `B=0`, but with a repeated trace endpoint, the size-one/two/three sample counts are 45, 12 and 51, with median measures 3.011894, 3.603781 and 3.640690.
Their median top-two log shares are approximately 0.4115, 0.4851 and 0.5161.
For all trace-simple DP parents in those same primary strata, allowing simple endpoint roots, the counts are 172, 99 and 180, with median measures 2.644162, 2.775180 and 3.132053.
These additional descriptions preserve the endpoint distinction and do not establish a causal penalty from an endpoint multiplicity.

## Actual lower-tail witnesses and limits

The direct primitive minimum is the committed seed-34 proposal 1074, native diagnostic observation 17351, with `j=3`, actual size two, `B=0`, zero endpoint multiplicities and `G=1`.
Its complete measure center is approximately 1.3606107462500372.
It has eight certified exterior roots, all certified nonreal, and forty `meets_one` roots.
The top-one/two/four center log shares are approximately 0.267387, 0.534774 and 0.739543.

The DP primitive minimum is committed seed-32 proposal 448, observation 11542, with `j=1`, actual size one, `B=0`, zero endpoint multiplicities and `G=1`.
Its complete measure center is approximately 1.6951471325469833.
It has eleven certified exterior roots, ten certified nonreal and one certified real, plus thirty-four `meets_one` roots.
The top-one/two/four center log shares are approximately 0.299859, 0.408434 and 0.600013; the nonreal exterior roots supply approximately 0.700141 of the complete log center.
Both exact witnesses and all original root balls are retained under their observation indices in `lower_tail_witnesses`.
Neither is a new primitive target below 6/5 or a primitive near miss below 13/10.

The data therefore support a mixed finite diagnosis: repeated neutral trace roots can accompany an increase in the number of nonreal exterior roots, while simple-trace parents can also produce many exterior roots and large complete measure.
Some lower-tail witnesses have substantial contributions from the largest conjugate pair, but the remaining exterior roots still contribute materially.
Root splitting near a double trace root depends on perturbation sign and local structure, so multiplicity alone is not a causal explanation and repeated factors are not declared uniformly harmful.
The hard completion cap, differing parent laws, parent height selection, polynomial shape, seed realizations and conditioning on the primary class remain possible sources of selection and confounding.
This post-hoc analysis neither proves an asymptotic obstruction nor validates a new mutation law or a search-cost advantage.

## Reproduction and checks

Use the existing Python 3.14.7 and python-flint 0.9.0 runtime from the repository root.
The original-journal extraction command is:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_root_diagnostics.py extract --label s10_primitive_core_comparison --output mathematics/computations/programs/Yin_J_G0156/inputs/primitive_root_diagnostics.json
~~~

The original extraction was first written to `mathematics/computations/outputs/Yin_J_G0156/primitive_root_diagnostics_draft.json`, checked, and then retained as the native input.
Existing destinations are refused.
Reanalysis of the retained diagnostic input requires no journals and no Mahler roots:

~~~text
python -B mathematics/computations/programs/Yin_J_G0156/primitive_root_diagnostics.py analyze mathematics/computations/programs/Yin_J_G0156/inputs/primitive_root_diagnostics.json --output mathematics/computations/outputs/Yin_J_G0156/primitive_root_diagnostics_recheck.json
python -B mathematics/computations/programs/Yin_J_G0156/primitive_root_diagnostics.py self-test --output mathematics/computations/outputs/Yin_J_G0156/primitive_root_diagnostics_self_test_recheck.json
~~~

The exact fixtures check rational decimal parsing, nonreal/real/unknown boundaries, the squared-atom endpoint convention, all ten direct neutral templates and expansion by both root and factor multiplicity.
The actual extraction checks every factor's root-count sum, every whole degree, all neutral-product identities, actual Delta against child minus parent, per-run commit/primary counts and the journalled-proposal denominator.
Reanalysis from the saved compact input reproduced every group summary exactly.
The original self-test and reanalysis outputs are `primitive_root_diagnostics_self_test.json` and `primitive_root_diagnostics_recomputed.json` in the ignored J156 output directory.
The floating-point diagnostic shares remain explicitly approximate despite these checks.
