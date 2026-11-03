---
author: Yin
---

# Yin_T_F0008: Independent Review of the General Signed Schur Formula

Date: 2026-09-13.
Reviewer: the reviewing agent.
Target: the complete [general affine signed Schur module](../../claims/Yin_C_F0004_v1.md), including (A)-(C), equations (1)-(25), the bounded-inverse attainment statement, and the deterministic/circular specializations.

Finding: the full proof passes independent mathematical review.
Its primary result is a direct infimum over all positive definite matrices of the original coefficient size, for every affine complex-coefficient semicircular pencil.
The proof includes zero determinant and full centered MS24 recovery.
The coordinating agent owns Claim registration, current assessment and goal decisions; no mathematical Role is assigned here.

The reviewer did not author this module or discover its positive Stein argument.
Prior involvement includes source searches, candidate discussions, a paired reformulation of Yin_C_F0082, and the separate review of the earlier circular module.
During the present review, the reviewer independently reconstructed the weighted quadratic estimate, critical-point equations, Stein argument and resolvent transformation while the authors assembled the file, and reported the resulting checks.
The authors also disclosed another agent's preliminary algebra check.
These collaborations are recorded; neither is substituted for the complete assembled-file review below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [General signed-Schur finding](#general-signed-schur-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [General signed-Schur finding](#general-signed-schur-finding) | [C4 Statement](../../claims/Yin_C_F0004_v1.md#statement) | Complete original arbitrary-complex affine signed-Schur formula, regularized global extremum, zero determinant, bounded-inverse attainment and full centered MS24 specialization at the stated original source depths. |
| [General signed-Schur finding](#general-signed-schur-finding) | [C4 inner-form argument](../../claims/Yin_C_F0004_v1.md#the-inner-quadratic-form-is-positive-for-every-trial-matrix) | Entire positive inner form, compactness/existence, critical-point Stein sign, exact Dyson identification, value, ordered Schur formulation, rescaling and centered recovery chain. |
| [General signed-Schur finding](#general-signed-schur-finding) | [C4 fixed mathematical artifact](../../claims/Yin_C_F0004_v1.md) | Complete original proof and exact specializations; original inspection predates later determinant-first presentation, which has its separate limited self-review. No broader source proof, unregularized uniqueness or spectral-support claim. |

<a id="general-signed-schur-finding"></a>
The actual reviewer records candidate discussions, a paired reformulation of the preceding C_F0082 mechanism and concurrent mathematical exchanges while the authors assembled the proof.
Those known substantive mathematical context facts make this finding self-reviewed under the current rule, even though the reviewer did not author the positive Stein argument and separately reconstructed every displayed step.
The original 2026-09-13 inspection, its independent wording, actual checks and limits remain historical evidence; this declaration maintenance is no new review or inferred isolation.

## 1. Mathematical contract and genuine inputs

The inspected setting allows every finite matrix size, arbitrary complex constant and semicircular coefficient matrices, and an empty noise family.
The covariance maps \(\eta\) and \(\rho\) are both retained.
No selfadjointness of an original coefficient, positive capacity, irreducibility, spectral gap or existing optimizer is required for (A)-(B).

The proof uses Yin_C_F0002's matrix Dyson identity, strict half-plane uniqueness and logarithmic primitive.
Its explicit moment and primitive arguments apply to the selfadjoint hermitization used here.
Yin_C_F0002's later invocation of the centered MS24 equality is not a premise.
The finite positive-map norm interface is already accepted in the [analytic dependency record](../../ledger/Yin_L_F0002_v1.md).
The signed Schur action connects to Yin_C_F0079, but Yin_C_F0079's determinant theorem is not used to infer a global extremum.

Spe26, Yin_C_F0082, the earlier circular global minimum and HP03's Jensen theorem are not dependencies of this new proof.
HLN07 is related-source reading only.
The proof therefore supplies an independent mechanism for the full coefficient scope; it is not a reparameterization of Yin_C_F0082's feasible set.
This is a dependency assessment, not a priority or novelty claim.

## 2. Every trial has a unique inner maximizer

For \(Q>0\), the inner quadratic form acts on the real Hilbert space of complex matrices with pairing \(\operatorname{Re}\operatorname{Tr}(X^*Y)\).
Left multiplication by \(C_Q>0\) and right multiplication by \(Q^{-1}>0\) are commuting positive selfadjoint operators.
The antilinear term \(Y\mapsto\rho(Y^*)\) is selfadjoint for the real pairing: cyclically rotating \(\operatorname{Tr}(X^*a_jY^*a_j)\) interchanges \(X\) and \(Y\).

The weighted matrices in (7) satisfy the written equality of traces.
The inequality \(|\operatorname{Tr}(Z_j^2)|\le\operatorname{Tr}(Z_j^*Z_j)\) bounds the absolute value of each pseudo-covariance summand by its corresponding covariance quadratic term.
Consequently the complete form is bounded below by \(\varepsilon^2\operatorname{Tr}(Y^*YQ^{-1})\), strictly positive when \(Y\ne0\).

Thus the real-linear inverse exists for every positive trial, the inner maximum is finite and unique, and its value equals \(\operatorname{Re}\operatorname{Tr}(a^*Y_Q)\), with no missing factor two.
Smooth dependence on \(Q\) follows by inversion of a smoothly varying invertible finite real matrix.
No complex-linearity is incorrectly assigned to the pseudo-covariance term.

The trial \(Y=0\) makes the maximum nonnegative.
The lower bound (9) is therefore valid, and the scalar function \(\lambda-\log\lambda\) controls each eigenvalue both near zero and at infinity.
Sublevel sets lie in compact subsets of the positive cone.
Continuity then gives an actual interior global minimum.
This supplies existence before the later analysis of critical points.

## 3. The critical-point sign argument

Envelope differentiation holds because the inner first variation vanishes.
Differentiating the inverse of \(Q\) keeps the order \(Q^{-1}Y^*CYQ^{-1}\); differentiating \(C_Q\) gives the Hilbert--Schmidt adjoint of \(\eta\).
These terms give exactly (10), with \(P=C^{-1}-YQ^{-1}Y^*\) initially only Hermitian.

The normalization gives
\[
 K=I-U^*U=Q+\Phi^*(W),\qquad W=I-UU^*,
 \qquad \Phi(I)=I-\varepsilon^2C^{-1}<I.
\]
At this point it would be invalid to assume either \(K\) or \(W\) positive.
The unitary extension of the polar factor of the square matrix \(U\) is legitimate even at deficient rank: its initial and final complements have equal dimension.
Hence \(W=VKV^*\) holds with an actual unitary \(V\).

The resulting map \(\Lambda=\Phi^*\circ\operatorname{Ad}_V\) is completely positive, and
\(\Lambda^*(I)=V^*\Phi(I)V<I\).
Its adjoint has operator norm less than one in the norm induced by the matrix operator norm.
Therefore the spectral radius of \(\Lambda\) is less than one; finite dimensionality supplies the norm-convergent Neumann series even if \(\|\Lambda\|\) itself is not less than one in a different chosen norm.
Applying the inverse to (11) gives
\[
 K=\sum_{k\ge0}\Lambda^k(Q)>0.
\]
The zeroth term supplies strictness.
This proves \(W>0\) and \(P>0\) without a feasibility assumption on trials.
Complete positivity is used as preservation of positive matrices, not as positivity of a Hilbert--Schmidt quadratic form.

## 4. Identification of every critical point

The Schur inverse (14) is correct because the Schur complement over \(-Q\) is \(C^{-1}\).
The inner equation gives the off-diagonal blocks \(a-\rho(Y^*)\) and their adjoints; the envelope equation gives the bottom-right block \(-I-\eta^*(P)\).
Thus \(q^{-1}=A-\Theta(q)\) retains the entire covariance (15).

The transformed matrix
\[
 \mathcal R=
 \begin{pmatrix}i\varepsilon P&Y\\Y^*&iQ/\varepsilon\end{pmatrix}
\]
has strictly positive imaginary part.
Direct inversion verifies (17), including the signs of both off-diagonal pseudo-covariance terms.
Therefore \(-\mathcal R\) solves the physical upper-half-plane Dyson equation at \(i\varepsilon\), with strictly negative imaginary part.
The retained Yin_C_F0002 uniqueness result applies at this positive regularization.
No unproved uniqueness at a real gap is needed.

Comparing with the actual resolvent of the hermitization identifies
\[
 P=E[(SS^*+\varepsilon^2I)^{-1}],\quad
 Y=E[(SS^*+\varepsilon^2I)^{-1}S],\quad
 Q=\varepsilon^2E[(S^*S+\varepsilon^2I)^{-1}].
\]
Boundedness of \(S\) gives strict positivity of these diagonal expectations.
Hence all critical points coincide.
Since a global minimum was already proved to exist, its optimizer is unique.
This is a global argument rather than an inference from one stationary solution.

## 5. Value and ordered Schur formulation

Both diagonal factors transforming \(q\) into \(\mathcal R\) have determinant modulus one: their powers of \(\sqrt{\varepsilon}\) cancel across the two size-\(m\) blocks.
The Schur determinant therefore gives
\[
 |\det\mathcal R|=\det(C^{-1})\det Q.
\]
Multiplying the blocks of \(\Theta(\mathcal R)\mathcal R\) gives the negative diagonal contribution \(-2\operatorname{Tr}(P\eta(Q))\) and the two conjugate off-diagonal contributions with real part \(2b_\rho\).
This verifies (18).

The normalized hermitization determinant equals \(\frac12\varphi\log(SS^*+\varepsilon^2I)\); there is no additional factor two.
Yin_C_F0002's primitive then gives (19).
The two trace identities below it cancel the covariance correction exactly and identify the minimum with \(2m\log\Delta_\varepsilon(S)\).
All finite traces here are unnormalized.

Substituting the free Schur variables (20) into the real action yields (21).
Its unique inner maximum and subsequent minimum over \(P_s\) give (22) in the stated order.
The top-left block of (20) need not be positive at an arbitrary trial; its positivity is established only at the optimizer.
No extrema are interchanged.

## 6. Removal of regularization and complete centered recovery

The substitution \(Q=\varepsilon^2R\) is a bijection of positive cones for every \(\varepsilon>0\).
Its effects were checked individually:

- \(C_Q=\varepsilon^2(I+\eta(R))\), so the determinant powers cancel.
- \(C_QYQ^{-1}=(I+\eta(R))YR^{-1}\), while \(\rho(Y^*)\) is unchanged.
- Only \(\operatorname{Tr}Q=\varepsilon^2\operatorname{Tr}R\) retains the parameter.

This proves (23).
The operator \(\mathcal T_R\) is the regularized inner operator at parameter one, so it is invertible for every \(R>0\), including at zero determinant of the original pencil.

For \(c=\inf_R\mathcal V(R)\), every regularized infimum is at least \(c\).
Testing an arbitrary fixed \(R\) bounds the limiting infimum from above by \(\mathcal V(R)\).
These inequalities prove (24), also for \(c=-\infty\).
Together with spectral monotone convergence they establish the direct formula (A); monotonicity and continuity of the exponential on extended real limits establish (B).
The argument does not substitute zero into the old fixed-\(Q\) objective.

For zero mean, the inner maximum vanishes identically.
Determinant monotonicity gives one side of (C), and the test \(R=tB\), \(t\to\infty\), gives the other for every fixed \(B>0\).
Singular outputs are included by determinant continuity.
Taking the infimum afterwards handles zero capacity and nonattainment.
The exponent \(1/(2m)\) and constant \(e^{-1/2}\) exactly recover MS24 for arbitrary complex semicircular coefficients.
The disappearance of \(\rho\) is justified by zero mean, not assumed for the affine problem.

## 7. Attainment and exact specializations

If \(S\) is boundedly invertible, the rescaled minimizers converge in matrix norm to \(R_*=E[(S^*S)^{-1}]>0\).
The trace correction tends to zero.
Continuity of the always-defined finite real-linear solve and of \(\mathcal V\) gives actual attainment at \(R_*\).
The inner limit is \(E[(SS^*)^{-1}S]=E[(S^*)^{-1}]\).
For positive selfadjoint \(S\), these become \(E[S^{-2}]\) and \(E[S^{-1}]\); the text correctly distinguishes \(E[S^{-2}]\) from \(E[S^{-1}]^2\).

For empty noise, the objective reduces to \(-\log\det R-m+\operatorname{Tr}(Ra^*a)\).
Its invertible-case minimum and its singular-case kernel scaling both give the stated determinant, without requiring normality of \(a\).
When \(\rho=0\), the explicit inner solution \((I+\eta(R))^{-1}aR\) gives the displayed circular specialization.

No correction was required.
General unregularized attainment or uniqueness, spectral-support identification and convergence rates are not certified.
Numerical searches were not rerun and are not proof premises.
This review is internal mathematical review, not formal verification, external expert review or publication review.
Navigation-only later changes do not alter this evidence; substantive changes require scoped reinspection.



Original inspection: 2026-09-13.
This separated finding retains its original inspection and disclosures; its current relationship is the declared self-review above.
The related [self-review scope](Yin_R_F0007_v1.md#determinant-presentation-finding) is separate evidence; neither scope extends the other's findings.
