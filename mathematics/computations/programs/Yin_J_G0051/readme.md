---
author: Yin
---

# Exact dyadic congruence controls for low-energy reciprocal auxiliaries

Responsible current argument: [C572v2](../../../claims/Yin_C_G0572_v2.md#dyadic-low-energy-fixed-scope).
The original frozen [L233](../../../ledger/Yin_L_G0233_v1.md#complete-retained-proof-and-review) remains the actual input of R132.
Exact finite certificates on the actual quartic, degree-six and original-Lehmer inputs cover mod-two quotient orders and divisions, low-energy congruence representatives and complete integer resultants.
This is not an unrestricted auxiliary search or an asserted near-one coverage theorem.

## Program and exact result

[verify.py](verify.py) and verification.json (`mathematics/computations/outputs/Yin_J_G0051/verification.json`) retain the completed bounded author certificate, checked using Python with SymPy.
The input list contains exactly the three polynomials and three auxiliary choices displayed in D100.
There is no coefficient-box, height or growing-degree search.
The proof of absence of trinomials at every degree for two inputs is D100's symbolic classification, not a computational extrapolation.

The program factors each binary reduction by exact bit-polynomial trial division, verifies product reconstruction and irreducibility of each small factor by all possible monic constant-one divisors through half its degree, and finds its root order by testing all divisors of 2^f-1.
It then checks the complete quotient order h, including repeated factors, by tau^h=1 and tau^(h/p)!=1 for each prime divisor p of h.
It evaluates D100's order criterion and verifies its canonical trinomial when applicable.
The all-exponent theorem itself is not assumed proved by this finite routine.

For each chosen integer F, monic division supplies actual U,V with F=P U+2V and verifies that identity.
The full signed resultant is computed both by SymPy's polynomial resultant routine and by the exact Bareiss determinant of the multiplication-by-F matrix in Z[t]/(P).
The program also computes Norm(V), checks Res(P,F)=2^d Norm(V), and retains the full resultant factorization, degree, content, coefficient norms and rho.
These are two calculations in one author program using the same SymPy integer library, not an independent software implementation or separate review.
Prior fixed proofs supply the actual irreducibility and Salem scope; the program additionally checks rational irreducibility at these inputs.

| Actual input | Complete binary quotient order h | Minimum degree for (P,2), S2<2 | Chosen signed resultant | All original dyadic depths |
| --- | ---: | ---: | ---: | --- |
| Quartic | 5 | 5 | -16 | Exactly1 |
| Degree six | 12 | 8 | 256 | Exactly4/3 |
| Original Lehmer | 31 | 31 | -1024 | Exactly1 |

The rootwise statements in the last column are proved in D100 from the exact divisions, unit half-remainder norms, and the degree-six local multiplicity bound with total norm4 for Phi3.
They are not inferred from a numerical root list or merely by dividing a total valuation by degree.
The JSON additionally records the complete signed period resultants -16,-1280,-1024; the middle value includes its factor5 and is distinct from the chosen trinomial norm256.

## Reproduction

The retained exact binary trial-division routine replaces a `sympy.factor_list(P, modulus=2)` call that failed in the installed FLINT factor-sorting interface before producing a result.
This was an implementation failure, not a failed mathematical assertion.
The current complete result includes Norm(V), the three full orders and unambiguously signed resultants.
From the repository root:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0051/verify.py
```

All assertions passed.
A reviewer can preserve the author JSON by supplying a distinct `--output` path.
This is actual author execution and retained exact evidence, not a separately organized independent check or unrestricted near-one conclusion.

## Separate review of the completed certificate

The coordinating noncontributor reviewer completed the [complete retained review](../../../audits/reviews/Yin_R_G0775_v1.md#dyadic-low-energy-complete-independent-review), including every native file here.
A read-only complete replay intercepted the output write and agreed with every saved JSON field.
A separate one-off calculation used plain integer coefficient arithmetic and rational Gaussian determinant elimination, independently checking the full U,V identities, chosen resultants, half-remainder norms, Phi3 norms and full period norms.
Separate binary arithmetic also rechecked factor reconstruction and orders.
All checks passed.
The latter calculation was actually executed but is not a second retained program artifact; the replay and the separate implementation are not conflated.
The symbolic all-exponent classification and rootwise valuation proofs were fully reviewed in the responsible mathematical material.
These finite certificate checks do not establish unrestricted near-one coverage.

## Fixed retention

The complete current D100 argument is adopted in [C572v2](../../../claims/Yin_C_G0572_v2.md#statement) after the [actual isolated whole finding](../../../audits/reviews/Yin_R_G0775_v1.md#current-v2-whole-finding), with the reduction multiplicity3 and covering power4 distinguished.
The earlier [v1 SELF adoption](../../../claims/Yin_C_G0572_v1.md#decision-complete-current-self-adoption) at 2026-10-22T19:31 and its [withdrawal](../../../claims/Yin_C_G0572_v1.md#decision-withdraw-inaccurate-multiplicity-summary) at 2026-10-22T20:46 retain their actual input and evidence.
The [R753 SELF accounts](../../../audits/reviews/Yin_R_G0753_v1.md#current-complete-whole-self-finding) and [R774 independent negative finding](../../../audits/reviews/Yin_R_G0774_v1.md#reduction-multiplicity-defect) remain separate from the new corrected-version finding.
The original R132 written finding, author replay and different integer implementation remain their actual dated input and distinct checking scopes; the earlier v1 SELF supplied no missing original relationship declaration.
References to D100 identify that retained author argument.
The all-exponent classification has the precise actual-order and strict coefficient-energy scope stated there.
Higher-depth, selected-root, multiprime and larger-energy alternatives and input-uniform near-one coverage remain open.

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
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0775_v1.md#current-v2-whole-finding) |
