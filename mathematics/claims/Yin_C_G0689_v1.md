---
author: Yin
---
# Complete modulo-sixteen lifting obstruction above a same-polynomial modulo-eight class

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root requested testing the actual next residual precision without treating large q as automatic success.
Same_trace derived the complete next first-error image, its explicit finite inverse, the remaining true second-error and composition map, and the all-coefficient-lift criterion and count below.
This is author mathematics, not independent review.
Focused reuse read adopted C686 and its whole R907, C202's exact changing-divisor proof, and the adopted C675/C677/C680 actual same-polynomial interfaces.
C202 only states its modulo4-to-modulo8 layer; the necessary new integer halves, both canonical quotient terms, proper derivative image and complete modulo16 elimination are proved here.
No native computation, coefficient enumeration, external source theorem or claim of a passing modulo16 input is used.

The [D1 modulo-sixteen section](../drafts/Yin_D_G0001.md#complete-mod-sixteen-fiber-obstruction) is development provenance, not a logical input.
This entire theorem is initially open for fresh isolated whole review.

## Statement

### SX1: complete actual input and exact all-lift criterion

Let A be a positive multiple of4, phi=X^2+X+1 over F_2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic square prime to Xphi, with Y|Y(chi) and Y|Y(X^3+X).
Set H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A and C_0=X^A Y(chi)Psi^(7A).
Assume H_0^6=C_0^21 modulo phi^(4A) and h>=17A.
For all irreducibles of H_0 choose monic integer lifts P_psi with P_X=X and retain every full even exponent N_psi.
Put

    mathcal_H=product P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product psi^(N_psi/2), J_H^2=H_0,
    Phi=X^2+X+1 over Z,
    S=product P_psi^(N_psi/2)Phi^(7A/2),
    P=Phi^A K, T=S^2+2P+4W.                          (SX1)

Choose actual integer K,W with degK<d-2A, degW<d, and suppose

    k=Kbar, k^11=H_0C_0^2 modulo phi^(4A),
    J_H|k, [X^i]k=0 for odd A/2<=i<3A/2.              (SX2)

Fix s in{1,-1}.
For each actual monic divisor T define

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T(T(C_2))/2,
    b=rem_T(T(C_3))/3, c=rem_T(T(C_5))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)).

Assume coefficientwise F(T)=X_s(T)=0 modulo8.
C686 supplies such actual inputs in its q>=256 range.
Let

    B=F_2[X]/U, B_H=F_2[X]/H_0,
    B_phi=F_2[X]/phi^(7A),
    E_F=(F(T)/8)bar, E_X=(X_s(T)/8)bar.              (SX3)

All divisions by8 take place on the ACTUAL integer canonical coefficients before reduction.
We classify ALL monic coefficient classes T_new modulo32 with T_new=T modulo8 for which both residuals vanish modulo16.
No earlier coefficient class modulo8 is changed in this theorem.

First require

    E_F=0 in B_H,
    E_F in phi^(9A/2) B_phi.                          (SX4)

If SX4 fails, no such T_new exists.
If it holds, in R=F_2[X]/phi^(5A/2) define

    r=H_0 E_F/(phi^(9A/2)k^10),
    t=phi^(A/2)/k,
    u=r+t r^2+t^3 r^4.                               (SX5)

The factor phi^(9A/2) is divided out exactly using SX4, at the indicated quotient precision; the remaining powers of k are units.
Choose the representative u_0 of degree<5A and its coefficient0/1 integer lift U_0, and set

    V_0=Phi^(3A/2)U_0, T'=T+8V_0.                    (SX6)

Then degV_0<8A<d, F(T')=0 modulo16, and X_s(T')=0 modulo8.
Let E'_X=(X_s(T')/8)bar be its actual next error.
The remaining complete criterion is

    E'_X=0 in B_H,
    E'_X=0 modulo phi^(4A),                           (SX7)

followed, if SX7 holds, by

    e=E'_X/(phi^(4A)k^4) in F_2[X]/phi^(3A),
    Omega=C_0^2Psi^(4A)/k^4,
    e' in Omega phi^2 span_F2{chi^(2j):
                                  0<=j<3A/4}.        (SX8)

Here the prime is ordinary differentiation in the even-precision quotient.
The displayed span is a proper space of dimension3A/4.
Thus SX4, SX7 and SX8 are NECESSARY AND SUFFICIENT for a simultaneous modulo16 solution above the fixed T modulo8.
They do not assert that the constructed C686 inputs pass them automatically.
The criterion is independent of the permitted representative choices in SX5--SX6 in the translated sense proved below.

