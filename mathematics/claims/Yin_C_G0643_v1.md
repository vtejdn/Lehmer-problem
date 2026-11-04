---
author: Yin
---
# Uniform endpoint parity and the necessary dyadic layer for odd half-multiplicity

Human author Yin.
Root proposed the formal inverse, two module determinant arguments and dyadic-window application.
The same_trace contributor checked and completed the exact degree bounds, the m=1 case, all formal-unit divisions and original precisions, the necessary actual layer multiplicity, the infinite family and the nonsquare control example.
Both are mathematical contributors; neither independently reviews this new proof.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused reuse inspected the adopted C634 uniform support/order theorem, C636's uniform module bases, C197/C199's actual normalized inputs and C609v2's complete-factor parity.
Those fixed results do not contain the general module parity or necessary dyadic-layer theorem below.
The [D1 candidate](../drafts/Yin_D_G0001.md#uniform-endpoint-parity-candidate) records development provenance, not a logical dependency.
This is a materially broader statement than C634's m=5 parity conclusion, so C634 remains unchanged.
No native mathematical computation, new J, order scan or multiplicity-fourteen feasibility calculation is used.

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
This theorem needs no later finite full-jet exclusion, and does not use C640's remaining-range result.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:19 |
| status | open |
| reason | Register the all-m module endpoint parity, homogeneous-cube consequence with an explicit nonsquare control, and the complete necessary actual dyadic layer for every odd half-multiplicity on the stated original domain. This excludes the exact no-power window family, including infinitely many multiplicities. Every original q/layer and degree cost is retained; A_0=14 receives only its necessary64q layer and remaining20q weight. No native computation was used. Fresh isolated whole mathematical review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform parity and exact original layer](#statement) | EP1--EP6, including all m, arbitrary auxiliary degree, nonsquare control, original compulsory unit multiplicity and infinite no-power family; no A_0=14 exclusion or layer sufficiency. |
| argument | [Full determinant and original gate proof](#argument) | Formal inverse, both parity-specific polynomial degree bounds and unit divisions, m=1 boundary, full original-layer noncancellation, sixth-power/square-root precisions and exact costs. |
| dependency | [Uniform Laurent support/order](Yin_C_G0634_v1.md#statement) | Only its all-m support and order theorem, to place every homogeneous-cube f in the complete module domain; no reliance on its m=5-specific parity proof or later remaining ranges. |
| dependency | [Uniform complete module bases](Yin_C_G0636_v1.md#statement) | Exact M_1/M_2 free-module representations, degree bounds and constants for every m; no use of its A_0=12 finite-image conclusions. |
| dependency | [Actual original normalization](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unique-unsaturated domain and canonical maximal common q. |
| dependency | [Full normalized original gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Complete original integer layers/weight, root6m/error8m, inherited D and S order2m, old relation and lift independence. |
| dependency | [Complete complement and degrees](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual phi-unit B with deg B<4m, every saturated surplus/extra factor, and canonical degree costs. |
| dependency | [Normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divisibility of W_U' and hence Y', without replacing complete Y by a global square. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB for the SAME complete original V_0, at all allowed even A_0. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:28 |
| status | proved |
| reason | Adopt the entire uniform endpoint-parity and compulsory original-layer theorem after main reading of complete C643 and isolated whole R849. Both formal-unit determinants cover every m and all small cases; the original gate and integer weight force the unique power in (8m,10m] with actual coefficient1 for odd m, excluding the complete no-power family. All actual q, integer indices, precision and degree expenses remain. The nonsquare control and A0=14 necessary64q/remaining20q boundary exclude global-square, sufficiency and unrestricted-completion inferences. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform parity and exact original layer](#statement) | EP1--EP6, including all m, arbitrary auxiliary degree, nonsquare control, original compulsory unit multiplicity and infinite no-power family; no A_0=14 exclusion or layer sufficiency. |
| argument | [Full determinant and original gate proof](#argument) | Formal inverse, both parity-specific polynomial degree bounds and unit divisions, m=1 boundary, full original-layer noncancellation, sixth-power/square-root precisions and exact costs. |
| dependency | [Uniform Laurent support/order](Yin_C_G0634_v1.md#statement) | Only its all-m support and order theorem, to place every homogeneous-cube f in the complete module domain; no reliance on its m=5-specific parity proof or later remaining ranges. |
| dependency | [Uniform complete module bases](Yin_C_G0636_v1.md#statement) | Exact M_1/M_2 free-module representations, degree bounds and constants for every m; no use of its A_0=12 finite-image conclusions. |
| dependency | [Actual original normalization](Yin_C_G0199_v5.md#statement) | Full original P/T/field/residual/Haar/unique-unsaturated domain and canonical maximal common q. |
| dependency | [Full normalized original gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Complete original integer layers/weight, root6m/error8m, inherited D and S order2m, old relation and lift independence. |
| dependency | [Complete complement and degrees](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Actual phi-unit B with deg B<4m, every saturated surplus/extra factor, and canonical degree costs. |
| dependency | [Normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divisibility of W_U' and hence Y', without replacing complete Y by a global square. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB for the SAME complete original V_0, at all allowed even A_0. |
| review | [Independent whole parity-layer finding](../audits/reviews/Yin_R_G0849_v1.md#whole-uniform-parity-layer-finding) | Entire EP1--EP14, both complete modules/formal determinants and boundary cases, arbitrary auxiliary degree/nonsquare control, all original integer layers and6m/8m precision, exact infinite family and degree costs; prior source/review boundaries retained. |

