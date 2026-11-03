---
author: Yin
---
# Actual high-power same-polynomial solutions of both modulo-eight residuals

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed keeping q/2-th powers through the first correction, using actual coefficient subrings and retaining an integer derivative condition through the second correction.
Same_trace checked the full actual first half-remainder, both bounded CRT constructions, the different first integer lift, actual monic division and all primary components, and the derivative argument giving the final high square condition.
This is author mathematics, not independent review or adoption.
Focused reuse read C683, the complete adopted C677/C680 corrections and C675 final same-polynomial criterion, as well as their C603/C699/C702 and original C667/C668 interfaces.
C683 is a fixed pending-review dependency at this registration; its required structured-base and low-carry claims are used conditionally until established.
The other named correction interfaces are already adopted.
No native computation, parameter enumeration or external source theorem is used.

The [D1 high-power section](../drafts/Yin_D_G0001.md#high-power-full-mod-eight-construction) is development provenance, not a logical premise.
This entire theorem is initially open for fresh isolated whole mathematical review.

## Statement

### HP1: full input and actual simultaneous conclusion

Let a>=2 be even, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y_b in F_2[X] be monic and prime to Xphi, with Y_b|Y_b(chi) and Y_b|Y_b(X^3+X).
Set

    H_b0=X^a Y_b, h_b=degH_b0,
    C_b0=X^a Y_b(chi)Psi^(7a),
    H_b0^6=C_b0^21 modulo phi^(4a), h_b>=17a.          (HP1)

The final two relations are hypotheses.
Choose fixed monic integer lifts P_psi of every irreducible of H_b0, with P_X=X and the full exponent N_b,psi, and put H_b=product P_psi^(N_b,psi)=X^a mathcal_Y_b.
Let q be a power of2 with q>=256, and set

    A=aq, H_0=H_b0^q, h=qh_b, d=h+14A,
    U=H_0phi^(7A), mathcal_H=H_b^q,
    Phi=X^2+X+1 over Z, chi_0=X Phi^2,
    C_b=X^a mathcal_Y_b(chi_0)Phi(chi_0)^(7a),
    C=C_b^q, C_0=C_b0^q,
    J_H=H_b0^(q/2), j_H=h/2,
    S=(H_b Phi^(7a))^(q/2).                           (HP2)

In particular S^2=mathcal_H Phi^(7A), h>=17A, and all indicated integer powers are actual ones.
Fix one sign s in{1,-1}.
For every input HP1--HP2 there is a monic integer T_* of degree d and reduction U such that its SAME canonical integer divided remainders

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3, c_T=rem_T(T(C_5))/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5))

satisfy the simultaneous coefficientwise congruences

    F(T_*)=X_s(T_*)=0 modulo8.                        (HP3)

The construction has the actual form

    T_*=mathcal_H Phi^(7A)+2Phi^A K_2+4W_2+8Z,
    degK_2<d-2A, degW_2<d, degZ<d.                   (HP4)

It first constructs a concrete T_2 with F=0 modulo8, X_s=0 modulo4 and zero complete low second quarter.
For this fixed T_2 modulo8, exactly2^(d-3A) coefficient classes T_2+8Z modulo16 satisfy HP3.
This is the fiber over that constructed base, not a count of all possible bases or simultaneous solutions for both signs.
The theorem constructs each selected sign separately.

For the paid C667/C668 inputs, a=2m and Y_b=Y_0 retain their complete factors and satisfy HP1.
The actual parameters remain

    A=2mq, d=q(30m+degY_0),
    canonical degree gap=q(5m-Q-5degH),
    original integer layer weight=12mq.              (HP5)

No change in the reduction U, its characteristic-two canonical remainder, the original degree, integer layer multiplicities or actual maximal Frobenius q is made.
For generic HP1, q is merely the specified raised power; maximality is asserted only when supplied by the original C667 input.
No equality of synthetic G_int with actual G_can, characteristic-zero residual identity, irreducibility, total reality, original realization or Task completion is concluded.

