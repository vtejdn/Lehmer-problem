---
author: Yin
---

<a id="msedsv22-u001"></a>
# MSEDSV22-U001: fixed-degree Gram and rational rounding/projection attribution

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [MSEDSV22 arXiv:2202.06544v2](../../../literature/pdf/MSEDSV22--arxiv-v2.pdf),4October2023,9PDFpages; artifact provenance. Canonical work year2022 is its formal ISSAC publication and first public arXiv year, not the v2 revision year. No publisher-edition equivalence audit.

Passages: Section4,PDFp.5, degree-d monomial Gram definition and strict-positive/positive-definite assertion citing[9,Theorem2.5]; Section5,PDFp.6,Algorithm3 lines11--17 and its continuation at the top ofPDFp.7. Title/version/ordered authors and star/Gaussian conventions onPDFp.1; reference[9] inspected as a citation only.

Inspection: 2026-10-12,Yin. Actual downloaded primary PDF parsed, title/version/page count and unchanged retained bytes checked. SelectedPDFpp.5--7 text-read and visually inspected from Poppler renderings; only the stated paragraphs/equations/algorithm steps were checked for known-method attribution. Coverage: Read, with selected method/statement inspection; no whole-paper or complete algorithm-proof audit.


## Selected source meaning and role

The source works with Hermitian trigonometric Laurent polynomials, with star reversing powers AND conjugating coefficients.
In Section4 it uses v_d=(1,z,...,z^d)^T and a Hermitian matrix of size d+1 satisfying f=v_d^*Qv_d.
It states strict circle positivity is equivalent to existence of a positive-definite Gram of that SAME degree block, attributing the statement to Dumitrescu2017,Theorem2.5.
That original book passage/proof was NOT inspected or acquired here.

Section5 explicitly identifies csos3 as an adaptation of Peyrl--Parrilo's rounding/projection algorithm.
For positive input with Gaussian integer coefficients, Algorithm3 rounds a numerical Gram to Gaussian-rational entries, corrects each diagonal coefficient sum within the SAME d+1 dimension, reflects entries by conjugation and uses LDL to obtain positive rational weights and degree-at-most-d Gaussian-rational polynomial factors.
These selected steps establish the existing fixed-degree/rational-interior METHOD attribution; no implementation, termination, numerical solver, precision/bit-size or complexity theorem is adopted by this unit.
Section4.2/Lemma8 and the other algorithm proofs are outside this inspection verdict.

The REAL rational symmetric specialization, explicit one-entry-per-lag right inverse/positivity bound and the G0001 integer-residue physical-window application are project arguments, not stronger conclusions silently extracted from this source.
No rationality of one real/complex spectral factor is asserted.
The known source mechanism is credited without a novelty claim.
[PP08-U001](../PP08/Yin_U001.md#pp08-u001) owns the separately inspected original rational-affine method attribution.

This unit supports naming and known-method identification for [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), alongside the existing [C_G10v2 Gram construction](../../../claims/Yin_C_G0010_v2.md#rational-positive-laurent-gram-lemma) and [C_G13v2 nonreal lifting interface](../../../claims/Yin_C_G0013_v2.md#nonreal-fixed-inventory-and-lifting-costs).
It is not an independent project-proof review, a full-source audit, a coefficient-field descent theorem, a new arithmetic-cost premise or a uniform Lehmer-gap result.
Local proofs supply every additional real-rational and physical-window deduction.
