---
author: Yin
---

# Every finite convolution has strict Fourier deficit and positive entropy production

This retains the complete original2026-10-07 [L109 proof](../ledger/Yin_L_G0109_v1.md).
The assigned ms25_source agent derived the Fourier extension; the coordinator contributed the whole-word concavity and quantitative production bounds9a–9b.
The complete original partial/contributor/whole checks remain at their sufficient [R31 home](../audits/reviews/Yin_R_G0031_v1.md#contribution-and-review-scope).
No source,computation or Task is newly executed.

## Statement

Let alpha be a hyperbolic algebraic unit of degree d,with m=log M(P)>0.
For each fixed integer k>=1 use the per-time sum of k independent fair signs and its algebraic-sum rate h_k.
Let c_opt(P) be the supremum of the exact integral-multiplier trace amplitudes and L_eff the P-only frequency spacing.
Then0<c_opt(P)<1 and

    m-h_k>=g(c_opt(P)^k)/L_eff>0 for every k>=1.

The complete proof retains the actual k-dependent separation radius
a_k=a k^(-(d-s)/s),noise volume gamma_k and Gaussian boundary C_(P,k).
For each fixed multiplier and smoothing parameter epsilon it proves the full finite inequality6 before taking N to infinity,then epsilon to0,then the multiplier supremum.
No uniform k-boundary or optimizing multiplier is assumed.
For hyperbolic full-order coding,the same deficit belongs to its changed-law kth convolution entropy.

The separate repeated-column theorem gives0<=m-h_k<=C(m)/k²,where
C(m)=(5/12)(exp(2m)-1)²(1-exp(-4m)).
Set h_(k=0)=0.
Whole-word data processing proves h_(k+1)-h_k<=h_k-h_(k-1).
Consequently h_(k+1)>h_k for all k>=1.
More explicitly,put

    d_k=g(c_opt(P)^k)/L_eff,
    n_k=max(k+1,ceil sqrt(2C(m)/d_k)).
    h_(k+1)-h_k>=d_k/[2(n_k-k)]>0.

All constants remain input dependent.

Combining deficits yields
sup_(k>=1)k² g(c_opt(P)^k)<=L_eff C(m).
For0<c<=1/2,k²g(c^k) is nonincreasing,so k=1 is the strongest member of this particular envelope.
For every fixed0<c<1,the expression tends to0 as k tends to infinity;finite k optimization can still matter when c>1/2.
No universal maximizing integer,uniform amplitude lower bound,original-binary entropy equality with m,unit-circle extension or Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-isolated-complete-convolution-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:37 |
| status | open |
| reason | Full original k-dependent separation/Fourier/KL proof, whole-word concavity and finite-step production bounds retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Complete fixed-k hyperbolic-unit Fourier deficit, exact finite constants/ordered limits and optimized supremum, strict convolution entropy production/concavity and all finite-k envelope limitations. |
| argument | [Complete argument](#argument) | Full original1–10 including9a–9b: k-dependent norm separation/disjoint smoothing, actual k-th amplitude and Gaussian signs, multiplier supremum, whole-word information/noise concavity, quantitative increment and positive-series optimization. |
| dependency | [Complete Gaussian/smoothing theorem](Yin_C_G0297_v1.md#argument) | Exact signed-frequency cross-term and KL proof; the actual k-dependent noise separation and boundaries are explicitly rebuilt here. |
| dependency | [Full multiplier and spacing theorem](Yin_C_G0298_v1.md#argument) | Exact every-integral-multiplier positive amplitude, P-only limiting denominator and nonuniform finite offsets/supremum, preserving all fixed-multiplier quantifiers. |
| dependency | [Strengthened multiplier caps](Yin_C_G0304_v1.md#two-unit-defect-energy-floor) | Exact integral-defect energy floor and upper cap ensuring c_opt<1,not an amplitude lower bound. |
| dependency | [Quantitative repeated-sign convergence](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact actual rate convergence/monotonicity and C(m)/k² upper deficit; the scalar proof is an accepted separately checked premise here. |
| dependency | [Changed-digit toral equality](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) | Only the fixed finite integer iid coding/convolution interpretation; never identifies changed-law rates with original h1. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:44 |
| status | proved |
| reason | Adopt the complete original fixed-k Fourier/KL strictness,whole-word concavity and quantitative positive convolution-step theorem after actual whole self-review,with all k-dependent finite boundaries,supremum and exact envelope limits preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete fixed-k hyperbolic-unit Fourier deficit, exact finite constants/ordered limits and optimized supremum, strict convolution entropy production/concavity and all finite-k envelope limitations. |
| argument | [Argument](#argument) | Full original1–10 including9a–9b: k-dependent norm separation/disjoint smoothing, actual k-th amplitude and Gaussian signs, multiplier supremum, whole-word information/noise concavity, quantitative increment and positive-series optimization. |
| dependency | [Dependency](Yin_C_G0297_v1.md#argument) | Exact signed-frequency cross-term and KL proof; the actual k-dependent noise separation and boundaries are explicitly rebuilt here. |
| dependency | [Dependency](Yin_C_G0298_v1.md#argument) | Exact every-integral-multiplier positive amplitude, P-only limiting denominator and nonuniform finite offsets/supremum, preserving all fixed-multiplier quantifiers. |
| dependency | [Dependency](Yin_C_G0304_v1.md#two-unit-defect-energy-floor) | Exact integral-defect energy floor and upper cap ensuring c_opt<1,not an amplitude lower bound. |
| dependency | [Dependency](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact actual rate convergence/monotonicity and C(m)/k² upper deficit; the scalar proof is an accepted separately checked premise here. |
| dependency | [Dependency](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) | Only the fixed finite integer iid coding/convolution interpretation; never identifies changed-law rates with original h1. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0546_v1.md#current-convolution-deficit-finding) | Exact current full statement,complete retained original proof and all selected interfaces,self-reviewed; historical findings retain their actual old inputs and precise partial/contributor/whole relationships. |


### Decision isolated-complete-convolution-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:13 |
| status | proved |
| reason | Adopt the actual fresh context-isolated whole-target finding, formed before R31/R546 and followed by their full scope-specific comparison, preserving every fixed-k boundary, ordered limit, source depth and nonuniformity limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete fixed-k hyperbolic-unit Fourier deficit, exact finite constants/ordered limits and optimized supremum, strict convolution entropy production/concavity and all finite-k envelope limitations. |
| argument | [Argument](#argument) | Full original1–10 including9a–9b: k-dependent norm separation/disjoint smoothing, actual k-th amplitude and Gaussian signs, multiplier supremum, whole-word information/noise concavity, quantitative increment and positive-series optimization. |
| dependency | [Dependency](Yin_C_G0297_v1.md#argument) | Exact signed-frequency cross-term and KL proof; the actual k-dependent noise separation and boundaries are explicitly rebuilt here. |
| dependency | [Dependency](Yin_C_G0298_v1.md#argument) | Exact every-integral-multiplier positive amplitude, P-only limiting denominator and nonuniform finite offsets/supremum, preserving all fixed-multiplier quantifiers. |
| dependency | [Dependency](Yin_C_G0304_v1.md#two-unit-defect-energy-floor) | Exact integral-defect energy floor and upper cap ensuring c_opt<1,not an amplitude lower bound. |
| dependency | [Dependency](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact actual rate convergence/monotonicity and C(m)/k² upper deficit; the scalar proof is an accepted separately checked premise here. |
| dependency | [Dependency](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs) | Only the fixed finite integer iid coding/convolution interpretation; never identifies changed-law rates with original h1. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0546_v1.md#current-convolution-deficit-finding) | Exact current full statement,complete retained original proof and all selected interfaces,self-reviewed; historical findings retain their actual old inputs and precise partial/contributor/whole relationships. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0558_v1.md#g307-whole-independent-finding) | Entire statement and original(1)–(10), including9a–9b, necessary complete Fourier/Gaussian, repeated-sign and changed-law coding chains; independently reviewed, with no source/PDF/native run. |


## Complete retained argument

<a id="argument"></a>
Let alpha be an algebraic unit with monic irreducible polynomial P, with no unit-circle conjugate, and put m=log M(P)>0.
Let d=deg P, and s the real dimension of its stable embedding space.
Use the normal real stable matrix A, stable embedding iota, and product bodies K_N of [C G0298](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy).
Let k>=1 be a fixed integer, and let eta_j be independent, each distributed as a sum of k independent fair signs.
Set

    S_(N,k)=sum_(j=0)^(N-1) eta_j alpha^j,
    H_(N,k)=H(S_(N,k)),    h_k=lim_N H_(N,k)/N.           (1)

The limit exists by independent-block subadditivity.
For k=1 this is the original fair-binary rate, with the usual injective sign/bit affine conversion.
All logarithms are natural.

<a id="convolution-sign-separation"></a>
### Separation and smoothing with the full k dependence

Write

    rho=max_(stable beta)|beta|<1,
    T=max_(stable beta)(1-|beta|)^(-1),
    a=[product_(expanding beta)(|beta|-1)]^(1/s),
    a_k=a k^(-(d-s)/s),
    V_0=vol(K_0),    gamma_k=a_k^s V_0.                 (2)

Complex pairs in the expanding product are counted twice.
We have K_N=A^N K_0 and vol(K_N)=V_0 exp(-Nm).

The difference of two digit sums in (1) is 2x, where x=sum_(j<N) delta_j alpha^j has integral coefficients |delta_j|<=k.
If x!=0, then alpha^(-N)x is a nonzero algebraic integer.
Its expanding conjugates satisfy

    |beta^(-N)x(beta)|<k/(|beta|-1).

If iota(x) belonged to a_k K_N, the stable part of the absolute norm would be at most a_k^s.
The full norm would then be strictly less than

    a_k^s k^(d-s)/product_(expanding beta)(|beta|-1)=1,

which is impossible.
Thus distinct stable digit-sum atoms differ by a vector outside 2a_k K_N.
Their translates of a_k K_N are disjoint.

Let Y_(N,k)=iota(S_(N,k)), and add independent noise U_(N,k) uniform on a_k K_N.
The actual stable embedding preserves the algebraic fibers, so the resulting density f_(N,k) has exact differential entropy

    h_diff(f_(N,k))=H_(N,k)+log gamma_k-Nm.              (3)

Also Y_(N,k) lies in kT K_0.
Comparing with the standard Gaussian density phi on R^s, as in L G0102, gives

    D(f_(N,k)||phi)<=Nm-H_(N,k)+C_(P,k),
    C_(P,k)=|log gamma_k|+(s/2)log(2pi)
                              +(s/2)(kT+a_k)^2.        (4)

These are finite constants for each fixed P,k; no uniform bound in k is being asserted.
Packing the same disjoint translates into (kT+a_k)K_0 also gives |supp Y_(N,k)|<=((kT+a_k)/a_k)^s exp(Nm).
Consequently h_k<=m, independently of the lower convergence estimate used later.

<a id="convolution-fourier-deficit"></a>
### The same frequency spacing and the k-th power amplitude

For theta in O_K minus {0}, use the exact trace multiplier and frequencies from [C G0299](Yin_C_G0298_v1.md#algebraic-trace-multiplier).
The k independent signs in each digit give

    |hat law(Y_(N,k))(zeta_(theta,t))|
        =product_(j=0)^(N-1)|cos(2pi u_(theta,j-t))|^k
        >=c_P(theta)^k.                                (5)

Thus there is no new amplitude independent of k.
Let L_eff be the input-dependent, theta-independent spacing in that record.
For fixed theta choose its finite offset t_0 so that the sampled frequencies zeta_(theta,t_0+j L_eff), j>=1, have norm at least 4^j and successive norm ratio at least four.
The Gaussian signed-frequency expansion is unchanged.

Fix 0<epsilon<1, and choose B_(epsilon,theta,k)>=0 with

    2pi a_k sqrt(s)||zeta_(theta,0)||
                     rho^B <=sqrt(2epsilon).

The noise Fourier factor is then at least 1-epsilon for every sampled frequency with t<=N-B.
The Gaussian/KL proof of L G0102 consequently yields the full finite bound

    Nm-H_(N,k)
      >=floor[(N-B_(epsilon,theta,k)-t_0)_+/L_eff]
                   g((1-epsilon)c_P(theta)^k)
                    -C_(P,k)-log2,                     (6)

where

    g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x).

The signs of the real Fourier coefficients can be chosen separately, exactly as in that proof.
This also covers even k, when the unsmoothed coefficients are nonnegative.
There is no independence assumption between frequencies or scales.

First fix k,theta,epsilon and let N tend to infinity.
Then let epsilon tend to zero.
We obtain

    m-h_k>=g(c_P(theta)^k)/L_eff.                        (7)

The constants and the order of limits in (6) are essential: k is fixed during this limiting argument.
Write

    c_opt(P)=sup_(theta in O_K minus {0}) c_P(theta).

The uniform multiplier caps of L G0103, strengthened in [C G0305](Yin_C_G0304_v1.md#two-unit-defect-energy-floor), give 0<c_opt(P)<1.
No maximum or optimizing multiplier is asserted to exist.
Since the left side of (7) and its spacing are independent of theta, continuity and monotonicity permit taking this supremum after the fixed-multiplier bounds:

    boxed: m-h_k>=g(c_opt(P)^k)/L_eff>0
                                      for every k>=1.  (8)

This is actual strictness for each finite convolution power, not a conclusion from the toral measure's weak convergence.
Via the separately proved [exact coding entropy bridge](Yin_C_G0303_v1.md#coding-entropy-scope-and-costs), it also applies to the entropy of that convolution power of the invariant toral law.
The entropy in (1) belongs to the changed digit law; it is not identified with the original h_1.

<a id="convolution-amplitude-budget"></a>
### The quantitative upper budget

The companion [repeated-column posterior proof](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) supplies the quantitative upper deficit

    0<=m-h_k<=C(m)/k^2,
    C(m)=(5a_0^2/12)[1-(1+a_0)^(-2)],
    a_0=exp(2m)-1.                                     (9)

That proof is a separate input, not derived from weak Fourier convergence or from the strictness argument.

<a id="strict-convolution-entropy-production"></a>
### Strict entropy production at every convolution step

The coordinator contributed the following additional deduction from the two deficit bounds.
Set H_(N,0)=0 and h_0=0.
For each fixed N, let Y_1,Y_2,... be iid copies of the original complete length-N sign sum.
Their k-term sum has entropy H_(N,k).
Independence gives

    H_(N,k)-H_(N,k-1)=I(Y_1;Y_1+...+Y_k).

Adding the next independent whole-word sum is a noise channel.
Data processing therefore shows that these differences decrease with k.
Dividing by N and taking the limit at each fixed k proves

    h_(k+1)-h_k<=h_k-h_(k-1),   k>=1.                   (9a)

The companion proof already gives h_k nondecreasing and converging to m.
Since (8) makes every finite h_k strictly below m, a zero increment would, by (9a), force all later increments to vanish.
Thus h_(k+1)>h_k for every k>=1.

There is also an explicit positive bound.
Put

    d_k=g(c_opt(P)^k)/L_eff,
    n_k=max(k+1,ceil sqrt(2C(m)/d_k)).

Then C(m)/n_k^2<=d_k/2.
Equations (8)--(9) give h_(n_k)-h_k>=d_k/2, whereas discrete concavity gives h_(n_k)-h_k<=(n_k-k)(h_(k+1)-h_k).
Consequently

    boxed: h_(k+1)-h_k>=d_k/[2(n_k-k)]>0,   k>=1.       (9b)

Every constant here remains input dependent.
This is a quantitative increase along the actual convolution laws, not a uniform positive increment over k or over the unresolved near-one core.

<a id="optimizing-convolution-fourier-tests"></a>
### What optimizing k adds to the convergence budget

Combining (9) with (8) gives

    sup_(k>=1) k^2 g(c_opt(P)^k)<=L_eff C(m).             (10)

This can sharpen a finite quantitative constraint; it is not legitimate to dismiss every k comparison only because one side is exponential asymptotically.
There is, however, an exact range where optimization adds nothing to this particular upper envelope.
For 0<c<=1/2, the positive expansion

    g(x)=sum_(r>=1) x^(2r)/[2r(2r-1)]

shows that k^2 g(c^k) decreases with k.
Indeed, each term's ratio at k+1 versus k is

    ((k+1)/k)^2 c^(2r)<=4c^2<=1.

Therefore for c_opt(P)<=1/2 the k=1 inequality is already the strongest member of (10).

For every fixed 0<c<1, the same series gives g(c^k)<=log2*c^(2k), and hence k^2 g(c^k)->0.
Thus the positive deficits in (8) are compatible with the polynomial upper deficits in (9) as k grows.
They do not force an impossible amplitude or a new positive Mahler gap merely by taking arbitrarily large k.

For c>1/2 the finite supremum in (10) may improve the numerical restriction; no universal maximizing integer or input-independent bound for c_opt is assumed.
The remaining arithmetic obligation is a lower control of c_opt(P), relative to L_eff and the small-m quantity C(m), strong enough to violate (10).
As in the original witness, this entire argument excludes unit-circle conjugates.
