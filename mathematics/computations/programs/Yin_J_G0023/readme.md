---
author: Yin
---

# Independent reproduction of the Lehmer joint simplex certificate

## Question and scope

Reproduce the J G0022 exact verifier and independently check decisive joint-geometry and algebraic conventions.

## Files

| File | Role |
| --- | --- |
| [verify.py](verify.py) | Reviewer reproduction with output routing and independent 8 by 8 edge-simplex/whole-cell interval implementation. |
| source-verification.json (`mathematics/computations/outputs/Yin_J_G0023/source-verification.json`) | Rerun of the original Fraction verifier, with all mathematical payload fields compared to the author's output. |
| independent-verification.json (`mathematics/computations/outputs/Yin_J_G0023/independent-verification.json`) | Independent root brackets, cell/geometry interval checks and source-payload comparison. |

## Reproduction

From repository root run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0023/verify.py`.
Dependencies: Python, python-flint and SymPy.
Inputs are the original J G0022 verify.py, reused-cover.json integer-word table and verification.json.
Existing author output is read for the reproduction comparison; the independently implemented geometry uses only the integer words and grid.

The source rerun imports the author's verifier without changing any mathematical function or assertion.
It passes an explicit reviewer output path to the author's verifier while keeping its actual source input unchanged.
The independent calculation uses trace-root rational isolation of width at most 2^(-240), 300-bit Arb arithmetic, forward endpoint translations divided by zeta^k, and 8 by 8 edge-matrix inversion.
It does not use the author's interval functions, augmented inverse, saved decimal roots or geometry.
No random seed or optimizer is used.
Default outputs use `mathematics/computations/outputs/Yin_J_G0023/`.

## Results and limits

The rerun matched every mathematical field of the retained author result.
It reproduced 50 cells, 450 blocks, 17 joint simplices, threshold 1500 and drop 5589/1000.

The separately written calculation independently checked all 450 closed-cell word images and their intermediate expanding-strip bounds, all 17 full eight-dimensional simplex ball/margin conditions, and exact seed irreducibility/root geometry.
All checks passed.
Its per-cell margins and rational root intervals are retained.
The [written full-chain review D G0019](../../../audits/reviews/Yin_R_G0069_v1.md#lehmer-joint-descent-review) owns the review of the original interval code and the mathematical implications to real-strip control and finite compact reduction.

This independently authored checker is additional finite evidence, not a proof assistant or a new result beyond D G0017's partial theorem.
It neither reruns numerical discovery nor establishes compact termination, an infinite actual Lehmer core, an original-law tail estimate, or the unrestricted gap.

The later complete radius-eight infinite-core theorem belongs to [C399](../../../claims/Yin_C_G0399_v1.md#lehmer-infinite-core-theorem).
This original radius-1500 experiment and its fixed review retain their earlier partial scope.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
