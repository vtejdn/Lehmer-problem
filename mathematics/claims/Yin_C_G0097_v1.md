---
author: Yin
---
# Bounded union-prime support, weighted residue synchronization and actual norm income

Date: 2026-10-13T04:28.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
The actual_income subagent authored the ENTIRE12:22 original D24.
The averaged_lcm subagent independently WHOLE-reviewed that original in R333 and NOW authors this statement/extraction wrapper, becoming a contributor to this new artifact.
Root supplied no original covering proof and will separately inspect the actual wrapper.
Original R333 does not prospectively review this newly authored statement or selection.
Initial status is proof draft / under review; every original candidate, failed transfer, source/cost boundary, proof and freeze is retained below.

## Statement

**A. Exact finite cover and arbitrary weighted capture.**
Let Q be a set of r>=1 distinct rational primes, S a finite nonempty set of positive integers whose prime divisors belong to Q, and w_a>0 arbitrary real weights.
Put N_r=(4r+3)^r and W=sum_(a in S)w_a.
For an integer X>=1 define ordered sums, including all repeated labels,

    T_2(X)=sum_(a,b in S, lcm(a,b)<=X)w_a w_b,
    T_3(X)=sum_(a,b,c in S, lcm(a,b,c)<=X)w_a w_b w_c,
    H_X=max_(integer1<=n<=X)sum_(a in S, a divides n)w_a.

For every anchor a in S with a<=X, its oriented compatible star

    B(a)={b in S:b<=a and lcm(a,b)<=X}

is covered by the divisor sets of at most N_r actual integers n_j<=X, all supported on Q.
There is no dilation of X.
Consequently

    H_X>=T_2(X)/(2N_r W),
    H_X>=T_3(X)/(2N_r W^2).

If every selected pair, including its diagonal, has lcm<=X, then H_X>=W/N_r.
A pair density T_2/W^2>=delta, or a triple density T_3/W^3>=delta, gives H_X>=delta W/(2N_r).
No totient-capacity bound, bound on prime sizes or bound on the number of orders is assumed.
For r=0 only order1 is possible; set N_0=1 and obtain H_X=W directly.
These constants also apply when the union support has at most r primes, by monotonicity of N_r.

**B. Actual same-time arithmetic income with complete costs.**
Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d, alpha a root, K=Q(alpha), m=log M(P)>0, and p a GOOD prime not dividing disc(P).
Select a nonempty set S of COMPLETE occurring reduced-root order groups, with actual original-root counts w_o and selected mass W.
Thus sum over all groups equals d, w_o<=phi(o), and p divides no order.
Assume the UNION of prime divisors of selected orders has size at most r, W>=gamma*d, an integer1<=X<=C*d, and T_2(X)>=delta W^2, for fixed C>0, 0<gamma,delta<=1 and r>=0.
The same conclusion follows from T_3(X)>=delta W^3.

Then there is ONE actual n<=X, supported on that union and therefore prime to p, for which

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(all d original p-adic roots a_i)v_p(a_i^n-1),
    log C_n>=A_p(n)>=eta*d,
    eta=gamma*delta*log2/(2N_r)>0.

Every original root and every initial, exceptional or later valuation remains on the left, including unselected groups.
Prime-to-p time does not imply initial depth1.
No different-time income is added.
The single auxiliary is t^n-1 of full degree n, coefficient content1 and squared coefficient norm2; no rational coefficient or packet denominator is introduced.
L168's exact finite same-time criterion therefore gives STRICT m>m0(C,eta)>0.
Under the all-pairs premise, eta improves to gamma*log2/N_r.
Actual powered-degree drops remain paid by the original norm tower.
In the reciprocal good-prime subclass order1/2 are absent, so r0 is empty there.

**C. Explicit necessary prime-pool growth under hypothetical near-one coverage.**
Retain

    c=log2/4, h0=c exp(-20),
    b(h)=max(h,sqrt(h/c)log sqrt(c/h)),
    Omega(h)=19 b(h)^(1/6), 0<h<=h0.

