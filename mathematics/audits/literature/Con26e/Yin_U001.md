---
author: Yin
---
# Con26e-U001: strong Hensel lifting in complete non-Archimedean fields

Date: 2026-10-18T11:18.
Human record author Yin.
The assigned source-only helper located and read the precise statements, and the realization author reread them in the actual retained PDF.
This inspection supplies no project construction or independent review of the new Salem realization.

<a id="con26e-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Keith Conrad, Hensel's Lemma, undated public 25-page author notes, retained Con26e.pdf. Publication and first-public-release dates remain unknown; the key uses the 2026 inspection-year convention.

Passages: Page 6 Theorem 4.1 and its following comparison with the simple-root form; page 18 Theorem 9.1 and complete valued-field hypotheses; pages 18--19 distinguish the polynomial theorem from additional power-series and ring variants.

Inspection: Exact complete statements and hypothesis/conclusion normalization read directly in the retained source. The helper also read the same primary online passages. The full proofs in Sections 5--6 and the power-series/ring generalizations were not independently audited or adopted.


Let K be a field complete for a non-Archimedean absolute value and let o={x in K: |x|<=1}.
Let f in o[X] and a in o satisfy |f(a)|<|f'(a)|^2.
Theorem 9.1 gives a unique root alpha in o with |alpha-a|<|f'(a)|, and additionally

    |alpha-a|=|f(a)/f'(a)|,
    |f'(alpha)|=|f'(a)|!=0.

For K=Q_p this is Theorem 4.1 on page 6.
In additive valuation notation, its sufficient condition is v(f(a))>2v(f'(a)); a nonzero derivative need not be a unit.
The normalized simple-root case v(f(a))>0 and v(f'(a))=0 is included.
The complete field need not be Q_p itself: finite extensions with their extended absolute values meet Theorem 9.1.

This established theorem is accepted at statement/applicability scope.
It is needed to keep j distinct Q_2 roots when j>2, so they cannot all have distinct reductions modulo 2.
The consumer must check the stronger derivative inequality and disjoint root neighborhoods; the ordinary simple-root-modulo-2 statement alone would not suffice there.
The later reciprocal quadratic has nonzero derivative in its finite residue field and uses the simple-root specialization in the actual completion.
No numerical root computation, root-count experiment or new valuation estimate is supplied by this source unit.

The notes begin with an introduction and have no printed contents list in the inspected front matter.
