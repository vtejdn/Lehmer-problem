---
author: Yin
---
# Structured higher Frobenius powers with removable low modulo-eight error

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed the structured q>=4 family, its fourth-power integer half-remainder argument and a square-preserving first correction.
Same_trace checked the existence of the complete structured modulo4 base, both signs of every relevant integer remainder, the first-quarter square condition and the true canonical-divisor contribution of that correction.
The corrected dyadic low contribution has factor phi^(2A).
The following is author mathematics, not independent review.
Focused reuse read the complete C669/C672 actual error, C675 next quarter, C677 first correction and now-adopted C680 low-image theorem, together with C667's normalized complete input and original costs.
No native test, parameter enumeration or external source theorem is used.

The [D1 fourth-power section](../drafts/Yin_D_G0001.md#fourth-power-low-obstruction-candidate) is development provenance, not a logical premise.
This entire theorem is initially open for fresh isolated whole mathematical review.

## Statement

### FP1: full normalized polynomial input and actual conclusion

Let a>=2 be EVEN, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b in F_2[X] be monic and prime to Xphi, satisfying Y_b|Y_b(chi) and Y_b|Y_b(X^3+X).
Put

    H_b0=X^a Y_b, h_b=degH_b0,
    C_b0=X^a Y_b(chi)Psi^(7a),
    H_b0^6=C_b0^21 modulo phi^(4a), h_b>=17a.           (FP1)

The last two relations are hypotheses.
Choose fixed monic integer lifts P_psi of every irreducible psi of H_b0, using P_X=X and its FULL exponent N_b,psi.
Write H_b=product P_psi^(N_b,psi)=X^a mathcal_Y_b.
Let q be a power of2 with q>=4, and put

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    U=H_0phi^(7A), mathcal_H=H_b^q,
    Phi=X^2+X+1 over Z, chi_0=X Phi^2,
    C_b=X^a mathcal_Y_b(chi_0)Phi(chi_0)^(7a),
    C=C_b^q, C_0=C_b0^q,
    S=(H_b Phi^(7a))^(q/2), J_H=H_b0^(q/2).           (FP2)

These are actual integer powers where integer polynomials are displayed.
In particular S is an integer square, S^2=mathcal_H Phi^(7A), and J_H^2=H_0.
The actual degree is d, and h>=17A.

Fix s in{1,-1}.
There exist actual integer K_f,W_f with degK_f<d-2A, degW_f<d, and a monic

    T_f=mathcal_H Phi^(7A)+2Phi^A K_f+4W_f,             (FP3)

with reduction U, such that its SAME canonical divided remainders

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T(T(C_2))/2, b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5))

satisfy

    F(T_f)=0 modulo8, X_s(T_f)=0 modulo4,
    (X_s(T_f)/4)bar in phi^(4A)
                          (F_2[X]/phi^(7A)).           (FP4)

All congruences mean coefficientwise congruences of actual canonical integer remainders.
The final inclusion is the complete removal of the low second quarter; it is NOT the assertion X_s(T_f)=0 modulo8.
All non-phi primary components of X_s(T_f) already vanish modulo8.
The final high square-image condition from C675 remains open.

The construction has three bounded stages: an actual K_b^q,W_b^(q/2) modulo4 base, one high K correction making F=0 modulo8 while preserving the low-image class, and the adopted C680 correction removing that low class.
It does not assume arbitrary local quotient coordinates are realized.

## Argument

### FP2: actual q-power modulo4 base and complete eta

Let k_b be the unique CRT representative which is the eleventh root of H_b0 C_b0^2 modulo phi^(4a) and is zero modulo H_b0 X^(a/2).
Its degree is below h_b+17a/2.
The root exists because the unit group at phi has order divisible only by2 and3, and the CRT moduli are coprime.
Let K_b be its coefficient0/1 integer lift and take K=K_b^q, k=k_b^q.
Then

    degK<h+17A/2<d-2A,
    k^11=H_0C_0^2 modulo phi^(4A),
    J_H|k, X^(3A/2)|k.                                (FP5)

