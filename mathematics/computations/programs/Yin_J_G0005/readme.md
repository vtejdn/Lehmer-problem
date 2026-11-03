---
author: Yin
---

# Cyclotomic residue tables and the sharp degree-34 repair control

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md), the [relative-order argument](../../../claims/Yin_C_G0262_v2.md#minimal-vanishing-order), and the [full-family proof](../../../claims/Yin_C_G0263_v1.md).
Assigned AI ms25_source prepared main.py for Yin; assess_shortness_route independently prepared verify.py without importing it.
The coordinator read both complete programs and the supporting mathematical mechanisms.

## Question and scope

The finite residue calculations test 0<=n,a<m, gcd(n,a,m)=1, at m in {1,2,3,4,5,6,10,12}.
The proof of completeness for all possible orders is a separate vanishing-sum argument in L G0045, not an extrapolation from this list.

The single sharp control has n=21,k=13,a=8 and q=t^42-t^29-t^21-t^13+1.
Its cyclotomic quotient p=q/(Phi_10 Phi_12) has degree 34.
Exact computations check its trace polynomial, finite-field irreducibility, a real trace interval, graph characteristic polynomial and girth, normalized traces and a rigorous Mahler upper bound.
No variable-degree or unbounded numerical search is claimed.

All decisive calculations use integers, rational numbers or finite fields.
The separate numerical orientation uses SymPy nroots with 35 digits, maxsteps=250, a modulus threshold 1+10^(-20), and a 30-digit Mahler display.
It has no certified root enclosures.
The bounded exact Graeffe search tests iterations 0 through at most 12, and succeeds at iteration 9.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Residue reductions, the degree-34 control, trace and GF(3) data, graph characteristic polynomial, numerical orientation and exact even/odd Graeffe iterations. |
| result.json (`mathematics/computations/outputs/Yin_J_G0005/result.json`) | Every residue pair, polynomial coefficient vectors, all GF(3) Frobenius remainder codes, rational trace evaluations, auxiliary root counts, graph/repair data, every attempted squared coefficient norm and the successful iterate coefficients; numerical probe explicitly separate. |
| [verify.py](verify.py) | Independent integer quotient rings, reciprocal trace basis, custom finite-field Frobenius/gcd, rational Sturm calculation, graph walks/Newton reconstruction, normalized traces and resultant root squaring. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0005/verification.json`) | Named mathematical comparisons, independent graph and irreducibility checks, all-index repair interpretation and the exact norm certificate. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0005/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0005/verify.py
```

Use SymPy, without command-line parameters or random inputs.
The coordinator executed both retained programs; the separately authored verifier passed all 44 mathematical checks.
It compares values, not execution metadata, and does not certify the exploratory numerical root probe.

Generated data use `mathematics/computations/outputs/Yin_J_G0005/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

## Results and limits

The independent retained calculation agrees on every displayed residue table, polynomial coefficient, GF(3) remainder code, rational trace value and retained Graeffe iterate.
The trace polynomial has degree 17 and is irreducible modulo 3; its sign change between 1/2 and 5/8 gives a real embedding where y^2-4 is negative.
The written quadratic-lift argument therefore proves p irreducible of degree 34.
Graph walks reconstruct q exactly, with 42 vertices, 44 edges, period one and girth 13.
The graph and cyclotomic correction imply exactly b_1(p)=b_10(p)=b_12(p)=-1 as the negative normalized traces at all indices, giving canonical degree 23.
Phi_10 Phi_12 repairs with degree eight, and the written divisor/totient argument proves this minimum; the program does not enumerate every possible repair.

After nine root-squaring operations, the exact squared coefficient norm N satisfies N*10^1024<13^1024.
The Jensen-Parseval inequality M(G)^2<=sum|coeff(G)|^2 and M(G^9(p))=M(p)^512 prove M(p)<13/10.
The independent verifier obtains the same final coefficients through resultants, not the original even/odd recurrence.
Its numerical probe value, approximately 1.2947532193, is not needed for this strict inequality.
Auxiliary trace-root counts are exact but not needed for the irreducibility or Mahler certificate.

The full-family order classification, cyclotomic multiplicities, Perron/all-power implications and interpretation of minimum repair remain mathematical arguments in L G0045.
This one control proves sharpness of its repair bounds in the specified small reciprocal class; it does not establish a Lehmer gap or a sequence of positive measures tending to one.
No human or formal verification is claimed.

The complete current mathematical proof is [C263](../../../claims/Yin_C_G0263_v1.md#argument).
At 2026-10-21T06:39 the constructor actually reran the complete retained verifier body read-only in memory, suppressing only its final native write; all44 comparisons passed and original result/verification bytes remained unchanged.
That current self-check is recorded in [R532](../../../audits/reviews/Yin_R_G0532_v1.md#current-complete-length-five-finding), with no producer or numerical-probe execution.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
