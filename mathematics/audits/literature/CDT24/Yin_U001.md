---
author: Yin
---
# CDT24-U001: the expansion threshold for integral holonomic germs

<a id="cdt24-u001"></a>
## Inspected statement and comparison scope

Use the [220-page author manuscript and edition boundary](readme.md), not an assumed identification with arXiv v2.
Agent-S inspected Theorem 2.5.1 and (2.5.2)--(2.5.6), pp. 16--17; (6.0.4)--(6.0.6), pp. 67--68; Theorems 7.1.6, 7.1.10 and 7.1.13, pp. 93--94; and Theorem 8.0.1 with Remark 8.0.6, pp. 123--124.
The coordinating agent directly checked the statements on pp. 16--17 and 123--124 and the applicability below.
These are statement and hypothesis checks, not a source-proof audit or an independent review of project mathematics.

<a id="zero-denominator-threshold"></a>
## Zero denominator type retains a strict analytic threshold

In the zero-denominator specialization of Theorem 2.5.1, let \(r\) germs \(f_i\in\mathbb Z[[x]]\) be linearly independent over \(\mathbb Q(x)\) and holonomic.
For the closed-disk specialization needed in L445, let \(\varphi\) be holomorphic on a neighborhood of \(\overline{\mathbb D}\), fix zero, and make every \(f_i\circ\varphi\) meromorphic on \(\mathbb D\).
With Haar probability \(\mu\), the stated bound is
\[
 r\le\frac{B(\varphi)}{\log|\varphi'(0)|},
 \qquad
 B(\varphi)=\iint_{\mathbb T^2}\log|\varphi(z)-\varphi(w)|\,d\mu(z)d\mu(w),
 \qquad |\varphi'(0)|>1.
\]
The general denominator penalty is \(\tau(b)=r^{-2}\sum_i(2i-1)\sigma_i\ge0\), where \(\sigma_i\) are the ordered denominator row sums specified in (2.5.2).
Theorem 8.0.1 replaces this by \(\tau^{\flat\flat}(b)+\tau^\sharp(e)\), still requiring a strictly positive difference from \(\log|\varphi'(0)|\).
The nonnegative denominator counts in (8.0.2) vanish for \(b=0\), and the integration penalty vanishes for \(e=0\).
The convexity corrections (8.0.4)--(8.0.5) improve the numerator while retaining that denominator and hypothesis.

The [L445 orbit sums](../../../ledger/Yin_L_G0445_v1.md#rotated-radicals) are integral algebraic germs, hence holonomic, so their denominator data can already be zero.
Thus these improvements provide no negative denominator credit from extra dyadic divisibility and do not make a supplied map with \(|\varphi'(0)|\le1\) admissible.
This is a direct applicability check, not a prohibition on different functions, maps or arithmetic evaluation estimates.
The separate [D11 disk comparison](../../../drafts/Yin_D_G0011.md#neutral-disk), including its proposed transfer to actual Salem roots, retains its unreviewed working scope.
No universal obstruction for original Lehmer inputs or new positive Mahler gap is inferred.
