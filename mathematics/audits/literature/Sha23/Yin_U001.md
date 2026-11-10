---
author: Yin
---

<a id="sha23-u001"></a>
# Sha23-U001: Rouché's theorem on a disk, with multiplicity

## Source and actual reading

Use the [May 14, 2023 Princeton notes](readme.md).
On 2026-11-10 the assigned AI read the exact statement of Corollary 7.44 on printed/PDF page 83 and its short proof on pages 83--84, together with Theorem 7.43 on page 81 and its explicit zero/pole order convention.
Those three pages were also visually checked in the retained original.
The argument principle is accepted as a standard input at the displayed statement; its underlying residue-theorem proof and the rest of the lecture notes were not audited.
This is ordinary source Preparation, not an independent review of a project argument.
The existing Ope26c-U003 Taylor/Rouché application was checked as a reuse lead, but it did not supply this general source statement.

<a id="rouche-disk"></a>
## Accepted disk statement and normalization

Let \(z_0\in\mathbb C\), \(r>0\), and
\[
D=\{z:|z-z_0|<r\}.
\]
Suppose \(f,h\) are holomorphic on an open set containing \(\overline D\), and
\[
|h(z)|<|f(z)|\qquad(z\in\partial D).
\tag{1}
\]
Then \(f\) and \(f+h\) have the same number of zeros in \(D\), including multiplicities.

Here the zero count means
\[
N_D(F)=\sum_{\substack{\alpha\in D\\F(\alpha)=0}}\operatorname{ord}_{\alpha}(F),
\]
where the order is the least exponent with nonzero coefficient in the local Taylor expansion.
The strict boundary inequality ensures that neither function is zero on \(\partial D\), and that neither is identically zero on the disk component.
The counts are finite.
The conclusion concerns the open disk; zeros on its boundary are excluded by the hypotheses.

Corollary 7.44 writes the comparison as \(|g-f|<|f|\) for two holomorphic functions \(f,g\).
Taking \(g=f+h\) gives exactly (1).
Its proof invokes Theorem 7.43, whose page-81 statement explicitly counts a zero or pole by its order, so the multiplicity convention is part of this source use.

The short proof was checked at that dependency depth.
For \(0\le t\le1\), \(f+th\) stays nonzero on the circle because \(|f+th|\ge|f|-|h|>0\).
The argument-principle integral of \((f+th)'/(f+th)\), divided by \(2\pi i\), is therefore a continuous integer-valued function of \(t\), and is constant.
This is the source's homotopy argument, not a new project proof.

No statement with a nonstrict inequality, a boundary zero, or a merely approximate boundary comparison is adopted.
For an application to an explicit polynomial, the actual comparison functions, disk and strict inequality remain the consumer's obligations.
This unit performs no development or checking of \(z^m a+a^\#\), no Mahler calculation, and no theorem about its exterior roots.
