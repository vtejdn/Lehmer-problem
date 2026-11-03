---
author: Yin
---
# Exact minimal-radius signed-binomial profiles and a coefficient-subclass Mahler bound

Date: 2026-10-12T10:28.
Human author Yin.
Internal fixed extraction under the continuing G0001 instruction.
Root supplied the substantive central-coefficient/restricted-binomial/completion candidate; rounding_recovery authored the complete original D10 proof.
The ENTIRE original account is retained below.
g0001_routes independently whole-reviewed that18:14 proof in R263 and NOW authors this registered statement/wrapper.
This new contribution bars the extractor from independently reviewing the actual extraction.
Root and the original author are also proof contributors.
A distinct noncontributor actual extraction finding remains required before adoption.

## Statement

Let P(t)=sum_(j=0)^(2s)a_j t^j be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial, original degree d=2s>=2.
Thus a_0=a_(2s)=1 and a_j=a_(2s-j).
Use actual K=Q(alpha), O0=Z[alpha], sigma(alpha)=alpha^-1 and full Norm_K(alpha)=1.
No absence of unit-circle roots is assumed.
Write m(P)=sum_(P(beta)=0)log max(1,|beta|).

A half-profile has finite positive normalized rational weights lambda_b and nonzero INTEGER atoms f_b with actual nonzero values u_b=f_b(alpha) in O0, such that

    G(t)=sum_b lambda_b f_b(t)f_b(t^-1),
    sum_b lambda_b=1, G(alpha)=1/2.

The COMPLETE restricted class considered here uses only signed monomials +/-t^i,0<=i<=s, and binomials eta t^i+xi t^j with DISTINCT exponents0<=i<j<=s and coefficients eta,xi in{+1,-1}.
All allowed signs and positions, with positive rational weight repetitions/splits, are permitted; zero-weight types are omitted.
A coefficient2 monomial, repeated exponent, higher-term polynomial or nonprimitive multiple is outside this class.
Every allowed atom has degree<=s<d, so its actual integer value is nonzero.

**A. General minimal radius and the zero-central-coefficient boundary.**
No normalized half-profile of arbitrary nonzero INTEGER atoms can have physical common coefficient-window width less than s.
If a_s=0, even the WHOLE arbitrary-integer-atom class in allowed width s is empty.
These statements precede the two-term restriction and use the actual minimal polynomial, not a numerical selected embedding.

For a_s!=0 put epsilon=sign(a_s) and

    H(t)=epsilon t^-s P(t)
        =h+sum_(l=1)^s h_l(t^l+t^-l),
    h=|a_s|>0, h_l=epsilon a_(s+l),
    S=sum_(l=1)^s|h_l|>=1, h_s=epsilon,
    H_max=max_(|z|=1)H(z)>=h>0.

The ACTUAL radius of H is s.
The following conclusions use this nonzero-central-coefficient case.

**B. Exact restricted-class existence, every symbol and attained minimum.**
A half-profile in the COMPLETE restricted class exists if and only if

    2h>=3S.

When this holds, ALL its possible circle symbols are precisely

    G=1/2+cH,
    c in Q, 1/[2(h-S)]<=c<=3/(2h).

Every rational c in this CLOSED interval is attained by an explicit finite positive rational packet after zero labels are omitted.
Every such symbol has actual Laurent radius s and actual common coefficient union width s.
The minimum circle maximum in this restricted class is attained and equals

    C_bin(P)=1/2+H_max/[2(h-S)]
             <=(2h+S)/[2(h-S)]<=4.

For s>1 this is NOT asserted to be the optimum over arbitrary integer atoms of degree<=s or over the whole degree<d half-profile class.

**C. Complete minimizing class and all ACTUAL initial costs.**
Let M0=2(h-S),c0=1/M0.
Every minimizing profile has total binomial weight |h_l|/M0 at each gap l with h_l!=0, entirely of coefficient product sign(h_l).
No binomial occurs at a zero h_l, and no opposite-sign cancellation occurs at an active gap.
Its total monomial weight is(2h-3S)/M0.
Conversely EVERY allowed finite positive rational split among these signs/positions/types minimizes.
The canonical profile is

    f_l=1+sign(h_l)t^l, weight |h_l|/M0 for h_l!=0,
    f_0=1, weight (2h-3S)/M0 if positive.

At2h=3S there is no monomial label.
The canonical ACTUAL initial coefficient denominator is1, all atoms are primitive, and its ACTUAL least initial weight denominator is M0 because |h_s|1 supplies weight1/M0.
For a noncanonical rational minimizing split its ACTUAL least weight denominator M_profile is a multiple of M0.

Retain the FULL SIGNED degree-d integers

    D_l=Norm_K(1+sign(h_l)alpha^l)
       =Res(P,1+sign(h_l)t^l)!=0.