## Argument

### HP2: the actual structured modulo4 base and first half-remainder

Use the concrete C683 FP2 construction.
Thus k_b is the eleventh root of H_b0 C_b0^2 modulo phi^(4a), zero modulo H_b0 X^(a/2), and has degree<h_b+17a/2.
With its coefficient0/1 integer lift K_b set K=K_b^q and k=k_b^q.
The actual C699 error is a q-th power eta_s=e_s^q, with deg e_s<6a.
Let W_b be its coefficient0/1 lift and set W=W_b^(q/2), w=e_s^(q/2).
Then

    T_0=S^2+2Phi^A K+4W,
    F(T_0)=X_s(T_0)=0 modulo4,
    k^11=H_0C_0^2 modulo phi^(4A),
    J_H|k, X^(3A/2)|k,
    degK<h+17A/2, degW<3A.                            (HP6)

The actual eta and both signs of its half-remainder are established in C683 FP2--FP4; no choice of a or c independently is made.
C683 also proves that the low second quarter of T_0 belongs to I_low=phi^A Fr(F_2[X]/phi^(4A)).

We strengthen the power information of its ACTUAL first half-remainder.
Use

    mathcal_H C^2+3K^11=Phi^(3A)L_F+2M_F,
    U_F=(H_b C_b^2)^(q/2), V_F=K_b^(11q/2).

The stronger root in HP6 implies phi^(2A)|(U_Fbar+V_Fbar).
Actual monic division therefore gives U_F-V_F=Phi^(2A)Q_F+2R_F.
Modulo4,

    U_F^2+3V_F^2
      =Phi^(4A)Q_F^2+2Phi^(2A)V_FQ_F.

Take the actual remainder modulo Phi^(3A), then its legitimate half and reduction.
Since the first displayed term has zero remainder, one obtains the EXACT identity

    M_Fbar=phi^(2A) rem_(phi^A)(V_Fbar Q_Fbar),
    Q_Fbar=(U_Fbar+V_Fbar)/phi^(2A).                  (HP7)

Both V_Fbar and Q_Fbar are q/2-th powers: numerator and exact divisor of the latter have this form.
Monic division of a q/2-th power by phi^A=(phi^(2a))^(q/2) gives a quotient and remainder that are q/2-th powers, by uniqueness after raising the lower division.
Thus M_Fbar itself is a q/2-th-power polynomial, not merely divisible by phi^(2A).

The complete C603 first quarter is

    O_F=phi^A k L_Fbar/H_0^2
        +phi^(2A)k^9w^2/H_0+phi^(3A)k^10w/H_0
        +phi^(4A)(M_Fbar+k^9D_K)/H_0,
    D_K=Delta(K)bar+k^2=k^2,
    Delta(B)=(B(C_2)-B^2)/2.                           (HP8)

Here L_Fbar=(H_0C_0^2+k^11)/phi^(3A) is a q-th power.
Every term of HP8 is a q/2-th power in F_2[X]/phi^(7A).
All denominators are units, and taking their inverses preserves that image.
The statement uses phi^(7A)=(phi^(14a))^(q/2), so it includes the FULL precision7A.
The stronger root gives O_F in phi^(2A), as in C677.
Consequently, with A_F=C_0^2+phi^(4A)k^8w^2, the target

    ell_1=H_0 A_F^(-1)(O_F/phi^(2A))
                                      modulo phi^(5A) (HP9)

is a q/2-th power at the full precision5A.

### HP3: a different actual first lift with complete power structure

Both CRT moduli in

    ell_1 equal to HP9 modulo phi^(5A),
    ell_1=0 modulo J_H X^(5A/2)                        (HP10)

are q/2-th powers:

    phi^(5A)=(phi^(10a))^(q/2),
    J_H X^(5A/2)=(H_b0 X^(5a))^(q/2).

