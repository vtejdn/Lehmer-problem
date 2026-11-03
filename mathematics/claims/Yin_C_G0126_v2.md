---
author: Yin
---
# Capture for complete layers of comparable prime products

Date: 2026-10-15.
Human author Yin.
The g_bridge_audit AI authors this new bounded leap after the complete C124 terminal-support proof was fixed.
At allocation C124 was under review; it has since been adopted with whole independent R479.
Root supplied the unrestricted target and the optional intersecting-family source lead, not a proof step for the layer argument below.

<a id="general-capture-responsible-question"></a>
## Exact unrestricted target

For a finite nonempty array of distinct positive integer orders with 0<w_o<=phi(o), write

    W=sum_o w_o,
    T_X=sum_(a,b,c: lcm(a,b,c)<=X) w_a w_b w_c,
    H_X=max_(integer 1<=n<=X) sum_(o divides n) w_o.

The triple sum is ordered and allows repeated labels.
For every fixed C>0 and delta>0, do constants B>=1 and c>0 exist such that integer 1<=X<=CW and T_X>=delta W^3 imply H_(floor(BX))>=cW?
All constants must be independent of support, degree, primes and exponents.
Alternatively seek a genuine capacity counterfamily with the SAME fixed C,delta and H_(floor(BX))/W->0 for every fixed B.
Neither a diverging pair-energy ratio nor a single finite failure of a sharper constant decides this target.

## Bounded reuse and limits

Read C96's exact full-squarefree pair-energy counterfamily and its missing positive-triple premise; C99's full-squarefree-threshold positive capture; C104's sharp product weak moment and paid finite envelopes; C105's exact full-ideal extremal reduction and proper-divisor witness; C108 v2's nested near-Cauchy counterexamples and excluded-prime deficit; C115's simultaneous compression/rounding at near-global fractional extremality; and C124's complete terminal-support proof, now adopted after R479.
None supplies an unrestricted bound, and the FALSE universal linear short-pair premise and strong-norm shortcuts remain excluded.

This inquiry will test a concrete new mechanism or family while retaining phi capacity, original W, fixed-positive delta, linear X and a truly fixed enlarged window.
No new independent review, new source theorem, native program or J is asserted.
Necessary developments and failed constructions belong directly below; useful existing proofs are cited rather than copied.

<a id="general-capture-working"></a>
## Working argument

No unrestricted conclusion at allocation.
The following is a complete restricted theorem and a concrete failed counterfamily, not an unrestricted resolution.
No native computation is needed.

<a id="general-capture-layer-statement"></a>
<a id="statement"></a>
## 1. Complete comparable-prime layers cannot yield the proposed counterfamily

Let P>=2 be real, let Q be any pool of m distinct primes in (P,2P], and choose 0<=k<=m.
For every k-element subset A of Q put o_A=product_(p in A)p.
Include ALL these distinct orders, with the SAME arbitrary real weight

    0<w<=min_(|A|=k) phi(o_A).

Write W=w binom(m,k), and define the ordered, repeated-label triple mass T_X and capture H_X exactly as in the responsible question.
The pool need not consist of all primes in its interval.

**Restricted theorem.**
For every fixed C>0 and 0<delta<=1 there is c(C,delta)>0 such that, on every such complete layer,

    1<=X<=CW,  T_X>=delta W^3  ==>  H_X>=c(C,delta) W.       (1)

Thus the enlargement can be B=1 on this class.
No bound on k or the union of primes is assumed.
The constant is existential, not an effective constant extracted below.

More precisely, uniformly in P, k, the pool, w and X satisfying the displayed conditions, along any sequence with

    m->infinity,  1<=k<=m-1,  1<=X<=CW,

one has

    T_X/W^3 -> 0.                                         (2)

The same finite capture conclusion holds when the layer weights have a fixed distortion bound Lambda>=1: all orders are present and there is w>0 with w<=w_A<=Lambda*w for every A, while individually w_A<=phi(o_A).
Its constants may depend on C, delta and Lambda.
This does not cover arbitrary thinning, zero weights, uncontrolled distortion, or a general mixture of layers.

