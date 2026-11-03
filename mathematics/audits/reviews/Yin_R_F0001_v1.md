---
author: Yin
---

# Affine Semicircular Determinant: Proof Review

Date: 2026-09-12.
Reviewer: the reviewing agent.
Claim: [Yin_C_F0002](../../claims/Yin_C_F0002_v1.md#statement).
Authoritative argument: [Affine Semicircular Determinants](../../claims/Yin_C_F0002_v1.md#yin_c_f0002).
This is a review of an ordinary project deduction answering the user's affine MS24 question; it does not designate a main theorem or change an existing goal contract.

Review relationship: **self-reviewed**, with the substantive contributions disclosed below.
The reviewer previously derived the logarithmic primitive, supplied the elementary pointwise uniqueness argument, and checked the proposed removal of the regularization term.
The root assembled and wrote the complete ledger argument.
This agent reread and checked that written argument after contributing to its development; that rereading does not establish an independent review.

Checked artifact: the complete Claim argument identified above, including equations (1)-(15), the covariance obstruction, all three simpler cases, and the stated unresolved optimization question.
Later substantive changes require a corresponding review update.
The responsible Claim material and its selected decision own the current assessment.

Reviewed editorial revision, same date: The zero-drift sentence now explicitly says that the matrix expectation is block diagonal and identifies centered sign symmetry as the reason.
The revised sentence was checked.
No other mathematical text changed.
The passed review therefore covers this current revision as well.
The root also separately reported visually checking the same MS17 PDF p. 248 source interface.

Outcome: **passed within the exact stated scope**.
No blocking mathematical issue was found.
The affine identity holds for arbitrary complex matrix coefficients of a finite standard semicircular family, including zero noise, singular deterministic coefficients, and zero determinant.
A separately established global optimization formula, novelty claim, or spectral-gap estimate is not part of this outcome.

## Accepted Inputs and Local Source Verification

The user prohibited network searches for this exploration.
This review used only local files and mathematical deduction; no network request, search, or download was made.

The local [MS17 PDF](../../literature/pdf/MS17.pdf) was inspected at the following exact interfaces:

- Chapter 9, Definition 10 and Theorem 11(1), (2), (4), printed p. 239 / PDF p. 248, especially equation (9.20).
  The PDF page was also rendered and visually checked.
  These give the Cauchy/R-transform relation and the covariance R-transform of an operator-valued semicircular element.
- Proposition 13, printed pp. 241-242 / PDF pp. 250-251, gives compatibility between matrix-valued and scalar cumulants.
  Applied to the specified free standard semicircular family, it produces the covariance used in Yin_C_F0002, with no extra factor of the matrix size.
- Equation (9.5), printed p. 231 / PDF p. 240, and the discussion on printed p. 232 / PDF p. 241 support the moment-series derivation and analytic continuation.
  Yin_C_F0002 also writes the precise affine moment recursion, preserving the order of deterministic insertions.

The remaining general inputs are the tracial spectral calculus, the equality of the scalar spectral distributions of `S*S` and `SS*` in a finite tracial algebra, and the normalized logarithmic definition of the determinant.
Their conventions agree with the existing [MS24 foundations](../literature/MS24/Yin_U001.md#determinant-convention) and [analytic dependency supplement](../../ledger/Yin_L_F0002_v1.md).

The centered [MS24-U003](../literature/MS24/Yin_U003.md#ms24-u003) is used only to identify the zero-drift functional with ordinary capacity.
The derivation of the affine determinant identity does not use Cohn rank theory, the MSY23 full-matrix theorem, arithmetic determinant approximation, operator-scaling complexity bounds, or an external uniqueness theorem for the Dyson equation.
This scoped verification does not constitute a full audit of the MS17 monograph or a literature-priority search.

## Checks of the Complete Argument

| Portion of Yin_C_F0002 | Review evidence and result |
| --- | --- |
| Setting and equations (1)-(3) | The state on `M_m(M)` is normalized. Hermitization has size `d=2m`. All coefficient matrices in the hermitized problem are selfadjoint, although the original coefficients need not be. For each positive regularization parameter the candidate formula uses an invertible matrix with strictly negative imaginary part. Zero determinant is expressly included. |
| Full covariance, equation (5) | Direct block multiplication gives `eta(t)`, `rho(r)`, `rho-tilde(q)`, and `eta*(p)` in the stated positions. The extra maps contain no adjoints beyond those written. The Hilbert-Schmidt adjoint convention is correct. |
| Resolvent existence and equation (6) | Boundedness and selfadjointness of the hermitization give a strictly negative matrix imaginary part, with a positive scalar lower bound for its negative. This proves invertibility. The first cumulant is the deterministic matrix, the second is `Theta`, and higher cumulants vanish. The displayed affine recursion and large-parameter expansion reproduce the Dyson equation in the correct order, followed by analytic continuation. |
| Pointwise uniqueness and equation (7) | Both displayed imaginary-part identities hold. The difference satisfies `D=G1 Theta(D) G2`, with no adjoint on `G2`. After the stated normalization, the left row square sum and right column square sum are strictly below the identity because the regularization parameter is positive. Their operator-norm product is strictly below one, forcing the difference to vanish. This includes an empty noise family. |
| Bilinear symmetry, equation (8) | Cyclicity of the ordinary matrix trace proves the identity. No complex conjugation or Hilbert-Schmidt adjoint is substituted for this bilinear relation in differentiating the action. |
| Primitive and equations (9)-(10) | An analytic logarithm of the nonzero scalar function `det G(z)` exists on the simply connected upper half-plane. Differentiation of the inverse Dyson equation, followed by cyclicity and equation (8), gives the normalized trace of `G(z)`. Matching with `log z+o(1)` along the positive imaginary axis fixes the additive constant. This step is essential and is present. |
| Regularized identity, equation (11) | Taking real parts gives one half of the logarithm of `H^2+epsilon^2`. The two equally weighted diagonal blocks have identical scalar distributions. The resulting coefficients are exactly `-1/(2m)` and `1/(4m)`. Monotone truncated spectral integration handles the limit even when the logarithmic integral is negative infinity. |
| Capacity-shaped limit, equations (12)-(13) | The trace of the Dyson equation contributes exactly `-2m`, accounting for the factor `e^m`. The discarded trace is between zero and `2m`. Positive determinant excludes a zero atom, so dominated convergence makes that trace tend to zero. If the determinant is zero, the exponential factor remains between `e^(-m)` and one and the product still tends to zero. No unjustified exchange of a singular inverse limit is used. |
| Zero drift, equation (4) | Equation (2) reduces to the determinant of the regularized matrix inverse. Comparing the already proved affine identity with centered MS24 yields ordinary capacity with exponent `1/(2m)`, including zero capacity. This identification is downstream of the affine identity and creates no circular proof. |

In the zero-drift discussion, the statement that the matrix expectation of the resolvent is **block diagonal** is correct: the joint semicircular law is invariant under simultaneous sign reversal, and the off-diagonal resolvent blocks are odd in the centered hermitization.
The suggested clarification of the original wording was adopted and rechecked in the editorial revision identified above.

## Obstructions, Normalizations, and Smaller Cases

The covariance-only obstruction was checked in both versions appearing in the ledger.
For a real `t>2`, strict Jensen gives `log Delta(t+s)<log t`, while the integral of `log(t^2+s^2)/2` is strictly greater than `log t`.
The operators `t+s` and `t+i s` have the same deterministic term and exactly the same ordinary covariance map.
Thus even the pair consisting of the deterministic coefficient and the entire original covariance map is insufficient.
The auxiliary maps in equation (5) distinguish the two examples.

The scalar potential in equation (14) has the correct square-root branch and additive constant.
Its continuous real boundary value on the semicircular support is `x^2/4-1/2`.
At the imaginary argument the same formula gives equation (15), including its positive sign.
These scalar checks do not require a circular Brown-measure theorem.

The three simpler cases were also checked:

1. **Pure constant.**
   If `a0` is invertible, the limiting matrix is `-A^(-1)`.
   Its inverse determinant has absolute value `|det a0|^2`, and the trace exponential is `e^m`.
   Equation (3) therefore gives `|det a0|^(1/m)`.
   A singular constant gives zero through the already justified regularized limit.
2. **One semicircular variable.**
   With invertible `a1`, the pointwise determinant polynomial factors using the algebraic eigenvalues of `a1^(-1)a0`.
   Integrating its logarithmic absolute value gives the displayed sum of scalar potentials.
   Nonreal eigenvalues and nondiagonalizable coefficient matrices cause no problem.
   Real roots have an integrable logarithmic singularity against the semicircular density.
3. **Selfadjoint coefficients.**
   Directly using `M_m(C)` gives the smaller resolvent equation and coefficients `-1/m` and `1/(2m)` in the logarithmic formula.
   The trace symmetry needed for the primitive remains valid because the coefficients are selfadjoint.
   Doubling the matrix size is only needed to cover arbitrary complex coefficients by the same selfadjoint argument.

A separate read-only recheck by `affine_scalar_obstructions`, communicated on the same date, agreed on the covariance-only counterexample, equations (14)-(15), the pure-constant normalization, the one-variable formula for a possibly nonnormal coefficient quotient, and the exact conversion from (11) to (12).
That review requested no mathematical correction and also used no network.
It is additional evidence for those specific scalar and normalization checks, not an additional claim that all general analytic arguments received an uninvolved review.

## Scope of the Passed Review

The proof establishes an exact finite-dimensional resolvent-limit formula and proves that it occupies the capacity term in the centered normalization.
The local functional is defined independently from the Fuglede-Kadison determinant, through uniquely specified finite matrix solutions.
Calling it a local affine functional is therefore justified; calling it a known standard capacity or a proved unrestricted infimum would not be justified by this argument.

The final discussion correctly leaves a comparably simple global optimization representation unresolved.
The branch condition at positive regularization is part of the theorem, and an arbitrary stationary solution at zero is not substituted for it.
No statement about bounded invertibility, inverse square integrability, arbitrary non-semicircular inputs, or priority was inferred.
Subject to the explicitly accepted local inputs above, the checked complete argument supports recording Yin_C_F0002 as proved at this exact scope.

## Review of the Determinant Notation Addendum

On 2026-09-12 the user requested a compact determinant expression in place of the exponential trace and normalized root.
The ledger appends [equations (16)-(18)](../../claims/Yin_C_F0002_v1.md#determinant-only-form) without changing the preceding proof.
The earlier review above retains its scope over the preceding complete argument.

The root checked the addition, and another AI agent independently read and checked the appended section without editing it.
For every invertible complex matrix G, multiplicativity and the triangularization identity det(exp X) = exp(Tr X) give exactly the absolute determinant in (16).
Absorbing exp(-1/2) times the identity matrix gives (17); the normalized finite-dimensional Fuglede-Kadison determinant gives (18).
No commutation of A and G, matrix logarithm, or complex-root branch is needed.
Only the nonnegative determinant values need converge.
The finite-regularization qualification from the original proof is retained.

Outcome: the algebraic addendum passed.
This is notation conversion within Yin_C_F0002, not a new mathematical claim or an optimization characterization.
This check was offline and does not extend the earlier source-audit scope.



Original inspection: 2026-09-12.
The original inspection date and checked mathematical scope are retained; the disclosed contribution establishes a self-review relationship.
The related [monotonicity self-review](Yin_R_F0006_v1.md#monotonicity-self-review) is separate evidence; neither scope extends the other's findings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Main argument finding](#scope-of-the-passed-review) | self-reviewed |
| [Notation addendum finding](#review-of-the-determinant-notation-addendum) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Main argument finding](#scope-of-the-passed-review) | [Exact affine statement](../../claims/Yin_C_F0002_v1.md#statement) | Actual 2026-09-12 complete affine determinant statement and covariance obstruction, under the recorded tracial/source inputs; preliminary primitive and uniqueness contributions are disclosed, so this is contributor self-review. |
| [Main argument finding](#scope-of-the-passed-review) | [Main argument](../../claims/Yin_C_F0002_v1.md#resolvent-existence-and-pointwise-uniqueness) | Complete equations (1)-(15), including existence, uniqueness, bilinear trace primitive and additive constant, regularization, zero determinant, covariance obstruction and the three simpler cases; no coverage of the later equations (19)-(22). |
| [Notation addendum finding](#review-of-the-determinant-notation-addendum) | [Determinant addendum](../../claims/Yin_C_F0002_v1.md#determinant-only-form) | Actual same-date checks of equations (16)-(18), multiplicativity and det(exp X), scalar absorption and finite-regularization limit qualifications; the combined account includes the author's self-check, and another agent's rereading alone does not establish isolated-context independence. |
