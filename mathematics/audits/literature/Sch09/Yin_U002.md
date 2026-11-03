---
author: Yin
---

<a id="sch09-u002"></a>
# Sch09-U002: a dimension-dependent upper bound for the arithmetic minimum

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Sch09 arXiv v1](../../../literature/pdf/Sch09--arxiv-v1.pdf), 12January2009,22pages, artifact, unchanged.

Passages: Section2, sphere-packing density/volume identities and Hermite-constant definition(6), p.4; equation(8) and its density/ellipsoid explanation, p.5. Theorem2 on p.5 is adjacent context, not a newly re-audited foundational proof.

Inspection: 2026-10-11T18:32. Root AI for Yin directly text-read the selected pp.4--5 and visually inspected p.5, after verifying source identity/version and the preceding positive-form conventions. Accepted classical upper bound at exact statement/applicability scope with the displayed elementary packing/volume conversion checked. No whole-survey, enumeration or original Minkowski proof audit.


For every real symmetric positive-definite d-by-d matrix Q, let lambda(Q)=min_(0!=r in Z^d) r^T Q r and let kappa_d be the volume of the Euclidean unit ball in R^d.
The selected bound is

    lambda(Q)<=C_d (det Q)^(1/d),
    C_d=4/kappa_d^(2/d).

This is the classical dimension-dependent lattice bound recorded as source equation(8).
The selected source derives it from the packing-density bound<=1 and the sphere/ellipsoid volume expression.
Those identities and the direction of the implication were checked.
The coefficient C_d is not a dimension-independent constant, no sharp Hermite constant or table value is used, and no division of lambda or the trace by d is imposed.

The bound is accepted as an established external input for the [integer-energy capacity asymptotic investigation](../../../claims/Yin_C_G0018_v1.md), whose quotient Q=G_W is proved positive definite in the responsible C16 argument.
That consumer must itself prove every Loewner/determinant comparison, integer-capacity dual interface, original polynomial/degree normalization and fixed-input limit.
This source supplies no uniform conditioning, Toeplitz dual completeness, period estimate, rational optimizer or Lehmer gap.

This new unit preserves [U001](Yin_U001.md#sch09-u001) at its earlier definition/terminology-only scope.
The selected additional inequality has now been checked expressly; the former record is not retroactively enlarged.
No new artifact acquisition or source-version equivalence is asserted.
