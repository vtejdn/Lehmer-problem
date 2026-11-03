---
author: Yin
---
# The full dyadic Galois field is not contained in any fixed finite-generator radical field

Human author Yin.
The complete author deduction below was first retained in the continuing D42 inquiry at2026-10-20T10:36, after C181 was frozen.
This fixed Claim retains that argument in full for its own independent review, with the original division between source inputs and project proof.

Root proposed the finite-base/metabelian comparison as the missing distinction from CDPT26's fixed-generator corollary.
The draft_comparison_cleanup AI supplies the complete normality, finite-intersection and nonmetabelian arguments below, including the explicit finite2-group witness.
The later whole independent review and adoption are recorded in the selected assessment; this result does not alter C181 or its existing inspection scope.
No mathematical program, finite group enumeration or field scan is performed.

## Statement

Let B_infinity be the compositum of ALL finite Galois2-extensions of Q unramified at finite primes other than2.
For every fixed number field K and every fixed finitely generated subgroup Gamma of the multiplicative group of algebraic numbers, the claim is

    B_infinity is not contained in K(mu,Gamma^div).       (N1)

Here mu is the set of all roots of unity and Gamma^div includes roots of all positive integer orders, not only2-power orders.
Consequently the same noncontainment holds with Gamma^(S-div) for any fixed set of rational primes S, including S={2}.
The quantifiers fix K and Gamma BEFORE selecting a finite field B; they do not deny that each separate finite B can be placed in a field with a different base or different generators.

<a id="argument"></a>
## Complete argument

<a id="pro-two-source-interface"></a>
### Actual arithmetic and group-theoretic source inputs

