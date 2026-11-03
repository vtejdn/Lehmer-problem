---
author: Yin
---

# Complete full-field Salem relative regulator and every ordinary-index price

This retains the complete necessary mathematical argument from [complete original L400](../ledger/Yin_L_G0400_v1.md#salem-regulator-finding).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let alpha be a genuine Salem number, K=Q(alpha), [K:Q]=2t>=4, sigma its inverse involution and F=Q(alpha+alpha^(-1)), a totally real field of degree t.
Let tau>1 be the smallest Salem number in the full field K at the accepted fixed-field generator scope.
Then Q(tau)=K, alpha=tau^a for an integer a>=1, and sigma has the same fixed trace field F.
Use FULL integer-unit groups U_K=O_K^*, U_F=O_F^*, with mu_K=mu_F={1,-1}.
In Sun18's norm-in-mu and deleted-place determinant convention,

    E_(K/F)={u in U_K:Norm_(K/F)(u) in mu_F}
           =ker Norm_(K/F)={+/-tau^j:j in Z},
    Reg(K/F)=log tau.

The equality with norm one uses positivity at the t-1 nonsplit real places and t>=2.
The normalized determinant deletes one archimedean place above every place of F, leaving exactly one real row of weight1 and the free generator tau.
This is not an unnormalized Euclidean covolume or an ordinary-regulator ratio.
For the ordinary regulators R_K,R_F with complex row weights2, put

    Q=[U_K:U_F E_(K/F)],
    i=[U_F:mu_F Norm_(K/F)(U_K)].

Both actual quotient maps and torsion costs give

    Q in {1,2,4}, Q divides2^(t-1),
    i Q=2^(t-1),
    R_K/R_F=i log tau=2^(t-1)log tau/Q.

These statements do not assert realization of every Q value in every degree; in particular t=2 excludes Q=4.
The identities follow from the full norm-one group, u/sigma(u), the square-unit quotient and the actual weighted determinant, without a maximal-order replacement by a smaller order or an uninspected index theorem.
At the exact GH01 author-manuscript statement scope, its Salem unit e=tau^b and tau=e^(j/2), for positive integers b,j, satisfy b j=2 and b Q=2u with u in{1,2}; its displayed2^(t-2)log(e)/u agrees with the above ordinary ratio.
This is a normalization comparison, not a new original Stark or Chinburg proof audit.

Grant ONLY FOR AN IMPLICATION TEST the ordinary-ratio bound AS REPORTED in the inspected published secondary Paz14 Theorem3.5,

    R_K/R_F >= (c1*c2^2)^t,
    c1=11.5^(-39), c2=1.15, kappa=c1*c2^2<1.

It yields only

    log tau>=Q*kappa^t/2^(t-1)>=2*(kappa/2)^t,

whose right side tends to zero with t.
No original FS99 full text/proof, later correction, strongest-current-bound claim or source-original theorem acceptance is inferred from this secondary report.
A uniform positive lower bound for the rank-one normalized Reg(K/F) is a uniform positive lower bound for log tau itself on these Salem fields.
In particular a hypothetical absolute-positive rank-relative bound c0*c1^rank would give that missing gap at rank1; it is an explicitly conjectural boundary at the inspected GH01 scope.
Sun18's different intersection of units over two DISTINCT real quadratic subfields has rank|A_K|-3=t-2, not this norm-one rank1.
Their compositum has degree4, so t=3 is impossible; a high-rank covolume lower bound does not control this individual direction without charging the other directions and lattice index.
An actual smaller-order generator eta=tau^b with possibly unbounded b has log eta=b log tau, and its larger logarithm supplies no free uniform lower bound for tau.
The complete original four-section proof, formulas1--5, seven exact source/comparison scopes, actual source inspection/contribution/conditional/negative limits and full-ring versus actual-order distinction follow below.
No regulator computation, field construction, numerical inversion, new gap class or Task/E transition is asserted.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:27 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Full-field Salem generator](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Only smallest fixed-field Salem generator, full degree and powers at existing selected statement/displayed-proof depth; no quantitative regulator bound. |
| dependency | [Actual full-order unit lattice](../audits/literature/Con26/Yin_U001.md#con26-u001) | Only totally real full-order rank/lattice and finite torsion at actual source-proof limits; no general complex convention imported. |
| dependency | [Exact relative regulator definition](../audits/literature/Sun18/Yin_U001.md#sun18-u001) | Only norm-in-mu group, exact deleted-place weights and ordinary identity; distinct high-rank theorem at statement scope, no analytic or ancestor proof audit. |
| dependency | [GH01 normalization and conjectural comparison](../audits/literature/GH01/Yin_U001.md#gh01-u001) | Only identified author-manuscript unit/index/power statements as normalization cross-check and expressly conjectural rank-relative bound; no original proof/publication equivalence. |
| dependency | [Paz14 secondary implication test](../audits/literature/Paz14/Yin_U001.md#paz14-u001) | Only exact ordinary-regulator convention and published SECONDARY report, granted conditionally for the failed implication; no direct FS99 text/proof/correction acceptance. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:30 |
| status | proved |
| reason | Adopt the entire exact registered statement and retained original proof after direct whole SELF inspection, preserving all original source/author/review/native/date and conditional/negative/remaining boundaries. This current construction supplies no old-date review, new source proof, native experiment or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Only smallest fixed-field Salem generator, full degree and powers at existing selected statement/displayed-proof depth; no quantitative regulator bound. |
| dependency | [Exact dependency](../audits/literature/Con26/Yin_U001.md#con26-u001) | Only totally real full-order rank/lattice and finite torsion at actual source-proof limits; no general complex convention imported. |
| dependency | [Exact dependency](../audits/literature/Sun18/Yin_U001.md#sun18-u001) | Only norm-in-mu group, exact deleted-place weights and ordinary identity; distinct high-rank theorem at statement scope, no analytic or ancestor proof audit. |
| dependency | [Exact dependency](../audits/literature/GH01/Yin_U001.md#gh01-u001) | Only identified author-manuscript unit/index/power statements as normalization cross-check and expressly conjectural rank-relative bound; no original proof/publication equivalence. |
| dependency | [Exact dependency](../audits/literature/Paz14/Yin_U001.md#paz14-u001) | Only exact ordinary-regulator convention and published SECONDARY report, granted conditionally for the failed implication; no direct FS99 text/proof/correction acceptance. |
| review | [Exact review](../audits/reviews/Yin_R_G0698_v1.md#complete-salem-regulator-whole-self-finding) | Entire genuine Salem/full-ring/relative-rank/normalization/ordinary-index theorem and every conditional secondary/high-rank/actual-order/source boundary. Entire original L400 account, all four sections/formulas1--5, seven fixed inputs and full proof, source inspections/contributions/failed-implication/remaining limits. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-18T13:14.
Human author Yin.
Root requested this bounded source/applicability inquiry; loglog_cyclic_review inspected the sources and developed the exact normalization and index calculation below.
This is author-level retained analysis, not a new accepted Claim, independent review or source-original proof audit.
No regulator computation, field construction, parameter scan or numerical inversion was performed.

<a id="salem-regulator-finding"></a>
## Finding

For the FULL field K generated by a genuine Salem number, let tau be its smallest Salem number and let F=Q(tau+tau^(-1)).
With the inspected deleted-place convention, the normalized relative regulator is exactly

    Reg(K/F)=log tau.                               (1)

The ordinary regulator ratio is a different quantity.
Writing [F:Q]=t and

    Q=[O_K^*:O_F^* ker N_(K/F)],
    i=[O_F^*:mu_F N_(K/F)(O_K^*)],

one has

    Q in {1,2,4}, Q divides2^(t-1),
    iQ=2^(t-1),
    R_K/R_F=i log tau=2^(t-1)log tau/Q.              (2)

Thus the growing factor is real and belongs to the ordinary regulator ratio, not to (1).
A uniform positive lower bound for the rank-one quantity (1) is precisely a uniform positive gap for the smallest Salem generators.
It is not supplied by the bounded source interfaces inspected here.
The reported ordinary-ratio bound examined below yields only an exponentially decaying bound after the exact conversion, and the inspected high-rank intersection theorem does not control this single direction.
No new total-Salem-measure gap class is obtained in this bounded inquiry.

<a id="salem-regulator-source-screen"></a>
## 1. Reuse and exact inspected sources

The accepted [L385 actual-order generator](Yin_C_G0454_v1.md#actual-order-relative-unit-generator) and [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001) distinguish full-field Salem generators from generators of an actual-order subgroup.
[L388](Yin_C_G0009_v1.md#actual-order-units-in-every-log-cone), using the accepted [Con26-U001](../audits/literature/Con26/Yin_U001.md#con26-u001), supplies the logarithmic full unit lattice and its rank, but no uniform regulator lower bound.
These actual scopes were read before the new comparison.
The local bibliography and source-unit search found no existing regulator account covering the needed normalization.

The supplied Hironaka URL is a different work from Hir01 and Hir06.
The actual source is the30-page Ghate--Hironaka manuscript dated15August2000, corresponding to their2001 Bulletin AMS paper.
[GH01-U001](../audits/literature/GH01/Yin_U001.md#gh01-u001) retains the inspected Sections5.1--5.2, author pages22--24, the visually checked power-of-two and unit-index factors on page23, and the expressly conjectural rank-relative lower bound.
Original Stark and Chinburg proofs and the published GH01 rendering were not inspected.
Those formulas are a normalization cross-check, not unexamined proof premises of (1)--(2).

The published [Sun18-U001](../audits/literature/Sun18/Yin_U001.md#sun18-u001), printed131--135/PDF2--6 with printed132 visually inspected, gives the complete relative-unit and deleted-place regulator definition and its ordinary-ratio identity.
It also states the paper's different high-rank intersection result.
Its analytic proof and the original Costa--Friedman and Friedman--Skoruppa proofs were not audited.
The ordinary regulator convention and the reported general ratio bound were checked directly in [Paz14-U001](../audits/literature/Paz14/Yin_U001.md#paz14-u001), with Theorem3.5 on printed53/PDF8 visually inspected.

FS99's publisher supplied bibliographic metadata and subscription access, not its full text.
Paz14 is a PUBLISHED SECONDARY REPORT of that theorem, not direct inspection of FS99.
The calculation in Section4 is deliberately an applicability test of the inequality AS REPORTED, even granting its stated constants; it does not claim source-original acceptance, original-proof inspection, or resolution of later constant/proof corrections.
A bounded discovery search also indicated later discussions of corrections to intermediate FS99 estimates, but no such discussion is used as a mathematical premise or as a verified erratum account here.
No exhaustive survey or strongest-current-bound claim is made.

<a id="salem-relative-regulator-identity"></a>
## 2. The normalized relative regulator is log of the full-field generator

Let alpha be a genuine Salem number, K=Q(alpha), d=2t>=4, and sigma its inverse involution.
The trace field F=Q(alpha+alpha^(-1)) is totally real of degree t.
K has two real places above the distinguished real place of F, and one complex place above each of the other t-1 real places.
The fixed-field theorem gives a smallest Salem number tau in K, and every Salem number in K is tau^a for a positive integer a.
In particular alpha=tau^a, Q(tau)=K and its inverse involution fixes the same F.
Both mu_K and mu_F equal {1,-1}, since K has a real embedding.

Sun18 defines E_(K/F) as full integer units whose relative norm belongs to mu_F.
At each of the t-1 nonsplit real places of F, a relative norm of a nonzero K-element is a positive squared complex modulus.
Since t>=2, that norm cannot be the constant -1.
Consequently

    E_(K/F)=ker(N_(K/F):O_K^* -> O_F^*).             (3)

Every element w of (3) has modulus1 at all complex places of K.
If its distinguished real value has absolute value1, injectivity of that embedding forces w=1 or w=-1.
Otherwise a sign and, if necessary, inversion make its distinguished value greater than1, its other real value its positive inverse, and all complex values unit-modular.
If this number generated a proper subfield of K, its expanding conjugate would repeat more than once among K's embeddings, which is impossible.
It is therefore a genuine full-degree Salem number in K.
The accepted Smy15 fixed-field theorem now gives

    E_(K/F)={+/-tau^j:j in Z}.                       (4)

This is the full-ring group; membership in a smaller order is not assumed.

In the Sun18 determinant delete one archimedean place of K above every place of F.
All t-1 complex places are deleted, as is one of the two real places.
Only one real place remains, with weight1, and tau is a free generator of the rank-one group (4).
The resulting one-by-one determinant is abs(log tau)=log tau.
This proves (1) without a hidden complex weight2, Euclidean sqrt(2) covolume, or ordinary-regulator factor.

<a id="salem-unit-index-prices"></a>
## 3. Every ordinary-regulator index and power of two

Write U_K=O_K^*, U_F=O_F^*, E=ker N_(K/F), and Q=[U_K:U_F E].
The homomorphism

    delta:U_K -> E, delta(u)=u/sigma(u)

has kernel U_F.
Since delta(tau)=tau^2 and delta(-1)=1, its image contains <tau^2>, and

    U_K/(U_F E) is isomorphic to delta(U_K)/<tau^2>.

By (4), the latter is a subgroup of {+/-tau^j}/<tau^2>, a group of order4.
Hence Q is finite and lies in {1,2,4}.

The norm map has kernel E, takes U_F to U_F^2 and induces

    U_K/(U_F E) is isomorphic to N_(K/F)(U_K)/U_F^2.

Thus the latter quotient has order Q.
The norm image cannot contain -1, by the nonsplit-place positivity already used in (3).
Dirichlet's unit rank gives |U_F/U_F^2|=2^t, including its torsion {1,-1}.
Adjoining -1 to the norm image doubles its quotient over U_F^2, so

    i=[U_F:{+/-1}N_(K/F)(U_K)]=2^t/(2Q)=2^(t-1)/Q.

This proves the index part of (2), including Q dividing2^(t-1).
For t=2 this divisibility automatically excludes Q=4.

The regulator identity can also be checked directly, without importing an uninspected index formula.
Take a free unit basis of U_F and append tau.
In the weighted logarithmic matrix for K, delete one real row.
The tau column is log tau in the remaining real row and zero in every complex row.
Every complex row of a base-unit column is twice the corresponding real logarithm for F.
Expansion along the tau column gives subgroup regulator

    2^(t-1)R_F log tau.

The subgroup U_F E contains the full torsion of U_K and has index Q, so its regulator is Q R_K.
Therefore R_K/R_F=2^(t-1)log tau/Q=i log tau, completing (2) and agreeing with Sun18's reported general ratio identity.

The GH01 source provides a consistent independent normalization comparison at its actual statement scope.
Its e is a Salem number, so e=tau^b for a positive integer b.
The source's assertion that tau=e^(j/2) gives bj=2, hence b is1 or2.
Since the source index of U_F<e> is2u, with u in{1,2}, one has bQ=2u.
Its ratio formula becomes

    2^(t-2)log(e)/u
       =2^(t-1)log(tau)/Q,

exactly the independently derived expression above.
This comparison consumes neither the original Stark proof nor any algorithm for finding e or tau.

<a id="reported-regulator-bound-diagnosis"></a>
## 4. The concrete lower-bound chain and why it gives no new gap

Paz14 Theorem3.5 reports the ordinary ratio inequality

    R_K/R_F >= (c1*c2^[K:F])^[F:Q],
    c1=11.5^(-39), c2=1.15.

Grant that reported inequality in full and write kappa=c1*c2^2.
A Salem extension has [K:F]=2 and [F:Q]=t, so (2) gives only

    log tau=(Q/2^(t-1))(R_K/R_F)
       >=(Q/2^(t-1))*kappa^t
       >=2*(kappa/2)^t.                             (5)

The explicit kappa is below1: c2<2 and c1<1/4 already suffice.
Thus the right side tends to zero as t grows.
This is weaker in its degree behavior than a uniform positive lower bound, even before asking whether more refined source hypotheses can improve it.
The calculation does not refute a Salem gap; it shows that this particular bound cannot establish one.
If one had the stronger normalized inequality Reg(K/F)>=kappa^t, it would still decay for these constants, rather than supply a gap.
No uninspected normalized FS99 theorem is asserted by this observation.

A full rank-relative inequality Reg(L/F)>=c0*c1^(rank(E_(L/F))), with fixed positive constants, would give Reg(K/F)>=c0*c1 at relative rank1.
By (1) that is a uniform lower bound for log tau itself.
On the Salem extension class, this is the original positive-gap question in regulator notation, exactly the conjectural boundary highlighted in GH01.
The local calculation does not make that missing lower bound easier or establish it for a new class.

Sun18's new theorem instead bounds Reg_(F1,F2)(K), for the intersection of relative units over TWO distinct real quadratic subfields.
That group's rank is |A_K|-3=t-2, not the rank1 group in (4).
The compositum has degree4, so if both quadratic fields are present then4 divides2t; the case t=3 that would give rank1 cannot occur.
For its stated large-degree range the rank therefore grows.
When the two subfields lie in F, the Salem relative units lie inside that intersection by norm transitivity, but its covolume lower bound does not lower-bound this individual direction without an upper control on the other unit directions and the relevant lattice index.
Even abstractly, fixed or large lattice covolume does not prevent a short basis vector when other basis directions lengthen.
No such additional arithmetic upper control is supplied by the inspected source.

Finally, a generator eta for an actual smaller-order relative-unit subgroup has eta=tau^b for an integer b>=1, as in L385.
Its larger log eta is not the full-ring normalized Reg(K/F), and a lower bound for it cannot simply be divided by an unbounded b to obtain a uniform bound for tau.
This preserves the actual-order/full-field distinction throughout.

## Outcome and retained limits

The useful result of this bounded inquiry is the exact normalization (1)--(2) and the explicit failed implication (5), with all degrees and indices paid.
The source-normalized relative regulator is a valid restatement of the primitive Salem logarithm; the inspected general lower bounds do not provide a new arithmetic coverage class.
The next genuinely different input would have to control this rank-one regulator uniformly, or provide concrete additional arithmetic information yielding such control after all other directions and indices are charged.
No construction, numerical calculation, new Claim, independent acceptance or G0001 execution transition is made.
The original FS99 text and later correction details remain uninspected; this limits the stated literature claim to the exact primary definitions and published secondary bound actually read.

<a id="salem-regulator-fixed-inputs"></a>
## Exact fixed input and comparison scopes

| Role | Target | Scope |
| --- | --- | --- |
| Full-field generator | [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Smallest Salem generator, powers and full degree in a fixed Salem field; no regulator lower bound. |
| Unit rank convention | [Con26-U001](../audits/literature/Con26/Yin_U001.md#con26-u001) | Free unit rank and finite torsion needed for the square-unit quotient and determinant basis; prior source-proof limits retained. |
| Relative regulator definition | [Sun18-U001](../audits/literature/Sun18/Yin_U001.md#sun18-u001) | Deleted-place determinant, relative units with norm in roots of unity, ordinary-ratio normalization and distinct high-rank intersection scope; no new audit of its analytic theorem. |
| Classical normalization comparison | [GH01-U001](../audits/literature/GH01/Yin_U001.md#gh01-u001) | Inspected author-manuscript Stark/Chinburg statements and unit-index factors as a cross-check, plus the explicitly conjectural rank-relative boundary; original proofs and published rendering uninspected. |
| Conditional reported bound | [Paz14-U001](../audits/literature/Paz14/Yin_U001.md#paz14-u001) | Exact published secondary report of FS99, granted only for the displayed failed implication; no original-source theorem/proof or later correction acceptance. |
| Actual-order comparison | [L385](Yin_C_G0454_v1.md#actual-order-relative-unit-generator) | Order-subgroup generator is a power of the full-field generator; no automatic uniform index or regulator control. |
| Prior lattice comparison | [L388](Yin_C_G0009_v1.md#actual-order-units-in-every-log-cone) | Full unit lattice/rank interface, without a regulator lower bound or a short-direction estimate. |
