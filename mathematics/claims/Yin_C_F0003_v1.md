---
author: Yin
---

# Finite Dyson derivative system reconstructs regularized Brown measures and selfadjoint spectral data

## Current assessment
[Selected decision](#decision-m04-isolated-review)

## Affine Spectral Potentials from the Matrix Dyson Equation

<a id="statement"></a>

<a id="yin_c_f0003"></a>
The Brown construction and elliptic benchmarks remain explicitly accepted source results.
No mathematical Role is assigned.

Date: 2026-09-12.
Author: another AI agent.
Record kind: project derivation and selected local-source check, prepared within the user's three authorized affine-determinant routes.
No network searches or downloads were performed.
This module specializes [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002); it makes no novelty claim.

## Setting and exact logarithmic potential

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, let \(s_1,\ldots,s_n\in M\) be freely independent standard semicircular elements, and set
\[
 T=\sum_{j=1}^n a_j\otimes s_j\in M_m(M),\qquad
 S_z=T-zI_m,\qquad \varphi=\operatorname{tr}_m\otimes\tau.
\]
Here \(a_j\in M_m(\mathbb C)\) are arbitrary, \(z\in\mathbb C\), and matrix traces denoted by \(\operatorname{tr}\) are normalized.
Define
\[
 A_z=\begin{pmatrix}0&-zI_m\\-\bar zI_m&0\end{pmatrix},\quad
 B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},\quad
 \Theta(R)=\sum_j B_jRB_j.
\]
For \(\varepsilon>0\), let \(G=G_\varepsilon(z)\) be the unique solution of
\[
 G^{-1}=i\varepsilon I_{2m}-A_z-\Theta(G),\qquad \operatorname{Im}G<0.
 \tag{SP1}
\]
The existence, uniqueness, normalization, and primitive are the ones proved in Yin_C_F0002.
Write \(G_{pq}\), \(p,q\in\{1,2\}\), for its \(m\)-by-\(m\) blocks.
The exact regularized potential is
\[
\begin{aligned}
 u_\varepsilon(z)
 &=\frac12\varphi\log(S_z^*S_z+\varepsilon^2I_m)\\
 &=-\frac1{2m}\log|\det G_\varepsilon(z)|
   +\frac1{4m}\operatorname{Re}\operatorname{Tr}_{2m}
      \bigl(\Theta(G_\varepsilon(z))G_\varepsilon(z)\bigr).
\end{aligned}
\tag{SP2}
\]
In particular \(u(z)=\log\Delta_\varphi(T-zI_m)=\lim_{\varepsilon\downarrow0}u_\varepsilon(z)\), including the value \(-\infty\).
The capacity-shaped version of the same identity is
\[
 u(z)=-\frac12+\frac1{2m}
       \log\mathcal C_{\mathrm{aff}}(-zI_m;a_1,\ldots,a_n),
 \tag{SP3}
\]
with \(\log0=-\infty\).
The symbol \(\mathcal C_{\mathrm{aff}}\) retains Yin_C_F0002's status as local notation, not a standard named capacity from a source.

## Brown measure and the local source boundary

The retained [MS17 PDF](../literature/pdf/MS17.pdf), Chapter 11, supplies the following selected interfaces.
These passages were read locally this round, and PDF pp. 277 and 285 were also rendered and visually inspected.

| Interface | Exact locator | Scope consumed here |
| --- | --- | --- |
| Brown logarithmic potential | Theorem 5 and Definition 6, printed p. 268 / PDF p. 276, equations (11.6)-(11.7) | For a bounded element in a faithful tracial von Neumann algebra, the potential is subharmonic, and its normalized distributional Laplacian is a probability measure supported in the operator spectrum. |
| Positive regularized Laplacian | Printed p. 269 / PDF p. 277, equation (11.8) and the adjacent calculation | The source uses a regularizer \(\delta\) here; in this module \(\delta=\varepsilon^2\). |
| Resolvent block and weak regularization limit | Section 11.9, printed pp. 276-277 / PDF pp. 284-285, equations (11.14)-(11.15) | The regularized Brown measure is recovered from the lower-left hermitized resolvent block and converges weakly to the Brown measure. Apply the source with the ambient algebra \((M_m(M),\varphi)\). |
| Elliptic benchmark | Theorem 9, printed p. 275 / PDF p. 283 | The nondegenerate scalar elliptic model has uniform Brown measure on its ellipse, and the operator spectrum is that ellipse. This spectrum equality is specific to this cited example. |

