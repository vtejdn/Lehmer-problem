---
author: Yin
---
# Exact denominator-three affine residual screen

## Question and scope

Before execution, 2026-10-20T11:22, entropy_attainment_bridge declares this first finite batch under root's explicit authorization for the [complete denominator-three reduction](record.md#denominator-three-reduction).
The original domain is a totally real field F, nonzero integral a,b,c, s in{1,-1}, 2c^2=3a^5, b^2-a^3+s(c^3-2b^5)=0 and g=c^3-2b^5!=0.
The question is a strict violation of abs(Norm_F(g))>=2^([F:Q]/2) in the32 choices b=(u/3)c+v, u,v in{-2,-1,1,2}.
The complete pre-run analytic reduction in [record.md](record.md#denominator-three-reduction) leaves exactly four sign representatives: (1,2,-1),(-1,2,-1),(2,1,1),(-2,1,1).
It uses accepted C178/C182/C184, the complete original norm tower and a directly retained Rolle bound.
The finite conclusion will concern only this32-case family, not all rational affine pairs or unrestricted residual triples.

Root supplied the denominator3 selection,3-prime split and representative choices.
The author checked and retained the exact reduction, original denominator/integrality reconstruction and native calculation.
Both are contributors; this is not independent review.
The earlier J111 integer-affine experiment has a different domain and supplies no numerical input.
Its exact-polynomial/subprocess workflow is reused operationally, with the new rational b integrality test explicitly added.

## Files

[inputs.json](inputs.json) fixes the complete parameter family, four representatives and limits.
[record.md](record.md#denominator-three-reduction) preserves the complete analytic reduction and exact whole-field reconstruction.
[main.py](main.py) retains the complete rational polynomial, denominator clearing, primitive ZZ factorization, factor-product check and conditional degree5 field checks.
results.json (`mathematics/computations/outputs/Yin_J_G0112/results.json`) retains the actual complete author output; a timeout, failed check or exception would instead leave incomplete.json.
The program resolves Yin_J_G0112 from its own native directory and does not consume earlier outputs.

## Reproduction

From the repository root, with the repository SymPy installation, run:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0112/main.py

All coefficients, factors, Sturm counts, field representatives and norms are exact in ZZ or QQ.
Each case is a separate process capped at15 seconds; the entire declared mathematical pass is capped at60 seconds.
The output budget is64MiB, checked before atomic publication.
A failed mathematical launch is not automatically retried or escalated.
No larger grid, new denominator or numerical root isolation is authorized by these limits.

## Results and limits

The single authorized author pass completed on2026-10-20.
The recorded complete mathematical pass took3.0160000000032596 seconds, within the declared15-second per-case and60-second aggregate limits.
The exact arithmetic backend was SymPy1.14.0.
No retry, escalation or larger parameter family was executed.
Every rational polynomial, cleared integer polynomial, signed content and complete primitive factorization is retained in the actual output.
All four factor-product reconstructions passed exactly.

| (u,v,s) | Clearing denominator | Signed content | Complete primitive factor degrees | Positive leading coefficient |
| --- | --- | --- | --- | --- |
| (1,2,-1) | 3^22 | 1 | 25, multiplicity1 | 32 |
| (-1,2,-1) | 3^22 | -1 | 25, multiplicity1 | 32 |
| (2,1,1) | 3^22 | -1 | 25, multiplicity1 | 2^30 |
| (-2,1,1) | 3^22 | 1 | 25, multiplicity1 | 2^30 |

Each sole primitive irreducible factor is nonmonic, so no computed representative has an algebraic-integer c satisfying its annihilating equation.
This also excludes integral residual triples in the eight sign-equivalent cases.
The other24 original cases were removed only as possible strict norm violations by the analytic reduction; their removal is not a proof that they have no solutions.
Combining those distinct conclusions gives the author result that the stated32-case family contains no strict violation of the original full-field norm threshold.
It does not resolve arbitrary rational affine coefficients or the unrestricted residual singleton.

No monic degree5 factor survived.
Consequently no Sturm count, rational-affine b-integrality test, reconstruction of a, original-equation field check or norm comparison was exercised in this run.
Those conditional branches remain in the declared native program but are not finite evidence established by this negative result.
The separate [independent verifier](verify_independent.py) completed its one declared four-case pass in2.7189999999973224 seconds.
Its complete output (`mathematics/computations/outputs/Yin_J_G0112/verification.json`) reconstructs every b,Q,H coefficient, the minimal clearing denominator, contents, primitive factors and factor products with independently written Python integer arrays, binomial coefficients and Fraction arithmetic.
It also checks the complete32-to8-to4 parameter-label selection; the mathematical validity of those filters is a separate whole-review obligation.
The verifier neither imports nor reruns main.py.
Its irreducibility check uses SymPy1.14.0 Poly.is_irreducible on the four retained factors, so this part shares the author's symbolic engine and is not a second independent backend.
All four irreducibility checks returned true.
The unexercised Sturm, integrality, reconstruction and norm branches remain unexercised in the verifier as well.
To reproduce this separate same-scope verification from the repository root:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0112/verify_independent.py

The completed [whole independent R463](../../../audits/reviews/Yin_R_G0463_v1.md#denominator-three-screen-whole-independent-finding) records PASS for the entire analytic reduction, original norm tower, native reconstruction and precisely bounded negative conclusion.
Its disclosed shared-engine irreducibility boundary is unchanged.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0463_v1.md#denominator-three-screen-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0463_v1.md#denominator-three-screen-whole-independent-finding) |
