---
author: Yin
---

<a id="mpv98-u002"></a>
<a id="unrestricted-cyclotomic-products"></a>
# Counting unrestricted products of cyclotomic polynomials

In §3.2, Mossinghoff, Pinner and Vaaler write \(c(n)\) for the number of products of monic cyclotomic polynomials of exact degree \(n\), with \(c(0)=1\).
Their Euler product, given in the proof of Lemma 3.3, is
\[
  \sum_{n\ge0}c(n)e^{-nz}
    =\prod_{m\ge1}(1-e^{-\varphi(m)z})^{-1},
  \qquad \operatorname{Re}z>0.
\]
Each indexed factor permits arbitrary nonnegative multiplicity of \(\Phi_m\), including \(m=1,2\).
Unique factorization therefore counts each monic product once, with nonzero constant term.

Immediately after (3.12) the authors attribute to Boyd and Montgomery the estimate
\[
  c(n)=A\,\frac{\exp(B\sqrt n)}{n\sqrt{\log n}}\!
       \left(1+O\!\left(\frac{\log\log n}{\log n}\right)\right),
  \qquad
  A=\frac{\sqrt{105\zeta(3)e^{-\gamma}}}{4\pi^2},
  \qquad B=\frac{\sqrt{105\zeta(3)}}{\pi},
\]
as \(n\to\infty\), where \(\gamma\) is Euler's constant.
The nearby Theorem 3.2 concerns a different sequence \(r_2(n)\), restricted to reciprocal products of degree \(2n\) with multiplicities at most two.

The counting definition, asymptotic, constants and product were read from the rendered [author version](../../../literature/pdf/MPV98--author-ps.pdf), pp. 9–10, and compared with the indexed text of the [published article](https://doi.org/10.1090/S0025-5718-98-01007-2), pp. 1715–1716.
This checks the statement as reported in MPV98.
The [original Boyd–Montgomery chapter](https://doi.org/10.1515/9783110848632-004) and its proof were unavailable for direct inspection.
