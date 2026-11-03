---
author: Yin
---

# MS24: Moments, Hermitization and Scaling

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained arXiv:2406.15922v1, 19 pages; margin date 2024-06-22 and distinct title-page date 2024-06-25.

Passages: Source: [MS24 PDF](../../../literature/pdf/MS24.pdf), Propositions 3.2-3.3, Lemma 3.5 and Remark 3.6, printed/PDF pp. 10-12; conventions from [U001](Yin_U001.md#ms24-u001).

Inspection: Date/reviewer: 2026-09-12, assigned MS24 reviewer.


The registered artifact and acquisition record retain both dates.

## MS24-U002

Source: [MS24 PDF](../../../literature/pdf/MS24.pdf), Propositions 3.2-3.3, Lemma 3.5 and Remark 3.6, printed/PDF pp. 10-12; conventions from [U001](Yin_U001.md#ms24-u001).
Date/reviewer: 2026-09-12, assigned MS24 reviewer.
The complete local pairing and block-matrix arguments were reconstructed; the source p. 12 formulas were inspected visually.
The MS17 moment convention and norm passage were checked in the local primary book.

### Covariance and Hermitization

Let S=sum_i a_i tensor s_i in M_m(M), with the standard free semicircular family and arbitrary complex coefficient matrices from U001.
With E=id tensor tau,

\[
\eta(b)=E[SbS^*]=\sum_i a_i b a_i^*,
\qquad
\eta^*(b)=E[S^*bS]=\sum_i a_i^*b a_i.
\]

This is a covariance **pair** in the nonselfadjoint case, not the assertion that its full operator-valued star-distribution is determined by eta alone.

The hermitization H=S^h is the selfadjoint element

\[
H=\begin{pmatrix}0&S\\S^*&0\end{pmatrix}
=\sum_i\begin{pmatrix}0&a_i\\a_i^*&0\end{pmatrix}\otimes s_i
\in M_{2m}(M).
\]

If rho(b)=sum_i a_i b a_i, then direct block multiplication gives

\[
\eta^h
\begin{pmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{pmatrix}
=
\begin{pmatrix}
\eta(b_{22})&\rho(b_{21})\\
\rho^*(b_{12})&\eta^*(b_{11})
\end{pmatrix}.
\]

Here rho* is the Hilbert-Schmidt adjoint, namely sum_i a_i* b a_i*.
The map eta^h is completely positive and self-dual.
The normalized block determinant formula gives Delta(H)=Delta(S), including zero values.
Also ||H||=||S|| and

\[
\eta^h(I_{2m})=\operatorname{diag}(\eta(I_m),\eta^*(I_m)),
\qquad
\operatorname{ds}(\eta^h)=2\operatorname{ds}(\eta).
\]

The factor two uses Tr_(2m), not tr_(2m).

### Corrected Arbitrary Scaling Formula

For c_1,c_2 in M_m(C) and S'=(c_1 tensor 1)S(c_2 tensor 1), multiplicativity gives

\[
\Delta(S')=|\det c_1|^{1/m}|\det c_2|^{1/m}\Delta(S).
\]

The associated covariance pair is

\[
\eta'(b)=c_1\eta(c_2bc_2^*)c_1^*
       =\eta_{c_1,c_2^*}(b),
\quad
(\eta')^*(b)=c_2^*\eta^*(c_1^*bc_1)c_2
       =(\eta^*)_{c_2^*,c_1}(b).
\]

Lemma 3.5(i) prints eta_(c1,c2) and (eta*)_(c2,c1) instead.
Those formulas match coefficients c_1 a_i c_2* under the source's scaling definition.
Both versions coincide for the positive c_1,c_2 actually used in Sections 3-4; all determinant factors are correct even for arbitrary c_1,c_2.
No nonsingular hypothesis is needed for this determinant identity.

### Pairing Estimates

For a selfadjoint matrix-valued semicircular H with covariance theta, the operator-valued moment-cumulant rule gives

\[
E[H^{2k}]=\sum_{\pi\in NC_2(2k)}\kappa_\pi,\qquad E[H^{2k+1}]=0,
\]

where kappa_pi is obtained by nesting theta along the noncrossing pairing.
The input and nesting convention are directly checked in MS17, Chapter 9, Definition 7 and equation (9.16), printed p. 236/PDF p. 245; the norm calculation appears after equation (9.5), printed p. 231/PDF p. 240.

Each nested k-pair term with inserted matrices b_0,...,b_(2k) has norm at most ||theta||^k times the product of their norms.
Remove an adjacent pair from pi, replace the resulting theta(I) insertion by I+(theta(I)-I), and use this multilinear bound.
Induction gives

\[
\|\kappa_\pi-I\|
\le\left(\sum_{j=0}^{k-1}\|\theta\|^j\right)\|\theta(I)-I\|.
\]

There are C_k pairings, where C_k=(k+1)^(-1) binom(2k,k).
Taking the normalized trace proves Proposition 3.3:

\[
\left|(\operatorname{tr}\otimes\tau)(H^{2k})-C_k\right|
\le C_k\left(\sum_{j=0}^{k-1}\|\theta\|^j\right)\|\theta(I)-I\|.
\]

Odd moments vanish.
If theta(I)=I, every nested term is I and H has precisely the standard semicircular distribution (Proposition 3.2).
In the original selfadjoint coefficient case eta=eta*, so eta(I)=I already is double stochasticity.
In the general case both eta(I)=I and eta*(I)=I make the hermitization standard semicircular; its determinant is e^(-1/2).

The same pairing bound gives ||E[H^(2k)]||<=C_k||theta||^k.
Faithfulness of the trace identifies the spectral support with the operator spectrum, so

\[
\|H\|\le 2\|\theta\|^{1/2}.
\]

For a positive map theta, ||theta||=||theta(I)||.
Consequently theta_j(I)->I supplies both convergence of every scalar moment to the semicircular moments and a uniform norm bound for H_j.
This is the precise approximate input used in [U003](Yin_U003.md#ms24-u003); the covariance maps themselves need not converge to a fixed map.