When these conditions hold, the EXACT number of such monic coefficient classes modulo32 is

    2^(2d-47A/4).                                    (SX9)

Otherwise it is zero.
The count is for one fixed sign and one fixed T modulo8, including ALL its lifts, not only a chosen low-dimensional correction family.
It retains all primary components, even where their next errors are unchangeable.

## Argument

### SX2: all modulo-eight-preserving lifts and the first next-error map

Use the canonical polynomials alpha=a mod2 and gamma=c mod2, each of degree<d.
C675 gives globally

    bbar=0, alpha=rem_U(phi^(2A)k^2),
    gamma=rem_U(phi^(2A)C_0),
    alpha=gamma=0 in B_H.                            (SX10)

At phi, alpha=phi^(2A)k^2 and gamma=phi^(2A)C_0.
In particular alpha^4=0 in B.
The root and old support also imply k^6=C_0^3 modulo phi^(4A): the eleventh power of k^6/C_0^3 is H_0^6/C_0^21=1, and the eleventh-power map is injective on this finite unit group, whose order has only prime factors2 and3.

For any integer V with degV<d put T_V=T+8V and v=Vbar.
C202's exact identity gives

    a(T_V)=a+4H_V,
    H_V=rem_(T_V)(V(C_2)-V Q_2),
    T(C_2)=T Q_2+2a.                                 (SX11)

Thus H_Vbar=v^2 in B.
The odd divided remainders change by multiples of8.
The actual modulo8 change of X_s is4alpha^2v^2, while F remains zero modulo8 because alpha^4=0.
Consequently precisely the v in

    K_8={v:alpha^2v^2=0}
       ={v:phi^(3A/2) divides v as a polynomial}      (SX12)

preserve both residuals modulo8.
The last equality uses the canonical degree<d representative; there is no restriction on the H_0 components.
Their dimension is d-3A.

Perform the ACTUAL integer divisions

    2c^2-3a^5=T Q_F+F(T),
    a^4=T Q_4+2R_4.                                  (SX13)

The second remainder is even by alpha^4=0.
On changing T to T_V, the first old numerator contributes F(T)-8Q_F V.
The odd quotient change contributes zero to F modulo16.
The dyadic fifth-power change is -60a^4H_V=4a^4H_V modulo16.
Use the second division in SX13 in the SAME new quotient: a^4=2R_4-8VQ_4.
Hence the legitimate next error changes by

    E_F(T_V)+E_F=R_4bar v^2+Q_Fbar v in B.            (SX14)

This contains the actual canonical-divisor carry Q_Fbar v.

At phi the C675 actual representative a=P^2+2Xi modulo4 gives a^4=Phi^(8A)K^8 modulo4.
The actual T relation then gives

    R_4bar=phi^(2A)k^9/H_0 in B_phi.                  (SX15)

Indeed Phi^(8A)=-2Phi^(2A)K/mathcal_H modulo4, and the monic coefficient half is legitimate before reduction.
On B_H, a is even in the localized free module, so R_4bar=0 there.
Reduction of the first division SX13 gives the polynomial identity U Q_Fbar=alpha^5.
Write alpha=phi^(2A)k^2+U q_a.
In the quotient at phi, the binomial expansion of alpha^5/U leaves only phi^(3A)k^10/H_0; its other possibly surviving term has factor phi^(8A).
On B_H, H_0 divides alpha as a polynomial, so H_0^4 divides Q_Fbar.
Therefore SX14 is zero on B_H and equals

    Psi_F(v)=phi^(2A)k^9v^2/H_0
                     +phi^(3A)k^10v/H_0 in B_phi.    (SX16)

For v=phi^(3A/2)u this becomes

    Psi_F(v)=phi^(9A/2)k^10/H_0 * (u+t u^2),
    t=phi^(A/2)/k.                                   (SX17)

In R from SX5 the additive operator N(u)=t u^2 satisfies N^3=0, since N^3(u)=t^7u^8 has phi-order at least7A/2>5A/2.
Thus I+N has the explicit inverse I+N+N^2.
This proves SX5, and shows the COMPLETE first-error image on K_8 is

    phi^(9A/2) B_phi, of dimension5A,                (SX18)

with kernel precisely the global polynomial multiples of phi^(4A), unrestricted on B_H.
This proves necessity and sufficiency of SX4 for solving F modulo16 while retaining both residuals modulo8.
It also proves SX6 without an iterative coefficient search.

### SX3: the final shared16W map

