---
author: Yin
---

# G0001: reciprocal trace orders, square resultants and doubled Frobenius modules

Date: 2026-10-07.

The complete current mathematical proof is retained in [C243](../claims/Yin_C_G0243_v1.md#reciprocal-trace-domain).
This dated input keeps its full mathematics, with the original formal contribution/review accounts retained in [R519](../audits/reviews/Yin_R_G0519_v1.md#historical-trace-author-finding).

Bounded direct work by assigned AI review_matrix_completion for Yin.
The coordinating AI proposed testing the reciprocal trace reduction and its interaction with powered order indices.
The proofs below refine the arithmetic structure of [L G0059](Yin_L_G0059_v1.md#powered-order-index) and the integral quotient of [L G0063](Yin_L_G0063_v1.md#mixed-sylvester-domain).
No new source, numerical scan or claim of novelty is used.

The useful outputs are an exact trace-order index formula, a genuine two-copy decomposition of the base Frobenius quotient, and a precise factorization of the confluent arithmetic surplus.
Reducing the degree of a polynomial from 2r to r does not by itself halve the entropy cost of the original algebraic flow.

<a id="reciprocal-trace-domain"></a>
## Trace fields and finite-exponent degree guards

Let alpha be a nontorsion algebraic unit with irreducible monic reciprocal minimal polynomial P of degree d=2r.
In particular its constant coefficient is 1.
Write

    z=alpha+alpha^(-1),       K=Q(alpha),       F=Q(z),
    P(t)=t^r T(t+t^(-1)),

where T is monic integral of degree r.
The last representation follows by expressing each t^j+t^(-j) as an integral polynomial in t+t^(-1).
Define

    C_0(x)=2, C_1(x)=x, C_(n+1)=x C_n-C_(n-1),
    U_(-1)(x)=0, U_0(x)=1, U_(n+1)=x U_n-U_(n-1).

For n>=1 these satisfy

    C_n(z)=alpha^n+alpha^(-n),
    alpha^n=U_(n-1)(z) alpha-U_(n-2)(z).              (1)

The map alpha -> alpha^(-1) defines a nonidentity field automorphism sigma of K, since P is reciprocal and alpha is not torsion.
The quadratic relation alpha^2-z alpha+1=0 shows that [K:F]=2 and F is the fixed field of sigma.
Consequently T is the minimal polynomial of z and is separable; no total-reality assumption is being made.

Choose one representative alpha_j from each inverse pair and put z_j=alpha_j+alpha_j^(-1), 1<=j<=r.
For every a>=1 retain the full degree-r polynomial

    T^[a](x)=product_j(x-C_a(z_j)).

It is monic integral and

    P^[a](t)=t^r T^[a](t+t^(-1)).                     (2)

Indeed the inverse pairs of roots give (2) directly.
On K_a=Q(alpha^a), sigma remains nonidentity: otherwise alpha^(2a)=1.
Its fixed field is F_a=Q(C_a(z)), and [K_a:F_a]=2 by the same quadratic argument.
Hence

    [K:K_a]=[F:F_a],
    deg(alpha^a)=2r  iff  deg(C_a(z))=r.              (3)

If this degree guard fails, both full powered polynomials retain the same embedding-fiber multiplicity.
Thus the trace construction does not silently repair a degree drop.
The remaining index statements require (3) for their specified a.
An all-positive-power endpoint from [L G0059](Yin_L_G0059_v1.md#all-positive-power-existence-descent) supplies these guards simultaneously at existence scope.

Distinct positive exponents also give disjoint trace-root sets.
An equality C_a(z_i)=C_b(z_j) implies alpha_i^a=alpha_j^b or alpha_i^a=alpha_j^(-b).
Inversion permutes the original conjugates, so the finite-order Galois argument from L G0057 excludes either equality when a!=b.
The same argument also excludes zero mixed resultants below, independently of within-level degree preservation.

<a id="reciprocal-trace-order-index"></a>
## The powered order index separates trace and inverse-pair contributions

Set

    O=Z[alpha],       B=Z[z],
    O_a=Z[alpha^a],   B_a=Z[C_a(z)].

The unit condition gives alpha^(-1) in O, so B is a subring of O.
The quadratic relation, and alpha not in F, prove the exact direct sum of B-modules

    O=B direct_sum alpha B.                          (4)

For example every nonnegative power of alpha belongs to the right side by (1), and directness follows over F.
Under the degree guard, the analogous assertion is

    O_a=B_a direct_sum alpha^a B_a.

Let

    J_a=[B:B_a],
    W_a=Norm_(F/Q)(U_(a-1)(z))=Res(T,U_(a-1)).

All these are finite/nonzero: vanishing of U_(a-1)(z_j) would imply alpha_j^(2a)=1.
In the basis of (4), the inclusion of O_a has block form

    [ M_a     -mult(U_(a-2)(z)) M_a ]
    [  0       mult(U_(a-1)(z)) M_a ],

where M_a is the inclusion matrix for B_a in B in their monogenic bases.
Therefore

    I_a=[O:O_a]=J_a^2 |W_a|,
    v_p(I_a)=2 v_p(J_a)+v_p(W_a).                    (5)

This is a relation between the displayed monogenic orders, not a statement about maximal orders.
It holds at ramified primes and at p=2 as well as at unramified primes.

The signed version is equally exact.
Put

    j_a=product_(i<j)
          (C_a(z_j)-C_a(z_i))/(z_j-z_i),

the determinant of M_a, so |j_a|=J_a.
Grouping the full Vandermonde ratio b_a of L G0059 by inverse pairs gives

    b_a=W_a j_a^2.                                  (6)

Within each inverse pair the ratio is U_(a-1)(z_j).
Between two pairs the product of the four differences is (z_i-z_j)^2, and the powered version is (C_a(z_i)-C_a(z_j))^2.
Their ratios give (6), with no unexplained sign.
In particular the previously unspecified integer H_a in b_a=W_a H_a is exactly the square j_a^2.

For reference, the signed discriminant identity is

    disc P=(disc T)^2 T(2) T(-2).                    (7)

To see this, write P as the product of t^2-z_j t+1.
Each quadratic has discriminant z_j^2-4, and the resultant of two such quadratics is (z_i-z_j)^2.
The discriminant product formula gives (7).
Also C_a(z)^2-4=(z^2-4)U_(a-1)(z)^2, so (7) at exponent a and the trace discriminant ratio j_a^2 recover I_a^2=J_a^4 W_a^2.
The W_a factor is exactly the inverse-pair/cyclic factor already present in L G0059, where c_(2a)=c_2 W_a^2.

<a id="reciprocal-mixed-resultant-square"></a>
## Mixed resultants are exact integer squares

For a!=b define

    S_(a,b)=Res(T^[a],T^[b]),
    R_(a,b)=Res(P^[a],P^[b]).

The trace resultant is a nonzero integer, and

    R_(a,b)=S_(a,b)^2.                               (8)

Indeed evaluating P^[b] at alpha_j^a and alpha_j^(-a) gives respectively alpha_j^(ar) T^[b](C_a(z_j)) and alpha_j^(-ar) T^[b](C_a(z_j)).
Their product is the square of the trace evaluation.
Multiplying over j proves (8).
The full degree is even, so the determinant convention product_(i,j) (alpha_i^a-alpha_j^b) in L G0063 has the same sign as this resultant.
In fact R_(a,b)>0; no absolute-value sign is needed in (8).
Both identities retain multiplicities if a level is not degree preserving.

For a prime p and q=p^s, s>=1, the Laurent identity C_q(t+t^(-1))=t^q+t^(-q) gives C_q(x)=x^q modulo p.
The substitution Z[x] -> Z[t,t^(-1)], x -> t+t^(-1), is injective over every coefficient field, since its highest Laurent exponent detects the leading coefficient.
Coefficientwise Frobenius then gives

    T^[aq]=T^[a] modulo p,
    p^r divides S_(a,aq),
    p^(2r) divides R_(a,aq).                         (9)

Thus the familiar p^d floor is exactly the square of a p^r trace floor, not an additional independent divisibility input.

<a id="reciprocal-frobenius-two-copy-module"></a>
## The normalized base Frobenius quotient is two copies of a trace quotient

Take a=1 and q=p^s.
Let A be multiplication by alpha on O, and let D be multiplication by z on B.
Define the integral polynomial

    theta_q(x)=rem_T(T(C_q(x)))/p,       deg theta_q<r. (10)

This is integral even at ramified primes: modulo p, T(C_q(x))=T(x^q)=T(x)^q, so its remainder modulo T is zero.
Equation (2) evaluated at alpha^q gives in O

    P(alpha^q)/p=alpha^(rq) theta_q(z).               (11)

The first factor is a unit of O.
Multiplication by theta_q(z) acts separately and identically on the two summands of (4).
Consequently there is an isomorphism of finite abelian groups

    coker(P(A^q)/p)
      isomorphic to (B/theta_q(z) B) direct_sum
                    (B/theta_q(z) B).                (12)

There is also the unnormalized version with p theta_q in place of theta_q.
All groups are finite by mixed-root separation.
This is an integral module assertion, stronger than merely recognizing a square determinant.
By the cyclic elimination and primitive-overlattice construction in L G0063, the group on the left of (12) is the normalized base Frobenius Sylvester quotient.

In particular

    |S_(1,q)|/p^r=|Norm_(F/Q) theta_q(z)|,
    R_(1,q)/p^(2r)=|Norm_(F/Q) theta_q(z)|^2,
    v_p R_(1,q)=2r+2 v_p(Norm theta_q(z)).            (13)

The first equality is stated with absolute values because the signed determinant of theta_q(D) differs from S_(1,q)/p^r by the harmless resultant interchange sign (-1)^(r^2).

Let rho_q=rem_P(P(t^q))/p, as in L G0063.
Reducing (12)'s multiplication maps modulo p gives the precise first-lifting nullity identity

    deg gcd(P mod p, rho_q mod p)
       =2 deg gcd(T mod p, theta_q mod p).            (14)

For any monic f over a field, multiplication by g in the algebra k[x]/f has kernel dimension deg gcd(f,g): writing f=h f_1, g=h g_1 with coprime f_1,g_1, the kernel consists of multiples of f_1 modulo f.
This proof does not require f to be squarefree.
Together with the unit in (11) and the free rank-two decomposition (4), it proves (14) also at p=2 and at nonreduced primes.

Thus the first-lifting test genuinely has half as many polynomial variables, and its extra full valuation is even.
This does not provide a new lower bound for the size of that extra valuation: it is the exact same finite group invariant, repeated twice.

For a degree-preserving a the same assertions apply with alpha replaced by alpha^a, O replaced by O_a, B replaced by B_a and T replaced by T^[a].
The determinant and trace floor remain those in (8)--(9).
Identifying this companion presentation with the original-lattice mixed Sylvester cokernel needs the cyclicity guard described in L G0063 (globally I_a=1, or locally p not dividing I_a).
No general two-copy assertion for that original mixed Sylvester module is inferred solely from its determinant.

<a id="reciprocal-confluent-surplus"></a>
## Exact confluent factorization and the already-counted branch factor

For finitely many distinct positive exponents a with positive multiplicities m_a, assume each selected exponent is degree preserving.
Let V_P be the normalized-derivative confluent Vandermonde on the 2r inverse-paired roots at each level, and V_T the corresponding confluent Vandermonde on the r trace roots C_a(z_j), with the same multiplicities.
The direct product formula of L G0057 gives

    |det V_P|^2
      =|det V_T|^4
          product_a product_j
            |alpha_j^a-alpha_j^(-a)|^(2 m_a^2).       (15)

For completeness, partition all inverse pairs across all levels.
Within one pair the factor on the right is exactly its full Vandermonde difference; between two different pairs the product of the four full differences is the square of the trace difference.
Raising these factors to the two multiplicities and taking the absolute square proves (15).
No differentiation chain rule or omitted derivative factorial enters this argument.

Writing B_0=|T(2)T(-2)|, the extra factor in (15) is

    product_a (B_0 W_a^2)^(m_a^2).                   (16)

Specialize to L G0057: base multiplicity k, selected distinct prime levels p with multiplicity one.
Define the trace arithmetic surplus by

    Q_tr=product_p J_p^2
          product_p (|S_(1,p)|/p^r)^(2k)
          product_(p<q) |S_(p,q)|^2.

Every factor is a positive integer.
If Q_P denotes the original Q_arith of L G0057, then (5), (8) and (9) give the exact identity

    Q_P=Q_tr^2 product_p W_p^2.                      (17)

The extra W_p factors are already the cyclic/index factors of L G0059.
Formula (17) does not manufacture an additional floor by counting the same divisibility a second time.
It specifies precisely what a trace-only surplus would discard.

<a id="reciprocal-trace-lehmer-control"></a>
## The retained small-core control has trace surplus one

Use the Lehmer polynomial and exact controls in [J G0009](../computations/programs/Yin_J_G0009/readme.md).
Its trace polynomial is directly

    T=C_5+C_4-C_2-C_1-1
      =x^5+x^4-5x^3-5x^2+4x+3.                     (18)

Indeed multiplying (18) at x=t+t^(-1) by t^5 reproduces the retained polynomial coefficient by coefficient.
Here

    W_2=Norm z=-3,
    W_3=Norm(z^2-1)=T(1)T(-1)=1.

The retained indices I_2=3 and I_3=1 now give J_2=J_3=1 by (5).
The retained mixed resultants R_(1,2)=2^10, R_(1,3)=3^10 and R_(2,3)=1 imply

    |S_(1,2)|=2^5, |S_(1,3)|=3^5, |S_(2,3)|=1.

Consequently, for the selected primes {2,3} and every k>=1,

    Q_tr=1,       Q_P=9.                            (19)

Thus in this genuine small reciprocal-core control, the complete nontrivial arithmetic surplus comes from the inverse-pair branch factor W_2^2, not from an enlarged trace Frobenius quotient.
This is a structural reading of existing exact evidence, not a new computation or a uniform assertion for other inputs/primes.

<a id="reciprocal-trace-entropy-boundary"></a>
## The trace companion has a different entropy cost

For a complex number w let rho(w) be the larger modulus of the two roots of t^2-w t+1.
Since their product is 1, rho(w)>=1.
The exact original Mahler cost is

    m(P)=sum_(j=1)^r log rho(z_j),
    m(T)=sum_(j=1)^r log max(1,|z_j|).               (20)

These are different functions.
Under the existing monic integral entropy interface in [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001), with the integral-lattice restriction justified as in [L G0061](Yin_L_G0061_v1.md#adjoint-entropy-comparison), multiplication by z on B has algebraic entropy m(T), not m(P)/2.
For example the retained Lehmer control has one positive root alpha>1, so its trace root alpha+alpha^(-1)>2 gives m(T)>log 2, while the accepted control has m(P)<log 1.3.
Thus this actual small-core trace companion has larger entropy than the original flow.

Elementary bounds make the dimension-dependent loss explicit.
For rho=rho(w), the triangle inequality gives |w|<=rho+rho^(-1) and the quadratic equation gives rho^2<=|w| rho+1.
With phi=(1+sqrt(5))/2 this implies

    max(1,|w|)<=2 rho(w),
    rho(w)<=phi max(1,|w|),

and hence

    m(T)<=m(P)+r log 2,
    m(P)<=m(T)+r log phi.                            (21)

The second scalar bound follows by solving the quadratic: for |w|<=1 its positive root is at most phi; for |w|>=1 the ratio of that positive root to |w| is at most phi.

Also |C_a(w)|<=2 rho(w)^a.
A future estimate adapted to these Chebyshev trace values could therefore use the original cost in (20), rather than ordinary trace-companion entropy.
Such an estimate is a separate analytic input, not ruled out here.

What does cancel automatically is the purely formal gain from recognizing a square: dividing (8), (13) or (17) by their common factor of two in logarithmic form also halves the degree and the same repeated determinant cost.
Equation (15) retains the branch cost explicitly.
No entropy gap follows from the square or two-copy identities alone, and no blanket obstruction to all possible trace-based analytic estimates is asserted.

<a id="reciprocal-trace-module-review"></a>
## Review and remaining scope

The complete original 2026-10-07 contribution and review accounts are retained in [R519](../audits/reviews/Yin_R_G0519_v1.md#historical-trace-author-finding).
Their exact author/contributor/whole-check scopes and current finding relationships remain there.
No new source, computation, unrestricted gap or resolution of G0001 is asserted.
