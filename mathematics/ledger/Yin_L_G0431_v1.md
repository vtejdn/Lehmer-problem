---
author: Yin
---
# Single-Haar weight identity, regularization and the lower-certificate boundary

The current complete mathematical statement and necessary original proof are adopted in [C575v1](../claims/Yin_C_G0575_v1.md#decision-complete-current-self-adoption), with the actual [whole constructor SELF finding](../audits/reviews/Yin_R_G0757_v1.md#current-g432-complete-self-finding).
The complete original analysis, source and author boundaries, failures and mathematical continuation questions remain below.


Original formulation: 2026-10-11.
Human author Yin; the original authoring AI agent formulated and self-checked the elementary identities and their scope.
This fixed account retains that baseline, its complete proofs, source interfaces and estimate-direction limitations.
The later [R180 scalar-functional check](../audits/reviews/Yin_R_G0180_v1.md#whole-proof-finding), [R_F3 coefficient-interface check](../audits/reviews/Yin_R_F0003_v1.md#coefficient-whole-independent-finding) and [R_F4 scalar-capacity check](../audits/reviews/Yin_R_F0004_v1.md#scalar-capacity-whole-independent-finding) cover only their declared reused interfaces, not a whole-account acceptance or an integer Mahler gap.
The original retention represented no new proof review, numerical experiment or source inspection.

<a id="single-haar-formulation"></a>
## Exact object, existing inputs and normalization

Let U be a Haar unitary in a finite tracial von Neumann algebra: tau(U^n)=0 for every nonzero integer n.
Only W*(U), with its Haar probability trace, is used.
Fourier identification gives W*(U)=L-infinity(T,mu).
For any nonzero p in Z[t,t^-1],
\[
m(p)=\log M(p)=\log\Delta_\tau(p(U))
=\int_{\mathbb T}\log|p(z)|\,d\mu(z).
\]
All logarithms are natural.
No freeness hypothesis is imposed; different powers of U are dependent functions of the same unitary.
The integral is finite, including unit-circle zeros, whose logarithmic singularities are integrable.

The [Luc22 scalar interface](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) owns the source identification and kernel convention.
For this nonzero scalar polynomial the kernel is zero, so ordinary and kernel-removed FK determinants agree.
The same source's [abelian matrix reduction](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation) retains the unnormalized matrix trace for square weak isomorphisms; no division by degree or matrix size is introduced here.

The [F0008 general affine formula](../claims/Yin_C_F0004_v1.md#statement) and [attainment theorem](../claims/Yin_C_F0005_v1.md#yin_c_f0005) supply methodological comparisons.
Their exact formulas require free semicircular inputs; no such formula or finite-dimensional Dyson closure is transferred to p(U).
The [F0008 regularized proof](../claims/Yin_C_F0004_v1.md#regularized-minimum-used-in-the-proof) identifies its regularized optimizer as the conditional expectation of the inverse square; its trace normalization and source-specific hypotheses remain unchanged.

## Positive-weight functional and the elementary identity

Put B=|p|^2 on T.
Let W consist of measurable real weights w for which some constants 0<a<=b<infinity satisfy a<=w<=b almost everywhere.
Equivalently, w and its inverse are bounded positive elements of W*(U).
Define
\[
J_p(w)=\int_{\mathbb T}\bigl(Bw-\log w-1\bigr)\,d\mu.
\]
Then
\[
2m(p)=\inf_{w\in W}J_p(w).                       \tag{1}
\]
This is the scalar positive-weight specialization of the elementary log variational identity, not a new quantitative theorem.

For completeness, for x,y>0,
\[
xy-\log y-1-\log x=xy-1-\log(xy)\ge0,
\]
with equality precisely when xy=1.
Since B>0 almost everywhere, integration gives J_p(w)>=integral log B=2m(p).
For delta>0 use w_delta=(B+delta)^-1, which belongs to W, and compute
\[
J_p(w_\delta)=\int\log(B+\delta)\,d\mu
-\int\frac{\delta}{B+\delta}\,d\mu.
\]
The first integral decreases to integral log B by logarithmic integrability and monotone convergence applied to a bounded upper constant minus log(B+delta).
The second tends to zero by dominated convergence, since the zero set has Haar measure zero.
This proves (1).

Equality at a bounded weight requires w=1/B almost everywhere.
For a polynomial, this belongs to W exactly when p has no unit-circle zero.
Otherwise (1) is an unattained infimum in W, although its value is finite.
Allowing suitable unbounded affiliated weights changes the admissible class and its attainment; do not confuse these formulations.
In particular a positive determinant gap does not require a spectral gap for p(U).
Salem inputs can have unit-circle zeros.

<a id="regularization-and-direction"></a>
## Regularization and the direction of estimates

For epsilon>0 set
\[
m_\varepsilon(p)=\tfrac12\int\log(B+\varepsilon^2)\,d\mu,\qquad
w_\varepsilon=(B+\varepsilon^2)^{-1}.
\]
The regularized functional has an attained minimum,
\[
2m_\varepsilon(p)
=\min_{w\in W}\int\bigl((B+\varepsilon^2)w-\log w-1\bigr)\,d\mu,
\]
at w_epsilon, and
\[
\frac{d}{d\varepsilon}m_\varepsilon(p)
=\varepsilon\int(B+\varepsilon^2)^{-1}\,d\mu,\qquad
m_\varepsilon(p)\downarrow m(p).
\]
Differentiation is valid for each positive epsilon by bounded domination.
The exact error is
\[
E_\varepsilon(p):=m_\varepsilon(p)-m(p)
=\tfrac12\int\log\!\left(1+\frac{\varepsilon^2}{B}\right)d\mu\ge0. \tag{2}
\]
Its integrability follows from that of log B.
Fixed-input convergence in (2) supplies no input-uniform rate.

A trial weight, or restriction to a finite positive trigonometric trial family, gives an upper bound for the infimum.
A proposed Lehmer lower certificate must instead establish a global lower bound L_epsilon(p)<=m_epsilon(p), together with a separately justified error bound E_epsilon(p)<=R_epsilon(p).
A sufficient candidate goal on the positive-measure hard core is
\[
L_{\varepsilon(p)}(p)-R_{\varepsilon(p)}(p)\ge c>0,             \tag{3}
\]
with c independent of the original degree and input.
Neither certificate in (3) is currently available here.
The choice of epsilon and every degree, coefficient, approximation and auxiliary cost must be explicit; the argument must not assume the desired Lehmer gap.

<a id="reuse-and-next-discriminator"></a>
## Relation to existing arithmetic and finite-section work

For real coefficients F(t)=sum f_j t^j,
\[
|F(e^{i\theta})|^2=E_F+
2\operatorname{Re}\sum_{h\ge1}A_h(F)e^{ih\theta},\quad
E_F=\sum_jf_j^2,\quad A_h(F)=\sum_j f_jf_{j+h}.
\]
The [L318 signed bundle](Yin_L_G0318_v1.md#simultaneous-coherence-fixed-scope) uses these coefficients for a family of actual integer auxiliaries F_a on a fixed original polynomial P, aggregated before absolute values.
The single-Haar functional may be studied for P or for specified F_a, but those are different objects.
An estimate for the circle distribution of P does not automatically control the bundle's normalized signed correlations, nor replace its all-conjugate resultant calculation.
Any cross-route inequality must retain actual inputs, weights, full resultants and radial expenses.

The [L4 finite Gram/Toeplitz analysis](Yin_L_G0004_v1.md#degree-window-tests), with the retained [Den09 finite-section input](../audits/literature/Den09/Yin_U002.md#finite-section-determinant), already supplies fixed-input limiting interpretations and finite certificates with their full degree/boundary costs.
Its decreasing Schur residuals approach M(p)^2 from above.
Reproducing that limit, a finite positive residual or qualitative logarithmic integrability does not establish (3).

A correctly directed application of (3) still needs a named arithmetic constraint on the original single-Haar multiplier, or an explicit weighted inequality for the actual L318 auxiliary bundle, with degree dependence and behavior at circle zeros retained.
The relevant controls are cyclotomic inputs with m=0, noncyclotomic unit inputs with circle zeros, and the exact same original polynomial or auxiliary family used in the bound; this account contains no executed control calculation.
Jensen/Mahler alone, an upper trial value, a fixed-input Toeplitz limit, or spectral separation that excludes the intended Salem scope does not supply (3).
The continuing arithmetic question belongs to [S3](../strategies/Yin_S_G0003.md#single-haar-analytic-focus), with its present Task disposition unchanged.