Their lower moduli are coprime.
The Frobenius map is injective from each lower quotient to the corresponding image, because irreducible orders multiply by q/2.
Solve the lower CRT and take its unique polynomial representative ell_b of degree<h_b+25a.
The unique representative in HP10 is ell_1=ell_b^(q/2), and its degree is below j_H+25A/2<=h+4A.
Since ell_b is zero modulo H_b0 X^(5a), it is divisible by X^(6a).
Take its coefficient0/1 integer lift L_b, but use the ACTUAL power

    L_1=L_b^(q/2), K_1=K+Phi^(4A)L_1,
    T_1=T_0+2Phi^(5A)L_1, W_1=W.                     (HP11)

Thus X^(3A) divides L_1 over Z.
C677 applies to every actual representative with the required reduction and degree, so F(T_1)=0 modulo8 and X_s(T_1)=0 modulo4.

The low preservation in C683 FP6 also holds for this particular lift, although it is not in general the coefficient0/1 lift of ell_1.
To check this point, retain its actual Q=Phi^(5A)L_1 and N=Q_NT_0+R_N from the C675 representatives.
The exact division Q_N=Phi^(3A)R+2Z_0 still has Rbar=Q_Nbar/phi^(3A) a q-th power.
The canonical-divisor carry is phi^(2A)(k/H_0)Rbar ell_1 modulo phi^(4A).
The actual integer factor X^(3A)|L_1 gives phi^(6A)|Q(C_5)bar, so the C5 change and C3 change vanish in that low quarter by the actual divisions in C683 FP6.
Finally its dyadic identity

    delta A_rep=Q(C_2)+2Q^2+4PQ-4QDelta(S),
    P=Phi^A K,

uses no coefficient-lift restriction.
The same actual T_1 relation gives the low cube contribution phi^(2A)k^6 ell_1^2/H_0^2.
All occurrences of L_1(C_2) in that legitimate quarter reduce to ell_1^2.
Therefore the COMPLETE low variation remains

    O_1+O_0=phi^(2A)
         [k^6ell_1^2/H_0^2+(k/H_0)Rbar ell_1]
                                      modulo phi^(4A), (HP12)

where O_i=(X_s(T_i)/4)bar denotes the actual canonical quarter.
This check retains all integer half/carry and composition arguments of C683; it does not infer equality of errors from equal reductions of T.
Since ell_1 is a q/2-th power, HP12 belongs to I_low.
Together with the structured initial low error, this proves

    O_1 mod phi^(4A) belongs to I_low.                 (HP13)

The root, global J_H divisibility, low K conditions and every degree bound are preserved.

### HP4: coefficient subrings under powers and actual monic division

For an integer polynomial B, k>=0 and 1<=r<=k+1,

    B^(2^k) modulo2^r belongs to
                (Z/2^rZ)[X^(2^(k-r+1))].             (HP14)

Indeed B^2=B(X^2) modulo2.
If two integer polynomials agree modulo2, their 2^j-th powers agree modulo2^(j+1), by repeated squaring.
For k>=r this replaces B^(2^k) by B(X^2)^(2^(k-1)) modulo2^r.
Iterate until the remaining exponent is2^(r-1), which proves HP14.
The terminal case k=r-1 is the unrestricted polynomial ring.

For any commutative coefficient ring, monic division of two polynomials in X^t remains in that same subring if the divisor is monic.
This follows by performing division in the variable X^t and using uniqueness of quotient and remainder.
Reduction modulo an integer commutes with monic division, so this applies to the reductions of actual integer canonical quotients.
Dividing an actual even polynomial by2 also preserves a subring assertion modulo8 when the numerator was in that subring modulo16: all coefficients outside it were multiples of16.

Let N be a power of2 with N>=8.
Then

    C_2^N=X^(2N) modulo16,
    C_p^N modulo8 belongs to (Z/8Z)[X^(N/2)]
                                               (p=3,5). (HP15)

