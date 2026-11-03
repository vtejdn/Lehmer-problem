---
author: Yin
---
# An exact same-coefficient modulo-four square-image obstruction

Human author Yin.
Root proposed the actual half-difference, C5 cube expansion and three-term second-residual error.
The same_trace contributor checked all integer divisions and changing-divisor terms, specified the global factorized lift and other-primary conditions, proved the complete square-image equivalence and sign translation, and constructed the discriminating pair of coefficient classes.
These are author contributions, not independent review of this theorem.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Focused reuse inspected the exact C196/C197 half-difference and local-module arguments, C202's same-divisor correction map, C603's FE8 coefficient calculation and C649's full root/support precision.
The [D1 SAME-T section](../drafts/Yin_D_G0001.md#same-t-mod4-square-image-candidate) is development provenance, not a proof dependency.
The proof below states every required polynomial hypothesis directly and does not rely on an unreviewed existence construction of such data.
No native calculation, numerical coefficient scan, new child agent or higher-modulus iteration is used.
This whole statement and proof are initially open for fresh isolated whole mathematical review.

## Statement

Let A>=2 be EVEN, put Phi=X^2+X+1 over Z, phi=Phi mod2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be monic and prime to Xphi, with every occurring irreducible factor of multiplicity at least2, and assume

    Y|Y(chi), Y|Y(X^3+X), X^(2A)|Y'.

Put H_0=X^A Y, U=H_0phi^(7A), d=degU and C_0=X^A Y(chi)Psi^(7A).
Assume the exact old support congruence

    H_0^6=C_0^21 modulo phi^(4A).                         (S1)

The exponent A belongs to the ACTUAL U being lifted; no replacement by a normalized A_0 is implicit.
Choose one monic integer lift P_psi of every irreducible factor psi of H_0, with P_X=X, and use the FULL exponent N_psi to define

    mathcal_H=product_(psi|H_0)P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_(psi|H_0)psi^(ceil(N_psi/2)).

This factorized integer lift, rather than an arbitrary coefficient lift of U, is part of the input.
Let Z be the unique unit eleventh root of H_0C_0^2 modulo phi^(3A).
Choose any integer K satisfying

    Kbar=Z modulo phi^(3A), J_H|Kbar,
    deg(Phi^A K)<d.                                      (S2)

Such choices exist by CRT with degK<6A+degJ_H.
For an integer W of degree<d let

    T_W=mathcal_H Phi^(7A)+2Phi^A K+4W.                   (S3)

Every T_W is monic of the SAME degree d and has reduction U.
Use the actual integer monic divisions

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_(T_W)(T_W(C_2))/2,
    b=rem_(T_W)(T_W(C_3))/3,
    c=rem_(T_W)(T_W(C_5))/5,
    F(T_W)=rem_(T_W)(2c^2-3a^5),
    X_s(T_W)=rem_(T_W)(b^2-a^3+s(c^3-2b^5)), s=1 or-1.

All statements about divisibility modulo4 refer to the canonical integer coefficients of these actual remainders.

### Exact first residual and calculated second error

For EVERY W, all coefficients of F(T_W) are divisible by4, and all coefficients of X_s(T_W) are even.
On every non-phi primary component both residuals already vanish modulo4.
The global reductions are a_bar=(phi^A Kbar)^2, b_bar=0, while c_bar is zero on the H_0-primary components and equals phi^(2A)C_0 on B_phi=F_2[X]/phi^(7A).
In particular

    Kbar^6=C_0^3 modulo phi^(4A),
    a_bar^5=0, a_bar^3=c_bar^3 in F_2[X]/U.              (S4)

For the exact remaining coefficient, use the concrete integer polynomials

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A),
    D_K=((K(C_2)-K^2)/2)bar+Kbar^2.

Perform the ACTUAL canonical monic integer division

    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A.                  (S5)

Its remainder is even and L_sbar is divisible by phi^(3A), so these are well-defined integer polynomials.
With w=Wbar, the complete local half-error is

    (X_s(T_W)/2)bar
      =phi^A Kbar L_sbar/H_0
       +phi^(6A)(M_sbar+Kbar^4D_K)
       +phi^(4A)(C_0^2Psi^A Kbar(chi)+Kbar^4w^2)
                                               in B_phi. (S6)

The first term is the changing-divisor contribution and cannot be omitted.
All denominators are units in the specified component.
Every term is in phi^(4A), but this order condition alone is not sufficient.

