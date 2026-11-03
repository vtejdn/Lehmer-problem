---
author: Yin
---
# Exact four-entry rank-seven coefficient identity

<a id="four-entry-symbolic-protocol"></a>
## Question and fixed formal domain

The [changed four-entry family](../../../claims/Yin_C_G0538_v1.md#four-entry-changed-question) releases U_(3,5)=w from J108's fixed value2, in addition to its actual-entry variables x=U_(0,2),y=U_(3,4),z=U_(4,6).
All remaining matrix entries, the unit diagonal, rank7 and full target(t+1)Phi6 P4 remain fixed exactly as in inputs.json.
This J derives the ENTIRE determinant polynomial in Z[t,x,y,z,w], not a finite parameter search or a fitted model.
The variables are actual entries, not displacements.

The author batch expands all5040 signed permutations over the formal integer polynomial ring.
A separately implemented recursive Laplace expansion, memoized by the remaining column subset and using its exact cofactor sign, must give the identical complete polynomial.
Both are author checks and are not described as independent noncontributor review.
The complete ascending coefficients t^0 through t^7, unit endpoints, full reciprocal symmetry and separate variable degree bounds at most2 are retained.
The special substitution w=2 must agree coefficientwise with J108's accepted full three-variable coefficient map.
The first coefficient must also agree with the directly derived trace(U^-1 U^t) expression in the responsible draft.

No integer grid, additional prime, modulus, root approximation, Groebner basis, elimination solver, parameter-height box or enlarged target set is selected.
The resulting exact map will be used for a separately written analytic integer argument; no realization or all-integer exclusion is inferred merely from obtaining the map.
If later mathematics supplies an actual integer target matrix, its full original/absolute/cover cost evidence requires explicit retention before any realization claim.

## Resources and reproduction

Exactly one author symbolic batch has an aggregate30-second wall cap,256MiB worker commit and hard-working-set caps, and32MiB complete output cap including serialization and publication.
The small parent monitor is excluded only from worker memory.
The Windows Job and working-set guard is operational reuse from J108's verifier, with its preservation-inclusive deadline and no unguarded fallback.
A cap or failed assertion makes this batch incomplete, and existing output is never overwritten implicitly.

The implementation uses standard Python exact integers and formal exponent dictionaries.
From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0109/main.py
```

## Current result

The single declared author batch completed in0.156 seconds, within the unchanged30-second/256MiB/32MiB caps.
All5040 formal determinant terms agreed with the separately implemented120-state polynomial Laplace recursion.
The three nontrivial coefficient polynomials contain12,27,32 nonzero monomials, respectively.
Their exact w=2 specialization agrees with the accepted J108 map, and the first coefficient agrees with the directly derived trace formula.
These two algorithms are author cross-checks, not independent noncontributor evidence.
The complete author output (`mathematics/computations/outputs/Yin_J_G0109/author/result.json`) and resource outcome (`mathematics/computations/outputs/Yin_J_G0109/author/execution.json`) are retained.
Peak worker commit was11223040 bytes and peak job commit13328384 bytes.
The angular_envelope_review agent authored both methods and the written reduction; root supplied the broad changed-family question only.
The author execution had no failed batch or second run, and used no parameter scan, prime/modulus test or elimination solver.

The [complete written integer reduction](../../../claims/Yin_C_G0538_v1.md#four-entry-derivative-square-price) uses this exact map to close all integer parameters by two square identities and a complete finite algebra table.
The corrected whole proof excludes this entire four-entry family and is covered by the separate whole review linked below.
On2026-10-18T16:47, the author corrected two final c substitutions exposed by root's first independent comparison, from-1,-4 to3,4 at(-1,2,0,1),(-1,2,0,2).
The [exact correction and complete seven-row recheck](../../../claims/Yin_C_G0538_v1.md#four-entry-final-table-correction) retain the failed-comparison boundary and unchanged full coefficient map.
The independent comparison did fail; its retained evidence and any scoped corrected comparison belong to the reviewer and are separate from the successful author symbolic batch above.
No general rank-seven nonexistence or companion-cost conclusion is implied by this symbolic identity computation.

## Native files

The complete formal inputs are [inputs.json](inputs.json), and the two author determinant methods and guard are in [main.py](main.py).
The prior coefficient specialization is the accepted J108 verifier payload (`mathematics/computations/outputs/Yin_J_G0108/verifier/verification.json`), used only to check the exact w=2 identity.
No J108 mathematical helper is imported.

<a id="independent-four-entry-verification"></a>
## Complete independent verification and corrected whole review

Root's independently written [verifier](verify.py) reconstructs all eight pencil coefficients from81 tensor nodes using integer triangular inversion/Newton identities and exact quadratic tensor interpolation.
It imports no author mathematical helper and preserves the complete unbounded formal identity by the proved separate variable-degree bounds.
The [protocol](verify_protocol.md) additionally declares coefficientwise square identities and all32 mathematically bounded candidate substitutions.

The first independent execution (`mathematics/computations/outputs/Yin_J_G0109/verifier/execution.json`) failed at the final seven-row comparison after0.234 seconds; its source remains in [verify_initial.py](verify_initial.py).
It exposed two incorrect written c values, now3 and4, while the complete symbolic map and range/candidate assertions already passed.
After the author's explicit correction, the same-domain revised batch completed in0.187 seconds with peak worker/job commit11452416/13557760 bytes under the unchanged30-second/256MiB/32MiB caps.
The full corrected payload (`mathematics/computations/outputs/Yin_J_G0109/verifier_revised/result.json`), precomparison arithmetic (`mathematics/computations/outputs/Yin_J_G0109/verifier_revised/comparison_input.json`) and execution outcome (`mathematics/computations/outputs/Yin_J_G0109/verifier_revised/execution.json`) are retained.
All81 full pencils, complete coefficients,32 candidates and seven corrected nonzero final values agree.
The two original errors and both actual execution outcomes are preserved; no result is claimed from the failed batch.

[Whole R424](../../../audits/reviews/Yin_R_G0424_v1.md#four-entry-whole-independent-finding) covers the corrected complete L416 argument, this entire native group, all resource outcomes and actual contributor/shared-runtime limits.
This establishes only the stated four-entry integer exclusion, with no general rank-seven or companion-cost assertion.

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
| `author/result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0737_v1.md#current-g416-complete-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0538_v1.md) |
| `verifier_revised/result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0737_v1.md#current-g416-complete-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0538_v1.md) |
