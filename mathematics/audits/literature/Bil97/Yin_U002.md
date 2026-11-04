---
author: Yin
---
# Bil97-U002: fixed finite sums of small points with nontorsion pair ratios

Date: 2026-10-18T12:33.
Human record author Yin.
Root proposed the torsion-character-block argument for a fixed finite sum and its zero-output, fixed-output and Salem-monomial consequences.
The entropy_attainment_bridge AI supplies the reuse comparison and complete statement/applicability checks below.
Both are contributors to this application; the earlier R392 review covers U001 only and is not an independent review of this new unit.
This is a direct consequence of the accepted torus Bogomolov theorem, not a new small-point theorem or a claim of priority.
No numerical scan, new Claim or original source-proof audit is performed.

<a id="bil97-u002"></a>
## Read; accepted source and author-checked finite-sum application

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Yuri Bilu, Limit distribution of small points on algebraic tori, Duke Mathematical Journal89(3) (1997), 465--476; same retained Bil97--published.pdf as U001, with printed465 at PDF1.

Passages: Printed465/PDF1 for the absolute projective tuple-height convention; printed474--475/PDF10--11 for the complete Theorem5.1, the torsion-subvariety convention and its Qbar scope.

Inspection: The assigned author directly text-read and visually inspected these passages during the preceding source/application review and reuses their exact accepted statements here. The present weaker pairwise hypothesis, character blocks, zero/fixed-output cases, height bound and own-degree consequence are newly author-checked. No original Bilu, Zhang or Bombieri--Zannier proof audit.


The exact external input and definitions are retained in [U001's Theorem5.1 account](Yin_U001.md#torus-bogomolov-complement).
For any fixed Zariski-closed X in G_m^N over Qbar, let X* remove all torsion subvarieties contained in X, including zero-dimensional ones.
If X* is nonempty, Theorem5.1 gives

    eta_X=inf_(z in X*) H_N(z)>0,
    max_i h_abs(z_i)<=H_N(z)<=sum_i h_abs(z_i).       (1)

The constant depends on the fixed variety and ambient dimension; no effective value or uniformity over varying varieties is used.
The theorem applies to varieties defined over Qbar, which is essential for a fixed algebraic output below.
No Bilu strictness or joint multiplicative independence of the input tuple is assumed in this application.

### Reuse boundary

The accepted [ESS02 nondegenerate-equation statement](../ESS02/Yin_U001.md#ess-exact-counting-bound) counts nondegenerate solutions inside a fixed finite-rank multiplicative tuple group.
The [AV09 sharper count](../AV09/Yin_U001.md#retained-primary-statement) is not adopted for this application.
Neither count is needed here, and neither is silently converted into the present degree-uniform height assertion.
Pairwise nontorsion ratios are not the same hypothesis as the absence of every vanishing proper subsum.
No fixed finite-rank group or subsum-nondegeneracy assumption is imposed below.
The already inspected exact Theorem5.1 is sufficient, so no further literature acquisition or search is needed for this consequence.

## Fixed project consequence

The complete finite-sum statement, torsion-character argument, zero/fixed-output cases, height/finiteness proof and varying Salem-monomial use are retained in [C853](../../../claims/Yin_C_G0853_v1.md#statement).
The [original R394 finding](../../reviews/Yin_R_G0394_v1.md#finite-sum-application-independent-finding) retains its exact earlier source/application scope; R392 remains confined to the earlier U001 application now fixed in C852.
This source unit retains the accepted Theorem5.1 interface, edition and original-source proof limits, without a new project assessment or retroactive source reading.