Indeed k is even divisible by H_0, a stronger condition than J_H|k.
The actual normalized identities and forward divisibilities raise to the q-th power, so the complete square-input C672 domain holds.

For these concrete integers use the C669 definitions

    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A,
    D_K=Delta(K)bar+k^2, Delta(B)=(B(C_2)-B^2)/2,
    eta_s=(L_sbar/phi^(3A))/(H_0k^3)
        +phi^(2A)(M_sbar/k^4+D_K)
        +C_0^2Psi^A k(chi)/k^4 modulo phi^(3A).         (FP6)

Adopted C672 proves M_+bar=0 and M_-bar=rem_(phi^A)(k^6) for these actual integer divisions.
The latter is a q-th power, since k^6 is a q-th power and phi^A=(phi^a)^q, so polynomial division commutes with taking that power.
Also Delta(K)bar=0 because K is an actual even power, hence D_K=k^2.
Finally

    L_sbar/phi^(3A)=(C_0^3+k^6)/phi^(4A)

is a q-th-power polynomial: numerator and divisor are q-th powers and the division is exact.
Every factor and denominator in FP6 consequently has a q-th-power description, so eta_s=e_s^q for a unique e_s in F_2[X]/phi^(3a).
Uniqueness follows from the injective q-th-power map into F_2[X]/phi^(3A); orders multiply by q.
Choose its polynomial representative of degree<6a, lift it coefficientwise to W_b, and set

    W=W_b^(q/2), w=e_s^(q/2), degW<3A.                 (FP7)

Then w^2=eta_s at the FULL required precision.
C669/C672 give actual simultaneous F=X_s=0 modulo4 for T=S^2+2Phi^A K+4W on every primary.
Both choices of s are covered by their own concrete e_s.
In addition w is a global square because q>=4.
This proves the existence of the structured base before using any of its proposed power properties.

### FP3: fourth-power integer half-remainders for both signs

Put

    U_4=K_b^(3q/2), V_4=C_b^(3q/4),
    K^6=U_4^4, C^3=V_4^4.

C669 gives k^6=C_0^3 modulo phi^(4A).
Thus phi^A divides U_4bar+V_4bar, and actual monic integer division gives U_4-V_4=Phi^A Q_4+2R_4.
Expansion over Z, BEFORE any local division, yields

    U_4^4-V_4^4
      =4V_4^3 Phi^A Q_4+6V_4^2 Phi^(2A)Q_4^2
        +4V_4 Phi^(3A)Q_4^3+Phi^(4A)Q_4^4 modulo8.

Every term involving R_4 is divisible by8.
The remainder after division by Phi^A is therefore divisible by8.
For the positive sign, this proves that M_+ is divisible by4 and

    L_+=-2V_4^2 Phi^A Q_4^2-Phi^(3A)Q_4^4 modulo4.    (FP8)

For the negative sign perform the ACTUAL integer division K^6=Phi^A Q_K+R_K.
Since -C^3-K^6=-(C^3-K^6)-2K^6, exact monic linearity gives

    L_-=-L_+-2Q_K, M_-=-M_+-R_K.                      (FP9)

In particular Q_Kbar and R_Kbar are q-th powers by the same polynomial division argument.
The extra quotient term in FP9 is retained in the next error; it is not suppressed by a sign-free reduction.

### FP4: the structured low second quarter is in the exact image

Use the C675 actual auxiliaries

    P=Phi^A K,
    Xi=Delta(P)+P^2+W(C_2)-2PDelta(S)+Delta(S)^2,
    P_5=P(C_5), B_3=P(C_3)-Q_3^2P,
    S(C_3)=Q_3S+2E_3,
    E_s=-P L_s+mathcal_H Phi^(6A)M_s
             +3mathcal_H Phi^(4A)(sC^2P_5-K^4Xi),
    E_s=Phi^(7A)L_E+2M_E, degM_E<14A.                  (FP10)

