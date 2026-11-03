---
author: Yin
---

<a id="pp08-u001"></a>
# PP08-U001: rational-affine Gram correction under strict feasibility

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [PP08 author-hosted published-layout PDF](../../../literature/pdf/PP08--published.pdf),Theoretical Computer Science409(2008),269--281,13PDFpages; artifact provenance. Title/authors/venue/year/DOI are verified in the actual primary file. No alternate-edition equivalence asserted.

Passages: Printed272/PDF4,Section2.2 equations(3)--(4) defining the coefficient-affine Gram fiber; printed274--275/PDF6--7,Section3 Assumption1 and rounding context; printed276/PDF8,Propositions7--8 and the adjacent perturbation proof; printed279/PDF11,AppendixA proof of Proposition7.

Inspection: 2026-10-12,Yin. Actual primary PDF downloaded, parsed and retained unchanged after title/ordered-author/page/version checks. Listed passages text-read; printed276 and279 visually inspected from Poppler renderings. Coverage: Read with selected method/proof-step inspection, not a whole-paper or implementation/complexity audit.


## Selected source meaning and role

For rational p and a chosen monomial column z, the source's affine fiber is L={Q symmetric:p=z^TQz}.
Section3's standing Assumption1 is existence of a STRICTLY FEASIBLE Gram.
Proposition7 corrects coefficient-sum errors by their multiplicities, giving the orthogonal projection onto L with rational arithmetic when Q and p are rational.
AppendixA explicitly verifies both exact coefficient matching and orthogonality to the linear kernel.

Proposition8 uses a positive margin epsilon for the numerical matrix, distance delta to L and rounding error tau.
It displays the bound on the projected perturbation by sqrt(delta^2+tau^2); its stated condition tau^2+delta^2<=epsilon^2 concludes POSITIVE SEMIDEFINITENESS.
The selected argument and rational projection supply the known rational-interior mechanism.
This unit does not replace its standing strict-feasibility assumption with mere nonnegativity, or claim every rational semidefinite boundary has rational points.

The source concerns ordinary multivariate polynomial SOS.
It does not by itself establish strict feasibility of a fixed-degree Laurent Gram fiber, the literal real self-star Laurent specialization, rationality of a single spectral factor or the G0001 actual integer-residue/window/cost conclusions.
Those are separate local arguments.
[MSEDSV22-U001](../MSEDSV22/Yin_U001.md#msedsv22-u001) identifies the selected subsequent trigonometric fixed-degree/rounding method.

This is selected known-method attribution for [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), not an imported proof of the project's stronger real-rational Gram lemma or an independent review of that project proof.
No solver/implementation execution, whole-paper audit, full SOS classification, external foundational-proof audit or algorithm-complexity acceptance is asserted.
