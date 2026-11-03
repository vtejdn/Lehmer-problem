---
author: Yin
---
# CDPT26-U001: fixed radical groups, cyclotomic composita and the remaining full 2-extension class

Date: 2026-10-20T10:07.
Human record author Yin.
The draft_comparison_cleanup AI inspected this primary preprint while screening the continuing D42 automatic powered-Frobenius question.
The first candidate used radicals of a rational prime; root subsequently proposed the unit radical of1+sqrt2 and the substantially larger class of all finite Galois2-extensions unramified outside2.
Those candidate mechanisms are not source theorems or accepted arithmetic constructions merely because they motivate this inspection.

<a id="cdpt26-u001"></a>
## Read; accepted selected comparison statements with preprint limits

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Andrea Conti, Ilaria Del Corso, Arnaud Plessis and Lea Terracini, Small points in radical extensions of number fields, arXiv:2607.29208v1,31 July2026,18-page primary author preprint. No journal publication or later-version equivalence is asserted.

Passages: Printed/PDF pages1--5: height and Property(B), finite rank and division groups, Theorems0.3--0.4, Remark0.6, Corollaries0.7--0.9 and their displayed proofs. Pages16--17: Theorem5.1 and its complete final descent proof. Pages17--18: exact references identifying the earlier height and radical-extension inputs.

Inspection: Read the complete named statements and displayed corollary/remark proofs; read the final descent to understand the finite-extension and discrete-valuation hypotheses. The intermediate Sections1--4, recent p-adic Lie input, Kummer/ramification ancestors and cited binomial irreducibility theorem were not independently audited. The statements are accepted as existing-source comparison inputs at this exact scope, not as an independently verified whole proof or a published theorem.


The unchanged [primary preprint](../../../literature/pdf/CDPT26--arxiv-v1.pdf) and exact version.
The inspected front matter has no printed table of contents; its page5 outline describes the five sections.
Search snippets and an automated secondary summary supplied leads only; the conclusions below were checked against the actual primary PDF.

<a id="division-group-conventions"></a>
### Complete division-group conventions

