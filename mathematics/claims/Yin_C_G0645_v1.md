---
author: Yin
---

# Actual endpoint-product envelopes and linear doubling-overlap bounds

The precise analytic question is whether the complete actual endpoint counts give a uniform all-n bound on D_n=p_(2n)/p_n^2, while preserving the original law and chronological normalization.
Contributor original_law derives the following fixed-quartic comparison after root selected the actual count/normalizer gap.
The original endpoint profile, core packing and dyadic identity are existing inputs; none is claimed as a new mechanism here.
The result supplies an explicit linear overlap bound and its paid normalization consequences, not an original mean-branch decision or uniform label congestion.
No finite screen or J is used.

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta, O=Z[beta], B=1/(beta-1) and S_real=beta B.
Let D be the actual full original zero-to-zero core, with its strict real bounds |x_+|<B and |x_-|<S_real.
Every digit has its ORIGINAL independent probability1/4,1/2,1/4 at-1,0,1.
For every integer n>=1 put

    nu_n(x)=Pr(sum_(j=0)^(n-1)eta_j beta^j=x),
    p_n=nu_n(0)>0,
    c_n(x)=4^n nu_n(x),
    w_n(x)=nu_n(x)nu_n(beta^n x)/p_n^2,
    D_n=p_(2n)/p_n^2=c_(2n)(0)/c_n(0)^2=sum_(x in D)w_n(x).

The integer counts c_n include every word with weight2^(number of zero digits).
All quantities use the complete return denominator; no earlier zero visits, endpoint representations or intermediate states are removed.
Write rho(x)=|x(zeta)| and define the explicit fixed constants

    kappa=1/|1-zeta^2|,
    h_n=n/2+kappa,
    gamma=4sqrt(B S_real),
    G_n=1+gamma sqrt(pi h_n)+gamma^2 h_n,
    C_star=G_1=1+gamma sqrt(pi(1/2+kappa))
                         +gamma^2(1/2+kappa).

Then, for EVERY n>=1 and x in O,

    nu_n(x)/p_n<=exp(-rho(x)^2/(2h_n)),
    w_n(x)<=exp(-rho(x)^2/h_n).                            (1)

In particular the complete SAME-TIME doubling count obeys

    1<=D_n<=G_n<=C_star n,
    c_(2n)(0)<=G_n c_n(0)^2<=C_star n c_n(0)^2,           (2)
    limsup_(n->infinity) D_n/n<=8 B S_real.                (3)

The first inequality in (1) is the specified isotropic specialization of the existing C432 endpoint profile; the new overlap estimate retains BOTH endpoint factors in w_n and sums over the actual core.
The sum is not replaced by a uniform lattice or graph law.

Let R=exp(lim_n[-log p_n/n]) be the TRUE original exponential return radius, and a_n=R^n p_n.
No identity R=beta is assumed.
Then

    1/(2 C_star n)<=a_n<=1       for EVERY n>=1,
    liminf_(n->infinity) n a_n>=1/(16 B S_real).           (4)

For every n>=1,J>=1 let

    H_(n,J)=sum_(j=0)^(J-1)2^(-j-1)log D_(2^j n),
    H_n=sum_(j>=0)2^(-j-1)log D_(2^j n)=-log a_n,
    epsilon_(n,J)=2^-J log(2^(J+1) C_star n).

The explicit finite-observation remainder is

    0<=H_n-H_(n,J)<=epsilon_(n,J),
    exp(-H_(n,J)-epsilon_(n,J))<=a_n<=exp(-H_(n,J)).        (5)

The largest return time appearing in H_(n,J) is2^J n.
The tail bound in (5) is analytic and does not presume that later original returns were computed.
All constants are for this fixed quartic and its actual neutral phase; no degree-uniform or near-one estimate is claimed.
C432 already supplies the polynomial order of an a_n lower bound, and C285 already supplies midpoint moment upper bounds.
The new assertions are (2)--(3) and the explicit constants/remainder resulting from this product-overlap estimate, not a new polynomial order or moment theorem.

