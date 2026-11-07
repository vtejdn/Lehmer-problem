---
author: Yin
---

<a id="san20-u001"></a>
# Integer-valued functions of bounded Fourier algebra norm

Sanders's Theorem 1.1 gives a bound uniform over all finite abelian groups on the number of signed coset indicators needed to express an integer-valued function.
The input used here is the [arXiv v5 edition](readme.md#arxiv-v5), Section 1, printed pp. 1–2.

<a id="finite-abelian-fourier-algebra-norm"></a>
## Fourier normalization

For a finite abelian group \(G\), its dual \(\widehat G\) consists of homomorphisms from \(G\) to the complex unit circle.
For \(f:G\to\mathbb C\), Sanders gives each point of \(G\) mass \(1/|G|\) and uses
\[
 \widehat f(\gamma)=\frac1{|G|}\sum_{x\in G} f(x)\overline{\gamma(x)},
 \qquad
 \|f\|_{A(G)}=\sum_{\gamma\in\widehat G}|\widehat f(\gamma)|.
\]
Thus the transform averages on \(G\) and the algebra norm sums on \(\widehat G\).

## Theorem 1.1 and its signed-sum form

Fix \(M\ge1\).
For every finite abelian \(G\) and every \(f:G\to\mathbb Z\) with \(\|f\|_{A(G)}\le M\), let \(\mathcal W(G)\) consist of all cosets of all subgroups of \(G\).
There are integers \(z(W)\) such that
\[
 f(x)=\sum_{W\in\mathcal W(G)}z(W)1_W(x)\quad(x\in G),
 \qquad
 \sum_{W\in\mathcal W(G)}|z(W)|\le \exp\!\left(M^{4+o(1)}\right).
\]
The bound depends only on \(M\), with the asymptotic exponent taken as \(M\to\infty\).
Replacing each nonzero coefficient with \(|z(W)|\) copies of \(1_W\) carrying its sign gives a signed sum of the asserted length, with repetitions allowed.
The subgroups underlying different cosets may differ.

The Fourier convention and statement were read in the [preprint](../../../literature/pdf/San20--arxiv-v5.pdf) and compared with Section 1 and Theorem 1.1 in the [published article](https://doi.org/10.1007/s00041-020-09732-y).
Theorem 1.1 is used at statement level.
Its proof and the preceding analytic and combinatorial estimates were outside this inspection.
