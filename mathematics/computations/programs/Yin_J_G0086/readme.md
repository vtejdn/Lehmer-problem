---
author: Yin
---

# Bounded exact positive moments by a finite arcsine state

## Question and scope

The signed integer-state recurrence and its exact division/bit costs belong to [C439](../../../claims/Yin_C_G0439_v1.md), with analytic moment and tail limits in [C434](../../../claims/Yin_C_G0434_v1.md#positive-log-moment-identity).
Root supplied the core integration-by-parts derivation; these are author-side native calculations with a separately recorded review.
The original [inputs.json](inputs.json) contains four coefficient lists: [-1,1], [1,1,1], [1,-3,1] and the ascending original Lehmer list [1,1,0,-1,-1,-1,-1,-1,0,1,1].

Stage 1 compares every finite-state I[n,k], n=0,...,64 and k=0,...,d, against direct Laurent convolution CT[(z+z^-1)^k Z^n], where Z=H^2-P(z)P(z^-1).
Stage 2 uses only the same Lehmer input through n=1024, after checking Stage 1's complete input/range/normalization payload.
The exact scalar comparisons at n=0,64,128,256,512,1024 and final eleven-state vector are mathematical certificates, not resume checkpoints.
No independent direct verification beyond 64 is claimed for the author calculation.

## Files and reproduction

[fast.py](fast.py) implements the signed exact-division recurrence; [direct.py](direct.py) independently implements Laurent products and binomial states without recurrence imports.
[worker.py](worker.py) checks the fixed scopes and publishes successful output atomically.
[main.py](main.py) enforces a live 30-second subprocess limit for each scope.
All mathematical arithmetic uses standard-library integers; no numerical roots, quadrature, random seed or floating certificate is used.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0086/main.py --mode compare
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0086/main.py --mode lehmer1024
```

The comparison.json (`mathematics/computations/outputs/Yin_J_G0086/comparison.json`) output is an explicit prerequisite of the second command.
lehmer1024.json (`mathematics/computations/outputs/Yin_J_G0086/lehmer1024.json`) retains the complete final scope.
Output and atomic intermediates resolve from this J's output home independently of caller cwd.

## Results and limits

Stage 1 passed 1,235 independent state equalities: 130 for the linear control, 195 for each quadratic and 715 for Lehmer.
All 960 signed divisions and every state-size, scalar range/monotonicity and Fourier-coefficient bound passed.
Stage 2 passed 10,240 signed divisions, 10,240 extended-state bounds, 11,275 stored-state bounds, 1,025 scalar range bounds and 1,024 monotonicity bounds.
Its n=64 overlap agrees exactly with Stage 1.
The largest triangular numerator/divisor have 6,513/14 bits; the final scalar numerator has 1,954 decimal digits and denominator 9^2048.
No tail constants, logarithmic enclosure, lower Mahler certificate or input-uniform gap follows from these states alone.

## Completed separate review

[R205](../../../audits/reviews/Yin_R_G0205_v1.md#finite-arcsine-state-whole-finding) checks the complete proof/program/output scope.
Its initial complete author mathematical self-check exposure makes that original whole arrangement SELF; the separately implemented mathematical verification remains the original actual evidence.
The current complete [R642 self-review](../../../audits/reviews/Yin_R_G0642_v1.md#current-finite-arcsine-whole-finding) additionally reconstructs the same original finite results read-only and adopts no extra source or parameter domain.
Its separately implemented read-only verification uses direct original-Laurent convolution for the small full states and an independently constructed recurrence for the retained n=1024 comparisons and final state.
It does not claim direct convolution beyond 64 or promote these finite checks to a uniform cutoff.

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
| `comparison.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0205_v1.md#finite-arcsine-state-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0209_v1.md#critical-positive-tail-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0642_v1.md#current-finite-arcsine-whole-finding) |
| `lehmer1024.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0205_v1.md#finite-arcsine-state-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0209_v1.md#critical-positive-tail-whole-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0642_v1.md#current-finite-arcsine-whole-finding) |
