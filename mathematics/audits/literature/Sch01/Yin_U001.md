---
author: Yin
---

# Sch01: Integer Group-Ring Determinant Input

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: [Sch01, arXiv PDF](https://arxiv.org/pdf/math/9807032), v2 (2011-08-10), compiled 2018-10-18; 26 numbered article pages followed by two errata pages.

Source passages: The input follows from Theorem 1.21 (p. 6), Proposition 2.4 (p. 8), and Lemma 6.8 (p. 19), using residual finiteness of free groups.

Inspection: Record: 2026-09-12, the coordinating agent, selected primary statements and applicability checked; accepted external input.

<a id="sch01-u001"></a>
## Sch01-U001: Kernel-Removed Determinants and the Free-Group Specialization

Source: [Sch01, arXiv PDF](https://arxiv.org/pdf/math/9807032), v2 (2011-08-10), compiled 2018-10-18; 26 numbered article pages followed by two errata pages.
Canonical bibliographic identity is in [references.bib](../../../literature/references.bib).

Record: 2026-09-12, the coordinating agent, selected primary statements and applicability checked; accepted external input.
The original approximation proof is not independently audited.

### Exact interface and normalization

For the free group \(F_n\), any positive selfadjoint \(B\in M_m(\mathbb ZF_n)\) satisfies
\[
\int_{(0,\infty)}\log t\,dF_B(t)\geq0,\qquad
F_B(t)=(\operatorname{Tr}_m\otimes\tau)(1_{[0,t]}(B)).
\]
The matrix trace here is **unnormalized** and the integral **excludes the kernel**.
These conventions are in Definitions 1.1 and 1.3 (p. 2) and Definition 1.18 (pp. 5-6).
The input follows from Theorem 1.21 (p. 6), Proposition 2.4 (p. 8), and Lemma 6.8 (p. 19), using residual finiteness of free groups.

The appended errata (PDF pp. 27-28) restrict amenable extensions to **normal** amenable extensions.
This restriction does not remove finite groups or the residually finite case.
We do not import the original broader extension claim.

### Conversion used by MS24

For \(T\in M_m(\mathbb ZF_n)\), put \(B=T^*T\).
If \(T\) has zero kernel on \(\ell^2(F_n)^m\), its ordinary normalized Fuglede-Kadison determinant satisfies
\[
\log\Delta_{\operatorname{tr}_m\otimes\tau}(T)
=\frac{1}{2m}\int_{(0,\infty)}\log t\,dF_{T^*T}(t)\geq0.
\]
Thus \(\Delta(T)\geq1\).
The factor \(2m\) accounts for the square and trace normalization.
Kernel removal cannot be discarded when \(T\) is not injective.

This supplies the integer Haar-model determinant bound used in [MS24, Section 4](../../../literature/pdf/MS24.pdf), through [MS24-U004](../MS24/Yin_U004.md#ms24-u004).
The separate free-field realization supplies injectivity of that particular \(T\); neither the determinant theorem nor integrality alone supplies it.
Residual finiteness of free groups is a retained standard group-theoretic foundation.
No new project Claim is allocated for this specialization.

### Evidence and stopping boundary

The subsequent MS24-focused audit on 2026-09-12 gives an [explicit finite-quotient proof of the injective free-group specialization](#finite-quotient-determinant-proof), including a direct finite-permutation construction for residual finiteness, possible kernels of the finite matrices, and the order of the logarithmic cutoff limits.
That exact consumed input is now reconstructed and independently reviewed.
This does not upgrade the broader kernel-removed statement or the full Sch01 closure theorem to a full-proof audit.
The following paragraph retains the original source-access evidence.

The version header, exact definitions, Theorem 1.21, Proposition 2.4, Lemma 6.8 and appended errata were inspected in primary parsed text.
The elementary proof of Lemma 6.8 and the subgroup/inverse-limit argument in Proposition 2.4 were read; the full stability/approximation proof of Theorem 1.21 was not reviewed.

The search was triggered by MS24's reliance on a kernel-removed determinant theorem.
Queries used the title, author and "semi-integral determinant".
The arXiv record verified the publication and correction history.
Versioned PDF access and local downloads failed; the unversioned arXiv endpoint exposed the identified v2.
Screenshot requests also failed.
Therefore this is a primary statement/interface check with a disclosed rendering limitation, not a full PDF proof audit.
No local artifact was retained.
Search stopped after resolving the exact normalization and the relevance of the erratum.

## Complete retained specialization proof

The exact original 2026-09-12 proof below was retained from L_F0077 at 2026-10-21T01:19.
The original R_F0125 finding checked the complete finite-quotient argument, possible finite-matrix kernels, cutoff order and normalized conclusion at its disclosed relationship and source limits.
The general kernel-removed theorem and broader Sch01 approximation/extension proof retain the earlier unit's uninspected-proof limits.
This maintenance neither reopens the source nor performs a new mathematical review.

## Integral Free-Group Determinants by Finite Quotients

<a id="finite-quotient-determinant-proof"></a>

The exact needed input has a direct proof:

> If \(T\in M_m(\mathbb ZF_n)\), represented on \(\mathbb C^m\otimes\ell^2(F_n)\), is injective, then \(\Delta_\varphi(T)\geq1\).

This is the injective free-group specialization of [Sch01-U001](#sch01-u001).
The primary source's Lemma 6.8, p. 19, contains the finite integer characteristic-polynomial argument; Theorem 6.9, pp. 19-21, uses bounded spectral approximation.
Remark 6.10, p. 21, explicitly separates the resulting bound from convergence of determinants.
The following proof retains precisely that distinction and does not import a determinant approximation theorem.

### Finite quotients and uniform bounds

Choose finite-index normal subgroups \(N_k\lhd F_n\) with \(N_{k+1}\subseteq N_k\) and \(\bigcap_kN_k=\{e\}\), and let \(G_k=F_n/N_k\).

The finite quotients can be constructed directly.
On the finite word ball \(B_R\subset F_n\), the partial maps \(w\mapsto g_iw\), restricted to pairs whose endpoints lie in \(B_R\), are injective partial permutations.
Extend each to a permutation of \(B_R\), and use freeness to obtain a homomorphism \(F_n\to\operatorname{Sym}(B_R)\).
A reduced word of length at most \(R\) acts on \(e\) by the prescribed successive multiplications, since all intermediate suffixes lie in \(B_R\), and therefore a nonidentity such word does not fix \(e\).
Taking the intersections of the kernels of these homomorphisms for \(R\leq k\) gives the required nested family.
This also verifies directly the residual-finiteness input used in this specialization.

Let \(T_k\) be the image of \(T\) acting on \(\mathbb C^m\otimes\ell^2(G_k)\), and set
\[
B=T^*T,\qquad B_k=T_k^*T_k,\qquad d_k=m|G_k|.
\]
Every \(B_k\) is a positive semidefinite integer \(d_k\)-by-\(d_k\) matrix.
Write \(T=\sum_{g\in S}C_g\otimes\lambda(g)\) with finite \(S\) and \(C_g\in M_m(\mathbb Z)\).
Unitarity of both regular representations gives a common spectral bound
\[
\|T\|,\|T_k\|\leq\sum_{g\in S}\|C_g\|,
\qquad 0\leq B,B_k\leq K I,
\]
where \(K\geq1\) is fixed and may be chosen larger than the square of this sum.

### Spectral convergence and kernel masses

Let \(\mu\) be the probability spectral measure of \(B\) for \(\varphi\), and \(\mu_k\) the eigenvalue counting measure of \(B_k\) divided by \(d_k\).
For a fixed nonnegative integer \(r\), the group-ring matrix \(B^r\) has finite support.
Eventually no nonidentity group element in that support lies in \(N_k\), so
\[
\frac{1}{d_k}\operatorname{Tr}(B_k^r)
=\varphi(B^r)
\quad\hbox{for all sufficiently large }k.
\tag{2}
\]
Indeed the normalized trace of a finite-group regular permutation is one at the identity and zero elsewhere, exactly as for the infinite regular representation.
Polynomial approximation of continuous functions on \([0,K]\) now yields weak convergence \(\mu_k\Rightarrow\mu\).

Injectivity of \(T\) implies \(\mu(\{0\})=0\).
Put \(\alpha_k=\mu_k(\{0\})\).
Then \(\alpha_k\to0\).
For example, for each \(\delta>0\), a continuous function on \([0,K]\) that equals one at zero, decreases linearly to zero at \(\delta\), and vanishes above \(\delta\), bounds \(1_{\{0\}}\) from above.
Use weak convergence and then \(\delta\downarrow0\).
This argument needs no theorem asserting convergence of arbitrary group-ring kernel dimensions.
Some or all finite quotient matrices \(T_k\) may still be singular.

### Integer products and truncated logarithms

The product of the nonzero eigenvalues of \(B_k\) is, up to sign, the first nonzero coefficient of its integer characteristic polynomial.
Positivity makes this product a positive integer; if \(B_k=0\), the empty product is one.
Consequently
\[
J_k:=\int_{(0,K]}\log t\,d\mu_k(t)
=\frac{1}{d_k}\log\!\prod_{\lambda>0}\lambda
\geq0.
\tag{3}
\]

For fixed \(0<\varepsilon<1\), \(f_\varepsilon(t)=\log\max(t,\varepsilon)\) is continuous on \([0,K]\), and
\[
\int f_\varepsilon\,d\mu_k
=\alpha_k\log\varepsilon
  +\int_{(0,K]}\log\max(t,\varepsilon)\,d\mu_k(t)
\geq\alpha_k\log\varepsilon+J_k
\geq\alpha_k\log\varepsilon.
\tag{4}
\]
First let \(k\to\infty\).
Weak convergence and \(\alpha_k\to0\) imply
\[
\int f_\varepsilon\,d\mu\geq0
\quad\hbox{for every }0<\varepsilon<1.
\]
Next let \(\varepsilon\downarrow0\).
The functions \(\log K-f_\varepsilon\) are nonnegative and increase.
Monotone convergence gives
\[
\int\log t\,d\mu(t)
=\lim_{\varepsilon\downarrow0}\int f_\varepsilon\,d\mu
\geq0.
\]
In particular the negative logarithmic part is integrable.
By the definition of the ordinary normalized Fuglede-Kadison determinant,
\[
\log\Delta_\varphi(T)
=\frac12\int\log t\,d\mu(t)\geq0.
\tag{5}
\]

This proves the exact required lower bound.
The order of limits in (4) is essential.
Replacing \(\alpha_k\log\varepsilon\) by zero before taking \(k\to\infty\), or claiming that all \(T_k\) are invertible, would be incorrect.
Equations (2)-(5) do not assert \(J_k\to\int\log t\,d\mu(t)\), and no uniform estimate on the smallest nonzero eigenvalues is required.

### Normalization and the source erratum

Sch01 uses the unnormalized trace \(\operatorname{Tr}_m\otimes\tau\) and a logarithmic determinant that excludes the kernel.
For the present injective \(T\),
\[
\int_{(0,\infty)}\log t\,
 d[(\operatorname{Tr}_m\otimes\tau)(1_{[0,t]}(T^*T))]
=2m\log\Delta_\varphi(T).
\]
Both the square and the trace normalization are necessary.
If \(T\) has a kernel, its ordinary determinant is zero even when the kernel-removed logarithmic integral is nonnegative.
The finite-quotient proof above does not justify discarding that distinction.

Sch01's appended erratum restricts its broader amenable-extension argument to normal amenable extensions.
The proof retained here only uses finite quotient representations and the elementary truncation argument; it uses none of those extension steps.
Its conclusion is therefore unaffected by the cited erratum.
This is not an audit or repair of Sch01's entire closure theorem.