For the first claim, write N=2^n and expand (X^2-2)^N.
For every1<=j<=N, the coefficient valuation is at least n-v_2(j)+j>=n+1>=4; the estimate follows from j binom(N,j)=N binom(N-1,j-1).
For the second, write C_p=X R_p(X^2), where R_3(Y)=Y-3 and R_5(Y)=Y^2-5Y+5.
HP14 with r=3 gives R_p(Y)^N modulo8 in Y^(N/4).
After substituting Y=X^2 and multiplying by X^N, the claimed subring is X^(N/2).

Suppose now that an actual monic T of degree d belongs modulo16 to (Z/16Z)[X^N].
Its dyadic canonical polynomial is a_T=rem_T Delta(T).
By HP15, T(C_2)-T^2 modulo16 belongs to X^N; the legitimate half followed by actual monic division proves a_T modulo8 belongs to X^N.
For p=3,5, HP15 and division by the unit p modulo8 show that b_T,c_T modulo8 belong to X^(N/2).
The divisor T modulo8 also lies in that subring.
Consequently the actual canonical second residual modulo8 belongs to X^(N/2).
If it is coefficientwise divisible by4, its quarter satisfies

    (X_s(T)/4)bar belongs to F_2[X^(N/2)].             (HP16)

No local primary congruence has been composed with C_p, and no division by2 in characteristic two is used.

For T_1 in HP11 the exact expression is

    T_1=(H_b Phi^(7a))^q
          +2(Phi^a K_b)^q+4W_b^(q/2)
          +2(Phi^(10a)L_b)^(q/2).

Set N=q/16 and E=q/32.
HP14 shows T_1 modulo16 is in X^N, and N>=16.
The actual modulo4 condition and HP16 therefore give

    O_1 in F_2[X^E], E>=8.                            (HP17)

Moreover T_1' is coefficientwise divisible by8, because each actual power in its displayed expression has exponent divisible by q/2>=128.
The prime denotes ordinary integer polynomial differentiation.

### HP5: low elimination with fourth-power residues and the specified lifts

Write k_1=K_1bar and retain w=Wbar.
Both k_1 and w are q/2-th powers globally, while H_0 is a q-th power.
The C680 low-elimination equation is

    v^2=H_0 O_1/(phi^A k_1^5) modulo phi^(3A).         (HP18)

The polynomial O_1 is globally divisible by phi^A by HP13.
Because O_1 is an E-th power, A is divisible by E, and the division is exact, O_1/phi^A is an E-th-power polynomial.
All other factors in HP18, including the unit denominator and the modulus phi^(3A), have E-th-power descriptions.
Thus its right side is an E-th power in that quotient.
Taking its lower representative and then an E/2-th power yields a polynomial solution v of degree<3A.
Since E/2>=4, this v is a fourth power globally.
This is a valid C680 choice because3A<h+11A.

Use the ACTUAL C680 correction target

    ell_2=[phi^(3A)k_1^9v^2
                      +phi^(5A/2)k_1^10v]/A_F1
                                         modulo phi^(5A),
    A_F1=C_0^2+phi^(4A)k_1^8w^2,
    ell_2=0 modulo J_H X^(5A/2).                      (HP19)

Its numerator, unit denominator and both CRT moduli are fourth powers.
Take the unique least-degree representative by the fourth-root CRT.
Then ell_2 is a global fourth power and degell_2<j_H+25A/2<=h+4A.
The high target and modulus are divisible by phi^(5A/2), hence so is ell_2 as a polynomial.
Because5A/2 is divisible by4, the exact quotient ell_2/phi^(5A/2) is a fourth power too.

Now use precisely the C680 lifts, not arbitrary replacements:

    V=coefficient0/1 lift of v,
    M=coefficient0/1 lift of ell_2/phi^(5A/2),
    L_2=Phi^(5A/2)M,
    D=Phi^(3A/2)V, Q_2=Phi^(5A)L_2,
    K_2=K_1+Phi^(4A)L_2,
    W_2=W+Phi^(3A/2)V,
    T_2=T_1+2Q_2+4D.                                 (HP20)

