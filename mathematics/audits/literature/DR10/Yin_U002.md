---
author: Yin
---

<a id="dr10-u002"></a>
# DR10-U002: outer matrix polynomial factorization on the circle

## Source and inspection

[Source and edition notes](readme.md).

Source edition: The existing [33-page author-hosted survey](../../../literature/pdf/DR10--author-survey.pdf), whose exact edition and acquisition boundary are recorded in the DR10. The author file has no verified mathematical revision date; neither its producer date nor related arXiv or published metadata identifies that date. No equivalence with another edition is asserted.

Passages: Theorem 2.1, printed/PDF p.4; analytic Toeplitz and outer conventions, pp.4--5, including Definition 2.2 and displayed (2.4)--(2.5); proof text through p.6 and uniqueness remark on p.7 read for context.

Inspection: 2026-10-13T06:35. Human author Yin; delegated F0010 matrix-extension AI directly text-read the retained primary artifact using pdftotext, matched the statement, adjoint orientation, degree and outer definition, and checked their finite-matrix applicability. Coverage Read and accepted statement; no independent audit of the entire source proof, no visual page inspection, no original Rosenblum/Rosenblatt proof review, and no uniqueness theorem adopted.


## Exact accepted statement

Let G be a Hilbert space and let B(z)=sum_{k=-s}^s B_k z^k be a Laurent polynomial with coefficients in L(G).
If B(z)>=0 for every z on the unit circle, Theorem 2.1 gives an analytic polynomial H(z)=sum_{j=0}^s H_j z^j, with coefficients in L(G), such that B(z)=H(z)^*H(z) on that circle.
One may choose H to be outer.
Its degree is at most s; trailing coefficients may vanish.

The source defines the analytic Toeplitz multiplier T_H on the one-sided Hilbert direct sum G direct-sum G direct-sum ... .
Outer means that the closure of its range is F direct-sum F direct-sum ... for a closed subspace F of G.
Closure is essential here: bounded invertibility of H on the circle is not assumed.
The source polynomial-factor convention is H^*H, matching (1) of the consuming matrix argument.
The theorem includes nonnegative singular symbols and does not require strict positivity.

## Finite-matrix application and accepted-input decision

For F0010, take G=C^r and B(z)=P(z)^*P(z), with P an arbitrary complex matrix Laurent polynomial.
Shift P by a Laurent monomial to obtain ordinary powers 0,...,s; B has degrees between -s and s, is nonnegative at every circle point, and meets the theorem's hypotheses.
The resulting H is square r-by-r, has degree at most s, and supplies a feasible block coefficient Gram.

This is an established external theorem accepted as a resolved input at the exact statement/applicability scope above under the repository's accepted-external-input rule.
Its original proof is not independently reviewed.
Merely reading pp.5--6 does not upgrade the source to Audited within scope.
The prior [U001](Yin_U001.md#dr10-u001) remains the separate scalar attribution record with its original limited inspection.

The consuming [matrix-capacity argument](../../../claims/Yin_C_F0008_v1.md#matrix-finite-gram-capacity) separately proves the deductions needed for the capacity: when det P is not identically zero, outerness forces F=C^r, point evaluation then makes H(z) invertible throughout the open disk, and scalar Jensen gives the determinant of H(0).
The finite coefficient spectrahedron, its global upper bound for every feasible Gram, exact capacity exponent, singular-locus conclusion and normalization are local deductions, not statements quoted from this source.
Their whole-proof review remains separate.

## Search and unused scope

The reuse check found the retained DR10 scalar unit and artifact, then expanded to pp.4--7 because the matrix extension was explicitly required by F0010.
The registered bibliography and existing artifact suffice; no new source acquisition was attempted.
Theorem 2.1's complete operator proof, its general infinite-dimensional extensions, the source's uniqueness remark, later Schur-complement algorithms, multivariable and noncommutative factorizations are not adopted by this unit.
No rational or integer coefficient factor, degree-uniform numerical condition number, or semicircular determinant formula follows from this acceptance.