Take L_sbar/phi^(3A) by exact polynomial division before reduction and define

    eta_s=(L_sbar/phi^(3A))/(H_0 Kbar^3)
       +phi^(2A)(M_sbar/Kbar^4+D_K)
       +C_0^2Psi^A Kbar(chi)/Kbar^4
                                   modulo phi^(3A).      (S7)

Then the full simultaneous criterion is

    F(T_W)=X_s(T_W)=0 modulo4
       if and only if w^2=eta_s modulo phi^(3A).          (S8)

Thus the fixed monic coefficient class T_W modulo4 admits a correction4W if and only if eta_s belongs to the Frobenius-square image of F_2[X]/phi^(3A), equivalently eta_s'=0 in that ring.
When it does, exactly2^(d-3A) of the2^d coefficient classes T_W modulo8 work; otherwise none do.
This counts one shared correction for both actual residuals on every primary.

The two signs have equivalent solvability.
If w solves the positive sign, then

    w_minus=w+phi^A Kbar modulo U                         (S9)

solves the negative sign, and conversely.
Equivalently eta_-+eta_+=(phi^A Kbar)^2 modulo phi^(3A).
This relates solutions for different signs, not necessarily the same W for both signs.

### A uniform discriminating pair of actual coefficient classes

Let K_0 be the coefficient0/1 integer lift of the unique CRT representative in S2 of degree<6A+degJ_H.
Let j be the least ODD integer at least A/2, so A/2<=j<A.
Let L be the coefficient0/1 lift of J_H X^(j-A/2), and put

    K_1=K_0+Phi^(3A)L.                                   (S10)

Both choices satisfy S2 and preserve the SAME U, reduction classes a_bar,b_bar,c_bar, old support and any additional full C649 gate and prescribed integer-layer data attached to those polynomial inputs.
They define distinct allowed monic coefficient classes modulo4, and their first residuals vanish modulo4 for every W.
For either fixed sign their explicitly computed eta values satisfy

    eta_s(K_1)+eta_s(K_0)
       =C_0^2Psi^(4A)Lbar(chi)/K_0bar^4
                                        modulo phi^(2A),
    ord_phi(eta_s(K_1)+eta_s(K_0))'=2j<2A.               (S11)

Hence their difference is NOT a square modulo phi^(3A).
They cannot both pass S8; by S9, at least one of the two coefficient classes has no correction4W solving both residuals for EITHER sign.
No native evaluation is needed for this conditional all-A pair certificate.
It does not identify which of the two fails without evaluating its actual eta and does not exclude another soluble K.

### Complete precision and original-input boundary

The theorem is for the SAME actual integer polynomial and canonical quotients modulo4; no free a,b,c or independent residual corrections are substituted.
It shows that even compatible full formal-gate data do not make EVERY monic modulo4 coefficient class automatically liftable.
It does NOT assert that such gate data fail to admit SOME other choice of K; that existential issue remains open here.
When applying this to U=U_0^q, use the actual exponent A=ord_XU and degree d, not the normalized exponent or a smaller hypothetical field.
A successful S8 supplies neither the separate C202 modulo8 conditions nor C603's first error, nor the characteristic-zero residuals, irreducible reciprocal nontorsion P, total reality or an original realization.
All original integer layers, q and degree costs retain their actual roles.
No new original A_0 exclusion or unrestricted Task completion follows.

## Argument

### MT1: complete polynomial input and one specified integer coefficient class

Let A>=2 be EVEN, phi=X^2+X+1, Phi=X^2+X+1 over Z, chi=Xphi^2, and Psi=phi(chi).
Let Y in F_2[X] be monic and prime to Xphi, with every occurring irreducible factor of multiplicity at least2.
Assume

    Y divides Y(chi), Y divides Y(C_3),
    X^(2A) divides Y', C_3=X^3+X.

Put H_0=X^A Y, U=H_0phi^(7A), d=degU, and C_0=X^A Y(chi)Psi^(7A).
Assume the full old support congruence

    H_0^6=C_0^21 modulo phi^(4A).                         (MT1)

The additional full C649 gate may also be prescribed; it is retained unchanged in the coefficient-pair comparison below, but MT1 and the stated low derivative are the only gate data needed in this calculation.
The A here is the exponent of the ACTUAL U under study; it is not silently replaced by a normalized A_0 for the same integer T.

