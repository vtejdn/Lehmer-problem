---
author: Yin
---

# Finite tests of the binary-product endpoint correction

## Question and scope

This group retains the finite construction and measure diagnostics for the r>=2 endpoint correction in [L456 v2](../../../ledger/Yin_L_G0456_v2.md#binary-product-finite-computation), following the rounding and endpoint-kernel exploration in [v1](../../../ledger/Yin_L_G0456_v1.md#rounding-counterexample-boundary).
The tested parameters are r=2,3,4,5,6,7 and k=2^r.
The exact integer construction, reciprocal symmetry, value at one, closed formula and modulo-two auxiliary are checked for all six parameters.
SymPy exact factorization and double-precision root-based measure diagnostics are retained only for r=2 through 6.
The attempted r=7 factorization did not complete and was stopped; no factorization, irreducibility or root-based measure result is claimed there.
The r=7 completed diagnostics are full-polynomial shifted-FFT logarithmic integrals.

## Files

- [main.py](main.py) constructs the specified six inputs and produces the bounded results.
  It never attempts r=7 factorization.
- Generated [results.json](../../outputs/Yin_J_G0139/results.json) belongs to this group's ignored output home and is reproducible from the program without other inputs.

## Reproduction

From the repository root, run:

```powershell
python mathematics/computations/programs/Yin_J_G0139/main.py
```

From another working directory, use the corresponding absolute path to main.py.
The script resolves its output home from its own group location.
It requires SymPy and NumPy; the original calculations used SymPy 1.14.0 and NumPy 2.4.4.
All polynomial coefficients, closed-form checks, factor reconstruction and modulo-two checks use integer or exact symbolic arithmetic.
Factorization uses SymPy factor_list; the returned exact factors are multiplied back into the original polynomial.
The floating calculations use double-precision NumPy roots and shifted circle averages.
They have no certified error bounds and are not mathematical proof inputs.

The factor-based diagnostics use all factors with their multiplicities.
Cyclotomic factors are assigned their exact zero measure.
For r=2 through 6, two direct evaluation grids have 16384 and 65536 samples and angular offset 0.371.
For r=7, two shifted FFT grids have 262144 and 1048576 samples with the same offset.
The program writes a single result JSON only after every claimed bounded computation completes.
The retained program completed successfully on 2026-11-06 and wrote the linked output.

## Results and limits

The original finite calculation found Phi_6 times one degree-14 noncyclotomic factor for r=2.
For r=3,4,5,6, factor_list returned the whole degree-32,64,128,256 polynomial as one irreducible factor.
The corresponding whole-polynomial logarithmic-measure diagnostics were approximately 0.30162, 0.64811, 0.90915, 1.10680 and 1.29947.
The r=7 full-circle integral diagnostics were approximately 1.45650 and 1.45639 on the two specified grids.
These floating values suggest increasing cost in the tested range and supply no certified inequalities or all-r conclusion.

The subsequent [all-parameter modulo-two exclusion](../../../ledger/Yin_L_G0456_v2.md#binary-product-complete-original-return) belongs in the responsible ledger argument and does not rely on these numerical observations or finite irreducibility results.
This group is ordinary author computation, not an independent project review.