All quotients and remainders are the actual integer ones.
The last even remainder exists because the structured base already solves X_s=0 modulo4.

First calculate M_Ebar BELOW phi^(4A) without guessing its half.
In the free module (Z/4Z)[X]/Phi^(4A), FP10 gives2M_E=-Phi^A K L_s, since all other terms contain Phi^(4A).
Using FP8--FP9 and the legitimate module half gives

    M_E,+bar=phi^(2A)k V_4bar^2 Q_4bar^2
                                              modulo phi^(4A),
    M_E,-bar=M_E,+bar+phi^A k Q_Kbar
                                              modulo phi^(4A). (FP11)

These are squares divisible by phi^A.
This use of a monic quotient over Z/4Z is what justifies the half; reduction modulo2 alone would not.

Next, S is an integer square, so Delta(S)bar=0, while P is an integer q-th power and Delta(P)bar=0.
Thus Xibar=Pbar^2+w^2 is a q-th power globally.
The reductions of L_s,M_s,mathcal_H,C,K,P_5 and all outer phi powers in E_s are q-th powers.
Consequently E_sbar is a q-th-power polynomial.
Its exact division by the q-th power phi^(7A) proves that L_Ebar is also a q-th power.
This is a statement about the actual quotient, not an independent selection of its residue.

Now C675 gives, modulo phi^(4A),

    O_X=(X_s(T)/4)bar
       =M_Ebar/H_0+phi^A k L_Ebar/H_0^2
        +w L_sbar/H_0
        +phi^(2A)(C_0 P_5bar^2+k^2 Xibar^2)
        +B_3bar^2.                                    (FP12)

Each displayed term is a square and divisible by phi^A.
For the first two use FP11 and the q-power quotient just proved.
For the third use w being a square and phi^(3A)|L_sbar.
The fourth has its explicit factor phi^(2A).
Finally phi^A divides B_3bar because both Pbar and P(C_3)bar are divisible by phi^A.
Hence

    O_X mod phi^(4A) belongs to
       I_low=phi^A Fr(F_2[X]/phi^(4A)).                 (FP13)

This conclusion applies to both signs on the actual structured modulo4 base.
It does not yet assert F=0 modulo8.

### FP5: the actual first-quarter target is square at sufficient precision

For the same base, C603 uses

    J_F=mathcal_H C^2+3K^11=Phi^(3A)L_F+2M_F.

Let U_F=(H_b C_b^2)^(q/2) and V_F=K_b^(11q/2).
Then J_F=U_F^2+3V_F^2, and its reduction is divisible by phi^(4A) by FP5.
Thus phi^(2A)|(U_Fbar+V_Fbar), and actual division gives U_F-V_F=Phi^(2A)Q_F+2R_F.
Modulo4,

    J_F=U_F^2-V_F^2
       =Phi^(4A)Q_F^2+2Phi^(2A)V_FQ_F modulo4.

Dividing by Phi^(3A), the first term has zero remainder and the second's remainder is2Phi^(2A)rem_(Phi^A)(V_FQ_F).
Thus the ACTUAL half-remainder satisfies

    phi^(2A)|M_Fbar.                                  (FP14)

C603's remaining terms are

    O_F=phi^A k L_Fbar/H_0^2
       +phi^(2A)k^9w^2/H_0+phi^(3A)k^10w/H_0
       +phi^(4A)(M_Fbar+k^9D_K)/H_0.

The reduction L_Fbar=(H_0C_0^2+k^11)/phi^(3A) is a q-th power.
All displayed terms other than M_F have at least square structure, since w is a q/2-th power and D_K=k^2.
The M_F term vanishes modulo phi^(6A) by FP14.
Therefore O_F is a square modulo phi^(6A), and its order is at least2A by the stronger root.

The unit A_F=C_0^2+phi^(4A)k^8w^2 is a square.
Hence the correction target

    ell=H_0 A_F^(-1)(O_F/phi^(2A)) modulo phi^(5A)

