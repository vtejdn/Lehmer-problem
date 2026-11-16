---
author: Yin
---

# Exterior root mass in the half-degree encoding of a reciprocal polynomial

<a id="statement"></a>
## A lower bound for the full polynomial

Let \(f\) be a monic real polynomial of degree \(r\) with \(f(0)\ne0\), and put \(g(z)=z^rf(1/z)\).
For \(N\ge1\) and \(|\tau|=1\), set \(D=z^N f+\tau g\) and write \(m=\log M\) for logarithmic Mahler measure.
List the positive numbers \(s_i=\log|\alpha_i|\) for the roots of \(f\) outside the unit circle, with multiplicities, and let \(k\) be their number.
For \(0<u\le1/4\) put \(L(u)=\sum_{i=1}^k\min(s_i,u)\).
If \(Nu>8L(u)/u\), then
\[
 m(D)\ \ge\ m(f)-4L(u)+\log\!\left(1-\exp[-Nu+8L(u)/u]\right).       \tag{1}
\]
In particular for \(v>0\) and \(N\ge4(8k+v)\),
\[
 m(D)\ \ge\ m(f)-\frac{4k(8k+v)}{N}+\log(1-e^{-v}).                 \tag{2}
\]
The estimate concerns the full polynomial, or its positive factor when every other factor has measure one.
It allows arbitrary degrees, coefficient heights and distances of individual roots from the circle.
The [fixed-seed Salem–Boyd convergence theorem](../audits/literature/Hir06/Yin_U001.md#hir06-u001) gives context for the one-sided estimate with a changing seed.

<a id="circle"></a>
## Choosing an interior circle

Fix a circle of radius \(\rho=1-t\), with \(u\le t\le2u\).
The factors of \(f/g\) may be written \((z-\alpha)/(1-\bar\alpha z)\), pairing conjugates in the denominator.
For \(|\alpha|\le1\) the modulus of this factor is at most one in the disk, with removable cancellations for unit roots.
For \(|\alpha|>1\) put \(b=|\alpha|^{-1}\) and \(x=1-b\).
The modulus of the corresponding inverse Blaschke factor on this circle is at most \((1-b\rho)/|\rho-b|\), by minimizing the modulus of the Blaschke factor at the angle of its zero.
The bound is at most \((x+t)/|x-t|\).
We claim
\[
 \frac1u\int_u^{2u}\log\frac{x+t}{|x-t|}\,dt\ \le\ 8\min(1,x/u).   \tag{3}
\]
When \(x\le u/2\), the integrand is bounded by \(2x/(t-x)\le4x/u\).
When \(x\ge4u\), the ratio is at most three.
In the remaining range set \(y=x/u\), \(w=t/u\).
The integral average is at most \(\log6+\int_1^2\log^+(1/|y-w|)\,dw\le\log6+2<4\), while \(\min(1,y)\ge1/2\).
This proves (3), including an integrable singularity inside the interval.

For an exterior root with logarithmic modulus \(s_i\), one has \(x=1-e^{-s_i}\le s_i\).
Summing (3) gives a radius in the interval at which \(g\) is nonzero throughout the circle and \(\sup_{|z|=\rho}|f/g|\le\exp(8L(u)/u)\).
This also holds directly when there are no exterior roots.
Since \(\rho^N\le e^{-Nu}\), putting \(b_0=\exp[-Nu+8L(u)/u]<1\) gives \(|D|\ge(1-b_0)|g|\) on the chosen circle.
The circular logarithmic mean of \(D\) there is at most \(m(D)\) by Jensen's formula.
The circular logarithmic mean of \(g\) there is exactly \(m(f)-\sum_i\min(s_i,-\log\rho)\), since its interior roots are precisely the reciprocals of the exterior roots of \(f\), and \(m(g)=m(f)\).
Here \(-\log\rho\le 2t\le4u\), so this sum is at most \(4L(u)\).
Averaging the pointwise bound proves (1).
Using \(L(u)\le ku\) and \(u=(8k+v)/N\) proves (2).

<a id="half-degree"></a>
## A necessary condition on every reciprocal input approaching measure one

Let \(P\) be a monic reciprocal irreducible integer polynomial of degree \(d=2N\ge4\) with \(m(P)>0\).
Both [half-degree seeds](Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) are monic integral unit polynomials with \(z^Nf+g=(z+1)P\), and neither is proportional to its reversal.
At least one irreducible factor of each seed must therefore be nonreciprocal, whence \(m(f)\ge m_0=\log\theta_0\) by [Smyth's bound](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number), where \(\theta_0>1\) solves \(\theta_0^3-\theta_0-1=0\).
Since \(m(D)=m(P)\), (2) with \(v=4\) gives
\[
                 N\ge512k^2\quad\Longrightarrow\quad m(P)>m_0/2.      \tag{4}
\]
Indeed \(k\ge1\), \(4k(8k+4)/N\le3/32\), and \(3/32-\log(1-e^{-4})<m_0/2\) (already \(\theta_0>1.3\)).
Thus any \(P\) below this threshold has more than \(\sqrt d/32\) exterior roots in each of its two specified seeds.

There is also a constraint on the exterior logarithmic mass, even when the number of exterior roots is large.
Along any sequence \(m(P)\to0\) of such positive inputs the degrees tend to infinity, since for bounded degrees and measures the coefficients of monic integer polynomials are bounded.
For either choice of seed at each index, and every fixed \(a>0\),
\[
 \liminf L(a/\sqrt N)\ \ge\ \min(m_0/4,a^2/8),\qquad
 \liminf\frac{k}{\sqrt N}\ \ge\ \sqrt{m_0/32}.                       \tag{5}
\]
Indeed, on a subsequence on which \(L(a/\sqrt N)\) stays strictly below both constants by a fixed amount, the exponential in (1) tends to zero and \(m(f)-4L(a/\sqrt N)\) stays positive by a fixed amount.
This contradicts \(m(P)\to0\).
Use \(L(a/\sqrt N)\le ak/\sqrt N\) at \(a=\sqrt{2m_0}\) for the second assertion.
The older [separated-root alternative](Yin_C_G0345_v1.md#encoding-inverse-and-cyclic-cost) controls every positive factor under its annulus and delay assumptions.
Here (5) is necessary on an arbitrary hypothetical near-one reciprocal sequence, with no annulus assumption, through the exact single positive factor in its representation.
Whether the two half-degree seeds can simultaneously meet (5) for measures approaching one remains open.

## Assessment history

### Decision radial-bound-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T12:50 |
| status | open |
| reason | Submit the radial estimate and its application to both seeds for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full delayed polynomial](#statement) | Both inequalities, with no coefficient or annulus constraint. |
| argument | [Interior circles](#circle) | Averaged inverse Blaschke factors and exact Jensen loss at the chosen radius. |
| argument | [Original polynomial](#half-degree) | Finite square-root bound and asymptotic truncated-mass condition for both seeds. |
| dependency | [Two exact seeds](Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) | Encoding identity and nonreciprocity of both monic unit seeds. |
| dependency | [Nonreciprocal lower bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Mahler measure at least the plastic number for a nonreciprocal irreducible integer unit. |

### Decision radial-bound-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T13:05 |
| status | proved |
| reason | The common-circle estimate and both half-degree consequences pass independent review, including the strict finite threshold and the truncated exterior mass. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full delayed polynomial](#statement) | Both inequalities, with no coefficient or annulus constraint. |
| argument | [Interior circles](#circle) | Averaged inverse Blaschke factors and exact Jensen loss at the chosen radius. |
| argument | [Original polynomial](#half-degree) | Finite square-root bound and asymptotic truncated-mass condition for both seeds. |
| dependency | [Two exact seeds](Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) | Encoding identity and nonreciprocity of both monic unit seeds. |
| dependency | [Nonreciprocal lower bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Mahler measure at least the plastic number for a nonreciprocal irreducible integer unit. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v3.md#radial-half-degree-review) | Entire radial estimate and both original-polynomial consequences, with no annulus or coefficient bound. |

## Current assessment

[Selected decision](#decision-radial-bound-reviewed)
