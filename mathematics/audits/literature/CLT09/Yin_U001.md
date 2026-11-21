---
author: Yin
---

# Global heights of generic small points for a second metrized line bundle

<a id="clt09-u001"></a>
<a id="integrable-metrics"></a>
## Admissible metrics and the normalization of height

Chambert-Loir and Thuillier work on an integral projective scheme \(X\) over a number field \(F\).
A metrized line bundle is admissible, in their terminology, if it is a quotient of two adelically semipositively metrized line bundles.
Zhang calls such a metrized line bundle integrable.
For an algebraic point \(x\), the height is the intersection height of its closed point divided by the degree of that point.
For the whole variety, write \(h_{\bar L}(X)=(\widehat c_1(\bar L)^{d+1}\mid X)\), where \(d=\dim X\). [Edition](readme.md#edition) · [Point heights, printed page 978](../../../literature/pdf/CLT09.pdf#page=3) · [Admissible metrics, printed page 987](../../../literature/pdf/CLT09.pdf#page=12)

<a id="height-convergence"></a>
## Lemme 6.1

Let \(d\ge1\), and let \(L\) be ample with a semipositive adelic metric.
Put \(V=(c_1(L)^d\mid X)\) and \(s=h_{\bar L}(X)/((d+1)V)\).
Suppose that \((x_n)\) is generic and \(h_{\bar L}(x_n)\to s\).
Genericity requires each proper geometric closed subvariety to contain only finitely many terms.
For every admissibly metrized line bundle \(\bar M\), the lemma gives
\[
 \lim_{n\to\infty} h_{\bar M}(x_n)
 =\frac{(\widehat c_1(\bar L)^d\widehat c_1(\bar M)\mid X)
       -d\,s\,(c_1(L)^{d-1}c_1(M)\mid X)}{V}.
\]
The proof obtains the lower bound from the arithmetic volume of \(L^{\otimes t}\otimes M\) and applies it to the inverse of \(\bar M\) for the upper bound.
The equality involving the height of an effective divisor in Théorème 1.2(b) is a separate hypothesis for local logarithmic test functions.
The inspected global-height lemma assumes no section of \(M\).
This inspection checked the statement, the normalizations and the passage from the lower bound to convergence, and accepts the arithmetic-volume input as stated. [Hypotheses of Théorèmes 1.1–1.2, printed pages 979–980](../../../literature/pdf/CLT09.pdf#page=4) · [Lemme 6.1 and its proof, printed pages 1002–1003](../../../literature/pdf/CLT09.pdf#page=27)
