---
author: Yin
---

# Small total first-return mass does not control the weighted excursion tail

Date: 2026-10-09.
Bounded G0001 derivation by the assigned execution_and_deliverables AI for Yin, with the coordinating AI's contribution to the rank-based total-tail bound disclosed below.
Complete independent review was finished on 2026-10-09; the coordinating AI accepted this source for fixed-ledger adoption on the same date.
No numerical calculation, path enumeration, new source or novelty claim is involved.
The useful conclusions are an all-degree bound on the actual unweighted first-return mass and a nonvanishing complete weighted tail on actual irreducible algebraic units.
The renewal identity alone is not claimed as new progress or a gap proof.

Fixed inputs were read before this derivation: the complete-path warning in [L G0008](Yin_L_G0008_v1.md#polynomial-fiber-counterexample), the [basis-block collision bound](Yin_L_G0094_v1.md#independent-basis-block-collision), the [norm-grid support bound](Yin_L_G0091_v1.md#norm-grid-support-bound), the [explicit finite collision rate](Yin_L_G0097_v1.md#refined-binary-poisson-rates), and the actual irreducible Salem family in [L G0131](Yin_L_G0131_v1.md#linear-exponent-cyclic-coverage).
The fixed-order and linear-moment boundaries of L G0085/L G0086 and the original binary-law scope of L G0089 remain unchanged.

<a id="actual-first-return-paths"></a>
## 1. Every actual path and its weight

Let alpha be an algebraic unit of degree d, with minimal polynomial P.
Unless explicitly stated otherwise alpha is nontorsion, and m=log M(P)>0.
Let eta_0,eta_1,... be independent with

    Pr(eta=0)=1/2,        Pr(eta=1)=Pr(eta=-1)=1/4,
    X_0=0,               X_(j+1)=alpha X_j+eta_j.

All X_j lie in Z[alpha].
Define the genuine endpoint and first-return probabilities

    p_n=Pr(X_n=0),             p_0=1,
    f_n=Pr(X_n=0 and X_j!=0 for every 1<=j<n),   n>=1.       (1)

The difference of two independent fair-bit sums has the eta law.
Reversing the n independent indices therefore gives

    p_n=Col(sum_(j=0)^(n-1) xi_j alpha^j),                 (2)

where xi_j are independent fair bits.
There is no modification of the input law.
For a prescribed eta word its probability is 2^(-n-s), where s is its number of nonzero symbols.
Its endpoint polynomial is

    Q_n(t)=sum_(j=0)^(n-1) eta_j t^(n-1-j).

Endpoint return means P divides Q_n.
First return additionally means Q_l(alpha)!=0 for every 1<=l<n, with Q_l formed from that word's first l symbols by the same convention.
These conditions and all word weights are retained, with no state truncation or omitted excursions.

The single zero digit gives f_1=1/2.
If n>1 is a first return, then eta_0!=0, so Q_n is nonzero of degree n-1.
Irreducibility gives

    f_1=1/2,             f_n=0 for 2<=n<=d.              (3)

Partitioning a returning path by its first positive return time, and using the independent remaining digits from state zero, gives

    p_n=sum_(j=1)^n f_j p_(n-j),             n>=1.       (4)

For real z>=0 put U(z)=sum_(n>=0) p_n z^n and F(z)=sum_(n>=1) f_n z^n, allowing infinity.
Each finite path is uniquely a concatenation of its first-return excursions.
Nonnegative-term summation consequently gives the extended-value identity

    U(z)=sum_(a>=0) F(z)^a.                              (5)

This follows first coefficientwise and then by Tonelli.
In particular F(z)<1 implies U(z)=1/(1-F(z))<infinity.
No converse inference from a killed finite-state chain or a finite prefix of (4) is used.

<a id="uniform-small-unweighted-return-tail"></a>
## 2. The complete nontrivial return mass is already small in large degree

For every algebraic unit of degree d>=3, including cyclotomic units, one has

    sum_(n>=2) f_n
       <= T_d:=d 2^(-d) [1+8/(3(d-2))].                 (6)

This result is about the actual entire finite-return probability mass, not a truncation or a hypothesized mixing estimate.
In particular, F(1)=1/2+O(d 2^(-d)) as d tends to infinity, with the explicit one-sided error (6).
A bound exceeding 1 at a small d remains valid but is not advertised as informative there.

Here is the complete rank estimate.
On the dual torus of Z[alpha], the exact Fourier formula for (2) is

    p_n=integral product_(j<n) cos^2(pi <y,alpha^j>) dy.

For n>=d write q=floor(n/d)>=1.
The first qd factors split into q consecutive blocks of d columns, each an integral basis: multiplication by a power of an algebraic unit is an automorphism of Z[alpha].
Drop the remaining factors, which are at most one, and apply Holder with q equal exponents to these q nonnegative block products.
Changing torus coordinates by the corresponding integral basis gives the fixed L G0094 bound, with its proof displayed here:

    p_n<=b_q^d,         b_q=binom(2q,q)/4^q,
    integral product_(j in a block) cos^(2q)(pi <y,alpha^j>) dy
                     = b_q^d.                          (7)

The Holder product consists of q such integrals, each raised to 1/q.
The scalar integral equals b_q by expanding cos^(2q) and retaining its constant Fourier coefficient.

The sharper elementary bound needed for summation is

    b_q<=(3q+1)^(-1/2),              q>=1.              (8)

It is equality at q=1.
The ratio b_(q+1)/b_q=(2q+1)/(2q+2) proves induction because

    (2q+1)^2(3q+4)<=(2q+2)^2(3q+1),

whose right side minus left side is q.
Since the comparison function in (8) is decreasing, for d>2

    sum_(q>=1) b_q^d
      <=2^(-d)+integral_1^infinity (3x+1)^(-d/2) dx
       =2^(-d)[1+8/(3(d-2))].                          (9)

Finally f_n<=p_n and (3) allow a sum only over n>d.
There are at most d integers n with a given q=floor(n/d).
Applying (7)--(9) proves (6).
The repeated first returns counted in p_n only enlarge this upper bound; no assertion that p_n=f_n was made.

The unit and rank hypotheses suffice for this estimate, with no expanding-root separation or positive-Mahler premise.
It therefore cannot, by itself, force any positive entropy rate.
The next section quantifies the precise weighted tail which a rate test still needs.

<a id="complete-weighted-return-tail-lower-bound"></a>
## 3. The full weighted tail remains large above the actual measure

For an actual nontorsion algebraic unit with M=M(P)<2, take any real z with M<z<2.
Then

    sum_(n>d) f_n z^n >= 1-z/2 >0,                     (10)

with infinity allowed on the left.
Thus a small value of (6) gives no automatic control of this exponentially weighted tail.

Indeed the retained L G0091 support bound and Cauchy--Schwarz give

    p_n >=1/|supp(sum_(j<n) xi_j alpha^j)|
         >=(4n)^(-d) M^(-(n-1)).                       (11)

Consequently p_n z^n tends to infinity for z>M, so U(z)=infinity.
By (5), F(z)>=1.
Removing its term f_1 z=z/2 and using (3) proves (10).
This is also consistent with the original-law rate inequality h_2<=m: a weighted renewal sum below one at z would have proved h_2>=log z.
Formula (11) gives the needed implication directly, without treating that rate inequality as a new external input.

Both (6) and (10) hold for every actual input satisfying their stated conditions.
In particular they apply conditionally to any sufficiently near-one reciprocal unit if one exists; they do not construct such inputs.
No bound on its actual weighted tail was discarded.
Rather, the inequalities show that late rare excursions can carry the entire obstruction to the proposed rate despite exponentially small total finite-return probability above f_1.

<a id="salem-first-return-tail-control"></a>
## 4. An actual Salem control with arbitrarily late weighted mass

To give actual varying-degree inputs inside the reciprocal, all-positive-power-degree-preserving class, use exactly the fixed L G0131 family, also retained in [L G0147](Yin_L_G0147_v1.md#plastic-family-uniform-flux):

    P_N=t^N(t^3-t-1)+(1-t^2-t^3),
    N=9 modulo 120, N>=129,        d=N+3.                (12)

Each P_N itself is the actual irreducible Salem minimal polynomial, with positive exterior root alpha_N, and every positive power of alpha_N has degree d.
There is no cyclotomic padding or selected-factor transfer.
If theta>1 is the root of t^3-t-1, the fixed result gives theta<M(P_N)=alpha_N<4/3 and M(P_N) tending to theta.
The elementary inequality theta>5/4 is also retained there: t^3-t-1 is increasing on [1,infinity) and has value -19/64 at 5/4.

The original collision rate is bounded away from zero.
L G0097 gives p_n<=exp(-n D(m)/2), with D(m)>=g(sqrt(1-exp(-2m))) and g(x)>=x^2/2.
Thus

    h_2(alpha_N)>9/100,
    h_2(alpha_N)<=m(P_N)<log(4/3).                       (13)

The lower bound follows from D(m)/2>=(1-M(P_N)^(-2))/4>9/100.
The upper bound follows directly from (11) on taking normalized logarithms.
Rate existence uses the fixed original-law subadditivity interface of L G0089; all limits here keep the input P_N fixed.
No varying-degree/time limit is interchanged.

Now fix the exact test exponent c=log(4/3).
Equations (3), (6) and (10) give simultaneously for every actual input in (12)

    f_1=1/2,               f_n=0 for 2<=n<=d,
    sum_(n>=2) f_n <=d 2^(-d)[1+8/(3(d-2))] ->0,
    sum_(n>d) f_n (4/3)^n >=1/3.                        (14)

Every fixed finite prefix of the first-return law is eventually identical to f_1=1/2 with all later coefficients zero, and the full unweighted difference from that defective law tends to zero.
Yet the complete weighted tail in (14) stays bounded below.
Consequently no modulus tending to zero with that unweighted difference can bound this weighted tail on all actual algebraic units.
All excursions are included, and the actual entropy in (13) is positive; this is not the cyclotomic killed-chain control from L G0008.

## Exact decision boundary and contribution record

This closes a particular shortcut in the proposed first-return route: arbitrarily long initial freedom, tiny total nontrivial return mass, and positive original-law entropy do not control the needed weighted tail at a prescribed c.
The obstruction already occurs in an actual irreducible varying-degree family, and (6)/(10) give a direct general conditional comparison for any actual sufficiently small-measure input.

The family (12) is reciprocal and all-positive-power-degree-preserving, but its measures tend to theta>1.
It is not a near-one Mahler family.
In particular it does not refute a smaller universal positive c or an extra theorem restricted to sufficiently near-one reciprocal inputs.
Such a theorem must rule out the rare late weighted excursions by new arithmetic information, not infer it from (6) or a finite renewal calculation.
Neither a uniform gap nor a new near-one family is proved.

The execution_and_deliverables AI proposed the original-law excursion test, derived the complete weighted-tail obstruction, and assembled the actual-family application and this proof.
The coordinator contributed the reuse of L G0094's basis-block bound for the generic total-tail estimate, the sharper b_q bound and its summation constant, and the choice of L G0131's actual Salem family for the final control; the assigned AI checked and wrote the full finite and infinite-sum argument in Section 2.
Both are contributors to the assembled result.
The old Salem-family, basis-block and norm-grid proofs remain fixed-interface reuse at the scopes explicitly stated above.
No mathematical computation or fixed-material edit was performed.

The growth_arithmetic_status AI completed an independent review on 2026-10-09 of the entire proof, Sections 1--4 and equations (1)--(14).
The review found no substantive defect or missing hypothesis.
It checked the actual paths and word weights, the first-return zero segment, the complete Tonelli renewal identity, the basis-block Fourier/Holder bound, the sharper b_q estimate and the 8/[3(d-2)] integral constant, the actual support bound and its implication U(z)=infinity for z>M, the complete weighted-tail lower bound, the Salem progression and its fixed-input guards, the constants 4/3 and 9/100 and the full-tail bound 1/3, and all limit and near-one scope boundaries.

The reviewer supplied no new mathematical derivation, edits or computations to this result.
This was not a blind review: the reviewer had the assigned question, contributor context and fixed dependencies.
The reviewer's earlier contribution to L G0131 is disclosed as reuse of that fixed interface; the review does not claim a new independent audit of the old family proof.
The coordinator and the assigned author are contributors, so their checks are not the independent review of this assembled result.
The later source changes are limited to this review record, completion wording and links normalized for the fixed-ledger destination; the mathematical body is unchanged.

The coordinating AI accepted this complete independently reviewed argument for fixed-ledger allocation on 2026-10-09.
No mathematical body or old fixed version was changed by adoption.
The existing retained computations are reused only at their stated scopes; no new mathematical computation ran.