These bounds hold in both possible critical-mean branches.
They do not assert D_n tends to infinity, D_n is eventually bounded by a constant, or the critical mean is finite or infinite.
They give no lower bound on every endpoint count along a C631 label path and no upper bound on its paid inter-label congestion.
The original critical mean, uniformly paid label comparison and unrestricted Lehmer Task remain unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision linear-overlap-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:42 |
| status | open |
| reason | Register the complete actual endpoint-product Gaussian sum and explicit all-n linear doubling-overlap bound, with its true-radius normalized-return constants and finite dyadic remainder. Existing endpoint profiles, packing, midpoint moments and polynomial return order are explicitly reused. No uniform inter-label congestion, critical-mean classification or unrestricted Task conclusion is supplied; fresh isolated whole review remains pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact all-n statement](#statement) | Every n>=1 at the fixed actual quartic, complete original endpoint and integer counts, true core and both real strips, neutral phase constant including singular early cases, same-time overlap envelope, all-n and limiting constants, true radius, finite dyadic observation scope and every remaining limit. |
| argument | [Complete product and normalization proof](#argument) | Sections 1--5 and formulas 1--10, exact reuse, both original endpoint factors, before-conditioning independence only, current complete count identity, actual-core Gaussian layer sum, exact dyadic constants/remainder and the absence of conductance lower control. |
| dependency | [Original neutral endpoint profile](Yin_C_G0432_v1.md#complete-neutral-covariance-profile) | Complete original endpoint MGF and Gaussian profile for all lengths, actual deterministic covariance and singular cases; no conditional covariance identity or coordinate independence. |
| support | [Original integer-endpoint MGF](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Existing full original endpoint Fourier/zero-digit-removal inequality underlying C432, with complete zero-endpoint normalization. |
| dependency | [Actual-core neutral packing](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Integer norm at both real embeddings and neutral pair, strict original strips, separation and N(r)<=(1+4sqrt(B S_real)r)^2; no uniform lattice law. |
| dependency | [Complete original midpoint product](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Exact original endpoint product, true core membership, full chronological return denominator and pointwise normalization. |
| dependency | [True-radius dyadic identity](Yin_C_G0555_v1.md#dyadic-critical-normalization) | Actual entropy limit, a_n=R^n p_n, exact nonnegative dyadic expansion and finite observation times; no identification R=beta or truncated unseen return data. |
| support | [Existing moment and phase bounds](Yin_C_G0285_v1.md#midpoint-proxy-explicit-linear-scale) | Already retained finite geometric phase bound and distinct midpoint projection/moment results; no new moment theorem or lower diffusion premise. |
| support | [Existing polynomial return order](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Prior complete operator estimate already implies fixed-quartic polynomial lower order for normalized return; that order is not claimed anew. |
| support | [Current selected energy and flow frontier](Yin_C_G0627_v2.md#statement) | Exact complete original conditional-tail/label comparisons remain unchanged; the new upper endpoint envelope supplies no intermediate conductance lower bound. |
| support | [Exact alternating label lift](Yin_C_G0631_v1.md#statement) | Actual same-current-length/full-negative-word lifting and necessary label-load lower bound; an upper D_n estimate is not an upper congestion estimate. |
| support | [Exact mean-branch boundary](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | All-late bounded D_n versus merely linear growth and the unresolved actual critical-mean classification. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:50 |
| status | proved |
| reason | Adopt the complete fixed-quartic original endpoint-product, linear overlap and true-radius dyadic statements after main reading of complete C645 and isolated whole R851. Both original factors, actual core and integer counts, every-n singular cases, exact constants and limsup/liminf quantifiers, finite remainder and maximum observation time are retained. The polynomial1/n order was already known; neither the critical-mean branch nor an upper weighted-label congestion bound is decided. No unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact all-n statement](#statement) | Every n>=1 at the fixed actual quartic, complete original endpoint and integer counts, true core and both real strips, neutral phase constant including singular early cases, same-time overlap envelope, all-n and limiting constants, true radius, finite dyadic observation scope and every remaining limit. |
| argument | [Complete product and normalization proof](#argument) | Sections 1--5 and formulas 1--10, exact reuse, both original endpoint factors, before-conditioning independence only, current complete count identity, actual-core Gaussian layer sum, exact dyadic constants/remainder and the absence of conductance lower control. |
| dependency | [Original neutral endpoint profile](Yin_C_G0432_v1.md#complete-neutral-covariance-profile) | Complete original endpoint MGF and Gaussian profile for all lengths, actual deterministic covariance and singular cases; no conditional covariance identity or coordinate independence. |
| support | [Original integer-endpoint MGF](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Existing full original endpoint Fourier/zero-digit-removal inequality underlying C432, with complete zero-endpoint normalization. |
| dependency | [Actual-core neutral packing](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Integer norm at both real embeddings and neutral pair, strict original strips, separation and N(r)<=(1+4sqrt(B S_real)r)^2; no uniform lattice law. |
| dependency | [Complete original midpoint product](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Exact original endpoint product, true core membership, full chronological return denominator and pointwise normalization. |
| dependency | [True-radius dyadic identity](Yin_C_G0555_v1.md#dyadic-critical-normalization) | Actual entropy limit, a_n=R^n p_n, exact nonnegative dyadic expansion and finite observation times; no identification R=beta or truncated unseen return data. |
| support | [Existing moment and phase bounds](Yin_C_G0285_v1.md#midpoint-proxy-explicit-linear-scale) | Already retained finite geometric phase bound and distinct midpoint projection/moment results; no new moment theorem or lower diffusion premise. |
| support | [Existing polynomial return order](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Prior complete operator estimate already implies fixed-quartic polynomial lower order for normalized return; that order is not claimed anew. |
| support | [Current selected energy and flow frontier](Yin_C_G0627_v2.md#statement) | Exact complete original conditional-tail/label comparisons remain unchanged; the new upper endpoint envelope supplies no intermediate conductance lower bound. |
| support | [Exact alternating label lift](Yin_C_G0631_v1.md#statement) | Actual same-current-length/full-negative-word lifting and necessary label-load lower bound; an upper D_n estimate is not an upper congestion estimate. |
| support | [Exact mean-branch boundary](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | All-late bounded D_n versus merely linear growth and the unresolved actual critical-mean classification. |
| review | [Independent entire fixed-target finding](../audits/reviews/Yin_R_G0851_v1.md#linear-overlap-whole-independent-finding) | Entire statement and Sections1--5, actual law/count normalization, singular early lengths, packing and Gaussian constants, true-radius telescope, all-late limiting constants and full finite remainder/time accounting; all comparison/source limits retained. |

<a id="argument"></a>

<a id="endpoint-product-reuse-and-scope"></a>

## 1. Exact reuse and the declared count question

The current original-law frontier is the [C627v2 complete label/word comparison](Yin_C_G0627_v2.md#statement) and [C631 exact alternating lift](Yin_C_G0631_v1.md#statement).
Those fixed results preserve complete mass and word probabilities, but do not bound actual label congestion.
The chosen analytic question is the all-n endpoint-product and normalization bound stated above, with no finite coordinate or length scan.

[C419](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) already proves the original integer-endpoint exponential-moment inequality.
[C432 Section2](Yin_C_G0432_v1.md#complete-neutral-covariance-profile) already derives its complete neutral endpoint profile, including singular covariance.
[C285 Section3](Yin_C_G0285_v1.md#midpoint-proxy-explicit-linear-scale) retains the elementary geometric-sum phase bound and its different midpoint projection consequences.
They are exact inputs here; no new conditional independence or covariance identity is introduced.
[C602 Section3](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) supplies the actual integer-norm neutral separation and the all-radius packing bound.
[C204](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) and [C555](Yin_C_G0555_v1.md#dyadic-critical-normalization) supply the complete midpoint product, true radius and exact dyadic normalization.
The existing C432 lower bound a_n>=1/E_n already has fixed-quartic order1/n; the present proof does not relabel that order as new.

The searched existing homes contain moment upper bounds, profile bounds, fixed-hub costs and the exact dyadic identity, but no direct bound (2) using both pointwise endpoint factors and C602's actual-core packing constant.
Only this complete product-count comparison and its explicit consequences are newly retained.

<a id="actual-double-endpoint-gaussian-envelope"></a>
## 2. Multiplying the two actual endpoint profiles

Put v_j=(Re(zeta^j),Im(zeta^j))^t and C_n=sum_(j<n)v_j v_j^t.
This is the deterministic MGF proxy of C432, twice the unconditioned neutral covariance, not an assumed conditional covariance.
For every u in R^2 and z=(Re(x(zeta)),Im(x(zeta)))^t, its exact original endpoint inequality is

    nu_n(x) exp(u dot z)<=p_n exp(u^t C_n u/2).           (6)

The trace of C_n is n.
Its traceless part is one half of the real symmetric matrix associated with sum_(j<n)zeta^(2j), so

    ||C_n-(n/2)I||=(1/2)|sum_(j<n)zeta^(2j)|
       <=1/|1-zeta^2|=kappa.

The finite geometric sum justifies this at every n; it uses no equidistribution or asymptotic independence.
Hence C_n<=h_n I.
Choosing u=z/h_n in (6) gives

    nu_n(x)/p_n<=exp(-|z|^2/(2h_n)).                     (7)

The scalar h_n is positive, so this proof also handles n=1 and any singular C_n without an inverse matrix.
If the endpoint is unsupported, the left side is zero and the same inequality holds.

Multiplication by beta^n acts at the chosen neutral place as multiplication by zeta^n, an ordinary orthogonal rotation.
It therefore preserves rho(x), and (7) gives the SAME bound for nu_n(beta^n x)/p_n.
Multiplying these two proved numerical inequalities gives the second part of (1).
No independence between the two normalized endpoint profiles is asserted or needed.
Their product is exactly the original midpoint summand, not a substituted joint law.

To check the complete normalization explicitly, BEFORE conditioning split an original length-2n word into two independent n-word polynomials U and V.
Its return event is U+beta^n V=0; the two halves are not asserted to remain independent after conditioning.
Sign symmetry gives

    p_(2n)=sum_(x in O)nu_n(-beta^n x)nu_n(x)
          =sum_(x in O)nu_n(beta^n x)nu_n(x).             (8)

Every positive term corresponds to an actual two-sided return through x in the original core, so the sum may be written over D.
Dividing by the full p_n^2 yields exactly w_n and D_n, with no omitted representations.
The x=0 term is1, giving D_n>=1.
The powers of4 cancel in the integer-count identity in the Statement because the two lengths are n,n and2n at the SAME original time scale.

<a id="gaussian-core-sum-linear-overlap"></a>
## 3. Summation in the actual core and the linear constant

For clarity the specific packing interface is recalled with its original real strips.
If x,y in D are distinct, v=x-y is a nonzero algebraic integer and

    1<=|Norm(v)|=|v_+ v_-| |v(zeta)|^2
                      <4 B S_real |v(zeta)|^2.

Thus distinct core points have neutral separation greater than d_0=1/(2sqrt(B S_real)).
The disjoint disks of radius d_0/2 centered at points with rho<=r lie in the disk of radius r+d_0/2.
Their Euclidean areas give the existing all-r packing bound

    N(r)=card{x in D:rho(x)<=r}<=(1+gamma r)^2.           (9)

This is a count of actual algebraic integers, using BOTH real embeddings and the neutral conjugate pair.
It is not a continuum approximation or a claim that all points of a comparison lattice occur.

For h>0 the nonnegative layer identity is

    exp(-rho^2/h)=integral_(rho)^infinity (2r/h)exp(-r^2/h)dr.

Summing over the countable actual core and using nonnegative integration and (9) gives

    sum_(x in D)exp(-rho(x)^2/h)
      <=integral_0^infinity (2r/h)exp(-r^2/h)(1+gamma r)^2dr
      =1+gamma sqrt(pi h)+gamma^2 h.                    (10)

The three terms use respectively the elementary integrals of r, r^2 and r^3 against exp(-r^2/h).
The upper integral is finite, so it also certifies convergence of the comparison sum.
The actual endpoint product in (8) has finite support in any case.
Apply (1) and (10) with h=h_n to obtain D_n<=G_n.
For n>=1 one has h_n<=n h_1, sqrt(h_n)<=sqrt(n)sqrt(h_1)<=n sqrt(h_1) and1<=n, proving G_n<=C_star n.
Finally h_n/n tends to1/2 and sqrt(h_n)/n tends to0, so G_n/n tends to gamma^2/2=8 B S_real.
This proves (2)--(3) at every stated original length.

<a id="linear-overlap-critical-normalization"></a>
## 4. Exact dyadic consequence and finite remainder

Use C555's true-radius identity H_n=-log a_n, where the entire dyadic sum is finite and each summand is nonnegative.
The elementary sums

    sum_(j>=0)2^(-j-1)=1,
    sum_(j>=0)j 2^(-j-1)=1

and D_(2^j n)<=C_star 2^j n imply

    H_n<=sum_(j>=0)2^(-j-1)log(C_star 2^j n)
       =log(2 C_star n).

Exponentiating gives the all-n lower bound in (4); a_n<=1 is the existing original entropy normalization.
There is no replacement of the true R by beta or by a finite-length estimate.

For the sharper asymptotic constant let epsilon>0.
By (3) there is a finite onset N_epsilon such that D_m<=(8 B S_real+epsilon)m for every m>=N_epsilon.
For every n>=N_epsilon, every dyadic multiple 2^j n also satisfies this bound.
The same calculation gives

    n a_n>=1/[2(8 B S_real+epsilon)].

Taking the liminf in n and then decreasing epsilon to zero proves the second part of (4).
This is an ALL-LATE bound for each fixed epsilon, justified by the explicit deterministic envelope G_m, not a subsequence argument.

For finite n,J the remaining tail is bounded directly by

    sum_(j>=J)2^(-j-1)log(C_star 2^j n)
       =2^-J[log(C_star n)+(J+1)log2]
       =epsilon_(n,J).

Together with nonnegative summands this proves (5).
Its finite data H_(n,J) involve D_n through D_(2^(J-1)n), whose largest complete return entry is p_(2^J n).
No later entries are sampled or silently treated as known.
The error tends to zero at each fixed n and input with its displayed constants, and no varying-input uniformity is asserted.

<a id="linear-count-bound-and-unpaid-congestion"></a>
## 5. What this count bound changes and what it does not

The new actual count control is uniform over ALL n and uses the complete original normalizers.
It excludes superlinear growth of the actual doubling overlap at this fixed quartic and supplies the explicit normalization bracket (5).
It is compatible with C204's finite-mean branch D_n tending to the finite mean and with its infinite-mean branch supplying a common unbounded subsequence.
An upper bound proportional to n decides neither alternative.
The all-n return lower bound has the same polynomial order already available from C432; the direct overlap comparison supplies its new explicit constant and dyadic remainder here.

C627 and C631 keep their complete original selected masses, actual current-length support and exact lifting statements.
The current upper envelope does not provide a positive lower bound on nu_n(x) at each intermediate label used by a sign path, nor a lower bound on every needed original edge conductance.
An upper estimate for D_n cannot be substituted into C631's NECESSARY lower congestion bound to produce an upper congestion bound.
In particular no uniform label coefficient, original sign-flow load, or critical-mean conclusion follows from (1)--(5).
No lower diffusive moment or local central limit estimate has been assumed, and the neutral coordinates have not been made independent.
The next quantitative load problem still requires actual endpoint-count lower control or another paid weighted-label construction.
