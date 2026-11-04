---
author: Yin
---
# Complete composition density and a refined finite norm character

Human author Yin.
Root proposed the iterated-Theta density mechanism and identified the distinction between the generic finite norm condition and the complete finite image.
The same_trace contributor checked the all-precision density, proved the even norm character and its improved lift-independent finite precision, and derived the explicit uniform countercontrol and the three exact finite kernel identifications.
Both are mathematical contributors; neither independently reviews this new theorem.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Focused reuse inspected the adopted formal-unit/norm theorem C652, the complete divisor/composition identities C608/C609v2, and the adopted entire finite images C621v2/C640/C651.
The new argument proves density and precision analytically; no new native program, support scan, target execution or larger quotient is used.
The [D1 continuation](../drafts/Yin_D_G0001.md#complete-factor-density-and-sharp-norm-candidate) is development provenance, not a logical input.
This statement is initially open for fresh isolated whole mathematical review.

## Statement

Work over F_2, put phi(X)=1+X+X^2 and chi(X)=Xphi(X)^2, and let x(t) be the formal inverse of chi at0.
For positive odd n let B_n be the complete trace polynomial of all nonidentity n-th roots, one trace per inverse pair, with B_1=1.
For odd n>1 let W_n be its primitive-order version, so

    B_n=product_(d dividing n,d>1)W_d,
    W_5=phi, B_(5n)=phi B_n(chi).

All orders and multiplicities below are arbitrary unless a finite precision is specified explicitly.
Let U=1+tF_2[[t]] and use the adopted C652 homomorphism

    Theta(h)=h(t)^5/h(chi(t)),
    ell:U->Z_2, ker ell=Theta(U), ell(1+t)=1.

Its exact identities ell(phi)=-1 and ell(h(x))=ell(h)/5 are part of that adopted input.

### Density and removal of every finite composition factor

Put e_0=1+t and e_(j+1)=Theta(e_j).
Then

    e_j=1+t^(2j+1)+higher terms, j>=0,                      (D1)

and every u in U has a UNIQUE convergent expression

    u=product_(j>=0)e_j^(a_j), a_j in Z_2.                 (D2)

Each e_j is a finite rational product of odd-index B_n.
Consequently these B_n generate a dense subgroup of U and generate every low-X unit quotient modulo X^N, for every N>=1.

Define

    R_N=F_2[X]/chi(X)^N=F_2[X]/(X^Nphi^(2N)),
    G_N=group generated in R_N^* by all W_n,
                  n odd,n>1,n!=5.

Equivalently G_N is the set of classes of finite products of those W_n with nonnegative integer multiplicities.
For every h in U and EVERY N>=1,

    h(chi) modulo chi^N belongs to G_N.                    (D3)

There is no bound on the degree or support orders of the resulting complete polynomial representative.
In particular, if Y,H are polynomials with Y prime to Xphi, H(0)=1 and YH(chi) a complete product of the allowed W_n, then

    Y modulo chi^N belongs to G_N for every N.             (D4)

This is a finite membership statement; it does not assert that Y or H individually has a global complete-factor factorization.

### The normalized character at the original finite precision

Let A_high be the free rank4 high algebra over F_2[[t]] obtained by factoring chi(X)-t into its simple root x(t) and its complementary monic factor reducing to phi^2.
It identifies with the phi-adic completion of F_2[X], with base parameter t=chi(X).
Write V=A_high^* and let N_high,Tr_high be its algebraic norm and trace.
The full completed unit group is U times V, with the first component written as a series u(X) at X=0.
For g=(u,v) define

    Phi(g)=ell(N_high(v))-(4/5)ell(u).                      (D5)

This is the character of the full norm ratio N_chi(g)(t)/u(t), since its simple-branch norm is u(x(t)).
For EVERY completed unit g, Phi(g) lies in2Z_2.
Thus

    Pi(g)=Phi(g)/2                                        (D6)

is a well-defined continuous surjective homomorphism to Z_2.
The closure of the full allowed complete-factor group is contained in ker Pi.
No converse at all precisions is asserted.

For every N>=1, Pi induces a well-defined surjective homomorphism on the ORIGINAL finite quotient

    Pi_N:R_N^* -> Z/(2^floor(log_2 N)),
    G_N subset ker Pi_N.                                 (D7)

The target for N=1 is the trivial group.
Equivalently Phi is determined modulo the least power of2 STRICTLY greater than N by the class modulo chi^N.
This conclusion requires no unknown higher coefficient of either primary component and no extension to a larger quotient.
The kernel in (D7) has exact index2^floor(log_2 N).
A minimal-conductor assertion beyond this established precision is not made for arbitrary N.

### A uniform failure of the weaker finite norm criterion

For every dyadic N>=2, let c_N in R_N^* be the unique CRT class

    c_N=1 modulo X^N,
    c_N=X^(N/2) modulo phi^(2N).                            (D8)

Its full norm ratio PASSES the weaker necessary condition

    Phi(c_N)=0 modulo N,                                  (D9)

Here Phi modulo N is the weaker condition obtained by applying C652's character to the norm ratio modulo t^N; equivalently one may compute that ratio from any polynomial CRT representative.
But

    Pi_N(c_N)=-(N/2)/5!=0 modulo N,                        (D10)

so c_N does NOT belong to G_N.
This refutes sufficiency of the weaker finite condition at every such N while preserving C652's exact necessary theorem.
It does not refute sufficiency of the stronger Pi_N condition.

At precisely N=8,24,32, the adopted complete finite images additionally imply

    G_N=ker Pi_N.                                         (D11)

Their respective certified indices are8,16,32.
No other N, no infinite completed-kernel equality and no original characteristic-zero realization follows from those three equalities.

### Exact original interface and boundaries

Consider the SAME original domain of C652, restated here to delimit (D4).
Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1, degree2r, original root alpha, K=Q(alpha), delta=alpha+alpha^(-1), and totally real F=Q(delta).
Let T be the actual monic degree-r trace minimal polynomial, with P(z)=z^rT(z+z^(-1)) and [K:F]=2.
For C_p(z+z^(-1))=z^p+z^(-p), take the actual integral divided monic remainders theta_p=rem_T(T(C_p))/p, p=2,3,5, and their nonzero values a,b,c at delta.
Assume2c^2=3a^5 and b^2-a^3+s(c^3-2b^5)=0 for s in{1,-1}, with g=c^3-2b^5!=0.
Let G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2, R_can=G_can mod2, and assume the normalized circle Haar mean of log(G_can(z+z^(-1))^2) is0, with the integrable logarithm at zeros.
Assume phi is uniquely unsaturated: ord_phi R_can<ord_phi U, and every other irreducible psi dividing U has ord_psi R_can>=ord_psi U.
Keep the actual maximal q=2^k with U=U_0^q and R_can=R_0^q, and write ord_XU/q=A_0=2m.
The adopted input supplies

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3)=X^(2m)Yphi^(12m)B,
    B=X^(Q-m)H(chi),
    Q dyadic,2m<Q<5m,H(0)=1,5deg H<5m-Q,
    V_0=R_0/phi^(12m)=X^(m+Q)YH(chi).

