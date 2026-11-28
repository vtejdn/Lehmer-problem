---
author: Yin
---

# Exterior root separation and the logarithmic range of end widths

<a id="width"></a>
## What a small complete closure requires

Let \(Q\in\mathbb Z[X]\) be monic of degree \(r\), let \(Q^*=X^rQ(1/X)\) and let \(P=X^nQ\pm Q^*\) be irreducible and noncyclotomic, \(n>r\), \(d=n+r\).
Fix \(1<\lambda<\theta\), where \(\theta\) is the plastic number, and assume \(M(P)\le\lambda\).
Then
\[
                     n\ll_\lambda r\log(2r),\qquad r\gg_\lambda d/\log(2d).
\]
The [degree-ten competitor](Yin_C_G0904_v5.md#record) permits \(\lambda=19/16\) for all strict records of degree at least ten.
In particular this excludes the range \(r=o(d/\log d)\) without having to select a shorter closure.
We also give a test for an actual shorter closure on the positive Salem branch.

Remove a power of \(X\) from \(Q\) and absorb it into \(X^n\).
This only increases \(n\), decreases \(r\), and preserves \(d\) and the measure.
As in the [end-block argument](Yin_C_G0904_v7.md#width), \(r\ge1\), \(Q,Q^*\) are coprime, none of the block roots lie on the unit circle, and every irreducible factor of \(Q\) has logarithmic measure at least \(m_0=\log\theta>0\).
Write \(m=\log M(Q)\ge m_0\).

<a id="separation"></a>
## The total separation cost of the exterior roots

Index the distinct roots \(\beta_i\) of \(Q\) by \(i\), with multiplicities \(e_i\).
Put \(a_i=\beta_i\) for an interior root, and \(a_i=1/\overline{\beta_i}\), \(x_i=-\log|a_i|\) for an exterior root.
Let \(I\) index the exterior roots.
Write \(\rho(z,w)=|z-w|/|1-\bar w z|\) in the disk and \(g(z,w)=-\log\rho(z,w)\).
Set \(S_i=\sum_{h\in I,\ h\ne i}e_h g(a_i,a_h)\) for \(i\in I\), \(J=\sum_i e_i^2\), and
\[
 \mathcal D=\left|\prod_{i<h}(\beta_i-\beta_h)^{2e_ie_h}\right|.
\]
The product before taking absolute value is a nonzero rational integer because its exponents are even, its factors are integral and Galois automorphisms preserve root multiplicities.
It coincides in absolute value with the discriminant in the squarefree case.
One has
\[
           \sum_{i\in I}e_i S_i
        \le 2rm-\log\mathcal D+J\log r+O(r+J).                     \tag{1}
\]
To see this, divide each root difference by \(\max(1,|\beta_i|)\max(1,|\beta_h|)\).
For a same-side pair the resulting modulus is \(|1-\bar a_h a_i|\rho(a_i,a_h)\).
For an opposite-side pair it is \(|1-\bar a_h a_i|\).
In the logarithm of the ordered-pair product the removed factors cost at most \(2rm\).
Omitting the nonpositive log distances from the interior pairs therefore gives (1) once we control the off-diagonal kernel sum.
For \(t=e^{-1/r}\) the full sum of \(e_i e_h\log|1-t\bar a_h a_i|\) is \(-\sum_{l\ge1}(t^l/l)|\sum_i e_i a_i^l|^2\le0\).
Removing its diagonal costs at most \(J\log(1/(1-t))\le J(\log r+O(1))\).
Replacing \(t\) by one in the remaining terms costs \(O(r)\) since \(|1-u|/|1-tu|\le2/(1+t)\) for \(|u|\le1\), by the maximum modulus principle.
This proves (1), including repeated irreducible factors.

<a id="clusters"></a>
## Matching exterior roots in sets of overlapping disks

Put \(O(z)=\prod_{i\in I}((z-a_i)/(1-\bar a_i z))^{e_i}\) and let \(B(z)\) be the corresponding product on the interior indices.
Up to division by a common zero-free factor in the disk and multiplication by a constant, the equation \(P(z)=0\) becomes \(O(z)=c z^nB(z)\) with \(|c|=1\).
This follows by writing each factor \(z-\beta_i\) and \(1-\overline{\beta_i}z\) on its own side of the circle and using that \(Q\) is real.
In particular \(|B(z)|\le1\) throughout the disk.
Since \(P\) is monic and reciprocal up to sign with unit constant, its log measure is the sum of \(-\log|\gamma|\) over its roots in the disk.

Take \(0<\epsilon<1/1000\), to be fixed in terms of \(\lambda\).
Form the union of the disks \(\rho(z,a_i)<\eta_i=\epsilon |a_i|/r^2\), \(i\in I\).
If \(a_i\) lies in a component \(U\), every \(z\in\overline U\) satisfies
\[
 \rho(a_i,z)\le\gamma_i=8\epsilon |a_i|/r,\qquad
 -\log|z|\ge(1-16\epsilon)x_i .
\]
Indeed the distance \(\operatorname{artanh}\rho\) satisfies the triangle inequality and any two points in one closed disk are at distance at most \(3\eta_h\).
A chain of at most \(r\) disks gives distance at most \(3\epsilon A/r\) with \(A\) the largest center modulus in the component.
Since \(|v-w|\le2\rho(v,w)\), one has \(A\le |a_i|+6\epsilon A/r\le 2|a_i|\).
The displayed bound for the log radius follows from \(|z|\le (|a_i|+\gamma_i)/(1+|a_i|\gamma_i)\) and \(1-|a_i|^2\le2x_i\).
In particular no component contains zero.

At \(z\in\partial U\), every exterior root satisfies \(\rho(z,a_h)\ge\eta_h\).
For \(h\ne i\) with \(\rho(a_i,a_h)>2\gamma_i\), the nonnegative function \(g(\cdot,a_h)\) is harmonic on the disk of radius \(\rho(a_i,a_h)\) in the automorphism coordinate centered at \(a_i\).
Harnack's inequality at half this radius gives \(g(z,a_h)\le3g(a_i,a_h)\).
For \(h\ne i\) with \(\rho(a_i,a_h)\le2\gamma_i\), one has \(|a_h|\ge |a_i|-4\gamma_i\ge |a_i|/2\).
Thus \(g(z,a_h)\le \log(2r^2/\epsilon)+x_i\), while \(g(a_i,a_h)\ge\log(r/(16\epsilon))+x_i\).
The former is bounded by a fixed multiple of the latter.
For \(h=i\) the cutoff is \(g(z,a_i)\le2\log r+x_i+\log(1/\epsilon)\).
Consequently, with an absolute \(C\), throughout \(\partial U\) one has
\[
          -\log|O(z)|\le C S_i+e_i(2\log r+x_i+\log(1/\epsilon)).
\]
Call \(i\) good if \((1-16\epsilon)nx_i\) strictly exceeds this last upper bound.
A component with at least one good center has \(|O|>|z^nB|\) everywhere on its boundary, so the roots of \(P\) it contains match the number of exterior centers there with multiplicities.
The count also follows by continuously turning on \(c z^n B\) without a boundary zero, allowing tangencies between circles.
Every such root contributes at least \((1-16\epsilon)x_i\) for every good \(i\) in the component.
Summing by disjoint components gives \(\log M(P)\ge(1-16\epsilon)\sum_{i\ {\rm good}}e_ix_i\).

Choose \(\epsilon\) so small that \((1-16\epsilon)m_0>\log\lambda\).
Since \(\sum_{i\in I}e_i x_i=m\), bad centers carry at least \(c_\lambda m\) for some \(c_\lambda>0\).
Sum their defining inequalities against \(e_i\).
By (1), \(\sum_{i\in I}e_i^2 x_i\le rm\), \(\mathcal D\ge1\), and \(J\le r\max_i e_i\), this gives
\[
                    nm\ll_\lambda rm+J\log(2r).
\]
Each irreducible factor occurring \(e_i\) times costs at least \(e_i m_0\), so \(\max_i e_i\le m/m_0\).
This proves the claimed logarithmic width bound.

<a id="squarefree"></a>
## A discriminant condition for width proportional to the degree

For a squarefree reduced block a sharper comparison is
\[
          nm\ll_\lambda rm+\big(r\log r-\log|\operatorname{disc}Q|\big)_+ .
\]
In particular \(r=o(d)\) forces the positive difference on the right, divided by \(rm\), to tend to infinity.
To retain this term, use separate disks of radii \(\eta_i=\epsilon |a_i|\exp(-S_i)\) around the exterior centers.
They are pairwise disjoint since \(\exp(-S_i)\le\rho(a_i,a_h)\) for \(i\ne h\), and intersection would require \(\rho(a_i,a_h)\le\eta_i+\eta_h\).
In this squarefree case the Blaschke product with just its \(i\)-th factor removed has modulus \(\exp(-S_i)\) at \(a_i\).
The Schwarz–Pick inequality bounds its modulus below by \((1-\epsilon)\exp(-S_i)\) on the boundary, also when the product is constant.
Hence \(-\log|O(z)|\le 2S_i+x_i+\log(1/(\epsilon(1-\epsilon)))\) there, with \(-\log|z|\ge(1-2\epsilon)x_i\).
The same root comparison now gives \(nm\ll_\lambda \sum_i S_i+m+r\), where the sum is over the exterior centers.
Using (1) with \(J=r\) proves the assertion.

<a id="shorter"></a>
## Testing the sign and the number of exterior roots of a shorter closure

Suppose \(P=X^nQ+Q^*\) is a positive Salem minimum with exterior root \(\alpha\).
Then \(P(1)<0\) and \(Q(1)<0\), by the positive reciprocal root pair and all the remaining conjugate pairs on the circle.
Also \(Q(\alpha)\ne0\) by coprimality.
For \(1\le j<n\) write \(D_j^\pm=X^jQ\pm Q^*\).
At \(\alpha\) one has
\[
 D_j^+(\alpha)=(\alpha^j-\alpha^n)Q(\alpha),\qquad
 D_j^-(\alpha)=(\alpha^j+\alpha^n)Q(\alpha).
\]
Any negative value here forces a real root larger than \(\alpha\) by monicity, excluding that sign for every shorter exponent.
For \(Q(\alpha)<0\) the surviving plus sign has a root in \((1,\alpha)\).
For \(Q(\alpha)>0\) the surviving minus sign has such a root whenever \((j-r)Q(1)+2Q'(1)<0\), since this expression is \((D_j^-)'(1)\).

The number of exterior roots can be tested from the arguments of the block roots.
Define the phase of \(z^jQ(z)/Q^*(z)\) on the unit circle as a continuous lift on \(0\le t\le2\pi\), \(z=e^{it}\).
Its derivative is \(j+\sum_{i\notin I}e_i K_i(t)-\sum_{i\in I}e_i K_i(t)\), where \(K_i(t)=(1-|a_i|^2)/|e^{it}-a_i|^2\).
This follows from the argument derivative of one Blaschke factor.
For a sign whose level \(\mp1\) has only transverse crossings, let \(b_j\) count its negative crossings once per circle.
The winding is \(j+r-2k\), where \(k=\sum_{i\in I}e_i\).
Therefore the circle has \(j+r-2k+2b_j\) simple roots of that closure, and reciprocity shows that the number of its exterior roots is exactly \(k-b_j\).
If the surviving sign has the root in \((1,\alpha)\) just certified and \(b_j=k-1\), then \(1<M(D_j^\pm)<\alpha\).
Thus an actual strict Salem record excludes this joint sign and crossing condition at every \(j<n\).
Tangencies need a separate count, and the measure and separation bounds above do not force such a shorter exponent throughout \(d/\log(2d)\ll r=o(d)\).

<a id="example"></a>
## An explicit shorter closure below the plastic number

Take \(Q=x^5-x^3-1\) and \(P=x^{15}Q+Q^*=x^{20}-x^{18}-x^{15}-x^5-x^2+1\).
This is an irreducible Salem polynomial with \(5/4<M(P)<13/10<\theta\).
The shorter exponent \(j=12\) gives
\[
    x^{12}Q-Q^*=(x-1)(x^6+x^3+1)L(x),
\]
where \(L\) is the [degree-ten Lehmer polynomial](Yin_C_G0904_v5.md#record).
The first two factors are cyclotomic, so \(1<M(x^{12}Q-Q^*)=M(L)<19/16<M(P)\).
This example supplies a competitor for a complete separated closure of small measure which is itself outside the strict-record class.

Here are exact verifications for \(P\).
Let \(y=x+x^{-1}\), \(D_0=2,D_1=y,D_{k+1}=yD_k-D_{k-1}\).
Then \(x^{-10}P=H(y)=D_{10}-D_8-D_5\), with
\[
 H=y^{10}-11y^8+43y^6-y^5-70y^4+5y^3+41y^2-5y-4.
\]
Its signs alternate from positive to negative at the ten rational arguments
\[
 -2,\ -19/10,\ -9/5,\ -8/5,\ -1,\ -1/5,\ 1/2,\ 1,\ 3/2,\ 19/10 .
\]
These give nine roots in \((-2,2)\).
As \(H(2)=-2\) and \(H\) is monic, its remaining root is above two.
Modulo three, successive cubing and reduction by \(H\) give \(y^{3^{10}}=y\) and
\[
 y^{3^2}=y^9,\qquad y^{3^5}=-y^9+y^8+y^7-y^6+y^4+y^2+1 .
\]
Subtracting \(y\) from each of the last two remainders gives gcd one with \(H\) by the Euclidean algorithm.
Thus all irreducible factor degrees divide ten and none divides two or five, proving irreducibility.
For a root \(y\) of \(H\), the element \(y^2-4\) is negative at a real embedding of \(\mathbb Q(y)\), so \(x^2-yx+1\) is irreducible over that field.
This gives the claimed irreducible reciprocal polynomial with just one exterior root.
Evaluation gives \(P(5/4)<0<P(13/10)\), and \((13/10)^3-13/10-1<0\).
Direct multiplication proves the shorter factorization.

## Assessment history

### Decision separation-and-shorter-closures

| Field | Value |
| --- | --- |
| date | 2026-11-28T08:07 |
| status | proved |
| reason | Counting the disk zeros component by component bounds the lost exterior measure by the integral separation cost. On the Salem branch the root crossings test the remaining sign, and the degree-twenty example has an explicit competitor. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Width comparison](#width) | Width at least degree divided by its logarithm for a whole separated closure. |
| argument | [Root separation](#separation) | Integral weighted discriminant and disk Green functions. |
| argument | [Root matching](#clusters) | Rouché comparison on components with multiplicities. |
| argument | [Squarefree case](#squarefree) | The retained discriminant deficit in the width bound. |
| argument | [Shorter closures](#shorter) | Sign and crossing criteria on the positive Salem branch. |
| argument | [Worked comparison](#example) | Exact shorter exponent and factorization with a Lehmer factor. |
| dependency | [End-block hypotheses](Yin_C_G0904_v7.md#width) | Coprimality and measure lower bound for block factors. |
| dependency | [Lehmer competitor](Yin_C_G0904_v5.md#record) | Measure and explicit ceiling for the degree-ten input. |
| review | [Width and sign examination](../audits/reviews/Yin_R_G0562_v1299.md#finding) | First five sections including repeated roots, the squarefree refinement and the conditional crossing count. |
| review | [Independent example examination](../audits/reviews/Yin_R_G0562_v1303.md#finding) | The sixth section on the degree-twenty example, its Salem property and the strict shorter comparison. |

## Current assessment

[Selected decision](#decision-separation-and-shorter-closures)
