---
author: Yin
---
# Exact longer-cycle Stokes surgery controls

## Question

Test a changed local cycle operation beyond the five-cycle example, including the effect of order and arbitrary attachments.
The associated structural argument owns the mathematical derivation.
No capped search failure will be called an impossibility proof.

The responsible complete derivation, hypotheses and scope are in [C437v2](../../../claims/Yin_C_G0437_v2.md#retained-cycle-proof).
This is a bounded exact mechanism study; no unrestricted scalar-gap or representation conclusion follows.

## Programs and reproduction

- [controls.py](controls.py) checks canonical cycles of lengths3--12 and exhausts all233 rank-four integral upper-unitriangular matrices with E<=3.
  It retains controls.json (`mathematics/computations/outputs/Yin_J_G0025/controls.json`).
- [verify_family.py](verify_family.py) separately implements mutation congruences, symbolically checks all intermediate and final coupling formulas with arbitrary earlier/later attachments, verifies both signs of the cycle polynomial using direct determinant evaluations, and checks the rank-four exclusion, explicit lattice Gram identity and degree-barrier controls.
  It retains verification.json (`mathematics/computations/outputs/Yin_J_G0025/verification.json`).

From the repository root, using Python with SymPy:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0025/controls.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0025/verify_family.py
```

Both retained results pass their exact checks; no numerical approximation is used.

## Results

The consecutive-order n-cycles have energies n,n+1,...,n+1,n-1 for n>=4; the length-three control decreases directly3->2.
The rank-four order(0,2,1,3) yields (t^2+1)^2, which none of the233 lower-energy candidates realizes.
The second checker rules them out already by determinants at1 and-1:32 candidates survive the first value and none the second.

Five symbolic path blocks of sizes3--7 contain all15--35 independent couplings to two earlier and three later vertices, together with arbitrary outside blocks.
Every prefix and final formula passes.
Both cycle-polynomial formulas pass on all76 orderings for n=3--6, modulo rotation/reversal; each uses n+1 exact determinant evaluations.
The checker also verifies the explicit even-sum-lattice Gram basis and index two for n=4--12, and twelve first-step degree controls for cycle lengths4--6 with0--3 leaves per cycle vertex.

The all-size statements are proved by the complete determinant expansion, basis calculation and lattice/degree arguments in [C437v2](../../../claims/Yin_C_G0437_v2.md#retained-cycle-proof).
The bounded symbolic and enumeration controls do not replace those proofs.
Programs were authored by the same structural agent, so separate implementation is not an independent-agent review.
The general non-switchability obstruction preserves rank and integral congruence; its isolated-cycle polynomials and absolute-cover factors are cyclotomic, with zero extra Mahler cost.
The pendant family supplies no small-measure coverage assertion.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
