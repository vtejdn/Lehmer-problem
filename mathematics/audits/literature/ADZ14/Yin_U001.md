---
author: Yin
---
# ADZ14-U001: central extensions above a bounded local-degree field

Date: 2026-10-20T09:40.
Human record author Yin.
The draft_comparison_cleanup AI inspected the retained primary manuscript for the D42 automatic-supply question.
Root proposed testing composita of an abelian field with a field where a fixed prime splits completely.
This unit accepts the precise existing source theorem and records its direct applicability; it is not an independent review of a new project construction.

<a id="adz14-u001"></a>
## Read; accepted central-extension height statements

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso, Sinnou David and Umberto Zannier, On fields with the Property (B), HAL hal-00649954 manuscript deposited 9 December 2011, 16 pages. The bibliography records the later Proc. Amer. Math. Soc. 142(6) (2014), 1893--1910 article; no whole-version equivalence with its 18-page published rendering is asserted.

Passages: Printed/PDF pages 1--2: height/property definitions, Theorem 1.2 and Corollary 1.3. Page 5: exact finite central-extension setup. Pages 7--8: Proposition 4.2 and the finite-to-infinite implication. The numbering is that of this retained manuscript, not the published Theorem 1.5/Corollary 1.7 numbering reported by other records.

Inspection: Direct PDF text reading of the complete named statements, finite setup, and displayed reduction; matched the base degree and local-degree dependence to the actual compositum use. The ramification/descent proof was read for scope, without independently auditing its AZ10 ancestors, local class-field input or all proof details. The limited auxiliary-formula issue below is recorded explicitly.


The [retained HAL manuscript](../../../literature/pdf/ADZ14--hal-20111209.pdf) has its exact acquisition and version.
The inspected opening has no printed contents list.
The later journal PDF was not obtained for a version comparison.

<a id="bogomolov-property"></a>
### Definitions and height convention

For a set A of algebraic numbers, the Bogomolov property, or Property (B), means that some c(A)>0 bounds h_abs(alpha) below for every nonzero alpha in A that is not a root of unity.
Equivalently, every nonzero element of A of height less than c(A) is a root of unity.
This uses the absolute logarithmic Weil height, with all finite places and the primitive minimal-polynomial convention in [Smy08-U001](../Smy08/Yin_U001.md#smy08-height-normalization).
For an algebraic integer alpha of original degree d, m(alpha)=d h_abs(alpha).

<a id="bounded-local-degree"></a>
For a number field K, an algebraic extension E/K and a fixed non-Archimedean place v of K, bounded local degree at v means that one integer d0 bounds [E_w:K_v] for every extension w of v.
For an infinite algebraic extension this is equivalently a common bound on all corresponding finite local subextensions.
The place and d0 are fixed before the field or element varies.

<a id="central-local-height-theorem"></a>
### Exact finite theorem and infinite extension

In the manuscript's finite setup, let K be a number field of degree d0_base over Q, let L/K be finite Galois with group G, and let N be a subgroup contained in Z(G).
Put E=L^N.
Choose a prime q of E above a prime wp of K over the rational prime p, and write e0=[E_q:K_wp].
Proposition 4.2 states that there is c(p,e0,d0_base)>0 such that

    h_abs(alpha)>=c(p,e0,d0_base)
       for every alpha in L^* which is not a root of unity.

The same constant is independent of [L:E], [E:K] and the original degree of alpha.
N is central, and hence normal and abelian; the hypothesis is stronger than merely saying that L/E is abelian.
No unramifiedness of L/E, integrality or unit condition on alpha is imposed.

Theorem 1.2 gives the infinite version: if L/K is Galois and the field fixed by Z(Gal(L/K)) has uniformly bounded local degree at v, then L has Property (B), with an effective positive constant depending only on v, that bound and [K:Q].
Its finite-subextension proof uses Proposition 4.2.
Corollary 1.3, assuming finite exponent of G/Z(G), is a sufficient specialization and is not the whole theorem.

These are accepted established external statements at the inspected statement/applicability scope.
No new lower-height theorem or original-source proof audit is claimed.

### A limited printed-formula issue outside the required parameter use

The manuscript's Lemma 2.1 on pages 3--4 prints the closed form s(p,rho,lambda)=p^k rho+max(0,lambda-k) for all lambda>=0.
Its preceding finite sum has instead the form p^min(k,lambda) rho+max(0,lambda-k); the printed simplification agrees when lambda>=k but can fail for lambda<k.
For example lambda=0 and k>0 leave the finite sum equal to rho rather than p^k rho.
The subsequent height proof uses existence of a sufficiently large lambda, so this small-lambda issue does not change that invoked consequence.
The project does not use the printed all-lambda formula; its own valuation amplification remains the separately accepted binomial argument in L205.
This observation is not a whole-source verdict or a claim that the uninspected published edition retains the same typographical issue.

<a id="abelian-split-compositum-application"></a>
### Direct applicability to the proposed actual compositum

Let A/Q be any finite abelian extension and B/Q any actual finite Galois extension in which a fixed rational prime p splits completely.
Set L=AB and G=Gal(L/Q), with both fields contained in a common algebraic closure.
Restriction embeds G into Gal(A/Q) times Gal(B/Q); linear disjointness is unnecessary.
The subgroup N=Gal(L/B) is central: its restriction to B is the identity and its restriction to A commutes with every restriction because Gal(A/Q) is abelian.
The injective restriction map then makes its commutator with every element of G trivial.
Its fixed field is exactly B.

For any prime q of B over p, complete splitting gives B_q=Q_p.
The finite theorem therefore applies with K=Q, E=B, e0=1 and d0_base=1, proving

    h_abs(alpha)>=c(p,1,1)>0,
    m(alpha)>=deg(alpha)c(p,1,1)

for every nonzero nontorsion alpha in AB.
The uniform bound is independent of A, B and their intersection.
It already covers every original integer-unit input in this proposed family, whether or not its own field is Galois.
Consequently this family cannot be claimed as new gap coverage merely because G/Z(G) has no uniform exponent or because the abelian-subgroup index is unbounded.
Actual totally real Galois fields B/Q with group S_j and complete splitting of2, for every j>=5, are supplied by the [C_G164 symmetric-field construction](../../../claims/Yin_C_G0164_v1.md#ramified-symmetric-real-crt) at its parameter r=1.
Its complete CRT/Hensel construction and [R_G389 whole-review scope](../../reviews/Yin_R_G0389_v1.md#actual-realization-whole-independent-finding) concern actual fields, with unbounded degree as j varies.
Only that intermediate symmetric field is used here, not C164's subsequent Salem extension, whose root group and Frobenius classes differ.
These retained project-application details supply no inverse-Galois assertion from the ADZ source theorem and do not enlarge this unit's original source-inspection scope.
