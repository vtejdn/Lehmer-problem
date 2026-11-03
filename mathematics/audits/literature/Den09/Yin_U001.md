---
author: Yin
---

<a id="den09-u001"></a>
# Den09-U001: Mahler measure as a Fuglede--Kadison determinant

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Den09, [retained PDF](../../../literature/pdf/Den09.pdf), Christopher Deninger, *Mahler measures and Fuglede--Kadison determinants*, arXiv:0905.0604v1, 5 May 2009, 25 PDF pages. This review belongs to v1, not automatically to the later journal typesetting.

Passages: Section 1, pp.1--2; the complete group-algebra/Fourier interpretation on pp.4--5 in Section 2; normalization checks against pp.10--11,15,18. These are the preprint's own page numbers, equal to PDF page numbers.

Inspection: 2026-10-06, human author Yin; prepared by an assigned AI source-review agent, with direct source reading and self-check of this record. The agent read the full 25-page artifact; Sections 2--4 are recorded separately in U002. Rendered pp.1--2 were inspected for the height assertion and determinant definition. No independent human review, formal verification or recursive review of cited foundational proofs is asserted.


## Assessment

**Audited within scope** for the definitions, trace/Fourier normalization and the passage from spectral regularization to the Mahler identity.
General Fuglede--Kadison multiplicativity and Fourier identification are retained standard external inputs at the precise interfaces below, not original proofs independently rechecked.
**Questioned** for the literal normalized-height sentence on p.1; it is missing the degree factor under the usual absolute logarithmic Weil-height convention.

