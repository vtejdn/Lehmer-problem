---
author: Yin
---

# Individual two-prime order support and efficiency-four same-time income

Date: 2026-10-15.
Human author Yin.
Continuing author inquiry under the explicitly resumed G0001 goal.
This working material carries no independent review or adopted theorem.

## Responsible question and starting scope

Investigate whether fixed efficiency beyond two, positive compatible density and a degree-linear window force a positive mass of actual residue orders into a uniformly capturable structure.
Begin with the first non-prime-power regime, retaining Frobenius multiplicities, complete original roots and all norm costs.
Permit a structural leap or a sharp counterexample with its actual scope.
Initial inputs: C100, L395, C97, C83, L217 and the unchanged G0001 contract.

<a id="two-prime-short-pair-question"></a>
## Exact outcome sought and reuse boundary

The present inquiry asks for a uniform same-exponent root capture from positive ordered TRIPLE density when each actual order has bounded multiplicative complexity.
The old universal short-pair bound is false by [C96](Yin_C_G0096_v1.md#statement), while [L395](../ledger/Yin_L_G0395_v1.md#individual-support-star-cover-failure) refutes replacing a bounded UNION of primes by an individual support bound in a particular bounded-number-of-covers argument.
Neither result excludes a capacity-weighted ROW bound under a fixed individual support restriction.
A bounded cover and a bounded sum of capacities are different assertions.

The author read [C100](Yin_C_G0100_v1.md#statement), [C97](Yin_C_G0097_v1.md#statement), [C91's exact residual implication](Yin_C_G0091_v1.md#global-triple-short-pair-criterion), C94/C96, L395/L396, and [L217](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope).
The full norm interface is [L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), with actual group/depth inputs from [L159](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) and [C256](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail).
These are reused at their accepted scopes; the present paper does not independently re-audit them.

Before sustained proof work, a bounded source screen searched the local literature registry, bibliography and contents/audit text for weighted least-common-multiple bounds, individual prime support, oriented rows, two-prime orders and Carmichael efficiency, then searched the web using the corresponding phrases.
It located no exact applicable extension in the inspected results.
The C100 retained Chen lead remains a cardinality lead with its prior access limitation, not a newly read or adopted theorem.
The elementary order divisibility needed here is already used and proved at the required scope in C100.
No new external theorem, source acquisition, source-original proof review or novelty claim is a premise.
The search stops because the direct weighted row argument below supplies the needed restricted bound; it does not establish literature-wide absence.

<a id="two-prime-short-pair-statement"></a>
## Statement

Let omega(a) be the number of DISTINCT rational primes dividing the positive integer a, with omega(1)=0.
For any finite nonempty set S of positive integers with omega(a)<=2 for each a in S, assign arbitrary REAL capacities

    0<w_a<=phi(a),       W=sum_(a in S) w_a.

No common finite prime pool is required.
For real Y>=1 and integer X>=1, put

    P_2(Y)=sum_(a,b in S, lcm(a,b)<=Y) w_a*w_b,
    h(n)=sum_(a in S, a divides n) w_a,
    H_X=max_(integer 1<=n<=X) h(n),
    T_X=sum_(a,b,c in S, lcm(a,b,c)<=X) w_a*w_b*w_c.

All tuples are ORDERED; diagonals and every repeated label are included.
The proposed proved deductions in this author artifact are

    B_N^(2)(a):=sum_(1<=b<=a,omega(b)<=2,lcm(a,b)<=N)phi(b)
               <=128 N

for every integer N>=1 and 1<=a<=N with omega(a)<=2, together with

    P_2(Y)<=256 Y W,                                      (1)

and, for every fixed 0<delta<=1,

    T_X>=delta W^3  =>  H_X>=delta^2 W^2/(1024 X).          (2)

Zero weights may be included and then removed.
Neither (1) nor (2) asserts capture from ordinary pair density alone.
In particular pairwise compatibility is not silently substituted for the stated triple density.
The constants are explicit safe constants, without optimality claims.

For actual good-prime order groups, the same conclusion applies whenever EACH selected order has efficiency

    o/ord_o(p)<=4,                                         (3)

including the endpoint4, because (3) forces omega(o)<=2.
At fixed W>=gamma*d, X<=C*d and delta>0, it gives one exponent n<=C*d with full original local income at least

    eta*d,   eta=gamma^2 delta^2 log(2)/(1024 C)>0.          (4)

Here the actual polynomial is monic irreducible, nontorsion and a unit, p is prime to its polynomial discriminant, the selected groups are complete, all norms use the original field and all d roots, and the sole auxiliary is t^n-1 with full degree n, content1 and squared coefficient norm2.
The accepted L168 finite criterion then gives STRICT m(P)>m0(C,eta)>0.
No depth is replaced by its first floor in the original norm, and no different-time income is combined.

Finally allow an UNRESTRICTED actual selected inventory with the same fixed W>=gamma*d, X<=C*d and T_X>=delta W^3, and define epsilon as the fraction of its selected root mass carried by orders with omega(o)>=3.
Put kappa=delta-1+(1-epsilon)^3.
Whenever kappa>0, one same-time capture satisfies

    H_X>=kappa^2 W^2/(1024 X),

and its full local income is at least gamma^2 kappa^2 log2/(1024 C) times d.
Consequently any HYPOTHETICAL m(P)->0 sequence with actual coverage at fixed gamma,delta,C must have

    liminf epsilon>=1-(1-delta)^(1/3).

Every order counted in epsilon has efficiency>4, so the same lower bound holds for the fraction of selected root mass with efficiency>4.
This is a necessary escape under actual coverage, not a proof that the coverage or such a sequence exists.

The complete arguments and costs follow.
General fixed efficiency K>4, general individual support>=3, ordinary pair density, and automatic near-one coverage are not established.

<a id="argument"></a>
## Argument and complete controls

<a id="two-prime-elementary-capacities"></a>
## 2. Elementary capacity estimates

For every real y>0, let

    F(y)=sum_(q prime, k>=1, q^k<=y) phi(q^k).

Each prime power is a distinct positive integer, and phi(n)<=n.
Thus

    F(y)<=y^2.                                             (5)

For y<1 the sum is empty.
For y>=1, with m=floor(y), the larger sum over all positive integers is at most m(m+1)/2<=m^2<=y^2.
The same upper bound holds after excluding any prime set.
No prime-counting asymptotic or sparsity theorem is needed.

For any prime p and any h>0, the exact geometric totient sums give

    sum_(j>=1, p^j<=h) phi(p^j)<=h,
    sum_(j>=1, p^j>h) phi(p^j)/p^(2j)<=1/h.                (6)

For the first assertion, if p^J is the largest eligible power, the sum is p^J-1; an empty sum is zero.
For the second, let j0>=1 be the least integer with p^j0>h.
Then the sum equals p^(-j0), which is less than1/h.
In particular for each integer e>=1,

    sum_(j>e) phi(p^j)/p^(2j)=p^(-e-1).                  (7)

These statements retain all exponents and work also when h<1.

<a id="two-prime-oriented-row"></a>
## 3. Uniform capacity of the oriented compatible row

For integer N>=1 and 1<=a<=N with omega(a)<=2, define

    B_N^(2)(a)=sum_(1<=b<=a, omega(b)<=2,
                         lcm(a,b)<=N) phi(b).

Then

    B_N^(2)(a)<=128 N.                                    (8)

Write Q for the set of prime factors of a.
The sum is bounded by the following three types, which cover every b.
The possible repeated counting of b1 in the first two bounds would only increase the estimate; one may equivalently assign b1 to the first type.

**Type I: every prime factor of b belongs to Q.**
Apply [C97's finite oriented-star cover](Yin_C_G0097_v1.md#statement) to the finite set consisting of a and these b, at the SAME threshold N and anchor a.
Since |Q|<=2, at most (4*2+3)^2=121 actual integers n_j<=N cover the b by their divisor sets.
For Q empty use the direct singleton b1, or C97's r0 convention.
At each covering integer,

    sum_(b divides n_j) phi(b)=n_j.

Consequently this type contributes at most121N.
This is a local use of a FIXED anchor's own prime set, not a bounded-union assertion about the complete S in Section1.
The divisor-sum identity is the same elementary identity used in C91's full-divisor lower control.

**Type II: gcd(a,b)=1.**
The two restrictions imply

    b<=Y:=min(a,N/a)<=sqrt(N).

By the elementary bound for the totient sum over all integers, the contribution is at mostY^2<=N.
This includes prime powers and two-prime b; their individual prime restriction is unnecessary for this bound.

**Type III: b shares a prime with a but also has a prime outside Q.**
Because omega(b)<=2, it has a UNIQUE representation

    b=p^j q^k,  p in Q, q not in Q, j,k>=1.

There are at most two choices of the shared prime p.
Fix one, and write

    e=v_p(a)>=1,    a=p^e c,    p does not divide c,
    R=N/a>=1.

If 1<=j<=e, exact least-common-multiple factorization gives lcm(a,b)=a*q^k.
The conditions become

    q^k<=min(R,a/p^j).

Coprimality of p and q gives phi(b)=phi(p^j)phi(q^k).
By (5), this portion is at most

    sum_(1<=j<=e) phi(p^j) min(R,a/p^j)^2.                (9)

Put h=a/R>0.
Terms with p^j<=h contribute at most R^2 h=aR=N by the first part of (6).
Terms with p^j>h contribute at most a^2/h=aR=N by the second part of (6).
Extending the finite sums only increases them.
Thus (9) is at most2N, with no assumption on the relative sizes of a andR.

If j>e, exact factorization instead gives lcm(a,b)=c*b.
Hence

    b<=Y:=min(a,N/c).

Equations (5) and (7) bound this portion by

    sum_(j>e) phi(p^j) F(Y/p^j)
       <=Y^2 sum_(j>e) phi(p^j)/p^(2j)
       =Y^2/p^(e+1)
       <=N/p<=N.                                         (10)

The penultimate inequality uses Y^2<=a*(N/c)=p^e N.
The exclusion q not in Q can be dropped for this upper estimate; it is retained for the exact representation and factorization before estimating.
In particular no input denominator or change of an actual order is introduced.

For each p, the total TypeIII contribution is at most3N, so both choices contribute at most6N.
Adding Types I--III proves

    121N+N+6N=128N,

as claimed.
When a=1 TypeIII is empty; the same safe bound holds.
This proof bounds the SUM of all eligible capacities.
It does not produce a bounded number of divisor sets for TypeIII and therefore makes none of the false covering inferences excluded by L395.

<a id="two-prime-ordered-short-pairs"></a>
## 4. Ordered short pairs with every diagonal retained

Fix real Y>=1 and N=floor(Y).
If lcm(a,b)<=Y then both a,b<=N.
Terms with larger labels contribute zero.
Orient each remaining unordered off-diagonal pair toward its larger integer label; every diagonal is present once.
Precisely,

    P_2(Y)
      =2 sum_(a in S,a<=N) w_a
             sum_(b in S,b<=a,lcm(a,b)<=N) w_b
          -sum_(a in S,a<=N) w_a^2.

Using w_b<=phi(b), the row bound (8), and nonnegativity of the final square sum yields

    P_2(Y)<=256 N sum_(a in S,a<=N)w_a<=256 Y W.

This proves (1) on arbitrary positive REAL capacities, with orders outside the threshold and empty eligible sets handled.
For 0<Y<1 the left side is zero, which will be used separately below.
The proof does not assume a full divisor downset, full capacities or any global union-prime bound.

<a id="two-prime-triple-residual-transfer"></a>
## 5. Exact triple-density transfer without a scale loss

The mechanism is [C91's already proved conditional residual argument](Yin_C_G0091_v1.md#global-triple-short-pair-criterion), now supplied with (1) on this RESTRICTED class instead of its refuted universal antecedent.
For completeness the direct inequalities are retained.

For a,b in S put L=lcm(a,b) and

    U_X(a,b)=sum_(c in S,lcm(L,c)<=X)w_c.

When L>X this is zero.
Otherwise partition eligible c by the unique integer j for which lcm(L,c)=Lj.
It satisfies 1<=j<=floor(X/L), and c dividesLj.
Each bucket has total at most h(Lj)<=H_X.
Therefore

    U_X(a,b)<=min(W, X H_X/L).                            (11)

If T_X>=delta W^3, fix epsilon=delta/512>0 and split the ordered pairs at L<=epsilon W.
When epsilon W>=1, (1) bounds their probability mass P_2(epsilon W)/W^2 by256epsilon.
When epsilon W<1 there are no such pairs.
The remaining pairs each have U_X/W<=XH_X/(epsilon W^2).
Thus in both cases

    delta<=T_X/W^3
          <=256epsilon+XH_X/(epsilon W^2),

which gives (2), since 256epsilon=delta/2.
All repeated labels and all originally ineligible orders remain in their correct sums; no particular anchor is assigned an average.
Positive triple density ensures H_X>0.

In the regime X<=C0 W this is the explicit all-finite bound

    H_X>=delta^2 W/(1024 C0).

This conclusion needs triple density.
This argument supplies no implication from an arbitrary positive pair density to triple density.
In particular C100's pair-density theorem remains stronger on its own prime-power domain; that established result is not replaced by this extension.

<a id="efficiency-four-prime-support"></a>
## 6. Actual efficiency at most four implies individual support at most two

Let p be a prime, o>=1 be prime to p, and f=ord_o(p), with ord_1(p)=1.
Then

    omega(o)>=3  =>  o/f>4.                              (12)

This is an elementary order-divisibility consequence of the Chinese remainder decomposition and Euler's theorem, as used in C100.
Here is the complete needed proof.

If o is odd with s>=3 distinct prime factors, write it as a product of s distinct odd prime powers.
Each corresponding totient is even.
The order f divides the least common multiple of these totients, which is at most their product divided by2^(s-1): inductively lcm(x,y)<=xy/2 for even x,y.
The product is phi(o), so f<=phi(o)/4<o/4.

If o=2^e u is even and omega(o)>=3, then u has s>=2 distinct odd prime factors.
When e=1 the order modulo2 is1; hence f divides the least common multiple of the s odd-prime-power totients, which is at most phi(u)/2^(s-1)<=phi(u)/2.
Thus

    o/f>=4u/phi(u)>4.

When e>=2, the totient of2^e is also even.
There are s+1 even factors, so f<=phi(o)/2^s<=phi(o)/4<o/4.
This proves (12) in every case.
No cyclicity classification, unproved primitive-root distribution or analytic estimate is used.
Its contrapositive proves (3) implies omega(o)<=2, with a STRICT inequality in (12) permitting the endpoint4.

An initial diagnostic of the smaller regime f>o/4 was to classify the orders more finely.
That refinement is unnecessary for (1)--(4): the argument uses only individual support at most two and the existing upper capacity.
In particular it does not need to assert that every occurring Frobenius group has full phi(o) mass or to prove common-prime localization.

<a id="efficiency-four-actual-original-norm"></a>
## 7. Actual original norm, one exponent and the complete costs

Let P be an ACTUAL monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d>=2, with root alpha, K=Q(alpha), O0=Z[alpha], and m(P)=log M(P)>0.
Let p be a GOOD prime, meaning p does not divide disc(P).
Select COMPLETE occurring reduced-root order groups S.
Every actual order is prime to p and its weight w_o is the number of ALL original reduced roots of that order, with each irreducible reduction factor counted by its degree once.
Existing L159 gives

    1<=w_o<=phi(o),       W=sum_(o in S)w_o<=d.

Require omega(o)<=2 for every selected order; condition (3) is sufficient, not necessary.
Suppose fixed C>0 and 0<gamma,delta<=1 satisfy

    W>=gamma*d,   integer 1<=X<=C*d,   T_X>=delta W^3.     (13)

By (2), one actual n<=X has h(n)>=gamma^2 delta^2 d/(1024 C).
If needed replace n by the least common multiple of the selected orders actually captured at n.
This replacement divides n and retains EXACTLY those selected groups; the captured set is nonempty and all its orders are prime to p.
Thus one may take n prime to p without increasing n or changing the captured mass.
No new order or smaller polynomial is substituted.

Keep the full original signed norm and local income

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)v_p(C_n)
          =(log p)sum_(ALL d original p-adic roots alpha_i)
                                      v_p(alpha_i^n-1).

Every captured root has valuation at least1 at this SAME exponent, by the good-prime first-return floor of L74.
Hence

    log C_n>=A_p(n)>=h(n)log p
          >=[gamma^2 delta^2 log2/(1024 C)]d=eta*d.       (14)

All initial, exceptional and later depths remain on the left, including p2.
Prime-to-p n does not assert depth exactly1.
Every unselected original root and every other-prime nonnegative contribution stays in the full norm.
Nontorsion guarantees alpha^n-1 nonzero; no selected subnorm or sum of different-time incomes is used.

The actual auxiliary is the SINGLE t^n-1, with full degree n<=Cd, content1 and squared coefficient norm2.
There is no rational coefficient denominator, indexed weight denominator, latent matrix trace normalization, time inflation or removal of original embeddings.
A drop in the degree of alpha^n remains paid by the original norm tower in L168.
Its accepted finite criterion gives the STRICT conclusion

    m(P)>m0(C,eta)>0,                                    (15)

for precisely the class (13).
L168's Pri11 statement/applicability scope is inherited; its original source proof is not newly audited.
This theorem extends the actual efficient-order TRIPLE-density class from efficiency<=2 to efficiency<=4; it does not extend C100's separate pair-density conclusion, give automatic near-one coverage, or resolve unrestricted G0001.

<a id="two-prime-near-one-mass-escape"></a>
## 8. A necessary amount of higher-complexity mass under hypothetical near-one coverage

There is also a quantitative consequence when the actual selected inventory S in (13) has unrestricted order complexity.
Keep the actual fixed gamma,delta,C coverage, and let

    epsilon=(1/W)sum_(o in S,omega(o)>=3)w_o,  0<=epsilon<=1,
    kappa=delta-1+(1-epsilon)^3.

Let S_low be the subset with omega(o)<=2 and W_low=(1-epsilon)W.
The total weight of ALL ordered triples having at least one discarded label is exactly W^3-W_low^3.
Their compatible subcollection cannot have more weight.
Consequently

    T_low>=kappa W^3.                                    (16)

If kappa>0, then W_low>0 and its actual normalized density delta_low=T_low/W_low^3 lies in(0,1].
Applying (2) to S_low gives

    H_X>=delta_low^2 W_low^2/(1024 X)
        >=kappa^2 W^6/(1024 X W_low^4)
        >=kappa^2 W^2/(1024 X).                          (17)

Here the full-inventory H_X is at least its restricted counterpart.
All actual costs and the same-exponent norm transfer of Section7 apply unchanged, yielding eta>=gamma^2 kappa^2 log2/(1024 C).

Therefore, along ANY HYPOTHETICAL sequence of actual inputs with m(P)->0 and actual certificates satisfying fixed gamma,delta,C as in (13), necessarily

    liminf epsilon >= 1-(1-delta)^(1/3).                 (18)

Indeed a subsequence a fixed amount below that threshold would have kappa bounded below by a fixed positive constant; (15) would contradict m(P)->0.
Every order counted in epsilon has efficiency>4 by (12), so the same lower bound holds for the mass fraction of groups with efficiency>4.
The converse implication is not asserted: an order can have at most two prime factors and still have efficiency>4.

For delta1, (18) says epsilon tends to1; for small positive delta it is a fixed positive fraction.
This is a necessary MASS escape under ACTUAL positive triple-density coverage.
It does not prove that a near-one sequence exists or that the stated coverage is available for any input.
It is stronger than merely saying that at least one selected order must violate the old efficiency2 criterion.

<a id="two-prime-boundaries-and-checks"></a>
## 9. Relation to previous obstructions and author checks

The general C96 averaged counterfamily has no uniform individual support bound2; (1) is a restricted replacement, not a reversal of that result.
C98 refutes an unrestricted estimate with linear dependence on delta; (2) uses quadratic dependence and a different individual-support hypothesis.
L395's prime-packet example refutes a bounded number of divisor-set covers under an individual support restriction, but its X/W tends to infinity.
The present row proof never claims such a cover for varying external primes; it sums their actual capacities instead.
C97 is used only on one fixed anchor's OWN prime set, where its union hypothesis is true.

L217's fixed-prime family has individual support2 and efficiency15/4, but lacks positive fixed triple density on a fixed degree-linear window.
Its complete norm/depth costs and m(P)=Theta(d) remain unchanged.
Combining its retained H_X/d->0 with (2) would force its actual normalized triple density to vanish at each fixed C; this is a consistency consequence, not a new polynomial construction or near-one result.
C100's stronger prime-power pair-density and concentration statements also remain unchanged.

The author checked the full partition of b, uniqueness of the single shared prime in TypeIII, both exact lcm formulas, totient multiplicativity only at coprime primes, the y<1 endpoint in (5), both h<1 and h>=1 in (6), the exact tail p^(-e-1), the inequality Y^2<=p^eN, every diagonal in the oriented-pair identity, real thresholds and capacities, the epsilonW<1 residual case, strictness at efficiency4, all even/odd support cases, actual full groups and original norms, and the ordered deleted-triple mass in (16).
These are AUTHOR checks, not independent review.

The algebraic author supplied the row partition, geometric bounds, restricted pair theorem, efficiency implication, actual norm assembly and mass-escape deduction.
Root selected the inquiry and requested complete scope/cost checking after the author reported the candidate; root did not supply a proof step.
There has been no native mathematical program, computation group, numerical experiment, formal assistant run, new external theorem or source registration by this author.
General K>4 and general no-loss capture remain open; the research goal and execution authority remain with root.

<a id="two-prime-entire-author-freeze"></a>
## Entire author freeze for independent review

2026-10-14T19:19.
The ENTIRE present artifact is author-complete and frozen for a noncontributing review: exact question and bounded reuse/source screen; the Statement, Sections2--9 and equations(1)--(18); the uniform128N oriented capacity row,256YW ordered short-pair bound and1024-denominator triple capture; efficiency<=4 including its endpoint; complete actual original norm and auxiliary costs; the exact higher-complexity mass escape; source, contribution and failure boundaries.
At root's requested retention structure, the author added explicit Statement/Argument anchors and restated the already proved row, full-cost and mass-escape conclusions in that Statement, without changing any proof or scope.
The optional scoped material command returned checked1, which checks structure only and is not an independent mathematical verdict.
No global record or accepted Claim has been changed by the author.
Independent review and any later adoption remain separate from this author contribution.

## Fixed organization

The entire author original above is retained at its actual final freeze, including source searches, contributor accounts, unsuccessful methods and all limitations.
Author-stage wording records history.
This actual fixed artifact, including the exact statement and complete argument, awaits a separately organized noncontributor whole review.
Allocation asserts no accepted mathematics.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:22 |
| status | open |
| reason | Register the entire author-frozen statement and argument from the resumed parallel G0001 round for independent review of this actual fixed artifact. Preserve all hypotheses, failures, source limits and contributor accounts. No unrestricted gap, automatic near-one coverage or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Exact input](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:28 |
| status | proved |
| reason | Adopt the complete separately organized review of the actual fixed statement and entire retained original. Individual two-prime capacity rows, the efficiency-four triple-density class, full same-exponent norm income and the conditional higher-complexity mass escape are proved at their stated scopes. Ordinary pair-only capture, higher efficiency and automatic near-one coverage remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Exact input](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |
| review | [Actual whole review](../audits/reviews/Yin_R_G0796_v1.md#two-prime-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Dependency](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#two-prime-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact retained argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Exact retained dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#two-prime-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact retained argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Exact retained dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#two-prime-whole-independent-finding) | Complete actual statement, entire retained argument, every declared direct input and the precise source and scope limitations. |

### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact retained argument](#argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Finite oriented-star cover for each anchor's own at-most-two-prime pool. |
| dependency | [Exact retained dependency](Yin_C_G0091_v1.md#global-triple-short-pair-criterion) | Credited residual mechanism with the new restricted pair bound. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete actual root-count capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | All original roots and actual local depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure transfer. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0102-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |
