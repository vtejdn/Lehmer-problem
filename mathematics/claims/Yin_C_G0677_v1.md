---
author: Yin
---

# Exact high-coefficient correction of the first modulo-eight residual

Human author Yin.
Root derived the exact linear change of the adopted C603 first quarter, the bounded global correction preserving the full modulo4 class condition, and the application to the paid canonical families.
This is new author mathematics and initially open for fresh isolated whole review.
The active [G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
The complete adopted C669, C671 and C672 interfaces and actual C603 first-quarter formula were read before this deduction.
The separate full second-quarter C675 is not a premise and is not claimed solved here.
No native computation, parameter scan or external source theorem is used.

## Statement

Let A>=2 be even, Phi=X^2+X+1 over Z, phi=Phi mod2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic square prime to Xphi, satisfying Y|Y(chi), Y|Y(X^3+X).
Put H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A and C_0=X^A Y(chi)Psi^(7A), and assume

    H_0^6=C_0^21 modulo phi^(4A), h>=14A.                (HC1)

Choose fixed monic integer lifts of every irreducible factor of H_0, with full even exponents N_psi and P_X=X, and set

    mathcal_H=product_psi P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_psi psi^(N_psi/2), j_H=h/2,
    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A).

For actual integers K,W of degrees below d-2A and d respectively put

    T=mathcal_H Phi^(7A)+2Phi^A K+4W,
    a=rem_T(T(X^2-2))/2,
    b=rem_T(T(X^3-3X))/3,
    c=rem_T(T(X^5-5X^3+5X))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

All congruences below are coefficientwise congruences of these actual canonical integer remainders.
The selected sign s is fixed.
Suppose k=Kbar and w=Wbar satisfy

    k^11=H_0C_0^2 modulo phi^(4A), J_H|k,
    [X^i]k=0 for odd A/2<=i<3A/2,
    F(T)=X_s(T)=0 modulo4.                              (HC2)

This strengthened-root starting family is nonempty for every polynomial input HC1: take the unique CRT k equal to the eleventh root modulo phi^(4A) and zero modulo J_H X^A, lift it coefficientwise, and then choose W by adopted C672.
Its initial K has degree below j_H+9A<d-2A.

Use the exact first-quarter definitions

    mathcal_H C^2+3K^11=Phi^(3A)L_F+2M_F, degM_F<6A,
    D_K=((K(X^2-2)-K^2)/2)bar+k^2,
    O_F=(F(T)/4)bar in B_phi=F_2[X]/phi^(7A).

The adopted C603 formula is

    O_F=phi^A k L_Fbar/H_0^2
       +phi^(2A)k^9 w^2/H_0
       +phi^(3A)k^10 w/H_0
       +phi^(4A)(M_Fbar+k^9D_K)/H_0.                    (HC3)

The stronger root implies O_F in phi^(2A) B_phi.
Define the UNIT

    A_F=C_0^2+phi^(4A)k^8 w^2 in B_phi.                 (HC4)

For any integer L with J_H X^A dividing ell=Lbar and degL<h+4A, put

    K_new=K+Phi^(4A)L,
    T_new=mathcal_H Phi^(7A)+2Phi^A K_new+4W.            (HC5)

Then the full modulo4 residual condition HC2 is preserved with the SAME W, and the exact first-quarter change is LINEAR:

    O_F(T_new)=O_F(T)+phi^(2A) A_F ell/H_0
                                            in B_phi.  (HC6)

Consequently choose the unique CRT class with

    ell=H_0 A_F^(-1)(O_F/phi^(2A)) modulo phi^(5A),
    ell=0 modulo J_H X^A,
    degell<j_H+11A<=h+4A,                               (HC7)

and lift it coefficientwise to an integer L.
This is a globally valid correction, and it gives

    F(T_new)=0 modulo8, X_s(T_new)=0 modulo4.            (HC8)

No second-residual modulo8 solution is asserted.
For the fixed starting K,W, among all reductions ell of degree below h+4A divisible by J_H X^A, exactly

    2^(h-j_H-7A)=2^(h/2-7A)                             (HC9)

give HC8 by this construction; every such reduction gives a distinct T_new modulo4.
These finite classes always exist because h>=14A.
Every integer representative of a qualifying ell that respects the degree bound preserves both congruences in HC8; no integer coefficientwise8-divisibility of its change is presumed.

### Actual canonical application

Choose the C667 complete representative by its prescribed Y_pre B_n^3 construction, with n>30L_0 and L_0 the least power of2 at least8m+1.
Then degY_0>=3(n-1)/2>=45L_0>360m, hence degY_0>=26m.
For EVERY q=2^k>=2 use

    A=2mq, Y=Y_0^q,
    h=q(2m+degY_0), d=q(30m+degY_0).

Thus h>=14A, and HC1--HC8 give an actual monic integer T of the SAME degree d and reduction U_0^q for which the first residual vanishes modulo8 and the second modulo4.
This applies to both C668v2 families with their already paid representative construction and all existing degree bounds; no additional polynomial degree or change of original q is required.
The characteristic-two canonical R, full root/gate, actual maximal q and all integer layers remain attached to the unchanged U.
Neither the second modulo8 residual nor G_int=G_can, characteristic-zero identities, irreducibility, total reality or an original realization follows.

## Argument

### 1. Starting roots, actual degrees and complete quarters

Because H_0 and C_0 are phi-units and the unit group modulo phi^(4A) has only prime divisors2 and3, the eleventh-power map is bijective.
Its unique root can be combined with zero modulo J_H X^A, since the two moduli are coprime.
Their product degree is8A+j_H+A=j_H+9A< h+12A=d-2A.
The coefficientwise lift K has this actual degree.
Its low X^(3A/2) divisibility gives every odd coefficient condition in C672, while the stronger root includes the required3A root.
Adopted C672 then supplies an actual W of degree below d satisfying both modulo4 residuals for either chosen sign.
This proves nonemptiness without presuming any modulo8 condition.

For any such starting pair, actual monic division gives the even remainder2M_F in HC3.
The reduction of its quotient is

    L_Fbar=(H_0 C_0^2+k^11)/phi^(3A).

HC2 makes the numerator divisible by phi^(4A), so phi^A divides L_Fbar.
Every term of the complete HC3 therefore lies in phi^(2A).
The quotient O_F/phi^(2A) is consequently well-defined modulo phi^(5A).
The leading term C_0^2 in A_F is a unit, making A_F a unit at the same and larger displayed precision.
All divisions in HC7 are thus legal in their indicated quotients.

### 2. The complete modulo4 condition survives with the same W

The degree restriction on L gives

    deg(Phi^(4A)L)<8A+h+4A=h+12A=d-2A.

Thus K_new and T_new have the same allowed bounds and T_new is monic of degree d.
The factor J_H in ell preserves the global J_H constraint, and the higher phi^(4A) change preserves the stronger root modulo phi^(4A).
Also J_H X^A includes X^(3A/2), so the low forbidden coefficients of K are unchanged.

More than the solvability criterion is preserved: the same W remains a solution.
Use the exact full C671 variation of the C669 error for delta K=Phi^(3A)L_1 with L_1=Phi^A L.
Its reduction gives

    eta_s(K_new)+eta_s(K)
      =phi^(4A)(k/H_0)ell^2+Omega Psi^A ell(chi)
                                           modulo phi^(3A),
    Omega=C_0^2Psi^(4A)/k^4.

The first term vanishes at that modulus.
Since X^(3A/2)|ell, its composition with chi is divisible by phi^(3A), so the second term vanishes too.
This is equality of the complete eta classes, not just equality of their derivatives.
C669's all-primary iff therefore preserves both actual modulo4 residuals with exactly the same W for the fixed sign.
No free a,b,c coordinate or separate residual correction has been substituted.

### 3. Exact linear change of the first quarter

Write delta=phi^(4A)ell and k_new=k+delta.
The integer difference3(K_new^11-K^11) is divisible by Phi^(4A), hence by Phi^(3A), so the actual remainder M_F is unchanged EXACTLY.
In the characteristic-two polynomial domain,

    k L_Fbar=(H_0 C_0^2 k+k^12)/phi^(3A).

For k+delta the numerator difference is H_0 C_0^2 delta+(k+delta)^12+k^12.
The twelfth-power difference starts with k^8 delta^4, then k^4 delta^8 and delta^12, because12 has binary digits1100.
After division by phi^(3A) and multiplication by the outer phi^A of HC3, all those terms have order at least14A, so they vanish modulo phi^(7A).
The ENTIRE first-term change is thus

    phi^(2A) C_0^2 ell/H_0.

The change of k^9 is k^8 delta plus terms of order at least8 times the order of delta.
Its contribution to the second HC3 term is exactly

    phi^(6A) k^8 w^2 ell/H_0 modulo phi^(7A).

The change of k^10 begins with delta^2, so the third HC3 term does not change at this precision.
Changes of k^9 in the fourth term have order at least8A after its outer phi^(4A), and hence vanish.

For completeness the half-difference D_K is not held artificially fixed.
The actual additive and product rules, and evenness of4A, give

    D_(K+Phi^(4A)L)+D_K
       =phi^(8A)Delta(L)bar+phi^(4A)k ell+phi^(8A)ell^2.

Multiplication by the outer phi^(4A) in HC3 puts every one of these terms beyond7A.
Together with unchanged M_F this accounts for all of HC3, including every divided-remainder and changing-divisor contribution.
Adding the two surviving terms proves precisely HC6 with A_F as defined in HC4.
The identity is linear in ell at the FULL required precision; no iterative Hensel claim is needed.

### 4. Global construction, every primary and exact finite fibers

The moduli phi^(5A) and J_H X^A are coprime.
Their product degree is10A+j_H+A=j_H+11A.
HC1 gives j_H=h/2 and j_H+11A<=h+4A, so the CRT representative HC7 and its integer coefficient lift obey the actual permitted degree bound for L.
HC6 then makes O_F(T_new)=0 in the phi-primary quotient.
In every non-phi primary, adopted C669 gives a_bar=c_bar=0 for the actual T_new, since it is still in the same admissible polynomial family.
Thus a and c are even in the localized quotient modulo8, making 3a^5 and2c^2 both multiples of8 there.
The first residual therefore vanishes on EVERY primary modulo8.
The monic free module and its localizations detect global coefficientwise zero, proving the first half of HC8.
The second half was already proved globally in Section2.

All allowable reductions ell form the vector space of multiples of J_H X^A of degree below h+4A, of dimension h+3A-j_H.
Restriction to the phi^(5A) residue is onto because its CRT product degree is at most h+4A.
That residue has10A binary dimensions.
Every target residue has exactly2^(h-j_H-7A) preimages, proving HC9 including its zero-exponent endpoint.
Distinct such ell give distinct T_new modulo4, since their difference divided by2 is the nonzero polynomial phi^(5A)(ell_1+ell_0), whose degree is below d.

If L changes by2V, T_new changes by4Phi^(5A)V, not generally by8 as an INTEGER polynomial.
Nevertheless its modulo4 reduction is unchanged, and the first-quarter calculation above depends only on ell: the actual M_F remains unchanged under any Phi^(4A)L change and the reduced half-difference formula retains every possible integer lift.
Consequently HC8 holds for every integer representative of a qualifying ell that respects the degree bound, and the modulo4 second condition is unchanged by the actual C669 eta comparison.
No claim about invariance of the second quarter modulo8 is made.

### 5. Paid canonical degrees and remaining coupled obstruction

In the explicitly chosen C667 representative Y_0=Y_pre B_n^3, every factor is monic and degY_pre>=0.
Since n>30L_0, both n and30L_0+1 are odd and n-1>=30L_0.
Thus degY_0>=3(n-1)/2>=45L_0, with L_0>=8m+1.
This exceeds360m and in particular implies degY_0>=26m.
For every q>=2, the actual h=q(2m+degY_0) is at least28mq=14A.
Every hypothesis of HC1 follows from the adopted square canonical input, with the full exponents and actual degree d.
The high-coefficient correction changes no degree or reduction, so all original U/R, maximal-q, full formal gate, integer layer and paid-degree statements retain their exact scopes.
Both adopted C668 families use this paid representative and therefore satisfy this additional degree margin.

This establishes an actual next precision for the first residual while preserving the solved second residual modulo4.
It does not make the second residual vanish modulo8 or force the separate full second-quarter condition to hold.
Nor does it identify the actual integer canonical G_can with a chosen zero-Haar G_int or establish characteristic-zero residuals, irreducibility, total reality, original field-value nonvanishing or the original reciprocal realization.
There is no q1 claim or unrestricted Task conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:04 |
| status | open |
| reason | Register the exact full first-quarter linear change under a high K correction, preservation of the complete modulo4 eta with the same W, bounded global CRT construction and finite fibers. Every paid C667/C668 representative at q>=2 has enough degree margin, so its first actual residual can vanish modulo8 while the second remains solved modulo4. The second modulo8 equation and original characteristic-zero realization are not supplied. This is root author mathematics requiring fresh independent whole review; no native computation or new Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire high-coefficient correction](#statement) | HC1--HC9, every stated square input and degree margin, nonempty stronger-root bases, all actual K/W and global L constraints, exact linear quarter change, same-W modulo4 preservation, global first modulo8 solution, counts and paid canonical applications. |
| argument | [Complete exact correction proof](#argument) | Five sections, actual integer remainder and half-difference variations, characteristic-two12/9/10 powers with every order, whole eta preservation, bounded CRT/all-primary detection and full representative expenses. |
| dependency | [Adopted complete first quarter](Yin_C_G0603_v1.md#statement) | FE3--FE4 with the actual integer H,C,K,W and monic divisor, including the full changing-divisor term; no new claim to the original first-error formula. |
| dependency | [Adopted full modulo4 error](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | All-primary actual residuals, exact eta and integer halves, root consequence and global square-image iff. |
| dependency | [Adopted full coefficient variation](Yin_C_G0671_v1.md#decision-whole-reviewed-2026-10-24) | EK7 at deltaK=Phi^(3A)(Phi^A L), exact eta equality at full3A precision; not only derivative invariance. |
| dependency | [Adopted square-input construction](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Nonempty actual modulo4 bases from the strengthened CRT root and low coefficient zeros, all full exponents and every q>=2 canonical application. |
| support | [Paid canonical representative](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | The actual Y_pre B_n^3 choice and n>30L_0 supply the needed lower degree margin, with all unchanged U/R/q/layer/canonical costs. |
| support | [Both adopted canonical families](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Applications only, every large dyadic m and separate m14 at q>=2; existing upper costs remain valid because T degree is unchanged. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T03:18 |
| status | proved |
| reason | The entire fixed HC1--HC9 statement and five-section argument were directly read and checked against fresh isolated whole R898. Adopt the exact high-K correction preserving the same W and complete modulo4 eta, full first-quarter linearity, all-primary modulo8 conclusion, precise fibers and every integer lift, with both paid canonical-family applications and unchanged degrees. The second residual modulo8, G_int=G_can, characteristic-zero identities and unrestricted original realization remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire high-coefficient correction](#statement) | HC1--HC9, every stated square input and degree margin, nonempty stronger-root bases, all actual K/W and global L constraints, exact linear quarter change, same-W modulo4 preservation, global first modulo8 solution, counts and paid canonical applications. |
| argument | [Complete exact correction proof](#argument) | Five sections, actual integer remainder and half-difference variations, characteristic-two12/9/10 powers with every order, whole eta preservation, bounded CRT/all-primary detection and full representative expenses. |
| dependency | [Adopted complete first quarter](Yin_C_G0603_v1.md#statement) | FE3--FE4 with the actual integer H,C,K,W and monic divisor, including the full changing-divisor term; no new claim to the original first-error formula. |
| dependency | [Adopted full modulo4 error](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | All-primary actual residuals, exact eta and integer halves, root consequence and global square-image iff. |
| dependency | [Adopted full coefficient variation](Yin_C_G0671_v1.md#decision-whole-reviewed-2026-10-24) | EK7 at deltaK=Phi^(3A)(Phi^A L), exact eta equality at full3A precision; not only derivative invariance. |
| dependency | [Adopted square-input construction](Yin_C_G0672_v1.md#decision-whole-reviewed-2026-10-24) | Nonempty actual modulo4 bases from the strengthened CRT root and low coefficient zeros, all full exponents and every q>=2 canonical application. |
| support | [Paid canonical representative](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | The actual Y_pre B_n^3 choice and n>30L_0 supply the needed lower degree margin, with all unchanged U/R/q/layer/canonical costs. |
| support | [Both adopted canonical families](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Applications only, every large dyadic m and separate m14 at q>=2; existing upper costs remain valid because T degree is unchanged. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0898_v1.md#high-coefficient-first-quarter-whole-independent-finding) | Complete fixed statement, argument, exact input applicability, actual integer/global scope, every application and all stated limitations; the main agent read the complete finding before this adoption. |

