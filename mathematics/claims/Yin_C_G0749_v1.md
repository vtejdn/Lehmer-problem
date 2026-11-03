---
author: Yin
---

# Forced product reducibility and exact own-core canonical precision loss

Human author Yin.
The [selected G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
Provenance: project deduction from the exact integer factors and canonical systems of the adopted sources below.
Root proposed the exact integer factorization, reciprocal factor, use of the adopted cofactor identity to test the core's own canonical system, and the actual first-core half argument.
Earlier_bit_obstruction checked the complete actual degree and quotient maps, derived the direct own-core binary formulas and exact full-primary orders, and checked the reciprocal and Mahler consequences.
Root read the entire stable CF1--CF7 statement and proof, including the direct own-divisor formulas and exact first half.
Both are contributors, not independent reviewers.
The [D5 development](../drafts/Yin_D_G0005.md#exact-common-factor-and-own-core-obstruction) is provenance only; this fixed material includes the complete necessary argument and has no mutable-D dependency.
The actual source is [adopted C746](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25); the higher finite applications use the exact factor-preserving outputs of [adopted C748](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25).
The existing adequate algebraic input is [adopted C736 FT1--FT4](Yin_C_G0736_v1.md#ft1-exact-domain-and-canonical-factor-identity), which allows common factors and performs every prime division in the integers.
No new theorem about arbitrary irreducible factors is used or asserted.
This complete author theorem is initially open for fresh independent whole review.

## Statement

### CF1. Exact domain and statement

Use the full C746 parameter and source domain: kappa>=5, M=2^kappa, original dyadic q>=2^(M+kappa-3), a>=2 even, A=aq, H_b0=X^aY_b and H_b=X^a mathcal_Y_b.
Here Y_b is prime to Xphi, both full forward divisibilities Y_b|Y_b(chi) and Y_b|Y_b(lambda) hold, phi=X^2+X+1, chi=Xphi^2 and lambda=X^3+X.
Every full factor and its multiplicity are retained in the chosen monic integer H_b.
Write H_0=H_b0^q, h=q degH_b, d=h+14A, Phi=X^2+X+1 over Z and S=(H_bPhi^(7a))^(q/2).
The adopted source retains h>(9M+1)A and its full old8a and multiplicity-floor conditions; the structural deductions below use only their explicitly identified consequences.
Let T be an actual factor-preserving polynomial from the source or finite continuation, so

    T=S^2+2Phi^A K+4W,
    H_b^((1-1/M)q)|K, H_b^((1-2/M)q)|W over Z,
    degK<d-2A, degW<d,
    k^11=H_0 C_0^2 modulo phi^(4A),              (CF1)

where k=Kbar and C_0=X^A Y_b(chi)^q phi(chi)^(7A).
The last identity makes k a unit at phi because H_0 and C_0 are units there.
The unchanged actual S, integer factors and degrees, full binary forward divisibilities and this unit consequence are the only normalized data used in the proof below.
In particular no product residual congruence is a premise of the own-core calculation.

Put nu=q/M, r=q-2nu and define the ACTUAL integer quotients

    K_*=K/H_b^(q-nu), W_*=W/H_b^r,
    B=H_b^r,
    A_core=H_b^(2nu)Phi^(7A)
                  +2H_b^nu Phi^A K_*+4W_*.

Then T=B A_core is an exact integer factorization, both factors are monic of positive degree, and

    deg A_core=d_core=2h/M+14A.                  (CF2)

For any monic integer divisor P, write a_P=theta_2(P), b_P=theta_3(P), c_P=theta_5(P), using the actual divided remainders defined in CF3, and put

    F(P)=rem_P(2c_P^2-3a_P^5),
    G(P)=rem_P(c_P^3-2b_P^5),
    X_epsilon(P)=rem_P(b_P^2-a_P^3
                             +epsilon(c_P^3-2b_P^5)).

For this canonical system computed with A_core as its OWN divisor, the conclusions are

    ord_2 F(A_core)=1,
    ord_phi G(A_core)bar=12A/M,
    ord_phi X_epsilon(A_core)bar=12A/M,
                              epsilon=1 and epsilon=-1. (CF3)

The two displayed phi-orders are exact polynomial orders, equivalently exact orders in the full phi^(7A) component of the own binary quotient.
Here ord_2 of a nonzero integer polynomial is the minimum2-adic valuation of its coefficients.
In particular ord_2 X_1(A_core)=ord_2 X_(-1)(A_core)=ord_2 G(A_core)=0, while the first residual is even but not divisible by4.
The actual first-half identity is stated only modulo phi^A in CF5.
The explicit reciprocal and exact Mahler identities are proved in CF6 below.

## Complete argument

### CF2. Integer factorization, degrees and shared factors

The common integer divisor B divides S^2=H_b^q Phi^(7A), 2Phi^A K and 4W separately.
Their integer quotients give CF2 without a modular factor extraction or a change of S.
The actual degree bounds give

    degK_*<h/M+12A,
    degW_*<2h/M+14A=d_core.

Consequently 2H_b^nu Phi^A K_* has degree<d_core, whereas H_b^(2nu)Phi^(7A) is monic of degree d_core.
This proves the stated degree and monicity of A_core.
Since r>0 and degH_b>=a>0, both B and A_core have positive degree and T is reducible over Z.
The binary core divisor is exactly

    U_core=A_corebar=H_b0^(2nu)phi^(7A).         (CF4)

No integer coprimality of B and A_core is asserted.
Indeed their binary gcd is H_b0^(2nu), because r>=2nu and H_b0 is prime to phi.
The integer gcd may be different; no inference from that binary gcd is needed.
The full phi-primary component is F_2[X]/(phi^(7A)), since the complementary H_b0^(2nu) factor is a unit there.
All multiplicities in that component and in its complement are retained.

### CF3. Actual own-divisor maps before binary reduction

For each monic integer P and p in{2,3,5}, set

    P(C_p)=P Q_p(P)+p theta_p(P),
    theta_p(P)=rem_P P(C_p)/p,
    C_2=X^2-2, C_3=X^3-3X,
    C_5=X^5-5X^3+5X.

Frobenius modulo p makes the actual remainder coefficientwise p-divisible and Q_p(P)=P^(p-1) modulo p.
These are integer definitions before any dyadic reduction.
For P=A_core and T=B A_core, subtraction of the two actual divisions gives

    p(theta_p(T)-B(C_p)theta_p(A_core))
      =A_core(Q_p(A_core)B(C_p)-B Q_p(T)).

The bracket on the right is coefficientwise divisible by p: its reduction is A_core^(p-1)B^p-B(BA_core)^(p-1)=0.
Dividing that INTEGER bracket and canceling p in Z[X] gives the exact C736 identity

    [theta_p(T)]=[B(C_p)theta_p(A_core)]
                                      in Z[X]/(A_core). (CF5)

Thus a T-remainder can be reduced to this factor quotient, but it becomes a weighted own-core canonical value.
No coprimality or cancellation of B or A_core was used.
Every B(C_p) in CF5 is composed as a full integer polynomial, rather than by substituting into an arbitrary quotient class.
For p=3,5, subsequent reduction modulo2 commutes with the already completed odd division, whose scalar is1 in F_2.
For p=2 we instead use the genuine integer Delta(P)=(P(C_2)-P^2)/2, for which theta_2(P)=rem_P Delta(P).

### CF4. Direct own-core binary canonical values

Write

    S_core=H_b^nu Phi^(7A/2),
    P_core=H_b^nu Phi^A K_*,
    A_core=S_core^2+2P_core+4W_*.

These are integer polynomials because A is even.
The integer identities

    Delta(V^2)=2V^2Delta(V)+2Delta(V)^2,
    Delta(V+Z)=Delta(V)+Delta(Z)-VZ,
    Delta(2V)=V(C_2)-2V^2,
    Delta(4V)=2V(C_2)-8V^2

show directly that Delta(A_core)bar=P_corebar^2.
In the FULL binary quotient R_core=F_2[X]/(U_core), the own canonical classes therefore satisfy

    alpha=theta_2(A_core)bar
         =[phi^(2A)H_b0^(2nu)K_*bar^2],
    beta=theta_3(A_core)bar=[U_core(lambda)]=0,
    gamma=theta_5(A_core)bar=[U_core(chi)].      (CF6)

For beta, the full forward divisibility of Y_b and X|lambda give H_b0|H_b0(lambda), while phi|phi(lambda).
Raising those divisibilities to their actual exponents proves U_core|U_core(lambda), including every repeated factor.
It is not merely a vanishing statement at simple roots.
The reduction for gamma uses C_5bar=chi and the actual odd integer division in CF3.
Factoring the full composed polynomial gives

    U_core(chi)=phi^(4A/M) gamma_0,
    gamma_0=X^(2A/M)Y_b(chi)^(2nu)
                                     phi(chi)^(7A). (CF7)

The factor gamma_0 is a unit at phi: X is a unit there, chi=0 modulo phi, Y_b(0)=1 and phi(0)=1.
Also H_b0 is a unit at phi, and k=H_b0^(q-nu)K_*bar is a unit by CF1, so K_*bar is a unit there.
It follows in the full phi^(7A) component that

    ord_phi alpha=2A,
    beta=0,
    ord_phi gamma=4A/M.                         (CF8)

Both nonzero orders are strictly below7A, so they are well defined independently of representatives.
The argument proves the direct own-divisor formulas without assuming that division by the cofactor preserves any product precision.

### CF5. Cofactor orders and exact failure of second precision

The full cofactor weights in CF5 have binary phi-orders

    ord_phi B(C_2)bar=0,
    ord_phi B(C_3)bar=0,
    ord_phi B(C_5)bar=2ar=2A(1-2/M).             (CF9)

For C_2 this follows from H_b0(X^2)=H_b0(X)^2.
For C_3, lambda permutes the two roots of phi because lambda=X+1 modulo phi; H_b0 is nonzero at both roots.
For C_5, H_b0(chi)=X^a phi^(2a)Y_b(chi), with the other factors units at phi, proving the exact last order.
The full product canonical values at this component are

    theta_2(T)bar=phi^(2A)k^2,
    theta_3(T)bar=0,
    theta_5(T)bar=phi^(2A)C_0.                  (CF10)

The first formula follows by the same integer Delta calculation for T=S^2+2Phi^AK+4W; the odd formulas follow from U=H_0phi^(7A) and its full lambda/chi compositions.
CF5 and CF9 recover CF8, agreeing with the direct calculation.
For the nonunit C_5 weight, cancellation determines gamma only modulo phi^(7A-2ar), not modulo phi^(7A).
Nevertheless its exact order is2A-2ar=4A/M because the product has exact order2A<7A.
No stronger precision is obtained by that cancellation.

Define the core residuals using the OWN canonical integer polynomials and the OWN monic A_core remainder, exactly as for T.
Their binary classes in R_core are

    F(A_core)bar=alpha^5=0,
    G(A_core)bar=gamma^3,
    X_epsilon(A_core)bar=beta^2+alpha^3+gamma^3
                             =alpha^3+gamma^3. (CF11)

The first zero is global in R_core: the polynomial representing alpha^5 is divisible by H_b0^(10nu)phi^(10A), hence by U_core=H_b0^(2nu)phi^(7A).
Therefore the actual first core residual is coefficientwise even, allowing the legitimate integer half used below.
At phi, gamma^3 has exact order12A/M, while alpha^3 has exact order6A.
Since M>=32,

    0<12A/M<6A<7A,

so the leading gamma^3 term cannot cancel and both second signs give the same exact order12A/M.
Monic reduction by U_core subtracts a multiple of phi^(7A), which cannot change any of these strictly smaller orders.
Thus the canonical polynomial remainders themselves have the exact orders claimed in CF3, not just a chosen representative in a localization.
In particular both X_1(A_core) and X_(-1)(A_core) fail divisibility by2 and G(A_core) is nonzero.

To determine the exact first coefficient valuation, return to the actual integer canonical polynomials a_c=theta_2(A_core), c_c=theta_5(A_core) and the actual monic quotient Q_F,c defined by

    2c_c^2-3a_c^5=A_core Q_F,c+F(A_core).

The binary order of alpha implies a_c belongs to(2,Phi^A): its actual monic Phi^A remainder has even coefficients.
Hence a_c^5 belongs to(32,Phi^A), and the explicit integer core formula gives A_core=4W_* modulo Phi^A.
Reducing the displayed integer residual identity modulo(4,Phi^A) therefore gives

    F(A_core)=2c_c^2 modulo(4,Phi^A).

The quotient Z[X]/(Phi^A) is a free Z-module, with its canonical monic remainder basis.
Taking those actual integer remainders first, their difference is coefficientwise divisible by4.
As F(A_core) itself is even, divide that remainder identity by2 over Z and only then reduce modulo2 to obtain

    (F(A_core)/2)bar=gamma^2 modulo phi^A,
    ord_phi((F(A_core)/2)bar modphi^A)=8A/M<A.  (CF11a)

The exact order follows from CF7 and M>=32; its nonzero value proves that F(A_core)/2 is not coefficientwise even.
Thus ord_2 F(A_core)=1 exactly.
This is a legitimate half in the monic Phi^A module, with no cancellation of2 in a dyadic torsion quotient and no claim of a full A_core-quotient formula for the half.
No additional property of W_* or of the actual quotient Q_F,c is needed.

For comparison, the weighted product G has order3(2ar)+12A/M=6A at phi, consistent with the full-product value phi^(6A)C_0^3.
The product alpha cube also begins at6A, where the retained sixth-root identity can cancel it in the second residual.
That product cancellation occurs at different weights from the own-core system; it does not give the core a residual congruence.

### CF6. Reciprocal factors and exact Mahler bookkeeping

For any monic integer polynomial V of degree e, define its reciprocal trace lift by

    P_V(z)=z^e V(z+z^(-1)).

This is a monic integer polynomial of degree2e, constant coefficient1 and reciprocal coefficients.
The leading term of V supplies both extreme coefficients; all lower terms have exponents strictly between them.
Multiplication of these Laurent-polynomial expressions gives the exact polynomial identities

    P_T=P_(H_b)^r P_(A_core),
    P_(H_b)=(z^2+1)^a P_(mathcal_Y_b),
    P_T=(z^2+1)^(ar) P_(mathcal_Y_b)^r
                                              P_(A_core). (CF12)

Both factors P_(H_b)^r and P_(A_core) have positive degree, so P_T is reducible over Z as well.
The cyclotomic factor (z^2+1)^(ar) is an unavoidable displayed divisor; its exponent is a lower bound on the total multiplicity if the remaining factors also vanish at z=+i or z=-i.
No exact multiplicity beyond the displayed factor is assumed.

Using the Task's logarithmic Mahler measure, m(V)=log|lead(V)|+sum log max(1,|rho|), with every root rho counted with multiplicity, the root multiset of a product is the union of the factor multisets.
This directly proves additivity here, even for shared roots:

    m(P_T)=r m(P_(H_b))+m(P_(A_core))
          =r m(P_(mathcal_Y_b))+m(P_(A_core)).   (CF13)

The last equality uses that both roots of z^2+1 lie on the unit circle and its leading coefficient is1.
These are exact identities and degree statements only.
They provide neither a positive nor a small positive measure estimate, and impose no root-location or irreducibility conclusion on the core.

### CF7. Scope of the structural consequence

The adopted C746 BOTH8 output already gives an actual family to which every conclusion above applies.
For each separately fixed epsilon and every N>=1, take the factor-preserving constructed representative in adopted C748 GA18.
It has the full product residual precision2^N and all CF1 data, so it is reducible with the exact displayed factor and its core still has exact first/second coefficient valuations(1,0), for both own second signs.
All parameters, degrees and factors remain those paid by that actual construction.
This assertion concerns the factor-preserving representatives, not arbitrary elements of the unrestricted final coefficient fiber in C748.

The failure of precision transfer is for this explicitly defined core, and applies to both own residual signs of that core.
It does not assert that every irreducible factor of T, of the core or of the reciprocal polynomial fails its own residual conditions.
Further factor selection requires its own actual cofactor maps and residual compatibility.
The exact smaller degree and Mahler decomposition therefore do not turn the finite product construction into an irreducible near-one Mahler family or a characteristic-zero solution.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision forced-factor-own-core-precision-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:00 |
| status | open |
| reason | Register the complete forced common-factor and exact own-core precision theorem CF1--CF7 for the actual factor-preserving C746/C748 domain. The integer factorization T=H_b^r A_core has monic positive-degree factors and d_core=2h/M+14A; the full product and reciprocal lift are reducible, with no assertion that the core itself is reducible. Actual own-divisor canonical maps give coefficient valuations F=1, X_1=X_(-1)=G=0, exact binary phi-orders12A/M for G and both X, and exact first-half order8A/M only modulo phi^A. Every integer half, shared-factor and nonunit-cofactor limitation, full primary, reciprocal cyclotomic divisor and exact Mahler additivity is retained. The arbitrary finite application uses only the adopted factor-preserving constructed representatives with all original costs, not unrestricted endpoint fiber elements. Root and Earlier_bit_obstruction are contributors; fresh independent whole review remains outstanding. No arbitrary irreducible-factor obstruction, root/height or positive/small Mahler estimate, compatible limit, characteristic-zero realization or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete forced-factor and core-precision statement](#statement) | CF1 exact C746/C748 factor-preserving domain and CF1--CF3: actual factorization, degrees and core coefficient valuations; CF6--CF7 explicitly included reciprocal factor, exact Mahler identity and separate-sign/every-finite-N application with its source/fiber/irreducible-factor limitations. |
| argument | [Complete integer, own-divisor and reciprocal proof](#complete-argument) | Entire CF2--CF7 and CF4--CF13: actual factor/degree and shared-factor bounds; integer C736 quotient bracket; direct full binary alpha/beta/gamma calculation; exact cofactor orders with correctly reduced cancellation modulus; global binary first zero and genuine monic Phi^A half CF11a proving exact valuation1; both-sign second and G orders; reciprocal factor/measure identity and precisely scoped finite application. |
| dependency | [Adopted exact integer canonical cofactor identity](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 exact monic factor identity for p=2,3,5, including common/repeated factors and actual integer bracket division before modular reduction. CF3 states and checks that identity at A_core and B; no unit-compatibility or arbitrary factor-precision inheritance is assumed. Its example, irreducibility and other comparison scopes are not inputs. |
| dependency | [Adopted actual parameterized BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS0 and the complete original source/actual factor interface supply unchanged S, exact J_K/J_W integer divisibility, degree bounds, binary K root and full forward source at each kappa>=5, original q>=2^(M+kappa-3), old8a/floor2 and h>(9M+1)A. CF1 isolates the structural consequences actually used; no residual precision is needed to derive the core obstruction. GS5 conditional bookkeeping is not an input. |
| dependency | [Adopted finite-precision factor-preserving construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA4 retained exact factors, degrees, unchanged S and normalized roots, and GA18 separate-sign/every-finite-N constructed representatives, with their originally paid q/source/root/degree/derivative expenses and nonzero canonical G. Used only for the application in CF7; the elementary structural theorem does not establish new source existence or extend precision. Its unrestricted highest-correction fibers are expressly excluded unless the actual factor hypotheses separately hold. |
| support | [Task Mahler definition](../tasks/Yin_T_G0001_v1.md#contract) | Definition only: logarithmic Mahler measure includes the leading coefficient and every root with multiplicity. CF6 proves product additivity directly from this definition; no entropy equivalence or analytic gap bound is a premise. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:09 |
| status | proved |
| reason | Register the complete forced common-factor and exact own-core precision theorem CF1--CF7 for the actual factor-preserving C746/C748 domain. The integer factorization T=H_b^r A_core has monic positive-degree factors and d_core=2h/M+14A; the full product and reciprocal lift are reducible, with no assertion that the core itself is reducible. Actual own-divisor canonical maps give coefficient valuations F=1, X_1=X_(-1)=G=0, exact binary phi-orders12A/M for G and both X, and exact first-half order8A/M only modulo phi^A. Every integer half, shared-factor and nonunit-cofactor limitation, full primary, reciprocal cyclotomic divisor and exact Mahler additivity is retained. The arbitrary finite application uses only the adopted factor-preserving constructed representatives with all original costs, not unrestricted endpoint fiber elements. Adopt fresh independent whole R969 after inspecting its exact fixed-target bindings, complete reasoning and limitations. Root and Earlier_bit_obstruction remain proof contributors; the context-isolated reviewer contributed no repair. The complete CF1--CF7 statement and argument, including CF11a and all source/fiber restrictions, passed. No arbitrary irreducible-factor obstruction, root/height or positive/small Mahler estimate, compatible limit, characteristic-zero realization or unrestricted G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete forced-factor and core-precision statement](#statement) | CF1 exact C746/C748 factor-preserving domain and CF1--CF3: actual factorization, degrees and core coefficient valuations; CF6--CF7 explicitly included reciprocal factor, exact Mahler identity and separate-sign/every-finite-N application with its source/fiber/irreducible-factor limitations. |
| argument | [Complete integer, own-divisor and reciprocal proof](#complete-argument) | Entire CF2--CF7 and CF4--CF13: actual factor/degree and shared-factor bounds; integer C736 quotient bracket; direct full binary alpha/beta/gamma calculation; exact cofactor orders with correctly reduced cancellation modulus; global binary first zero and genuine monic Phi^A half CF11a proving exact valuation1; both-sign second and G orders; reciprocal factor/measure identity and precisely scoped finite application. |
| dependency | [Adopted exact integer canonical cofactor identity](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT4 exact monic factor identity for p=2,3,5, including common/repeated factors and actual integer bracket division before modular reduction. CF3 states and checks that identity at A_core and B; no unit-compatibility or arbitrary factor-precision inheritance is assumed. Its example, irreducibility and other comparison scopes are not inputs. |
| dependency | [Adopted actual parameterized BOTH8 source](Yin_C_G0746_v1.md#decision-whole-reviewed-2026-10-25) | GS0 and the complete original source/actual factor interface supply unchanged S, exact J_K/J_W integer divisibility, degree bounds, binary K root and full forward source at each kappa>=5, original q>=2^(M+kappa-3), old8a/floor2 and h>(9M+1)A. CF1 isolates the structural consequences actually used; no residual precision is needed to derive the core obstruction. GS5 conditional bookkeeping is not an input. |
| dependency | [Adopted finite-precision factor-preserving construction](Yin_C_G0748_v1.md#decision-whole-reviewed-2026-10-25) | GA1--GA4 retained exact factors, degrees, unchanged S and normalized roots, and GA18 separate-sign/every-finite-N constructed representatives, with their originally paid q/source/root/degree/derivative expenses and nonzero canonical G. Used only for the application in CF7; the elementary structural theorem does not establish new source existence or extend precision. Its unrestricted highest-correction fibers are expressly excluded unless the actual factor hypotheses separately hold. |
| support | [Task Mahler definition](../tasks/Yin_T_G0001_v1.md#contract) | Definition only: logarithmic Mahler measure includes the leading coefficient and every root with multiplicity. CF6 proves product additivity directly from this definition; no entropy equivalence or analytic gap bound is a premise. |
| review | [Fresh independent whole forced-factor and own-core review](../audits/reviews/Yin_R_G0969_v1.md#whole-forced-factor-core-precision-pass) | Entire fixed statement and argument CF1--CF7, displayed CF1--CF13 including the genuine first half CF11a, exact input decisions and all source, finite, fiber, factor and analytic limits; independently reviewed with declared exact bindings. Accepted C746/C748 input interfaces were checked without a new whole audit of their transitive proofs. |

