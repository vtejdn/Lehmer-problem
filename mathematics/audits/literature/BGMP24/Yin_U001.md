---
author: Yin
---

# BGMP24: zero-compatible regularization and a questioned final constant

<a id="bgmp24-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: [BGMP24 published article](../../../literature/pdf/BGMP24.pdf), Brunault, Guilloux, Mehrabdollahei and Pengo, *Limits of Mahler measures in multiple variables*, AIF74(4)(2024),1407--1450, DOI10.5802/aif.3611, 45 PDF pages including cover. The original 2026-10-10 inspection used arXiv2203.12259v2, 27 June2022, and selected published online passages; its depth remains as stated below.

Passages: Published definitions pp.1413--1415 / PDF pp.8--10; Proposition4.10 pp.1429--1431 / PDF pp.24--26; Proposition4.11 and Lemmas4.12--4.13 pp.1431--1434 / PDF pp.26--29; Corollary4.14 p.1434 / PDF p.29; Theorem4.1 p.1420 / PDF p.15 and equations(4.23)--(4.26) pp.1436--1437 / PDF pp.31--32.

Inspection: On2026-10-10 orbit_research AI for Yin checked the exact definitions and selected statements, text-read the regularization proofs and visually inspected preprint PDF pages6,11,12,14. Proposition4.10 is accepted for the explicit application below at statement/applicability depth with its displayed layer-cake proof checked. Its underlying Theorem4.6 sublevel estimate is retained as an external input, not independently re-proved. No full-paper proof audit or formal verification is asserted. The final Theorem4.1 constant is questioned and is not adopted.


The 2026-10-14 source maintenance compared the complete mathematical content of the previously retained preprint with the published article throughout Sections 1–5: notation, convergence lemmas, exponential and general error bounds with their proofs, sublevel/regularization mechanisms, all polynomial examples and figures, the full logarithmic asymptotic expansion and perspectives.
The published article covers those arguments and examples, with editorial and reference changes; no necessary unique preprint argument or useful correction was identified.
This supports using the published artifact and its locators.
The accepted interface, constant objection and local repairs below remain; the comparison is not an independent full-paper proof audit.

## Accepted regularization interface

For a nonzero complex Laurent polynomial P in n variables, let k be its number of nonzero coefficients, D=diam(P) the maximum coordinate width of its exponent support, L1 the sum of coefficient moduli and L_infinity their maximum.
Let A be an integer m-by-n matrix, m<=n, and rho(A) the smallest infinity norm of a nonzero integer vector killed by A; an injective A has rho=infinity.
The pushforward of normalized Haar measure on the m-torus under the monomial map is mu_A; mu_n is normalized Haar measure on the n-torus.

Proposition4.10 states: if k>=2, L_infinity(P)=1, rho(A)>D, 0<alpha<1 and epsilon>0, then

    0<= integral [ (1/2)log(|P|^2+epsilon)-log|P| ] dmu_A
       <= C2(n,k,alpha) epsilon^((1-alpha)/(2(k-1))),
    C2(n,k,alpha)=12k^2(18 n k^2)^(n-1) alpha^(1-n)/(1-alpha).

Applying the same statement to the identity matrix gives the identical mu_n bound.
Zeros are allowed; this is precisely a bound on their logarithmic regularization cost.
The condition rho>D prevents distinct support monomials from colliding, so P_A retains its nonzero coefficient count and normalization.
The displayed proof pushes Haar measure forward by |P| and applies a nonnegative layer-cake integral to the sublevel bound from Theorem4.6.
The beta integral and the stated coarse sine bound give the displayed C2.
For sublevel parameters above one the trivial probability bound supplies the same coarse extension.
These are selected checked steps, not a fresh proof of the source's underlying multivariate sublevel theorem.

This established earlier proposition is accepted for the [complete C_G433 fixed-polynomial application](../../../claims/Yin_C_G0433_v1.md#effective-trinomial-phase-cutoff): n=2, m=1 or 2, k=3 or 11 after coefficient normalization, and rho>4.
It is not made conditional solely because the underlying source sublevel theorem was not independently re-audited.
The concrete final-constant objection below occurs in a later optimization and does not enter this accepted interface.

## Checked comparison and avoided proof step

The source's regularization uses the holomorphic function (1/2)Log(PP*+epsilon), where P* is conjugate reciprocal, on the annulus sum_i|log|z_i||<=delta with

    delta=min(sqrt(epsilon)/(D L1(P)), log(4/3)/D).

The radial Taylor proof in Proposition4.11 has purely imaginary linear term and bounds the real quadratic error by (1/2)D^2 L1^2 exp(D||h||_1)||h||_1^2, leaving real part PP*+epsilon at least epsilon/3.
The complete [C_G433 proof](../../../claims/Yin_C_G0433_v1.md#effective-trinomial-phase-cutoff) supplies its own elementary upper bound and rank-one Fourier summation from this mechanism.
Thus it does not need the final optimization in Theorem4.1 or its stated constant.
The source's Lemma4.13 proof writes f_epsilon=log(Q+epsilon) once although the defined function is half that logarithm; the local proof retains the half explicitly and proves its looser bound directly.
This observation does not challenge the earlier Proposition4.10.

The published equations(4.25)--(4.26), pp.1436--1437 / PDF pp.31--32, claim the numerical comparison

    50k^2(18 n k^2)^(n-1)e^n/[n(k-1)]^(n-1)
       <=8(36 e k)^(n-1).

At n=2,k=3 the ratio of the two sides is (2025/48)e>1, so this displayed comparison is false.
The preceding claimed minimizer alpha=n(k-1)/log(rho) also differs from the derivative's minimizer (n-1)(k-1)/log(rho); its chosen value can still be used without claiming optimality.
These findings concern the displayed proof and constants.
They do not constitute a polynomial counterexample to Theorem4.1, invalidate qualitative Lawton convergence, or establish that no sharper bound exists.
No author contact, broad erratum search or priority claim is made.
The local repaired deduction deliberately avoids both disputed steps.

## Search, acceptance and scope

The trigger was L179's non-effective primitive-trinomial limit.
The bounded search checked existing Den09-U002/L50 inputs and then primary sources for quantitative Lawton convergence allowing zeros.
The identified article supplied the required earlier regularization interface.
Its theorem constant prompted visual inspection and a specific preprint/publication comparison; both retained the same numerical problem.
The source's asymptotic expansions and other polynomial families were not adopted.
Search stopped after the earlier interface and a direct local repair sufficed; no exhaustive literature or source-proof audit is claimed.
The current reading state is Read with the explicitly accepted earlier interface and a Questioned later constant, rather than an undifferentiated whole-source assessment.