V and M belong to Z[X^4], so V' and M' have every coefficient divisible by4.
Also3A/2,5A/2 and15A/2 are divisible by4.
Therefore D' and Q_2' are divisible by4, and

    T_2' is coefficientwise divisible by8.            (HP21)

C680 proves for these exact bounded choices that

    F(T_2)=0 modulo8, X_s(T_2)=0 modulo4,
    O_2=(X_s(T_2)/4)bar is zero modulo phi^(4A).        (HP22)

Indeed HP18 is exactly its complete low-image equation, and HP19 restores the first quarter while preserving the same new W modulo4.
Its complete changing-divisor and C5 calculations apply to the specified lift in HP20 without alteration.
All non-phi primary components vanish modulo8 by C675.
The bounds are degV<3A<h+11A, degL_2<h+4A, degK_2<d-2A and degW_2<d.
In particular T_2 is monic of the SAME degree d and has reduction U.

### HP6: an integer derivative lemma for canonical divided remainders

Let T be any monic integer polynomial whose derivative is coefficientwise divisible by8.
If an integer polynomial B has B' divisible by8, its actual canonical remainder R=rem_T B also has R' divisible by8.
For B=QT+R, differentiation gives R'=-Q'T modulo8, since B' and QT' vanish there.
But degR'<degT, so monic division of that congruence forces R'=0 coefficientwise modulo8.
This argument works over Z/8Z despite its zero divisors because the divisor is monic.

For a_T use the actual integer Delta(T)=(T(C_2)-T^2)/2.
Its exact derivative is

    Delta(T)'=X T'(C_2)-T T',

which is divisible by8.
Since a_T=rem_T Delta(T), the preceding argument gives a_T'=0 modulo8.
For p=3,5 the derivative of T(C_p) is divisible by8.
The same remainder argument gives (p b_T)'=0 or (p c_T)'=0 modulo8.
As p is odd, b_T' and c_T' are themselves zero modulo8.
These integer divided remainders exist for every monic T: C_p=X^p modulo p and the Frobenius congruence gives T(C_p)=T^p modulo p, so its remainder is divisible by p.

The polynomial b_T^2-a_T^3+s(c_T^3-2b_T^5) consequently has derivative divisible by8.
A final application of actual monic division proves

    X_s(T)'=0 modulo8.                               (HP23)

If X_s(T) is also coefficientwise divisible by4, write X_s(T)=4R with R in Z[X].
Equation HP23 gives R'=0 modulo2, hence Rbar is a GLOBAL square polynomial over F_2.
This assertion concerns the canonical remainder's coefficients, not merely a derivative-zero local class.

Apply this lemma to the actual T_2 in HP20--HP22.
It proves O_2 is globally a square.
Since phi^(4A)|O_2 by HP22, its exact quotient by this square polynomial is a square.
The unit k_2^4 is also a square.
Therefore

    O_2/(phi^(4A)k_2^4)
                  is a square modulo phi^(3A).        (HP24)

This is the complete remaining C675 high condition, now proved for the constructed base.

### HP7: final shared correction, fiber and original applicability

Choose z solving

    z^2=O_2/(phi^(4A)k_2^4) modulo phi^(3A),

and any degree<d representative, with an integer lift Z of that degree.
C675's ACTUAL same-divisor correction T_*=T_2+8Z leaves the first residual zero modulo8 and changes the second quarter by phi^(4A)k_2^4z^2.
Every non-phi component remains zero.
This proves HP3 coefficientwise on the entire canonical free module.

The final square map fixes z modulo phi^(3A/2), has rank3A, and leaves all other coordinates free.
Hence precisely2^(d-3A) degree<d classes z produce the stated T_* modulo16 above the fixed T_2 modulo8.
The final correction can be absorbed in W_2+2Z and obeys the same actual degree bound in HP4.
No earlier correction increases the monic degree or changes U.

