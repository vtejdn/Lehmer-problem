---
author: Yin
---

<a id="smy08-u001"></a>
# Smy08-U001: height normalization, the house and degree-dependent bounds

## Source and inspection

Source edition: Smy08, [retained PDF](../../../literature/pdf/Smy08.pdf), arXiv:math/0701397v2, 28 January 2008; 28 pages.

Passages: Sections 1--4 in full, printed pp.322--327 / PDF pp.1--6; equations (1)--(13), introductory Lehmer formulation, height and house conventions, and the reported auxiliary-function mechanisms.

Inspection: 2026-10-06, coordinating AI agent for human author Yin. Complete assigned text read, formulas on complete rendered PDF pp.1--5 checked, elementary calculations below reproduced; an assigned reviewer independently checked the multiplicity correction. No independent second whole-source review or formal verification is asserted.


## Assessment and proof boundary

**Audited within scope** for the normalization conversions, elementary house comparisons, Fejer identity and annulus estimate, and the corrected resultant mechanism explicitly proved here.
**Read** for the externally reported lower-bound theorems and their summarized proof architectures: their original full proofs were not recursively audited.
**Questioned at literal scope** for the minimal-polynomial resultant assertion in Section 4.2.
The error affects the stated intermediate arithmetic input, not an established refutation of Dobrowolski's theorem.

<a id="smy08-height-normalization"></a>
## Mahler measure and the absolute logarithmic height

For a nonzero polynomial $P(t)=a_0\prod_{i=1}^d(t-\alpha_i)$ over $\mathbb C$, with roots counted with multiplicity, use natural logarithms and
$$
M(P)=\exp\left(\int_0^1\log|P(e^{2\pi it})|\,dt\right)
=|a_0|\prod_i\max(1,|\alpha_i|),\qquad m(P)=\log M(P).
$$
Jensen's identity for each linear factor proves the equality.
Zeros on the circle have integrable logarithmic singularities; they do not invalidate the integral.
The zero polynomial is excluded.
Nonzero constant polynomials have $M(P)=|P|$, and $M(PQ)=M(P)M(Q)$.

For an algebraic number $\alpha$, $P_\alpha$ means the **primitive integer minimal polynomial with positive leading coefficient**.
Its degree is $d=[\mathbb Q(\alpha):\mathbb Q]$.
In particular it need not be monic.
With $K=\mathbb Q(\alpha)$ and local absolute values extending the usual rational absolute values,
$$
h_{\rm abs}(\alpha)=\frac{m(P_\alpha)}d
=\frac1d\sum_v [K_v:\mathbb Q_v]\log^+|\alpha|_v.
$$
At real and complex places the weights are respectively 1 and 2.
At finite places use $|p|_p=p^{-1}$.
The finite-place contributions total $\log a_0$, explaining the leading-coefficient term in (3)--(5); using only archimedean roots for a nonintegral number loses it.
The expression is unchanged on enlarging the field.
The zero value $h_{\rm abs}(0)=0$ is understood separately with $\log^+0=0$.

For example $h_{\rm abs}(a/b)=\log\max(|a|,b)$ for coprime integers $a,b$ with $b>0$.
For $\alpha=2^{1/d}$, $m(\alpha)=\log2$ while $h_{\rm abs}(\alpha)=\log2/d$.
Thus Lehmer asks for $d h_{\rm abs}(\alpha)\ge c>0$ on nonzero nontorsion algebraic numbers; a degree-independent lower bound on $h_{\rm abs}$ is false.
Fixed-degree finiteness is elementary from $|a_k|\le\binom d k M(P)$ and does not yield a uniform gap over unbounded degree.

**Kronecker precision, p.322.** For arbitrary integer polynomials the measure-one characterization is $P=\pm t^k\prod_j\Phi_j(t)^{e_j}$, with finitely many nonnegative integer exponents.
The literal phrase “a power of z times a cyclotomic polynomial” must allow a product with multiplicities: $(t-1)^2$ is an immediate test.
For an irreducible minimal polynomial this reduces to $\alpha=0$ or a root of unity.
This is a convention/precision guard, not a challenge to Kronecker's theorem.