Choose, for every irreducible factor psi of H_0, a monic integer lift P_psi with reduction psi, using P_X=X.
If N_psi is its FULL exponent in H_0, set

    mathcal_H=product_psi P_psi^(N_psi)=X^A mathcal_Y,
    T_00=mathcal_H Phi^(7A).

This FACTORIZED lift is important: the condition that all N_psi>=2 proves Delta_2(T_00)bar=0 modulo U.
An arbitrary coefficient0/1 lift of U is not assigned that property without proof.
Let

    J_H=product_(psi|H_0) psi^(ceil(N_psi/2)).

It includes X^(A/2), is prime to phi, and has degree at most degH_0.
Let Z be the unique unit eleventh root of H_0C_0^2 modulo phi^(3A).
Choose an integer polynomial K with

    Kbar=Z modulo phi^(3A), J_H divides Kbar,
    deg(Phi^A K)<d.                                      (MT2)

Such a K exists by CRT, with degK<6A+degJ_H<d-2A.
For any integer W of degree<d put

    T_W=mathcal_H Phi^(7A)+2Phi^A K+4W.                   (MT3)

This is a monic degree-d polynomial in one fixed coefficient class modulo4.
All quotient polynomials below use THIS SAME T_W and actual integer monic division:

    a=theta_2(T_W), b=theta_3(T_W), c=theta_5(T_W),
    theta_p(T)=rem_T(T(C_p))/p,
    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

Each divided remainder is integral because C_p=X^p modulo p and monic division commutes with reduction.

### MT2: actual reductions on ALL primary components

For an integer polynomial P put Delta_2(P)=(P(C_2)-P^2)/2.
The product rule modulo2 gives Delta_2(P^n)bar=n Pbar^(2n-2)Delta_2(P)bar.
For each factor exponent n>=2 the displayed power is divisible by Pbar^n when n is odd, and the coefficient vanishes when n is even.
Applying the product rule to the entire factorized T_00 shows U divides Delta_2(T_00)bar.
The additive half-difference formula for T_W=T_00+2U_1+4W, U_1=Phi^A K, then gives globally

    abar=phi^(2A)Kbar^2=(phi^A Kbar)^2 in F_2[X]/U.

The condition J_H|Kbar makes this class zero in EVERY H_0-primary component.
Both odd quotients have their actual reductions rem_U U(C_p), since3 and5 are units modulo2.
The two forward divisibilities imply U|U(C_3), and H_0|U(chi).
Consequently

    bbar=0 globally,
    cbar=0 on H_0-primary components,
    cbar=phi^(2A)C_0 in B_phi=F_2[X]/phi^(7A).           (MT4)

On every non-phi primary, all of a,b,c have zero reduction, hence are even in the localized free monic quotient modulo4.
Their actual residuals F and X_s are therefore already zero modulo4 there, for every W.
No phi-only check is substituted for those other components.
These primary localizations detect zero in the finite quotient (Z/4Z)[X]/(T_W): a nonzero element has a proper annihilator contained in a maximal ideal, and cannot vanish after localization at that ideal.
The maximal ideals are exactly those above the irreducible factors of U because2 is nilpotent.
After all local components vanish, the monic free basis1,X,...,X^(d-1) identifies this with coefficientwise divisibility by4 of the canonical remainder.

The root choice MT2 and MT1 imply

    Kbar^6=C_0^3 modulo phi^(4A).                        (MT5)

Indeed raising Kbar^11=H_0C_0^2 modulo phi^(3A) to the sixth power raises its error to at least6A.
Thus (Kbar^6/C_0^3)^11=1 modulo phi^(4A) by MT1.
The eleventh-power map is bijective on this unit group, whose order is3*4^(4A-1), proving MT5.
This also proves a_bar^3=c_bar^3 globally and a_bar^5=0, so both canonical residuals are even and their integer coefficient halves are defined.

### MT3: the exact local dyadic coefficient and first residual

Work in the localization Q_4 of(Z/4Z)[X]/(T_W) at polynomials prime to phi.
Monicity makes the global quotient free over Z/4Z; localizing gives ann(2)=2Q_4 and a unique half modulo2 of every even class.
The divisor relation is

    Phi^(7A)=-2Phi^A K/mathcal_H modulo4.

