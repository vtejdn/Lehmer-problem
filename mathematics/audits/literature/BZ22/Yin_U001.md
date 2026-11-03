---
author: Yin
---

# BZ22-U001: Brown potential and the normal-source density interface

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Online arXiv:2209.12379v2, 2025-02-04, 25-page PDF/HTML; distinct from 33-page v1 of 2022-09-26.

Passages: Introduction pp. 1-2; Theorem 2.2 p. 4; Definition 3.1/Lemma 3.2 pp. 10-12; Theorem 3.6 p. 15; Lemmas 3.7-3.10 pp. 16-18.

Inspection: 2026-09-11 selected statements and differentiated density/fixed-point chain checked; underlying Brown/free-convolution foundations accepted, not re-audited.


<a id="bz22-u001"></a>
## Selected input and original reading

This responsible source home was prepared at 2026-10-21T01:01 from the actual retained original source-reading account.
The original reading dates, exact source version, inspection depth and limitations remain those recorded below.
This maintenance did not reopen the original source, acquire bytes, perform a new source-proof review.

## Retained selected source content

<a id="bz22-density-interface"></a>
Date: 2026-09-11.
Reader: the spectral-extension research agent.
Selected source-interface audit for Yin_C_F0043, not a full-paper audit.

## Exact source and version

Hari Bercovici and Ping Zhong, *The Brown measure of a sum of two free nonselfadjoint random variables, one of which is R-diagonal*, [arXiv:2209.12379v2](https://arxiv.org/abs/2209.12379v2), 2025-02-04; [25-page PDF](https://arxiv.org/pdf/2209.12379v2), [primary HTML](https://arxiv.org/html/2209.12379v2).
The title and theorem numbering differ from the 33-page v1 of 2022-09-26.
The bibliographic key retains the first public preprint year: the arXiv record has no journal reference and the [author's research list](https://sites.google.com/view/pzhong/research) still labels the work submitted on the inspection date.
DHH+25's bibliography names v1, but its Definition 3.1 / Theorem 3.6 references match v2.
Both versioned PDFs were inspected locally to establish this distinction using temporary diagnostic copies; those inspections were not canonical literature intake.

The relevant checked units are Theorem 2.2 and its fixed-point discussion (p. 4), Definition 3.1 and Lemma 3.2 (pp. 10-12), Theorem 3.6 (p. 15), Lemma 3.8 (pp. 16-17), and Lemmas 3.9-3.10 (pp. 17-18).
The chain from Lemma 3.7's differentiated potential through the density formula and implicit differentiation was read and algebraically checked.
The underlying free convolution and Brown-potential formulas remain accepted source inputs.

## Brown Measure Convention

The inspected v2 Introduction, printed/PDF pp. 1-2, defines the Brown measure of a bounded operator \(T\) through its logarithmic potential:
\[
\mu_T=\frac1{2\pi}\Delta_\lambda\,\tau(\log|T-\lambda|),
\]
with the Laplacian interpreted in distributions.
This is the source's standard finite-tracial convention, attributed there to Brown.
The present intake checks its formulation, not Brown's original construction or priority independently.
Ordinary operator spectrum is a different object.
Yin_C_F0043 uses the established bounded inclusion of Brown support in that spectrum and separately proves equality at its stated scope.

## Accepted interface and its limit

Let bounded non-scalar \(X_1,X_2\) be free, with \(X_2\) R-diagonal.
Theorem 3.6 gives containment of the Brown support of \(X_1+X_2\) in the closure of its open subordination domain \(\Omega\), and real-analytic area density on \(\Omega\).
It does **not** claim equality of support with that closure.
Its separate Corollary 3.11 establishes positivity under an additional moment bound; that bound is unavailable when the negative second moment is infinite.

For \(\lambda\in\Omega\), write the two interior subordination values as \(ir,is\), with \(r,s>0\), and set

\[
H_1=H_{\widetilde\mu_{|X_1-\lambda|}},\quad
H_2=H_{\widetilde\mu_{|X_2|}},\quad
H_1(ir)=is,\quad H_2(is)=ir.
\]

The derivatives \(q=H_1'(ir)\), \(h=H_2'(is)\) are real, and the interior fixed-point argument gives \(|hq|<1\).
The non-automorphism assumption needed there is satisfied in Yin_C_F0043 because its step cannot be a scalar multiple of a Haar unitary.
Put

\[
\begin{aligned}
d&=|\lambda-X_1|^2,&
A&=\tau((d+r^2)^{-1}),\\
C&=\tau((d+r^2)^{-2}),&
D&=\tau((\lambda-X_1)(d+r^2)^{-2}).
\end{aligned}
\]

When \(X_1\) is normal, Lemmas 3.8-3.10 give the following exact specialization of their density formula:

\[
\pi\rho(\lambda)
=r^2C-\frac{2h|D|^2}{A^2(1-hq)},
\qquad
q=\frac{2C}{A^2}-\frac1{r^2A}-1,
\qquad
A=\frac1{r(r+s)}.
\tag{B1}
\]

The sign in front of the second term is negative.
This follows by substituting \(\omega_1=ir\) in the source's formula, rather than guessing a sign from positivity.
The two resolvent factors in Lemma 3.8 coincide exactly because \(X_1\) is normal.
Normality cannot be silently dropped from (B1).

Formula (B1), support containment, and the interior fixed-point facts are the external inputs consumed by the linked C_F0043 proof.
The extra positivity argument for normal \(X_1\) is written explicitly in Yin_C_F0043 proof version 2; it is a project deduction and is not attributed to Theorem 3.6.
KPZ26's announced forthcoming stronger perturbation theorem is not consumed.
