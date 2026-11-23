---
author: Yin
---

# Salem factors through degree 44 in every primitive direction

<a id="classification"></a>
## A single nonmonic family through degree 44

Let \(q\ge2\), \(|a|=q\), \(|b|=q+1\), \(\epsilon=\pm1\), and \(1\le u<v\) be coprime integers.
Suppose \(z\) is a nontorsion unit root of \(a(1+\epsilon X^{g(u+v)})+b(X^{gu}+\epsilon X^{gv})\) at some integer \(g\ge1\).
If \(\beta=z^g\), up to sign and conjugacy, is a Salem number of degree at most 44, then \(q=2,\ u=1,\ v=13,\ \epsilon=+1\).
In that family exactly the preimages of the signed sextic roots described in the [short-exponent-one classification](short_one.md#classification) qualify.
This also classifies reciprocal unit factors of primitive degree at most 44 with exactly one exterior root, since an exterior quadratic reciprocal unit would have integer trace of absolute value at least three.
Indeed after reflection and passage to a positive exterior root \(\lambda\), the strict radial bound gives \(\lambda+\lambda^{-1}\le\lambda^u+\lambda^{-u}<2(q+1)/q\le3\).
Factors with several exterior conjugates are outside the classification.

<a id="bounds"></a>
## Why only two additional short exponents occur

Use rational conjugacy and, if necessary, substitute \(-X\) to take the primitive root \(\lambda>1\) to be the positive Salem number.
Reflection replaces \(b,\epsilon\) by \((-1)^u b,(-1)^{u+v}\epsilon\) and preserves the coefficient magnitudes.
The real numbers \(1+\epsilon\lambda^{u+v}\) and \(\lambda^u+\epsilon\lambda^v\) have the same sign.
Thus after an overall sign the coefficients are \(q,-p\) with \(p=q+1\).
If \(\lambda<13/10\), the [previous exact test](catalogue.md#catalogue) and Mossinghoff's stated joint completeness for this size and degree leave only a hit at \(q=1\).
We may therefore use \(\lambda\ge13/10\).

Write \(T=\lambda^u\).
The [radial estimate](../../../claims/Yin_C_G0345_v869.md#radius) gives \(q<2T/(T-1)^2\) and \(T+T^{-1}<2p/q\le3\), hence \(T<3\).
The upper bound for \(q\) decreases with \(T>1\).
At \(u\ge2\), comparison with \(T\ge(13/10)^u\) leaves exactly \(2\le q\le7\) for \(u=2\) and \(2\le q\le3\) for \(u=3\) as possible ranges.
At \(u\ge4\) that upper bound is less than two.

For the degree \(D=[\mathbb Q(\lambda):\mathbb Q]\le44\), all \(D-1\) other conjugates of \(T\) counted over this field have modulus at most one.
The algebraic integer \(qT-p\) is nonzero because a positive rational unit must equal one.
Its nonzero integer norm gives \(|qT-p|\ge(p+q)^{1-D}\).
The section equation now bounds the long exponent by
\[
 (13/10)^v\le \lambda^v=\frac{pT-q}{|qT-p|}<(3p-q)(p+q)^{43}.
\]
Thus the earlier long-exponent cutoff remains valid at either new short exponent.

<a id="reproduction"></a>
## Exact factorization in the residual ranges

The [program](salem_directions.py) calculates each cutoff by integer arithmetic, tests coprime exponents and both signs, and reconstructs every factorization including its content and multiplicities.
In the retained ranges it finds no monic noncyclotomic irreducible factor of degree at most 44 and constant coefficient of absolute value one.
The complementary short-exponent-one case and its only witness are [already classified](short_one.md#classification).

| \(u\) | \(q\) in increasing order | First excluded \(v\) at each \(q\) | Signed parents tested |
| ---: | --- | --- | ---: |
| 2 | 2, 3, 4, 5, 6, 7 | 272, 328, 370, 403, 431, 455 | 2,244 |
| 3 | 2, 3 | 272, 328 | 790 |

Run the following from the checkout with Python 3 and python-flint 0.9.0 to reproduce all 3,034 additional factorizations.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/salem_directions.py
~~~
