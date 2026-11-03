---
author: Yin
---



# Connected signed-diamond and equal-scalar controls

[C595](../../../claims/Yin_C_G0595_v1.md#signed-diamond-necklace-construction) owns the complete all-k theorem.
The finite domain is five pairs k=2,3,4,5,6, without random or adaptive search.
Order vertices a0,b0,c0,a1,...,a(k-1),b(k-1),c(k-1),ak.
V has diagonal1 and V(ai,bi)=V(ai,ci)=V(bi,a(i+1))=-1, V(ci,a(i+1))=+1, and V(a0,ak)=-1; other entries vanish.
Z is the direct sum of k copies[[1,-2],[0,1]], one copy[[1,-1],[0,1]] and I_(k-1).
Each presentation retains its negative absolute companion and literal proper two-sheet cover in vertex-then-sheet order.

Put q=t+1,d=t²+1,e=(t-1)², F(-1)=0,F0=1,F1=e,Fj=eF(j-1)-4t²F(j-2).
The companion residual is Dk=(d²-tq²)F(k-1)-8dt²F(k-2)+16t⁴F(k-3)-2^k q(t^(2k)+t).
The complete original target is q^(k-1)(t-1)^(2k)(t²+t+1).
Every tr(N^j N^T),1≤j≤n-1, is checked:4k+1 at j1,2^k at j2k and0 otherwise.

## Programs and reproduction

[verify.py](verify.py) uses SymPy integer monodromy characteristic polynomials and writes result.json (`mathematics/computations/outputs/Yin_J_G0081/result.json`).
[review_independent.py](review_independent.py) uses only standard-library integers and writes review_result.json (`mathematics/computations/outputs/Yin_J_G0081/review_result.json`).
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0081/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0081/review_independent.py
```

Both accept `--output` for another destination and retain120-second live limits.
The reviewer requires the completed author result and refuses to overwrite its report; no draft is a mathematical input.
Default output home is `mathematics/computations/outputs/Yin_J_G0081/`.

## Result and checking boundary

All30 literal polynomials, full factor products, matrix costs, continuants and mixed path traces passed.
Connected absolute traces are6,11,20,37,70.
At k4 the companion has additional(t-1)² factors, so q^(k-1) is not claimed to be its complete neutral part.
Exact factor lists certify full product identities, without a new residual irreducibility or root-location claim.

The [complete noncontributor review](../../../audits/reviews/Yin_R_G0150_v1.md) checked all30 matrices,550 full-pencil and55 residual determinant values,30 factor products,25 continuants and60 mixed-trace entries by a different exact implementation.
No author program was imported; the whole written all-k argument was separately reviewed.
The bound concerns the given connected presentation, not an infimum over congruences or every form with that scalar.
The original is completely neutral, so these controls establish neither positive irreducible complexity nor a G0001 solution.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
