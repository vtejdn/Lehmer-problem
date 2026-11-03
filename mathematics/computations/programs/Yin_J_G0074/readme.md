---
author: Yin
---

<a id="weighted-cycle-independent-verification-declaration"></a>
<a id="weighted-cycle-complete-independent-payload-review"></a>

# Growing weighted cycle full scalar controls

[C564 statement](../../../claims/Yin_C_G0564_v1.md#statement) and [entire proof](../../../claims/Yin_C_G0564_v1.md#argument) retain the all-index theorem, adopted after [the actual whole current SELF](../../../audits/reviews/Yin_R_G0750_v1.md#weighted-cycle-whole-self).
The original complete [written](../../../audits/reviews/Yin_R_G0138_v1.md#weighted-cycle-complete-written-review) and [computational](../../../audits/reviews/Yin_R_G0138_v1.md#weighted-cycle-complete-computational-review) findings retain the original L295/J74 inputs, real dates and SELF relationships; separate implementation supplies no isolation.
The finite domain is a=3,4,5,6,7,8.
B_a has diagonal1, superdiagonal1, lower-left-2 and other entries0; D_a=|B_a|.
Original and absolute presentations are[[I,-B_a],[0,I]] and[[I,-D_a],[0,I]].
The literal proper cover uses interleaved sheets, copying nonpositive edges to the same sheets and positive edges as negative crossed-sheet edges, with identity diagonal.
All18 literal matrices retain complete polynomial arrays, rank, height, energy and282 degree-plus-one integer pencils.
The formal numerator identities use an independent y for t^a; numerical substitution does not replace them.

## Programs and reproduction

[verify.py](verify.py) uses SymPy monodromy characteristic polynomials with direct integer Bareiss pencil checks, reusing the author's J72 pattern.
It writes result.json (`mathematics/computations/outputs/Yin_J_G0074/result.json`).
[review_independent.py](review_independent.py) writes review_result.json (`mathematics/computations/outputs/Yin_J_G0074/review_result.json`) using the reviewer's J72 standard-library elimination/interpolation/polynomial primitives.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0074/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0074/review_independent.py
```

Both retain120-second limits; the reviewer consumes the completed author result, without a retired-draft dependency.
Generated files belong to `mathematics/computations/outputs/Yin_J_G0074/`.

## Complete finite result and review

All18 polynomials and282 saved pencils passed, with complete factor products, reciprocal/trace arrays, B/D determinants, endpoint signs and both first-index rational-root lists.
Original/absolute costs are(2a,2,2a+3); cover costs are(4a,2,4a+6).
The B/D determinants are1+2(-1)^a and1-2(-1)^a; complete P_a/A_a polynomials differ by8t^a.
All endpoint values at1,3,4,5, full formal numerator/difference coefficients and trace cubics at a=3 are checked.
Rational-root candidates are every signed divisor of the constant coefficient, without inferring irreducibility for later indices.

The nonblind noncontributor reviewer imports no author code or SymPy.
It rebuilds all matrices and reconstructs complete polynomials by independent Bareiss evaluations and Newton interpolation.
Bareiss is also used by the author for scalar checks; the different complete reconstruction route, not that classical algorithm alone, supplies the implementation distinction.
Fraction Gaussian elimination independently checks B/D determinants; Laurent expansion checks trace arrays; sparse bivariate arithmetic checks every formal identity.
Every native mathematical field passed, while the coordinator separately reviewed the all-a root count, monotonicity, factor-degree estimates and limits.
No full-source proof audit, arbitrary-target coverage, cost optimum, near-one family or Mahler gap follows from these six controls.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
