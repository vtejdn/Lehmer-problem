---
author: Yin
---
# Joint C3/C5 order and cancellation obstructions to zero canonical Haar

Date: 2026-10-20T15:26.
Human author Yin.
This substantive v2 strengthens the same zero-Haar cyclotomic-order question as [v1](Yin_C_G0199_v1.md#statement), preserving its physical proof, [adopted decision](Yin_C_G0199_v1.md#decision-whole-reviewed-2026-10-20) and [whole independent R481 finding](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding).
Root proposed the C3/C5 pairing and the further multiple-of-six cancellation test.
The draft_inventory_later agent completed the uniform trace multiplicities, critical-point and target-degree cases, exact quotient orders, full weighted pairing and strict large-source witness.
Both are mathematical contributors to the new JT1--JT15 and CC1--CC8 arguments.
The complete earlier KC1--KC9 proof is retained below, with its original source and actual review scope.
No numerical computation, parameter enumeration, new source acquisition, original-input realization or independent review of this v2 is claimed.
No later research on orders divisible by 5 is included.

<a id="statement"></a>
## Exact strengthened theorem statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal trace polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integer quotient polynomials

    theta_p=rem_T(T(C_p(X)))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

The values a,b,c are nonzero algebraic integers in this same F.
For either sign s in {1,-1}, assume the complete original residual system f=e+s g=0 and g!=0.
Put

    G=rem_T(theta_5^3-2theta_3^5), w=deg G<r,
    I_can=integral_T log G(z+z^(-1))^2 dmu,
    U=T mod 2, R=G mod 2,
    A=theta_2 mod 2, B=theta_3 mod 2, C=theta_5 mod 2,
    tau=C3 mod 2=X^3+X,
    chi=C5 mod 2=X^5+X^3+X.

The measure mu is normalized Haar probability and circle zeros have the integrable-logarithm convention.
Assume I_can=0 for the conclusions below.

**A. Complete reduced cyclotomic multiplicities.**
One has w>=1, lc(G)=epsilon in {1,-1}, R!=0 and deg R=w.
There is a finite product with all multiplicities retained,

    H(z)=epsilon z^w G(z+z^(-1))
        =product_m Phi_m(z)^(a_m), a_m>=0,
    sum_m a_m phi(m)=2w<d.

Here Phi_m is the m-th cyclotomic polynomial, phi is Euler's totient, and a_1,a_2 are even.
For every occurring odd part n, define

    E_n=sum_(b>=0) a_(2^b n) lambda_b,
    lambda_0=1, lambda_b=2^(b-1) for b>=1,
    nu_n=E_n for n>1, and nu_1=E_1/2 if n=1 occurs.

All irreducible F_2 trace factors of exact odd order n occur in R with the same exponent nu_n.
The phrase exact odd order means the order of z when x=z+z^(-1) is a root of the trace factor; it is independent of inversion or Frobenius conjugacy.
Write Omega_n for all such irreducible factors and

    h_n=min{h>=1:2^h congruent to +/-1 modulo n} for n>1,
    Omega_1={X}, h_1=1.

Every member of Omega_n has degree h_n, and

    deg R=sum_n h_n nu_n |Omega_n|.

Every irreducible factor psi of U belongs to one of these sets; write S_n for the subset occurring in U and N_psi for its exponent.
Both tau and chi preserve the complete geometric U-root set, though tau can send order n to order n/gcd(n,3).

**B. Joint order and multiplicity obstruction.**
For k=3,5 write B_k(n) for the existence of j>=0 with k congruent to +2^j or -2^j modulo n.
In particular B_3(1) and B_5(1) hold.
There must be an occurring odd part n satisfying

    not B_5(n), and
    [5 divides n or (not B_3(n) and 6 divides nu_n)].

Consequently zero Haar is impossible if every occurring n satisfies

    B_5(n) or
    [gcd(n,5)=1 and (B_3(n) or 6 does not divide nu_n)].

This includes the joint-order exclusion with B_5(n) or [gcd(n,5)=1 and B_3(n)], and the exclusion when all occurring n are coprime to 5 and none of the nu_n are divisible by 6.
It does not forbid individual factors in these classes from coexisting with factors outside them.
No upper bound on any original degree, order or multiplicity is imposed.

**C. Exact necessary large-source cancellation witness.**
If every occurring n is coprime to 5, then some n has a factor psi in S_n for which

    N_psi>5nu_n/3,
    6 divides nu_n,
    not B_3(n), not B_5(n), n!=1,3,
    ord_psi B=nu_n/2.

Let psi_chi and psi_tau be the factors of U containing chi(x) and tau(x), respectively, for a root x of psi.
Then

    N_(psi_chi)=nu_n/3,
    N_(psi_tau)=nu_n/2.

The chi target has the same order n and degree h_n; its permutation of S_n is injective.
The tau target has order n/gcd(n,3) and can have a smaller degree.
Its exponent above is measured against the SOURCE nu_n, not an assumed equal target-group multiplicity.
For every source in the full domain the local tau degree is 2 exactly at n=3 and 1 otherwise, and

    ord_psi U(tau)=e_3(x) N_(psi_tau).

The excluded formal n=3 high-source case would instead require N_(psi_tau)=nu_n/4; the complete proof keeps that critical-point distinction.
The claimed witness is necessary, not a sufficient construction of the original characteristic-zero residual equations.

**D. Unchanged original expense and prior mechanism.**
All original resultants are nonzero and

    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log 2,
    sum_m a_m phi(m)=2w<d.

The exact finite-field criterion of v1 remains valid: for any x=z+z^(-1) in an algebraic closure of F_2 with z of odd order n, chi(x) lies in the Frobenius orbit of x exactly when B_5(n) holds.
The same criterion with tau uses B_3(n).
The full reductions of Phi_(2^b n), the n=1 double trace multiplicity and all original field/resultant scalars are retained in the proof.
These conclusions assert no residual existence, no elimination of orders divisible by 5 or the remaining multiple-of-six cancellations, no positive-Haar reciprocal-factor exclusion and no unrestricted paid transfer or Mahler gap.

<a id="argument"></a>
## Complete proof with the fixed predecessor mechanism

The first part retains the complete KC1--KC9 proof of v1.
Its historical author account and exact R481 review remain distinct from the new joint-order and cancellation arguments that follow.

<a id="zero-haar-cyclotomic-order-obstruction"></a>
## The all-degree cyclotomic-order obstruction to zero canonical Haar

Date: 2026-10-20T15:06.
Human author Yin.
Root proposed the all-order exclusion and the exact finite-field trace-orbit criterion below.
The draft_inventory_later agent checked the complete reduction, both directions of the criterion, the original canonical support and multiplicity implications, and wrote this author account.
Both are contributors; this original author account preceded the independent R481 review of v1, whose scope does not cover the new JT or CC arguments below.
No computation, parameter enumeration, new source acquisition or new original-input construction is used.

The responsible question is whether the actual canonical residual can have zero Haar logarithm, with its complete cyclotomic factorization and original weighted resultant expense retained.
The already fixed [C196v3 graph proof](Yin_C_G0196_v3.md#canonical-c5-residue-graph) supplies the exact remainder identity, every original residue-cluster support and the saturation of a self-target orbit.
It does not already state the cyclotomic-order characterization proved here.
For the classical cyclotomic step, [L79's exact CRT-defect argument](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) already gives the complete reduction of Phi_(p^a n) and the exact orders of its roots when p does not divide n.
[Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) owns the inspected definition, integrality and divisor-factorization source interface, with its original inspection limits.
The elementary reduction is reused from L79, not newly attributed to Bel17's characteristic-zero separability statements.
The measure-zero characterization is the product-with-multiplicities convention in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001).
No assertion of new classical cyclotomic or finite-field theory is made.

### Exact actual input and conclusion

Use the complete actual trace domain and full residual equations of [C196v3's statement](Yin_C_G0196_v3.md#statement).
Explicitly, P in Z[z] is monic irreducible reciprocal nontorsion with constant coefficient 1 and degree d=2r; alpha is a root, delta=alpha+alpha^(-1), K=Q(alpha), and F=Q(delta) is totally real.
Its actual monic degree-r trace polynomial is T, with P(z)=z^r T(z+z^(-1)) and [K:F]=2.
For p=2,3,5 put

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    f=e+s g=0, g!=0, s in {1,-1}.               (KC1)

Here C_p(z+z^(-1))=z^p+z^(-p), and a,b,c are the actual nonzero integral quotient values for this same T.
Define

    G=rem_T(theta_5^3-2theta_3^5), w=deg G<r,
    I_can=integral_T log G(z+z^(-1))^2 dmu,
    U=T mod 2, R=G mod 2,
    chi=C5 mod 2=X^5+X^3+X.                      (KC2)

The measure mu is normalized Haar probability and the finite circle zeros use the integrable logarithm convention.
The conclusion is that I_can=0 requires at least one cyclotomic factor Phi_m in the monic reciprocal pullback of G whose odd part n=m/2^(v_2(m)) satisfies

    5 is not congruent to +2^j or -2^j modulo n
                         for every integer j>=0. (KC3)

There is no upper bound on w, r, m, n or their multiplicities in this implication.
It is a necessary obstruction, not an assertion that such an actual residual G exists or that an order satisfying (KC3) supplies one.

### The exact odd-order trace criterion

Let x belong to an algebraic closure of F_2 and choose z with z+z^(-1)=x.
Such z exists by the monic equation z^2+xz+1=0, and its constant coefficient makes z nonzero.
It belongs to the multiplicative group of some finite extension of F_2, so its exact order n is odd.
The other choice of z is z^(-1); when x=0 they coincide at z=1 and n=1.
For every j>=0 the characteristic-two Chebyshev and Frobenius identities give

    chi(x)=z^5+z^(-5),
    x^(2^j)=z^(2^j)+z^(-2^j).                    (KC4)

For nonzero u,v in any field, equality u+u^(-1)=v+v^(-1) holds exactly when u=v or u=v^(-1).
Indeed u is then a root of Y^2-(v+v^(-1))Y+1=(Y-v)(Y-v^(-1)); this argument also covers a repeated root in characteristic two.
Apply this with u=z^5 and v=z^(2^j).
It proves

    chi(x) belongs to the Frobenius orbit of x
      iff 5 congruent +/-2^j modulo n
                            for some j>=0.       (KC5)

The Frobenius orbit is exactly the root set of the irreducible polynomial of x over F_2.
The criterion is independent of the chosen root x of that irreducible polynomial: replacing x by x^(2^k) replaces z by z^(2^k) or its inverse and preserves its odd exact order.
For n=1 the congruence is automatic and chi(0)=0.
If 5 divides n, the congruence is impossible since 2^j is a unit modulo n whereas 5 is not.
No identification of the generator's irreducible degree with a full local residue-field degree is used.

### Cyclotomic reduction identifies the relevant orders

For m=2^a n with n odd, the exact reduction already proved in L79 specializes to

    Phi_m(Z) mod 2 =
       Phi_n(Z) mod 2,                  if a=0,
       (Phi_n(Z) mod 2)^(2^(a-1)),      if a>=1.  (KC6)

For clarity, the second equality is the reduction of
Phi_(2^a n)(Z) Phi_n(Z^(2^(a-1)))=Phi_n(Z^(2^a)).
Frobenius gives the two powers of Phi_n modulo 2, and cancellation is in the polynomial domain F_2[Z].
This includes n=1 and a=1, so no exception for Phi_1, Phi_2 or higher powers of 2 is omitted.
Because n is odd, Z^n-1 has no repeated roots in characteristic two.
Its divisor factorization, or equivalently L79's exact-order proof, shows that the roots of Phi_n mod 2 are precisely the distinct elements of exact order n.
Consequently every geometric root of Phi_m mod 2 has exact order n; the exponent in (KC6) retains all repetitions.

Now suppose I_can=0.
Scalar Jensen and Kronecker, with the full scalar factor, imply that the leading coefficient of G is a sign epsilon in {1,-1} and that

    H(Z)=epsilon Z^w G(Z+Z^(-1))
        =product_m Phi_m(Z)^(a_m),
    a_m>=0, sum_m a_m phi(m)=2w<d.               (KC7)

Only finitely many a_m are nonzero.
The constant coefficient of H is 1, so there is no monomial factor.
If w=0, then G=+1 or -1 and R=1, contradicting the C196v3 assertion that every irreducible factor of the positive-degree U divides R.
Thus the possible zero-Haar case has w>=1 and a nonempty factor product.
The multiplicities of Phi_1 and Phi_2 in H are even because the trace pullback has double contact at Z=1 and Z=-1, respectively; (KC6) itself does not need this additional restriction.
Monicity up to sign implies R!=0 and deg R=w, so there is no degree drop here.

### Original support and full multiplicities force the contradiction

Assume, for contradiction, that every m with a_m>0 fails (KC3), so its odd part satisfies the congruence in (KC5).
Let psi be any irreducible factor of U and let x be one of its roots.
The actual per-cluster consequence (CG4) of C196v3 gives psi|R, hence R(x)=0.
Choose z with z+z^(-1)=x as above.
Reducing the pullback identity in (KC7) gives

    H mod 2=Z^w R(Z+Z^(-1)),

so z is a root of H mod 2 and therefore a root of Phi_m mod 2 for some occurring m.
By (KC6) its exact odd order is the odd part n of that m.
The assumed congruence and (KC5) show that chi(x) is a root of the same psi.
This works for every psi|U, not merely for one cluster carrying some positive part of the original norm.

Write U=product_psi psi^(N_psi), retaining all original exponents.
Since psi(chi(x))=0, the irreducibility of psi gives psi|psi(chi).
The factor psi(chi)^(N_psi) in U(chi) then gives

    ord_psi U(chi)>=N_psi for every psi|U,
    U divides U(chi), hence U divides U(chi)^3.  (KC8)

Possible ramification of chi or collisions with other factors only increase this divisibility.
It does not require U to be squarefree.
But the exact original remainder identity (CG3) in C196v3 is R=rem_U(U(chi)^3).
Equation (KC8) therefore forces R=0, contradicting the nonzero monic reduction from (KC7).
This proves (KC3).
Equivalently, C196v3 guarantees an unsaturated orbit for every nonzero R of degree less than deg U, and (KC5) says that its associated odd order cannot satisfy the stated congruence.
The contradiction concerns self-target orbits, not arbitrary permutations or longer cycles of the full chi-stable root set.

### What this closes and what it leaves

This is an all-degree exclusion for the specified class of occurring cyclotomic orders.
In particular, arbitrary powers of 2 in the orders do not evade it when every odd part satisfies the same congruence criterion.
It does not eliminate an order failing that criterion, bound the number or sizes of such orders, or settle the positive-Haar reciprocal noncyclotomic branch.
No finite table of orders or additional numerical cutoff is substituted for the universal quantifier in (KC3).

All original K11 expenses and multiplicities remain:

    sum_m a_m phi(m)=2w<d,
    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log 2.          (KC9)

Indeed H(alpha)=epsilon alpha^w g, Norm_K(alpha)=1 and [K:F]=2, so the absolute full resultant is |Norm_F(g)|^2.
Every resultant factor is nonzero because P is irreducible nontorsion.
The last inequality is the original full-residual income supplied by [C191v2's all-cluster theorem](Yin_C_G0191_v2.md#statement) at its adopted scope; it is not strengthened by the order test.
The degree of H is 2w, not the field degree d, and phi(m) has not been replaced by m.
Thus the next unresolved zero-Haar object is the same original weighted cyclotomic resultant expression with at least one order satisfying (KC3), subject to the full divided self-composition equations.
No uniform Mahler gap, useful paid transfer or actual realization follows from this necessary order obstruction alone.

The new argument uses C196v3's already adopted graph/remainder theorem with its [whole independent R474 finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding), and reuses L79, Bel17-U001 and Smy08-U001 at the precise scopes stated above.
The draft_inventory_later agent's earlier review of C196v3 does not independently review this new root-proposed application, and its C191 original-return authorship is not presented as an independent recheck of the reused arithmetic income.
This completes the retained KC1--KC9 proof; its actual independent R481 coverage remains the v1 scope only.

<a id="zero-haar-joint-three-five-order-obstruction"></a>
## Joint C3/C5 exclusion by uniform cyclotomic trace multiplicities

Date: 2026-10-20T15:18.
Human author Yin.
Root proposed the joint C3/C5 high-to-low multiplicity pairing and its stronger necessary order condition.
The draft_inventory_later agent verified and completed the uniform trace multiplicities, the critical order-one case, the same-degree factor permutation, all local polynomial valuations and the complete weighted pairing argument.
Both are contributors to this new extension, which is author work awaiting independent review.
The already adopted [C199v1](Yin_C_G0199_v1.md#argument) retains the earlier C5-only application without modification.
This section neither changes that fixed version nor assumes a new review of its source inputs.
No numerical computation, parameter enumeration, new source acquisition or realization of an original residual input is used.

The reuse check uses [C196v3's actual graph proof](Yin_C_G0196_v3.md#canonical-c5-residue-graph) for every-cluster support, exact remainders and the self-target obstruction, and [L79](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) for the complete cyclotomic reduction.
[Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) and [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) retain the exact classical cyclotomic and scalar-Jensen/Kronecker source boundaries used above.
Those inputs do not already give the joint pairing inequality below.
The new issue is the simultaneous actual C3 equation and the uniform multiplicities imposed by a complete cyclotomic factorization, rather than another finite canonical-degree cutoff.

### Same original domain and exact strengthened target

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient 1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume that F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r trace polynomial, with P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integer quotients and full residual system

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    f=e+s g=0, g!=0, s in {1,-1}.               (JT1)

The values a,b,c are nonzero algebraic integers in this same actual field.
Set G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod 2, R=G mod 2, and assume the normalized squared Haar logarithm I_can of G(z+z^(-1)) is zero.
As in the complete scalar argument above, the nonzero constant case is excluded by every-cluster support, w>=1, and

    H(z)=epsilon z^w G(z+z^(-1))
        =product_m Phi_m(z)^(a_m),
    epsilon=lc(G) in {1,-1}, a_m>=0,
    deg R=w, R!=0, sum_m a_m phi(m)=2w<d.        (JT2)

Only finitely many a_m are positive, and the multiplicities of Phi_1 and Phi_2 are even.
For an odd positive integer n and k=3 or 5, write B_k(n) for the condition that k is congruent to +2^j or -2^j modulo n for some j>=0.
In particular B_3(1) and B_5(1) hold.
The strengthened conclusion is that some occurring m, with odd part n=m/2^(v_2(m)), must satisfy

    not B_5(n), and [5 divides n or not B_3(n)]. (JT3)

Equivalently, zero Haar is impossible if EVERY occurring odd part satisfies

    B_5(n) or [gcd(n,5)=1 and B_3(n)].           (JT4)

This does not individually prohibit a factor with (JT4) from coexisting with factors outside that class.
No upper bound on degree, order or multiplicity is assumed.

### Uniform multiplicity at every trace factor of one odd order

For each occurring odd n define

    E_n=sum_(b>=0) a_(2^b n) lambda_b,
    lambda_0=1, lambda_b=2^(b-1) for b>=1.       (JT5)

The full reduction identity in L79 gives H mod 2=product_n (Phi_n mod 2)^(E_n).
The roots in each factor are all primitive roots of exact order n, each with multiplicity E_n.
This retains every dyadic part of every original cyclotomic order, including m=1 and m=2.
Primitive roots of distinct odd orders are disjoint.

Write q(z)=z+z^(-1).
For odd n>1 and a root z of exact order n, one has q'(z)=1+z^(-2)!=0, since z^2!=1.
Thus q is unramified at z and the local multiplicity of R at x=q(z) equals that of H mod 2 at z.
The identity H mod 2=z^w R(q(z)) has a nonvanishing monomial factor at every such z.
The equality q(z)=q(v) is equivalent to v=z or z^(-1), as proved by factoring the quadratic with that trace.
It follows that every trace point of exact odd order n>1, and hence every irreducible trace factor of that order, has the SAME multiplicity

    nu_n=E_n in R,                              n>1. (JT6)

No trace point can belong to two different odd orders.

For n=1 the only point is z=1 and its trace is x=0.
Here the exact identity q(z)=(z+1)^2/z gives local degree 2, so

    nu_1=ord_X R=E_1/2                          if E_1>0. (JT7)

The integer E_1 is even: a_1 and a_2 are even, and lambda_b is even for b>=2.
Thus the double critical point is counted explicitly rather than assigned the unramified formula (JT6).
If n=1 does not occur, no order-one factor is included.

Let Omega_n denote the finite set of monic irreducible trace factors of exact odd order n over F_2.
For n>1 all of them have the same degree

    h_n=min{h>=1: 2^h congruent to +/-1 modulo n}. (JT8)

Indeed q(z)^(2^h)=q(z) holds exactly when z^(2^h)=z or z^(-1), and z has exact order n.
This test is independent of the chosen primitive z.
For n=1 put Omega_1={X} and h_1=1.
Every member of Omega_n occurs in R with the same exponent nu_n; the full cyclotomic polynomial, not a selected subset of its primitive roots, is what supplies this uniformity.
Consequently

    deg R=sum_n h_n nu_n |Omega_n|.             (JT9)

The sum runs over exactly the odd orders with E_n>0.
This formula agrees with deg(H mod 2)=2deg R, including the exceptional factor 2 in (JT7).

### Exact quotient congruences and factor permutations

Put A=theta_2 mod 2, B=theta_3 mod 2, C=theta_5 mod 2, tau=C3 mod 2=X^3+X, and chi=C5 mod 2=X^5+X^3+X.
Monic division commutes with reduction, and 3 and 5 are both 1 modulo 2.
The actual quotient formulas and both residual equations therefore give

    B congruent U(tau) modulo U,
    C congruent U(chi) modulo U,
    R congruent C^3 congruent U(chi)^3 modulo U,
    A^3 congruent B^2+R modulo U,
    A^5 congruent 0 modulo U.                   (JT10)

The last two relations use e+s g=0 and f=0 respectively; both signs become the same equations modulo 2.
No replacement of the divided theta_2 by U(X^2) is made.

By the adopted C196v3 every-cluster result, every irreducible factor of U occurs in R.
For each n let S_n be the subset of Omega_n that occurs in U, and write its positive exponents as N_psi.
Every factor of U belongs to one such S_n.
Furthermore chi sends the root set of U into itself by R=rem_U(U(chi)^3) and the support implication R(x)=0.

The quadratic trace identity used for C199's criterion works for k=3 as well as k=5:
C_k(x) is in the Frobenius orbit of x=q(z) exactly when k is congruent to +/-2^j modulo the exact order n of z.
Thus B_k(n) means that C_k preserves each individual member of Omega_n.
This is an exact self-target assertion, stronger than permuting Omega_n.

Suppose n>1 and gcd(n,5)=1.
Then z -> z^5 is a permutation of primitive order-n roots, commutes with Frobenius and inversion, and therefore induces a permutation pi_n of Omega_n by chi.
Because S_n is chi-closed and finite, pi_n also permutes S_n.
The map chi is unramified at its order-n trace points.
Indeed differentiation of chi(q(z))=q(z^5) in characteristic two gives

    chi'(q(z)) q'(z)=z^4 q'(z^5)!=0,

since both z and z^5 have the same odd order n>1.
Consequently, for psi in S_n,

    ord_psi U(chi)=N_(pi_n(psi)).                (JT11)

No full local residue-field degree or maximal-order assumption enters this polynomial valuation.

### Pairing all high exponents with disjoint low targets

If B_5(n) holds, every psi in S_n is a chi-self-target.
The complete exponent argument of (KC8) gives N_psi<=nu_n individually.
This includes n=1, using the actual exponent nu_1 from (JT7), without differentiating q at z=1.
Therefore this class satisfies sum_(psi in S_n) N_psi<=nu_n |S_n|.

It remains to consider a group with gcd(n,5)=1 and B_3(n).
The case n=1 has already been handled, so take n>1.
Every psi in S_n is a tau-self-target.
The factor psi(tau)^(N_psi) of U(tau), together with (JT10), implies

    B congruent 0 modulo psi^(N_psi).

Call psi high when N_psi>nu_n.
At a high factor, the congruence R=U(chi)^3 modulo psi^(N_psi) has smaller left valuation nu_n.
The unequal-order rule and (JT11) yield 3N_(pi_n(psi))=nu_n.
Likewise A^3=B^2+R modulo psi^(N_psi), with B^2 divisible by psi^(2N_psi), gives 3ord_psi A=nu_n.
Finally A^5=0 modulo psi^(N_psi) gives 5ord_psi A>=N_psi.
Thus every high factor obeys

    3 divides nu_n,
    N_(pi_n(psi))=nu_n/3,
    N_psi<=5nu_n/3,
    N_psi+N_(pi_n(psi))<=2nu_n.                 (JT12)

Its target is not high because nu_n/3<=nu_n, and all these targets are distinct because pi_n is injective.
Hence the high factors and their targets form disjoint pairs.
Every unpaired factor has exponent at most nu_n, by the definition of high.
Summing the pair bounds and the bounds for the remaining factors proves

    sum_(psi in S_n) N_psi<=nu_n |S_n|           (JT13)

for the entire group, including when there are no high factors.
In particular an empty high set requires no artificial target or pairing.
The argument does not assume that every factor in Omega_n occurs in U.

### Complete degree contradiction and retained original expense

Assume every occurring odd order satisfies (JT4).
For each n, the first case or (JT13) applies.
Multiply by its actual common degree h_n, sum all groups, and use S_n subset Omega_n and (JT9).
This gives

    deg U=sum_n h_n sum_(psi in S_n) N_psi
       <=sum_n h_n nu_n |S_n|
       <=sum_n h_n nu_n |Omega_n|=deg R.         (JT14)

But deg R=w<r=deg U by the actual canonical normalization.
The contradiction proves (JT3) with all original factor multiplicities and without a bound on any degree or order.

The full original expenses remain

    sum_m a_m phi(m)=2w<d,
    sum_m a_m log|Res(P,Phi_m)|
       =2log|Norm_F(g)| >=(6d/11)log 2.          (JT15)

These are the exact identities and adopted C191v2 norm input retained in [C199v1 KC9](Yin_C_G0199_v1.md#argument); the new pairing does not improve that income or remove its original degrees.
The remaining zero-Haar question now requires an occurring odd part with neither a C5 self-target nor, when 5 is coprime to it, a C3 self-target.
An order divisible by 5 is not eliminated by this argument, and no occurrence of any remaining order is asserted.
The positive-Haar reciprocal noncyclotomic branch and the unrestricted paid transfer remain open.

The exact logical additions are the uniform trace multiplicities (JT5)--(JT9), the actual joint congruences (JT10), and the full injective pairing (JT11)--(JT14).
The adopted C196v3 graph is reused at its [R474 scope](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding); that prior review does not review the present new deduction, whose author includes its reviewer.
The retained C191 norm floor uses its actual independent R468 coverage rather than a self-review of the author's older original-return contribution.
This completes the joint-order pairing; the following cancellation argument strengthens its necessary condition within the same original domain.

<a id="zero-haar-joint-order-cancellation-boundary"></a>
### Exact cancellation exception and the necessary multiple-of-six multiplicity

Date: 2026-10-20T15:22.
Root proposed testing whether the joint-order bound could be extended without the C3 self-target hypothesis when the uniform multiplicity is not divisible by 6.
The draft_inventory_later agent completed the proof, including the necessarily larger high source, full C3 support closure, cross-order targets and the critical order-three case.
Both are contributors; the new conclusion remains at author-check scope.
This strengthens the same zero-Haar problem using exactly (JT1)--(JT15) and adds no computation or external source.

Keep all the original hypotheses, factor groups and notation of (JT1)--(JT10).
In particular R is nonzero, deg R=w<r, and every factor in Omega_n has its complete uniform exponent nu_n.
No C3 self-target condition is imposed in this subsection.
We will show that zero Haar requires an occurring odd n satisfying

    not B_5(n), and
    [5 divides n or (not B_3(n) and 6 divides nu_n)].
                                                            (CC1)

The integer nu_n is the actual exponent from (JT5)--(JT7), not a selected exponent of a cyclotomic factor before reduction.
In particular, if every occurring odd order is coprime to 5 and every such nu_n is not divisible by 6, zero Haar is impossible.
More generally the forbidden all-order class is

    B_5(n) or
    [gcd(n,5)=1 and (B_3(n) or 6 does not divide nu_n)]
                       for every occurring n.   (CC2)

We also retain the exact local witness that can obstruct this enlarged degree bound.

First, the entire original U-support is closed under tau, not only under chi.
For every psi|U, the relation A^5=0 modulo U implies that A vanishes at every root x of psi.
The already adopted support theorem gives R(x)=0.
Then A^3=B^2+R modulo U gives B(x)=0, and B=U(tau) modulo U gives U(tau(x))=0.
Thus tau sends every source factor to a factor psi_tau of U.
If the source trace has exact odd order n, the target has exact odd order

    n_tau=n/gcd(n,3).                            (CC3)

This follows directly from tau(q(z))=q(z^3), and the trace determines the order up to inversion.
The target degree may be smaller and the target may belong to another order group.

Let e_3(x) be the local degree of tau at a source trace point x.
For n>1 and n!=3, both q'(z) and q'(z^3) are nonzero, and
tau'(q(z)) q'(z)=z^2 q'(z^3) proves e_3(x)=1.
For n=1, x=0 and tau(X)=X+X^3 has local degree 1.
For n=3, x=1 and tau(1+Y)=Y^2+Y^3 has local degree 2.
These are all cases, so exact polynomial factorization gives

    e_3(x)=2 if n=3, and e_3(x)=1 otherwise,
    ord_psi U(tau)=e_3(x) N_(psi_tau).           (CC4)

The order of a polynomial at a geometric root equals its psi-adic exponent, because irreducible polynomials over F_2 are separable.
No residue-field degree multiplier is inserted into (CC4).

Now fix a group with gcd(n,5)=1; its n=1 case is already a C5 self-target, so consider n>1.
The permutation pi_n, local equality (JT11), and uniform exponent nu=nu_n remain available without B_3(n).
Call psi high when N=N_psi>nu.
The exact R congruence alone still gives

    N_(pi_n(psi))=nu/3.                          (CC5)

Consequently 3 divides nu, every high target is low, and the high-to-low pairs remain disjoint.
Put t=ord_psi B, allowing t=infinity if B is the zero polynomial.
If 2t!=nu, the smaller of 2t and nu is strictly below N.
The unequal-order rule applied to A^3=B^2+R modulo psi^N then gives

    3 ord_psi A=min(2t,nu)<=nu.

This includes B=0 by the convention min(infinity,nu)=nu.
The residual f equation gives 5 ord_psi A>=N, and hence

    2t!=nu implies N<=5nu/3.                    (CC6)

There is no use of the order group or degree of psi_tau in this implication.
It treats all cross-order C3 targets permitted by (CC3).

Thus a high source with N>5nu/3 must have the exact cancellation equality 2t=nu.
Together with (CC5), this requires 6 to divide nu.
Because t=nu/2<N and B=U(tau) modulo psi^N, (CC4) also yields the precise target relation

    N>5nu/3 implies
      6 divides nu,
      ord_psi B=nu/2,
      e_3(x) N_(psi_tau)=nu/2,
      N_(pi_n(psi))=nu/3.                       (CC7)

The relation for psi_tau uses the source exponent nu_n; it is not a comparison with the possibly different exponent nu_(n_tau) of R at the target group.
Accordingly it does not justify pairing C3 targets across different order groups.
In the formal n=3 case (CC4) would require N_(psi_tau)=nu/4 and therefore 12 dividing nu.
However n=3 satisfies B_5(3), so every source there already has N<=nu and no high source is possible.
The same is true of n=1.
A genuine witness in (CC7) therefore has n!=1,3 and N_(psi_tau)=nu/2.

If B_3(n) held at a high source, tau would be a self-target and B would be divisible by psi^N, contradicting t=nu/2<N in (CC7).
Likewise B_5(n) would exclude every high source by the self-target saturation bound.
Thus every witness in (CC7) necessarily has neither B_3(n) nor B_5(n).

For a fixed coprime-to-5 group, if every high source has N<=5nu/3, the disjoint pairing (CC5) gives the same inequality (JT13), with no B_3 hypothesis.
In particular this holds whenever 6 does not divide nu, by (CC6)--(CC7).
When B_3 holds, the earlier JT proof supplies the bound even if 6 divides nu.
Together with the B_5 self-target case, every group satisfying (CC2) obeys

    sum_(psi in S_n) N_psi<=nu_n |S_n|.         (CC8)

The full common-degree summation (JT14) then gives deg U<=deg R and contradicts the actual canonical degree.
This proves (CC1)--(CC2).

There is a more explicit necessary witness if every occurring odd order is coprime to 5.
Since deg U>deg R>=sum_n h_n nu_n |S_n|, some group satisfies sum_(psi in S_n)N_psi>nu_n |S_n|.
If all its high sources had N<=5nu_n/3, the disjoint pair bound would contradict this strict group excess.
Therefore that group contains a source satisfying the full (CC7), with neither B_3 nor B_5.
Its C5 target has exponent nu_n/3 and its C3 target, possibly of order n/3, has exponent nu_n/2.
This is a necessary actual polynomial configuration, not a construction or an assertion that exact cancellation suffices to satisfy the characteristic-zero residual equations.

The unchanged full resultants and original degree expense remain (JT15).
Orders divisible by 5 and the remaining multiple-of-six cancellation configurations are not excluded.
No positive-Haar branch or unrestricted transfer is resolved, and no further case enumeration is part of this bounded round.

<a id="exact-inputs"></a>
## Exact inputs and contribution boundaries

| Input | Exact role |
| --- | --- |
| [C196v3](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Same actual trace/full residual domain, CG3 exact remainder, CG4 support at every original cluster and CG5 self-target saturation with complete factor exponents; no later C196 candidate is a premise. |
| [C191v2](Yin_C_G0191_v2.md#statement) | Original norm income abs(Norm_F(g))>=2^(6r/11) at all original local weights, only for the unchanged KC9/JT15 weighted-resultant expense. |
| [L79](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | Complete Phi_(2^b n) reduction and exact odd-order roots, including n=1, every dyadic part and all repeated factors; no later entropy/module deduction. |
| [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Inspected classical definition, integrality and divisor factorization, with its unchanged original-proof and bad-characteristic limits. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Jensen, exact Kronecker product with multiplicities, leading sign and integrable circle zeros. |
| [C199v1](Yin_C_G0199_v1.md#argument) | Physical adopted predecessor and complete KC1--KC9 proof, retained again above; the new JT/CC deduction was not part of its decision. |
| [R481](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) | Actual independent whole v1 consumer review, only at its KC1--KC9 scope. |
| [R474](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual accepted independent C196v3 graph/remainder coverage; not a review of any new present deduction. |
| [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing whole independent C191 original-norm coverage with its actual upstream authorship boundary. |

The uniform trace multiplicities, common factor degrees, permutation/unramified interfaces, exact joint congruences, high/low pairing and all cancellation exceptions are proved completely here.
They do not import an arithmetic realization theorem or an unchecked equal-degree assumption on maximal residue fields.
The draft_inventory_later agent reviewed C196v3 in R474 and coauthored earlier C191 original-return formulas; it is a contributor to the present new proof and claims no independent review of this version.
Root contributed to the upstream graph route and the new JT/CC arguments.
The actual upstream independent evidence is reused only at its corresponding fixed scope.
No mutable draft, pending later Claim, native computation or new external source is a logical premise.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:26 |
| status | open |
| reason | Strengthen the same zero-Haar order question by complete uniform trace multiplicities, joint C3/C5 weighted pairing and the necessary multiple-of-six exact cancellation witness, retaining KC1--KC9, JT1--JT15, CC1--CC8 and all original expenses. Both authors contributed; v1 and its R481 adoption remain at their exact scope. New whole independent review is required. No residual construction, order-divisible-by-5 exclusion or unrestricted transfer is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete joint-order theorem](#statement) | Full actual original domain, uniform multiplicities and critical n=1 trace, all-degree joint-order/cancellation obstruction, strict large-source witness, n=3 local degree, complete weighted resultants and all remaining limits. |
| argument | [Entire retained and new proof](#argument) | Complete KC1--KC9, JT1--JT15 and CC1--CC8: exact quotients, both support closures, all degrees and multiplicities, factor permutations, disjoint pairs, unequal/tied orders, cross-order tau targets and full degree contradiction. |
| dependency | [Original canonical graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | CG3--CG5 in the actual same-T domain, every-cluster support and all exponent saturation; no later revision used. |
| dependency | [Original norm floor](Yin_C_G0191_v2.md#statement) | Complete original Norm_F(g) income only for KC9/JT15; original degrees and every local weight retained. |
| dependency | [Cyclotomic reduction](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | All Phi_(2^b n) reductions and exact odd-order roots with multiplicities and n=1; no unrelated module results. |
| dependency | [Classical cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Retained definition/integrality/divisor-factorization scope, without a new source-proof or bad-characteristic audit. |
| dependency | [Scalar Haar and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalized squared Haar, monic sign, all roots and products with repetitions, constants and circle zeros. |
| support | [Physical adopted predecessor](Yin_C_G0199_v1.md#argument) | Entire KC1--KC9 retained above with the original author/source account; its v1 decision is not extended to JT/CC. |
| support | [Independent predecessor consumer](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) | Whole actual v1 review only, not present-version or new-proof review. |
| support | [Independent graph input](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual upstream C196v3 coverage with reviewer-now-author role disclosed. |
| support | [Independent norm input](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing complete norm interface and old author boundary, not a new independent self-review. |
| support | [Exact current inputs](#exact-inputs) | Nine input/support rows, both contributors, no mutable proof premise, all source boundaries and no computation. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:38 |
| status | proved |
| authority | Internal adoption within Yin's retained-draft zero-Haar and original-transfer inquiry. |
| reason | Adopt complete KC1--KC9, JT1--JT15 and CC1--CC8 through actual whole independent consumer R483. The proof retains every cyclotomic multiplicity and trace degree, exact joint support, disjoint same-order pairing, all unequal/tied valuation cases and the necessary multiple-of-six large-source cancellation witness with its precise C3 target. All original weighted resultants and source/review boundaries remain unchanged. Orders divisible by5, remaining cancellations, positive-Haar reciprocal factors and unrestricted paid transfer remain open. Later same-coset or cross-order author work is not adopted here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete joint-order theorem](#statement) | Full actual original domain, uniform multiplicities and critical n=1 trace, all-degree joint-order/cancellation obstruction, strict large-source witness, n=3 local degree, complete weighted resultants and all remaining limits. |
| argument | [Entire retained and new proof](#argument) | Complete KC1--KC9, JT1--JT15 and CC1--CC8: exact quotients, both support closures, all degrees and multiplicities, factor permutations, disjoint pairs, unequal/tied orders, cross-order tau targets and full degree contradiction. |
| dependency | [Original canonical graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | CG3--CG5 in the actual same-T domain, every-cluster support and all exponent saturation; no later revision used. |
| dependency | [Original norm floor](Yin_C_G0191_v2.md#statement) | Complete original Norm_F(g) income only for KC9/JT15; original degrees and every local weight retained. |
| dependency | [Cyclotomic reduction](../ledger/Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) | All Phi_(2^b n) reductions and exact odd-order roots with multiplicities and n=1; no unrelated module results. |
| dependency | [Classical cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Retained definition/integrality/divisor-factorization scope, without a new source-proof or bad-characteristic audit. |
| dependency | [Scalar Haar and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalized squared Haar, monic sign, all roots and products with repetitions, constants and circle zeros. |
| support | [Physical adopted predecessor](Yin_C_G0199_v1.md#argument) | Entire KC1--KC9 retained above with the original author/source account; its v1 decision is not extended to JT/CC. |
| support | [Independent predecessor consumer](../audits/reviews/Yin_R_G0481_v1.md#zero-haar-odd-order-consumer-whole-finding) | Whole actual v1 review only, not present-version or new-proof review. |
| support | [Independent graph input](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual upstream C196v3 coverage with reviewer-now-author role disclosed. |
| support | [Independent norm input](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Existing complete norm interface and old author boundary, not a new independent self-review. |
| support | [Exact current inputs](#exact-inputs) | Nine input/support rows, both contributors, no mutable proof premise, all source boundaries and no computation. |
| review | [Whole independent joint-order and cancellation finding](../audits/reviews/Yin_R_G0483_v1.md#joint-order-cancellation-consumer-whole-finding) | Entire actual A--D and KC/JT/CC, all five dependencies and five supports, complete uniform multiplicities, critical points, weighted pairing and strict witness; author-overlapping old graph and support closures explicitly reused through actual R474/R624 evidence rather than independently self-reviewed. |