Here Y is prime to Xphi and B remains the complete canonical complement with every surplus and extra factor.
The actual V_0 has complete nonnegative odd-order multiplicities after removing W_5, and its exact endpoint order is m+Q.
Thus YH(chi) itself is a complete UNIT product, and (D4) gives Y in G_N for every N, particularly N=4m for its full prescribed target.
This legal finite removal of H(chi) does not make Y globally complete or divide original integer layer exponents by q.

For clarity retain all original zero-Haar layer data

    G_can=V_int product_(b>=0)F_(2^b*5)^(a_b),
    a_b>=0 integers,
    lambda_0=lambda_1=1,lambda_b=2^(b-1) for b>=2,
    sum a_b lambda_b=12mq,
    a_b=0 for lambda_b>8mq,
    S_star=sum_(a_b odd,4mq<lambda_b<12mq)
       X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                          phi^(12m-lambda_b/q).

The integer trace factors F_n are defined by Phi_n(z)=z^(phi(n)/2)F_n(z+z^(-1)), and V_int retains all other factors and the sign.
No original layer is changed by the finite group argument.
The full C649 jets, corrected phi^(6m) root and phi^(8m) gate remain at their adopted scope, and the exact costs stay

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(5m-Q-5deg H)>0.

The strengthened finite character is NOT evaluated on those actual targets here.
In particular no higher-precision cancellation of the original correction is inferred from C652: quadratic terms that vanish modulo t^(4m) can contribute at the additional coefficient needed for (D7).
The already adopted remaining range{24,28,32,...}, actual maximal q, nonsquare U_0/R_0, canonical remainders and fields are unchanged.

## Argument

### 1. The iterated-Theta basis and density

