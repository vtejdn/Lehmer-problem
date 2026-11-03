---
author: Yin
---
# Four-prime rows and the distinction between support and efficiency

Date: 2026-10-14T19:50.
Human author Yin.
Continuing algebraic inquiry under the resumed G0001 goal.

## Responsible question

The whole-reviewed C106 proves individual three-prime row capture and hence efficiency-eight conditional income.
Determine whether the analogous uniform oriented capacity row bound is actually false at four prime factors, or find a mechanism that extends it.
The three-shared-prime exponent grid and one external prime is the immediate discriminator, but a different useful construction is welcome.
Preserve any actual prime-counting lower premise and all finite ranges.
Distinguish an abstract support counterfamily from bounded actual o/ord_o(p) efficiency, fixed positive triple density and genuine polynomial realization.
A failed row bound alone decides none of those larger statements.

<a id="four-prime-reuse-and-source-scope"></a>
## Reuse, source scope and actual contributions

The strategy_critique AI authors this inquiry after its completed independent C105/J94 review.
Root supplied the question and the three-shared-prime diagnostic, not a counterexample, counting estimate, density argument or efficiency proof.
The author read the current [C106](Yin_C_G0106_v1.md#statement), [C94's earlier unrestricted row obstruction](Yin_C_G0094_v1.md#oriented-row-bound-failure), L395's individual-support cover failure and [L17's elementary prime-reciprocal divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence).
C106 controls individual support at most3; C94 does not keep the anchor's support bounded.
Neither supplies the four-prime counterexample below.
C96/C105 retain their different averaged/extremal domains and are not premises here.

No prime-counting lower theorem is assumed.
The needed subsequence lower growth is derived below from the already retained divergence of the prime reciprocal series, whose harmonic/Euler-product proof and DLMF27.11.E8 attribution are retained at [C220](Yin_C_G0220_v1.md#discriminant-divergence).
All further counting is elementary and explicit.
The earlier bounded support-row literature screens are reused; the author does not claim novelty or an exhaustive search.

The later efficiency check recognizes the classical multiplicative-order fact for prime divisors of Fermat numbers.
A targeted source search found and the author directly text-read the primary university-hosted [Trinity College Dublin Course374 Primality notes](https://www.maths.tcd.ie/pub/coursework/374/Primality.pdf), the101-page online PDF, Proposition4.7 proof, printed4--18/PDF99 and its continuation onto PDF100.
That proof gives ord_r(2)=2^(j+1) when r divides2^(2^j)+1.
The author/date of this online edition were not verified.
A Roma-hosted candidate endpoint returned404.
The checked TCD passage is attribution for the short order argument reproduced completely below; no prime-distribution theorem, whole-course audit, downloaded artifact, new source registration or external unproved premise is supplied.
The source's primality heuristics and later primality test are not used.

## Statement

Let omega(o) count DISTINCT prime factors.
Define the complete oriented row

    B_N^(4)(a)=sum_(1<=b<=a,omega(b)<=4,lcm(a,b)<=N)phi(b).

There is NO finite absolute K such that B_N^(4)(a)<=KN for all positive integers1<=a<=N with omega(a)<=4.
In fact the anchor in the construction always has exactly THREE prime factors, and every other selected label has exactly FOUR.

The proof specifies an increasing sequence of finite integer parameters R_m, anchors a_m and windows X_m=a_m R_m.
For each m>=1 it constructs a finite DISTINCT capacity array S_m containing a_m, with exact full weights w_o=phi(o), total W_m, and every selected label in the anchor's oriented compatible row.
It satisfies

    W_m>m X_m,    B_(X_m)^(4)(a_m)>m X_m,               (1)
    X_m/W_m ->0,
    H_(X_m)/W_m ->0,
    T_(X_m)/W_m^3 ->0,                                 (2)

where H and T are the original peak divisor mass and ordered repeated-label triple mass.
The triple mass is positive at every finite member.
Thus this is NOT a fixed-positive-density counterexample, despite the especially affordable window.
It also rules out a uniformly bounded number of divisor-set covers of these whole stars at times<=X_m, since each such time captures at most H_(X_m).

Furthermore the full inventories have no uniform order-efficiency bound for ANY common coprime base, even if the base varies with m.
Precisely, for every K there is m0 such that for all m>=m0 and all integers ell coprime to every label in S_m,

    max_(o in S_m) o/ord_o(ell)>K.                      (3)

This negative scope matters: the construction does not refute a fixed-efficiency theorem, a uniform MASS-AVERAGED short-pair estimate for individual support4, nonlinear positive-density capture, actual near-one coverage or G0001.
It supplies no irreducible polynomial realization, designated good prime, valuation depths or full original Mahler costs.
All assertions in(1)--(3) concern the explicitly defined integer capacity arrays.

## Argument

<a id="prime-weight-subsequence-without-pnt"></a>
## 1. A sufficient prime-weight subsequence from reciprocal divergence alone

For a prime r>=7 let L(r) be the unique integer with2^L(r)<=r<2^(L(r)+1), and for integer R>=7 put

    A(R)=sum_(7<=r<=R,r prime) L(r)^2.                  (4)

Then A(R)/R is unbounded.
Suppose instead that A(R)<=C R for every integer R>=7.
For every integer j>=3, all primes in[2^j,2^(j+1)) have L(r)=j, so their number is at most

    A(2^(j+1))/j^2 <= C 2^(j+1)/j^2.

Their reciprocal sum is at most2C/j^2.
Summing over j would make the prime-reciprocal series converge after removal of finitely many primes, contrary to the accepted L17 divergence.
The numerical series sum1/j^2 converges, for instance by1/j^2<=1/[j(j-1)] and telescoping for j>=2.
No prime-counting asymptotic or lower bound on every interval has been used.

Define R_0=6.
For each integer m>=1 let R_m be the LEAST integer R>R_(m-1) satisfying

    A(R)>675 m R.                                       (5)

Such an integer exists because removing finitely many arguments from an unbounded sequence of ratios leaves it unbounded.
This is an exact finite definition involving integer counts and powers only; no efficient search, numeric value or performed enumeration is claimed.
The sequence is strictly increasing and tends to infinity.

<a id="four-prime-finite-star-construction"></a>
## 2. Exact finite stars with a three-prime anchor

Fix any integer R>=7.
Let

    L=floor(log_2 R),
    E=1+ceil(log_2 R),   a=30^E,   X=aR.                (6)

Equivalently E is the least integer satisfying2^(E-1)>=R.
In particular L>=2 and E<=L+2.
For each prime7<=r<=R, independently select all pairs of integers

    0<=u<=floor(L(r)/3),
    0<=v<=floor(L(r)/6).                                (7)

Let w=w(r,u,v) be the LEAST nonnegative integer for which

    D=2^u 3^v 5^w>=r.

Since3^v<=2^(2v), the bounds in(7) give

    2^u3^v<=2^(2L(r)/3)<=r^(2/3)<r.

Thus w>=1, and minimality gives

    r<=D<5r.                                            (8)

We have u,v<=E-1.
Also5^(E-1)>=2^(E-1)>=R>=r, so w<=E-1.
Therefore D divides a and

    g=a/D=2^(E-u)3^(E-v)5^(E-w)

has all three exponents positive.
Define the selected neighbor

    b(r,u,v)=r g=a r/D.                                 (9)

It is an integer with exactly four distinct prime factors2,3,5,r.
The external prime r cannot equal the smooth number D, so (8) implies b<a.
As r is prime to a and g divides a,

    lcm(a,b)=a r<=aR=X.                                 (10)

Every selected neighbor is therefore in the claimed oriented row.
Distinct triples(r,u,v) give distinct labels: the unique external prime recovers r; unique factorization of D then recovers u,v,w.
None equals the anchor a.

Let S_R consist of a and ALL these b, with full integer capacities phi(o).
Since g has all three fixed prime factors,

    phi(g)=(4/15)g,
    phi(b)=(r-1)phi(g)
           >(4/75)a (r-1)/r >=(2/75)a.                 (11)

The number of choices in(7) is

    (floor(L(r)/3)+1)(floor(L(r)/6)+1)>=L(r)^2/18.

Thus their total weight, before even adding the positive anchor weight, is at least

    (a/675) A(R).                                      (12)

Write W_R for the whole selected mass.
At R=R_m, equations(5) and(12) give W_R>m aR=mX.
Since the whole selected set lies in the anchor's row, B_X^(4)(a)>=W_R>mX.
This proves(1) and the failure of every uniform four-prime row constant.
In contrast, C106's proved bound at individual support3 remains unaffected.

<a id="four-prime-capture-decay"></a>
## 3. The affordable window still captures a vanishing mass fraction

Group the neighbors by their external prime r, and denote that group's total weight by V_r.
Each label has b<=a and phi(b)<=b, and the number of labels for r is at most(L+1)^2.
Thus

    V_r<=a(L+1)^2.                                     (13)

The anchor weight is phi(a)<=a.
For any n<=X, a captured neighbor's external prime must divide n.
The number of distinct external primes dividing n is at most log_2 n<=log_2 X.
From(6), log_2 30<5 and E<=L+2 give

    log_2 X <5(L+2)+(L+1)=6L+11<=12L,

where L>=2 is used in the last inequality.
Therefore the peak mass obeys

    H_X<=a[1+12L(L+1)^2].                              (14)

On the sequence R=R_m, W_R>m aR, hence

    H_X/W_R < [1+12L(L+1)^2]/(mR) ->0.                 (15)

The limit follows from R_m->infinity and (log R)^3/R->0.
Also X/W_R<1/m.
These are actual inequalities for the finite capacity arrays, not a change of the time window or of their weights.
Any cover by k divisor sets at times<=X has total covered mass at most k H_X, so a cover of all S_R needs k>=W_R/H_X, tending to infinity.

<a id="four-prime-actual-triple-density-decay"></a>
## 4. Their exact triple density cannot stay positive

Let T_X use all ordered triples, including repeated labels, of S_R.
It is positive because the anchor's repeated diagonal is compatible.
We bound every possible compatible triple by the following union of three events.

First, a triple containing the anchor has total weight at most3a W_R^2.
Second, a triple having two neighbor labels with the SAME external prime has total weight at most

    3 W_R sum_r V_r^2
       <=3 a(L+1)^2 W_R^2,                             (16)

using(13).
These are upper bounds with harmless multiple counting.

For the remaining case, the three external primes r1,r2,r3 are distinct.
Each associated core g_i=a/D_i satisfies g_i>a/(5r_i)>=a/(5R).
The external primes are absent from all the cores, so

    lcm(b1,b2,b3)=r1 r2 r3 lcm(g1,g2,g3).

If all three external primes exceeded Y=(5R^2)^(1/3), this lcm would exceed (5R^2)*a/(5R)=aR=X.
Consequently any remaining compatible triple has an external prime at most Y.
Since Y<2R^(2/3), the total mass of all such small-prime groups is at most

    sum_(r<=Y)V_r <=2a R^(2/3)(L+1)^2.                 (17)

Only the trivial bound that there are at most Y positive integer candidates was used.
The weight of triples with a coordinate in these groups is at most three times(17) times W_R^2.
Combining all three events gives

    0<T_X/W_R^3
       <=[3a+3a(L+1)^2(1+2R^(2/3))]/W_R
       <[3+3(L+1)^2(1+2R^(2/3))]/(mR) ->0             (18)

on R=R_m.
Every compatible triple is accounted for, and no ordinary pair-density hypothesis was substituted for triple density.
The family therefore does not refute nonlinear fixed-positive-density capture, even though X/W_R->0 and H_X/W_R->0.
The mass-averaged short-pair ratio P_2(X)/(XW_R) has not been evaluated or shown unbounded by this row construction.

<a id="four-prime-efficiency-failure"></a>
## 5. The entire inventories necessarily escape every fixed efficiency bound

This scope check does not postulate an actual finite-field realization.
It proves that no choice of a common coprime integer base can make EVERY selected order uniformly efficient along the full family.

For each j>=2 choose any prime r_j dividing the integer2^(2^j)+1.
It is odd, and

    2^(2^j)=-1 mod r_j,
    ord_(r_j)(2)=2^(j+1),
    2^(j+1) divides r_j-1.                             (19)

Indeed the order divides2^(j+1) after squaring, but cannot divide2^j because -1 differs from1 modulo an odd prime.
Every divisor of2^(j+1) is a power of2, so the order is exact; Lagrange's theorem gives the last divisibility.
This is the classical short Fermat-divisor argument identified in the TCD passage above, repeated here in full.
It implies r_j>=2^(j+1)+1>5, without assuming that a Fermat number is prime or using a prime-progression theorem.

For all sufficiently large R_m, the external prime r_j occurs in the construction.
Use its selected pair u=v=0, so w is the least integer with5^w>=r_j and

    g=2^E3^E5^(E-w),    b=r_j g.

All core exponents are positive by Section2.
In particular phi(g) is divisible by2^(E-1).
Since R_m>=r_j>=2^(j+1)+1, we have E-1=ceil(log_2 R_m)>=j+2.
Hence

    gcd(phi(g),r_j-1)>=2^(j+1).                        (20)

For any integer ell coprime to b, Euler's theorem on the two coprime factors g and r_j gives

    ord_b(ell) divides lcm(phi(g),r_j-1).

Consequently

    b/ord_b(ell)
       >=[g r_j/(phi(g)(r_j-1))]gcd(phi(g),r_j-1)
        >2^(j+1).                                     (21)

For an arbitrary proposed fixed K, choose j with2^(j+1)>K.
Every sufficiently late inventory contains this label and violates the bound at EVERY common coprime base ell.
This proves(3), even if ell changes with m.
If a base is not coprime to all selected labels, the full inventory is already ineligible as a complete common good-prime root-order selection.
No conclusion is made about a smaller subinventory after discarding labels.

<a id="four-prime-method-boundary"></a>
## 6. What this decides and what must change next

The uniform capacity ROW method has an exact support threshold in the presently proved range: C106 supplies a constant at individual support3, while the present finite family refutes every such constant at support4.
Keeping the whole row and tuning constants cannot prove an individual-support4 extension.
A new averaged estimate, genuine positive-density localization, or additional ACTUAL efficiency/arithmetic structure would be a different proposition and remains possible.

The construction deliberately measures its missing hypotheses instead of treating them as unknown: its normalized triple density tends to0, and its full inventories have no fixed efficiency bound for any common coprime base.
Thus it does not refute an efficiency16 theorem merely because support4 would be the next necessary complexity class.
Nor does a heavy oriented row prove that the averaged short-pair constant fails on support4.
There is no actual polynomial, original degree assignment, norm/depth upper bound or total small Mahler measure in the construction.

The author checked the dyadic reciprocal-divergence implication, finite recursive choice of R_m, every exponent and divisibility bound, uniqueness of all labels, full phi values, the constants675 and12, the affordability and capture limits, complete repeated-label triple classification, the elementary order argument and its quantifiers over every common base.
No native computation, J program, numerical prime data, new accepted external theorem or global T/E/S/fixed material edit was performed.
Root supplied only the responsible question/diagnostic and received summaries; the counterexample, capacity/density bounds and efficiency proof are this author's contributions.
Independent whole review remains to be arranged by root.

<a id="four-prime-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T19:57.
ENTIRE author-complete artifact frozen for a noncontributor whole review: responsible question and exact reuse/source/contribution boundaries; Statement and full Argument; Sections1--6/equations1--21; the finite four-prime star, prime-reciprocal existence proof, affordable-window and capture limits, explicit vanishing triple density, and the all-common-base efficiency obstruction.
Every claimed negative conclusion and every unrefuted averaged/fixed-efficiency/near-one scope remain explicit.
The optional scoped material check returned checked1 and supplies no mathematical review.
No independent acceptance or Task completion is claimed.
Root may retain the entire actual original with its statement/argument anchors and arrange review of that fixed material.

## Fixed organization

The entire author-frozen original above is retained at its final actual scope, including all useful failed mechanisms, exact construction and limiting costs, source attribution and contribution accounts.
It awaits a separately organized noncontributor whole review; direct whole retention is not acceptance.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:59 |
| status | open |
| reason | Register this complete author artifact for independent whole review. Four-prime row failure and its measured density/efficiency limitations; no averaged-pair or fixed-efficiency countertheorem asserted. The original G0001 goal remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete four-prime oriented-row obstruction, capture/density decay and every-common-base efficiency escape. |
| argument | [Entire argument](#argument) | Complete finite construction, all bounds, prime-reciprocal implication, order argument and all scope limits. |
| dependency | [Prime-reciprocal divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Accepted elementary divergence, with its retained source scope. |
| dependency | [Three-prime positive boundary](Yin_C_G0106_v1.md#statement) | Actual proved row at support3, used only to state the exact contrast with the new support4 obstruction. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete four-prime oriented-row obstruction, capture/density decay and every-common-base efficiency escape. |
| argument | [Entire argument](#argument) | Complete finite construction, all bounds, prime-reciprocal implication, order argument and all scope limits. |
| dependency | [Prime-reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Accepted elementary divergence, with its retained source scope. |
| dependency | [Three-prime positive boundary](Yin_C_G0106_v1.md#statement) | Actual proved row at support3, used only to state the exact contrast with the new support4 obstruction. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0796_v1.md#four-prime-whole-independent-finding) | Entire actual statement/argument and all direct inputs, exact correction or construction boundaries and preserved source limits. |

### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete four-prime oriented-row obstruction, capture/density decay and every-common-base efficiency escape. |
| argument | [Entire argument](#argument) | Complete finite construction, all bounds, prime-reciprocal implication, order argument and all scope limits. |
| dependency | [Prime-reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Accepted elementary divergence, with its retained source scope. |
| dependency | [Three-prime positive boundary](Yin_C_G0106_v1.md#statement) | Actual proved row at support3, used only to state the exact contrast with the new support4 obstruction. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0109-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:11 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt R463 complete independent review of the actual four-prime row obstruction and all finite/density/efficiency boundaries. The constructed arrays have vanishing triple density and escape every common-base fixed efficiency bound, so the averaged and fixed-efficiency alternatives remain open. The unrestricted G0001 objective remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete four-prime oriented-row obstruction, capture/density decay and every-common-base efficiency escape. |
| argument | [Entire argument](#argument) | Complete finite construction, all bounds, prime-reciprocal implication, order argument and all scope limits. |
| dependency | [Prime-reciprocal divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Accepted elementary divergence, with its retained source scope. |
| dependency | [Three-prime positive boundary](Yin_C_G0106_v1.md#statement) | Actual proved row at support3, used only to state the exact contrast with the new support4 obstruction. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0796_v1.md#four-prime-whole-independent-finding) | Entire actual statement/argument and all direct inputs, exact correction or construction boundaries and preserved source limits. |
