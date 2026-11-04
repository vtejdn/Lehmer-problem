---
author: Yin
---

<a id="gl06-u001"></a>
# GL06-U001: finite Gram lifting of a strictly positive Laurent symbol

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [GL06 arXiv:math/0503133v1](../../../literature/pdf/GL06--arxiv-v1.pdf),7March2005,19pages; artifact. Published identity is Journal of Approximation Theory139(2006),327--345; no version-equivalence audit.

Passages: Section2, especially the diagonally normalized Gram entries on p.5 and the finite Toeplitz/remainder positivity argument on pp.6--7.

Inspection: 2026-10-12, Yin; mathematical author directly read selected pp.3--7. Root text-read title/version and pp.5--7 and visually inspected p.5. Full source and cited matrix Fejer--Riesz/Dritschel proofs not audited.


The source distributes each Laurent coefficient across its Gram diagonal using the reciprocal of that diagonal's length.
For dimension M=m+1 this gives entries h_(j-i)/(M-|j-i|) in the scalar case.
It compares this Gram matrix with a scaled Toeplitz section of the positive symbol and bounds the remainder to obtain positivity for sufficiently large dimension.

This checked construction supplies classical attribution.
The current one-variable real rational specialization proves its own coefficientwise remainder bound and strict rational positivity threshold, then uses rational LDL with positive rational weights.
It does not assume rationality of a complex spectral factor, import the source's printed numerical remainder constant, or adopt a multivariable factorization theorem.
Index conventions are fixed by the local identity v*Qv=h; the current real self-reciprocal coefficients satisfy h_l=h_-l.

The Hermite correction, polynomial damping, nonzero-value repair, full integer resultants and all window/denominator costs are separate project deductions.
The source establishes none of those arithmetic interpolation conclusions.
The search was triggered by recognizing the finite normalized-Gram mechanism.
[Publisher metadata](https://www.sciencedirect.com/science/article/pii/S0021904505001899) and the [coauthor's institutional list](https://geronimo.math.gatech.edu/publications/) verify publication identity; the exact inspected version remains the preprint above.
No priority claim or whole-paper audit follows.

<a id="original-complementary-lift-reviewer-reading"></a>
## Original complementary-lift reviewer occurrence

The distinct critical_tail_author review of2026-10-12 directly inspected the already retained arXiv math/0503133v1 after an unavailable versioned web fetch.
The actual [R_G216 source account](../../reviews/Yin_R_G0216_v1.md#actual-source-inspection-and-final-limits) reports title/author/version and19pages, complete text reading of PDFpp.3,5,6,7, and a rendered visual check of p.5, including the conjugate/index orientation of the normalized Gram diagonal entries.
Its individual source-reading minute is unrecorded; the00:23 review minute and00:22 project author freeze are not substituted for it.
The original Fourier/Gram/perturbative attribution is the same inspected version; the project proves its own coefficient error constant and rational LDL rather than adopting a source numerical constant, multivariable theorem, complex spectral factor or cited Fejer--Riesz/Dritschel proof.
No whole-paper or published/preprint equivalence audit was performed; the original source-render byproduct was removed.
This retention adds neither a new source reading nor acquired bytes.
