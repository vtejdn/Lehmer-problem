---
author: Yin
---

# Exact resultant content collapse in an irreducible reciprocal family

Date: 2026-10-10.
Fixed retention of the complete D G0061 proof and noncontributor finding.
The coordinating AI for Yin authored all new mathematics; resultant_research independently reviewed the entire argument.
The coordinator adopts precisely the scope below.

<a id="resultant-content-collapse-fixed-scope"></a>
## Adopted scope

For every odd prime p>=3, the actual reciprocal irreducible input P=t^(2p)-3t^p+1 has degree d=2p and fixed Mahler measure(3+sqrt5)/2.
Its full doubling resultant is4^d but the common polynomial ideal is(P,4), with exact interpolation denominator4.
The actual L174 adjugate seed has content4^(d-1).
After its removal the primitive seed has coefficient sum at most116, and the whole doubling auxiliary and complementary factor have the retained degree-independent measure bounds.

This proves a concrete failure of transferring the exponential resultant or unnormalized seed floor through uncontrolled content normalization.
L174 already retained that limitation.
The present family has fixed positive total measure and no unit-circle conjugates; it neither gives a near-one counterexample nor excludes a near-one-only cost obstruction.
No cofactor is asserted cyclotomic.
G0001 remains unresolved.
Only heading depth and relative navigation are transformed below; historical pending-review text records chronology.

<a id="retained-resultant-content-collapse-proof"></a>
## Exact resultant content loss and bounded primitive doubling auxiliaries

Date: 2026-10-10.
Direct proof by the coordinating AI for Yin.
The complete argument below is new work of that coordinator in this round; the assigned agents supplied none of its derivations.
It is self-checked and pending full separate noncontributor review.
No external theorem, finite scan or new program is used.

### Reuse and question