All signed monomials have full norm+1.
Every same-gap/same-product-sign binomial has exactly the signed norm D_l, including shifted or sign-reversed labels.
For ANY minimizing rational split,

    product_b Norm_K(u_b)^(M_profile lambda_b)
      =product_(l:h_l!=0)D_l^(M_profile|h_l|/M0),
    Lambda_initial=(1/d)sum_b lambda_b log|Norm_K(u_b)|
      =(1/(d M0))sum_(l:h_l!=0)|h_l|log|D_l|>=0.

No D_l is assumed positive or a unit; every integer copy and content is retained.
These are INITIAL profile weights and norms.
The nonzero lag-s symbol is not yet complementary and is not assigned the final original-root inequality.

**D. Actual-radius finite completion, FINAL costs and restricted-subclass gap.**
Choose any minimizing profile above, x=2G-1=2c0H, and the rational circle bound C4, so x(circle) is contained in[-1,7].
The adopted C43 whole-interval theorem gives a rational polynomial p of actual degree1<=e<=5 with

    p(0)=1, p'(0)=-1/2,
    R(X)=[1-(1+X)p(X)^2]/X^2 in Q[X],
    R(X)>1/98 for EVERY X in[-1,7].

This includes the endpoint X=-1 and the polynomial value at0.
Put K_rem=R(x)/2, of ACTUAL radius L<=(2e-1)s, and use C34 at that L to choose fixed positive rational d_a and ordinary rational g_a of degree<=L with K_rem=sum_a d_a g_a g_a*.
Write Z_a=xg_a and D_sum=sum_a d_a>0.
For EVERY positive rational rho, define

    v_b=p(x)f_b, K_(a,+/-)=Z_a/rho+/-1,
    delta=rho^2 D_sum,
    omega_b=lambda_b/(1+delta),
    omega_(a,+/-)=d_a rho^2/[2(1+delta)].

Every final value is a NONZERO actual O0 integer: original labels retain u_b and repaired labels have values+/-1.
The final weights are positive rational, sum1 and give ALL-lag constant covariance

    E'=(1/2+delta)/(1+delta).

For finite rho=1/N with delta<=1, one has1/2<E'<=3/4, and with profile/filter/Gram FIXED these energies tend to1/2 as N grows.
No limiting packet or bounded denominators is asserted.
The original filtered supports lie in[-es,(e+1)s], the complete repair supports in[-s,s+L], and ALL labels lie in[-es,2es].
ONE common shift therefore gives ACTUAL physical width

    T<=3es<=15s=15d/2.

This local support count uses the actual radius s and includes all repair constants and factors; it does not use C52.

At EACH finite rho retain actual least coefficient denominator q, actual least FINAL weight denominator M_w, positive copies n_b=M_w omega_b and full signed original norms N_b.
Original norms remain their D_l or1; repair norms are+1 because d is even.
The common monomial has norm1.
With integer numerators F_b=qV_b of the finally shifted polynomials,

    Res(P,F_b)=q^d N_b,
    product_b Res(P,F_b)^(n_b)=q^(d M_w)product_b N_b^(n_b),
    S_int=sum_b omega_b||F_b||_2^2=q^2 E',
    Lambda_final=(1/d)sum_b omega_b log|N_b|
                 =Lambda_initial/(1+delta),
    I=log q+Lambda_final,
    Lambda_final-(1/2)log E'
       =I-(1/2)log S_int<=(T/d)m(P)<=(3e/2)m(P).

For content g_b, the factor g_b^d in Res(P,F_b) and divisibility g_b^d | q^d N_b remain; no primitive-content discount is taken.
FINAL multiplicities are not the old initial copies.
No upper q/M_w/height bound is claimed.
Taking only the scalar limit of these actual finite inequalities gives

    m(P)>=[log2+2Lambda_initial]/(3e)
         >=[log2+2Lambda_initial]/15>=log2/15.

This is a gap for the EXPLICIT coefficient-defined subclass2h>=3S, with the declared restricted profile construction, not an unrestricted selector.

**E. Exact controls and remaining domain.**
For the OLD family P_A=t^2-A t+1, integer A>=3, this recovers C39's already accepted

    C_bin=1+3/[2(A-1)],
    M0=2(A-1), D_1=2-A,

with the same complete minimizing signed1,t,1-t profiles, initial q1 and canonical copied signed product2-A.
C39 supplies full integer-class optimality for THIS degree-one family; it is not inferred for s>1.

For the ACTUAL boundary quartic

    P=t^4+t^3-3t^2+t+1,
    H=3-(t+t^-1)-(t^2+t^-2), h3,S2,M0=2,

the mod2 irreducible polynomial proves actual irreducibility.
The trace polynomial y^2+y-5 has one root in(1,2) and one below-2, giving a genuine unit-circle pair and a real reciprocal pair off the circle.
Thus no no-circle hypothesis is imposed.
The canonical profile is1-t and1-t^2 at weights1/2, with no monomial.
It has G(1)=0, so x=-1 is actually attained, while

    H_max=21/4, C_bin=25/8,
    initial q1, M_profile2, contents1,
    full signed norms1,-3, copied signed product-3,
    Lambda_initial=log3/8.

The resulting valid bound is m(P)>=[log2+(log3)/4]/15.
This is a hand control of the restricted optimum, not a new full-profile optimum or a near-one family.

