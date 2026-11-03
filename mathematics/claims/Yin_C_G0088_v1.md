---
author: Yin
---
# Circular compatible-link density and single-time original norm capture

Date: 2026-10-12T17:44.
Human author Yin.
Internal fixed extraction under continuing G0001 authorization.
Rounding-recovery authored the ENTIRE new D44 score proof and controls; root supplied the broad question only.
g0001_review_recovery independently WHOLE-reviewed actual final01:36:12 D44 in R317 and NOW authors this new statement/decision/extraction wrapper.
It is a contributor to this artifact and cannot independently review its actual extraction.
R317 remains original whole support only.
Initial status is proof draft / under review, awaiting a different noncontributor's actual inspection.
The complete candidate, unresolved shortcut, source/role/cost boundaries and original freezes remain below.

## Statement

Fix an ACTUAL monic irreducible P in Z[t] of ORIGINAL degree d>=1, constant coefficient+/-1 and nontorsion root alpha.
Reciprocity is allowed but not required.
Put K=Q(alpha), total m=log M(P)>0, and for every integer n>=1 retain the COMPLETE signed norm

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=abs(D_n) in Z_(>0).

Fix a GOOD rational prime p, meaning p does not divide disc(P).
Its reduction has d DISTINCT nonzero roots.
Let O_p be their finite set of occurring multiplicative orders and w_o the actual number of original roots of order o, with each residue factor contributing its degree ONCE.
Thus p does not divide o, every occurring w_o is a positive INTEGER, w_o<=phi(o), and sum_o w_o=d.
Select ANY nonempty subset S of complete occurring groups, retaining ALL their actual mass, and put W=sum_(o in S)w_o, so1<=W<=d.

**A. Exact finite counting model and score.**
Choose, for each o in S, EXACTLY w_o distinct primitive o-th complex roots of unity as rational angles in[0,1).
These are COUNTING points for the already actual capacities; they need not be P's characteristic-zero conjugates and do not assert a new polynomial realization.
Different exact orders have disjoint points.
Sort the W distinct angles theta_i, with order labels a_i, and define theta_(W+1)=theta_1+1,a_(W+1)=a_1 and

    g_i=theta_(i+1)-theta_i>0, sum_i g_i=1.

For W1 the single gap is1.
Same-order distinct endpoints, repeated order labels, order1 and the circular wraparound are included.
For ANY integer X>=1 define, INCLUDING a=b,

    U_X(a,b)=sum_(o in S, lcm(a,b,o)<=X)w_o,
    Score_X=sum_(i=1)^W U_X(a_i,a_(i+1)),
    H_X(S)=max_(integer1<=n<=X)sum_(o in S, o divides n)w_o.

An anchor can itself appear as the third group.
This counts actual ROOT mass, not the number of groups.
The score is an integer in[0,W^2], and zero links are allowed.
Each such finite certificate can be checked by rational angle comparisons and integer gcd/lcm, but no inexpensive original order inventory, optimal-model algorithm or completed enumeration is asserted.

**B. Constructive single-time capture and full root-count upper bound.**
For EVERY actual input, selection, model and X in A,

    H_X(S)>=Score_X/X,
    Score_X<=X H_X(S)<=X min(W,X).

If Score_X>0, choose an edge i maximizing U_i/g_i, where U_i=U_X(a_i,a_(i+1)).
It has U_i>0, L_i=lcm(a_i,a_(i+1))<=X and B_i=floor(X/L_i)>=1.
Partition ONLY its compatible third groups by

    r(o)=o/gcd(o,L_i), 1<=r(o)<=B_i.

One occupied bucket supplies ONE actual n=L_i*r<=X with p not dividing n and selected returned root mass at least

    ceil(U_i/B_i)>=U_i L_i/X
                   >=U_i/(X g_i)>=Score_X/X.

Other groups returning at that same n remain included.
The gap inequality is g_i>=1/L_i, so the displayed direction is L_i>=1/g_i.
For U_i0 no bucket or L_i<=X assertion is required; U_i<=X H_X g_i still holds.
Summing those inequalities uses the complete circumference1.
H_X<=min(W,X) follows from the ORIGINAL mass capacity and sum_(o|n)phi(o)=n; it bounds ROOT COUNT only, not valuation depth or full local income.
No arithmetic incomes at different times are combined.

**C. Weak coverage certificates, trimming and precise necessary budget.**
If0<delta<=1 and Score_X>=delta W^2, then B captures at leastdelta W^2/X original roots at one actual time.
Necessarily X>=sqrt(delta)W.

Several finite conditions suffice.
If at least k adjacent edges have U_i>=theta W with0<theta<=1, then Score_X>=k theta W.
Thus k>=(1-epsilon)W,0<=epsilon<1, suffices with delta=(1-epsilon)theta, even if every remaining link is zero and nonadjacent anchors are unrestricted.
Alternatively, U_X(a,b)>=theta W for EVERY pair of labels INCLUDING diagonals guarantees Score_X>=theta W^2 for EVERY model.
The old all-three rule on at least3 groups implies theta1, but for one or two groups the at-most-three nonvacuity guard is necessary.

For a precise trimming certificate, let T be a subset of selected groups of total actual mass V and suppose EVERY NONEMPTY subset of T of size AT MOST3 has a common exponent<=X.
Keep all W model points.
At least max(2V-W,0) circular edges have both endpoints in T, and each such edge has link mass at least V.
Hence EVERY model satisfies

    Score_X>=V max(2V-W,0).

In particular V=(1-epsilon)W with0<=epsilon<1/2 gives delta=(1-epsilon)(1-2epsilon)>0.
This includes W1/W2 and requires no contiguous placement of T.
The half threshold is not claimed optimal.
The MAIN score theorem permits DIFFERENT compatible third-group sets at different edges and does not require any one heavy trimming set.
A small score in one model alone does not exclude a different model or a large actual return peak.

**D. Complete original local income and finite measure consequence.**
At the ONE n from B with positive score,

    A_p(n):=(log p)v_p(C_n)
       =(log p)sum_(all d original p-adic roots a)v_p(a^n-1)
       >=(Score_X/X)log p.

