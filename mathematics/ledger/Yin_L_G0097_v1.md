---
author: Yin
---

# A fourth-moment refinement of the binary Mahler comparison

The current complete mathematical proof is retained in [C290](../claims/Yin_C_G0290_v1.md#argument).
The original mathematical text below remains the fixed old input, with its original date and old review bindings.

Date: 2026-10-07.
Direct proof by the coordinating AI for Yin, continuing the posterior/Gram argument of [the companion note](Yin_L_G0094_v1.md#endpoint-gram-mahler-entropy).
This note uses the extra constraint that the observation is a linear image of independent fair signs.
It improves the comparison error near zero, without producing a positive Mahler gap.
No new source, computation or novelty claim is involved.

<a id="fourth-posterior-moment"></a>
## The cubic test of a posterior bias

Let xi=(xi_0,...,xi_(N-1)) be independent fair signs, let V be a real matrix of full row rank, and observe Y=V xi.
Write

    Pi=V^T(VV^T)^(-1)V,
    a_i=Pi_(j,i),  l=Pi_(j,j),
    L=sum_i a_i xi_i,  b=E[xi_j|Y].

The row projection makes L measurable with respect to Y.
Its coefficients satisfy a_j=l and sum_i a_i^2=l.
The companion posterior-covariance proof gives E b^2>=l.
When l=0 the bounds below are immediate, so first take l>0.

Independence and the even moments of fair signs give the exact identities

    E[b L^3]=E[xi_j L^3]=3l^2-2l^3,
    E L^4=3l^2-2 sum_i a_i^4<=3l^2.                    (1)

For the first identity, the only surviving terms in xi_j L^3 have all indices equal to j, or one index j and two equal indices i different from j.
Their sum is a_j^3+3a_j sum_(i!=j)a_i^2=3l^2-2l^3.
The second identity is the expansion of the fourth moment of a fair-sign sum.
It is positive because E L^2=l>0.

Holder's inequality with exponents 4 and 4/3 gives

    E b^4 >= (E[b L^3])^4/(E L^4)^3
           >= l^2(3-2l)^4/27.                           (2)

This does not assume that the nonlinear posterior b equals its linear predictor L, or that either is Gaussian.
It uses an exactly computable mixed moment, not an unjustified comparison between their fourth moments.

For natural-log mutual information define

    g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x).

The fair prior gives I(xi_j;Y)=E g(b).
The positive series g(x)=sum_(a>=1) x^(2a)/(2a(2a-1)), including its continuous endpoints, yields g(x)>=x^2/2+x^4/12.
Consequently

    I(xi_j;Y)>=F(l),
    F(l)=l/2+l^2(3-2l)^4/324.                            (3)

The function F is increasing on [0,1].
Its derivative is

    F'(l)=1/2+l(3-2l)^3(1-2l)/54.

It is at least 1/2 for l<=1/2.
For l>=1/2 the magnitude of the negative second term is at most 8/54, so it remains strictly positive.
We may therefore substitute any valid lower bound for l into (3).

<a id="cubic-mahler-comparison-error"></a>
## The algebraic orbit consequence

Let alpha be a nonzero algebraic integer of degree d, P its monic irreducible polynomial, m=log M(P), and h_1 its fair binary Shannon entropy rate.
Fair-sign and fair-bit sums have exactly the same fibers, by an injective affine change of the output.
In the full rational power coordinates of the companion note, the endpoint leverage satisfies

    l_(N-1)=1-G_(N-1)/G_N>=1-exp(-2m)   for N>d.          (4)

This is its exact finite dual-Gram/monic-Jensen inequality; no asymptotic determinant ratio is needed.
For N<=d the entropy increment is exactly log2.
Since F(l)<=F(1)=1/2+1/324<log2, these times also obey the bound.
For example log2>=2/3 follows by integrating the geometric series for 2 atanh(1/3), which suffices for the last strict inequality.
Thus (3)--(4) and the decreasing-increment limit give, for every N>=1,

    Delta_N>=F(1-exp(-2m)),
    h_1>=F(1-exp(-2m)).                                  (5)

Together with the companion bound, the explicit best lower bound available from these two arguments is

    D(m)=max(g(sqrt(1-exp(-2m))), F(1-exp(-2m))),
    Delta_N>=D(m),  h_1>=D(m).                            (6)

The maximum is needed: the fourth-moment estimate is intended to improve the small-m regime, and is not asserted stronger at every m.

Writing z=1-exp(-2m), direct Taylor expansion at zero gives

    z=2m-2m^2+(4/3)m^3+O(m^4),
    F(z)=z/2+z^2/4-(2/3)z^3+O(z^4),
    F(1-exp(-2m))=m-(20/3)m^3+O(m^4).                   (7)

Every function here is analytic in a neighborhood of zero, so the O-terms have absolute constants in a fixed sufficiently small neighborhood.
In contrast, the companion g-based bound is m-(2/3)m^2+O(m^3); (7) is strictly stronger for sufficiently small positive m.

For the algebraic-unit application, the norm-counting upper bound is h_1<=m.
Along any hypothetical sequence of positive measures m tending to zero, (5)--(7) therefore imply

    0<=m-h_1<=(20/3)m^3+O(m^4),
    h_1/m=1-O(m^2).                                     (8)

This is conditional on such a sequence existing.
It does not construct one or exclude one.
The lower bound (6) still tends to zero, and the retained strict entropy loss for some inputs is compatible with (8).

<a id="refined-binary-poisson-rates"></a>
## Return to the retained collision and moment interfaces

In this section retain the nontorsion algebraic-unit application domain of the cited Poisson and moment records.
Set A_(N,0)=1, as in L G0086's Poisson series; the same central-mode argument also covers floor(lambda N)=0.

The fair-sum comparison of [L G0089](Yin_L_G0089_v1.md#abelian-binary-entropy-comparison) and the thinning proof of [L G0090](Yin_L_G0090_v1.md#mahler-dependent-poisson-rate) now apply with the explicit full-input lower bound H_N>=N D(m).
In their notation, for every N and every fixed lambda>0,

    p_max(S_N), Col_binary(S_N)<=exp(-N D(m)/2),
    C_orig(N,lambda)<=exp(-N b(lambda)D(m)),
    b(lambda)=-log(exp(-4lambda)+(1-exp(-4lambda))/sqrt(2))/log2,

    A_(N,floor(lambda N))/N^(2floor(lambda N))
       <=4(ceil(2lambda N)+1)^2 exp(-N b(lambda)D(m)).    (9)

The comparison and thinning arguments are reused at their recorded review scopes; this note supplies the stronger Shannon input.
The dependence on m remains explicit.
These are not uniform positive exponents over the unresolved small-Mahler core, and do not prove the all-order Gaussian moment bound sought in the earlier route.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0027_v1.md#contribution-and-actual-review), with its original inspected scope and relationship.