Every ACTUAL reciprocal flat polynomial is outside this selector: either a_s0 and A applies, or h1,S>=1 and2h>=3S fails.
This says nothing negative about wider radii, higher-term atoms or unrestricted half-profiles.
All source, finite construction, initial/FINAL cost and noncompletion boundaries are retained in the full argument.
Unrestricted G0001 remains unresolved.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:28 |
| status | open |
| reason | Register the exact complete restricted-class theorem, all symbols and minimizers, initial and FINAL costs, actual-radius completion, coefficient-subclass gap and circle-endpoint control. Entire original proof/history is preserved. R263 covers only the original18:14 whole account; its reviewer now contributes this new wrapper, requiring a distinct noncontributor actual extraction finding before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual reciprocal domain, general minimal-radius/central-zero floor, complete restricted-class theorem and all costs/controls/limits. |
| argument | [Entire original proof](#argument) | ENTIRE original D10 starting scope/reuse, Sections1--9/theorem/equations1--19, initial/FINAL arithmetic, both controls, source/contribution history and18:14 freeze. |
| dependency | [Actual whole-interval filter](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | Accepted rational prescribed-jet polynomial for actual integer half-profiles and full interval[-1,7], with no no-circle, unit-only or uniform-selector assumption. |
| dependency | [Actual-radius rational Gram](Yin_C_G0034_v1.md#statement) | Strictly positive rational self-star K_rem at actual radius L, positive rational weighted ordinary squares degree<=L; no denominator bound. |
| dependency | [Accepted complete paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | All nonzero values, FINAL normalized weights and exact covariance; smaller actual-s support is counted locally. |
| dependency | [Full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY after complementarity, with same FINAL weights, nonzero full signed resultants and actual physical width. |
| support | [Old complete degree-one theorem](Yin_C_G0039_v1.md#integer-square-mass-weak-certificate-and-degree-one) | Existing whole-integer mass/equality result, credited as the s1 predecessor. |
| support | [Old actual quadratic optimum](Yin_C_G0039_v1.md#quadratic-full-integer-circle-profile-optimum) | Accepted full integer-profile optimum only for P_A,A>=3, with actual initial denominator and signed norms. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0263_v1.md#central-binomial-whole-independent-finding) | ENTIRE original18:14 D10 and its exact accepted-input interfaces only; no prospective new statement/extraction acceptance. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:35 |
| status | proved |
| reason | Adopt the independently performed whole-author finding and separate actual fixed-extraction/interface finding at their precise scopes. Preserve the complete restricted-class proof, all finite original costs, boundary control and contribution history. This is a coefficient-subclass result, not higher-degree full-profile optimality or unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual reciprocal domain, general minimal-radius/central-zero floor, complete restricted-class theorem and all costs/controls/limits. |
| argument | [Entire original proof](#argument) | ENTIRE original D10 starting scope/reuse, Sections1--9/theorem/equations1--19, initial/FINAL arithmetic, both controls, source/contribution history and18:14 freeze. |
| dependency | [Actual whole-interval filter](Yin_C_G0043_v2.md#chebyshev-damping-actual-domain-and-statement) | Accepted rational prescribed-jet polynomial for actual integer half-profiles and full interval[-1,7], with no no-circle, unit-only or uniform-selector assumption. |
| dependency | [Actual-radius rational Gram](Yin_C_G0034_v1.md#statement) | Strictly positive rational self-star K_rem at actual radius L, positive rational weighted ordinary squares degree<=L; no denominator bound. |
| dependency | [Accepted complete paired repair](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width) | All nonzero values, FINAL normalized weights and exact covariance; smaller actual-s support is counted locally. |
| dependency | [Full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY after complementarity, with same FINAL weights, nonzero full signed resultants and actual physical width. |
| support | [Old complete degree-one theorem](Yin_C_G0039_v1.md#integer-square-mass-weak-certificate-and-degree-one) | Existing whole-integer mass/equality result, credited as the s1 predecessor. |
| support | [Old actual quadratic optimum](Yin_C_G0039_v1.md#quadratic-full-integer-circle-profile-optimum) | Accepted full integer-profile optimum only for P_A,A>=3, with actual initial denominator and signed norms. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0263_v1.md#central-binomial-whole-independent-finding) | ENTIRE original18:14 D10 and its exact accepted-input interfaces only; no prospective new statement/extraction acceptance. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0265_v1.md#c56-central-binomial-actual-extraction-finding) | Actual A--E, complete retained argument/preservation and all current direct interfaces, independent of original authors and wrapper contributor. |

## Registration and preservation

Date: 2026-10-12T10:28.
The assigned extractor retains the ENTIRE original D10 body with only short author-front-matter removal, first-title demotion, exact relative Claim-link rebasing and terminal whitespace normalization.
Every substantive proof, theorem, equation, cost, control, bounded-reuse/source/contribution disclosure and18:14 freeze remains.
Historical pending-review and C52 chronology are retained at their original scope; C52 supplies no premise here.
R263 stays independent for the old whole proof, while authoring this new registered statement makes its reviewer a contributor to the actual extraction.
A different noncontributor must review the actual statement, preservation and interfaces.
No native mathematical execution, new source acquisition, target-proof repair or adoption is performed by this registration.
Root owns later acceptance, consumer/index work and any retirement of the original draft.

## Argument

## Minimal-radius signed-binomial half-profiles and central coefficient dominance

Date: 2026-10-12T10:08.
Human author Yin.
New bounded AUTHOR inquiry under root-coordinated G0001.
Root supplied the substantive central-coefficient, restricted-binomial, exact-circle-cost and local-radius completion candidates; this author reconstructs the complete proof or precise failure.
Both are contributors and neither can independently review this account.

## Question and scope

For an ACTUAL monic irreducible reciprocal nontorsion integer-unit minimal polynomial of degree 2s, determine exactly when a normalized finite positive rational half-profile built from signed monomials and signed two-term polynomials at distinct exponents in [0,s] exists, and its exact minimum circle maximum within that COMPLETE restriction.
Retain actual nonzero original values, full signed norms, contents, q_initial=1, actual initial and FINAL weight denominators, and physical windows.
Do not treat coefficient-2 monomials as binomials.
Reuse the degree-one C39 theorem directly, without claiming it as new.
If accepted C43 filtering applies, locally count support at radius s; C52 is not adopted as a proof premise.
No native computation, new source or adoption belongs to this author assignment.

## Initial reuse screen

The adopted C39 exact integer-square mass, degree-one equality and quadratic half-profile optimum were read, alongside C43's actual filter/paired-repair/support/norm account and C10's full original-root bound.
Bounded Claims/ledger searches by central coefficient dominance, signed binomial half-profile and monomial/binomial normalization found the exact s=1 predecessor and other different energy/congruence results, but no existing general central-dominance classification.
This bounded screen supplies no novelty or priority claim.
The necessary new steps are finite coefficient matching and actual support accounting from these adequate local inputs; no new source theorem is required.

<a id="central-binomial-domain-and-reuse"></a>
## 1. Actual domain, exact reuse and the restricted class

The author read [C39](Yin_C_G0039_v1.md#statement), including its degree-one whole-integer mass and exact quadratic profile optimum; [C43 v2](Yin_C_G0043_v2.md#statement) and its [complete filtering/Gram/repair account](Yin_C_G0043_v2.md#chebyshev-damping-gram-repair-and-width); and the [C10 full original-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality).
The positive Gram step uses the already adopted [C34](Yin_C_G0034_v1.md#statement) at its actual radius, not a new factorization claim.
The new C52 selector was initially read as a candidate and root subsequently reported its exact adoption; this proof does not depend on C52 and locally reconstructs the smaller support count needed here.
The degree-one result below is explicitly a reuse/control of C39, not a new discovery.
No external source theorem, exhaustive novelty search or native program is needed for the remaining finite coefficient calculation.

Let P(t)=sum_(j=0)^(2s) a_j t^j be the ACTUAL monic irreducible self-reciprocal nontorsion integer-unit minimal polynomial, of original degree d=2s>=2.
Thus a_0=a_(2s)=1 and a_j=a_(2s-j).
Work in K=Q(alpha), actual O0=Z[alpha] and sigma(alpha)=alpha^-1.
Reciprocity gives this actual field involution, while monicity and a_0=1 give alpha,alpha^-1 in O0 and Norm_K(alpha)=1, as in C10.
No absence of unit-circle roots is assumed.

An actual half-profile here is a finite family of nonzero integer polynomials f_b, positive rational weights lambda_b summing to one and

    G(t)=sum_b lambda_b f_b(t) f_b(t^-1),
    G(alpha)=sum_b lambda_b u_b sigma(u_b)=1/2,
    u_b=f_b(alpha) in O0 minus {0}.                 (1)

The COMPLETE restricted class in this account requires every atom to be either a signed monomial +/-t^i, 0<=i<=s, or a signed binomial eta t^i+xi t^j, 0<=i<j<=s, eta,xi in {+1,-1}.
The two exponents are distinct.
A coefficient-2 monomial, a repeated exponent, a trinomial and a denominator-cleared nonprimitive multiple are not members of this class.
Positive rational repetitions/splits are permitted, and a type with zero total weight is omitted.
Every allowed polynomial has degree<=s<d and therefore has actual nonzero integral value by minimality.
No test of norm size is substituted for that degree/order fact.

Assume first a_s!=0.
Choose epsilon=sign(a_s), and put

    H(t)=epsilon t^(-s)P(t)
        =h+sum_(l=1)^s h_l(t^l+t^(-l)),
    h=|a_s|>0, h_l=epsilon a_(s+l),
    S=sum_(l=1)^s |h_l|>=1, h_s=epsilon in {+1,-1}.
                                                            (2)

All h,h_l,S are integers and the ACTUAL radius of H is s.
The letter H denotes this centered minimal polynomial, not the positive Gram remainder in Section 6.
Write H_max=max_(|z|=1)H(z); it is a real number and H_max>=h>0 by averaging.

<a id="central-binomial-exact-theorem"></a>
## 2. Complete restricted-class theorem

**Theorem.**
In the domain above:

1. A half-profile made of arbitrary nonzero INTEGER atoms cannot have common coefficient-window width less than s.
   In the width-s restricted class of Section 1, existence holds exactly when

       2h>=3S.                                     (3)

   If a_s=0, the whole integer-atom class of allowed width s is empty, not merely the signed-binomial subclass.

2. When (3) holds, ALL possible circle symbols in the restricted class are precisely

       G=1/2+cH,
       c in Q, 1/[2(h-S)]<=c<=3/(2h).              (4)

   Their actual Laurent radius and their actual common coefficient union width are s.
   The smallest circle maximum in this COMPLETE restricted class is attained and equals

       C_bin(P)=1/2+H_max/[2(h-S)]
          <=(2h+S)/[2(h-S)]<=4.                    (5)

   This is not an assertion of optimality over arbitrary integer atoms of degree<=s, or over the full degree<d half-profile class.

3. Put M0=2(h-S), c0=1/M0.
   Every minimizing profile has, for each l with h_l!=0, TOTAL binomial weight |h_l|/M0 at gap l, and all of those binomials have coefficient product sign(h_l).
   No binomial occurs at h_l=0 and no opposite-sign cancellation occurs at any gap.
   Its TOTAL signed-monomial weight is

       (2h-3S)/M0.                                 (6)

   Conversely every such finite positive rational split among allowed signs/positions/types minimizes.
   In particular a canonical realization uses

       f_l=1+sign(h_l)t^l, weight |h_l|/M0,
       f_0=1, weight (2h-3S)/M0 if positive.        (7)

   At equality 2h=3S no monomial label is included.
   There is no negative or zero weight hidden in the construction.

4. The canonical profile has ACTUAL initial coefficient denominator 1 and ACTUAL least initial weight denominator M0.
   All its atoms are primitive.
   For an arbitrary rational minimizing split, the actual weight denominator M_profile is a multiple of M0, and its full signed copied norm product is exactly the one in (12) below.

5. Applying the adopted C43 whole-interval filter and locally counting the radius-s supports gives ACTUAL finite complementary rational packets with full nonzero integral values, all lags zero, energy E' decreasing to 1/2 through finite choices and physical common width T<=15s.
   Every original norm, numerator content, coefficient denominator and FINAL weight is paid in (16)--(18) below.
   Consequently every ACTUAL input satisfying (3) has the restricted-subclass gap

       m(P)>=(log2)/15,                            (8)

   with the norm-income refinement in (19).
   This conclusion includes possible unit-circle roots but imposes the explicit coefficient condition (3); it does not solve unrestricted G0001.

<a id="central-binomial-minimal-radius"></a>
## 3. Minimal radius and exact coefficient necessity

First let a finite normalized profile of arbitrary nonzero integer polynomials have one common allowed window [0,r].
Its constant coefficient is

    G_0=sum_b lambda_b ||f_b||_2^2>=1,              (9)

because every integer atom has positive integer energy.
If r<s and G(alpha)=1/2, then t^r(G-1/2) is a rational polynomial of degree<=2r<d that vanishes at alpha.
Minimality forces it to be identically zero, contradicting (9).
A common Laurent shift does not alter any f f* and preserves nonzero integer values, so this proves the physical-window version as well.

Now allow r=s.
The polynomial t^s(G-1/2) has degree<=d and vanishes at alpha.
It is a rational scalar multiple of P.
For a_s=0, this forces G_0=1/2, again contradicting (9).
For a_s!=0 it forces G=1/2+cH for a rational c, and (9) implies c>0.
In particular its lag-s coefficient is c h_s!=0, so its radius is EXACTLY s.

In the restricted class write b_l^+ and b_l^- for total weights of binomials at gap l with coefficient product +1 and -1, respectively, and B_bin=sum_l(b_l^++b_l^-).
A monomial has square symbol 1 and a binomial has symbol 2+eta xi(t^l+t^-l).
Thus normalized weights give the EXACT identities

    G_0=1+B_bin,
    b_l^+-b_l^-=c h_l,
    B_bin=c h-1/2,
    cS<=B_bin<=1.                                 (10)

No coefficient signs, shifts or repeated gaps are lost: absolute values of the net lag coefficients give the first inequality, while the second uses the actual total weight.
Hence c(h-S)>=1/2 and ch<=3/2.
Feasibility forces h>S and c0<=c<=3/(2h).
This interval is nonempty exactly when h<=3(h-S), or 2h>=3S.
These deductions concern the complete allowed atom class, with no inventory cutoff beyond the stated two-term restriction.

<a id="central-binomial-sufficiency-optimum"></a>
## 4. Sufficiency, every symbol and all minimizing profiles

Assume 2h>=3S, so M0=2(h-S)>0.
In (7), the positive binomial weights have sum S/M0<=1 and the displayed monomial weight is exactly 1-S/M0>=0.
The identity

    (1+delta t^l)(1+delta t^-l)=2+delta(t^l+t^-l)

shows that their symbol is 1+c0S+c0 sum_l h_l(t^l+t^-l).
Since c0(h-S)=1/2, this is exactly 1/2+c0H.
Evaluating at alpha gives (1), and degree<=s<d proves nonzero actual integer values of every label.
This establishes sufficiency without Gram factorization or an existence relaxation.

For completeness, every rational c in (4) is also attained.
Start with binomial weights c|h_l| of sign(h_l) at each nonzero gap, totaling cS.
Add an opposite-sign pair of gap-one binomials with total weight

    b_extra=c(h-S)-1/2>=0,

split equally, omitting the pair when zero.
These two symbols have opposite lag-one terms, so they add no net lag.
Total binomial weight becomes ch-1/2<=1.
Add the constant monomial with weight 3/2-ch when positive.
All weights are rational and nonnegative, sum one and give the symbol 1/2+cH.
Coinciding types may be kept as separate indexed labels.
Gap one is available since s>=1.
This proves the converse part of (4), including both endpoints.

Because c>0, the circle maximum of 1/2+cH is 1/2+cH_max.
The positive number H_max makes this strictly increasing in c.
Hence c=c0 is necessary and sufficient for the minimum (5).
At c0, (10) forces

    sum_l(b_l^++b_l^-)=sum_l|b_l^+-b_l^-|=c0S.

Each summand's excess is nonnegative, so equality forces no opposite signs at any nonzero gap and no binomial mass at a zero gap.
This proves exactly the minimizing classification in the theorem.
The actual gap-s coefficient is nonzero; at allowed width s, only a binomial with exponents 0 and s has this gap.
At least one such label is present, so the actual union width is s, also for split minimizers.

Finally H(z)<=h+2S on the circle, so

    C_bin(P)<=1/2+(h+2S)/[2(h-S)]
             =(2h+S)/[2(h-S)]<=4.                 (11)

The last inequality is exactly 2h>=3S.
No positivity of H is assumed: H may change sign, and the symbol G may vanish at some circle points when the monomial weight is zero.
The later C43 filter covers the entire interval starting at x=-1 and therefore includes this endpoint.
A no-circle restriction would be unnecessary here.

<a id="central-binomial-initial-norms-and-weights"></a>
## 5. Initial actual integers, complete norms, contents and least weights

All polynomials in the initial restricted class have integer coefficients with content one, so their actual coefficient denominator is q_initial=1.
The canonical weight at gap s is 1/M0 because |h_s|=1.
All other canonical weights have denominator dividing M0, proving that its ACTUAL least initial weight denominator is exactly M0, including the endpoint with no monomial.
The integer copied counts are |h_l| for each binomial and 2h-3S for the constant when present; their sum is M0.

Set delta_l=sign(h_l) for h_l!=0 and retain

    D_l=Norm_K(1+delta_l alpha^l)
       =Res(P,1+delta_l t^l) in Z minus {0}.

These are FULL SIGNED degree-d norms, not trace norms or selected-root products.
Their nonvanishing follows from l<=s<d and the actual minimal polynomial.
All signed monomials have full norm +1 because d is even and Norm_K(alpha)=1.
Every signed binomial at the same gap/sign product differs from 1+delta_l t^l by a signed monomial factor, also of full norm +1; it therefore has exactly the same signed norm D_l.

For any rational minimizing split, let M_profile be the actual least denominator of its individual weights.
The total weight of gap-s labels is 1/M0, so M_profile/M0 is an integer.
Its complete signed copied product and norm income are therefore

    product_b Norm_K(u_b)^(M_profile lambda_b)
       =product_(l:h_l!=0) D_l^(M_profile |h_l|/M0),
    Lambda_initial=(1/d)sum_b lambda_b log|Norm_K(u_b)|
       =(1/(d M0))sum_(l:h_l!=0)|h_l|log|D_l|>=0.
                                                            (12)

This equality keeps all positive rational splits and every integer copy.
In the canonical case M_profile=M0 and the exponents are |h_l|.
None of the D_l is assumed to be a unit, positive, or numerically bounded across inputs.
No normalization of an initial polynomial by its field value or its norm is performed.
The profile is not yet complementary: its nonzero lag-s coefficient is c0 h_s.
Hence the original-root complementary inequality is not applied to this initial packet.

<a id="central-binomial-local-completion"></a>
## 6. Actual-radius completion reconstructed from accepted C43

Use any minimizing profile above and its exact circle bound C=4.
Set x=2G-1=2c0H.
It is a rational self-star Laurent polynomial of ACTUAL radius s, vanishes at every original root and has x(z) in [-1,7] on the circle because G is a nonnegative sum of squares and G<=4.
By the adopted C43 whole-interval theorem with B=7 there is a rational polynomial p with actual degree e satisfying

    1<=e<=ceil(sqrt8)+2=5,
    p(0)=1, p'(0)=-1/2,
    R(X)=[1-(1+X)p(X)^2]/X^2 in Q[X],
    R(X)>1/(2*7^2) for -1<=X<=7.                  (13)

This invokes C43 at its actual accepted statement; it does not reprove its Chebyshev construction or use its separate scalar-degree lower-bound source.
The quotient is an exact polynomial, including at X=0.
Its degree is 2e-1: the leading term of (1+X)p^2 has degree 2e+1 and nonzero coefficient.
In particular e>=1 follows independently from the nonzero prescribed derivative.

Let v_b=p(x)f_b and K_rem=R(x)/2.
Then K_rem is strictly positive on the whole circle, and the exact identity is

    1/2-sum_b lambda_b v_b v_b*=x^2 K_rem.

Apply C34 at the ACTUAL radius L of K_rem, with L<=(2e-1)s, to obtain a finite rational identity K_rem=sum_a d_a g_a g_a*, d_a>0, and ordinary rational g_a of degree<=L.
Put Z_a=x g_a, D_sum=sum_a d_a>0.
For any positive rational rho, use repaired coordinates

    K_(a,+)=Z_a/rho+1, K_(a,-)=Z_a/rho-1,
    delta=rho^2 D_sum,
    omega_b=lambda_b/(1+delta),
    omega_(a,+/-)=d_a rho^2/[2(1+delta)].           (14)

The final weights are positive rational and sum one.
Every v_b has actual value u_b because p(0)=1, and the repaired coordinates have actual values +1 and -1 because x(alpha)=0.
Pair expansion gives exact constant covariance

    sum_final omega V V* = E'=(1/2+delta)/(1+delta).
                                                            (15)

Take rho=1/N with an integer N large enough that delta<=1.
Then 1/2<E'<=3/4.
Keeping the chosen profile, filter and finite Gram fixed while N grows supplies individually admissible finite packets with E' tending to 1/2.
It does not assert a limiting packet or fixed denominators.

Here the smaller actual radius is counted locally.
Since f_b is supported in [0,s], p(x)f_b is supported in [-es,(e+1)s].
The remainder factors give Z_a and both repaired coordinates in [-s,s+L], contained in [-s,2es].
Because e>=1, EVERY original and repaired label lies in [-es,2es].
A single common monomial translates the actual union minimum to zero; its physical span satisfies

    T<=3es<=15s=15d/2.                             (16)

This accounts for the repair constants, both signs, rational approximation already contained in the actual C43 polynomial and every Gram polynomial at its ACTUAL radius.
No separate monomial shifts, degree d-1 substitution, cancellation of support endpoints or C52 premise is used.
Norm(alpha)=1 makes the common monomial's signed full norm +1.

<a id="central-binomial-final-costs-and-gap"></a>
## 7. Full completion costs and the restricted-subclass gap

For EACH finite positive rho let q be the actual least coefficient denominator of the finally shifted rational polynomials V_b, let F_b=qV_b be their integer numerators, let M_w be the actual least denominator of the FINAL weights omega_b and let n_b=M_w omega_b be their positive integer multiplicities, summing to M_w.
Put N_b=Norm_K(V_b(alpha)), retaining every original conjugate.
Initial labels retain the signed norms of their u_b; repair labels have norm +1 because d is even.
Consequently

    Res(P,F_b)=q^d N_b,
    product_b Res(P,F_b)^(n_b)
         =q^(d M_w) product_b N_b^(n_b),
    S_int=sum_b omega_b ||F_b||_2^2=q^2 E',
    Lambda_final=(1/d)sum_b omega_b log|N_b|
         =Lambda_initial/(1+delta)>=0,
    I=log q+Lambda_final.                          (17)

The root norms of the initial classes D_l in (12) now carry their FINAL weights, divided by 1+delta; their earlier raw multiplicities are not reused as final ones.
No upper bound on q, M_w or numerator coefficients is claimed.
If g_b is a numerator's content, its exact resultant factor g_b^d and divisibility g_b^d | q^d N_b remain in (17); the numerator is not silently made primitive.
These are actual full integer quantities at every finite rho.

Apply the adopted C10 original-root inequality ONLY after (15):

    Lambda_final-(1/2)log E'
      =I-(1/2)log S_int <= (T/d)m(P)
      <=(3e/2)m(P).                                (18)

For the fixed actual profile/filter/Gram let positive rational rho decrease to zero.
Every finite term obeys (18), Lambda_final tends to the known nonnegative Lambda_initial, and E' tends to 1/2.
Thus

    m(P)>=[log2+2 Lambda_initial]/(3e)
          >=[log2+2 Lambda_initial]/15
          >=log2/15.                               (19)

This is a scalar limiting inference from actual finite packets: if it failed, a sufficiently small finite rho would already contradict (18).
No width-cap reversal on an unconstructed object, source infimum attainment, packet at rho=0 or uncharged limit of integer norms enters.
Formula (19) is a coefficient-defined subclass bound, not an input-uniform selector for arbitrary reciprocal polynomials.
Inputs failing (3), including a_s=0, remain outside this construction; failure of this particular class does not refute other half-profiles or unrestricted G0001.

<a id="central-binomial-controls-and-limits"></a>
## 8. Old quadratic control and a circle-root boundary control

For the OLD actual family P_A=t^2-A t+1, integer A>=3, take s=1, H=A-t-t^-1, h=A, S=1.
The formulas give c0=1/[2(A-1)] and

    C_bin=1/2+(A+2)/[2(A-1)]
         =1+3/[2(A-1)].

Its minimizing signed 1,t,1-t classification, canonical denominator 2(A-1), binomial norm 2-A and full signed product 2-A are exactly C39's ALREADY adopted result.
C39 proves optimality in the whole initial integer class in this quadratic case; our general theorem asserts that wider optimality only by this explicit reuse when s=1, not by extrapolation to s>1.

For a hand boundary control with actual circle roots, consider

    P=t^4+t^3-3t^2+t+1,
    H=3-(t+t^-1)-(t^2+t^-2), h=3, S=2, M0=2.

This P is irreducible over Q: modulo 2 it is t^4+t^3+t^2+t+1, with no root in F2, and the only possible irreducible quadratic factor would be t^2+t+1; its square is t^4+t^2+1, not this polynomial.
Hence no degree-one or degree-two factor exists modulo 2, proving irreducibility of the monic integer polynomial.
Writing y=t+t^-1 gives P=t^2(y^2+y-5).
The trace roots are (-1+sqrt21)/2 in (1,2) and (-1-sqrt21)/2<-2.
The first supplies a unit-circle pair; the second supplies a real reciprocal pair with one modulus greater than one.
Thus the input is an actual reciprocal nontorsion unit and no no-circle hypothesis can describe this example.

At the exact boundary 2h=3S, the canonical profile consists of 1-t and 1-t^2, each at weight 1/2, with no monomial label.
Its symbol G=1/2+H/2 vanishes at t=1, so x=-1 is genuinely attained.
Formula (13) explicitly covers this endpoint.
On the circle y in [-2,2], H=5-y-y^2 has maximum 21/4 at y=-1/2; therefore the exact restricted optimum is

    C_bin=25/8<4.

Both initial values are nonzero.
Their full signed norms are P(1)=1 and P(1)P(-1)=-3, since Norm(1-alpha^2)=Norm(1-alpha)Norm(1+alpha).
The canonical coefficient denominator is 1, weight denominator 2, contents 1 and complete copied signed product -3; Lambda_initial=log3/8.
Equation (19) therefore gives the valid restricted bound m(P)>=[log2+(log3)/4]/15 for this particular input.
These are hand calculations, not an executed scan or a new full-profile optimum.
No assertion is made that this example minimizes total measure within the coefficient-defined subclass.

The coefficient restriction leaves a substantial uncovered class.
If the actual reciprocal minimal polynomial is flat, all coefficients in {0,+1,-1}, then either a_s=0 or h=1 and S>=1.
The first case has the general radius-s impossibility, while the second violates 2h>=3S.
Thus this minimal-radius signed-binomial class covers NO such flat input.
This is a failure of the stated restricted selector, not a refutation of a wider-radius or higher-term integer profile.
It is consistent with C29's different first-window diagonal-covariance obstruction and with previously accepted unrestricted qualitative existence.

<a id="central-binomial-entire-author-freeze"></a>
## 9. Complete author self-check and frozen handoff

The author checked the actual reciprocal unit/involution/monogenic domain; the restriction to distinct exponents and coefficients exactly +/-1; the integer constant-coefficient floor and general minimal-radius argument; the a_s=0 case, sign of c, exact net-lag equations and feasibility interval; the constructive realization of every rational c, including omitted zero weights; exact circle maximum, no-cancellation equality classification, gap-s support and endpoint denominator; every initial signed full norm, primitive content, rational split and copied exponent; the C43 whole interval including x=-1, exact filter degree and remainder, C34 actual-radius assumptions, positive Gram factors and paired nonzero repair; all final weights, physical supports, one common shift, scalar/weight denominators, full signed resultants and contents; the valid finite-to-scalar limit giving (19); the inherited quadratic scope and every identity, irreducibility/root-domain fact and full norm in the boundary quartic; and the exact flat-input failure boundary.
No source claim, full-profile optimality for s>1 or unrestricted Task conclusion is being inferred.

The COMPLETE Sections 1--9, Theorem in Section 2 and equations (1)--(19), including both controls, source/reuse/contribution and all original cost distinctions, are AUTHOR-FROZEN at 2026-10-12T10:14.
Root supplied the substantive candidate and this author reconstructed it; both are contributors and cannot supply the whole independent review.
This is a complete proof draft with author self-check, awaiting a separately organized whole noncontributor review and later root-controlled registration/adoption if warranted.
The existing C39 quadratic theorem is reused, not newly asserted as a project contribution.
Scoped material checking passed for the preceding full proof and is repeated after this freeze; those checks concern structure and locators, not mathematical correctness.

This assignment used no native mathematical program, solver, enumeration, new J or new source acquisition.
Root retains actual adoption responsibility.
G0001 remains active and unrestrictedly unresolved; the next local step is the whole review of this frozen body.