Suppose u=1+t^r+O(t^(r+1)) with r positive and odd.
For a nonconstant monomial t^n, the first term of chi(t)^n-t^n occurs at degree n+2^(nu_2(n)+1), because chi(t)/t=1+t^2+t^4.
For n=r this is r+2 with coefficient1.
If n>r is odd, the degree is n+2>r+2; if n>r is even, it is at least n+4>r+2.
Thus u(chi)-u has exact leading term t^(r+2).
Moreover u^5-u=u(u^4-1) has leading degree4r>r+2.
Subtracting and dividing by the unit u(chi) proves Theta(u)=1+t^(r+2)+higher terms.
Starting from e_0=1+t gives (D1).

The units e_j^(2^s) have leading terms t^((2j+1)2^s), and these degrees cover every positive integer exactly once.
An increasing-coefficient elimination chooses their binary exponents uniquely and produces every unit.
The leading degrees tend to infinity, so the products converge; any first difference between two choices would have a unique noncanceling least degree.
Grouping the binary exponents for a fixed j proves the unique expression (D2).

Let B be the rational-function multiplicative group generated by all odd B_n.
It contains1+t=B_3 and phi=B_5.
The complete identity B_n(chi)=B_(5n)/phi shows that B is closed under composition by chi and hence under Theta.
It therefore contains every e_j, proving density and every finite low-X generation assertion.
This proof has no bound on the support orders and is independent of any native finite table.

### 2. Every composition is a finite complete member

Fix N and h in U.
Use the density just proved to find a finite rational B_n product b(t) with b=h modulo t^N.
After composition, b(chi)=h(chi) modulo chi^N.
Every factor B_n(chi)=D_(5n)=B_(5n)/phi is exactly a product of allowed W_d: the squarefree divisor product contains W_5 once and exact division removes only that factor.
This includes arbitrary higher five-orders.
Every inverse is a nonnegative power in the FINITE group R_N^*, so b(chi) has a finite nonnegative complete-factor representative in that quotient.
This proves (D3).
If YH(chi) is complete, its class lies in G_N and the class H(chi) lies in G_N by (D3), so their quotient Y lies there as well.
This proves (D4) without any global factor assertion about either quotient factor.

### 3. Evenness of the norm character

C652 constructs the rank5 algebra F_2[[t]][X]/(chi(X)-t), its simple branch x(t), and the complementary rank4 algebra A_high.
It proves

    Tr_high(a) in tF_2[[t]] for every a in A_high,
    N_high(X)=t/x(t)=phi(x(t))^2.                            (P1)

For the trace, multiplication modulo t acts on F_2[X]/phi^2 with two successive F_4 quotients carrying the same residue multiplication, so their traces add to0.
The full norm of X+1 is chi(1)+t=1+t, whence

    N_high(X+1)=(1+t)/(1+x(t)).                             (P2)

Since x(t)=t+O(t^3), both (P1) and (P2) are1 modulo t^2.

The unit group of F_2[X]/phi^2 has order12 and is generated by X and X+1.
Their residues generate F_4^*, and

    X^3=1+(X+1)phi,
    (X+1)^3=1+Xphi

give two linearly independent principal coefficients modulo phi^2.
Thus any high unit differs from a product of X and X+1 by1+phi^2 a=1+t b, with b in A_high because X is a unit.
The norm of this last factor is1+tTr_high(b) modulo t^2, hence1 by (P1).
It follows that N_high(v)=1 modulo t^2 for every high unit v.

Under C652's character, ell modulo2 equals the coefficient of t: Theta(U) begins in degree at least3, and (1+t)^a has coefficient a modulo2.
Therefore ell(N_high(v)) is even.
The low term in (D5) is divisible by4, proving Phi in2Z_2 and the integrality of Pi.
Continuity and homomorphism properties follow from those of the determinant norm and ell.
For the completed pair g=(1,X^3), one has Pi(g)=-3/5, since ell(phi)=-1 and ell(phi(x))=-1/5.
The high unit X^3 is principal, so its2-adic powers converge and their Pi values cover Z_2, proving surjectivity.
For any complete factor, C652 proves its full norm ratio belongs to Theta(U), so Phi=0 and hence Pi=0.
Taking closures preserves this containment.

### 4. Finite lift independence at the refined precision

Let two completed unit pairs have the same class in R_N.
Their low quotient is1+X^N a and their high quotient is1+phi^(2N)b=1+t^N c, with c in A_high.
Let L=2^ceil(log_2 N) and K=2^ceil(log_2(N+1)).
C652's finite ell precision makes the low term of Phi change by a multiple of4L.
For the high quotient, the determinant expansion is

    N_high(1+t^N c)=1+t^N Tr_high(c)+O(t^(2N)).             (P3)