Valuations use v_p(p)=1.
The good-prime first-return floor is at least1; the left side keeps every actual initial/exceptional/later depth and unselected returned root.
Prime-to-p time does NOT make initial depth exactly1.
Other primes may add income, and no upper bound for them is claimed.
All original norms remain nonzero and in the original K even if alpha^n has smaller degree.

Fix real0<gamma,delta<=1 and C>0.
If an ACTUAL input has a good prime, a selection with W>=gamma*d, an integer1<=X<=Cd and an actual model with Score_X>=delta W^2, then some ONE n<=Cd has

    A_p(n)>=eta*d,
    eta=(delta gamma^2/C)log2>0.

The prime may vary with the input.
Necessarily C>=gamma sqrt(delta); the stronger C>=gamma restriction from all-three synchronization is NOT imposed.
Applying the accepted L168 same-exponent criterion gives the STRICT bound m(P)>m0(C,eta)>0.
Explicitly choose T_ana>=1,R_ana>=2 so exp(-T_ana)/2+1/R_ana<=eta/4, put

    K_ana=(3exp(T_ana)+T_ana/R_ana)(4R_ana+1),
    tau=min(1,eta/4,eta^2/(16K_ana^2)),
    choose integer B_ana>=55 with log(B_ana)/B_ana<=tau,
    m0=min(tau/C,epsilon_(B_ana)/(2C)).

Here epsilon_(B_ana)>0 is the SAME finite L168 height floor for nontorsion units of degree at most B_ana; its finite enumeration is not executed and no numerical value is claimed.
The actual norm tower and h=nm/d pay for powered-degree drop.
At m<=m0, L168 gives log C_n/d<=3eta/4<eta at that SAME n, contradicting A_p(n)>=eta*d.
No new Dim19 sharpening or source proof is needed for this implication.

Consequently, on a HYPOTHETICAL m->0 sequence, for every fixed gamma,delta,C, sufficiently late inputs fail the score condition at EVERY good prime, EVERY selected W>=gamma*d and EVERY permitted model.
This is a necessary consequence, not proof that the new coverage criterion holds near one or that such a sequence exists.

**E. Actual strict weakening at a smaller linear window.**
Reuse L159's genuine irreducible reciprocal integer-unit family

    F_q(t)=P_Lehmer(t^q), d=10q, rational prime q>41,
    P_Lehmer=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.

Its full measure equals the fixed positive M(P_Lehmer), and3 is good.
The retained base Lehmer prime3 data are masses2,8 at orders4,82.
Since gcd(q,164)=1, the FOUR complete actual groups are

    (4,2),(4q,2(q-1)),(82,8),(82q,8(q-1)).

Take the FULL group set, W=d=10q, X=82q=(41/5)d and T={82,82q}, of mass V8q.
Every order in T divides X.
At most4q circular edges touch the2q outside vertices, so EVERY model has at least6q T-to-T edges and

    Score_X>=48q^2=(12/25)d^2,
    H_X(S)>=(12/205)d,
    some n<=X has A_3(n)>=(12/205)d log3.

The direct time n82q returns EXACTLY the82/82q groups, with root mass8q and actual income AT LEAST8q log3: neither4 nor4q divides82q.
At this SAME window lcm(4q,82q)=164q>X, so this pair has zero link, and the three distinct orders4q,82q,82 are incompatible.
Thus even all-pair and all-three synchronization fail on the FULL set while the new circular score has a fixed positive fraction.
The strict weakening is witnessed by an actual irreducible polynomial; this particular control also has a heavy subset, which the main theorem does not require.

The original q expanding roots, q-th-power degree drop, full signed degree10q norm and fixed positive measure remain.
The old accepted house statement enters only this comparison family's irreducibility argument.
This is not a near-one or all-powers-degree-preserving family, and no new factorization or order run is claimed.

**F. Every-model obstruction, unresolved global average and full costs.**
For any actual selection and model, Score_X<=X H_X(S) and H_X(S)log p<=max_(n<=X)A_p(n).
On the adopted C83 family at its fixed good prime2, for every fixed C>0 and sufficiently large members set X=floor(Cd)>=1.
Its COMPLETE all-depth income satisfies max_(n<=Cd)A_2(n)/d->0, so

    sup_(all permitted actual-count models) Score_X/d^2
       <=(X/d)*max_(n<=X)A_2(n)/(d log2) ->0.

For selected W>=gamma*d, normalization by W^2 adds only the fixed factor1/gamma^2.
This bounds every model's score, preserving C83's all-pair short times and full m(P)=Theta(d); it is not an all-prime norm upper bound or a near-one counterfamily.

The DIFFERENT global ordered weighted triple statistic

    Dens_X=(1/W^3)sum_(a,b in S)w_a*w_b*U_X(a,b)

has no proved implication here to a positive circular score for some model, or directly to one-time linear income.
Circular adjacency frequencies need not equal w_a*w_b/W^2.
The attempted shortcut from a global average to a maximizing-lcm pair is unresolved, and no actual polynomial counterexample to that global-average implication is asserted.
Abstract hypergraphs or arbitrary weights are not substituted for actual root capacities.

