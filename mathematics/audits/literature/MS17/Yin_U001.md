---
author: Yin
---

# MS17: Selected Affine and Spectral Inputs

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: the retained [MS17 PDF](../../../literature/pdf/MS17.pdf), with canonical bibliographic identity in [references.bib](../../../literature/references.bib).

Source passages: Operator-valued semicircular covariance and Cauchy/R-transform relation ; Chapter 9, Definition 10 and Theorem 11(1),(2),(4), printed p. 239 / PDF p. 248; Proposition 13, printed pp. 241-242 / PDF pp. 250-251 ; Earlier locally checked inputs for Yin_C_F0002; exact proof scope and visual evidence remain in the [analytic supplement](#offline-affine-extension-additional-source-interfaces). Selected definitions: Sections 1.11–1.12, Definitions 11–12, printed pp. 14–16 / PDF pp. 27–29; definition-level reading is separate from the analytic interfaces.

Inspection: The Brown construction and probability-measure weak convergence are accepted source inputs, not a claim that their original proofs have been fully independently audited.

## MS17-U001

Date: 2026-09-12.
Source: the retained [MS17 PDF](../../../literature/pdf/MS17.pdf), with canonical bibliographic identity in [references.bib](../../../literature/references.bib).
This is selected local reading for Yin_T_F0008, not an audit of the monograph as a whole.
The user prohibited network searches and downloads during this run.

| Interface | Exact retained-PDF location | Acceptance and use |
| --- | --- | --- |
| Operator-valued semicircular covariance and Cauchy/R-transform relation | Chapter 9, Definition 10 and Theorem 11(1),(2),(4), printed p. 239 / PDF p. 248; Proposition 13, printed pp. 241-242 / PDF pp. 250-251 | Earlier locally checked inputs for Yin_C_F0002; exact proof scope and visual evidence remain in the [analytic supplement](#offline-affine-extension-additional-source-interfaces). |
| Brown potential and measure | Chapter 11, Theorem 5 and Definition 6, printed p. 268 / PDF p. 276, equations (11.6)-(11.7) | Accepted source theorem: for a bounded element in a faithful tracial von Neumann algebra, log Delta(T-z) is subharmonic and its distributional Laplacian divided by 2pi is a probability measure supported in the operator spectrum. |
| Positive regularized Laplacian | Printed p. 269 / PDF p. 277, equation (11.8) | Primary page read and visually checked by the spectral agent and the coordinating agent.
The source uses a regularizer delta; the project spectral module uses delta = epsilon squared. The local derivative and trace-positivity calculation is independently reproduced in the project proof. |
| Hermitized resolvent block and weak regularization limit | Section 11.9, printed pp. 276-277 / PDF pp. 284-285, equations (11.14)-(11.15) | Accepted source probability-measure weak convergence. PDF p. 285 was visually checked by the spectral agent and the coordinating agent. The density normalization follows the explicit 1/(2pi) Laplacian convention; the informal source parenthesis suppresses that factor. |
| Normal specialization | Printed p. 270 / PDF p. 278 | Brown measure agrees with the scalar spectral measure for normal operators. This does not assert normality of an arbitrary affine pencil. |
| Scalar elliptic example | Theorem 9, printed p. 275 / PDF p. 283 | Accepted ellipse and uniform Brown law, including spectrum equality for that specific model. Scalar scaling/rotation and the circular/line degenerations are checked in the consuming module. |

The chapter-specific page offsets above were checked against the retained PDF; a uniform offset from Chapter 9 must not be applied to Chapter 11.

The full consuming derivation and exact formulas are in [Affine Spectral Potentials](../../../claims/Yin_C_F0003_v1.md), with [independent proof review](../../reviews/Yin_R_F0012_v1.md#new-calculations-checked).
The finite Dyson derivative equation, its invertibility at positive regularization and the exact matrix trace factors are project calculations.
The Brown construction and probability-measure weak convergence are accepted source inputs, not a claim that their original proofs have been fully independently audited.

The source interfaces do not give a uniform bound for the inverse Dyson linearization as epsilon tends to zero, pointwise convergence of regularized densities, or equality of Brown support and spectrum for general nonnormal coefficients.
No additional source search or literature-priority conclusion is part of this unit.

<a id="probability-and-freeness"></a>
## Selected probability-space and freeness definitions

The retained selected reading recorded 2026-09-10 covered Section 1.11 and the beginning of Section 1.12, printed pp. 14–15 / PDF pp. 27–28, Definitions 11–12.
These definition and presentation observations are separate from the Chapter 9/11 theorem interfaces above; no new whole-book proof audit is claimed.

For a unital complex algebra A with unital linear functional phi, unital subalgebras (A_i) are free when phi(a_1 ... a_n)=0 for every n>=2 and every centered a_j in A_{i(j)} whose neighboring indices differ.
The equivalent formulation allowing n=1 adds only the already assumed centering condition.
Centered means phi(a_j)=0.
The defining condition is on alternating products, not on arbitrary mixed products.
A noncommutative probability space specifies the unital algebra and functional.
A star-probability setting additionally specifies a star-algebra and positivity of the state: phi(a* a)>=0 for every a.
Faithfulness means phi(a* a)=0 implies a=0; traciality means phi(ab)=phi(ba).
When A is a C*-algebra and phi is a state, the source calls the pair a C*-probability space.
It calls phi nondegenerate when phi(yx)=0 for all y implies x=0 and phi(xy)=0 for all y implies x=0.
The stated equivalence of nondegeneracy and faithfulness for positive states is an accompanying source result, not an extra defining clause.
For a von Neumann algebra, the source's W*-probability space requires a faithful normal state, with normality expressed as weak-star continuity.
Tracial W*-probability additionally requires phi(ab)=phi(ba).
These faithful, normal, tracial and von Neumann assumptions must not be added to every noncommutative probability space.
The source statements were rechecked as retained-PDF text on 2026-10-17T15:44 at printed pp. 15–16 / PDF pp. 28–29; no new visual or proof audit was performed.
The compact centered-product formulation in Definition 11 bridges the abstract condition and its verification in a representation.
The source's different settings must not be compressed into a probability-space label that silently adds or omits hypotheses.
The NS06 definition account separately distinguishes generated unital algebras from generated star-algebras.

## Semicircular source passages and the offline affine input

This original 2026-09-12 source account was retained from [L_F2](../../../ledger/Yin_L_F0002_v1.md) at 2026-10-21T01:19, without reopening the book or re-reviewing the project extension.
The analytic-dependency reader checked Chapter 9 Definition 7/equation (9.16), p. 236 / PDF 245, Remark 9 pp. 237-238 / PDF 246-247, Definition 10(2) p. 239 / PDF 248, and the norm discussion after equation (9.5), p. 231 / PDF 240.
Printed pp. 231 and236 were visually inspected.
These supply the ordered semicircular pairing convention and faithful-norm interface; the complete consumed pairing induction is already retained in [MS24-U002](../MS24/Yin_U002.md#pairing-estimates).
The source's wider general cumulant/freeness/subordination foundations remain accepted rather than fully re-proved.

<a id="offline-affine-extension-additional-source-interfaces"></a>
On 2026-09-12 the user asked for the determinant formula with a deterministic coefficient matrix and prohibited network searches for this exploration.
The local MS17 Chapter 9 interfaces were checked at Definition 10 and Theorem 11(1), (2), (4), printed p. 239 / PDF p. 248, especially equation (9.20); Proposition 13, printed pp. 241-242 / PDF pp. 250-251; and equation (9.5), printed p. 231 / PDF p. 240, with the continuation discussion on printed p. 232 / PDF p. 241.
PDF p. 248 was also rendered and visually inspected.
These passages supply operator-valued semicircular cumulants, matrix/scalar cumulant compatibility and the Cauchy/R-transform relation, with no extra matrix-size factor in the covariance.
