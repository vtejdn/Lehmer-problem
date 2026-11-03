---
author: Yin
---

# Certified degree-scale moments of the plastic Salem phase map

## Question and scope

Determine exact or validated signs of the phase-map moments for an actual accepted primitive Salem family, with fixed positive limiting Mahler measure.
This does not construct a near-one sequence.

The responsible [C408 complete argument](../../../claims/Yin_C_G0408_v1.md#retained-salem-energy-argument) proves the circle phase relation, the residue formula, the moving-frequency limit and the exact positive-Salem damping identity.
The fixed family input is [L G0131](../../../ledger/Yin_L_G0131_v1.md), using [L G0038](../../../ledger/Yin_L_G0038_v1.md).
This J does not reprove their irreducibility classification.

## Files

- [main.py](main.py): 400-bit Arb evaluation of the finite residue coefficient for c_k, 1<=k<=32, and the 16 dyadic products -c_k c_(2k)/k.
  It isolates the plastic root by exact rational bisection to width <=2^(-320).
  The c_1/c_2 outputs are cross-checked against separately displayed closed formulas.
  results.json (`mathematics/computations/outputs/Yin_J_G0030/results.json`) retains the intervals and all signs.
- [exact.py](exact.py): a separately implemented finite formal-series calculation in Q(theta), with theta^3-theta-1=0.
  It reduces c_4, c_8 and -c_4 c_8/4 to rational quadratic expressions and proves their coarse enclosures by exact rational interval substitution.
  The interval endpoints for theta have exact opposite polynomial signs.
  exact-results.json (`mathematics/computations/outputs/Yin_J_G0030/exact-results.json`) retains the reduced coefficients and rational bounds.
  No main.py output is used as an oracle.
- [finite_input.py](finite_input.py): one actual P_129 input, degree 132 and Fourier frequency 516.
  Sparse exact Newton sums through 1032, an exact root bracket of width below 2^(-800), and 1000-bit Arb arithmetic certify the actual coefficient using the written Salem identity.
  finite-result.json (`mathematics/computations/outputs/Yin_J_G0030/finite-result.json`) retains the input, exact sums, root bracket and interval result.
  A second expansion by pair types is a same-author consistency check, not an independent proof.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0030/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0030/exact.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0030/finite_input.py
```

Dependencies: Python, SymPy and python-flint.
The first and third programs use Arb balls, not unvalidated decimal roots.
The middle program uses only exact rational/number-field arithmetic.
None uses randomness or numerical integration, and none truncates an infinite Fourier sum to infer a tail bound.
Reruns replace their corresponding result JSON with the recalculated mathematical payload.

## Results and limits

All 32 residue intervals, the c_1/c_2 closed-form comparisons and the 16 dyadic-product signs passed.
The exact calculation certifies c_4<0<c_8 and

    0.021931 < -c_4 c_8/4 < 0.021932.

The actual degree-132 calculation certifies

    -C_516(P_129)/(516*132)
        =0.02142602846843519960... > 1/50.

The responsible fixed argument proves that this finite value is part of an actual irreducible primitive family with positive linear fourth-delay Fourier contribution.
Its Mahler measure tends to the plastic number, not one.
A positive term does not bound the complete signed mixed-resultant sum.
The computation therefore supplies no new arithmetic surplus, high-band upper bound or Lehmer conclusion.
Exact/ball arithmetic and the analytic reduction remain implementation-dependent evidence; no independent verifier or independent mathematical review is claimed in this J.

The complete mathematical argument resides in [C408](../../../claims/Yin_C_G0408_v1.md#retained-salem-energy-argument).
The original fixed account and actual historical whole-review scopes remain in [L G0174](../../../ledger/Yin_L_G0174_v1.md#retained-salem-energy-argument); current finding relationships belong to the exact selected C and R.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
