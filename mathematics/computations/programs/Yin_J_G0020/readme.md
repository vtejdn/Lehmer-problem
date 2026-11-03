---
author: Yin
---

# Certified cyclotomic signed-tail calculations

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), [D G0015](../../../claims/Yin_C_G0004_v1.md).

## Question and scope

Evaluate the exact damped-root cyclotomic sums and their low-mode-subtracted tails for genuine reciprocal low-measure inputs and radical controls.
Bounds require validated intervals; numerical output is not an all-degree statement.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact seed factorization and trace-root isolation, exact rational scaled resultants, validated damped-root correction and signed tails, separate root-factor checks. |
| results.json (`mathematics/computations/outputs/Yin_J_G0020/results.json`) | All integer seed coefficients, exact trace-root brackets, precision/scope, 360 tail intervals with checked coarse rational enclosures, and 180 representation-comparison outcomes. |

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0020/`, independently of the caller's directory.
Actual required inputs are read from their producing J output homes; program imports still use the corresponding program homes.
These retained outputs are local and Git-ignored; a clone can lack them.
Verification reports unavailable inputs without automatically rerunning discovery or substituting other results.

## Reproduction

From the repository root, run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0020/main.py`.
The author calculation uses python-flint and SymPy.
Output is written in this J's output home, without a dependency on old output.
Inputs are the six ascending integer coefficient lists in the program, both sign twists, q in {1,2,3,41,101,1009}, r in {1,2,3,4,6}, N=2 and t=1-1/(Dq).
No randomness is used.

Each trace root is exactly isolated in a rational interval of width at most 2^(-240); all subsequent ball arithmetic uses 280-bit working precision.
Scaled polynomial resultants are exact rational numbers.
Transcendental logarithms and the algebraic exterior-root correction use propagated Arb interval enclosures, following the [FLINT interval contract](https://flintlib.org/doc/arb.html), also checked in installed docstrings.
There is no infinite-series truncation.
In addition to each retained ball with radius, the program explicitly verifies a coarse rational enclosure with denominator 10^8.
The float midpoint is used only to propose that coarse interval; its validity is checked against the original ball before publication.

## Results and limits

The completed run certified 360 finite signed-tail intervals and checked the required inequality S_r<=phi(r)H in every case.
It also checked 180 overlaps with the separately evaluated root-factor formula for q<=3.
All six seeds passed exact irreducibility and Salem root-pattern checks.
Root-factor comparisons are same-author cross-checks, not an independent verifier or proof review.
No output is published until all assertions succeed.

For the untwisted q=1 Lehmer seed, the five tails in r order {1,2,3,4,6} are approximately {0.720797,-0.778797,-0.072560,-0.796272,0.857084}; the degree-18 seed has {0.225273,1.517508,0.403283,-0.543440,-0.373168}.
These are rounded summaries, while the exact input data and validated enclosures remain in the JSON.
The opposite actual trace pairs (-1,1) and (1,-1) have constant size.
They do not establish a square-root trace pattern along a near-zero-total-measure family.

The program's seed admissibility is exact.
It does not certify irreducibility of higher-q lifts, a completeness or minimality property of the seed selection, any all-degree numerical inequality, or a sequence with total measure tending to zero.
Total m remains the seed's fixed positive value under lifting.
The [responsible draft](../../../claims/Yin_C_G0004_v1.md) owns the exact object reduction, the all-q fixed-seed bounded-tail argument, and the separately written coefficient-size theorem; those statements are not inferred from the finite table.
No fixed-result adoption or unrestricted G0001 resolution is asserted.

The coordinating AI separately read and reran the complete author program, reproducing all 360 tail certificates and upper bounds and all 180 factor comparisons.
This is separate execution and code inspection of the author program, not an independently implemented algorithm.
The exact written checks and author-interaction disclosure are retained in [D G0015's combined local review](../../../claims/Yin_C_G0004_v1.md#combined-arithmetic-local-review).

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