The direct binomial/product calculation used in C603 FE8 applies before assuming any first-residual divisibility: Delta_2(Phi^(7A)) vanishes in Q_4 because A is even and every surviving term has an even coefficient and at least7A powers of Phi.
The product Delta_2(mathcal_H Phi^(7A)) vanishes there as well; Phi^(14A) is zero in Q_4.
Expanding the full actual T_W then gives

    a=Phi^(2A)K^2+2Z_a in Q_4,
    Z_abar=phi^(2A)D_K+w^2,
    D_K=Delta_2(K)bar+Kbar^2, w=Wbar.                    (MT6)

Here Z_a is the actual half, not a free quotient coordinate.
The equality uses Delta_2(Phi^A)bar=0 for even A and W(C_2)bar=w^2.

Since cbar=phi^(2A)C_0, expansion of the actual first residual and reduction by the SAME divisor gives

    F(T_W)=2Phi^(4A)(mathcal_H C^2+3K^11)/mathcal_H
                                                       modulo4, (MT7)

for any integer lift C of C_0 as in MT4.
For example a^5=Phi^(10A)K^10 modulo4: its first correction contains2Phi^(8A), which vanishes after the divisor relation.
Then Phi^(10A)K^10=-2Phi^(4A)K^11/mathcal_H modulo4.
This proves MT7 without changing the monic divisor while taking powers.
Because Kbar^11=H_0C_0^2 modulo phi^(3A), MT7 is zero in Q_4.
Combined with MT4 on all other primaries, EVERY coefficient of F(T_W) is divisible by4 for EVERY W.
Thus the first residual is fully settled in this chosen modulo4 coefficient class, not merely at its reduced generator.

### MT4: actual C5 cube and the changing-divisor half of the second residual

Use the concrete integer lifts

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A).

Then Cbar=C_0, and C_5=chi_0+2E_5 for an integer polynomial E_5.
Since5 is1 modulo4, the actual c equals T_W(C_5) in Q_4.
Taylor expansion of mathcal_H(X)Phi(X)^(7A) at chi_0 is legitimate modulo4.
Its derivative modulo2 is chi^A Y'(chi)Psi^(7A), because A and7A are even.
The hypothesis X^(2A)|Y' therefore gives phi-order at least6A for this derivative.
In the cube its Taylor correction is multiplied by2Phi^(4A), so it vanishes by2Phi^(7A)=0 in Q_4.
The exact remaining cube is

    c^3=Phi^(6A)C^3+2Phi^(4A)C^2Psi_0^A K(chi_0)
                                                       modulo4. (MT8)

Every occurrence of the odd quotient and every Taylor term was expanded before monic reduction; no independent c coefficient was selected.
Since bbar=0 globally, b^2 and2b^5 vanish modulo4.

For either sign s, perform the ACTUAL monic integer division

    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A.                 (MT9)

The integer remainder is even by MT5, so this defines integer L_s,M_s without division by a characteristic-two zero divisor.
In fact L_sbar is divisible by phi^(3A), again by MT5.
Using MT6 and MT8, reduce the term Phi^(7A)L_s by the same T_W relation before taking the legitimate half.
The complete local error is

    (X_s(T_W)/2)bar
      =phi^A Kbar L_sbar/H_0
       +phi^(6A)(M_sbar+Kbar^4D_K)
       +phi^(4A)(C_0^2Psi^A Kbar(chi)+Kbar^4w^2)
                                           in B_phi.     (MT10)

The first term is exactly the changing-divisor contribution; dropping it would change the obstruction.
All denominators are units in B_phi.
Every displayed term has order at least4A, but this divisibility alone is not the square-image condition.

### MT5: exact necessary-and-sufficient square image and both signs

The polynomial quotient L_sbar/phi^(3A) is taken in F_2[X] before entering the local ring.
Define the fully calculated class

    eta_s=(L_sbar/phi^(3A))/(H_0 Kbar^3)
       +phi^(2A)(M_sbar/Kbar^4+D_K)
       +C_0^2Psi^A Kbar(chi)/Kbar^4
                                  modulo phi^(3A).       (MT11)

Cancel the exact factor phi^(4A) in MT10 against modulus phi^(7A) and divide by the unit Kbar^4.
Together with the already vanishing other primaries and first residual, this proves

    F(T_W)=X_s(T_W)=0 modulo4
       if and only if w^2=eta_s modulo phi^(3A).          (MT12)

