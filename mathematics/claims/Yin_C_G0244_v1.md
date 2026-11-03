---
author: Yin
---

# Scalar congruences, exact cyclic norms and the complete dyadic-product optimum

This retains the complete original 2026-10-07 proof of [L67](../ledger/Yin_L_G0067_v1.md).
The direct mathematical proof and the historical source-attribution account remain distinct, with all original optimization and coverage restrictions.

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible minimal polynomial P of degree d, let O=Z[alpha], K=Q(alpha), a>=1 an integer, beta=alpha^a and m=log M(P).
All norms retain all d original embeddings even when beta has smaller degree.
For every nonconstant F in Z[t] with F(beta)!=0, degree D and exact unit-circle supremum C(F), every proved divisibility F(beta) in p^s O gives

    m>=(d/a)[s log p-log C(F)]/D.

This follows from exact integral-order norm divisibility and the circle bound inside and outside the unit disk, without maximal-order, ramification or powered-degree hypotheses.
If beta=1 modulo pO, then for every integer r>=0,

    beta^(p^r)-1 in p^(r+1)O,
    m>=(d/a)[(r+1)log p-log 2]/p^r.

Within precisely these single cyclic tests the maximizing r are 1 and 2 at p=2, 1 at p=3, and 0 at p>=5, with respective coefficients log 2/2, log(9/2)/3 and log(p/2).

If beta=1 modulo 2O, the exact auxiliary

    G(t)=(t^2-1)^4(t^2+1),
    deg G=10, G(beta) in 2^9 O,
    C(G)=2^9/5^(5/2)

proves m>=(d/a)log 5/4.
This is the known BDM07 certificate reconstructed at the present order-congruence scope, with no novelty claim or unproved identification of source coefficient-congruence hypotheses.
For every finitely supported sequence of nonnegative integer weights w_j, not all zero, put

    F(t)=product_(j>=0) Phi_(2^j)(t)^(w_j),
    W=sum_j w_j, D=sum_j w_j deg Phi_(2^j),
    B(F)=[W log 2-log C(F)]/D.

The complete finite-measure proof gives B(F)<=log 5/4, and G attains equality.
This optimum concerns exactly these dyadic cyclotomic products with their automatic 2^W floor and exact circle cost, including all finite dyadic orders and multiplicities.
Extra arithmetic divisibility, noncyclotomic auxiliaries such as the retained DM05 Q=5t^4+6t^2+5, other primes and other methods remain outside the optimality assertion.

