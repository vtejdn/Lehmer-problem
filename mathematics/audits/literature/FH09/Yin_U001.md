---
author: Yin
---

<a id="fh09-u001"></a>
# FH09-U001: the exact-dimensionality input for finite affine systems

## Source and inspection

[Source and edition notes](readme.md).

Source edition: FH09; [retained PDF](../../../literature/pdf/FH09.pdf).

Passages: Retained arXiv:1002.2036v1, 10 February 2010; published CPAM 62 (2009). Definitions and conventions on printed/PDF pp. 4--7, especially Definitions 2.4, 2.5 and 2.7 and Theorem 2.8 on p. 7.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148. Coordinator checked the primary PDF statement, nearby definitions, arXiv metadata and rendered p. 7. The original proof of Theorem 2.8 was not reviewed. This is statement/applicability inspection and acceptance of an established external input, not a full proof audit.


## State and exact input

**Read; accepted external theorem at statement and applicability scope.**
Theorem 2.8 treats the pushforward under a conformal $C^1$ iterated-function-system coding map of a shift-invariant measure.
Its pointwise dimension is the ratio of pointwise projection entropy to the Lyapunov exponent.
In the ergodic case this is almost surely constant, so the pushforward is exact dimensional.
Only this exact-dimensionality consequence is accepted here.

The source's projection entropy is a conditional-entropy difference associated with the coding map.
It is not defined as the entropy rate of complete finite affine maps.
Identifying these quantities requires an additional theorem; neither their names nor the acceptance here identifies them.

## Applicability to Ope26d

For a finite indexed family $x\mapsto r_i x+t_i$ on $\mathbb R$ with $0<|r_i|<1$, choose a sufficiently large compact interval invariant under all maps.
They extend to smooth invertible maps on an open neighborhood, with derivative norm and least singular value both $|r_i|$; they are conformal.
The Bernoulli coding measure for a positive probability vector is shift invariant and ergodic.
Negative ratios preserve the derivative-norm condition, and repeated indexed maps are allowed.
No separation hypothesis is needed.

Thus [Ope26d-U001](../Ope26d/Yin_U001.md#ope26d-u001) may use the existence of a constant local dimension.
The elementary conversion between that constant, lower Hausdorff measure dimension and full-mass Hausdorff dimension is separately explained in the consuming manuscript.
The entropy-rate formula itself is not supplied by this dependency.

## Search, limits and downstream use

The source was pursued because it is the external exact-dimensionality premise explicitly cited in family148.
The exact arXiv version, author/title and journal reference were verified.
Theorem 2.8 and its hypotheses were available in the primary text, so no secondary report was substituted.
No concrete objection to this specialization was found.
The original projection-entropy theorem proof, nonconformal parts, and historical priority are outside this unit.
No Lean theorem or kernel execution is asserted.
