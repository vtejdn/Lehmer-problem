---
author: Yin
---
# Efficiency-two residue orders, prime-power density and complete same-time norm capture

Date: 2026-10-13T05:12.
Human author Yin.
Internal fixed extraction within the continuing G0001 authorization.
The actual_income subagent authored the ENTIRE NEW D25 frozen2026-10-13T04:59.
The separately assigned averaged_lcm subagent independently WHOLE-reviewed that original in R338 and NOW authors this statement/extraction wrapper, becoming a contributor to this new artifact.
Root provided the inquiry, density-variant request and unused source lead, without contributing a proof step; it will separately inspect this ACTUAL wrapper.
R338 covers the original only.
Initial assessment is proof draft / under review, with complete original history preserved below.

## Statement

**A. Exact low-efficiency classification and actual full groups.**
Let p be prime, gcd(p,o)=1, and f_p(o)=ord_o(p), with f_p(1)=1.
If o/f_p(o)<=2, then o is1, an odd prime power,2 or4.
At every permitted nontrivial order f_p(o)=phi(o).
For an ACTUAL good-prime reduced-root inventory, any nonempty COMPLETE group satisfying this condition therefore has w_o=phi(o), including w_1=1 if order1 occurs.
This follows from the exact Frobenius constraint that w_o is a positive multiple of f_p(o) and at most phi(o).
The reciprocal good-prime subclass separately excludes orders1/2.
No converse assertion that every listed modulus occurs for a given p is made.

**B. Prime-power capacities and density without a union-prime bound.**
Let S be a finite nonempty set of positive integers each equal to1 or a prime power, with arbitrary real weights0<w_a<=phi(a), total W, and integer X>=1.
Define

    U_X=sum_(a in S,a<=sqrt(X))w_a,
    w_1=the weight of1 if present, otherwise0,
    V_q=sum_(a in S,a=q^e<=X,e>=1)w_a,
    G_X=max({w_1} union {w_1+V_q:V_q>0}),
    H_X=max_(integer1<=n<=X)sum_(a in S,a divides n)w_a.

Thus G_X=0 when no order is eligible.
Every positive G_X is ACTUALLY captured at1 or the largest selected eligible power of one prime, at a time<=X.
In particular G_X<=H_X.
Write ordered compatible masses, including every repeated label,

    T_2(X)=sum_(a,b in S,lcm(a,b)<=X)w_a w_b,
    T_3(X)=sum_(a,b,c in S,lcm(a,b,c)<=X)w_a w_b w_c.

Then

    U_X<=1+sqrt(X)pi(sqrt(X)),
    pi(y)<=7y/log y for all real y>=16,
    U_X<=1+14X/log X for all integer X>=256,
    T_2(X)<=G_X W+2U_X W,
    T_3(X)<=G_X^2 W+3U_X W^2.

The finite prime estimate is proved by the retained elementary dyadic/binomial theta argument; an analytic prime-number theorem is not a premise.
Consequently positive pair density at least delta gives G_X/W>=max(0,delta-2U_X/W), and positive triple density at least delta gives G_X/W>=sqrt(max(0,delta-3U_X/W)).
No bound on the UNION of order primes or on their sizes is assumed.

For fixed C0>0 and0<delta<=1, put the explicit finite constants

    Z=max(256,8C0/delta,exp(112C0/delta)),
    c(C0,delta)=min(delta/2,sqrt(delta)/(1+ceil(Z)))>0.

If X<=C0 W and EITHER T_2(X)>=delta W^2 OR T_3(X)>=delta W^3, then ONE n<=X, equal to1 or a prime power, captures at least c(C0,delta)W.
This holds for EVERY finite member, including small X and missing order1.
On any such sequence with fixed C0,delta and W->infinity,

    liminf G_X/W>=delta under the pair-density premise,
    liminf G_X/W>=sqrt(delta) under the triple-density premise.

**C. All-pairs concentration.**
If every selected pair INCLUDING its diagonal has lcm<=X, then S={1} is captured at1.
Otherwise choose the largest selected nontrivial prime power M.
It satisfies M<=X and

    h(M)>=W-sqrt(X)pi(sqrt(X)),
    H_X>=W-sqrt(X)pi(sqrt(X)).

For X>=256 and X<=C0W, h(M)/W>=1-14C0/log(X).
Hence for unbounded W the ACTUAL prime-power time M captures1-o(1) of all selected mass.
The finite constant in B with delta1 separately handles every small member.

