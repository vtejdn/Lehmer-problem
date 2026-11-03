---
author: Yin
---
# Hun74-U006: finite-field extensions, irreducible degrees and Frobenius

Date: 2026-10-18T11:33.
Human record author Yin.
The realization author directly inspected the retained primary pages while constructing the actual Salem family and reread the same rendered pages before this source-unit registration.
This is a selected statement/applicability inspection, separate from the earlier Chapter IV proof audit and its PID unit U006.

<a id="hun74-u006"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Thomas W. Hungerford, Algebra, retained user-supplied 528-page Springer printing in Hun74.pdf; the exact later printing date remains unknown as recorded in the original intake.

Passages: Chapter V Section5, printed pages279--281 / PDF pages305--307; Corollaries5.7--5.9 and Proposition5.10, with Lemma5.5 and Proposition5.6 supplying the adjacent Frobenius and splitting-polynomial conventions.

Inspection: Exact statements, field/cardinality hypotheses, prescribed-degree quantifiers and the displayed Frobenius mechanism were read directly from rendered primary pages. The source's proofs and proof sketches were not subjected to a new complete proof audit; Corollary5.9 leaves its proof as an exercise using5.8 and1.6, whose complete exercise solution is not claimed to have been source-audited.


For every prime p and integer n>=1, Corollary5.7 gives a field with p^n elements and uniqueness up to field isomorphism.
For every finite field K and integer n>=1, Corollary5.8 gives a finite simple extension F=K(u) of degree n, and any two degree-n extensions are K-isomorphic.
Corollary5.9 supplies an irreducible polynomial of degree n in K[X] for every such K,n.
Dividing its nonzero leading coefficient gives a monic irreducible polynomial of the same degree, which is the normalization used by the project.

Proposition5.10 states that every finite-degree extension F/K of finite fields is finite and Galois, with cyclic Galois group.
Lemma5.5 identifies x maps to x^(p^r) as an injective homomorphism in characteristic p and as an automorphism on a finite field.
Proposition5.6 realizes a field of cardinality p^n as the splitting field of X^(p^n)-X over the prime field.
The proof sketch of5.10 explicitly identifies x maps to x^p as a generator for the extension over the prime field; for K of cardinality q=p^b, its b-th power x maps to x^q generates Gal(F/K).
In the project residue fields over F_2, the convention is therefore arithmetic Frobenius x maps to x^2.

These established statements are accepted at their checked statement/applicability scope.
The project uses finite fields with prime cardinalities exceeding j, and degrees j,j-1,2, to prescribe the squarefree factor patterns (j),(j-1,1),(2,1,...,1).
The degree-at-least-two irreducible factors have no root in the base field, and enough distinct linear factors exist because that field has more than j elements.
Separability follows from the finite-field Galois statement.
The same interface supplies the notation and cardinality of the residue field F_(2^ell).

No number-field realization, global Frobenius lift, Hensel neighborhood, simultaneous real-root condition, unit-lattice argument or Salem construction follows from this source unit alone.
Those are separate project or source inputs in the consuming proof.
The finite abelian group decomposition used elsewhere remains in [Hun74-U005](Yin_U005.md#hun74-u005), not in this finite-field unit.
The original intake owns the artifact identity and acquisition facts; no new source acquisition or printing identification is asserted.
