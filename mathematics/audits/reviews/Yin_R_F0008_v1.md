---
author: Yin
---

# Capacity Sources: Independent Interface Review

Date: 2026-09-12.
Reviewer: the coordinating agent, separate from the three assigned source reviewers.
This record reviews specified mathematical interfaces and corrections; the source units own the complete reusable statements.
It is not an independent audit of every page or external foundation.

## Retention and actual arrangement

This R home was prepared at 2026-10-21T01:03 from the complete original 2026-09-12 coordinating-agent interface review.
Its original date, primary passages, source inspections, corrections and limited verdicts below remain unchanged.
The coordinator is explicitly separate from the three assigned source reviewers; the inspected units identify its checks of their corrections.
The retained account does not establish initial isolation from source-development explanations or earlier review findings.
The initial context relationship is therefore unknown for these three actual interface findings, without converting their old independent descriptions into current certification.
This maintenance performs no new original-source opening or review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Gur04 interface finding](#capacity-gur04-finding) | unknown |
| [GGOW20 interface finding](#capacity-ggow20-finding) | unknown |
| [MS24 interface finding](#capacity-ms24-finding) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Gur04 interface finding](#capacity-gur04-finding) | [Gur04 U002](../literature/Gur04/Yin_U002.md#gur04-u002) | Qualitative capacity/scaling reconstruction, without the earlier mixed-discriminant comparison constant. |
| [Gur04 interface finding](#capacity-gur04-finding) | [Gur04 U003](../literature/Gur04/Yin_U003.md#gur04-u003) | Exact scaling, sign correction, sublevel bound, uniqueness and explicit zero-map boundary. |
| [Gur04 interface finding](#capacity-gur04-finding) | [Gur04 U004](../literature/Gur04/Yin_U004.md#appendix-c-corrections) | Only the Lemma C.2 and Proposition C.5(1) counterchecks reproduced below; other quantum-permanent/complexity/hardness limits unchanged. |
| [GGOW20 interface finding](#capacity-ggow20-finding) | [GGOW20 U002](../literature/GGOW20/Yin_U002.md#ggow20-u002) | Integral capacity lower bound and two displayed local normalization/complex-trace repairs. |
| [GGOW20 interface finding](#capacity-ggow20-finding) | [GGOW20 U003](../literature/GGOW20/Yin_U003.md#ggow20-u003) | Near-minimizer domain, exact exponential capacity premise and both Lemma 5.1 branches for Lemma 3.6; no whole Section 3 upgrade. |
| [GGOW20 interface finding](#capacity-ggow20-finding) | [GGOW20 U004](../literature/GGOW20/Yin_U004.md#ggow20-u004) | Only adjoint objective orientation, singular marginal counterexample and relative-error conversion; no full continuity modulus or precision exponents. |
| [MS24 interface finding](#capacity-ms24-finding) | [MS24 U003](../literature/MS24/Yin_U003.md#ms24-u003) | Normalized determinant/capacity formula and both inequalities, with square-hermitization and approximate-scaling interfaces. |
| [MS24 interface finding](#capacity-ms24-finding) | [MS24 U004](../literature/MS24/Yin_U004.md#ms24-u004) | Integer Haar-model capacity proof with exact kernel and 2m trace/square conversion at the accepted Sch01 interface depth. |

## Artifacts and Scope

- [Gur04](../../literature/pdf/Gur04.pdf): published pp. 448-484.
  Reviewed the qualitative capacity/scaling reconstructions and selected Appendix C objections.
- [GGOW20](../../literature/pdf/GGOW20.pdf): **published full article (2020)**, pp. 223-290.
  Reviewed Section 2.3 and Section 3.2, with the relevant branch in Lemma 5.1.
  The removed nine-page conference artifact is not the basis of these assessments.
- [MS24](../../literature/pdf/MS24.pdf): arXiv v1, pp. 1-19.
  Reviewed the determinant/capacity conventions, two-inequality proof and integer Haar-model proof, including the specific repairs below.


<a id="capacity-gur04-finding"></a>
## Gur04: Qualitative Chain and Auxiliary Overreach

The [U002-U002 reconstruction](../literature/Gur04/Yin_U002.md) was checked independently.
Cauchy-Binet gives nonnegative determinant coefficients; the independent-vector selection criterion and compactness over unitary bases give a uniform positive coefficient under rank non-decrease.
A rank-deficient projection yields determinant-one test matrices with capacity tending to zero in the converse direction.
This proves the qualitative equivalence without importing the earlier mixed-discriminant comparison constant.

Positive capacity increases under alternating normalizations and stays bounded above by one after normalization.
The determinant ratio tends to one; fixed marginal trace forces the other marginal's eigenvalues to tend to one.
This proves convergence of the stochasticity defects.
It does not prove convergence of the scaling matrices.

For exact scaling, the constrained derivative gives \(T^*(T(C)^{-1})=C^{-1}\).
The determinant-one inverse congruence uses \(|\det C_2|^{-2/N}C_2^*C_2\), correcting the sign printed on p. 464.
The strict-subset selection argument gives the eigenvalue-ratio sublevel bound; Jensen equality and the equal-rank projection family give uniqueness and its converse.
The zero map at \(N=1\) still requires the explicit positive-capacity condition before an inverse is formed.

The following two objections in [U004](../literature/Gur04/Yin_U004.md#appendix-c-corrections) were independently checked against the source statements:

1. In Lemma C.2, take a standard complex Gaussian \(z\), \(P(z)=z\), \(g(z)=z(|z|^2-2)\), and scalar substitution \(A=2\).
   The two purportedly equal inner products are \(0\) and \(12\), using \(\mathbb E|z|^2=1\), \(\mathbb E|z|^4=2\).
   Thus the arbitrary-\(L^2\) assertion is false, while the homogeneous holomorphic polynomial use is a distinct, valid restriction.
2. In Proposition C.5(1), let \(X=\begin{pmatrix}a&a\\d&d\end{pmatrix}\) with independent symmetric signs \(a,d\).
   Each permutation selects independent, centered, variance-one entries, yet \(\det X=0\).
   For the identity map the claimed quantum permanent is \(2\).
   Independence along individual permutations is insufficient for the mixed moments in that assertion.

These objections do not refute the IID Gaussian determinant identity or the central scaling theorem.
The remaining quantum-permanent, complexity and hardness assessments retain the source reviewer's stated depth; this review does not upgrade them.

<a id="capacity-ggow20-finding"></a>
## GGOW20: Capacity Bound and Approximate Minimizers

The full-version [capacity unit](../literature/GGOW20/Yin_U002.md#ggow20-u002) corresponds to Theorem 2.18, pp. 251-252.
For integral Kraus matrices \(A_i\) of size \(n\), a nonzero determinant blow-up has integral witnesses \(D_i\) satisfying \(\sum_i\|D_i\|_{\mathrm{HS}}^2\leq n^2d\).
For determinant-one \(X>0\), normalizing \(C_i=T_A(X)^{-1/2}A_iX^{1/2}\) gives \(\sum_iC_iC_i^*=I\).
The Hilbert-Schmidt bound on \(Y=\sum_iD_i\otimes C_i\) is \(\operatorname{Tr}(YY^*)\leq n^3d\).
Integrality, determinant multiplicativity and arithmetic-geometric mean then yield \(\det T_A(X)\geq n^{-2n}\), independently of the witness dimension \(d\).
The blow-up existence theorem is a retained algebraic input; it is not reproved here.

Two local repairs preserve this argument:

- Lemma 2.17's printed proof uses the false complex identity \(\operatorname{Tr}(XY^*)=\operatorname{Tr}(YX^*)\).
  Its inequality follows instead from the Hilbert-Schmidt triangle inequality followed by scalar Cauchy-Schwarz.
  The theorem's real integral application is therefore safe.
- Theorem 2.20's denominator and trace bounds on p. 253 must involve \(T_A^*(I)\), before normalization, rather than the already normalized \(T^*(I)=I\).

For the [approximate-minimizer interface](../literature/GGOW20/Yin_U003.md#ggow20-u003), Lemma 3.10 is on **p. 258 / PDF p. 36**.
Require \(T(C)>0\), as ensured by the positive-capacity hypothesis used in MS24.
Scaling gives the exact bound \(\operatorname{cap}(Z)\geq e^{-\delta}\).
The printed weakened bound \(1-\delta\) alone does not justify applying Lemma 3.6 with the same parameter.

Lemma 3.6 also needs the two branches of Lemma 5.1.
If the marginal eigenvalue defect is \(\alpha>1\), the product
\[
f(t)=\prod_i(1+t(x_i-1))
\]
strictly decreases for \(t>0\), because
\[
(\log f)'(t)=-t\sum_i\frac{(x_i-1)^2}{1+t(x_i-1)}<0.
\]
Comparison at \(t=\alpha^{-1/2}<1\) gives \(\prod_i x_i<e^{-1/6}\), incompatible with the lower bound \(e^{-\delta}\) for \(\delta\leq1/6\).
Thus \(\alpha\leq1\), and the other branch gives \(\alpha\leq6\delta\), including the endpoint.
This completes the specific quantified interface used by MS24.

### Additional Algorithmic Scope Check

The [Sections 4-5 unit](../literature/GGOW20/Yin_U004.md#ggow20-u004) distinguishes its conservative asymptotic reconstruction from the literal printed constants and the incomplete quantitative continuity bookkeeping.
The coordinating agent independently confirmed the orientation issue in Theorem 4.5: an approximate fixed point for \(X\mapsto T(T^*(X)^{-1})^{-1}\) is a Lemma 3.9 input for **\(T^*\)**.
Its determinant objective is \(\det T^*(C)/\det C\), and the perturbation comparisons must use that adjoint consistently.
Equality of the two capacities does not make the two objectives at a fixed \(C\) equal.

The singular-marginal counterexample in that unit also checks directly: Kraus matrices \(E_{11},E_{21}\) give \(T(I)=I\) and \(T^*(I)=2E_{11}\).
A singular adjoint marginal still certifies zero capacity through a common Kraus kernel; the printed inference that the other marginal is singular is unnecessary and false.
Finally, a bound \((1-\epsilon)\widehat c\leq c\leq\widehat c\) is a reciprocal upper-relative-error bound, so a smaller internal tolerance is needed for a symmetric \(1\pm\epsilon\) output guarantee.

This check does not upgrade the full continuity modulus or every precision exponent to independently verified.
The [Appendix A unit](../literature/GGOW20/Yin_U005.md#ggow20-u005) retains its separate assigned-reviewer assessment.

<a id="capacity-ms24-finding"></a>
## MS24: Normalization and Both Determinant Bounds

The [main formula](../literature/MS24/Yin_U003.md#ms24-u003) is
\[
\Delta_{\operatorname{tr}_m\otimes\tau}\left(\sum_i a_i\otimes s_i\right)
=e^{-1/2}\operatorname{cap}\left(b\mapsto\sum_i a_i b a_i^*\right)^{1/(2m)}.
\]
The scalar semicircular variables have variance one.
The coefficients may be arbitrary complex matrices.
Capacity uses the ordinary finite-dimensional determinant; the Fuglede-Kadison determinant uses the normalized matrix trace.

Independent checks confirmed:

- The sentence after Proposition 2.8 wrongly declares the adjoint automatically unital for every \(c>0\).
  For the depolarizing map on \(M_2(\mathbb C)\) and \(c=\operatorname{diag}(2,1)\), the adjoint marginal is \(\operatorname{diag}(4/3,2/3)\).
  The actual proof obtains it from a minimizer or a quantified approximate minimizer.
- With the source scaling convention, coefficients \(c_1a_ic_2\) have covariance \(\eta_{c_1,c_2^*}\).
  The factors used in the determinant proof are positive, so the source's arbitrary-factor star error does not affect those applications.
- Exact scaling and hermitization give the indecomposable case.
  A fixed free depolarizing perturbation gives norm convergence and the lower bound by upper semicontinuity.
  Approximate scaling gives moment convergence with a uniform norm bound for the upper bound.
  Apply the positive-operator semicontinuity statement to **squares** of the hermitizations in equation (3.7).
- The [integer-capacity proof](../literature/MS24/Yin_U004.md#ms24-u004) uses an injective integer free-group matrix \(T\), with \(\Delta(T)\geq1\), and compares the scaled determinant to its normalized second moment.
  The exact kernel and \(2m\) trace/square conversion are checked in [Sch01-U001](../literature/Sch01/Yin_U001.md#sch01-u001).
  This yields capacity at least one; substituting into the semicircular formula yields \(e^{-1/2}\).

The retained external foundations are the audited source rank/scaling interfaces, free-field realization, operator-valued semicircular construction and bounded Fuglede-Kadison multiplicativity.
Sch01's approximation theorem is accepted at the recorded primary-statement depth, not independently reproved.

## Reuse Boundary and Review Evidence

The source chain provides algebraic fullness and logarithmic control near zero.
It does not provide a spectral gap.
Already a standard scalar semicircular element has positive determinant and an unbounded inverse with infinite \(L^2\) norm.
Thus these results do not settle the active rational-boundedness questions merely by substituting another family of operators.

The coordinating agent reviewer read the specified primary passages and source-unit reconstructions and visually checked Gur04 p. 462, MS24 p. 8, and the full GGOW article pp. 250 and 258.
Other rendered passages are identified by their assigned reviewers.
No source PDF was edited, no numerical algorithm was implemented, and no formal verification was performed.
Cross-review approval here is limited to the explicit arguments above, with their corrections and retained foundations.
