# Independent full four-variable verification protocol

Root independently implements a complete exact reconstruction of the J109 pencil and checks the finite algebra in the author-ready four-entry proof dated2026-10-18T16:42, now fixed with its explicit correction in [L415](../../../ledger/Yin_L_G0415_v1.md#four-entry-final-table-correction).
Root suggested the changed entry but supplied no new coefficient formula, square identity, range bound or exclusion step.
Root authored upstream J108 and L413; their separate R568/R565 findings are reused, not relabelled as independent upstream review.
The arrangement is nonblind and uses the same Windows host and standard Python exact integers.
No author mathematical helper is imported; only the existing operational Windows resource guard is reused.

## Exact batch

The fixed matrix and actual variable positions are precisely inputs.json.
Each variable occurs in two transposed pencil positions, so the determinant degree in EACH variable is at most2.
Recompute the full pencil at all81 tensor nodes in{0,1,2}^4 using triangular integer inversion, traces of powers of U^-1 U^t and the exact Newton identities.
Invert the four tensor Vandermonde factors with the rational quadratic Lagrange basis; use integer numerator polynomials and the complete denominator16.
This reconstructs every coefficient identically on the unbounded formal domain, rather than fitting or searching a parameter box.
Read the author payload only after all81 pencils and the complete coefficient map have been computed independently.
Compare every coefficient t^0 through t^7, all variables, unit endpoints and reciprocity.

Using that reconstructed polynomial map, independently expand the two square identities and H=7-5a+3b-c coefficientwise over the integers.
Verify the five displayed quadratic z restrictions and all32 square/parity solutions after the author's analytic proof closes the unbounded x range.
Evaluate b and c for exactly those32 candidates and compare the complete seven surviving a=b=-1 tuples and all their nonzero c values.
This is a finite check of the supplied exhaustive algebra, not a new parameter search or an independently discovered size bound.
The reviewer separately checks the large-|x| inequality and all range endpoints in the written whole proof.
No prime, higher modulus, additional target, larger matrix or numerical root calculation is selected.

## Resources and native evidence

One verifier batch has an aggregate30-second wall cap,256MiB worker commit and hard-working-set caps, and32MiB complete output including serialization/publication.
The small parent monitor is outside only the worker-memory budget.
The guard fails closed, keeps all existing author outputs unchanged, and refuses an existing verifier directory.
No mathematical run occurs during source preparation or AST parsing.
Reproduction: `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0109/verify.py`.
All81 full pencils, the complete independently reconstructed coefficient map, exact identity results, all32 candidate coefficients and the seven final survivors belong to `mathematics/computations/outputs/Yin_J_G0109/verifier/result.json`.
The separate execution.json records the actual resource outcome.
A cap, assertion failure or preservation overrun makes the batch incomplete.

## First independent batch and required arithmetic correction

The first declared batch stopped at the final comparison assertion after0.234 seconds, with peak worker commit11870208 bytes and peak job commit13979648 bytes.
Its complete-map, grouped-map, H/square identity, quadratic-range and32-candidate assertions had already passed.
No complete verifier payload was published; the actual failure remains in the original verifier/execution.json and the original source in verify_initial.py.
Direct substitution identified two author-table c values: (-1,2,0,1) gives3, and (-1,2,0,2) gives4, whereas the original table wrote-1 and-4.
The whole conclusion is not adopted from this failed batch.
The author is asked to check and correct the table; the polynomial map and bounded domain remain unchanged.
After that correction, one revised batch may repeat precisely the same mathematics under the same30-second/256MiB/32MiB caps, preserving all initial evidence and publishing to a distinct verifier_revised directory.
It will retain all computed candidates before its final comparison so any future assertion has inspectable arithmetic evidence.

The author has now checked all seven values and frozen the corrected column(-2,3,4,-2,-1,1,1), retaining both original errors in the draft's correction section.
The revised verifier changes only those two expected table values, the distinct output directory and pre-comparison diagnostic preservation; all independent mathematics and resource bounds remain unchanged.

## Actual revised completion

The authorized same-domain revised batch completed in0.187 seconds, peak worker/job commit11452416/13557760 bytes, below all unchanged caps.
All81 full pencils, coefficientwise identities,32 finite candidates and the seven corrected nonzero values agreed.
The initial failed source/status remain unchanged; revised complete evidence is in verifier_revised/result.json, comparison_input.json and execution.json under this J's output directory.
This is nonblind same-runtime independent mathematical reconstruction and whole proof review, not formal verification or an additional parameter search.
