---
author: Yin
---
# Simultaneous two-column root-basis and changed-order test

## Question and scope

Responsible [C429](../../../claims/Yin_C_G0429_v1.md#statement) retains the complete changed two-column/order theorem beyond L250's fixed-order single-column construction.
For the exact G0 and path basis Q0, test all15 pairs of positions and every ordered pair of actual norm-two roots in {-1,0,1}^6.
Both new columns must satisfy the norm equations and their exact2-by-2 replacement minor must be +/-1.
The pre-run cap is15*114^2=194940 pairs.
Separate old single-column controls from genuine changes.

A subsequently declared changed-order extension deduplicates signs and unordered bases among the genuine changes and tests all60 cyclic/reversal representatives.
The proved simultaneous invariance of BOTH original and absolute polynomials makes this complete for ordering of those fixed bases.
Its pre-run cap was15379 bases and922740 orders.
The actual count is7446 bases and446760 orders.
A final diagnostic changes only the scalar target to the explicitly displayed S6=t^6-t^4-t^3-t^2+1, on that SAME finite set.
No larger root cube or basis class was added.

## Files

| Program | Native output | Actual role |
| --- | --- | --- |
| [search.py](search.py) | search_result.json (`mathematics/computations/outputs/Yin_J_G0055/search_result.json`) | Complete194940-pair fixed-order test, actual114 roots, exact minor/Pfaffian/first coefficient, every position count and target hit. |
| [orders.py](orders.py) | orders_result.json (`mathematics/computations/outputs/Yin_J_G0055/orders_result.json`) | Reconstruct and deduplicate genuine bases, complete60-order test for Phi6 P4, full coefficient/energy histograms and height. |
| [smaller_control.py](smaller_control.py) | smaller_result.json (`mathematics/computations/outputs/Yin_J_G0055/smaller_result.json`) | Same basis/order scope with secondary S6 target, preserving a separate output. |
| [verify.py](verify.py) | verification.json (`mathematics/computations/outputs/Yin_J_G0055/verification.json`) | Distinct full polynomial subset expansion on3 actual bases, all720 orders each, full original/absolute/cover checks and scalar Bareiss cover checks. Additional SAME-author verification. |

No external data, network access, numerical root oracle or retired-draft runtime dependency is required.
The displayed seed is the actual input.
The verification program reads the native mathematical payloads, not a material hash.
Reviewer-only files, if later added, are separate from these nine author files.

## Reproduction

Run from the repository root using the Python standard library.
Every mathematical branch uses exact integers.
Execute in dependency order:

~~~powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0055/search.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0055/orders.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0055/smaller_control.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0055/verify.py
~~~

Each command writes its named regenerable JSON in this J output home.
No .tmp mathematics, floating decision, random seed or partial-result publication is used.

## Results and limits

The fixed-order test processed194940 pairs,64736 unimodular pairs,3220 old single-column controls,61516 genuine pairs and11248 Pfaffian±3 cases, with no full target.
The changed-order test has7446 distinct sign-normalized unordered bases and446760 orders,79867 Pfaffian±3 cases and no Phi6 P4 target.
The same-domain S6 test has71095 Pfaffian±1 cases and no target.
Complete target parameters, energy histogram and height are retained.

The coefficient histograms show a!=2 mod4 among the tested Pfaffian+/-3 cases and a!=0 mod4 among the tested Pfaffian+/-1 cases.
These are EXACT FINITE observations only, not unbounded congruence theorems.
The candidate energies range17--69 and maximum strict-upper height is3.
The [full C429 cost argument](../../../claims/Yin_C_G0429_v1.md#two-column-complete-cost-scope) retains all original/absolute/cover definitions, the full literal factorization, coarse scalar-measure bounds and the unchanged cheaper L191 Phi2^2 P4 control.
The secondary polynomial is a smaller positive-measure scalar by a local proof, but no matrix realizing it was found.
There is no target realization, finite or global optimum, unbounded two-column exclusion or unrestricted gap result.

The added author verifier expands4320 complete degree-six polynomials:3 explicit bases times720 labelled orders times original/absolute.
It checks their exact60 dihedral classes, reciprocal endpoints and first coefficients.
Three complete degree-twelve cover expansions and39 additional integer Bareiss values check the full cover factorization.
These checks passed.
They are a different calculation by the SAME author; they do not replace separately organized noncontributor review of the full program or its complete finite coverage.

Source scope: the prior HPM22 seed attribution and local L246/L250 proofs are reused.
A search returned only unadopted primary-source discovery snippets for the secondary polynomial; no page, minimality theorem or new source identity is accepted.
The direct scalar facts needed for the target are proved in [C429](../../../claims/Yin_C_G0429_v1.md#secondary-sextic-local-facts).
No source registry/artifact was changed.
The complete proof and actual source boundaries belong to C429 and the [original L254 history](../../../ledger/Yin_L_G0254_v1.md#complete-retained-proof-and-review).

## Author self-check and handoff

The unrestricted second-root system, three-column changes and different seeds lie outside this completed finite search.

## Current adoption and complete review scope

The adopted [C429](../../../claims/Yin_C_G0429_v1.md#statement) retains the complete theorem/proof and selected [actual whole SELF finding](../../../audits/reviews/Yin_R_G0630_v1.md#two-column-ordering-whole-self-finding).
The [original entire R117](../../../audits/reviews/Yin_R_G0117_v1.md#two-column-complete-independent-review) is also SELF because shared target counts and limits preceded its finding; its separately implemented original checks and fixed L254/J55 inputs remain unchanged.

The separate [review_independent.py](review_independent.py) and review_result.json (`mathematics/computations/outputs/Yin_J_G0055/review_result.json`) rebuild all729 cube vectors,194940 full basis determinants,7446 bases and446760 order representatives without importing author implementations.
Different determinant/Pfaffian methods recover all150962 target-Pfaffian full polynomials, all counts/histograms, energy17--69 and maximum height3.
Additional36000 symmetry polynomials, all4320 author-sample polynomials and39 literal-cover values also pass.
The entire separately implemented original computation passed.
Its algorithmic distinction does not establish agent-context isolation.
The present fixed-domain reviewer replay reproduced its complete native result with the sole final write intercepted in memory; no author producer or native file was changed.
The proof and independent execution cover exactly the genuine class, retaining the discarded3220 arbitrary-order boundary and finite-only residue observations.

The independent checker remains runnable after retirement of D121; no draft is a mathematical input.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0117_v1.md#two-column-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0630_v1.md#two-column-ordering-whole-self-finding) |