For a subgroup Gamma of the multiplicative group of algebraic numbers and a set S of rational primes, Gamma^(S-div) consists of all alpha for which alpha^n belongs to Gamma for some positive integer n whose prime divisors lie in S.
For S={p}, write Gamma^(p-div).
For S the set of all rational primes, write Gamma^div.
These sets include the compatible roots of unity arising from1 in Gamma.
The rank of a subgroup is dim_Q(Gamma tensor_Z Q); it is distinct from finite generation.
The main theorem assumes Gamma is finitely generated, not an arbitrary varying union of finite-rank groups.
The set of all roots of unity is denoted mu.
Use the existing complete [height/Property(B) convention](../ADZ14/Yin_U001.md#bogomolov-property): the source bounds absolute logarithmic height outside height-zero elements.

<a id="radical-property-b-criterion"></a>
### Exact general criterion and its fixed parameters

Theorems0.3 and5.1 assume an algebraic extension F/Q, a finitely generated subgroup Gamma of F^*, and a rational prime p, with three hypotheses.
First, F is Galois over some number field.
Second, F' minus Gamma^div has Property(B) for every finite extension F'/F.
Third, some embedding of the algebraic closure of Q into the algebraic closure of Q_p makes the topological closure of F a discrete valuation field.
The bars denoting algebraic closures in the source must not be dropped: an embedding of all algebraic numbers into Q_p itself is not the assertion.
The conclusion is that F(Gamma^(p-div)) minus Gamma^div has Property(B).
The excluded division group is an essential part of the statement.
Neither this theorem nor its finite-prime extension supplies a constant uniform over changing Gamma or changing the base data.

Theorem0.4 treats a fixed finite prime set S and all finite F'/F, under the first two hypotheses and the discrete-valuation condition at each p in S.
It additionally requires Gamma to consist of p-adic units at all but at most one prime of S.
For a singleton S this last requirement imposes no unit restriction.
This is why p=2 and a generator divisible by2 are not excluded from the singleton application.

<a id="cyclotomic-radical-coverage"></a>
### Cyclotomic radical coverage and the division-group branch

Corollary0.7 states that for a fixed finitely generated Gamma in the algebraic numbers, a fixed finite prime set S satisfying that same all-but-one unit condition, and every number field K containing Q(Gamma), the set

    K(mu,Gamma^(S-div)) minus Gamma^div

has Property(B).
The corollary includes all roots of unity, not just the p-power ones.
Its displayed proof adjoins the roots of unity of order prime to S, applies the preceding theorem, and uses the existing abelian-extension height input for finite extensions of that base.
The source's reference[5] is the2000 Amoroso--Zannier paper; it is not the separately registered2010 theorem merely because both authors agree.

Remark0.6 separately states the positive answer to Lehmer's problem on each such fixed field, including Gamma^div minus mu.
Its argument takes the least n such that x^n belongs to Q(mu,Gamma), uses the cited binomial irreducibility theorem to get n as the corresponding relative degree, and then applies the abelian-extension height bound to x^n.
Thus deg(x)h_abs(x)>=n h_abs(x)=h_abs(x^n)>=c_Gamma>0 on that branch.
The full conclusion combines this bound with the Property(B) bound off Gamma^div.
This source proof was read at the stated scope; the cited Lang irreducibility theorem was not independently re-audited.
One must neither omit the division-group branch nor assume it has a positive absolute-height floor.

<a id="fixed-radical-candidate-comparison"></a>
### Exact comparison with the two proposed fixed radical towers

For Gamma=<p> and S={p}, the only algebraic integer units in Gamma^div are roots of unity.
Indeed alpha^n=p^k for integers n>=1,k, and the p-adic valuation of a unit forces k=0.
Corollary0.7 therefore already bounds the absolute height of every nontorsion integer unit in Q(mu,p^(1/p),p^(1/p^2),...).
The numbers p^(1/p^n) themselves are nonunits, have absolute height(log p)/p^n and total measure log p, and supply no exception to this unit statement or a Lehmer counterexample.

For u=1+sqrt2, Gamma=<u>, S={2} and K=Q(sqrt2), Corollary0.7 bounds height only outside Gamma^div in K(mu,u^(1/2),u^(1/4),...).
The unit radicals u^(1/2^n) lie in the excluded group and have heights h_abs(u)/2^n, so this entire unit domain has no uniform positive absolute-height lower bound.
Nevertheless Remark0.6 already gives a positive total-measure gap on the entire fixed field, including that division-group branch.
Consequently the specific fixed-u radical tower with arbitrary cyclotomic composita, retained in [C_G181's exact controls](../../../claims/Yin_C_G0181_v1.md#argument), is not a new total-gap application.
This comparison needs no assertion about the local ramification or full Galois group of each proposed finite model.

Finite abelian A/Q may also be included by the standard Kronecker--Weber embedding into Q(mu).
The established cyclotomic reduction is explicitly used in the already retained [AD00 author manuscript](../../../literature/pdf/AD00--author.pdf), abstract and the transitions following its cyclotomic propositions; those passages were read for this attribution.
No new proof of Kronecker--Weber or claim of an earliest attribution is made.

### Exact source comparison and separate project arguments

The larger proposed class permits every finite Galois2-extension B/Q unramified outside2, together with every finite abelian A/Q unramified at2.
This source has not been shown to place all those B inside one field K(mu,Gamma^(2-div)) with fixed number field K and fixed finitely generated Gamma.
A different Gamma or K for each B would allow the source constants to vary and would not prove a uniform gap for that whole class.
The two fixed radical-tower comparisons do not themselves establish that broader automatic supply.
The actual full-class parameter supply is retained in [C_G181](../../../claims/Yin_C_G0181_v1.md#statement), and its fixed-domain noncontainment in [C_G183](../../../claims/Yin_C_G0183_v1.md#statement).
The original-unit consequence and the simultaneous fixed-domain, residue-degree and absolute-height comparison are separately proved in [C_G185](../../../claims/Yin_C_G0185_v1.md#statement) and [C_G186](../../../claims/Yin_C_G0186_v1.md#statement).
These are project arguments, not conclusions or additional proof inspections of this source unit; their exact limits preserve the distinction from the more general infinite-base hypotheses above.
In particular [C_G183's source interface](../../../claims/Yin_C_G0183_v1.md#pro-two-source-interface) separately records its later reading of Theorem2.1 and Remark2.2 at printed/PDF7, outside this unit's initially selected passages; it does not retroactively supply an independent proof audit of Sections1--4.