These are actual integer orders with valid real Euler capacities; taking P to be an integer and w=P^k gives a nonempty integer-capacity example because p>P implies p-1>=P.
No actual irreducible polynomial realizing these capacities, no uniform Frobenius orbit divisibility, and no near-one realization is asserted.

<a id="general-capture-layer-probability"></a>
<a id="argument"></a>
## 2. Exact layer probability and variance

For Sections 2--4 take a nonendpoint layer 1<=k<=m-1, so m>=2.
Endpoint layers and empty prime pools are treated in Section 5.
Sample A_1,A_2,A_3 independently and uniformly from the k-subsets of Q.
Put j=m-k, U=|A_1 union A_2 union A_3|, and I=|A_1^c intersect A_2^c intersect A_3^c|=m-U.
This is exactly the original normalized mass law in the equal-weight model, including coincident labels.
Thus

    T_X/W^3 = Pr(lcm(o_A1,o_A2,o_A3)<=X).                  (3)

For each prime-coordinate i, its indicator of lying in all three complements has mean (j/m)^3.
For distinct coordinates i,l, their joint probability is

    [j(j-1)/(m(m-1))]^3 <= (j/m)^6                        (4)

when m>=2, including j=0 or1.
Hence these indicators have nonpositive pair covariances.
Complementing the indicators gives the same covariance for union membership.
Consequently

    E I=j^3/m^2,   E U=m-j^3/m^2,
    Var I=Var U<=min(E I,E U)<=min(j^3/m^2,3k).             (5)

The last bound uses the pointwise inequality U<=3k.
The m=0 and m=1 cases have only one order and will be handled directly, without these divisions by m.