Thus the fixed coefficient class T_W modulo4 admits such a shared W exactly when eta_s belongs to the Frobenius-square image of F_2[X]/phi^(3A).
Equivalently eta_s'=0 in that same ring, since3A is even: choose its degree<6A representative, whose derivative can be divisible by phi^(3A) only if it is identically zero, then take its polynomial square root.
The derivative is independent of representative because(phi^(3A))'=0.

When soluble, the square root fixes precisely w modulo phi^(3A/2).
The other primary components and all higher permitted coefficients are free.
Consequently among the2^d monic coefficient classes T_W modulo8 above the fixed T modulo4 there are EXACTLY2^(d-3A) simultaneous solutions; otherwise there are none.
This is an exact fiber count for the SAME actual residuals, not a statistical model.

The two signs have equivalent solvability conditions.
Their divided residual errors differ by cbar^3=a_bar^3 globally, and a_bar=(phi^A Kbar)^2.
Therefore the solution translation is

    w_for_minus=w_for_plus+phi^A Kbar modulo U.          (MT13)

It adds a valid degree<d coefficient class and changes the correction by exactly a_bar^3.
The first residual stays zero.
Equivalently eta_-+eta_+=(phi^A Kbar)^2 modulo phi^(3A), a square.
This relates solutions for opposite signs; it does not assert that the same W solves both signs.

### MT6: a discriminating pair with the SAME U and full formal gate

Let j be the least ODD integer at least A/2, so A/2<=j<A for every even A>=2.
Put

    Lbar=J_H X^(j-A/2),
    K_1=K_0+Phi^(3A)L,

Here L is the coefficient0/1 integer lift of the displayed polynomial, and K_0 is the coefficient0/1 lift of the unique CRT representative of degree<6A+degJ_H in MT2.
Both K_i satisfy the SAME root congruence modulo phi^(3A), the same J_H condition and the degree bound in MT2.
Indeed degK_1<6A+degH_0+A/2<d-2A.
They give the same U, old support, low derivative, actual reduction classes a_bar,b_bar,c_bar, and any additional specified C649 full gate and integer-layer data.
The first residual is zero modulo4 for every W in either class; the two classes differ only in allowed actual coefficients of T modulo4.
They are distinct: their difference is2Phi^(4A)L, whose nonzero reduction after dividing by2 has degree below d.

For a fixed sign, compare their EXACT eta classes from MT11.
Modulo phi^(2A), the difference of the first terms is zero: the numerator C_0^3+Kbar^6 changes first at order6A, which becomes order2A after division by phi^(4A), while its denominator change is still higher.
The middle term already has the factor phi^(2A).
The last term gives

    eta_s(K_1)+eta_s(K_0)
       =C_0^2Psi^(4A)Lbar(chi)/K_0bar^4
                                       modulo phi^(2A).  (MT14)

The multiplier is a SQUARE unit.
At X=0 the polynomial Lbar has exact leading term X^j, with j odd, since J_H/X^(A/2) has constant1.
Using chi'=phi^2, the derivative of Lbar(chi) has exact phi-order2j.
Terms in phi^(2A) have derivatives still in phi^(2A), because2A is even.
Consequently

    ord_phi(eta_s(K_1)+eta_s(K_0))'=2j<2A.              (MT15)

Their difference is NOT a square class modulo phi^(3A).
Thus they cannot both satisfy MT12.
By MT13 the criterion is sign-independent, so at least one of these two completely specified modulo4 coefficient classes has NO integer correction4W solving the two residuals modulo4 for EITHER sign.
This is a uniform all-A certificate against automatic lifting of every full-formal-gate coefficient class, without a native test or an unproved numerical seed.
It does not identify which class fails without calculating its actual eta, and does not exclude existence of a different soluble K.

### MT7: precision, hypothesis and realization limits