For actual inputs in B with union size r and Cm<=h0, L209's accepted increasing full norm modulus gives

    N_r>=gamma*delta*log2/[2Omega(Cm)].

For r>=1 this is equivalently the lower inequality

    r log(4r+3)>=log[gamma*delta*log2/(2Omega(Cm))].

Along any HYPOTHETICAL sequence satisfying the same fixed C,gamma,delta and actual pair-density premise, with m->0, necessarily r->infinity and

    r log(4r+3)>=(1/12)log(1/m)
                   -(1/6)log log(1/m)-O_(C,gamma,delta)(1),
    liminf r log log(1/m)/log(1/m)>=1/12.

The same holds under positive triple density.
These are consequences of ACTUAL coverage, not a proof of that coverage or existence of a near-one sequence.
L209's exact original/powered-degree interface and accepted Pri11/Dim19 statement/applicability scopes remain unchanged; no original external proof audit is claimed.

**D. Controls and limits.**
For at most two primes and the all-pairs premise, the sharper H_X=W follows by choosing occurring orders that attain each maximal prime exponent.
The union-support assumption is essential to the stated constants; bounding the prime support of each order separately does not establish it.
C83's full-pair/sublinear-local-income control and L217's efficient-order/two-prime control retain their distinct missing premises and full m=Theta(d) costs.
No unrestricted averaged short-lcm bound, unrestricted density implication for growing r, automatic near-one residue coverage, efficient-order-plus-pairwise theorem, positive unrestricted Mahler gap or zero-gap family is concluded.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:28 |
| status | open |
| reason | Register the exact finite fixed-union-prime cover, weighted pair/triple capture, actual same-time positive-income implication and conditional prime-pool growth, preserving the ENTIRE original12:22 D24. Original whole R333 passed without repairs; its reviewer now authors this wrapper, which awaits a distinct actual extraction/interface review. No automatic coverage or unrestricted Task result is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Entire original proof](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [L159 actual capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [L74 complete floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [L168 finite cost](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [L209 powered-height modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [C83 all-pair control](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [L217 efficient-order control](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Original whole independent review](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:31 |
| status | proved |
| reason | Adopt entire original R333 and distinct actual extraction R446 for the finite common-prime-pool cover, weighted pair/triple capture, full same-exponent arithmetic income, finite Mahler consequence and conditional quantitative prime-pool growth. The union-support and actual density hypotheses remain explicit; neither automatic near-one coverage nor the unrestricted G0001 gap is proved. Root did not contribute a covering proof or wrapper and independently inspected the actual extraction; all original history and source limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Entire original proof](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [L159 actual capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [L74 complete floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [L168 finite cost](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [L209 powered-height modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [C83 all-pair control](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [L217 efficient-order control](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Original whole independent review](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0796_v1.md#c97-bounded-pool-actual-extraction-finding) | Complete actual A--D, retained original and all direct interfaces, exact physical window, all weights/depths, union support, modulus and liminf, source and unresolved-scope boundaries. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Argument](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [Dependency](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [Support](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [Support](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Support](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#c97-bounded-pool-actual-extraction-finding) | Complete actual A--D, retained original and all direct interfaces, exact physical window, all weights/depths, union support, modulus and liminf, source and unresolved-scope boundaries. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Exact retained argument](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [Exact retained support](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#c97-bounded-pool-actual-extraction-finding) | Complete actual A--D, retained original and all direct interfaces, exact physical window, all weights/depths, union support, modulus and liminf, source and unresolved-scope boundaries. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Exact retained argument](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [Exact retained support](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#c97-bounded-pool-actual-extraction-finding) | Complete actual A--D, retained original and all direct interfaces, exact physical window, all weights/depths, union support, modulus and liminf, source and unresolved-scope boundaries. |


### Decision current-complete-powered-height-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:10 |
| status | proved |
| reason | Maintain the existing L209 input at the complete same-object C504 proof home after reading the full necessary consumer statement, argument interface and current scope against the complete C504 argument. Exactly the increasing Omega on the tiny actual-powered-height domain, norm-tower multiplicities and original Pri11/Dim19 statement/applicability scope, used for the conditional prime-pool growth bound. Preserve every other field except this actual date/reason, all nonmatching relations/reviews/scopes, every old decision and all mathematics. Historical reviewers retain their actual fixed inputs and are not represented as having read the later C504; no new whole review or independent-coverage upgrade is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Exact retained argument](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [Exact retained dependency](Yin_C_G0504_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [Exact retained support](Yin_C_G0527_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#c97-bounded-pool-actual-extraction-finding) | Complete actual A--D, retained original and all direct interfaces, exact physical window, all weights/depths, union support, modulus and liminf, source and unresolved-scope boundaries. |


### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--D, arbitrary positive weights, fixed union support, ordered repeats, all actual norms/depths/costs, quantitative necessary growth and unresolved unrestricted scope. |
| argument | [Exact retained argument](#argument) | ENTIRE12:22 D24, starting question and reuse, failed stronger transfer, all Sections1--5, equations1--13, sources, controls and original freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Complete good-prime root counts, p-free orders and reciprocal order1/2 boundary. Capacities are not required by the combinatorial cover. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Exact original root count and unramified first-return lower floor at the SAME n, all actual depths retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Positive eta*d at n<=Cd implies strict m>m0(C,eta); original norm tower and accepted source scope unchanged. |
| dependency | [Exact retained dependency](Yin_C_G0504_v1.md#height-uniform-cyclic-cost-modulus) | Exact increasing Omega(h) on0<h<=h0 with all actual powered-degree drops and retained Pri11/Dim19 input scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison only: full pairwise synchronization, sublinear all-depth binary income and growing union prime pool, with full m=Theta(d). |
| support | [Exact retained support](Yin_C_G0527_v1.md#efficient-order-fixed-scope) | Comparison only: primes3,5 and efficient orders, without the all-pairs bounded-linear-window hypothesis. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0333_v1.md#bounded-pool-whole-independent-finding) | Entire actual12:22 original and direct interfaces, no proof repairs. Does not prospectively review this newly authored wrapper. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0097-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |

## Organization after adoption

After original whole R333 and actual extraction R446, the selected decision adopts the exact fixed result.
Root compared the entire original body under the declared frontmatter/title/newline normalization, repaired exact incoming locators to the retained anchors, and retired the redundant working draft.
All original mathematical, failed-transfer, source and freeze text remains below.

## Argument

The ENTIRE actual12:22 original D24 follows, with ONLY the duplicate author/framework front matter removed and its initial title lowered by one heading level.
Its eight explicit anchors, original question/reuse and failed-transfer history, Sections1--5, equations1--13, exact proof and source/cost/control boundaries, author checking and freeze remain unchanged.
Relative links are valid from the sibling Claims directory.
The original author-stage pending-review wording records that earlier stage; the current assessment belongs to the selected decision above.
No draft retirement or actual extraction review is asserted by this preservation paragraph.

## Actual near-one arithmetic income and the residue-coverage gate

Date: 2026-10-13.
Human author Yin.
This rolling author inquiry is carried out by the actual_income subagent under the root's explicit assignment within the active [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
This file is a new proof investigation, not an adopted Claim or independent review.

<a id="actual-income-responsible-question"></a>
## Responsible question and starting scope

For an actual monic irreducible nontorsion integer-unit polynomial P of original degree d, decide whether the near-one hypothesis m(P) approaching zero can force a positive root-weighted order-triple density or circular score at a good prime with physical window X at most C d.
All original roots, complete local depths, and the full original norm must be retained.
Abstract finite-field order arrays are not actual near-one examples.
The immediate target is a proved bridge, or a precise obstruction to a proposed bridge, relevant to the missing same-exponent arithmetic income A(n) at least eta d.

The initial reuse set comprises [C86](Yin_C_G0086_v1.md#statement), [C88](Yin_C_G0088_v1.md#statement), [C91](Yin_C_G0091_v1.md#statement), [C94](Yin_C_G0094_v1.md#statement), [C83](Yin_C_G0083_v1.md#statement), and [L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion).
No new claim, source theorem, native program or fixed result is asserted at creation.

<a id="actual-income-reuse-and-changed-scope"></a>
## Bounded reuse, failed transfer and changed scope

The initial inspection read the exact conditional interfaces in C86/C88/C91, the full-cost limitation of C83, L159's Frobenius/inversion orbit capacities, L168's same-time criterion, and [L209's quantitative powered-height modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus).
C88 already proves that every positive-density circular score must fail along a hypothetical m(P) tending to zero.
Restating that necessary condition would not establish coverage.

A potentially stronger conjunction remains open here: pairwise short synchronization together with a bound o/ord_o(p) <= K.
C83 lacks the efficiency bound; [C527](Yin_C_G0527_v1.md#efficient-order-fixed-scope) has efficient orders but lacks pairwise short synchronization.
The elementary inequality ord_o(p) <= lambda(o), where lambda is the exponent of the unit group modulo o, bounds the prime-support complexity of EACH individual order when o/ord_o(p) is bounded.
It does not bound the UNION of primes across different orders.
No implication between these two different support assertions is adopted.
In particular, the theorem below uses the explicit union-support assumption and does not resolve this conjunction.

A bounded web search on 2026-10-13 used the two queries "set of integers pairwise least common multiple at most x sum Euler phi bounded prime factors" and "least common multiple clique totient sum large gcd finite set integers bounded prime factors".
The primary [Hilberdink--Toth abstract, arXiv:1604.04508](https://arxiv.org/abs/1604.04508) concerns average values of functions of lcm over boxes and does not provide the present covering statement in the inspected abstract.
It is not a proof dependency.
No secondary search result, source theorem, acquisition or bibliographic registration is used.
This is a bounded lead check, not a novelty assertion or exhaustive literature survey.

The new elementary argument instead resolves a fixed UNION-support subcase of actual coverage.
The size of the reduction prime and the sizes of the order primes remain unrestricted.
No native mathematical program or numerical experiment has been run.

<a id="bounded-order-prime-pool-cover"></a>
## 1. A bounded cover of a compatible oriented star

Let Q={q_1,...,q_r} be a set of r >= 1 distinct rational primes and let S be a finite nonempty set of positive integers whose prime divisors all belong to Q.
Assign arbitrary positive real weights w_b; no totient-capacity condition is needed for this combinatorial lemma.
Fix an integer X >= 1 and an anchor a in S with a <= X.
Consider only

    B(a)={b in S : b <= a and lcm(a,b) <= X}.

Write N_r=(4r+3)^r.
There exist at most N_r positive integers n_j <= X, all supported on Q, whose divisor sets cover B(a).
Consequently at least one of them captures weight at least

    (sum_(b in B(a)) w_b)/N_r.                         (1)

The anchor belongs to B(a), so the set is nonempty.
The construction proves the bound for the actual integer X; no dilation of the physical window is made.

**Proof.**
Put R=X/a >= 1.
If R=1, every b in B(a) divides a, so the single integer n=a suffices.
Assume R>1 and write L=log R>0,

    a=product_i q_i^(u_i),   b=product_i q_i^(v_i),
    y_i=L/log q_i,           c_i=ceil(y_i),
    ell_i=max(0,u_i-c_i),    v'_i=max(v_i,ell_i).

The two actual inequalities defining B(a) give

    sum_i (v_i-u_i)log q_i = log(b/a) <= 0,
    sum_i max(v_i-u_i,0)log q_i
          =log(lcm(a,b)/a) <= L.                         (2)

The truncated vector v' still satisfies

    sum_i (v'_i-u_i)log q_i <= 0.                       (3)

Indeed if no coordinate changed this is the first part of (2).
If a coordinate changed, then v_i<ell_i, so ell_i>0 and v'_i-u_i=-c_i, whose logarithmic contribution is at most -L.
Truncation does not change any positive contribution; their total remains at most L by (2).
Every other negative contribution is nonpositive.
This proves (3), including the case of several changed coordinates.

Each coordinate now lies in the finite range

    ell_i <= v'_i <= u_i+floor(y_i),
    (u_i+floor(y_i))-ell_i <= c_i+floor(y_i).             (4)

Define the positive integer step and rounded exponent

    t_i=max(1,floor(y_i/r)),
    k_i=ell_i+t_i ceil((v'_i-ell_i)/t_i).

Thus k_i >= v'_i >= v_i.
If t_i=1, all exponents are integral and rounding adds exactly zero.
If t_i>=2, then

    0 <= (k_i-v'_i)log q_i < t_i log q_i <= L/r.

Together with (3), summing over coordinates yields

    n(b):=product_i q_i^(k_i) <= a exp(L)=X,
    b divides n(b).                                      (5)

In fact the inequality is strict in the nontrivial positive-rounding case, but no strictness is needed.
Every n(b) is an integer supported on the same Q.
The common grid starts ell_i and steps t_i depend only on a, X and Q, not on b.

There are at most ceil((c_i+floor(y_i))/t_i)+1 possible values of k_i.
If y_i<r, then t_i=1 and this number is at most 2r.
If y_i>=r, then t_i=floor(y_i/r)>=1 and y_i<r(t_i+1).
Hence

    (c_i+floor(y_i))/t_i
       <= (2y_i+1)/t_i < 2r+(2r+1)/t_i <=4r+1.

The number of values is therefore at most 4r+2, in particular at most 4r+3.
At most N_r vectors k, and hence at most N_r integers n(b), occur.
Taking the weightiest fiber of b -> n(b) proves (1).
Extra b dividing that n only increase its captured weight.
This proof uses no numerical rounding approximation.
All floor and ceiling operations have exact real definitions; they can alternatively be decided by integer-power comparisons.

For r=0 the only possible order is 1; the statement holds separately with N_0=1 and n=1.
The formula (4r+3)^r is not needed at that boundary.

<a id="bounded-order-prime-pool-density"></a>
## 2. Weighted pair density and triple density give actual one-time capture

For the same S and weights put

    W=sum_(a in S) w_a,
    T_2(X)=sum_(a,b in S, lcm(a,b)<=X) w_a w_b,
    T_3(X)=sum_(a,b,c in S, lcm(a,b,c)<=X) w_a w_b w_c,
    H_X=max_(integer 1<=n<=X) sum_(b in S, b divides n)w_b.

All tuples are ORDERED and repeated labels, including diagonals, are retained.
For r>=1 the following unconditional bounds hold:

    H_X >= T_2(X)/(2 N_r W),
    H_X >= T_3(X)/(2 N_r W^2).                           (6)

If EVERY selected pair has lcm at most X, including the diagonal, the stronger bound is

    H_X >= W/N_r.                                         (7)

To prove (6), orient a compatible pair toward its numerically larger endpoint and count a diagonal once.
With B_w(a)=sum_(b<=a, lcm(a,b)<=X)w_b, one has exactly

    sum_a w_a B_w(a)
       =[T_2(X)+sum_(a<=X)w_a^2]/2 >= T_2(X)/2.           (8)

If T_2=0 the first inequality of (6) is immediate.
Otherwise some anchor has B_w(a)>=T_2/(2W)>0, and such an anchor necessarily has a<=X.
Apply (1) to that star.
The second inequality follows from T_3<=W T_2, because each compatible ordered triple has a compatible first pair and its possible third weights sum to at most W.
For (7), choose the largest selected integer a; its star is all S.
If r=0 then H_X=W and both conclusions hold directly with N_0=1.

Consequently a positive weighted PAIR density T_2/W^2 >= delta gives H_X >= delta W/(2N_r).
Positive triple density >=delta gives the same bound.
The constants depend only on the size r of the UNION of prime divisors, independently of X, the sizes of those primes, the number of order groups, the weights, or any totient capacities.
This does not assert that a positive pair density occurs for an arbitrary actual polynomial.

<a id="bounded-order-prime-pool-actual-income"></a>
## 3. Actual polynomial interface, complete norms and all depths

Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial, let alpha be a root, K=Q(alpha), d=deg P and m=m(P)>0.
Let p be a GOOD prime, p not dividing disc(P).
By [L159](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity), the complete order groups have actual integer root counts w_o, their sum over all occurring orders is d, p does not divide any o, and w_o<=phi(o).
Select a nonempty set S of COMPLETE occurring groups, retaining their full root counts, and set W=sum_(o in S)w_o.
Let Q be the union of the prime divisors of these selected orders; it has finite size r and never contains p.

Apply (6) with these ACTUAL weights and integer X>=1.
If T_2(X)>=delta W^2, then ONE actual integer n<=X satisfies

    sum_(o in S, o divides n)w_o >= delta W/(2N_r).

The constructed n is supported on Q, so p does not divide n.
This fact does not imply that the initial valuations equal one.
Retain the complete original signed norm and local income

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(all d original p-adic roots a_i)
                                v_p(a_i^n-1).

Every original root is counted once, including unselected groups and every initial, exceptional or deeper valuation.
[C256's good-prime floor](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) gives, at this SAME n,

    log C_n >= A_p(n) >= delta W log p/(2N_r).            (9)

No contribution from another time or another polynomial is added.
All omitted local and other-prime contributions are nonnegative.
The single actual auxiliary is t^n-1, with full degree n, coefficient content 1 and squared coefficient norm 2.
There is no coefficient denominator, indexed packet denominator, changed original degree or discarded powered-field multiplicity.
Root-order grouping supplies the certificate, not a finite-field lift of a newly invented polynomial.

Fix constants C>0, 0<gamma,delta<=1 and integer r>=0.
If an actual input admits the above data with W>=gamma d, X<=C d, union support at most r and pair density at least delta, then

    A_p(n) >= eta d,
    eta=gamma delta log2/(2N_r)>0.                       (10)

Thus [L168's finite same-time criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) yields m(P)>m_0(C,eta)>0, at its retained explicit constant and source-inspection scope.
No proof re-audit of its Pri11 input is claimed.
Under the all-pairs hypothesis (7), eta can instead be gamma log2/N_r.
A positive triple density also suffices through (6), without relying on any universal averaged-lcm constant K.

For a reciprocal good-prime input, order 1 and order 2 are absent by L159's actual reciprocity calculation.
Thus the r=0 case is empty in that subclass; keeping it in the general theorem prevents a vacuity at general integer units.

<a id="near-one-pair-density-prime-complexity"></a>
## 4. Quantitative prime-pool growth on a hypothetical near-one sequence

For the same fixed C,gamma,delta and an actual pair-dense input with X<=C d, use the accepted [L209 powered-height modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus):

    c=log2/4, h_0=c exp(-20),
    b(h)=max(h,sqrt(h/c) log sqrt(c/h)),
    Omega(h)=19 b(h)^(1/6),                  0<h<=h_0,
    log C_n/d <= Omega(nm/d).

The function Omega is increasing on this interval.
When C m<=h_0, equation (9) therefore gives the fully explicit necessary bound

    N_r >= gamma delta log2/[2 Omega(Cm)],
    r log(4r+3) >= log[gamma delta log2/(2 Omega(Cm))]
                                      when r>=1.         (11)

For r=0 the first inequality holds with N_0=1.
Every actual powered-degree drop is already paid in L209's norm tower; no degree-preservation assumption is added here.
This use also retains L209's accepted Pri11 and Dim19 statement/applicability boundaries, rather than claiming their external original proofs were checked anew.

As m tends to zero with C,gamma,delta fixed, the explicit modulus implies

    r log(4r+3) >= (1/12)log(1/m)
                   -(1/6)log log(1/m)-O_(C,gamma,delta)(1).
                                                               (12)

Indeed for small h the second term defining b dominates, and log(1/Omega(h))=(1/12)log(1/h)-(1/6)log log(1/h)+O(1), with c fixed.
Therefore any HYPOTHETICAL sequence of such actual pair-dense inputs with m->0 must have r->infinity, and

    liminf r log log(1/m)/log(1/m) >= 1/12.               (13)

For clarity, write t=log(1/m).
If r>=t along a subsequence, the ratio in (13) tends to infinity there.
On a subsequence with r<t, one has log(4r+3)<=log t+O(1); division of (12) by t proves the stated liminf.
Thus no unstated inversion of an asymptotic inequality is used.
The same necessary growth follows from positive triple density.
Equations (11)--(13) are consequences conditional on ACTUAL coverage, not an assertion that a near-one sequence exists or that such coverage is automatic.

<a id="bounded-pool-scope-and-controls"></a>
## 5. Controls, precise limits and author verification

The two-prime case has a sharper direct check: if every selected pair has lcm<=X and all orders use q_1,q_2, choose one occurring order attaining each of the two maximal prime exponents.
Their lcm is the lcm of ALL selected orders, so that one n<=X captures W.
The one-prime and empty-support cases are immediate.
This confirms that the general covering constant is deliberately nonoptimal.

C83 remains compatible with the new theorem: its full-mass pairwise short synchronization and sublinear all-depth local income force its union of order primes to grow; the proof there takes all odd orders in a growing range.
Its full m=Theta(d) still prevents a near-one claim.
L217 instead has order primes only 3 and 5 but no bounded pairwise linear-window hypothesis; applying the theorem without checking that hypothesis would be invalid.
The older C88 all-model score obstruction does not refute (9), since it does not give the new bounded-pool pair-density hypothesis for those controls.

This theorem is a conditional positive bridge for a new explicitly restricted class.
It proves neither a uniform upper bound for C91's unrestricted averaged short-lcm extremum nor a general pair-density implication when r grows.
It does not establish pair density, a bounded prime pool, the efficient-order conjunction discussed above, a new near-one family, or the unrestricted G0001 gap.
The next actual-input problem is whether near-one structure gives enough compatible mass with a controlled UNION prime pool, or whether another direct selector remains effective despite the necessary growth (12).
Bounds on the prime support of each order separately must not be silently substituted.

The author checked the grid truncation before rounding, exact integrality of rounded exponents, the R=1 and r=0 boundaries, the case of empty oriented stars, diagonal/orientation factors, the all-pairs sharper factor, original-degree and all-depth norm interfaces, the explicit modulus interval, and the asymptotic liminf step.
All mathematical inequalities above are hand arguments; no retained numerical or native program evidence is asserted.
This is contributor checking only.
A separate noncontributor review of the entire actual draft and its direct accepted-input interfaces is required before fixed adoption.

<a id="bounded-pool-entire-author-freeze"></a>
## Entire-author freeze

2026-10-13T04:22.
The entire present draft is ready for a separate noncontributor review, including its original question, bounded reuse and unsuccessful stronger transfer, Sections 1--5, equations (1)--(13), precise actual norm and source interfaces, and all scope limits.
Root supplied only the broad research assignment and subsequent coordination about parallel work; it supplied no covering lemma, rounding construction or proof step.
The actual_income subagent authored this entire mathematical draft.
No mathematical claim is yet adopted and no source or native program artifact was newly acquired.
