---
author: Yin
---

# Complete length-five cyclotomic factors, sharp repair bounds and the small Perron core

This retains the complete original2026-10-07 family and whole-core proofs, with all repeated-root, native and nonconverse boundaries explicit.

## Statement

For integers1<=k<n with gcd(n,k)=1, put a=n−k and q=t^(2n)−t^(2n−k)−t^n−t^k+1.
Its entire cyclotomic part is square-free and consists exactly of the Phi6/Phi10/Phi12 factors under the congruence conditions in the complete table retained below; deg c<=8.
For the whole noncyclotomic quotient f=q/c, every negative normalized net trace has index in{1,2,6,10,12} and magnitude<=1; the canonical cycle-repair degree is<=23 and the minimum over all cyclotomic repairs is<=8.
The explicit n=21,k=13 quotient by Phi10 Phi12 is an irreducible degree34 reciprocal unit, with every positive power degree-preserving,1<M<13/10<theta0, canonical degree23 and unique minimum repair Phi10 Phi12 of degree8.
The positive family graph is binary, primitive and unimodular of dimension2n with actual edge and Frobenius excess2.
For every monic irreducible reciprocal integer unit p with a positive uniquely maximal-modulus conjugate and1<M(p)<theta0, L(p)=5 or equivalently E(p)=2 forces every length-five completion to this coprime all-minus family; it therefore admits such a zero-free positive primitive realization of dimension<=deg p+8.
The quotient f need not be irreducible in the general family; no chosen individual factor inherits its repair bound without accounting for all other noncyclotomic factors, and no complete noncyclotomic-root classification or uniform Mahler gap is proved.

