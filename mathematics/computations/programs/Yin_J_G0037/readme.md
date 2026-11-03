---
author: Yin
---
# Exact recursive height-one seed certificate

Completed bounded program for the [complete current C425 construction](../../../claims/Yin_C_G0425_v1.md#height-one-negative-phase-balance).
The [original L179 account](../../../ledger/Yin_L_G0179_v1.md#retained-height-one-negative-argument) preserves the fixed historical review input and original execution scope.
The only root-isolation input is the single recursively defined 64-term seed, with a certified circle sup-norm bound from its paired recursion.
There is no broad coefficient enumeration or irreducibility claim.

Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0037/certify.py` from the repository root.
The source is [certify.py](certify.py); the complete successful output is certificate.json (`mathematics/computations/outputs/Yin_J_G0037/certificate.json`).
The Python program uses python-flint with 192-bit working precision and a 768-bit maximum root-isolation precision.
Exact integer autocorrelations check all six paired norm identities, and an exact polynomial gcd checks squarefreeness.
All63 roots are isolated into pairwise disjoint complex balls;31 are strictly outside the unit circle and32 strictly inside.
The outside product is enclosed near6.8505729309192798991 and rigorously exceeds137/20.
The root data retain ball centers/radii as display evidence; rerunning the actual ball operations, rather than treating rounded displays as an independent certificate, checks the claimed inequalities.

The current certificate proves the seed threshold137/20 and the exact rational four-copy ratio below2/3 used by the effective averaging bound.

Only the one seed is expanded computationally.
Its four separated copies and the much higher-degree almost anti-reciprocal specializations are handled in D45 by exact identities and an elementary quantitative averaging proof.
An explicit huge cutoff is proved there, while no high-degree specialization has been expanded.
The initial qualitative Lawton argument was replaced before review by that direct proof.
The [original complete proof and certificate review](../../../audits/reviews/Yin_R_G0078_v1.md#height-one-negative-phase-independent-review) and [J G0038](../Yin_J_G0038/readme.md) record the separately reconstructed coefficient list and stronger-precision root check.

The current [R647 whole independent finding](../../../audits/reviews/Yin_R_G0647_v1.md#isolated-height-one-negative-whole-finding) covers the complete mathematical construction and original fixed evidence, including one original-domain J38 read-only replay at2026-10-21T20:10.
The original R78 whole arrangement remains UNKNOWN, the earlier R773 SELF and original executions remain historical, and no producer/native bytes were changed.
The exact classical paired-recursion attribution is retained in [Erd14-U001](../../../audits/literature/Erd14/Yin_U001.md#erd14-u001), without importing that paper's Mahler theorems or replacing this seed certificate.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
