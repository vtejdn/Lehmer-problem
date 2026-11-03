---
author: Yin
---

# Exact degree-four Macaulay attempts for three prescribed width-five norm lifts

## Question and scope

Use the original P=t^4-2t^3+t^2-2t+1, u_+=2+2alpha^2-alpha^3, u_-=2+alpha^2-alpha^3, k_f=2 and k_g=2,3,4, with positive normalized signs.
[C430](../../../claims/Yin_C_G0430_v1.md#independent-twist-width-four-obstruction) gives the reversal reduction and complete scope.
Every degree-at-most-five representative is f=f_seed+(a+bt)P and g=g_seed+(c+dt)P, with seeds reduced modulo actual P.
The six exact equations for ff*+2gg*=1 are tested for a certificate 1=sum h_l E_l with every product term of total degree at most 4.
All allowed multiplier monomials are included, including zero original equations as zero.
This is a fixed-degree certificate attempt, not an open-ended Groebner or nonlinear feasibility search.

## Files and reproduction

[main.py](main.py) uses standard-library integers/Fraction, with a live 60-second supervisor limit across all three cases.
The full data.json (`mathematics/computations/outputs/Yin_J_G0085/data.json`) retains original equations and representatives, monomial conventions, exact matrices/rhs, ranks/pivots and all left-null witnesses.
Atomic stage publication distinguishes completed cases from a genuinely interrupted calculation.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0085/main.py
```

The command needs no generated input or random seed and resolves its output from the actual J location.

## Results and limits

All three 70-by-90 systems completed with rank 50 and augmented rank 51.
Each retained left-null witness satisfies yA=0 and yb=1 by direct exact evaluation.
Thus no unit-ideal certificate occurs in the declared degree-four product domain.
An inconsistent Macaulay system is this completed finite negative finding, not a native crash or a proof of original nonlinear feasibility, all-degree certificate absence or a width-five lifting obstruction.
The complete current mathematical interpretation is [C430](../../../claims/Yin_C_G0430_v1.md#width-five-declared-macaulay-attempt), with the original fixed account and execution provenance preserved in L377.

## Completed separate review and later exact application

[R203](../../../audits/reviews/Yin_R_G0203_v1.md#paraunitary-whole-finding) separately checked the full declared proof/program/output scope and all three witnesses without importing author code.
Its actual whole agent relationship is SELF because its initial complete target read included the author self-check; the separate implementation remains a distinct fact.
The [current complete SELF reconstruction](../../../audits/reviews/Yin_R_G0632_v1.md#current-paraunitary-whole-finding) rechecked all three exact matrices/rhs/ranks/pivots/witnesses read-only, with native data unchanged.
The later complete [C453 exact lift](../../../claims/Yin_C_G0453_v1.md#all-dyadic-depths-and-finite-certificate-consequence), adopted through [R658 whole SELF](../../../audits/reviews/Yin_R_G0658_v1.md#current-exact-quartic-lift-whole-finding), supplies(a,b,c,d)=(2/3,1/3,-2/3,-1/3) for k_g=3 and checks all six equations.
Original [R210](../../../audits/reviews/Yin_R_G0210_v1.md#exact-quartic-lift-whole-finding) retains its full old proof/interface/no-run scope as SELF because the actual assignment supplied those target conclusions and its initial body included the author check.
That point excludes unit-ideal certificates at every degree for that case only; the other two cases retain their original finite scope.
No new J85 run was performed for that later deduction.

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
| `data.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0203_v1.md#paraunitary-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0632_v1.md#current-paraunitary-whole-finding) |
