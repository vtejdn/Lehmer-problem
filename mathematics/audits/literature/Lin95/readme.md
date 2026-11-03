# Lin95 source reading

Source/version: [registered author PostScript-derived PDF](../../../literature/pdf/Lin95--author-ps-converted.pdf), with its version and conversion.
The journal edition was not obtained or compared; all page numbers below are author/PDF pages.

Trigger/intended use: Yin's explicit request to check the small-entropy-factor argument behind Lin99 and assess its relevance to G0001 while that Task remains paused.
Date/reviewer: 2026-10-18, Yin, prepared by root with self-check of this record.
The reusable detailed proof reconstruction is owned by [Lin99-U001](../Lin99/Yin_U001.md#proof-reconstruction), rather than duplicated here.

## Reading scope and findings

The introduction and the statements of Theorem 2.1, Theorem 3.3, Corollary 3.10, Theorem 4.6 and Theorem 4.10 were read.
Section 4, pp.12-20, was read in detail; its sensitive coding, periodic-block, quotient and interpolation passages on pp.14-20 were checked visually.
The full dimension-theory proof in Section 3 and the minimal-system construction in Section 5 were not audited.

Theorem 4.6 is stated for finite-dimensional compact metric systems and produces arbitrarily small-entropy continuous factors separating a specified pair.
Section 4 actually uses the small-boundary approximation properties obtained in Section 3, rather than dimension directly in the coding or quotient construction.
Lin99 Lemma 6.8 explains how SBP supplies the boundary interface needed for its generalization.
The repeated p-block intersection in Lemma 4.2 handles periodic points through low coding complexity, despite their positive return frequency.
Proposition 4.5 produces a continuous factor from the closure of a possibly discontinuous symbolic coding to the actual quotient space.
It must not be replaced by an assertion that the original indicator coding is continuous.

The Hausdorff-distance formula for fibers on pp.16-17 is not a valid general description of the quotient topology.
Lin99 p.257 explicitly acknowledges the corresponding published-version error.
Using the topology of the closed equivalence relation and any compatible metric makes the subsequent compactness/diameter argument valid; this is the correction used in Lin99-U001.
The damaged Remark 4.7 wording in this author copy is not used for a stronger singleton-fiber conclusion.

<a id="entropy-interpolation"></a>
## Entropy interpolation and its exact dependence

Lemma 4.9 proves that the entropy of the simultaneous countable factor image is the supremum of the entropies of its finite-coordinate images.
Its product metrics should be chosen uniformly bounded, for example by one, so the weighted tails are uniformly small.

Theorem 4.10 states: for a finite-dimensional (X,T), a factor Y_0 with h_top(Y_0)<h_top(X), and r strictly between these values, there is an intermediate factor Y with h_top(Y)=r and factor maps X to Y to Y_0 agreeing with the given map to Y_0.
Its proof uses only arbitrarily small-entropy factors separating pairs, countable subcovers of X times X minus the diagonal, product subadditivity, and Lemma 4.9.
Consequently the same proof can use Lin99 Theorem 6.7 when SBP is assumed; this is also the mechanism described in Lin99's introduction, p.228.

The inspected author p.20 starts with a parameter h below h_top(X)-h_top(Y_0), but subsequently compares total factor entropies directly with h.
To state the valid argument without that target/increment ambiguity, fix the total target r in (h_top(Y_0),h_top(X)) and take the first error budget below r-h_top(Y_0).
At each stage, keep the finite join immediately before its entropy first exceeds r; that join has entropy in (r-delta,r].
If equality occurs, the target has already been reached.
Otherwise append a new separating family with a smaller error budget, and take the limiting countable join.
Lemma 4.9 gives entropy exactly r, while retaining Y_0 as a coordinate preserves the specified intermediate-factor map.
This normalization correction concerns the author version inspected here, not a claim about an uninspected journal passage.

## Scope boundary

The checked Section 4 mechanisms are accepted for the bounded comparison with SBP, with the quotient-topology correction and the interpolation parameter clarification above.
The finite-dimensional approximation theorem is an identified established source input whose full original proof was not audited in this reading.
These factors need not be group quotients, and their entropy increments are not identified with algebraic entropies of successive quotient groups.
