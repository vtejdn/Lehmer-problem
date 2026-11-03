---
author: Yin
---

# Strict Fourier deficit for every finite convolution power

The current complete mathematical proof is retained in [C306](../claims/Yin_C_G0306_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
This note extends the actual trace-frequency/KL proof to a fixed sum of k fair signs at each time, keeping its separation and boundary constants.
It does not infer measure entropy from weak Fourier convergence.
No new source or computation is used.

Let alpha be an algebraic unit with monic irreducible polynomial P, with no unit-circle conjugate, and put m=log M(P)>0.
Let d=deg P, and s the real dimension of its stable embedding space.
Use the normal real stable matrix A, stable embedding iota, and product bodies K_N of [L G0102](Yin_L_G0102_v1.md#disjoint-smoothing-relative-entropy).
Let k>=1 be a fixed integer, and let eta_j be independent, each distributed as a sum of k independent fair signs.
Set

    S_(N,k)=sum_(j=0)^(N-1) eta_j alpha^j,
    H_(N,k)=H(S_(N,k)),    h_k=lim_N H_(N,k)/N.           (1)

The limit exists by independent-block subadditivity.
For k=1 this is the original fair-binary rate, with the usual injective sign/bit affine conversion.
All logarithms are natural.

<a id="convolution-sign-separation"></a>
## Separation and smoothing with the full k dependence

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
## The same frequency spacing and the k-th power amplitude

For theta in O_K minus {0}, use the exact trace multiplier and frequencies from [L G0103](Yin_L_G0103_v1.md#algebraic-trace-multiplier).
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

The uniform multiplier caps of L G0103, strengthened in [L G0107](Yin_L_G0107_v1.md#two-unit-defect-energy-floor), give 0<c_opt(P)<1.
No maximum or optimizing multiplier is asserted to exist.
Since the left side of (7) and its spacing are independent of theta, continuity and monotonicity permit taking this supremum after the fixed-multiplier bounds:

    boxed: m-h_k>=g(c_opt(P)^k)/L_eff>0
                                      for every k>=1.  (8)

This is actual strictness for each finite convolution power, not a conclusion from the toral measure's weak convergence.
Via the separately proved [exact coding entropy bridge](Yin_L_G0106_v1.md#coding-entropy-scope-and-costs), it also applies to the entropy of that convolution power of the invariant toral law.
The entropy in (1) belongs to the changed digit law; it is not identified with the original h_1.

<a id="convolution-amplitude-budget"></a>
## The quantitative upper budget

The companion [repeated-column posterior proof](Yin_L_G0108_v1.md#quantitative-convolution-entropy-convergence) supplies the quantitative upper deficit

    0<=m-h_k<=C(m)/k^2,
    C(m)=(5a_0^2/12)[1-(1+a_0)^(-2)],
    a_0=exp(2m)-1.                                     (9)

That proof is a separate input, not derived from weak Fourier convergence or from the strictness argument.

<a id="strict-convolution-entropy-production"></a>
## Strict entropy production at every convolution step

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
## What optimizing k adds to the convergence budget

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



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0031_v1.md#contribution-and-review-scope), with its original inspected scope and relationship.
