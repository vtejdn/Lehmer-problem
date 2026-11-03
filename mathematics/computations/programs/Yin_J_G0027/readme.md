---
author: Yin
---

# Independent normalized Lehmer convex-body certificate check

## Question and scope

Reproduce J G0024's exact certificate without changing author outputs and independently implement the normalized-axis geometry and uniform drop check.

The current complete mathematical home is [C399](../../../claims/Yin_C_G0399_v1.md#lehmer-infinite-core-proof).
The linked original R records the complete proof review as SELF after its actual earlier substantive target inputs; independently implemented arithmetic retains its separate scope.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Reviewer source rerun with output routing, then separately implemented normalized edge-system certificate check. |
| source-verification.json (`mathematics/computations/outputs/Yin_J_G0027/source-verification.json`) | Reproduced author exact payload under the reviewer runtime. |
| independent-verification.json (`mathematics/computations/outputs/Yin_J_G0027/independent-verification.json`) | Independent root brackets, axis barycentric enclosures, positive denominator bounds and cell-specific additive drops. |

## Reproduction

From repository root run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0027/verify.py`.
Dependencies: Python, python-flint and SymPy.
No randomness or numerical optimizer is used.
Outputs use `mathematics/computations/outputs/Yin_J_G0027/`; the original J G0024 output is not overwritten.

The source rerun imports J G0024 verify.py, including its J G0022 primitives, and passes an explicit reviewer output destination.
It compares every mathematical result field to the retained author output.
The independent calculation reads the original integer words, rational targets and grid.
It reuses only this reviewer's [J G0023](../Yin_J_G0023/verify.py) independent_roots and vertex helpers, then performs new 8 by 8 edge solves for the normalized vertices.
Root isolation is exact to width 2^(-240); Arb arithmetic uses 300-bit precision.
Every normalized denominator, barycentric sign and claimed drop is checked with propagated interval errors.

## Results and limits

The source payload matched, with the author file preserved.
The independent calculation passed all 32 normalized axis certificates and all 288 full closed-cell word uses, including their intermediate expanding-strip bounds.
There are 217 distinct words, each of length at most eleven.
Every squared displacement denominator is strictly positive, and both cell-specific minimum costs, weights and additive drops meet or exceed the source's reported rational bounds.
The independent drops are approximately 0.5707382335... and 0.5971013309..., with the full enclosures retained; the common claimed lower bound is 57/100.

The [full written review D G0023](../../../audits/reviews/Yin_R_G0069_v1.md#normalized-lehmer-radius-eight-review) owns the logical transition from cross-polytope containment to uniform actual-state descent and the real-strip, zero-prefix and finite-residue arguments.
This computation supplies independently implemented finite evidence, not formal verification.
Complete radius-eight descent is distinct from compact enumeration/termination, an infinite actual Lehmer core and a uniform probability or gap estimate.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
