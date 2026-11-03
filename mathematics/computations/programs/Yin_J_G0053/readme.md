---
author: Yin
---

# Rank-six integral root-basis and neutral-padding test

## Question and scope

Responsible
[C573 current complete proof](../../../claims/Yin_C_G0573_v1.md#root-basis-neutral-padding-fixed-scope) asks whether a changed non-bipartite integral norm-two basis/order construction can realize Phi6 times the actual quartic P4.
The completed author work proves a full bipartite exclusion and a reflection/sign/order orbit obstruction, then constructs a different unpadded irreducible sextic outside that orbit.
The prescribed Phi6 P4 target remains unresolved; the new sextic has larger measure than P4 and expensive complete companion and cover costs.
The original frozen [L246](../../../ledger/Yin_L_G0246_v1.md#complete-retained-proof-and-review) remains the actual input of the dated R145 finding.

## Executed files, reproduction and finite scope

The discovery cap of25000 proposals was declared before execution.
The subsequent684-pair and228-pair tests were separately declared changed constructions.
[C573 current complete proof](../../../claims/Yin_C_G0573_v1.md#root-basis-neutral-padding-fixed-scope) owns the complete authored proof and precise failure/success scopes.
Five author programs and outputs are retained:

| Program | Actual output | Exact scope |
| --- | --- | --- |
| [search.py](search.py) | search_result.json (`mathematics/computations/outputs/Yin_J_G0053/search_result.json`) | Declared25000-proposal reflection/order search, seed11320261010, energy cap1000, basis-entry cap1000000. Failed prescribed Phi6 P4 target; selected integral basis and all its8 operations retained. |
| [verify.py](verify.py) | verification.json (`mathematics/computations/outputs/Yin_J_G0053/verification.json`) | Exact selected-basis replay, seed square identity, both full polynomials,13 integer points proving the full12-degree cover determinant, all64 binary quadratic vectors, all729 vectors in the short-root cube,114 actual norm-two roots, and complete rational trace-root isolation. |
| [short_replacements.py](short_replacements.py) | short_replacements.json (`mathematics/computations/outputs/Yin_J_G0053/short_replacements.json`) | Separately declared684 pairs:114 retained roots times6 positions in the original basis;444 unimodular replacements; no target. |
| [path_replacements.py](path_replacements.py) | path_replacements.json (`mathematics/computations/outputs/Yin_J_G0053/path_replacements.json`) | Separately declared228 pairs: same roots, two central columns of one explicit path basis;112 unimodular replacements;64 target-mod2 matches; no exact target. |
| [changed_control.py](changed_control.py) | changed_control.json (`mathematics/computations/outputs/Yin_J_G0053/changed_control.json`) | Complete certificate of the selected unpadded irreducible sextic, its actual integer basis and unitriangular matrix, full absolute matrix and12-by-12 cover, rational trace intervals, irreducibility and original power traces2,6,5. |

The programs use Python with SymPy and completed the declared finite calculations.
They use no private input or external numerical root oracle.
The discovery program's floating score and acceptance probability select proposals only.
Every target comparison, basis operation and retained determinant certificate is exact.
The two short-root tests are separately declared changed algebraic tests; they are not an extension of the completed25000-proposal annealing cap or an exhaustive search of all integer bases.

The programs can be reproduced in the following dependency order, writing their regenerable outputs in this J output home:

~~~powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/search.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/short_replacements.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/path_replacements.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/changed_control.py
~~~

The first run executed exactly25000 proposals, accepted4919 moves and rejected6336 proposed states by the declared energy/basis bound.
It selected the saved energy17/height2 basis at proposal9011.
Its non-target polynomial is[1,-3,1,1,1,-3,1], companion[1,-37,-51,-51,-51,-37,1].
The selected operation list, full basis, exact Gram and all polynomial coefficients are retained.
D113 proves that the ENTIRE specified reflection/sign/order orbit has polynomial Phi7 modulo2, regardless of search length, while the prescribed target reduces to Phi3 Phi5.
The proof, not the finite count, supports that operation-class exclusion.

The short-root certificate identifies actual norm-two vectors outside the initial reduced root orbit.
Replacement in a path basis changes the binary component partition from7+1 to3+5 and produces a concrete unpadded control with full polynomial[1,-2,-1,3,-1,-2,1].
The target Phi6 P4 was not obtained.
The displayed new V has rank6, height2 and energy24.
Its complete companion is[1,-38,-61,-69,-61,-38,1], and the actual literal cover has rank12, height2 and energy48.
D113 proves the sextic irreducible Salem configuration and gives every original/absolute/cover Mahler contribution through its three exact trace roots.
Original measure is below log2 but above the old quartic value; companion/original ratio exceeds5, so this is an expensive no-padding control, not a cost optimum.

The exact author verifier is distinct from the independent implementation below.
The failed finite searches are not universal nonexistence results.
Source attribution and the full reflection-orbit/bipartite proofs belong to C573 at its exact retained current scope.

The short-root outputs retain target-mod2 counts0 and64; the changed-control certificate retains exact first three power traces2,6,5.

## Complete independent review and fixed retention

The [original R782 finding](../../../audits/reviews/Yin_R_G0782_v1.md#neutral-padding-complete-independent-review) retains its dated full proof/computation checking arrangement and original frozen L246 input.
The complete current mathematical home is [C573](../../../claims/Yin_C_G0573_v1.md#actual-root-basis-argument), with the earlier [R755 whole SELF](../../../audits/reviews/Yin_R_G0755_v1.md#current-complete-whole-self-finding).

The separately implemented [review_independent.py](review_independent.py), with its actual review_result.json (`mathematics/computations/outputs/Yin_J_G0053/review_result.json`), uses integer Bareiss elimination and polynomial subset determinants over Z[t].
It imports no author module for the independent mathematical checks.
The actual run checked all64 binary quadratic vectors, all729 short vectors and114 roots, all684 original-basis and228 path-basis pairs,444 and112 unimodular replacements,64 changed-partition target-parity matches, every selected matrix and both complete rank12 cover determinants, four full trace-root interval families and the stated irreducibility/cost interfaces.
All these checks passed.

The original25000-proposal annealer was additionally replayed with writes intercepted in memory.
Every retained mathematical output field agreed.
This is a separately recorded same-algorithm reproduction, not the independent determinant or exhaustive candidate verification.
The complete written finding also covers the unbounded reflection-orbit argument and the bipartite integer obstruction, which finite enumeration alone would not prove.
The full review retains the actual checking relationship.

Run the independent checker with:

~~~powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0053/review_independent.py
~~~

Its mathematical inputs are the native J53 programs/data.
The retired D113 is not a mathematical input.
Both finite failed-target scopes, the changed sextic and all complete costs retain the exact limits in C573.
That earlier SELF supplies neither the missing original whole-review relationship declaration nor a new native execution or independent replay.
No unrestricted realization or Lehmer gap follows.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
