---
author: Yin
---
# Three-group order synchronization and one-time original norm income

Date: 2026-10-12T17:25.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
Rounding-recovery authored the ENTIRE new D42 proof.
g0001_review_recovery previously supplied only a read-only existing-material locator search, then independently WHOLE-reviewed the actual01:13:07 original in R314.
This agent NOW authors the present statement/extraction wrapper and is a contributor to this artifact; it cannot independently review its actual extraction.
R314 remains support for the original whole proof only.
Initial status is proof draft / under review, awaiting a different noncontributor's actual review.

## Statement

Let P in Z[t] be an ACTUAL monic irreducible polynomial of ORIGINAL degree d>=1, constant coefficient+/-1, and nontorsion root alpha.
Reciprocity is allowed but not required.
Set K=Q(alpha), m=log M(P)>0, using ordinary total logarithmic Mahler measure.
For every integer n>=1 retain the COMPLETE original signed norm and its absolute value

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=abs(D_n) in Z_(>0).

Fix a rational GOOD prime p, meaning p does not divide disc(P).
The reduction has d distinct nonzero roots.
Let O_p be their finite set of occurring multiplicative orders, and let w_o be the number of original reduced roots of exact order o.
Each residue factor contributes its degree ONCE.
Thus

    p does not divide o, w_o in Z_(>0),
    w_o<=phi(o), sum_(o in O_p)w_o=d.

These are actual good-prime root counts.
Arbitrary positive real weights or bad-prime repeated-root multiplicities are not substituted.
Select ANY nonempty subset S of occurring groups, retaining EVERY original root within each selected group, and put

    W=sum_(o in S)w_o, 1<=W<=d,
    L=max_(a,b in S)lcm(a,b),

where a=b IS included in the maximum.

**A. Finite circular capacity.**
More generally, for ANY nonempty finite set S of positive integers and positive INTEGER weights w_o<=phi(o), the same definitions give W<=L.
The proof chooses W distinct primitive roots of unity, counts their circular gaps including wraparound, and uses the fact that a gap between orders a,b is a positive integer multiple of1/lcm(a,b).
The one-point case and same-order endpoints are included.
This is a counting lemma, not an integer-polynomial realization theorem.
For |S|>=2 the maximum L is attained by a pair of DISTINCT orders.

**B. Exact actual three-group capture.**
Suppose |S|>=3 and an integer X>=1 satisfies

    lcm(a,b,c)<=X for EVERY THREE DISTINCT a,b,c in S.

Equivalently every such triple has some common return exponent<=X; those initially supplied exponents need not agree.
Then W<=L<=X and B=floor(X/L)>=1.
There exists ONE integer n<=X with p not dividing n such that

    sum_(o in S, o divides n)w_o
      >=ceil(W/B)>=W/B>=W L/X>=W^2/X.

More precisely, choose a distinct pair a,b attaining L, put r(o)=o/gcd(o,L), and partition S by its values r(o) in{1,...,B}.
An occupied bucket of mass at leastceil(W/B) gives n=Lr.
All its groups return at that ONE actual time.
Additional groups returning there remain included.
No full common lcm of all groups, cross-time sum of income or supplied sparse-polynomial witness is assumed.

A uniform small-group variant REPLACES the triple premise by: EVERY NONEMPTY subset of S of size AT MOST3 has a common exponent<=X.
For |S|1 or2, the lcm of all selected orders is then L<=X and captures ALL W roots, so the same displayed lower bounds hold.
The literal three-distinct premise alone is vacuous in those cases and supplies no return bound.

**C. Full original local income with all actual depths.**
At the SAME n in B,

    A_p(n):=(log p)v_p(C_n)
       =(log p)sum_(all d original p-adic roots a)v_p(a^n-1)
       >=ceil(W/B)log p>=(W^2/X)log p.

The local root valuations use v_p(p)=1.
At a good prime each returned root has actual depth at least1; all nonreturned roots contribute0.
The left side keeps every actual original root and depth, including larger initial values and the binary exceptional possibilities.
No exact depth1 equality is asserted.
Other groups or rational primes may add income, and no upper bound on them is claimed.
The original norm is nonzero for all n by nontorsion and retains the original field K even if alpha^n has smaller degree.

**D. Positive-density finite criterion and explicit inherited measure constant.**
Fix real0<gamma<=1 and C>0.
If an ACTUAL input has a good prime p and S,X satisfying B or its at-most-three variant with W>=gamma*d and X<=C*d, then one SAME integer n<=C*d satisfies

    A_p(n)>=eta*d, eta=(gamma^2/C)log2>0.

The prime may vary with the input; eta is independent of it.
Necessarily C>=gamma because X>=W.
For S=O_p with at least3 groups and every triple common by C*d, take gamma1 and X=floor(C*d), giving eta=log2/C.
The sharper finite ceil(d/floor(X/L))*log p bound remains valid.

For an explicit positive consequence, use L168's already accepted finite constants.
Choose T_ana>=1 and R_ana>=2 with exp(-T_ana)/2+1/R_ana<=eta/4, and put

    K_ana=(3exp(T_ana)+T_ana/R_ana)(4R_ana+1),
    tau=min(1,eta/4,eta^2/(16K_ana^2)),
    choose integer B_ana>=55 with log(B_ana)/B_ana<=tau,
    m0=min(tau/C,epsilon_(B_ana)/(2C))>0.

