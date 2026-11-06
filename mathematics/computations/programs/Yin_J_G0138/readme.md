---
author: Yin
---

# Cyclotomic central-perturbation full-measure probes

## Question and scope

This computation group tests actual integer polynomials Phi_n(z)-c*z^(phi(n)/2) for the unrestricted [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract).
The minus-two program uses c=2 at n=15,105,1155 and compares complete logarithmic Mahler measure with the small positive real exterior root.
The minus-one program uses c=1 at n=35,105,1155, extracts every cyclotomic factor exactly, and estimates the complete remaining measure.
Neither probe assumes Salem geometry or irreducibility.
The assigned external_structural_lead agent developed and inspected this ordinary author computation for Yin.
There is no independent review or certified numerical root isolation.

## Minus-two files and reproduction

Run `python mathematics/computations/programs/Yin_J_G0138/main.py` from the repository root.
The retained native program is [main.py](main.py).
The program requires NumPy and SymPy and records their actual versions with the Python version in its generated result.
The retained reproduction used Python 3.14.3, NumPy 2.4.4 and SymPy 1.14.0.
It uses exact integer cyclotomic coefficients and exact factorization only for n=15,105.
It evaluates shifted boundary grids with 2^17, 2^19 and 2^21 points using complex double-precision FFTs.
For degrees at most 48 it also computes floating-point roots, treating modulus greater than 1+1e-7 as exterior and imaginary part less than 1e-7 in magnitude as numerically real.
These thresholds are numerical screens, not certified root counts.
There is no randomness or required prior output.
The replaceable generated result is [results.json](../../outputs/Yin_J_G0138/results.json).

## Minus-two results and limits

The completed interactive probe gave approximate total logarithmic measures 0.64456923, 0.94244 and 1.15160 at the three inputs.
The first two numerical root sums agreed with those approximate totals; their positive real exterior roots contributed approximately 0.32228462 and 0.04671623.
The n=15 polynomial factors exactly as (z^4-z^3-1)(z^4+z-1), while the n=105 factorization returned one irreducible degree-48 factor.
A slow attempted factorization at n=1155 was stopped and supplies no irreducibility conclusion.
The retained program reproduces only the completed factorization scopes and does not repeat that unfinished attempt.
The boundary samples and root calculations have no interval error bounds; mesh refinement is not an error certificate or an asymptotic assertion.
The rigorous no-cyclotomic-factor and total-measure lower bounds belong to [L457](../../../ledger/Yin_L_G0457_v1.md#complete-exterior-root-cost) and do not depend on these numerical observations.

## Minus-one files and reproduction

Run `python mathematics/computations/programs/Yin_J_G0138/center_one.py` from the repository root.
The retained native program is [center_one.py](center_one.py), with its own replaceable output [center_one_results.json](../../outputs/Yin_J_G0138/center_one_results.json).
This program was run successfully with Python 3.14.3, NumPy 2.4.4 and SymPy 1.14.0; it records actual dependency versions in each generated output.
Its only inputs are n=35,105,1155, with c=1 and the exact exponent phi(n)/2.
It records full integer coefficients of the original polynomial and the residual after removing all cyclotomic factors, as well as the complete cyclotomic orders and multiplicities.

For input degree D, an integer totient sieve lists all k<=2D^2 with phi(k)<=D.
The exact bound phi(k)^2>=k/2, proved in the program docstring and [L457 v2](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test), makes this order list exhaustive.
The program generates each possible cyclotomic polynomial over Z and rejects it only when its reduction does not divide the original polynomial modulo two.
Monicity preserves degree and nonvanishing on reduction, so an actual integer cyclotomic divisor cannot be rejected by that filter.
Each modular pass is tested by repeated exact integer division on the residual, and exact multiplication checks reconstruction of the original input.
All actual multiplicities are retained; modular passes alone are never called factors.
Complete rational factorization is then run only on residuals of degree at most 48, covering n=35,105 and excluding n=1155.

The residual is evaluated on shifted boundary grids with 2^17, 2^19 and 2^21 points using double-precision FFTs.
For residual degrees at most 48, floating-point roots are also computed and modulus greater than 1+1e-7 is the exterior screen.
There is no randomness, required prior output, certified numerical interval or certified root count.
The original minus-two program and its results.json output remain separate and unchanged.

## Minus-one results and limits

The completed exact extraction gives cyclotomic degree 14 at n=35 and 105, and degree 34 at n=1155.
The corresponding residual degrees are 10,34,446.
The first two residuals each have one irreducible factor, whereas the exact number of irreducible factors of the degree-446 residual is not determined.
Its exhaustive cyclotomic exclusion proves that every irreducible factor of that residual has positive measure; its nonzero degree proves there is at least one.
All degrees and factor counts retain multiplicity.
The complete blocks, their justification and the exact trace reduction showing the absence of all exterior real roots belong to [L457 v2](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-trace-reduction).

The finest residual-grid estimates are approximately 0.24965569, 0.41441535 and 0.74500526 respectively.
The first two numerical root sums are approximately 0.2496548880 and 0.4144129341, with two and eight exterior roots in those screens.
Removing cyclotomic factors preserves total logarithmic Mahler measure exactly, but these numerical estimates have no error certificates.
No root computation or complete rational factorization was performed for the degree-446 residual.
The finite estimates establish neither monotonicity nor a positive-to-zero sequence nor a gap throughout the unbounded-prime-count family.
The separately proved bounded-prime-count exclusion is the [sparse completion in L457 v2](../../../ledger/Yin_L_G0457_v2.md#bounded-prime-count-completion), using the existing accepted DS17 statement rather than numerical evidence.
