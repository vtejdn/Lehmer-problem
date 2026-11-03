---
author: Yin
---

# Exact terminal classification of length-five Salem polynomials

Context: [MS26-U001](../../../audits/literature/MS26/Yin_U001.md#ms26-u001), for [G0001](../../../tasks/Yin_T_G0001_v1.md).
Program authored by assigned AI assess_shortness_route; independently read and checked by the coordinating AI for Yin.

## Question and scope

Check all coprime pairs 1<=k<n, 2<=n<=13 for q=t^(2n)-t^(2n-k)-t^n-t^k+1, using exact rational root counts.
The source audit supplies the separate analytic exclusion of n>13, the correction of the source's lower endpoint from n=4 to n=2, and the proof that the root pattern is equivalent to being a Salem polynomial in this range.
This computation checks only that finite terminal step.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Standard-library Fraction/Sturm enumeration, polynomial gcd grouping, rational root isolation and exact Lehmer factor identification. |
| result.json (`mathematics/computations/outputs/Yin_J_G0001/result.json`) | Every one of the 57 candidate records, all counts and endpoints, 17 accepted pairs and 13 ordered groups. |
| [verify.py](verify.py) | Separate SymPy reconstruction and exact irreducible-factor/root-count check, without importing the main program. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0001/verification.json`) | Independent comparison of all 57 records and all 13 group intervals. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0001/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0001/verify.py
```

The author program uses the standard library; the verifier uses SymPy.
Root isolation uses 80 rational bisections; 45-digit decimal displays do not decide root type, equality, ordering or minima.
No random inputs or heuristic tolerance are used.

Generated data use `mathematics/computations/outputs/Yin_J_G0001/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

## Results and limits

The completed enumeration gives 57 candidates, 17 exact Table 1 pair matches and 13 distinct Salem numbers; the minimum group is (6,5),(7,3).
The exact identity q_(6,5)=Phi_6 p_Lehmer identifies the minimum.
All 57 trace polynomials are square-free, which is checked rather than assumed.
The coordinating AI reproduced both retained programs successfully.
The independent program reconstructs trace polynomials from Chebyshev expressions, factors the actual q polynomials, and checks all counts, exact groups, rational intervals and the minimum without importing main.py.
Every compared record agrees.

The analytic reduction, completeness of the trace criterion, source errata and adoption boundary belong to MS26-U001.
No length-six classification, general reciprocal length-five Mahler minimum, or Lehmer gap is proved by this finite check.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
