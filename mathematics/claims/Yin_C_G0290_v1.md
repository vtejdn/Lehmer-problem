---
author: Yin
---

# Cubic posterior test and every-time binary/Mahler entropy comparison

This retains the complete original2026-10-07 [L97 proof](../ledger/Yin_L_G0097_v1.md), authored by the coordinator for Yin.
The actual old whole checking and precision requests remain in [R27](../audits/reviews/Yin_R_G0027_v1.md#contribution-and-actual-review).
No source, computation or Task is newly executed.

## Statement

Let xi consist of independent fair signs, V be a full-row-rank real matrix and Y=V xi.
For a row of Pi=V^T(VV^T)^(-1)V put a_i=Pi_(j,i),l=Pi_jj,L=sum_i a_i xi_i and b=E[xi_j given Y].
Define g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x) and

    F(l)=l/2+l²(3-2l)^4/324,    0<=l<=1.

Then F is increasing and I(xi_j;Y)>=F(l).
The proof uses the exact mixed moment E[bL³]=3l²-2l³ and Holder, without identifying posterior b with linear predictor L.

For every nonzero algebraic integer alpha of degree d, put m=log M(P),where P is its monic irreducible polynomial.
Let Delta_N be the increments of Shannon entropy of its fair binary sum and h1 their limit.
For every integer N>=1,

    Delta_N>=D(m), h1>=D(m),
    D(m)=max(g(sqrt(1-exp(-2m))),F(1-exp(-2m))).

The first d increments equal log2; later times use the exact finite dual-Gram/Jensen leverage bound.
No asymptotic determinant ratio is needed.
Near zero,

    F(1-exp(-2m))=m-(20/3)m³+O(m^4).

The local absolute remainder is uniform in a sufficiently small fixed neighborhood.
For algebraic units h1<=m, so along any hypothetical sequence m>0 tending to0,
0<=m-h1<=(20/3)m³+O(m^4) and h1/m=1-O(m²).
This does not construct or exclude that sequence; the maximum in D is essential outside the small-m branch.

For the nontorsion unit application, every N>=1 and every fixed lambda>0 satisfy

    p_max(S_N),Col_binary(S_N)<=exp(-N D(m)/2),
    C_orig(N,lambda)<=exp(-N b(lambda)D(m)),
    b(lambda)=-log(exp(-4lambda)+(1-exp(-4lambda))/sqrt2)/log2,
    A_(N,floor(lambda N))/N^(2floor(lambda N))
       <=4(ceil(2lambda N)+1)² exp(-N b(lambda)D(m)).

