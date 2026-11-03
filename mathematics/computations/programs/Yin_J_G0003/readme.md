---
author: Yin
---

# Exact certificate for nonminimal canonical net-trace repair

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md), [L G0034's finite repair](../../../claims/Yin_C_G0240_v1.md#finite-nettrace-repair), and the [minimum-repair proof](../../../claims/Yin_C_G0249_v1.md).
Both programs were prepared by assigned AI ms25_source for Yin.
The coordinator read both complete programs, checked the supporting proof and reran both retained commands below.
The alternative arithmetic implementation is separate from the recorded independent proof review.

## Question and scope

Check the finite exact arithmetic supporting the example

    q=t^24-t^17-t^12-t^7+1=Phi_6 p,

where p is the degree-22 irreducible reciprocal polynomial specified in result.json.
The responsible proof shows that the canonical cycle repair of p has degree seven while the unique minimum-degree cyclotomic repair Phi_6 has degree two, within the small reciprocal, all-power-degree-preserving Perron class.
This is a counterexample to minimum-degree optimality of that repair procedure, not to Lehmer's conjecture.

The fixed input consists of this one polynomial, its trace polynomial Q defined by p(t)=t^11 Q(t+t^(-1)), eight rational trace intervals, and the bound endpoint t=12/11.
All calculations use exact integers, rationals or GF(2); there are no floating-point root estimates, tolerances, random inputs or unbounded parameter scans.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Standard-library polynomial arithmetic, mod-2 squaring certificate, rational endpoint evaluations, first six normalized net traces, and completion coefficient/length checks. Writes result.json in the J output home. |
| result.json (`mathematics/computations/outputs/Yin_J_G0003/result.json`) | Full coefficient arrays, finite-field remainder chain, all eight rational interval endpoint values, bound evaluation, first six normalized net traces and both completion lengths. |
| [verify.py](verify.py) | Separate SymPy reconstruction without importing main.py; checks the retained arithmetic payload and independently computes a complete rational Sturm certificate. Reads result.json and writes verification.json in the J output home. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0003/verification.json`) | Comparison of 16 mathematical payload fields, symbolic irreducibility checks, the full positively rescaled primitive integer Sturm sequence, exact endpoint values/signs/variations and real-root counts. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0003/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0003/verify.py
```

The author program uses the standard library; the verifier uses SymPy.
Both resolve their output home from the actual repository/J location.
Verification requires `result.json` and compares its 16 mathematical payload fields and exact Sturm data, not execution metadata or prose.
No command-line input or precision setting is required for this fixed instance.
The coordinator reproduced both retained programs successfully; that arithmetic check remains distinct from independent review of the supporting proof.

Generated data use `mathematics/computations/outputs/Yin_J_G0003/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

## Results and limits

The main certificate and separate SymPy implementation agree on all 16 compared payload fields.
SymPy additionally reports Q irreducible over GF(2) and over Q, and p irreducible over Q.
Reconstruction by Chebyshev polynomials yields the displayed trace polynomial without importing the main program's recurrence or coefficient list.
A reciprocal-polynomial logarithmic derivative independently produces the normalized trace tuple

    (b_1(p)...,b_6(p))=(-1,1,1,0,0,-1).

The canonical factor has degree seven and its completion has degree 29 and coefficient length 20.
Phi_6 has degree two and its completion q has degree 24 and coefficient length five.
The full bound evaluation and all eight strict sign changes agree exactly.

The extended verifier retains a Sturm sequence with every member multiplied by a positive rational to make it a primitive integer polynomial.
Its variation counts at (-infinity,-2,2,+infinity) are (10,10,2,1).
Thus Q has exactly eight real roots in (-2,2), exactly nine real roots in total, one real root above 2 and none below -2.
Neither endpoint is a root.
These results agree with separate calls to SymPy's count_roots.
Since Q has degree 11, precisely two trace roots are nonreal.
Under the separately justified trace-to-reciprocal-root correspondence, this gives exactly three expanding conjugates of p without using the Salem classification in MS26/L G0036.

The computation certifies this finite instance and the displayed arithmetic.
All-order net-trace positivity uses the explicit positive primitive graph in the responsible proof.
Minimum degree among every cyclotomic repair, all-power field degree preservation, the strict Mahler bound and the interpretation of the Sturm count use that proof's arithmetic, graph, field and root-pattern arguments.
The finite program does not enumerate all repairs or infer those all-order statements from b_1,...,b_6.
Independent proof review of the integer-program and example logic was reported by the coordinator; that review is separate from these executed arithmetic checks, and this README does not create another proof assessment.
No uniform entropy lower bound or Lehmer gap is established.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
