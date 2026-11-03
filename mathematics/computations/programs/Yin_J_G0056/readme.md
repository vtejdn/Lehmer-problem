---
author: Yin
---

# Actual centered edge Wronskian and complete arithmetic costs

Exact centered-edge Wronskian computation supporting the current complete [C423v2](../../../claims/Yin_C_G0423_v2.md#statement), selected with its [complete isolated R653 finding](../../../audits/reviews/Yin_R_G0653_v1.md#edge-derivative-isolated-whole).
The original L253 input remains fixed.
The boundary polynomial is Z=t(A'B-AB')-NAB from PF=A+t^N B, of degree at most2d-2.

## Responsible argument and actual execution

The declared eighteen cases are the quartic, P6 and original Lehmer inputs at j=d-1,d,2d-1, and P=t^2-a t+1 for a=3,4,5 at j=1,2,4.
[verify.py](verify.py), requiring SymPy, writes verification.json (`mathematics/computations/outputs/Yin_J_G0056/verification.json`).
All eighteen exact checks passed; every tested normalized full-resultant-minus-S2 margin is strictly negative by integer comparison.

The program reconstructs the rational coefficient projection from P, clears actual primitive content, then derives both edge blocks and the derivative auxiliary.
It checks both complete polynomial identities, original-root remainder, every original degree and actual leading/trailing exponent, middle coefficient, content, full signed resultants, discriminant factor, squared coefficient norms and the invariant margin sign.
No expected output coefficients or resultants are used to construct the objects.
All complete coefficients and exact integers remain in the JSON.
The program protects an existing output from overwrite; an independent replay should intercept or redirect its write while preserving these author bytes.

This is an author exact-algebra pilot and scope disclosure, not an independent mathematical review or an all-input theorem.
The actual higher-degree input classifications are reused from the fixed arguments linked in D120.
There is no root-isolation run, certified decimal Mahler computation, prime-depth enumeration or scan outside the eighteen declared cases.
The all-j quadratic negative-margin and root-location results are proved in D120 and are not inferred from this table.
No failed execution or output repair occurred in this pilot.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0056/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0056/review_independent.py
```

Default results belong to `mathematics/computations/outputs/Yin_J_G0056/`.

## Independent method

The independent standard-library checker covers the same eighteen pairs.
It obtains the centered residual from V^T(VV^T)^(-1)V e_j in the integer remainder row space, independently of the author's shifted-P kernel system.
Whole resultants are determinants of multiplication in Q[t]/(P).
It imports no author code; neither this finite check nor an author replay supplies the general proof.

## Completed separate implementation and original review

The [separate implementation](review_independent.py) and result (`mathematics/computations/outputs/Yin_J_G0056/review_result.json`) record18 passes with all25 reconstructed result fields per case matching the author data.
The name, input polynomial and j are separately checked as input identity.
The separate author replay also matched every mathematical field.
The original whole proof review at 2026-10-10T00:40 covered the infinite quadratic control, while leaving all-input negativity and the unrestricted Task open, as retained in [R653's later historical comparison](../../../audits/reviews/Yin_R_G0653_v1.md#edge-derivative-isolated-whole).

C423v2 owns the current complete theorem/proof; L253 retains the substantive original exploration and original reviewed input.
The original R152 finding retains its UNKNOWN initial arrangement in that later comparison; distinct exact implementation is separate from agent-context isolation.
D120 denotes the original authoring phase.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0627_v1.md#edge-derivative-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0653_v1.md#edge-derivative-isolated-whole) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0627_v1.md#edge-derivative-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0653_v1.md#edge-derivative-isolated-whole); [Claim support and recorded result](../../../claims/Yin_C_G0423_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0423_v2.md) |
