---
author: Yin
---
# Actual failure of the two-term high-power trace-remainder model

Human author Yin.
The [active G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed the actual two-term dyadic identity and its use with the doubled-support C691 family.
Same_trace verified that identity, constructed the entire bounded strong-root coefficient input, and derived the complete first-quarter obstruction and both modulo4 sign conditions below.
This is author mathematics, not independent review.
Focused reuse read the adopted C691 full family, C686 actual multi-correction scope, C689 whole next-layer criterion and the exact C603/C669/C672 integer-half interfaces.
No native computation, coefficient enumeration or external source theorem is used.
The content is a rigorous failure of a proposed simplification, not a claim that the full modulo16 problem or the original Task is impossible.

The [D1 two-term section](../drafts/Yin_D_G0001.md#two-term-high-power-dyadic-remainder) is development provenance, not a logical premise.
This entire theorem is initially open for fresh isolated whole review.

## Statement

### TT1: complete normalized input and precise obstruction

Let a>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b be monic and prime to Xphi, with EVERY occurring irreducible multiplicity at least2, and assume Y_b|Y_b(chi) and Y_b|Y_b(X^3+X).
Set

    H_b0=X^a Y_b, h_b=degH_b0,
    C_b0=X^a Y_b(chi)Psi^(7a),
    H_b0^6=C_b0^21 modulo phi^(8a), h_b>=17a.          (TT1)

The last two relations are hypotheses.
Let N_b,psi be every full irreducible exponent of H_b0 and set

    J_b=product psi^ceil(N_b,psi/2), j_b=degJ_b.

Choose monic integer lifts P_psi, with P_X=X, and put H_b=product P_psi^(N_b,psi)=X^a mathcal_Y_b.
Let k_b be ANY polynomial satisfying

    k_b^11=H_b0 C_b0^2 modulo phi^(8a),
    J_b X^a|k_b, degk_b<h_b+12a.                      (TT2)

Such a polynomial always exists by the bounded CRT proved below.
Choose ANY integer lift K_b of this degree.
For any power q of2 with q>=16 and any EVEN integer lambda put

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    mathcal_H=H_b^q, K=K_b^q, k=k_b^q,
    Phi=X^2+X+1 over Z, chi_0=X Phi^2,
    C_b=X^a mathcal_Y_b(chi_0)Phi(chi_0)^(7a),
    C=C_b^q, C_0=C_b0^q,
    F_b=H_b Phi^(7a), D_b=Phi^a K_b,
    P=D_b^q=Phi^A K,
    T_lambda=F_b^q+lambda P.                         (TT3)

Every T_lambda is an actual monic integer polynomial of degree d and reduction U=H_0phi^(7A).
For its SAME canonical divided remainders define

    a_T=rem_T(T(X^2-2))/2,
    b_T=rem_T(T(X^3-3X))/3,
    c_T=rem_T(T(X^5-5X^3+5X))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).

Then NO even lambda in TT3 satisfies F(T_lambda)=0 modulo8.
More precisely:

    lambda=0 modulo4:
        F(T_lambda)=0 modulo2 but F(T_lambda)!=0 modulo4;

    lambda=2 modulo4:
        F(T_lambda)=0 modulo4,
        ord_phi[(F(T_lambda)/4)bar]=4A.              (TT4)

The order in the second line is the exact truncated order in B_phi=F_2[X]/phi^(7A).
It is strictly below7A and hence proves actual coefficient failure modulo8.

For the second line write lambda=2+4t.
Its simultaneous modulo4 signs are EXACTLY

    X_+(T_lambda)=0 modulo4 iff lambda=6 modulo8,
    X_-(T_lambda)=0 modulo4 iff lambda=2 modulo8.      (TT5)

Thus the natural lambda=6 positive-sign and lambda=2 negative-sign bases do solve the actual modulo4 equations, but BOTH fail the first residual modulo8, before any modulo16 test can apply.
The exclusions cover every actual K_b allowed by TT2 and every actual integer lift of it.
Odd lambda, which changes the stated characteristic-two reduction, is outside this theorem.

For adopted C691 take a=2m and Y_b its complete Y.
Its doubled16m old support is exactly TT1 at8a, so the entire construction and obstruction apply, with

    A=2mq, d=q(30m+degY_b),
    original layer weight=12mq,
    canonical degree gap=q(m-8-5degH).               (TT6)

No support factor, degree or actual maximal q is removed.
This theorem does not exclude C691's independent higher-coefficient corrections, does not contradict the multi-correction C686 modulo8 solution, and proves no characteristic-zero nonexistence.

## Argument

### TT2: actual degree bounds and the strong root

Every exponent N_b,psi is at least2.
For integers n>=2 one has ceil(n/2)<=2n/3, including the even endpoint n=2.
Consequently j_b<=2h_b/3.
The eleventh-power map is invertible on the unit group modulo phi^(8a), whose order has only prime factors2 and3.
Combine that root with zero modulo J_b X^a.
The moduli are coprime and the unique least-degree CRT representative satisfies

    degk_b<j_b+17a<=2h_b/3+17a<h_b+12a,

where the strict final inequality follows from h_b>=17a>15a.
Thus TT2 has an actual bounded representative.
The X exponent of J_b is a/2, so TT2 gives X^(3a/2)|k_b.
After raising by q,

    k^11=H_0C_0^2 modulo phi^(8A),
    J_H=H_b0^(q/2)|k, X^(3A/2)|k,
    degK<d-2A, degP<d.                               (TT7)

For the first divisibility, q ceil(N_b,psi/2)>=qN_b,psi/2 at every actual factor.
The old support raised to q and the root in TT7 imply

    k^6=C_0^3 modulo phi^(8A),                        (TT8)

because the eleventh power of k^6/C_0^3 is H_0^6/C_0^21=1 and the eleventh-power map is injective.
No stronger integer relation is inferred from this local characteristic-two equality.

### TT3: the actual dyadic remainder identity

For any integer polynomials B,D, with B monic and degD<degB, put B_0=B^q and P_0=D^q.
For even lambda, T=B_0+lambda P_0 is monic.
Coefficient Frobenius gives B(C_2)=B^2 modulo2 and D(C_2)=D^2 modulo2, where C_2=X^2-2.
Repeated squaring therefore gives, for q>=16,

    B_0(C_2)=B_0^2 modulo32,
    P_0(C_2)=P_0^2 modulo32.

Taking the legitimate integer half in Delta(T)=(T(C_2)-T^2)/2 yields

    Delta(T)=-lambda B_0P_0
                  +lambda(1-lambda)P_0^2/2 modulo16.

In the actual quotient by T, B_0=-lambda P_0 exactly.
Hence the canonical integer coefficient congruence is

    a_T=rem_T([lambda(lambda+1)/2]P_0^2) modulo16.    (TT9)

The scalar is integral because lambda is even.
This identity uses the SAME actual monic divisor, commutation of monic division with reduction, and an integer half before reduction.
It does not substitute a local congruence into C_2.
For lambda=2 the scalar is3; for lambda=6 it is21, hence5 modulo16.
Applying TT9 to B=F_b,D=D_b gives the identity for TT3.

If lambda is divisible by4, that scalar is even.
Thus a_T is even in every primary quotient and a_T^5=0 modulo4.
The actual odd divided remainder has c_Tbar=phi^(2A)C_0 at phi.
It follows that

    (F(T_lambda)/2)bar=phi^(4A)C_0^2 in B_phi,

which is nonzero because C_0 is a unit and4A<7A.
Globally F is even since a_T is even, so this proves the entire first line of TT4, including lambda=0.

### TT4: the exact modulo4 signs in the remaining family

Suppose lambda=2+4t and write T_lambda=mathcal_H Phi^(7A)+2Phi^A K+4W with W=tP.
All C672 inputs hold by TT1 and TT7: the actual factorized base has full even exponents, both global forward divisibilities hold, the stronger root includes the required root, and the low odd coefficient condition follows from X^(3A/2)|k.
In particular F(T_lambda)=0 modulo4 for every t, on every primary.

Use the actual C669/C672 divisions

    sC^3-K^6=Phi^A L_s+2M_s,
    D_K=Delta(K)bar+k^2=k^2.

The last equality holds because K is an actual even integer power.
C672 supplies the genuine integer-half identities M_+bar=0 and M_-bar=rem_(phi^A)(k^6).
By TT8,

    L_sbar/phi^(3A)=(C_0^3+k^6)/phi^(4A)

has phi-order at least4A, so its contribution to the complete error eta_s modulo phi^(3A) is zero.
Also k(chi) has phi-order at least3A by its GLOBAL X^(3A/2) factor.
Substitution in the exact error, with every remaining term retained, gives

    eta_+=phi^(2A)k^2,
    eta_-=phi^(2A)
               [rem_(phi^A)(k^6)/k^4+k^2]=0
                                      modulo phi^(3A). (TT10)

For the negative equality, the bracket has numerator divisible by phi^A before reduction.
But Wbar=tbar phi^A k, hence Wbar^2=tbar phi^(2A)k^2.
The positive target is nonzero in that quotient, since k is a unit and2A<3A.
C669/C672's all-primary iff now gives exactly TT5.
This step confirms that the relevant failure below is not merely an unverified modulo4 base.

### TT5: the actual first half-remainder and the uncancelled first quarter

Use the exact C603 integer division

    J_F=mathcal_H C^2+3K^11=Phi^(3A)L_F+2M_F.

Let U_F=(H_b C_b^2)^(q/2) and V_F=K_b^(11q/2), so J_F=U_F^2+3V_F^2.
TT7 gives phi^(4A)|(U_Fbar+V_Fbar).
Actual monic division therefore gives U_F-V_F=Phi^(4A)Q+2R.
Modulo4 the actual polynomial identity is

    J_F=Phi^(8A)Q^2+2Phi^(4A)V_FQ.

Both terms are divisible by Phi^(3A).
Thus the remainder2M_F is divisible by4 coefficientwise, proving

    M_Fbar=0.                                        (TT11)

This is an integer half-remainder calculation, not a reduction-only division.
Furthermore

    L_Fbar=(H_0C_0^2+k^11)/phi^(3A),
    ord_phi L_Fbar>=5A.                              (TT12)

Now apply the COMPLETE C603 first-quarter formula to this actual T_lambda.
The actual modulo4 prerequisite was checked in TT4.
With w=tbar phi^A k and D_K=k^2, its two W terms are both tbar phi^(4A)k^11/H_0 and cancel in characteristic two.
Using TT11 gives the exact identity

    O_F=(F(T_lambda)/4)bar
       =phi^A k L_Fbar/H_0^2+phi^(4A)k^11/H_0
                                            in B_phi. (TT13)

The first term has order at least6A by TT12.
The second has EXACT order4A because k and H_0 are units.
It cannot be cancelled, and its order is below7A.
This proves the second line of TT4 for ALL t, independently of which sign passed TT5.

The doubled old support and still stronger choices of the eleventh-root jet do not remove this particular term in this two-term family.
It is the actual dyadic half contribution D_K=k^2.
The fixed C686 construction uses additional independent coefficient corrections and therefore is not of this prescribed two-term form.
No assertion that its output can be collapsed to TT3 is valid.

### TT6: original application and continuing boundary

C691 supplies every complete normalized input in TT1, with all multiplicities at least2, both forward divisibilities, the doubled old relation at16m=8a and the paid degree margin.
The CRT in TT2 uses only its existing degree allowance; it introduces no new support and does not change U_0^q or its actual maximal q.
The integer cyclotomic layers, zero-Haar synthetic lift, canonical degree gap and all higher-five factors remain attached to the same original data.
The exact actual costs are TT6.

The two-term identity is useful but does not bypass the full first-quarter correction.
This entire proposed simplification fails already modulo8, even on those doubled-support inputs, so it cannot be a route to modulo16 by itself.
The remaining multi-correction problem is still the actual evaluation of C689's first low/non-phi error and then its second low/high derivative conditions.
The proof supplies neither a passing nor a universally failing C689 class.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:49 |
| status | open |
| reason | Register the complete actual two-term failure for every stated strong-support input, bounded root coefficient, q>=16 and even scalar: the true dyadic remainder modulo16, exact modulo4 sign classes, actual first half-remainder and uncancelled phi^(4A) quarter, with all scalar boundaries and original degree/support costs. No failure of multi-correction C686 or all C691/C689 inputs is asserted. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete two-term obstruction](#statement) | TT1--TT6, every normalized support/multiplicity/degree hypothesis, all bounded strong-root K_b and integer lifts, every q>=16 and even lambda, exact first-residual failures and second modulo4 signs, complete original applicability limits. |
| argument | [Whole actual proof](#argument) | TT7--TT13 and TT2--TT6, bounded ceil-multiplicity CRT, actual Frobenius/monic remainder identity, all scalar cases, full eta and integer halves, real first-quarter cancellation and surviving leading term. |
| dependency | [Actual square-input modulo4 interface](Yin_C_G0672_v1.md#argument) | SQ6 and actual sign-dependent half-remainders, all-primary iff and first-residual modulo4 success for every W; matched to the raised strong-root/low CRT input. |
| dependency | [Exact first-quarter identity](Yin_C_G0603_v1.md#statement) | FE1--FE4, actual integer division of H C^2+3K^11 and all four quarter terms, including the true D_K contribution; M_Fbar=0 and the exact leading order are proved here. |
| support | [Adopted complete doubled-support family](Yin_C_G0691_v1.md#statement) | Application only: a=2m, every full Y multiplicity, both forward divisibilities, old support at16m=8a, actual maximal q, integer layers and paid canonical degree/gap; no higher residual success is imported. |
| support | [Actual multi-correction modulo8 theorem](Yin_C_G0686_v1.md#statement) | Applicability boundary only: its independent coefficient corrections are not assumed to collapse into this two-term family, and its proved solutions are not contradicted. |
| support | [Complete higher-lift criterion](Yin_C_G0689_v1.md#statement) | Continuing question only: this two-term family fails before its full-modulo8 input condition, so no conclusion about all its earlier multi-correction choices is inferred. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T05:06 |
| status | proved |
| reason | Adopt the fresh isolated whole review of all TT1--TT13 and the complete actual two-term argument. Every allowed even scalar fails the first residual modulo8; the sharper modulo4 sign classes, true dyadic half, surviving order4A term and unchanged C691 application costs are proved at the full declared scope. This restricted failure does not exclude independent multi-correction constructions, every C689 input, characteristic-zero realization or the unrestricted Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete two-term obstruction](#statement) | TT1--TT6, every normalized support/multiplicity/degree hypothesis, all bounded strong-root K_b and integer lifts, every q>=16 and even lambda, exact first-residual failures and second modulo4 signs, complete original applicability limits. |
| argument | [Whole actual proof](#argument) | TT7--TT13 and TT2--TT6, bounded ceil-multiplicity CRT, actual Frobenius/monic remainder identity, all scalar cases, full eta and integer halves, real first-quarter cancellation and surviving leading term. |
| dependency | [Actual square-input modulo4 interface](Yin_C_G0672_v1.md#argument) | SQ6 and actual sign-dependent half-remainders, all-primary iff and first-residual modulo4 success for every W; matched to the raised strong-root/low CRT input. |
| dependency | [Exact first-quarter identity](Yin_C_G0603_v1.md#statement) | FE1--FE4, actual integer division of H C^2+3K^11 and all four quarter terms, including the true D_K contribution; M_Fbar=0 and the exact leading order are proved here. |
| support | [Adopted complete doubled-support family](Yin_C_G0691_v1.md#statement) | Application only: a=2m, every full Y multiplicity, both forward divisibilities, old support at16m=8a, actual maximal q, integer layers and paid canonical degree/gap; no higher residual success is imported. |
| support | [Actual multi-correction modulo8 theorem](Yin_C_G0686_v1.md#statement) | Applicability boundary only: its independent coefficient corrections are not assumed to collapse into this two-term family, and its proved solutions are not contradicted. |
| support | [Complete higher-lift criterion](Yin_C_G0689_v1.md#statement) | Continuing question only: this two-term family fails before its full-modulo8 input condition, so no conclusion about all its earlier multi-correction choices is inferred. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0914_v1.md#whole-two-term-high-power-obstruction-finding) | Entire current fixed statement and argument, all direct-input applications, exact quantifiers and declared limits; independently reviewed. |
