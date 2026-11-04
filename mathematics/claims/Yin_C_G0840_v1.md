---
author: Yin
---

# Uniform dyadic precision ceilings for varying conductors and unit-resultant cofactors

Human author Yin.
Root proposed the varying-conductor norm and trace-gain mechanism, the general Newton estimate and the balanced uniform-six profile.
Contributor characteristic_zero_bridge checked the complete argument, actual order denominator, endpoint and empty-cofactor cases, all positive norm signs and degree costs, and supplied the explicit positive-measure unit-resultant cofactor.
Both are substantive contributors, not independent reviewers.
The [selected adopted decision](#decision-whole-reviewed-2026-10-28) is proved through [whole independent R1060](../audits/reviews/Yin_R_G1060_v1.md#whole-finding).
Its separate review covers the full varying-conductor argument; the initial OPEN decision and fixed argument below retain their historical wording.
No native computation, new source acquisition, Yu bound or maximal-order identification is a premise.

The classical Newton and finite Lagrange formulas have the [source-attribution scope recorded in R1060](../audits/reviews/Yin_R_G1060_v1.md#accepted-inputs-and-source-completeness), reusing [Mas12 Problem7(a)](../audits/literature/Mas12/readme.md#newton-identity-selected-attribution) and [Nat26 DLMF3.3(i)](../audits/literature/Nat26/readme.md#lagrange-interpolation-attribution-20261012).
These are formula attribution and applicability checks; the local coefficient derivations remain in VC5--VC6, with no new source-proof audit or historical-priority claim.

## Statement

<a id="varying-conductor-unit-resultant-family"></a>
### Definition and domain: original trace family with two unit resultants

Use integer traces C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), and complete monic primitive trace polynomials z^(phi(m)/2)F_m(z+z^(-1))=Phi_m(z), m>2.
Let ell>=2 be an integer, N=15*2^ell, d_ram=2^(ell-2), and u,v>=0 integers.
Let U in Z[X] be monic of any nonnegative degree with Res(U,F_(N/2))=+/-1 and Res(U,F_(N/5))=+/-1.
The monic constant U=1 is included; no root-location, irreducibility or cyclotomic condition on U is imposed.
Set T=F_15^u F_3^v F_N U and use the ORIGINAL integer canonical polynomials

    a=rem_T(T(C_2))/2, c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5).

Each scalar division occurs in integer coefficients before evaluation or reduction.
The actual trace degree is d_T=4u+v+8d_ram+deg U, and the full reciprocal degree is2d_T.
For nonzero H in Z[X], let nu_2(H) be the minimum dyadic valuation of its nonzero coefficients, and put nu_2(0)=infinity.
Then

    F!=0;
    if 5u!=d_ram+v,
       nu_2(F)<=floor(min(5u/d_ram,1+v/d_ram));
    if v=5u-d_ram>=0,
       nu_2(F)<=ceil(5u/d_ram)+4.                         (ST1)

No bound is asserted optimal or attained, and no separate ceiling for another residual alone is claimed.

### Exact field, order and general norm statements

For a primitive Nth root zeta, put theta=zeta+zeta^(-1), L=Q(zeta), K=Q(theta), R_full=Z[zeta] and R=Z[theta].
Let x_2=C_2(theta), x_5=C_5(theta), A=a(theta) and C=c(theta).
These are the genuine original values A=T(x_2)/2 and C=T(x_5)/5 and are nonzero algebraic S-units supported only above2.
The degrees are [K:Q]=8d_ram, [Q(x_2):Q]=4d_ram and [Q(x_5):Q]=2d_ram.
At EVERY dyadic place normalized by v_2(2)=1,

    v_2(A)=u/d_ram,             v_2(C)=v/(2d_ram),
    Norm_(K/Q)(A)=2^(8u),       Norm_(K/Q)(C)=2^(4v),
    rho=2C^2/(3A^5),
    Norm_(K/Q)(rho)=2^(8d_ram+8v-40u)*3^(-8d_ram).        (ST2)