For any rational prime p and any nonzero scalar residue c, beta=c modulo pO implies m>=(d/a)log 5/4.
For odd p its balanced representative gives the stronger elementary bound m>=(d/a)log[p/(1+abs(c))]>=(d/a)log(3/2); p=2 uses G.
Consequently a fixed exponent budget a<=Cd gives the restricted-class uniform gap log 5/(4C), with no bound on p or powered-degree condition.
At every prime, including ramified ones, this order congruence is equivalent to A^a=cI modp and P modp dividing t^a-c, for the integral companion A.
If p does not divide discP, full reduced-root collapse u_i^a=lambda forces lambda in F_p^* and gives that congruence; without squarefreeness root collapse alone need not kill nilpotent Jordan terms.
No uniform exponent budget covering the small-Mahler core or unrestricted entropy-capture/Lehmer conclusion is proved.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:00 |
| status | open |
| reason | Register the complete original argument with exact domains and source/evidence boundaries; actual whole current review and adoption follow separately. No independent-review label, new research, source acquisition or numerical verification is supplied by registration. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full statement](#statement) | All integral-order/circle bounds, exact cyclic optimizers, complete dyadic product and class-specific optimum, arbitrary-prime scalar implication and root/matrix/order boundaries. |
| argument | [Complete retained proof](#argument) | Entire original norm proof, all binomial floors, exact degree 10 maximum, fixed four-point measure and every dyadic order, balanced scalar inequalities and full semisimple/nilpotent distinction. |
| support | [Original exact certificate attribution](../audits/literature/BDM07/Yin_U001.md#bdm07-u001) | Original2026-10-07 statement/formula provenance at Lemma3.1/Theorem3.3 and printed355 Cor3.4/proof reading; no whole source-proof audit or identity of source and local hypotheses. |
| support | [Explicit noncyclotomic escape](../audits/literature/DM05/Yin_U001.md#dm05-u001) | Only the retained Q mechanism and exact F3/rational-improvement interface outside the dyadic-only class; source numerical optimization/global algorithms are not adopted as premises. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:05 |
| status | proved |
| reason | Adopt the complete scalar/cyclic norm theorem and exact dyadic-product optimum after actual whole current self-review of every order/embedding/valuation/supremum/finite-measure and root-matrix interface. The known certificate attribution, restricted automatic-floor class and missing arithmetic coverage remain explicit; no independent review or all-auxiliary optimum is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All integral-order/circle bounds, exact cyclic optimizers, complete dyadic product and class-specific optimum, arbitrary-prime scalar implication and root/matrix/order boundaries. |
| argument | [Argument](#argument) | Entire original norm proof, all binomial floors, exact degree 10 maximum, fixed four-point measure and every dyadic order, balanced scalar inequalities and full semisimple/nilpotent distinction. |
| support | [Support](../audits/literature/BDM07/Yin_U001.md#bdm07-u001) | Original2026-10-07 statement/formula provenance at Lemma3.1/Theorem3.3 and printed355 Cor3.4/proof reading; no whole source-proof audit or identity of source and local hypotheses. |
| support | [Support](../audits/literature/DM05/Yin_U001.md#dm05-u001) | Only the retained Q mechanism and exact F3/rational-improvement interface outside the dyadic-only class; source numerical optimization/global algorithms are not adopted as premises. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0522_v1.md#current-scalar-dyadic-finding) | Entire current statement, complete retained argument and every selected interface, self-reviewed; historical findings stay tied to the original inputs and exact stages. |

## Complete retained argument

<a id="argument"></a>

The entire original mathematical proof, every local formula number and all failure/coverage/source limits are retained below.
Only heading depth and already established current responsible locators change.

<a id="scalar-congruence-norm-domain"></a>
### The order, congruence and exact norm convention

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
### The direct cyclic prime-power floor and its limited optimization

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
### A stronger exact dyadic product gives log(5)/4

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

The exact auxiliary polynomial, degree ten, divisibility weight nine, circle supremum and log(5)/4 constant already appear in Borwein--Dobrowolski--Mossinghoff, *Lehmer's problem for polynomials with odd coefficients*, Annals of Mathematics 166 (2007), printed p.355, Corollary 3.4 and its proof ([retained BDM07 attribution](../audits/literature/BDM07/Yin_U001.md#bdm07-u001)).
The present proof gives the stated monogenic-order congruence form directly; it is not a new auxiliary polynomial or a claim that the source's coefficient-congruence theorem has identical hypotheses.

<a id="dyadic-product-exact-scope-optimum"></a>
### Exact optimum within all dyadic products with the automatic floors

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
Dubickas--Mossinghoff, *Auxiliary polynomials for some problems regarding Mahler's measure*, Acta Arithmetica 119.1 (2005), printed p.70, introduces Q(t)=5t^4+6t^2+5 at exactly the maximizing points of G and combines it with powers of G to improve their auxiliary bound ([retained DM05 source unit](../audits/literature/DM05/Yin_U001.md#dm05-u001)).
The exact F3 refinement and a strict rational improvement check are retained in [DM05-U001](../audits/literature/DM05/Yin_U001.md#dm05-u001).
Q is outside the dyadic cyclotomic product class used in (9).
This attribution does not adopt that paper's numerical optimization or enlarge the optimality claim proved here.

<a id="balanced-scalar-congruence-gap"></a>
### Arbitrary scalar collapse gives a gap without a bounded prime

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
### From reduced roots to the actual order congruence

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
