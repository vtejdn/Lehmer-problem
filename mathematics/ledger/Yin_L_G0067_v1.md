---
author: Yin
---

# G0001: scalar congruence, cyclic norms and the exact dyadic-product certificate

Date: 2026-10-07.

The complete current mathematical proof is retained in [C244](../claims/Yin_C_G0244_v1.md#scalar-congruence-norm-domain).
This original dated input keeps its full mathematics; formal contribution/review accounts are retained in [R522](../audits/reviews/Yin_R_G0522_v1.md#historical-scalar-dyadic-author-finding).

Bounded direct reconstruction by assigned AI review_matrix_completion for Yin.
The coordinating AI proposed the direct cyclic-norm proof and balanced scalar lift; the author supplied the dyadic auxiliary product and its exact class-specific optimization.
Actual review and contribution scopes are recorded below.
A subsequent bounded primary-source attribution identified the known log(5)/4 auxiliary certificate, as recorded below.
The proof is direct and uses no external theorem premise, numerical scan or claim of novelty.

The result replaces a double-Vandermonde estimate under full modular collapse by a direct norm bound.
It requires neither degree preservation of selected powers nor a bounded residue prime.
An exact optimization is proved only for explicitly specified dyadic cyclotomic products with their automatic divisibility floors and unit-circle costs.
This is not an optimality theorem over all auxiliary polynomials, arithmetic information or approaches to Lehmer's problem.

<a id="scalar-congruence-norm-domain"></a>
## The order, congruence and exact norm convention

Let alpha be a nontorsion algebraic unit with monic irreducible minimal polynomial P of degree d, let O=Z[alpha], and put

    M=M(P),       m=log M,       beta=alpha^a,       a>=1.

All norms below are field norms from K=Q(alpha) to Q.
They retain all d embeddings even when Q(beta) is a proper subfield.
Thus

    product_sigma max(1,|sigma(beta)|)=M^a.           (1)

The abelian group O is free of rank d.
If a nonzero gamma belongs to p^s O, write gamma=p^s eta with eta in O.
Multiplication by eta on the integral power basis has a nonzero integer determinant, so

    |Norm gamma|>=p^(sd).                            (2)

This argument uses divisibility in the displayed order; no maximal order, ramification hypothesis, or unramified norm convention is required.
If F is a nonzero product of cyclotomic polynomials, then F(beta)!=0, since beta is not a root of unity.
Also beta-c!=0 for every integer c: a rational integer that is an algebraic unit is 1 or -1, either of which would make alpha torsion.

For a nonzero complex polynomial F of degree D, set

    C(F)=max_(|t|=1) |F(t)|.

The maximum-modulus principle applied to F in the unit disk and to t^D F(1/t) in the unit disk proves

    |F(w)|<=C(F) max(1,|w|)^D       for all complex w.

Consequently, whenever F is integral and F(beta) is nonzero,

    |Norm F(beta)|<=C(F)^d M^(aD).                   (3)

Combining (2) and (3), a proved divisibility F(beta) in p^s O gives

    m >= (d/a) [s log p-log C(F)]/D.                 (4)

The exact circle supremum in (3), rather than a coefficient-sum upper bound for it, is relevant to the improvement below.

<a id="cyclic-prime-power-norm-floor"></a>
## The direct cyclic prime-power floor and its limited optimization

Suppose beta=1 modulo pO.
Binomial induction gives, for r>=0,

    beta^(p^r)-1 in p^(r+1) O.                      (5)

Indeed if u=1+p^s v with s>=1, expansion of u^p-1 makes every term divisible by p^(s+1).
For the final term this uses sp>=s+1, which holds also for p=2 and s=1.
There is no division by a nonunit or any reduced-root hypothesis in this induction.

Since C(t^n-1)=2, (4)--(5) prove

    m >= (d/a) [(r+1)log p-log 2]/p^r.              (6)

In particular at p=2 and r=1,

    Norm(beta^2-1) has absolute value >=4^d,
    m >= d log 2/(2a).                              (7)

Equivalently, both beta-1 and beta+1 are divisible by 2 in O.
Their product is nonzero.
The archimedean bound is 2^d M^(2a), which proves (7) directly.
At r=2 the bound in (6) is the same.

The best value within just the tests (6) is explicit:

| Prime | Maximizing r | Maximum coefficient multiplying d/a |
| --- | --- | --- |
| 2 | 1 and 2 | log 2/2 |
| 3 | 1 | log(9/2)/3 |
| p>=5 | 0 | log(p/2) |

For verification put L=log p and l=log 2.
The difference between successive coefficients has the sign of

    L-(p-1)((r+1)L-l).

This expression decreases with r.
At p=2 it is positive at r=0, zero at r=1 and negative thereafter.
At p=3 it is positive at r=0 because 4>3, and negative at r=1 because 27>4.
For p>=5 it is already negative at r=0: (p-2)log p>(p-1)log 2 follows from (p-2)/(p-1)>=3/4 and 5^(3/4)>2.
No optimality beyond this stated family of cyclic tests is implied.

<a id="dyadic-log-five-norm-certificate"></a>
## A stronger exact dyadic product gives log(5)/4

Continue with beta=1 modulo 2O.
Take

    G(t)=(t^2-1)^4(t^2+1)
        =Phi_1(t)^4 Phi_2(t)^4 Phi_4(t),
    deg G=10.

The nine cyclotomic factors are each divisible by 2 when evaluated at beta, so G(beta) belongs to 2^9 O.
In particular this also follows from beta^2-1 in 4O and beta^2+1 in 2O.
On the unit circle write t=exp(i theta) and x=sin^2(theta).
Then

    |G(t)|=2^5 x^2 sqrt(1-x),       0<=x<=1.

Its square has its unique interior maximum at x=4/5: the derivative of x^4(1-x) is x^3(4-5x), and the endpoints give zero.
Therefore

    C(G)=2^9/5^(5/2).

The exact norm estimate (4) is now

    m(P) >= (d/a) log 5/4.                          (8)

This improves (7), since 5>4.
It uses no selected-power degree guard.
The strict increase arises from the exact archimedean cost of a weighted product; it does not presume a stronger p-adic floor.

The exact auxiliary polynomial, degree ten, divisibility weight nine, circle supremum and log(5)/4 constant already appear in Borwein--Dobrowolski--Mossinghoff, *Lehmer's problem for polynomials with odd coefficients*, Annals of Mathematics 166 (2007), printed p.355, Corollary 3.4 and its proof ([retained BDM07 PDF](../literature/pdf/BDM07.pdf)).
The present proof gives the stated monogenic-order congruence form directly; it is not a new auxiliary polynomial or a claim that the source's coefficient-congruence theorem has identical hypotheses.

<a id="dyadic-product-exact-scope-optimum"></a>
## Exact optimum within all dyadic products with the automatic floors

The scope of this optimization is the following precise class.
For arbitrary finitely supported nonnegative integer weights w_j, not all zero, let

    F(t)=product_(j>=0) Phi_(2^j)(t)^(w_j),
    W=sum_j w_j,
    D=sum_j w_j deg Phi_(2^j).

Here Phi_1=t-1 and Phi_(2^j)=t^(2^(j-1))+1 for j>=1.
The congruence beta=1 modulo 2O implies F(beta) in 2^W O.
The normalized coefficient supplied by exactly this floor and the exact circle cost is

    B(F)=[W log 2-log C(F)]/D.                       (9)

Then

    B(F)<=log 5/4,

and the G above attains equality.
Thus (8) is the exact best certificate in this specified class, even allowing all finite dyadic orders and all their nonnegative multiplicities.

Here is a direct proof of the upper bound.
Put c=log 5/4 and let mu be the uniform probability measure on the four distinct roots of

    5t^4+6t^2+5=0.

These roots lie on the unit circle: their squares are z=(-3+4i)/5 and its conjugate.
At these four points,

    integral log|Phi_1| dmu
      =integral log|Phi_2| dmu=log 2-c,
    integral log|Phi_4| dmu=log 2-2c.                (10)

For the first identity the product of the four absolute values is 16/5, by evaluating the monic polynomial t^4+(6/5)t^2+1 at 1 or -1.
For the second, |t^2+1|=|z+1|=2/sqrt(5) at every support point.

For j>=3 put n=2^(j-2), an even positive integer.
At a support point with t^2=z,

    |Phi_(2^j)(t)|=|1+z^n|
       =2 |Re((-3+4i)^(n/2))|/5^(n/2)
       >=2/5^(n/2).                                (11)

The real part in the numerator is an odd integer: in its binomial expansion the term (-3)^(n/2) is odd, and every remaining real term contains a positive even power of 4.
It is therefore nonzero and has absolute value at least one.
Since deg Phi_(2^j)=2^(j-1)=2n, (11) gives

    integral log|Phi_(2^j)| dmu
       >=log 2-c deg Phi_(2^j).                     (12)

All values being integrated are nonzero.
For any product F in the stated class, linearity and log C(F)>=integral log|F| dmu give

    log C(F)>=W log 2-cD,

which is precisely B(F)<=c.
The proof uses a fixed finite measure, not a limiting or numerical optimization.

The automatic floors are part of the scope.
Extra divisibility of specific values, odd-prime norms, different auxiliary polynomials or weighted functions outside these products could change the bound.
Their optimality is not addressed by (9)--(12).

There is a concrete established escape from this restricted class.
Dubickas--Mossinghoff, *Auxiliary polynomials for some problems regarding Mahler's measure*, Acta Arithmetica 119.1 (2005), printed p.70, introduces Q(t)=5t^4+6t^2+5 at exactly the maximizing points of G and combines it with powers of G to improve their auxiliary bound ([retained DM05 PDF](../literature/pdf/DM05.pdf)).
The exact F3 refinement and a strict rational improvement check are retained in [DM05-U001](../audits/literature/DM05/Yin_U001.md#dm05-u001).
Q is outside the dyadic cyclotomic product class used in (9).
This attribution does not adopt that paper's numerical optimization or enlarge the optimality claim proved here.

<a id="balanced-scalar-congruence-gap"></a>
## Arbitrary scalar collapse gives a gap without a bounded prime

Suppose now that beta=c modulo pO for some scalar c in F_p^*.
For odd p choose its balanced integer representative, so 1<=|c|<=(p-1)/2.
By (2), the nonzero value beta-c has norm of absolute value at least p^d.
For every complex w,

    |w-c|<=(1+|c|) max(1,|w|).

Equations (1)--(2) therefore give

    m(P)>=(d/a) log[p/(1+|c|)]
         >=(d/a) log[2p/(p+1)]
         >=(d/a) log(3/2).                           (13)

For p=2 the only nonzero scalar is 1, so (8) applies instead.
Since (3/2)^4>5, the combined conclusion for every rational prime is

    alpha^a is a nonzero scalar modulo pO
       ==> m(P)>=(d/a) log 5/4.                     (14)

In particular, fix C>0.
If a<=Cd and the displayed scalar congruence holds at any prime p, then

    m(P)>=log 5/(4C).                               (15)

No upper bound on p, degree-preservation hypothesis, or separate finite-degree completion is needed for this restricted class.

<a id="scalar-collapse-root-matrix-interface"></a>
## From reduced roots to the actual order congruence

Let A be the companion matrix of P.
The following are always equivalent, including at ramified primes:

    alpha^a=c modulo pO;
    A^a=cI modulo p;
    P mod p divides t^a-c in F_p[t].                 (16)

Indeed O/pO=F_p[t]/(P mod p), and multiplication by t^a-c is the zero map exactly when it annihilates the identity element.
This is the precise order-divisibility input to all preceding norm bounds.

If p does not divide disc P, then P mod p has d distinct roots u_i in the algebraic closure of F_p, all nonzero since P is a unit polynomial.
If all u_i^a equal one common lambda, Frobenius permutes the roots and shows lambda^p=lambda.
Thus lambda is a nonzero scalar c in F_p.
Squarefreeness now implies the polynomial divisibility in (16), or equivalently diagonalization gives A^a=cI.
Conversely that congruence clearly makes all the powered reduced roots equal c.

For p=2 this is exactly the condition P mod 2 divides t^a-1.
The squarefree hypothesis is needed only for inferring order divisibility from distinct-root data.
Knowing (16) directly lets one omit it.
A collision of all reduced eigenvalues without that hypothesis would not eliminate nilpotent Jordan terms.

For any unit and any prime not dividing its discriminant, some exponent makes all reduced roots equal 1, since their orders are finite.
That existence does not bound the exponent relative to d.
The substantive restriction in (15) is a<=Cd.
This work proves no uniform C covering the small-Mahler core and hence no unrestricted Lehmer gap or general entropy-capture conclusion.

<a id="scalar-congruence-norm-review"></a>
## Contribution, review and boundary

The complete original 2026-10-07 contribution and review account is retained in [R522](../audits/reviews/Yin_R_G0522_v1.md#historical-scalar-dyadic-author-finding).
The author, actual contributed mechanisms and separate targeted/whole findings remain at their exact scopes and current relationships there.
No new computation, source-proof audit or unrestricted arithmetic coverage is asserted.
