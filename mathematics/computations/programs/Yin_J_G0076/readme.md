---
author: Yin
---

<a id="plastic-tree-independent-computation-declaration"></a>
<a id="plastic-tree-complete-independent-computation-review"></a>

# One-ascent cycle to three-arm tree complete controls

[C578](../../../claims/Yin_C_G0578_v1.md#statement) retains the complete current theorem and proof; [R784](../../../audits/reviews/Yin_R_G0784_v1.md#preserved-complete-original-r202-accounts) retains the full original written and computational findings at their actual inputs.
The [current isolated whole C578 finding](../../../audits/reviews/Yin_R_G0784_v1.md#cycle-tree-current-independent) includes the separately declared new read-only check of this complete original payload; it is distinct from both historical executions.
The exact finite domain is n=4,...,12.
V has size n+1, diagonal1, entries V[i,i+1]=-1 for0<=i<=n-3, V[n-2,n-1]=+1, V[0,n-1]=V[n-1,n]=-1, and zero elsewhere above the diagonal.
For h=e1+...+e(n-2), Q has columns e0,-e2,...,-e(n-2),e(n-1)-h,h,en.
W=Q^T V Q is the all-negative tree with edges(j,j+1),1<=j<=n-4, and(0,n-1),(n-3,n-1),(n-2,n-1),(n-2,n).
Every Q, integer inverse, determinant and full congruence is retained.

For F=t^3-t-1, Fstar=1-t^2-t^3, G=t^3-2t^2-t+1 and Gstar=1-2t-t^2+t^3, full polynomials are P=[t^(n-1)F-Fstar]/(t-1), A=[t^(n-1)G-Gstar]/(t-1).
The five literal matrices V,Vminus,W,cover(V),cover(W) have polynomials P,A,P,PA,P^2.
Interleaved proper covers retain every signed edge and identity diagonal; Wminus=W.
Formal numerator checks use independent y for t^(n-1).

## Programs and reproduction

[verify.py](verify.py), requiring SymPy, writes result.json (`mathematics/computations/outputs/Yin_J_G0076/result.json`) using author helpers reused from J75.
[review_independent.py](review_independent.py) writes review_result.json (`mathematics/computations/outputs/Yin_J_G0076/review_result.json`) using only the standard library.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0076/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0076/review_independent.py
```

Both retain120-second limits; the reviewer requires the completed result and no retired draft.
Generated files belong to `mathematics/computations/outputs/Yin_J_G0076/`.

## Complete finite result and review

All45 full polynomials,612 pencils, nine basis conversions/inverses, edge and cost fields, five boundary factorizations and formal seed/endpoint checks passed.
Per-index pencil counts are40,47,54,61,68,75,82,89,96.
P(1)=8-n and A(1)=-n; n4–8 have zero original measure.
The n9 control is the complete original Lehmer polynomial with identical companion, square cover, rank10, energy9 and neutral degree zero.
Its fixed irreducibility premise is reused, not newly inferred by an oracle.

The complete original computational project finding is retained in [R784](../../../audits/reviews/Yin_R_G0784_v1.md#plastic-tree-complete-computational-review), with all original method, mathematical-field coverage, source and negative limits.
Its actual original review minute is unrecorded in the retained finding/native report; this navigation does not assign a new act or independent arrangement.

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
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0784_v1.md#cycle-tree-current-independent) |
