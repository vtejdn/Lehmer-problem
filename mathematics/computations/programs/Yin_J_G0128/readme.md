---
author: Yin
---
# Three complete-support projections for the multiplicity-twelve gate

Human author Yin.
The same_trace contributor owns this bounded calculation and its two author implementations.
The fixed C621v2/J126 complete group and all earlier target questions remain unchanged.

## Question and scope

Put phi=X^2+X+1, chi=Xphi^2, M=X^8phi^16 and R=F_2[X]/M.
Let G be the image of every complete primitive odd-order trace polynomial W_n, n>1,n!=5, with arbitrary finite nonnegative multiplicities.
Use the [adopted C621v2 exact image and normal forms](../../../claims/Yin_C_G0621_v2.md#argument), whose native input is the fixed J126 certificate (`mathematics/computations/programs/Yin_J_G0126/inputs/certificate.json`).
No generator, pivot, group closure proof or source-order range is changed.

The complete analytic argument in [C636](../../../claims/Yin_C_G0636_v1.md#argument) forces exactly four complements B=X^10H(chi), H(t)=1+ut+vt^2, for A_0=12.
All four full formal gates are feasible by the displayed CRT construction, including the two genuinely nonsquare B when u=1.
For an ACTUAL original input, H(chi) is respectively1, W_3W_15, its square or W_25, and the complete V_0 factorization therefore makes Y a complete product with nonnegative uniform multiplicities.
The mandatory projection of Y is

    Y=(1+X^4)/H(X)^2 modulo X^8,
    Y=X^14/H(chi)^7 modulo phi^16.

The inverse H(X)^(-2) is taken ONLY modulo X^8, where H(0)=1; for H=phi it is not a phi-primary inverse.
H(chi) is a unit at both components.
The case(u,v)=(0,0) is y^7 for C630's class yG of exact order4, so it is already excluded analytically.
Test ONLY the remaining three prescribed targets, in the order(0,1),(1,0),(1,1), then stop regardless of the results.
There is no extra ratio test, support construction, coefficient search, new modulus or higher-order scan.

## Finite certificate and bounds

Construct each CRT target explicitly from its two displayed components in the forty-dimensional quotient.
Use the fixed order-three factor and37 ordered principal bits of J126.
For each target cancel at most37 strictly increasing pivot positions, retaining a96-coordinate generator exponent vector modulo48 and the residual.
Thus all three targets use at most111 pivot cancellations.
A residual1 is a membership witness; a nonidentity residual whose first bit is absent from the fixed complete pivot list proves nonmembership through the adopted normal-form theorem.
No BFS, insertion queue or new generator calculation is used.

The second implementation reconstructs the same three CRT targets with dense polynomial arithmetic and Euclidean inverses.
It verifies each target equals its full96-generator product times its residual, every ordered cancellation, each used pivot expression and the missing-bit or identity conclusion.
The unchanged source reconstruction and complete group coverage remain the adopted C621v2/J126 inputs.
Both programs are author checks, not independent agent review.

## Files

The retained programs are [main.py](main.py) and [verify.py](verify.py).
The sole required cross-group native input is the fixed J126 certificate (`mathematics/computations/programs/Yin_J_G0126/inputs/certificate.json`).
A missing input stops execution without an automatic replacement run.
The new certificate (`mathematics/computations/outputs/Yin_J_G0128/certificate.json`) retains all three targets, full96-coordinate product expressions, residuals and ordered traces.
The verification result (`mathematics/computations/outputs/Yin_J_G0128/verification.json`) retains the separate dense checks.
No fixed predecessor is edited.

## Reproduction

Run from the repository root in this order:

```text
python mathematics/computations/programs/Yin_J_G0128/main.py
python mathematics/computations/programs/Yin_J_G0128/verify.py
```

Both use Python standard-library exact arithmetic and derive their own output home from the program location.
The elementary arithmetic and fixed-group reduction kernels are copied from the same contributor's J127 implementations; the old files are neither imported nor edited.
The new main program constructs the three CRT targets, and the second program reconstructs each component with dense polynomial arithmetic and Euclidean inversion.

## Results and limits

Both declared native implementations completed.

| u | v | Target | Member | Residual | First missing bit | Cancellations |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 101104001 | no | 34cf799601 | 20 | 5 |
| 1 | 0 | 5000fc005 | yes | 1 | none | 18 |
| 1 | 1 | 15010ec015 | no | b6dbdb6d01 | 36 | 22 |

All displayed polynomials are in hexadecimal coefficient notation.
The total45 cancellations lie within the declared111 bound.
The separate implementation checks all three exact CRT targets and full96-generator product identities, all ordered reductions and28 distinct used pivot expressions.
The positive case has the genuine nonsquare complement B=X^10(1+chi); it was retained without any higher-precision or original-coefficient continuation.
The other three formal complements remain in the analytic classification and formal-gate CRT construction, including the earlier analytically excluded(0,0) case.

No extra ratio test or source/precision expansion was performed.
An analytic comparison after the three tests gives T_(0,1)=T_(1,0)^2/T_(0,0) in the same CRT ring because H_(0,1)=H_(1,0)^2.
With the fixed C630 class yG of order4, this puts T_(0,1) in yG, while T_(0,0) is in y^3G and the positive T_(1,0) is in G.
The T_(1,1) residual equals the fixed C630/J127 residual for y^2, so their full product identities put T_(1,1) in y^2G.
Thus the four targets have four distinct cosets; they cannot all be merged into the old nonmember class by complete-group multiplication.

Membership is only necessary for an original input; it does not establish the complete phi^48 gate, canonical C3/C5 multiplicities, full integer layers, maximal global q or a same-T realization.
A nonmembership conclusion uses the actual all-order reduction and complete Y factorization, not an arbitrary polynomial-degree cutoff.
No A_0=14 or larger quotient test belongs to this group.
The full module/formal-gate theorem, all four distinct cosets and actual original necessary complement are fixed in [C636](../../../claims/Yin_C_G0636_v1.md#decision-initial), initially open for fresh isolated whole mathematical/native review.

## Independent reproduction and adoption

[Independent whole R844](../../../audits/reviews/Yin_R_G0844_v1.md#whole-a12-classification-native-finding) reproduced both author programs and added [reviewer_check.py](reviewer_check.py), using the reviewer's separate exponent-set arithmetic and Euclidean inversion.
Its retained output (`mathematics/computations/outputs/Yin_J_G0128/reviewer_verification.json`) verifies exactly the declared three CRT targets, all full96-factor products, all45 ordered cancellations and28 used pivot expressions.
The fixed J126/J127 inputs were read but not rerun or altered, and the author implementations remain author evidence.
The complete analytic and native result is [adopted in C636](../../../claims/Yin_C_G0636_v1.md#decision-whole-reviewed-2026-10-23).
This adoption retains the positive projection witness without claiming a full original realization or an entire A0=12 exclusion.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0844_v1.md#whole-a12-classification-native-finding) |
| `reviewer_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0844_v1.md#whole-a12-classification-native-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0844_v1.md#whole-a12-classification-native-finding) |