Here epsilon_(B_ana) is L168's finite positive lower bound on absolute heights of all nontorsion units of degree at most B_ana, defined there through a finite coefficient list.
No enumeration has been executed and no numerical value is assigned.
The analytic B_ana is distinct from the bucket count B.
Since0<=A_p(n)<=log C_n at that SAME exponent, the actual L168 criterion gives the STRICT conclusion

    m(P)>m0(C,eta).

That criterion keeps the exact powered degree and original norm tower; no all-powers degree-preservation premise is imposed.
It needs the existing Pri11 discrepancy statement at its accepted scope, with no new Dim19 sharpening.

Consequently, on a HYPOTHETICAL sequence m(P)->0, for every fixed gamma,C sufficiently late inputs have no positive-density actual good-prime group selection with this finite compatibility.
For the full group set with at least3 groups, some triple must have lcm>Cd.
With one or two groups the conclusion instead concerns an at-most-three subset's common period.
No near-one sequence is asserted to exist, and small measure does not supply the triple-affordability hypothesis.

**E. Retained genuine positive control.**
Reuse L159's actual irreducible reciprocal unit

    F_q(t)=P_Lehmer(t^q), d=10q,
    P_Lehmer=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,

for rational prime q>41.
Its fixed full Mahler measure equals M(P_Lehmer), and3 is a good prime.
The accepted base Lehmer prime3 data are root orders4,82 with original masses2,8.
Because gcd(q,164)=1, every base root of order o has exactly one q-th root of order o and q-1 of order oq.
The FOUR actual groups are therefore

    (order,mass)=(4,2),(4q,2(q-1)),
                 (82,8),(82q,8(q-1)).

They total ALL10q roots.
Every triple shares the SINGLE period164q=(82/5)d.
At that time the actual full local income is A_3>=d log3, stronger than B's generic guarantee.
This is a retained actual polynomial control with an elementary full-order classification, not a new native factorization.
The old irreducibility uses L159's accepted house-statement scope; that input is for this control only.
The family has fixed positive total measure, q expanding roots and a q-th-power degree drop.
It is not a near-one or all-powers-degree-preserving family.

**F. Exact contrast with C83 and complete costs/limits.**
The adopted C83 family has every pair lcm<=8d but A_2(n)/d->0 uniformly on EVERY fixed n<=Cd window.
Hence for EVERY fixed C and all sufficiently large members of that family, some actual triple has lcm>Cd: otherwise B--C with W=d would contradict that uniform bound.
Its full m(P)=Theta(d), all original binary depths and absence of an all-prime norm upper bound remain unchanged.
L217's separate bounded order/residue-degree condition likewise supplies no triple hypothesis.

The actual auxiliary for B--D is the SINGLE integer polynomial t^n-1, retaining full degree n<=Cd, coefficient content1 and squared coefficient norm2.
Its resultant includes all d roots and full signed D_n before the absolute value.
No rational packet q/M, erased cofactor or smaller powered-field norm replaces these costs; the elementary coefficient norm does not substitute for L168's complete product estimate.

