---
author: Yin
---
# Exact low second-error elimination preserving the first modulo-eight residual

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed varying W by Phi^(3A/2)V and restoring the first quarter with the adopted C677 high K correction, together with a stronger low-X condition to control the actual C5 composition.
Same_trace checked that bounded construction and derived the entire change of the second quarter below phi^(4A), including its genuine canonical-divisor carry.
The resulting full low-image and finite-family elimination below are author mathematics, not independent review.
Focused reuse inspected the full C677 correction and C675 actual quotient representatives, and reused C603 FE11 and C202's final8V boundary.
No native calculation, degree scan or external source theorem is used.

The [D1 low second-error section](../drafts/Yin_D_G0001.md#first-fixed-low-second-obstruction) is development provenance, not a logical input.
This complete theorem is initially open for fresh isolated whole mathematical review.

## Statement

### LR1: full input, exact deformation and statement

Let A>=2 be EVEN, Phi=X^2+X+1 over Z, phi=Phi mod2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic square prime to Xphi, with Y|Y(chi) and Y|Y(X^3+X).
Put H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A, and C_0=X^A Y(chi)Psi^(7A).
Assume H_0^6=C_0^21 modulo phi^(4A) and h>=17A.
Use fixed monic integer lifts P_psi of all irreducibles of H_0, with P_X=X and full even exponents N_psi, and set

    mathcal_H=product P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product psi^(N_psi/2), j_H=h/2,
    S=product P_psi^(N_psi/2)Phi^(7A/2),
    P=Phi^A K, T=S^2+2P+4W.

Fix s in{1,-1}, choose K,W in Z[X] with degK<d-2A and degW<d, and write k=Kbar,w=Wbar.
Assume

    k^11=H_0C_0^2 modulo phi^(4A), J_H|k,
    [X^i]k=0 for odd A/2<=i<3A/2,
    F(T)=0 modulo8, X_s(T)=0 modulo4.                  (LR1)

Here for every actual monic divisor T,

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,

    a(T)=rem_T(T(X^2-2))/2,
    b(T)=rem_T(T(X^3-3X))/3,
    c(T)=rem_T(T(X^5-5X^3+5X))/5,
    F(T)=rem_T(2c(T)^2-3a(T)^5),
    X_s(T)=rem_T(b(T)^2-a(T)^3
                         +s(c(T)^3-2b(T)^5)).

All residual congruences are coefficientwise congruences of the canonical integer remainders.
Adopted C677 constructs such starting pairs for these inputs because h>=17A implies its required14A margin.
Set

    O=(X_s(T)/4)bar in B_phi=F_2[X]/phi^(7A),
    A_F=C_0^2+phi^(4A)k^8w^2,
    e=3A/2, f=5A/2, n_V=h+11A, t_L=(h-17A)/2.         (LR2)

For EVERY v in F_2[X] of degree<n_V, take its coefficient0/1 integer lift V.
Choose ANY ell of degree<h+4A satisfying

    ell=[phi^(3A)k^9v^2+phi^(5A/2)k^10v]/A_F
                                            modulo phi^(5A),
    ell=0 modulo J_H X^(5A/2).                         (LR3)

The target in the first congruence is well-defined at precision5A.
Such ell exist, with exactly2^t_L choices for each v.
Each ell is divisible by phi^f and by X^(3A).
Let M be the coefficient0/1 lift of ell/phi^f and choose the SPECIFIED integer lift L=Phi^f M.
Then define

    D=Phi^e V, Q=Phi^(5A)L=Phi^(15A/2)M,
    W_new=W+D, K_new=K+Phi^(4A)L,
    T_new=T+2Q+4D.                                    (LR4)

Write k_new=K_newbar.
All degrees remain below the original bounds; T_new is monic of the SAME degree d.
Every such T_new satisfies F(T_new)=0 modulo8 and X_s(T_new)=0 modulo4.
With O_new=(X_s(T_new)/4)bar, the full LOW variation is

    O_new+O=phi^A(k^5/H_0)v^2 modulo phi^(4A).          (LR5)

The coefficient k^5/H_0 is a square unit modulo phi^(4A).
Consequently the EXACT variation image, as all v and ell above range, is

    I_low=phi^A Fr(F_2[X]/phi^(4A)),
    dim_F2 I_low=3A.                                  (LR6)

Here Fr denotes the image of squaring.
This equals the set of square classes divisible by phi^A in that ring.
It is generally a proper subspace, and the quotient of F_2[X]/phi^(4A) by I_low has dimension5A.

There exists a pair in LR3--LR4 with O_new=0 modulo phi^(4A) if and only if

    [O mod phi^(4A)]=0 in
              (F_2[X]/phi^(4A))/I_low.                (LR7)

Equivalently O is divisible by phi^A and O/phi^A is a square modulo phi^(3A).
When LR7 holds, there are precisely2^(h+8A) choices of v and2^t_L choices of ell for each, hence

    2^((3h-A)/2) distinct T_new modulo8                (LR8)

in this explicitly lifted family with F=0 modulo8 and O_new=0 modulo phi^(4A).
If LR7 fails, there are none.
The full family has2^(n_V+t_L) distinct T_new modulo8; these counts use the specified coefficient lifts V,M and do not count extra integer presentations twice.
The invariant LR7 is unchanged by this whole family and by any further T_new+8Z.
Its vanishing alone does NOT solve the full second residual modulo8: the remaining quotient O_new/(phi^(4A)k_new^4) must still be a square modulo phi^(3A), as in C675.

## Argument

### LR2: first-error restoration, bounded CRT and original degrees

The change W->W+Phi^e V preserves the C669 equation w^2=eta_s(K) modulo phi^(3A).
C603 FE11 gives its complete first-quarter change

    delta O_F=phi^(5A)k^9v^2/H_0
                    +phi^(9A/2)k^10v/H_0.

The new A_F equals the old one in B_phi because its difference is phi^(7A)k^8v^2.
Thus C677 HC6 restores O_F=0 exactly by LR3.
The stronger low modulus in LR3 includes J_H X^A, so C677 preserves the complete modulo4 eta with the same new W, not just its solvability.
This proves both stated residual congruences on all primary components.

The CRT moduli in LR3 are coprime and their product has degree

    10A+j_H+5A/2=j_H+25A/2<=h+4A.

The inequality is exactly h>=17A.
Therefore there are2^((h+4A)-(j_H+25A/2))=2^t_L solutions ell with the stated bound.
The high target is divisible by phi^f, and the modulus phi^(5A) is also, so every ell is divisible by phi^f as a POLYNOMIAL.
Since J_H contains X^(A/2), the low condition gives X^(3A)|ell.
As phi(0)=1, it follows that X^(3A)|(ell/phi^f).
Consequently the chosen M is divisible by X^(3A) over Z.
The structured lift L=Phi^f M has precisely reduction ell and degree<h+4A.
It gives deg(K_new)<h+12A=d-2A.
Also degD<3A+n_V=d, so degW_new<d.
All auxiliary half-integer-looking exponents are integers because A is even.

### LR3: polynomial representatives and the genuine divisor carry

Use the actual polynomial representatives from C675:

    Xi=Delta(P)+P^2+W(C_2)-2PDelta(S)+Delta(S)^2,
    A_rep=P^2+2Xi,
    C_rep=5Phi^(2A)C+2P(C_5)+4(W(C_5)+R_5),

where Delta(B)=(B(C_2)-B^2)/2, chi_0=X Phi^2,
C=X^A mathcal_Y(chi_0)Phi(chi_0)^(7A), and
R_5=S(chi_0)E_5S'(chi_0)+E_5^2S'(chi_0)^2 with E_5=(C_5-chi_0)/2.
The fixed actual integer quotient in S(C_3)=Q_3S+2E_3 defines B_3=P(C_3)-Q_3^2P.
Thus an explicit integer polynomial representing the second residual modulo8 is

    N=4B_3^2-A_rep^3+s C_rep^3.                        (LR9)

The ignored term2b^5 is zero modulo8 by C675.
All these are actual global polynomials; no localized congruence is composed with C_5.

Perform the actual monic division N=Q_N T+R_N.
The canonical remainder R_N is congruent to X_s(T) modulo8, hence is coefficientwise divisible by4.
Reduction modulo2 gives

    Q_Nbar U=Nbar=phi^(6A)(k^6+C_0^3).

C669's root/support consequence gives phi^(4A)|(k^6+C_0^3).
Polynomial cancellation therefore proves

    ord_phi Q_Nbar>=3A.                               (LR10)

To compare different divisors, work over the localization where mathcal_H is a unit.
Put a_0=A/2 and u=1+2Phi^(a_0)M/mathcal_H.
Using the EXACT polynomial identity T=mathcal_H Phi^(7A)+2Phi^A K+4W gives

    T_new=uT+4D_eff-8Phi^(a_0)WM/mathcal_H,
    D_eff=Phi^e(V-KM/mathcal_H).                       (LR11)

The factor u is a unit modulo8.
In the quotient by T_new, the contribution from the old polynomial N is consequently R_N-4u^(-1)Q_N D_eff modulo8.
Its divided change has phi-order at least3A+e=9A/2>4A, by LR10.
Thus the old canonical remainder contributes O unchanged BELOW phi^(4A).
This explicitly accounts for the changing-divisor carry; replacing T by T_new without this calculation would not be valid.

### LR4: actual composed changes and the low second-quarter formula

Keep the representatives in LR9 and denote their new-minus-old changes by delta.
The C3 quotient Q_3 and C5 polynomial R_5 are fixed because S is fixed.
Since Q=Phi^(15A/2)M, both Qbar and Q(C_3)bar are divisible by phi^(15A/2).
For the latter, use the actual polynomial divisibility phi|phi(X^3+X).
It follows that4delta(B_3^2)=0 modulo8 in the phi quotient.

For C5, the actual change is

    delta C_rep=2Q(C_5)+4D(C_5).

The chosen M has X^(3A) as an INTEGER factor, and C_5 modulo2 is chi of phi-order2.
Therefore Q(C_5)bar is divisible by phi^(6A).
Write its actual monic division as Q(C_5)=Phi^(6A)R+2E with an even remainder.
The cube difference is

    delta(C_rep^3)=6Phi^(4A)C^2 Q(C_5)
        +4Phi^(4A)C^2 D(C_5)
        +4 C_rep Q(C_5)^2 modulo8.

Here C_rep^2=Phi^(4A)C^2 modulo4.
In the first term, the part containing2E is already a multiple of4Phi^(4A), while the Phi^(6A)R part has6Phi^(10A), which becomes a multiple of4Phi^(4A) after the SAME T_new relation.
The second term has that form directly.
The third has zero reduction after its factor4 because its phi-order is at least2A+12A>=7A.
Thus the C5 contribution to the quarter has order at least4A.
The low-X condition, not a composition of a local phi congruence, is what proves this.

For the dyadic representative, direct use of Delta(P+Q)=Delta(P)+Delta(Q)-PQ gives the EXACT change

    delta A_rep=Q(C_2)+2Q^2+2D(C_2)
                               +4PQ-4QDelta(S).

In the quotient modulo8 by T_new the last two terms vanish, since their factors after4 have phi-order at least7A.
Also2Q^2=0 there: Q^2 has Phi^(15A), and Phi^(14A) becomes4Phi^(2A)K_new^2/mathcal_H^2.
Expand Phi(C_2)=Phi^2+2Delta(Phi).
Every correction term beyond Phi^(15A) in Q(C_2) vanishes modulo8: the first has an even coefficient and phi-power15A-2, and all later surviving coefficients have factor4 and power at least15A-4.
Two applications, or one application after that even coefficient, of the actual divisor relation justify these bounds for EVERY A>=2.
The remaining identity is

    Q(C_2)=4Phi^(3A)K_new^2 M(C_2)/mathcal_H^2
                                                    modulo8.

Consequently delta A_rep is even, its square contributes nothing to the cube change at this precision, and A_rep^2=P^4 modulo4 gives

    delta(A_rep^3)=6Phi^(4A)K^4 D(C_2) modulo8.

More explicitly, the quadratic cube term is4 A_rep D(C_2)^2, whose reduction after4 has order2A+6A>=7A.
Now expand D(C_2) modulo4:

    D(C_2)=Phi^(3A)V(C_2)
            +2e Phi^(3A-2)Delta(Phi)V(C_2) modulo4.

The second summand contributes to the divided cube only from order7A-2>=4A.
In the first, reducing6Phi^(7A) using T_new gives

    delta(A_rep^3)/4
           =phi^A k^4 k_new v^2/H_0 modulo phi^(4A).

Since k_new=k modulo phi^(4A), this is phi^A k^5v^2/H_0.
Combining this with the C3/C5 calculations and the genuine divisor carry LR11 proves LR5, including its actual canonical coefficient interpretation.
Both s=1 and s=-1 give the same variation after reducing the legitimate quarter modulo2.

### LR5: exact image, invariant, reconstruction and counts

Differentiate k^11=H_0C_0^2 modulo phi^(4A).
The modulus has zero derivative and H_0 is a square, so k'=0 there.
Thus k^5/H_0 is a square unit in that even-precision ring.
As v ranges over polynomials of degree<n_V, its residues modulo phi^(3A/2) range freely, since n_V>=3A.
The map v->phi^A(k^5/H_0)v^2 consequently has rank3A and kernel precisely v divisible by phi^(3A/2).
This proves the full image LR6 and all directions have globally bounded representatives.
The ambient ring modulo phi^(4A) has dimension8A, giving the quotient dimension5A.

Therefore LR7 is necessary and sufficient for removing the complete low quarter while restoring F modulo8.
If it holds, solve

    v^2=H_0 O/(phi^A k^5) modulo phi^(3A)

and choose a polynomial representative of degree<3A; LR3 then supplies its globally admissible retuning ell.
Every solution v has2^(n_V-3A)=2^(h+8A) representatives of degree<n_V.
Each such v has2^t_L allowed ell, proving the number in LR8.

The specified lifts ensure these pairs give DISTINCT T_new modulo8.
Different ell have different T_new modulo4, since their difference divided by2 is phi^(5A) times a nonzero polynomial of degree making the product<d.
For fixed ell the chosen M and L are fixed; different v then change T_new by4Phi^e times a nonzero reduction of degree<d.
The total family size is therefore2^(n_V+t_L), with no duplication.
No count of unrestricted alternate integer lifts of L is intended.

Adopted C202 shows a further8Z changes O_X only in phi^(4A)Fr(B_phi), while keeping F unchanged here.
It cannot alter LR7.
Passing LR7 leaves the high square-image test from C675 genuinely unresolved; it does not prove full second-residual modulo8 solvability.

### LR6: paid canonical applications and remaining question

For the paid C667 representative, degY_0>=45L_0>360m.
Thus at every actual q>=2, A=2mq and h=q(2m+degY_0) satisfy h>=17A, which only requires degY_0>=32m.
No additional support or original degree is introduced.
The same d=q(30m+degY_0), actual maximal q, characteristic-two canonical R, integer layer weight12mq and strict canonical gap q(5m-Q-5degH) remain unchanged.

The new invariant has not been proved zero or nonzero on every C677 starting base.
Its nonzero value would exclude all deformations LR3--LR4 and all subsequent8Z above them; it would not exclude every possible K,W outside that stated family.
When it vanishes the complete low part can be removed with the exact count above, but the high square-image obstruction remains.
Neither synthetic G_int=actual G_can, characteristic-zero residual equations, irreducibility, total reality, an original realization nor Task completion is asserted.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:23 |
| status | open |
| reason | Register the full declared first-preserving coefficient deformation, exact low second-quarter change with actual C2/C3/C5 and canonical-divisor carry, complete3A-dimensional image,5A-dimensional quotient invariant, bounded global reconstruction and finite distinct-class counts. The invariant's value on canonical starting bases and the higher square-image test remain open. No native computation or original realization is asserted. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire low-image and elimination theorem](#statement) | LR1--LR8, every stated square input and actual starting T, h>=17A, the full bounded v/ell family with specified integer lifts, both preserved residual congruences, exact low image, existential iff and all counts/limits. |
| argument | [Whole actual change and reconstruction](#argument) | LR9--LR11 and all LR2--LR6 sections, complete first retuning, global degree/CRT, actual residual representative and monic quotient, unit-adjusted divisor carry, genuine C2/C3/C5 composition, every order bound, image/kernel/fiber and original costs. |
| dependency | [Adopted exact first correction](Yin_C_G0677_v1.md#statement) | Nonempty stronger-root F8/X4 bases and HC6 complete K variation with same-W eta preservation; used with the stronger low constraint and checked h>=17A CRT. |
| dependency | [Actual first-quarter W variation](Yin_C_G0603_v1.md#argument) | FE11 at the same T and W increment Phi^(3A/2)V, retaining both quadratic and linear terms before the high K retuning. |
| dependency | [Adopted complete actual quotient representatives](Yin_C_G0675_v1.md#argument) | MQ9--MQ13 actual A_rep/C_rep/B_3 and all-primary setup, plus the remaining exact high square-image boundary; no local congruence is composed with C5. |
| dependency | [Actual root/support consequence](Yin_C_G0669_v1.md#statement) | Kbar^6=C_0^3 modulo phi^(4A), complete eta and all-primary modulo4 criterion; supplies the exact quotient-order bound and initial W preservation. |
| support | [Final same-input8Z boundary](Yin_C_G0202_v1.md#coupled-layer-statement) | Final correction cannot change the low invariant; its entire full mod8 criterion is not assumed solved by low elimination. |
| support | [Paid canonical representatives and costs](Yin_C_G0667_v1.md#statement) | Application only: existing degY_0>=45L_0>360m, actual q and degree/layer/canonical identities; no additional support, degree or original realization. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:38 |
| status | proved |
| reason | The entire fixed LR1--LR11 statement and all LR2--LR6 argument sections were read directly, together with the complete fresh isolated R901. Adopt the exact first-preserving low second-quarter elimination, full actual polynomial and canonical-divisor carry, globally realized3A-dimensional image and5A-dimensional quotient invariant, precise iff and all distinct coefficient counts with the specified integer lifts. The invariant is not yet evaluated on all canonical starting bases, and the high square-image test and original realization remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire low-image and elimination theorem](#statement) | LR1--LR8, every stated square input and actual starting T, h>=17A, the full bounded v/ell family with specified integer lifts, both preserved residual congruences, exact low image, existential iff and all counts/limits. |
| argument | [Whole actual change and reconstruction](#argument) | LR9--LR11 and all LR2--LR6 sections, complete first retuning, global degree/CRT, actual residual representative and monic quotient, unit-adjusted divisor carry, genuine C2/C3/C5 composition, every order bound, image/kernel/fiber and original costs. |
| dependency | [Adopted exact first correction](Yin_C_G0677_v1.md#statement) | Nonempty stronger-root F8/X4 bases and HC6 complete K variation with same-W eta preservation; used with the stronger low constraint and checked h>=17A CRT. |
| dependency | [Actual first-quarter W variation](Yin_C_G0603_v1.md#argument) | FE11 at the same T and W increment Phi^(3A/2)V, retaining both quadratic and linear terms before the high K retuning. |
| dependency | [Adopted complete actual quotient representatives](Yin_C_G0675_v1.md#argument) | MQ9--MQ13 actual A_rep/C_rep/B_3 and all-primary setup, plus the remaining exact high square-image boundary; no local congruence is composed with C5. |
| dependency | [Actual root/support consequence](Yin_C_G0669_v1.md#statement) | Kbar^6=C_0^3 modulo phi^(4A), complete eta and all-primary modulo4 criterion; supplies the exact quotient-order bound and initial W preservation. |
| support | [Final same-input8Z boundary](Yin_C_G0202_v1.md#coupled-layer-statement) | Final correction cannot change the low invariant; its entire full mod8 criterion is not assumed solved by low elimination. |
| support | [Paid canonical representatives and costs](Yin_C_G0667_v1.md#statement) | Application only: existing degY_0>=45L_0>360m, actual q and degree/layer/canonical identities; no additional support, degree or original realization. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0901_v1.md#whole-first-preserving-low-elimination-finding) | Entire fixed target, all actual quotient/composition/carry steps, every parameter and endpoint, exact image/fibers and canonical costs; the main agent read the complete finding before adoption. |