Since Tr_high(c) lies in t and2N>=N+1, the result is1 modulo t^(N+1).
Its ell value is therefore divisible by K.
One has K<=2L, so the low contribution is divisible by K as well.
Consequently Phi changes by a multiple of K, and Pi changes by a multiple of K/2.
For integral N>=1, K/2=2^floor(log_2 N), proving that Pi_N is defined on the SAME finite quotient.
The pair (1,X^3) exists as a unit CRT class there and has odd Pi_N value -3/5, so the finite map is surjective.
Complete products have value0, proving (D7) and its exact kernel index.
This proof shows precisely why a higher formal norm precision is available from the original two-primary data; it does not assume that missing coefficients have been supplied.

### 5. Explicit countercontrol to the weaker criterion

For dyadic N>=2 take the completed lift of (D8) with u=1 and v=X^(N/2).
From (P1),

    ell(N_high(v))=(N/2)*2ell(phi(x))=-N/5.

Thus Phi=-N/5, which is0 modulo N, proving (D9).
But Pi=-(N/2)/5 is nonzero modulo N=2^floor(log_2 N), proving (D10) and c_N outside G_N.
Every other completed lift differs in Phi by a multiple of2N and gives the same conclusions by Section4.
A polynomial CRT representative therefore has the same weak norm-ratio value and the same refined obstruction.
At N=8 this is exactly the class y^2 with y=(1+X^4,X^2) in C630/J127, whose old coset has order4; the present proof does not require a new run or that older certificate.
The failure concerns the WEAKER finite criterion only, not the exact infinite character kernel or sufficiency of (D7).

### 6. The three whole finite images and the remaining gap