## Lehmer's target and Section 2

The survey poses the positive-gap problem, as well as giving Lehmer's polynomial and its historically smallest known positive measure.
A positive absolute gap is weaker than asserting this particular polynomial realizes the optimal gap.
The existing [Task contract](../../../tasks/Yin_T_G0001_v1.md#contract) must keep those statements separate.
The description of Pierce numbers checks that monicity, integral coefficients and the absence of roots of unity make each relevant product a nonzero integer.
An asymptotic derived with no roots on the unit circle cannot simply be quoted for unit-circle nonroots of unity without its additional Diophantine input.

The multivariate approximation statement attributed to Boyd, its Newton-polytope qualification, and the closed-set conjecture were read as external reports.
Their proofs and present-day status are outside this unit.
Neither permits deleting the unbounded-degree difficulty from the one-variable problem.

<a id="smy08-house"></a>
## House and its relation to the gap

For an algebraic integer define $\operatorname{house}(\alpha)=\max_i|\alpha_i|$.
If $r>0$ conjugates lie outside the unit circle,
$$
M(\alpha)^{1/d}\le M(\alpha)^{1/r}\le\operatorname{house}(\alpha)\le M(\alpha).
$$
If $\alpha$ is a unit, $M(\alpha^{-1})=M(\alpha)$; at least one of the two outside-root counts is at most $d/2$, giving $M(\alpha)\le\max(\operatorname{house}(\alpha),\operatorname{house}(\alpha^{-1}))^{d/2}$.
For nonzero algebraic integral $\alpha$, $M(\alpha)<2$ implies its nonzero integer norm has absolute value one.
All of these restrictions matter.
Equation (9) follows from $e^x\ge1+x$: $\operatorname{house}(\alpha)\ge1+m(\alpha)/d$.

**Historical status, not a defect in the 2008 source.** Sections 3 and 7 describe Schinzel--Zassenhaus as a conjecture.
Dim19 now provides the primary statement $\operatorname{house}(\alpha)\ge2^{1/(4d)}$ for noncyclotomic monic irreducible polynomials of degree $d>1$.
The retained 2019 v1 Theorem 1 was read at statement scope.
On 2026-10-06 the [Annals publisher record](https://annals.math.princeton.edu/articles/22975) lists the work as forthcoming, accepted 2026-08-27; the accepted 2026 text was not compared with v1.
This resolves the stated house-scale problem, not Lehmer's uniform Mahler gap: bounding only the largest root by $1+O(1/d)$ gives no uniform lower bound for its full logarithmic product.
No proof audit of Dimitrov is claimed.

## Section 4: checked mechanisms and external theorems

The Blanksby--Montgomery and Stewart estimates are degree dependent.
In the displayed Fejer identity the phase-shifted sum $\sum_{j=0}^K e^{ix(K/2-j)}$ is real, so its ordinary square is nonnegative; expansion gives the printed cosine weights.
The annulus estimate (10) is valid: writing $z=re^{it}$, the function $|re^{it}-1|^2$ is convex in $r\in[\rho,\rho^{-1}]$, so it suffices to check the endpoints against $\rho^{-2}|\rho e^{it}-1|^2$; at $r=\rho^{-1}$ equality holds, and at $r=\rho$ the difference is nonnegative.
These local checks do not audit the original lower-bound proofs.

For a nonzero algebraic integer of degree $d\ge2$ that is not a root of unity, the reported Dobrowolski benchmark has the form
$$
m(\alpha)\ge c\left(\frac{\log\log d}{\log d}\right)^3.
$$
Keep the chosen constant, degree range and asymptotic threshold together; the small-degree negative right side is merely vacuous.
Cantor--Straus, Louboutin and Voutier improvements are source reports, not independently reproduced here.
Their degree dependence still tends to zero.
No inference of today's best constant is made from this historical survey.

Section 4.3's multivariable estimate assumes multiplicative independence and a common number field of degree $d$; the relative estimate uses $D$, the degree over a finite abelian extension, and a constant depending on the base field.
These are not interchangeable degrees.
The elliptic-curve estimates require a nontorsion point and constants depending on the fixed curve and base field.
Formulas with $\log d$ in a denominator need a stated range $d\ge2$ (or a customary harmless modification for small degree).
They concern canonical heights, not the same function $h_{\rm abs}$ on algebraic numbers.
These statements were read; their original proofs and sharp ranges remain external.

<a id="smy08-resultant-multiplicity"></a>
## F1 — P1: the minimal-polynomial resultant loses multiplicity

**Locator/trigger:** Section 4.2, printed p.326 / PDF p.5.
The text claims the resultant of the minimal polynomials of $\alpha$ and $\alpha^p$ is divisible by $p^d$ for every prime $p$, where $d=\deg\alpha$.
This fails when powering lowers degree.

**Exact reproduction:** take $\alpha=\sqrt2$, $p=2$, $d=2$.
Then
$$
P_\alpha=t^2-2,\qquad P_{\alpha^2}=t-2,\qquad
\operatorname{Res}(t^2-2,t-2)=2\notin4\mathbb Z.
$$
The number is nonzero and not a root of unity, so those conditions do not repair the literal assertion.

**Corrected reusable interface:** for a nonzero algebraic integer $\alpha$ that is not a root of unity, with monic minimal polynomial $P$ of degree $d$, keep every powered conjugate, including multiplicity:
$$
Q_p(t)=\prod_{i=1}^d(t-\alpha_i^p)
=P_{\alpha^p}(t)^{[\mathbb Q(\alpha):\mathbb Q(\alpha^p)]}\in\mathbb Z[t].
$$
Frobenius on the symmetric coefficients gives $Q_p\equiv P\pmod p$.
Write $Q_p=P+pR$ with $R\in\mathbb Z[t]$.
Since $P$ is monic,
$$
\operatorname{Res}(P,Q_p)=p^d\operatorname{Res}(P,R)\in p^d\mathbb Z.
$$
If $P,Q_p$ shared a root, some conjugate $\beta$ of $\alpha$ would satisfy $\sigma(\beta)=\beta^p$ for a Galois automorphism of the normal closure.
Iterating its finite order $k$ gives $\beta^{p^k-1}=1$, impossible when $\alpha$ is not a root of unity.
Hence the resultant is nonzero and has modulus at least $p^d$.
In the test case $Q_2=(t-2)^2$ and the resultant is 4.
The original minimal-polynomial version is safe only after separately proving degree preservation.

**Impact/recommendation:** the [arithmetic strategy](../../../strategies/Yin_S_G0004.md) must retain the multiplicity or a degree-preservation hypothesis in every use of this input.
This repairs a specific local mechanism; it does not purport to reprove all of Dobrowolski's argument.
The original theorem remains an accepted external benchmark at its stated scope.

**Status:** newly identified in the existing retained source, 2026-10-06; exact hand calculation and a separate assigned-agent algebra check agree.
No current Claim proof used the defective literal assertion.
The existing strategy is updated to link this corrected input.

## Verification and downstream scope

The coordinating agent read Sections 1--4 and inspected the complete rendered pages identified above.
The elementary proofs/counterexample in this unit were checked directly, without numerical root heuristics or a proof assistant.
The [source entrance](readme.md) records the bounded correction search and whole-body division of work.
The [entropy strategy](../../../strategies/Yin_S_G0001.md) keeps its primary priority; this audit adds an exact arithmetic interface and preserves the Task contract and fixed prior assessment.
No original reference is claimed to be fully audited merely because its theorem appears in this survey.
