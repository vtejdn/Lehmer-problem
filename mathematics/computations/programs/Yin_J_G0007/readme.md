---
author: Yin
---

# Exact integral bounds for alternating kernels

Context: the direct argument and accepted Lawton interface in [C224](../../../claims/Yin_C_G0224_v1.md#alternating-kernel-scope).

## Question and scope

Check the rational arithmetic in two lower-integral certificates: the S4 two-variable Mahler measure and the fixed three-variable limit P both exceed 4/3.
Retain separately the six exploratory integral values that guided the argument.
There is no finite polynomial enumeration, certified quadrature, effective specialization rate, or test of the unspecified remaining kernels.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Fraction and integer comparisons for the S4 endpoint radicals and both lower-integral products. |
| result.json (`mathematics/computations/outputs/Yin_J_G0007/result.json`) | Exact positive margins and product differences. |
| [diagnostics.py](diagnostics.py) | Exploratory mpmath quadrature for r=1,2,3,4,5,10. |
| diagnostics.json (`mathematics/computations/outputs/Yin_J_G0007/diagnostics.json`) | Uncertified diagnostic logarithmic and multiplicative measures; no proof uses these values. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0007/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0007/diagnostics.py
```

The exact program uses standard-library integer/Fraction arithmetic.
Diagnostics use mpmath 1.3.0 at 30 decimal digits, without random input.
Quadrature subdivisions are 0, pi/6 and every j*pi/(2n) inside that interval for n=2r+1.
Threshold cusps mean the working precision is not a rigorous error bound.
The six diagnostic values remain observations, not premises of the exact lower-integral proof.

Generated output uses `mathematics/computations/outputs/Yin_J_G0007/`, independently of the caller's directory.
Actual retained output is local and Git-ignored; a clone may lack it.
Verification reports missing required inputs without substituting other data or implicitly running a producer.
These are current reproduction instructions, not a new execution or proof review.

## Results and limits

The authoring AI's exact comparison passed.
The coordinator separately executed both retained commands and reproduced the rational comparisons and diagnostic values.
The S4 product uses four endpoint beta bounds with weights 5,5,2,3 and compares against (4/3)^60.
The three-variable product uses seven cosine lower bounds and compares against (4/3)^12.
Every retained difference is strictly positive in exact arithmetic.
The complete interval coverage, Jensen integrability and Lawton hypotheses are retained in [C224](../../../claims/Yin_C_G0224_v1.md#argument), with [actual current and historical findings](../../../audits/reviews/Yin_R_G0511_v1.md#current-alternating-kernel-finding) kept at their separate scopes; this short arithmetic program alone does not establish them.
The coordinator read the complete program and checked the radical squares, Taylor remainder sign and integration weights.
The diagnostics neither prove monotonicity nor cover any other r.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
