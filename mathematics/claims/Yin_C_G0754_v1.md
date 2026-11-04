---
author: Yin
---

# Completely cyclotomic first-bit residuals with nonzero binary canonical G

Human author Yin.
Root proposed the cyclotomic trace product, its E=9A binary profile, the exact two local targets for a complete Y and the full canonical congruence to be tested.
Earlier_bit_obstruction read the complete-group generation and forward-row interfaces, simplified the high target, supplied the actual character-zero completion using the explicit C657 endpoint unit, and checked the integer trace product and all full-primary canonical remainders.
Both are contributors, not independent reviewers.
Root read the entire stable OC1--OC6 statement and proof and separately read the actual C664 generation/calibration and C657 endpoint interfaces.
This complete author theorem is initially open for fresh independent whole review.
The construction uses adopted finite-kernel generation at its actual scope; it assumes no unit-group surjectivity and no numerical membership result.

The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: project deduction from the adopted exact complete-factor kernel, explicit character correction and actual canonical integer maps selected below.
The [D5 development](../drafts/Yin_D_G0005.md#cyclotomic-odd-g-first-bit-complete-target) is provenance only; this fixed material contains the complete necessary proof and has no mutable-D dependency.

## Statement

### OC1. Exact source reuse and statement

The required complete-factor image is [C664 G4--G5 and HG7](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24), not the whole ambient unit group.
Its character is calibrated by C664 HG1, and [C657 K2/KL2 at L=2](Yin_C_G0657_v1.md#decision-whole-reviewed-2026-10-24) supplies the exact high unit used below.
[C667 FC1--FC4](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) proves the global forward multiplicities for those actual whole rows; its special original-gate target is not assumed here.
The fixed J130 contract was inspected: it concerns X^32 phi^64 and two different targets, so it is neither executed nor reused as numerical evidence for this modulus.
No new native computation or finite-rank inference is needed because the adopted character theorem supplies exact membership and a bounded finite product.
The actual trace factors and dyadic divided remainder of the last factor use [C752 CY3--CY4](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25).

Work over F_2 with

    phi=X^2+X+1, chi=Xphi^2, Psi=phi(chi),
    lambda=X^3+X.

There exists a monic complete odd-order trace product Y, prime to Xphi, with

    Y=1 modulo X^3, Y=X modulo phi^3,
    Y divides Y(chi), Y divides Y(lambda),
    degY<=110400.                              (OC1)

It can be chosen from the explicit40 whole rows in OC3, each with an exponent in{0,...,23}, with every primitive support order below240 and coprime3.
The existence of the exponent vector is supplied by the exact adopted finite-kernel theorem; no particular numerical vector or expanded Y is asserted computed here.
Choose the integer lift mathcal_Y by replacing every complete primitive W_n factor of this Y by its full monic integer trace factor F_n, with the SAME nonnegative multiplicity.
Then mathcal_Ybar=Y, degmathcal_Y=degY and its reciprocal lift is completely cyclotomic.

For EVERY dyadic q>=2, use that same Y and lift, and put f=X^2+X-1 and g=X^2-X-1.
Define the integer trace polynomials and form the actual monic T_q by

    C_0=2, C_1=X, C_(n+1)=X C_n-C_(n-1),
    C_2=X^2-2, C_3=X^3-3X,
    C_5=X^5-5X^3+5X,

    D_q=(X^2 f^2 mathcal_Y)^q,
    V_q=g(C_(16q)),
    T_q=D_q V_q.                               (OC2)

Compute every canonical polynomial using T_q itself as divisor:

    a=rem_(T_q)T_q(C_2)/2,
    b=rem_(T_q)T_q(C_3)/3,
    c=rem_(T_q)T_q(C_5)/5,
    F=rem_(T_q)(2c^2-3a^5),
    G=rem_(T_q)(c^3-2b^5),
    X_epsilon=rem_(T_q)(b^2-a^3+epsilon(c^3-2b^5)),
    epsilon in{1,-1}.

All prime divisions are actual integer coefficient divisions, as in adopted C736.
Write Delta(P)=(P(C_2)-P^2)/2, an actual integer polynomial for every integer P.
Then the SAME T_q satisfies

    F=X_1=X_(-1)=0 modulo2,
    Gbar!=0, ord_phi Gbar=12q,
    degT_q=q(degY+38)<=110438q.                 (OC3)

Here P_H(z)=z^(degH)H(z+z^(-1)) denotes the reciprocal trace lift of a monic integer H.
The reciprocal polynomial is exactly

    P_(T_q)=(Phi_4^2 Phi_5^2 P_(mathcal_Y))^q
                                           * Phi_(160q),
    degP_(T_q)=2q(degY+38)<=220876q,
    m(P_(T_q))=0.                              (OC4)

Thus even F/X and nonzero BINARY canonical G do not, in an arbitrary binary profile, force a noncyclotomic factor.
This statement is at coefficient precision2 only; no simultaneous higher2^N precision or precision-compatible infinite lift is asserted.

## Complete argument

### OC2. The prescribed high target and a legitimate character-zero completion

All inverses in the following target are in the high phi-unit ring:

    v_0=X^(-1)(1+X^8)^(-1)Psi^9 modulo phi^3.

In fact v_0=X modulo phi^3.
Indeed 1+X^8=(X+1)^8 and X(X+1)=1+phi, so

    X^(-1)(1+X^8)^(-1)=X^7(1+phi)^(-8)
                                      =X^7 modulo phi^3.

Also Psi=1+Xphi^2+X^2phi^4, giving Psi^9=1+Xphi^2 modulo phi^3.
Using X^3=1+(X+1)phi, one obtains

    v_0-X=phi^2[X(X+1)^2+X^8] modulo phi^3=0,

since the bracket vanishes modulo phi.
No inverse of phi or of a nonunit in the combined low/high ring has been taken.

Use R_3=F_2[X]/(X^3phi^6), and define its unit class c_* by the two COMPLETE CRT conditions

    c_*=1 modulo X^3,
    c_*=X(1+Xphi^3) modulo phi^6.              (OC5)

The second condition retains more high coefficients than the required target modulo phi^3.
It is chosen to make the actual finite character vanish.
In the completed product use the low lift u=1 and high lift v=Xw_2, w_2=1+Xphi^3.
C664 HG1 gives c_high(X)=-1/5 in Z_2.
C657's explicit L=2 calculation gives c_high(w_2)=Pi(1,w_2)=1 modulo2, with its actual norm1+t^2 modulo t^3 and t=chi.
Therefore the exact finite character at this modulus, whose target is Z/2 because floor(log_2 3)=1, has

    Pi_3(c_*)=c_high(X)+c_high(w_2)
                       -(2/5)ell(1)=1+1=0 modulo2. (OC6)

The evaluation uses an actual completed lift of the entire CRT class and the adopted lift-independent character.
It does not discard the extra coefficient at phi^3 or infer that every unit target belongs to the complete-factor image.
C664 G4 now gives c_* in the full complete-factor subgroup G_3.

### OC3. Full whole-row representative and both forward divisibilities

At r=3 the exact C664 parameters are

    L_3=8, e_3=24.

The32 ordinary rows begin with odd n,1<=n<80,5 not dividing n; use B_n unless3 divides n, in which case use B_(n+80).
These indices are coprime15 and below160.
The8 divided rows begin with odd j,1<=j<16; choose the least k in{0,1,2} such that ell=j+16k is coprime15 and use

    D_(5ell)=B_(5ell)/phi=B_ell(chi).

Their source orders5ell are below240.
The common predivision modulus X^3phi^7 in C664 retains both primary components when phi is divided, so these are actual whole polynomial rows with the claimed classes in R_3.
Because c_* is in G_3, the exact G5 conclusion supplies a nonnegative product of these40 rows with every exponent at most23 representing c_*.
Choose this actual polynomial as Y.
Its degree obeys the adopted complete bound

    degY<=75 L_3^2(e_3-1)=110400.               (OC7)

Every ordinary row is a product of complete W_d for d>1 dividing its index, with gcd(d,15)=1.
Every divided row is a product of complete W_d W_(5d) for d>1 dividing ell.
Thus the full factorization has the C667 pattern

    Y=product_(d>1,gcd(d,15)=1)
                        W_d^(u_d)W_(5d)^(v_d),
    0<=v_d<=u_d,                               (OC8)

with no W_5, no X and all actual repeated factors retained.
The full identities W_d(chi)=W_d W_(5d) and W_(5d)(chi)=W_(25d) make Y|Y(chi).
Every support order is coprime3, so the complete identity W_n(lambda)=W_n W_(3n) makes Y|Y(lambda).
These are the actual global polynomial statements proved in C667 FC1--FC4, not conclusions from the local CRT jets.
Equation OC5 gives Y=1 modulo X^3 and Y=X modulo phi^3, proving all of OC1.
Replacing precisely the factors in OC8 by F_d,F_(5d) defines the monic integer mathcal_Y and proves the complete cyclotomic identity for P_(mathcal_Y), with unchanged degree and multiplicity.

### OC4. Actual dyadic canonical reduction and the complete odd reductions

The actual polynomial V_q=F_(160q) has

    V_qbar=phi^(16q),
    a_(V_q)=1-C_(16q)

by the full integer quotient identity C752 CY9 and its legitimate pure-composition remainder.
The displayed equality is for the OWN divisor V_q, not yet for T_q.
Since q is even, the exact Delta product rule gives Delta(D_q)bar=0.
Using T_q=D_q V_q in that INTEGER rule and then reducing modulo2, the actual T_q canonical class is

    alpha=a_Tbar=[D_qbar^2 Delta(V_q)bar].

The integer difference Delta(V_q)-a_(V_q) is divisible by V_q; after multiplication by D_q^2 its contribution is divisible by the actual T_q.
Consequently this is legitimately

    alpha=[alpha_0^q],
    alpha_0=X^4Y^2phi^4(1+X^16),
    U=T_qbar=X^(2q)Y^qphi^(18q).               (OC9)

The actual odd prime divisions are already integral before reduction, so in F_2[X]/U

    beta=b_Tbar=[U(lambda)]=0,
    gamma=c_Tbar=[U(chi)]=[gamma_0^q],
    gamma_0=X^2Y(chi)phi^4Psi^18.              (OC10)

The first zero follows from X|lambda, phi|phi(lambda) and the full Y-forward condition, at every multiplicity.
The formula for gamma composes the actual full polynomial U; it does not compose a local quotient class for Y.
At phi, gamma_0 has exact order4 because Y(chi) and Psi are units there, so gamma has exact order4q.

### OC5. Both complete first-bit residuals and nonzero canonical G

The binary first residual is alpha^5.
The polynomial alpha_0^(5q) contains X^(20q)Y^(10q)phi^(20q), hence is divisible by the ENTIRE U=X^(2q)Y^qphi^(18q).
Thus F=0 modulo2 globally, including every non-phi primary.
Since beta=0, both second signs reduce to alpha^3+gamma^3, and Gbar=gamma^3.
Both alpha^3 and gamma^3 are separately divisible by X^(2q)Y^q, using Y|Y(chi) for the latter.
For the remaining full phi^(18q) component their sum has representative

    X^(6q)phi^(12q)
       [X^6Y^6(1+X^16)^3+Y(chi)^3Psi^54]^q.   (OC11)

The actual low condition Y-1 divisible by X^3 gives Y(chi)-1 divisible by chi^3, hence by phi^6.
This substitution is applied to an actual global polynomial divisibility.
The high condition Y=v_0 modulo phi^3 gives after legitimate squaring

    X^2Y^2(1+X^16)=Psi^18 modulo phi^6.

Cubing it and using Y(chi)=1 modulo phi^6 shows the bracket in OC11 is divisible by phi^6.
Its q-th power is divisible by phi^(6q), proving the full phi^(18q) second congruence.
Together with the full complementary factor already checked, this proves X_1=X_(-1)=0 modulo2 as actual polynomial remainders.
Meanwhile gamma^3 has exact order12q<18q at phi, so the canonical Gbar is nonzero, with precisely that polynomial phi-order because monic reduction subtracts a multiple of phi^(18q).
In particular the actual integer G is nonzero and coefficientwise odd somewhere.

### OC6. Complete reciprocal factors, degrees and precision boundary

The primitive-order factorization of V_q and every factor of mathcal_Y give exactly OC4.
All those reciprocal factors are cyclotomic and monic, so their full logarithmic Mahler measure is zero.
The actual degrees are degD_q=q(6+degY), degV_q=32q and degT_q=q(38+degY), giving both stated bounds without dropping any factor.
The same construction works for each dyadic q>=2, with a single chosen whole Y independent of q.
This is not a claim that increasing q raises the simultaneous coefficient precision above2.

Writing A=2q, this source has phi-exponent18q=9A rather than the7A domain of C752.
Its nonzero alpha order4q is exactly compatible with the C752 cyclotomic alternative: E=18q and w=16q give2(E-w)=4q.
There is therefore no conflict with C752's specific source-profile obstruction or positive-measure conclusion.
The earlier broad implication from nonzero binary G and first-bit F/X precision to noncyclotomicity is false, while the question of analogous all-cyclotomic examples at every prescribed higher precision remains unresolved here.
No original C746/C748 source, h bound or original residual degree expense is silently reassigned to this different polynomial.
No irreducible certificate, characteristic-zero residual identity, positive-measure example or unrestricted Lehmer conclusion is supplied by this first-bit construction.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision cyclotomic-odd-g-first-bit-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:48 |
| status | open |
| reason | Register the entire OC1--OC6 construction. The exact high target simplifies to X modulo phi^3 and is completed in R_3 by X(1+Xphi^3), whose actual finite Pi_3 vanishes with low component1. Adopted C664 therefore supplies a whole40-row representative Y with exponents0--23, degree<=110400, complete supported factor multiplicities and both global forward divisibilities. The exponent vector is proved to exist, not asserted numerically computed. One such Y and its unchanged full integer lift work for every dyadic q>=2 in T_q=(X^2f^2 mathcal_Y)^q g(C_(16q)). The SAME polynomial has F,X_1,X_(-1) even and actual canonical Gbar nonzero with exact phi-order12q; its entire reciprocal product is cyclotomic of degree<=220876q and measure0. All actual integer divisions, product carries, complementary/full phi^(18q) components, whole factors, target character, bounds and trace maps are retained. The profile is E=9A and does not contradict C752's E=7A theorem. Root and Earlier_bit_obstruction are contributors; fresh independent whole review remains outstanding. The result proves coefficient precision2 only; varying q is not asserted to increase that precision. No computed row vector, arbitrary higher-precision cyclotomic realization, compatible infinite lift, reassigned original C746/C748 costs, irreducible or positive-measure certificate, characteristic-zero residual identity or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete first-bit construction statement](#statement) | OC1--OC4 and OC6: existence of the complete bounded whole Y and its fixed integer trace lift, all dyadic q>=2 using that same Y, actual same-divisor F/X for both signs modulo2 with nonzero binary G and exact phi-order12q, entire cyclotomic reciprocal identity/degree/measure, forty-row existence versus computation, E=9A and every finite-precision/source boundary. |
| argument | [Complete character, whole-row and canonical proof](#complete-argument) | Entire OC2--OC6 and OC5--OC11: exact unit target simplification, actual completed lift and Pi_3 correction, safe row/predivision/exponent/degree generation, both full forward multiplicities and integer lift, actual dyadic product quotient cancellation before reduction, odd canonical maps, complete non-phi and phi^(18q) residuals, exact nonzero G order, reciprocal factors and all retained limits. |
| dependency | [Adopted exact all-depth complete-factor generation](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G4--G5/HG1/HG7: calibrated c_high(X)=-1/5, exact G_3=kerPi_3, full finite image and actual safe forty coprime-three whole rows at L_3=8,e_3=24, nonnegative exponents<=23, complete predivision precision and degree<=110400. No unit-group surjectivity or special original canonical target is inferred; OC6 proves membership of the selected completed target. |
| dependency | [Adopted exact high-unit endpoint character](Yin_C_G0657_v1.md#decision-whole-reviewed-2026-10-24) | K2/KL2 at L=2: the completed high unit1+Xphi^3 has Pi(1,w_2)=1 modulo2, including its actual norm1+t^2 modulo t^3. The unit supplies the character correction, not an assumed deep-kernel element at N=3; the actual Pi_3 evaluation uses the complete low/high CRT class. |
| dependency | [Adopted whole-row forward multiplicities](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC4 actual ordinary/divided-row factor pattern W_d^u W_(5d)^v with0<=v<=u and support coprime3, giving both full polynomial forward divisibilities. Only that row mechanism is used. Its special C1 original-gate target, multiplicity-floor adjustment, nonsquare/fresh-factor claims and synthetic integer G construction are not premises. |
| dependency | [Adopted actual integer canonical product maps](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 prime-divisible monic remainders, integral Delta and exact product rule at arbitrary monic integer factors. OC4 retains the actual V_q quotient, cancellation of its multiple in T_q, and even q power before reduction; no automatic factor residual inheritance is assumed. |
| dependency | [Adopted exact cyclotomic trace and dyadic remainder formulas](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3--CY4/CY8--CY9: full monic integer trace factors and binary reductions, F_(160q)=g(C_(16q)), exact own dyadic divided remainder1-C_(16q), and complete reciprocal factor identity. The source obstruction and degree theorem remain at E=7A; OC6 explicitly checks the new E=9A profile against its valuation alternative without claiming a contradiction or extending that obstruction. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:57 |
| status | proved |
| reason | Register the entire OC1--OC6 construction. The exact high target simplifies to X modulo phi^3 and is completed in R_3 by X(1+Xphi^3), whose actual finite Pi_3 vanishes with low component1. Adopted C664 therefore supplies a whole40-row representative Y with exponents0--23, degree<=110400, complete supported factor multiplicities and both global forward divisibilities. The exponent vector is proved to exist, not asserted numerically computed. One such Y and its unchanged full integer lift work for every dyadic q>=2 in T_q=(X^2f^2 mathcal_Y)^q g(C_(16q)). The SAME polynomial has F,X_1,X_(-1) even and actual canonical Gbar nonzero with exact phi-order12q; its entire reciprocal product is cyclotomic of degree<=220876q and measure0. All actual integer divisions, product carries, complementary/full phi^(18q) components, whole factors, target character, bounds and trace maps are retained. The profile is E=9A and does not contradict C752's E=7A theorem. Adopt fresh context-isolated whole R974 after root read all OC1--OC6, the fixed statement and precise generation/character/source interfaces, and the entire independent finding. Root and Earlier_bit_obstruction remain contributors; the reviewer contributed no repair. The accepted finite theorem supplies the bounded existential row vector, and every actual full canonical and reciprocal assertion passed with its precision2-only boundary. The result proves coefficient precision2 only; varying q is not asserted to increase that precision. No computed row vector, arbitrary higher-precision cyclotomic realization, compatible infinite lift, reassigned original C746/C748 costs, irreducible or positive-measure certificate, characteristic-zero residual identity or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete first-bit construction statement](#statement) | OC1--OC4 and OC6: existence of the complete bounded whole Y and its fixed integer trace lift, all dyadic q>=2 using that same Y, actual same-divisor F/X for both signs modulo2 with nonzero binary G and exact phi-order12q, entire cyclotomic reciprocal identity/degree/measure, forty-row existence versus computation, E=9A and every finite-precision/source boundary. |
| argument | [Complete character, whole-row and canonical proof](#complete-argument) | Entire OC2--OC6 and OC5--OC11: exact unit target simplification, actual completed lift and Pi_3 correction, safe row/predivision/exponent/degree generation, both full forward multiplicities and integer lift, actual dyadic product quotient cancellation before reduction, odd canonical maps, complete non-phi and phi^(18q) residuals, exact nonzero G order, reciprocal factors and all retained limits. |
| dependency | [Adopted exact all-depth complete-factor generation](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G4--G5/HG1/HG7: calibrated c_high(X)=-1/5, exact G_3=kerPi_3, full finite image and actual safe forty coprime-three whole rows at L_3=8,e_3=24, nonnegative exponents<=23, complete predivision precision and degree<=110400. No unit-group surjectivity or special original canonical target is inferred; OC6 proves membership of the selected completed target. |
| dependency | [Adopted exact high-unit endpoint character](Yin_C_G0657_v1.md#decision-whole-reviewed-2026-10-24) | K2/KL2 at L=2: the completed high unit1+Xphi^3 has Pi(1,w_2)=1 modulo2, including its actual norm1+t^2 modulo t^3. The unit supplies the character correction, not an assumed deep-kernel element at N=3; the actual Pi_3 evaluation uses the complete low/high CRT class. |
| dependency | [Adopted whole-row forward multiplicities](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC4 actual ordinary/divided-row factor pattern W_d^u W_(5d)^v with0<=v<=u and support coprime3, giving both full polynomial forward divisibilities. Only that row mechanism is used. Its special C1 original-gate target, multiplicity-floor adjustment, nonsquare/fresh-factor claims and synthetic integer G construction are not premises. |
| dependency | [Adopted actual integer canonical product maps](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 prime-divisible monic remainders, integral Delta and exact product rule at arbitrary monic integer factors. OC4 retains the actual V_q quotient, cancellation of its multiple in T_q, and even q power before reduction; no automatic factor residual inheritance is assumed. |
| dependency | [Adopted exact cyclotomic trace and dyadic remainder formulas](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3--CY4/CY8--CY9: full monic integer trace factors and binary reductions, F_(160q)=g(C_(16q)), exact own dyadic divided remainder1-C_(16q), and complete reciprocal factor identity. The source obstruction and degree theorem remain at E=7A; OC6 explicitly checks the new E=9A profile against its valuation alternative without claiming a contradiction or extending that obstruction. |
| review | [Fresh independent whole cyclotomic odd-G first-bit review](../audits/reviews/Yin_R_G0974_v1.md#whole-cyclotomic-odd-g-first-bit-finding) | Entire fixed OC1--OC6 and OC1--OC11, exact character-zero complete target, bounded whole generation and factors, actual canonical maps on every primary, both signs and exact odd G, complete cyclotomic product/degree/measure and all precision/source boundaries; independently reviewed with exact statement and proof bindings. |

