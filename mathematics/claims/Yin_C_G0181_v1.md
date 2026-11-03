---
author: Yin
---
# Dyadic Galois composita: automatic central Frobenius and a uniform total-measure gap

Human author Yin.
Root proposed the full arithmetic class, its decomposition/inertia proof using quadratic subfields, and the unit-radical and odd-cyclotomic comparison controls.
The draft_comparison_cleanup AI supplied the complete field and degree checks, exact polynomial/discriminant/reduction calculations, source inspection and precise prior-coverage boundaries below.
Both are mathematical contributors; the later whole independent review and adoption are recorded in the selected assessment below.
No numerical root isolation, prime search, parameter scan, evaluated asymptotic sequence or mathematical program was performed.
The exact calculations below are symbolic arguments, not new numerical evidence.

## Statement

Let B/Q be any finite Galois extension of2-power degree, unramified at all finite rational primes other than2; ramification at infinite places is allowed.
Let A/Q be any finite abelian extension unramified at2, and put L=AB in a common algebraic closure.
Then2 is totally ramified in B, A intersect B=Q, and Gal(L/Q)=Gal(A/Q) times Gal(B/Q).
For each prime of L above2 there is an actual residue-Frobenius lift sigma which is central in this global group.
It therefore supplies p=2,f=1,kappa=1 to the completed powered-Frobenius interface.
Every nontorsion algebraic integer unit alpha in L consequently satisfies

    m(alpha)>=log2/12.                                    (1)

The bound is uniform over A,B,alpha and their degrees and does not require Q(alpha)/Q to be Galois.
Equivalently the same bound holds for every integer unit in the union of all these actual finite composita, outside roots of unity.

For this selected lift, the C179 centralizer data are C=Gal(L/Q), N=<sigma>, K=Q and

    nu=[I intersect C:I intersect N]=[B:Q],
    [L^N_q:Q_2]=[B:Q].                                  (2)

This records the actual cost for that lift and subgroup, not an optimization over all central subgroups or all primes.
The entire class has no uniform positive absolute-height lower bound even on its nontorsion integer units, as the explicit controls below prove.
A positive total-measure gap and such absolute-height decay are compatible.

For each n>=0 put q=2^n, u=1+sqrt2 and gamma_n=u^(1/q)>1 using the positive real root.
The polynomial

    P_n(X)=X^(2q)-2X^q-1                                  (3)

is its monic irreducible polynomial of degree2q, all its roots are units, and its actual splitting field B_n is a member of the stated B class.
Moreover

    m(gamma_n)=log u,
    h_abs(gamma_n)=(log u)/(2q)->0.                        (4)

For any odd prime ell and a primitive ell-th root of unity zeta_ell, put alpha_(n,ell)=gamma_n zeta_ell.
With A_ell=Q(zeta_ell), these are actual inputs in A_ell B_n with

    deg(alpha_(n,ell))=2q(ell-1),
    m(alpha_(n,ell))=(ell-1)log u,
    P_(alpha_(n,ell)) mod2 = (Phi_ell mod2)^(2q).           (5)

Every irreducible factor of that reduction has degree ord_ell(2), with every multiplicity retained.
These degrees are unbounded as ell varies through odd primes.
Thus bounded original residue-degree mass at2 is not automatic for the full compositum class, even though the central-lift bound(1) is automatic.
These particular controls have fixed or growing positive total measure and are not a near-one sequence or a Lehmer counterexample.

This is a complete author candidate for an arithmetic application of the existing ratio/residue criterion.
It is not a claim that no prior theorem in the global literature covers the class, and its precise inspected comparisons are stated below.

<a id="inputs-and-source-screen"></a>
## Exact inputs and bounded source comparison