is square modulo phi^(4A).
Choose its CRT representative zero modulo J_H X^(5A/2), of degree<j_H+25A/2<=h+4A.
Its coefficient0/1 integer lift L has an ACTUAL factor X^(3A).
C677 now applies to

    K_1=K+Phi^(4A)L, T_1=T+2Phi^(5A)L, W_1=W,

giving F(T_1)=0 modulo8 and X_s(T_1)=0 modulo4 with unchanged actual degree and reduction.
It remains to check the low second error for this real first correction.

### FP6: low second-error change under the first correction

Put Q=Phi^(5A)L.
Use the actual C675 polynomial representatives

    A_rep=P^2+2Xi,
    C_rep=5Phi^(2A)C+2P(C_5)+4(W(C_5)+R_5),
    N=4B_3^2-A_rep^3+sC_rep^3,

where R_5=S(chi_0)E_5S'(chi_0)+E_5^2S'(chi_0)^2 and E_5=(C_5-chi_0)/2.
Let N=Q_N T+R_N be actual monic division.
The remainder R_N is congruent to X_s(T) modulo8 and has coefficients divisible by4.
Reduction gives

    Q_Nbar U=phi^(6A)(k^6+C_0^3),
    phi^(3A)|Q_Nbar.

Moreover the right side and U are q-th powers, so Q_Nbar is a q-th power by polynomial cancellation.
Perform actual division Q_N=Phi^(3A)R+2Z.
Then

    Rbar=Q_Nbar/phi^(3A)

is a q-th power.
In the quotient by T_1=T+2Q, the old N contributes R_N-2Q_N Q.
The same actual divisor gives

    -2Phi^(8A)RL-4Phi^(5A)ZL
      =4Phi^(2A)K_1RL/mathcal_H
                         -4Phi^(5A)ZL modulo8.

The second term has quarter order5A and disappears only on reducing that legitimate quarter modulo phi^(4A).
Thus the genuine canonical-divisor carry in the low error is

    phi^(2A)(k/H_0)Rbar ell modulo phi^(4A).             (FP15)

The C3 change in4B_3^2 vanishes at this precision because Qbar and Q(C_3)bar have phi-order at least5A.
For C5, the ACTUAL integer factor X^(3A)|L gives phi^(6A)|Q(C_5)bar.
The change in C_rep is2Q(C_5), so its cube changes by6Phi^(4A)C^2Q(C_5)+4C_rep Q(C_5)^2 modulo8.
Write Q(C_5)=Phi^(6A)R_5^*+2E_5^* by actual monic division.
The summand6Phi^(4A)C^2Q(C_5) gives only quarter order at least4A after using T_1, and4C_rep Q(C_5)^2 has zero quarter reduction because its phi-order is at least14A.
This is the same complete composition mechanism retained in C680 LR4, with its hypothesis checked directly here.
No local phi congruence has been composed with C5.

For the dyadic change, use the exact formula

    delta A_rep=Q(C_2)+2Q^2+4PQ-4QDelta(S).

Since S is an integer square, Delta(S) is even and the last term is0 modulo8.
In the quotient by T_1,

    Q(C_2)=-2Phi^(4A)K_1 L(C_2)/mathcal_H
             -4Phi^(3A)W L(C_2)/mathcal_H modulo8,
    2Q^2=-4Phi^(4A)K_1L^2/mathcal_H modulo8,
    4PQ=4Phi^(6A)KL.

The first identity follows by expanding Phi(C_2)=Phi^2+2Delta(Phi); the correction coefficients vanish after the actual divisor relation, since5A is even.
Retain all three terms before taking the cube.
Their squared change is zero modulo8, and A_rep^2=P^4 modulo4.
After multiplication by3P^4, every term except the first in Q(C_2) has factor4 and phi-order at least7A.
Reducing that first term once more by T_1 gives the exact LOW quarter contribution

    delta(A_rep^3)/4
        =phi^(2A)k^6 ell^2/H_0^2 modulo phi^(4A).      (FP16)

In particular its exponent is2A, not A.