This unit supports [Den09-U002](Yin_U002.md#den09-u002).
It creates no project Claim or Task.
Broad applications named in the introduction, including entropy and Lyapunov formulas, are pointers rather than audited consequences here.

<a id="mahler-measure"></a>
## Mahler conventions and singularities

For $P\in L^\infty(\mathbb T^d,\mu)$ with normalized Haar probability $\mu$,

$$
m(P)=\int_{\mathbb T^d}\log|P|\,d\mu\in\mathbb R\cup\{-\infty\},
\qquad M(P)=\exp m(P)\in[0,\infty).
$$

The logarithm is natural, $\log0=-\infty$, and $\exp(-\infty)=0$.
Essential boundedness bounds the positive part of $\log|P|$, so the extended integral is unambiguous.
No principal-value convention or exclusion of zeros is used.
A nonzero Laurent polynomial has integrable logarithm and therefore positive Mahler measure; this familiar analytic fact is stated but not proved in Section 1 and is retained as a standard input.
It does not extend to every nonzero bounded measurable function.

In one variable, Jensen's formula gives, for $P(z)=a\prod_{j=1}^n(z-\alpha_j)$,

$$
m(P)=\log|a|+\sum_{j=1}^n\log\max\{1,|\alpha_j|\}.
$$

Multiplication by a Laurent monomial does not change $M$, since its absolute value is one on the torus.
Unit-circle zeros are allowed in this formula.
For example, $M(1-z)=1$ although $1-z$ is not bounded away from zero.
In contrast, a bounded function that vanishes on a set of positive Haar measure has $M=0$; even an almost-everywhere positive function can have $M=0$ if its negative logarithm is not integrable.

<a id="fk-determinant"></a>
## Determinant, trace and regularization

Let $\mathcal N$ be a nonzero finite von Neumann algebra, equipped with a faithful normal finite trace $\tau$, and let $A\in\mathcal N$ be bounded.
Put $|A|=(A^*A)^{1/2}$.
For invertible $A$,

$$
\Delta_\tau(A)=\exp\tau(\log|A|).
$$

For arbitrary $A$ the source defines the **unmodified** determinant

$$
\Delta_\tau(A)=\lim_{\varepsilon\downarrow0}
\exp\tau\bigl(\log(|A|+\varepsilon I)\bigr).
$$

Writing $\nu_A(B)=\tau(1_B(|A|))$, spectral calculus and monotone convergence give

$$
\log\Delta_\tau(A)=\int_{[0,\|A\|]}\log t\,d\nu_A(t).
$$

For the monotone-convergence step, subtract the logarithms from a common finite upper bound before applying the theorem; the functions need not be nonnegative themselves.
This interpretation covers $-\infty$.
Equivalently,

$$
\log\Delta_\tau(A)=\frac12\lim_{\varepsilon\downarrow0}
\tau\bigl(\log(A^*A+\varepsilon I)\bigr).
$$

The two regularizations have the same spectral limit; their finite-$\varepsilon$ expressions are not asserted equal.
The factor $1/2$ is necessary when using $\log|A|^2$ or $\log(A^*A)$.

The trace in Section 1 need not have mass one: scaling it to $c\tau$ raises the determinant to the power $c$.
All subsequent group-algebra formulas use the canonical trace with $\tau(I)=1$.
In particular, for $A\in M_n(\mathbb C)$ and $\tau=\operatorname{Tr}/n$,

$$\Delta_\tau(A)=|\det A|^{1/n},$$

including zero for singular matrices.
With the unnormalized matrix trace the exponent $1/n$ is absent.
Invertibility implies positive determinant; positive determinant does not imply bounded invertibility.
A nonzero kernel has positive spectral mass at zero by faithfulness and forces determinant zero, but injectivity alone does not imply positive determinant.
For instance, multiplication by $P(e^{i\theta})=e^{-1/|\theta|}$ for $0<|\theta|\le\pi$ is bounded and injective on $L^2(\mathbb T)$, while its logarithmic integral is $-\infty$.

The source retains multiplicativity $\Delta_\tau(AB)=\Delta_\tau(A)\Delta_\tau(B)$ for bounded elements of a finite von Neumann algebra.
Its original Fuglede--Kadison proof is outside this inspection.
In particular,

$$\Delta_\tau(A^*A)=\Delta_\tau(A)^2,$$

not $2\Delta_\tau(A)$.
Source v1 has that latter typo in the proof of Theorem 17, treated in U002.

<a id="group-fourier-convention"></a>
## Group algebra and the exact Mahler interface

For a discrete group $\Gamma$, the source uses the algebra of bounded **left-$\Gamma$-equivariant** operators on $\ell^2\Gamma$.
If $R_\gamma x=x\gamma$, its embedding of the Banach convolution $*$-algebra is

$$
r:\ell^1\Gamma\longrightarrow\mathcal N\Gamma,
\qquad r(f)=\sum_{\gamma\in\Gamma} f_\gamma R_{\gamma^{-1}},
\qquad \|r(f)\|\le\|f\|_1,
$$

with $f^*=\sum_\gamma\overline{f_\gamma}\gamma^{-1}$.
The canonical trace is

$$\tau_\Gamma(A)=\langle A\delta_e,\delta_e\rangle,\qquad
\tau_\Gamma(r(f))=f_e.$$

The inverse in $R_{\gamma^{-1}}$ makes $r$ a homomorphism rather than an antihomomorphism.
The map $f\mapsto\widetilde f=\sum_\gamma f_\gamma\gamma^{-1}$ used later in the paper does **not** conjugate coefficients and must not be confused with $f^*$.

For abelian $\Gamma$ with dual $\widehat\Gamma$, the Fourier transform

$$\mathcal Ff(\chi)=\sum_\gamma f_\gamma\chi(\gamma)$$

identifies $\mathcal N\Gamma$ with multiplication by $L^\infty(\widehat\Gamma,\mu)$ functions.
Write $\widehat A=\mathcal F(A\delta_e)$ for the operator's symbol.
On group-algebra elements this is $\widehat{r(f)}(\chi)=\mathcal Ff(\chi^{-1})$, not generally $\mathcal Ff(\chi)$.
Haar measure is invariant under $\chi\mapsto\chi^{-1}$, so either polynomial convention gives the same Mahler measure.

The inspected argument first checks $\mathcal F(Af)=\mathcal Ff\,\mathcal F(A\delta_e)$ on the dense group algebra, and then obtains

$$\tau_\Gamma(A)=\int_{\widehat\Gamma}\widehat A\,d\mu.$$

Functional calculus sends $|A|+\varepsilon I$ to $|\widehat A|+\varepsilon$, and the preceding spectral/monotone argument yields

$$
\Delta_{\mathcal N\Gamma}(A)
=\exp\int_{\widehat\Gamma}\log|\widehat A|\,d\mu.
$$

Thus for $\Gamma=\mathbb Z^d$ the source's equation (1) is exactly

$$\Delta_{\mathcal N\mathbb Z^d}(A)=M(\widehat A).$$

It applies to every bounded $A$ in the group von Neumann algebra, including those with zero determinant.
Its specialization to Laurent polynomials does not require nonvanishing on the torus.
It supplies no scalar Mahler polynomial for an arbitrary nonabelian group element; the determinant remains the applicable noncommutative object.

<a id="height-normalization-finding"></a>
## Finding P2: the normalized Weil height needs division by degree

**Source-existing normalization error, first recorded here on 2026-10-06:** Section 1, p.1, says $m(P)$ is the normalized Weil height of an algebraic integer $\alpha$ with monic minimal polynomial $P$.
Under the standard absolute logarithmic convention, if $d=[\mathbb Q(\alpha):\mathbb Q]$,

$$h(\alpha)=\frac1d\sum_{\sigma:\mathbb Q(\alpha)\hookrightarrow\mathbb C}
\log\max\{1,|\sigma(\alpha)|\}=\frac{m(P)}d.$$

The finite-place terms vanish because $\alpha$ is integral.
For $\alpha=\sqrt2$, $P=X^2-2$ has $m(P)=\log2$, while $h(\sqrt2)=\tfrac12\log2$.
This directly reproduces the discrepancy.
Either replace the sentence with $m(P)=d\,h(\alpha)$ or explicitly name an unnormalized height.
The determinant/Mahler identity and the approximation theorems do not use this sentence and remain unaffected.
No transfer of the error assessment to uninspected source versions is made.

## Dependencies and limits

The original proofs of Fuglede--Kadison multiplicativity [FK52], the standard Fourier/von Neumann identification and nonzero Laurent-polynomial logarithmic integrability were not recursively audited.
The Fourier trace computation, regularization passage, one-variable normalization test and finite-matrix specialization above were directly checked.
Section 1's cited entropy, torsion, invariant-subspace and Lyapunov applications remain outside this unit's proof coverage.
No whole-literature errata search or present-day research-status conclusion is asserted.