## Current assessment
[Selected decision](#decision-complete-retained-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:15 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every coprime integer1<=k<n, a=n−k, q=t^(2n)−t^(2n−k)−t^n−t^k+1: complete exact Phi6/Phi10/Phi12 congruence table, all factors simple and deg c<=8; for the whole noncyclotomic quotient f, only indices1,2,6,10,12 can be negative, each>=−1, D<=23 and R*<=8. The explicit n21,k13 degree34 irreducible reciprocal all-power-preserving1<M<13/10 control attains D23 and unique R*8. Every eligible irreducible reciprocal strict-Perron small core with L5/E2 admits the stated primitive zero-free edge-excess2 realization of dimension<=degree(p)+8. |
| argument | [Argument](#argument) | Entire <=5 minimal-unit-sum classification including repeated terms, exhaustive10-pair/pentagon reduction, exact sine derivative simplicity, cyclotomic Euler table, positive primitive graph with k1/a1 guards, full small-core sign/gcd reduction, minimum over all repair orders, complete mod3 degree17 and nonsquare degree34 proof, all-power argument and nine-step exact Graeffe/Jensen coefficient certificate; no complete expanding-root count or general factor classification is asserted. |
| dependency | [Complete rational minimal-relation proof](Yin_C_G0262_v2.md#minimal-vanishing-order) | Local all-prime relative-order lemma with arbitrary rational signs and repeated roots; no original Mann theorem is imported. |
| dependency | [Length/excess normal forms](Yin_C_G0234_v1.md#excess-two-equivalence) | Exact reciprocal five-term normal forms, exceptional Mahler value and E2/L5 equivalence in the stated small-measure unit domain. |
| support | [Original exact native certificate](../computations/programs/Yin_J_G0005/readme.md) | Exact degree34/Graeffe/residue/graph data and separate44-comparison verifier; optional root probes/counts are not theorem premises. |
### Decision complete-retained-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:39 |
| status | proved |
| reason | Actual complete statement-and-argument self-check recorded at its real current date; historical findings remain at their actual scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every coprime integer1<=k<n, a=n−k, q=t^(2n)−t^(2n−k)−t^n−t^k+1: complete exact Phi6/Phi10/Phi12 congruence table, all factors simple and deg c<=8; for the whole noncyclotomic quotient f, only indices1,2,6,10,12 can be negative, each>=−1, D<=23 and R*<=8. The explicit n21,k13 degree34 irreducible reciprocal all-power-preserving1<M<13/10 control attains D23 and unique R*8. Every eligible irreducible reciprocal strict-Perron small core with L5/E2 admits the stated primitive zero-free edge-excess2 realization of dimension<=degree(p)+8. |
| argument | [Complete argument](#argument) | Entire <=5 minimal-unit-sum classification including repeated terms, exhaustive10-pair/pentagon reduction, exact sine derivative simplicity, cyclotomic Euler table, positive primitive graph with k1/a1 guards, full small-core sign/gcd reduction, minimum over all repair orders, complete mod3 degree17 and nonsquare degree34 proof, all-power argument and nine-step exact Graeffe/Jensen coefficient certificate; no complete expanding-root count or general factor classification is asserted. |
| dependency | [Complete rational minimal-relation proof](Yin_C_G0262_v2.md#minimal-vanishing-order) | Local all-prime relative-order lemma with arbitrary rational signs and repeated roots; no original Mann theorem is imported. |
| dependency | [Length/excess normal forms](Yin_C_G0234_v1.md#excess-two-equivalence) | Exact reciprocal five-term normal forms, exceptional Mahler value and E2/L5 equivalence in the stated small-measure unit domain. |
| support | [Original exact native certificate](../computations/programs/Yin_J_G0005/readme.md) | Exact degree34/Graeffe/residue/graph data and separate44-comparison verifier; optional root probes/counts are not theorem premises. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0532_v1.md#current-complete-length-five-finding) | Complete exact current statement and proof, with every quantifier, boundary and external/native limit specified in this finding; constructor self-review, with no retrospective isolation or Task advancement. |

## Argument

<a id="complete-length-five-cyclotomic-table"></a>
### Statement and the irreducibility boundary

Let

    q_(n,k)(t)=t^(2n)-t^(2n-k)-t^n-t^k+1,
    1<=k<n,       gcd(n,k)=1,       a=n-k.

Then gcd(n,a)=1.
The entire cyclotomic part c of q is square-free and is specified by this table.
All congruences in a row are modulo the displayed order; independent signs are permitted.

| Factor | Exact condition |
| --- | --- |
| Phi_6 | n=0 and a=+1 or -1; or n=+2 or -2 and a=3. |
| Phi_10 | gcd(n,10)=1 and a=+2n or -2n. |
| Phi_12 | n=+2 or -2 and a=+3 or -3; or n=+3 or -3 and a=+4 or -4. |

No other cyclotomic factor occurs.
In particular Phi_6 and Phi_10 cannot coexist, and deg c<=8.

Put f=q/c, the whole noncyclotomic quotient.
We do not assume that f is irreducible.
Its normalized net traces are

    b_j(f)=(1/j) sum_(d|j) mu(j/d) sum_(alpha root of f) alpha^d,

with roots counted with multiplicity.
The only possible negative indices are

    j in {1,2,6,10,12},       b_j(f)>=-1.

The canonical cycle repair degree D(f) and minimum cyclotomic repair degree R_*(f) satisfy the uniform bounds

    D(f)=sum_j j max(0,-b_j(f))<=23,
    R_*(f)<=8.                                         (1)

Both bounds are attained simultaneously by an actual irreducible reciprocal unit:

    n=21, k=13,
    p(t)=(t^42-t^29-t^21-t^13+1)/(Phi_10(t)Phi_12(t)).   (2)

For this p, deg p=34, D(p)=23, and the unique minimum repair is Phi_10 Phi_12, of degree eight.
It has all-power degree preservation and the exact small-core bound

    1<M(p)<13/10<theta_0.                              (3)

If a general member q_(n,k) equals an irreducible p times a cyclotomic product, its noncyclotomic quotient is that p, so (1) applies.
The statement does not apply (1) separately to an arbitrary chosen irreducible factor when q has other noncyclotomic factors.

There is also a full-core consequence.
Let p be an irreducible reciprocal unit with 1<M(p)<theta_0 and a positive uniquely maximal-modulus conjugate.
If its cyclotomic shortness is L(p)=5, equivalently its minimum unimodular Frobenius excess is E(p)=2 by L G0033, then (1) applies to p.
It admits a positive primitive unimodular realization with actual edge excess two, no zero padding, and dimension at most deg p+8.
This consequence is proved below by reducing every length-five completion to the coprime all-minus family.
It does not equate Frobenius excess with arbitrary nonnegative edge excess when zero padding or entries greater than one are permitted.

<a id="five-root-vanishing-classification"></a>
### The only minimal sums of at most five unit roots

A minimal vanishing sum here consists of roots of unity with coefficient +1, counted with multiplicity, and has no nonempty proper vanishing subsum.
Up to multiplication by a root of unity, a minimal sum of at most five terms is exactly

    1+(-1),       1+omega+omega^2,
    1+eta+eta^2+eta^3+eta^4,

where omega and eta have orders three and five.

Here is the small-order step in full.
Normalize one term to 1.
The relative-order lemma linked above proves that the common order M of the normalized terms is square-free and divides the product of primes at most the number of terms.
Thus M divides 30.
If 5 divides M, there must be five terms.
Write each term as eta^j xi, with xi an (M/5)-th root and 0<=j<5.
Over Q(zeta_(M/5)), the minimal polynomial of eta is 1+X+...+X^4, by the coprime cyclotomic degree formula.
Grouping by j makes the five coefficient sums equal.
If a group were empty, all sums would be zero; minimality would force a single occupied group, contrary to 5 dividing the relative order.
Hence each group has exactly one term, all five xi are equal, and the sum is a rotated regular pentagon.

If 5 does not divide M, all terms belong to the sixth roots, which are +1,-1,+omega,-omega,+omega^2,-omega^2.
If both signs of any one of these three directions occur, there is an opposite pair, so minimality makes that pair the whole sum.
Otherwise the relation is A_0+A_1 omega+A_2 omega^2=0, where each integer A_i has the sign of all terms in its direction.
Linear independence of 1 and omega gives A_0=A_1=A_2.
They must be nonzero, and absolute value greater than one would contain a proper three-term vanishing sum.
Thus all absolute values are one, giving a regular triangle.
This also excludes a minimal four-term sum.

Consequently any vanishing sum of exactly five roots of unity is either a rotated regular pentagon, or an opposite pair together with a regular triangle.
This conclusion permits repeated terms and needs no separation assumption on the roots.

### Applying the classification and proving completeness

Let zeta have order m and be a zero of q.
Divide q(zeta) by zeta^n and put x=zeta^n, y=zeta^a.
Then

    x+x^(-1)-y-y^(-1)-1=0.                           (4)

These are five roots of unity with coefficient +1 after incorporating the displayed minus signs into the roots.
Bezout's identity for gcd(n,a)=1 gives

    m=lcm(ord x,ord y).                               (5)

First suppose (4) splits into an opposite pair and a triangle.
All opposite pairs fall into the following exhaustive cases; interchanging a variable and its inverse changes none of the conclusions.

| Opposite pair | Remaining condition | ord x, ord y | m |
| --- | --- | --- | --- |
| x, x^(-1) | y+y^(-1)=-1 | 4,3 | 12 |
| -y, -y^(-1) | x+x^(-1)=1 | 6,4 | 12 |
| x, -1 | x=1 and y+y^(-1)=1 | 1,6 | 6 |
| -y, -1 | y=-1 and x+x^(-1)=-1 | 3,2 | 6 |

A mixed pair x and -y or -y^(-1) would give x=y or y^(-1); their other inverse terms then cancel as well, leaving -1=0.
Thus those four mixed choices are impossible.
This accounts for all ten unordered pairs in (4).
The four remaining rows yield exactly the congruence conditions for orders six and twelve in the statement, and those conditions conversely give (4).

If (4) is minimal, its five terms form a regular pentagon.
Since one term is -1, their set is exactly -{1,eta,eta^2,eta^3,eta^4}.
The inverse pair x,x^(-1) consists of negative nontrivial fifth roots, so x has order ten; y has order five.
The two inverse pairs occupy the complementary nonzero exponent pairs modulo five, which gives y=x^2 or x^(-2).
By (5), m=10.
Equivalently gcd(n,10)=1 and a=+2n or -2n modulo ten.
Conversely a primitive tenth root x satisfies

    x^2+x^(-2)-(x+x^(-1))+1=0,

so these conditions imply (4).
This proves the complete order and congruence table for every n,k in scope, without a finite upper cutoff on n.

### All cyclotomic factors are simple

Write H(t)=t^n+t^(-n)-t^a-t^(-a)-1, so q=t^n H.
At a root of unity the derivative condition for repetition is

    n(x-x^(-1))=a(y-y^(-1)).                          (6)

For order six, one side is zero and the other is nonzero in each of the two cases above.
For order twelve, the nonzero sine differences have magnitudes 2 and sqrt(3), so (6) would require the rational number n/a to be an irrational signed multiple of sqrt(3).
For order ten, y=x^(+2) or x^(-2), and

    y-y^(-1)=+/- (x-x^(-1))(x+x^(-1)).

The real number x+x^(-1) satisfies X^2-X-1=0 and is irrational.
Equation (6) is again impossible.
Thus every cyclotomic root is simple.

The order-six condition makes n even, whereas the order-ten condition makes n odd, so those factors cannot coexist.
When order twelve occurs with n even, its congruence row automatically gives order six.
The possible complete cyclotomic products, and the bounds they imply, are therefore as follows.
The listed pair (n,k) witnesses the occurrence of each product; it need not attain the row's repair bounds.

| c | Example (n,k) | Positive b_j(c) | deg c | Bound on D(f) |
| --- | --- | --- | --- | --- |
| 1 | (2,1) | none | 0 | 0 |
| Phi_6 | (4,1) | j=1,6 | 2 | 7 |
| Phi_10 | (7,1) | j=1,10 | 4 | 11 |
| Phi_12 | (9,5) | j=2,12 | 4 | 14 |
| Phi_6 Phi_12 | (10,7) | j=1,12 | 6 | 13 |
| Phi_10 Phi_12 | (9,1) | j=1,10,12 | 8 | 23 |

Every positive entry in the third column equals one.

<a id="uniform-repair-bounds"></a>
### The positive graph and the uniform repair bounds

Use the explicit positive graph from L G0033: one cycle has k vertices u_0,...,u_(k-1), and the other has 2n-k vertices v_0,...,v_(2n-k-1).
Add the arrows

    u_(k-1)->v_0,       v_(a-1)->u_0.

Its only simple cycles have lengths k,2n-k,n; only the first two are disjoint.
The disjoint-cycle determinant expansion gives characteristic polynomial q.
It has 2n vertices, 2n+2 arrows, entries in {0,1}, determinant one and actual nonnegative edge excess two.
This remains valid at k=1 or a=1.
The cross arrows give strong connectivity.
Return cycles of lengths k and n pass through u_0, and their gcd is one, so the graph is primitive.

Thus every b_j(q) is a nonnegative count of primitive closed-walk orbits.
On the other hand

    b_j(Phi_m)=mu(m/j) if j divides m, and zero otherwise.

For Phi_6 the nonzero entries at j=1,2,3,6 are 1,-1,-1,1.
For Phi_10 those at j=1,2,5,10 are 1,-1,-1,1.
For Phi_12 those at j=2,4,6,12 are 1,-1,-1,1.
Adding these lists gives the table's positive columns and maxima.
Since

    b_j(f)=b_j(q)-b_j(c),

negativity is possible only at the displayed positive correction indices, and has magnitude at most one.
This proves the canonical support, magnitude and degree claims.
Also c itself repairs f back to q, proving R_*(f)<=deg c<=8.
None of these inferences removes an additional noncyclotomic factor without accounting for its net traces.

<a id="excess-two-perron-core"></a>
### From the family to every small reciprocal Perron unit of shortness five

Let p satisfy the full-core hypotheses in the statement, with positive uniquely dominant root lambda>1.
Take any cyclotomic completion q=p c of coefficient length five.
The reciprocal parity argument in [L G0033](Yin_C_G0234_v1.md#excess-two-equivalence) gives either the exceptional shape t^(2n)+/-3t^n+1 or

    q=t^(2n)+epsilon(t^(n+a)+t^(n-a))+delta t^n+1,
    1<=a<n,       epsilon,delta in {1,-1}.             (9)

The exceptional shape has Mahler measure (3+sqrt(5))/2, which is also M(p) because the quotient is cyclotomic.
It is excluded by M(p)<theta_0.
For t=exp(u)>1, divide (9) by t^n:

    t^(-n)q(t)=2cosh(nu)+2epsilon cosh(au)+delta.

When epsilon=+1 this is positive for either delta.
When epsilon=-1 and delta=+1 it is positive because n>a and u>0.
Since q(lambda)=0, necessarily epsilon=delta=-1.
Thus (9) has precisely the all-minus shape, with k=n-a.

Put g=gcd(n,a)=gcd(n,k).
If g>1, every exponent of q is divisible by g, so q(t)=Q(t^g).
The numbers lambda zeta for all g-th roots of unity zeta would then be distinct roots of q of modulus lambda.
All lie outside the unit circle and hence belong to p, contradicting the unique maximal-modulus conjugate.
Therefore g=1.
The complete family theorem applies, and c is exactly one of the square-free products in the table; there are no other noncyclotomic factors because q=p c by construction.

In particular every length-five completion has deg c<=8.
The positive graph above realizes it in dimension deg p+deg c<=deg p+8, with determinant one, entries in {0,1}, actual nonnegative edge excess two, and full algebraic entropy m(p).
There are no zero roots to remove.
L G0033 gives the stated equivalence between L(p)=5 and E(p)=2 in this Mahler range.
No assertion here identifies E(p) with the least edge excess of unrestricted singular presentations.
Nor is a uniform bound asserted for higher shortness levels or for the whole non-Perron reciprocal class.

<a id="sharp-degree34-control"></a>
### A sharp irreducible small-core control

For n=21,k=13,a=8, the table gives c=Phi_10 Phi_12.
The graph's shortest cycle has length thirteen, so b_j(q)=0 for 1<=j<=12.
The only negative normalized net traces of p=q/c are therefore

    b_1(p)=b_10(p)=b_12(p)=-1,

and all later ones are nonnegative.
Hence the canonical repair is

    (t-1)(t^10-1)(t^12-1),       D(p)=23.

Every repair must give positive corrections at indices ten and twelve.
Factors affecting each index have orders divisible by that index and degree at least phi(10)=phi(12)=4.
A factor affecting both would have order divisible by 60 and degree at least phi(60)=16.
Thus a repair of degree at most eight uses disjoint collections to cover the two indices, costing at least four each.
The available c has degree eight; equality forces one copy of Phi_10 and one of Phi_12, with no other factors.
This proves the unique optimum R_*(p)=8, including all possible cyclotomic orders rather than just divisors of q.

To verify irreducibility explicitly, let C_0=2, C_1=y and C_j=y C_(j-1)-C_(j-2).
Exact division gives

    C_21(y)-C_8(y)-1=(y^2-y-1)(y^2-3)Q(y),
    p(t)=t^17 Q(t+t^(-1)),

    Q(y)=y^17+y^16-16y^15-15y^14+104y^13+89y^12
         -354y^11-265y^10+680y^9+415y^8-741y^7-326y^6
         +432y^5+105y^4-114y^3-4y^2+8y-1.             (7)

Encode a polynomial over F_3 by sum_j a_j 3^j with a_j in {0,1,2}.
The reduction of Q has code 205301006.
The consecutive remainders of y^(3^j) modulo Q, for j=1,...,17, have codes

    27, 19683, 34170624, 14308929, 76051063, 101411536,
    90269161, 86759586, 17437436, 58904357, 110398560,
    74965331, 94507160, 65537644, 118123312, 124546888, 3.

Also Q(0),Q(1),Q(2) are all 2 modulo three.
Thus Q divides y^(3^17)-y and has no linear factor over F_3.
Since 17 is prime, Q is irreducible over F_3 and over Q.

There is a real conjugate y_0 in (1/2,5/8), since exact evaluation gives

    Q(1/2)=-68117/131072<0,
    Q(5/8)=988704177203917/2251799813685248>0.

The primitive graph supplies a positive uniquely dominant root lambda>1 of q; q(1)=-1 ensures the radius is greater than one.
It belongs to p, because c is cyclotomic.
Put y=lambda+lambda^(-1), a root of Q.
The degree-17 field Q(y) has a real embedding sending y to y_0, where y_0^2-4<0.
Consequently y^2-4 is not a square in Q(y).
The quadratic t^2-yt+1 remains irreducible over that field, so lambda has degree 34 and p is irreducible.

The unique maximal-modulus conjugate also proves all-power degree preservation, exactly as in L G0039: extensions of the identity embedding of Q(lambda^h) can send lambda only to conjugates of modulus lambda, hence only to lambda.
Thus Q(lambda^h)=Q(lambda) for every h>=1.
The graph and L G0033's reciprocal lower bounds also give E(p)=2 and L(p)=5.

<a id="graeffe-mahler-upper"></a>
### A coefficient-only certificate for the Mahler upper bound

The small-core assertion in (3) is not inferred from approximate roots.
For a monic polynomial P of even degree, write P(t)=E(t^2)+t O(t^2) and set

    G(P)(t)=E(t)^2-t O(t)^2.

Its roots are the squares of P's roots, counted with multiplicity, since P(z)P(-z)=G(P)(z^2).
Therefore M(G(P))=M(P)^2.
Repeating nine times for p gives a degree-34 integer polynomial P_9 whose full coefficients are retained.
Its exact squared coefficient norm is

    N=151553966467055387975393809053850548147231395191693267879212150915100548493859773995080255953869213818409114096995719.

The exact integer comparison in the retained certificate is

    N*10^1024 < 13^1024.                              (8)

For any polynomial P, the Mahler integral formula, Jensen's inequality for the logarithm, and Parseval give

    M(P)^2<=sum_j |coefficient_j(P)|^2.

Applying this to P_9 and using root squaring gives

    M(p)^1024=M(P_9)^2<=N<(13/10)^1024.

Thus M(p)<13/10.
Since (13/10)^3-13/10-1=-103/1000<0 and x^3-x-1 is increasing for x>=1, 13/10<theta_0.
The Perron root already gives M(p)>1.
This establishes (3) by exact arithmetic, independently of a numerical root count or root-modulus enclosure.

### Consequence and retained evidence

For this entire primitive positive length-five family, cyclotomic orders, multiplicities, original negative net-trace indices, canonical repair degree and optimized repair degree are uniformly bounded, independently of polynomial degree and without the Salem root restriction.
The bounds D<=23 and R_*<=8 are sharp even for an irreducible reciprocal all-power-degree-preserving unit with M<theta_0.
The normal-form argument extends the bounded-repair conclusion to the entire small reciprocal Perron core at E(p)=2, together with a positive primitive realization of dimension at most deg p+8.
This is not an entropy gap or a classification of the family's noncyclotomic factors.
The neutral order argument uses the special five-term reciprocal structure and coprime exponents; it does not yet extend to arbitrary bounded edge excess.
