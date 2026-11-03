---
author: Yin
---

# MS24: Analytic Dependency Review

<a id="ms24-analytic-dependencies"></a>

Date/reviewer: 2026-09-12, independent analytic-dependency reviewer.
This supplement checks the analytic inputs actually consumed by [MS24-U001](../audits/literature/MS24/Yin_U001.md#ms24-u001), [U002](../audits/literature/MS24/Yin_U002.md#ms24-u002) and [U003](../audits/literature/MS24/Yin_U003.md#ms24-u003).
It adds evidence to those units without allocating another U or C identifier.
The MS24 version is arXiv 2406.15922v1, printed/PDF pp. 1-19.

The original coordinating-agent second check is retained in [R8](../audits/reviews/Yin_R_F0008_v2.md#ms24-analytic-dependency-second-finding), with its exact primary-page and proof-scope limits.

The required analytic chain is resolved at the scope below.
In particular, the proof uses the ordinary Fuglede-Kadison determinant of bounded operators, including its zero values.
It does not require an unbounded multiplicativity theorem, a kernel-omitting determinant, or a general theorem on continuity of operator-valued semicircular distributions.
Functional calculus, finite polar decomposition, the scalar free semicircular moment rule and polynomial approximation on a compact interval remain ordinary foundational inputs; this is not a re-audit of their original constructions.

Current complete source-proof homes, 2026-10-21: [FK52-U001](../audits/literature/FK52/Yin_U001.md#fk52-u001), [MS24-U005 v2](../audits/literature/MS24/Yin_U005.md#retained-analytic-proof-interfaces), the sufficient existing [MS24-U002 pairing proof](../audits/literature/MS24/Yin_U002.md#pairing-estimates), and [MS17-U001 v2](../audits/literature/MS17/Yin_U001.md#semicircular-source-passages-and-the-offline-affine-input).
The original text remains the exact fixed input of older R_F0074/R_F0001/R_F0111; its offline extension scope and source limits are unchanged.

## Evidence and Minimal Interfaces

| Input | Primary passage checked | Exact use and review depth |
| --- | --- | --- |
| Bounded determinant multiplicativity | FK52, definition p. 521/PDF 2, Theorem 1 and Lemmas 2-3 pp. 522-524/PDF 3-5; Lemma 5 and the following unnumbered argument pp. 528-529/PDF 9-10 | Selected proofs read and reconstructed. The necessary case is multiplication on either side by invertible elements of the finite-dimensional coefficient algebra. The source's stronger bounded, possibly singular product identity also passes this review. |
| Relationship to the previously retained unbounded source | [HS07 author version](../literature/pdf/HS07--author.pdf), Definition 2.1 p. 3, Lemma 2.4 pp. 5-7 and Proposition 2.5 p. 7 | These passages explicitly retain bounded multiplicativity from Fuglede-Kadison. They are not an independent foundation for that bounded theorem. The new direct FK52 check removes this extra layer for the MS24 proof. |
| Hermitization and normalization | [MS24](../literature/pdf/MS24.pdf), Proposition 2.3 and Lemma 3.5(ii), pp. 6 and 12 | Rechecked directly from block spectral calculus and traciality, including zero atoms. General multiplicativity is unnecessary for this identity. |
| Upper semicontinuity along bounded moment convergence | MS24 Proposition 2.4 p. 7, used in Sections 3.3-3.4 pp. 13-14 | Direct truncated-log proof checked below. The finite bound is essential to the retained formulation; trivial kernels are not needed for the ordinary determinant. |
| Semicircular pairing rule and insertion order | [MS17 PDF](../literature/pdf/MS17.pdf), Chapter 9, Definition 7/equation (9.16) p. 236/PDF 245; Remark 9 pp. 237-238/PDF 246-247; Definition 10(2) p. 239/PDF 248 | Primary definitions, recursive insertion and the semicircular specialization read. The usual scalar semicircular Wick rule supplies the model; coefficient matrices retain their order. The source's general cumulant theory is accepted rather than fully re-proved. |
| Uniform norm and near-unital moment control | MS17, discussion after equation (9.5), p. 231/PDF 240; MS24 Proposition 3.3 pp. 10-11 | The moment estimate and its use of faithfulness were checked. The MS24 quantitative pairing induction is reconstructed below. No concentration or random-matrix norm convergence theorem is needed. |

FK52 printed pp. 524, 528 and 529, MS17 printed pp. 231 and 236, and MS24 printed pp. 7, 12 and 14 were visually inspected through rendered pages in addition to text extraction.
FK52's proof scope is the bounded determinant, not the paper's separate character, uniqueness or factor-dimension theorems.
In particular, Lemma 6 following the product proof is not needed.

## Bounded Multiplicativity and the Factor Convention

Let \((\mathcal N,\sigma)\) be a finite von Neumann algebra with faithful normal tracial state and let \(\Delta_\sigma\) use the ordinary log integral from [U001](../audits/literature/MS24/Yin_U001.md#determinant-convention).
FK52 formulates its result in a finite factor.
The selected proof uses spectral/holomorphic functional calculus, trace cyclicity and unitary polar decomposition; these ingredients hold in the present finite tracial algebra.
The usual completion of a polar partial isometry to a unitary uses finiteness.
No uniqueness of the scalar trace or classification by scalar projection dimension enters this selected argument.

For invertible factors, the central calculation is the traced derivative

\[
\frac{d}{dt}\sigma(\log X(t))
 =\sigma(X(t)^{-1}X'(t)),
\qquad X(t)>0,
\]

obtained by differentiating the resolvent formula and using cyclicity inside the trace.
For \(X(t)=e^{tA^*}e^B e^{tA}\), \(B=B^*\), integration gives

\[
\sigma\bigl(\log(e^{A^*}e^B e^A)\bigr)
 =\sigma(B)+2\operatorname{Re}\sigma(A).
\]

Polar decomposition then gives multiplicativity on invertible elements.
The derivative formula without the trace is not asserted.

The analytic extension in FK52 preserves multiplicativity even when a determinant is zero.
The review checked its positive sandwich argument: for bounded \(H,K\ge0\), use

\[
R_\varepsilon=H+\varepsilon^2(K+\varepsilon I)^{-1},
\qquad
A_\varepsilon=R_\varepsilon(K+\varepsilon I)R_\varepsilon.
\]

Both factors are invertible and

\[
A_\varepsilon
 =HKH+\varepsilon H^2+2\varepsilon^2 H
       +\varepsilon^4(K+\varepsilon I)^{-1}\ge HKH,
\]

with norm convergence to \(HKH\).
Also \(R_\varepsilon\ge H\) and \(\|R_\varepsilon-H\|\le\varepsilon\).
The determinant converges for positive norm approximations from above, by Lemma 5.
Passing to the limit gives

\[
\Delta_\sigma(HKH)=\Delta_\sigma(H)^2\Delta_\sigma(K).
\]

This is an equality of finite nonnegative numbers; no division by a zero determinant occurs.
Unitary polar decomposition and \(\Delta(T^*T)=\Delta(T)^2\), the latter a direct spectral identity, give the bounded product formula.
These are checks of the cited classical proof, not new project results.

Consequently, for \(S\in M_m(M)\) and invertible \(c_1,c_2\in M_m(\mathbb C)\),

\[
\Delta_{\operatorname{tr}_m\otimes\tau}
 \bigl((c_1\otimes1)S(c_2\otimes1)\bigr)
 =|\det c_1|^{1/m}|\det c_2|^{1/m}\Delta(S).
\]

This is exactly the scale-removal operation in MS24.
The required positive factors are invertible when the covariance has positive capacity, is strictly positive, or satisfies \(\eta(I)>0\) in the directly treated zero-capacity branch.
Indeed, \(c>0\) gives \(\eta(c)\ge\lambda_{\min}(c)\eta(I)\).
The case \(\eta(I)\) singular is separated before normalizing.
Affiliated inverses of \(S\) are never inserted into this identity.

The previously retained HS07 statement remains correct at its stated scope.
Its author-version Lemma 2.4, p. 6, has a minor displayed typo: the bound ending in \(-2\Delta(B)\) must read \(-2\log\Delta(B)\).
The preceding equality already has \(-2\tau(\log B)\); positivity of \(\Delta(B)\) makes the corrected expression finite.
This typo does not affect the direct bounded dependency retained here, and this observation does not claim a full HS07 audit.

## Hermitization Does Not Need an Inverse

For \(S\in\mathcal N\), set

\[
H=\begin{pmatrix}0&S\\S^*&0\end{pmatrix}\in M_2(\mathcal N),
\qquad
|H|=\operatorname{diag}\bigl((SS^*)^{1/2},(S^*S)^{1/2}\bigr).
\]

Traciality gives \(\sigma((SS^*)^k)=\sigma((S^*S)^k)\) for all positive integers \(k\).
The two compactly supported spectral probability measures therefore agree, including their mass at zero.
Integrating the logarithm with the normalized block trace yields

\[
\Delta_{\operatorname{tr}_2\otimes\sigma}(H)=\Delta_\sigma(S),
\qquad
\Delta_{\operatorname{tr}_2\otimes\sigma}(H^2)=\Delta_\sigma(S)^2.
\]

The second identity also follows directly from the spectral distribution of \(|H|\).
Both survive zero determinant.
Thus there is no hidden injectivity premise in MS24's reduction to a positive operator.

## Positive Log Semicontinuity

Let \(P_j,P\ge0\) be bounded operators in tracial probability spaces, possibly different ones, such that their scalar moments converge and \(\sup_j\|P_j\|\le K<\infty\).
Enlarge \(K\) to include \(\|P\|\).
Polynomial approximation on \([0,K]\) gives weak convergence of their spectral measures \(\mu_j\) to \(\mu\).
For \(\varepsilon>0\), the function \(g_\varepsilon(t)=\log\max(t,\varepsilon)\) is continuous there and

\[
\limsup_j\int\log t\,d\mu_j(t)
 \le\int g_\varepsilon(t)\,d\mu(t).
\]

Taking the decreasing infimum over \(\varepsilon\downarrow0\) gives

\[
\log\Delta(P)\ge\limsup_j\log\Delta(P_j),
\qquad
\Delta(P)\ge\limsup_j\Delta(P_j).
\]

The conclusion includes \(-\infty\) logarithms and zero atoms.
Consequently, MS24 Proposition 2.4 can be used in this form without the source's restriction to trivial kernels.
The printed bound \(\sup_j\|P_j\|\le\infty\) is not the intended finite bound.
The source's cited kernel-omitting determinant theorem is not needed for this elementary ordinary-determinant argument.

For the upper bound in MS24, apply the result to the **squares** \(H_\delta^2\) of the normalized hermitizations and to the square of a standard semicircular element.
These operators are positive and have uniformly bounded norms.
Applying Proposition 2.4 literally to signed \(H_\delta\), as in the display preceding equation (3.7), would not match its hypotheses.
Squaring yields exactly the same required conclusion \(\limsup_\delta\Delta(H_\delta)\le e^{-1/2}\).

For the lower bound, a fixed perturbation \(S_t=S+\sqrt t\,B\) gives norm convergence directly, hence norm convergence of the positive squares of the hermitizations.
No continuity modulus for covariance maps is consumed.
Neither use requires uniform control of negative moments or uniform integrability of \(|\log t|\); only this one-sided semicontinuity is asserted.

## The Semicircular Moment and Norm Inputs

For a selfadjoint matrix-valued semicircular element \(H\), write \(E=\operatorname{id}\otimes\tau\) and \(\theta(b)=E[HbH]\).
The scalar free semicircular moment rule, with coefficient matrices kept in their original order, gives

\[
E[H^{2k}]=\sum_{\pi\in NC_2(2k)}K_\pi,
\qquad E[H^{2k+1}]=0.
\]

Here \(K_\pi\) is obtained by nesting \(\theta\) according to \(\pi\).
MS17 Definition 7 and Remark 9 specify this insertion rule; Definition 10(2) gives its semicircular specialization.
The general freeness/cumulant equivalence and subordination theorem adjacent to that definition are not needed for this calculation on an explicit scalar semicircular family.

Each term involves exactly \(k\) applications of \(\theta\), so \(\|K_\pi\|\le\|\theta\|^k\).
More generally, inserting coefficient matrices gives the same bound multiplied by their norms.
Strip one adjacent pair from \(\pi\) and write the resulting \(\theta(I)\) insertion as \(I+(\theta(I)-I)\).
The error term contains \(k-1\) remaining applications of \(\theta\), while the first term is the stripped pairing.
Induction gives

\[
\|K_\pi-I\|
 \le\left(\sum_{r=0}^{k-1}\|\theta\|^r\right)\|\theta(I)-I\|.
\]

Summing over the \(C_k\) noncrossing pairings and applying the normalized scalar trace gives the estimate in MS24 Proposition 3.3.
The same norm bound gives

\[
(\operatorname{tr}\otimes\tau)(H^{2k})
 \le C_k\|\theta\|^k\le4^k\|\theta\|^k.
\]

Faithfulness is relevant: it identifies the support of the scalar spectral law with the spectrum of the selfadjoint element.
Hence \(\|H\|\le2\|\theta\|^{1/2}\), as in the MS17 passage.
A nonfaithful state would yield only a bound on its visible spectral support.

For the completely positive maps here, \(\|\theta\|=\|\theta(I)\|\) needs no additional general positive-map theorem.
With a Kraus representation, write \(\theta(b)=V^*(I\otimes b)V\).
The upper bound follows from \(\|V\|^2=\|\theta(I)\|\), and equality follows by evaluating at \(I\).
Thus \(\theta_j(I)\to I\) gives both uniformly bounded \(\|H_j\|\) and convergence of every scalar moment to the standard semicircular moments.
Convergence of the full maps \(\theta_j\) is unnecessary.

The lower-bound perturbation can be realized using finitely many additional free standard semicircular variables and a Hermitian matrix basis orthonormal for the unnormalized Hilbert-Schmidt trace.
The coefficients must be divided by \(\sqrt m\) to obtain \(b\mapsto\operatorname{tr}_m(b)I\); [U003](../audits/literature/MS24/Yin_U003.md#ms24-u003) records this normalization.
If a larger tracial model is used, the determinant of the original \(S\) is preserved because its compactly supported \(*\)-distribution is preserved.
Existence of such a free semicircular family is the usual full Fock model already used in the repository's [Miy22 setup](../audits/literature/Miy22/Yin_U001.md), not an assertion that the original ambient algebra already contains the extra variables.

## Offline Affine Extension: Additional Source Interfaces

On 2026-09-12 the user asked for the determinant formula with a deterministic coefficient matrix and prohibited network searches for this exploration.
The local MS17 Chapter 9 interfaces were checked at Definition 10 and Theorem 11(1), (2), (4), printed p. 239 / PDF p. 248, especially equation (9.20); Proposition 13, printed pp. 241-242 / PDF pp. 250-251; and equation (9.5), printed p. 231 / PDF p. 240, with the continuation discussion on printed p. 232 / PDF p. 241.
PDF p. 248 was also rendered and visually inspected.
These passages supply operator-valued semicircular cumulants, matrix/scalar cumulant compatibility and the Cauchy/R-transform relation, with no extra matrix-size factor in the covariance.

The resulting [Yin_C_F0002 project deduction](../claims/Yin_C_F0002_v1.md#yin_c_f0002) writes the affine moment recursion, proves pointwise uniqueness of the regularized Dyson solution and derives its logarithmic primitive.
It proves an exact finite-dimensional functional replacing the centered capacity term, including zero determinants.
It also proves that the deterministic term and the original covariance map alone do not determine the answer for general complex coefficients.
The [main contributor review](../audits/reviews/Yin_R_F0001_v1.md#scope-of-the-passed-review) and [monotonicity author check](../audits/reviews/Yin_R_F0006_v1.md#monotonicity-self-review) identify their exact inspected portions and disclose their self-review relationships.

This is a project extension, not a statement attributed to MS24 or a full audit of MS17.
MS24's centered formula is used only to identify the new functional at zero drift.
No ordinary-capacity-style global optimization formula or novelty claim is established.
These additional interfaces do not alter the source proof chains or their previously recorded audit boundaries.

## Search Scope and Remaining Boundaries

The trigger was the MS24-focused request to verify upstream dependencies, specifically HS07's retained bounded theorem.
Existing MS24, HS07 and MS17 primary passages were read first.
The search for the original bounded theorem located the published FK52 article through an academic collected-works mirror.
Selected theorem, convention and proof passages were checked, including the zero-determinant extension.
The search stops because this supplies the exact missing provenance and checked proof scope; no audit of unrelated determinant extensions is necessary.

No unresolved analytic premise remains in the two determinant-formula inequalities at the corrected scope recorded here.
The capacity-minimizer, near-minimizer and algebraic rank interfaces are separate dependencies, to be assessed in their own reviews.
In particular, this analytic supplement does not certify all statements or algorithmic constants in Gur04/GGOW20, nor does it turn positivity of a determinant into boundedness of an inverse.
