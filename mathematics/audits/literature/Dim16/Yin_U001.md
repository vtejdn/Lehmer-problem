---
author: Yin
---

# Dim16-U001: the reported logarithmic-form bound and an all-index cyclic-norm consequence

Date: 2026-10-07.
Source inspection and direct specialization by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

<a id="dim16-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Vesselin Dimitrov, *Convergence to the Mahler measure and the distribution of periodic points for algebraic Noetherian Z^d-actions*, arXiv:1611.04664v2, 1 January 2017; first public version 15 November 2016. Retained [Dim16.pdf](../../../literature/pdf/Dim16.pdf), 450537 bytes, 39 PDF pages.

Passages: Printed/PDF p.29, Section 9, equation (9.1) and its immediately preceding/following hypotheses; p.30 discussion of the degree dependence. Bibliographic identity and version are on p.1 and the versioned arXiv record.

Inspection: The retained identity page and pp.29--30 were rendered and visually read; text extraction was compared. The reported bound is accepted as an external Baker--Wustholz statement, not as a newly proved main theorem of Dim16. Its original transcendence proof and numerical absolute constant were not audited. The paper's main multivariable convergence theorem is not an input to this unit.


**Source interface read and accepted with the guards below.**
The direct specialization and finite-threshold deductions are fixed in C854.
This status does not claim a complete proof audit of the external logarithmic-form theorem, or a full-paper audit of Dim16.

<a id="dim16-reported-bound"></a>
## The exact adopted interface

For a nontorsion nonzero algebraic number beta of degree D with bounded absolute logarithmic Weil height, Dim16 (9.1) reports

    -log|beta^b-1| <= kappa D^4 log D max(h(beta),1/D) log b.       (1)

The source says the implied constant is absolute.
We use only D>=2, b>=2 and h(beta)<=1.
Increasing kappa if necessary, fix one absolute kappa>=1 valid on this bounded-height scope.
No numerical value of kappa is supplied or certified by this unit.

The displayed source discusses b in N, but its literal log b right side at b=1 is not a valid general upper bound.
We therefore adopt (1) only for b>=2; the n=1 cyclic-norm case below is established separately by integrality.
Degree-one nontorsion algebraic units do not occur.
The source's D in Section 9 is algebraic degree, whereas its d elsewhere often counts variables; they are not interchangeable.
The h(beta) in (1) is Weil height, not coefficient height.

The source attributes (1) to Baker--Wustholz, with its references [9] and [10].
We have read the reported specialization, not those original proofs.
Its p.30 discussion of a possible much stronger bound is explicitly hypothetical and is not adopted.
Historical statements there about the state of the art are not current-status conclusions.

## Fixed local deduction

The complete all-index cyclic-norm statement, original-root normalization, n=1 integrality guard and finite threshold are retained in [C854](../../../claims/Yin_C_G0854_v1.md#statement).
Its genuine 2026-10-07 checking scope below is preserved without a new mathematical assessment or a new reading of the original logarithmic-form proof.

## Relation to retained sources and actual review

The retained War05 periodic-point interface supplies a per-input asymptotic limit and keeps its Baker input external.
The inspected Smy08 Fejer/Blanksby interfaces do not themselves supply the all-n rate (2).
Dim16 (9.1) is selected for its explicit degree and height dependence; reconstruction of a polynomial from finitely many cyclic resultants is a different question and is not used here.
Only this one additional source was selected in the bounded search.

The source agent performed the stated local PDF inspection and self-checked the local (2)--(5) now retained in C854.
No original Baker--Wustholz proof, full Dim16 proof or numerical constant was independently verified.
The coordinator read the complete unit and independently inspected the rendered original pp.29--30, checking the reported formula, height and degree conventions, exponent-one guard, and hypothetical status of the proposed stronger bound.
It checked the complete direct specialization (2)--(5), now retained in C854, including the all-n threshold and the numerically uncalibrated constant.
Assigned AI review_matrix_completion independently checked those direct deductions and the comparison with L G0076; the original transcendence estimate remained its stated external premise.
Neither check found a substantive defect.
This does not assert independent verification of the original Baker--Wustholz proof or of any uninspected Dim16 theorem.