Combining the actual composed changes with FP15 yields

    O_X(T_1)+O_X(T)
       =phi^(2A)[k^6 ell^2/H_0^2
                         +(k/H_0)Rbar ell]
                                      modulo phi^(4A). (FP17)

Both summands lie in I_low: k,H_0,Rbar are q-th powers, ell is square at this precision, and phi^(2A) is a square.
Together with FP13 this proves that the FIRST-MODULO8 base T_1 has zero C680 low invariant.

### FP7: removal of the low quarter and original scope

All C680 hypotheses hold for T_1: h>=17A, the actual root modulo phi^(4A), the global J_H and low odd-coefficient conditions, F=0 modulo8 and X_s=0 modulo4.
The first correction preserves the low K conditions because L has factor X^(3A).
Equation FP17 shows that its low invariant vanishes.
Apply C680's bounded v/ell construction with its specified integer lifts to obtain T_f in FP3 satisfying FP4.
This proves actual existence, without evaluating an unbounded coefficient list or presuming surjectivity of the high error map.

For any paid C667 input take a=2m, Y_b=Y_0 and q the ACTUAL chosen Frobenius power with q>=4.
Its old support and forward divisibilities are FP1, and degY_0>=45L_0>360m implies h_b>=17a.
Every stage keeps the same

    d=q(30m+degY_0), A=2mq,
    canonical degree gap=q(5m-Q-5degH),
    original integer layer weight=12mq.

The global maximal q of U and its characteristic-two canonical R remains unchanged, because the reduction U is unchanged.
No smaller characteristic-zero input is inferred from the normalized construction.
Both adopted C698 canonical families therefore admit this actual partial modulo8 construction at every q>=4 with their original costs.

