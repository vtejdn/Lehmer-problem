---
author: Yin
---

<a id="sch09-u001"></a>
# Sch09-U001: arithmetic minimum and Ryshkov halfspace terminology

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Sch09 retained arXiv v1](../../../literature/pdf/Sch09--arxiv-v1.pdf), Achill Schürmann, *Enumerating perfect forms*, arXiv:0901.1587v1, 12 January2009, 22pages; artifact.

Passages: Introduction equation(2), PDF/printed p.1; quadratic-form/trace conventions in Section2 p.3; Section3 equations(9)--(10), p.5.

Inspection: 2026-10-11T18:15. D11 author directly read the primary arXiv v1 HTML Sections1--3 for these definitions and language, after its PDF fetch failed. Root subsequently acquired/validated the exact v1 PDF, text-read the selected pp.1,3,5 and visually inspected p.5. This is a bounded definition/convention check; no source proof of local finiteness, perfect forms or algorithms is adopted or audited.


For a REAL SYMMETRIC POSITIVE DEFINITE matrix Q of size d, the source defines the arithmetic minimum

    lambda(Q)=min{r^T Q r: r in Z^d, r!=0}.

Its trace pairing is the ordinary UNNORMALIZED pairing <Q,R>=Tr(QR).
Hence r^T Qr=<Q,rr^T>.
Section3 defines the threshold-one Ryshkov region by Q positive definite and lambda(Q)>=1, equivalently r^T Qr>=1 for every nonzero integer vector.
The printed equation(10) writes a parameter lambda while equation(9) fixes threshold1.
The present threshold-one attribution uses lambda=1; a chosen positive threshold c is the immediate rescaling c times that region.
No ambiguity in that printed parameter is imported into a project estimate.

The minimum exists and is positive for positive definite Q: comparison with a positive multiple of the Euclidean squared norm leaves only finitely many integer points below any fixed candidate value.
That elementary fact and the displayed trace identity can be checked directly.
This record accepts the established definition and terminology as attribution, without importing the later local-finiteness theorem, perfection/eutaxy criteria, enumeration algorithm, convex-duality completeness or rational optimizer attainment.

The intended [finite-window integer-moment consumer](../../../claims/Yin_C_G0016_v1.md#integer-moment-author-self-check) supplies its own exact residue map, FINITE nonzero integer rank-one moment hull, rational kernel-noise realization, affine-density argument, Toeplitz/quotient bounds and whole-lattice equality certificate.
This source does not identify that finite hull with its closure and does not prove the consumer's new sufficiency or strong duality.
There is no assertion of original historical priority for this source's definitions.

The canonical bibliography distinguishes the inspected22-page preprint from its published version.
Formal venue/DOI/page metadata were checked using the primary HIM publication list and the AMS indexed contents; the inconsistent volume/end-page in the arXiv abstract's journal-reference field was not silently copied.
No equivalence audit of the preprint and published mathematical proofs was performed.
No Lean or native mathematical program was used in this source inspection.
