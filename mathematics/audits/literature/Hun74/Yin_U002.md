---
author: Yin
---

# Free Modules and Vector Spaces

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained user-supplied published printing of Hungerford’s *Algebra*, 528 PDF pages; original retrieval origin unknown; exact printing and artifact evidence.

Passages: Source: Hun74 printing, §IV.2, pp. 180–190 / PDF pp. 206–216.

Inspection: Review: 2026-09-10, the coordinating agent, self-review; numbered main results and their proof mechanisms audited within scope.


Retained user-supplied published printing of Hungerford’s Algebra, 528 PDF pages; the original retrieval origin is unknown.

## Hun74-U002

- Source: Hun74 printing, §IV.2, pp. 180–190 / PDF pp. 206–216.
- Review: 2026-09-10, the coordinating agent, self-review; numbered main results and their proof mechanisms audited within scope.
Main text ends p. 188; exercises on pp. 188–190 are not exhaustively audited.
- Inputs: [module/direct-sum conventions](Yin_U001.md#module-conventions), Zorn's lemma, elementary cardinal arithmetic with choice, and the specified elementary ideal/field facts.
These set-theoretic and Chapter III foundations are retained, not independently proved here.

<a id="free-module-and-basis"></a>
## Definitions

The text on p. 181 defines linear independence using finite relations with coefficients on the acting side.
A basis is a linearly independent generating set.
Under IV.2.1, pp. 181–182, a unitary left module is free iff it has a basis, iff it is a direct sum of copies of R, iff maps from its basis into any unitary left R-module extend uniquely to module homomorphisms.
The zero module is free on the empty basis.
The source's main free-module convention over a ring with identity is the unitary one; it separately warns about free objects in the category allowing nonunitary modules.

**Definition IV.2.8, p. 185.**
A nonzero ring with identity has the invariant dimension property when all bases of any free module have the same cardinality; in that setting the cardinality is its rank.
For vector spaces the term dimension is used.
This is not a definition of inner matrix rank, von Neumann dimension or the complex rank of an operator.

<a id="division-ring-bases"></a>
## Division-Ring Basis Interface

**Theorem IV.2.4, p. 183.**
Every left vector space over a division ring D has a basis; every linearly independent subset is contained in a basis.
There is no finite-dimensionality or commutativity hypothesis.
The same statement for right vector spaces follows by passage to D-opposite, which is again a division ring.

The proof uses Zorn's lemma on independent subsets containing the prescribed set.
Unions of chains are independent because each relation involves finitely many vectors.
If a maximal independent set failed to span, adjoining an outside vector would stay independent: a nonzero coefficient can be inverted **on its correct side** to solve for that vector.
This is Lemma IV.2.3.
No topology or boundedness is involved.

This exact source input is accepted for the right-basis extension reported under former Yin_C_F0035-P1.
The [original project proof and actual review scope](readme.md#original-equalizer-use) are located in the fixed source collection; this source input alone supplies no local equalizer proof or new adoption.
Its unitary module hypothesis holds because the division subring and ambient ring share their identity.

## Remaining Main Results and Proof Checks

| Result and locator | Scope and checked mechanism |
| --- | --- |
| IV.2.1, pp. 181–182 | Basis, sum-of-copies and free universal property are equivalent in the unitary category. Send coordinate units to the basis elements; unique finite coefficient expansions give the maps and inverses. |
| IV.2.2, pp. 182–183 | Every unitary module is a quotient of a free module; finite generation permits a finite free cover. Use a free module on a generating set and evaluate its basis. |
| IV.2.5, pp. 183–184 | Every spanning set of a division-ring vector space contains a basis. A maximal independent subset of that set must span it, by the same adjoining-vector argument. |
| IV.2.6, pp. 184–185 | Over a nonzero ring with identity, if a free module has an infinite basis, every basis has the same infinite cardinality. Expand basis vectors in finite supports in each other; the reverse expansions bound the fibers needed for the cardinal comparison. A finite basis cannot span infinitely many independent basis vectors. This does not prove the finite invariant dimension property for an arbitrary ring. |
| IV.2.7, p. 185 | Division-ring bases have equal cardinalities. The infinite case uses IV.2.6; the finite case is the exchange argument with invertible nonzero coefficients. |
| IV.2.9, p. 185 | Over a ring with the invariant dimension property, free modules are isomorphic iff their ranks agree. Transport a basis for necessity, match bases for sufficiency. |
| IV.2.10, pp. 185–186 | For a proper two-sided ideal I and free F, F/IF is free over R/I with the images of the original basis. Independence follows by testing the finite coefficients modulo I. |
| IV.2.11–2.12, p. 186 | A nonzero quotient ring with the invariant dimension property passes that property back to R. In particular a division-ring quotient suffices; every nonzero commutative ring with identity has the property via a maximal ideal and its field quotient. Existence of maximal ideals is a retained standard Zorn application. |
| IV.2.13, p. 187 | For a subspace W of V over a division ring, dim(W) is at most dim(V), and dim(V)=dim(W)+dim(V/W). Equality of subspace and ambient dimension forces equality of spaces only when the ambient dimension is finite. Extend a basis of W to one of V and use the complementary cosets. |
| IV.2.14–2.15, p. 187 | Adapted bases, rank-nullity, and the finite-dimensional sum/intersection formula. Use the quotient basis and first/second isomorphism theorems. Cardinal addition in the infinite case must not be cancelled. |
| IV.2.16, p. 188 | For division rings R contained in S contained in T, the left dimensions multiply: dim_R(T)=dim_S(T) dim_R(S). If u is a left S-basis vector of T and v a left R-basis vector of S, the product basis uses **vu**, as follows by two successive left expansions. |

The familiar complement consequence (also Exercise IV.2.5, p. 189) is immediate from basis extension: every subspace of a division-ring vector space has an algebraic complement.
It is not true that every module over a general ring is free, or that submodules of arbitrary free modules are free.
The source's p. 183 warning explicitly separates those cases.
Finite-dimensional injectivity/surjectivity tests follow from rank-nullity with the finite-dimensional assumption retained.

## Acceptance and Review Boundary

The basis and dimension results above are accepted standard external inputs with the displayed algebraic hypotheses.
The review reconstructs the finite-support, exchange and quotient interfaces, not the foundations of choice/cardinal arithmetic.
No assertion about a continuous dual, a Hilbert basis, a bounded functional or a completed tensor follows from these results.
The earlier account reports an independent artifact review under former Yin_C_F0035, whose original home remains unlocated; this source attribution is self-reviewed and establishes no current project review selection.
