---
author: Yin
---



# Exact finite-map relative Gaussian discriminator

[L286](../../../ledger/Yin_L_G0286_v1.md#finite-tail-current-reuse) contains the conjectured profile C1 and its finite-tail motivation.
The scalar domain consists of all sorted lists of lengths1–8 with entries in{1,2,3,4}, and every nonzero endpoint.
The original difference law has numerator weights1,2,1 and denominator4^b.
For Q=sum a_j^2 the exact test is count(z)^Q*2^(z^2)<=count(0)^Q.
Column signs preserve this law and zero columns have no effect.

The separate joint-covariance domain fixes columns(1,0),(0,1), followed by k=0,...,4 nondecreasing choices from(1,0),(0,1),(1,1),(1,-1),(2,1),(1,2).
These are210 full-rank two-dimensional maps with at most6 digits.
For Q=XX^T, D=det Q and v=z^T adj(Q)z, the exact test is count(z)^D*2^v<=count(0)^D.
Both are finite abstract map classes, not actual non-torsion algebraic power orbits.

## Programs and reproduction

[main.py](main.py) writes result.json (`mathematics/computations/outputs/Yin_J_G0071/result.json`); [vector.py](vector.py) writes result-vector.json (`mathematics/computations/outputs/Yin_J_G0071/result-vector.json`).
Each result retains every input, endpoint count, denominator, covariance and failure list.
[review_independent.py](review_independent.py) writes review_result.json (`mathematics/computations/outputs/Yin_J_G0071/review_result.json`).
All use the standard library; run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0071/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0071/vector.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0071/review_independent.py
```

Author stages have separate60-second limits and publish only completed payloads; the reviewer has a120-second limit and requires both results.
Generated outputs belong to `mathematics/computations/outputs/Yin_J_G0071/`.

## Complete finite outcome

The scalar stage checked494 maps and14470 nonzero inequalities; the vector stage checked210 maps and13200 inequalities.
All passed, with normalization, symmetry and positive covariance checked exactly.
The noncontributor reviewer used explicit fair binary words and full endpoint autocorrelation, without author imports or ternary convolution.
It matched all28374 distribution entries, all inequalities, complete covariance/denominator/scope/failure fields and exact types.
The [complete finding](../../../audits/reviews/Yin_R_G0769_v1.md#finite-tail-pressure-complete-independent-review) covers the written proof separately.
The [adequate unconditional hyperbolic theorem](../../../claims/Yin_C_G0310_v1.md#statement) and [complete full-tail implication conditional on C529](../../../claims/Yin_C_G0529_v1.md#statement) remain distinct.
The current conditional theorem has [actual whole independent written finding](../../../audits/reviews/Yin_R_G0769_v1.md#whole-current-independent-finding); it does not turn these finite original tests into a proof of C1 or a new execution.
The [new isolated finite-map finding](../../../audits/reviews/Yin_R_G0787_v1.md#original-j71-complete-independent-finding) checked both complete author programs statically and independently reconstructed every saved scalar/vector endpoint, covariance, comparison, key and exact type at the same original domains.
Its direct ternary enumeration completed at 2026-10-22T21:20 in 0.9870229000225663 seconds under a predeclared 60-second total cap, without running an author or earlier reviewer program or changing the native files.
That new finite inspection and the R769 conditional proof retain distinct scopes.
The [separate independent inspection of the original hyperbolic fixed-prefix argument](../../../audits/reviews/Yin_R_F0011_v1.md#current-original-hyperbolic-fixed-prefix) covers complete L286 Sections 1–2, including the global maximum, stationarity and autocorrelation argument, at its actual 2026-10-22T21:42 initial judgment.
The finite-map inspection alone supplies no replacement for that written argument.
A finite counterexample could refute the abstract conjecture; these finite passes do not establish its universal truth or a Mahler gap.

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
| `result-vector.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0787_v1.md#original-j71-complete-independent-finding) |
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0787_v1.md#original-j71-complete-independent-finding) |