For C667 take a=2m, Y_b=Y_0 and the original actual q>=256.
Its complete forward data and old support imply HP1, and its prescribed fresh factor gives degY_0>=45L_0>360m, so h_b>=17a.
This includes the two adopted C668v2 families at their exact scopes.
The resulting degree, canonical gap and integer layer weight are HP5, and the final fiber is2^(q(24m+degY_0)).
The unchanged nonsquare normalized input preserves the actual maximal q exactly as supplied in C667.
The proof does not infer maximality from a finite jet and does not discard a higher-five-order component or its cost.

The construction solves both stated residuals modulo8 for the SAME actual integer monic T_*.
It does not solve any higher precision, impose a new spectral condition, identify the synthetic cyclotomic G_int with G_can, or realize the original characteristic-zero Task.
No claim for q<256 is made by this argument.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:02 |
| status | open |
| reason | Register actual simultaneous same-polynomial solutions of both canonical residuals modulo8 for every declared normalized input and every q>=256, with the complete first half-remainder, power-preserving bounded corrections, actual coefficient subrings/monic division, low elimination, integer derivative lemma, all primary components and final shared8Z fiber. C683 is a fixed pending-review dependency at registration; no characteristic-zero realization or Task completion is asserted. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual simultaneous theorem](#statement) | HP1--HP5, all normalized hypotheses, actual integer factorized input and q>=256, either separately chosen sign, bounded monic same-reduction T, both residuals modulo8, exact final fiber and unchanged original costs. |
| argument | [Whole power-preserving construction](#argument) | HP6--HP24 and HP2--HP7, actual half-remainder and q/2 CRT, distinct integer lift with full canonical carry, coefficient-subring and derivative lemmas, specified fourth-power residue lifts, all-primary high condition and final shared correction. |
| dependency | [Structured base and low error](Yin_C_G0683_v1.md#argument) | Fixed pending-review dependency: FP2--FP4 actual K_b^q/W_b^(q/2), full eta and both sign remainders, initial low square image; FP6 full actual first-correction carry, rechecked here for the different integer lift. No adopted status is presumed. |
| dependency | [Exact first quarter](Yin_C_G0603_v1.md#statement) | FE4 actual first-quarter formula with the genuine L_F/M_F and divisor term; the stronger q/2-th-power remainder and full-precision correction target are proved here. |
| dependency | [First actual correction](Yin_C_G0677_v1.md#statement) | HC2--HC8 for every bounded integer representative, same-W modulo4 preservation and exact first modulo8 solution; strengthened global CRT and actual power lift are established here. |
| dependency | [Specified complete low correction](Yin_C_G0680_v1.md#statement) | LR1--LR7 with its exact V/M integer lifts, actual first-restoration and low-quarter formula; the fourth-power choices and derivative preservation are proved here, rather than changing that family. |
| dependency | [Actual low-correction proof](Yin_C_G0680_v1.md#argument) | LR3--LR4 complete canonical-divisor and actual C2/C3/C5 calculations, applicable to the specified HP20 lifts without alteration. |
| dependency | [All-primary final correction and fibers](Yin_C_G0675_v1.md#statement) | MQ1 and MQ7--MQ8 with its true integer canonical residuals, all non-phi vanishing, exact shared8Z high square-image iff and 2^(d-3A) fiber over a fixed T_2 modulo8. |
| dependency | [Actual final coupled-map proof](Yin_C_G0675_v1.md#argument) | MQ5 and MQ7, actual canonical quotients, all other primaries, first-residual stability and exact final correction/count; no independent a/c coordinates. |
| support | [Complete canonical original input](Yin_C_G0667_v1.md#statement) | Application only: normalized a=2m/Y_0, full forward divisibilities, old support, paid degree margin and original maximal q/layer/gap data, unchanged by these integer corrections. |
| support | [Both adopted canonical families](Yin_C_G0668_v2.md#statement) | Application only through their C667 polynomial input at actual q>=256; no equality of synthetic G_int with actual G_can or original characteristic-zero realization follows. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:15 |
| status | proved |
| reason | The complete fixed HP1--HP24 statement and six-section argument were directly read, followed by all of fresh isolated R907. Adopt actual simultaneous same-polynomial solutions of both canonical residuals modulo8 for every stated normalized input and every dyadic q>=256, for each separately chosen sign, with exact final fiber and unchanged degree, reduction and paid canonical costs. C683 is now actually proved at its linked decision; the registration-time pending description is historical. No higher precision, characteristic-zero residual identity, spectral realization, G_int=G_can or original Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual simultaneous theorem](#statement) | HP1--HP5, all normalized hypotheses, actual integer factorized input and q>=256, either separately chosen sign, bounded monic same-reduction T, both residuals modulo8, exact final fiber and unchanged original costs. |
| argument | [Whole power-preserving construction](#argument) | HP6--HP24 and HP2--HP7, actual half-remainder and q/2 CRT, distinct integer lift with full canonical carry, coefficient-subring and derivative lemmas, specified fourth-power residue lifts, all-primary high condition and final shared correction. |
| dependency | [Adopted structured base and low error](Yin_C_G0683_v1.md#decision-whole-reviewed-2026-10-24) | Actual adopted dependency: FP2--FP4 actual K_b^q/W_b^(q/2), full eta and both sign remainders, initial low square image; FP6 full actual first-correction carry, rechecked here for the different integer lift. C683 is proved by its actual 2026-10-24T04:04 decision; its unchanged mathematical scope is used here. |
| dependency | [Exact first quarter](Yin_C_G0603_v1.md#statement) | FE4 actual first-quarter formula with the genuine L_F/M_F and divisor term; the stronger q/2-th-power remainder and full-precision correction target are proved here. |
| dependency | [First actual correction](Yin_C_G0677_v1.md#statement) | HC2--HC8 for every bounded integer representative, same-W modulo4 preservation and exact first modulo8 solution; strengthened global CRT and actual power lift are established here. |
| dependency | [Specified complete low correction](Yin_C_G0680_v1.md#statement) | LR1--LR7 with its exact V/M integer lifts, actual first-restoration and low-quarter formula; the fourth-power choices and derivative preservation are proved here, rather than changing that family. |
| dependency | [Actual low-correction proof](Yin_C_G0680_v1.md#argument) | LR3--LR4 complete canonical-divisor and actual C2/C3/C5 calculations, applicable to the specified HP20 lifts without alteration. |
| dependency | [All-primary final correction and fibers](Yin_C_G0675_v1.md#statement) | MQ1 and MQ7--MQ8 with its true integer canonical residuals, all non-phi vanishing, exact shared8Z high square-image iff and 2^(d-3A) fiber over a fixed T_2 modulo8. |
| dependency | [Actual final coupled-map proof](Yin_C_G0675_v1.md#argument) | MQ5 and MQ7, actual canonical quotients, all other primaries, first-residual stability and exact final correction/count; no independent a/c coordinates. |
| support | [Complete canonical original input](Yin_C_G0667_v1.md#statement) | Application only: normalized a=2m/Y_0, full forward divisibilities, old support, paid degree margin and original maximal q/layer/gap data, unchanged by these integer corrections. |
| support | [Both adopted canonical families](Yin_C_G0668_v2.md#statement) | Application only through their C667 polynomial input at actual q>=256; no equality of synthetic G_int with actual G_can or original characteristic-zero realization follows. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0907_v1.md#whole-high-power-simultaneous-mod-eight-finding) | Entire actual high-power construction, full M_F power and integer first lift, all coefficient subrings and monic division, exact prescribed corrections and derivative lemma, all-primary shared correction and complete final fiber. |