For an integer Z with degZ<d, the exact changing-divisor formula applied to T+16Z gives a change8rem_U(z^2) modulo16 in a.
The odd divided remainders and divisor modulo16 are unchanged.
Thus, for any actual full modulo8 base under SX1--SX2,

    E_F(T+16Z)=E_F,
    E_X(T+16Z)=E_X+alpha^2 z^2.                       (SX19)

The first equality uses alpha^4=0.
The second image is zero on B_H and exactly

    I_high=phi^(4A)k^4 Fr(B_phi), dim_F2 I_high=3A      (SX20)

on B_phi.
Every nonempty fiber has2^(d-3A) possible degree<d reductions z.
In particular no highest correction16Z can repair the first next error or any second error outside this actual square image.
This is the precise next-layer specialization of the changing-divisor proof, not a presumption that C202 had already asserted modulo16.

### SX4: the full remaining8Phi^(4A)M change of the second error

After SX6, every other first-residual modulo16 class above T modulo8 differs from T' by8Phi^(4A)M modulo16, by the exact kernel in SX18.
Take any integer M of degree<d-8A and write m=Mbar, V=Phi^(4A)M and T''=T'+8V.
Its degree remains d and it preserves both old modulo8 equations and F modulo16.
The actual K is unchanged and W changes by an even polynomial; hence all reduced input data in SX2 and SX10 are unchanged.