We use only the elementary prime count already proved in [C100](Yin_C_G0100_v1.md#prime-power-small-order-capacity): pi(y)<=7y/log y for y>=16.
In particular, when P>=8,

    m<=pi(2P)<=14P/log(2P)<=14P/log P.                      (6)

There is no prime number theorem or uninspected asymptotic source dependency here.
Any sequence m->infinity necessarily has P->infinity.

<a id="general-capture-layer-time"></a>
## 3. Two different capacity bounds pay the time in the two regimes

First, for every k-set, phi(o_A)<=o_A<=(2P)^k.
Therefore w<=(2P)^k and X<=C(2P)^k binom(m,k).
As every prime in the union exceeds P, compatibility implies

    U<=L:=k+[k log2+log binom(m,k)+log C]/log P.            (7)

This is merely a real upper bound on the integer U; no rounding equality is claimed.
It is useful away from the almost-full layer.

For that latter regime retain the exact full product N=product_(p in Q)p.
If B is ANY j-element missing set, the capacity of its complementary order is

    phi(o_(Q\B))=phi(N)/product_(p in B)(p-1)
                 <=N/(P-1)^j.

The common weight is at most this capacity.
Thus

    W<=N binom(m,j)/(P-1)^j.

The exact triple lcm is N/product_(p in A_1^c intersect A_2^c intersect A_3^c)p.
Compatibility at X<=CW therefore implies

    product_(p in the common missing set)p
       >=(P-1)^j/[C binom(m,j)],
    I>=a:=[j log(P-1)-log binom(m,j)-log C]/log(2P).        (8)

Whenever a>0, (5) and Markov give Pr(compatible)<= (j^3/m^2)/a.
This is an original-time inequality with the full product N canceled exactly; replacing w by the much looser (2P)^k here would lose the needed information.
In particular a large total number of prime factors has not been treated as a free normalization.

<a id="general-capture-layer-asymptotic"></a>
## 4. Proof of the uniform vanishing statement

It suffices to show that from every sequence m->infinity one can extract subsequences on which the compatibility probability tends to zero, with every possible limiting value of k/m covered.
Indeed, a failure of (2) would provide a sequence with probability bounded below by some positive constant; the following subsequence argument contradicts that.
Pass to a subsequence k/m->alpha in [0,1].
All logarithms are natural.

### 4A. Positive fraction strictly below the full layer

If 0<alpha<1, use binom(m,k)<=2^m and (7) to obtain L=k+o(m), since log P->infinity.
Equation (5) gives

    (E U-k)/m -> (1-alpha)-(1-alpha)^3 >0,
    Var U<=3k<=3m.

Thus E U-L is bounded below by a positive multiple of m eventually.
Chebyshev implies Pr(U<=L)->0, and (7) proves the assertion.

### 4B. Sparse layer, including fixed k

Suppose alpha=0.
The elementary bound binom(m,k)<=(e m/k)^k and (6) imply

    L/k <=1+log(2e m/k)/log P+log C/(k log P)
          <=2+o(1),                                     (9)

uniformly for k>=1 along this subsequence: for sufficiently large P, m<=P, so log(2e m/k)<=log P+log(2e), and the final term is bounded above by max(log C,0)/log P.
Meanwhile (5) gives E U/k=3-3k/m+(k/m)^2 ->3.

If k->infinity, eventually E U-L>=k/2 and Var U<=3k, so Chebyshev yields Pr(U<=L)<=12/k->0.
If k stays bounded, pass to a constant positive integer k.
Eventually L<3k.
Whenever U<3k, two of the three sampled sets intersect.
For one pair E|A_i intersect A_l|=k^2/m, so a union bound and Markov give

    Pr(U<3k)<=3k^2/m ->0.                               (10)

Every sequence of integer k has a subsequence of one of these two types.
These alternatives cover alpha=0 without trying to use Chebyshev with a fixed nonvanishing variance bound.

### 4C. Almost-full layer

Suppose alpha=1 and write theta=j/m->0, with j>=1.
Define C_+=max(C,1).
The binomial bound gives

    a/j >=[log(P-1)-1+log theta-(log C_+)/j]/log(2P).      (11)

If theta>=P^(-1/2), then for large P the numerator in (11) is at least (1/2)log P-log2-1-log C_+.
Hence a/j>=1/4 eventually, and

    Pr(compatible)<=4 theta^2 ->0.                       (12)

If theta<P^(-1/2), use j>=1, theta>=1/m, (6), and P-1>=P/2.
With D_C=log28+1+log C_+ we obtain

    a/j >=[log log P-D_C]/log(2P)>0                     (13)

eventually.
Therefore

    Pr(compatible)
      <=theta^2 log(2P)/(log log P-D_C)
      <=log(2P)/[P(log log P-D_C)] ->0.                   (14)

Both alternatives have positive a for all sufficiently large parameters, as required for Markov.
Switching between them causes no gap: the displayed bounds tend to zero in each case.
This includes fixed j and very slowly growing j.
Together 4A--4C prove (2).

<a id="general-capture-layer-finite"></a>
## 5. All-finite capture and bounded distortion

By uniform (2), for fixed C,delta there is an integer M(C,delta)>=2 such that no model with m>=M and 1<=k<=m-1 can have T_X>=delta W^3 at X<=CW.
Otherwise selecting one violating model for every increasing lower bound on m contradicts (2).
For m<M there are at most 2^m<=2^M labels.
Positive T_X means some selected order o_A<=X.
At that ACTUAL integer time,

    H_X>=w=W/binom(m,k)>=2^(-M) W.                       (15)

When k=0 or k=m there is just one order (also for m=0 or1); positive triple mass implies it is eligible, so H_X=W.
Thus (1) holds with c=2^(-M), including small P, small X, all real capacities, the empty prime pool with its order1, and both endpoint layers.
The order inventory itself is never empty because its full layer contains binom(m,k)>=1 labels.
If delta>1 the premise is impossible; the theorem was stated on its meaningful range.

For bounded distortion take w=min_A w_A, so w<=min_A phi(o_A) and w<=w_A<=Lambda*w.
Let d_X denote the UNIFORM probability in (3), on the same pool and layer.
The original total and triple masses obey

    w binom(m,k)<=W<=Lambda*w binom(m,k),
    T_X/W^3<=Lambda^3 d_X,
    X<=C Lambda*w binom(m,k).                            (16)

Apply the equal-weight result with parameters C Lambda and delta/Lambda^3.
A positive weighted density therefore bounds m in the nonendpoint layers by an M depending only on these parameters.
Any eligible order then has weight at least w>=W/[Lambda binom(m,k)], so

    H_X>=2^(-M) W/Lambda.                                (17)

This argument preserves the original weighted law by paying its explicit domination factor; it does not silently replace that law by a product measure.
For arbitrary uncontrolled weights (16) supplies no uniform constant.

<a id="general-capture-layer-scope"></a>
## 6. What this discriminator settles and what it does not

The attempted counterfamily was a complete fixed-cardinality layer of products of comparable large primes, hoping that a triple union could fit within a mass-linear window while no single short multiple captured a positive fraction.
The capacity/time calculation defeats that construction: away from the full layer, a typical three-fold union is too large; near the full layer, the full-product complement cost forces an atypically large three-fold missing intersection.
Fixed positive density actually bounds the prime pool on this class, without assuming a bounded prime pool at input.

The class permits unbounded k before density is imposed, and it is not a divisor ideal or a multiplicative weight profile.
The conclusion is a direct original-mass capture, not a repetition of an abstract unbounded indicator.
It does NOT imply any inclusion between this class and C124's bounded terminal-remainder class: these are different hypotheses, and no separation example is claimed.
The full Euler weights phi(o_A) on a layer are not covered uniformly merely because the primes lie in (P,2P]; their ratio can grow with k.
Arbitrary subfamilies, zero weights and mixtures can change both the law and the relevant capacity estimate; no extension to them has been proved.

For an ACTUAL monic irreducible nontorsion integer-unit polynomial F of original degree d, root alpha and field K=Q(alpha), a good prime p and COMPLETE selected root groups must really have this full-layer form (or the declared bounded distortion) to use (1).
If their actual W>=gamma*d with fixed gamma>0, integer X<=C*d and T_X>=delta W^3, use the proved capture constant c(C/gamma,delta), or c(C/gamma,delta,Lambda).
The captured original integer time n<=X then gives the existing [C256 original-root interface](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail),

    D_n=Norm_(K/Q)(alpha^n-1)=Res(F,t^n-1),
    C_n=|D_n| in Z_(>0),
    log C_n>=(log p)v_p(C_n)>=gamma*c*log2*d.              (18)

Every original root and every nonnegative local-depth contribution remains in that full norm; no powered field or thinned multiplicity is substituted.
The auxiliary t^n-1 has original degree n<=Cd, content1 and squared coefficient norm2.
[L168's existing finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), at its accepted Pri11 statement/applicability scope, then gives its strict Mahler lower bound for fixed C,gamma,delta and (when used) Lambda.
This is only a conditional application of the existing interfaces.
This draft does not construct that polynomial class or replace the missing automatic coverage; abstract capacity arrays are not near-one inputs.

The unrestricted target remains open.
In particular this proof supplies neither a general weak fractional moment estimate nor a positive-density-to-intersecting-subfamily theorem, and does not preserve capture under compression.
C105's universal-energy extremal reduction does not preserve the starting total mass, triple density or actual polynomial realization.
It therefore does not by itself transport this original-mass positive-density capture problem to a full divisor ideal; no simultaneous monotonicity of energy and capture is asserted here.
C96's pair divergence still omits the positive triple premise; C99 addresses its own full threshold inventory, not arbitrary restrictions.
Those failed shortcuts remain excluded.

<a id="general-capture-source-boundaries"></a>
## 7. Failed intersection transfers and source limits

This author directly inspected the publisher text of Arocha--Bracho--Montejano, *Complex Homothetic Sections and Projections Through a Helly Type Theorem for Cosets of S1*, Discrete and Computational Geometry 74 (2025),805--813, [DOI10.1007/s00454-024-00679-1](https://link.springer.com/article/10.1007/s00454-024-00679-1): Theorem1.2, Lemma3.2 and its proof, and Theorem3.3.
The displayed Helly conclusions concern nonempty intersections of pairwise intersecting cosets of closed subgroups of the circle, or finite families of integer cosets.
They supply neither a bounded positive return time nor a weighted positive-density conclusion.
In our setting all unrestricted return subgroups o*Z already intersect at0; the useful event is a positive return at most X.
Truncating to {n:1<=n<=X,o divides n} does not preserve the coset domain.
Thus no result of this paper is imported as a premise or represented as solving the time constraint.
This is a negative applicability screen, not a full-paper proof audit.

Root also suggested missing-prime-set intersection and supplied primary leads to [regular 3-wise families](https://sites.math.rutgers.edu/~narayanan/pdf/regular_3_families.pdf), [symmetric 3-wise families](https://sites.math.rutgers.edu/~narayanan/pdf/symmetric_3_families.pdf), and [arXiv2112.08685](https://arxiv.org/abs/2112.08685).
The separately assigned f agent screened their exact hypotheses and root relayed the finding that none supplies the positive-density and heterogeneous-weight transfer needed here.
This draft does not import their theorems or claim to have independently audited those papers.
The actual missing interfaces remain explicit: positive density of compatible triples does not itself assert compatibility for EVERY triple of a positive-mass subfamily; the Euler-capacity law is not a common-parameter Boolean product measure; and even a qualitative intersection needs its original numerical product/time cost.
Sections 2--5 instead prove their needed uniform-layer probability estimates directly, without any intersecting-family theorem.

<a id="general-capture-layer-author-freeze"></a>
## Author check and frozen scope

2026-10-15T08:14.
The g_bridge_audit author freezes this ENTIRE draft for separate retention and whole review.
The actual result is Sections1--5: complete comparable-prime layers with equal or uniformly comparable positive weights, uniform vanishing of triple density for nonendpoint layers with unbounded pool, and original-time B=1 capture for every finite member under fixed positive density and linear time.
Section6 retains the conditional actual-polynomial norm/cost interface and precise unresolved general scope.
Section7 retains the useful failed transfers and their source-inspection limits.
Root supplied the responsible general question and optional source lead, and suggested orienting the title toward the actual restricted result; it supplied no proof step in this layer theorem.
The f agent's separate source screen is not participation in this proof; any subsequent mathematical review must record its actual relationship and exact fixed inputs.

Author self-check covered the original equal-weight law and its bounded-distortion domination, negative covariances, the fixed-k collision case, both near-full Markov thresholds and their eventual positivity, real P and capacities, C<1, m=0/1, k=0/m, integer time, all-finite extraction, and the original-field norm, degree and coefficient costs in the conditional application.
The exact primary source used as a mathematical dependency is only the already proved elementary prime estimate in C100; the conditional application additionally uses L74 and L168.
The comparison sources in Section7 are not proof inputs.
`material.py check` returned checked1 for this draft before the freeze paragraph; this is structural evidence only.
No numerical experiment, J, independent review or unrestricted capture conclusion is claimed.

## Version 2 comparison-scope correction

2026-10-15T08:25.
Separate whole review of the actual v1 identified an unsupported comparison in Section6: the cited C105 reduction does not establish the asserted simultaneous increase of energy and capture.
Preserve v1 and its actual review finding.
This version narrows that sentence to C105's explicit non-preservation of total mass, triple density and actual polynomial realization.
No replacement monotonicity theorem is assumed.
The complete-layer theorem, all18 equations, proofs, actual norm consequence and dependencies are unchanged.
The original author freeze above remains a historical account; this correction does not retroactively alter its inspection.
Root implemented the review's scope correction without supplying a new proof step.
The actual v2 requires its own complete review finding.

## Fixed organization

Retain the complete author account: general question and reuse boundaries, the complete comparable-prime layer theorem, exact original law and capacities, three uniform asymptotic regimes, finite capture and bounded distortion, conditional full-norm consequence, negative source-applicability screen, useful failed counterfamily and author freeze.
Root supplied direction and an optional source lead, not a proof step.
Separate actual whole review is pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T08:25 |
| status | open |
| reason | Retain the complete v1 mathematics with its unsupported C105 comparison precisely narrowed; separate whole review of this actual v2 is pending. Retain original-window capture for complete comparable-prime layers with equal weights or fixed weight distortion. Their nonendpoint growing-pool models lose positive triple density at a mass-linear time. General thinned, mixed or uncontrolled-weight inventories and actual good-prime coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete-layer capture](#statement) | Entire equal-weight and bounded-distortion theorem, uniform nonendpoint density vanishing and exactly conditional actual-polynomial consequence. |
| argument | [Entire layer argument](#argument) | Complete Sections1--7, all displayed equations, every subsequence regime, finite endpoint cases, exact source/reuse boundaries, author check and failed general shortcuts. |
| dependency | [Elementary prime-count bound](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16, hence the stated comparable-prime pool bound for P>=8. |
| dependency | [Full original local norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups, all original roots and depths at the one captured time. |
| dependency | [Original-degree finite income](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual W>=gamma*d and X<=C*d application with full signed norm, original degree and auxiliary cost; no actual class existence inferred. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T08:29 |
| status | proved |
| reason | Adopt R481 actual v2 whole noncontributor review, preserving its v1 comparison-scope finding and this version's precise correction. Complete comparable-prime layers with equal or fixed-distortion weights have original-window positive capture; nonendpoint growing pools lose positive triple density. Arbitrary thinning, uncontrolled weights and actual coverage remain outside this result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete-layer capture](#statement) | Entire equal-weight and bounded-distortion theorem, uniform nonendpoint density vanishing and exactly conditional actual-polynomial consequence. |
| argument | [Entire layer argument](#argument) | Complete Sections1--7, all displayed equations, every subsequence regime, finite endpoint cases, exact source/reuse boundaries, author check and failed general shortcuts. |
| dependency | [Elementary prime-count bound](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16, hence the stated comparable-prime pool bound for P>=8. |
| dependency | [Full original local norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups, all original roots and depths at the one captured time. |
| dependency | [Original-degree finite income](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual W>=gamma*d and X<=C*d application with full signed norm, original degree and auxiliary cost; no actual class existence inferred. |
| review | [Actual v2 whole finding](../audits/reviews/Yin_R_G0798_v1.md#complete-layer-v2-whole-independent-finding) | Complete actual corrected statement/proof, all18 equations, finite and limit cases, three direct inputs, source boundaries and v1 comparison history. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire equal-weight and bounded-distortion theorem, uniform nonendpoint density vanishing and exactly conditional actual-polynomial consequence. |
| argument | [Argument](#argument) | Complete Sections1--7, all displayed equations, every subsequence regime, finite endpoint cases, exact source/reuse boundaries, author check and failed general shortcuts. |
| dependency | [Dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16, hence the stated comparable-prime pool bound for P>=8. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups, all original roots and depths at the one captured time. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual W>=gamma*d and X<=C*d application with full signed norm, original degree and auxiliary cost; no actual class existence inferred. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#complete-layer-v2-whole-independent-finding) | Complete actual corrected statement/proof, all18 equations, finite and limit cases, three direct inputs, source boundaries and v1 comparison history. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire equal-weight and bounded-distortion theorem, uniform nonendpoint density vanishing and exactly conditional actual-polynomial consequence. |
| argument | [Exact retained argument](#argument) | Complete Sections1--7, all displayed equations, every subsequence regime, finite endpoint cases, exact source/reuse boundaries, author check and failed general shortcuts. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16, hence the stated comparable-prime pool bound for P>=8. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups, all original roots and depths at the one captured time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Conditional actual W>=gamma*d and X<=C*d application with full signed norm, original degree and auxiliary cost; no actual class existence inferred. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#complete-layer-v2-whole-independent-finding) | Complete actual corrected statement/proof, all18 equations, finite and limit cases, three direct inputs, source boundaries and v1 comparison history. |

### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire equal-weight and bounded-distortion theorem, uniform nonendpoint density vanishing and exactly conditional actual-polynomial consequence. |
| argument | [Exact retained argument](#argument) | Complete Sections1--7, all displayed equations, every subsequence regime, finite endpoint cases, exact source/reuse boundaries, author check and failed general shortcuts. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16, hence the stated comparable-prime pool bound for P>=8. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups, all original roots and depths at the one captured time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Conditional actual W>=gamma*d and X<=C*d application with full signed norm, original degree and auxiliary cost; no actual class existence inferred. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g126-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