**D. Actual same-exponent arithmetic income and finite Mahler consequence.**
Let P be ACTUAL monic irreducible nontorsion in Z[t], with constant coefficient+/-1, ORIGINAL degree d, root alpha, K=Q(alpha), m=log M(P)>0, and a GOOD prime p not dividing disc(P).
Select COMPLETE occurring order groups of actual mass W>=gamma*d, with fixed0<gamma<=1, and require o/f_p(o)<=2 for every selected order.
Let integer1<=X<=C*d, C>0, and suppose their weighted pair density T_2/W^2 or triple density T_3/W^3 is at least fixed0<delta<=1.

Then ONE actual n<=X, equal to1 or a power of one order prime and thus prime to p, satisfies

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(ALL d original p-adic roots a_i)v_p(a_i^n-1),
    log C_n>=A_p(n)>=eta*d,
    eta=gamma*c(C/gamma,delta)*log2>0.

Every original root, unselected group, initial/exceptional/deeper valuation and other-prime nonnegative contribution remains.
Prime-to-p time does not mean first depth1.
The actual auxiliary t^n-1 has full degree n, content1 and squared coefficient norm2; no rational coefficient/indexed packet denominator occurs.
The norm remains in the original K, including powered-degree drops.
L168's accepted finite criterion gives STRICT m>m0(C,eta)>0 with its existing Pri11 statement/applicability scope.
Under all-pairs synchronization use delta1; the asymptotic captured fractions in B/C retain their stated hypotheses.

**E. Genuine control and unresolved scope.**
The actual reciprocal polynomial t^2-3t+1 has degree2, total m=log[(3+sqrt5)/2]>0, fixed good prime2 and one order3 group of full mass2, with f_2(3)=2.
At n3 the exact signed norm is-16, C_3=16 and A_2(3)=4log2.
Both original local roots have first valuation2.
This is a full-cost fixed positive control, not a near-one family.

