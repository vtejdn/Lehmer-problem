---
author: Yin
---
# Doubled old support and low coefficient control in the unchanged trace construction

Human author Yin.
The [current G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
The [D1 unchanged-root section](../drafts/Yin_D_G0001.md#doubled-support-unchanged-root-control) is development provenance, not a logical input.
This is a complete author argument awaiting fresh isolated whole review.

Original_law identified the need to control the low W coefficient of the actual first-repaired input.
Root proposed stronger-root source variants and their degree margins.
Same_trace observed that taking the sixth power of the ORIGINAL C699 fourth-order root already doubles its error order, and checked the actual sign-dependent half-remainders, unchanged construction stages and source costs below.
Root independently checked the same sixth-power identity and sign simplification.
This uses the adopted C691, C669/C672, C699, C702 and C706 at their exact interfaces.
It does not modify a fixed predecessor or claim that the second residual's remaining low test has been evaluated.
No native computation or new coefficient/support search is used.

## Statement

### OS1: complete inputs and exact conclusions

Let a>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b be monic and prime to Xphi, with Y_b dividing both Y_b(chi) and Y_b(X^3+X).
Set H_b0=X^aY_b, h_b=degH_b0 and C_b0=X^aY_b(chi)Psi^(7a), and assume the STRONG old support

    H_b0^6=C_b0^21 modulo phi^(8a), h_b>=34a.        (OS1)

Choose fixed monic integer lifts of every irreducible of H_b0, with P_X=X, retaining its full multiplicities, and write their product as H_b=X^a mathcal_Y_b.
For any power q of2 with q>=512 put

    A=aq, H_0=H_b0^q, C_0=C_b0^q,
    h=qh_b, d=h+14A, U=H_0phi^(7A),
    Phi=X^2+X+1 over Z, mathcal_H=H_b^q,
    chi_0=X Phi^2, C_b=X^a mathcal_Y_b(chi_0)Phi(chi_0)^(7a),
    C=C_b^q, S=(H_bPhi^(7a))^(q/2),
    J_2=H_b^(q/2), J_3=H_b^(3q/4).                 (OS2)

Execute the ORIGINAL C699 CP2--CP5 construction for each separately chosen sign s in{1,-1}, using its CP6 power choices when their stated q range applies.
In particular its initial k_b is the eleventh root of H_b0C_b0^2 only modulo phi^(4a), with zero low residue modulo H_b0X^(a/2).
Its actual lift K_b is divisible by H_bX^(a/2), and K_0=K_b^q has

    degK_0<h+17A/2<d-2A,
    k_0^11=H_0C_0^2 modulo phi^(4A),
    X^(3A/2)|K_0 over Z.                            (OS3)

NO stronger root, weaker initial factor, altered degree bound or renormalized q is needed.
The stronger consequence is

    k_0^6=C_0^3 modulo phi^(8A).                     (OS4)

Let W_0 be the actual initial C699 modulo4 choice and w_0=W_0bar.
Then its complete sign-dependent residue is

    w_0=phi^A k_0 modulo phi^(3A/2) if s=+1,
    w_0=0 modulo phi^(3A/2) if s=-1.                (OS5)

Let K_*,W_* and T_*=S^2+2Phi^AK_*+4W_* be the ACTUAL final C699 modulo8 output.
Thus F(T_*)=X_s(T_*)=0 coefficientwise modulo8, degK_*<d-2A, degW_*<d, and the exact integer factors J_3 dividing K_* and J_2 dividing W_* are retained.
With k_*=K_*bar and w_*=W_*bar, it also satisfies

    k_*^6=C_0^3 modulo phi^(8A),
    w_*=phi^A k_* modulo phi^(3A/2) if s=+1,
    w_*=0 modulo phi^(3A/2) if s=-1.                (OS6)

The same OS6 statement about W holds after the actual factor-compatible first16 repair of C702, with its SAME K_*.
For q>=8192 choose the derivative-preserving C706 repair and call its output T_dagger=S^2+2Phi^AK_*+4W_dagger.
It has unchanged degree, exact J_2 dividing W_dagger, derivative divisible by16, F=0 modulo16, X_s=0 modulo8, and both residuals modulo16 zero on every H_0-primary.
Its actual second eighth is a GLOBAL square polynomial, and

    ord_phi W_daggerbar>=A,
    W_daggerbar^6 belongs to phi^(6A)F_2[X].         (OS7)

These are actual coefficient-input conclusions, not a computation of the remaining second low error.
The stronger positive-sign equality in OS6 gives exact order A in that case; the negative sign gives order at least3A/2.
The actual canonical residuals throughout are

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3, c_T=rem_T(T(C_5))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).


## Argument

### OS2: sixth-power error doubling in the actual unit quotient

Work in F_2[X]/phi^(8A), where H_0,C_0 and k_0 are units.
The initial root only asserts k_0^11=H_0C_0^2 modulo phi^(4A), so write

    k_0^11/(H_0C_0^2)=1+delta, ord_phi delta>=4A.

In characteristic2 the EXACT binomial identity is

    (1+delta)^6=1+delta^2+delta^4+delta^6.

All nonconstant terms vanish modulo phi^(8A).
The raised old support from OS1 gives H_0^6=C_0^21 at the same precision.
Consequently

    (k_0^6/C_0^3)^11
       =(1+delta)^6 H_0^6/C_0^21=1 modulo phi^(8A).

The unit group has order3*4^(8A-1), coprime to11, so raising to the eleventh power is an automorphism.
This proves OS4 without increasing the original root precision.
More generally any k congruent to k_0 modulo phi^(4A) has k^6=k_0^6 modulo phi^(8A), by the same binomial identity after division by k_0.
This observation will apply to all later K corrections, not only to a hypothetical stronger eleventh root.

### OS3: actual integer halves and the complete initial eta for both signs

All C669/C672 hypotheses hold at the ACTUAL exponent A: Y_b^q is square, both forward divisibilities raise to the q-th power, every full H_0 multiplicity is even, and the old support is stronger than their required4A.
The original C699 K_0 satisfies the full J_H and low coefficient conditions, with degree<d-2A.
Retain the actual integer monic division

    sC^3-K_0^6=Phi^A L_s+2M_s, degM_s<2A,
    D_K=Delta(K_0)bar+k_0^2,
    Delta(K_0)=(K_0(C_2)-K_0^2)/2.                  (OS8)

C672's actual square-of-an-integer-difference argument gives

    M_+bar=0,
    M_-bar=rem_(phi^A)(k_0^6).                     (OS9)

Its hypotheses are literal here: C is an actual integer square and k_0^6=C_0^3 modulo phi^(4A).
In particular OS9 is not inferred by dividing a characteristic-two zero class.
Since K_0 is an actual EVEN q-th power, Delta(K_0)bar=0 and D_K=k_0^2.
The complete C669 error is

    eta_s=[(C_0^3+k_0^6)/phi^(4A)]/(H_0 k_0^3)
           +phi^(2A)(M_sbar/k_0^4+k_0^2)
           +C_0^2Psi^A k_0(chi)/k_0^4
                                  modulo phi^(3A). (OS10)

The first quotient is exact polynomial division before local reduction.
By OS4 its numerator after division has order at least4A, so this whole term is zero at the stated3A precision.
The full-polynomial condition X^(3A/2)|k_0 gives phi^(3A)|k_0(chi), so the composed term is zero as well.
For the positive sign, the remaining term is phi^(2A)k_0^2.
For the negative sign, rem_(phi^A)(k_0^6)+k_0^6 is divisible by phi^A; therefore its middle term is zero modulo phi^(3A).
We have the EXACT two classes

    eta_+=phi^(2A)k_0^2,
    eta_-=0                         modulo phi^(3A). (OS11)

The actual C699 choice satisfies w_0^2=eta_s at this complete precision.
Squaring doubles phi-orders, so OS11 is equivalent to OS5.
Its actual power construction and J_2 factor are unchanged: e_s is the lower q-th root of eta_s, the CRT selects rho=e_s modulo phi^(3a) and rho=0 modulo H_b0, its actual H_b-divisible lift is R_b, and W_0=R_b^(q/2).
This is exactly C699 CP2; the extra old support changes none of its integer half, degree, CRT or all-primary assumptions.

### OS4: propagation through the unchanged corrections

The actual later C699 stages have

    K_1=K_0+Phi^(4A)L_1,
    K_*=K_1+Phi^(4A)L_2,
    W_1=W_0,
    W_2=W_0+Phi^(3A/2)V,
    W_*=W_2+2Z.                                   (OS12)

Their complete actual carry, composition, power, factor and degree proofs already apply literally: neither the initial K lift nor any other choice is replaced here.
In particular k_*=k_0 modulo phi^(4A), so the last assertion of OS2 proves the first line of OS6.
Also w_*=w_0 modulo phi^(3A/2); the final2Z changes no reduction.
Multiplying k_*-k_0 by phi^A still vanishes at this precision.
Thus OS5 propagates to exactly OS6.

C702's first16 repair retains K_* and changes W_* by

    Phi^(4A)M+2Z_1+2Phi^(3A/2)U_1.

Its reduction is w_*+phi^(4A)m, so OS6 persists under that repair as well.
For q>=8192 use the literal C706 power choices at the SAME q, not at q/4.
All of its initial derivative32, fourth-power eighth, actual factorized CRT, derivative16 and global-square conclusions follow at their already adopted scope.
This proves OS7 and the stated first-repaired input without a modified initial-factor theorem.
No derivative preservation after a separately chosen subsequent correction is asserted here.

### OS5: actual C691 supply and every original expense

Take any actual C691 DG1--DG8 source, with its homogeneous exponent Q=2^s, s>=82, m=Q/4-2, complete H_aux, complement B_aux=X^(Q-m)H_aux(chi), and complete global Y_0.
Set a=2m, Y_b=Y_0 and choose the original q>=8192.
C691 DG6 is exactly OS1's support precision because16m=8a.
Both complete forward divisibilities are global and unchanged.
Its representative includes the actual fresh B_n^3 with n>30L, L=4Q.
Thus degY_0>=3(n-1)/2>360m and h_b=2m+degY_0>181a, which pays the34a margin with no new support factor.

Every polynomial degree, integer layer and source component stays at C691's original scale:

    A=2mq, d=q(30m+degY_0),
    w_can=q(26m+degY_0+degB_aux),
    d-w_can=q(m-8-5degH_aux)>5qm/256,
    d<=q(14400Q^3+1206Q^2+128Q),
    actual integer layers a_0=12mq, a_j=0 for j>=1. (OS13)

The chosen q is the ORIGINAL actual maximal Frobenius power of U_0^q and its characteristic-two canonical R_0^q, justified by C691's shared exact fresh triple factor.
The full reduction U and its canonical characteristic-two remainder stay unchanged under the coefficient corrections; the complete synthetic integer factors and zero-Haar layer data retain their original separate status.
The synthetic integer G_int is still not identified with the actual canonical integer G_can.
There is no passage to q/4, enlarged degree, altered original multiplicity or omitted higher-five component in this source application.

The result supplies a literal C706 first-repaired input with known low W residue for every selected original q>=8192 in this source family.
It does not itself compute or clear the second eighth-error below phi^(4A), prove simultaneous residuals modulo16, or realize the characteristic-zero original Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:11 |
| status | open |
| reason | Register the exact stronger-support transmission in the unchanged coefficient construction: the original fourth-order eleventh root already yields eighth-order sixth-power compatibility; the actual C669/C672 halves give explicit eta for each sign and low W control through C699, C702 and C706. Actual C691 sources supply every hypothesis at original q>=8192 with all degrees, maximal q, full components and integer layers paid. No modified initial factor, renormalization, second-error evaluation or full modulo16 conclusion is asserted. Fresh independent whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unchanged-root source theorem](#statement) | OS1--OS7, complete normalized and actual hypotheses, original construction and q range, exact sign residues, final derivative-preserving input and limits. |
| argument | [Complete source and propagation proof](#argument) | OS8--OS13 and OS2--OS5, exact sixth-power binomial and unit automorphism, legitimate integer half-remainders, complete eta, unchanged actual correction sequence and full C691 costs. |
| dependency | [Actual same-coefficient modulo4 error](Yin_C_G0669_v1.md#statement) | S5--S8 complete actual integer division, changing-divisor eta and all-primary square-image iff, used at the original A. |
| dependency | [Actual square-input half-remainders](Yin_C_G0672_v1.md#argument) | Section2 integer difference-square proof of M_+bar=0 and M_-bar=rem_phiA(k^6); all hypotheses are matched directly, not inferred from characteristic-two division. |
| dependency | [Unchanged actual coefficient construction](Yin_C_G0699_v1.md#argument) | Original CP2--CP5 with its full H_b initial factor, actual powers, all carry/composition/factor/degree proofs and final correction sequence; CP6 choices used only in their stated range. |
| dependency | [Earlier-bit actual first repair](Yin_C_G0702_v1.md#statement) | Factor-compatible first16/second8 construction with SAME K and explicit W change; no derivative property is silently assigned to arbitrary later moves. |
| dependency | [Adopted derivative-preserving repair](Yin_C_G0706_v1.md#statement) | Literal original q>=8192 construction, same degree/K/factors, derivative16, global-square second eighth and retained low-W congruence; no passing second-low test inferred. |
| dependency | [Actual doubled-support source family](Yin_C_G0691_v1.md#statement) | DG1--DG8 and Sections4--6, old precision16m=8a, full global representative and fresh factor, original maximal q, canonical characteristic-two identity, every integer layer and degree/gap bound. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:22 |
| status | proved |
| reason | Adopt the complete unchanged-root source theorem after main reading of C707 and fresh isolated whole R928, including its truthful review arrangement and separate source-cost inspection. The exact sixth-power identity doubles the original fourth-order root error, actual integer halves determine both signs of eta, and unchanged C699/C702/C706 corrections preserve the low W residue and original q. C691 supplies all hypotheses with every full factor, actual maximal q, layer and degree/gap expense retained. No second-low residual value, simultaneous modulo16 solution or original realization is inferred by this source theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unchanged-root source theorem](#statement) | OS1--OS7, complete normalized and actual hypotheses, original construction and q range, exact sign residues, final derivative-preserving input and limits. |
| argument | [Complete source and propagation proof](#argument) | OS8--OS13 and OS2--OS5, exact sixth-power binomial and unit automorphism, legitimate integer half-remainders, complete eta, unchanged actual correction sequence and full C691 costs. |
| dependency | [Actual same-coefficient modulo4 error](Yin_C_G0669_v1.md#statement) | S5--S8 complete actual integer division, changing-divisor eta and all-primary square-image iff, used at the original A. |
| dependency | [Actual square-input half-remainders](Yin_C_G0672_v1.md#argument) | Section2 integer difference-square proof of M_+bar=0 and M_-bar=rem_phiA(k^6); all hypotheses are matched directly, not inferred from characteristic-two division. |
| dependency | [Unchanged actual coefficient construction](Yin_C_G0699_v1.md#argument) | Original CP2--CP5 with its full H_b initial factor, actual powers, all carry/composition/factor/degree proofs and final correction sequence; CP6 choices used only in their stated range. |
| dependency | [Earlier-bit actual first repair](Yin_C_G0702_v1.md#statement) | Factor-compatible first16/second8 construction with SAME K and explicit W change; no derivative property is silently assigned to arbitrary later moves. |
| dependency | [Adopted derivative-preserving repair](Yin_C_G0706_v1.md#statement) | Literal original q>=8192 construction, same degree/K/factors, derivative16, global-square second eighth and retained low-W congruence; no passing second-low test inferred. |
| dependency | [Actual doubled-support source family](Yin_C_G0691_v1.md#statement) | DG1--DG8 and Sections4--6, old precision16m=8a, full global representative and fresh factor, original maximal q, canonical characteristic-two identity, every integer layer and degree/gap bound. |
| review | [Fresh independent whole unchanged-root finding](../audits/reviews/Yin_R_G0928_v1.md#whole-proof-finding) | Entire OS1--OS13 statement and proof, actual finite precision and sign halves, unchanged source/correction interfaces, complete original costs and accepted-input depth; later dependency-status exposure and separate source review are disclosed exactly. |

