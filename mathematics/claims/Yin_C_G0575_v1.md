---
author: Yin
---

# Complete single-Haar bounded-weight variational identity and exact regularization boundary

The complete original mathematical argument is retained from [L431](../ledger/Yin_L_G0431_v1.md#single-haar-formulation).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The original scalar baseline is dated2026-10-11. R180, R_F3 and R_F4 retain only their stated coefficient/scalar-functional interfaces and original targets; none is used as whole-account acceptance of this complete baseline. No original source inspection or foreign whole-proof review is repeated here.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Let U be ONE Haar unitary in a finite tracial von Neumann algebra, with tau(U^n)=0 for every nonzero integer n and tau(I)=1.
Use only W*(U), identified with L-infinity(T,mu) for Haar probability mu; different powers of U are dependent functions of this same unitary and no freeness hypothesis is imposed.
For every NONZERO p in Z[t,t^-1] put B(z)=abs(p(z))^2 and m(p)=integral log|p|=log M(p).
Its logarithm is integrable even at its finitely many circle zeros, the scalar kernel has trace0, and both ordinary and kernel-removed FK determinants equal M(p) at their respective accepted conventions.

Let W be exactly the measurable real weights w with0<a<=w<=b<infinity almost everywhere for some constants a,b depending on w.
Thus both w and w^-1 are bounded positive elements.
Define
    J_p(w)=integral(Bw-log w-1)dmu.
Then
    2m(p)=inf_(w in W)J_p(w).
Equality at a weight occurs exactly for w=1/B almost everywhere, so the infimum is attained in W if and only if p has NO unit-circle zero.
The value remains finite and the infimum is unattained otherwise; allowing unbounded affiliated weights changes this domain and its attainment.

For every epsilon>0 put
    m_epsilon(p)=(1/2)integral log(B+epsilon^2)dmu,
    w_epsilon=(B+epsilon^2)^-1 in W.
Then
    2m_epsilon(p)=min_(w in W)integral[(B+epsilon^2)w-log w-1]dmu,
    d m_epsilon(p)/d epsilon=epsilon integral(B+epsilon^2)^-1 dmu,
    m_epsilon(p) downarrow m(p),
    E_epsilon(p)=m_epsilon(p)-m(p)
       =(1/2)integral log(1+epsilon^2/B)dmu>=0.
The regularized minimum is attained at w_epsilon.
The exact error is integrable; fixed-input convergence gives no input-uniform rate.

Every trial weight or finite positive trigonometric trial family gives an UPPER bound for the infimum.
A valid lower-certificate implication requires a global L_epsilon(p)<=m_epsilon(p) and a separately justified E_epsilon(p)<=R_epsilon(p), giving m(p)>=L_epsilon(p)-R_epsilon(p).
A uniform positive lower gap would require this difference>=c>0 on the entire selected positive-measure original-input class, with all original degrees, coefficients, approximation and auxiliary costs paid.
Neither missing certificate is supplied here.
The scalar distribution of p does not automatically control a different integer-auxiliary bundle's signed correlations or full original-root resultants.
No finite-dimensional free-semicircular formula, matrix-trace division, spectral gap excluding Salem circle zeros, input-uniform convergence rate or unrestricted Mahler conclusion is imported.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:36 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | All nonzero integer Laurent polynomials on one actual Haar unitary, complete bounded positive/inverse-bounded weight class, infimum/attainment/circle-zero/regularization/error/direction proofs and all single-variable/source/cross-route limits. |
| argument | [Entire complete argument](#argument) | All nonzero integer Laurent polynomials on one actual Haar unitary, complete bounded positive/inverse-bounded weight class, infimum/attainment/circle-zero/regularization/error/direction proofs and all single-variable/source/cross-route limits. |
| dependency | [Exact fixed input](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exactly group-fourier-convention: Canonical single-group Haar/Fourier and scalar FK/Jensen conventions with finite polynomial circle zeros; foundational proof depth unchanged. |
| dependency | [Exact fixed input](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exactly luc22-kernel-removed-determinant: Exact kernel-removed convention and agreement with the ordinary scalar determinant for nonzero polynomial null zero set; no arbitrary-kernel equivalence. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:41 |
| status | proved |
| reason | Under current human maintenance authorization, adopt the exact complete current Statement and original Argument after the actual R757 whole constructor SELF inspection. Preserve original dates, source/author/checking/interface limits, open summary predecessor and every unresolved arithmetic/near-one boundary. No new research or producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | All nonzero integer Laurent polynomials on one actual Haar unitary, complete bounded positive/inverse-bounded weight class, infimum/attainment/circle-zero/regularization/error/direction proofs and all single-variable/source/cross-route limits. |
| argument | [Entire complete argument](#argument) | All nonzero integer Laurent polynomials on one actual Haar unitary, complete bounded positive/inverse-bounded weight class, infimum/attainment/circle-zero/regularization/error/direction proofs and all single-variable/source/cross-route limits. |
| dependency | [Exact fixed input](../audits/literature/Den09/Yin_U001.md#den09-u001) | Exactly group-fourier-convention: Canonical single-group Haar/Fourier and scalar FK/Jensen conventions with finite polynomial circle zeros; foundational proof depth unchanged. |
| dependency | [Exact fixed input](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Exactly luc22-kernel-removed-determinant: Exact kernel-removed convention and agreement with the ordinary scalar determinant for nonzero polynomial null zero set; no arbitrary-kernel equivalence. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0757_v1.md#current-g432-complete-self-finding) | Entire exact current Statement and complete Argument with all listed actual fixed interfaces, all domains, quantifiers, normalization, source and upper/lower estimate boundaries; constructor SELF. |

## Complete original argument

<a id="argument"></a>

### Original account: Single-Haar weight identity, regularization and the lower-certificate boundary

Original formulation: 2026-10-11.
Human author Yin; the original authoring AI agent formulated and self-checked the elementary identities and their scope.
This fixed account retains that baseline, its complete proofs, source interfaces and estimate-direction limitations.
The later [R180 scalar-functional check](../audits/reviews/Yin_R_G0180_v1.md#whole-proof-finding), [R_F3 coefficient-interface check](../audits/reviews/Yin_R_F0003_v1.md#coefficient-whole-independent-finding) and [R_F4 scalar-capacity check](../audits/reviews/Yin_R_F0004_v1.md#scalar-capacity-whole-independent-finding) cover only their declared reused interfaces, not a whole-account acceptance or an integer Mahler gap.
No new proof review, numerical experiment or source inspection is represented by this retention.

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

The [F0008 general affine formula](Yin_C_F0004_v1.md#statement) and [attainment theorem](Yin_C_F0005_v1.md#yin_c_f0005) supply methodological comparisons.
Their exact formulas require free semicircular inputs; no such formula or finite-dimensional Dyson closure is transferred to p(U).
The [F0008 regularized proof](Yin_C_F0004_v1.md#regularized-minimum-used-in-the-proof) identifies its regularized optimizer as the conditional expectation of the inverse square; its trace normalization and source-specific hypotheses remain unchanged.

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
The [L318 signed bundle](Yin_C_G0600_v1.md#statement) uses these coefficients for a family of actual integer auxiliaries F_a on a fixed original polynomial P, aggregated before absolute values.
The single-Haar functional may be studied for P or for specified F_a, but those are different objects.
An estimate for the circle distribution of P does not automatically control the bundle's normalized signed correlations, nor replace its all-conjugate resultant calculation.
Any cross-route inequality must retain actual inputs, weights, full resultants and radial expenses.

The [L4 finite Gram/Toeplitz analysis](../ledger/Yin_L_G0004_v1.md#degree-window-tests), with the retained [Den09 finite-section input](../audits/literature/Den09/Yin_U002.md#finite-section-determinant), already supplies fixed-input limiting interpretations and finite certificates with their full degree/boundary costs.
Its decreasing Schur residuals approach M(p)^2 from above.
Reproducing that limit, a finite positive residual or qualitative logarithmic integrability does not establish (3).

A correctly directed application of (3) still needs a named arithmetic constraint on the original single-Haar multiplier, or an explicit weighted inequality for the actual L318 auxiliary bundle, with degree dependence and behavior at circle zeros retained.
The relevant controls are cyclotomic inputs with m=0, noncyclotomic unit inputs with circle zeros, and the exact same original polynomial or auxiliary family used in the bound; this account contains no executed control calculation.
Jensen/Mahler alone, an upper trial value, a fixed-input Toeplitz limit, or spectral separation that excludes the intended Salem scope does not supply (3).
The continuing arithmetic question belongs to [S3](../strategies/Yin_S_G0003.md#single-haar-analytic-focus), with its present Task disposition unchanged.