The theorem resolves the specified efficiency<=2 covered class, including the endpoint, and proves the combinatorial prime-power-capacity result for arbitrary smaller real weights.
It does not solve the general fixed K>2 conjunction or produce automatic near-one density/efficiency.
Individual prime-support bounds are not union-support bounds.
C83/L217 retain their distinct missing hypotheses and full costs; no cardinality theorem from the uninspected Chen lead is imported.
On a hypothetical m->0 sequence, the fixed C,gamma,delta hypotheses in D must eventually fail, without proving existence or nonexistence of such a sequence.
The unrestricted G0001 goal remains open.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:12 |
| status | open |
| reason | Register exact efficiency<=2 classification, prime-power weighted pair/triple-density capture with explicit all-finite constants, asymptotic chain concentration, actual full-norm positive income and genuine depth2 control. ENTIRE actual12:59 original and whole independent R338 are retained. Its reviewer now authors this wrapper, requiring a distinct actual extraction/interface review before adoption. GeneralK>2 and automatic near-one coverage remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted statement](#statement) | Complete A--E, threshold2 including endpoints, arbitrary prime-power capacities, all finite and asymptotic bounds, actual original norms/costs and remaining scope. |
| argument | [Entire original argument and history](#argument) | ENTIRE NEW12:59 D25, responsible question, bounded source/reuse/failed transfer, Sections1--6/equations1--11, all norms, controls and author freeze. |
| dependency | [L159 Frobenius capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Exact complete group multiplicities, capacities and reciprocal order1/2 exclusion. |
| dependency | [L159 dyadic theta argument](../ledger/Yin_L_G0159_v1.md#necessary-prime-range-for-density) | Existing elementary binomial/dyadic prime bound, fully recalled and adapted to the stated finite pi estimate. |
| dependency | [L74 original root floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, all original roots, complete actual depths on the left, first-return floor including p2. |
| dependency | [L168 finite norm-cost criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict m>m0(C,eta) after eta*d income at n<=Cd, with original-field norm tower and accepted Pri11 source scope. |
| support | [C83 all-pairs control](Yin_C_G0083_v1.md#statement) | Comparison: full pairwise synchronization/sublinear local income without the present low-efficiency hypothesis; complete m=Theta(d) retained. |
| support | [L217 efficient-order control](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison: efficient orders3^a5^b at ratio15/4, without a uniformly short all-pair window. |
| support | [C97 separate bounded-union result](Yin_C_G0097_v1.md#statement) | Comparison only; its explicit union bound is not assumed from individual efficiency and is not used to prove the new prime-power density theorem. |
| support | [Original whole independent review](../audits/reviews/Yin_R_G0338_v1.md#efficient-two-whole-independent-finding) | Entire actual12:59 original and all direct interfaces, no repairs; does not pre-review this newly authored wrapper. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-13T05:19 |
| status | proved |
| reason | Adopt R338 original whole review and R340 distinct actual extraction review for the complete efficiency<=2 classification, arbitrary prime-power-capacity density theorem, every finite constant and asymptotic guard, actual original-norm income and depth2 control. General K>2 and automatic near-one coverage remain unresolved; this restricted positive bridge does not complete G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted statement](#statement) | Complete A--E, threshold2 including endpoints, arbitrary prime-power capacities, all finite and asymptotic bounds, actual original norms/costs and remaining scope. |
| argument | [Entire original argument and history](#argument) | ENTIRE NEW12:59 D25, responsible question, bounded source/reuse/failed transfer, Sections1--6/equations1--11, all norms, controls and author freeze. |
| dependency | [L159 Frobenius capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Exact complete group multiplicities, capacities and reciprocal order1/2 exclusion. |
| dependency | [L159 dyadic theta argument](../ledger/Yin_L_G0159_v1.md#necessary-prime-range-for-density) | Existing elementary binomial/dyadic prime bound, fully recalled and adapted to the stated finite pi estimate. |
| dependency | [L74 original root floors](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, all original roots, complete actual depths on the left, first-return floor including p2. |
| dependency | [L168 finite norm-cost criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict m>m0(C,eta) after eta*d income at n<=Cd, with original-field norm tower and accepted Pri11 source scope. |
| support | [C83 all-pairs control](Yin_C_G0083_v1.md#statement) | Comparison: full pairwise synchronization/sublinear local income without the present low-efficiency hypothesis; complete m=Theta(d) retained. |
| support | [L217 efficient-order control](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison: efficient orders3^a5^b at ratio15/4, without a uniformly short all-pair window. |
| support | [C97 separate bounded-union result](Yin_C_G0097_v1.md#statement) | Comparison only; its explicit union bound is not assumed from individual efficiency and is not used to prove the new prime-power density theorem. |
| support | [Original whole independent review](../audits/reviews/Yin_R_G0338_v1.md#efficient-two-whole-independent-finding) | Entire actual12:59 original and all direct interfaces, no repairs; does not pre-review this newly authored wrapper. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0340_v1.md#efficient-two-actual-extraction-finding) | Complete actual statement and preserved argument, all finite and limiting cases, direct source/interfaces and remaining unrestricted scope. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete A--E, threshold2 including endpoints, arbitrary prime-power capacities, all finite and asymptotic bounds, actual original norms/costs and remaining scope. |
| argument | [Argument](#argument) | ENTIRE NEW12:59 D25, responsible question, bounded source/reuse/failed transfer, Sections1--6/equations1--11, all norms, controls and author freeze. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Exact complete group multiplicities, capacities and reciprocal order1/2 exclusion. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#necessary-prime-range-for-density) | Existing elementary binomial/dyadic prime bound, fully recalled and adapted to the stated finite pi estimate. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, all original roots, complete actual depths on the left, first-return floor including p2. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict m>m0(C,eta) after eta*d income at n<=Cd, with original-field norm tower and accepted Pri11 source scope. |
| support | [Support](Yin_C_G0083_v1.md#statement) | Comparison: full pairwise synchronization/sublinear local income without the present low-efficiency hypothesis; complete m=Theta(d) retained. |
| support | [Support](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison: efficient orders3^a5^b at ratio15/4, without a uniformly short all-pair window. |
| support | [Support](Yin_C_G0097_v1.md#statement) | Comparison only; its explicit union bound is not assumed from individual efficiency and is not used to prove the new prime-power density theorem. |
| support | [Support](../audits/reviews/Yin_R_G0338_v1.md#efficient-two-whole-independent-finding) | Entire actual12:59 original and all direct interfaces, no repairs; does not pre-review this newly authored wrapper. |
| review | [Review](../audits/reviews/Yin_R_G0340_v1.md#efficient-two-actual-extraction-finding) | Complete actual statement and preserved argument, all finite and limiting cases, direct source/interfaces and remaining unrestricted scope. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--E, threshold2 including endpoints, arbitrary prime-power capacities, all finite and asymptotic bounds, actual original norms/costs and remaining scope. |
| argument | [Exact retained argument](#argument) | ENTIRE NEW12:59 D25, responsible question, bounded source/reuse/failed transfer, Sections1--6/equations1--11, all norms, controls and author freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Exact complete group multiplicities, capacities and reciprocal order1/2 exclusion. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#necessary-prime-range-for-density) | Existing elementary binomial/dyadic prime bound, fully recalled and adapted to the stated finite pi estimate. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, all original roots, complete actual depths on the left, first-return floor including p2. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict m>m0(C,eta) after eta*d income at n<=Cd, with original-field norm tower and accepted Pri11 source scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison: full pairwise synchronization/sublinear local income without the present low-efficiency hypothesis; complete m=Theta(d) retained. |
| support | [Exact retained support](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope) | Comparison: efficient orders3^a5^b at ratio15/4, without a uniformly short all-pair window. |
| support | [Exact retained support](Yin_C_G0097_v1.md#statement) | Comparison only; its explicit union bound is not assumed from individual efficiency and is not used to prove the new prime-power density theorem. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0338_v1.md#efficient-two-whole-independent-finding) | Entire actual12:59 original and all direct interfaces, no repairs; does not pre-review this newly authored wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0340_v1.md#efficient-two-actual-extraction-finding) | Complete actual statement and preserved argument, all finite and limiting cases, direct source/interfaces and remaining unrestricted scope. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete A--E, threshold2 including endpoints, arbitrary prime-power capacities, all finite and asymptotic bounds, actual original norms/costs and remaining scope. |
| argument | [Exact retained argument](#argument) | ENTIRE NEW12:59 D25, responsible question, bounded source/reuse/failed transfer, Sections1--6/equations1--11, all norms, controls and author freeze. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Exact complete group multiplicities, capacities and reciprocal order1/2 exclusion. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#necessary-prime-range-for-density) | Existing elementary binomial/dyadic prime bound, fully recalled and adapted to the stated finite pi estimate. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same actual n, all original roots, complete actual depths on the left, first-return floor including p2. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict m>m0(C,eta) after eta*d income at n<=Cd, with original-field norm tower and accepted Pri11 source scope. |
| support | [Exact retained support](Yin_C_G0083_v1.md#statement) | Comparison: full pairwise synchronization/sublinear local income without the present low-efficiency hypothesis; complete m=Theta(d) retained. |
| support | [Exact retained support](Yin_C_G0527_v1.md#efficient-order-fixed-scope) | Comparison: efficient orders3^a5^b at ratio15/4, without a uniformly short all-pair window. |
| support | [Exact retained support](Yin_C_G0097_v1.md#statement) | Comparison only; its explicit union bound is not assumed from individual efficiency and is not used to prove the new prime-power density theorem. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0338_v1.md#efficient-two-whole-independent-finding) | Entire actual12:59 original and all direct interfaces, no repairs; does not pre-review this newly authored wrapper. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0340_v1.md#efficient-two-actual-extraction-finding) | Complete actual statement and preserved argument, all finite and limiting cases, direct source/interfaces and remaining unrestricted scope. |

## Argument

The ENTIRE actual12:59 NEW D25 follows, with ONLY its duplicate author/framework front matter omitted and its first title demoted by one heading level.
All nine explicit original anchors, responsible question, source/reuse and failed general-K history, Sections1--6/equations1--11, complete proof, actual control, scope/source boundaries, contributor checking and author freeze remain unchanged.
Relative links remain valid in this sibling Claims directory.
Original author-stage pending-review wording records history; the current assessment is selected above.
No draft retirement, actual extraction review or adoption is asserted here.

## Efficient residue orders and pairwise short synchronization

Date: 2026-10-13.
Human author Yin.
New author inquiry by actual_income under the continuing G0001 task and root assignment.
This draft contains substantive ongoing research, not an adopted result or independent review.

<a id="efficient-pairwise-responsible-question"></a>
## Exact responsible question and starting reuse

For an ACTUAL monic irreducible nontorsion integer-unit polynomial of original degree d, a good prime p and complete occurring order groups with counts w_o, investigate the conjunction of pairwise lcm at most C d and o/ord_o(p) at most K, uniformly over all selected orders.
A positive-density variant must state exactly which pairs or groups it covers.
The aim is a same-time linear root capture or a rigorous actual counterfamily with every root, depth and original Mahler cost paid.
Neither the single-order ratio nor an individual bound on the number of prime factors is a bound on their UNION.

Starting inputs are [L159's actual Frobenius capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity), [C83's full-pair counterfamily](Yin_C_G0083_v1.md#statement), [C527's efficient-order counterfamily](Yin_C_G0527_v1.md#efficient-order-fixed-scope), and [C97's bounded-union-support theorem](Yin_C_G0097_v1.md#statement).
The now adopted [C96](Yin_C_G0096_v1.md#statement) and [C98](Yin_C_G0098_v1.md#statement) refute stronger averaged and linear-in-density candidates without solving the genuine fixed-density or near-one question.
All these exact scopes were read before the present analysis.
No new computation or result is asserted at creation.

<a id="efficient-pairwise-reuse-boundary"></a>
## Reuse, bounded source check and the remaining general question

The two existing negative controls do not meet the conjunction: C83 supplies complete pairwise short synchronization without a uniform o/ord_o(p) bound, whereas L217 has efficient orders supported on3,5 but does not supply pairwise synchronization on a fixed degree-linear window.
C97 covers a bounded UNION of order primes; bounding each order's prime support does not give that union.
The general fixed K>2 conjunction remains unresolved here.

The current elementary argument proves a definite low-ratio case, including the endpoint K=2, and also a positive weighted pair/triple-density version.
Root requested that the density variant be checked but supplied no proof step.
No general-K assertion, sparse-support induction or union-support implication is assumed.

Root supplied a primary-source lead to Chen, Sequences with bounded l.c.m. of each pair of terms, Acta Arithmetica84(1998),71--95, at https://matwbn.icm.edu.pl/ksiazki/aa/aa84/aa8416.pdf, noting its cardinality-maximizer scope.
This author's direct open on2026-10-13 returned403 Forbidden.
Its content/proof was not acquired or used, and no transfer to root-weighted capacities is claimed.

For attribution of the classical sparsity of primes, this author directly read the primary [DLMF27.12 page](https://dlmf.nist.gov/27.12), its definition of pi(x), and equation27.12.E4.
The displayed asymptotic in particular implies pi(x)=o(x); its original analytic proof and stronger expansion are NOT adopted as premises.
The precise nonoptimal finite bound needed below is instead proved completely from [L159's existing elementary dyadic theta argument](../ledger/Yin_L_G0159_v1.md#necessary-prime-range-for-density).
This preserves classical attribution without introducing an uninspected analytic theorem or claiming novelty for prime sparsity.
No mathematical native program, source acquisition or new global source record was made.

<a id="efficient-two-order-classification"></a>
## 1. Efficiency at most two forces prime powers and full root groups

Let p be a rational prime, let o be a positive integer prime to p, and write f_p(o)=ord_o(p), with f_p(1)=1.
Suppose

    o/f_p(o)<=2.                                         (1)

Then o=1, an odd prime power,2, or4.
At every nontrivial permitted order,

    f_p(o)=phi(o).                                        (2)

Consequently, for a GOOD-prime root inventory of an actual monic irreducible integer-unit polynomial, every nonempty order group satisfying(1) has its FULL capacity w_o=phi(o), including w_1=1 when order1 occurs.
No reciprocal hypothesis is required; the good-prime reciprocal case separately excludes orders1/2 by L159.

Here is a complete proof.
If o has at least two distinct odd prime divisors, split it into coprime factors A,B each having an odd prime divisor.
Their totients are both even.
The order modulo o is the least common multiple of the two component orders, and therefore divides lcm(phi(A),phi(B))<=phi(o)/2.
Since phi(o)<o, this makes o/f_p(o)>2, contradicting(1).

If o=2^e u with e>=1 and odd u>1, then for e=1 its order is at most phi(u), giving o/f>=2u/phi(u)>2.
For e>=2 Euler's order divisibility gives f<=phi(o), whereas o/phi(o)=2u/phi(u)>2.
Thus no mixed even/odd modulus occurs.

For o=2^e with e>=3, every odd p satisfies p^2=1 modulo8.
Squaring repeatedly proves p^(2^(e-2))=1 modulo2^e: if z=1 modulo2^k then z^2=1 modulo2^(k+1).
Hence f<=2^(e-2) and o/f>=4, again impossible.
The only remaining nontrivial moduli are odd prime powers,2,4.
On an odd prime power, a proper divisor f of phi(o) is at most phi(o)/2<o/2, forbidden by(1); hence f=phi(o).
For o2 this is immediate, and for o4 condition(1) forces f2=phi(4).
This proves(2).

Finally L159's actual Frobenius-orbit constraint says that w_o is a positive multiple of f_p(o) and at most phi(o).
Equations(1)--(2) therefore force w_o=phi(o).
The order1 orbit has size1 and its capacity is1.
No arbitrary finite-field array has been substituted for an actual root group in this implication.

For comparison, a general bound o/f_p(o)<=K only gives an individual support restriction.
If o has k>=1 odd prime divisors, Euler order divisibility and the common factor2 in the k odd prime-power totients give f_p(o)<=phi(o)/2^(k-1), and hence 2^(k-1)<=K.
This places no bound on the UNION of primes across different orders.
The positive result below uses the stronger classification at K<=2, not that invalid union inference.
L217's actual order15 already has ord_15(2)=4 and ratio15/4, illustrating a non-prime-power order once the ratio is relaxed; no sharp general-K transition is claimed.

<a id="prime-power-small-order-capacity"></a>
## 2. Small-order capacity and the elementary prime bound

Let S be any finite set of positive integers, each equal to1 or a prime power, with arbitrary positive real capacities

    0<w_a<=phi(a), W=sum_(a in S)w_a.

For an integer X>=1 let U_X be the weight of selected orders a<=sqrt(X), and let pi(y) count the rational primes at most y.
Then

    U_X <= 1+sqrt(X) pi(sqrt(X)).                        (3)

Indeed order1 contributes at most1.
For one prime q<=y, if q^e is its largest power at most y, then the total capacity of ALL its positive powers up to y is

    sum_(i=1)^e phi(q^i)=q^e-1<=y.

Any selected subset or smaller weights contribute at most this.
Summing over at most pi(y) primes proves(3), even if some selected orders exceed X.

The precise finite estimate used here is

    pi(y)<=7y/log y for every real y>=16,
    U_X<=1+14X/log X for every integer X>=256.          (4)

For completeness, write theta(y)=sum_(q<=y)log q.
Every prime in(2^(k-1),2^k] divides binomial(2^k,2^(k-1)), including k1.
This binomial coefficient is at most2^(2^k), so dyadic summation gives theta(2^k)<2^(k+1)log2, and therefore theta(y)<4y log2 for y>=2, exactly as in L159.
The primes up to sqrt(y) number at most sqrt(y); every remaining prime contributes more than(log y)/2 to theta(y).
Thus

    pi(y)<=sqrt(y)+2theta(y)/log y
          <sqrt(y)+8(log2)y/log y.

For y>=16, log y<=sqrt(y), as checked at16 and then by differentiating sqrt(y)-log y.
Hence sqrt(y)<=y/log y, and1+8log2<7 proves the first part of(4).
Set y=sqrt(X) for the second.
The constant7 is only a convenient rigorous upper bound; no asymptotic prime theorem is used.

<a id="prime-power-density-chain-capture"></a>
## 3. Positive weighted pair/triple density forces one prime-power chain

Retain S,w,W,X.
For each prime q put

    V_q=sum_(a in S, a=q^e<=X, e>=1)w_a,
    w_1=the selected weight at1, or0 when1 is absent.

Define G_X as the largest mass captured by ONE eligible prime-power chain, allowing order1:

    G_X=max({w_1} union {w_1+V_q:V_q>0}).

The maximum is well-defined, with G_X=0 when no order is at most X.
Whenever G_X>0, it is actually captured at n=1 or at the largest selected eligible power of one prime q.
That actual n is at most X, and every selected power of that same prime below it divides n.
Thus G_X<=H_X, where H_X is the unrestricted original capture peak on1<=n<=X.

With ordered, repeated-label pair and triple masses

    T_2(X)=sum_(a,b in S,lcm(a,b)<=X)w_a w_b,
    T_3(X)=sum_(a,b,c in S,lcm(a,b,c)<=X)w_a w_b w_c,

one has the finite inequalities

    T_2(X)<=G_X W+2U_X W,
    T_3(X)<=G_X^2 W+3U_X W^2.                           (5)

To prove them, any compatible pair involving two different nontrivial order primes has lcm equal to the product of those two orders; at least one must therefore be at most sqrt(X).
A compatible triple involving at least two different primes likewise has a pair of that kind and hence at least one small coordinate.
Any tuple containing order1 also has a small coordinate.
The only remaining tuples have all their labels on one prime-power chain, necessarily among its eligible orders.
Their total pair mass is at most sum_q V_q^2<=G_X sum_q V_q<=G_X W, and their triple mass is at most sum_q V_q^3<=G_X^2 W.
Counting all tuples with at least one small coordinate by the union bound gives2U_X W and3U_X W^2, respectively.
Double counting only enlarges these upper bounds.
No density is assigned to an arbitrarily chosen anchor.

Consequently, for0<delta<=1,

    T_2(X)>=delta W^2 => G_X/W>=max(0,delta-2U_X/W),
    T_3(X)>=delta W^3 => G_X/W>=sqrt(max(0,delta-3U_X/W)).
                                                               (6)

These are actual one-chain conclusions, stronger than merely a bound on an arbitrary composite time.
They require no bound on the initial UNION prime pool.
The triple implication also gives pair density at least delta because T_3<=W T_2, as every compatible triple has a compatible first pair.

For an explicit UNIFORM finite statement, fix C0>0,0<delta<=1 and suppose X<=C0 W.
Define

    Z=max(256,8C0/delta,exp(112C0/delta)),
    c(C0,delta)=min(delta/2,sqrt(delta)/(1+ceil(Z)))>0.    (7)

If either density premise in(6) holds, then ONE n<=X which is1 or a prime power captures at least c(C0,delta)W.
To check the large case X>=Z, equations(3)--(4) and W>=X/C0 give

    U_X/W<=1/W+14C0/log X<=delta/8+delta/8=delta/4.

Pair density therefore gives G_X/W>=delta/2.
Triple density implies that pair premise as just observed, so the same bound follows.
For X<Z, let V be the total mass of eligible orders<=X.
Since T_2<=V^2, pair density gives V>=sqrt(delta)W; the triple premise again supplies the pair premise.
The eligible set partitions into at most1+pi(X)<=1+ceil(Z) groups, namely order1 and each prime-power chain.
Their individual masses are each at most G_X, so G_X>=sqrt(delta)W/(1+ceil(Z)).
This proves(7), including small X, missing order1, empty individual chains and arbitrary weights subject to capacity.
No numerical value of the deliberately large constant was calculated.

There is a stronger asymptotic structural consequence.
On any sequence with fixed C0,delta, W->infinity and X<=C0 W, a positive pair or triple density forces X->infinity: eligible total mass is at most X(X+1)/2, whereas pair density requires it to be at least sqrt(delta)W.
Thus(4) gives U_X/W->0, and(6) implies

    liminf G_X/W>=delta under positive pair density,
    liminf G_X/W>=sqrt(delta) under positive triple density.
                                                               (8)

In particular an actual positive fraction of the selected mass lies in a SINGLE order-prime chain (plus possible order1), despite an unrestricted initial union of order primes.

<a id="prime-power-all-pairs-concentration"></a>
## 4. The all-pairs case concentrates almost all mass

Suppose every selected pair, INCLUDING its diagonal, has lcm<=X.
Then all selected orders are eligible.
If S={1}, n1 captures all W.
Otherwise let M be the largest selected nontrivial prime power and let q0 be its underlying prime.
At n=M, every selected q0-power and order1 returns.
For another prime q, write A_q for its largest selected power.
Then

    A_q<=M, A_q*M<=X,
    A_q<=min(M,X/M)<=sqrt(X).

Its ENTIRE selected chain has capacity at most A_q, by the telescoping totient sum used in(3).
Thus the unreturned mass at n=M is at most sqrt(X) pi(sqrt(X)), and

    h(M)>=W-sqrt(X)pi(sqrt(X)),
    H_X>=W-sqrt(X)pi(sqrt(X)).                          (9)

In particular, for X>=256 and X<=C0 W,

    h(M)/W>=1-14C0/log X.                              (10)

On any such sequence with W->infinity, the actual prime-power time M captures a fraction tending to1.
Equation(7) with delta1 separately handles EVERY finite member, so the asymptotic is not being used without a small-case bound.
The one-chain set in this conclusion has union support at most one, but that conclusion was derived from the efficiency/capacity/density conditions; it was not assumed from an individual support count.

<a id="efficient-two-actual-norm-income"></a>
## 5. Complete actual arithmetic income and near-one boundary

Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d, alpha a root, K=Q(alpha), and m=m(P)>0.
Let p be a GOOD prime.
Select a nonempty set S of COMPLETE occurring order groups, with all their actual original-root counts w_o, total W>=gamma d for fixed0<gamma<=1.
Assume every selected order satisfies o/f_p(o)<=2.
Section1 gives the prime-power classification and full capacities, so Sections2--4 apply to these actual inventories without constructing a new polynomial.

Suppose an integer1<=X<=C d has weighted pair density T_2/W^2>=delta>0 or triple density T_3/W^3>=delta, with fixed C>0,delta<=1.
Since X<=(C/gamma)W, equation(7) gives one actual n<=X, equal to1 or a power of ONE order prime, with captured original-root mass at least c(C/gamma,delta)W.
No such order prime equals the reduction prime p, so p does not divide n.

Retain the complete signed norm and all actual local depths:

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(ALL d original p-adic roots a_i)
                                      v_p(a_i^n-1).

The [C256 good-prime same-time floor](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) now gives, at this SAME n,

    log C_n>=A_p(n)>=eta d,
    eta=gamma c(C/gamma,delta)log2>0.                    (11)

Every unselected root, actual first/exceptional/deeper valuation and other-prime contribution remains on the left; prime-to-p time does not mean depth exactly1.
No different-time contributions are added.
The single auxiliary is the actual integer t^n-1 of full degree n<=Cd, content1 and squared coefficient norm2.
No rational coefficient or indexed-packet denominator arises, and the norm never changes to the smaller minimal field of alpha^n.

The accepted [L168 finite same-exponent criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) therefore gives STRICT m(P)>m0(C,eta)>0 at its exact original source-inspection scope.
Under the full all-pairs hypothesis one may use delta1, and along unbounded selected mass the prime-power certificate captures1-o(1) of W by(9)--(10).
Under positive pair density its asymptotic fraction is at least delta; under positive triple density it is at least sqrt(delta), by(8).

This is a proved conditional coverage bridge at the low-efficiency-ratio threshold2.
It does not prove that an arbitrary near-one input admits any good prime, positive-density selection or order-efficiency bound of this form.
In particular, on a hypothetical m(P)->0 sequence, no sufficiently late input can satisfy all the fixed C,gamma,delta hypotheses with o/f<=2.
This is an exclusion of that covered class, not existence or nonexistence of a near-one sequence.
Pri11's input in L168 retains its accepted statement/applicability boundary; no new original-source proof audit is asserted.

<a id="efficient-two-controls-and-limits"></a>
## 6. Genuine control, higher-ratio gate and author check

The actual reciprocal polynomial P(t)=t^2-3t+1 supplies a small positive control.
It is irreducible because its discriminant5 is not a rational square, its constant1 makes it a unit polynomial, and its larger root rho=(3+sqrt5)/2>1 proves nontorsion.
Its original degree is2 and total m=log rho>0.
At p2 the reduction t^2+t+1 is squarefree, with two roots of order3, f_2(3)=2 and ratio3/2<=2.
Thus W=d=2 and the one actual time n3 captures all original roots.

The complete norm can be checked exactly, without assuming minimal depth.
From alpha^2=3alpha-1 one obtains alpha^3-1=4(2alpha-1), and Norm(2alpha-1)=4-2*3+1=-1.
Hence the signed norm at3 is-16, C_3=16 and A_2(3)=4log2.
In the unramified local ring, 2alpha-1 is a unit, so each of the two roots has first valuation2, illustrating why the general lower floor in(11) must not be turned into an equality.
All full measure and original-degree costs of this control remain present; it is not a varying near-one family.

The argument does not solve the original conjunction for arbitrary fixed K>2.
The exact point where it stops is Section1: such inventories can have orders with several distinct primes, so compatibility of labels from different prime-power chains is no longer the disjoint-product condition used in(5).
A bound on the number of prime factors per order does not supply a bounded union or the small-coordinate decomposition.
No unproved induction or weighted transfer from Chen's cardinality theorem fills that gap.
C97 remains available when an ACTUAL bounded union is separately established; neither C83 nor L217 meets all the present low-ratio density hypotheses.

The author checked the K2 endpoint and o1/2/4 cases, full Frobenius group capacities, arbitrary smaller real capacities in the combinatorial theorem, exact prime-power telescoping, dyadic binomial constants, real y and small X endpoints, every ordered/repeated-label tuple and small-coordinate union bound, chains with no eligible orders, the actual maximizer time, both branches of the explicit uniform constant, unbounded-mass asymptotics, all-pairs concentration, and every original norm/degree/source boundary.
The complete fixed control was checked symbolically by the displayed degree-two relation.
No native mathematical program, new computation group or numerical search was performed.


<a id="efficient-two-entire-author-freeze"></a>
## Entire author freeze

2026-10-13T04:59.
The ENTIRE current draft is author-complete and held for a separately organized noncontributor review: original responsible question, bounded reuse/source and failed general-K transfer, Sections1--6/equations1--11, exact K2 classification, small-order capacity, prime bound, both density variants, explicit all-finite constant, one-chain asymptotics, all-pairs concentration, actual norm and measure interface, genuine control and remaining near-one limits.
The actual_income subagent authored every new proof step.
Root supplied the general inquiry, the request to check the density variant and an unused source lead, not a mathematical derivation or repair.
This is contributor checking only; no independent verdict or Claim adoption is asserted.
The reused working address D25 carries none of the former retired D25's scope, which remains entirely preserved in C98.
