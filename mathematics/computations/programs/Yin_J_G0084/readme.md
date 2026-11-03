---
author: Yin
---



# Exact moment controls for a regularized single-Haar lower certificate

[C379](../../../claims/Yin_C_G0379_v1.md#single-haar-moment-lower-certificate) owns the complete analytic reduction.
The original [L358](../../../ledger/Yin_L_G0358_v1.md#frozen-author-account) retains the fixed author freeze and execution context.
The finite domain consists of z-1, z²+z+1, z²-3z+1 and the original Lehmer polynomial[1,1,0,-1,-1,-1,-1,-1,0,1,1] in ascending order, each at epsilon=1/4 and N=64.
Moments are exact integers/rationals; algebraic functions and logarithms use outward rational intervals.
Independent binomial Chebyshev checks cover k≤8, moment/Fourier bounds cover k≤64 and certificate direction is checked against known measures of the first three controls.

## Program and reproduction

[main.py](main.py) writes data.json (`mathematics/computations/outputs/Yin_J_G0084/data.json`) after every assertion succeeds.
Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0084/main.py` from the repository root.
The program uses standard-library Fraction arithmetic,100-bit algebraic bisection and128 terms of a range-reduced atanh logarithm series, with no random input or floating certification.
Output belongs to `mathematics/computations/outputs/Yin_J_G0084/`.

## Exact result and limits

All declared moment, coefficient and direction checks passed.
The outward lower-certificate intervals are:

| Input | Lower-certificate interval, denominator10^18 |
| --- | --- |
| z-1 | [-0.000000006371739922,-0.000000006371739921] |
| z²+z+1 | [-0.351574168904568570,-0.351574168904568569] |
| z²-3z+1 | [0.475476702547483780,0.475476702547483781] |
| Lehmer | [-3.908887255960695643,-3.908887255960695642] |

The reciprocal quadratic gives a positive lower certificate; cyclotomic controls give no false positive.
The Lehmer result is a vacuous lower bound from coarse regularization cost, not a negative measure or a root/measure approximation.
These are author checks, not an independent project proof review.
No other input, scan, optimization or unrestricted Mahler gap is claimed.

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
| `data.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0184_v1.md#whole-restricted-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0585_v1.md#haar-lower-whole-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0589_v1.md#g382-whole-isolated-check); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0589_v2.md#g382-whole-isolated-check) |