Only the high second-quarter square-image condition remains at this dyadic layer.
No full X_s=0 modulo8, equality of synthetic G_int with actual G_can, characteristic-zero residual identities, irreducibility, total reality, original realization or Task completion is asserted.
The q=1 and q=2 inputs are outside this theorem's constructed low-obstruction conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:50 |
| status | open |
| reason | Register actual bounded q>=4 power bases, the full q-power eta and chosen integer W, both-sign fourth-power half-remainders and low quarter, the true first half-remainder/square correction target, exact first-retuning canonical carry and low-image preservation, and resulting actual removal of the low second quarter while F vanishes modulo8. The high square-image test, full second modulo8 solution and original realization remain open. No native computation or new original exclusion is claimed. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire structured construction](#statement) | FP1--FP4, complete normalized input and actual integer powers, every q>=4 and either fixed sign, bounded monic T_f with original reduction/degree, first residual modulo8, second modulo4 and removal of its complete low quarter; no high or characteristic-zero conclusion. |
| argument | [Whole integer construction and correction](#argument) | FP5--FP17 and all FP2--FP7 sections, bounded CRT and actual q-power eta/W, positive and negative integer half-remainders, every quotient power and first-quarter target, actual C2/C3/C5/canonical carry, low-image preservation and paid application. |
| dependency | [Actual complete modulo4 error](Yin_C_G0669_v1.md#statement) | Entire factorized-base eta, exact integer L_s/M_s and root/support consequence, all-primary same-T iff; matched to the actual raised data. |
| dependency | [Square-input actual half-remainders](Yin_C_G0672_v1.md#argument) | M_+bar=0 and M_-bar=rem_(phi^A)k^6, integer square/base hypotheses and modulo4 existence; the stronger fourth-power remainder and q-power eta are proved here. |
| dependency | [Exact first quarter](Yin_C_G0603_v1.md#statement) | Full FE4 with its actual L_F/M_F and changing-divisor term, used to prove the square target at precision6A. |
| dependency | [Exact second quarter and representatives](Yin_C_G0675_v1.md#argument) | MQ6 and MQ9--MQ15, genuine E_s/L_E/M_E, all-primary actual polynomial representatives, C5 term and both divisor contributions; no error coordinate is selected independently. |
| dependency | [Adopted first correction](Yin_C_G0677_v1.md#statement) | Exact K correction preserving the SAME W modulo4, full F8 and bounded original degree; strengthened low CRT is checked here at h>=17A. |
| dependency | [Adopted exact low elimination](Yin_C_G0680_v1.md#statement) | Complete declared correction family and iff for I_low, applied only after proving the actual first-corrected base has zero invariant; its high obstruction remains unresolved. |
| dependency | [Actual low-composition calculation](Yin_C_G0680_v1.md#argument) | LR3--LR4 source mechanism for global C3/C5 change, checked again for the distinct first correction Q=Phi^(5A)L and with its own exact divisor carry FP15--FP17. |
| support | [Paid complete canonical input](Yin_C_G0667_v1.md#statement) | Application only: normalized a=2m, full forward/root/canonical input, degree lower margin, actual maximal q and unchanged original layers/gap; no synthetic integer lift is equated to G_can. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:04 |
| status | proved |
| reason | The complete fixed FP1--FP17 statement and six-section argument were directly read, followed by all of fresh isolated R904. Adopt the actual q>=4 structured base, complete q-power eta, both-sign fourth-power integer remainders, actual first-quarter target and bounded correction, true first-retuning canonical carry and removal of the complete low second quarter. All original costs and maximal-q application scopes remain unchanged. The complete high square-image condition, full second modulo8 solution and original realization are not asserted by this theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire structured construction](#statement) | FP1--FP4, complete normalized input and actual integer powers, every q>=4 and either fixed sign, bounded monic T_f with original reduction/degree, first residual modulo8, second modulo4 and removal of its complete low quarter; no high or characteristic-zero conclusion. |
| argument | [Whole integer construction and correction](#argument) | FP5--FP17 and all FP2--FP7 sections, bounded CRT and actual q-power eta/W, positive and negative integer half-remainders, every quotient power and first-quarter target, actual C2/C3/C5/canonical carry, low-image preservation and paid application. |
| dependency | [Actual complete modulo4 error](Yin_C_G0669_v1.md#statement) | Entire factorized-base eta, exact integer L_s/M_s and root/support consequence, all-primary same-T iff; matched to the actual raised data. |
| dependency | [Square-input actual half-remainders](Yin_C_G0672_v1.md#argument) | M_+bar=0 and M_-bar=rem_(phi^A)k^6, integer square/base hypotheses and modulo4 existence; the stronger fourth-power remainder and q-power eta are proved here. |
| dependency | [Exact first quarter](Yin_C_G0603_v1.md#statement) | Full FE4 with its actual L_F/M_F and changing-divisor term, used to prove the square target at precision6A. |
| dependency | [Exact second quarter and representatives](Yin_C_G0675_v1.md#argument) | MQ6 and MQ9--MQ15, genuine E_s/L_E/M_E, all-primary actual polynomial representatives, C5 term and both divisor contributions; no error coordinate is selected independently. |
| dependency | [Adopted first correction](Yin_C_G0677_v1.md#statement) | Exact K correction preserving the SAME W modulo4, full F8 and bounded original degree; strengthened low CRT is checked here at h>=17A. |
| dependency | [Adopted exact low elimination](Yin_C_G0680_v1.md#statement) | Complete declared correction family and iff for I_low, applied only after proving the actual first-corrected base has zero invariant; its high obstruction remains unresolved. |
| dependency | [Actual low-composition calculation](Yin_C_G0680_v1.md#argument) | LR3--LR4 source mechanism for global C3/C5 change, checked again for the distinct first correction Q=Phi^(5A)L and with its own exact divisor carry FP15--FP17. |
| support | [Paid complete canonical input](Yin_C_G0667_v1.md#statement) | Application only: normalized a=2m, full forward/root/canonical input, degree lower margin, actual maximal q and unchanged original layers/gap; no synthetic integer lift is equated to G_can. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0904_v1.md#whole-structured-higher-power-finding) | Entire actual q>=4 construction, all true integer halves and quotient powers, both signs, full first-retuning composition/carry and low elimination, with each paid canonical application and remaining boundary. |