The actual arithmetic auxiliary remains the SINGLE integer polynomial t^n-1 at full degree n<=Cd, coefficient content1 and squared coefficient norm2.
Its resultant is the full signed D_n before absolute values and includes all d roots.
No packet q/M, dropped cofactor or smaller powered-field norm is used, and its coefficient energy is not substituted for L168's complete cost.
Bad-prime repeated-root mass, unproved near-one coverage, optimality of the score/threshold, a new universal income mechanism and an unrestricted G0001 gap remain outside.
Existing root/floor/cost/source interfaces retain credit and their recorded acceptance depths.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:44 |
| status | open |
| reason | Register the exact circular compatible-link criterion, constructive one-time root/norm capture, robust finite coverage and finite measure consequence, actual smaller-window strict control, all-model obstruction and explicit unresolved global average. The ENTIRE original final D44 is retained. R317 covers that original only; this new authored wrapper needs separate actual extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F, actual original good-prime counts/model, all edge/zero/small-size cases, one-time bounds, finite constants, exact controls and open boundaries. |
| argument | [Entire retained original body](#argument) | COMPLETE original candidate/reuse/failed-average history and Sections1--7/equations1--22, all nine anchors, sources/roles/costs/controls and actual01:35:12 plus01:36:12 freezes. |
| dependency | [L159 actual root capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual distinct good-prime roots and positive integer complete-group counts w_o<=phi(o), not bad-prime multiplicities or arbitrary real weights. |
| dependency | [L74 original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Whole original K/Q signed norm, every residue-degree contribution, no scalar-content or powered-degree substitution. |
| dependency | [L74 good-prime floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Original first-return lower bounds including p2, with ALL actual depths retained in the full income rather than set equal to the floor. |
| dependency | [L168 finite cost criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | SAME n<=Cd and A_p(n)>=eta*d, exact finite m0 parameters and original-powered-degree accounting. No arithmetic coverage comes from that cost theorem itself. |
| dependency | [L168 finite height floor](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Unchanged finite epsilon_(B_ana)>0 used in m0; no executed enumeration or numerical constant. |
| dependency | [L159 radical control](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure with its retained accepted house scope, only for the comparison family. |
| dependency | [L159 good-prime control](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | Retained base prime3 masses/orders and squarefreeness; new four-group/smaller-window calculations are explicit in the argument. |
| dependency | [C83 all-depth counterfamily](Yin_C_G0083_v1.md#statement) | F's every-model score collapse follows only from its actual fixed-prime all-window full-depth bound, with Theta(d) measure and other-prime limits unchanged. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY accepted compact real Lipschitz discrepancy statement through L168 at its actual powered degree and source-proof limits. |
| dependency | [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY retained house subsection Dim19 v1 statement for the old radical-control irreducibility, not the new score criterion. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0317_v1.md#circular-link-whole-independent-finding) | ENTIRE actual final01:36:12 D44 and direct/source/control interfaces. Its reviewer now authors this wrapper, so no prospective actual extraction review or adoption is supplied. |
| support | [C86 retained original ancestry](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Credited SAME-PROOF D42 gap/residual antecedent, now adopted after R425; the new score argument fully supplies every needed finite step locally. |
| support | [J11 retained verification](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing exact base Lehmer prime3 factor/order evidence at its original independently verified scope; programs/full outputs remain solely in J and are not rerun. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:51 |
| status | proved |
| reason | Adopt original whole R317 and separate actual extraction R319. The actual circular compatible-link score gives one-time full original norm income and the inherited finite measure consequence; exact robustness, smaller-window strict control and every-model obstruction are fixed. All failed-average history and original costs remain. Global weighted triple-density coverage and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE A--F, actual original good-prime counts/model, all edge/zero/small-size cases, one-time bounds, finite constants, exact controls and open boundaries. |
| argument | [Entire retained original body](#argument) | COMPLETE original candidate/reuse/failed-average history and Sections1--7/equations1--22, all nine anchors, sources/roles/costs/controls and actual01:35:12 plus01:36:12 freezes. |
| dependency | [L159 actual root capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual distinct good-prime roots and positive integer complete-group counts w_o<=phi(o), not bad-prime multiplicities or arbitrary real weights. |
| dependency | [L74 original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Whole original K/Q signed norm, every residue-degree contribution, no scalar-content or powered-degree substitution. |
| dependency | [L74 good-prime floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Original first-return lower bounds including p2, with ALL actual depths retained in the full income rather than set equal to the floor. |
| dependency | [L168 finite cost criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | SAME n<=Cd and A_p(n)>=eta*d, exact finite m0 parameters and original-powered-degree accounting. No arithmetic coverage comes from that cost theorem itself. |
| dependency | [L168 finite height floor](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Unchanged finite epsilon_(B_ana)>0 used in m0; no executed enumeration or numerical constant. |
| dependency | [L159 radical control](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure with its retained accepted house scope, only for the comparison family. |
| dependency | [L159 good-prime control](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | Retained base prime3 masses/orders and squarefreeness; new four-group/smaller-window calculations are explicit in the argument. |
| dependency | [C83 all-depth counterfamily](Yin_C_G0083_v1.md#statement) | F's every-model score collapse follows only from its actual fixed-prime all-window full-depth bound, with Theta(d) measure and other-prime limits unchanged. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY accepted compact real Lipschitz discrepancy statement through L168 at its actual powered degree and source-proof limits. |
| dependency | [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY retained house subsection Dim19 v1 statement for the old radical-control irreducibility, not the new score criterion. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0317_v1.md#circular-link-whole-independent-finding) | ENTIRE actual final01:36:12 D44 and direct/source/control interfaces. Its reviewer now authors this wrapper, so no prospective actual extraction review or adoption is supplied. |
| support | [C86 retained original ancestry](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Credited SAME-PROOF D42 gap/residual antecedent, now adopted after R425; the new score argument fully supplies every needed finite step locally. |
| support | [J11 retained verification](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing exact base Lehmer prime3 factor/order evidence at its original independently verified scope; programs/full outputs remain solely in J and are not rerun. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0319_v1.md#c88-circular-link-actual-extraction-finding) | Entire actual C88 A--F and retained original, every direct/source/control/cost interface; separate root noncontributor. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ENTIRE A--F, actual original good-prime counts/model, all edge/zero/small-size cases, one-time bounds, finite constants, exact controls and open boundaries. |
| argument | [Argument](#argument) | COMPLETE original candidate/reuse/failed-average history and Sections1--7/equations1--22, all nine anchors, sources/roles/costs/controls and actual01:35:12 plus01:36:12 freezes. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual distinct good-prime roots and positive integer complete-group counts w_o<=phi(o), not bad-prime multiplicities or arbitrary real weights. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Whole original K/Q signed norm, every residue-degree contribution, no scalar-content or powered-degree substitution. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Original first-return lower bounds including p2, with ALL actual depths retained in the full income rather than set equal to the floor. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | SAME n<=Cd and A_p(n)>=eta*d, exact finite m0 parameters and original-powered-degree accounting. No arithmetic coverage comes from that cost theorem itself. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Unchanged finite epsilon_(B_ana)>0 used in m0; no executed enumeration or numerical constant. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure with its retained accepted house scope, only for the comparison family. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | Retained base prime3 masses/orders and squarefreeness; new four-group/smaller-window calculations are explicit in the argument. |
| dependency | [Dependency](Yin_C_G0083_v1.md#statement) | F's every-model score collapse follows only from its actual fixed-prime all-window full-depth bound, with Theta(d) measure and other-prime limits unchanged. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY accepted compact real Lipschitz discrepancy statement through L168 at its actual powered degree and source-proof limits. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY retained house subsection Dim19 v1 statement for the old radical-control irreducibility, not the new score criterion. |
| support | [Support](../audits/reviews/Yin_R_G0317_v1.md#circular-link-whole-independent-finding) | ENTIRE actual final01:36:12 D44 and direct/source/control interfaces. Its reviewer now authors this wrapper, so no prospective actual extraction review or adoption is supplied. |
| support | [Support](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Credited SAME-PROOF D42 gap/residual antecedent, now adopted after R425; the new score argument fully supplies every needed finite step locally. |
| support | [Support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing exact base Lehmer prime3 factor/order evidence at its original independently verified scope; programs/full outputs remain solely in J and are not rerun. |
| review | [Review](../audits/reviews/Yin_R_G0319_v1.md#c88-circular-link-actual-extraction-finding) | Entire actual C88 A--F and retained original, every direct/source/control/cost interface; separate root noncontributor. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | ENTIRE A--F, actual original good-prime counts/model, all edge/zero/small-size cases, one-time bounds, finite constants, exact controls and open boundaries. |
| argument | [Exact retained argument](#argument) | COMPLETE original candidate/reuse/failed-average history and Sections1--7/equations1--22, all nine anchors, sources/roles/costs/controls and actual01:35:12 plus01:36:12 freezes. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual distinct good-prime roots and positive integer complete-group counts w_o<=phi(o), not bad-prime multiplicities or arbitrary real weights. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Whole original K/Q signed norm, every residue-degree contribution, no scalar-content or powered-degree substitution. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Original first-return lower bounds including p2, with ALL actual depths retained in the full income rather than set equal to the floor. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | SAME n<=Cd and A_p(n)>=eta*d, exact finite m0 parameters and original-powered-degree accounting. No arithmetic coverage comes from that cost theorem itself. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Unchanged finite epsilon_(B_ana)>0 used in m0; no executed enumeration or numerical constant. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure with its retained accepted house scope, only for the comparison family. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#actual-isolated-linear-return-certificate) | Retained base prime3 masses/orders and squarefreeness; new four-group/smaller-window calculations are explicit in the argument. |
| dependency | [Exact retained dependency](Yin_C_G0083_v1.md#statement) | F's every-model score collapse follows only from its actual fixed-prime all-window full-depth bound, with Theta(d) measure and other-prime limits unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY accepted compact real Lipschitz discrepancy statement through L168 at its actual powered degree and source-proof limits. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY retained house subsection Dim19 v1 statement for the old radical-control irreducibility, not the new score criterion. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0317_v1.md#circular-link-whole-independent-finding) | ENTIRE actual final01:36:12 D44 and direct/source/control interfaces. Its reviewer now authors this wrapper, so no prospective actual extraction review or adoption is supplied. |
| support | [Exact retained support](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Credited SAME-PROOF D42 gap/residual antecedent, now adopted after R425; the new score argument fully supplies every needed finite step locally. |
| support | [Exact retained support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing exact base Lehmer prime3 factor/order evidence at its original independently verified scope; programs/full outputs remain solely in J and are not rerun. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0319_v1.md#c88-circular-link-actual-extraction-finding) | Entire actual C88 A--F and retained original, every direct/source/control/cost interface; separate root noncontributor. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | ENTIRE A--F, actual original good-prime counts/model, all edge/zero/small-size cases, one-time bounds, finite constants, exact controls and open boundaries. |
| argument | [Exact retained argument](#argument) | COMPLETE original candidate/reuse/failed-average history and Sections1--7/equations1--22, all nine anchors, sources/roles/costs/controls and actual01:35:12 plus01:36:12 freezes. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual distinct good-prime roots and positive integer complete-group counts w_o<=phi(o), not bad-prime multiplicities or arbitrary real weights. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Whole original K/Q signed norm, every residue-degree contribution, no scalar-content or powered-degree substitution. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Original first-return lower bounds including p2, with ALL actual depths retained in the full income rather than set equal to the floor. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | SAME n<=Cd and A_p(n)>=eta*d, exact finite m0 parameters and original-powered-degree accounting. No arithmetic coverage comes from that cost theorem itself. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Unchanged finite epsilon_(B_ana)>0 used in m0; no executed enumeration or numerical constant. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure with its retained accepted house scope, only for the comparison family. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#actual-isolated-linear-return-certificate) | Retained base prime3 masses/orders and squarefreeness; new four-group/smaller-window calculations are explicit in the argument. |
| dependency | [Exact retained dependency](Yin_C_G0083_v1.md#statement) | F's every-model score collapse follows only from its actual fixed-prime all-window full-depth bound, with Theta(d) measure and other-prime limits unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY accepted compact real Lipschitz discrepancy statement through L168 at its actual powered degree and source-proof limits. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY retained house subsection Dim19 v1 statement for the old radical-control irreducibility, not the new score criterion. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0317_v1.md#circular-link-whole-independent-finding) | ENTIRE actual final01:36:12 D44 and direct/source/control interfaces. Its reviewer now authors this wrapper, so no prospective actual extraction review or adoption is supplied. |
| support | [Exact retained support](Yin_C_G0086_v1.md#triple-anchored-residual-cover) | Credited SAME-PROOF D42 gap/residual antecedent, now adopted after R425; the new score argument fully supplies every needed finite step locally. |
| support | [Exact retained support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing exact base Lehmer prime3 factor/order evidence at its original independently verified scope; programs/full outputs remain solely in J and are not rerun. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0319_v1.md#c88-circular-link-actual-extraction-finding) | Entire actual C88 A--F and retained original, every direct/source/control/cost interface; separate root noncontributor. |

## Registration and complete preservation

The [original D44 entire freeze](#circular-link-entire-author-freeze) is extraction ancestry.
The actual full original has25676 characters,232 lines and9 explicit anchors.
Its ENTIRE body follows, with only duplicate author/framework front matter removed, the first title demoted by one hash and terminal/separating blank-line normalization.
All22 equations, initial candidate, failed global-average shortcut, positive/zero edge arguments, controls, source/contribution boundaries and both freeze records remain.
All original relative links remain valid here; no rebasing or mathematical normalization is performed.

Rounding-recovery remains sole new-proof author.
Review-recovery's R317 covers the actual complete original as an independent whole review, with its C86 wrapper ancestry role disclosed.
This new statement/extraction makes review-recovery a contributor to THIS artifact and requires a different actual reviewer.
The root supplied no new proof or wrapper and may arrange that inspection.
The original D44 remains unchanged and unretired.

At this registration C86 actually selects its2026-10-13T01:39 organized-reviewed decision after separate R425 actual review.
The historical C86-under-review observations in D44 and R317 remain true at their original reading times and are NOT silently rewritten.
D44's complete finite score proof already avoids any reliance on prospective acceptance; the current C86 adoption introduces no new premise or changed result here.


No native mathematical run, source acquisition, adoption, draft retirement or unrestricted Task conclusion accompanies this registration.
Complete body retention and structural checks do not independently certify the new wrapper.

## Argument

## Circular link density and robust one-time arithmetic capture

Date: 2026-10-12T17:30.
Human author Yin.
New AUTHOR inquiry by rounding-recovery.
Root supplied only the broad question whether a weaker, checkable coverage condition can replace ALL-three-group synchronization.
No intended verdict, formula or proof was supplied.
This author owns the earlier D42 proof; R314 is its separate original whole review, while its current C extraction requires its own actual review.
No mathematical native computation is authorized or proposed here.

<a id="circular-link-candidate-and-reuse"></a>
## Responsible candidate and bounded reuse

The entire D42 and R314 were read at their actual original scope, together with accepted C83's all-pair counterfamily.
The bounded current C/L/D screen for weighted triple density, codegree, link mass and mass trimming found no exact retained version of the candidate below.
L159 gives actual good-prime root capacity, L74 gives full original local norm and first-return floors, L168 gives the exact same-time arithmetic-income cost implication.
The earlier L225 anchored sparse-polynomial cover has a different required witness and is not assumed.
This is bounded reuse, not a novelty certificate.

A plain positive average density of compatible weighted triples has not been shown sufficient.
The tempting step of selecting an arbitrary maximizing pair from that average is unjustified: the average need not supply its compatible third mass.
This unresolved route is retained and will not be reported as proved.

The proposed changed discriminator is the SUM of compatible-third mass along the consecutive edges of a finite rational-angle model of the ACTUAL distinct root counts.
For an edge whose endpoint orders have lcm L and positive link mass U, the earlier residual partition gives a real return time with mass at least U L/X.
Its positive angular gap g is at least1/L.
If H is the maximum actual captured mass by X, then U<=H X g.
Summing over the full circle may therefore produce H>=sum_edges U/X without requiring every triple, every pair, or every edge to be compatible.

The model must use EXACTLY the actual integer capacities of an existing good-prime polynomial, with all selected groups and full original norms retained.
It is a counting certificate, not a synthetic weighted incidence array asserted realizable over the integers.
The target is a positive-density score implying one actual n<=C*d and positive-linear local income, with no inference that near-one inputs satisfy that score.
A genuine existing radical family will test strict weakening at a fixed physical exponent window.
Full proof, failures and limits will be appended here before any complete author freeze.


<a id="circular-link-actual-data-and-score"></a>
## 1. Actual root data and the finite circular score

Let P in Z[t] be ACTUAL monic irreducible, of ORIGINAL degree d>=1, constant coefficient+/-1, and with nontorsion root alpha.
Write K=Q(alpha), m=log M(P)>0 and, for every n>=1,

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0).                                (1)

Fix a GOOD prime p, meaning p does not divide disc(P).
Its reduction has d DISTINCT nonzero roots.
Their actual multiplicative orders o are prime to p.
Let w_o be the actual number of original roots of order o, with each irreducible factor contributing its degree ONCE.
The accepted [L159 interface](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) gives

    w_o in Z_(>0), w_o<=phi(o), sum_o w_o=d.              (2)

Choose any nonempty subset S of its occurring order groups, keeping the complete actual mass of each chosen group, and put W=sum_(o in S)w_o.
Thus1<=W<=d.
Reciprocity is permitted and retains L159's actual Frobenius/inversion restrictions, but is not needed by the proof.
No bad-prime repeated-root mass or arbitrary real weight is substituted.

A rational-angle counting model chooses, for each o in S, EXACTLY w_o distinct primitive o-th roots of unity, written as rational angles in[0,1).
For o1 the unique angle is0.
Distinct orders yield disjoint points.
The capacity(2) guarantees existence.
Sort the resulting W DISTINCT angles as theta_1<...<theta_W, give each point its exact order label a_i, and put theta_(W+1)=theta_1+1, a_(W+1)=a_1.
Define positive circular gaps

    g_i=theta_(i+1)-theta_i>0, sum_(i=1)^W g_i=1.         (3)

The W1 case has its single gap1 and the same order at both ends.
Points of the same order at different angles are allowed.
The model is an explicit finite COUNTING certificate using the already actual integer counts.
It is not a proposed new polynomial realization, and its complex roots need not be the characteristic-zero conjugates of P.
Since returns depend only on o, every model made with the same actual group counts gives valid bounds for that same P.

For an integer X>=1 and any two order labels a,b in S, INCLUDING a=b, define the compatible-third mass and circular score

    U_X(a,b)=sum_(o in S, lcm(a,b,o)<=X)w_o,
    Score_X=sum_(i=1)^W U_X(a_i,a_(i+1)).               (4)

U_X counts actual ROOT mass, not the number of third groups.
An anchor order can itself appear as the third order; there is no vacuous three-DISTINCT convention in this new definition.
The score is an integer between0 and W^2.
Many anchor pairs and many circular edges may have U_X=0.

The finite data are checkable with rational comparisons and integer gcd/lcm: actual order/mass certificates, W primitive fractions with the exact assigned counts, their circular order, and W lists of compatible groups.
The score needs only those W adjacent anchors, not an assumption on all pairs or all triples.
This is not a claim that finding the original polynomial factor/order inventory or an optimal model is inexpensive.
No factorization, enumeration, floating angle calculation or new native program has been run.

Define the actual selected-root peak

    H_X(S)=max_(integer1<=n<=X) sum_(o in S, o divides n)w_o.
                                                               (5)

The maximum is finite and can be zero; its definition does not claim it has been enumerated.

<a id="circular-link-capture-theorem"></a>
## 2. Circular link density gives one actual capture time

**Theorem1.**
For EVERY actual input, group selection, rational-angle model and integer X>=1 in Section1,

    H_X(S)>=Score_X/X,
    Score_X<=X H_X(S)<=X min(W,X).                     (6)

If Score_X>0, there is a SINGLE integer n<=X with p not dividing n such that the actual returned selected mass is at leastScore_X/X.
A sharper finite construction is: choose a circular edge i maximizing U_i/g_i, where U_i=U_X(a_i,a_(i+1)); let

    L_i=lcm(a_i,a_(i+1))<=X,
    B_i=floor(X/L_i)>=1.

One of its actual residual buckets yields n=L_i r<=X and returned mass at least

    ceil(U_i/B_i)>=U_i L_i/X
                    >=U_i/(X g_i)>=Score_X/X.          (7)

Every quantity belongs to this same actual input and original group inventory.
No sum of arithmetic incomes at different times is used.

**Proof.**
Fix an edge with U_i>0 and write a,b,L,U,g for its data.
Because some third group o has lcm(a,b,o)<=X, necessarily L<=X and B=floor(X/L)>=1.
For every compatible third order put r(o)=o/gcd(o,L).
Then

    lcm(L,o)=L r(o)<=X, so1<=r(o)<=B.                  (8)

Partition ONLY these compatible groups by r(o), retaining their full positive integer masses.
Their B bucket masses sum to U.
One occupied bucket has mass at leastceil(U/B).
At n=Lr all its orders divide n.
Since every actual order, L and r is prime to p, n is also prime to p.
Additional selected or unselected groups can return at this n, which only helps.
This is the old [D42 residual-bucket mechanism](Yin_C_G0086_v1.md#triple-anchored-residual-cover) applied to the compatible link instead of assuming that link is the whole S.
Its complete finite argument has just been provided, so no pending Claim-wrapper acceptance is a hidden premise.

The edge's positive circular gap is a positive integer multiple of1/lcm(a,b), including the final wraparound and the W1 case.
Hence g>=1/L.
Together with B<=X/L this gives

    H_X(S)>=ceil(U/B)>=U L/X>=U/(Xg),
    U<=X H_X(S) g.                                    (9)

For U=0 the last inequality remains true without requiring L<=X or defining a nonzero bucket.
Sum it over ALL W circular edges and use sum g_i=1 to obtain Score_X<=X H_X(S).
Equivalently, because Score_X=sum g_i(U_i/g_i), a maximizing edge has U_i/g_i>=Score_X; when the score is positive, that edge is eligible for the explicit construction.
This proves the first inequality and(7).

Finally, for any actual n the returning selected groups have total mass at mostsum_(o|n)phi(o)=n.
The identity counts the n roots of t^n-1 by their exact complex orders (or partitions integers1,...,n by their gcd with n).
The total is also at most W.
Thus H_X(S)<=min(W,X), proving the rest of(6).
This capacity upper bound concerns ROOT mass only; it does not put an upper bound on actual valuation depth or on A_p.

This argument reuses the arithmetic denominator of each circular gap, but does NOT require selecting a largest pair lcm or proving that all third groups join that pair.
Its sum of link masses is the new quantitative discriminator.
The weighted sum is paid by the actual total circumference1.

<a id="circular-link-density-and-trimming"></a>
## 3. Checkable weak coverage and robustness

Fix0<delta<=1.
The condition

    Score_X>=delta W^2                                (10)

is a circular compatible-link density condition.
It does not require ALL triples, all pairs, or even every adjacent edge to be compatible.
By Theorem1 it guarantees one actual n<=X capturing at leastdelta W^2/X roots.
The score's capacity bound also implies X>=sqrt(delta)W for any actual instance.

Several explicit certificates suffice for(10).

First, if at least k of the W adjacent edges have U_i>=theta W, where0<theta<=1, then Score_X>=k theta W.
In particular k>=(1-epsilon)W with0<=epsilon<1 gives delta=(1-epsilon)theta.
Bad edges can have ZERO link, and there is no condition on nonadjacent anchors.
The integer k need not equal the real lower threshold.

Second, if EVERY pair of order labels in S has U_X(a,b)>=theta W, including diagonal pairs, then every angle model has Score_X>=theta W^2.
This gives a positive compatible-third mass version of the earlier ALL-three rule.
The earlier all-three hypothesis with at least3 groups implies theta1 also for repeated pairs, by adjoining an extra distinct order when necessary.
For one or two groups, its at-most-three guard is still necessary; this new pair-link definition handles those cases directly without vacuity.

Third, the following precise trimming certificate is useful and supplies a strict actual control below.
Suppose T is a subset of the selected groups S with total actual mass V, and EVERY subset of T of size AT MOST3 has common exponent<=X.
(The nonvacuous all-three condition with |T|>=3 is equivalent here.)
Keep all W model points and edges, including those outside T.
An edge with both endpoints in T has U_i>=V.
There are at least

    max(2V-W,0)

such edges: the W-V outside vertices are each incident to two directed circular edges, so at most2(W-V) edges touch the outside.
This includes W1 and W2 and does not assume that T occupies a contiguous arc.
Consequently EVERY angle model satisfies

    Score_X>=V max(2V-W,0).                            (11)

If V=(1-epsilon)W with0<=epsilon<1/2, this gives delta=(1-epsilon)(1-2epsilon)>0.
It shows robustness to deleting up to a fixed fraction below one half of root mass.
It does not say the half threshold is optimal or exclude other certificates when V<=W/2.
The earlier theorem could instead be applied directly to T; the NEW score criterion additionally permits link mass to come from DIFFERENT third-group sets at different adjacent edges, with no single common trimming set supplied.

These hypotheses are exact finite statements on the original root inventory.
The theorem is sufficient rather than an optimizer characterization: a small score in one model does not rule out a better model or a large actual return mass.
Conversely, the bound holds for EVERY model, so a proven small actual peak bounds all of their scores at once.

<a id="circular-link-full-income-and-measure"></a>
## 4. Complete norm income and the unchanged analytic cost interface

At a good prime the roots lie in an unramified splitting field with v_p(p)=1.
A root of residue order o has v_p(alpha_i^n-1)>=1 if o divides n and valuation0 otherwise.
These are [C256's automatic good-prime floors](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail), not claimed exact depths.
The full original signed norm and local income are

    D_n=product_(all d original roots)(alpha_i^n-1),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(all d original p-adic roots)v_p(alpha_i^n-1).
                                                               (12)

All factors are nonzero by nontorsion and every local valuation is nonnegative.
Thus at the actual n from Theorem1,

    A_p(n)>=(Score_X/X)log p.                          (13)

The left side retains ALL original roots, arbitrarily deep initial valuations, binary exceptional behavior and any extra returned orders.
No equality with a depth-one floor or upper bound for the remaining local/all-prime income is asserted.
The constructed time is prime to p, but that does not force initial depths to equal1.

**Corollary2.**
Fix0<gamma,delta<=1 and C>0.
Suppose an actual input has a good prime p, selected complete groups with W>=gamma*d, an integer1<=X<=C*d, and an actual rational-angle model satisfying(10).
Then at ONE actual n<=C*d,

    A_p(n)>=eta*d,
    eta=(delta gamma^2/C)log2>0.                       (14)

The prime may vary because log p>=log2.
The necessary root-capacity budget for such an instance is C>=gamma sqrt(delta); no stronger C>=gamma condition from the earlier ALL-three theorem is imported.

Apply the SAME accepted [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) to(14), using A_p(n)<=log C_n at this same n.
Choose T_ana>=1,R_ana>=2 so exp(-T_ana)/2+1/R_ana<=eta/4, put

    K_ana=(3exp(T_ana)+T_ana/R_ana)(4R_ana+1),
    tau=min(1,eta/4,eta^2/(16K_ana^2)),
    choose integer B_ana>=55 with log B_ana/B_ana<=tau,
    m0=min(tau/C,epsilon_(B_ana)/(2C))>0.              (15)

L168's finite epsilon_(B_ana)>0 is its unchanged lower bound for heights of nontorsion units of bounded degree.
It is not a newly computed constant.
Its complete norm tower and h=nm/d include powered-field degree drop.
For m<=m0, that theorem gives log C_n/d<=3eta/4<eta, contradicting(14).
Therefore EVERY input satisfying this new score condition obeys m(P)>m0(C,eta).

The sole analytic theorem remains L168's accepted Pri11 compact discrepancy statement and its recorded source/applicability limits.
No new external proof inspection, Dim19 sharpening or source acquisition is needed for this consequence.
The sufficient arithmetic condition is new; the cost theorem and its finite escape construction receive their old credit.

On a HYPOTHETICAL near-one sequence, for every fixed gamma,delta,C the score criterion must eventually fail at EVERY good prime and EVERY selected W>=gamma*d and EVERY counting model.
This is a necessary structural consequence of the accepted cost bound, not an assertion that the criterion covers near-one inputs.
The complete auxiliary remains the ONE integer polynomial t^n-1 at its ACTUAL degree n<=Cd, content1 and coefficient squared norm2, with its full original resultant(1).
No packet q/M, unpriced cofactor or smaller powered-field norm is substituted.

<a id="circular-link-actual-strict-control"></a>
## 5. Actual strict weakening: the four-group radical control

Use the same retained actual family as D42, with a rational prime q>41:

    F_q(t)=P_Lehmer(t^q), d=10q,
    P_Lehmer=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.         (16)

The accepted [L159 radical argument](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) proves it is irreducible reciprocal nontorsion with full M(F_q)=M(P_Lehmer)>1; [its good-prime control](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) and retained [J11 evidence](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) give the base prime3 groups of orders4,82 and masses2,8.
Their prior verification is reused, not rerun.
The original accepted house-statement boundary is needed only for this old family's irreducibility argument, not for Theorem1 or its finite m0.

Since q>41 is prime, gcd(q,164)=1.
Above each root of order o in{4,82}, exactly one q-th root has order o, while q-1 have order oq: exponentiation by q is invertible on the order-o subgroup, and nonidentity q-th roots of unity have order q.
Thus the FOUR actual groups are

    (4,2), (4q,2(q-1)), (82,8), (82q,8(q-1)).          (17)

They total ALL d=10q roots.
The reduction remains squarefree because its derivative is q*t^(q-1)*P_Lehmer'(t^q), nonzero at every reduced root modulo3.
No omitted extra factor or root multiplicity is present.

Take the FULL group set S, so W=d, and the SMALLER actual time window

    X=82q=(41/5)d,
    T={82,82q}, V=8q, W-V=2q.                         (18)

Every selected order in T divides X.
Therefore every model edge whose endpoints lie in T has compatible-third mass at least8q.
Among all10q circular edges, at most4q touch the2q outside vertices.
Hence at least6q edges have both endpoints in T, without any assumption about their angular arrangement.
For EVERY model,

    Score_X>=48q^2=(12/25)d^2,
    H_X(S)>=48q^2/(82q)=(12/205)d,
    some n<=X has A_3(n)>=(12/205)d log3.              (19)

These are not synthetic incidence weights: all counts and orders belong to the explicit irreducible polynomial(16).
The direct return n=82q is stronger still: precisely the82/82q groups return, because82q has2-adic order1 whereas both4 and4q are divisible by4.
Its selected root mass is exactly8q and its actual local income is AT LEAST8q log3.
No exact valuation-depth claim is made.

At this SAME window, the pair4q,82q has lcm164q>X, so its link mass is0.
In particular the DISTINCT triple4q,82q,82 is incompatible.
Thus ALL-three synchronization and even ALL-pair synchronization fail on the FULL group set S at this fixed linear window, whereas the circular score has the uniform positive fraction12/25.
The new condition is strictly weaker in a fully realizable actual family, not merely a rescaled version of the ALL-three hypothesis.
An explicit heavy subset also certifies this particular control; the theorem itself requires no common heavy subset whose every triple is compatible.

The full measure is the fixed positive old Lehmer value, not a quantity tending to zero.
This family has q expanding roots and an actual q-th-power degree drop.
Its complete resultant always remains Norm_(Q(root F_q)/Q)(alpha^n-1) of degree10q.
No original norm sign, conjugate multiplicity or fixed positive measure is removed.
This is a positive control of weaker coverage, not a near-one family, an all-powers-degree-preserving control or a counterexample to the Mahler-gap question.

<a id="circular-link-obstructions-and-unresolved-average"></a>
## 6. A stronger all-model obstruction and the unresolved global-average question

For any fixed actual S,X, Theorem1 gives the converse necessary bound

    Score_X<=X H_X(S)                                 (20)

for EVERY rational-angle model.
By L74, every captured selected root contributes at least log p to the full local income, so H_X(S)log p<=max_(n<=X)A_p(n).
Thus small full local income forces small circular score for all models simultaneously; choosing a more favorable rational-angle model cannot evade it.

For the adopted [C83 actual counterfamily](Yin_C_G0083_v1.md#statement), take its FULL fixed-prime2 root set and any fixed C>0, X=floor(Cd).
Its COMPLETE all-depth income has max_(n<=Cd)A_2(n)/d->0.
Hence

    sup_(all actual-count angle models) Score_X/d^2
       <=[X/d]*(max_(n<=X)A_2(n)/(d log2))
       ->0.                                          (21)

This includes its high initial/time depths exactly through the accepted bound and keeps every original root.
For selected subfamilies W>=gamma*d, the same upper bound relative to W^2 also tends to0, with factor1/gamma^2.
This rules out the NEW positive circular-link coverage condition throughout that large-measure counterfamily, not only ALL-three synchronization.
Its old all-pair short periods, full m(P)=Theta(d), good prime and all-prime-income limitations are unchanged.

A different, weaker-looking data summary would be the global ordered weighted triple density

    Dens_X=(1/W^3)sum_(a,b in S)w_a w_b U_X(a,b).       (22)

This draft DOES NOT prove that Dens_X bounded below by a positive constant forces Score_X>=delta W^2 for some model, or itself forces one-time linear income.
The circular edge frequencies are not generally w_a w_b/W^2; they are constrained by distinct primitive rational points and exact gap arithmetic.
The abandoned shortcut of assigning the global average to a maximizing-lcm pair has no justification.
No actual polynomial counterfamily to this global-density implication has been found here either.
It remains a precise open step after the present positive theorem.

Likewise, a generic dense abstract hypergraph or arbitrary weighted incidence matrix is not an actual counterexample under(2).
The theorem uses a restricted but checkable form of triple density with explicit actual root capacities and a complete one-time norm transfer.
There is no claim of a minimum sufficient density statistic, optimal constants or unrestricted near-one coverage.

<a id="circular-link-sources-and-author-check"></a>
## 7. Provenance, exact limits and author verification

The prior [D42 original proof](Yin_C_G0086_v1.md#triple-synchronization-entire-author-freeze), independently whole-reviewed by [R314](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding), supplied the circular denominator and residual-bucket antecedents.
The author of the present draft also authored D42 and therefore does not independently review either here.
At the initial reuse read its fixed C86 wrapper was under review; none of its prospective adoption is a premise.
The complete finite arguments needed for the new score theorem are supplied in Sections1--2, and the new score sum, robust edge/mass conditions, smaller-window actual control and all-model obstruction are the current author contribution.

L159/L74 provide actual distinct-root capacities and full original norm/floor conventions.
L168 supplies the unchanged full product cost and finite positive measure consequence.
The Lehmer/J11/house interfaces are old input only for the explicit comparison family.
C83 supplies its accepted large-measure all-depth obstruction.
L225's sparse auxiliary and L213's low-degree escape remain different mechanisms and supply no hidden coverage hypothesis.
No new external theorem, global source record or claim of historical priority is made.

The author hand-checked all W1/W2 and repeated-order edge cases, exact circular wraparound, positive-versus-zero link branches, lcm and floor directions, compatible-only integer bucket masses, p-prime times, every actual original norm/depth contribution, score range and root-capacity ceiling, the distinction between link density and global triple average, edge-count trimming without interval assumptions, every positive-density/m0 constant, all four radical masses and the exact smaller window, failure of full-set pair/triple compatibility, and the uniformity over all models in(21).
The full actual source/interface passages and the complete original D42/R314 were read.
No native mathematical program, factorization, all-n scan, external source acquisition or target adoption was performed.

Source and former author claims remain at their actual scopes; this new whole proof requires a separate noncontributing review.

<a id="circular-link-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T17:35.
Freeze the ENTIRE actual candidate/reuse and failed-average-step account, Sections1--7/equations(1)--(22), complete original-domain and model definitions, constructive one-time proof, all costs and boundaries, actual strict positive control, all-model negative consequence, source/contribution account and explicitly unresolved global-average implication.
No mathematical native work was run.
Root supplied the broad question only and may arrange a separate whole independent review.


2026-10-12T17:36.
Final author delivery freeze after coordinated SAME-PROOF locator maintenance: the two original D42 links now point to its complete retained anchors in C86, whose actual complete preservation was checked.
No mathematical statement, proof, source scope or earlier history changed.
The initial C86-under-review description above records the actual initial reading, not its later adoption state.
This final freeze includes the ENTIRE body at the preceding freeze and this locator account; no prospective independent verdict is asserted.
