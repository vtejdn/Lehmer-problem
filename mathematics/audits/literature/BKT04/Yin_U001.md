---
author: Yin
---

<a id="bkt04-u001"></a>
# BKT04-U001: The prime-field sum-product input for BV19b

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [BKT04 retained preprint](../../../literature/pdf/BKT04.pdf), arXiv:math/0301343v3, 10 March 2006, 29 pages. Acquisition. The bibliographic work was published in 2004; v3 is not asserted byte-identical to the journal article.

Passages: Theorem 1.1 and surrounding field/sum/product definitions, printed/PDF p.1.

Inspection: 2026-10-11, human author Yin; primary statement, title, authors, version margin, quantifiers and application range read directly and visually checked by the same AI auditor. Pages 2--29 and the original proof are unreviewed.


## Accepted statement and coverage

**Read**, with the established theorem **accepted for use at statement/applicability depth**.
This is not an Audited within scope proof assessment.

For each fixed 0<a<1/2 there are constants c(a)>0 and eta(a)>0 such that for every prime p and subset A of F_p,
\[
p^a<|A|<p^{1-a}\ \Longrightarrow\
\max\{|A+A|,|AA|\}\ge c(a)|A|^{1+\eta(a)}.
\]
The constants may depend on a.
This does not state an absolute exponent for all subsets, a result over every extension field, or a result for product rings.

## Exact consumer and limit

[BV19b-U003](../BV19b/Yin_U003.md#bv19b-u003) selects a=min(delta/2,1/16) and applies this input only while p^delta <= |A| <= p^(7/8), for sufficiently large p.
It absorbs the fixed prefactor and supplies the separate elementary large-set covering proof locally in that source audit.

The [arXiv record](https://arxiv.org/abs/math/0301343v3) identifies the exact revision and its separate distance-set correction.
No geometric application or previous-version proof coverage is adopted.
The original sum-product proof, its recursive dependencies, and the rest of this 29-page paper remain outside the requested BV19b dependency check.
