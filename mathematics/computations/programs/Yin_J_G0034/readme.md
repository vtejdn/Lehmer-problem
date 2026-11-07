---
author: Yin
---
# Independent quartic phase-arrangement and matrix-bound check

Separately implemented review computation for the D34/J33 quantitative two-step certificate.
The responsible [D G0035 finding](../../../audits/reviews/Yin_R_G0803_v1.md#quartic-two-step-independent-review) owns the complete proof review and its noncontributing, nonblind arrangement.
Independent implementation describes code authorship; the R finding does not establish isolated inherited mathematical context.
The author artifacts remain read-only.

## Implementation and reproduction

The retained [verify.py](verify.py) imports no author root, algebraic, phase, matrix or certificate-verifier code.
It uses the explicit nested-radical quartic root with rational square-root enclosures, recomputes all phase events and exact rank-based membership masks, matches the complete integer matrix set and verifies the retained positive-vector inequalities through M(M^T v).
It also checks the new actual lower coset and its Rayleigh quotient through ||M^T h||^2.
Only the standard library is required.
Its fixed source is J33's `inputs/certificate.json`; it requires no ignored discovery output.

```powershell
python -B mathematics/computations/programs/Yin_J_G0034/verify.py
```

The checker uses Python.
It writes its own verification.json (`mathematics/computations/outputs/Yin_J_G0034/verification.json`) only after every assertion passes.
Source discovery and verification programs were read but not rerun; this is a separate full implementation using their retained integer witnesses, not a claim of independent discovery.

## Exact executed scope

The checker independently proves a sufficient coordinate box[-7,7]x[-6,6], then enlarges to the author's complete declared box[-8,8]x[-7,7] to compare its phase partition.
It reconstructs63 by65 axis intervals,4095 interior cells, all16637 phase faces including12542 lower-dimensional cases, and512 axis boundary-subset checks.
The complete set of138 integer matrices is equal to the source set, with maximum dimensions13 by13.
All138 strictly positive integer vectors and1615 coordinate inequalities pass, with minimum integer slack999999951 and q=97.

The actual lower representative(-413,774,0,-180) lies in independently reconstructed phase cells(14,38), with zero-based interval indices.
Its strict block equals the retained witness matrix.
The exact Rayleigh numerator and denominator are9633565984214612 and100000003825002; their ratio is strictly greater than96.
The upper certificate and that actual lower witness therefore support sqrt(96)/16 < ||K^2|| <= sqrt(97)/16, subject to the full operator/coverage proof reviewed in D35.

An initial reviewer run stopped because it incorrectly required the independently derived tighter box to equal the source box.
Replacing that overly restrictive assertion by proved inclusion and an explicit enlargement repaired the checker; it did not change or challenge the author inputs.
The corrected checker includes all upper and lower checks.

This is independent computation within the disclosed separately organized review, not formal proof verification or personal human inspection.
It covers the fixed quartic phase certificate, not the original Lehmer input, an optimized norm, a general Salem family or a uniform Mahler gap.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