The Brown construction and weak-convergence statements are accepted from these source interfaces, not independently reconstructed from Brown's original work.
The existing [BZ22 convention audit](../audits/literature/BZ22/Yin_U001.md#brown-measure-convention) uses the same normalization.
MS17's informal density parenthesis following (11.15) suppresses a normalization factor; the explicit conventions here are
\[
 \mu_T=\frac1{2\pi}\nabla_z^2u,
 \qquad \nabla_z^2=4\partial_{\bar z}\partial_z,
 \qquad \partial_z=\tfrac12(\partial_x-i\partial_y).
 \tag{SP4}
\]
The differentiated finite matrix equation below is a direct project calculation, not an additional theorem attributed to MS17.

## Exact derivatives from one finite linear system

Put \(Q=S_z^*S_z+\varepsilon^2I_m\) and \(P=S_zS_z^*+\varepsilon^2I_m\).
Direct inversion of the hermitization gives
\[
 G_{21}=-\bigl(\operatorname{id}_{M_m}\otimes\tau\bigr)(Q^{-1}S_z^*).
\]
Differentiating the trace of the logarithm (valid for the strictly positive \(Q\)) therefore yields
\[
 \boxed{\quad\partial_z u_\varepsilon(z)
       =\tfrac12\operatorname{tr}_m G_{21}.\quad}
 \tag{SP5}
\]
In fact \(\partial_zQ=-S_z^*\), so both sides equal \(-\tfrac12\varphi(Q^{-1}S_z^*)\).
This fixes the sign relative to the \((i\varepsilon-H)^{-1}\) resolvent convention.

Let
\[
 E_{21}=\begin{pmatrix}0&0\\I_m&0\end{pmatrix},\qquad
 \mathcal L_G(X)=X-G\Theta(X)G.
\]
The matrix \(X=\partial_{\bar z}G_\varepsilon(z)\) is characterized by
\[
 \boxed{\quad\mathcal L_G(X)=-GE_{21}G.\quad}
 \tag{SP6}
\]
Indeed, \(\partial_{\bar z}A_z=-E_{21}\).
Differentiating (SP1), multiplying on both sides by \(G\), and collecting terms proves (SP6).

This linear system is uniquely solvable at every \(\varepsilon>0\).
If \(\mathcal L_G(X)=0\), the weighted contraction in the Yin_C_F0002 uniqueness proof, with the two solutions both equal to \(G\), proves \(X=0\).
Since the domain is finite dimensional, injectivity implies invertibility.
This proves invertibility at fixed positive regularizer; it supplies no uniform bound as \(\varepsilon\downarrow0\).

Consequently the density of the regularized Brown measure can be obtained entirely from finite matrix equations:
\[
 \boxed{\quad
 \rho_\varepsilon(z)
   =\frac1\pi\operatorname{tr}_m X_{21}
   =\frac{\varepsilon^2}{\pi}\varphi(Q^{-1}P^{-1})\ge0.
 \quad}
 \tag{SP7}
\]
The first expression is real, even though (SP6) is a complex matrix equation.
To verify the second, differentiate (SP5) at the operator level and use
\[
 S_zQ^{-1}S_z^*=I_m-\varepsilon^2P^{-1}.
\]
This gives
\[
 \partial_{\bar z}\partial_z u_\varepsilon
 =\tfrac12\varphi(Q^{-1}-Q^{-1}S_zQ^{-1}S_z^*)
 =\tfrac{\varepsilon^2}{2}\varphi(Q^{-1}P^{-1}).
\]
Positivity follows from \(\varphi(Q^{-1}P^{-1})=\varphi(Q^{-1/2}P^{-1}Q^{-1/2})\ge0\), not from any assertion that the two positive factors commute.
Thus
\[
 \rho_\varepsilon(z)\,d^2z\ \Longrightarrow\ \mu_T
 \qquad(\varepsilon\downarrow0)
 \tag{SP8}
\]
by the selected MS17 interface.
This weak limit includes atoms and measures concentrated on curves.
Pointwise convergence of the densities, differentiation of a pointwise limit, and absolute continuity of \(\mu_T\) are not asserted.

## Selfadjoint coefficients: a smaller spectral equation

Suppose now \(a_j=a_j^*\) for every \(j\), so \(T=T^*\).
Set \(\eta(b)=\sum_j a_jba_j\).
For \(w\) in the upper half-plane, the \(m\)-by-\(m\) matrix
\[
 g(w)=\bigl(\operatorname{id}_{M_m}\otimes\tau\bigr)((wI_m-T)^{-1})
\]
satisfies
\[
 g(w)^{-1}=wI_m-\eta(g(w)),\qquad\operatorname{Im}g(w)<0.
 \tag{SP9}
\]
The Yin_C_F0002 primitive applied directly to \(T\), without doubling, gives
\[
 \boxed{\quad
 u(w)=-\frac1m\log|\det g(w)|
       +\frac1{2m}\operatorname{Re}\operatorname{Tr}_m(\eta(g(w))g(w)).
 \quad}
 \tag{SP10}
\]
No extra regularizer is needed when \(\operatorname{Im}w>0\), because \(T-wI_m\) is then invertible.
For real \(x\), \(u(x)=\lim_{v\downarrow0}u(x+iv)\).
The scalar spectral measure \(\nu_T\) has Cauchy transform \(\operatorname{tr}_m g\), hence for real \(a<b\),
\[
 \lim_{v\downarrow0}-\frac1\pi\int_a^b
       \operatorname{Im}\operatorname{tr}_m g(x+iv)\,dx
 =\nu_T((a,b))+\tfrac12\nu_T(\{a,b\}),
 \tag{SP11}
\]
and
\[
 \nu_T(\{x\})=-\lim_{v\downarrow0}v\operatorname{Im}
                         \operatorname{tr}_m g(x+iv).
 \tag{SP12}
\]
Both formulas follow directly by integrating the scalar kernel \(v/((x-t)^2+v^2)\), then applying dominated convergence.
Thus no separate unaudited Stieltjes inversion theorem is needed.
The Brown measure of this normal operator equals \(\nu_T\), regarded as a measure on the real line; the source states this normal specialization on printed p. 270 / PDF p. 278.

Faithfulness identifies \(\operatorname{supp}\nu_T\) with the operator spectrum.
A real open interval is a spectral gap precisely when the physical Cauchy transform has analytic continuation across it with selfadjoint boundary values: the forward implication follows from the operator resolvent; the reverse follows from (SP11), locally on compact subintervals.
An arbitrary real algebraic solution of (SP9) is insufficient for such a conclusion; continuation must concern the physical solution selected in the upper half-plane.

## Scalar tests that preserve the missing covariance

For \(m=1\), write
\[
 v=\sum_j|a_j|^2,\qquad c=\sum_j a_j^2.
\]
If \(v=0\), then \(T=0\), \(u(z)=\log|z|\), and \(\mu_T=\delta_0\).
Assume \(v>0\).
Rotating \(T\) and the spectral coordinate by the same scalar phase makes \(c=r\ge0\), where \(r=|c|\le v\).
The real and imaginary coefficient vectors then are orthogonal.
Their semicircular linear combinations are free, and have variances \((v+r)/2\) and \((v-r)/2\); this follows immediately from their only nonzero, second free cumulants.

For \(r<v\), MS17 Theorem 9, after scalar scaling and rotation, gives the ellipse
\[
 \mathcal E=\left\{x+iy:
  \frac{x^2}{(v+r)^2/v}+\frac{y^2}{(v-r)^2/v}\le1\right\},
 \qquad
 d\mu_T=\frac{v}{\pi(v^2-r^2)}1_{\mathcal E}\,d^2z.
 \tag{SP13}
\]
The same law is recovered from the two-by-two Dyson equation.
In the interior limit write
\[
 G_0=\begin{pmatrix}-ih&\bar q\\q&-ih\end{pmatrix},\quad h>0.
\]
The inverse equation gives \(h^2+|q|^2=1/v\) and \(v\bar q+rq=z\), hence
\[
 q=\frac{x}{v+r}-i\frac{y}{v-r},\qquad
 u(z)=\frac{\log v-1}{2}
        +\frac{x^2}{2(v+r)}+\frac{y^2}{2(v-r)}
 \quad(z\in\mathcal E).
 \tag{SP14}
\]
The additive constant is fixed by the centered MS24 identity at \(z=0\).
Outside the ellipse the physical scalar branch satisfies
\[
 rq(z)^2-zq(z)+1=0,\qquad q(z)\sim z^{-1}\quad(|z|\to\infty),
\]
and
\[
 u(z)=-\log|q(z)|+\tfrac r2\operatorname{Re}(q(z)^2).
 \tag{SP15}
\]
This outside expression has derivative \(q/2\) and the normalization \(u(z)-\log|z|\to0\).
It matches (SP14) and its first derivatives on the ellipse.
For \(r=0\), interpret \(q(z)=1/z\): one obtains the disk of radius \(\sqrt v\), constant density \(1/(\pi v)\), and potential \((\log v-1)/2+|z|^2/(2v)\) inside and \(\log|z|\) outside.
For \(r=v\), the model is a rotated real semicircular element of variance \(v\); the measure is on a line, and (SP13)-(SP14), which divide by \(v-r\), do not apply.

These are known source examples and consistency checks, not new general Brown-measure theorems.
They show that a candidate capacity-type variational formula must retain \(c\) as well as \(v\): varying \(c\) at fixed \(v\) changes a disk into an ellipse or a line segment.

## Remaining scope and useful continuation

1. Equations (SP1), (SP6), and (SP7) give a finite-dimensional route to regularized Brown measure for arbitrary matrix coefficients, but no uniform stability estimate as \(\varepsilon\downarrow0\) has been proved here.
   Deriving one under explicit covariance hypotheses is a separate route.
2. For arbitrary nonnormal coefficients the Brown support is contained in the operator spectrum.
   Equality is not concluded from the determinant formula, from vanishing regularized density, or from boundedness of the expected resolvent.
   The selfadjoint case and the cited scalar elliptic example have stronger, separately justified conclusions.
3. The scalar elliptic family provides a stringent variational benchmark: a successful formula must produce both its interior quadratic potential and exterior algebraic branch, with the correct transition and degenerate line-supported case.
   Its phase transition can guide constrained or ordered saddle formulations.
4. In the selfadjoint case, real spectral gaps allow the direct \(m\)-by-\(m\) positive or negative resolvent formulation.
   Such gap-restricted optimization formulas should be tested first against (SP9)-(SP12), while distinguishing an order restriction from a global variational result valid on the spectrum.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:09 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#exact-derivatives-from-one-finite-linear-system) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0012_v1.md#new-calculations-checked) | Complete finite derivative system and regularized Brown potential, selfadjoint Cauchy/Poisson inversion and exact scalar elliptic, circular and line-supported benchmarks. Brown construction and weak convergence remain accepted local MS17 interfaces; uniform boundary stability and general Brown support/spectrum equality are excluded. |


### Decision m04-isolated-review

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:23 |
| status | proved |
| reason | Adopt the separately performed isolated review of the complete unchanged derivative and spectral module, retaining its accepted Brown/source foundations, historical unknown finding and all zero-regularizer and support/spectrum limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#exact-derivatives-from-one-finite-linear-system) | Whole finite derivative-system proof, regularized Brown potential, selfadjoint inversion and source-based scalar benchmarks. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0012_v1.md#f0081-complete-derivative-and-spectral-finding) | Complete SP1-SP15: fixed-positive-regularizer invertibility, derivative/sign/normalized positive Laplacian, Brown probability weak limit, physical selfadjoint spectral inversion and exact elliptic/circular/line benchmarks; accepted MS17 foundations remain explicit, with no uniform boundary stability or general Brown support/spectrum equality. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; Brown foundations accepted from local MS17

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#exact-derivatives-from-one-finite-linear-system) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md#new-calculations-checked) | Complete finite derivative system and regularized Brown-measure potential, selfadjoint spectral inversion and source-based scalar benchmarks; the record states that the module was written by the reviewing agent and that root independently checked its derivation and selected local source pages; uniform boundary stability and general Brown support/spectrum equality are not established. |

Original review classification and limitations: independently reviewed; Brown foundations accepted from local MS17

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

<a id="decision-candidate-0004"></a>

### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#exact-derivatives-from-one-finite-linear-system) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md#new-calculations-checked) | Complete finite derivative system and regularized Brown-measure potential, selfadjoint spectral inversion and source-based scalar benchmarks; the record states that the module was written by the reviewing agent and that root independently checked its derivation and selected local source pages; uniform boundary stability and general Brown support/spectrum equality are not established. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Complete finite derivative system and regularized Brown-measure potential, selfadjoint spectral inversion and source-based scalar benchmarks; the record states that the module was written by the reviewing agent and that root independently checked its derivation and selected local source pages; uniform boundary stability and general Brown support/spectrum equality are not established.

Review: [Exact material](../audits/reviews/Yin_R_F0012_v1.md#new-calculations-checked).

Material covered by that review: [Exact material](Yin_C_F0003_v1.md).
