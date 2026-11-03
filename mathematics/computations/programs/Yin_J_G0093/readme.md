---
author: Yin
---

# Complete original six-digit endpoint heat-bath graphs at n7 through n10

## Question and scope

For the original quartic P=(1,-1,-1,-1,1), use exactly n=7,8,9,10, N=2n, all original ternary digits at weights 1,2,1 and denominator 4, and all 729 six-digit local words.
[C81](../../../claims/Yin_C_G0081_v1.md) owns the complete finite interpretation; [C76](../../../claims/Yin_C_G0076_v1.md) owns its separately reviewed all-n core paths.
Rounding-recovery authored the new program; root supplied the bounded question and scope inspection.
J92 counts are secondary checks only, without importing its program or vertex/graph payload.

The author constructs every full returned word and P quotient by contiguous-half matching, then every conditional transition using the actual complete outside word and endpoint fiber.
The kernel chooses uniformly among N-5 six-digit intervals and resamples the whole local endpoint fiber with original conditional weights, including unchanged choices.
The complete local/vertex/fiber/transition/component payload, exact true midpoint moments, component projection/residual, two Dirichlet calculations and every specified C76 path are retained.

## Files and reproduction

[main.py](main.py) is the author implementation; [verify.py](verify.py) is the independently authored reconstruction.
Both use exact standard-library integers/Fraction and Windows resource observations.
Live limits are 120 supervisor seconds, 115 worker seconds, 512 MiB working set and 64 MiB per streamed JSON.
Per-n structural caps are 60,000 halfwords, 100,000 vertices, 100,000 global fibers, 5,000,000 conditional entries and 5,000,000 aggregated directed entries.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0093/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0093/verify.py
```

The author needs no generated input; the verifier reads result.json (`mathematics/computations/outputs/Yin_J_G0093/result.json`) for comparison and writes verification.json (`mathematics/computations/outputs/Yin_J_G0093/verification.json`).
Default paths resolve from the actual repository/J location.
Each complete checked case is retained in the pending mathematical payload; an interrupted writing file is not a completed case.
Canonical output replaces its atomic intermediate only after the entire declared domain passes.
Failure retains its actual reached scope; complete diagnostic progress is removed after success, and no resume interface or extra computation is implied.

### Actual one-run outcome

The author completed the declared calculation on 2026-10-12, after the human workspace hold had been released.
All 729 local words form 525 exact endpoint fibers.

| n | Complete vertices | Original integer mass W_n | Global conditional fibers | Nontrivial undirected edges | Components | Frozen vertices | Zero-component vertices | Zero-component integer mass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 201 | 35120 | 1113 | 880 | 1 | 0 | 201 | 35120 |
| 8 | 547 | 170848 | 3793 | 2712 | 1 | 0 | 547 | 170848 |
| 9 | 1481 | 835448 | 12373 | 8158 | 5 | 4 | 1477 | 835384 |
| 10 | 4083 | 4119392 | 39847 | 24632 | 5 | 4 | 4079 | 4119136 |

Directed conditional-entry counts, including diagonals, are 4217,13557,42217,131401; aggregated directed-entry counts are 1961,5971,17797,53347.
All original row sums, detailed balance, sign symmetry, exact returns, component masses and C76 path consistency checks passed.
With u=(1-sqrt(13))/2, the true midpoint second moments are (1324-547u)/2195, (3672-1560u)/5339, (79982-34589u)/104431 and (111909-48309u)/128731.
The invariant component-mean energy is 0 at n=7,8, (32-8u)/104431 at n=9 and (32-8u)/128731 at n=10.
Each of the four frozen singleton components has weight 16 at n=9 or 64 at n=10 and midpoint norm 4-u; the zero component is centered.
The full frozen words, quotients and field midpoints remain in the payload and C81.

<a id="independent-verifier-preexecution-declaration"></a>
## Separately authored independent reconstruction

The noncontributor g0001_review_recovery reviewer disclosed its earlier J92/C64 review roles.
It uses parity-half enumeration, generic high-end monic division, partitioning by complete outside words, union-find components and independently derived trace-ring norms A^2+uAB+B^2 with z^2=uz-1 and u^2=u+3.
Fiber energy uses weighted pairwise-difference variance; component/global variance uses centered vectors; ordered-edge energy includes its factor 1/2.
Core paths are reconstructed by changing integer quotients and multiplying back by P.
No author helper, saved vertex list or source result generates the independent graph.

<a id="six-digit-independent-native-completion"></a>
## Actual independent one-run completion

The distinct reconstruction completed on 2026-10-13 without a failed trial, repair, retry or enlarged domain.
Every mathematical field matched, across 2,978,089 recursive structure/value comparisons; this count includes containers, not only distinct mathematical quantities.
All words, exact weights, original quotients, transition rows, component moments, midpoint decompositions, both Dirichlet energies and every path field were independently checked.
The displayed 17-digit W, 13-digit quotient and eight padded signed frozen words were checked after full graph construction.
Historical terminal summaries were also compared at that time; present verification uses the complete mathematical payload directly.
[R305](../../../audits/reviews/Yin_R_G0305_v1.md#six-digit-finite-whole-native-independent-finding), [R307](../../../audits/reviews/Yin_R_G0307_v1.md#c81-finite-actual-extraction-finding) and [C81's selected decision](../../../claims/Yin_C_G0081_v1.md#decision-organized-reviewed) own the whole/native, extraction and adoption scopes separately.
Connected n=7,8 does not imply a uniform gap; disconnected n=9,10 does not imply infinitely many disconnected lengths or refute an eventual-gap premise.
No all-n freezing/connectivity, mixing rate, asymptotic midpoint result, chronological-mean classification or unrestricted gap follows from this finite computation.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