Use A_(N,0)=1, including the zero central-mode case.
These rates depend on m and do not prove the all-order Gaussian moment target or a common positive gap.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:56 |
| status | open |
| reason | Complete original mixed-moment, finite orbit and refined rate arguments retained; current whole check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire fair-sign cubic posterior theorem, every-N nonzero-algebraic-integer D(m) comparison, local absolute cubic error and unit-domain binary/Poisson/linear-moment consequences with zero-order and uniformity limits. |
| argument | [Complete argument](#argument) | Complete original1–9: exact mixed/fourth moments, Holder exponents, global monotonicity and early endpoint, finite Gram leverage, Taylor constants and conditional near-zero conclusion, all inherited collision/Poisson/central-mode normalizations. |
| dependency | [Full posterior and finite Gram proof](Yin_C_G0287_v1.md#argument) | Exact covariance lower bound, every-time B(m), finite nonzero-algebraic-integer endpoint leverage and decreasing entropy increments, without a source-proof or asymptotic ratio premise. |
| dependency | [Fair-group comparison](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact half-Shannon max-atom/collision bound for independent fair sums. |
| dependency | [Full thinning and Poisson theorem](Yin_C_G0282_v1.md#mahler-dependent-poisson-rate) | Exact deterministic-increment thinning and Poisson Fourier product, used with the explicit Shannon input D(m), preserving its original nontorsion-unit moment domain. |
| dependency | [Balanced central-mode comparison](Yin_C_G0277_v1.md#balanced-poisson-moment-bridge) | Complete factor4(ceil(2lambda N)+1)^2 moment/Poisson inequality, with the original series convention A_(N,0)=1 and the zero central-mode case. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:03 |
| status | proved |
| reason | Adopt the complete original cubic posterior theorem, every-N nonzero-algebraic-integer D(m) bound, absolute cubic error and exact unit-domain collision/Poisson/moment deductions after actual whole self-review; original unit/zero-order precision requests preserve the checked proof and create no substantive repair debt. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fair-sign cubic posterior theorem, every-N nonzero-algebraic-integer D(m) comparison, local absolute cubic error and unit-domain binary/Poisson/linear-moment consequences with zero-order and uniformity limits. |
| argument | [Argument](#argument) | Complete original1–9: exact mixed/fourth moments, Holder exponents, global monotonicity and early endpoint, finite Gram leverage, Taylor constants and conditional near-zero conclusion, all inherited collision/Poisson/central-mode normalizations. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Exact covariance lower bound, every-time B(m), finite nonzero-algebraic-integer endpoint leverage and decreasing entropy increments, without a source-proof or asymptotic ratio premise. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact half-Shannon max-atom/collision bound for independent fair sums. |
| dependency | [Dependency](Yin_C_G0282_v1.md#mahler-dependent-poisson-rate) | Exact deterministic-increment thinning and Poisson Fourier product, used with the explicit Shannon input D(m), preserving its original nontorsion-unit moment domain. |
| dependency | [Dependency](Yin_C_G0277_v1.md#balanced-poisson-moment-bridge) | Complete factor4(ceil(2lambda N)+1)^2 moment/Poisson inequality, with the original series convention A_(N,0)=1 and the zero central-mode case. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-cubic-comparison-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fair-sign cubic posterior theorem, every-N nonzero-algebraic-integer D(m) comparison, local absolute cubic error and unit-domain binary/Poisson/linear-moment consequences with zero-order and uniformity limits. |
| argument | [Argument](#argument) | Complete original1–9: exact mixed/fourth moments, Holder exponents, global monotonicity and early endpoint, finite Gram leverage, Taylor constants and conditional near-zero conclusion, all inherited collision/Poisson/central-mode normalizations. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Exact covariance lower bound, every-time B(m), finite nonzero-algebraic-integer endpoint leverage and decreasing entropy increments, without a source-proof or asymptotic ratio premise. |
| dependency | [Dependency](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) | Exact half-Shannon max-atom/collision bound for independent fair sums. |
| dependency | [Dependency](Yin_C_G0282_v1.md#mahler-dependent-poisson-rate) | Exact deterministic-increment thinning and Poisson Fourier product, used with the explicit Shannon input D(m), preserving its original nontorsion-unit moment domain. |
| dependency | [Dependency](Yin_C_G0277_v1.md#balanced-poisson-moment-bridge) | Complete factor4(ceil(2lambda N)+1)^2 moment/Poisson inequality, with the original series convention A_(N,0)=1 and the zero central-mode case. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-cubic-comparison-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0547_v1.md#f-g291) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="fourth-posterior-moment"></a>
### The cubic test of a posterior bias

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
### The algebraic orbit consequence

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
### Return to the retained collision and moment interfaces

In this section retain the nontorsion algebraic-unit application domain of the cited Poisson and moment records.
Set A_(N,0)=1, as in L G0086's Poisson series; the same central-mode argument also covers floor(lambda N)=0.

The fair-sum comparison of [C G0281](Yin_C_G0280_v1.md#abelian-binary-entropy-comparison) and the thinning proof of [C G0283](Yin_C_G0282_v1.md#mahler-dependent-poisson-rate) now apply with the explicit full-input lower bound H_N>=N D(m).
In their notation, for every N and every fixed lambda>0,

    p_max(S_N), Col_binary(S_N)<=exp(-N D(m)/2),
    C_orig(N,lambda)<=exp(-N b(lambda)D(m)),
    b(lambda)=-log(exp(-4lambda)+(1-exp(-4lambda))/sqrt(2))/log2,

    A_(N,floor(lambda N))/N^(2floor(lambda N))
       <=4(ceil(2lambda N)+1)^2 exp(-N b(lambda)D(m)).    (9)

The comparison and thinning arguments are reused at their recorded review scopes; this note supplies the stronger Shannon input.
The dependence on m remains explicit.
These are not uniform positive exponents over the unresolved small-Mahler core, and do not prove the all-order Gaussian moment bound sought in the earlier route.