The fixed [L174 doubling auxiliary and content boundary](Yin_L_G0174_v1.md#doubling-auxiliary-factor-universality) constructs a seed through the full resultant R and proves that its coefficient content c divides R.
It explicitly does not give an exponential lower bound for the remaining scalar R/c.
The [radical-family controls in D10](../claims/Yin_C_G0007_v1.md) already distinguish fixed positive measure from a near-one family.
This proof determines the entire scalar and ideal for a different elementary radical family, and bounds its complete primitive auxiliary and complementary measure.
It neither claims a new family in the literature nor treats fixed positive measure as a near-one input.

<a id="exact-resultant-content-collapse"></a>
### 1. Actual irreducible reciprocal inputs of unbounded degree

Let p>=3 be any odd prime, d=2p, and put

    beta=(3+sqrt(5))/2,
    P(t)=t^(2p)-3t^p+1,
    alpha=beta^(1/p)>1.

Then P is monic, reciprocal, irreducible over Q, and nontorsion, with constant term one and degree d.
Its Mahler measure is exactly beta, independently of p.

Here is a direct irreducibility proof to avoid assuming irreducibility of a composition.
Put K=Q(beta), a real quadratic field.
If X^p-beta has a proper monic factor over K of degree r, 1<=r<p, the product of its selected roots is an element c of K satisfying c^p=beta^r: its roots are alpha times pth roots of unity, and the sign of the constant coefficient is removed before taking this product.
Choose integers a,b with ar+bp=1.
Then gamma=c^a beta^b belongs to K and gamma^p=beta.
The element gamma is an algebraic integer unit, since both gamma and its inverse satisfy monic equations over the ring of algebraic integers.
Its norm to Q is one: its norm raised to the odd power p is Norm(beta)=1.
At the designated real embedding gamma is the unique real pth root beta^(1/p), strictly between1 and beta.
Its other embedding is gamma^(-1).
Consequently its integral trace gamma+gamma^(-1) lies strictly between2 and beta+beta^(-1)=3, a contradiction.
This also excludes the rational gamma case.
Thus X^p-beta is irreducible over K.
Since beta=alpha^p, K is contained in Q(alpha), so [Q(alpha):Q]=2p and P is the minimal polynomial.

Its roots are all pth roots of beta and beta^(-1).
Exactly p have modulus beta^(1/p)>1 and p have reciprocal modulus.
This proves M(P)=beta and nontorsion.
There are no unit-circle conjugates in this family.
Although individual conjugate moduli tend to one, m(P)=log beta is fixed positive; this distinction is essential.

### 2. Full resultant versus the exact ideal denominator

Retain the full powered polynomial Q=P^[2], with all d conjugate squares, as in L174.
Since p is odd, squaring permutes the pth roots of unity and beta^2+beta^(-2)=7.
Thus, with u=t^p,

    P=u^2-3u+1,
    Q=u^2-7u+1,
    Q-P=-4u,
    Res(P,Q)=4^d.                                           (1)

For the resultant, Q(alpha_i)=-4 alpha_i^p at every root of P and product_i alpha_i=1.
Since d is even their product is 4^d, including its sign.

Despite this exponential determinant, there is the small integral identity

    (7-u)P+(u-3)Q=4.                                        (2)

It follows by substituting Q=P-4u and expanding u^2-3u+1.
In particular the full polynomial ideal is exactly

    (P,Q)=(P,4) in Z[t],
    (P,Q) intersect Z = 4Z.                                 (3)

The first equality follows in both directions from Q=P-4u and (2).
For the second, reduction modulo4 gives the quotient (Z/4Z)[t]/(P mod4), a free Z/4Z module with basis1,t,...,t^(d-1), because P is monic.
A constant vanishes in this quotient exactly when divisible by4.
Thus the additive annihilator exponent of Z[t]/(P,Q) is4, whereas its cardinality is4^d.
In particular cardinality or resultant size cannot be substituted for the least integral Bezout scalar.

There is also an exact version adapted to the seed interpolation.
The least positive integer D for which an integral f can satisfy

    f = D t modulo P,
    f = D(t^2-1) modulo Q                                  (4)

is4.
Necessity follows by taking their difference in the common quotient in(3): D(t^2-t-1) must vanish.
Its degree two is less than d, so freeness modulo4 forces4 to divide D.
The construction in the next section attains D=4.
This argument does not assume a Chinese remainder theorem for two comaximal integer ideals; those ideals are not comaximal here.

### 3. Exact content of the L174 adjugate representative

For a prescribed rational scalar the solution AP+BQ to a constant, with deg A,deg B<d, is unique over Q.
Indeed a difference satisfies AP=-BQ; coprimality forces Q to divide A, so both differences vanish.
Therefore the actual degree-bounded identity with resultant R=4^d used by the L174 Sylvester-adjugate construction is

    A_R=4^(d-1)(7-u),
    B_R=4^(d-1)(u-3).

Its constructed seed is exactly

    f_R=t B_R Q+(t^2-1)A_R P = 4^(d-1) f,
    f=t(u-3)Q+(t^2-1)(7-u)P.                               (5)

The actual degree of f is k=3p+2 and its leading coefficient is-1: the second summand has that leading term, while the first has degree3p+1.
Hence f is primitive, and the positive coefficient content of f_R is exactly

    c=4^(d-1),       R/c=4.                                 (6)

This identifies the normalization of that specific representative, not just a potentially more efficient unrelated seed.
It retains only a constant scalar from an exponentially large resultant.
In the coefficient sum norm,

    ||P||_1=5,  ||Q||_1=9,
    ||7-u||_1=8,  ||u-3||_1=4,
    ||f||_1 <= 4*9+2*8*5 = 116.                            (7)

This bound is independent of p and automatically bounds coefficient height after any overlap and cancellation.
It is a safe triangle bound, not an optimized constant.
Evaluating(2) in the two quotient rings verifies

    f(alpha)=4alpha,
    f(alpha^2)=4(alpha^4-1),                                (8)

with the same identities at reciprocal conjugates.
These are precisely the L174 evaluations with its normalized scalar D=4.

### 4. Complete auxiliary and cofactor cost, with the boundary retained

Use the actual reversal f*(t)=t^k f(1/t) and define

    G_f(t)=[f*(t)^2 f(t^2)+f(t)^2 f*(t^2)]/2.

The complete proof in L174 applies to(8): G_f is integral by reduction modulo2, nonzero by its rational functional-equation argument, divisible by P in Z[t], and formally reciprocal at length4k.
Equivalently the unnormalized auxiliary there is exactly c^3 G_f, which retains the same nonvanishing and target factor.
Let ell be the initial monomial order.
Then

    G_f=t^ell P C,
    C in Z[t] is nonzero and reciprocal,
    deg G_f <= 4k = 12p+8.

The reciprocal assertion uses the actual degree after monomial removal, as in L174, and the fact that P(0)=1; division by the monic reciprocal P preserves reciprocity.
No factor or scalar is dropped from C.
The coefficient norm is bounded for the entire polynomial:

    ||G_f||_1 <= ||f||_1^3 <= 116^3,
    m(G_f) <= log ||G_f||_1 <= 3 log116,
    0 <= m(C) = m(G_f)-log beta <= 3 log116-log beta.       (9)

The measure inequality follows from the supremum norm on the unit circle and Jensen's formula; zeros there do not change the integrable logarithmic identity.
A monomial has Mahler measure one and a nonzero integer polynomial has measure at least one.
Thus the full complementary factor has a uniform upper measure bound in this unbounded-degree family.
It is not asserted cyclotomic or of vanishing measure.
Its possible leading scalar is included.

### Contribution, checks and next gate

The coordinator developed and checked the full irreducibility and fixed-measure proof, powered-polynomial multiplicities, signed resultant, both ideal equalities and the exact interpolation minimum, uniqueness of the degree-bounded Bezout pair, exact content and primitive leading coefficient, and all coefficient and full-cofactor bounds.
The general nonvanishing/reciprocity argument is explicitly reused from independently reviewed L174, not newly claimed.
No computation, source acquisition or independent verification has yet occurred for this new combined proof.

This actual family proves that the full resultant floor and the unnormalized coefficient-height statement cannot in general survive primitive normalization as exponential floors.
L174 already guarded against making that unsupported inference; the present result is an exact witness for its open normalization boundary, not a correction to its fixed proof.
Conversely it does not refute a genuinely near-one-only obstruction: these irreducible inputs have m=log beta throughout, despite unbounded degree and individual moduli tending to one.
Nor does a bounded, possibly large complementary measure yield the uniform positive gap.
A useful next test must control the least interpolation denominator or actual cofactor cost on a family whose total Mahler measure tends to one, without substituting resultant cardinality for annihilator exponent.
G0001 remains active and unresolved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0092_v1.md#separate-complete-noncontributor-review), with its original inspected scope and relationship.

## Retention and review bindings

The [complete noncontributor review](../audits/reviews/Yin_R_G0092_v1.md#exact-resultant-content-independent-review) covers the entire [retained proof](#retained-resultant-content-collapse-proof): actual irreducibility and measure, full powered polynomial and signed resultant, ideal/cardinality/annihilator distinctions, exact interpolation minimum, adjugate uniqueness and content, and all complete auxiliary/cofactor costs.
The reviewer supplied none of the mathematics.
L174's separately fixed proof is reused at its explicit scope.

The complete D G0061 proof and noncontributor review are retained here at their original scopes.
This proof-only retention adds no source theorem, program, numerical check or Task completion.
