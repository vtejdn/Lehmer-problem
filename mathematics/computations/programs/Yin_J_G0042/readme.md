---
author: Yin
---
# Pendant-chain interlaced determinant certificates

Responsible complete argument: [C488](../../../claims/Yin_C_G0488_v1.md#bounded-measure-interlaced-fixed-scope).
Bounded exact symbolic checks for the chain-extension determinant recurrence, fixed cubic numerators, an irreducible degree-six member and complete signed/absolute factors.

## Files and reproduction

- [verify.py](verify.py) constructs the actual integer matrices and computes the characteristic polynomial of -V^(-1)V^T for k=0,...,6, both original and absolute presentations.
  It compares these independently computed polynomials with the written chain formula, checks unit diagonals, entry height, squared-entry cost, reciprocity, complete displayed factorizations, the degree-six trace/irreducibility, the k=3 trace, seed root discriminants and endpoint signs, gcd(H,H*), and every inspected r_k(1).
- verification.json (`mathematics/computations/outputs/Yin_J_G0042/verification.json`) retains the successful exact output, including every complete coefficient list and factorization for these fourteen matrix instances.
  These are finite checks, not an all-k factorization or irreducibility assertion.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0042/verify.py
```

The author check uses Python with SymPy and passed, including the k=3 control and pairwise-factor interfaces.
No numerical roots are used.
Exact arithmetic and factor/irreducibility routines use SymPy and its configured backend; no independently implemented algebra system is claimed.

## All-k proof and limits

D70 derives the full pendant-chain recurrence and proves the exterior-root counts and costs directly.
The original seed is H=t^3+6t^2+21t+12 and the absolute seed is J=t^3-42t^2+21t-36.
Every full determinant is retained as (t^(k+2)H-H*)/(t-1), or its J counterpart, with no deleted unknown circle factor.
The original matrix has rank k+4, entry height3 and squared-entry sum k+21.
Its complete signed cover has rank2k+8 and squared-entry sum2k+42.

The proof supplies pairwise distinct reciprocal irreducible factors with nonreal trace, unbounded degree and complete measure in(log4,log36), together with their entire retained cyclotomic cofactors.
Only the k=2 degree-six polynomial is claimed irreducible as a whole in this argument.
The absolute determinant has exactly one expanding positive root and measure below log84.
These measures stay far from zero.
Positive coefficients exclude every Salem target factor from this particular chain family.
No arbitrary coefficient prescription, small-measure uniform coverage, full G0001 gap, or independent review is asserted by the author checks.


## Complete separate review and fixed argument

The complete current C488 decision adopts the [actual whole SELF in R700](../../../audits/reviews/Yin_R_G0700_v1.md#current-pendant-chain-whole-finding).
The [entire original R102 proof/program finding](../../../audits/reviews/Yin_R_G0102_v1.md#pendant-chain-complete-independent-review) retains its03:39 original scope and UNKNOWN initial relationship; the original listed author checks remain separately SELF.
The reviewer read the entire author program and reran it with its JSON output write intercepted in memory, reproducing every mathematical field for all fourteen actual matrix instances.
This was a separately organized proof/program review and rerun of the same author implementation, not a newly implemented algebra system.
No all-k claim is inferred from the finite execution.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
