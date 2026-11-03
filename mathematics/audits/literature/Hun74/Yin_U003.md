---
author: Yin
---

# Projective and Injective Modules

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained user-supplied published printing of Hungerford’s *Algebra*, 528 PDF pages; original retrieval origin unknown; exact printing and artifact evidence.

Passages: Source: Hun74 printing, §IV.3, pp. 190–199 / PDF pp. 216–225.

Inspection: Review: 2026-09-10, the coordinating agent, self-review; main statements and proof chain audited within scope.


Retained user-supplied published printing of Hungerford’s Algebra, 528 PDF pages; the original retrieval origin is unknown.

## Hun74-U003

- Source: Hun74 printing, §IV.3, pp. 190–199 / PDF pp. 216–225.
- Review: 2026-09-10, the coordinating agent, self-review; main statements and proof chain audited within scope.
Exercises pp. 198–199 surveyed, not exhaustively solved.
- Dependencies: [exactness/splitting](Yin_U001.md#exact-sequences), [free covers and bases](Yin_U002.md#hun74-u002), Zorn's lemma, and the elementary additive properties of the rational numbers.
No operator-algebra injectivity theorem is involved.

<a id="projective-injective-definitions"></a>
## Definitions and Equivalent Criteria

**Definition IV.3.1, pp. 190–191.**
P is projective if every map P to C lifts through every surjective module map B to C.
**Definition IV.3.6, pp. 193–194.**
J is injective if every map A to J extends across every injective module map A to B.
The source initially formulates these for modules generally.
In the unitary setting over a ring with identity it explains why testing unitary modules suffices.
For example, any module A decomposes as 1A plus the submodule annihilated by 1; maps from a unitary module land in 1A.

The equivalences with direct summands, splitting and exactness of Hom are theorems, located here and in [U004](Yin_U004.md#hom-exactness).
They are accepted known characterizations, not new project Claims.

## Proof Audit

| Result and locator | Content and verified mechanism |
| --- | --- |
| IV.3.2, pp. 191–192 | A free module is projective. Choose a preimage of each basis image under the surjection and extend linearly by the universal property. |
| IV.3.3, p. 192 | Every module has a surjection from a projective module. In the unitary category the free cover of IV.2.2 suffices. The source also discusses the appropriate free objects for the general nonunitary category; it does not identify those with unitary free modules. |
| IV.3.4, pp. 192–193 | P is projective iff every short exact sequence ending in P splits iff P is a direct summand of a free module. Lift the identity for the first implication, split a free cover for the second, and restrict a lift on the free overmodule for the converse. |
| IV.3.5, p. 193 | A direct sum is projective iff each component is. Lifts from the components assemble by the direct-sum universal property; projection and inclusion recover each component's lifting property. |
| IV.3.7, p. 194 | A product is injective iff each factor is. Extensions are taken coordinatewise; projections/inclusions give the converse. This is a product assertion, not a general direct-sum assertion. |
| IV.3.8, pp. 194–195 | For a unitary J over a ring with identity, injectivity is equivalent to extending every map from a left ideal to R. For sufficiency take a maximal partial extension h on H inside B. For b outside H set L={r:rb belongs to H}; extend r to h(rb) from L to a map k on R and put c=k(1). The extension on H+Rb is h(a)+rc. If two expressions agree, their scalar difference lies in L, which proves representation independence. It strictly extends h, a contradiction. |
| IV.3.9, pp. 195–196 | An abelian group is divisible iff it is injective as a Z-module. Extension from nZ solves n times x equal to a given element; the zero ideal has the zero extension. Apply IV.3.8 for the converse. |
| IV.3.10, p. 196 | Every abelian group embeds in a divisible group. Write it as F/K for a free abelian group F, embed F into the direct sum of copies of Q on its basis, and pass to the quotient by K. Direct sums of divisible groups and their quotients are divisible, by solving each finite-support equation. This direct-sum observation, rather than the product statement IV.3.7 alone, justifies this step. |
| IV.3.11, pp. 196–197 | If J is a divisible abelian group, Hom_Z(R,J) is injective as a left R-module with (r f)(x)=f(xr). Given a map from a left ideal, extend its evaluation at 1 as an additive map to R; the required extension sends r to the function x to the extended value at xr. The order xr checks left R-linearity. |
| IV.3.12, p. 197 | Every unitary left R-module A embeds in an injective one. Embed its additive group into a divisible J and use a to the function r to ra, followed by the inclusion into Hom_Z(R,J). Evaluation at 1 proves injectivity; IV.3.11 supplies the injective target. |
| IV.3.13, pp. 197–198 | J is injective iff every short exact sequence starting in J splits iff J is a direct summand of every module containing it. Extend the identity to get a retraction; for the converse split an embedding in the injective overmodule from IV.3.12 and restrict extensions. |

The identity-based parts above use rings with identity and unitary modules exactly where displayed; this is sufficient for project use.
The source's category reductions explain, rather than suppress, the distinction from arbitrary modules.
The explicit ideal-extension and divisible-envelope calculations were checked; Zorn's lemma and the additive-group free-cover foundation are retained inputs.

## Available Consequences and Limits

Over a division ring, basis complements show that every unitary module is both projective and injective (compare Exercise IV.3.3, p. 198).
This is an algebraic consequence, useful for split exactness before tensoring.
It does not assert that a topological module has a bounded splitting, or that a von Neumann algebra is injective in the operator-algebra sense.
No present Claim is assigned this entire section as a dependency merely because the terminology is now indexed.
