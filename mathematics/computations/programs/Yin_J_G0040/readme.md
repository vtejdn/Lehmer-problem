---
author: Yin
---
# Actual normalized ideal descent and three-state termination

## Native input availability

The adopted fifty-cell cover is retained in [inputs/ideal-cover.json](inputs/ideal-cover.json):818 distinct integer words,1379 cell uses and the selected rational auxiliary vertices.
This minimum payload was extracted from the existing original cover12.json and hull_verification.json in experimental-math-ai's local J40 outputs; the source discovery diagnostics and pilot runs are unnecessary verification inputs.
Both [verify_hulls.py](verify_hulls.py) and [review_independent.py](review_independent.py) read that same tracked certificate and reproduce the complete geometric scope with the standard library.
The restored-input checks reproduce the original radius, displacement and real-margin bounds, all1080626 four-vertex subsets and5453 supporting hyperplanes, together with the distinct5625-tuple compact check.
These are current replay checks of the retained object; the original dated proof and review relationships keep their recorded scopes.

## Question and scope

For the degree-six Salem root of t^6-t^5-t^3-t+1 and I=(2,beta^2+beta+1), certify normalized four-real-dimensional neutral displacements c/||c||^2 of original words whose translation lies in I, then check the complete actual ideal residue at radius5/2.
The responsible complete proof is [C476](../../../claims/Yin_C_G0476_v1.md#degree-six-return-core-fixed-scope).
All50 closed real cells and all neutral coordinates are covered.
The norm-only target was not attained by discovery; the changed construction succeeds through the explicitly terminated three-state residue instead.

## Files

- [inputs/ideal-cover.json](inputs/ideal-cover.json): the adopted words and rational vertices, with each cell referencing the shared818-word list.
- [probe.py](probe.py): bounded floating-point word discovery, retaining integer words and nonbinding numerical hull data.
- pilot.json (`mathematics/computations/outputs/Yin_J_G0040/pilot.json`), pilot12.json (`mathematics/computations/outputs/Yin_J_G0040/pilot12.json`): initial three-cell diagnostics at lengths10 and12.
- cover12.json (`mathematics/computations/outputs/Yin_J_G0040/cover12.json`): integer words for the complete50-cell length12 cover, plus nonbinding numerical discovery fields.
- [exact.py](exact.py): rational outward interval and field-embedding utilities, adapted from the inspected J22 interval pattern to the degree-six trace cubic.
- [verify_hulls.py](verify_hulls.py): exact reconstruction of the retained rational inner-polytope boundaries, complete real-cell and F4 checks, and error transfer to the actual normalized vectors.
- hull_verification.json (`mathematics/computations/outputs/Yin_J_G0040/hull_verification.json`): successful exact50-cell output and rational auxiliary vertices.
- [verify_compact.py](verify_compact.py): complete coefficient box proof,5625-tuple classification and exact integer return paths.
- compact_verification.json (`mathematics/computations/outputs/Yin_J_G0040/compact_verification.json`): successful complete three-state residue and path output.
- [review_independent.py](review_independent.py) and review_independent_result.json (`mathematics/computations/outputs/Yin_J_G0040/review_independent_result.json`): orbit_research's separately implemented and executed full certificate verification, with its original contribution, coverage and native-comparison boundaries preserved in [the later complete R689 comparison](../../../audits/reviews/Yin_R_G0689_v1.md#l199-and-r98).

Both author verifiers use the shared exact.py utility.
They establish different certificate obligations and are not independent reviews.
Floating roots, facets and radii are never proof inputs; the hull checker reads only cell identifiers and integer words from discovery data.

## Reproduction

From the repository root, the complete discovery command is:

For discovery, select a compatible Python environment containing the declared NumPy and SciPy dependencies; the shared baseline dependency file does not include SciPy.
The command below uses normal package resolution.
Exact verification requires only the Python standard library and [inputs/ideal-cover.json](inputs/ideal-cover.json).
It needs no discovery run or previously generated J40 output.

```powershell
$geometryCells = (50..99) -join ','
python -B mathematics/computations/programs/Yin_J_G0040/probe.py --length 12 --cells $geometryCells --output cover12.json
```

The earlier three-cell runs used the default cells50,75,99 and lengths10 and12, producing pilot.json and pilot12.json respectively.
Discovery requires NumPy and SciPy.

The exact standard-library commands are:

```powershell
python -B mathematics/computations/programs/Yin_J_G0040/verify_hulls.py
python -B mathematics/computations/programs/Yin_J_G0040/verify_compact.py
```

The exact checks passed.
Algebraic interval operations round outward at scale10^35.
The retained auxiliary rational vertices use grid10^(-10), with the original deterministic per-cell perturbations avoiding degeneracy; every actual-coordinate error is checked explicitly against1/100000.
Integer supporting-plane tests construct and inspect the full rational hull boundary.
Outputs are written only after all assertions pass.

The separate reviewer command is:

```powershell
python -B mathematics/computations/programs/Yin_J_G0040/review_independent.py
```

The reviewer check passed, importing and rerunning none of the author programs.
It uses the supplied integer words and rational vertices as witnesses, dyadic outward arithmetic at2^110 and independent Chebyshev recurrences for neutral geometry.
It exhausts all1,080,626 four-vertex subsets, recovering5,453 complete supporting hyperplanes over all50 cells, and separately derives coefficient bounds by Lagrange duals before visiting all5,625 tuples.
The reviewed constants, complete three-state set and integer return paths agree with the author results.
This is independent verification and complete noncontributor proof review, not independent discovery or formal proof verification.

## Results and limits

The complete50-cell certificate has1379 word uses and818 distinct words of length at most12.
It proves a centered actual normalized-hull radius2009/10000>1/5, squared displacement lower bound61/250, squared-radius descent drop549/500000 outside R=5/2, and strict real endpoint margin at least71/2000000.
Every word translation belongs to the actual ideal.

The compact checker proves coefficient bounds[2,2,2,1,1,2], visits all5625 integer tuples, excludes4220 by nonzero residue,1330 by the expanding bound, six by the stable bound and66 by the neutral bound.
Exactly three remain:0 and+/-a with a=1-beta^(-3).
All retained states are also positively checked inside the closed domain.
Exact six-digit original words return each nonzero state to zero.

The complete C476 proof combines these separate certificates with [C467v2's complete at-most-four-digit legal entry into I](../../../claims/Yin_C_G0467_v2.md#four-state-real-overlap-entry), proving narrow-domain co-return for this actual degree-six order.
The [complete C400 conditional strip theorem](../../../claims/Yin_C_G0400_v1.md#exact-salem-return-strip) then identifies its full actual return core.
The norm-only isolation threshold1/(2J(I)) about0.328352 was not reached and is not claimed necessary.
Neither a larger fractional module nor a finite-search failure is used to infer the result.
General Salem termination, varying-input cost control, original-law weighted tails and the unrestricted gap remain open.
The original complete noncontributor proof-and-certificate finding reported a full pass at its actual2026-10-10 scope; [the later complete comparison](../../../audits/reviews/Yin_R_G0689_v1.md#l199-and-r98) preserves that old R98 result, actual inputs/date/native limits and UNKNOWN initial relationship.
The current C476 decision adopts the [complete independent whole finding in R689](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding).
The [earlier complete R685 whole finding](../../../audits/reviews/Yin_R_G0685_v1.md#current-degree-six-ideal-core-whole-finding) remains SELF and does not establish the original reviewer's isolation.
R689 separately records its later original-domain reviewer-checker execution at 2026-10-21T23:11--2026-10-21T23:12 of 11.844 seconds, complete field-for-field report agreement and unchanged bytes across all twelve original files.
That later check preserves the original native execution dates and the earlier maintenance account's actual no-new-run scope; this navigation update runs no code or verifier.
Its nonblocking wording clarification explicitly distinguishes ideal membership of block endpoints and complete translations from intermediate digit states, whose residues need not stay zero.
The original [targeted reread](../../../audits/reviews/Yin_R_G0098_v1.md#degree-six-original-ideal-wording-reread-finding) is narrow SELF because the same reviewer supplied the concrete residue1 countercheck and mathematical endpoint/block explanation before the author amended the sentence and the reviewer checked that clarified interface.


The complete [C478 arithmetic connection](../../../claims/Yin_C_G0478_v1.md#degree-six-principal-saturation-fixed-scope) proves I=(beta^3-1)O=(1-beta^(-3))O of index4 and rho(1-beta^(-3))^2=(beta+beta^(-1))^2-1 in(3,4), in an actual input saturated at the full doubling resultant.
The coordinator supplied its new cross-route derivations; its current decision adopts the [complete independent whole finding in R697](../../../audits/reviews/Yin_R_G0697_v1.md#c482-whole-independent-finding).
The [earlier R686 whole finding](../../../audits/reviews/Yin_R_G0686_v1.md#current-degree-six-principal-whole-finding) remains SELF, while the [entire original R99 whole](../../../audits/reviews/Yin_R_G0697_v1.md#l200-and-r99) retains its UNKNOWN initial relationship and the original listed author checks remain separately SELF.
These identities do not replace the complete hull or compact-slice certificates here and assert no uniform inverse, control-cost or arithmetic-income bound.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.

## Recorded runs

The local output names below identify the particular recorded runs used by the linked fixed materials.
Those records retain the original inputs, parameters, known dates and checked scopes; the existing instructions above identify the programs and reproduction commands.
These links locate the original results and checks, without asserting verification of the present README or a new execution.
Generated output files remain local and are not synchronized.

| Local run output | Original result or check record |
| --- | --- |
| `compact_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
| `cover12.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
| `hull_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
| `pilot.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
| `pilot12.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
| `review_independent_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0689_v1.md#independent-degree-six-ideal-core-whole-finding) |
