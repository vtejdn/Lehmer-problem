---
author: Yin
---

# Exact matched parity fibers in original quartic bridges at n6 through n10

## Question and scope

For the original quartic P=(1,-1,-1,-1,1), compute complete original returned-word moments at n=6,7,8,9,10, with original digits -1,0,1 at probabilities 1/4,1/2,1/4.
[C55](../../../claims/Yin_C_G0055_v1.md) owns the complete mathematical reduction and finite onset statement.
The author g0001_routes supplied the new derivation/program; root supplied the broad question and coordination.
The author program independently implements parity matching and contiguous-beta-half matching, with exact agreement on full return mass and total neutral midpoint second moment.
These two author implementations share helpers and are not a noncontributor review.

The candidate is the first lexicographically ordered matched additive translation of the C51 shortest gamma-fiber pair, in increasing n and strict midpoint-crossing shift order.
It replaces (A,-1,-1,-1,-1,B) by (A-1,1,1,1,1,B-1), A,B in {0,1}, preserving every outside same-parity digit and requiring an actual matching odd endpoint.
Candidate selection stops after the first witness; all five complete moment calculations continue.

## Files and reproduction

[main.py](main.py) supervises [worker.py](worker.py); [verify.py](verify.py) is the separately authored verifier.
Both supervised commands use standard-library integer/Fraction arithmetic, a live 180-second supervisor limit and a 175-second worker deadline.
Default outputs use this J's ignored output home, independently of caller cwd.

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0091/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0091/verify.py
```

The author needs no generated input.
The verifier reads the full result.json (`mathematics/computations/outputs/Yin_J_G0091/result.json`) only for comparison and writes verification.json (`mathematics/computations/outputs/Yin_J_G0091/verification.json`).
Complete outputs are published atomically; incomplete rows remain distinguishable and successful publication removes transient progress.
The author output contains every matched endpoint row and exact moment/witness data, not an expanded list of every enumerated word.

<a id="completed-exact-parity-run"></a>
## Completed sole execution and actual finite outcome

The author completed the declared calculation on 2026-10-12.
All 88,209 words per grouping and 176,418 total visits were processed, with full original probabilities, support, centering, sign and total-covariance checks.

| n | matched endpoint pairs | pairs with positive within-parity innovation | original return mass numerator C_n over16^n |
| --- | --- | --- | --- |
| 6 | 75 | 0 | 7296 |
| 7 | 201 | 0 | 35120 |
| 8 | 539 | 8 | 170848 |
| 9 | 1435 | 42 | 835448 |
| 10 | 3921 | 138 | 4119392 |

The denominator in the last column is 16^n.
The first candidate is n=8, shift 1, A=1, B=0 and outside translation gamma^7-1.
Its even words are (-1,1,-1,-1,-1,-1,0,1) and (-1,0,1,1,1,1,-1,1); the matching odd word is (1,1,1,0,-1,-1,-1,0).
Both full interlaced words divide exactly by P and each has original probability 2^-29.
The even and odd endpoint masses have integer numerators 4 and 4, yielding conditional endpoint mass 1/10678.
The midpoint squared difference is 5+2sqrt(13), giving this endpoint contribution (5+2sqrt(13))/42712 and full n=8 within-parity trace 7(5+2sqrt(13))/53390.
Total midpoint motion is already positive at n=6,7 although their within-parity innovation is zero.
Together with C51's singleton result through length 5, this identifies original length 16 as the first positive time of this parity certificate, not first total midpoint motion.

<a id="independent-verification-declaration"></a>
## Independent verification method

The noncontributor g0001_review_recovery reviewer uses generic convolution/reduction modulo original P, complete contiguous-half returned-word reconstruction, then parity regrouping and direct weighted prefix first/second moments.
It imports neither author program and does not use the author's cross/penalty formulas as its calculation path.
An independently formed basis inverse converts gamma labels solely for comparison; exact rational-square tests determine neutral signs.
All original weights, marginal endpoints, full matched rows and deterministic candidate fields are compared after independent reconstruction.

<a id="independent-verification-complete"></a>
## Completed independent finite verification

The separate calculation completed on 2026-10-12 and matched all 6,171 endpoint groups and reconstructed 6,387 complete returned words, with per-n word counts 75,201,547,1481,4083.
It verified every mathematical matched-row field, full original-law moment decomposition and entire first witness.
With tau_-=(1-sqrt(13))/2, the within-parity traces are 0, 0, (49-28tau_-)/53390, (960-536tau_-)/522155 and 383/111940-(7409/3861930)tau_-.
The candidate contribution is equivalently (7-4tau_-)/42712.
[R795](../../../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) owns the whole proof/program/output finding; subsequent Claim extraction has its own scope.
No asymptotic growth, diffusive limsup, uniform gap or native statement outside n=6--10 follows.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.

## Recorded runs

The local output names below identify the particular recorded runs used by the linked fixed materials.
Those records retain the original inputs, parameters, known dates and checked scopes; the existing instructions above identify the programs and reproduction commands.
These links locate the original results and checks, without asserting verification of the present README or a new execution.
Generated output files remain local and are not synchronized.

| Local run output | Original result or check record |
| --- | --- |
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0795_v1.md#c55-matched-parity-actual-extraction-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0795_v1.md#current-g0055-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0795_v1.md#c55-matched-parity-actual-extraction-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) |
