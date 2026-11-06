---
author: Yin
---
# Inverse additive structure, original digit laws and the missing integer carry control

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This 2026-11-05 inquiry compares inverse-additive mechanisms for the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Contributors plan_arithmetic and plan_entropy prepared the source comparison and original-law calculations for Yin, and the coordinating agent assembled their exact interfaces.
These are author-checked explorations, without independent proof review, a new uniform arithmetic bound or an adopted resolution of the Task.
The [C231 all-power norm descent](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) permits working on reciprocal all-power degree-preserving near-one endpoints at its selected SELF-review and nonreciprocal-source scope.
Every probability law below belongs to the actual chosen endpoint; no law is transported through that descent.

The newer inverse theorems improve structural extraction from an already small expansion parameter.
The inspected inputs do not supply a degree-independent small two-block parameter for the original integer law, a bound on the lengths of its approximate module strings, or control of the information lost under reduction modulo two.
This is a limitation of these proposed transfers, not a refutation of inverse-additive strategies in general.

<a id="inspected-inverse-theorems"></a>
## Inspected source statements and their actual scope

[Bloom, arXiv:2501.11580v2](https://arxiv.org/pdf/2501.11580v2), revised 7 October 2025, was inspected at PDF pp.2--3, Theorems 1--3, and pp.5--7, the relevant proof of Theorem 3.
For a finite nonempty A in F_p[t], bounds |A+A|<=K1|A| and |A+tA|<=K2|A| yield a generalized F_p[t]-progression of rank O_p(log K2), size between K2^(-O_p(1))|A| and K1^(O_p(1))|A|, whose K2^(O_p(1)) translates cover A.
The constants may depend on the fixed characteristic; the general F_q version in Theorem 2 requires the stated controls for all scalar dilates.
Rank counts polynomial strings, not their combined F_p-vector-space dimension.
Theorem 3's rank-zero base case uses the fact that multiplication by t raises the highest degree of a nonzero polynomial in a finite-dimensional subspace of F_q[t].
That argument does not apply to an arbitrary finite quotient by a polynomial.
No uniform string-length or integer relation-height bound for this application was identified in those passages.

[Gowers--Green--Manners--Tao, arXiv:2311.05762v2](https://arxiv.org/pdf/2311.05762v2), revised 12 December 2023, was inspected at PDF p.2, Theorem 1.3, and p.4, Theorem 1.8.
The former gives, for an integer set with doubling at most K, a subset of size at least K^(-C1/2)|A| and affine dimension at most C2 log K, with absolute constants; the stated footnote permits C1=220 and C2=40/log 2.
It gives neither mass under a specified nonuniform digit law nor near invariance under multiplication by alpha.
The latter is a Shannon--Ruzsa structural theorem in F_2^n, so it concerns the quotient information rather than an automatic lift to the original order.

[Gowers--Green--Manners--Tao, arXiv:2404.02244v2](https://arxiv.org/pdf/2404.02244v2), revised 20 May 2024, was inspected at PDF p.1, Theorem 1.1, and p.4, Theorem 1.3.
For a group annihilated by s, the covering bound is (2K)^(O(s^3)) and the entropic structure cost is O(s^3) times the source's entropic Ruzsa distance.
The subgroup containment in an iterated difference set also retains its s- and K-dependent number of summands.
Consequently choosing a growing prime incurs an explicit characteristic cost, and the inspected conclusions contain no low-height rational invariant-space lift.

[Hochman's 98-page author PDF](https://math.huji.ac.il/~mhochman/preprints/ssms-multi-d.pdf) was inspected at PDF p.13 for the hidden dimension dependence, p.14 for H_n=H(mu,D_n)/n, and p.19 for Theorem 2.8.
The [arXiv record](https://arxiv.org/abs/1503.09043v2) identifies a revision dated 5 June 2017; file identity between that revision and the inspected author PDF was not established.
The theorem takes bounded-support measures and a small convolution-entropy increment at specified fine scales and supplies scale-dependent real subspaces with the stated local saturation and concentration.
Its parameters retain dimension, support, accuracy and scale dependence; neither rationality nor a uniform height of those subspaces is supplied.
The self-similar-system consequences also cannot be applied directly to a companion map whose conjugates have different moduli.

These are statement and application checks, with the specified additional Bloom proof passage inspected; they are not independent audits of the complete papers.
The older [BV20 entropy interface](../audits/literature/BV20/Yin_U001.md#bv20-u001) and [C286 inverse-concentration comparison](../claims/Yin_C_G0286_v1.md#statement) keep their separate source scope.
No claimed optimality or novelty follows from the absence of a transfer in this bounded comparison.

<a id="string-rank-and-quotient-control"></a>
## String rank, actual rational dimension and the quotient boundary

Let alpha have irreducible degree d and let 1<=s<d.
In its actual field set V_s=span_Q(1,alpha,...,alpha^(s-1)).
Linear independence of the first d powers gives

    dim V_s=s,
    dim(V_s+alpha V_s)-dim V_s=1.

Thus s=d-1 permits a long single string with boundary one in the original irreducible field itself.
The space is not invariant, and irreducibility does not turn a small boundary into a small rational dimension.
This calculation applies without discarding the reciprocal or all-power degree-preserving domain; it makes no assertion that positive measures tend to zero there.

Likewise, in F_2[t] the formal coefficient set [N] of degree less than N has ordinary doubling one and operator doubling |[N]+t[N]|/|[N]|=2.
It is already one arbitrarily long string before a polynomial P or its Mahler measure is supplied.
For O=Z[alpha], evaluation instead takes values in O/2O=F_2[t]/(P mod 2).
Once N>=d the binary orbit law there is uniform on the entire quotient, including bad or repeated reductions.
The precise entropy and collision information lost at this second passage is retained below.
Neither the formal single string nor the saturated quotient supplies the needed integer lift.

<a id="original-binary-input-to-inverse-addition"></a>

## Original binary objects for an inverse-addition comparison

Contributor plan_entropy prepared this interface for Yin on 2026-11-05, Asia/Shanghai.
It compares the actual integer probability law, its support, single-digit entropy increments, two-block addition, and reduction modulo a prime.
The source comparisons above retain their own inspected statements and limitations; the calculations here do not assert a new inverse theorem.
This is an author comparison using the fixed inputs below, with no new computation or independent review.

Let alpha be an actual nontorsion algebraic unit, P its monic irreducible polynomial, d=deg P, O=Z[alpha], and m=log M(P)>0.
All entropies and logarithms below are natural and unnormalized by d or by the observation length.
Let epsilon_j be independent fair bits, and put

    X_N=sum_(j=0)^(N-1) epsilon_j alpha^j,
    mu_N=law(X_N), A_N=supp(mu_N), H_N=H(X_N),
    Delta_n=H_n-H_(n-1), H_0=0,
    q_N=Pr(X_N=X'_N), a_N=-log q_N.                  (IA1)

The prime denotes an independent copy.
[C212](../claims/Yin_C_G0212_v1.md#statement) supplies the rates and their directions, after conversion from bits: h_2=lim a_N/N<=h_1=lim H_N/N<=m.
Its finite a_N/N is an upper certificate for h_2, not the single-digit Shannon increment or a doubling parameter.
[C436](../claims/Yin_C_G0436_v1.md#statement) supplies g(m)<=h_2 with g(m) tending to zero as m tends to zero; it supplies no positive degree-independent gap by itself.

### The actual long-time budget and its mass

Use the complete [C283 increment and near-invariance theorem](../claims/Yin_C_G0283_v1.md#statement), including its fixed source and review scope.
For 0<epsilon<=1 set

    k=ceil[(2d/epsilon)log(8d/epsilon)], N=2k-1,
    delta=m+epsilon.

Then Delta_k<=delta and log|A_N|<=N delta.
The same original law mu_N has JS(mu_N,tau_(alpha^j)mu_N)<=delta for every 0<=j<N, and the final shift j=N has JS exactly Delta_(N+1)<=delta.
Here JS is the entropy gain from mixing a law equally with its indicated translate, not from adding an independent copy of the whole law.
The corresponding TV bounds are at most sqrt(2delta), with TV equal to half the l1 distance.
The stronger punctured-law statement supplies actual matched binary words of total fraction at least 1-sqrt(2delta) in each of the two labelled punctured copies; it does not assert a common unweighted set with small doubling.

For the two genuinely independent whole blocks define

    sigma_N=H(X_N+alpha X'_N)-H_N,
    sigma_N^+=H(X_N+X'_N)-H_N.

Adding the N new bits one at a time and using the JS contraction under convolution already proved in C283 gives

    0<=sigma_N<=N delta, 0<=sigma_N^+<=N delta.        (IA2)

Indeed each partial sum has law mu_N convolved with the bits already added, so the next bit's JS gain is no greater than the corresponding gain against mu_N.
The shifts for sigma_N are alpha,...,alpha^N, and those for sigma_N^+ are 1,...,alpha^(N-1), all covered above.
Thus K_ent=exp(sigma_N) is a valid entropic expansion budget, with its full factor N retained.
It is not exp(Delta_(N+1)).

The same support A_N carries probability exactly one.
Let K_set be the maximum of its two set-expansion ratios displayed next.
Its elementary set bounds, which need no conversion from weighted entropy to a uniform law, are

    |A_N+A_N|/|A_N|<=|A_N|<=exp(N delta),
    |A_N+alpha A_N|/|A_N|<=|A_N|<=exp(N delta).        (IA3)

They provide actual simultaneous set inputs, but only with this potentially large K.
For 0<m<=1 and epsilon=m, C283 gives

    N<(4d/m)log(8d/m)+1,
    log K_ent, log K_set<=2mN
                          <8d log(8d/m)+2m,          (IA4)

and the punctured matching fraction is at least 1-2sqrt(m) when this is positive.
No high-mass flatter subset with a better doubling budget is produced by these statements.

The degree cost in the sequential-bit certificate cannot be removed just by optimizing k.
[C287's posterior leverage bound](../claims/Yin_C_G0287_v1.md#statement) gives Delta_k>=d/[2(2k-1)] whenever 2k-1>=d.
For N=2k-1 and any delta>=Delta_k in that range, N delta>=d/2.
This is a lower bound on that certificate's expense, not a claim that the true sigma_N or the true set-doubling logarithm is at least d/2.
The genuinely small degree-independent quantity supplied here is the single-digit gain after a paid observation time, not a small degree-independent two-block gain.

### Exact short-window comparison

If 1<=N and N+1<=d, the power-basis map is injective on all coefficient vectors involved in A_N+alpha A_N.
Consequently

    H_N=N log2, Delta_(N+1)=log2, a_N=N log2,
    H(X_N+alpha X'_N)=(3N+1)log2/2,
    sigma_N=(N+1)log2/2,
    |A_N+alpha A_N|=4*3^(N-1),
    |A_N+alpha A_N|/|A_N|=2*(3/2)^(N-1).              (IA5)

The two endpoint coefficients are fair bits; each of the N-1 interior coefficients is the sum of two independent fair bits and has entropy 3log2/2.
All these coefficients are independent, since they use disjoint input bits.
The same argument gives sigma_N^+=N log2/2 and |A_N+A_N|/|A_N|=(3/2)^N.
Thus replacing the whole second block by one new digit changes the quantity even before any arithmetic relation occurs.
The exact collision-free interval and its dependence on degree agree with C212/C436; a small asymptotic h_2 does not change this finite interval.

### Reduction modulo two and the missing integer carry information

Write bar x for the image of x in R_2=O/2O, a vector space of dimension d over F_2 even when P modulo two is reducible or has repeated factors.
For every N>=d, the first d binary digits form a uniform element of R_2 in the actual power basis.
The remaining independent digits translate that uniform law, so bar X_N is exactly uniform.
Since alpha is a unit, alpha bar X'_N is also uniform and independent, and their sum is uniform.
Therefore the quotient support is the whole R_2, both additive set-doubling constants equal one, and

    H(bar X_N+alpha bar X'_N)-H(bar X_N)=0             (IA6)

for every unit and every N>=d, independently of m.

The omitted information has an exact expression.
Define C_N=H(X_N | bar X_N).
The finite entropy chain rule gives, for N>=d,

    H_N=d log2+C_N,
    sigma_N=H(X_N+alpha X'_N | bar X_N+alpha bar X'_N)
                                  -C_N.              (IA7)

For N>=d+1 the single-digit increment is Delta_N=C_N-C_(N-1).
Thus the small quotient doubling in (IA6) pays none of the integer conditional-entropy difference required for (IA2).

The same loss is visible for the original collision observable.
Let nu_(N,r) be the conditional law of X_N in the residue fiber r and let Col(nu)=sum_x nu(x)^2.
Every residue has probability 2^(-d), so

    q_N=2^(-d) E_(r uniform in R_2) Col(nu_(N,r)),
    a_N=d log2-log E_r Col(nu_(N,r)).                 (IA8)

The quotient collision probability is just 2^(-d).
For each fixed input its quotient entropy rates are zero, while its actual Shannon and collision rates are carried by the respective residual terms in (IA7)--(IA8).
These identities retain the full original probabilities and require no limiting theorem or independence within a residue fiber.

For comparison, the formal binary coefficient set in F_2[t] is the subspace V_N of polynomials of degree less than N.
It has |V_N+V_N|/|V_N|=1 and |V_N+tV_N|/|V_N|=2 for every N, without using P or m.
Evaluation in R_2 has image dimension min(N,d), so the low-doubling free-module object and the saturated quotient object do not supply a relation-preserving lift of the integer law.
For any prime p>=3 and N+1<=d, the coefficients 0,1,2 in (IA5) remain distinct modulo p, and the same short-window set counts hold in O/pO.
At larger windows neither injectivity nor the integer carry terms may be dropped without a separate argument.

The remaining possible inverse-addition input is therefore specific: obtain a substantially better same-object expansion bound, or prove that an inverse structure found after reduction controls the conditional integer information in (IA7)--(IA8), with the actual mass, prime, degree and time expenses retained.
The existing small single-bit gain, approximate affine invariance, or a finite-quotient K=1 supplies none of those additional conclusions.
No claim is made that every inverse-addition strategy is excluded; only these available inputs and their exact costs have been identified.
