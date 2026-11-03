---
author: Yin
---

# Exact checks for the essential cyclotomic-block family

Context: G0001 and the family in [L G0048](../../../claims/Yin_C_G0269_v1.md#unbounded-essential-block-family).
The finite exclusion and its relation to the analytic limit are recorded in [L G0050](../../../claims/Yin_C_G0271_v1.md#essential-family-measure-obstruction).

## Question and scope

For exactly g=3,4,5,8,16,32, form

    S_6(x)=1-x+x^2-x^3+x^4-x^5+x^6,
    r_g(t)=S_6(t^g)-t^(2g+1)-t^(4g-1),
    q_g(t)=(t^g+1)r_g(t).

Determine the exact factorization returned over ZZ, identify its cyclotomic factors, retain exploratory root data, and test whether a coefficient certificate proves Mahler measure above 4/3.
The script accepts only these six parameters.
It makes no claim for other g, and no transfer of repair bounds to a selected irreducible factor.
A separate small rational program checks the arithmetic in two analytic lower-integral certificates for the limiting two-variable polynomial.
Their interval coverage and specialization hypotheses belong to the complete argument in L G0050.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact ZZ factorization and reconstruction, cyclotomic identification, numerical root probes, and exact Graeffe coefficient certificates. |
| result.json (`mathematics/computations/outputs/Yin_J_G0006/result.json`) | Every tested polynomial and factor, full numerical probes, all final certificate coefficients and integer inequalities, and earlier iteration outcomes. |
| [verify.py](verify.py) | Independent integer Newton trace recurrence, cyclotomic trace subtraction and coefficient reconstruction; imports neither the author program nor SymPy. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0006/verification.json`) | Exact product, full final coefficient arrays and strict-inequality comparisons; no numerical or irreducibility certification. |
| [limit/verify.py](limit/verify.py) and limit/result.json (`mathematics/computations/outputs/Yin_J_G0006/limit/result.json`) | Exact rational comparisons for the four-interval radical proof and separate five-interval Taylor proof of the limiting M>4/3; no numerical quadrature. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0006/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0006/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0006/limit/verify.py
```

The author program uses SymPy and NumPy; both verification programs use only the standard library.
All six allowed g values are the default; `--g` may explicitly select a subset.
Each completed parameter result is retained in the same output file, preserving other completed parameter scopes.
This is mathematical partial coverage, not a mandatory execution archive or a claim that uncomputed parameters completed.
The coordinator's separate Newton verifier passed 83 checks on ten final coefficient certificates.
The limit verifier reproduced both positive rational comparison margins; its analytic coverage and source boundary remain in L_G0050.

Generated data use `mathematics/computations/outputs/Yin_J_G0006/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

NumPy's companion-matrix root algorithm uses float64 coefficients and complex128 outputs, with a 53-bit significand.
The exploratory expanding root count uses the condition abs(root)>1+10^-7; roots with modulus within 10^-7 of one are placed in a separate near-unit count.
The reported numerical Mahler estimate multiplies max(1,abs(root)) for every root and is not a validated enclosure.
Normalized polynomial residuals are saved as diagnostics, not as root-count certificates.
There is no random input or seed.

The lower certificates use exact integer arithmetic.
Write P(t)=E(t^2)+t O(t^2) and define its monic Graeffe transform by

    G(P)(t)=(-1)^(deg P) [E(t)^2-t O(t)^2].

Its roots are the squares of the roots of P.
Consequently M(G^s(P))=M(P)^(2^s).
For a monic degree-d polynomial, its coefficient of t^k has absolute value at most binomial(d,k) times its Mahler measure: each product in the elementary symmetric sum has modulus at most the product of max(1,abs(root)) over all roots.
Therefore a retained coefficient A=abs([t^k]G^s(P)) satisfying

    A*3^(2^s)>binomial(d,k)*4^(2^s)

proves M(P)>4/3.
The coefficient arrays are in ascending exponent order; large integers are decimal strings in JSON.
Every final array, chosen index, binomial factor, and the two comparison integers is retained.
This inference needs no numerical root accuracy.

## Results and limits

All six retained parameter cases produced a strict lower certificate above 4/3 for the single noncyclotomic factor returned in each case.
The exact factorization product was checked against r_g.
The factorization column below reports the output of SymPy's exact ZZ `factor_list`; irreducibility is a library result, with no separate finite-field or proof-assistant certificate supplied by this computation.

| g | Exact factorization pattern | Exploratory M(r_g) | Exploratory expanding count | Noncyclotomic certificate (degree d, iteration s, index k) |
| --- | --- | ---: | ---: | --- |
| 3 | Phi_12 times degree-14 factor | 1.411156411855 | 3 | (14,7,3) |
| 4 | Degree-24 irreducible output | 1.464959241291 | 7 | (24,7,12) |
| 5 | Phi_6 times degree-28 factor | 1.342930187562 | 5 | (28,11,5) |
| 8 | Phi_6 times degree-46 factor | 1.421791518021 | 11 | (46,9,12) |
| 16 | Degree-96 irreducible output | 1.395851154097 | 21 | (96,11,24) |
| 32 | Phi_6 times degree-190 factor | 1.387995891735 | 41 | (190,12,49) |

All factors have multiplicity one.
Since x^3-x-1 is increasing for x>=1 and its value at 4/3 is 1/27>0, its positive root theta_0 satisfies theta_0<4/3.
Thus the retained strict coefficient inequalities exclude these six whole r_g, and their displayed noncyclotomic factors, from the range M<theta_0.
This Mahler exclusion does not depend on independently proving those factors irreducible.

The whole-polynomial root residual diagnostics range from about 3.7*10^-15 to 3.5*10^-13.
They neither prove the exploratory root counts nor certify unit-circle membership.
This finite evidence does not establish a uniform or asymptotic Mahler bound, an irreducibility pattern for all g, or a new all-parameter repair theorem.
No numerical observation substitutes for the exact lower certificates.

The authoring AI checked the formulas, all product identities and the coefficient-bound implication.
The coordinator read the complete author program and wrote a separate verifier using sparse integer Newton recurrences on the original r_g, in a rolling buffer.
It subtracts the explicitly identified Phi_6 or Phi_12 power sums, samples every 2^s-th power, and reconstructs the entire final squared-root polynomial by Newton identities.
This independently checks the final arrays and exact inequalities without reusing the Graeffe recurrence or numerical roots.
The earlier iteration probes are retained diagnostics, not separately certified first-success claims.
A separate exact integer comparison also checks the rational product used in L G0050's four-interval analytic limit bound; the complete analytic argument and its accepted Lawton input remain in that ledger.

The complete current all-offset analytic proof is [C271](../../../claims/Yin_C_G0271_v1.md#argument).
At 2026-10-21T06:39 the constructor actually reran the retained limit verifier body read-only in memory, suppressing only its final native write; all four radical and five Taylor margins/products passed with the original limit result bytes unchanged.
This separate current self-check is recorded in [R532](../../../audits/reviews/Yin_R_G0532_v1.md#current-complete-uniform-measure-finding); the main producer,83-check finite verifier and finite-g scan were not rerun.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