The actual definition of B_infinity and the Schmid presentation are retained in [Sch14-U001](../audits/literature/Sch14/Yin_U001.md#sch14-u001).
For the particular open subgroup needed here, this author additionally read the complete Proposition2.4 and its displayed proof at printed114/PDF4 of [the same publisher artifact](../literature/pdf/Sch14--publisher.pdf).
Taking its n=2 and K=Q(zeta_4)=Q(i), the proof states exactly that

    F_2=Gal(B_infinity/Q(i))

is a free pro-2 group of rank2.
This is a standard arithmetic input inherited from the source's cited classical2-rational-field theorem, whose ancestor proof is not independently audited here.
It concerns the actual maximal arithmetic extension, not an abstract group chosen in place of a number field.

The newly inspected [Rib12-U001](../audits/literature/Rib12/Yin_U001.md#rib12-u001) supplies the finite-basis universal property and Theorem2.6.1: open subgroups of a free pro-2 group are free pro-2.
The class of finite2-groups is closed under extensions as required there.
Its finite Schreier basis construction applies to the finite-index subgroups here; no unquoted rank formula is needed.
The standard Kummer attribution was also checked directly in the already retained [CDPT26 manuscript](../literature/pdf/CDPT26--arxiv-v1.pdf), printed/PDF7, Theorem2.1 and Remark2.2, for characteristic-zero fields containing the required roots of unity.
This is an additional selected passage beyond CDPT26-U001's initial inspection; the abelian-kernel fact needed below is also proved directly.
None of the recent paper's height proof or intermediate ramification arguments is required for this noncontainment result.

The standard finite Galois correspondence and infinite restriction/inverse-limit interfaces used below are Stacks [Tag09DW](https://stacks.math.columbia.edu/tag/09DW) and [Section0BMI](https://stacks.math.columbia.edu/tag/0BMI), specifically Lemmas9.22.2--9.22.3, Theorem9.22.4 and Lemma9.22.5.
Their actual primary statement/applicability inspection is retained in [R455's source check](../audits/reviews/Yin_R_G0455_v1.md#finite-and-infinite-galois-source-check).
That inspection concerns the official online tags and their displayed restriction/inverse-limit explanations, with no identified project commit or PDF page numbering.
It does not inherit the version or scope of The26b-U001 or the separately retained More on Algebra chapter.
This source declaration identifies the standard inputs of the already displayed finite-compositum and inverse-limit argument; it changes no mathematical assertion or proof step.

### Every open subgroup of F_2 is nonmetabelian

A profinite group is called metabelian here when its closed commutator subgroup is abelian; equivalently its second closed derived subgroup is trivial.
Subgroups and continuous quotients preserve this property.
Let H be an open subgroup of F_2.
By the exact open-subgroup theorem, H is free pro-2 on a finite basis.
The universal property gives a continuous surjection pi:F_2->Z_2^2 by sending its two free generators to the standard coordinate generators.
The image pi(H) has finite index, at most[F_2:H], in Z_2^2.
It is compact and thus closed, so it is an open subgroup of that abelian pro-2 group.

H cannot be procyclic or trivial.
If it were, the image of pi(H) in(Z/2^k Z)^2 would be cyclic, hence have order at most2^k, for every k.
But the fixed finite-index bound M gives that image order at least2^(2k)/M, a contradiction once2^k>M.
Thus the finite free rank of H is at least2.

For completeness, a single explicit finite quotient shows that every free pro-2 group of rank at least2 is nonmetabelian.
Let R be the free associative algebra F_2<X,Y> modulo all words of degree at least6, and let J be its ideal spanned by the nonempty words.
The set1+J is a finite group: J^6=0 makes each inverse the finite geometric sum, and its cardinality is a power of2.
Put a=1+X,b=1+Y and let G_0 be their subgroup.
Use the commutator convention[x,y]=x^(-1)y^(-1)xy.
Expanding those finite inverses gives

    c=[a,b]=1+C_2 modulo J^3, C_2=XY+YX,
    d=[a,c]=1+D_3 modulo J^4, D_3=X^2Y+YX^2.

Both c and d belong to the commutator subgroup of G_0.
Their commutator has the exact nonzero degree5 term

    [c,d]=1+C_2 D_3+D_3 C_2,
    C_2 D_3+D_3 C_2
      =XYX^2Y+XY^2X^2+YXYX^2
          +X^2YXY+X^2Y^2X+YX^2YX.                    (N2)

All higher-degree terms vanish in R.
The six displayed words are distinct basis words; the two occurrences of YX^3Y in the expansion cancel in characteristic2, and no displayed term cancels.
Hence[c,d]!=1, so G_0 is a finite nonmetabelian2-group generated by a,b.
The free pro-2 universal property maps two basis elements of H to a,b and every other basis element to1, producing G_0 as a continuous quotient.
Therefore H is not metabelian.
This proves the required obstruction for EVERY open H, without citing a mere group name or relying on an unexecuted finite-group scan.

### Every fixed radical field has a metabelian group after a finite base change

Suppose, for contradiction, that the inclusion denied by(N1) held.
Choose one finite Galois number field K_0/Q containing K, i and a finite generating set of Gamma.
It contains every element of Gamma.
Set

    R_0=K_0(mu,Gamma^div), C_0=K_0(mu).

The field R_0/K_0 is Galois: every K_0-embedding permutes roots of unity and the roots of each polynomial X^m-gamma, with gamma in Gamma.
The intermediate extension C_0/K_0 is abelian, as each cyclotomic compositum has an automorphism group injecting into the abelian group of automorphisms of its roots of unity.
The kernel Gal(R_0/C_0) is abelian.
Indeed for beta with beta^m in Gamma and for theta in this kernel, theta(beta)/beta is an m-th root of unity, which the kernel fixes.
For two such automorphisms theta,eta, their two root-of-unity multipliers consequently commute and give theta eta(beta)=eta theta(beta).
They also commute on C_0; those fields and radical elements generate R_0, so the automorphisms commute everywhere.
This checks the exact Kummer interface with full roots of unity and fixed base, without assuming Gamma is invariant under Gal(K_0/Q).

Thus Gal(R_0/K_0) is an extension of an abelian group by an abelian group and is metabelian.
The assumed B_infinity containment implies B_infinity K_0 is an intermediate Galois extension of R_0/K_0.
Its Galois group is a continuous quotient, hence metabelian.

### Actual finite-base intersection and contradiction

Let E=B_infinity intersect K_0.
This is a finite number field, since K_0 is finite; it contains Q(i).
Both original extensions are Galois over Q, so the usual restriction isomorphism is

    Gal(B_infinity K_0/K_0) = Gal(B_infinity/E).      (N3)

This can also be read on a cofinal system of actual finite Galois subfields B containing E, where B intersect K_0=E and the finite Galois compositum theorem applies, and then passed to inverse limits.
The right side is an OPEN subgroup of F_2=Gal(B_infinity/Q(i)), with finite index[E:Q(i)].
It cannot be metabelian by the preceding proved obstruction, contradicting the radical-field conclusion.
This proves(N1).

<a id="noncontainment-boundaries"></a>
### Exact arithmetic and comparison consequence

Since B_infinity is the directed union of actual finite Galois2-ramified fields, its noncontainment implies that for each fixed K,Gamma there exists an ACTUAL such finite B not contained in K(mu,Gamma^div).
This is an arithmetic field-level statement, with no abstract-group-only realization gap.
It rules out covering the entire C181 B-family by one fixed finite-base/finitely-generated radical field from CDPT26's corollary, even after allowing all division orders.
It does not assert a near-one unit outside that field, global novelty of the total-measure theorem, or failure of every more general infinite-base hypothesis in CDPT26's Theorem5.1.
Those stronger statements are not consequences of this exact noncontainment result.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:38 |
| status | open |
| reason | Register the complete actual-field noncontainment in every fixed finite-base/finitely-generated radical field, including all division orders. Root proposed the comparison and the drafting agent supplied the full group, kernel, normality and intersection argument; independent review remains required. This is not a near-one input or global novelty theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact fixed-field noncontainment](#statement) | For every fixed number field K and finitely generated algebraic multiplicative Gamma, the actual maximal2-ramified Galois field is not contained in K(mu,Gamma^div); fixed parameters precede the actual finite-field witness. |
| argument | [Complete group and arithmetic proof](#argument) | Accepted actual free pro-2 subgroup, open-subgroup and rank argument, exact finite nonmetabelian quotient, radical normality/abelian kernel, finite normal base intersection, actual restriction inverse limits and final field consequence. |
| dependency | [Actual2-ramified field source](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Exact B_infinity and finite Galois field class; additional Proposition2.4 proof passage is inspected explicitly in the local source-interface section. |
| dependency | [Exact additional source interface](#pro-two-source-interface) | Sch14 printed114/PDF4 Proposition2.4 at n=2 gives Gal(B_infinity/Q(i)) free pro-2 rank2; actual primary version and inherited proof limit, precise Kummer attribution, and the standard finite/infinite Galois source interfaces already used in N3. |
| dependency | [Free pro-2 universal and open-subgroup inputs](../audits/literature/Rib12/Yin_U001.md#rib12-u001) | Exact finite-basis universal property and extension-closed Theorem2.6.1, without importing an unquoted rank or nonmetabelian assertion. |
| support | [Fixed-radical height domain](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Comparison only with fixed K,Gamma corollary; no use of the recent height proof or rejection of every infinite-base theorem. |
| support | [Dyadic arithmetic application](Yin_C_G0181_v1.md#statement) | The actual broad B class whose fixed-radical coverage is compared; its Mahler bound and controls are not premises of the group-theoretic noncontainment. |
| support | [Exact consequence and limits](#noncontainment-boundaries) | Actual finite-field witness for every fixed K,Gamma, preserving quantifier order and excluding unsupported near-one or all-literature conclusions. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:48 |
| status | proved |
| authority | Internal adoption within Yin's selected automatic-supply inquiry. |
| reason | Adopt the complete actual-field noncontainment through noncontributor whole R455 and its source-only declaration readback. Every fixed finite base and finitely generated multiplicative group fails to contain the full dyadic Galois field even with all division orders. The original finite-field quantifier and absence of any near-one or all-literature claim are retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact fixed-field noncontainment](#statement) | For every fixed number field K and finitely generated algebraic multiplicative Gamma, the actual maximal2-ramified Galois field is not contained in K(mu,Gamma^div); fixed parameters precede the actual finite-field witness. |
| argument | [Complete group and arithmetic proof](#argument) | Accepted actual free pro-2 subgroup, open-subgroup and rank argument, exact finite nonmetabelian quotient, radical normality/abelian kernel, finite normal base intersection, actual restriction inverse limits and final field consequence. |
| dependency | [Actual2-ramified field source](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Exact B_infinity and finite Galois field class; additional Proposition2.4 proof passage is inspected explicitly in the local source-interface section. |
| dependency | [Exact additional source interface](#pro-two-source-interface) | Sch14 printed114/PDF4 Proposition2.4 at n=2 gives Gal(B_infinity/Q(i)) free pro-2 rank2; actual primary version and inherited proof limit, precise Kummer attribution, and the standard finite/infinite Galois source interfaces already used in N3. |
| dependency | [Free pro-2 universal and open-subgroup inputs](../audits/literature/Rib12/Yin_U001.md#rib12-u001) | Exact finite-basis universal property and extension-closed Theorem2.6.1, without importing an unquoted rank or nonmetabelian assertion. |
| support | [Fixed-radical height domain](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Comparison only with fixed K,Gamma corollary; no use of the recent height proof or rejection of every infinite-base theorem. |
| support | [Dyadic arithmetic application](Yin_C_G0181_v1.md#statement) | The actual broad B class whose fixed-radical coverage is compared; its Mahler bound and controls are not premises of the group-theoretic noncontainment. |
| support | [Exact consequence and limits](#noncontainment-boundaries) | Actual finite-field witness for every fixed K,Gamma, preserving quantifier order and excluding unsupported near-one or all-literature conclusions. |
| review | [Whole fixed-radical finding](../audits/reviews/Yin_R_G0455_v1.md#dyadic-fixed-radical-noncontainment-whole-finding) | Entire final statement and proof, N1--N3, every source interface and exact field-level consequence, including the later source-only declaration readback. |