The norms of A and C are positive and count all8d_ram embeddings, including subfield repetitions.
At every prime above3, F(theta) has valuation0.
The actual order statements are

    R_full intersect K=R,
    2^(ceil(5u/d_ram))/A^5 in R,
    Tr_(K/Q)(R) subset2^(ell-1)Z.                        (ST3)

No maximal-order assertion is made.
The following general lemma is also part of the statement: if S is any full-rank integer order in a number field E, s>=0 is an integer and Tr_(E/Q)(S) subset2^s Z, then for every z in S_(2)=S tensor Z_(2) and integer k>=1,

    Norm_(E/Q)(1+2^k z)-1 in2^(k+s) Z_(2).               (ST4)

Here Z_(2) consists of rationals with odd denominator, and all embedding multiplicities count.
The complete elementary Newton-identity proof is [VC6](#trace-gain-newton-norm-congruence).

### Uniform-six corollary, positive-measure examples and limits

For EVERY ell>=4 with u=v=2^(ell-4)=d_ram/4 and EVERY allowed U,

    F not in128Z[X], nu_2(F)<=6,
    d_T=37*2^(ell-4)+deg U.                              (ST5)

For every ell>=2 and integer M>=4, the explicit cofactor

    U_M=1+(X-M)F_(N/2)F_(N/5)                            (ST6)

is monic of degree6d_ram+1 and has both ordered resultants equal to1.
It has a real root in(M-1,M), so P_(U_M)(z)=z^(deg U_M)U_M(z+z^(-1)) has positive FULL logarithmic Mahler measure.
The full original reciprocal polynomial is exactly Phi_15^u Phi_3^v Phi_N P_(U_M), so its full measure is m(P_(U_M))>0, retaining all roots and multiplicities.
Its degrees are d_T=14d_ram+4u+v+1 and2d_T; in ST5 these become61*2^(ell-4)+1 and twice that number.
There is no nearzero-measure, Salem, total-reality or irreducibility assertion.

The general domain includes u=v=0,U=1, where T=F_N is irreducible cyclotomic and nu_2(F)=0.
Whenever4u+v+deg U>0, the complementary factor to F_N has positive degree and T is reducible.
Every balanced input and every explicit positive-measure example is therefore reducible.
No irreducible lift, C720 positive-measure certificate or unrestricted Lehmer result follows, and no necessity of these auxiliary equations for that unrestricted problem is asserted.

## Exact inputs and extraction scope

[C266's selected retained proof](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption), specifically its [cyclotomic CRT/unit argument](Yin_C_G0266_v1.md#exact-cyclotomic-crt-defect), supplies actual integer Bezout unit inverses and the exceptional Phi_(Mp^j)(zeta_M)/p unit in Z[zeta_M].
Its retained complete-current review relationship is self-review, not a newly performed independent source review.
[C736](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) supplies integer prime-divided own-divisor remainders and their exact evaluations, including repeated factors.
[C839](Yin_C_G0839_v1.md#decision-whole-reviewed-2026-10-28) is the accepted fixed-conductor predecessor and source of the order-unit/relative-trace proof mechanism; its independent review is not attributed to this extension.
All newly varying conductor, general trace-gain norm, endpoint, positive-measure and scope arguments are included below.
The C839 special-family comparison uses its elementary cofactor-unit calculation only, not C837 UV7's Yu/logarithmic argument.

The proof was developed at [D6's varying-conductor question](../drafts/Yin_D_G0006.md#varying-conductor-unit-resultant-precision-ceiling), which is extraction provenance only and supplies no logical premise.
The complete VC1--VC8 proof is retained here; no mutable draft, native output or pending review is a mathematical dependency.

## Complete argument

### VC1. Exact domain and proposed coefficient ceiling

Use the integer traces C_0=2,C_1=X,C_(j+1)=X C_j-C_(j-1).
For m>2 let F_m be the complete monic primitive trace polynomial defined by z^(phi(m)/2) F_m(z+z^(-1))=Phi_m(z).
Let ell>=2 be an integer and put

    N=15*2^ell, d_ram=2^(ell-2), n_K=8d_ram=2^(ell+1).

Let u,v>=0 be integers and let U in Z[X] be monic, of any nonnegative degree, satisfying

    Res(U,F_(N/2))=+/-1,
    Res(U,F_(N/5))=+/-1.                                (VC1)

The monic constant U=1 is allowed.
Set T=F_15^u F_3^v F_N U, and use the SAME original divisor throughout:

    a=rem_T(T(C_2))/2, c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5),
    C_2=X^2-2, C_5=X^5-5X^3+5X.

All scalar divisions are integer coefficient divisions before any evaluation, by C736.
Define nu_2 of a nonzero integer polynomial as the minimum valuation of its nonzero coefficients, and put nu_2(0)=infinity.
The complete conclusions proved below are

    F!=0;
    if 5u!=d_ram+v,
       nu_2(F)<=floor(min(5u/d_ram,1+v/d_ram));
    if v=5u-d_ram>=0,
       nu_2(F)<=ceil(5u/d_ram)+4.                       (VC2)

The original trace degree and full reciprocal degree are respectively

    d_T=4u+v+8d_ram+deg U,      2d_T.                    (VC3)

There is no assertion that either upper bound is optimal or attained.
The coefficient conclusion is necessary for any simultaneous residual precision that includes divisibility of this original F; no bound for a different residual alone is asserted.

### VC2. Actual order units from the two resultants and cyclotomic factors

Choose a primitive Nth root zeta, and set

    L=Q(zeta), theta=zeta+zeta^(-1), K=Q(theta),
    R_full=Z[zeta], R=Z[theta],
    x_2=zeta^2+zeta^(-2), x_5=zeta^5+zeta^(-5).

The field degrees are [L:Q]=16d_ram and [K:Q]=8d_ram.
The elements x_2,x_5 are primitive N/2 and N/5 traces, with real subfield degrees4d_ram and2d_ram, respectively.
Thus their relative degrees in K are2 and4, including when ell=2.

For M=N/2 or N/5, multiplication by U on the free integer order Z[X]/(F_M) has determinant Res(F_M,U), equal to+/-1 by VC1 and the resultant interchange formula.
Its integer multiplication matrix is unimodular, so its inverse applied to1 gives an actual polynomial inverse for U modulo F_M.
Consequently U(x_2) and U(x_5) are units in their actual trace orders Z[x_2] and Z[x_5], hence in R_full.
This does not require U to be cyclotomic, squarefree, irreducible, totally real or to have nonzero constant coefficient.
The same conclusion could be expressed by the integer resultant Bezout identity; it is stronger than knowing only that these values are nonzero.

C266's exceptional quotient-unit proof, with index ratios N/(N/2)=2 and N/(N/5)=5, gives

    F_N(x_2)/2 in R_full^times,
    F_N(x_5)/5 in R_full^times.                          (VC4)

Indeed the cyclotomic assertion is Phi_N(zeta_M)/p in Z[zeta_M]^times, and conversion to the trace polynomial multiplies by a root-of-unity unit.
Also F_3(x_2) is a unit because (N/2)/3=5*2^(ell-1) is not a prime power, and F_15(x_5) is a unit because neither index has an integral prime-power ratio with the other.
C266's nonexceptional integer Bezout inverses place these units in R_full itself.

Since T(theta)=0, the original quotient identities give

    A:=a(theta)=T(x_2)/2=u_A F_15(x_2)^u,
    C:=c(theta)=T(x_5)/5=u_C F_3(x_5)^v,
    u_A,u_C in R_full^times.                            (VC5)

In particular A,C are nonzero.
These are evaluated ORIGINAL canonical polynomials, not the unweighted canonical variables belonging to the proper factor F_N.

### VC3. Pure dyadic factors, every place and positive full norms

The exact identities

    Phi_15(z)=(z^15-1)(z-1)/[(z^5-1)(z^3-1)],
    Phi_3(z)=(z^3-1)/(z-1)

give F_15(x_2) as an R_full-unit times pi=1-zeta^30, and F_3(x_5) as an R_full-unit times pi'=1-zeta^15.
For the first identity, the other orders are15*2^(ell-1),3*2^(ell-1),5*2^(ell-1); for the second the denominator order is3*2^ell.
All these orders are mixed, not prime powers, so their1-root factors are actual cyclotomic-order units by C266.
The orders of zeta^30 and zeta^15 are respectively2^(ell-1) and2^ell.

If xi is a primitive2^r root with r>=1, every ratio(1-xi^j)/(1-xi), for odd j modulo2^r, is a unit in Z[xi].
Its inverse is the geometric sum obtained from any positive odd k with jk=1 modulo2^r.
Multiplying all2^(r-1) ratios and using Phi_(2^r)(1)=2 proves

    (1-xi)^(2^(r-1))/2 in Z[xi]^times.

This includes r=1, where xi=-1 and the displayed quotient is1.
It follows, at EVERY dyadic place normalized by v_2(2)=1, that

    v_2(A)=u/d_ram,          v_2(C)=v/(2d_ram).           (VC6)

Both A and C are algebraic S-units supported only above2, with the displayed actual order factorizations.
At every prime above3 they are units, so the two terms in F(theta)=2C^2-3A^5 have distinct valuations there, namely0 and the positive valuation of3.
Hence F(theta)!=0 and the ORIGINAL polynomial F is never zero.
This argument covers balanced and unbalanced exponents, empty U and the smallest conductor.

Every embedding of K sends theta to another primitive N trace, so the same valuations hold for all n_K conjugate values at a fixed dyadic place.
The only rational prime support of the norms is2.
Moreover A lies in Q(x_2) and C in Q(x_5), whose relative degrees in K are even2 and4; their nonzero rational subfield norms are raised to those even powers.
Thus the full norms are POSITIVE and exactly

    Norm_K(A)=2^(8u),       Norm_K(C)=2^(4v),
    rho=2C^2/(3A^5),
    Norm_K(rho)=2^(8d_ram+8v-40u)*3^(-8d_ram).           (VC7)

All n_K embeddings, including repetitions from proper subfields, are counted.
These norms do not replace the original degree d_T or the full reciprocal measure.

### VC4. Unbalanced valuation and the actual order denominator

If 5u!=d_ram+v, the two dyadic term valuations at EVERY place are distinct.
Therefore

    v_2(F(theta))=min(5u/d_ram,1+v/d_ram).

Coefficientwise2^n divisibility of F implies v_2(F(theta))>=n because theta is integral.
This proves the unbalanced assertion of VC2, with its floor and without an inference in the reverse direction.

For the balanced case, and in fact for any u, put a_den=ceil(5u/d_ram).
The equality R_full intersect K=R follows directly from zeta^2-theta*zeta+1=0: every element of R_full is a(theta)+zeta*b(theta), and subtracting its complex conjugate forces b(theta)=0 when the element is real.
A real unit of R_full and its real inverse therefore lie in R^times.
From VC3, A is a unit times pi^u and pi^(d_ram)/2 is a unit of R_full.
Consequently

    d_A:=2^(a_den)/A^5 in R_full,
    d_A in R because it is real.                       (VC8)

Explicitly, the first assertion is a unit times pi^(a_den*d_ram-5u), with nonnegative exponent.
This proves order membership rather than substituting local integrality for membership in a possibly nonmaximal order.
Only the stated resultant-unit hypotheses on U are used for this denominator.

### VC5. Relative Chebyshev trace gain for every ell>=2

Put m=2^(ell-1)=2d_ram, t=C_m(theta), K_0=Q(t), R_0=Z[t].
Here zeta^m has exact order30, so [K_0:Q]=4 and [K:K_0]=m.
The monic f_t(X)=C_m(X)-t has degree m and root theta and is therefore its relative minimal polynomial.
The relation and field degree show that R=R_0[theta] is free over R_0 with basis1,theta,...,theta^(m-1).
Since R_0 is free of rank4 over Z, R is a free integer order of rank n_K.

Differentiating C_m(z+z^(-1))=z^m+z^(-m) gives

    f_t'(theta)=m h,
    h=(zeta^m-zeta^(-m))/(zeta-zeta^(-1)) in R^times.      (VC9)

The numerator and denominator are root-of-unity multiples of1-zeta^(2m) and1-zeta^2, whose orders are15 and N/2.
Both are mixed, so their quotient is an R_full-unit by C266 and is a real R-unit by VC4.
For any g in R_0[X], monic reduction and Lagrange interpolation at the m distinct roots give

    Tr_(K/K_0)(g(theta)/f_t'(theta))
          =[X^(m-1)] rem_(f_t)g in R_0.

The coefficient identity follows because f_t(X)/(X-theta_i) is monic of degree m-1 in each interpolation term.
Given r in R, choose g with g(theta)=r h; then the displayed trace equals Tr_(K/K_0)(r)/m.
Taking the absolute trace of the integral R_0 element proves

    Tr_(K/Q)(R) subset 2^(ell-1) Z.                    (VC10)

The argument includes ell=2, where m=2; no growing-conductor maximal-order or codifferent formula is required.

<a id="trace-gain-newton-norm-congruence"></a>
### VC6. General integer-order trace gain and a norm congruence

Let S be any full-rank integer order in a number field E, let s>=0 be an integer, and assume Tr_(E/Q)(S) subset2^s Z.
Write S_(2)=S tensor Z_(2), where Z_(2) consists of rationals with odd denominator.
For z in S_(2), let e_i(z) be the elementary symmetric coefficients of ALL [E:Q] embedding values, retaining multiplicities.
They belong to Z_(2): write z=r/b with r in S and b odd and use the integer characteristic polynomial of multiplication by r on the free order S.
Every power z^j belongs to S_(2), so its trace belongs to2^s Z_(2).

The generating polynomial E_z(T)=product_sigma(1+T sigma(z)) satisfies

    E_z'(T)/E_z(T)
       =sum_(j>=1)(-1)^(j-1)Tr(z^j)T^(j-1).

Comparing coefficients after multiplication by E_z(T) proves the Newton identity

    i e_i(z)=sum_(j=1..i)(-1)^(j-1)e_(i-j)(z)Tr(z^j).

All terms on the right are in2^s Z_(2), since every e_(i-j) is2-integral.
Hence v_2(e_i(z))>=s-v_2(i).
For every integer k>=1, each nonconstant term in the full norm expansion has

    v_2(2^(ki)e_i(z))>=ki+s-v_2(i)>=k+s,

because v_2(i)<=i-1<=k(i-1) for i>=1.
Summing all terms gives the all-degree congruence

    Norm_(E/Q)(1+2^k z)-1 in2^(k+s) Z_(2), k>=1.         (VC11)

This pays the higher norm coefficients even when the degree and trace gain grow; a quadratic truncation alone is not being imported from C839.
The argument proves the needed elementary identity directly and does not assume distinct values sigma(z).

### VC7. Balanced exponents and the uniform-six profile

Now assume v=5u-d_ram>=0, so u>=1 and VC7 gives Norm_K(rho)=3^(-n_K).
Since n_K=2^(ell+1), elementary repeated difference-of-squares gives

    v_2(3^(-n_K)-1)=ell+3.                             (VC12)

Indeed 3^(2^(ell+1))-1 is(3-1)(3+1) times the ell factors3^(2^j)+1, j=1,...,ell, each of the latter having valuation1.
Suppose the ORIGINAL F were coefficientwise divisible by2^(a_den+5), and write F=2^(a_den+5)H with H in Z[X].
Equations VC8 and the original evaluation imply

    rho-1=F(theta)/(3A^5)=2^5 z,
    z=H(theta)d_A/3 in R_(2).

Apply VC11 with s=ell-1 and k=5, using VC10.
It forces v_2(Norm_K(rho)-1)>=ell+4, contradicting VC12.
This proves the balanced ceiling nu_2(F)<=a_den+4 in VC2.
Equivalently, if n>=a_den+1 and2^n divides F, VC11 gives n-a_den+ell-1<=ell+3, hence n<=a_den+4.

For EVERY ell>=4 choose u=v=2^(ell-4)=d_ram/4.
The balance identity holds, a_den=ceil(5/4)=2, and therefore

    F not in128 Z[X],      nu_2(F)<=6,                  (VC13)

uniformly across ALL these conductors and ALL monic U satisfying VC1.
Here d_T=37*2^(ell-4)+deg U and the full reciprocal degree is twice that number.
The original C839 family is an ell=6 specialization with u=v=4 and a particular cyclotomic U, whose remaining factors satisfy the two unit conditions by the selected C837 UV1--UV4/C839 unit argument.
No claim of attainment or sharpness of6 follows.

At ell=2 the fields have degrees8,4,2 and pi=1-zeta^30=2; the actual denominator construction and trace gain2 remain valid.
The general empty case u=v=0,U=1 gives T=F_N and lies in the UNBALANCED case, with nu_2(F)=0.
It is not a reducible input, so a blanket reducibility assertion for all of VC1 would be false.
Every balanced case has u>=1 and hence a nonconstant complementary factor to F_N, so those inputs, including VC13, are reducible.

### VC8. Explicit noncyclotomic unit-resultant cofactors and the scope boundary

For any ell>=2 and any integer M>=4 put

    U_M(X)=1+(X-M)F_(N/2)(X)F_(N/5)(X).                 (VC14)

This is monic of degree6d_ram+1.
Modulo either trace factor it equals1, so Res(F_(N/2),U_M)=Res(F_(N/5),U_M)=1.
The two trace degrees4d_ram and2d_ram are even, so interchange of resultant arguments also gives BOTH ordered resultants in VC1 equal to1.
Thus this is an explicit allowed cofactor for every stated conductor.

All roots of the two primitive trace factors lie strictly in(-2,2).
At X=M-1>=3 each factor is a product of positive numbers strictly larger than1.
Consequently U_M(M-1)<0, whereas U_M(M)=1>0.
There is a real root x_* in(M-1,M), in particular x_*>2.
The monic reciprocal integer polynomial

    P_(U_M)(z)=z^(deg U_M) U_M(z+z^(-1))

has a real root(z_*=(x_*+sqrt(x_*^2-4))/2)>1, so its FULL logarithmic Mahler measure is positive.
No irreducibility or location of its other roots is assumed.
The full reciprocal polynomial of T factors EXACTLY as

    z^(d_T)T(z+z^(-1))=Phi_15(z)^u Phi_3(z)^v Phi_N(z) P_(U_M)(z).

The cyclotomic factors have measure0, so the full input measure equals the positive full measure of P_(U_M), including all its roots and multiplicities.
For this explicit U_M the degrees are d_T=14d_ram+4u+v+1 and2d_T; in the uniform-six specialization they are61*2^(ell-4)+1 and twice that number.
This is a genuine extension beyond wholly cyclotomic cofactors, but not a nearzero-measure construction or a Salem/total-reality assertion.

For a general allowed U the theorem makes no root-location or measure assumption.
The input T is reducible whenever4u+v+deg U>0, because its complementary monic factor to F_N then has positive degree; the sole empty-complement case is T=F_N.
The positive-measure examples above and all balanced inputs are reducible, so no irreducible-lift result or C720 positive-measure certificate is supplied.
No implication that these auxiliary residual equations are necessary for the unrestricted Lehmer problem is asserted.
The fixed C839 proof and adoption remain unchanged; this complete varying-conductor/order/Newton extension remains OPEN pending its own whole review.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision varying-conductor-unit-resultant-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T21:18 |
| status | open |
| reason | Fix the complete varying-conductor/unit-resultant precision theorem, original canonical nonvanishing and both exponent branches, positive full field norms, actual order denominator, all-degree Newton norm congruence, uniform-six profile and explicit positive-Mahler cofactors with every degree and reducibility boundary. Root and characteristic_zero_bridge are substantive contributors. The complete author argument awaits fresh whole independent review and responsible adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire varying-conductor and general order statement](#statement) | ST1--ST6: all ell>=2/u/v/monic unit-resultant U, original a/c/F and full degree, coefficient ceilings/nonvanishing, every-place norms/order/trace facts, general integer-order norm lemma, uniform6, explicit positive full-measure example and empty/reducibility/irreducible-lift limits. |
| argument | [Complete VC1--VC8](#complete-argument) | Actual resultant-order inverse, all cyclotomic unit factors, pure dyadic factors at every place, positive norm multiplicities, exact order denominator, relative monic basis/Lagrange trace, general Newton higher-term estimate, original coefficient contradiction, ell2 and empty cases, explicit noncyclotomic U and full degree/measure proof. |
| dependency | [Actual cyclotomic-order unit interface](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Exact-cyclotomic-crt-defect proof of integral Bezout units for non-prime-power index ratios and Phi_(Mp^j)(zeta_M)/p units in the actual integer cyclotomic order, including mixed-order1-root factors; selected complete retained-proof/self-review scope only, no maximal-order theorem. |
| dependency | [Genuine original canonical operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Integer prime-divided own-divisor remainders and exact factor-root evaluation/cofactor identity with all multiplicities; no canonical variables of F_N substituted for those of T. |
| support | [Fixed-conductor elementary predecessor](Yin_C_G0839_v1.md#decision-whole-reviewed-2026-10-28) | Actual order-unit and relative Chebyshev/Lagrange mechanism and ell6 special-family comparison, including elementary cofactor units. Its fixed conclusion/review does not supply the new varying-conductor or Newton proof; no Yu/logarithmic or native premise is used. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T21:26 |
| status | proved |
| reason | Adopt the complete ST1--ST6/VC1--VC8 theorem after root read the entire fixed argument and the fresh whole independent R1060 finding. Every conductor, original divisor, actual unit-resultant order, full positive norm and trace gain, higher Newton term, both coefficient bounds, positive-measure cofactor and full degree/reducibility boundary is covered. C266 retains its accepted self-reviewed input scope; no maximal-order identification, Yu premise, irreducible lift, optimality of six or unrestricted Lehmer conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire varying-conductor and general order statement](#statement) | ST1--ST6: all ell>=2/u/v/monic unit-resultant U, original a/c/F and full degree, coefficient ceilings/nonvanishing, every-place norms/order/trace facts, general integer-order norm lemma, uniform6, explicit positive full-measure example and empty/reducibility/irreducible-lift limits. |
| argument | [Complete VC1--VC8](#complete-argument) | Actual resultant-order inverse, all cyclotomic unit factors, pure dyadic factors at every place, positive norm multiplicities, exact order denominator, relative monic basis/Lagrange trace, general Newton higher-term estimate, original coefficient contradiction, ell2 and empty cases, explicit noncyclotomic U and full degree/measure proof. |
| dependency | [Actual cyclotomic-order unit interface](Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Exact-cyclotomic-crt-defect proof of integral Bezout units for non-prime-power index ratios and Phi_(Mp^j)(zeta_M)/p units in the actual integer cyclotomic order, including mixed-order1-root factors; selected complete retained-proof/self-review scope only, no maximal-order theorem. |
| dependency | [Genuine original canonical operations](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | Integer prime-divided own-divisor remainders and exact factor-root evaluation/cofactor identity with all multiplicities; no canonical variables of F_N substituted for those of T. |
| support | [Fixed-conductor elementary predecessor](Yin_C_G0839_v1.md#decision-whole-reviewed-2026-10-28) | Actual order-unit and relative Chebyshev/Lagrange mechanism and ell6 special-family comparison, including elementary cofactor units. Its fixed conclusion/review does not supply the new varying-conductor or Newton proof; no Yu/logarithmic or native premise is used. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1060_v1.md#whole-finding) | Entire ST1--ST6 statement and VC1--VC8 proof, exact accepted interfaces and existing Newton/Lagrange attribution, all conductor/empty/positive-measure endpoints and all degree and scope costs; no inherited author development or mathematical repair. |

