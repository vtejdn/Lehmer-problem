---
author: Yin
---

<a id="aknr18-u001"></a>
# Univariate root moduli and the geometric tails of a dominant monomial

<a id="tropical"></a>
## The logarithmic coordinates

For a complex Laurent polynomial \(f(X)=\sum_{j=1}^t c_j X^{a_j}\) in \(n\) variables with distinct exponents \(a_j\in\mathbb Z^n\) and \(c_j\ne0\), its amoeba consists of the vectors \((\log|z_1|,\ldots,\log|z_n|)\) at zeros \(z\in(\mathbb C^*)^n\).
Its Archimedean tropical variety \(T=\operatorname{ArchTrop}(f)\) is the set of \(s\in\mathbb R^n\) where at least two indices maximize \(\log|c_j|+\langle a_j,s\rangle\).
The authors use natural logarithms and the convex hull of the points \((a_j,-\log|c_j|)\).
In one variable the slopes of the lower edges of that hull are exactly the elements of \(T\).
These conventions occur in Definitions 1.1 and 1.4, Proposition 1.23 and Lemma 1.24 on pages 1, 2 and 8 of the [inspected edition](readme.md#edition).

<a id="tail"></a>
## The univariate estimate

Suppose \(n=1\), \(t\ge2\) and \(a_1<\cdots<a_t\).
Theorem 1.5 on page 3 puts every \(\log|z|\) for \(f(z)=0\), \(z\ne0\), in the open set
\[
(\min T-\log 2,\max T+\log 2)\ \cap\ \bigcup_{v\in T}(v-\log 3,v+\log 3).
\]
Each connected component contains as many logarithms of root moduli, counted with multiplicity, as the sum of the horizontal lengths of the lower edges whose slopes belong to that component.

For \(t\ge3\), Proposition 2.10 on page 12 controls the terms to the left of the right endpoint \((a_\ell,-\log|c_\ell|)\) of a lower edge of slope \(v\).
At \(s=\log|z|>v\), the ratio of \(|c_j z^{a_j}|\) to \(|c_\ell z^{a_\ell}|\) is at most \(e^{-(a_\ell-a_j)(s-v)}\) for each \(j<\ell\), since the endpoint term is maximal at \(v\).
The positive integer gaps \(a_\ell-a_j\) are distinct, so the sum of these ratios is strictly less than \((e^{s-v}-1)^{-1}\).
Applying the same argument to \(f(1/X)\) bounds the terms on the right, as in Lemma 2.11 on page 13.
Thus at distance at least \(\log 3\) from both breakpoints of an interior interval, each tail costs strictly less than half the dominant magnitude.
On an exterior interval there is only one tail, and distance \(\log 2\) suffices for strict dominance.

On 2026-11-18 the assigned agent checked the scalar localization statement, the termwise estimate and its reversal in the [author manuscript](readme.md#edition).
The authors invoke Pellet's theorem for the multiplicity counts and compare their nearest-breakpoint estimate with Ostrowski's indexed bounds in Remark 2.6 on page 11.
The inspection covered the direct nonvanishing argument.
The multiplicity count and the optimality assertions in Example 1.7 were read at statement depth.
The coefficients in Proposition 2.10 belong to one polynomial.
Using the largest coefficient magnitude across several polynomials at each exponent requires a separate argument at the point of application.
