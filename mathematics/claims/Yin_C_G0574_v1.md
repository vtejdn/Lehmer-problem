---
author: Yin
---

# Complete effective-support and refined angular-coherence comparison for the actual projection

The complete original mathematical argument is retained from [L430](../ledger/Yin_L_G0430_v1.md#effective-support-redundancy).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The original two author-level comparisons are retained at their actual 2026-10-18T10:25 and10:44 mathematical dates and2026-10-20T08:54 retention. Existing C92/C145/C158/C159 and their reviews are reused only at their exact scopes; none is prospective whole review of this new responsible statement.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be an actual monic irreducible nontorsion integer-unit minimal polynomial of degree d>=2 and TOTAL m=m(P)>0.
Put b=sum_i p_i^2>=2,g_h=sum_(i=0)^(d-h)p_i p_(i+h),H=P(t)P(t^-1),N=2d,T=2d-1.
The normalized d-by-d relation Gram has entries g_|i-j|/b and does not contain the extreme offsets+/-d, for which abs(g_d)=1.
If K counts the nonzero positive offdiagonal Gram offsets, the FULL symbol H has at most2K+3 terms and t^dH is a nonzero actual annihilator of width2d; C92 already gives a restricted gap at fixed K without spectral conditioning.
More generally choose K offsets S among1,...,d-1 and put
    tau_tail=(2/b)sum_(1<=h<d,h notin S)|g_h|,
    sigma=||H||_W/b=1+(2/b)sum_(h in S)|g_h|+tau_tail+2/b.
Then sigma<=2+2K+tau_tail and the COMPLETE effective support of t^dH satisfies rho_H=||t^dH||_1^2/||t^dH||_2^2<=sigma^2.
C92's exact annihilator bound therefore already supplies the fixed-K/bounded-tail gap class.
For c0=log2/4,h0=c0 exp(-20), define
    b_old(h)=max{h,sqrt(h/c0)log sqrt(c0/h)},
    epsilon_old(h)=min{1,15sqrt(b_old(h))+4h},0<h<=h0.
Whenever0<2m<=h0,
    sigma^2>=rho_H>=[1+epsilon_old(2m)]/[epsilon_old(2m)+4m].
Thus every hypothetical original positive-m sequence tending to0 has sigma->infinity and2K+tau_tail->infinity in every such decomposition; no such sequence is constructed.

Let A_rel be the N-by-d full coefficient matrix of P,tP,...,t^(d-1)P and R=I-A_rel(A_rel^T A_rel)^-1 A_rel^T, the actual rank-d residual projection.
Put
    a_n=sum_(j=0)^(N-1-n)R_(j,j+n),
    k(t)=1/2+(1/N)sum_(n=1)^T a_n(t^n+t^-n),
    kappa=(2/d)sum_(n=1)^T|a_n|,u=Tm/d.
For all original roots alpha_i=r_i z_i,|z_i|=1, let nu=d^-1 sum_i delta_(z_i),mu probability Haar and D=integral(1-k)dnu.
Then0<=D<=2u and the nonconstant coefficient mass of k is kappa/2.
For0<v<=exp(-40) define the EXACT accepted refined envelope
    ell=log(1/v),A(ell)=ell-log2400-3log ell,
    B(v)=2400v ell^3 A(ell),E(v)=min{1,15sqrt(B(v))+4v}.
For0<u<=exp(-40),
    kappa E(u)>=1-2D>=1-4u,
    kappa>=(1-4u)/E(u).
For0<2m<=exp(-40), also kappa>=(1-8m)/E(2m).
Consequently every hypothetical m->0 sequence must have kappa=Omega(m^-1/2[log(1/m)]^-2), with degree-independent constants.

For the ACTUAL cubic G3=log2-(1-k)/2-(1-k)^2/8-(1-k)^3/24, set x=k-1/2.
Its centered expansion and full coefficient upper bound are
    G3=C+(21/32)x-(3/16)x^2+x^3/24,
    W_*(G3)<=p(kappa)=(kappa^3+9kappa^2+63kappa)/192.
For gamma=log(4/3) and0<3u<=exp(-40),
    gamma-4m log2-1/16
       <=sum_(0<|n|<=3T)|G3hat(n)|E(|n|m/d)
       <=E(3u)p(kappa).
When0<6m<=exp(-40), E(3u) may be replaced by E(6m).
This compressed cubic estimate alone forces only kappa=Omega(m^-1/6[log(1/m)]^-2/3), weaker than the direct linear bound.

For v_poly=1-k, its actual nonzero rational annihilator has span<=2T, ||v_poly||_W=(1+kappa)/2 and||v_poly||_2^2>=1/4.
Specializing C92's same Gram proof to E gives, whenever0<2u<=exp(-40),
    rho(v_poly)>=[1+E(2u)]/[E(2u)+4u],
    kappa>=sqrt([1+E(2u)]/[E(2u)+4u])-1.
This gives only order m^-1/4[log(1/m)]^-1 in the width-2T estimate.
Define the actual finite normalized Gram column sum
    theta_d=(1/b)max_(0<=j<d)sum_(0<=i<d,i!=j)|g_|i-j||.
For theta_d<1, the accepted bound kappa<=(3theta_d+2/b)/(1-theta_d) gives
    (1-4u)(1-theta_d)<=(3theta_d+2/b)E(u)<=4E(u),
    1-theta_d<=4E(u)/(1-4u).
All envelope arguments are positive and inside their stated domains; no E(0), nonzero-resultant bound at a vanishing auxiliary, uniform arithmetic coefficient upper bound or unrestricted Mahler gap is supplied.
The old linear comparison, precise source/normalization scope and every missing-covering-class limitation remain in the complete argument.

## Current assessment

[Selected decision](#decision-complete-fixed-registration-open)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:35 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Both full original comparisons, all exact support/endpoints/tail costs and every refined linear/cubic/effective-support/Gram-margin inequality, original total m and all positive envelope domains, necessary-rate and missing-upper-bound limitations. |
| argument | [Entire complete argument](#argument) | Both full original comparisons, all exact support/endpoints/tail costs and every refined linear/cubic/effective-support/Gram-margin inequality, original total m and all positive envelope domains, necessary-rate and missing-upper-bound limitations. |
| dependency | [Exact fixed input](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support) | Entire exact zero-value rational-annihilator Gram/radial proof and actual epsilon/h0 scope; no nonzero-resultant substitution. |
| dependency | [Exact fixed input](Yin_C_G0158_v1.md#statement) | Actual rank-d projection in2d coordinates, Laurent root values, range/mean and exact cubic. |
| dependency | [Exact fixed input](Yin_C_G0159_v1.md#statement) | Exact increasing refined E(v), every powered-degree/multiplicity/frequency and weighted-cubic domain; source depth unchanged. |
| dependency | [Exact fixed input](Yin_C_G0145_v1.md#all-root-radial-kernel-contact) | Original full-root radial deficit D<=2u and actual coefficient/window normalization. |
| dependency | [Exact fixed input](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact actual inverse-Gram Laurent factorization and finite dominance kappa upper bound, with all endpoint costs. |
| support | [Exact fixed input](../ledger/Yin_L_G0318_v1.md#all-residual-columns-signed-diagonal-coherence) | Old already adopted linear coherence comparison only; no new original source proof or automatic arithmetic upper bound. |

## Complete original argument

<a id="argument"></a>

### Original account: Effective-support and angular-coherence comparisons for the actual projection

Human author Yin.
The effective-support comparison was authored on 2026-10-18T10:25 by shear_arithmetic under root's sparse-core and dense-tail question.
The angular comparison was authored on 2026-10-18T10:44 by entropy_attainment_bridge under root's question about the actual C158 cubic budget and C92/L321/C145.
The latter author supplied the linear-k comparison and centered cubic coefficient bound.
These completed comparisons are fixed at their original author-checked scope on 2026-10-20T08:54.
The first part rejects bounded-complexity inverse proposals already dominated by C92; the second compares necessary divergence rates without supplying the missing arithmetic upper bound.

<a id="effective-support-redundancy"></a>
## Both fixed-complexity inverse proposals are dominated by C92

Work at the actual window N=2d for a monic irreducible nontorsion integer unit P(t)=sum_(i=0)^d p_i t^i of degree d and total logarithmic Mahler measure m(P)>0.
Write b=sum_i p_i^2 and g_h=sum_(i=0)^(d-h)p_i p_(i+h).
Then b>=2, |g_d|=1, and the actual normalized d-by-d relation Gram has entries g_|i-j|/b.
The exact projection/inverse-Gram interface is [L321](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity).

The first proposed sufficient class fixes the number K of nonzero positive offdiagonal Gram offsets and a uniform spectral condition.
Its full Laurent symbol H=P(t)P(t^-1) has at most2K+3 terms: the Gram does not contain the two extreme offsets+/-d, which must be included.
The polynomial t^dH has exact width2d and annihilates every original root of P.
Thus [C92(A)](Yin_C_G0092_v1.md#statement) already gives a uniform positive total Mahler gap for this class without spectral conditioning.

The proposed dense-tail replacement chooses K offsets S and pays the FULL remaining normalized autocorrelation tail

    tau=(2/b)sum_(1<=h<d, h not in S)|g_h|.

Its normalized full symbol size obeys

    sigma=||H||_W/b
         =1+(2/b)sum_(h in S)|g_h|+tau+2/b
         <=2+2K+tau,

because |g_h|<=b by Cauchy--Schwarz for zero-padded coefficient shifts.
The missing endpoint cost2/b has not been omitted.
For the same actual annihilator F=t^dH,

    ||F||_1=b sigma,
    ||F||_2^2=b^2+2sum_(h=1)^d g_h^2>=b^2,
    rho_F=||F||_1^2/||F||_2^2<=sigma^2<=(2+2K+tau)^2.

C92 controls this EFFECTIVE support, not just the literal number of terms.
Therefore fixed K and bounded tau already give its gap class, with no spectral bound and no inverse-tail smallness condition.
Dense omitted entries alone do not create a new near-one coverage theorem.

C92 gives the sharper necessary escape condition directly.
Whenever0<2m(P)<=h0,

    sigma^2 >=rho_F
             >=[1+epsilon(2m(P))]/[epsilon(2m(P))+4m(P)].

Thus along any hypothetical positive-total-m sequence tending to zero, sigma must diverge and every such decomposition must have2K+tau tending to infinity.
No sequence is asserted to exist.
A useful improvement must permit that growth and exploit cancellation in the PRODUCT H B_d, rather than estimating the two factors by separate absolute coefficient sums.
This distinction also respects [C145's moving-logarithm expense](Yin_C_G0145_v1.md#kernel-finite-logarithm-expenses).

<a id="projection-coherence-reuse"></a>
## Refined angular comparison and existing sufficient inputs

The question is whether bounded Wiener mass of the actual fixed-2d residual kernel, or a small actual weighted C158 cubic budget, supplies a new structural route beyond the existing coherence and effective-support criteria.
The author read [C158's accepted setup](Yin_C_G0158_v1.md#decision-whole-reviewed-2026-10-18), [C159's accepted refined envelope](Yin_C_G0159_v1.md#decision-whole-reviewed-2026-10-18), [C145's complete radial contact](Yin_C_G0145_v1.md#all-root-radial-kernel-contact), [L318's full bundle estimate](../ledger/Yin_L_G0318_v1.md#all-residual-columns-signed-diagonal-coherence), [L321's finite Gram criterion](../ledger/Yin_L_G0321_v1.md#finite-gram-gap-and-near-one-boundary), [C92's zero-value support argument](Yin_C_G0092_v1.md#angular-short-annihilator-effective-support), and [L237's actual projection construction](Yin_C_G0570_v1.md#monomial-projection-uniform-margin).
These actual fixed inputs suffice; no new external theorem, primary-source search or claim of novelty is required for the elementary specialization below.
Bounded actual coherence already implies a restricted gap in L318/L321.
The new useful comparison is the stronger necessary rate supplied by C159 and the loss from compressing the cubic through a polynomial in coherence.

## Exact setting

Let P be a monic irreducible nontorsion integer unit polynomial of degree d>=2 and total logarithmic Mahler measure m>0.
All d original conjugates are alpha_i=r_i z_i with |z_i|=1.
Use C158's ACTUAL rank-d residual projection R in N=2d coordinates, its normalized Laurent kernel k, and the signed diagonal sums

    T=2d-1,
    a_n=sum_(j=0)^(N-1-n) R_(j,j+n),
    k(t)=1/2+(1/N)sum_(n=1)^T a_n(t^n+t^(-n)),
    kappa=(2/d)sum_(n=1)^T |a_n|.

Thus the total nonconstant coefficient mass of k is kappa/2.
On the circle 0<=k<=1 and integral k=1/2.
Let nu=d^(-1)sum_i delta_(z_i), let mu be normalized Haar measure, and put

    u=T m/d,
    D=integral (1-k) dnu.

C145 proves 0<=D<=2u, retaining every original root and the unit identity sum_i |log r_i|=2m.
Its sharper quadratic and off-circle-count bounds remain available but are not needed here.
Write E(v)=e_ref(v) for the exact increasing envelope of C159, defined only for 0<v<=exp(-40).
No value E(0) is used.
In particular E(v)=O(sqrt(v)[log(1/v)]^2) as v tends to zero.

<a id="linear-projection-coherence-expense"></a>
## Direct linear specialization is stronger than the cubic compression

Assume 0<u<=exp(-40).
Applying C159's finite Fourier estimate directly to k gives

    1/2-D
      =integral k dnu-integral k dmu
      <=sum_(0<|n|<=T)|khat(n)| E(|n|m/d)
      <=(kappa/2) E(u).

The equality is the exact definition of D and the mean of k.
The first inequality follows from the absolute discrepancy bound even if its left side were negative.
Here D<=2u and u<=exp(-40), so the resulting numerator is positive.
Consequently

    kappa E(u)>=1-2D>=1-4u,
    kappa>=(1-4u)/E(u).                              (1)

This is a direct use of accepted C145 and C159, with no resultant, logarithm or polynomial-value transfer.
The rational scalar denominator of R is irrelevant to this finite Fourier specialization because k itself is the actual already normalized test.
It is not discarded from a new arithmetic construction.

If additionally 0<2m<=exp(-40), monotonicity and u<2m give the convenient degree-free necessary inequality

    kappa>=(1-8m)/E(2m).                              (2)

Thus on any HYPOTHETICAL sequence of original inputs with m tending to zero,

    kappa=Omega(m^(-1/2)[log(1/m)]^(-2)).              (3)

This does not assert existence of that sequence.
The total measure, not m/d or the house, tends to zero in this statement.
The constants in the asymptotic follow from the fixed C159 envelope and are independent of d.

L318 already proves, for the same actual kernel and u, the necessary inequality

    kappa[epsilon_old(u)+2u]>=2exp(-2u)-1,            (4)

with its accepted L229 envelope epsilon_old.
In particular bounded kappa already forces a positive total-measure gap on any class with that bound.
Equation (1) improves the small-parameter rate through the newly accepted angular input; it does not discover a different bounded-coherence criterion or supply any automatic upper bound.
The linear contact argument also avoids paying the extra 2u inside the denominator of (4).
No ordering between the two displayed numerical bounds on their entire common domain is asserted.

<a id="centered-cubic-compression"></a>
## What the actual cubic coefficient bound gives

Let G_3 be C158's exact cubic, with v=1-k:

    G_3=log2-v/2-v^2/8-v^3/24.

Put x=k-1/2, so x has constant coefficient zero and ||x||_W=kappa/2.
Expanding the same polynomial around k=1/2 gives

    G_3=C+(21/32)x-(3/16)x^2+x^3/24,

where C is a constant.
For finite Laurent polynomials coefficient convolution gives ||fg||_W<=||f||_W||g||_W.
Deleting the constant coefficient cannot increase that norm.
Therefore the actual nonconstant mass obeys

    W_*(G_3)<=p(kappa),
    p(s)=21s/64+3s^2/64+s^3/192
        =(s^3+9s^2+63s)/192.                         (5)

Let L=3T, a valid frequency bound.
Under 0<Lm/d<=exp(-40), C159's accepted necessary weighted expense and monotonicity imply

    gamma-4m log2-1/16
      <=sum_(0<|n|<=L)|G3hat(n)|E(|n|m/d)
      <=E(3u)W_*(G_3)
      <=E(3u)p(kappa),   gamma=log(4/3).             (6)

For 0<6m<=exp(-40), E(3u)<=E(6m), so the rightmost factor can be replaced by E(6m).
Since gamma>1/4, the left side tends to gamma-1/16>0 as m tends to zero.
The polynomial p is increasing for nonnegative arguments.
For s>=1 one has p(s)<=73s^3/192.
Hence (6) alone forces, along a hypothetical near-one sequence,

    kappa=Omega(m^(-1/6)[log(1/m)]^(-2/3)).           (7)

For the last deduction kappa eventually exceeds 1; otherwise the right side of (6) would tend to zero.
This cubic compression is weaker than (3), and even weaker in power of m than the old linear L318 divergence using epsilon_old.
Thus feeding a crude cubic coefficient bound into C159 does not provide a new more effective coherence obstruction.
The actual frequency-weighted sum in (6) may retain information that (5) loses; no small upper bound for that actual sum has been obtained.

## Comparison with effective support and the finite Gram margin

The nonzero rational Laurent polynomial v=1-k vanishes at all original roots, by C158's exact k(alpha_i)=1.
Its constant coefficient is 1/2 and its exponent span is at most 2T.
It is nonconstant: otherwise its root value zero and circle mean 1/2 would be inconsistent.
C92 therefore applies at its actual positive span, with all its rational-zero-value hypotheses satisfied.
Writing rho(v)=||v||_W^2/||v||_2^2, the fixed constant coefficient gives

    ||v||_W=(1+kappa)/2,
    ||v||_2^2>=1/4,
    rho(v)<=(1+kappa)^2.

C92's original lower bound for rho consequently yields only a square-root lower bound for 1+kappa.
If its unchanged finite Gram calculation is specialized to the accepted C159 moment bound at width at most 2T, its strongest immediate conclusion here is

    rho(v)>=(1+E(2u))/(E(2u)+4u),
    kappa>=sqrt((1+E(2u))/(E(2u)+4u))-1,             (8)

whenever 0<2u<=exp(-40).
To check this substitution, the lower phase energy is S2^2[1-(rho-1)E(2u)], and the upper squared radial error is at most 2rho S2^2(2u); combining them gives (8).
Using the actual smaller span can improve its numerical value.
The width-2T version of (8) forces only order m^(-1/4)[log(1/m)]^(-1), weaker than (3).
This does not revise C92's fixed accepted statement or import its nonzero-resultant branch at a zero value.

Similarly, L237's selected-column positive margin and growing effective support are already sufficient to explain why sparse-support assumptions remain missing.
Neither (5) nor the coefficient norm identity turns those necessary support losses into an upper bound.

For an original relation Gram matrix satisfying L321's theta_d<1, retain its B=sum_i p_i^2 and exact upper estimate

    kappa<=(3theta_d+2/B)/(1-theta_d).

Combining with (1) gives

    (1-4u)(1-theta_d)<=(3theta_d+2/B)E(u)<=4E(u),
    1-theta_d<=4E(u)/(1-4u).                         (9)

Here B>=2 and theta_d<1 justify the last constant, and the denominator is positive on the declared domain.
This improves the old necessary vanishing rate of any strict dominance margin by substituting C159.
The structural sufficient condition theta_d<=1-delta, for fixed delta>0, remains exactly L321's already accepted restricted class.
No evidence establishes that any such delta covers all near-one integer inputs.

<a id="projection-comparison-boundary"></a>
## Remaining interface and author check

The missing direction is an arithmetic UPPER estimate for the actual signed Fourier coefficients, the actual weighted cubic sum, or the original relation Gram quantities on a class that covers the unrestricted near-one unit problem.
A bound kappa<=K on such a covering class would already work through L318; obtaining (1) does not construct it.
A proposed asymptotic upper estimate kappa=o(m^(-1/2)[log(1/m)]^(-2)) would contradict (3), but no such estimate is supplied.
Changing scalar approximation degree while retaining only a polynomial coefficient bound in kappa loses rather than gains the direct linear contact information.
The arithmetic recurrence and original-input constraints, rather than another positive Haar example or generic bounded circle range, remain the unclosed interface.
