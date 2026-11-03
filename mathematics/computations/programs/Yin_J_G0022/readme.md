---
author: Yin
---
# Original Lehmer joint neutral-block experiment

## Question and scope

Test joint eight-real-dimensional neutral displacements of original digit blocks for the Lehmer polynomial.
This is the bounded mechanism experiment in [D G0017](../../../ledger/Yin_L_G0170_v1.md#historical-lehmer-radius1500).

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0022/`, independently of the caller's directory.
Actual required inputs are read from their producing J output homes; program imports still use the corresponding program homes.
These retained outputs are local and Git-ignored; a clone can lack them.
Verification reports unavailable inputs without automatically rerunning discovery or substituting other results.

## Files and reproduction

- [probe.py](probe.py): enumerate original digit blocks of length at most eleven, select full joint eight-dimensional feasible simplices by linear programming, and retain integer words.
- pilot.json (`mathematics/computations/outputs/Yin_J_G0022/pilot.json`): the initial three-cell numerical experiment.
- cover.json (`mathematics/computations/outputs/Yin_J_G0022/cover.json`): the numerical full fifty-cell search, including poorly centered initial simplices.
- [reuse_simplices.py](reuse_simplices.py): reuse already discovered simplices on other cells where all their blocks remain legal; no longer words are introduced.
- reused-cover.json (`mathematics/computations/outputs/Yin_J_G0022/reused-cover.json`): final retained integer block table and nonbinding numerical diagnostics.
- [verify.py](verify.py): standard-library exact outward Fraction interval root/domain, block and joint simplex verifier; it imports no discovery code and ignores all saved decimal geometry.
- verification.json (`mathematics/computations/outputs/Yin_J_G0022/verification.json`): the successful exact run.

Reproduction from the repository root:

Discovery requires the stated NumPy and SciPy dependencies; the shared baseline dependency file does not include SciPy.
Use a compatible existing environment with normal package resolution.
The exact verification command retains its separately stated standard-library dependencies.

```powershell
python -B mathematics/computations/programs/Yin_J_G0022/probe.py --length 11 --cells 50,75,99
python -B mathematics/computations/programs/Yin_J_G0022/probe.py --length 11 --cells 50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99 --output cover.json
python -B mathematics/computations/programs/Yin_J_G0022/reuse_simplices.py
python -B mathematics/computations/programs/Yin_J_G0022/verify.py
```

Numerical discovery uses NumPy and SciPy.
Exact verification uses only the standard library and ignores the saved decimal geometry.

## Results and exact scope

All fifty cells are covered by 450 uses of words of length at most eleven, with seventeen distinct joint simplices.
The exact full eight-dimensional Euclidean neutral threshold is 1500, with squared norm drop at least 5589/1000.
The initial worst numerical threshold around 59923 reduced to about 1326 by cross-cell reuse before exact certification at 1500.

The verifier proves the trace quintic identity and irreducibility modulo two, then isolates its five roots in disjoint rational sign-changing brackets.
It constructs all four unit-circle pairs and checks the full real eight-vector of every displacement.
Fraction Gauss--Jordan inversion encloses the barycentric functions; their positive constants and gradient norms certify actual contained balls.
Every arithmetic operation is rounded outward on a rational grid of scale 10^40.

The responsible proof in D G0017 extends the covered positive annulus by signs and zero prefixes, controls both real strips, and proves finite reduction to a compact ten-real-dimensional algebraic residue.
That residue has not been enumerated or shown to reach zero.
No infinite actual Lehmer core, original-law tail bound, global gap, optimizer optimality, or independent review is asserted by these computation records.

The later complete radius-eight infinite-core theorem belongs to [C399](../../../claims/Yin_C_G0399_v1.md#lehmer-infinite-core-theorem).
This original radius-1500 experiment and its fixed review retain their earlier partial scope.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
