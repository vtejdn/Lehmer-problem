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

<a id="near-integer-iteration"></a>
## The nearby integer function in Lemma 10.2

Section 9 of the [same preprint](readme.md#arxiv-v5), printed p. 38, defines \(f_{\mathbb Z}\) by \(\|f-f_{\mathbb Z}\|_\infty\le\epsilon<1/2\), which determines the integer function uniquely.
Lemma 10.2 on printed pp. 43–44 applies to \(f\in A(G)\) with this approximation, \(f_{\mathbb Z}\ne0\), \(\|f\|_A\le M\), \(M\ge1\), and \(\epsilon\le\min(e^{-C M},1/8)\) for the absolute constant in the lemma.
For each \(0<\eta\le1/4\) it supplies a function \(g\) within \(\epsilon+\eta\) of an integer linear combination of cosets of one subgroup.
The sum of absolute coefficients of that combination is bounded in terms of \(M,\eta\) alone, and \(\|f-g\|_A\le\|f\|_A-1+\epsilon+\eta\).
The same statement appears on p. 51 of the [published article](https://doi.org/10.1007/s00041-020-09732-y).
Both editions print an integer codomain for \(f\) in Theorem 10.1, while Lemma 10.2 explicitly allows the near-integer input needed here.
The [odd-grid application](../../../ledger/Yin_L_G0464_v7.md#rounding) uses the lemma at statement level and gives its own finite iteration.
This inspection covers the convention and the stated input and output of the lemma, without an audit of its proof.
