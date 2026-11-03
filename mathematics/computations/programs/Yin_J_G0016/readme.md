---
author: Yin
---
# Signed Coxeter cover and mutation controls

## Question and scope

Exact finite tests for the determinant-preserving signed Coxeter mutations developed in [D G0009](../../../claims/Yin_C_G0002_v1.md).
Test a canonical sign double cover, its added determinant factor, and whether mutation reduces the sign-cover cost on explicit controls.
No unrestricted representation or Mahler-gap conclusion is claimed.

## Files

- [main.py](main.py): integral Stokes mutations, signed cover, exact dense-family controls, fixed-degree growth witness, and bounded orbit experiment.
- results.json (`mathematics/computations/outputs/Yin_J_G0016/results.json`): reproducible exact output, including every terminal matrix and its seeded discovery walk.
  The fixed-degree witness is also retained literally in the program.

## Reproduction

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0016/main.py
```

The structural_research authoring agent executed the program for Yin using SymPy.
All matrices, polynomials, determinants, energies and sign tests use exact integer/rational arithmetic.
There is no floating-point eigenvalue or Mahler-measure computation.
Output is regenerated at `mathematics/computations/outputs/Yin_J_G0016/results.json` after the whole run succeeds.

The orbit experiment has random seed 926104, 80 independent 24-step walks from the Y_(2,3,7) ten-vertex tree, and energy cap 60 at each sampled move.
Both adjacent mutation directions are available.
Greedy descent chooses the candidate of least squared-upper-entry energy, breaking ties by index and then forward direction, and takes only strict decreases.
The small plateau escape uses a breadth-first equal-energy search with node cap 4000; the retained rank-five escape was found after 14 discovered nodes.

The fixed-degree witness was initially found in a separate interactive random walk with seed 10109 after 3151 moves.
That discovery walk is not needed for the result: the literal witness is directly checked by two determinant calculations in this program.
The proof of its all-parameter growth is in D G0009.

Generated data are retained locally and excluded from Git; a clone can lack them.
Required verification inputs remain explicit, without automatic producer execution or a substituted result.

## Results and limits

The completed run verified:

- The dense neutral family and its explicit congruence to the A_n chain for every n=2,...,12, and full signed-cover determinant factorization for n=2,...,7.
- A strict adjacent-descent trap at n=5 with energy 5 and cyclotomic polynomial 1+t+...+t^5.
  Two specified forward moves escape with energies 5,5,4 to a switchable chain.
  All eight one-move energy changes and both matrices are retained.
- An exact 10 by 10 signed matrix with Lehmer polynomial, checked by its characteristic polynomial and independently by det(zV+V^T) at eleven integers z=-5,...,5.
  Seven family members k=0,...,6 preserve the same polynomial under double mutation.
  Their energies are 92, 1073, 48602, 2281484, 107179409, 5035149002, 236544821948.
  The growing absolute-presentation traces satisfy the derived bound trace>=energy-10.
- All 80 sampled walks end at literally distinct ordered matrices with the exact Lehmer polynomial.
  Strict greedy terminal energies are 9 through 13, and 66 of the 80 are nonswitchable.
  These are counts within this particular seeded experiment, not orbit classes or frequencies under a natural measure.

The trial assertion that strict descent always makes dense neutral matrices switchable failed.
The corrected completed run retains the mathematical failure as the rank-five trap rather than omitting it.
The finite data do not establish a universal reduction algorithm, an optimized cover-cost bound, an integral Stokes representation for arbitrary reciprocal input, or the Lehmer gap.
The general signed-cover identity, congruence, mutation formula and unbounded fixed-degree cost are derived directly in [D G0009](../../../claims/Yin_C_G0002_v1.md).

## Separate witness check

The coordinating reviewer separately implemented [review_witness.py](review_witness.py), reading the retained literal witness but importing no authoring helper or SymPy.
Run `python -B mathematics/computations/programs/Yin_J_G0016/review_witness.py` from the repository root.
The separate program checked 77 exact integer Bareiss determinants across k=0,...,6 under the constant two-move congruence.
All polynomials, saved energies and coupling rows matched.
review-witness.json (`mathematics/computations/outputs/Yin_J_G0016/review-witness.json`) retains this limited result.
This did not rerun the random discovery sample or audit external sources.
The separate written review of the all-parameter proof is recorded in D G0009.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