The adopted [C621v2 complete image](Yin_C_G0621_v2.md#statement) at X^8phi^16 has index8.
The adopted [C640 complete image](Yin_C_G0640_v1.md#statement) at X^24phi^48 has index16.
The adopted [C651 complete image](Yin_C_G0651_v1.md#statement) at X^32phi^64 has index32.
Each source includes all allowed odd orders via its proved period and divisor reduction and its complete certified native group calculation.
The same three indices are exactly2^floor(log_2 N), the kernel indices in (D7).
Containment and equality of finite indices therefore prove (D11), at precisely those three N.
No new computation or inference from a pattern is made.

The composition subgroup is now known to lie in the completed complete group, by (D3) and its density proof.
After removing it, the unresolved generation question is carried by the coprime-five B_n.
Indeed every allowed W_n is generated by coprime-five B_n and the B_n(chi), by C652's full divisor induction.
It remains to prove that the coprime-five generators fill the remaining norm kernel at ALL depths, or to construct a counterexample.
Neither the three finite indices nor low composition density proves that assertion.

### 7. Original applicability and unchanged precision limits

The adopted [C652 original interface](Yin_C_G0652_v1.md#statement) gives exactly the original hypotheses, canonical data, complete V_0, Q/H form, integer layers and costs stated above.
Every allowed W_n has constant coefficient1 and no phi factor, and Y,H(chi) also have constant1.
Thus ord_X V_0=m+Q, and removing that exact endpoint from its complete factorization leaves YH(chi) with complete nonnegative allowed multiplicities.
Applying (D4) supplies the original Y class in G_N for each specified N; the representative constructed for H(chi) need not have its original global degree and does not replace the original H or Y.
The full original degree formulas and actual q are therefore retained rather than recalculated from a surrogate representative.

For actual N=4m, Section4 permits a refined character on the full known target, but computing it requires all determinant terms that can contribute at the needed precision.
If an actual correction is1+Sigma a with Sigma in t^(N/2), its square vanishes modulo t^N but can contribute at t^N when the norm is inspected modulo t^(N+1).
This theorem performs no such target evaluation and assumes no disappearance of that quadratic contribution.
Consequently the original branch range and C652's necessary target formula are left at their adopted scopes.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:19 |
| status | open |
| reason | Register the complete all-precision B_n density and finite composition-removal theorem, the even normalized norm character and its lift-independent finite refinement, the uniform dyadic countercontrol to the weaker criterion, and the exact three finite kernel identifications using adopted full images. Original Y membership is justified without global completeness of H or Y. All q/layers/canonical costs and possible higher norm corrections remain; no all-depth converse, new native computation or original realization is asserted. Fresh isolated whole mathematical review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire density and refined finite theorem](#statement) | D1--D11, all-precision density/composition, normalized finite character, uniform weak-condition countercontrol, precisely three kernel equalities and exact original interface with unchanged limits. |
| argument | [Whole analytical argument](#argument) | All seven sections, exact leading orders/convergence, complete divisor support, high norm parity and trace precision, surjectivity and every lift, countercontrol, finite-index deductions and original membership/limits. |
| dependency | [Adopted formal-unit and norm theorem](Yin_C_G0652_v1.md#statement) | Exact Theta/ell quotient, finite ell precision, calibration, simple/high norm algebra and trace, all-order complete norm bridge and full original canonical interface. |
| dependency | [Complete trace and divisor identities](Yin_C_G0608_v1.md#argument) | B_n and W_n definitions, full divisor products, squarefreeness and allowed-factor support. |
| dependency | [All five-order composition](Yin_C_G0609_v2.md#argument) | B_(5n)=phi B_n(chi) for every odd n, preserving arbitrary higher five-orders. |
| dependency | [Entire N8 finite image](Yin_C_G0621_v2.md#statement) | Exact complete subgroup of X^8phi^16 and certified index8, used only for D11 at N8. |
| dependency | [Entire N24 finite image](Yin_C_G0640_v1.md#statement) | Exact complete subgroup of X^24phi^48 and certified index16, used only for D11 at N24. |
| dependency | [Entire N32 finite image](Yin_C_G0651_v1.md#statement) | Exact complete subgroup of X^32phi^64 and certified index32, used only for D11 at N32. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:27 |
| status | proved |
| reason | Adopt the entire D1--D11 theorem after main reading of complete C654 and isolated whole R866. The iterated-Theta basis gives all-precision composition membership, allowing finite removal of H(chi) for the SAME original Y without global factorization claims. The completed norm character is even, and its half induces a surjective lift-independent Pi_N on the original quotient at modulus2^floor(log2N). The explicit dyadic classes disprove sufficiency of the weaker finite criterion. Exactly N8,24,32 have kernel equality by accepted complete indices; no all-depth converse or stronger actual-target evaluation is asserted. Original q/layers/costs, possible top quadratic correction and all source/native boundaries remain. No new native or Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire density and refined finite theorem](#statement) | D1--D11, all-precision density/composition, normalized finite character, uniform weak-condition countercontrol, precisely three kernel equalities and exact original interface with unchanged limits. |
| argument | [Whole analytical argument](#argument) | All seven sections, exact leading orders/convergence, complete divisor support, high norm parity and trace precision, surjectivity and every lift, countercontrol, finite-index deductions and original membership/limits. |
| dependency | [Adopted formal-unit and norm theorem](Yin_C_G0652_v1.md#statement) | Exact Theta/ell quotient, finite ell precision, calibration, simple/high norm algebra and trace, all-order complete norm bridge and full original canonical interface. |
| dependency | [Complete trace and divisor identities](Yin_C_G0608_v1.md#argument) | B_n and W_n definitions, full divisor products, squarefreeness and allowed-factor support. |
| dependency | [All five-order composition](Yin_C_G0609_v2.md#argument) | B_(5n)=phi B_n(chi) for every odd n, preserving arbitrary higher five-orders. |
| dependency | [Entire N8 finite image](Yin_C_G0621_v2.md#statement) | Exact complete subgroup of X^8phi^16 and certified index8, used only for D11 at N8. |
| dependency | [Entire N24 finite image](Yin_C_G0640_v1.md#statement) | Exact complete subgroup of X^24phi^48 and certified index16, used only for D11 at N24. |
| dependency | [Entire N32 finite image](Yin_C_G0651_v1.md#statement) | Exact complete subgroup of X^32phi^64 and certified index32, used only for D11 at N32. |
| review | [Independent entire density and refined-character finding](../audits/reviews/Yin_R_G0866_v1.md#whole-density-refined-finite-character-finding) | Whole D1--D11 and seven proof sections, exact convergence/density and finite complete-factor removal, completed algebra/parity/surjectivity, every lift and N1 boundary, uniform weak-condition countercontrol and precisely three index deductions, with full original applicability and correction limits. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0126](../computations/programs/Yin_J_G0126/readme.md#reproducing-reviewed-runs), [Yin_J_G0129](../computations/programs/Yin_J_G0129/readme.md#reproducing-reviewed-runs), [Yin_J_G0130](../computations/programs/Yin_J_G0130/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
