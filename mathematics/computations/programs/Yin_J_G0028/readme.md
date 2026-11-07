---
author: Yin
---

# Independent Lehmer compact-superset enumeration check

## Question and scope

Independently validate J G0026's exact enclosing certificate and reproduce the integer candidate set.

The current complete mathematical home is [C399](../../../claims/Yin_C_G0399_v1.md#lehmer-infinite-core-proof).
The linked original R records the complete proof review as SELF after its actual earlier substantive target inputs; independently implemented arithmetic retains its separate scope.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Independently implemented embedding/LDL/enclosure validation and complete Python-integer enumeration with range-checked NumPy outward filters. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0028/verification.json`) | Certificate checks, exact arithmetic-size bounds, complete traversal counts and all-state comparisons. |
| independent-states.bin (`mathematics/computations/outputs/Yin_J_G0028/independent-states.bin`) | Complete independently reproduced candidate list in explicit little-endian uint64 form. |

## Reproduction

From repository root run `python -B mathematics/computations/programs/Yin_J_G0028/verify.py`.
Dependencies: Python, NumPy, SymPy and python-flint.
Inputs are J G0026's tracked inputs/enumeration-certificate.json, inputs/compact-states.bin.gz and inputs/enumeration.json.
The checker decompresses the native binary and compares every regenerated mathematical state and its sequence order; no previous author output is required.
The code imports no author enumeration/checker code.
It reuses only the reviewer's own J G0023 independent_roots helper; that helper checks irreducibility and isolates all trace roots exactly.

The certificate check uses 320-bit Arb with root intervals of width at most 2^(-240), exact integer/rational matrix arithmetic, and independently checked coefficient/overflow bounds.
Branching uses arbitrary-precision Python integers and math.isqrt.
Batches of at most 50000 leaf vectors use NumPy int64 only after every family of intermediate magnitudes is bounded below 2^63.
No random seed, floating-point pruning or volume estimate is used.
Explicit caps are inherited as stop conditions: 50000000 nodes and 2000000 candidates.
A partial binary stays separately named until full comparison succeeds.
Ordinary outputs are in this J output home; author data is read only.

## Results and limits

The independent enclosure, inverse-embedding coefficient bounds, unimodular matrix, exact LDL identity, triangular and basis rounding margins, outward filters and arithmetic-size checks all passed.
The complete traversal visited 4818379 nodes and 3077691 full leaves, retaining 797507 unique states without hitting either cap.
Every decoded mathematical state and the full sequence order matched the author's binary, not merely its count or fingerprint.
Explicit little-endian decoding and coefficient-range checks passed.

The complete [written review D G0024](../../../audits/reviews/Yin_R_G0069_v1.md#lehmer-compact-enumeration-review) owns the proof that this is a containing ellipsoid and that no actual K_8 point is lost by the traversal or filters.
This result is a complete finite superset; exact candidate membership, later exclusions, ancestry/path certificates and compact termination are outside this computation's scope.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
