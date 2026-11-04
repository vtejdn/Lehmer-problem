---
author: Yin
---

# MS24: Determinant and Capacity Conventions

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained arXiv:2406.15922v1, 19 pages; margin date 2024-06-22 and distinct title-page date 2024-06-25.

Passages: [MS24 PDF](../../../literature/pdf/MS24.pdf), Definitions 1.1, 2.1 and 2.5, Remarks 2.2/2.6, Propositions 2.3--2.10, printed/PDF pp. 3--9.

Inspection: 2026-09-12, assigned MS24 reviewer.
Definitions and local formulas were directly checked; external proof boundaries are collected in [U005](Yin_U005.md#ms24-u005).

## MS24-U001

<a id="determinant-convention"></a>
### The Ambient Algebra and Determinant

Let M be a finite von Neumann algebra with faithful normal tracial state tau.
For T in M, put |T|=(T* T)^(1/2) and let mu_|T| be its spectral probability distribution.
The ordinary Fuglede-Kadison determinant is

\[
\Delta_\tau(T)=\exp\left(\int_{[0,\infty)}\log t\,d\mu_{|T|}(t)\right),
\qquad \log 0=-\infty,\quad \exp(-\infty)=0.
\]

For matrices over M use the state tr_m tensor tau, where tr_m=Tr_m/m and Tr_m is the ordinary, unnormalized matrix trace.
In particular,

\[
\Delta(b\otimes 1)=|\det b|^{1/m},
\qquad b\in M_m(\mathbb C).
\]

Thus this determinant is a nonnegative real number, not a determinant with entries in M.
Its logarithm includes a zero atom: nonzero kernel forces Delta=0.
Conversely Delta>0 implies injectivity and affiliated invertibility in the finite algebra, but injectivity alone does not give Delta>0 for an arbitrary bounded operator.
MS24's equivalence concerns its particular semicircular linear models.

The scalar variables s_1,...,s_n in the paper are freely independent **standard** semicircular elements, each with mean zero, variance one and density (2 pi)^(-1) sqrt(4-t^2) on [-2,2].
They are selfadjoint elements of M.
The matrices a_i need not be selfadjoint.
The notation S=sum_i a_i tensor s_i always denotes a bounded operator in M_m(M); only when all a_i=a_i* is it an operator-valued semicircular element in the usual selfadjoint sense.
The source explicitly extends this name to its nonselfadjoint linear models.

### Determinant Facts Actually Used

Proposition 2.3 supplies multiplicativity for all bounded factors, equality Delta(T*)=Delta(T), Delta(P)<=tau(P) for P>=0, compatibility with trace-preserving amplification, and

\[
\Delta\begin{pmatrix}T_1&0\\0&T_2\end{pmatrix}
=\Delta\begin{pmatrix}0&T_1\\T_2&0\end{pmatrix}
=\Delta(T_1)^{1/2}\Delta(T_2)^{1/2}.
\]

The block matrices use the normalized trace tr_2 tensor tau.
The initial review accepted multiplicativity through HS07.
The later [analytic dependency review](../../../ledger/Yin_L_F0002_v1.md) checks the original FK52 bounded multiplicativity proof and its analytic extension, including zero determinants, and explains the finite tracial scope used here.
MS24's main proofs only multiply by bounded invertible matrix factors; they do not require the affiliated extension.
The remaining formulas follow directly from spectral distributions, polar decomposition and integration of log.
The geometric/arithmetic mean bound follows from scalar Jensen after replacing P by P+epsilon and passing down to the limit.
For a standard semicircular s, direct integration of its absolute-value density gives

\[
\log\Delta(s)=\frac1\pi\int_0^2\log t\sqrt{4-t^2}\,dt=-\frac12.
\]

The ordinary determinant is upper semicontinuous along positive operators whose distributions converge and whose norms have a common finite bound K.
Indeed use the continuous functions log(max(t,epsilon)) on [0,K]: the integral of log is their decreasing infimum, so the limiting integral is at least the limsup of the integrals.
This argument also permits zero kernels/zero determinants.
It verifies the needed version of Proposition 2.4 directly and does not require the source's kernel-removing determinant convention.
The printed hypothesis “sup_n ||T_n|| <= infinity” must be replaced by a **finite** bound in this application.

<a id="capacity-and-scaling"></a>
### Positive Maps, Capacity and Scaling

For a positive linear map eta:M_m(C)->M_m(C),

\[
\operatorname{cap}(\eta)
=\inf_{b>0,\ \det b=1}\det\eta(b)
=\inf_{b>0}\frac{\det\eta(b)}{\det b}.
\]

Here b>0 means positive definite; b>=0 means positive semidefinite.
Complete positivity means positivity of every matrix amplification.
The adjoint eta* is the Hilbert-Schmidt adjoint for the inner product tr_m(x y*).
The source definitions are:

- rank non-decreasing: rank eta(b)>=rank b for every b>=0;
- indecomposable: rank eta(b)>rank b whenever 1<=rank b<m;
- strictly positive: eta(b)>=alpha tr_m(b)I for some alpha>0 and all b>=0;
- doubly stochastic: eta(I)=eta*(I)=I.

Strict positivity implies indecomposability.
For m>=2, indecomposability also implies eta(I)>0: a kernel vector of eta(I) would be in the kernel of eta(b) for every 0<=b<=I, contradicting the test on a rank m-1 projection.
At m=1 the indecomposability condition is empty, including eta=0; use cap(eta)>0 for any normalization involving eta(c)^(-1/2).
This corrects the scalar boundary of Remark 2.6(iii)/Proposition 2.8 without changing the main determinant theorem.

The Gur04 inputs are: rank non-decreasing iff cap>0; an indecomposable map has a unique positive det-one capacity minimizer, and a positive attained capacity yields a doubly stochastic scaling.
The exact formulations, including the scalar boundary, are retained in the [Gur04 review](../Gur04/readme.md).

MS24 defines

\[
\eta_{c_1,c_2}(b)=c_1\eta(c_2^*bc_2)c_1^*,
\qquad
(\eta_{c_1,c_2})^*=(\eta^*)_{c_2,c_1}.
\]

For invertible c_1,c_2, substitution in the defining infimum gives

\[
\operatorname{cap}(\eta_{c_1,c_2})
=|\det c_1|^2|\det c_2|^2\operatorname{cap}(\eta).
\]

In particular, if c>0 and eta(c)>0, the normalized map

\[
\widetilde\eta=\eta_{\eta(c)^{-1/2},c^{1/2}}
\]

satisfies

\[
\widetilde\eta(I)=I,\qquad
\widetilde\eta^*(I)=c^{1/2}\eta^*(\eta(c)^{-1})c^{1/2}.
\]

The second equality need not equal I for an arbitrary c.
For eta(b)=tr_2(b)I and c=diag(2,1), it equals diag(4/3,2/3).
This directly disproves the starred “automatically” sentence following Proposition 2.8.
For an actual positive capacity minimizer it equals I, as required later.

### Approximation and Order

The source uses the **unnormalized** trace in

\[
\operatorname{ds}(\eta)
=\operatorname{Tr}_m((\eta(I)-I)^2)
 +\operatorname{Tr}_m((\eta^*(I)-I)^2).
\]

If eta is completely positive with cap(eta)>0, 0<delta<=1/6, and

\[
\operatorname{cap}(\eta)\ge e^{-\delta}
       \frac{\det\eta(c)}{\det c},
\]

then Proposition 2.10, importing the expanded GGOW Lemma 3.10, gives ds(tilde eta)<=6 delta.
The matrix eta(c)>0 follows from the positive-capacity hypothesis.
The expression Tr_m((c eta*(eta(c)^(-1))-I)^2) in the source is legitimate: its argument is similar to the Hermitian matrix tilde eta*(I)-I, hence their squared traces agree.
Do not silently replace that non-Hermitian square by A* A.

For positive eta_1>=eta_0, Proposition 2.9 gives cap(eta_1)>=cap(eta_0) and the stronger superadditivity of cap^(1/m).
The stronger statement applies the finite-dimensional Minkowski determinant inequality pointwise and then takes an infimum; that classical inequality is retained as the named external finite-dimensional input, not independently re-audited here.
The main theorem uses only monotonicity, which follows directly from determinant monotonicity on positive matrices (regularize singular matrices if necessary).

<a id="distribution-and-positivity"></a>
### Distribution and positivity terminology

In Definition 2.1's finite tracial setting, the distribution of a bounded selfadjoint T is the probability measure mu_T given by mu_T(E)=tau(1_E(T)) for Borel sets E in R.
For a general bounded T, the ordinary determinant above uses the distribution of the positive operator |T|, not a scalar spectral law of T itself.
For Definition 1.1, a linear map eta:M_m(C)->M_m(C) is positive when eta(b)>=0 for every b>=0.
Complete positivity tests every finite matrix amplification and is stronger.
The optimization domain b>0 consists of positive definite matrices, so their inverses are bounded; this does not supply bounded invertibility of arbitrary affiliated evaluations.
These are the source meanings retained by the selected definition reading and existing audit, rather than new conclusions about a nonselfadjoint spectral distribution.
