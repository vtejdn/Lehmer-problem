---
author: Yin
---

# Complete original quartic local-update graphs at n4 through n10

## Question and scope

For the original quartic P=(1,-1,-1,-1,1), enumerate every original length-2n returned ternary word at n=4,...,10, retaining weight 2^(number of zero digits) over denominator 4^(2n).
Build every legal nonzero one-site quotient update delta in {-2,-1,1,2}, all components and masses, the zero component and all frozen words.
[C64](../../../claims/Yin_C_G0064_v1.md) owns the complete finite interpretation and separate all-n proof.
Rounding-recovery authored the native construction; root supplied the broad question and execution-scope inspection.
J91 counts are secondary crosschecks, not a generator or graph oracle.

## Files and reproduction

[main.py](main.py) uses complete contiguous-half endpoint matching, full original-P division and direct legal perturbations.
The noncontributor reviewer's [verify.py](verify.py) uses complete even/odd matching, low-end quotient reconstruction, quotient-coordinate fibers/cliques and union-find.
Every independently constructed word, quotient, weight, adjacency, component/member/mass and summary is compared with the author's full payload.
Neither program uses numerical roots, floating mathematical tolerances or an imported author helper for independent reconstruction.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0092/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0092/verify.py
```

Both use the repository standard-library Python environment and Windows working-set checks.
Live limits are 120 supervisor seconds, 115 worker seconds and 512 MiB, with structural caps of 60,000 halfwords, 100,000 vertices and 5,000,000 directed neighbors per n.
The author requires no generated input; the verifier requires result.json (`mathematics/computations/outputs/Yin_J_G0092/result.json`) and writes verification.json (`mathematics/computations/outputs/Yin_J_G0092/verification.json`).
Paths resolve from the actual J location, and canonical complete results are published atomically only after all declared checks.

<a id="quartic-local-graph-native-completion"></a>
## Completed single execution

The author calculation completed on 2026-10-12 with every declared word, quotient, edge, component and exact mass retained.

| n | Returned words | Original integer mass W_n | Undirected edges | Components | Frozen vertices | Zero component size | Zero component mass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 11 | 328 | 16 | 1 | 0 | 11 | 328 |
| 5 | 29 | 1532 | 50 | 3 | 2 | 27 | 1524 |
| 6 | 75 | 7296 | 160 | 7 | 6 | 69 | 7200 |
| 7 | 201 | 35120 | 486 | 11 | 6 | 171 | 34096 |
| 8 | 547 | 170848 | 1496 | 15 | 8 | 449 | 163392 |
| 9 | 1481 | 835448 | 4478 | 23 | 14 | 1165 | 785520 |
| 10 | 4083 | 4119392 | 13560 | 51 | 34 | 3063 | 3799280 |

Each row's unconditional return probability is W_n/4^(2n), and each component's conditional mass is its integer mass divided by W_n.
The all-n frozen-family statement has a separate polynomial/window/seam/padding proof; finite table agreement does not prove it by extrapolation.

<a id="quartic-local-graph-independent-verification-declaration"></a>
## Independent verification method

The separately assigned g0001_review_recovery reviewer reconstructed all original even/odd-position words using generic monic polynomial division.
Original weights are counted directly; low-end quotient reconstruction checks the entire high residual.
Grouping legal quotients by every coordinate except one gives the complete update clique, and each edge is checked against its actual shifted-P digit difference.
Canonical union-find components and the signed-window criterion independently verify component and frozen-word data.

<a id="quartic-local-graph-independent-verification-completion"></a>
## Completed independent reconstruction

The distinct calculation completed on 2026-10-12, matching every mathematical field across 6,427 words, 20,246 undirected edges, 111 components and 70 frozen vertices.
It retained the full independently rebuilt graph, not only counts or equality flags.
The historical review also inspected the original operational records; these are not mathematical verification inputs.
[R279](../../../audits/reviews/Yin_R_G0279_v1.md#quartic-frozen-components-whole-independent-finding) retains the whole proof/native scope.
This supports the connected n=4 graph and disconnected n=5--10 graphs only, with no n<4 or n>10 native claim, eigenvalue magnitude, asymptotic midpoint growth or unrestricted gap.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
