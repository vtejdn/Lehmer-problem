---
author: Yin
---

# BV04-U003: original matrix-inversion-lemma inspection for the changed bulk proof

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Boyd and Vandenberghe, Convex Optimization, published2004; the existing registered author-hosted seventh printing with corrections2009, [BV04.pdf](../../../literature/pdf/BV04.pdf), with source identity and artifact baseline. No new source bytes or acquisition.

Passages: Preliminary AppendixA.5.5, printed646--651/PDF660--665; exact SectionC.4.3, printed677--679/PDF691--693, complete proof at printed678/PDF692, equations(C.7)--(C.9) and the ensuing general inverse identity.

Inspection: Original2026-10-10 bounded text inspection by the joint_boundary_research reviewer for Yin, recorded inside the R_G177 whole review completed at 2026-10-10T13:35; a separate exact reading instant was not recorded. Exact C.4.3 argument read, adjacent numerical-complexity context not adopted.


<a id="bv04-u003"></a>
## Exact statement, hypotheses and proof mechanism

For a nonsingular real n-by-n matrix A and rectangular real update factors B of size n-by-k and C of size k-by-n, suppose I_k+C A^(-1)B is nonsingular.
The source gives the matrix inversion lemma, named there also the Sherman-Woodbury-Morrison formula:

    (A+BC)^(-1)
      =A^(-1)-A^(-1)B(I_k+C A^(-1)B)^(-1)C A^(-1).

No symmetry or positive definiteness of A is assumed.
The complete selected proof sets y=Cx in (A+BC)x=b, eliminates x, solves (I_k+C A^(-1)B)y=C A^(-1)b and substitutes back for arbitrary b.
The required nonsingular base and small inverse are explicit; no numerical-stability or complexity guarantee is part of this accepted interface.

## Actual original reading and applicability

The [complete original inspection account](../../reviews/Yin_R_G0177_v1.md#changed-bulk-complete-independent-review) records bounded pdftotext extraction with layout.
Printed646--651 first supplied adjacent Schur and symmetric block-inverse material, but did not contain the exact rank-one identity.
One within-book text search then located the exact C.4.3 passage, whose full selected argument was read on printed678.
This was neither a rendered-page nor whole-book audit, and supplied no new acquisition.
Earlier BV04-U001 and U002 retain their distinct source passages, dates/readers and proof-depth boundaries.

For the [original changed-bulk argument](../../../ledger/Yin_L_G0352_v1.md#changed-neutral-cell-coupling), the base matrix is the displayed B, the update column is -t alpha v and the update row is v^T.
Its small denominator is 1-t alpha D/Delta.
The source is stated over real matrices; extension to the actual rational-function calculation over Q(t) is supplied by the locally verified algebraic identity and nonzero rational denominators, followed by polynomial continuation.
That extension and the full companion proof are local project mathematics, not an uninspected source theorem or a new matrix-theory claim.

This unit retains the actual earlier source occurrence from R_G177, without rereading the PDF, changing its baseline or reconstructing the old reviewer's isolation.
It supplies classical-method attribution and the exact inspected scope; the local complete proof and actual formal findings retain their separate responsible homes.
