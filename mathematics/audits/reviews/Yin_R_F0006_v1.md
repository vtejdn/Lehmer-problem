---
author: Yin
---

# Affine Semicircular Determinant: Proof Review: historical self-review scope

<a id="monotonicity-self-review"></a>
## Root Check of the Monotonicity Refinement

Date: 2026-09-12.
Reviewer: the coordinating agent, also the author of this addition.
Inspected addition: [equations (19)-(22)](../../claims/Yin_C_F0002_v1.md#monotonicity-and-scalar-infimum) to the previously checked file.
This is a self-review of the new refinement, not an independent review.
The preceding complete argument and determinant notation retain their earlier scoped reviews.

Checked the normalization in (19) directly from (12): log F equals log Delta_epsilon minus one half of the normalized trace of epsilon squared times (Q + epsilon squared I) inverse.
Both blocks of the hermitization contribute the same normalized trace.
With r = epsilon squared, the scalar integrand has derivative r / (2 (q + r)^2) in r; multiplication by 2 epsilon gives exactly epsilon cubed / (q + epsilon squared)^2.
This separately checks the cancellation and sign in (20).
Bounded spectrum and a strictly positive fixed parameter justify differentiation; no inverse of Q or integrability of log Q is assumed.

Strict monotonicity converts the already established limit to the scalar infima (21)-(22), including zero determinants.
At Q = 0 the determinant value is epsilon times exp(-1/2), and at Q = c squared I it is sqrt(c squared + epsilon squared) times exp(-epsilon squared / (2 (c squared + epsilon squared))), consistent with the derivative and both endpoint limits.
The discussion correctly distinguishes this constrained one-parameter infimum from optimization over all positive definite trial matrices.
It makes no claim that the latter representation is impossible.

Outcome: the elementary monotonicity proof passed the root's check.
The Yin_C_F0002 registry retains proved status and explicitly identifies the new refinement as self-reviewed.
No external search, numerical evidence or independent-agent review was used for this addition.


Original inspection: 2026-09-12.
This separated self-review scope retains its original checking relationship.
The related [main-argument contributor review](Yin_R_F0001_v1.md) is separate evidence; neither scope extends the other's findings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Monotonicity finding](#monotonicity-self-review) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Monotonicity finding](#monotonicity-self-review) | [Monotonicity refinement](../../claims/Yin_C_F0002_v1.md#monotonicity-and-scalar-infimum) | Actual 2026-09-12 author self-review of equations (19)-(22): normalized two-block trace, positive-parameter differentiation and sign, strict monotonicity, singular/zero-determinant endpoints, and only the constrained one-parameter infima; no unrestricted matrix optimization or nonexistence result. |
