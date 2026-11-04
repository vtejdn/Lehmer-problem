---
author: Yin
---
# Finite global triple-density bounds and exact divisor-downset extremal reduction

Date: 2026-10-12T18:08.
Human author Yin.
Internal fixed extraction under continuing G0001 authorization.
Rounding-recovery authored the original D45 model, partial theorem, finite extremal reduction and conditional implication, and NOW authors this new statement/extraction wrapper.
Root contributed the explicitly credited full-divisor lower control M_N>=N after the finite reduction; both are contributors and cannot independently review this artifact.
Review-recovery separately WHOLE-reviewed the actual entire02:00:08 original in R322.
That finding supports the original partial/conditional proof only and does not prospectively review this wrapper.
Initial status is proof draft / under review, pending a distinct actual extraction review.

## Statement

The registered results below are the UNCONDITIONAL finite bounds/reduction and the explicitly CONDITIONAL implication.
This original Claim proves finite bounds and a conditional implication; it does not itself establish positive-linear capture from positive global triple density.
The later [C96](Yin_C_G0096_v1.md#statement) refutes its universal short-pair premise, while [C142 v2](Yin_C_G0142_v2.md#statement) supplies the abstract positive-density capture implication by a different weak-moment argument.
Automatic positive-density coverage by actual polynomial inputs remains unresolved.

Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d, let K=Q(alpha), and fix a GOOD prime p, so p does not divide disc(P).
Its d reduced roots are distinct nonzero units.
For each occurring multiplicative order o let w_o be the ACTUAL complete number of original reduced roots of that order, with each residue factor contributing its degree ONCE.
Thus

    p does not divide o, w_o in Z_(>0),
    w_o<=phi(o), sum_o w_o=d.

Choose a NONEMPTY subset S of complete occurring groups and put W=sum_(o in S)w_o, so1<=W<=d.
All field norms continue to use d, not W.
For an integer X>=1 define

    h(n)=sum_(o in S, o divides n)w_o,
    H_X=max_(integer1<=n<=X)h(n),
    U_X(a,b)=sum_(o in S, lcm(a,b,o)<=X)w_o,
    T_X=sum_(a,b,c in S, lcm(a,b,c)<=X)w_a w_b w_c,
    Dens_X=T_X/W^3.

The triples are ORDERED independent samples from the probabilities w_o/W, with replacement.
Repeated labels, including all three equal, ARE counted.
This differs from the fraction of distinct group triples and from C88's circular-adjacent score.
Every original root count is an integer, not an arbitrary rational packet weight.

**A. Unconditional finite capture bound.**
Write Harm_j=sum_(r=1)^j1/r for j>=1, and put

    F_X=sum_(a in S, a<=X)(w_a/a)Harm_(floor(X/a)),
    E_X=sum_(a,b in S, lcm(a,b)<=X)w_a w_b/lcm(a,b).

Then

    T_X<=X H_X E_X,
    E_X<=H_X F_X,
    F_X<=sqrt(2W)(1+log X),
    T_X<=X H_X^2 F_X
       <=X H_X^2 sqrt(2W)(1+log X).

In particular for0<delta<=1 with Dens_X>=delta,

    H_X>=sqrt(delta) W^(5/4)
          /[2^(1/4)sqrt(X(1+log X))].

All zero-link and orders-above-X summands are zero.
The X1 endpoint is included.
The selected-W capacity bound is proved directly from w_o<=phi(o), not from treating W as the degree of another polynomial.
H_X is the actual finite peak; Harm_j is a separate harmonic number.

With W>=gamma*d and X<=C*d, for fixed gamma,delta,C>0, this gives a lower bound of order d^(3/4)/sqrt(log d).
The supplied fraction of d tends to zero.
It does NOT establish a positive-linear eta*d capture or discharge L168's input-uniform arithmetic gate.

**B. A sufficient short-pair inequality and the conditional linear consequence.**
For ANY finite nonempty INTEGER capacity array w_a in[1,phi(a)], of total W, and real Y>=1, define

    P_2(Y)=sum_(a,b, lcm(a,b)<=Y)w_a w_b.

Suppose there exists an absolute constant K>0 such that

    P_2(Y)<=K Y W

for EVERY such finite capacity array and EVERY real Y>=1.
This universal premise was open at the original proof stage and is now refuted by [C96](Yin_C_G0096_v1.md#statement).
The implication below is retained as a conditional result and supplies no unconditional application of that false universal premise.
Under this assumption, every actual input in A with Dens_X>=delta>0 satisfies

    H_X>=delta^2 W^2/(4KX).

Indeed the actual pair-link partition gives compatible-third probability at most XH_X/[W lcm(a,b)].
Splitting the pair distribution at epsilon W bounds Dens_X by K epsilon+XH_X/(epsilon W^2); choose epsilon=delta/(2K).
If epsilon W<1 the short-pair part is empty and the same bound holds.
The conclusion uses no average assigned to a particular maximizing pair.

Consequently, UNDER THAT SAME UNPROVED K ASSUMPTION, for fixed0<gamma,delta<=1,C>0 with W>=gamma*d, X<=Cd, there is ONE actual integer n<=X<=Cd such that

    A_p(n)>=eta*d,
    eta=delta^2 gamma^2 log2/(4KC)>0,

where A_p(n) is the full original local norm income defined in F.
The prime may vary.
L168 then gives the strict m(P)>m0(C,eta)>0 at its exact accepted finite-constant scope.
PartA alone does not imply this conditional conclusion.

**C. Exact finite extremal reduction, without a uniform upper bound.**
For every integer N>=1 let

    M_N=max_{0<=x_a<=phi(a), 1<=a<=N, sum x_a>0}
          [sum_(1<=a,b<=N, lcm(a,b)<=N)x_a x_b]
          /[sum_(a=1)^N x_a].

The variables x_a in this definition may be REAL.
The objective extends continuously by0 at the zero vector and has a positive maximum on its compact box.
Nevertheless it has an EXACT full INTEGER maximizer with divisor-closed support:

    M_N=max_{nonempty divisor-closed D subset{1,...,N}}
          [sum_(a,b in D, lcm(a,b)<=N)phi(a)phi(b)]
          /[sum_(a in D)phi(a)].

Divisor-closed means that a in D and b dividing a imply b in D.
The maximum may therefore be restricted to finitely many full-capacity integer sets with NO relaxation gap.
This statement neither identifies the maximizing set nor supplies a uniform upper bound.

For precision, the endpoint argument for one coordinate x has the objective

    f(x)=(x^2+2B0 x+C0)/(x+D0),

where D0 is the other mass, B0 the compatible-neighbor mass and C0 the other numerator.
When D0>0 its derivative numerator is

    Q(x)=x^2+2D0 x+2B0 D0-C0,
    Q'(x)=2x+2D0>0.

Thus its interval maximum is at0 or phi(a); when D0=0 the objective is x.
After endpoint rounding, an active coordinate a has compatible degree Deg_a, including itself, and maximality forces2 Deg_a W0-E0>=0.
A missing divisor b has neighbor mass at least Deg_a.
Its derivative at0 is nonnegative and the derivative numerator strictly increases, so adding any positive allowed mass at b would STRICTLY improve the ratio, a contradiction.
This proves exact downward closure at the finite maximum.

The universal K assumption in B is EQUIVALENT to

    M_N<=K N for EVERY integer N>=1.

For one direction use Y=N.
For the other remove orders a>Y, which cannot contribute to the numerator and can only depress its mass-normalized ratio, apply M_floor(Y), and restore the removed mass.
If all orders exceed Y the numerator is0.
This is equivalence for the larger abstract integer-capacity class, not a claimed equivalence between arbitrary extremizers and irreducible nontorsion polynomial realizations.

**D. Lower control, failed auxiliary bound and actual-realization limits.**
The full divisor set D={a:a divides N} gives sum_(a|N)phi(a)=N and every pair lcm<=N, so its numerator is N^2.
Hence

    M_N>=N for EVERY integer N>=1.

Any universal K in B must therefore satisfy K>=1.
Root suggested this lower control; its complete check is retained.
No equality M_N=N or uniform upper bound follows.

The abstract capacity array with orders1 and an odd prime ell, masses1 and ell-1, has W=ell but

    sum_(a,b)w_a w_b/lcm(a,b)=ell+1-1/ell>W.

It refutes ONLY that stronger proposed reciprocal-energy bound with constant1.
It does not refute B, positive global triple density implying linear capture, or a Mahler gap.

A full divisor set is the exact root inventory of t^N-1 in good characteristic, but that polynomial is cyclotomic and generally reducible.
The finite optimization can also include orders forbidden by a specified prime or reciprocal squarefree input.
No such abstract array is asserted to be an actual irreducible nontorsion counterfamily.
A uniform upper bound for the larger class would suffice for actual inputs; failure in that larger class would still require realization and full-cost work before becoming an actual counterexample.

**E. Small-group boundary checks.**
With one selected group, Dens_X>0 exactly when its order<=X, and then H_X=W.
With two groups, if their joint lcm<=X then H_X=W.
Otherwise every mixed ordered triple is incompatible and

    T_X=sum_(eligible o<=X)w_o^3<=H_X^2 W,
    Dens_X>=delta implies H_X>=sqrt(delta)W.

For general S, let V=sum_(o<=X)w_o and suppose at most k groups are eligible.
Then T_X<=V^3, so Dens_X>=delta gives V>=delta^(1/3)W and some individual eligible order gives H_X>=delta^(1/3)W/k.
Without a UNIFORM k bound this is not a linear capture theorem for an unbounded number of groups.

**F. Complete original norm, physical costs and unresolved scope.**
At every integer n>=1 keep the full signed original norm and exact actual local income

    D_n=Norm_(K/Q)(alpha^n-1)
       =Res(P,t^n-1)
       =product_(all d original roots)(alpha_i^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(all d original p-adic roots)v_p(alpha_i^n-1).

The good-prime floor gives A_p(n)>=h(n)log p at the SAME n, including p2 and arbitrarily deep initial/exceptional valuations on the left.
No exact depth1 equality, discarded original root, powered-degree substitution or upper bound for the remaining local/all-prime income is made.
The maximum H_X is attained in the nonempty finite integer range; it has not been numerically enumerated.

The actual auxiliary is the SINGLE integer polynomial t^n-1 at its full degree n<=X, coefficient content1 and squared coefficient norm2.
No rational coefficient denominator or final indexed packet denominator is introduced.
The full norm and, in the conditional branch, L168's actual norm-tower cost remain paid.

At the original proof stage the global-average-to-linear implication and uniform bound for M_N/N were unresolved.
The later C96 refutes the uniform bound, and C142 v2 establishes the abstract capture implication at the stated totient capacities without it.
Neither result supplies automatic positive triple density for actual near-one polynomial inputs.
C86's ALL-three criterion and C88's circular-adjacent density criterion do not settle this statistic.
C83 has no established positive global triple-density property, and its all-depth local o(d)/full Theta(d) measure scope is not promoted into a counterexample here.
No near-one coverage, all-prime norm upper bound, unrestricted arithmetic-income theorem or G0001 completion follows from this Claim.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T18:08 |
| status | open |
| reason | Register ONLY the unconditional finite sublinear capture and exact full-capacity divisor-downset extremal reduction/lower controls, together with the expressly conditional K-to-linear-income implication. The global-average main bridge and uniform K upper bound remain unresolved. Preserve the ENTIRE actual02:00:08 D45 and original R322 whole scope; this newly authored wrapper awaits a distinct actual extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact partial and conditional statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, explicitly OPEN uniform K assumption, conditional linear income, full norms and unresolved main scope. |
| argument | [Entire original author proof and history](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [L159 actual root capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [L74 full original norm and floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [C86 residual-bucket antecedent](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [C88 unresolved global-average boundary](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [C83 consistency comparison](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Original whole partial-result review](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T18:28 |
| status | proved |
| reason | Adopt original whole R322 and separate actual R325 ONLY for the unconditional finite SUBLINEAR capture, exact full-integer divisor-closed extremal reduction, lower/small-case controls and proved implication from the explicitly OPEN universal K bound. Uniform M_N/N and the ordinary global-density-to-linear-income bridge remain UNRESOLVED; root contributed the lower control and relies on distinct noncontributor findings. All original history remains. This is closeout organization under Yin's instruction to organize current progress and pause; no new exploration or unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact partial and conditional statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, explicitly OPEN uniform K assumption, conditional linear income, full norms and unresolved main scope. |
| argument | [Entire original author proof and history](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [L159 actual root capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [L74 full original norm and floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [C86 residual-bucket antecedent](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [C88 unresolved global-average boundary](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [C83 consistency comparison](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Original whole partial-result review](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |
| review | [Actual independent extraction finding](../audits/reviews/Yin_R_G0325_v1.md#c91-global-triple-partial-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; distinct noncontributor, precise partial/conditional or fixed-rank scope retained. |


### Decision averaged-premise-resolved

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:33 |
| status | proved |
| reason | Retain the exact already-reviewed unconditional finite bounds, finite extremal reduction and LOGICAL conditional implication. The later independently adopted C96 now refutes the formerly open universal K antecedent on full integer divisor downsets. Thus that antecedent is no longer an available research route; no unconditional positive-density-to-linear theorem is adopted. This is a scope reconciliation to the unchanged proof, not a repair, new proof or retrospective extension of R322/R325. See [C96 exact adopted result](Yin_C_G0096_v1.md#decision-organized-reviewed). |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact partial and conditional statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, historical universal K antecedent (now refuted by C96), conditional linear income, full norms and unresolved main scope. |
| argument | [Entire original author proof and history](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [L159 actual root capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [L74 full original norm and floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [C86 residual-bucket antecedent](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [C88 unresolved global-average boundary](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [C83 consistency comparison](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Original whole partial-result review](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0325_v1.md#c91-global-triple-partial-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; distinct noncontributor, precise partial/conditional or fixed-rank scope retained. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, historical universal K antecedent (now refuted by C96), conditional linear income, full norms and unresolved main scope. |
| argument | [Argument](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [Dependency](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [Support](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [Support](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Support](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |
| review | [Review](../audits/reviews/Yin_R_G0325_v1.md#c91-global-triple-partial-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; distinct noncontributor, precise partial/conditional or fixed-rank scope retained. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, historical universal K antecedent (now refuted by C96), conditional linear income, full norms and unresolved main scope. |
| argument | [Exact retained argument](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [Exact retained dependency](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [Exact retained support](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0325_v1.md#c91-global-triple-partial-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; distinct noncontributor, precise partial/conditional or fixed-rank scope retained. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--F: actual root-weighted repeated-label model, unconditional sublinear bounds, exact finite extremal reduction and equivalence, credited lower control, historical universal K antecedent (now refuted by C96), conditional linear income, full norms and unresolved main scope. |
| argument | [Exact retained argument](#argument) | ENTIRE actual02:00:08 D45, all eight anchors/equations1--11, initial model/reuse/failed transfers, full partial and conditional proofs, root lower-control credit, sources/costs/small cases and freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Good-prime distinct counts and w_o<=phi(o); its elementary selected-W capacity split is explicitly repeated, without replacing original d by a new field degree. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, every original root counted once, unramified good-prime first-return lower floor including p2, with complete actual depths retained on the left. |
| dependency | [Exact retained dependency](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Exact residual o/gcd(o,L), real time Lr and disjoint complete masses; the required compatible-only calculation is fully provided in the retained new proof. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | ONLY after the explicitly conditional uniform eta*d same-time certificate, gives strict m>m0(C,eta); accepted finite degree escape and Pri11 source scope unchanged. The unconditional sublinear bound does not discharge it. |
| support | [Exact retained support](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average) | Comparison/provenance: its circular-adjacent score and its expressly open iid global triple-density bridge are distinct. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Actual all-pair synchronization and all-depth2-primary o(d), with full m=Theta(d); no positive global-density property or all-prime upper bound imported. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0322_v1.md#global-triple-partial-whole-independent-finding) | Entire actual02:00:08 D45, equations1--11, all direct interfaces and actual contribution limits. Supports only the original partial/conditional scope and does not prospectively inspect this new wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0325_v1.md#c91-global-triple-partial-actual-extraction-finding) | Entire actual statement, complete retained original and all direct/source/control/cost interfaces; distinct noncontributor, precise partial/conditional or fixed-rank scope retained. |

## Argument

The ENTIRE actual D45 follows, with ONLY its duplicate short author/framework front matter omitted and its first title lowered by one heading level.
Every original model, attempted/failed transfer, equation, anchor, proof, root-provided lower-control contribution, source/cost boundary, small-case check and actual02:00:08 author freeze remains unchanged.
Relative links remain valid from this fixed Claim directory, so no rebasing is needed.
All eight original explicit anchors and eleven numbered equations are retained.

The earlier original creation paragraph records the actual initial broad assignment.
The later contribution section explicitly records root's subsequent lower-control observation; neither history is silently rewritten.
R322 independently reviewed the entire final original at its partial and conditional scope only.
Rounding-recovery now also authors the present statement/extraction, and root remains a contributor through the lower control.
Both require a different reviewer for this actual wrapper.
Current assessment belongs to the selected decision above; retained author-stage pending-review language is historical.

## Global weighted triple density and original-root capture

Date: 2026-10-12T17:42.
Human author Yin.
New AUTHOR inquiry by rounding-recovery under the root's broad question about the global weighted triple average.
Root supplied no construction or intended verdict.
The same author supplied D42 and D44; their earlier reviews and any later extraction retain their own scopes.
All new substantive exploration, successful or failed, belongs here.
No mathematical native program or external source acquisition has been run.

<a id="global-triple-exact-question"></a>
## Exact model and remaining bridge

Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of original degree d, and p a GOOD prime.
For its distinct nonzero reduced roots let O_p be the finite set of actual multiplicative orders and w_o their complete original-root counts.
Thus p does not divide o, w_o is a positive integer, w_o<=phi(o), and sum_o w_o=d.
Select complete groups S with W=sum_(o in S)w_o.
Every norm and actual local income will retain the entire original degree d, even when selected W<d.

For integer X>=1 define

    h(n)=sum_(o in S, o divides n)w_o,
    H_X=max_(1<=n<=X) h(n),
    U_X(a,b)=sum_(o in S, lcm(a,b,o)<=X)w_o,
    T_X=sum_(a,b,c in S, lcm(a,b,c)<=X)w_a w_b w_c,
    Dens_X=T_X/W^3.

The three group labels are ordered and sampled INDEPENDENTLY with probabilities w_o/W.
Repetitions a=b or b=c or all three equal ARE included.
This is a root-weighted average, not the fraction of distinct group triples; every coefficient is an actual integer original-root count.
These conventions also define the statistic without vacuity on one or two groups.

The target is: for fixed gamma,delta,C>0, do W>=gamma*d, X<=C*d and Dens_X>=delta force H_X>=eta*d for some eta depending only on those constants?
An affirmative result must give an actual one-time n<=X and then the full original local income A_p(n)>=(log p)H_X.
A negative example must distinguish an abstract integer-order capacity array from an actual polynomial realization, retaining good reduction, all root/depth data and full Mahler cost.
No near-one coverage is assumed in either case.

The accepted [C86](Yin_C_G0086_v1.md#statement) supplies the ALL-three criterion at its actual adopted scope.
The original D44, now fully retained in adopted [C88](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average), supplies a different circular-adjacent link score and explicitly unresolved global-average branch.
Its ordinary global-average implication was expressly left open.
Those two scores are not silently identified here.

<a id="global-triple-reuse-and-first-failures"></a>
## Reuse and initial failed transfers

L159's actual capacity and short-order average are available; L74 supplies the exact original norm and good-prime floors; L168 supplies the same-time arithmetic-income cost consequence.
C83 supplies an actual all-pair counterfamily with full-depth local income o(d), but it has not been shown to have a positive global triple density.
Its large Mahler cost and local-versus-total-income scope remain unchanged.
The earlier sparse-polynomial L225 witness supplies finite capture times under a different premise and is not presumed.

For one pair with L=lcm(a,b)<=X, the residual partition gives U_X(a,b)<=H_X floor(X/L).
Summing this crude inequality yields a reciprocal-lcm pair sum.
Simply asserting that this pair sum is at most W would be false: for the COMPLETE capacity array of orders1 and an odd prime ell, masses1 and ell-1, the pair sum is ell+1-1/ell>W=ell.
That finite calculation is only a warning about the proposed auxiliary inequality, not an actual polynomial counterexample to the target.

Likewise a general dense hypergraph need not supply the compatible link of a prescribed maximizing-lcm pair.
Such a hypergraph is not automatically an actual root-order incidence structure, so it cannot by itself refute the target.
No proof of the ordinary positive-density bridge or actual counterexample is asserted at this initial checkpoint.


<a id="global-triple-finite-sublinear-capture"></a>
## A finite quantitative consequence that does not yet reach linear mass

The following bound is proved WITHOUT assuming the desired linear conclusion.
It uses the actual root capacities and applies to the precise repeated-label convention above.
Let

    F_X=sum_(a in S, a<=X) (w_a/a) Harm_(floor(X/a)),
    Harm_j=sum_(r=1)^j 1/r, j>=1.

Here Harm_j is a harmonic number; H_X continues to mean only the actual captured-root peak.
Then

    T_X<=X H_X^2 F_X
       <=X H_X^2 sqrt(2W)(1+log X).                    (1)

In particular, whenever Dens_X>=delta>0,

    H_X>=sqrt(delta) W^(5/4)
          /[2^(1/4) sqrt(X(1+log X))].                 (2)

All quantities are actual finite integers or explicit real bounds.
Formula(2) implies a d^(3/4)/sqrt(log d) lower bound in the regime W>=gamma*d and X<=C*d, with fixed positive gamma,delta,C.
Its ratio to d still tends to zero; this theorem does NOT supply the required eta*d arithmetic income.

**Proof.**
For an eligible pair a,b write L=lcm(a,b)<=X.
Its compatible-third groups have residual r=o/gcd(o,L) in1,...,floor(X/L).
Each bucket returns at its own actual time Lr<=X, so every bucket has mass at most H_X.
Therefore

    U_X(a,b)<=H_X floor(X/L)<=H_X X/L.

Pairs with L>X have U_X=0.
Hence, writing

    E_X=sum_(a,b in S, lcm(a,b)<=X)w_a w_b/lcm(a,b),

one obtains T_X<=X H_X E_X.

Fix a<=X.
Partition the b with lcm(a,b)<=X by r=b/gcd(a,b), so lcm(a,b)=ar.
Every bucket is a subset of the roots returning at ar<=X, and its mass is at most H_X.
Thus

    sum_(b:lcm(a,b)<=X)w_b/lcm(a,b)
      <=(H_X/a) Harm_(floor(X/a)).

Multiply by w_a and sum a to get E_X<=H_X F_X.
This proves the first inequality in(1), with all ordered pairs and repetitions included.

For completeness, the selected-mass form of L159's elementary capacity argument is valid directly.
For any integer R>=0, positivity and w_a<=phi(a)<=a give

    sum_(a in S)w_a/a
      <=W/(R+1)+sum_(1<=a<=R)a(1/a-1/(R+1))
      =W/(R+1)+R/2.

Take R=ceil(sqrt(2W))-1.
The same exact one-variable estimate as L159 gives sum w_a/a<=sqrt(2W).
This uses the selected integer total W, not a false assertion that it is the degree of another polynomial.
Since Harm_j<=1+log j<=1+log X, the second inequality in(1) follows.
Rearrangement proves(2).
If T_X>0 then H_X>0, so no positive quantity has been divided by zero.
The X1 endpoint has harmonic number1 and log X0 and is included.

The arithmetic transfer remains honest: at a maximizing actual time n<=X, the full original A_p(n)>=(log p)H_X by L74.
Formula(2) therefore gives only that sublinear lower certificate, with every original root/depth retained.
It does not contradict C83's o(d) full-depth local upper bound.

<a id="global-triple-short-pair-criterion"></a>
## A precisely isolated stronger sufficient lemma

Define the actual SHORT-PAIR mass at real Y>=1 by

    P_2(Y)=sum_(a,b in S, lcm(a,b)<=Y)w_a w_b.

If one could establish an absolute constant K with

    P_2(Y)<=K Y W                                      (3)

for EVERY positive integer capacity array w_a<=phi(a), then the desired triple bridge would follow with a constant depending only on delta,C,gamma.
This is presently a CANDIDATE auxiliary inequality, not an accepted theorem or a supplied external premise.

Indeed let H=H_X and set A=X H/W.
The pair link inequality gives

    Dens_X<=sum_(a,b) (w_a w_b/W^2)
                       min(1,A/lcm(a,b)),

with pairs of lcm>X making no contribution to the true left side.
More usefully, split at a chosen epsilon W.
By(3), the short-pair probability is at most K epsilon.
On all remaining pairs the compatible-third probability is at most XH/(epsilon W^2).
Thus

    Dens_X<=K epsilon+XH/(epsilon W^2).

For delta>0 choose epsilon=delta/(2K).
If the threshold epsilon W<1, there are no such short pairs and that part is0, so the same displayed bound remains valid without invoking(3) below1.
Consequently Dens_X>=delta would imply

    H>=delta^2 W^2/(4K X).                             (4)

At W>=gamma*d, X<=Cd, this is an actual eta*d bound and would close the desired finite bridge.
Every inequality in this CONDITIONAL reduction is explicit.
The unproved step is exactly(3), not the bucket or norm transfer.

The weaker reciprocal-lcm energy bound with a logarithmic factor proved in(1) does not establish(3).
Nor does the maximum-pair capacity W<=max lcm: that maximum statement does not control the weighted lower tail of lcms.
An arbitrary dense abstract graph cannot be used to refute(3) while claiming integer-order realization.
No counterexample to(3) satisfying the required capacities has been verified here.


<a id="short-pair-finite-downset-reduction"></a>
## Exact finite reduction of the auxiliary short-pair problem

For an integer N>=1 define the finite maximum

    M_N=max_{0<=x_a<=phi(a), 1<=a<=N, sum x_a>0}
          [sum_(1<=a,b<=N, lcm(a,b)<=N)x_a x_b]
          /[sum_(a=1)^N x_a].                          (5)

REAL x_a are allowed in this variational definition.
Nevertheless the exact same maximum is attained at FULL INTEGER capacities on a divisor-closed nonempty subset:

    M_N=max_{nonempty D subset{1,...,N}, D divisor-closed}
          [sum_(a,b in D, lcm(a,b)<=N)phi(a)phi(b)]
          /[sum_(a in D)phi(a)].                       (6)

Divisor-closed means that a in D and b dividing a imply b in D.
This is a theorem about the finite auxiliary optimization, not an actual polynomial-realization claim.

**Proof, endpoint reduction.**
Extend the ratio to the zero vector by0.
Its nonnegative numerator is at most(sum x_a)^2, so the extension is continuous at zero and the compact box has a maximum.
The maximum is positive, for example from x_1=1.
Hold all but x_a=x fixed and let D0 be their total mass, B0 their compatible-neighbor mass for a, and C0 their ordered-pair numerator.
Since a<=N the diagonal is compatible, so the objective is

    f(x)=(x^2+2B0 x+C0)/(x+D0).

If D0=0, then B0=C0=0 and f(x)=x for x>0, continuously0 at0, so its maximum is at x=phi(a).
If D0>0, the numerator of f'(x) is

    Q(x)=x^2+2D0 x+2B0 D0-C0,
    Q'(x)=2x+2D0>0.                                   (7)

Thus f is either monotone or first decreasing and then increasing; any interior stationary point is a minimum.
Its maximum on[0,phi(a)] lies at an endpoint.
Starting at a global maximizer and replacing each coordinate in turn by a maximizing endpoint cannot lower its value or exceed the global maximum.
After finitely many steps every x_a is either0 or phi(a).
Hence some global maximizer has the full-capacity form of a subset D.

**Proof, downward closure.**
Let such a full-capacity maximizer have positive total W0 and numerator E0, and suppose a is present while some divisor b of a is absent.
Let Deg_a be the total mass of all present neighbors c with lcm(a,c)<=N, INCLUDING the present a itself.
Varying the coordinate x_a downward from its upper endpoint, maximality forces

    [2 Deg_a W0-E0]/W0^2>=0.                          (8)

If it were negative, a sufficiently small permitted decrease would increase the objective.
This formula also holds when a is the only present coordinate.

Every present neighbor c of a is a neighbor of b, since lcm(b,c) divides lcm(a,c).
Therefore the neighbor mass B_b for the missing b obeys B_b>=Deg_a.
When increasing its absent coordinate from0, the derivative is

    [2 B_b W0-E0]/W0^2>=0.

Its derivative numerator is of the form Q in(7), now with D0=W0>0, and is strictly increasing on x>=0.
Consequently the objective becomes STRICTLY larger for every positive added x_b, even if the derivative at0 equals0.
Adding some allowed0<x_b<=phi(b) contradicts global maximality.
No divisor can be missing, which proves(6).
The argument neither assumes that the support is initially divisor-closed nor silently changes the original actual root counts; it computes a larger finite extremal problem.

For an arbitrary finite capacity array w_a<=phi(a), orders a>Y contribute NOTHING to P_2(Y).
Removing them leaves the numerator unchanged and can only increase its ratio to total mass.
With N=floor Y>=1, its remaining ratio is at most M_N by(5).
Conversely every full-capacity divisor-closed set in(6) is itself a legitimate INTEGER capacity array.
Thus the following two UNIVERSAL AUXILIARY assertions are equivalent:

    P_2(Y)<=K Y W for every finite integer capacity array and every real Y>=1;

    M_N<=K N for every integer N>=1.                  (9)

The forward direction takes Y=N.
The reverse uses M_N<=KN<=KY and restores any removed positive mass.
If all orders exceed Y then P_2(Y)=0 separately.
Real optimization in(5) introduces no relaxation gap, because a full INTEGER maximizer exists by(6).

This reduction is finite and exact for each N.
It is not a proof that M_N/N is uniformly bounded.
No subset enumeration, asymptotic scan, numerical maximization or guessed optimizer has been performed.

<a id="short-pair-lower-control-and-boundaries"></a>
## A lower control and the remaining actual-input boundary

After the preceding finite reduction had been communicated, root suggested checking the full divisor set of floor Y as a lower control.
That specific observation is credited to root; the endpoint/downward-closure proof and the global-average/partial-capture calculations above were supplied by this author.
The following check is local and complete.

For integer N>=1 take D={a:a divides N} with x_a=phi(a).
Counting all N-th roots by exact order gives sum_(a|N)phi(a)=N.
Every pair in D has lcm dividing N and therefore at most N.
Its numerator is N^2, so

    M_N>=N.                                           (10)

Consequently any universal K in(9) must satisfy K>=1.
This verifies a lower bound only.
Neither M_N=N nor any uniform upper bound has been proved here.
This root-suggested observation does not enter the partial theorem(1)--(2) or the conditional implication(3)--(4).

The divisor set is an exact integer capacity array; it also describes the roots of t^N-1 in good characteristic.
That polynomial is cyclotomic and generally reducible.
It is NOT an actual irreducible nontorsion counterfamily to the main problem, and no full Mahler or valuation claim for such a family follows from it.
The finite optimization can include orders excluded by a specified good prime, or order1/2 excluded by a reciprocal squarefree reduction.
These additional actual constraints are not asserted by the auxiliary extremizer.
A uniform upper bound for the larger class WOULD suffice for the actual class; failure in the larger class would still require actual realization and cost work before becoming a counterexample in the intended domain.

The earlier reciprocal-energy warning using orders1 and an odd prime ell is likewise a fully checked capacity calculation only: its total W=ell and sum w_a w_b/lcm(a,b)=ell+1-1/ell.
It refutes only that proposed energy upper bound with constant1.
It does not refute(9), positive global triple density implying linear capture, or a Mahler gap.

For completeness, the repeated-label convention is benign at the smallest group counts.
With one selected group, Dens_X>0 exactly when its order<=X, and then H_X=W.
With two groups, if their joint lcm<=X again H_X=W.
If it exceeds X, every mixed ordered triple is incompatible and

    T_X=sum_(eligible groups o<=X)w_o^3<=H_X^2 W.

Thus Dens_X>=delta implies H_X>=sqrt(delta)W in the two-group case.
This is a boundary check, not a result covering an unbounded number of occurring groups.
In general the eligible mass V=sum_(o<=X)w_o satisfies T_X<=V^3; if there are at most k eligible groups, some group alone gives H_X>=delta^(1/3)W/k.
Without a uniform k bound this also fails to yield a uniform fraction.

<a id="global-triple-full-norm-and-source-scope"></a>
## Complete arithmetic scope, accepted inputs and author check

For every actual input used in the positive partial theorem, retain the full signed original-degree norm

    D_n=Res(P,t^n-1)=product_(all d original roots)(alpha_i^n-1),
    A_p(n)=(log p)v_p(|D_n|).

Nontorsion makes every D_n nonzero, and monicity/unit integrality makes |D_n| a positive integer.
At the good prime every original returned root has actual valuation at least1, including p2, and every nonreturned root has valuation0.
Therefore A_p(n)>=h(n)log p for the SAME actual time n.
The original local valuations, possible deeper initial or exceptional values, unselected groups and other-prime contributions are all retained.
No exact depth1 equality or upper bound on the rest of the norm is inferred.

A maximum in H_X is attained at an integer1<=n<=X because this is a nonempty finite range.
Under the partial lower bound(2), its full income is at least the displayed root-mass bound times log p.
Under the STILL UNPROVED uniform auxiliary bound(9), the CONDITIONAL consequence(4) would instead yield, for W>=gamma*d and X<=C*d,

    A_p(n)>=eta*d,
    eta=delta^2 gamma^2 log2/(4KC)>0.                 (11)

Only in that latter conditional case does the uniform same-time [L168 criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) immediately give a uniform positive m0(C,eta).
Its existing finite constants and accepted Pri11 statement/applicability scope remain unchanged.
Formula(2) alone has a degree-dependent fraction tending to zero and does not discharge that gate.

The physical auxiliary is t^n-1 at its full actual degree n<=X, coefficient content1 and squared coefficient norm2.
The complete original field norm, rather than a smaller powered degree or an unpriced factor, is used.
No rational packet coefficient denominator or indexed weight denominator is introduced.
All root weights here are integer counts forced by an actual good-prime reduction, not freely selected positive rational packet weights.

The mathematical inputs are the precise [L159 capacity proof](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity), reused locally with selected total W; [C256 original norm/floor convention](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail); [C86's retained residual argument](Yin_C_G0086_v1.md#triple-anchored-residual-cover), whose simple needed calculation is fully repeated here for links; and [C88's exact unresolved global-average boundary](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average).
[C83](Yin_C_G0083_v1.md#statement) is only a consistency comparison with its all-depth local o(d) and full Theta(d) cost; no positive triple density is claimed for that family.
L225 remains a different supplied-sparse-polynomial hypothesis.
No external theorem about GCD/lcm extremal sums was found, imported or presumed.

The bounded local search used the specific lcm sums, root capacities, weighted triples and divisor-closed/extremal terms in existing G materials.
It located the above interfaces, not a proof of(9).
This is not a novelty certificate or an exhaustive external literature search.
The local derivative and finite divisor arguments are fully supplied without disguising an unresolved uniform upper estimate as a classical theorem.

The author checked: all ordered/repeated labels; zero-link and all-orders-above-X cases; compatible-only residual buckets; the two independent appearances of H_X in(1); the harmonic/peak distinction; the selected-W capacity split and all exponent/constant directions; X1; the exact short-pair conditional splitting including epsilon W<1; compact extension at zero, endpoint extrema, the active-coordinate one-sided derivative, missing-divisor neighbor inclusion and STRICT improvement; restoration of removed mass; full divisor lower control; one/two-group cases; full norm and nonuniform-versus-uniform gate scope.
No mathematical native program, source acquisition, computation group or adoption was performed.

The specific full-divisor lower control contribution from root is disclosed above, so a noncontributor must review this entire candidate.

<a id="global-triple-partial-entire-author-freeze"></a>
## Entire partial-result author freeze

2026-10-12T18:00.
Freeze the ENTIRE actual model/reuse/failure account, equations(1)--(11), the complete unconditional sublinear capture theorem, exact finite downset reduction and lower control, the explicitly CONDITIONAL uniform short-pair-to-linear-income bridge, all small-case/full-norm/source/contribution limits and this freeze.
The main ordinary global-density implication remains UNRESOLVED: neither a uniform upper bound for M_N/N nor a genuine actual-polynomial counterexample was obtained.
This is useful finite partial progress and a precise remaining obligation, not a proof of one-time Omega(d) capture or unrestricted G0001.
A separate whole reviewer will check the stated partial and conditional scopes.
