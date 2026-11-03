---
author: Yin
---

<a id="full-payload-independent-review"></a>

# Factor-retaining vertex extensions and complete cover costs

The complete current proof is [C544 Part I](../../../claims/Yin_C_G0544_v1.md#factor-retaining-one-vertex-rigidity), with the [current whole independent written finding](../../../audits/reviews/Yin_R_G0770_v1.md#whole-current-independent-finding).
[L287](../../../ledger/Yin_L_G0287_v1.md#factor-retention-exact-test-declaration) retains the original fixed author declaration/input; [R770](../../../audits/reviews/Yin_R_G0770_v1.md#factor-retention-complete-independent-review) retains both original review scopes and UNKNOWN relationships.
The symbolic certificate covers the six-variable adjugate quadratic form for B=[[1,1],[0,1],[0,1],[0,1]], its unrestricted two-parameter kernel specialization and eight actual controls: six norm2 kernel vectors, zero and the A=4 boundary.
The six cyclic core orders and all seven insertion positions give252 cases, using explicit integral congruences.
No discovery scan or all-core theorem is inferred from these controls.

## Programs and reproduction

[verify.py](verify.py), requiring SymPy, writes result.json (`mathematics/computations/outputs/Yin_J_G0069/result.json`).
[review_independent.py](review_independent.py) uses only the standard library and writes review_result.json (`mathematics/computations/outputs/Yin_J_G0069/review_result.json`).
From the repository root run the corresponding command:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0069/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0069/review_independent.py
```

The author reconstructs all inputs directly; the reviewer consumes the completed mathematical result.
Outputs and failure diagnostics belong to `mathematics/computations/outputs/Yin_J_G0069/`.
Both programs retain live120-second limits.

## Complete result and checking scope

All symbolic identities, eight full matrix controls,236 saved integer pencil evaluations and252 cyclic cases passed.
The36 transported-core groups split into28 energy7 and8 energy8 groups, so core congruence does not preserve absolute expense.
The complete absolute polynomials, in ascending order, are respectively

```text
[1,0,-5,-10,-10,-5,0,1]
[1,-4,-17,-30,-30,-17,-4,1]
```

They equal(t+1)t^3 H(t+t^-1) for H=x^3-x^2-7x-4 and H=x^3-5x^2-15x-8.
Endpoint values[-2,1,-4,-7,16] at[-2,-1,0,3,4] and[-6,1,-8,-15,64] at[-2,-1,0,7,8] locate all three real roots and retain the complete expanding-pair costs.
The lambda4 boundary retains Phi2^2(t-1)^2 and Phi2^2(t^2-6t+1), with its full cover; it is outside the admissible open-window hypothesis.
The alternative neutral target Phi2 Phi4 P4 has cover cost greater than twice the original measure, with no Phi6 target or improved cost claimed.

The noncontributor computational reviewer used separately authored integer Bareiss determinants and degree-plus-one Newton interpolation, without author imports or SymPy.
Six basis vectors and fifteen pair sums at six nonzero t values recover all21 quadratic monomials in all six coefficients:126 symbolic pencil locations.
Sparse substitution verifies the unrestricted two-parameter identity; six-term determinant expansion verifies the full absolute Gram identity.
Every literal original/absolute/proper-cover matrix, full coefficient array, rank/height/energy,236 saved values and252 cyclic cases was checked.
The computation used636 distinct literal matrices and6853 pencil evaluations.
It is nonblind review, with earlier upstream roles disclosed; the complete written all-core proof remains the separately reviewed L287 argument.
No arbitrary-core coverage, unrestricted rank7 realization, cost optimum or Mahler gap follows from this finite certificate.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
