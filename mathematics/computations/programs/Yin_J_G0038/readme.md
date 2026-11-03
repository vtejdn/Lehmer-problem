---
author: Yin
---
# Independent certificate check for the height-one negative phase construction

Assigned noncontributor review of [L179 retained construction](../../../audits/reviews/Yin_R_G0078_v1.md#height-one-negative-phase-independent-review) and [J37](../Yin_J_G0037/readme.md).
Only the fixed degree63 input is computed.

The independently written [review.py](review.py) reconstructs all64 coefficients from binary adjacent-one parity, rather than importing the author's recursion program.
It then checks the six recursive relations and paired Laurent autocorrelations exactly, compares the entire coefficient list with the author artifact, and checks exact squarefreeness.
A fresh root isolation at320-bit working precision, with maximum1024 bits and requested radius2^(-180), returns63 pairwise disjoint balls:31 strictly exterior and32 strictly interior.
Their exterior modulus product is enclosed near6.85057293091927989912365455877 and rigorously exceeds137/20.
The exact rational four-copy phase comparison and both elementary averaging-cutoff comparisons also pass.

review.json (`mathematics/computations/outputs/Yin_J_G0038/review.json`) retains the complete output and root-ball displays.
The verified four-copy cutoff is n>=90071987178700800 with D_4=16777215; this is a proof parameter, not a polynomial expanded in this check.

From the repository root, run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0038/review.py`.
The checker uses Python with python-flint; all assertions passed.
The implementation is separately written and stronger in precision, but shares FLINT/Arb's rigorous root-isolation library with the author; that library's internals were not independently proved.
Polynomial evaluation containing zero is only a supplementary consistency check, not the basis for root existence or completeness.
Rounded ball displays are not substituted for the actual rerunnable ball operations.
No high-degree f or separated product was expanded.
The complete written proof and scope finding is appended in D45; no fixed promotion or unrestricted G0001 conclusion is implied.

The current [R647 whole independent finding](../../../audits/reviews/Yin_R_G0647_v1.md#isolated-height-one-negative-whole-finding) covers the complete mathematical construction and original fixed evidence, including one original-domain J38 read-only replay at2026-10-21T20:10.
The original R78 whole arrangement remains UNKNOWN, the earlier R773 SELF and original executions remain historical, and no producer/native bytes were changed.
The exact classical paired-recursion attribution is retained in [Erd14-U001](../../../audits/literature/Erd14/Yin_U001.md#erd14-u001), without importing that paper's Mahler theorems or replacing this seed certificate.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