In this paragraph all a,b,c,Q_2 refer to T'.
Define the ACTUAL quotients

    T'(C_5)=T' Q_5+5c,
    b^2-a^3+s(c^3-2b^5)=T' Q_X+X_s(T'),
    Delta(T')=(T'(C_2)-T'^2)/2=T' Q_D+a.

Thus Q_2=T'+2Q_D exactly.
Equation SX11 and reduction modulo4 allow H_V to be computed with divisor T', since T''=T' modulo8.
The odd quotient has the exact change c(T'')=c+8J_5, with

    J_5bar=rem_U(v(chi)-v Q_5bar).                    (SX21)

To justify integrality here, the exact remainder identity gives

    5(c(T'')-c)=8rem_(T'')(V(C_5)-VQ_5).

The left side is integral and5 is coprime to8, so c(T'')-c is divisible by8 and that remainder is divisible by5.
Its reduction gives SX21.
The same argument applies to b, whose square and fifth-power contributions have zero change modulo16.

Expansion of the actual cube terms, including the old canonical quotient Q_X, yields

    E_X(T'')+E'_X
      =(rem_(T')(a^2H_V)/2)bar
                     +gamma^2 J_5bar+Q_Xbar v.        (SX22)

The first canonical remainder is even because alpha^2v^2=0.
The coefficient is correct: -12 times that even remainder divided by8 reduces to its half modulo2.
Every quadratic and higher dyadic cube term is divisible by16.
Since T''=T' modulo8, computing that half modulo2 with the old divisor modulo4 is legitimate.
The last term in SX22 is the genuine changing-divisor contribution.

On B_H the first summand is zero, since a is even there and a^2 is divisible by4.
The other two are zero: gamma=0 there, and U Q_Xbar=alpha^3+gamma^3 is divisible by H_0^3, giving H_0^2|Q_Xbar.
Therefore the entire second-error variation is zero on B_H.

At phi, Phi(C_2)^(4A)=Phi^(8A) modulo4.
Using Q_2=T'+2Q_D and the SAME actual divisor relation gives

    H_V=-2Phi^(2A)K M(C_2)/mathcal_H
                     -2Phi^(4A)M Q_D modulo4.

After multiplication by a^2 and the legitimate half,

    (rem_(T')(a^2H_V)/2)bar
                       =phi^(6A)k^5 m^2/H_0 in B_phi. (SX23)

The other term has factor phi^(8A) and vanishes only after this half.

It remains to combine Q_Xbar with the quotient term in SX21.
The exact polynomial identities are

    phi^(2A)k^2=alpha+U q_a,
    phi^(2A)C_0=gamma+U Q_5bar,
    U Q_Xbar=alpha^3+gamma^3.

Expanding the cubes before reduction shows

    Q_Xbar+gamma^2Q_5bar
      =phi^(6A)(k^6+C_0^3)/U
                          +phi^(4A)k^4q_a in B_phi.  (SX24)

The quotient in the first term is polynomial: the old support/root gives phi^(4A)|(k^6+C_0^3), while J_H|k and H_0|C_0 give H_0|(k^6+C_0^3).
Here H_0|C_0 is the full forward divisibility in the input, and H_0 is prime to phi.
The displayed right side has phi-order at least3A.
Multiplication by v=phi^(4A)m therefore gives zero in B_phi.
Substitute into SX21--SX23 to obtain the FULL remaining change

    E_X(T'')+E'_X
       =phi^(6A)k^5m^2/H_0
                     +phi^(4A)C_0^2Psi^(4A)m(chi)
                                                   in B_phi. (SX25)

No local phi congruence was composed with C_5.
The composition m(chi) comes from the global polynomial V(C_5) after reduction.
All components and genuine canonical quotient terms have now been accounted for.

### SX5: exact derivative image, all-lift sufficiency and count

The first term of SX25 lies in I_high.
Indeed differentiating k^11=H_0C_0^2 modulo phi^(4A) gives k'=0 there, because the modulus and H_0 are squares and k is a unit.
Thus k^5/H_0 is a square in that quotient, which more than covers the precision needed after the factor phi^(6A).
Consequently, modulo the exact final image I_high, SX25 is simply

    phi^(4A)C_0^2Psi^(4A)m(chi).                      (SX26)

It changes neither the B_H component nor the part below phi^(4A).
This proves the necessity of SX7 after the first correction.

Divide by phi^(4A)k^4 modulo phi^(3A).
The class changes by Omega m(chi) modulo squares.
The coefficient Omega is a square unit, so its derivative is zero.
Since chi'=phi^2, its derivative change is

    Omega phi^2 m'(chi)
      =Omega phi^2 sum_(j>=0) m_(2j+1)chi^(2j).        (SX27)

Only0<=j<3A/4 survive modulo phi^(3A).
Their phi-orders are respectively2+4j, all distinct and below3A, so they are linearly independent over F_2.
Every such coefficient of m can be prescribed, because degm<d-8A=h+6A is larger than3A/2.
The image is therefore EXACTLY the space in SX8, of dimension3A/4, not merely contained in it.

In F_2[X]/phi^(3A), derivative zero is equivalent to being a square: the modulus is a square, and the unique representative of degree<6A has derivative zero exactly when it uses only even powers of X.
Hence SX8 is both necessary and sufficient for choosing m so that the remaining high error lies in I_high.
The final16Z from SX19 then removes it completely, on all primary components.
This proves the full criterion.

For counting, choose the coefficient0/1 lift M for every m of degree<d-8A, then the coefficient0/1 lift Z for every z of degree<d.
The monic classes

    T'+8Phi^(4A)M+16Z modulo32                        (SX28)

are all distinct: different m already give distinct classes modulo16; for the same m, different z give distinct classes modulo32.
They exhaust all first-residual modulo16 classes above the fixed modulo8 solution, since SX18 supplies exactly the phi^(4A) kernel and arbitrary further16Z.
If SX7--SX8 hold, exactly2^(d-8A-3A/4) choices of m satisfy the derivative equation.
For each, the final square map has exactly2^(d-3A) choices of z.
Multiplication gives precisely SX9.
No independence or random distribution of the original errors is assumed.

A different first solution in SX6 changes E'_X by SX25 and by the image SX19.
Thus SX7 and the coset test in SX8 are unchanged; actual integer changes of the first lift by16Z only translate within I_high.
This establishes the stated representative invariance.

### SX6: applicability and the genuine remaining question

Every adopted C686 output at actual q>=256 satisfies the present hypotheses with A=2mq, including A divisible by4 and the paid degree margin.
Its complete support, actual maximal q where supplied, characteristic-two canonical remainder, integer layer weight and original canonical gap remain unchanged for all lifts in SX28.
The theorem evaluates the ENTIRE next finite lifting question above one fixed modulo8 coefficient class, rather than an arbitrary free choice of a,c or an enlarged support family.

The new first obstruction cannot be changed anywhere in B_H or below phi^(9A/2).
Once it passes, the second low part below phi^(4A), all its B_H components and a proper high derivative quotient remain.
No proof that these quantities vanish for a particular C686 construction, or that they obstruct every earlier choice of that construction, is supplied here.
Evaluating or controlling those actual error classes through the earlier K/W/Y choices is the next substantive question.
Large q and the modulo8 integer-derivative lemma do not themselves establish these new modulo16 conditions.
No full modulo16 example, characteristic-zero identity, new original branch exclusion, small Mahler bound or Task completion is inferred.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:26 |
| status | open |
| reason | Register the complete same-polynomial modulo16 criterion above a fixed full modulo8 coefficient class: exact first next-error image/rank5A and finite inverse, all unchanged primary/low errors, full second half and canonical quotient terms, exact derivative image/rank3A/4, complete remaining16Z square image and all-lift fiber2^(2d-47A/4). No claim that a particular C686 class passes the new invariants, or that all earlier choices fail, is made. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual all-lift criterion](#statement) | SX1--SX9, all factorized input/support/root/degree hypotheses, actual full modulo8 base, every monic lift modulo32 above its fixed modulo8 class, first-error test and explicit correction, all second-error tests, exact count and unresolved actual-input evaluation. |
| argument | [Complete next-layer elimination](#argument) | SX10--SX28 and SX2--SX6, actual new half-remainders, both canonical-divisor carries, complete C2/C5 composition, full first image and inverse, all non-phi components, precise remaining derivative image, exhaustion/uniqueness/count and representative invariance. |
| dependency | [Exact actual changing-divisor identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | CL5--CL6 and integer monic-division compatibility, reused as an exact identity; its modulo8 specialization is not presumed to prove the new modulo16 conclusion. |
| dependency | [Actual old residual correction](Yin_C_G0202_v1.md#coupled-error-map) | CL9--CL10 identifying precisely which8V preserve the actual two modulo8 residuals; specialized after the current all-primary alpha is checked. |
| dependency | [Square-input actual representatives](Yin_C_G0675_v1.md#argument) | MQ3--MQ5, global a=P^2+2Xi, actual c reduction and bbar=0, all non-phi reductions and canonical free-module interpretation; the next integer halves and modulo16 changes are proved here. |
| support | [Existing final square image](Yin_C_G0675_v1.md#statement) | MQ7--MQ8 give the previous-layer model; the16Z map and its exact rank are rederived here at the new actual precision, with no automatic lift presumed. |
| support | [Actual nonempty modulo8 input](Yin_C_G0686_v1.md#statement) | Application only: every adopted q>=256 construction supplies SX1--SX3 with original complete support, degree/gap/layer and maximal-q boundaries; it does not supply any vanishing of the new invariants. |
| support | [Complete prior construction](Yin_C_G0686_v1.md#argument) | HP2--HP7 match the actual T form, stronger root, global J_H and low coefficient constraints and unchanged degree; no stronger derivative or residual precision is imported. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:43 |
| status | proved |
| reason | The complete fixed SX1--SX28 statement and five-section argument were directly read, followed by all of fresh isolated R912. Adopt the complete next-layer iff above a fixed actual modulo8 coefficient class: actual first-error image and finite inverse, both second-error canonical carries, every unchanged primary and low condition, exact proper derivative image, exhaustive lifts and fiber2^(2d-47A/4). The theorem does not show that any particular C686 output passes the new invariants, nor that all earlier choices fail. No modulo16 example or original realization is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual all-lift criterion](#statement) | SX1--SX9, all factorized input/support/root/degree hypotheses, actual full modulo8 base, every monic lift modulo32 above its fixed modulo8 class, first-error test and explicit correction, all second-error tests, exact count and unresolved actual-input evaluation. |
| argument | [Complete next-layer elimination](#argument) | SX10--SX28 and SX2--SX6, actual new half-remainders, both canonical-divisor carries, complete C2/C5 composition, full first image and inverse, all non-phi components, precise remaining derivative image, exhaustion/uniqueness/count and representative invariance. |
| dependency | [Exact actual changing-divisor identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | CL5--CL6 and integer monic-division compatibility, reused as an exact identity; its modulo8 specialization is not presumed to prove the new modulo16 conclusion. |
| dependency | [Actual old residual correction](Yin_C_G0202_v1.md#coupled-error-map) | CL9--CL10 identifying precisely which8V preserve the actual two modulo8 residuals; specialized after the current all-primary alpha is checked. |
| dependency | [Square-input actual representatives](Yin_C_G0675_v1.md#argument) | MQ3--MQ5, global a=P^2+2Xi, actual c reduction and bbar=0, all non-phi reductions and canonical free-module interpretation; the next integer halves and modulo16 changes are proved here. |
| support | [Existing final square image](Yin_C_G0675_v1.md#statement) | MQ7--MQ8 give the previous-layer model; the16Z map and its exact rank are rederived here at the new actual precision, with no automatic lift presumed. |
| support | [Actual nonempty modulo8 input](Yin_C_G0686_v1.md#statement) | Application only: every adopted q>=256 construction supplies SX1--SX3 with original complete support, degree/gap/layer and maximal-q boundaries; it does not supply any vanishing of the new invariants. |
| support | [Complete prior construction](Yin_C_G0686_v1.md#argument) | HP2--HP7 match the actual T form, stronger root, global J_H and low coefficient constraints and unchanged degree; no stronger derivative or residual precision is imported. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0912_v1.md#whole-mod-sixteen-all-lift-finding) | Entire SX1--SX28, all actual integer halves/compositions/canonical quotients, complete first and second image tests, every primary, all-lift exhaustion and exact count with representative invariance. |