The good-prime capacity is essential: repeated roots at a bad prime cannot be counted as distinct circular points, so no such extension is claimed.
The result is a SUFFICIENT finite arithmetic condition, not coverage of all near-one inputs, a new primitive-divisor theorem, an all-prime norm upper bound, an unrestricted positive-income mechanism or a G0001 completion.
L159/L74/L168 retain credit for actual root capacity, local floors and full cost; the circular-gap/residual-bucket implication is the new local deduction.
The prior sparse-cover, low-degree escape and counterfamily results keep their different premises and source boundaries.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:25 |
| status | open |
| reason | Register the finite circular-capacity and actual three-group single-time capture theorem, full original-depth income, positive-density finite measure consequence, exact radical control and pairwise countercomparison, retaining the ENTIRE original D42. R314 independently whole-reviewed only that original; this new authored wrapper requires separate actual extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, all actual original input/capacity/nonvacuity hypotheses, one-time bounds, finite constants, complete controls, original costs and limits. |
| argument | [Entire retained original proof](#argument) | COMPLETE original01:13:07 allocation/reuse/candidate/history, Sections1--7/equations1--15, all eight anchors, source/contributor boundaries and entire-author freeze. |
| dependency | [L159 actual capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Distinct actual good-prime roots, sum d and integer w_o<=phi(o); no bad-prime multiplicity substitution. |
| dependency | [L74 complete norm convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original field, residue-degree/ramification weighting and signed nonzero norm; no scalar-content or powered-degree replacement. |
| dependency | [L74 automatic floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | All original good-prime returned-root valuation floors, including p2; actual full depths remain on the left side. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Same actual n<=Cd and A_p(n)>=eta*d, exact finite parameters and powered-degree escape; no new income supplied by L168 itself. |
| dependency | [L168 finite height floor](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | The finite positive epsilon_(B_ana) used in the displayed m0; no executed enumeration or fixed numerical value. |
| dependency | [C83 exact pairwise counterfamily](Yin_C_G0083_v1.md#statement) | Only F's logical comparison: all-pair short times versus uniform all-depth sublinear2-primary income and full Theta(d) measure; no all-prime or near-one claim. |
| dependency | [L159 radical input](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure, at its retained accepted house-source scope. |
| dependency | [L159 isolated return control](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | E's actual base prime3 orders/masses, good-prime preservation and n=164q full return; new four-group classification explicitly assumes q>41. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY the accepted integer/simple-zero compact Lipschitz discrepancy statement through L168, with actual powered degree and source-proof limits unchanged. |
| dependency | [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY house subsection's retained Dim19 v1 statement for E's old radical-control irreducibility, not for the new criterion. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding) | Independent complete original01:13:07 D42 inspection, including locator-only prior helper role; that reviewer now authors this wrapper, so no prospective actual extraction coverage. |
| support | [J11 retained control evidence](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing verified base Lehmer prime3 degrees2/8 and orders4/82; original programs/results remain in J and are not duplicated or rerun. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:39 |
| status | proved |
| reason | Adopt original whole R314 and separately authored actual extraction R316. Actual good-prime root capacity and the nonvacuous three-group condition yield one original exponent with the stated full local income and inherited finite measure consequence. All original roots, actual depths, degree drops, old controls and costs remain. Coverage of near-one inputs and unrestricted G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, all actual original input/capacity/nonvacuity hypotheses, one-time bounds, finite constants, complete controls, original costs and limits. |
| argument | [Entire retained original proof](#argument) | COMPLETE original01:13:07 allocation/reuse/candidate/history, Sections1--7/equations1--15, all eight anchors, source/contributor boundaries and entire-author freeze. |
| dependency | [L159 actual capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Distinct actual good-prime roots, sum d and integer w_o<=phi(o); no bad-prime multiplicity substitution. |
| dependency | [L74 complete norm convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original field, residue-degree/ramification weighting and signed nonzero norm; no scalar-content or powered-degree replacement. |
| dependency | [L74 automatic floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | All original good-prime returned-root valuation floors, including p2; actual full depths remain on the left side. |
| dependency | [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Same actual n<=Cd and A_p(n)>=eta*d, exact finite parameters and powered-degree escape; no new income supplied by L168 itself. |
| dependency | [L168 finite height floor](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | The finite positive epsilon_(B_ana) used in the displayed m0; no executed enumeration or fixed numerical value. |
| dependency | [C83 exact pairwise counterfamily](Yin_C_G0083_v1.md#statement) | Only F's logical comparison: all-pair short times versus uniform all-depth sublinear2-primary income and full Theta(d) measure; no all-prime or near-one claim. |
| dependency | [L159 radical input](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure, at its retained accepted house-source scope. |
| dependency | [L159 isolated return control](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | E's actual base prime3 orders/masses, good-prime preservation and n=164q full return; new four-group classification explicitly assumes q>41. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY the accepted integer/simple-zero compact Lipschitz discrepancy statement through L168, with actual powered degree and source-proof limits unchanged. |
| dependency | [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY house subsection's retained Dim19 v1 statement for E's old radical-control irreducibility, not for the new criterion. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding) | Independent complete original01:13:07 D42 inspection, including locator-only prior helper role; that reviewer now authors this wrapper, so no prospective actual extraction coverage. |
| support | [J11 retained control evidence](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing verified base Lehmer prime3 degrees2/8 and orders4/82; original programs/results remain in J and are not duplicated or rerun. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0316_v1.md#c86-triple-synchronization-actual-extraction-finding) | Entire actual A--F, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor with accepted C83 ancestor authorship disclosed. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--F, all actual original input/capacity/nonvacuity hypotheses, one-time bounds, finite constants, complete controls, original costs and limits. |
| argument | [Argument](#argument) | COMPLETE original01:13:07 allocation/reuse/candidate/history, Sections1--7/equations1--15, all eight anchors, source/contributor boundaries and entire-author freeze. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Distinct actual good-prime roots, sum d and integer w_o<=phi(o); no bad-prime multiplicity substitution. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original field, residue-degree/ramification weighting and signed nonzero norm; no scalar-content or powered-degree replacement. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original good-prime returned-root valuation floors, including p2; actual full depths remain on the left side. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Same actual n<=Cd and A_p(n)>=eta*d, exact finite parameters and powered-degree escape; no new income supplied by L168 itself. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | The finite positive epsilon_(B_ana) used in the displayed m0; no executed enumeration or fixed numerical value. |
| dependency | [Dependency](Yin_C_G0083_v1.md#statement) | Only F's logical comparison: all-pair short times versus uniform all-depth sublinear2-primary income and full Theta(d) measure; no all-prime or near-one claim. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure, at its retained accepted house-source scope. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) | E's actual base prime3 orders/masses, good-prime preservation and n=164q full return; new four-group classification explicitly assumes q>41. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY the accepted integer/simple-zero compact Lipschitz discrepancy statement through L168, with actual powered degree and source-proof limits unchanged. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY house subsection's retained Dim19 v1 statement for E's old radical-control irreducibility, not for the new criterion. |
| support | [Support](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding) | Independent complete original01:13:07 D42 inspection, including locator-only prior helper role; that reviewer now authors this wrapper, so no prospective actual extraction coverage. |
| support | [Support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing verified base Lehmer prime3 degrees2/8 and orders4/82; original programs/results remain in J and are not duplicated or rerun. |
| review | [Review](../audits/reviews/Yin_R_G0316_v1.md#c86-triple-synchronization-actual-extraction-finding) | Entire actual A--F, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor with accepted C83 ancestor authorship disclosed. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--F, all actual original input/capacity/nonvacuity hypotheses, one-time bounds, finite constants, complete controls, original costs and limits. |
| argument | [Exact retained argument](#argument) | COMPLETE original01:13:07 allocation/reuse/candidate/history, Sections1--7/equations1--15, all eight anchors, source/contributor boundaries and entire-author freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Distinct actual good-prime roots, sum d and integer w_o<=phi(o); no bad-prime multiplicity substitution. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original field, residue-degree/ramification weighting and signed nonzero norm; no scalar-content or powered-degree replacement. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original good-prime returned-root valuation floors, including p2; actual full depths remain on the left side. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Same actual n<=Cd and A_p(n)>=eta*d, exact finite parameters and powered-degree escape; no new income supplied by L168 itself. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | The finite positive epsilon_(B_ana) used in the displayed m0; no executed enumeration or fixed numerical value. |
| dependency | [Exact retained dependency](Yin_C_G0083_v1.md#statement) | Only F's logical comparison: all-pair short times versus uniform all-depth sublinear2-primary income and full Theta(d) measure; no all-prime or near-one claim. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure, at its retained accepted house-source scope. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#actual-isolated-linear-return-certificate) | E's actual base prime3 orders/masses, good-prime preservation and n=164q full return; new four-group classification explicitly assumes q>41. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY the accepted integer/simple-zero compact Lipschitz discrepancy statement through L168, with actual powered degree and source-proof limits unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY house subsection's retained Dim19 v1 statement for E's old radical-control irreducibility, not for the new criterion. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding) | Independent complete original01:13:07 D42 inspection, including locator-only prior helper role; that reviewer now authors this wrapper, so no prospective actual extraction coverage. |
| support | [Exact retained support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing verified base Lehmer prime3 degrees2/8 and orders4/82; original programs/results remain in J and are not duplicated or rerun. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0316_v1.md#c86-triple-synchronization-actual-extraction-finding) | Entire actual A--F, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor with accepted C83 ancestor authorship disclosed. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--F, all actual original input/capacity/nonvacuity hypotheses, one-time bounds, finite constants, complete controls, original costs and limits. |
| argument | [Exact retained argument](#argument) | COMPLETE original01:13:07 allocation/reuse/candidate/history, Sections1--7/equations1--15, all eight anchors, source/contributor boundaries and entire-author freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Distinct actual good-prime roots, sum d and integer w_o<=phi(o); no bad-prime multiplicity substitution. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original field, residue-degree/ramification weighting and signed nonzero norm; no scalar-content or powered-degree replacement. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original good-prime returned-root valuation floors, including p2; actual full depths remain on the left side. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Same actual n<=Cd and A_p(n)>=eta*d, exact finite parameters and powered-degree escape; no new income supplied by L168 itself. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | The finite positive epsilon_(B_ana) used in the displayed m0; no executed enumeration or fixed numerical value. |
| dependency | [Exact retained dependency](Yin_C_G0083_v1.md#statement) | Only F's logical comparison: all-pair short times versus uniform all-depth sublinear2-primary income and full Theta(d) measure; no all-prime or near-one claim. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) | E's actual irreducible degree10q F_q and fixed full measure, at its retained accepted house-source scope. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#actual-isolated-linear-return-certificate) | E's actual base prime3 orders/masses, good-prime preservation and n=164q full return; new four-group classification explicitly assumes q>41. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | ONLY the accepted integer/simple-zero compact Lipschitz discrepancy statement through L168, with actual powered degree and source-proof limits unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Normalization/Kronecker conventions through L168; separately ONLY house subsection's retained Dim19 v1 statement for E's old radical-control irreducibility, not for the new criterion. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0314_v1.md#triple-synchronization-whole-independent-finding) | Independent complete original01:13:07 D42 inspection, including locator-only prior helper role; that reviewer now authors this wrapper, so no prospective actual extraction coverage. |
| support | [Exact retained support](../computations/programs/Yin_J_G0011/readme.md#exact-reductions-and-verification) | Existing verified base Lehmer prime3 degrees2/8 and orders4/82; original programs/results remain in J and are not duplicated or rerun. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0316_v1.md#c86-triple-synchronization-actual-extraction-finding) | Entire actual A--F, complete retained original and all direct/source/control/cost interfaces; separate actual noncontributor with accepted C83 ancestor authorship disclosed. |

## Registration and complete preservation

The [original D42 complete freeze](#triple-synchronization-entire-author-freeze) is extraction ancestry, not an additional mathematical premise.
The ENTIRE actual original has21907 characters,189 lines and8 explicit anchors.
Its body is retained below with only duplicate author/framework front matter removed, the first title demoted by one hash, and boundary blank-line normalization.
All15 numbered equations, original candidate/reuse/history, full proof, control/source/contribution limits and freeze remain.
Relative ../ledger/, ../claims/ and ../audits/ paths remain valid here without rebasing.
No proof is replaced by a summary.

Rounding-recovery remains the sole new-proof author.
Review-recovery's prior lookup supplied only old material locators, and R314 is its independent review of the original proof.
Authoring this new statement and wrapper NOW makes review-recovery a contributor to this extracted artifact, whose actual review must be performed by a different noncontributor.
Historical pending-review prose remains at its original date; the selected initial decision records the actual extraction's current pending review.
Neither the original draft nor R314 is rewritten or retired.


No mathematical native program, source acquisition, adoption, draft retirement or unrestricted Task conclusion accompanies this allocation.
Programs and original control payloads remain solely in their responsible J.
Structural retention/checks do not establish mathematical acceptance of this wrapper.

## Argument

## Three-group residue synchronization forces one-time linear arithmetic income

Date: 2026-10-12T17:13.
Human author Yin.
New AUTHOR inquiry by rounding-recovery under the continuing G0001 instruction.
Root supplied the broad question whether replacing pairwise order synchronization by EVERY THREE occurring groups changes the arithmetic-income conclusion.
Root supplied no formula, intended verdict or proof.
The author previously reviewed and extracted the distinct C83 pairwise counterfamily; that work is accepted antecedent context, not independent evidence for this new argument.
No native mathematical computation is proposed.

<a id="triple-synchronization-question-and-reuse"></a>
## 1. Responsible question, reuse and candidate history

The exact current gate is [L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion): ACTUAL same-exponent income A(n)>=eta*d at ONE n<=C*d, using the full original nonzero norm, forces a positive measure bound with the accepted cost theorem's constants and source limits.
L168 supplies cost, not arithmetic coverage.

The actual adopted [C83](Yin_C_G0083_v1.md#statement) puts every original root at the fixed good prime2 in short odd-order groups, synchronizes EVERY PAIR by one exponent<=8d, and yet has sublinear COMPLETE binary income at EVERY fixed linear window.
Its all-depth formula and full m(P)=Theta(d) cost remain essential: it is neither a near-one counterfamily nor an upper bound for all-prime norm income.
[L217](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) gives a different actual full-depth counterfamily with bounded order/residue-degree ratio, again at large total measure.
Neither states a three-group conclusion.

The actual [L159 root capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) supplies sum_o w_o=d and0<=w_o<=phi(o) at a GOOD prime.
Its [Frobenius/inversion refinement](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) gives further actual orbit restrictions; these are retained, not replaced by arbitrary real weights.
L159's square-root short-order average upper bound does not control a single peak and is not the new mechanism.
[L213](../ledger/Yin_L_G0213_v1.md#full-depth-fixed-scope) controls all depths on selected low-residue-degree mass; it does not synchronize the remaining mass or bound the unselected total norm.

A narrow internal C/L screen for three-way/triple lcm, circle/Farey spacing, root capacity and maximum pair lcm found no statement of the particular result below.
The review-recovery agent independently performed ONLY an additional read-only reuse search, reporting L159, L74, C83 and L217 and the different [L225 anchored sparse cover](../ledger/Yin_L_G0225_v1.md#anchored-sparse-cyclic-cover).
The author read that L225 passage: it produces finitely many actual capture times from a supplied bounded-term rational multiple of a cyclotomic auxiliary, using its accepted minimal-relation theorem.
No such polynomial or bounded support is assumed here.
That helper supplied no new proof and no independent review.
These are bounded search facts, not a novelty or historical-priority certificate.

The initial counterfamily approach considered restricting C83's dense short-order set further.
Merely taking all orders<=Q would make generic triple lcms of cubic scale while its available full root capacity is only quadratic scale; increasing arbitrary weights or adding repeated residue roots would violate the good-prime capacity premise.
No polynomial counterexample was claimed or constructed from that failed direction.

The changed candidate is positive: use the circular separation of distinct roots of unity to price the largest pair lcm in actual root units.
Then anchor a pair attaining that maximum, and use the three-group premise to bound the residual orders.
The proposed conclusion concerns an ACTUAL polynomial satisfying this finite condition; it does not assert that all near-one inputs satisfy it.
All development is retained here, not in a temporary mathematical scratch file.

<a id="triple-actual-domain-and-statement"></a>
## 2. Actual domain and complete theorem

Let P in Z[t] be monic and irreducible, of original degree d>=1, with constant coefficient+/-1 and a nontorsion root alpha.
Reciprocity is allowed but not required.
Put

    K=Q(alpha), m=log M(P)>0,
    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0), n>=1.                         (1)

Fix a rational GOOD prime p, meaning p does not divide disc(P).
Its reduction has d DISTINCT nonzero roots in an algebraic closure of F_p.
Let O_p be its finite set of occurring multiplicative orders and let w_o be the number of original reduced roots of exact order o.
Each actual residue factor contributes its degree ONCE.
Then

    p does not divide o,
    w_o in Z_(>0), w_o<=phi(o), sum_(o in O_p)w_o=d.     (2)

These are the old L159/L74 conventions.
No repeated-root or arbitrary-weight substitute is permitted.
In the reciprocal subdomain the joint Frobenius/inversion constraints and excluded endpoint orders from L159 remain true; the proof uses the weaker capacity(2).

Select ANY nonempty subset S of these occurring groups, keeping every original root within each selected group, and let

    W=sum_(o in S)w_o, 1<=W<=d,
    L=max_(a,b in S) lcm(a,b),                         (3)

where repeated a=b is allowed in this definition.
Suppose an integer X>=1 satisfies

    lcm(a,b,c)<=X
    for every THREE DISTINCT a,b,c in S,               (4)

and |S|>=3.
Equivalently, each such triple has some common return exponent<=X.
No requirement that these initial triple exponents agree is imposed.

**Theorem1 (actual three-group capture).**
The following conclusions hold:

    W<=L<=X, B=floor(X/L)>=1.
    There exists an integer n<=X, p not dividing n,
    sum_(o in S, o divides n)w_o
        >=ceil(W/B)>=W/B>=W L/X>=W^2/X.                (5)

The exact FULL local income at that SAME exponent satisfies

    A_p(n):=(log p)v_p(C_n)
           =(log p)sum_(all d original p-adic roots a)v_p(a^n-1)
           >=ceil(W/B)log p
           >=(W^2/X)log p.                             (6)

Every actual initial/exceptional/later valuation is included in A_p; none is replaced by an asserted exact depth1.
The lower bound needs only the good-prime first-return floor.
Other roots or primes can add income, and no upper bound on that additional contribution is claimed.

A uniform version includes |S|1 or2 if(4) is REPLACED by the requirement that EVERY NONEMPTY subset of S of size AT MOST3 have a common exponent<=X.
For |S|1 or2 the common period of all selected groups is itself<=X, so all W roots are captured.
If only the literal three-distinct condition is supplied in these small cases, it is vacuous and no return bound is inferred.

**Corollary2 (positive-density finite arithmetic criterion).**
Fix0<gamma<=1 and C>0.
If an ACTUAL input has a good prime p and a set S satisfying the nonvacuous hypothesis of Theorem1 (or the at-most-three variant), with

    W>=gamma*d, X<=C*d,

then some ONE actual n<=C*d has

    A_p(n)>=eta*d,
    eta=(gamma^2/C)log2>0.                             (7)

In this domain X>=W, hence C>=gamma is necessary.
The prime p may vary with the input; log p>=log2 makes eta independent of that choice.
For the FULL set S=O_p with at least3 groups and every triple common by C*d, one may take gamma1, X=floor(C*d), obtaining eta=log2/C.
The sharper finite boundceil(d/floor(X/L))log p remains available.

All selected mass, the exponent, and the valuation belong to the SAME original input and one prime at one time.
The theorem does not infer this finite triple-compatibility premise from small m, high residue degree, pairwise compatibility or bounded order/residue-degree ratio.

<a id="pair-lcm-circular-capacity"></a>
## 3. The maximum pair lcm pays for actual root capacity

**Lemma3 (finite circular capacity).**
For any nonempty finite set S of positive integers and positive INTEGER w_o<=phi(o), define W and L by(3).
Then W<=L.

For each o choose w_o DISTINCT primitive o-th complex roots of unity.
This is possible by the capacity bound; root sets belonging to different exact orders are disjoint.
Altogether there are W distinct points on the unit circle.
This selection is a COUNTING device for the actual capacities already established in(2), not a claim that an arbitrary incidence array is the reduction of an integer polynomial or that these complex roots are the conjugates of P.
Alternatively an isomorphism from the finite cyclic group containing the actual reduced roots to the corresponding complex roots of unity preserves their exact orders and gives such a set directly.

Choose rational angles in[0,1) for all W points and sort them.
The W positive circular gaps sum to1.
If W=1 its single gap equals1, which is at least1/L.
If W>1, a consecutive gap (including the final wraparound gap) has endpoints of orders a,b in S.
Their angles have denominators dividing a and b.
The positive difference, with1 added for wraparound, therefore has denominator dividing lcm(a,b)<=L.
Its positive numerator is an integer, so

    each circular gap>=1/lcm(a,b)>=1/L.
    1=sum_(all W gaps) gap>=W/L.                      (8)

This proves W<=L.
It uses the total number of DISTINCT points, not the number of groups.
It also covers different roots from the same order because lcm(o,o)=o was included.
Fractions need not be reduced after subtraction; a nonzero multiple of1/lcm(a,b) still has that lower size.
No metric property of finite fields is invoked.

For |S|>=2, the same maximum L is attained by a pair of DISTINCT orders: a diagonal o is no larger than lcm(o,b) for any other b.
Under the literal hypothesis(4) with |S|>=3, a third distinct group shows lcm(a,b)<=X for every pair.
Thus the maximizing pair satisfies W<=L<=X.
This proves the first part of(5) with the correct nonvacuity conditions.

This finite spacing proof is an elementary local capacity deduction from the credited L159 root-count interface.
It neither fills all phi(o) slots nor constructs a new number field; the current theorem already starts with its actual P.

<a id="triple-anchored-residual-cover"></a>
## 4. Anchored residual orders and one actual capture time

Assume |S|>=3 and select distinct a,b in S with lcm(a,b)=L.
For EVERY o in S define

    r(o)=o/gcd(o,L) in Z_(>0),
    lcm(L,o)=L r(o).                                  (9)

For o=a or b one has r(o)=1.
For every other o, the three-distinct hypothesis applies to a,b,o and gives lcm(L,o)<=X.
Therefore r(o) belongs to{1,...,B}, B=floor(X/L).
Each r(o) is prime to p since every selected order and L is prime to p.

Partition S into the DISJOINT buckets S_r={o:r(o)=r}, retaining their actual masses W_r=sum_(o in S_r)w_o.
Empty buckets are allowed.
The sum of the B bucket masses is W, so some r has W_r>=ceil(W/B)>0.
At

    n=Lr<=X, p does not divide n,                      (10)

every o in S_r divides n by(9).
Other buckets can also return at n, which only increases the captured root mass.
Thus the actual selected returning mass is at leastceil(W/B).
Since B<=X/L and L>=W, one has W/B>=WL/X>=W^2/X.
This proves(5).

If |S|1 or2 and the at-most-three premise holds, let n be the lcm of ALL its orders.
Then n=L<=X and all W roots return; also W<=L by Lemma3 and W>=W^2/X.
Here B=floor(X/L) could exceed1, but the stated capture lower bounds remain true because W>=ceil(W/B).
This proves that variant without exploiting a vacuous triple condition.

The construction uses at most B explicitly specified candidate times Lr, not the full lcm of every order and not a sum of incomes at different times.
These are genuine integer times for the actual roots.
No rational polynomial multiple or auxiliary support bound from L225 is assumed.
The relation to its anchored-cover idea is only the common final finite-pigeonhole structure; here the hypotheses and the mechanism producing a bounded list are the pair-capacity lemma and THREE-group arithmetic.

<a id="triple-full-original-local-income"></a>
## 5. Full original norm, arbitrary depths and measure consequence

The good-prime hypothesis makes each local root unramified at p.
In the local normalization v_p(p)=1, every root is an algebraic unit.
If its residue order o divides n, then v_p(a^n-1)>=1.
If o does not divide n, that valuation is0.
These are precisely [C256's good-prime automatic floors](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail).
No upper bound or equality for an initial depth is assumed, and the possible binary exceptional jump is not discarded.

Because P is monic and uses the ORIGINAL degree d,

    D_n=product_(all d original roots a)(a^n-1),
    v_p(C_n)=sum_(all d original p-adic roots a)v_p(a^n-1).
                                                               (11)

Every term is nonnegative.
The actual signed norm D_n is nonzero, since alpha is nontorsion and all conjugates share that property.
Thus C_n is a positive integer.
Counting the bucket roots in(10) proves(6); unselected order groups and deeper valuations remain in the full left side and can only strengthen the lower bound.
In particular(6) is valid at p2 with every depth retained, although n itself is prime to p.

Combining W>=gamma*d and X<=Cd with(6) gives

    A_p(n)>=W^2 log p/X
           >=gamma^2*d*log p/C
           >=eta*d, n<=Cd.                            (12)

At that same exponent0<=A_p(n)<=log C_n.
This is exactly the accepted [L168 finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), not a merged sum from multiple exponents.
For completeness its actual constants can be selected as follows.
With eta from(7), choose T_ana>=1 and R_ana>=2 satisfying exp(-T_ana)/2+1/R_ana<=eta/4, put

    K_ana=(3exp(T_ana)+T_ana/R_ana)(4R_ana+1),
    tau=min(1,eta/4,eta^2/(16K_ana^2)),
    choose integer B_ana>=55 with log B_ana/B_ana<=tau,
    m0=min(tau/C,epsilon_(B_ana)/(2C))>0,              (13)

where epsilon_(B_ana) is L168's finite positive lower bound for heights of nontorsion units of degree at most B_ana.
The symbols B_ana,T_ana,R_ana are analytic parameters and are distinct from the combinatorial bucket count B and actual time X.

L168 proves log C_n/d<=3eta/4<eta whenever m<=m0 and n<=Cd, including powered-field degree drop.
This contradicts(12).
Therefore every actual input satisfying Corollary2 has

    m(P)>m0(C,eta)>0.                                  (14)

This is a PRECISE SUFFICIENT ARITHMETIC CONDITION with a uniform consequence.
The supplied finite epsilon construction has not been executed here, and no numerical value of m0 is asserted.
L168's sole accepted Pri11 discrepancy statement and recorded source/applicability limits are inherited at their current exact scope; no new proof audit or source acquisition is claimed.
No Dim19 sharpening is needed for(13)--(14).

The contrapositive says that on a hypothetical sequence m->0, for every fixed gamma,C, sufficiently late inputs have NO positive-density set of actual good-prime order groups satisfying this bounded three-group compatibility.
In particular, if there are at least three occurring groups at a given good prime, some triple has lcm>Cd.
For one or two groups the correct conclusion concerns an at-most-three subset whose common period exceedsCd; one cannot report a nonexistent triple.

This theorem concerns full local arithmetic income at the original degree.
There is no coefficient denominator q, rational packet weight M or auxiliary cofactor to be suppressed: the actual auxiliary is the SINGLE integer polynomial t^n-1 at its full degree n<=Cd, and its resultant uses the entire P.
It has coefficient content1 and coefficient squared norm2, but that elementary fact is not substituted for the full product-cost theorem.
All powers alpha^n are priced by the original norm tower in L168.

<a id="triple-controls-and-scope"></a>
## 6. Existing actual controls and the two-versus-three distinction

The old L159 [isolated good-prime return family](../ledger/Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate) gives a nonvacuous positive control.
Reuse its irreducible reciprocal unit F_q(t)=P_Lehmer(t^q), degree d=10q, for prime q>41.
Its old good-prime3 reduction starts with the Lehmer groups of orders4 and82 and masses2 and8.
Since gcd(q,164)=1, above each root of order o in{4,82}, exactly ONE q-th root has order o and the other q-1 roots have order oq: raising to q is an automorphism on the order-o subgroup, while the other q-th roots have nontrivial q component.
Consequently the FOUR actual groups and masses are

    (order,mass)=(4,2),(4q,2(q-1)),
                 (82,8),(82q,8(q-1)).                (15)

They total10q, with all roots distinct because3 is good.
Every triple shares the SINGLE period164q=(82/5)d.
At that time the old automatic floor already gives A_3>=d log3, stronger than the general pigeonhole guarantee.
These are existing actual polynomial and full-root data plus an elementary order classification, not a newly computed factorization or a synthetic weighted incidence example.
The old irreducibility justification has its retained accepted house-statement scope in L159; it is reused only for this comparison and is not needed in Theorem1.
The family has fixed positive Mahler measure, q expanding roots and a q-th-power degree drop.
It does not approach measure1 or lie in the all-powers degree-preserving unresolved core.

Conversely, the adopted C83 family satisfies all-pair lcm<=8d yet A_2(n)/d->0 uniformly for every fixed linear window.
If its actual full order set also satisfied all-triple lcm<=Cd for one fixed C along infinitely many large members, Theorem1 would supply A_2(n)>=d log2/C at some n<=Cd, a contradiction.
Hence for EVERY fixed C and all sufficiently large members, at least one actual triple has lcm>Cd.
Its number of occurring odd orders is already at least3 for Q>=64.
This is a logical consequence of two precise accepted/current bounds, not a new native experiment or an all-prime norm upper bound.

C83's complete original norm valuations and full m(P)=Theta(d) cost are unchanged.
L217's bounded order/residue-degree counterfamily likewise does not acquire a three-group hypothesis by its old efficient-order claim.
L213's all-depth low-degree escape remains consistent: the new sufficient criterion may fail precisely because high-degree order groups cannot satisfy the required joint periods.
No theorem here deduces the criterion from that escape result or from small measure alone.

The good-prime assumption is essential to this proof's capacity step.
At a bad prime, reduction multiplicities can repeat the same root without adding new circular points, so W<=L cannot be deduced from the displayed multiplicity count.
No bad-prime extension is claimed.
Nonnegative actual depth is retained but is not a replacement for the missing capacity bound.
No arbitrary positive real root weights, uncounted extra factors, or selected complex phases are being sold as an actual polynomial.

<a id="triple-source-and-author-check"></a>
## 7. Contribution, source limits and author verification

The new local mechanism is the finite circular capacity lemma followed by the maximizing-pair residual partition, giving a genuine single-time positive-linear mass/income criterion from three-group compatibility, including positive-density selections and the small-group nonvacuity guard.
The old good-prime root capacities, local valuation floor and full-product cost criterion receive exact L159/L74/L168 credit.
C83/L217/L213/L225 and the old radical family are comparisons at their stated scopes.
No new Hensel, finite-field cyclicity, discrepancy, house, minimal-relation or Mahler-cost theorem is claimed.

The local circular-gap and integer-pigeonhole calculations are fully supplied.
The reuse screen found no particular existing project version, but that is not a historical novelty claim.
The criterion requires an ACTUAL polynomial and its actual good-prime counts; an abstract capacity lemma within the proof does not realize arbitrary root data over the integers.

The author hand-checked every diagonal/distinct-order issue in L, the final circular wraparound gap, nonreduced fractional denominators, all1/2/3-group boundary cases, exact residual identity lcm(L,o)=Lr(o), bucket disjointness and possible extra returns, the integer ceil and all inequality directions, original d/full norm versus selected W, prime-to-p time and arbitrary depths at p2, positive-density constants, finite analytic m0 and powered-degree drop, and all four old radical-control groups with q>41.
No mathematical native program, external search, source acquisition or adoption was performed.

This author proof requires a separate noncontributing whole review and is not an independently reviewed result.

<a id="triple-synchronization-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T17:13.
The ENTIRE actual candidate/reuse/history and Sections1--7, equations(1)--(15), every actual-input hypothesis, local/full norm and near-one distinction, original contribution/source limits and boundary cases are frozen for separate whole review.
The result is a sufficient arithmetic criterion; it does not prove its coverage over the unrestricted G0001 class.
Root supplied the broad inquiry only and may arrange an independent review.
The reuse-search helper supplied locators only and is not credited as a proof author or as a whole reviewer.
