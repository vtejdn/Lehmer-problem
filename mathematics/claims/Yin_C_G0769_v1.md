---
author: Yin
---

# A low core coefficient explicitly identifies half of the second-four obstructions

Human author Yin.
Root developed the LC1--LC5 candidate and checked its complete saved argument before fixed registration.
The [D1 author development](../drafts/Yin_D_G0001.md#low-core-linear-coefficient-square-test) is provenance only; the necessary argument is retained below.
At author registration, this fixed candidate was OPEN pending independent whole review and separate adoption.
The independent review of C768 does not cover this additional coefficient identification.

## Statement

Fix ANY actual source and EVERY original permitted base parameter s of [adopted C767](Yin_C_G0767_v1.md#decision-whole-reviewed-2026-10-26), and its entire actual height-one target fiber, of size2^(2N-1-t_new).
Retain its full integer trace T, core trace T_K, source factors and multiplicities, A=2m, phi=X^2+X+1 and all original degree/source costs.
Use the actual globally even canonical second residuals X_(epsilon,T), epsilon in{1,-1}, and the normalized local half E_epsilon of [adopted C768](Yin_C_G0768_v1.md#decision-whole-reviewed-2026-10-26), in F_2[X]/phi^(3A).
The coefficient [X]T_K is an even integer.
Define kappa(T)=([X]T_K)/2 modulo2 by integer coefficient division.
For every actual target output and either sign,

    kappa(T)=1 => ord_phi E_epsilon'=2A-2,
    kappa(T)=0 => phi^(2A) divides E_epsilon'.

Consequently every kappa=1 output admits no integer correction T+4W with degW<degT making the selected second residual divisible by4.
For each such output both ORIGINAL canonical second residuals have exact coefficient valuation1.
Its original F remains divisible by4, and the obstruction is to every unrestricted correction in its own coefficient class, not merely the height-one corrections.
Exactly2^(2N-2-t_new) actual target outputs have kappa=1.
This gives an explicitly specified failing half; it does not give the exact total number of failures or prove any kappa=0 output soluble.
The original source, s threshold, degree costs and actual height-one sign family are unchanged.
No whole-fiber exclusion, successful height-one second-four input, new raised-parameter theorem, Mahler upper bound, nearzero family or unrestricted G0001 conclusion is asserted.

## Complete argument

Fix a base C767 target output and write A=2m, T=A_big T_0, T_0=(X^2-4)J_n T_K as in C762.
The ACTUAL coefficient of X in T_K is even because T_Kbar has the full factor X^2.
Define the computable binary coefficient

    kappa(T)=([X]T_K)/2 modulo2.                 (LC1)

This is an integer coefficient half, not division in a binary quotient.
The conclusion under review is that kappa=1 identifies a failing output for BOTH separately chosen second-residual signs and every unrestricted4W correction in its own modulo4 coefficient class.
The case kappa=0 remains undecided by this low-order test.

### Actual low coefficients of the reference difference

Take P_X=X in the factor-lift reference T_base without changing the binary V=(T-T_base)/2 class: replacing X+2c by X in its even exponent A changes T_base by a multiple of4.
Then T_base has the ACTUAL integer factor X^A.
Every coefficient of T below X^A is even, and its coefficientwise half equals the corresponding coefficient of V.
This statement concerns that low truncation only; no global polynomial T/2 is used.

For every k>=1 the trace recurrence proves the INTEGER coefficient congruence

    C_(2^k)(Y)=Y^(2^k)+2 modulo4.

It holds at k=1 by C_2=Y^2-2 and follows at the next step by squaring and subtracting2.
Let S=A-4=Q/2-8, the sum of2^k for3<=k<=ell-2.
Consequently the actual fixed cofactor has

    A_big=C_N^S+2 sum_(k=3)^(ell-2) C_N^(S-2^k)
                                                    modulo4. (LC2)

All displayed exponents are nonnegative and even; terms with two selected factors2 vanish modulo4.
For odd N, C_N is an odd integer polynomial with C_Nbar=X B_N^2, so C_N/X is an even polynomial with odd constant coefficient.

The secondary terms in LC2 contribute to V modulo2 the polynomials C_Nbar^(S-2^k) T_0bar.
They have NO odd coefficients below X^A.
Indeed the first factor is a square; C762 gives T_0bar=X^4Y_1B_N^7phi^(7A)B_n^2, and C759 gives X^(4A)|Y_1' and B_N=1 modulo X^(4A).
Since4A is even, the latter identity also gives X^(4A)|B_N'.
The other displayed factors are squares, so the low truncation of T_0bar is even in X.
No claim that Y_1=1 in that low quotient is needed.

For the leading term C_N^S T_0 in LC2, use the ACTUAL T_0=(X^2-4)J_nT_K.
The -4 term contributes zero to its low coefficient half modulo2.
The remaining term is

    X^(A-2) (C_N/X)^S J_n T_K.

The factor (C_N/X)^S J_n is an even integer polynomial with odd constant coefficient: J_n=1+sum C_(2j) is even and J_nbar(0)=1.
There are no leading-term contributions below degree A-2.
Its coefficient half at degree A-1 is therefore exactly ([X]T_K)/2 modulo2.
Together with the secondary terms this proves

    [X^j]Vbar=0 for odd j<A-1,
    [X^(A-1)]Vbar=kappa(T).                    (LC3)

For an actual decomposition V=Phi^A K_loc+2W_0, put k=K_locbar.
The existence of this decomposition is part of the C767 target.
As phi^A has constant1 and only even powers, its inverse in the low X-series also has only even powers.
Thus LC3 gives the same two conclusions for k.
The local k is different from the reciprocal integer core K and its trace T_K.

### What the normalized derivative detects

The complete local formula used in C768 gives, for either sign and the ACTUAL canonical half,

    E_epsilon = C_0^2 Psi^A k(chi)/k^4 + w_0^2
                                    modulo phi^(2A).     (LC4)

Its first two remaining terms are divisible by phi^(2A), because the paid root k=Z_0 modulo phi^(3A) gives L_epsilon_bar divisible by phi^(5A).
The prefactor C_0^2 Psi^A/k^4 is a square unit and has zero derivative; A is even.
Also chi=Xphi^2 and chi'=phi^2.
By LC3 every odd term of k below X^(A-1) vanishes.
The term kappa X^(A-1) contributes derivative

    kappa X^(A-2) phi^(2A-2).

All later odd powers contribute at order at least2A+2, while even powers have derivative0.
Differentiating an error divisible by phi^(2A) does not lower that order, since2A is even.
Hence

    kappa=1 => ord_phi E_epsilon'=2A-2,
    kappa=0 => phi^(2A) divides E_epsilon'.     (LC5)

The first implication identifies an actual non-square class modulo phi^(3A), so it forbids every degree-bounded4W repair for either sign and gives v_2(X_+)=v_2(X_-)=1.
The second implication leaves the higher derivative coefficients unresolved and does not prove solvability.

For the fixed supported toggle of C768 KP3, delta Vbar=C_totbar S_kappa and S_kappa=X modulo X^2.
Since C_totbar has X-order A-2 and leading coefficient1, this toggle changes precisely the coefficient in LC3 by1.
Thus the fixed-point-free pairing exchanges the two kappa values; exactly half of the target outputs have kappa=1.
The argument identifies those as an explicitly specified failing half; additional kappa=0 members may still fail.
The count of ALL failing members is not claimed exact, and no successful height1 second-four realization, higher precision or unrestricted G0001 conclusion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision low-coefficient-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T07:31 |
| status | open |
| reason | Fix the complete LC1--LC5 author deduction identifying a computable failing half in the actual C767 target fiber. It uses the true low integer coefficients, genuine reference difference and complete local canonical half already established in C768. Separate independent whole review and adoption are required; C768's review is not evidence for this added identification. No conclusion on all kappa=0 outputs, whole-fiber impossibility, successful second-four realization or unrestricted Task completion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete coefficient identification](#statement) | Every actual source and original base s, full C767 target fiber, both signs, integer coefficient kappa, derivative order and divisibility, exact size of the identified failing half and all exclusions. |
| argument | [Complete LC1--LC5 proof](#complete-argument) | Actual coefficient halves, reference independence, dyadic trace congruence, secondary-term parity, low-series division, genuine local normalization, derivative order and supported involution count. |
| dependency | [Adopted actual target family](Yin_C_G0767_v1.md#decision-whole-reviewed-2026-10-26) | Full actual sign fiber/count, common integer factor-lift reference, unsquared target, source-root class and all original degree/source/multiplicity costs. |
| dependency | [Adopted actual canonical half and pairing](Yin_C_G0768_v1.md#decision-whole-reviewed-2026-10-26) | Complete KP1--KP5 local half and square-image test without the global J_H premise, same genuine integer representatives, exact supported toggle and fixed-point-free involution; KP6 actual count. |
| dependency | [Adopted copied core factors](Yin_C_G0762_v1.md#decision-whole-reviewed-2026-10-25) | Exact T=A_big(X^2-4)J_nT_K, A_big dyadic factors, true integer T_K, binary X^2Y_1B_N^7phi^(7A), C_tot X-order A-2 and all parity/degree conventions. |
| dependency | [Adopted source low jets](Yin_C_G0759_v1.md#decision-whole-reviewed-2026-10-25) | Complete preserved source, X^(4A) dividing Y_1 prime derivative and B_N=1 modulo X^(4A), with unchanged paid parameter and source hypotheses. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T07:38 |
| status | proved |
| reason | Root read the entire fixed coefficient argument and complete independent R989 finding and adopts LC1--LC5 at their exact base-source scope without substantive repair. The integer core coefficient kappa identifies exactly half of the actual C767 target outputs as failing every unrestricted coefficient-four repair for either separate sign; their original second residuals have exact coefficient valuation1. The kappa=0 class retains only the shorter derivative divisibility, with no solvability or exact total failure count. All original costs and the unresolved higher-precision, raised, Mahler-upper-bound and unrestricted-Task boundaries remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete coefficient identification](#statement) | Every actual source and original base s, full C767 target fiber, both signs, integer coefficient kappa, derivative order and divisibility, exact size of the identified failing half and all exclusions. |
| argument | [Complete LC1--LC5 proof](#complete-argument) | Actual coefficient halves, reference independence, dyadic trace congruence, secondary-term parity, low-series division, genuine local normalization, derivative order and supported involution count. |
| dependency | [Adopted actual target family](Yin_C_G0767_v1.md#decision-whole-reviewed-2026-10-26) | Full actual sign fiber/count, common integer factor-lift reference, unsquared target, source-root class and all original degree/source/multiplicity costs. |
| dependency | [Adopted actual canonical half and pairing](Yin_C_G0768_v1.md#decision-whole-reviewed-2026-10-26) | Complete KP1--KP5 local half and square-image test without the global J_H premise, same genuine integer representatives, exact supported toggle and fixed-point-free involution; KP6 actual count. |
| dependency | [Adopted copied core factors](Yin_C_G0762_v1.md#decision-whole-reviewed-2026-10-25) | Exact T=A_big(X^2-4)J_nT_K, A_big dyadic factors, true integer T_K, binary X^2Y_1B_N^7phi^(7A), C_tot X-order A-2 and all parity/degree conventions. |
| dependency | [Adopted source low jets](Yin_C_G0759_v1.md#decision-whole-reviewed-2026-10-25) | Complete preserved source, X^(4A) dividing Y_1 prime derivative and B_N=1 modulo X^(4A), with unchanged paid parameter and source hypotheses. |
| review | [Independent whole coefficient finding](../audits/reviews/Yin_R_G0989_v1.md#whole-coefficient-finding) | Entire C769 statement and LC1--LC5 argument, genuine integer halves and low jets, actual local half, derivative order and both signs, exact identified-half count, all four fixed dependency interfaces and stated exclusions. |

