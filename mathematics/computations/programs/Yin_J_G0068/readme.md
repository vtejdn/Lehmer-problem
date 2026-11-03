---
author: Yin
---
# Trace-norm moment and constrained auxiliary tests

## Question and scope

The exact two-point test has a120-second live author cap.
Use ONLY the original Lehmer P and the retained L280 direction c=(196,-235,458,-1024,-384).
Normalize it to Euclidean length1, round at exactly H=45 and H=179, with exact nearest-integer ties away from zero and a sign-preserving nonzero highest coordinate, then divide the gcd.
These grids are respectively ceil(4s sqrt(s)) and ceil(16s sqrt(s)), s=5, from D151 rounding bounds; no other grid, input, direction or search is allowed.
Reconstruct complete auxiliaries, original resultants, norm/energy/rho/content/degree and auxiliary trace root counts/costs; compare B with actual m by exact integer inequalities.
Keep both outcomes.
The source direction is not asserted to maximize the whole class, so actual success of its rounding must be checked rather than inferred from the existence theorem.
The complete theorem in [C524 current complete theorem](../../../claims/Yin_C_G0524_v2.md#statement) does not depend on this finite test.

## Files

- [rounding.py](rounding.py): the only author program.
  It performs exactly the two predeclared grids, reconstructs Q and both V/C polynomials, and computes trace and original resultants separately.
- rounding.json (`mathematics/computations/outputs/Yin_J_G0068/rounding.json`): native output of the sole author execution, including exact rational ratios, all trace-root isolating intervals, full coefficients and costs.
  Discovery decimals are labeled separately.

## Reproduction

From the repository root, run `.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0068/rounding.py`.
The author program writes `rounding.json` in this J output home; the reviewer consumes its completed mathematical payload.

The program requires Python with SymPy.
Exact nearest rounding avoids floating decisions: for a=H*|c_j| and S=sum c_i^2, n=floor(sqrt(floor(a^2/S))) is incremented exactly when4a^2>=S(2n+1)^2.
Signs are restored and a zero highest coordinate gets the original sign (positive at zero).
Rational root intervals come from exact SymPy isolation at requested width1e-10, not numerical roots.
The retained exact upper bound beta<1434031/1219123 comes from [C515's actual Lehmer input](../../../claims/Yin_C_G0515_v1.md#small-measure-norm-moment-controls); this run does not separately isolate beta or reprove the original input's irreducibility.

## Results and limits

Both prescribed controls are primitive of actual degree10 and full original signed resultant -N^2:

| Grid | Primitive vector | N | E | Full Mahler interval |
| --- | --- | --- | --- | --- |
| 45 | (7,-9,17,-38,-14) | 2896629273 | 4118 | (42,91/2) |
| 179 | (29,-34,67,-150,-56) | 2791077805721 | 64244 | (168,182) |

For both, exact integer/rational arithmetic verifies N^2/E^5>(343/320)(1434031/1219123)^10, proving B-m>log(343/320)/10>0.
The native root intervals certify three trace roots in(-2,2) and one in(-7/2,-17/5); D151's complete factorization yields the full Mahler intervals, with leading factors14 and56 included.
No auxiliary factor is discarded.
The exact coefficient-coherence rho values are14450/2059 and112896/16061; the distinct degree-energy mean is5 for both.

These are two prescribed checks of a previously retained direction, which is not known to maximize the whole class.
The first has lower complete cost; the second has slightly larger B.
The proof does not select a global optimizer, infer near-one coverage, or identify either polynomial with an actual centered window.
The complete input-independent height theorem in [C524 complete height/cost argument](../../../claims/Yin_C_G0524_v2.md#uniform-height-full-expenses) is proved separately and does not depend on this finite computation.

The author calculations and independent review below are distinct; G0001 remains unresolved.

## Declared separate verification domain

The independent implementation covers exactly both controls and every mathematical field using standard-library integers and rationals.
It uses a direct second-kind recurrence, full coefficient arrays, separate Sylvester/Bareiss trace and original resultants, squared-threshold rounding and opposite endpoint signs at all four disjoint trace-root intervals.
Four simple real roots exhaust the quartic, so this route shares no symbolic root-isolation implementation.
The original Lehmer identity and beta endpoint are reused from L280; no global maximizer or new grid is inferred.

## Completed separate inspection

The coordinating noncontributor completed the [whole proof review](../../../audits/reviews/Yin_R_G0137_v1.md#uniform-height-complete-independent-review).
[review_independent.py](review_independent.py) and review_result.json (`mathematics/computations/outputs/Yin_J_G0068/review_result.json`) reconstruct both full costs and every native mathematical field by the method above.
Source-reading assistance is disclosed in the finding and was not a contribution to the new local derivation.

## Fixed retention

[C524v2](../../../claims/Yin_C_G0524_v2.md#argument) owns the complete current theorem and corrected rounding statement.
[L284](../../../ledger/Yin_L_G0284_v1.md#complete-retained-proof-and-review) remains the original frozen argument input of [R137](../../../audits/reviews/Yin_R_G0137_v1.md#uniform-height-complete-independent-review); that old finding has no relationship declaration and is not retroactively bound to C524.
The program and both original native records are unchanged.
The finite controls supply no unrestricted gap.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0733_v1.md#corrected-c531-v2-complete-independent-finding); [Claim support and recorded result](../../../claims/Yin_C_G0524_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0524_v2.md) |
| `rounding.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0733_v1.md#corrected-c531-v2-complete-independent-finding) |
