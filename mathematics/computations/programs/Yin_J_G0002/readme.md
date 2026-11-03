---
author: Yin
---

# Exact algebraic checks for the excess-three Salem family

Context: the explicit q_N=t^(N+3)-t^(N+1)-t^N+1-t^2-t^3 family from [L G0020](../../../claims/Yin_C_G0222_v1.md#sparse-salem-delay-family), and the new [complete family argument](../../../claims/Yin_C_G0248_v1.md).
Programs by assigned AI assess_shortness_route for Yin; the coordinating AI read the complete programs and separately checked the displayed all-parameter arguments.

## Question and scope

Verify the finite polynomial identities used to eliminate every cyclotomic order, the surviving divisibility congruences and repeated-root remainders.
Corroborate the primitive excess-three graph, canonical repair and optimal degree-one repair on explicitly stated finite parameters.
Verify the separating interval in the already checked 13-number Salem classification using rational trace intervals.
All arithmetic is exact; analytic completeness is proved in the linked ledger, not inferred from a finite scan.

## Files

| File | Role |
| --- | --- |
| [eliminate.py](eliminate.py) | Five exact root-of-unity elimination identities, irreducible factors, complete surviving residue tests and square-freeness remainders. |
| elimination.json (`mathematics/computations/outputs/Yin_J_G0002/elimination.json`) | Complete finite identity and remainder output. |
| [check_family.py](check_family.py) | Net-trace checks through index 30 for 4<=N<=390, graph characteristic-polynomial checks at N=2,...,16,22,34, and rational interval separation. |
| family_checks.json (`mathematics/computations/outputs/Yin_J_G0002/family_checks.json`) | All tested family parameters and graph results, with exact separation evidence. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0002/eliminate.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0002/check_family.py
```

Use SymPy.
Inputs are explicit in the programs; `check_family.py` requires the actual J_G0001 result (`mathematics/computations/outputs/Yin_J_G0001/result.json`).
Generate or explicitly obtain that input before running the family check.
There are no random inputs or numerical root tolerances.
The finite net-trace bound is 30; the all-index conclusion uses the separate positivity proof and complete cyclotomic table.

Generated data use `mathematics/computations/outputs/Yin_J_G0002/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

## Results and limits

The coordinator read both programs and successfully reproduced the two retained calculations.
The elimination gives only Phi_2, Phi_8, Phi_12, Phi_18, Phi_30, each at its unique stated congruence and with multiplicity one.
Finite family checks agree with canonical repair t^2-1 exactly for N=10 mod12 and 1 otherwise, and minimum repair Phi_2 or 1 respectively.
Every tested graph has characteristic polynomial q_N, determinant of absolute value 1 and excess three.
Assigned AI review_matrix_completion separately reconstructed the elimination identities, residue tests and rational interval separation; its read-only exact check also passed.

The first scratch elimination attempt had an implementation assertion caused by comparing equal polynomials with different coefficient-domain metadata; exact monic-expression comparison repaired that issue before its output was used.
No claim relies on that failed run.
The retained programs do not prove the Rouché argument, graph classification, all-N congruence reduction or all-index primitive-orbit statement; those are separately written and reviewed in the ledger.
No Lehmer resolution or vanishing-entropy family is claimed.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
