---
author: Yin
---
# Quartic two-step kernel phase blocks

Context: [fixed quantitative argument](../../../claims/Yin_C_G0203_v1.md#quartic-two-step-certified-bound) develops a bounded quantitative pilot for the full original-law two-step strip kernel, using the finite block decomposition in [full-strip decomposition](../../../claims/Yin_C_G0203_v1.md#reciprocal-kernel-two-step-loss).

## Native input availability

The adopted138 positive integer vectors and actual lower-vector certificate are unavailable in this checkout and its selected local Git history.
The fixed program reconstructs the phase matrices, but the documented NumPy discovery and the scalar Rayleigh quotient do not determine those selected native vectors.
verify.py and the cross-J J34 verifier cannot currently check that complete selected certificate.
Supply the minimum original matrix-to-vector and actual lower-witness payload at this group's tracked inputs/ and point both exact consumers there; do not describe a newly selected positive vector as the original evidence.

## Question and scope

Cover every two-real phase for the quartic input by an exact finite arrangement and certify a rational upper bound on every integer matrix 16K^2.
Floating discovery and exact certificate verification remain distinct.
No neutral-radius truncation or Lehmer-input calculation is part of the current scope.

## Files

| File | Role |
| --- | --- |
| [core.py](core.py) | Exact degree-four field operations, rational root enclosure, proved coordinate-box checks, threshold arrangement and integer block construction. |
| [discover.py](discover.py) | Complete exact phase construction, NumPy discovery of positive-vector witnesses and one actual algebraic lower-bound coset. |
| certificate.json (`mathematics/computations/outputs/Yin_J_G0033/certificate.json`) | All 138 integer matrices with positive integer upper witnesses and the actual lower witness; approximate discovery fields are labelled separately. |
| [verify.py](verify.py) | Standard-library-only reconstruction of every phase matrix and exact integer verification of both bounds. |
| verified.json (`mathematics/computations/outputs/Yin_J_G0033/verified.json`) | Successful exact result with its finite scope, counts and mathematical bounds. |

## Reproduction

From the repository root, run `python -B mathematics/computations/programs/Yin_J_G0033/verify.py`.
The exact checker needs only the standard library.
It regenerates `verified.json` in `mathematics/computations/outputs/Yin_J_G0033/`.
It does not call the discovery program or use approximate eigenvalues from the certificate.

To reproduce discovery, use `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0033/discover.py` with NumPy installed.
It regenerates the full mathematical `certificate.json` in the same J output home.
The checker and discovery share `core.py`; this is a second execution/arithmetic boundary, not independent code authorship.
There is no random seed.
Caps are 50000 open phase cells and 60-second elapsed-time guards in the main loops.
The coordinate box has exactly 255 candidates per side; no neutral-radius cutoff is used.

## Results and limits

The completed exact check reconstructed 63 by 65 open phase cells, 138 distinct nonempty matrices, maximum dimensions 13 by 13, and checked every integer inequality `(M M^T)v<=97v` with positive integer v.
Minimum integer slack was 999999951.
The actual representative `r=-413+774 beta-180 beta^3` supplied a separate Gram Rayleigh quotient `9633565984214612/100000003825002>96`.
No cap was hit.

Together with D34's full coverage and boundary-submatrix proof, this certifies `sqrt(96)/16 < ||K^2|| <= sqrt(97)/16` for the entire quartic strip operator with the original weights.
Approximate discovery found maximum Gram eigenvalue 96.33565615730592 across the relaxed phase patterns; this decimal is not the certificate and is not asserted as an exact full norm.

This author-produced, author-rerun finite certificate now has a [complete noncontributing proof/coverage account](../../../audits/reviews/Yin_R_G0803_v1.md#quartic-two-step-independent-review), including a separately implemented full check in J G0034.
The complete operator and certificate arguments belong to [C203](../../../claims/Yin_C_G0203_v1.md#argument); the R account records the original mathematical checks without certifying isolated inherited context.
The rate remains weaker than the already fixed L30 diagonal bound, as compared explicitly in D34.
No Lehmer-input phase computation, degree-uniform estimate, or unrestricted Mahler gap is established.
The qualitative two-step argument and its complete noncontributor review are retained in the same fixed material.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0803_v1.md#fresh-quartic-certificate-finding) |
