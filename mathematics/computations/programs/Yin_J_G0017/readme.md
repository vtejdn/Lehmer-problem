---
author: Yin
---
# Plateau mutation paths for retained Lehmer presentations

## Question and scope

Find exact nonincreasing-energy paths from the 66 nonswitchable terminal matrices retained in J G0016 to switchable Stokes presentations.
Keep finite path validation distinct from unrestricted reduction or representation coverage.

## Files

- [main.py](main.py): bounded plateau search modulo a deterministic diagonal-sign gauge.
- paths.json (`mathematics/computations/outputs/Yin_J_G0017/paths.json`): every input matrix, partial/successful path, resource outcome, and final matrix.
- [barrier.py](barrier.py): the closed 50-state component and a one-unit energy excursion for one exact witness.
- barrier.json (`mathematics/computations/outputs/Yin_J_G0017/barrier.json`): all 50 component states and the three-move excursion certificate.
- [verify.py](verify.py): separately implemented dense congruence replay and symbolic local-surgery checks, authored by the same agent.
- verification.json (`mathematics/computations/outputs/Yin_J_G0017/verification.json`): concise exact-check output.

Input source: J G0016 results (`mathematics/computations/outputs/Yin_J_G0016/results.json`), used read-only.
The mathematical argument is in [D G0012](../../../claims/Yin_C_G0003_v1.md).

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0017/`, independently of the caller's directory.
Actual required inputs are read from their producing J output homes; program imports still use the corresponding program homes.
These retained outputs are local and Git-ignored; a clone can lack them.
Verification reports unavailable inputs without automatically rerunning discovery or substituting other results.

## Reproduction

Run from the repository root in this order:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0017/main.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0017/barrier.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0017/verify.py
```

The verifier uses SymPy.
No floating-point arithmetic is used.
The first program uses exact integer tuples and explicit neighbor updates.
The verifier instead multiplies dense integral congruence matrices, uses a different depth-first sign gauge, and checks the whole accumulated basis transformation.

The search uses all 66 nonswitchable matrices in the retained input and no new random seed.
At each level it explores equal-energy states until finding a strict decrease or a switchable state.
Bounds: 4000 discovered states per level and 12 decreasing/search segments per input.
Discarding a new state at the cap marks the result inconclusive even though the existing queue is still processed.
The barrier search uses at most 1000 states to close the energy-10 component and at most 30000 states for the energy-11 excursion.

## Results and limits

The plateau run found 44 switchable endpoints, 15 fully explored terminal components, and 7 node-cap stops.
It discovered 74307 normalized states over all search segments.
The successful paths use at most nine mutations in this run and end at energy 9.
A terminal component reached after an earlier chosen descent does not prove that every path from the original input is trapped.
The capped searches are inconclusive.

The selected energy-10 witness has exactly the Lehmer polynomial and a triangle-free nonswitchable graph.
Its normalized nonincreasing component has 50 states.
The dense verifier checked all 314 nonincreasing directed neighbors in that component and found it closed and without a switchable state.
A separate search found an exact three-move excursion after 77 discovered states, with energies 10,11,11,9.
Thus the minimum required energy increase for that witness and those operations is exactly one; D G0012 also proves the lower bound through a general triangle-free rigidity argument.

The dense verifier replayed all 261 retained mutations over the 66 inputs, checked each original Lehmer polynomial, accumulated congruences and final matrices, and verified every claimed successful endpoint.
It also symbolically checked the local five-cycle surgery with arbitrary integer tail coefficients and a variable three-dimensional outside block: the relative energies are +1,+1,-1.
The arbitrary-dimension statement is proved by block algebra in D G0012, not by extrapolating that test.

This validates finite paths and a precisely scoped local obstruction/surgery.
It does not classify a braid orbit, prove a general algorithm or an optimized cover bound, establish Stokes representation coverage, or resolve G0001.
The different implementation was written by the same authoring agent and is not independent-agent review.
No failed or capped search is represented as a universal nonexistence result.

The coordinating reviewer read the complete dense verifier and separately reproduced its complete path, closure and symbolic-macro checks.
This was separate execution/code inspection of that verifier, not another full discovery run or a third implementation.
D G0012 records the separate written review of the general rigidity and arbitrary-attachment surgery proofs.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
