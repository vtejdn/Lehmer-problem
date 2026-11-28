---
author: Yin
---

# A linear lower bound for the width of separated end blocks

<a id="width"></a>
## Comparing the full closure with its end block

Let \(Q\in\mathbb Z[X]\) be monic of degree \(r\ge1\), with \(Q(0)\ne0\) and \(\gcd(Q,Q^*)=1\), where \(Q^*(X)=X^r Q(1/X)\).
Write \(m=\log M(Q)\) and \(P=X^nQ\pm Q^*\), with \(n>r\).
There is an absolute constant \(C\) such that
\[
    \log M(P)\ \ge\ \left(1-C\frac rn\log\frac{2n}{r}\right)m.       \tag{1}
\]
Both signs and arbitrary block root multiplicities are allowed.
For an irreducible noncyclotomic complete closure with \(M(P)\le\lambda<\theta\), where \(\theta\) is the plastic number, this gives \(n\ll_\lambda r\) and \(r\gg_\lambda d\), with \(d=n+r\).
Indeed after absorbing any monomial factor in \(X^n\), [irreducibility ensures the block hypotheses and \(m\ge\log\theta\)](Yin_C_G0904_v7.md#width).
If the reduced width were zero the closure would be cyclotomic.
The reduction increases \(n\), decreases \(r\) and preserves \(d\).
The [degree-ten competitor](Yin_C_G0904_v5.md#record) therefore excludes \(r=o(d)\) for every sequence of strict records that are complete separated closures.
The comparison uses the original closure directly and does not assert the existence of a shorter exponent for each finite input.

<a id="energy"></a>
## A bounded separation kernel from the reciprocal resultant

Write the roots of \(Q\) with multiplicities, send an exterior root \(\beta_i\) to \(a_i=1/\overline{\beta_i}\) and an interior root to \(a_i=\beta_i\).
There are no unit circle roots since \(Q\) is real and coprime to \(Q^*\).
Put \(x_i=-\log|a_i|\), let \(I\) be the set of exterior indices, and use \(\rho(z,w)=|z-w|/|1-\bar w z|\).
Then \(\sum_{i\in I}x_i=m\) and \(\sum_{i=1}^r x_i=2m-\log|Q(0)|\le2m\).
The [reciprocal resultant estimate](Yin_C_G0904_v7.md#energy) gives
\[
 E(a)=\sum_{\ell\ge1}\frac{|\sum_i a_i^\ell|^2}{\ell}
     =-\sum_{i,h}\log|1-a_i\bar a_h|\le 2rm .
\]
Put \(T(z)=\sum_{h\in I}(1-\rho(z,a_h)^2)\) and \(T_i=T(a_i)\).
We claim
\[
                \sum_{i\in I}T_i\ll rm .                              \tag{2}
\]
For a pair of arbitrary indices put \(s=x_i+x_h>0,\ a_i\bar a_h=e^{-s+i\phi}\), and let \(K_v=(1-e^{-2v})/|1-e^{-v+i\phi}|^2\).
Logarithmic differentiation gives
\[
 L_{ih}=\frac12\int_s^{2s}K_v\,dv
 =\frac{s}{2}+\log|1-e^{-2s+i\phi}|-\log|1-e^{-s+i\phi}|.
\]
For \(s\le v\le 2s\), the denominator modulus is at most \(2|1-e^{-s+i\phi}|\) and the numerator increases.
Consequently \(L_{ih}\ge sK_s/8\).
Moreover
\[
 \frac{1-\rho(a_i,a_h)^2}{K_s}
 =\frac{(1-e^{-2x_i})(1-e^{-2x_h})}{1-e^{-2s}}\le 2x_i\le2s .
\]
All pair terms are nonnegative.
Summing \(L_{ih}\) over all ordered pairs gives \(r\sum_i x_i+E(a)-E(b)\), where \(b_i=|a_i|a_i\).
Since \(E(b)\ge0\), the sum is at most \(4rm\), which proves (2).

<a id="contours"></a>
## A local comparison on movable circles

Write \(x(z)=-\log|z|\) for \(0<|z|<1\).
Let \(O(z)\) be the product of the elementary Blaschke factors at the exterior centers and \(B(z)\) the analogous product for the interior roots.
In the disk the zeros of \(P\), with multiplicities, are those of \(O(z)-c z^n B(z)\), \(|c|=1\), by the [factorization of the closure](Yin_C_G0904_v8.md#clusters).
Fix \(0<\epsilon\le1/100\), let \(H=\epsilon |z|\), and put \(U(z,h)=\{u:\rho(u,z)<h\}\).
There is a radius \(H<h<(1+\epsilon)H\) such that on \(\partial U(z,h)\)
\[
             -\log|O(u)|\le C_1\,T(z)\big(1+\log(1/\epsilon)+x(z)\big) .   \tag{3}
\]
Here and below numbered constants are absolute.
Pass to the disk automorphism coordinate with center \(z\), and let \(b\) denote the coordinate of \(a_i\).
If \(|b|\ge1/2\), then for \(|v|=h\) the distance \(\rho(v,b)\) stays bounded below by an absolute positive constant.
The identity \(1-\rho(v,b)^2=(1-|v|^2)(1-|b|^2)/|1-\bar b v|^2\) bounds \(-\log\rho(v,b)\) by \(C(1-|b|^2)\).
If \(|b|<1/2\), the maximum of \(-\log\rho(v,b)\) on the circle is at most \(\log(2/|h-|b||)\).
Its average over the radius interval is at most \(C+\log(1/(\epsilon H))\), by integration of the logarithm over an interval of length \(\epsilon H\).
Each such index contributes at least \(3/4\) to \(T(z)\).
Averaging the sum of the individual maxima proves (3), even for coincident centers.

For \(0<\eta\le1/50\), points \(u\in\overline{U(z,\eta|z|)}\) satisfy
\[
     |u|/|z|=1+O(\eta),\qquad x(u)/x(z)=1+O(\eta).
\]
Indeed the extreme moduli in the disk lie at \((|z|\pm\eta|z|)/(1\pm\eta|z|^2)\).
The changes in their logarithms relative to \(\log|z|\) are \(O(\eta(1-|z|^2))=O(\eta x(z))\).
Also \(T(u)\asymp T(z)\) there, by the automorphism formula for \(1-\rho^2\) in the preceding paragraph.
These facts hold uniformly both towards zero and towards the unit circle.

Call \(i\in I\) good if
\[
         n x_i>C_2\,T_i\big(1+\log(1/\epsilon)+x_i\big)
\]
for a sufficiently large absolute \(C_2\).
Whenever \(U(z,H)\) contains a good center, the preceding comparisons and (3) give \(|O(u)|>|u|^n\ge |u^n B(u)|\) on the selected circle.
Rouché's theorem equates the numbers of zeros of \(P\) and of \(O\) in that circle.
Hence for every \(0<|z|<1\),
\[
  \#\{i\ {\rm good}:a_i\in U(z,\epsilon|z|)\}
  \ \le\ \#\{\gamma:P(\gamma)=0,\ \gamma\in U(z,(1+\epsilon)\epsilon|z|)\}.       \tag{4}
\]
The inequality with zero on the left needs no circle selection.
Repeated roots count with their multiplicities.
The bad exterior indices satisfy
\[
 \sum_{i\ {\rm bad}}x_i\ll \frac{rm}{n}\big(1+\log(1/\epsilon)\big)                \tag{5}
\]
by (2), \(T_i\le r\) and \(\sum_{i\in I}x_i=m\).

<a id="averaging"></a>
## Counting the logarithmic mass of the same root in neighboring disks

Integrate (4) against \(x(z)|z|^{-2}dA(z)/(1-|z|^2)^2\), with \(dA\) ordinary plane area.
For any \(0<|a|<1\), its contribution at radius parameter \(0<\eta\le1/50\) is
\[
 J_\eta(a)=\int_{\rho(z,a)<\eta |z|}
               \frac{x(z)}{|z|^2}\frac{dA(z)}{(1-|z|^2)^2}
           =\pi\eta^2 x(a)(1+O(\eta)).                                  \tag{6}
\]
On the integration set, \(|z|/|a|\) and \(x(z)/x(a)\) differ from one by \(O(\eta)\) by the local comparisons.
This set is enclosed between disks centered at \(a\) of radii \(\eta |a|(1-C\eta)\) and \(\eta |a|(1+C\eta)\) for an absolute \(C\), taking \(\eta\) sufficiently small.
For the inner inclusion apply the same modulus bound with center \(a\), then use symmetry of \(\rho\).
The area in \(dA(z)/(1-|z|^2)^2\) of a disk of radius \(h\) is \(\pi h^2/(1-h^2)\) by invariance under disk automorphisms.
These estimates give (6) with absolute uniform error.

Each interior root is nonzero because \(P\) has unit constant.
Reciprocity up to sign and monicity give \(\sum_{|\gamma|<1}x(\gamma)=\log M(P)\).
Interchanging finite sums and integrals in (4), and using (6) at \(\epsilon\) and \((1+\epsilon)\epsilon\), gives
\[
 (1-O(\epsilon))\sum_{i\ {\rm good}}x_i\le\log M(P).
\]
Combining with (5), we obtain (1) by taking \(\epsilon=c r/n\) with an absolute sufficiently small \(c>0\).
In particular \(n/r\to\infty\) would give \(\log M(P)\ge(1-o(1))\log M(Q)\), in conflict with \(M(P)\le\lambda<\theta\) on the irreducible branch.
The estimate handles the large squarefree discriminant deficits left by the [previous separation argument](Yin_C_G0904_v8.md#squarefree) as well as non-squarefree blocks.
For Salem records, the [sign and phase criterion](Yin_C_G0904_v8.md#shorter) remains available when an explicit finite shorter witness is wanted.

## Assessment history

### Decision linear-end-width

| Field | Value |
| --- | --- |
| date | 2026-11-28T08:28 |
| status | proved |
| reason | The reciprocal resultant bounds the interaction of reflected roots, and integration of the local zero counts recovers their logarithmic mass with uniform error. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Measure and width](#width) | Quantitative comparison for both signs and the linear width consequence for all complete record closures. |
| argument | [Bounded separation energy](#energy) | Integral reciprocal resultant and radial contraction, with all multiplicities. |
| argument | [Movable comparison circles](#contours) | Local Rouché counts for good centers and total bad mass. |
| argument | [Weighted disk counts](#averaging) | Area estimate, integration and choice of the radius parameter. |
| dependency | [Reciprocal resultant](Yin_C_G0904_v7.md#energy) | Fourier energy bound including repeated roots. |
| dependency | [Block factors](Yin_C_G0904_v7.md#width) | Reduction, coprimality and the nonreciprocal Mahler measure gap. |
| dependency | [Disk equation](Yin_C_G0904_v8.md#clusters) | Blaschke product factorization inside the unit disk. |
| dependency | [Record ceiling](Yin_C_G0904_v5.md#record) | Lower-degree competitor placing eventual records below the plastic number. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1304.md#finding) | Both signs, arbitrary multiplicities, all four proof sections and the record consequence. |

## Current assessment

[Selected decision](#decision-linear-end-width)
