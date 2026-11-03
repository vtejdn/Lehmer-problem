---
author: Yin
---

# MS24: Main Proofs and Their Upstream Dependencies

<a id="ms24-dependency-chain"></a>
## Scope and reading order

Date: 2026-09-12.
This review implements the user's designation of MS24 as the principal source and research input for this source study.
It concentrates on Theorems 1.2 and 1.3/4.1 and Corollary 1.4 of the retained MS24 v1.
It does not designate a new project theorem, select a new research goal, or treat MS24's Section 5 questions as established results.

Start with this dependency map, then read the authoritative proof units [U003](../audits/literature/MS24/Yin_U003.md#ms24-u003) and [U004](../audits/literature/MS24/Yin_U004.md#ms24-u004).
Three focused supplements expose the actual upstream arguments:

- [Scaling dependencies](../audits/literature/MS24/Yin_U006.md#ms24-scaling-dependency-review): the precise finite-dimensional inputs, their elementary reconstructions, and the zero-capacity boundary.
- [Analytic dependencies](../audits/literature/MS24/Yin_U005.md#retained-analytic-proof-interfaces): determinant identities, logarithmic semicontinuity, semicircular moments and operator norms.
- [Integer dependencies](../audits/literature/MS24/Yin_U004.md#complete-retained-algebra-and-haar-interfaces): the linear-rank/free-Haar interface and the integer free-group determinant bound.

These supplements deepen the existing U001-U005 reviews without allocating duplicate unit or Claim IDs.
A source proof, a reconstruction of its exact required interface, and an accepted foundational theorem have different review descriptions.
A reconstruction does not establish that every line of the source's printed proof is correct.

## The two main outputs

Let \(m,n\geq1\), let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(s_1,\ldots,s_n\in M\) be freely independent standard semicircular elements.
For arbitrary \(a_i\in M_m(\mathbb C)\), put
\[
 S=\sum_i a_i\otimes s_i\in M_m(M),\qquad
 \eta(b)=\sum_i a_i b a_i^*,\qquad
 \operatorname{cap}(\eta)=\inf_{\substack{b>0\\\det b=1}}\det\eta(b).
\]
The determinant below is the ordinary Fuglede-Kadison determinant for the **normalized** trace \(\operatorname{tr}_m\otimes\tau\), with zero atoms included in the logarithmic integral.

**Theorem 1.2** is
\[
 \Delta(S)=e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.
\]
No integrality or selfadjointness of the coefficient matrices is needed.
Capacity zero is included.

**Theorems 1.3/4.1** state that if \(a_i\in M_m(\mathbb Z)\) and \(\eta\) is rank non-decreasing, then
\[
 \operatorname{cap}(\eta)\geq1.
\]
The hypothesis concerns integral Kraus matrices, not merely integer coordinates of a linear map.
**Corollary 1.4** combines the two results with the rank interface: if the integral-coefficient \(S\) is invertible in the affiliated algebra, then
\[
 \Delta(S)\geq e^{-1/2}.
\]
Bounded invertibility is not the hypothesis or conclusion.

## Chain A: the determinant formula

| Step | Precise inference | Evidence and upstream role |
| --- | --- | --- |
| A1. Normalize and hermitize | For positive invertible matrix factors, determinant scaling is governed by ordinary finite-dimensional determinants. The hermitization \(H=\left(\begin{smallmatrix}0&S\\S^*&0\end{smallmatrix}\right)\) satisfies \(\Delta(H)=\Delta(S)\). | [U001](../audits/literature/MS24/Yin_U001.md#determinant-convention), [U002](../audits/literature/MS24/Yin_U002.md#ms24-u002), and the analytic supplement. Traces on both matrix sizes are normalized. |
| A2. Capacity zero | If \(\eta(I)\) is singular, \(S^*\) has a nonzero kernel. Otherwise row normalization at any \(b>0\), \(\det b=1\), gives \(\Delta(S)\leq\det\eta(b)^{1/(2m)}\). Take the infimum. | Direct use of A1 and \(\Delta(R)^2\leq(\operatorname{tr}_m\otimes\tau)(RR^*)\). No free-field theorem is required for this step. |
| A3. Strictly positive covariance | If \(\eta(b)\geq\alpha\operatorname{tr}_m(b)I\) for \(b\geq0\), determinant-one sublevel sets are compact. An attained minimizer gives both stochastic marginals by differentiation. | Exact needed specialization of the Gur04 scaling mechanism, fully reconstructed in the scaling supplement. Uniqueness of the minimizer is unnecessary. |
| A4. Doubly stochastic covariance | After scaling, the hermitized covariance sends \(I\) to \(I\). Every noncrossing-pairing contribution to an even moment is \(I\), so the scalar distribution is standard semicircular and its determinant is \(e^{-1/2}\). | MS24 Propositions 3.2/3.4; the selected MS17 pairing convention and its local induction are checked in U002 and the analytic supplement. |
| A5. Lower bound | In a tracial free extension, fix a depolarizing semicircular \(B\) and use \(S_t=S+\sqrt t B\). Then \(\eta_t=\eta+t\operatorname{tr}_m(\,\cdot\,)I\) is strictly positive, \(\operatorname{cap}(\eta_t)\geq\operatorname{cap}(\eta)\), and \(S_t\to S\) in norm. Upper semicontinuity applied to \(H_t^2\) gives the lower bound on \(\Delta(S)\). | U003 gives the common realization and both inequality directions. Only determinant monotonicity is needed; the stronger Minkowski inequality and covariance-continuity rates are not premises. |
| A6. Near minimizers | For \(\operatorname{cap}(\eta)>0\), choose \(c_\delta>0\) with \(\det\eta(c_\delta)/\det c_\delta\leq e^\delta\operatorname{cap}(\eta)\). Row normalization makes the other marginal tend to \(I\). | GGOW20 Lemma 3.10 / MS24 Proposition 2.10, independently reconstructed in the scaling supplement from capacity duality and a scalar logarithmic inequality. |
| A7. Upper bound | The hermitized normalized models converge in moments to the standard semicircle, with a common finite operator norm bound. Apply logarithmic upper semicontinuity to their squares, and undo the determinant scaling. | U002-U003 and the analytic supplement. Moment convergence alone would not justify a determinant limit; only the correct one-sided inequality is used. |

The source presents A3 through the general indecomposable-minimizer theorem and A6 through GGOW20.
The dependency-focused reconstruction checks the smaller conclusions actually required.
The formula can therefore be supported by the elementary scaling arguments and the specified determinant/semicircular foundations without importing Gur04's auxiliary quantum-permanent claims or GGOW20's algorithmic correctness assertions.

The limit directions deserve emphasis.
A5 uses
\[
 \Delta(H^2)\geq\limsup_{t\downarrow0}\Delta(H_t^2)
 \geq e^{-1}\operatorname{cap}(\eta)^{1/m}.
\]
A7 uses
\[
 \limsup_{\delta\downarrow0}\Delta(H_\delta^2)
 \leq\Delta(s^2)=e^{-1}.
\]
Both are applications of the same upper semicontinuity statement to different limiting families.
Neither is an assertion of continuity at the logarithmic singularity.

## Chain B: integer capacity and the semicircular corollary

| Step | Precise inference | Evidence and upstream role |
| --- | --- | --- |
| B1. Coefficient-space rank | For \(V\subseteq\mathbb C^m\), \(\operatorname{ran}\eta(p_V)=\sum_i a_iV\). Rank non-decrease is absence of a shrunk subspace. The linear hollow-matrix criterion then makes \(A(x)=\sum_i a_i x_i\) full over the free field. | Elementary range identity and the exact linear-rank criterion; the integer supplement follows the existing [MSY23 algebra audit](../audits/literature/MSY23/Yin_U001.md#msy23-u001), including its Cohn locator correction. No invariant-degree estimate is used. |
| B2. Haar evaluation | Full \(A\) gives an injective \(T=\sum_i a_i\otimes u_i\in M_m(L(F_n))\), where \(u_i\) are the canonical free Haar generators. | MSY23 Corollary 6.4 and its full-matrix evaluation interface. The integer supplement checks the hypotheses and the reduced-word dual route. Strong Atiyah integrality alone is not substituted for free-field realization. |
| B3. Arithmetic determinant | Since \(T\in M_m(\mathbb ZF_n)\) is injective, \(\Delta(T)\geq1\). | The exact Sch01 specialization is checked and independently reconstructed from finite quotients in the integer supplement. Injectivity is supplied by B2 before converting to the ordinary determinant. |
| B4. Capacity comparison | For arbitrary \(b>0\) with \(\det b=1\), set \(c_i=\eta(b)^{-1/2}a_i b^{1/2}\). Then \(\sum_i c_ic_i^*=I\), so \(\Delta(\widetilde T)\leq1\), while multiplicativity and B3 give \(\Delta(\widetilde T)\geq\det\eta(b)^{-1/(2m)}\). | The complete local argument is in U004. Hence \(\det\eta(b)\geq1\) for every such \(b\), and taking the infimum proves the bound. |
| B5. Transfer to semicirculars | If \(S\) is affiliated-invertible, a shrunk coefficient space would force a nonzero kernel by the finite-tracial dimension inequality. Thus \(\eta\) is rank non-decreasing; combine B4 with Chain A. | U004 and the rank discussion in the scaling supplement. This gives the stated corollary without assuming a bounded inverse. |

The arithmetic and analytic model change is one-way in the proof:
\[
 \text{integer coefficients and rank non-decrease}
 \longrightarrow \text{injective free-Haar model}
 \longrightarrow \Delta(T)\geq1
 \longrightarrow \operatorname{cap}(\eta)\geq1
 \longrightarrow \Delta(S)\geq e^{-1/2}.
\]
The capacity lower bound is not obtained by first assuming the semicircular lower bound.
Chain A itself does not use B3 or B4, so there is no circular dependence between the two main theorems.

## Normalization and hypothesis checks

- Matrix capacity uses the ordinary determinant; operator determinants use \(\operatorname{tr}_m=\operatorname{Tr}_m/m\).
  A finite matrix contributes \(|\det b|^{1/m}\).
- For \(T^*T\), Sch01's unnormalized logarithmic integral equals \(2m\log\Delta(T)\), provided \(\ker T=0\).
  The factor accounts for both squaring and trace normalization.
- The defect \(\operatorname{ds}\) uses the unnormalized matrix trace.
  Hermitization doubles it; convergence of this defect still gives operator-norm convergence of the marginals in a fixed finite dimension.
- Positive capacity makes every \(\eta(c_\delta)\) invertible.
  Strict positivity gives this independently for the perturbations.
  No formal inverse is written before one of these facts applies.
- Multiplication by \(\eta(b)^{-1/2}\) and \(b^{1/2}\) takes place in \(M_m(\mathbb C)\).
  No multiplicativity theorem for an unbounded inverse is needed.
- The arbitrary-coefficient model \(S\) need not be selfadjoint.
  Its hermitization is selfadjoint, and its square is positive.
  The source's missing stars in arbitrary scaling are corrected in U002.
- At \(m=1\), the printed indecomposability condition includes the zero map vacuously.
  A2 and strict positivity avoid using that condition to form an inverse.
  The Haar case \(n=1\) is included in the separate upstream check.

## Dependencies excluded from the main conclusions

| Source item | Actual role here |
| --- | --- |
| Gur04 Appendix C general \(L^2\) identity and weak independence assertions | Not used in Chains A or B; the counterexamples in the earlier Gur04 audit do not affect these chains. |
| Gur04's general uniqueness theorem for indecomposable minimizers | Context for the source proof; the strictly positive existence/differentiation argument suffices in the reconstruction. |
| GGOW20 Theorem 2.18, capacity at least \(m^{-2m}\) | Earlier bound for comparison. It is not a premise of MS24's stronger integer bound. |
| GGOW20 Sections 4-5 numerical precision and full quantitative continuity modulus | Not used. Their questioned printed details remain questioned without making the present chains conditional on them. |
| Matrix-substitution degree bounds and invariant-ring generation | Not needed for the retained linear hollow-matrix and Haar route. |
| BM23/Mai22 quantitative covariance-continuity results | Replaced in this reconstruction by a fixed free perturbation with direct norm convergence. Their source proofs are not thereby audited. |
| General sofic-group determinant theorem and every closure operation in Sch01 | The free-group finite-quotient specialization suffices. No claim about all such extensions is needed. |

## Review evidence and reuse boundary

The original coordinator check is retained in [R8](../audits/reviews/Yin_R_F0008_v2.md#ms24-dependency-map-coordinator-finding) at its exact main-chain and primary-page scope.

The subsequent scaling-reviewer pass and its two exact wording corrections are retained in [R8](../audits/reviews/Yin_R_F0008_v2.md#ms24-dependency-map-scaling-finding).

The [arXiv record](https://arxiv.org/abs/2406.15922) was rechecked on 2026-09-12 and still lists v1 only.
The retained local artifact remains unchanged.
The original [cross-source review](../audits/reviews/Yin_R_F0008_v1.md) remains valid at its narrower recorded scope; this follow-up adds an MS24-centered dependency analysis.

These inputs control logarithmic singular-value mass.
They do not imply a spectral gap or an \(L^2\) inverse: a standard scalar semicircular element already has positive determinant and an inverse with infinite \(L^2\) norm.
Extensions to other operator families require a separately formulated research argument.
This source review does not reopen or settle those project goals.
