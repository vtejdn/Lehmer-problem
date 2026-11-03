---
author: Yin
---

# BV04: contextual optimization references

Source: Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge University Press, 2004), retained author-hosted seventh printing with corrections (2009).
Bibliographic identity and artifact facts are in the [canonical bibliography](../../../literature/references.bib); the local artifact is [BV04.pdf](../../../literature/pdf/BV04.pdf).

## Scope and actual inspection

Selected passages were read on 2026-10-10.
This is a contextual source reading, not a whole-book audit or acceptance of a general optimization algorithm for affine determinant functionals.
The title and copyright pages identify the authors, edition, publication year and seventh printing.

- Section 3.3, Example 3.22, printed p.92 (PDF p.106), computes the conjugate of a strictly positive quadratic form.
  On the real Hilbert space of Hermitian matrices, a quadratic form with strictly positive operator `C_c+eta`, where `C_c(x)=cxc` and `c>0`, has its square completion expressed by the inverse of that operator.
  Strict positivity is a necessary separate hypothesis.
  Neither attainment of a remaining infimum nor interchange of extrema follows from this conjugacy.
- Appendix A.5.5, printed pp.650--651 (PDF pp.664--665), derives Schur elimination of a variable from a quadratic form.
  Eliminating a maximizing variable gives the reduced Hessian by this block operation, with its sign determined by the negative Hessian in that variable.
  Positive-definiteness and global conclusions require separate arguments.

The displayed elementary calculations and their quadratic-form specializations were checked.
No surrounding algorithmic or complexity results were reviewed or transferred.
Other chapters remain outside the present scope.
No source prose was reused.


<a id="selected-weak-duality-attribution"></a>
## Bounded weak-duality method attribution for G0001

At 2026-10-10T11:22, root AI for Yin directly text-read the existing BV04.pdf at printed215--219 (PDF229--233).
The exact consumed passage is Section5.1.3, printed216/PDF230, equation(5.2) and its complete displayed proof, with the Lagrangian definitions from Sections5.1.1--5.1.2.
Root visually inspected rendered PDF230 to confirm the componentwise nonnegative multiplier condition which text extraction encoded ambiguously.
The standard-form linear-program illustration on printed219 was also read, as a comparison only.
The prior quadratic-form inspection above is unchanged.

The source proves that each feasible dual lower bound lies below every primal feasible objective, for inequality multipliers nonnegative and equality multipliers unrestricted.
This bound does not require convexity.
The [D195 arithmetic bundle investigation](../../../ledger/Yin_L_G0328_v1.md) uses precisely this weak-duality certificate method: its own finite coefficient inequality is multiplied by nonnegative weights and combined with its exact normalization and surplus constraint.
The local argument proves that inequality directly with its actual H,r,v,y and scalar parameters; source notation for multipliers is not imported as a change of convention.

No strong-duality theorem, existence/attainment of an optimal pair, simplex correctness, solver termination or floating-point certificate is adopted from this source.
Matching actual rational feasible upper and lower witnesses can establish optimality by the elementary lower-bound implication; failure to find such witnesses proves no obstruction.
This is bounded classical-method attribution and hypothesis inspection, not a whole-book review or new source acquisition.
The complete local proof and all native numerical certificates retain their own independent-review obligations.

<a id="selected-tangent-method-attribution"></a>
## Bounded first-order tangent method attribution for full-surplus geometry

On 2026-10-10T13:01, joint_boundary_research AI for Yin directly text-read the existing canonical BV04.pdf at printed68--71 (PDF82--85), using pdftotext with explicit page limits and layout preservation.
The precise consumed method is Section3.1.3 at printed69, equation(3.2): on an open convex domain a differentiable convex function lies above each affine first-order approximation.
The complete proof at printed70 was read, including the one-variable limiting argument, its converse and the line restriction giving the multivariate condition.
The concave reversal at printed70 and the logarithm example at printed71 were also read as adjacent context.
This is a bounded text inspection, not a rendered-page or whole-book audit.
Two attempted optional Python PDF libraries were unavailable; their import failures supplied no source evidence.
The available pdftotext extraction then produced the actual selected text.

The [D213 full-surplus argument](../../../ledger/Yin_L_G0347_v1.md#exact-tangent-union) uses the classical first-order tangent method with the ACTUAL scalar function f(S)=S log(S/2), on the open interval S>0.
Its derivative is 1+log(S/2), and its second derivative is 1/S>0.
Its tangent at s is therefore [1+log(s/2)]S-s.
Adding the exact linear term 2L gives the halfspace family used there.
D213 directly proves the precise difference S[(s/S)-1-log(s/S)] and its nonnegativity, so no general convex-optimization theorem or new regularity assumption is needed as an external premise.
Root's contribution of the tangent family and elementary logarithmic proof remains explicitly attributed in D213; this source note supplies classical method attribution and does not alter that contribution boundary.

No source statement about superlevel convexity, exact nonlinear optimization, finite-grid boundary completeness, parametric LP convergence or solver guarantees is imported.
Those matters are separately proved or explicitly limited in D213.
In particular convexity of f does not make its superlevel feasible set convex.
The prior weak-duality and Schur inspections above remain unchanged; this does not upgrade their scope or constitute a new source acquisition.

[U001](Yin_U001.md#bv04-u001) separately records the newly checked finite-dimensional separation/support passages at printed46--51 for G0001 Toeplitz completeness.
Earlier selected inspections above are unchanged.

[U002](Yin_U002.md#bv04-u002) retains the distinct original quadratic/Schur, weak-duality and tangent inspections above, with their actual dates/readers and depth limits.
This additional source home performs no new PDF reading or acquisition and does not broaden U001.

[U003](Yin_U003.md#bv04-u003) retains the distinct original R251 review-time inspection of SectionC.4.3 at printed677--679, its complete matrix-inversion-lemma argument and the preceding unsuccessful adjacent-passage match.
The original real-matrix source scope, Q(t) local-extension boundary and actual reading method remain separate from the earlier units; no new PDF reading occurs.
