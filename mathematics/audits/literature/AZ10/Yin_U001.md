---
author: Yin
---
# AZ10-U001: uniform height over abelian extensions of a bounded-degree base

Date: 2026-10-18T10:48.
Human record author Yin.
The assigned G0001 coverage researcher inspected this primary source before treating a bounded-index-abelian Galois-group condition as new coverage.
The existing AM16 author manuscript, printed page 4, supplied the precise dihedral-reference lead.
This is a selected statement/applicability inspection, not an independent audit of the original proof.

<a id="az10-u001"></a>
## Read; accepted external statement and actual degree convention

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and Umberto Zannier, A uniform relative Dobrowolski's lower bound over abelian extensions, Bulletin of the London Mathematical Society 42(3) (2010), 489--498, DOI 10.1112/blms/bdq008; inspected institutional author manuscript AZ10--author-postprint.pdf, 15 PDF pages including cover and printed pages 1--14. No byte or mathematical-revision equivalence with the published rendering is asserted.

Passages: Printed pages 1--3 / PDF pages 2--4: height convention, definition of gamma_ab, Problem 1.1, Theorem 1.2, Corollary 1.3 and introductory proof discussion. The exact theorem and dihedral corollary are on printed page 2 / PDF page 3.

Inspection: Read the actual retained text and complete theorem/corollary, checked the base-degree parameter, nontorsion domain and abelian-extension hypothesis, and matched the new consumer's fixed field. The ramification/descent architecture in the introduction was read; the original proof and its ancestor theorems were not independently checked.


For the normalization use the complete [absolute logarithmic Weil height convention](../Smy08/Yin_U001.md#smy08-height-normalization).
Thus h_abs(alpha)=m(P_alpha)/[Q(alpha):Q], with all finite-place and leading-coefficient contributions included when alpha is not integral.
Let mu be the set of all algebraic roots of unity.

Theorem 1.2 states: if F is a number field of degree b=[F:Q], alpha is a nonzero algebraic number not in mu, and F(alpha)/F is abelian, then

    h_abs(alpha)>3^(-b^2-2b-6).                         (1)

Here abelian means a finite Galois extension with abelian Galois group.
The base field F need not be Galois over Q, and alpha need not be an algebraic integer, a unit or a generator of a normal extension over Q.
There is no discriminant parameter in (1).
The degree controlling this theorem is b=[F:Q], not [F(alpha):F] and not [Q(alpha):Q].
The abstract's final degree wording must not replace the explicit parameter in Theorem 1.2 and Problem 1.1.

This established statement is accepted for use at the inspected statement/applicability scope.
The proof architecture involves ramification and a Kummer descent to remove a field-generation restriction; it is not re-proved in this source unit.
No current-best-constant or global novelty claim is made.

<a id="abelian-height-infimum"></a>
## Definition: abelian height infimum

For a number field F, the source defines

    gamma_ab(F)=inf{h_abs(alpha): alpha in E^* minus mu,
                                   E/F finite abelian}.

The infimum ranges over all such extensions and nonzero nontorsion elements, not one chosen degree or one chosen extension.
Equation (1) supplies at least the safe bound gamma_ab(F)>=3^(-b^2-2b-6).
Only the pointwise strict bound (1) is needed in the project application; no strict inequality for an infimum is inferred merely from pointwise strictness.

## Direct bounded-index specialization and the actual scope gain

Suppose a finite Galois extension L/Q has an abelian subgroup A of index b.
Put F=L^A.
Then [F:Q]=b and L/F is abelian; normality of A in Gal(L/Q) is unnecessary.
For every nonzero nontorsion alpha in L, the intermediate extension F(alpha)/F is abelian because subgroups of A are normal.
The source statement therefore gives (1), and for original degree d=[Q(alpha):Q] it gives

    m(P_alpha)>d*3^(-b^2-2b-6).                         (2)

This is a direct Galois-correspondence specialization of the accepted source theorem, not a new project height theorem.
For b bounded it already supplies a uniform positive absolute-height bound, hence a uniform positive total Mahler gap, including nonnormal original fields.
The [powered-Frobenius bounded-index comparison](../../../ledger/Yin_L_G0435_v1.md#bounded-abelian-index-screen) must not label this domain as new gap coverage.

Corollary 1.3 explicitly covers dihedral L/Q and gives h_abs(alpha)>=3^(-14) for every nonzero nontorsion alpha in L.
Its normal cyclic subgroup has index 2; this matches the degree-two abelian base in Theorem 1.2.
The supplied bounded-index condition is still a restriction: small original total Mahler measure has not been shown to force it.
No bounded rational prime, bounded actual residue-Frobenius conjugacy class or near-one input sequence is supplied by this source theorem.

## Source and project boundaries

The manuscript starts directly with its introduction and has no printed contents list in the inspected front matter.
This inspection covers the named passages, not the entire fourteen-page proof.
This source inspection prevents a duplicate bounded-index coverage claim; it does not itself review the powered-lift argument now fixed in [L_G435](../../../ledger/Yin_L_G0435_v1.md#powered-frobenius-proof) or any unrestricted Task conclusion.
That argument was author-only at the date of this source inspection; its later project review retains its separate scope.