The criterion is for actual monic integer T and both coefficientwise canonical residuals modulo4, with their full shared correction.
It is stronger than merely checking the local formal gate, but it does not assert that the gate is insufficient for EXISTENCE of SOME choice of K; that separate existential question remains open here.
Neither the synthetic integer G_int nor the formal local root was substituted for the actual c or a in the calculation.
Even a successful MT12 gives neither the C202 modulo8 conditions, nor the C603 first error, nor the characteristic-zero residual equations or an original irreducible totally real trace input.
All original A,q, degrees and integer layers must retain their actual roles in any application.
No new original A_0 exclusion, unrestricted realization or Task completion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T01:55 |
| status | open |
| reason | Register the complete actual SAME-T modulo4 calculation, global factorized base and all-primary conditions, exact first-residual solution, integer second-error and necessary-and-sufficient square image, sign translation/fiber count, and the uniform two-class nonautomatic-lift certificate. No native scan, existential failure for every K, modulo8 or characteristic-zero realization is claimed. Fresh isolated whole mathematical review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual modulo4 theorem](#statement) | S1--S11, actual even A and complete U, fixed integer lifts and monicity, actual canonical quotients on every primary, exact divisions and square-image equivalence, both signs/counts, the complete pair certificate and all original limits. |
| argument | [Whole same-input calculation](#argument) | MT1--MT15, factorized half-difference, nilpotent-half ideals and local-to-global coefficient detection, root precision, same-divisor a/c expansions, exact error and polynomial half, derivative square test, signs, degree bounds and non-square pair difference. |
| support | [Generic integer half-difference](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Exact Delta_2 and product/additive rules, actual theta2 dependence on T modulo4; all needed uses are checked directly here. |
| support | [Whole-support local module](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | Earlier localized monic free-module and quotient precision mechanism, without assuming a full original realization. |
| support | [Exact changing-divisor identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | The actual SAME-T coefficient correction mechanism; the present modulo4 layer and explicit second error are proved at their stated scope. |
| support | [Actual dyadic coefficient](Yin_C_G0603_v1.md#argument) | FE8's calculation and precise module-half principle, rechecked here before asserting first-residual vanishing; FE4/FE5 are not assumed to vanish. |
| support | [Full formal support and corrected gate](Yin_C_G0649_v1.md#statement) | Application interface only: exact old support/root and low derivative, plus fixed optional full gate; the theorem directly assumes every used polynomial property. |
| support | [Global canonical candidate](Yin_C_G0667_v1.md#statement) | Conditional source of polynomial U/Y data at its own selected review state, not a premise of the self-contained generic calculation or an original realization. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:12 |
| status | proved |
| reason | Adopt the complete actual SAME-T modulo4 theorem through fresh isolated whole R889 after reading every statement/proof section and the entire review. For every admissible fixed K the exact eta square-image test is necessary and sufficient for one shared correction, with exact fiber count and sign translation. At least one of the two specified coefficient classes fails for either sign; another soluble K remains possible. Actual exponents, all primary components and the full changing-divisor half remain essential. No modulo8, characteristic-zero or unrestricted conclusion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual modulo4 theorem](#statement) | S1--S11, actual even A and complete U, fixed integer lifts and monicity, actual canonical quotients on every primary, exact divisions and square-image equivalence, both signs/counts, the complete pair certificate and all original limits. |
| argument | [Whole same-input calculation](#argument) | MT1--MT15, factorized half-difference, nilpotent-half ideals and local-to-global coefficient detection, root precision, same-divisor a/c expansions, exact error and polynomial half, derivative square test, signs, degree bounds and non-square pair difference. |
| support | [Generic integer half-difference](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Exact Delta_2 and product/additive rules, actual theta2 dependence on T modulo4; all needed uses are checked directly here. |
| support | [Whole-support local module](Yin_C_G0197_v3.md#quadratic-primary-local-mod4-bridge) | Earlier localized monic free-module and quotient precision mechanism, without assuming a full original realization. |
| support | [Exact changing-divisor identity](Yin_C_G0202_v1.md#integrality-and-changing-divisor) | The actual SAME-T coefficient correction mechanism; the present modulo4 layer and explicit second error are proved at their stated scope. |
| support | [Actual dyadic coefficient](Yin_C_G0603_v1.md#argument) | FE8's calculation and precise module-half principle, rechecked here before asserting first-residual vanishing; FE4/FE5 are not assumed to vanish. |
| support | [Full formal support and corrected gate](Yin_C_G0649_v1.md#statement) | Application interface only: exact old support/root and low derivative, plus fixed optional full gate; the theorem directly assumes every used polynomial property. |
| support | [Global canonical candidate](Yin_C_G0667_v1.md#statement) | Conditional source of polynomial U/Y data at its own selected review state, not a premise of the self-contained generic calculation or an original realization. |
| review | [Fresh independent whole finding](../audits/reviews/Yin_R_G0889_v1.md#whole-same-coefficient-mod-four-finding) | Entire S1--S11 and MT1--MT15, every actual even A, all-primary canonical residuals, exact changing-divisor half, square-image iff/count, both signs and complete two-K negative certificate. |

