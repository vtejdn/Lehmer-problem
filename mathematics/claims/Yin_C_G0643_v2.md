---
author: Yin
---
# Uniform endpoint constraints and complete homogeneous-cube classification

Human author Yin.
This substantive v2 preserves the [physical v1](Yin_C_G0643_v1.md#decision-whole-reviewed-2026-10-23) and reproduces its whole EP1--EP14 statement and proof below, before adding the canonical extraction, complete module and homogeneous-cube classifications, and original dichotomy SC1--SC6.
Root supplied the formal inverse and two determinant ideas for v1, and the new square-times-composition and dyadic descent proposal.
The same_trace contributor checked and completed both versions' units, boundary cases, exact degrees and original precisions, and supplied the primitive-core strengthening, its uniqueness/iteration proof and the actual-degree boundary checks for the full module classification, and the simultaneous fifth-root/odd-error proof of the exact homogeneous-cube classification.
Both are mathematical contributors.
V1's R1012 covers its adopted EP scope only; it does not independently review the new SC claims or this complete v2.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused reuse inspected C643v1's exact polynomial determinants and original homogeneous projection, C634/C636's uniform support/module interfaces, and C197/C199/C609's actual original hypotheses.
The [D1 extraction candidate](../drafts/Yin_D_G0001.md#canonical-square-composition-extraction) is development provenance, not a logical input.
No native mathematical computation, new J, higher precision or A_0=14 feasibility calculation is used.
The new complete version is initially open for fresh isolated whole mathematical review.

## Statement

### Uniform module parity and homogeneous-cube consequence

Work over F_2 and put phi=X^2+X+1, chi=Xphi^2=X+X^3+X^5.
For sigma in{1,2}, let M_sigma be the polynomials whose Laurent substitution X=z+z^(-1) has exponents only congruent to sigma or -sigma modulo5.
For EVERY integer m>=1 and every nonzero f in M_1 union M_2, if

    phi does not divide f,
    deg f<5m,
    ord_X f>=2m,

then ord_X f is EVEN.                                      (EP1)

Consequently, for every m>=1, every nonzero phi-unit f in F_2[X] with X^m dividing f and deg f<5m, and every polynomial A(t) in F_2[t] of arbitrary degree with A(0)=1,

    [f(X)A(chi(X))]^3=1 modulo phi^(4m)

implies

    ord_X f>=2m and ord_X f even.                           (EP2)

This asserts parity of the exact endpoint order, not that f is globally square.
Indeed at m=6 the explicit polynomials

    f=X^16(1+chi),
    A(t)=1+t+t^2+t^3+t^4+t^5+t^6+t^7

satisfy the cube hypothesis, but f'=X^16phi^2 is nonzero.     (EP3)

### Original odd half-multiplicity and its compulsory layer

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For an original root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and suppose F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2 and R_can=G_can mod2.
Assume the normalized circle Haar integral of log(G_can(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Assume

    ord_phi R_can<ord_phi U,
    ord_psi R_can>=ord_psi U for every irreducible psi dividing U,
                                               psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power, retaining the canonical U=U_0^q and R_can=R_0^q supplied by C199.
Put A_0=ord_XU/q and suppose A_0=2m with m ODD.

Retain the actual nonnegative integer multiplicities a_b of the order-2^b*5 factors in the SAME zero-Haar integer factorization of G_can.
Specifically, with F_n the integer trace polynomial defined by Phi_n(z)=z^(phi(n)/2)F_n(z+z^(-1)) for n>=3,

    G_can=V_int product_(b>=0) F_(2^b*5)^(a_b),
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq.

Here V_int includes all other factors and the sign; phi(n) in the trace definition is Euler's totient.

Then there must be a UNIQUE power of two ell=2^j such that

    8m<ell<=10m,
    a_(k+j+1)=1.                                          (EP4)

Every original layer with lambda_b>10mq has a_b=0.
The full remaining original layer weight is

    sum_(b!=k+j+1) a_b lambda_b=q(12m-ell).                  (EP5)

All a_b in these statements are original integers, at their original indices; none is divided by q or freely reassigned.
Condition (EP4) is NECESSARY and is not asserted sufficient for a formal full gate or an original realization.

In particular no original input in this domain can have A_0=2m for any odd m such that (8m,10m] contains no power of two.
This excludes m=1,3,5,9,11, and the infinite family

    m=2^h+1, h>=2, equivalently A_0=2^(h+1)+2.              (EP6)

For m=7, corresponding to A_0=14, the unique power in (56,70] is64.
The theorem forces a_(k+7)=1 and remaining layer weight20q.
It does NOT exclude A_0=14, and establishes neither compatibility nor infeasibility of its remaining conditions.

Before contradiction the complete degree identities are

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(4m-deg B)>0,

where U_0=X^(2m)phi^(14m)Y and B is the unique complete complement defined in the proof.
All complete factors, saturated surpluses, original q and integer layer costs are retained.
Other original domains, even m, sufficiency of the compulsory layer and unrestricted Task completion are not asserted.

### Canonical square-times-composition extraction

Use the complete module domain of (EP1): m>=1, f!=0, phi prime to f, f in M_sigma for sigma=1 or2, deg f<5m and ord_Xf>=2m.
There are canonically prescribed polynomials V in F_2[X] and H in F_2[t] such that

    f=V^2 H(chi), H(0)=1,
    V!=0, phi prime to V, V in M_(3-sigma),
    ord_XV=ord_Xf/2,
    2deg V+5deg H=deg f<5m.                               (SC1)

Here canonical has a precise polynomial meaning.
For the unique module expression f=X F(chi)+X^4G(chi) or f=X^2F(chi)+(X^3+X)G(chi), H is the monic gcd(F,G).
The two coefficients of V in the OPPOSITE module have gcd1.
This condition is called primitive only RELATIVE TO THESE TWO MODULE COEFFICIENTS.
The pair(V,H) is the unique pair satisfying the displayed global factorization, H(0)=1, the opposite-module requirement and that relative primitivity.
It says nothing about irreducibility, global squarefreeness or complete cyclotomic support of V.

For the first module the prescribed recipe is

    reduce F_o(t)/G_e(t)=A(t)/B(t), gcd(A,B)=1, B(0)=1,
    F=tA^2H, G=B^2H,
    V=Xphi A(chi)+X^2B(chi)
     =X^2(A+B)(chi)+(X^3+X)A(chi).

The subscripts e,o mean K(t)=K_e(t^2)+tK_o(t^2).
If F=0, use A=0,B=1,H=G.
For the second module and m>=2, put G=tJ and use

    reduce F_e(t)/J_e(t)=A(t)/B(t),
    gcd(A,B)=1, A(0)=B(0)=1,
    F=A^2H, J=B^2H,
    H=gcd(F,J)=gcd(F,G),
    V=X[A(chi)+(1+X^3)B(chi)]
     =X(A+B)(chi)+X^4B(chi).

For m=1 in the second module, f=X^2 and the recipe is V=X,H=1.
Every reduction is of an exact rational function over F_2, and each gcd is monic.

### Guaranteed finite extraction and the exact endpoint valuation

Let r_2=nu_2(m), so m=2^(r_2)m_odd with m_odd odd.
Starting f_0=f, apply (SC1) at the integer parameters m_i=m/2^i for i=0,...,r_2.
All these steps are valid, producing

    f_i=f_(i+1)^2 H_i(chi), H_i(0)=1,

with the module alternating each time.
Consequently

    f=f_(r_2+1)^(2^(r_2+1))
          product_(i=0)^(r_2) H_i(chi)^(2^i).              (SC2a)

For the canonical recipes, EVERY H_i with i>=1 is1, so in fact

    f=f_(r_2+1)^(2^(r_2+1)) H_0(chi),
    deg f=2^(r_2+1)deg f_(r_2+1)+5deg H_0,
    2^(nu_2(m)+1) divides ord_Xf.                          (SC2b)

This integer-parameter induction alone asserts no next step after i=r_2 and does not claim nu_2(ord_Xf)=nu_2(m)+1 or identify the global Frobenius power of f.
The subsequent actual-degree classification (SC4) is stronger and uses a different, endpoint-based termination argument.
The intermediate polynomials need only satisfy the complete MODULE domain; descent of a homogeneous cube equation is not assumed.

In the homogeneous-cube domain (EP2), write f=X^mB with phi prime to B and deg B<4m.
Then the stronger exact endpoint conclusion is

    ord_XB>=m>0,
    nu_2(ord_XB)=nu_2(m).                                 (SC3)

For its FIRST canonical extraction f=V^2H(chi), the complete B has the exact polynomial factorization

    B=[V/X^(m/2)]^2 H(chi)                       if m is even,
    B=X[V/X^((m+1)/2)]^2 H(chi)                  if m is odd.

Every displayed quotient is a polynomial.
Neither formula asserts B, f or H(chi) globally square; (EP3) remains an explicit nonsquare control.

### Complete module classification from the actual degree bound

The complete (EP1) domain has the following exact classification:

    f=X^Q H(chi), H in F_2[t], H(0)=1,
    Q is a power of2, 2m<=Q<5m,
    5deg H<5m-Q.                                          (SC4)

Conversely EVERY polynomial of this displayed form belongs to the (EP1) domain, in the unique module whose Laurent residue pair is plus-or-minus Q modulo5.
Both Q=ord_Xf and H are unique, and H is exactly the first canonical gcd of (SC1).
The capital Q is an endpoint exponent and is NOT the original maximal Frobenius power q.

More generally, for a nonzero phi-unit f in either module, put e=ord_Xf>=1 and N=deg f.
If N<(5/2)e, then e is a power of2 and f=X^eH(chi), H(0)=1, with5deg H<(3/2)e.
The converse to this actual-degree statement also holds.

In particular every homogeneous cube for f=X^mB necessarily has

    B=X^(Q-m)H(chi)

with precisely the range and strict degree bounds in (SC4), as well as (SC3).
This statement classifies the complete MODULE domain.
The sharper homogeneous-cube condition, including its exact endpoint boundary and every auxiliary coefficient, is classified next.

### Exact homogeneous-cube classification and all auxiliary coefficients

Let m>=1, f!=0 be prime to phi, X^m divide f and deg f<5m.
For A(t) in F_2[t] with A(0)=1, the homogeneous cube

    [f(X)A(chi(X))]^3=1 modulo phi^(4m)

holds if and only if f has the form

    f=X^Q H(chi), Q a power of2,
    2m<Q<5m, H(0)=1, 5deg H<5m-Q,                         (SC5)

and A has the following uniquely prescribed class modulo t^(2m).
For Q=2^s define the polynomial

    h_Q(X)=1+sum_(i=0)^(s-1) X^(Q-2^i),

using the empty sum h_1=1, and let x(t) be the formal inverse of chi at0.
Then

    A(t)=[H(t)h_Q(x(t))]^(-1) modulo t^(2m).

The inverse is of a formal series with constant1 and is reduced to its polynomial class modulo t^(2m).
Every higher coefficient of A is unrestricted, with no degree bound on A.
The endpoint Q=2m is impossible for the cube, even though it is allowed in the module classification (SC4).
This is a complete formal homogeneous-cube classification, not an original-input realization.

### Necessary original dichotomy at arbitrary half-multiplicity

Retain EVERY original P,T,field,residual,Haar,unique-unsaturation,q and integer-layer hypothesis stated above, but now let A_0=2m with ANY integer m>=1, replacing only the oddness restriction in the original EP application.
For the SAME actual normalized Y and complete B, the following necessary dichotomy holds.

If an odd original layer contributes with8m<lambda_b/q<=10m, there is a unique such power ell=2^j, its actual coefficient is a_(k+j+1)=1, and the remaining original layer weight is q(12m-ell).
Every original layer above10mq vanishes.

If NO odd original layer contributes in that interval, the full gate yields the homogeneous cube for f=X^mB.
Then the canonical extraction (SC1)--(SC2), exact endpoint valuation/factorization (SC3) and the sharper shape B=X^(Q-m)H(chi) of (SC5), with2m<Q<5m, hold for THIS actual complete B.
Moreover its SAME actual low-X polynomial Y=L(X^2) modulo X^(4m), deg L<2m, is forced to satisfy

    L(t)=[(1+t+t^2)^(7m) H(t)h_Q(x(t))]^(-1)
                                                 modulo t^(2m).       (SC6)

These cases are determined by the actual intermediate-layer occurrence, not by a choice of normalized coefficients.
For odd m the second case contradicts the adopted even ord_XB, recovering (EP4).
For even m it provides a stronger necessary endpoint restriction and complete square-times-composition factorization.
No converse, full original-input descent or sufficient construction is asserted.

The original q, nonsquare U_0/R_0, root precision6m, full precision8m and all original integer layers stay unchanged.
The complete degree identities remain r=q(30m+deg Y), w=q(26m+deg Y+deg B), r-w=q(4m-deg B)>0.
The extraction constructs no smaller integer T, canonical Y, trace field or original residual system.
In particular it does not enter or settle the inhomogeneous A_0=14 branch.

## Argument

### Exact inverse series and module interfaces

The [adopted C636 module theorem](Yin_C_G0636_v1.md#statement) supplies the unique representations

    M_1: f=X F(chi)+X^4G(chi),
    M_2: f=X^2F(chi)+(X^3+X)G(chi),
    F,G in F_2[t].

Their distinct leading degrees modulo5 imply deg F,deg G<m when deg f<5m.
Under ord_Xf>=2m and the phi-unit hypothesis, their constants are respectively

    M_1: F(0)=0,G(0)=1,
    M_2: F(0)=1,G(0)=0.

Indeed the X coefficient forces F(0)=0 in the first module and G(0)=0 in the second.
At a phi root, X^4=X and X^3+X=X^2, so the remaining coefficient must be1.
This also applies at m=1.

There is a unique formal series x(t) in tF_2[[t]] with chi(x(t))=t.
To prove existence and uniqueness, write x(t)=t+sum_(n>=2)c_n t^n.
In the coefficient of degree n in x+x^3+x^5, the coefficient c_n appears with coefficient1, and every other term uses only earlier c_i.
Thus recursive coefficient comparison uniquely defines x, without any analytic convergence assertion.
Its linear coefficient1 makes substitution order-preserving: for every nonzero polynomial h, ord_t h(x(t))=ord_X h.

The formal chain rule gives

    (1+x^2+x^4)x'=1,
    t=x(1+x^2+x^4),
    t x'=x.                                               (EP7)

The factor1+x^2+x^4 is a formal unit; x/t is also a well-defined unit series.
Comparison of coefficients in t x'=x shows that every EVEN-degree coefficient of x is zero.
Thus x has only odd powers, x^3=t H(t^2) for a series H in F_2[[u]], and x^6 is a series in t^2.

For every polynomial K of degree below n, write uniquely

    K(t)=K_e(t^2)+tK_o(t^2).

Then deg K_e<=floor((n-1)/2) and deg K_o<=floor((n-2)/2).
An impossible negative bound means the polynomial is zero; throughout, deg0=-infinity.
These exact bounds account for both parities of m in the two determinant arguments.

### The first module forces even endpoint order

Let f=X F(chi)+X^4G(chi) with deg F,deg G<m, F(0)=0,G(0)=1.
Put

    E(t)=F(t)+x(t)^3G(t),
    f(x(t))=x(t)E(t).

The hypothesis ord_Xf>=2m gives ord_tE>=2m-1.
Write x^3=tH(t^2), decompose F,G and E into even and odd series, and put u=t^2.
The exact formulas are

    E_e(u)=F_e(u)+uH(u)G_o(u),
    E_o(u)=F_o(u)+H(u)G_e(u).

The order condition gives

    ord_u E_e>=m, ord_u E_o>=m-1.

Form the POLYNOMIAL determinant

    Delta_1(u)=F_eG_e+uF_oG_o
              =G_eE_e+uG_oE_o.                           (EP8)

The second expression has order at least m.
For m=2r, all four polynomial pieces F_e,F_o,G_e,G_o have degree at most r-1, so deg Delta_1<=2r-1=m-1.
For m=2r+1, the even pieces have degree at most r and the odd pieces at most r-1, so again deg Delta_1<=2r=m-1.
These inequalities include m=1 with vanishing odd pieces.
Therefore Delta_1=0 identically.

Since G_e(0)=G(0)=1, division by G_e is permitted in F_2[[u]].
Equation (EP8) gives

    E_e=(uG_o/G_e)E_o,
    E(t)=tE_o(t^2)[1+tG_o(t^2)/G_e(t^2)].

The bracket has constant1.
Moreover E_o cannot vanish, since then E_e=0 and f(x(t))=0, contradicting f!=0 and order preservation.
Thus ord_tE=1+2ord_uE_o is odd.
It follows that ord_Xf=1+ord_tE is even.

### The second module forces even endpoint order

Let f=X^2F(chi)+(X^3+X)G(chi), where F(0)=1,G(0)=0.
Write G=tJ.
The strict bounds give deg F<m and deg J<m-1.
The exact identity in F_2[X,X^(-1)], with polynomial product, is

    (X+X^(-1))chi=(X^2+1)phi^2=1+X^6.

Consequently

    f=X^2[F(chi)+(1+X^6)J(chi)].                           (EP9)

If m=1, then J=0,F=1 and f=X^2, which has even order2.
Assume m>=2.
By (EP7), write1+x(t)^6=H(t^2), where H(0)=1, and put

    E(t)=F(t)+H(t^2)J(t),
    f(x(t))=x(t)^2 E(t).

Then ord_tE>=2m-2>=2.
The constant coefficient forces J(0)=1 because F(0)=1.
In the even/odd decomposition,

    E_e=F_e+HJ_e,
    E_o=F_o+HJ_o,
    ord_uE_e>=m-1, ord_uE_o>=m-1.

Form the POLYNOMIAL determinant

    Delta_2=F_eJ_o+F_oJ_e
           =E_eJ_o+E_oJ_e.                               (EP10)

The second expression has order at least m-1.
For m=2r, the bounds are

    deg F_e,deg F_o<=r-1,
    deg J_e<=r-1, deg J_o<=r-2,

so deg Delta_2<=2r-2=m-2.
For m=2r+1>=3, they are

    deg F_e<=r, deg F_o<=r-1,
    deg J_e,deg J_o<=r-1,

so deg Delta_2<=2r-1=m-2.
Thus Delta_2 vanishes identically for every m>=2.

Since J_e(0)=1, its inverse is a formal unit and

    E_o=(J_o/J_e)E_e,
    E(t)=E_e(t^2)[1+tJ_o(t^2)/J_e(t^2)].

The bracket has constant1, and E_e!=0 because f!=0.
Hence ord_tE=2ord_uE_e is even, so ord_Xf=2+ord_tE is even.
This completes (EP1) for both modules and all m.

### Homogeneous-cube consequence and the global-square boundary

Under the hypotheses of (EP2), the [adopted C634 uniform theorem](Yin_C_G0634_v1.md#statement) gives precisely f in M_1 union M_2 and ord_Xf>=2m.
It applies to arbitrary auxiliary degree and all coefficients.
Equation (EP1) therefore gives the even order, proving (EP2).
C634's old m=5-specific parity tables are not used.

For the explicit nonsquare control (EP3), one has deg f=21<30, ord_Xf=16 and phi prime to f.
The elementary identity

    X^6=1+chi+phi^3

gives X^48=1+chi^8+phi^24.
Also (1+chi)sum_(i=0)^7 chi^i=1+chi^8.
Therefore

    f A(chi)=X^16(1+chi^8)=X^64 modulo phi^24.

Since X^3+1=(X+1)phi, one has X^192+1=(X+1)^64phi^64, so the cube is1 modulo phi^24.
Yet f'=X^16phi^2 is nonzero.
Thus even endpoint order and the homogeneous local cube do not imply that f is globally square.
This is an exact polynomial control, not a native experiment or original-input construction.

### Actual normalized gate and every original layer

For an original input in the stated domain put A_0=2m.
The [actual C199v4 normalization and gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate), [complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) and [C199v5 original interfaces](Yin_C_G0199_v5.md#statement) give

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3),
    H_0=X^(2m)Y, C_00=X^(2m)Y(chi)Psi^(14m),
    V_0=R_0/phi^(12m)=H_0B,
    D_0=V_0+C_00^3 in phi^(2m),
    deg B<4m, phi prime to B,

where Psi=phi(chi), Y is monic prime to Xphi, and B includes EVERY saturated surplus and every extra remainder factor.
All of H_0,C_00,V_0 and B are phi-local units.

The [C197v3 derivative interface](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives X^(4m) dividing the derivative of the normalized T-support odd part W_U.
Writing Y=J^2W_U, with J(0)=1, gives X^(4m) dividing Y'.
The [C609v2 actual complete-factor parity](Yin_C_G0609_v2.md#statement) gives even ord_XB.
This uses the actual complete V_0 factorization, not an assumption that Y is square or that its factors individually have even multiplicity.

The exact root, old relation and full gate are

    Z_0^11=H_0C_00^2 modulo phi^(6m),
    H_0^6=C_00^21 modulo phi^(8m),
    Z_0D_0+H_0V_0S_star=0 modulo phi^(8m).                  (EP11)

The inherited D_0 order2m makes the product independent of the lift of Z_0: changing it by phi^(6m) changes the product by phi^(8m).
The gate also requires S_star in phi^(2m).

Retain every original a_b and lambda_b from the statement, with total weight12mq.
Only odd a_b with4mq<lambda_b<12mq contribute to S_star.
For such a layer, ell=lambda_b/q is a power of two and the exact term is

    X^(ell/2)(X+1)^ell phi^(12m-ell).                       (EP12)

The source index is b=k+j+1 when ell=2^j.
The high window excludes b=0,1, so distinct contributing indices give distinct ell and distinct phi orders.
The coefficient X^(ell/2)(X+1)^ell is a unit at phi.
Consequently the smallest phi order in any nonempty sum of these terms cannot cancel.

If a nonzero odd layer had ell>10m, choose the largest such ell.
Its term would have unique least phi order12m-ell<2m, contradicting S_star in phi^(2m).
Thus every layer in this range has even a_b.
But the original weight gives a_b ell<=12m and ell>10m, hence a_b<=1; therefore a_b=0.
Every occurring lambda_b is already strictly below12mq by C199, so this proves the asserted vanishing for all lambda_b>10mq.

### Why an odd m forces the unique middle layer

Suppose that no odd layer contributes with8m<ell<=10m.
After the preceding elimination, every term of S_star has ell<=8m, and hence

    S_star in phi^(4m).

Since Z_0 is a unit, the full equation (EP11) then forces D_0 in phi^(4m).
It follows that

    H_0B=C_00^3 modulo phi^(4m).                           (EP13)

The actual derivative X^(4m)|Y' gives the full low-X polynomial

    Y=L(X^2) modulo X^(4m),
    L(0)=1, deg L<2m.

Every low coefficient is retained.
Substitution of chi, whose phi order is2, gives

    C_00=Q^2 modulo phi^(8m),
    Q=X^m Psi^(7m)L(chi).                                 (EP14)

Taking sixth powers of (EP13) doubles its error order to at least8m: first square, then cube.
Use H_0^6=C_00^21 at that SAME precision and divide by the unit C_00^18.
The result is

    B^6C_00^3=1 modulo phi^(8m).

Substitution of (EP14) gives [(BQ)^3+1]^2=0 modulo phi^(8m).
Since phi is irreducible, the exact square valuation yields

    (BQ)^3=1 modulo phi^(4m).

Now take f=X^mB and A(t)=(1+t+t^2)^(7m)L(t).
They have A(0)=1, phi prime to f, X^m dividing f and deg f<5m.
Thus (EP2) forces ord_Xf even.
But ord_Xf=m+ord_XB is odd because m is odd and C609 gives even ord_XB.
This contradiction proves that an odd original layer MUST occur in(8m,10m].

That interval has ratio10/8<2, so it contains at most one power of two.
For its unique ell=2^j, the original weight bound a_(k+j+1)ell<=12m and ell>8m gives a_(k+j+1)<=1.
Its required odd parity therefore means the actual integer a_(k+j+1)=1.
Subtracting its original weight qell proves (EP5).
This is only a necessary layer constraint; it does not assert that the remaining gate, support, normalization or characteristic-zero equations can be met.

### Exact examples, infinite family and retained degree costs

The following direct integer inequalities check the stated small exclusions:

| m | Interval (8m,10m] | Consecutive powers bounding it |
| --- | --- | --- |
| 1 | (8,10] | 8,16 |
| 3 | (24,30] | 16,32 |
| 5 | (40,50] | 32,64 |
| 9 | (72,90] | 64,128 |
| 11 | (88,110] | 64,128 |

The lower endpoint8 in the first row is excluded by the open endpoint.
Thus none of the five intervals contains a power of two.

For every h>=2, m=2^h+1 is odd and

    2^(h+3)<8m,
    10m=10*2^h+10<16*2^h=2^(h+4),

where the last strict inequality follows from10<6*2^h.
These are consecutive powers of two, proving the infinite family (EP6) without a numerical range restriction.

For m=7 the actual correction window is28<ell<84.
The power64 lies in(56,70], so its original index is k+7 and its coefficient must be1.
Its correction has phi order84-64=20, which is below4m=28 but at least2m=14.
Thus the homogeneous projection is unavailable from the established gate alone.
The total84q weight leaves20q for all other original layers.
No further A_0=14 test or sufficiency argument is made.

Finally the exact complete factors give

    deg U_0=30m+deg Y,
    deg R_0=26m+deg Y+deg B.

The zero-Haar integer cyclotomic factorization has leading coefficient1 or-1, so reduction preserves deg G_can.
The original maximal q then gives precisely the degree identities in the statement.
No factor, surplus, field degree or original layer is removed to obtain the contradiction.
The global nonsquareness of U_0,R_0 remains C199's actual normalization conclusion, not an inference from either local cube or endpoint parity.
This theorem needs no later finite full-jet exclusion, and does not use C667's remaining-range result.

### Exact global extraction from the first determinant

Take the first module in (EP1), with its unique F,G and F(0)=0,G(0)=1.
The determinant already proved in (EP8) is the POLYNOMIAL identity

    F_e(u)G_e(u)+uF_o(u)G_o(u)=0.

Multiplying out at u=t^2 gives

    F(t)G_e(t^2)=tF_o(t^2)G(t),
    F(t)/G(t)=tF_o(t^2)/G_e(t^2).                          (SC7)

G and G_e are nonzero and G_e(0)=1, so the rational identities and the indicated unit at0 are legitimate.
Reduce F_o(t)/G_e(t) to coprime A(t)/B(t).
The monic denominator has B(0)=1 because it divides G_e.
Frobenius in F_2(t) gives

    F/G=tA^2/B^2.

The numerator tA^2 and denominator B^2 are coprime: gcd(A,B)=1 and B(0)=1.
From FB^2=GtA^2, polynomial divisibility therefore gives

    F=tA^2H, G=B^2H

for a polynomial H, with H(0)=1 from G(0)=1.
The coprime pair makes H=gcd(F,G).
If F=0, then F_o=0, the reduced ratio is0/1 and the same conclusion holds with A=0,B=1,H=G; no zero numerator is inverted.

Now Xchi=X^2phi^2, so exact substitution gives

    f=[Xphi A(chi)+X^2B(chi)]^2 H(chi).

The displayed V equals X^2(A+B)(chi)+(X^3+X)A(chi), proving it is in M_2.
At a phi root its value is X^2B(0)=X^2!=0.
Thus V is nonzero and prime to phi.
Since H(0)=1, H(chi) has order0 at both X and phi.
The exact order and degree equalities of (SC1) follow from the product and deg chi=5.
Finally the two M_2 coefficients of V are A+B and A, whose gcd is gcd(B,A)=1.

### Exact global extraction from the second determinant

For the second module, F(0)=1,G(0)=0.
At m=1 the degree bounds force F=1,G=0, so f=X^2, V=X and H=1 directly.
Assume m>=2 and write G=tJ.
The order argument in (EP9)--(EP10) already gave J(0)=1 and

    F_eJ_o+F_oJ_e=0.

Therefore

    F(t)J_e(t^2)=F_e(t^2)J(t),
    F(t)/J(t)=F_e(t^2)/J_e(t^2).                           (SC8)

Both F_e and J_e have constant1.
Reduce F_e(t)/J_e(t) to coprime A(t)/B(t); the canceled monic gcd also has constant1, so A(0)=B(0)=1.
Then F/J=A^2/B^2 and exact polynomial divisibility gives

    F=A^2H, J=B^2H, H=gcd(F,J), H(0)=1.

Since F(0)=1, the factor t is prime to F, whence

    gcd(F,G)=gcd(F,tJ)=gcd(F,J)=H.

Use the exact polynomial identity (X+X^(-1))chi=1+X^6 from (EP9).
It gives

    f=X^2[F(chi)+(1+X^6)J(chi)]
     =[X(A(chi)+(1+X^3)B(chi))]^2 H(chi).

The square-root factor is V=X(A+B)(chi)+X^4B(chi), so it belongs to M_1.
At a phi root, 1+X^3=0 and V=XA(0)=X!=0.
The same endpoint and full degree identities follow.
The two M_1 coefficients A+B and B are coprime.
The exceptional m=1 output V=X has module coefficients1,0, also coprime.

### Uniqueness of the prescribed primitive module factor

The preceding recipes establish existence with H=gcd(F,G).
For completeness, suppose another pair(W,K) has f=W^2K(chi), K(0)=1, with W a phi-unit in the opposite module whose two coefficients P,Q are coprime.

If f belongs to M_1, write W=X^2P(chi)+(X^3+X)Q(chi).
The identity X^6+X^2=Xchi+X^4 gives the unique M_1 coefficients of W^2K(chi):

    F=tQ^2K, G=(P+Q)^2K.

The phi-unit condition on W gives P(0)+Q(0)=1, since its phi residue is X^2(P(0)+Q(0)).
Also gcd(Q,P+Q)=1.
Thus tQ^2 and(P+Q)^2 are coprime, including the factor t, so gcd(F,G)=K.

If f belongs to M_2, write W=XP(chi)+X^4Q(chi).
The identity X^8=X^2+(X^3+X)chi gives

    F=(P+Q)^2K, G=tQ^2K.

The phi residue of W is X(P(0)+Q(0)), so P(0)+Q(0)=1.
Again the two factors preceding K are coprime and gcd(F,G)=K.

Therefore K=H in either case.
The equality W^2=V^2 then forces W=V because Frobenius is injective on the integral domain F_2[X].
This proves exactly the uniqueness asserted in (SC1), with its explicit relative-primitivity normalization.
No uniqueness among arbitrary unnormalized square-times-composition presentations is asserted.

### Finite descent and collapse of every later composition factor

Put r_2=nu_2(m) and m_i=m/2^i.
At each i<=r_2, assume f_i is in the (EP1) domain at parameter m_i.
Extraction gives f_i=f_(i+1)^2H_i(chi) with H_i(0)=1.
For i<r_2 the next parameter is an integer and the exact degree/order identities give

    deg f_(i+1)<5m_i/2=5m_(i+1),
    ord_Xf_(i+1)>=m_i=2m_(i+1).

The output remains nonzero, a phi-unit and in the opposite module.
Thus the next step is valid without requiring a new homogeneous cube or auxiliary polynomial.
Induction proves all r_2+1 promised extractions.
Multiplication of the identities gives (SC2a), retaining the degree identity

    deg f=2^(r_2+1)deg f_(r_2+1)
                +5 sum_(i=0)^(r_2) 2^i deg H_i.

Every output's two module coefficients have gcd1, by the recipes.
At the next first-module extraction this directly means H_i=gcd(F,G)=1.
At a next second-module extraction with parameter at least2, its formula uses J=G/t; F(0)=1 ensures gcd(F,J)=gcd(F,G)=1.
In particular when the preceding first-module output has coefficients(A+B,A) and is eligible for the next second-module step, its order condition makes A(0)=0; dividing A by t cannot introduce a common factor with A+B.
At the second-module boundary m_i=1 the already explicit output has H_i=1 as well.
Thus EVERY i>=1 has H_i=1, proving the collapsed factorization and full degree identity (SC2b).

Since each H_i(chi) is a unit at X, the endpoint order is multiplied by2 at each extraction.
It follows that2^(r_2+1) divides ord_Xf.
After the final odd parameter m_(r_2), the available inequalities do not assert another legal integer-parameter step.
We make no unbounded descent, valuation equality for f, or global-square inference for H_0(chi).

### The homogeneous complement has exact two-adic endpoint order

By (EP2), every homogeneous-cube f=X^mB enters the complete module domain.
Thus ord_Xf>=2m and (SC2b) apply.
Write m=2^(r_2)m_odd and ord_Xf=2^(r_2+1)n.
Then

    ord_XB=ord_Xf-m=2^(r_2)(2n-m_odd).

This difference is at least m>0, while2n-m_odd is odd.
Therefore nu_2(ord_XB)=r_2 exactly, proving (SC3).

At the first extraction ord_XV=ord_Xf/2>=m.
For even m, divide f=V^2H(chi) by X^m to obtain the displayed B square-times-composition formula.
For odd m, write X^m=X^(m+1)/X; ord_XV>=m>=(m+1)/2 makes V/X^((m+1)/2) a polynomial and gives the displayed extra X factor.
All divisions are thus polynomial, and H(0)=1 prevents hidden endpoint cancellation.
The nonsquare control (EP3) remains valid; neither the endpoint valuation nor these exact factorizations says H(chi) is square.

### Actual-degree extraction without an integer-parameter cutoff

Let f be a nonzero phi-unit in M_sigma, put e=ord_Xf>=2 and N=deg f, and assume N<(5/2)e.
The same module constants F(0),G(0) used above hold because e>=2.
We prove the exact polynomial extraction and primitive output under THIS actual-degree hypothesis.
The previously established algebra from a zero determinant remains applicable; it remains to verify the determinant degree/order bounds without using an integer m.

In the first module, G(0)=1.
If F=0, the exact formula f=X^4G(chi) immediately gives V=X^2,H=G and primitive output, without assigning a degree to the zero F.
Assume F!=0 and put a=deg F,b=deg G.
Distinct leading degrees modulo5 give

    a<=floor((N-1)/5), b<=floor((N-4)/5),
    a+b<=floor(2N/5)-1<=e-2.                              (SC9)

The last inequality uses the STRICT bound2N/5<e.
Use the same inverse series x(t) and E=F+x^3G.
Its exact order is e-1.
The even/odd components consequently satisfy

    ord_u E_e>=ceil((e-1)/2),
    ord_u E_o>=ceil((e-2)/2).

For the first polynomial determinant Delta_1=F_eG_e+uF_oG_o, the identity Delta_1=G_eE_e+uG_oE_o gives

    ord_u Delta_1>=floor(e/2).

The two polynomial terms have degree at most floor((a+b)/2):
for the second term use1+floor((a-1)/2)+floor((b-1)/2)<=floor((a+b)/2).
By (SC9),

    deg Delta_1<=floor((e-2)/2)=floor(e/2)-1.

Thus Delta_1=0, including either parity of e.
The exact first-module recipe, canonical gcd and primitive output therefore apply.

In the second module, if G=0 then F(0)=1 gives e=2.
Now N<5 and N=2+5deg F imply F=1.
Hence f=X^2, with V=X,H=1, as required.

Assume G!=0.
Since G(0)=0, deg G>=1; its leading degree3+5deg G cannot cancel the other module's degree2 modulo5.
Therefore N>=8 and N<(5/2)e forces e>=4.
Write G=tJ.
The exact order e-2 of E=F+(1+x^6)J is then positive, so its constant coefficient forces J(0)=1.
This verifies the needed denominator unit before using any ratio.
Put a=deg F and b=deg J.
Again the distinct leading degrees give

    a<=floor((N-2)/5),
    b<=floor((N-3)/5)-1,
    a+b<=floor(2N/5)-2<=e-3.                              (SC10)

Here the even/odd components of E have orders at least ceil((e-2)/2) and ceil((e-3)/2).
For Delta_2=F_eJ_o+F_oJ_e=E_eJ_o+E_oJ_e this gives

    ord_u Delta_2>=ceil((e-3)/2)=floor(e/2)-1.

The degree of each polynomial term is at most floor((a+b-1)/2), so (SC10) gives

    deg Delta_2<=floor((e-4)/2)=floor(e/2)-2.

Thus Delta_2=0.
The full second-module recipe applies, including F(0)=J(0)=1, the monic gcd, opposite module and primitive coefficients.

Both cases therefore yield f=V^2H(chi), with H(0)=1, e_V=e/2 and

    N_V=(N-5deg H)/2<=N/2<(5/2)e_V.                       (SC11)

In particular every e>=2 under the actual-degree hypothesis is EVEN.
The next extraction is governed by (SC11), not by an unjustified fractional m.

### Complete classification and its exact converse

Begin with a nonzero phi-unit module polynomial satisfying e>=1 and N<(5/2)e.
If e>=2, repeatedly apply the actual-degree extraction while the endpoint is at least2.
Every output remains a phi-unit in the opposite module and satisfies the same strict degree/order ratio by (SC11).
Every output is primitive in its two module coefficients, so all composition factors after the first equal1, with exactly the gcd/division justification already proved.

Each step halves the positive integer endpoint.
If the initial e were not a power of2, after nu_2(e) steps it would reach an odd endpoint greater than1, contradicting the evenness forced by the same extraction.
Thus e=2^s for an integer s>=0, and after s steps the endpoint is1.

At endpoint1 the strict degree ratio gives N<5/2, hence degree at most2.
In M_1 the only nonzero polynomial of degree at most2 is X.
In M_2 the only such polynomial is X^2, whose endpoint is2 rather than1.
The terminal polynomial is therefore exactly X.
This also proves the initial e=1 case directly, without any extraction.
It follows that

    f=X^(2^s)H_0(chi), H_0(0)=1,
    N=2^s+5deg H_0<(5/2)2^s.

The initial canonical gcd is H_0, and after fixing e=2^s the injectivity of substitution H(t) going to H(chi(X)) makes H_0 unique.

Conversely, take e=2^s and H(0)=1 with5deg H<(3/2)e.
The Frobenius identity gives

    (z+z^(-1))^e=z^e+z^(-e).

Since chi(z+z^(-1))=z^5+z^(-5), every exponent in H(chi) is a multiple of5.
Their product therefore has support in the pair plus-or-minus e modulo5.
A power of2 is prime to5, so this is exactly one of the two allowed module pairs.
The polynomial X^eH(chi) has endpoint e, is a phi-unit and has degree e+5deg H<(5/2)e.
This proves both directions of the actual-degree classification.

For the (EP1) domain, e>=2m and N<5m imply N<(5/2)e, so the classification gives Q=e with Q a power of2 and

    2m<=Q, Q+5deg H<5m.

These are exactly the bounds in (SC4).
Its converse follows from the same module membership and the stated endpoint/degree/unit inequalities.
For a homogeneous f=X^mB, divide by X^m to obtain the complete necessary B shape X^(Q-m)H(chi).
No auxiliary polynomial A is constructed from an arbitrary classified shape, so no homogeneous-cube converse is inferred.

### A polynomial approximation with an unavoidable odd error

For Q=2^s, the polynomial h_Q of (SC5) obeys the exact identity

    h_Q(X)^2+X^Q h_Q(X)+1=X^(2Q-1).                       (SC12)

For s=0 this is1+X+1=X.
For s>=1, the squares in h_Q^2 have exponents2Q-2^j for j=1,...,s.
The nonconstant terms in X^Qh_Q have exponents2Q-2^i for i=0,...,s-1, together with X^Q.
The terms with1<=i=j<=s-1 cancel, the j=s term cancels X^Q, and the remaining term is X^(2Q-1).
The two constant1 terms cancel as well, proving (SC12) without a finite test.

Work formally at t=1, with w=t-1 and

    X_0=t+t^(-1)=w^2/(1+w), ord_wX_0=2.
    delta=t^Q+h_Q(X_0).

Since X_0^Q=t^Q+t^(-Q), the element t^Q satisfies y^2+X_0^Qy+1=0.
Equation (SC12) therefore gives

    delta^2+X_0^Qdelta=X_0^(2Q-1).                        (SC13)

The right side is nonzero of order4Q-2.
If d=ord_wdelta were at least2Q, both left terms would have order at least4Q, a contradiction.
Thus d<2Q; the two left terms have distinct orders2d and2Q+d, so2d=4Q-2.
Consequently

    ord_w[t^Q+h_Q(X_0)]=2Q-1.

Every nonzero formal series k(X_0)-h_Q(X_0) has even w-order, twice its X_0-order.
It cannot cancel this odd leading order without introducing an earlier nonzero term.
Therefore NO k in F_2[[X_0]] can satisfy

    t^Q=k(X_0) modulo w^(2Q).

This is the exact obstruction at the endpoint, including all coefficients of the approximating formal series.

### Simultaneous fifth-root matching and the sharp boundary

Necessity begins with the complete module classification (SC4), supplied to every cube input by (EP2).
Thus f=X^QH(chi) with Q a power of2, Q>=2m and H(0)=1.
Work over an algebraic closure of F_2 containing a primitive fifth root xi.
For j=1,2,3,4 write z=xi^j t and X(z)=z+z^(-1), and put

    gamma_j=xi^(jQ)+xi^(-jQ).

The nonzero primitive fifth-root traces satisfy phi=0, so gamma_j is a NONTRIVIAL cube-one constant in F_4.
The Frobenius and trace identities give exactly

    X(z)^Q=gamma_j t^Q+xi^(-jQ)(t^Q+t^(-Q)),
    t^Q+t^(-Q)=X_0^Q,
    chi(X(z))=t^5+t^(-5)=chi(X_0).                       (SC14)

The second summand in the first identity has order2Q.
All four roots have the SAME X_0, h_Q(X_0) and chi(X_0); only their nonzero gamma_j constants differ.

For any A with A(0)=1, put J=HA, so J(0)=1.
At z=xi^j the residue of fA(chi) is gamma_j.
A principal unit u with constant1 satisfies

    u^3-1=(u-1)(u^2+u+1),

and the second factor has constant1.
Thus the cube condition at that point is equivalent, at the SAME precision, to

    X(z)^Q J(chi(X_0))=gamma_j modulo w^(4m).

If Q=2m, the second summand in (SC14) already has order2Q=4m.
After dividing by gamma_j and the unit J(chi(X_0)), the condition would require t^Q to equal a formal series in X_0 modulo w^(2Q).
The odd-error obstruction from (SC13) forbids this.
Therefore Q>2m is necessary.

If Q>2m, then2Q-1>=4m.
Equations (SC13)--(SC14) give, simultaneously for every j,

    X(z)^Q=gamma_j h_Q(X_0) modulo w^(4m).

Choose the polynomial class

    A_*(u)=[H(u)h_Q(x(u))]^(-1) modulo u^(2m).            (SC15)

It exists and has constant1 because each factor in the denominator has constant1.
The inverse x of chi is two-sided as a formal composition: chi has zero constant and linear coefficient1, and the same recursive uniqueness used in (EP7) proves x(chi(X_0))=X_0.
Substituting u=chi(X_0) into (SC15) gives

    H(chi(X_0))A_*(chi(X_0))h_Q(X_0)=1 modulo w^(4m),

since chi(X_0) has w-order2.
It follows that fA_*(chi)=gamma_j modulo w^(4m) at ALL four nonidentity fifth roots, hence its cube is1 there.

To return to F_2[X], note the exact factor identity

    phi(X(z))=z^(-2)(z^4+z^3+z^2+z+1).

It has a simple zero at each xi^j.
Also X'(z)=1+z^(-2) is nonzero there, so the substitution preserves the local order of every polynomial at its trace root.
The four points cover both distinct roots of phi.
The simultaneous order4m congruences therefore imply phi^(4m) divides[fA_*(chi)]^3-1 in F_2[X].
This proves sufficiency, with the full stated precision and one common auxiliary class.

### Uniqueness of the auxiliary class and unrestricted high coefficients

Suppose A and A_* both solve the cube for this f and have constant1.
At every xi^j they have the same residue gamma_j, so the principal-unit equivalence just used gives f(A-A_*)(chi)=0 to order4m.
Since f is a phi-unit, (A-A_*)(chi) is divisible by phi^(4m).

For a nonzero polynomial K(u), write K=u^ell K_0 with K_0(0)=1.
Then chi=Xphi^2 gives the EXACT valuation

    ord_phi K(chi)=2ell.

The factor X is a unit at phi, as is K_0(chi), so there is no hidden cancellation.
Thus ord_u(A-A_*)>=2m; if the difference is zero the same congruence is immediate.
Conversely changing A_* by any multiple of u^(2m) changes fA(chi) only by a multiple of phi^(4m), preserving the cube.
This proves uniqueness modulo u^(2m) and permits every higher coefficient, of arbitrary degree.
Together with the sharp boundary and complete module classification, it establishes the full if-and-only-if statement (SC5).

### Actual original applicability without an original-input descent

The original normalized C199 identities used in (EP11)--(EP14) hold for every A_0=2m with m>=1.
Oddness of m was used in the v1 contradiction only AFTER the homogeneous cube had been obtained.
For the general original application retain the SAME actual

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3),
    H_0=X^(2m)Y, V_0=H_0B,
    C_00=X^(2m)Y(chi)Psi^(14m),
    D_0=V_0+C_00^3 in phi^(2m),
    deg B<4m, phi prime to B.

The actual normalized derivative gives X^(4m)|Y', and C609 gives even ord_XB.
The original total weight is12mq.
The root Z_0 is defined at precision6m, and D_0 in phi^(2m) pays the lift error in the full precision8m equation

    Z_0D_0+H_0V_0S_star=0 modulo phi^(8m),
    H_0^6=C_00^21 modulo phi^(8m).

The requirement S_star in phi^(2m), distinct phi orders of its original terms and the integer weight eliminate all layers above10mq exactly as already proved.
None of these steps uses m odd.
There is at most one power of two in(8m,10m]; if its odd layer occurs, its original coefficient is at most1 by weight and hence exactly1, with the original index k+j+1.
This is the first case of (SC6).

If no such odd layer occurs, S_star lies in phi^(4m).
The unit Z_0 gives D_0 in phi^(4m), hence H_0B=C_00^3 at that precision.
Write Y=L(X^2) modulo X^(4m), L(0)=1,deg L<2m.
Substitution gives C_00=Q^2 modulo phi^(8m), Q=X^mPsi^(7m)L(chi).
Taking sixth powers of H_0B=C_00^3 raises the error order to8m.
The old relation yields B^6C_00^3=1 at8m; exact square valuation then yields(BQ)^3=1 at4m.
This is the homogeneous cube with f=X^mB and A(t)=(1+t+t^2)^(7m)L(t).

Apply (SC1)--(SC5) to this SAME complete B.
If m is odd, the valuation equality makes ord_XB odd, contradicting C609 and recovering the compulsory layer of (EP4).
If m is even, it gives nu_2(ord_XB)=nu_2(m) and the exact complete shape B=X^(Q-m)H(chi) with Q a power of2,2m<Q<5m and all strict degree bounds of (SC5), with every degree term included.
Moreover the actual auxiliary polynomial is A(t)=(1+t+t^2)^(7m)L(t), so (SC15) forces

    L(t)=[(1+t+t^2)^(7m) H(t)h_Q(x(t))]^(-1)
                                                 modulo t^(2m).

The actual derivative already gives deg L<2m, so this retains every low-X coefficient of the SAME Y.
These classified homogeneous data do not by themselves satisfy the full inhomogeneous gate or any original characteristic-zero condition.
This proves the necessary dichotomy only.
The integer layers are never divided by q, all costs remain r=q(30m+deg Y), w=q(26m+deg Y+deg B), and no surplus factor is dropped.

The canonical module roots f_i are new characteristic-two polynomials, not normalized original inputs.
Their relative primitivity is only gcd1 of two module coefficients; it implies no assertion about the original P,T,Y, fields, residuals, complete-order groups or maximal q.
In particular we do not infer that the original q can be increased, that R_0 or U_0 is square, or that an original solution descends to a smaller multiplicity.
The A_0=14 branch has its compulsory intermediate layer and is outside this homogeneous application.
No additional native or feasibility work is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:45 |
| status | open |
| reason | Preserve the complete adopted EP1--EP14 mathematics of physical v1 and add canonical global square-times-composition extraction, its relative-primitive uniqueness, all later H_i=1, the guaranteed nu_2(m)+1-step factorization, complete actual-degree module classification f=X^QH(chi), exact homogeneous-cube existence and unique auxiliary jet with sharp Q>2m boundary, and actual original necessary dichotomy including the SAME Y low jet. No global-square or original-input descent is inferred. Every original q/layer/canonical degree and6m/8m precision remains. Fresh isolated whole review must cover this complete v2; v1 review is not extended automatically. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole uniform parity, extraction and original statement](#statement) | Entire preserved EP1--EP6 plus new SC1--SC6, including canonical uniqueness, primitive-core collapse, complete module classification, homogeneous-cube iff/unique auxiliary jet, exact endpoint valuation, nonsquare control, original mandatory layer/infinite family and necessary arbitrary-m dichotomy. |
| argument | [Whole determinant, extraction and gate proof](#argument) | Complete preserved EP1--EP14 reasoning and new SC7--SC15/global divisibility and gcd normalization, actual-degree determinant bounds/finite termination, both module classification directions, telescoping odd error and simultaneous four-root homogeneous iff, all degrees and original gate precisions. |
| dependency | [Uniform Laurent support/order](Yin_C_G0634_v1.md#statement) | Only its all-m support and order theorem, to place homogeneous-cube f in the complete module domain; no m=5-specific parity or later remaining range. |
| dependency | [Uniform complete module bases](Yin_C_G0636_v1.md#statement) | Exact free-module representations, unique coefficients, degree bounds and constants for every m; no A_0=12 finite-image conclusions. |
| dependency | [Actual original normalization](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unique-unsaturated domain and canonical maximal common q, unchanged by module extraction. |
| dependency | [Full normalized original gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Complete original integer layers/weight, root6m/error8m, inherited D and S order2m, old relation and lift independence, valid at arbitrary A_0=2m. |
| dependency | [Complete complement and degrees](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual phi-unit B with deg B<4m, every saturated surplus/extra factor and canonical degree costs; extraction is of the complete B. |
| dependency | [Normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divides W_U' and hence Y', without replacing actual Y by a global square. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB for the SAME original V_0, used to exclude the homogeneous case at odd m only. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:58 |
| status | proved |
| reason | Adopt the ENTIRE physical v2 after main reading of the complete preserved EP and new SC statement/proof and isolated whole R853. Exact canonical extraction, relative-primitive uniqueness, finite extraction, complete actual-degree module classification, sharp homogeneous-cube iff and unique auxiliary low jet are proved at their full scopes. The original arbitrary-m necessary dichotomy retains the SAME complete B and Y, all integer layers, q,6m/8m precision and degrees. No global square, original-input descent, inhomogeneous A0=14 exclusion or unrestricted Task completion follows. Physical v1 and R1012 remain at their own unchanged scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole uniform parity, extraction and original statement](#statement) | Entire preserved EP1--EP6 plus new SC1--SC6, including canonical uniqueness, primitive-core collapse, complete module classification, homogeneous-cube iff/unique auxiliary jet, exact endpoint valuation, nonsquare control, original mandatory layer/infinite family and necessary arbitrary-m dichotomy. |
| argument | [Whole determinant, extraction and gate proof](#argument) | Complete preserved EP1--EP14 reasoning and new SC7--SC15/global divisibility and gcd normalization, actual-degree determinant bounds/finite termination, both module classification directions, telescoping odd error and simultaneous four-root homogeneous iff, all degrees and original gate precisions. |
| dependency | [Uniform Laurent support/order](Yin_C_G0634_v1.md#statement) | Only its all-m support and order theorem, to place homogeneous-cube f in the complete module domain; no m=5-specific parity or later remaining range. |
| dependency | [Uniform complete module bases](Yin_C_G0636_v1.md#statement) | Exact free-module representations, unique coefficients, degree bounds and constants for every m; no A_0=12 finite-image conclusions. |
| dependency | [Actual original normalization](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unique-unsaturated domain and canonical maximal common q, unchanged by module extraction. |
| dependency | [Full normalized original gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Complete original integer layers/weight, root6m/error8m, inherited D and S order2m, old relation and lift independence, valid at arbitrary A_0=2m. |
| dependency | [Complete complement and degrees](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual phi-unit B with deg B<4m, every saturated surplus/extra factor and canonical degree costs; extraction is of the complete B. |
| dependency | [Normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divides W_U' and hence Y', without replacing actual Y by a global square. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB for the SAME original V_0, used to exclude the homogeneous case at odd m only. |
| review | [New entire-v2 independent finding](../audits/reviews/Yin_R_G0853_v1.md#whole-v2-canonical-cube-classification-finding) | Complete EP1--EP14 and SC1--SC15, both module/gcd recipes and all zero boundaries, actual-degree descent/converses, exact odd error and four-root matching, every auxiliary coefficient and SAME-Y original applicability; all source/native/prior-review limits preserved. |

