---
author: Yin
---

# Cyclotomic delay blocks: boundary-log separation and the formal Euler obstruction

Date: 2026-11-05.
Prepared for Yin by the assigned agent-S exploration of the counterexample side of G0001.
This is an ordinarily self-checked exploration and failure diagnostic, without a new Claim, formal review or whole-goal conclusion.

<a id="scope-and-family-comparison"></a>
## Scope and relation to existing material

The investigated construction replaces a delayed seed by two independently chosen cyclotomic blocks and asks whether their boundary logarithms can cancel closely enough to yield positive total logarithmic Mahler measure tending to zero.
The degrees, multiplicities and numbers of nonzero coefficients of both blocks are unrestricted.
The answer for this construction is negative: distinct blocks have a uniform boundary-log separation, and the associated two-variable polynomial has total logarithmic measure at least log(theta_0).
Here theta_0 is the positive real root of t^3-t-1.
A consequence is that the raw finite Euler products of any positive-measure integral unit polynomial cannot be Cauchy in boundary L1, even though they converge formally.

The existing [L133 v1 reciprocal-degeneration argument](Yin_L_G0133_v1.md#near-one-seed-reciprocal-degeneration) and [fixed-seed limit](Yin_L_G0133_v1.md#fixed-seed-limit-and-scope) already combine Smyth's theorem with Jensen and Lawton for t^N f+f*.
The present version retains the same two-block delay mechanism, but changes the block hypothesis to two arbitrary monic cyclotomic products and extracts the boundary-log consequence.
It is a distinct scoped variant, not a replacement for v1's return accounting or a claim that its earlier [R40 review](../audits/reviews/Yin_R_G0040_v1.md#contributions-and-actual-review) covers this argument.
The original v1 remains the complete home of its unchanged results.

[C224](../claims/Yin_C_G0224_v1.md#statement) treats its alternating-kernel family and corresponding fixed and joint Lawton limits.
Its special kernels are not the unrestricted pair of cyclotomic blocks considered here.
[C240's formal Euler argument](../claims/Yin_C_G0240_v1.md#finite-nettrace-repair), originally in L34, already proves the needed integral formal factorization by coefficient recursion and logarithmic differentiation.
The new consequence below concerns boundary topology, not a new proof or interpretation of those formal exponents as nonnegative orbit counts.
The [finite Euler identity in L47](Yin_L_G0047_v1.md#girth-window-deletion) is a finite rational identity for cyclotomic deletion and supplies no boundary convergence of infinite truncations.
These comparisons justify retaining the present failure diagnostic in the L133 family rather than creating another construction family.

<a id="cyclotomic-boundary-log-gap"></a>
## Uniform separation for two cyclotomic blocks

Write T for the unit circle with normalized Haar measure dt, parametrized by exp(2 pi i t), 0<=t<1.
The L1 norm below is integral_T |h| dt.
For a nonzero polynomial H, m(H) is its total logarithmic Mahler measure, including its leading coefficient and every root with multiplicity.
For a two-variable polynomial, m_2 denotes the corresponding normalized torus integral.

A cyclotomic product means a monic product of cyclotomic polynomials with nonnegative integer multiplicities, including the empty product 1.
It has integer coefficients, no root zero, constant coefficient in {1,-1}, and total logarithmic measure zero.
The factor x is excluded from this definition.
This exclusion matters: x and 1 have identical boundary absolute values, so distinct polynomials with arbitrary zero-root factors would not satisfy the asserted separation.

Let A and B be any two such products and put

    P(x,y)=y A(x)-B(x),
    u(t)=log|A(exp(2 pi i t))|,
    v(t)=log|B(exp(2 pi i t))|.

Both u and v belong to L1(T); their finitely many logarithmic singularities are integrable, and each has integral zero.
Jensen in y gives

    m_2(P)=integral_T max(u,v) dt
          =(1/2) integral_T |u-v| dt
          =(1/2) ||log|A/B|||_L1.                         (1)

One may justify the iterated integral without assuming that P has no torus zeros.
For each x where A(x) and B(x) are not both zero, normalize by max(|A(x)|,|B(x)|).
After a rotation and possibly interchanging the two coefficients, the remaining y-factor has the absolute-value distribution of 1-r exp(2 pi i t), for some 0<=r<=1.
Its log has mean zero, positive part bounded by log 2, and hence L1 norm at most 2 log 2.
The normalizing logarithm max(u,v) is integrable, while the exceptional x form a finite null set.
Fubini therefore applies, including coincident cyclotomic roots and arbitrary multiplicities.

If A=B, P=A(y-1) and (1) is zero.
If A!=B, then

    m_2(P)>=log(theta_0),
    ||log|A/B|||_L1>=2 log(theta_0).                       (2)

Here is the exact specialization argument.
Write a=deg A, b=deg B, a_0=A(0), b_0=B(0), and take any integer N>2(a+b).
Set

    Q_N(x)=x^N A(x)-B(x).

This is monic in Z[x], of degree N+a, with constant coefficient -b_0 in {1,-1}; in particular it has no zero root.
With H*(x)=x^(deg H)H(1/x), the cyclotomic identities are A*=a_0 A and B*=b_0 B.
Indeed reciprocal roots preserve each cyclotomic multiset, and the leading coefficient of H* is H(0).
Consequently

    Q_N*=a_0 A-b_0 x^(N+a-b)B.                            (3)

If Q_N were reciprocal up to sign, its monicity and constant coefficient would force Q_N*=-b_0 Q_N.
Both shifted blocks in this equality begin above degree max(a,b), because N>2(a+b).
Comparison of the unshifted blocks therefore gives a_0 A=b_0 B.
Their leading terms imply a=b and a_0=b_0, whence A=B, contrary to the hypothesis.
Thus every Q_N in this stated range is nonreciprocal.

Factor Q_N into monic irreducibles over Z, with multiplicity.
Their constant coefficients are nonzero integers multiplying to -b_0, so every factor is an integral unit polynomial.
If all factors were reciprocal up to their respective constant signs, their product would be reciprocal up to its constant sign, contradicting (3).
At least one factor is therefore the minimal polynomial of a nonzero nonreciprocal algebraic integer.
The accepted Smyth bound makes the logarithmic measure of that factor at least log(theta_0).
Every other monic integral factor has nonnegative logarithmic measure, so

    m(Q_N)>=log(theta_0)                                  (4)

for every N>2(a+b).
This step concerns total polynomial measure; it does not put the same lower bound on every noncyclotomic factor of Q_N.

For the fixed pair A,B, specialize P at (x,y)=(t,t^N).
The nonzero integer relations on (1,N) are multiples of (N,-1), so their least sup norm is exactly N.
The accepted full Lawton theorem, including torus zeros, gives m(Q_N)->m_2(P).
Taking the limit in (4) proves (2).
No effective convergence rate or bounded-support assumption is used.
In particular, although Lawton is applied separately to each fixed pair, the final constant in (2) holds for every pair at once.
Varying A and B, their degrees, or their supports cannot produce a sequence of positive m_2(P) tending to zero in this class.
Likewise (4) rules out such a sequence of these one-variable specializations when each pair uses its stated sufficiently large delay.
It does not classify delays outside that range.

<a id="raw-euler-truncations-not-cauchy"></a>
## Raw Euler truncations cannot converge in boundary L1

Let p be a monic integer polynomial with p(0)=epsilon in {1,-1} and m(p)>0, allowing reducibility and repeated roots.
Normalize F=p/epsilon, so F belongs to 1+x Z[x], has leading coefficient in {1,-1}, has no zero root, and m(F)=m(p).
The formal factorization already proved in [C240](../claims/Yin_C_G0240_v1.md#finite-nettrace-repair) applies to every series in 1+x Z[[x]]:

    F(x)=product_(n>=1)(1-x^n)^(b_n),   b_n in Z.

Its elementary recursion does not need C240's Perron hypothesis, eventual positivity, or graph-realization input.
Define the finite rational functions

    E_N(x)=product_(1<=n<=N)(1-x^n)^(b_n).

Negative b_n are allowed, so these are not asserted to be polynomials.
Each E_N has E_N(0)=1, and its numerator and denominator are products of cyclotomic polynomials up to signs, without any x factor.
The formal identity says F-E_N has no nonzero coefficient of degree <=N in its Taylor expansion at zero.
It does not state convergence on the unit circle.

There are infinitely many nonzero b_n.
Otherwise F would be a finite quotient of products of 1-x^n.
Since F is a polynomial, all its zeros would then be roots of unity; its leading coefficient is a unit, so m(F)=0, a contradiction.

For M>N such that some b_n with N<n<=M is nonzero, let k be the least such n.
Then in the formal expansion at zero,

    E_M/E_N=1-b_k x^k+O(x^(k+1)),

so E_M/E_N is not the constant function 1.
Factor every 1-x^n into cyclotomic factors and cancel numerator and denominator factors.
The resulting expression is sigma A/B, where sigma is 1 or -1 and A,B are monic cyclotomic products, including the possibility that one is 1.
There is no zero-root factor or additional positive scalar: each factorization is integral and monic up to sign, and all original factors have constant coefficient 1.
If A=B, the quotient would be sigma; its value at zero is 1, forcing sigma=1, contrary to the displayed nonconstant coefficient.
Thus A!=B.
On T away from the finitely many zeros and poles, the difference of the real boundary logarithms equals log|A/B|.
All these functions are L1, so (2) gives

    ||log|E_M|-log|E_N|||_L1>=2 log(theta_0).               (5)

In particular distinct truncations cannot give the same boundary function almost everywhere.
This conclusion has used the exclusion of x factors; it is not inferred merely from inequality of arbitrary rational functions.
Selecting the increasing indices with b_n!=0 gives a sequence whose distinct boundary-log functions are pairwise separated by (5).
The entire raw truncation sequence is therefore not L1 Cauchy, and no sequence of distinct such truncations has an L1-convergent subsequence.

This obstruction holds for every positive value of m(p), however small it might be.
A proposed implication from small positive total measure to L1 convergence of these raw Euler truncations is therefore false throughout the proposed positive-measure domain.
It cannot be used to extend (2) to all integral units.
The original F is not a finite cyclotomic quotient when m(F)>0, and the formal approximation supplies no admissible boundary limit that would put it into that discrete set.

Interior approximation has a concrete and different behavior.
For every fixed 0<r<1,

    sup_t |log|1-r^n exp(2 pi i n t)|||
        <=-log(1-r^n) -> 0,

whereas

    ||log|1-exp(2 pi i n t)|||_L1
        =||log|1-exp(2 pi i t)|||_L1>0

is independent of n.
The equality follows from invariance of Haar measure under t->n t; positivity follows because the integrable function is not zero almost everywhere.
Thus even uniformly vanishing interior logarithms of these single factors provide no uniform recovery of their boundary L1 norms.
This is a direct topology diagnostic, not an asserted convergence theorem for the full infinite product at every r<1.

<a id="whole-polynomial-composition-control"></a>
## An elementary comparison for changing inner polynomials

A separate simple control on seed modification is useful for delimiting the failed construction search.
If f is monic in Z[x] and g is any nonconstant monic integer polynomial with g(0)=0, then

    m(f composed with g)>=m(f).                           (6)

Indeed write f(x)=product_i(x-alpha_i) with multiplicity.
Every monic complex polynomial g-alpha_i has constant term -alpha_i, so its Mahler measure is at least max(1,|alpha_i|), by the product of the absolute values of all its roots.
Additivity of logarithmic measure in the identity f(g)=product_i(g-alpha_i) proves (6).
The outer f need not be irreducible, reciprocal or a unit for this inequality.
When f is a unit, composition preserves monicity, integrality and its constant term, and (6) prevents successive such compositions from decreasing positive total measure.
The inner polynomial g may change at every step.
Selection of one irreducible factor after composition is outside this total-measure argument and would require separate factorization and measure accounting.
This observation provides no new small-measure seed and is not a proposed counterexample strategy.

<a id="source-reuse-and-assessment"></a>
## Source reuse, checks and remaining scope

Only two non-elementary inputs enter (2).
[Smy08 U002, nonreciprocal reduction](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) supplies the accepted statement M(alpha)>=theta_0 for every nonzero nonreciprocal algebraic integer, reported in Section 5.1, equation (15), of Chris Smyth's The Mahler measure of algebraic numbers: a survey, arXiv:math/0701397v2, 28 January 2008.
The survey version and its reported sharp theorem are the reused scope; neither Smyth's original sharp-bound proof nor a publisher/preprint equivalence is newly audited here.
[Den09 U002](../audits/literature/Den09/Yin_U002.md#den09-u002), Theorem 14 and Example 15 of the retained arXiv:0905.0604v1, 5 May 2009, supplies Lawton's full fixed-polynomial specialization limit for arbitrary integer vectors with the sup-norm relation length tending to infinity, including zeros.
The original Lawton proof is an accepted external input, not a new source audit; no effective or varying-template convergence rate is imported.
The C240 formal coefficient recursion is reused only for integral formal exponents and coefficient agreement, without its separate realization theorem.
No new bibliographic source or source-inspection record is required for these reuses.

The ordinary author check covered the zero-root exclusion, the unit constants and leading terms, the separated-block threshold, reciprocal normalization, passage to an actual nonreciprocal irreducible factor, the fixed-pair Lawton parameter, torus-zero integrability, signs and cancellations in Euler quotients, the distinct-truncation coefficient, and the exact total-measure scope of (6).
It is not an independent review or a complete source-proof audit.

The bounded exploration produces a useful failure diagnostic and no new counterexample mechanism.
It supplies neither an unrestricted positive Mahler gap nor a sequence of integral units with positive total measure tending to zero.
The original G0001 problem remains open in this exploration.
A future construction must introduce information not furnished by these raw two-block cyclotomic delays, formal truncations, or monic zero-constant inner compositions.
Possible factor selection, other multivariable coefficient forms, and modified approximation procedures are not ruled out, but no independent mechanism for them is asserted here.
