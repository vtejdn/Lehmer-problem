---
author: Yin
---

# Exact Lehmer control for the two-prime companion certificate

Current complete proof: [C226 proposed certificate](../../../claims/Yin_C_G0226_v1.md#joint-frobenius-minor-test), [coefficient-space obstruction](../../../claims/Yin_C_G0226_v1.md#coefficient-subspace-optimum) and [general lift boundary](../../../claims/Yin_C_G0226_v1.md#projection-cost-identity).
The original native input and execution facts below retain their L54/L55/L56 context; the current proof adoption does not redate or rerun them.

## Question and scope

For the single retained Lehmer polynomial

    p=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,

compute the exact two-prime maps F_ell=p(A^ell), ell=2,3, their coefficient matrix E at N=4d=40, J=det(F F^T), C=e_d(E^T E), Delta=|disc p|, G_N, and H=det(F(E^T E)^(-1)F^T).
Decide the signs of the resulting normalized entropy certificates.
The existing Salem/irreducibility input is retained in [MS26 U001](../../../audits/literature/MS26/Yin_U001.md) and [J G0001](../Yin_J_G0001/readme.md); the new programs do not redo that classification.
No parameter enumeration or approximate roots occur.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact companion-matrix evaluation, characteristic-polynomial coefficient cost, discriminant, orbit Gram and rational coefficient-space solve. |
| result.json (`mathematics/computations/outputs/Yin_J_G0008/result.json`) | Full input coefficients, integer/rational matrices, all elementary coefficients and exact comparison data. |
| [verify.py](verify.py) | Independent standard-library polynomial remainders, Newton identities, derivative norm, dual Toeplitz Gram and Schur-block determinant. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0008/verification.json`) | Independent integers, rational ratios, all Newton traces/coefficients and explicit author-payload comparisons. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0008/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0008/verify.py
```

The author program uses SymPy; the separate verifier uses only the standard library and imports no author code.
Verification requires the actual `result.json`; generate or explicitly obtain it first.
No external fetch, random seed, numerical tolerance or floating calculation is used.
The coordinator reproduced both retained programs, with all 29 named mathematical-payload comparisons passing.

Generated output uses `mathematics/computations/outputs/Yin_J_G0008/`, independently of the caller's directory.
Actual retained output is local and Git-ignored; a clone may lack it.
Verification reports missing required inputs without substituting other data or implicitly running a producer.
These are current reproduction instructions, not a new execution or proof review.

## Results and limits

Exact outputs are

    Delta=1332031009,        J=1142106771578809,
    C=32705007016634,        G_40=18006972477,
    det(E^T E)=515004740860,
    H=75593455205376240/25750237043.

The raw ratio Delta*J/(40^10*C) is strictly less than one.
Even multiplying it by binomial(20,10) leaves a number strictly below one, excluding a positive certificate with the sharper universal exterior-operator cost.
The best coefficient-space ratio Delta*H/40^10 is also strictly below one.
By the complete retained [optimality proof in C226](../../../claims/Yin_C_G0226_v1.md#coefficient-subspace-optimum), this closes every variant whose auxiliary columns remain in that same two-prime coefficient space, including arbitrary rational or integer combinations and scalings.
It does not close arbitrary new coefficient spaces or prove anything against Lehmer's entropy gap.
The direct full Gram ratio Delta*G_40/40^10 is strictly above one, so failure comes from the auxiliary restriction.

The separate simpler screen based only on sqrt(det(E^T E)) is retained with a false strict-comparison flag: that particular lower bound is too weak to certify failure.
It is not silently reported as a passed test.

The coordinator read the entire main program and independently reconstructed the decisive payload.
The verifier checks all elementary coefficients by integer Newton identities, F_2 and F_3 by polynomial remainders, Delta by the derivative multiplication norm, G_40 through the dual 30 by 30 Toeplitz Gram matrix, and H through a 30 by 30 integer Schur determinant.
It compares the displayed ratios and integer matrices, rather than execution metadata or file hashes.
The main program's rational compressed-Gram matrix entries are retained, but the independent H check certifies its determinant through a different construction rather than recomputing every such entry.
The precise comparison list and count are saved in verification.json.

The written proofs supply the relation between these quantities and entropy, the fixed-window admissibility, and the coefficient-space optimum.
Passing the scripts alone is not a proof of those implications or a uniform gap.

The actual current mathematical inspection and its evidence limits are recorded in [R513](../../../audits/reviews/Yin_R_G0513_v1.md#current-joint-minor-finding); it is self-review and does not turn algorithmic implementation independence into a claim about old proof-review isolation.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
