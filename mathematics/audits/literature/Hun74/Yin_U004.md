---
author: Yin
---

# Hom and Algebraic Duality

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained user-supplied published printing of Hungerford’s *Algebra*, 528 PDF pages; original retrieval origin unknown; exact printing and artifact evidence.

Passages: Source: Hun74 printing, §IV.4, pp. 199–207 / PDF pp. 225–233.

Inspection: Review: 2026-09-10, the coordinating agent, self-review; all main statements and proofs/sketches audited within scope, with the side conventions below.


Retained user-supplied published printing of Hungerford’s Algebra, 528 PDF pages; the original retrieval origin is unknown.

## Hun74-U004

- Source: Hun74 printing, §IV.4, pp. 199–207 / PDF pp. 225–233.
- Review: 2026-09-10, the coordinating agent, self-review; all main statements and proofs/sketches audited within scope, with the side conventions below.
Exercises pp. 206–207 surveyed; only explicitly checked consequences are imported.
- Dependencies: [module quotients and split sequences](Yin_U001.md#hun74-u001), [basis theorem](Yin_U002.md#division-ring-bases), [projective/injective criteria](Yin_U003.md#hun74-u003).

<a id="hom-and-bimodules"></a>
## Hom and Bimodule Definitions

The additive group Hom_R(A,B) consists of R-module homomorphisms, with their side determined by A and B.
Without extra data it is an abelian group; for noncommutative R there is no automatic R-module structure obtained by multiplying values on an arbitrary side.

The unnumbered definition on **p. 202** makes an **R–S bimodule** a left R-module and a right S-module with commuting actions: (ra)s=r(as).
The actions must be specified; the term alone does not imply any topology or norm.
Theorem IV.4.8, p. 203, supplies the following actions:

\[
\begin{aligned}
{}_R A,{}_R B_S &: \quad (f s)(a)=f(a)s
&&\text{on }\operatorname{Hom}_R(A,B),\\
{}_R C_S,{}_R D &: \quad (s g)(c)=g(cs)
&&\text{on }\operatorname{Hom}_R(C,D).
\end{aligned}
\]

Commutation of the two module actions proves R-linearity of each new map and the S-action axiom.
The right-module counterpart is obtained by reversing sides.
Pre/postcomposition respects these actions when the relevant maps preserve the additional side.

<a id="hom-exactness"></a>
## Hom Results and Proof Mechanisms

| Result and locator | Statement and checked proof |
| --- | --- |
| IV.4.1, p. 199 | Composition induces additive maps on Hom, contravariantly in the source and covariantly in the target. Associativity of composition checks functoriality. |
| IV.4.2, p. 200 | A sequence 0 to A to B to C is exact iff applying Hom_R(D,-) gives an exact sequence at the corresponding first two positions for every D. The forward argument factors a map with image in the kernel. The converse tests the relevant kernel modules and identity maps; a single arbitrary test object is insufficient. |
| IV.4.3, pp. 200–201 | The dual test for A to B to C to 0 uses Hom_R(-,D) for every D. Factor through a quotient for the forward implication. For the converse use C/Im(g), B/Im(f), and C to detect surjectivity, image/kernel equality and factorization. |
| IV.4.4, p. 201 | A short exact sequence splits iff all covariant Hom test sequences split, equivalently all contravariant ones split. A section or retraction induces the splitting; testing the identity of the appropriate endpoint recovers it. |
| IV.4.5–4.6, pp. 201–202 | P is projective iff Hom_R(P,-) preserves surjections, equivalently carries short exact sequences to short exact sequences. J is injective iff Hom_R(-,J) preserves the corresponding surjections induced by inclusions, equivalently is exact on short exact sequences. Combine left exactness with the lifting/extension definitions. |
| IV.4.7, p. 202 | Hom_R(direct-sum A_i,B) is the product of Hom_R(A_i,B); Hom_R(A,product B_j) is the product of Hom_R(A,B_j). Restriction and coordinate projection give the respective inverses. Infinite products cannot be replaced by direct sums. |
| IV.4.8–4.9, p. 203 | The bimodule-induced actions above and A isomorphic to Hom_R(R,A) for unitary left A. The latter map is evaluation at 1, with inverse a to (r to ra). Its left R-action is induced by the **right action on the argument R**. |

<a id="algebraic-dual"></a>
## Algebraic Dual and Coordinate Functionals

The definition after IV.4.9, **p. 203**, sets A* = Hom_R(A,R) for a left module A and gives it the right action (f r)(a)=f(a)r.
The dual of a right module is correspondingly a left module.
These are **algebraic duals**, with no boundedness or continuity requirement.
They are not Hilbert adjoints, conjugate spaces, Tomita conjugations or dual systems of operators.

**Theorem IV.4.10, p. 204.**
Dualizing a homomorphism reverses its direction and changes the acting side.
Duals preserve finite direct sums.
A short exact sequence of left vector spaces over a division ring dualizes to a short exact sequence of right vector spaces: extend a basis to split the original sequence, then use the split Hom criterion.
No finite-dimensionality is required for this exactness assertion.

**Theorem IV.4.11, p. 204.**
If a free left module has basis X, the coordinate functionals f_x form a right-linearly independent family in its dual.
They form a basis of the full dual when X is finite.
Independence follows by evaluating on x; in the finite case every functional f is the finite sum of f_x f(x).
In the infinite case an arbitrary functional can have nonzero values on infinitely many basis vectors, so this final sum is not generally available.

For a free **right** module, write v as a finite sum of x a_x and let f_x(v)=a_x.
Then f_x(vr)=f_x(v)r.
This direct right-sided version, together with IV.2.4, is the coefficient-functional input accepted for the project use reported under former Yin_C_F0035-P1.
The original project proof/review homes remain unlocated in the current retained F-family collection; these source inputs alone establish no current equalizer theorem.
Only one coordinate functional is needed there; no assertion that all functionals have finite support is used.

**Theorem IV.4.12, p. 205.**
Evaluation gives a left R-module map A to A**, a to (f to f(a)).
It is injective for a free unitary module and is an isomorphism for a finite free module.
Coordinate functionals separate points, proving injectivity; the finite dual basis gives surjectivity.
The following text calls a module reflexive when this evaluation map is an isomorphism.
The theorem does not give injectivity for arbitrary modules or surjectivity for arbitrary infinite free modules.

## Side and Review Boundaries

The p. 204 remark comparing a finite-dimensional vector space with its dual is imported as the equality of their respective left/right dimensions and the explicit coordinate correspondence.
No canonical same-side D-linear isomorphism V to V* is inferred over a noncommutative division ring: they have different specified sides.
In contrast, evaluation into V** has the original side and is canonical.

Exercise IV.4.5, p. 206, identifies End_R of the left regular module with R-opposite: an endomorphism is right multiplication by its value at 1, and composition reverses the order of those values.
This direct check is available as an orientation aid.
The later exercise references on infinite algebraic duals, including the cited external results, were not audited or accepted as new dependencies.
The verified coordinate-functional interface suffices for current use.
