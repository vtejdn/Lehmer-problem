---
author: Yin
---
# Effective-support and angular-coherence comparisons for the actual projection

The current complete mathematical statement and necessary original proof are adopted in [C574v2](../claims/Yin_C_G0574_v2.md#decision-complete-current-self-adoption), with the actual [whole constructor SELF finding](../audits/reviews/Yin_R_G0757_v1.md#current-g431-complete-self-finding).
The complete original analysis, source and author boundaries, failures and mathematical continuation questions remain below.


Human author Yin.
The effective-support comparison was authored on 2026-10-18T10:25 by shear_arithmetic under root's sparse-core and dense-tail question.
The angular comparison was authored on 2026-10-18T10:44 by entropy_attainment_bridge under root's question about the actual C158 cubic budget and C92/L321/C145.
The latter author supplied the linear-k comparison and centered cubic coefficient bound.
These completed comparisons are fixed at their original author-checked scope on 2026-10-20T08:54.
These comparisons supply no unconditional Mahler gap.
The first part rejects bounded-complexity inverse proposals already dominated by C92; the second compares necessary divergence rates without supplying the missing arithmetic upper bound.

<a id="effective-support-redundancy"></a>
## Both fixed-complexity inverse proposals are dominated by C92

Work at the actual window N=2d for a monic irreducible nontorsion integer unit P(t)=sum_(i=0)^d p_i t^i of degree d and total logarithmic Mahler measure m(P)>0.
Write b=sum_i p_i^2 and g_h=sum_(i=0)^(d-h)p_i p_(i+h).
Then b>=2, |g_d|=1, and the actual normalized d-by-d relation Gram has entries g_|i-j|/b.
The exact projection/inverse-Gram interface is [L321](Yin_L_G0321_v1.md#residual-laurent-square-identity).

The first proposed sufficient class fixes the number K of nonzero positive offdiagonal Gram offsets and a uniform spectral condition.
Its full Laurent symbol H=P(t)P(t^-1) has at most2K+3 terms: the Gram does not contain the two extreme offsets+/-d, which must be included.
The polynomial t^dH has exact width2d and annihilates every original root of P.
Thus [C92(A)](../claims/Yin_C_G0092_v1.md#statement) already gives a uniform positive total Mahler gap for this class without spectral conditioning.

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
This distinction also respects [C145's moving-logarithm expense](../claims/Yin_C_G0145_v1.md#kernel-finite-logarithm-expenses).

<a id="projection-coherence-reuse"></a>
## Refined angular comparison and existing sufficient inputs

The question is whether bounded Wiener mass of the actual fixed-2d residual kernel, or a small actual weighted C158 cubic budget, supplies a new structural route beyond the existing coherence and effective-support criteria.
The author read [C158's accepted setup](../claims/Yin_C_G0158_v1.md#decision-whole-reviewed-2026-10-18), [C159's accepted refined envelope](../claims/Yin_C_G0159_v1.md#decision-whole-reviewed-2026-10-18), [C145's complete radial contact](../claims/Yin_C_G0145_v1.md#all-root-radial-kernel-contact), [L318's full bundle estimate](Yin_L_G0318_v1.md#all-residual-columns-signed-diagonal-coherence), [L321's finite Gram criterion](Yin_L_G0321_v1.md#finite-gram-gap-and-near-one-boundary), [C92's zero-value support argument](../claims/Yin_C_G0092_v1.md#angular-short-annihilator-effective-support), and [L237's actual projection construction](Yin_L_G0237_v1.md#monomial-projection-uniform-margin).
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

The original angular author's complete listed check is preserved at [its responsible SELF finding](../audits/reviews/Yin_R_G0757_v1.md#original-angular-author-self-finding), at its original mathematical and retention dates.
