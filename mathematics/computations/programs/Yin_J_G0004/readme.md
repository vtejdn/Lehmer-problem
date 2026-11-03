---
author: Yin
---

# Exact interior-threshold test for the degree-22 reciprocal control

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md), [HS16-U001](../../../audits/literature/HS16/Yin_U001.md#hs16-u001), the [input proof](../../../claims/Yin_C_G0249_v1.md#degree22-small-core-counterexample), and the [threshold-control proof](../../../claims/Yin_C_G0258_v1.md#degree22-interior-threshold-control).
The coordinating AI prepared the original certificate for Yin; assigned synthesis author AI ms25_source supplied the separate verifier and checked the root-location inference.
Their actual target-author/contributor inspections are recorded at [R528](../../../audits/reviews/Yin_R_G0528_v1.md#original-threshold-contributor-finding), separately from the computational methods.

## Question and scope

For the single fixed polynomial q=t^24-t^17-t^12-t^7+1=Phi_6*p22, test the sufficient interior condition M(p22)^3<=2.
The decisive calculation uses exact rational complex arithmetic, a complete 24th-degree Taylor expansion on one specified rational disk, a rational positive-root test and a rational cubed lower bound.
No infinite parameter scan is involved.

The earlier numerical probe suggested failure of the condition and supplied a disk center.
It is retained as exploratory evidence only: 35-digit SymPy roots, maxsteps=300, a floating-point modulus filter greater than 1.000001 and 30-digit displays have no certified rounding error.
The exact scripts are independent of its output.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Standard-library Gaussian-rational Taylor coefficients, Rouche bound and Mahler lower bound; writes result.json. |
| result.json (`mathematics/computations/outputs/Yin_J_G0004/result.json`) | All 25 complex Taylor coefficients, exact norm bounds, disk, positive-root evaluation and cubed Mahler lower bound. |
| [verify.py](verify.py) | Independent SymPy polynomial shift over Gaussian rationals, without importing main.py; checks retained mathematical values and short rational brackets. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0004/verification.json`) | Exact agreement, factorization and disk checks, compact strict brackets and the interpretation boundary. |
| [probe.py](probe.py) | Preserved exploratory root calculation, with stable input/output locations and structured output. |
| probe.json (`mathematics/computations/outputs/Yin_J_G0004/probe.json`) | Numerical observation only, including precision, filter and approximate Mahler value. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0004/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0004/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0004/probe.py
```

The author program uses the standard library; the verifier and exploratory probe use SymPy.
The probe requires the actual J_G0003 result (`mathematics/computations/outputs/Yin_J_G0003/result.json`); the exact author and verifier specify q directly.
Generate or explicitly obtain that input before the optional probe.
The coordinator ran all three retained programs successfully.
The exact arithmetic, numerical root algorithm and filter keep the distinct scopes stated here; no random seed or external numerical input is needed.

Generated data use `mathematics/computations/outputs/Yin_J_G0004/`, independently of the caller's working directory.
The actual files linked above are retained locally and excluded from Git.
A fresh clone can lack them; verification requires the declared data and does not silently execute a producer.
Programs and mathematical accounts remain at the program home with the same J identity.
These are present reproduction instructions, not a new run or review.

## Results and limits

The retained exact runs passed and agreed on all 25 Taylor coefficients and every compared arithmetic quantity.
They give a root in the disk centered at (-94095-52062i)/100000 with radius 1/100000, because the non-linear-plus-constant bound is less than 19/100000 while the linear boundary term exceeds 31/100000.
The conjugate disk gives a distinct expanding root.
Together with the unique positive root greater than 2727/2500, their three Mahler factors give M(p22)>31535105874939/25000000000000, whose cube exceeds two.
The complete analytic reduction is retained in [C258](../../../claims/Yin_C_G0258_v1.md#argument), with the unique positive-root and full exact input proof in [C249](../../../claims/Yin_C_G0249_v1.md#degree22-small-core-counterexample).
The coordinator read both complete exact programs and the final proof, while the separate assigned agent's review covered the exact arithmetic and its Rouche/Mahler inference; these reviews are distinct from merely observing zero exits.

The retained numerical probe suggests M(p22) approximately 1.2615262661, above 2^(1/3) approximately 1.2599210499.
These decimal observations do not establish the strict inequality.
The exact certificate establishes failure of this theorem's sufficient determinant condition only; it does not prove empty interior, zero volume, any weighted-entropy conclusion or a Lehmer gap.
The source theorem and its connectedness dependencies retain their separate audit scope.
No human or formal verification is claimed.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
