---
author: Yin
---

<a id="ds17-u002"></a>
# DS17-U002: original bounded-support reading and sparse coefficient-height mechanism

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Existing retained arXiv:1606.04376v2,23 January2017,7 pages; original2026-10-06 source inspection retained, no acquisition, PDF overwrite or publication-equivalence audit.

Passages: Theorem1 p.1, derivative/reciprocal proof p.3, Theorem2 p.2 and Section4 p.5, with exact monomial and external-foundation limits below.

Inspection: Original2026-10-06 coordinating-agent statement/mechanism reading and selected renders; pp.2/5 and the additional height-proof p.3 were visually inspected as originally recorded. The assigned agent's p.3 calculation and coordinator readback remain original checks, not a newly established isolated full source audit.


## Complete original source account

Source and acquisition:.
Reviewer/date: coordinating AI for Yin, 2026-10-06; self-review only.

<a id="bounded-support-gap"></a>
Accepted external input: Theorem 2, retained v2 p.2, gives, for every fixed K, an eta_K>0 such that a nonzero integer polynomial with at most K nonzero coefficients has m=0 or m>=eta_K.
Neither irreducibility nor a degree bound is required.
Only this univariate consequence is used.

The statement and Section 4 proof on p.5 were read and visually checked.
The finite-coefficient reduction uses Corollary 2; closedness and isolation for each fixed coefficient tuple use reference [13], Theorems 1 and 2.
Those original proofs, and the earlier explicit sparse bounds, remain external and were not audited.
For tuple sets not containing zero, closedness supplies a neighborhood avoiding zero; this completes the displayed finite-union step.

Boundary correction: Corollary 2's formula must use K>=2.
For a single monomial M=h, so the printed expression h/2^(K-2) would incorrectly give 2h at K=1.
Theorem 2's one-term case instead follows directly from m(a*z^n)=log|a| for nonzero integer a.
Zero polynomials are excluded throughout.
No whole-paper proof audit is claimed.

<a id="sparse-height-bound"></a>
Additional accepted input, 2026-10-06: Theorem 1, retained PDF p.1, states h(f)<=2^(s-2)M(f) for a univariate complex polynomial with s>=2 nonzero terms, after removing any initial monomial.
Here h is coefficient height and M is multiplicative Mahler measure.
For at most K terms with K>=2 the bound h(f)<=2^(K-2)M(f) follows; when the actual support has one term use M=h directly.
The printed general-case proof on p.3 needs this separate monomial branch, just as the earlier Corollary 2 observation does.

Assigned AI review_matrix_completion independently checked the p.3 derivative/reciprocal induction and its support count; the coordinator checked the extracted argument and visually inspected the rendered page.
The induction uses M(f'/d)<=M(f), attributed in DS17 to its reference [9], Mahler's 1961 derivative paper.
That original proof remains an accepted external input via DS17 and was not acquired or independently audited here.
This additional scope does not close the original dependencies of Theorem 2.

The independent wording in that original source-check description is not a new certification of the old agent's context.
The actual selected proof mechanism, derivative inequality accepted through reference9 and uninspected original foundations remain exactly as recorded.
The later2026-10-12 [U001](Yin_U001.md#ds17-u001) accepts the bounded-support gap at its own separate inspected date and scope; it does not replace this original coefficient-height reading.