| Input | Role and limit |
| --- | --- |
| [Sch14-U001](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Actual finite2-ramified class, its precise quadratic subfields and realization/pro-2 scope; no abstract group alone supplies a field. |
| [C179 local-degree interface](Yin_C_G0179_v1.md#local-degree-source-interface) | Exact accepted decomposition/inertia and completion degrees, including nonnormal intermediate fields and actual tower degrees. |
| [L435 complete powered bridge](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Actual original nontorsion-unit criterion at bounded p,f,k, including auxiliary degree and all multiplicities; its p=2,f=k=1 specialization is log2/12. |
| [L205 original residue criterion](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Separate all-input bounded-degree reduction mass theorem, used for comparison; growing degrees in(5) defeat an automatic fixed-F premise at2, not every old application. |
| [Con26d-U001](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Exact monic Eisenstein irreducibility criterion applied to P_n(X+1). |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Simple-root specialization of the complete-valued-field Hensel theorem in the finite unramified completions used for P_n and X^ell-1. |
| [Exact unramified source interface](#unramified-lifting-source-interface) | The actual retained The26b chapter's Lemma113.8/Tag0EXR, separately inspected at printed/PDF334--335; this is not silently included in the older The26b-U001 scope. |
| [ADZ14-U001](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Stronger old absolute-height theorem and its exact local/base parameters, compared through C179 rather than incorrectly assumed uniform in growing inertia. |
| [AZ10-U001](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Uniform absolute-height bound for an abelian extension of a bounded-degree base; no such uniform base degree for the whole present class is inferred. |
| [CDPT26-U001](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Exact fixed finitely generated radical-group/cyclotomic domain, including the division-group total-measure branch and primary-preprint inspection limits. |

The source screen first reused the actual bounded-index, unramified-centralizer, original-residue and fixed-radical comparisons retained in D42/L435/C179 and their source units.
The selected primary-source search then used the exact combinations of Lehmer/height/Bogomolov with2-ramified, unramified outside2, totally ramified compositum and radical extensions.
It located Schmid's actual realization theorem and CDPT26's stronger fixed-radical coverage, both retained with exact version and inspection limits.
No inspected source stated a uniform total-measure theorem for the entire arbitrary-B class in(1).
This bounded search is not a field-wide novelty determination or a proof that all other height theorems fail to apply.

<a id="unramified-lifting-source-interface"></a>
## Exact simple-root and unramified-normal-closure source interface

The simple-root lifting in Sections4--5 uses the accepted [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) specialization of Conrad's Theorem9.1, printed/PDF18, with its complete non-Archimedean field and polynomial hypotheses.
In the actual finite unramified local extension whose residue field splits the reduced polynomial, lift each distinct residue root to an integral representative a.
The reduction hypotheses give v(P(a))>0 and v(P'(a))=0, hence the source's v(P(a))>2v(P'(a)) condition.
Distinct residue roots have disjoint residue classes, so their lifted roots remain distinct and supply the full local splitting.
This is the precise use already made in the proof; the stronger nonunit-derivative version and later power-series variants are not invoked.

The drafting author also directly read the existing [The26b More on Algebra chapter](../literature/pdf/The26b--more-algebra-20261002.pdf), version ed88ff78 compiled14 July2026, printed/PDF334--335, Lemma113.8, Tag0EXR, including its complete statement and displayed short proof.
Its first part preserves unramifiedness in intermediate extensions, its second permits an unramified normal closure of a finite unramified separable extension, and its third permits the compositum of finite unramified extensions inside an unramified extension.
The displayed proof of the second part takes the actual normal closure, which is exactly the alternate formulation used in Section4.
These established statements are accepted at this finite number-field/local-field application scope; their étale-algebra ancestors are not independently re-audited here.
This actual additional passage is outside the older [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) selection of09EC/09ED/09E8.
The present source-interface declaration records the existing lifting/normal-closure argument precisely and changes no polynomial, field, mathematical conclusion or parameter.

<a id="argument"></a>
## Complete actual-field proof

### 1. Complete ramification of every allowed B

A maximal proper subgroup M of a finite2-group G is normal of index2.
For completeness, induction on |G| proves this from the nontrivial center Z(G), whose nontriviality follows from the conjugacy-class equation.
If Z(G) is not contained in M, maximality gives G=M Z(G), making M normal, and the quotient is a nontrivial cyclic2-group with no proper nontrivial subgroup, hence order2.
If Z(G) is contained in M, apply induction to the maximal subgroup M/Z(G) of G/Z(G).
The abelian case is included in the first alternative; the trivial group needs no maximal subgroup.

Let D_B,I_B be the decomposition and inertia groups at a prime of B over2, and put G_B=Gal(B/Q).
If D_B were proper, choose a maximal subgroup M containing it.
Its index2 normality makes H=B^M a quadratic field, still unramified outside2, and the actual local-degree formula gives

    [H_v:Q_2]=[D_B:D_B intersect M]=1.

Thus2 splits in H.
But the precise Sch14 classification leaves only Q(i), Q(sqrt2) and Q(sqrt(-2)), each ramified at2.
This contradiction proves D_B=G_B, so B has a unique prime above2.

If I_B were proper in G_B=D_B, its normality and the same finite2-group argument would give a normal index2 subgroup M containing I_B.
The corresponding quadratic H has trivial inertia image at2, so it is unramified there, and it is also unramified at every other finite prime.
This again contradicts the three-field classification, without invoking a general Minkowski discriminant theorem.
Hence I_B=D_B=G_B: the residue field is F_2 and the ramification index is[B:Q].
The case B=Q satisfies the same conclusion with degree1.

### 2. Global disjointness, actual local product and central Frobenius

Put H=A intersect B.
As a subfield of B, H has a unique prime over2 and is totally ramified there: the total local degree of B equals its global degree, and the intermediate tower preserves this equality and residue field F_2.
As a subfield of A, it is unramified at2.
Therefore its ramification index and its global degree are both1, so H=Q.
Because A and B are Galois over Q, restriction now gives the full product G_A times G_B as Gal(AB/Q).

Choose the induced prime a of A and write t=[A_a:Q_2].
The extension A_a/Q_2 is finite unramified, while B_b/Q_2 is finite totally ramified of degree |G_B|.
Their intersection has both properties and is Q_2.
Both local extensions are Galois, so they are linearly disjoint; their compositum has degree t|G_B|.
Over A_a that compositum has ramification index at least |G_B|, because it contains B_b, and degree exactly |G_B|, so it is totally ramified.
Thus the actual residue degree of L at the chosen prime is t and the ramification index is |G_B|.

Restriction embeds its decomposition group into D_A times G_B.
Both sides have order t|G_B| by the local-degree interface, so equality holds.
Its inertia group is {1} times G_B.
Let sigma_A be the actual residue Frobenius of the unramified extension A_a/Q_2.
Then

    sigma=(sigma_A,1) in D_A times G_B

acts by the2-power map on the residue field of L, hence is an actual Frobenius lift.
It is central in the GLOBAL group G_A times G_B because G_A is abelian.
Its order is t, and the intersection of its cyclic subgroup with inertia is trivial.
This proves(2) by C179, with f=1,kappa=1.
No bounded t or bounded |G_B| is assumed.

### 3. Original unit and the complete uniform total-measure bound

Let alpha be any original nontorsion integer unit in L.
Its normal closure M/Q is an actual subfield of L because L/Q is Galois.
The restriction of sigma to M remains central, and remains an actual residue-Frobenius lift at the restricted prime.
Indeed restriction commutes with the reduction map and preserves the2-power action on the sub-residue field; every automorphism of M extends to L, so centrality also descends to the quotient global Galois group.
The completed L435 criterion therefore applies to the ORIGINAL alpha with p=2, f=1, k=1 and gives

    m(alpha)>=log2/[1^2(2-1)(2^1+1)2^(1+1)]=log2/12.

The general proof already includes the actual auxiliary rho=alpha^2/sigma(alpha), its nonzero integral-unit and nontorsion status, its own degree and all conjugate multiplicities.
In this central case sigma preserves Q(alpha), so the ratio lies in the original field and its total measure is at most3m(alpha); these are supplied by the same checked interface, not a replacement of original degree by a Galois degree.
The central-lift construction, rather than the existence of one small-measure example, establishes automatic coverage for every input in the full class.
Any finite collection of allowed fields is contained in another allowed compositum, so the same pointwise bound holds on their union.
This proves(1).

### 4. Exact unit-radical controls and their actual splitting fields

Fix q=2^n, u=1+sqrt2, u'=1-sqrt2=-u^(-1) and gamma=u^(1/q).
The monic polynomial P_n in(3) has constant term-1, so every root is an algebraic integer unit.
Modulo2, P_n(X+1)=X^(2q), because2q is a power of2, while its constant term P_n(1)=-2 is not divisible by4.
The monic Eisenstein criterion therefore proves irreducibility over Q and the actual degree2q of gamma.

All roots are gamma times q-th roots of unity and gamma^(-1) times the q-th roots of-1.
Consequently their splitting field is exactly

    B_n=Q(zeta_(2q),gamma).

It contains sqrt2=gamma^q-1, and every displayed root belongs to it.
The field Q(zeta_(2q),sqrt2) has2-power degree, and adjoining gamma is a succession of n quadratic radical steps, of degree at most q.
Since the displayed field is the splitting field, it is Galois of2-power degree.

For its finite ramification, differentiate:

    P_n'(X)=2q X^(q-1)(X^q-1).

The product of the roots is-1, and the product of beta^q-1 over all2q roots is[(u-1)(u'-1)]^q=(-2)^q.
The root formula for the discriminant gives exactly

    |disc(P_n)|=(2q)^(2q) 2^q.

Thus the reduction at each odd prime is squarefree.
Its distinct roots lie in a finite residue-field extension and lift by the simple-root Hensel property in the corresponding finite unramified local extension.
The local splitting field is therefore unramified at that prime; equivalently use the standard unramified-normal-closure interface already inspected in the existing The26b chapter, Lemma113.8, printed/PDF334--335.
Hence B_n is unramified at all odd finite primes and is an actual allowed B.
The preceding complete-ramification argument applies at2, without an independent local radical-field assumption.

Exactly q roots have modulus gamma>1 and q have modulus gamma^(-1)<1.
Thus m(P_n)=q log gamma=log u, while h_abs(gamma)=m(P_n)/(2q), proving(4).
These actual integer units rule out a uniform positive absolute-height bound on the entire class.
They do not rule out, or approach zero in, the total-measure bound(1).

### 5. Exact original reductions with unbounded residue degree

For an odd prime ell, A_ell=Q(zeta_ell) is abelian and unramified at2: the polynomial X^ell-1 has distinct roots modulo2, and the same unramified simple-root lifting applies.
Section2 therefore gives A_ell intersect B_n=Q and the full product of their Galois groups.
Every pair consisting of an original conjugate beta_i of gamma and a primitive ell-th root zeta_ell^a occurs as an image of alpha=gamma zeta_ell.
These images are distinct.
For if beta_i zeta_ell^a=beta_j zeta_ell^b, raising to the q-th power gives

    beta_i^q/beta_j^q=zeta_ell^(q(b-a)).

The left side is either1,-u^2 or-u^(-2); the latter two do not have modulus1.
Thus it is1, and ell being odd and q a2-power gives a=b modulo ell and then beta_i=beta_j.
There are exactly2q(ell-1) images, proving the original degree in(5).
All root-of-unity factors have modulus1, so multiplication over these distinct original embeddings gives the total measure(ell-1)log u.

At the prime above2, every beta_i reduces to1 because B_n is totally ramified and beta_i is a unit.
The reductions of the primitive ell-th roots remain distinct and primitive: X^ell-1 is separable modulo2 and Phi_ell(1)=ell is nonzero modulo2.
Reducing the complete original factorization therefore gives exactly(Phi_ell mod2)^(2q), with no omitted multiplicity or squarefree replacement.
The orbit of a primitive ell-th root under x->x^2 has length ord_ell(2), proving the asserted degree of every irreducible factor.
For each fixed F, a prime with ord_ell(2)<=F divides the nonzero integer product_(j=1)^F(2^j-1); there are only finitely many such primes.
The infinitude of odd primes therefore gives unbounded factor degrees, without selecting or scanning a numerical prime sequence.
For each fixed F the bounded-degree mass at2 is eventually zero on this control, although its total measure grows with ell.
This is a precise failure of automatic coverage by that original-residue premise, not a near-one counterexample or a rejection of other primes and other old arguments.

<a id="prior-coverage-boundaries"></a>
## What the existing comparisons establish

The complete powered-ratio criterion was already an old sufficient total-measure interface; this proof supplies its parameters automatically on a concrete varying original-input class.
Using an old theorem in that final step does not turn the preceding automatic arithmetic application into a tautological assumption of the desired bound.
Conversely, no global-priority or all-literature novelty conclusion follows from this application.

The ADZ and bounded-index-abelian height theorems cannot yield one uniform positive absolute-height bound on this entire unit class, since(4) directly contradicts such a bound.
For the specific central subgroup selected here the exact ADZ relative local degree is[B:Q], as(2) records; choosing a larger center or a different prime would require its own verified degree bound.
This comparison does not say that every individual input escapes ADZ or AZ10.

B alone has residue degree1 at2 and is already covered by the old original-residue criterion.
Adding arbitrary A does not preserve that bounded original residue-degree condition, as(5) shows on actual original polynomials.
The old criterion on a positive fraction, its auxiliary-ratio version and other-prime instances remain valid; they are not refuted by this control.

CDPT26 already provides a total-measure gap on the entire fixed field Q(sqrt2)(mu,u^(1/2),u^(1/4),...), including the division-group branch.
Thus the particular B_n models and their cyclotomic composita in(3)--(5) are not themselves new total-gap coverage.
The present arithmetic hypothesis instead allows EVERY finite Galois2-extension unramified outside2.
Sch14 identifies that actual class by its pro-2 presentation and finite realization criterion, but those facts alone do not prove any particular noncontainment in a fixed radical field.
No inspected source comparison supplies one fixed K and finitely generated Gamma covering the whole class with a uniform constant.
Allowing K or Gamma to vary with B does not provide such a constant.
This is the exact retained comparison boundary, not an assertion that no other theorem covers that entire class.

This candidate resolves the stated automatic p=2,f=kappa=1 supply on the full arithmetic class and gives its complete old-criterion consequence.
Whether to treat that scoped result as completing the current D42 inquiry is a separate Task/Strategy decision after whole independent review; the unrestricted G0001 Mahler-gap contract remains unresolved.

## Current assessment
[Selected decision](#decision-current-complete-residue-mass-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:20 |
| status | open |
| reason | Register the complete actual dyadic-compositum parameter supply and log2/12 bound, with exact unit-height and original-residue controls and carefully bounded existing-source comparisons. Root and the drafting agent contributed; independent whole review and any broader completion decision remain required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full arithmetic class and controls](#statement) | Every allowed A,B and original unit, central actual Frobenius, uniform total gap, exact ADZ cost and symbolic original-polynomial comparison controls. |
| argument | [Complete actual-field proof](#argument) | Maximal2-subgroup lemma, both ramification contradictions, global/local disjointness and full product, actual lift and original-field restriction, all polynomial/degree/discriminant/height/reduction calculations. |
| dependency | [Actual2-ramified source](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Precise quadratic classification and established arithmetic field class; broader presentation used only for scope identification at its inherited-proof limit. |
| dependency | [Complete original powered bridge](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Supplied p=2,f=k=1 with actual nontorsion unit and original multiplicities gives log2/12. |
| dependency | [Actual local-degree interface](Yin_C_G0179_v1.md#local-degree-source-interface) | Decomposition/inertia, prime towers and local degrees including nonnormal intermediate fields. |
| dependency | [Monic Eisenstein criterion](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Applied exactly to monic P_n(X+1), all lower coefficients divisible by2 and constant-2. |
| dependency | [Complete-valued-field simple-root lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual finite unramified completions, integral residue representatives, positive polynomial valuation and unit derivative, with all distinct roots retained. |
| dependency | [Exact unramified-normal-closure source interface](#unramified-lifting-source-interface) | Directly inspected The26b Lemma113.8/Tag0EXR at printed/PDF334--335 and exact Con26e applicability; no extension of The26b-U001's historical scope. |
| support | [Precise existing-source comparisons](#prior-coverage-boundaries) | Absolute versus total height, bounded original residue mass, fixed radical towers and the unresolved whole-class source inclusion/novelty boundary. |
| support | [Complete input and search scope](#inputs-and-source-screen) | Actual logical/comparison roles and bounded primary-source search, without a field-wide negative literature claim. |
| support | [Old original residue theorem](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Automatic B-only domain and fixed-F failure on actual A B controls at2, preserving auxiliary and other-prime coverage. |
| support | [Exact centralizer comparison](Yin_C_G0179_v1.md#statement) | Selected-lift inertia quotient and relative local degree, without optimizing over all possible source applications. |
| support | [Old ADZ height theorem](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Exact absolute-height and local/base-degree parameters, not a uniform bound for the growing inertia class. |
| support | [Bounded-base abelian height theorem](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Actual absolute-height scope and lack of an automatic bounded base degree for this whole class. |
| support | [Fixed-radical comparison](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Actual fixed-generator preprint theorem and division-group total-gap branch, not a uniform theorem for varying K or Gamma. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:42 |
| status | proved |
| authority | Internal adoption within Yin's selected four-inquiry continuation. |
| reason | Adopt the whole actual dyadic-compositum theorem through noncontributor R454 and its later source-declaration readback. Every allowed A,B and original nontorsion unit has the automatic central lift and total bound log2/12, with exact local-degree, height-decay and original-residue controls. This does not assert unrestricted G0001 completion or global literature novelty. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full arithmetic class and controls](#statement) | Every allowed A,B and original unit, central actual Frobenius, uniform total gap, exact ADZ cost and symbolic original-polynomial comparison controls. |
| argument | [Complete actual-field proof](#argument) | Maximal2-subgroup lemma, both ramification contradictions, global/local disjointness and full product, actual lift and original-field restriction, all polynomial/degree/discriminant/height/reduction calculations. |
| dependency | [Actual2-ramified source](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Precise quadratic classification and established arithmetic field class; broader presentation used only for scope identification at its inherited-proof limit. |
| dependency | [Complete original powered bridge](../ledger/Yin_L_G0435_v1.md#powered-lift-residue-transfer) | Supplied p=2,f=k=1 with actual nontorsion unit and original multiplicities gives log2/12. |
| dependency | [Actual local-degree interface](Yin_C_G0179_v1.md#local-degree-source-interface) | Decomposition/inertia, prime towers and local degrees including nonnormal intermediate fields. |
| dependency | [Monic Eisenstein criterion](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Applied exactly to monic P_n(X+1), all lower coefficients divisible by2 and constant-2. |
| dependency | [Complete-valued-field simple-root lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual finite unramified completions, integral residue representatives, positive polynomial valuation and unit derivative, with all distinct roots retained. |
| dependency | [Exact unramified-normal-closure source interface](#unramified-lifting-source-interface) | Directly inspected The26b Lemma113.8/Tag0EXR at printed/PDF334--335 and exact Con26e applicability; no extension of The26b-U001's historical scope. |
| support | [Precise existing-source comparisons](#prior-coverage-boundaries) | Absolute versus total height, bounded original residue mass, fixed radical towers and the unresolved whole-class source inclusion/novelty boundary. |
| support | [Complete input and search scope](#inputs-and-source-screen) | Actual logical/comparison roles and bounded primary-source search, without a field-wide negative literature claim. |
| support | [Old original residue theorem](../ledger/Yin_L_G0205_v1.md#local-rigidity-near-one-mass-fixed-scope) | Automatic B-only domain and fixed-F failure on actual A B controls at2, preserving auxiliary and other-prime coverage. |
| support | [Exact centralizer comparison](Yin_C_G0179_v1.md#statement) | Selected-lift inertia quotient and relative local degree, without optimizing over all possible source applications. |
| support | [Old ADZ height theorem](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Exact absolute-height and local/base-degree parameters, not a uniform bound for the growing inertia class. |
| support | [Bounded-base abelian height theorem](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Actual absolute-height scope and lack of an automatic bounded base degree for this whole class. |
| support | [Fixed-radical comparison](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Actual fixed-generator preprint theorem and division-group total-gap branch, not a uniform theorem for varying K or Gamma. |
| review | [Whole dyadic-compositum finding](../audits/reviews/Yin_R_G0454_v1.md#dyadic-composita-whole-independent-finding) | Entire registered arithmetic statement, proof, all original costs and exact prior-coverage limits. |
| review | [Actual source-declaration readback](../audits/reviews/Yin_R_G0454_v1.md#dyadic-source-declaration-readback) | Later explicit Con26e and The26b0EXR interfaces and expanded dependency declarations, with the mathematics unchanged. |


### Decision current-complete-residue-mass-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:42 |
| status | proved |
| authority | Internal adoption within Yin's selected four-inquiry continuation. |
| reason | Maintain exactly the current original L205 support as the complete same-object C491 proof home after reading the full needed consumer scope and complete C491 Sections1--5/equations1--15. Its actual original-degree/all-input/repeated-reduction/no-index-or-ramification-hypothesis mass bound, full same-exponent and cost scope is unchanged. Every other field except this actual date/reason, all nonmatching relations and scopes, review tuples, Statement/Argument, original source/authority and old decisions remain unchanged. Existing review findings keep their actual old inputs; this maintenance does not assert that an old reviewer read C491, add whole independent coverage or select a research Task/E. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full arithmetic class and controls](#statement) | Every allowed A,B and original unit, central actual Frobenius, uniform total gap, exact ADZ cost and symbolic original-polynomial comparison controls. |
| argument | [Complete actual-field proof](#argument) | Maximal2-subgroup lemma, both ramification contradictions, global/local disjointness and full product, actual lift and original-field restriction, all polynomial/degree/discriminant/height/reduction calculations. |
| dependency | [Actual2-ramified source](../audits/literature/Sch14/Yin_U001.md#sch14-u001) | Precise quadratic classification and established arithmetic field class; broader presentation used only for scope identification at its inherited-proof limit. |
| dependency | [Complete original powered bridge](Yin_C_G0580_v1.md#powered-lift-residue-transfer) | Supplied p=2,f=k=1 with actual nontorsion unit and original multiplicities gives log2/12. |
| dependency | [Actual local-degree interface](Yin_C_G0179_v1.md#local-degree-source-interface) | Decomposition/inertia, prime towers and local degrees including nonnormal intermediate fields. |
| dependency | [Monic Eisenstein criterion](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Applied exactly to monic P_n(X+1), all lower coefficients divisible by2 and constant-2. |
| dependency | [Complete-valued-field simple-root lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Actual finite unramified completions, integral residue representatives, positive polynomial valuation and unit derivative, with all distinct roots retained. |
| dependency | [Exact unramified-normal-closure source interface](#unramified-lifting-source-interface) | Directly inspected The26b Lemma113.8/Tag0EXR at printed/PDF334--335 and exact Con26e applicability; no extension of The26b-U001's historical scope. |
| support | [Precise existing-source comparisons](#prior-coverage-boundaries) | Absolute versus total height, bounded original residue mass, fixed radical towers and the unresolved whole-class source inclusion/novelty boundary. |
| support | [Complete input and search scope](#inputs-and-source-screen) | Actual logical/comparison roles and bounded primary-source search, without a field-wide negative literature claim. |
| support | [Old original residue theorem](Yin_C_G0491_v1.md#local-rigidity-near-one-mass-fixed-scope) | Automatic B-only domain and fixed-F failure on actual A B controls at2, preserving auxiliary and other-prime coverage. |
| support | [Exact centralizer comparison](Yin_C_G0179_v1.md#statement) | Selected-lift inertia quotient and relative local degree, without optimizing over all possible source applications. |
| support | [Old ADZ height theorem](../audits/literature/ADZ14/Yin_U001.md#adz14-u001) | Exact absolute-height and local/base-degree parameters, not a uniform bound for the growing inertia class. |
| support | [Bounded-base abelian height theorem](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Actual absolute-height scope and lack of an automatic bounded base degree for this whole class. |
| support | [Fixed-radical comparison](../audits/literature/CDPT26/Yin_U001.md#cdpt26-u001) | Actual fixed-generator preprint theorem and division-group total-gap branch, not a uniform theorem for varying K or Gamma. |
| review | [Whole dyadic-compositum finding](../audits/reviews/Yin_R_G0454_v1.md#dyadic-composita-whole-independent-finding) | Entire registered arithmetic statement, proof, all original costs and exact prior-coverage limits. |
| review | [Actual source-declaration readback](../audits/reviews/Yin_R_G0454_v1.md#dyadic-source-declaration-readback) | Later explicit Con26e and The26b0EXR interfaces and expanded dependency declarations, with the mathematics unchanged. |

