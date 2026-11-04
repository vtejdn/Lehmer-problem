---
author: Yin
---
# Paid common-divisor conditioning and the limits of collision localization

Date: 2026-10-15.
Human author Yin.
Continuing G0001 under the same root-owned execution; the g_bridge_audit AI develops this round.
Root proposes conditioning on common order-prime inventories and stripping that factor while asking whether a density increment can pay every retained-mass loss.
Root is a substantive contributor to that proposed mechanism, not an independent reviewer of its eventual use.

<a id="conditioning-responsible-question"></a>
## Responsible question and reuse boundary

Starting from C116's necessary intermediate-order-prime pair collisions, derive an actual paid conditioning/quotient invariant or identify a precise obstruction to turning it into positive-mass density localization.
Never infer a prime common to three labels from pair overlap.
Quotient real capacities are not complete groups of a new polynomial; every return must restore original root weights, physical time and full norm degree.

The bounded local screen read [L395](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) in full, including its exact common-factor capacity phi(ga)<=g phi(a), its prime-power/relative-core positive class and the failed bounded-star-cover induction.
C101 supplies the already accepted GCD-graph-derived logarithmic scale estimate, not an uncharged density increment.
C114 supplies the exact paid finite-core theorem.
C116 was fixed for independent whole review at the initial source check; before this freeze its actual [whole-reviewed decision](Yin_C_G0116_v1.md#decision-whole-reviewed-2026-10-15) adopted [R800 original actual-prime-budget](../audits/reviews/Yin_R_G0800_v1.md#actual-prime-budget-whole-independent-finding).
Its intermediate collision picture motivates the new question but is not a logical input in the positive proof below.
The needed new conclusion concerns arbitrary common-divisor conditional density and cumulative mass costs, beyond L395's already supplied transport.
A broader keyword search was truncated and supplies no absence evidence.
No novelty/exhaustive-search claim or new external theorem is asserted.
The finite transport calculations reuse L395's checked elementary capacity interface; the new partition estimate is a direct finite averaging argument requiring no new source theorem.

<a id="conditioning-working-argument"></a>
## Working argument

Preserve incremental deductions and useful failed implications here.
No native mathematical program is authorized or needed at this point.

<a id="partition-density-mass-invariant"></a>
<a id="argument"></a>
## 1. Exact partition density increment pays cumulative mass

Let a finite nonempty weighted label set have total W>0 and ordered repeated-label compatible-triple mass T=delta W^3>0.
Partition some or all labels into disjoint nonempty cells S_i, of masses W_i and internal triple masses T_i.
Suppose the ACTUAL internal retention is

    sum_i T_i >= a T,  0<a<=1.                         (1)

The omitted labels and cross-cell triples are fully charged in a.
Since sum_i W_i<=W, some cell with T_i>0 satisfies

    T_i/W_i >= a T/W.

Indeed otherwise summing T_i < (a T/W)sum_i W_i <=aT contradicts(1).
For p_i=W_i/W and delta_i=T_i/W_i^3 this is exactly

    delta_i p_i^2 >= a delta.                          (2)

No probability independence between prime events is used.
The occurrence of the square rather than the cube matters: it supplies the normalized density increase needed to pay the mass loss.

Repeat this selection finitely many times, allowing uniform rescaling of all weights between steps, which changes neither p nor delta.
If p_j is the chosen conditional mass fraction, a_j the actual retention lower bound, P_k=product_(j<k)p_j and A_k=product_(j<k)a_j, then induction gives

    delta_k P_k^2 >= delta_0 A_k,
    P_k >= sqrt(delta_0 A_k).                          (3)

The second line uses delta_k<=1.
Thus a depth-independent lower bound A_k>=a_*>0 keeps at least sqrt(delta_0 a_*) of the original mass, regardless of the number of levels.
It is NOT enough merely that a_j be a fixed positive constant: its product could vanish.
A sufficient explicitly paid condition is a_j>=1-epsilon_j with epsilon_j>=0 and sum_j epsilon_j<=1-a_*<1, since the finite product of(1-epsilon_j) is at least1-sum_j epsilon_j.
This is a direct finite averaging calculation, not an invocation of a source GCD-graph density increment.

<a id="common-factor-capacity-transport"></a>
## 2. Exact common-factor transport and physical invariants

For the arithmetic assertions from here onward, the labels are DISTINCT positive integers a in a finite set S, with0<w_a<=phi(a), and X>=1 is an integer.
Write W=sum_a w_a, T=T_X=sum_(lcm(a,b,c)<=X)w_a w_b w_c over all ordered triples in S including repetitions, and H_X=max_(integer1<=n<=X)sum_(a|n)w_a.
When T>0 put delta=T/W^3.
These are the exact meanings of capacity, density and capture below.

Suppose the chosen cell consists of labels divisible by a common integer g>=2.
Write a=g b and set u_b=w_(gb)/g, Y=floor(X/g).
L395's already checked phi(gb)<=g phi(b) gives u_b<=phi(b); there is no merging ambiguity because multiplication by one fixed g is injective.
For all tuples in the cell,

    lcm(gb_1,gb_2,gb_3)=g lcm(b_1,b_2,b_3).

Hence the quotient compatible mass is exactly T_cell/g^3, its total mass W_cell/g, and its triple density is EXACTLY delta_cell.
Positive T_cell proves Y>=1.
A quotient capture at time k<=Y returns precisely the original cell mass at time gk<=X after multiplying weights by g.
No new polynomial or new integral root-group law is asserted.

After finitely many steps put G=product of the stripped factors.
The current labels b correspond bijectively to a retained subset of ORIGINAL labels a=G b; the current real weights are w_a/G; the current physical window is exactly floor(X/G), because repeated integer floors commute with division by positive integers.
If current model mass is V, retained original mass is M=G V.
Conditional mass ratios p_j are therefore ratios of retained original masses.
Equations(3) apply to M/W, not to the smaller quotient mass V.
The actual original return time is Gk<=X.

For a prime q with q>sqrt(X), every eligible multiple of q has exponent exactly1 and its quotient is prime to q.
Here the SHARPER identity phi(qb)=(q-1)phi(b) permits u_b=w_(qb)/(q-1).
Using the uniform divisor q above deliberately pays the larger capacity factor; the sharper model has an extra q/(q-1) capacity advantage but is not needed for(3).
In particular stripping q does NOT create a free factor q of density or original mass.
All later arguments use the coarse exact physical invariant G and restore every original weight.

<a id="dominant-prime-partition"></a>
## 3. A concrete low-loss partition by primes above the square-root window

Assume now every current label a<=X, with integer X>=2.
A label can be divisible by at most ONE prime q>sqrt(X).
Partition labels carrying such a prime into their unique q-cells S_q.
Let S_0 be the remaining labels, including1; its original current-law mass fraction is rho.
Its labels have every prime factor at most sqrt(X).

Two labels in distinct q-cells have lcm divisible by distinct q r>X.
Consequently no compatible triple contained in the union of these cells can mix cells.
All compatible triples lost on passing to internal q-cells have at least one coordinate in S_0.
With repetitions retained, their exact ambient mass is at most

    [1-(1-rho)^3] W^3 <=3 rho W^3.

Thus the actual retention a=sum_q T_q/T satisfies

    a >= 1-[1-(1-rho)^3]/delta.                       (4)

The right side is useful only when positive.
If rho<=epsilon delta/3, then a>=1-epsilon.
Equations(1)--(3) choose one q-cell, then §2 strips q.
The new integer window Y=floor(X/q) is STRICTLY below sqrt(X).
Its labels remain eligible and its normalized capacities valid.
No statement about primes below the square-root window follows; pair overlap at an intermediate prime alone does not verify(4)'s small-rho premise.

<a id="recursive-roughness-capture-working"></a>
<a id="statement"></a>
## 4. Recursive sufficient certificate at arbitrary depth

Fix an integer N>=1 and0<a_*<=1.
Starting with an eligible finite capacity array and positive density delta_0, execute the preceding exact choices while the current window exceeds N.
Require at each executed step either the directly checked internal retention a_j>0, with all finite products A_j>=a_*, or the sufficient summable smooth-mass budgets rho_j<=epsilon_j delta_j/3 with sum epsilon_j<=1-a_*<1.
In the direct version a_j=sum_q T_q/T is the ACTUAL fraction, not the possibly negative lower bound in(4).
The requirement is on the actual chosen path, not every possible branch and not an automatic consequence of triple density.
Choose a cell maximizing T_q/W_q, so the rule is entirely finite; any maximizer is allowed, with the condition checked on its resulting path.

The windows strictly decrease and are squared down at every step.
For initial X>=2, after k>=1 executed steps the window is strictly less than X^(2^(-k)), so at most1+ceil(log_2(log_2 X)) steps are needed to reach window1.
If the initial window already lies at most N, use zero steps and the empty product A=1.
Thus every successful procedure terminates with a window<=N.
There are at most N distinct eligible labels there, so some label has at least1/N of its model mass and is captured at its own time.
Restoring original time and weights and using(3) gives

    H_X >= [sqrt(delta_0 a_*)/N] W.                   (5)

The actual product A may replace a_* in(5).
This proves an arbitrary-depth paid localization result for this explicit recursive structural class.
It does not prove that an actual polynomial supplies the required path/retentions.
A prescribed lower bound on the one-step retention alone is insufficient: the number of steps can grow, and that constant to the number of steps may tend to zero.
Equations(2)--(3), together with an actually bounded total loss, are what prevent repeated density charges.

<a id="initial-ineligible-and-actual-income"></a>
## 5. Initial ineligible mass and actual original-norm income

The original finite array may have labels above X.
Let its total mass be W, triple mass T=delta W^3>0, and let V be the mass of labels at most X.
All compatible triples are eligible, so V>0, T<=V^3 and the eligible density is delta_e=T/V^3.
No original group is split.
Apply the successful procedure to that eligible array, with the same actual product A>=a_*.
The previous conclusion restores original eligible weights and gives

    H_X >= sqrt(delta_e A)V/N
          =sqrt(A T/V)/N
          >=sqrt(delta A)W/N.                         (6)

Thus initial eligibility causes NO extra density/mass loss in this final inequality.
Equivalently its one-cell restriction has triple retention1, and already satisfies the squared-mass invariant.
It would be incorrect to use the smaller quotient mass as original degree, or to debit an additional fixed delta factor at every step.

For the actual polynomial domain, let P be monic irreducible nontorsion in Z[t] with constant coefficient+/-1 and original degree d.
Let ell be a good prime not dividing disc(P).
Select COMPLETE occurring residue-order groups with full original-root counts w_o, W>=gamma d for fixed0<gamma<=1.
Require an integer1<=X<=Cd, density delta_X>=delta>0, and the actual finite recursive certificate above with fixed integer N>=1 and fixed0<a_*<=1.
The accepted L159 capacities w_o<=phi(o) verify the initial array hypothesis.
Every later quotient law is explicitly only a real counting model; its selected original groups and returned integer time are tracked by §2.

Equation(6) supplies ONE integer n<=X capturing at least gamma sqrt(delta a_*)d/N original roots.
Keep the complete original signed norm and local income

    D_n=Res(P,t^n-1)=Norm_(Q(alpha)/Q)(alpha^n-1),
    log|D_n|>=A_ell(n)=v_ell(|D_n|)log ell
                  >=[gamma sqrt(delta a_*)/N]d log ell.

All original roots, unselected groups and higher/exceptional valuation depths remain on the left.
No income from different times is pooled and no quotient polynomial is asserted.
In particular eta=gamma sqrt(delta a_*)log2/N>0 is a fixed income coefficient.
The auxiliary t^n-1 retains its full degree n<=Cd, content1 and squared coefficient norm2.
L168's accepted original-norm finite criterion yields STRICT m(P)>m0(C,eta)>0, with its recorded powered-degree and source limits.
The common factors stripped in the proof divide actual residue orders and are prime to ell, but no claim of exact depth1 is used.

This is a positive ACTUAL covered class with an explicit finite certificate and no bounded-depth or bounded-mean-prime-support requirement.
L395 already treats a given common factor and suitable quotient support.
The additional conclusion here is that the paid recursive cell selection produces a positive original-mass subset despite arbitrarily many successive choices.
It does not merely assume that subset or claim general localization from density.

<a id="cumulative-loss-near-one-obligation"></a>
## 6. A quantitative cumulative-loss obligation near one

For the same actual domain define the finite original budget U_C(P)=max_(1<=n<=floor(Cd))log|D_n|/d, using only L168's already accepted uniform decay.
The actual floor gives H_X log ell<=d U_C(P).
For ANY successful path reaching window<=N with product A>0, equation(6) therefore forces

    A <= N^2 H_X^2/(delta_X W^2)
       <=N^2 U_C(P)^2/(delta gamma^2(log ell)^2).      (7)

All choices of eligible restriction, ties among maximizing cells and complete original selections retain the same upper bound.
For hypothetical near-one inputs retaining fixed delta,gamma,C and fixed N, every such successful path has A->0; alternatively the process can block earlier because no q-cell retains a compatible triple.
A blocked path has retention0 at its first block and does not satisfy the positive certificate.
When a positive path reaches N, (7) says explicitly

    sum_j -log a_j >=
      log[delta gamma^2(log ell)^2/(N^2 U_C(P)^2)],     (8)

whenever U_C(P)>0.
The right side tends to infinity near one.
If U_C(P)=0, positive-density actual coverage already contradicts the local floor, so no division by zero or positive path occurs.
The budget U_C and its decay are reused from L168; C116 was a motivating inquiry and is not a logical dependency of(7).

<a id="conditioning-failed-shortcuts-and-boundaries"></a>
## 7. Useful failure boundaries and actual contributions

Pair collision does not ensure this low-loss partition.
For any prime q, the one-label full-capacity array a=q^2, w=phi(q^2)=q(q-1), X=q^2 has W>=X/2, delta=1 and pair sharing of q with probability1.
Yet no label has a prime factor greater than sqrt(X); rho=1 and every dominant-prime cell is empty.
The procedure blocks for fixed N<X.
This is an exact finite capacity counterexample to an AUTOMATIC rough-partition inference from pair sharing, even with a linear window and density1.
It is already easily captured (H=W), and is not a near-one counterexample, an actual polynomial realization, or a refutation of another localization mechanism.
Letting q grow moves the shared prime outside every fixed pool while preserving the same obstruction.

Nor can pair overlap be promoted to a common prime for three labels: the three orders pq,pr,qr for distinct primes have pairwise intersections, while their three-way gcd is1.
The proofs above avoid that implication altogether: they use q>sqrt(X) to obtain a genuine disjoint partition and an exact incompatibility between DISTINCT cells, and pay every triple touching the omitted smooth cell.
C116's intermediate-prime collision window can extend both below and above sqrt(X); its conclusion supplies neither a positive proportion above sqrt(X) nor a bound on the omitted smooth mass.
No stronger conclusion is silently imported from it.

All arguments allow arbitrary positive REAL capacities, preserve ordered repetitions, and include the initial label1.
Zero weights can be removed.
Zero total or triple mass has no positive-density statement; T>0 ensures every chosen child and quotient has positive mass and a nonempty integer time range.
Empty q-cells are omitted.
If no positive internal triple remains, the certificate fails rather than choosing a zero-density child.
N=1 and X=1 use the stated zero-step case.
The square-root cutoff is strict, so primes with q^2=X lie in the omitted smooth part, and no floor or equality case is hidden.
Empty stripping products equal1.
Every finite product has factors in(0,1], and a_* is in(0,1].

Root supplied the substantive proposal of conditioning on a common order prime and paying cumulative mass by a density increment, and is a contributor to this mechanism.
The g_bridge_audit AI supplied the exact squared-mass invariant, its complete proof, the dominant-prime partition and leakage, the finite recursive certificate, actual original-norm transfer, and the quantitative cumulative-loss conclusion.
L395 supplies the existing common-factor capacity transport and is credited accordingly.
C114/C116 motivated this inquiry but their new theorems are not needed to prove the displayed positive certificate; no new external source theorem, mathematical program or J was used.
No universal near-one coverage, automatic smooth-mass budget or unrestricted Mahler gap has been proved.

<a id="conditioning-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T21:05.
Freeze the ENTIRE original account: exact partition retained-triple hypothesis and squared-mass density invariant; its finite induction and cumulative-product requirement; full common-divisor capacity/time/weight transport; strict dominant-prime partition and all discarded-triple charges; arbitrary-depth finite certificate and termination; initial ineligible-mass calculation; complete actual original-norm and degree costs; quantitative cumulative-loss necessity; exact failed inference and all boundaries; reuse/source limits and root/author contributions.
The author self-check includes arbitrary real weights, repeated tuples, initial and later normalizations, coarse versus sharp phi scaling, integer floor composition, every zero/empty case, the strict square-root endpoint, the finite depth bound, original eligibility inequality, restored physical time and full signed resultant, and the exact quantifiers of the conditional certificate.
No claim of automatically obtaining its retentions is made.
Separate noncontributor review must cover the actual fixed form; neither this author freeze nor a structural check supplies acceptance.

## Fixed organization

The ENTIRE final author body is retained: exact partition retention and squared-mass invariant, complete transport back to original weights/time, strict prime partition and cumulative-loss certificate, all actual norm prices, finite counterexamples, boundary cases and contribution/source limits.
Root contributed the conditioning mechanism, and cannot provide its independent whole review.
This actual fixed artifact awaits a separately organized noncontributor review.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:08 |
| status | open |
| reason | Retain the complete arbitrary-depth paid conditioning/localization class, physical return and actual norm costs, and exact cumulative-retention obstruction for whole independent review. Automatic retentions, general localization and original near-one coverage remain unproved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Recursive sufficient certificate and actual consequences](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Entire argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Existing common-factor transport](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Actual root-group capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Full original local norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Original norm decay](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:13 |
| status | proved |
| reason | Adopt [R797 original paid-conditioning](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) complete noncontributor review of the actual whole conditional certificate and every direct input. The squared-mass density invariant pays arbitrary-depth selections when the ACTUAL cumulative retention product stays positive; physical time, original weights and full norm costs are restored exactly. Automatic retention, general localization and near-one coverage remain open. Root's mechanism contribution is explicitly separated from independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Recursive sufficient certificate and actual consequences](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Entire argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Existing common-factor transport](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Actual root-group capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Full original local norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Original norm decay](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Actual entire finding](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) | Complete actual statement and §§1--7 argument, all selected interfaces, repeated/zero/floor cases, original norm and all-path loss quantifiers, source/contribution limits and failed automatic implications. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Dependency](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Review](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) | Complete actual statement and §§1--7 argument, all selected interfaces, repeated/zero/floor cases, original norm and all-path loss quantifiers, source/contribution limits and failed automatic implications. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Exact retained argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) | Complete actual statement and §§1--7 argument, all selected interfaces, repeated/zero/floor cases, original norm and all-path loss quantifiers, source/contribution limits and failed automatic implications. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Exact retained argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0395_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) | Complete actual statement and §§1--7 argument, all selected interfaces, repeated/zero/floor cases, original norm and all-path loss quantifiers, source/contribution limits and failed automatic implications. |

### Decision current-relative-core-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:37 |
| status | proved |
| reason | Use the newly adopted complete C471 as the same-object current home of the already-used exact L395 common-factor/totient or finite dyadic-prime deduction. The needed original proof and actual selected adoption were read directly; mathematical status, complete Argument, every other tuple and all original scopes are unchanged. This is proof-location maintenance, not a new independent verdict or retrospective repair of old UNKNOWN/SELF relationships; old dated input facts and fixed R bindings remain exact. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Exact argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Exact dependency](Yin_C_G0471_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Exact dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Exact dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Exact review](../audits/reviews/Yin_R_G0797_v1.md#paid-conditioning-whole-independent-finding) | Complete actual statement and §§1--7 argument, all selected interfaces, repeated/zero/floor cases, original norm and all-path loss quantifiers, source/contribution limits and failed automatic implications. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:39 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. The paid original-mass invariant, exact quotient transport, successful recursive certificate, original-norm consequence and every successful-path cumulative-loss necessity are supported, without automatic retention. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full §§4--6: exact successful-path hypotheses, fixed terminal N and cumulative retention, initial eligibility, same-time original norm income and all-path near-one product expense. |
| argument | [Exact argument](#argument) | Complete §§1--7/equations1--8, every partition/capacity/physical-time/density step, strict cutoff, finite endpoint and failed automatic inference. |
| dependency | [Exact dependency](Yin_C_G0471_v1.md#single-core-exact-window) | Exact phi(gb)<=g phi(b), quotient capacities and physical time/weight restoration; new density increment and cumulative selection are proved locally. |
| dependency | [Exact dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete selected original-root groups and actual phi capacities; quotient models are not new polynomial realizations. |
| dependency | [Exact dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time captured-root valuation floor with all original roots/depths and log ell retained. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Actual full resultant U_C(P) tending uniformly to zero on hypothetical near-one inputs, with original powered-field multiplicities retained. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler consequence from the stated actual linear income and n<=Cd with full auxiliary costs. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0118-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. |

