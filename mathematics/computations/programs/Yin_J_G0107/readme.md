---
author: Yin
---
# Two complete rank-seven targets and the modulo-four proper coefficient test

## Question and scope

Under the [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract), test whether the rank-six [L279 coefficient obstruction](../../../ledger/Yin_L_G0279_v1.md#universal-rank-six-coefficient-congruence) persists for the TWO complete rank-seven targets below.
The first is (t+1)Phi6 P4, P4=t^4-t^3-t^2-t+1.
The second is (t+1)P6, P6=t^6-t^5-t^3-t+1, retaining [L210's higher-energy and signature obligations](../../../ledger/Yin_L_G0210_v1.md#rank-seven-integral-energy-obstruction).
[L287](../../../ledger/Yin_L_G0287_v1.md#quartic-core-complete-extension-classification), [L214](../../../ledger/Yin_L_G0214_v1.md#stable-cancellation-fixed-scope) and [J104](../Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) retain their restricted coupling, cancellation and bipartite boundaries.
No arbitrary-integer realization, cover optimization or near-one conclusion follows from modular compatibility.
The later complete two-adic result is [C525](../../../claims/Yin_C_G0525_v1.md#statement), adopted with [R732](../../../audits/reviews/Yin_R_G0732_v1.md#current-c533-v1-complete-independent-finding); it does not supply an integral realization.
This new J owns the changed finite domain; the old J65 and every fixed conclusion remain unchanged.
Root authors this protocol and program.

<a id="rank-seven-mod-four-protocol"></a>
## Complete finite reduction and declared stopping rule

For every integral upper-unitriangular7-by7 U, p_U(t)=det(tU+U^T) is monic reciprocal of degree7, with ascending coefficients[1,a,b,c,c,b,a,1].
The exact target triples are(-1,-1,0) for (t+1)Phi6 P4 and(0,-1,-1) for (t+1)P6.
These are computed by the displayed full products before using them; all coefficients including both middle coefficients are checked in every witness.
Every U modulo4 is uniquely U0+2X, with21 binary strict-upper entries in each matrix and diagonal1.
The three coefficients f=(a,b,c) are integer polynomials in those21 variables.
Their exact first-order congruence is f(U0+2X)=f(U0)+2 Df(U0)X modulo4, since every product of two increments is divisible by4.
Thus all4^21 residue matrices reduce to the2^21 binary bases, their actual coefficient residues and complete3-by21 binary derivative map.
No entry-height, energy, support, cyclicity or basis-orbit assumption enters this reduction.

The author generates coefficient polynomials by all7! signed determinant permutations.
For a permutation, fixed vertices supply(t+1), ascents supply t and each strict-upper variable occurs once or twice.
Its Boolean support gives its value on binary bases; the full subset-sum transform computes all2^21 base coefficient triples modulo4.
Formal differentiation retains exponent multiplicity BEFORE Boolean reduction.
Only exponent-one variables contribute modulo2; exponent-two contributions vanish there.
The initial implementation evaluated derivative polynomials individually on target-parity bases, intending to stop on the first witness.
After its documented wall-time stop, the revised implementation evaluates the SAME formal derivative polynomials on all2^21 bases by packed three-bit XOR subset transforms.
For each column, an exact eight-bit image-set translation updates the full derivative image on every base.
The first solvable base for each target is retained with its full21-bit correction and actual integral U0+2X, while complete derivative maps and all feasible-base counts are also retained.
A concrete witness settles compatibility independently of those aggregate counts.
If no witness occurs, ALL target-parity bases and all derivative images must be checked before reporting a modular obstruction.
Any capped or failed run is incomplete and proves neither outcome.

Every positive witness is checked again by an exact integer determinant method independent of the Boolean table, retaining the ENTIRE actual integer polynomial, not merely its residue.
Its entire negative absolute companion and literal rank14 cover polynomial are also retained, with no deletion of neutral or positive factors.
The modular target is not substituted for that actual integer polynomial.
No Mahler cost is assigned without a separate proved root or norm analysis.
A noncontributor will separately check the protocol and exact witnesses; a negative outcome instead requires a separately reconstructed complete obstruction certificate before adoption.

The author batch has one aggregate300-second wall-time cap,512MiB worker commit/working-set cap and64MiB total output cap, including serialization.
The small parent monitor is excluded from the worker-memory cap and uses the already corrected J106 Windows guard mechanism with unchanged resource semantics.
The independent batch has the same caps.
No modulus8, further target, rank8 or coefficient-box search is selected.
No mathematical run has occurred at creation.

## Files and reproduction

The author [main.py](main.py) implements the declared exact domain and guarded launch.
A separate noncontributor protocol precheck passed without mathematical repair before the first run.
The independent [verify.py](verify.py) and [protocol](verify_protocol.md) are retained in this same J.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0107/main.py
```
The default output uses the containing J identity under mathematics/computations/outputs/.
It requires the repository Python environment and NumPy for exact small-residue array operations, with no floating-point mathematics.
No prior generated mathematical output is needed by the author calculation.

## Results and limits

The initial [implementation](main_initial.py) reached its300-second wall cap with no complete mathematical result.
Its retained failure record (`mathematics/computations/outputs/Yin_J_G0107/initial_timeout.json`) reports peak worker commit524840960 bytes and no completed result.json.
Its internal mathematical stage was not observable and is not inferred.
No compatibility or obstruction follows from that failed attempt.

The revised author implementation is selected for ONE further attempt within the SAME300-second,512MiB and64MiB caps and exact finite target domain.
It replaces repeated Python derivative evaluation by the complete packed XOR transforms proved above and fixes numerical-runtime thread counts to one before importing NumPy.
The first failure's cause is not claimed diagnosed merely from that change.
Stage messages will distinguish runtime import from completion of the actual coefficient maps if the revised attempt also stops.
The complete uncompressed coefficient/derivative/image arrays occupy exactly25 times2^21 bytes, plus small native headers; all output serialization remains charged.
No cap relaxation, mathematical domain expansion or independent verification has occurred at this revision.
That prerequisite was subsequently met by the revised complete author result, followed by the completed independent positive-witness run below.

<a id="rank-seven-mod-four-results"></a>
## Completed positive outcomes and actual limits

The revised author batch completed all2097152 binary coefficient and derivative maps within the original resource caps.
The separately authored verifier completed one positive-witness batch and reconstructed every required selected matrix, polynomial and all42 step-two derivative columns.
The complete native author result (`mathematics/computations/outputs/Yin_J_G0107/author/result.json`), full residue/derivative/image arrays (`mathematics/computations/outputs/Yin_J_G0107/author/tables.npz`) and independent result (`mathematics/computations/outputs/Yin_J_G0107/verifier/verification.json`) are retained.
The author execution (`mathematics/computations/outputs/Yin_J_G0107/author/execution.json`), independent execution (`mathematics/computations/outputs/Yin_J_G0107/verifier/execution.json`) and initial timeout (`mathematics/computations/outputs/Yin_J_G0107/initial_timeout.json`) distinguish their actual outcomes.
The initial300.015-second failure remains incomplete; the revised complete author calculation took1.047 seconds and the independent witness calculation0.1886771 seconds, with unchanged time/memory/output caps.
The revised peak worker commit was130555904 bytes, and the independent peak was13430784 bytes.
The change does not establish which stage or runtime behavior caused the initial failure.

| Complete target | Selected binary mask | Correction mask | Actual integer polynomial, ascending coefficients | Energy | Height |
| --- | --- | --- | --- | --- | --- |
| (t+1)Phi6 P4 | 7092 | 98304 | [1,-1,-5,-8,-8,-5,-1,1] | 16 | 2 |
| (t+1)P6 | 2323 | 64 | [1,0,-5,-9,-9,-5,0,1] | 9 | 2 |

Both actual integer polynomials agree with their COMPLETE target modulo4 and differ from it over Z.
The first complete derivative image is all eight vectors in F2^3; the second is{0,3,5,6} in the declared bit convention.
The full absolute and literal-cover polynomial arrays and every matrix entry remain in both native outputs, with no inferred Mahler cost.
Thus the rank-six modulo-four exclusion does not extend to exclude these TWO rank-seven targets.
No actual integer target realization, optimal rank/cost or unrestricted gap is proved.
In particular the second modular witness's energy9 does not evade L210's exact-target energy bound13: its actual integer polynomial is a different polynomial.

The author aggregate target-parity/compatible-base counts are respectively171375/168750 and197583/179712.
These counts and earliest-mask minimality are not independently reconstructed and are not premises of either compatibility conclusion.
The independent verifier checks the selected native array rows as well as reconstructing their mathematics; it does not turn that selected comparison into an all-array independent certificate.
Shared standard Python integer arithmetic, the same Windows host and nonblind schema/output access are disclosed in [the independent protocol](verify_protocol.md).
There is no formal verification or independently audited NumPy arithmetic runtime.
The actual positive witnesses alone settle the declared feasibility question; no modulus8 or additional target is selected by this completed test.

The native [verify.py](verify.py) reproduction command is:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0107/verify.py
```

It requires this J's complete author result and execution record, and refuses incomplete or negative branches.
The complete [R418 whole independent finding](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) checks this final finite account and all declared evidence boundaries.
Root adopted that reviewed positive scope in S1/S3/S6; the subsequent [L412 analytic two-adic continuation](../../../ledger/Yin_L_G0412_v1.md#two-adic-complete-realization) has its own separate R565 and is not folded into this finite computation.

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
| `author/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) |
| `author/result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) |
| `author/tables.npz` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) |
| `initial_timeout.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) |
| `verifier/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) |
| `verifier/verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0419_v1.md#two-adic-rank-seven-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0732_v1.md#current-c533-v1-complete-independent-finding); [Claim support and recorded result](../../../claims/Yin_C_G0525_v1.md) |
