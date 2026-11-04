---
author: Yin
---

# Exact full doubling-resultant reduction and energy limit controls

## Question and scope

Retain exact polynomial identities reducing the primitive plastic family complete doubling resultant to a plus-cyclic norm of the original Lehmer polynomial.
The responsible [C409 complete argument](../../../claims/Yin_C_G0409_v1.md#plastic-lehmer-resultant-reduction) owns the all-N derivation and the use of the already accepted [Dim16 all-index cyclic-norm bound](../../../claims/Yin_C_G0854_v1.md#dim16-cyclic-all-index).
The program certifies the sign and size of the resulting fixed energy constant without evaluating an infinite Fourier tail.

## Programs and evidence

[verify.py](verify.py) and verification.json (`mathematics/computations/outputs/Yin_J_G0035/verification.json`) retain:

- the exact identities h^2 f(z^2)+f^2 h(z^2)=2zL and h-z^8 f=(1-z)L, with Res(f,h)=-1 and Res(L,f)=1;
- direct complete powered-resultant checks for N=9 and N=129 against 2^(N+3) Res(L,z^(N-8)+1), including the plus-cyclic identity C_(2q)=C_q A_q;
- a separate substitution-resultant check for N=9;
- exact rational root brackets for the plastic and Lehmer roots and 320-bit Arb enclosures of the complete energy constant, the earlier fourth-delay coefficient and their difference.

For even-degree P(z)=E(z^2)+zO(z^2), the direct powered polynomial is E(t)^2-tO(t)^2.
Its roots are the squares of the complete P root multiset with multiplicities.
The program computes Res(P,P^[2]) using this polynomial before comparing it with the fixed-degree reduction.
It does not compute the left side by first substituting the claimed resultant identity.

The root brackets are obtained by exact rational bisection from (13/10,4/3) for theta and (117/100,118/100) for lambda, to width at most 2^(-280).
The established fixed-family and original-Lehmer root configurations supply uniqueness in those intervals.
Exact opposite endpoint signs are checked again.
Arb then propagates all root and arithmetic uncertainty through the logarithms and rational moment formulas.

## Reproduction and results

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0035/verify.py
```

Dependencies: Python, SymPy and python-flint.
Both exact finite identities pass; the Frobenius quotient is 1 at N=9 and 62723699809 at N=129.
The first case uses only the all-N algebraic identity; it is not assigned the uniform tau_N<4/3 bound, whose accepted condition is N>=16.

The validated complete energy constant is

    kappa=0.0119060695987979093132786328095...,
    119/10000 < kappa < 3/250.

The earlier fourth-delay coefficient exceeds kappa, with

    kappa-gamma=-0.01002506582917568187... < -1/100,
    kappa/log(theta)=0.04234028315108191908....

The two identities and three unit resultants are checked before any output is retained.
No randomness, approximate numerical integration or Fourier truncation is used.
These are author-written exact/validated controls, not an independently authored verifier or formal proof.

The complete all-index limit relies on D38's algebraic reduction and the existing accepted logarithmic-form source scope, whose numerical absolute constant remains uncalibrated.
Two finite resultants do not prove the limit by extrapolation.
The original-family total measure tends to log(theta)>0; no new source theorem, near-one family, uniform gap or fixed-ledger result is asserted.

The complete mathematical argument resides in [C409](../../../claims/Yin_C_G0409_v1.md#plastic-lehmer-resultant-reduction).
The original fixed account and actual historical whole-review scopes remain in [L G0174](../../../ledger/Yin_L_G0174_v1.md#plastic-lehmer-resultant-reduction); current finding relationships belong to the exact selected C and R.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
