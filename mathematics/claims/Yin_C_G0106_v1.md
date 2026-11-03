---
author: Yin
---
# Individual higher-prime order geometry beyond efficiency four

Date: 2026-10-15.
Human author Yin.
Continuing algebraic investigation under the explicitly resumed G0001 goal.

## Responsible question

The whole-reviewed [C102](Yin_C_G0102_v1.md#statement) controls individual two-prime orders and actual efficiency at most four.
Seek a genuine advance beyond that boundary: individual three-prime support, a paid hierarchy of low efficiency classes, or another algebraic mechanism using actual root-order data.
The earlier shared finite prime-pool result and unrestricted short-pair failures must retain their distinct scopes.
Follow a promising leap if the fixed row method fails, and preserve its full proof or decisive obstruction.
A density result still needs actual near-one coverage to address the original G0001 objective.

<a id="three-prime-reuse-and-scope"></a>
## Reuse, source scope and method change

The delegated strategy_critique AI authors this continuation.
It authored C102; root supplied this inquiry and coordinated independent work, but did not supply the proof below.
The author read the actual selected C102 statement/argument, [C97's finite anchor-star cover](Yin_C_G0097_v1.md#statement), [C100's elementary prime estimate](Yin_C_G0100_v1.md#prime-power-small-order-capacity), C91's residual transfer and the fixed L395/C96 boundaries.
C104 and the continuing correlated fractional inquiry were read as parallel context only.
Neither a product-envelope theorem nor an unreviewed correlated extremum is a premise here.

The prior source screen for individual-support weighted rows is retained in C102.
A bounded follow-up searched local literature contents/source audits and the web for three-prime least-common-multiple capacity rows and weighted totient sums; no exact applicable statement was located in the inspected results.
No new external source theorem or acquisition is used, and no absence or novelty claim is made.
The only additional estimate beyond the C102 mechanism is the elementary prime-power capacity bound obtained from C100's already retained proof of pi(y)<=7y/log y.
In particular no prime-number theorem is needed.

The new difficulty is a neighbor with TWO prime factors shared with the anchor and ONE new prime.
A crude y^2 bound alone leaves a logarithmic two-dimensional divisor-grid cost.
The logarithmic saving in the actual prime-power capacity pays that cost.
This is a capacity sum argument, not a claim that the varying-prime neighbors admit a bounded number of divisor-set covers.
Every original order and original coefficient/root cost is retained at the arithmetic application.

## Statement

Write omega(a) for the number of DISTINCT prime factors of a, with omega(1)=0.
For integer N>=1 and 1<=a<=N satisfying omega(a)<=3, define

    B_N^(3)(a)=sum_(1<=b<=a,omega(b)<=3,lcm(a,b)<=N)phi(b).

Then

    B_N^(3)(a)<=8192 N.                                  (1)

Consequently, for any finite nonempty capacity array on distinct positive integer orders with EACH omega(a)<=3 and arbitrary REAL weights0<w_a<=phi(a), put

    W=sum_a w_a,
    P_2(Y)=sum_(a,b,lcm(a,b)<=Y)w_a w_b,
    h(n)=sum_(a|n)w_a,
    H_X=max_(integer1<=n<=X)h(n),
    T_X=sum_(a,b,c,lcm(a,b,c)<=X)w_a w_b w_c.

All tuples are ordered, with every diagonal and repeated label.
For real Y>=1,

    P_2(Y)<=16384 Y W.                                    (2)

For integer X>=1 and0<delta<=1,

    T_X>=delta W^3 => H_X>=delta^2 W^2/(65536 X).           (3)

There is NO bound on the UNION of primes, their sizes, or the exponents.
No ordinary pair-density-to-capture theorem is asserted.
Zero weights can be removed.

For an ACTUAL monic irreducible nontorsion integer-unit polynomial P of ORIGINAL degree d, good prime p not dividing disc(P), and selected COMPLETE actual order groups of mass W>=gamma*d, condition o/ord_o(p)<=8 on each selected order implies omega(o)<=3, including the endpoint8.
Under X<=C*d and the same fixed positive triple density, one actual n<=C*d has FULL original local norm income at least

    eta*d, eta=gamma^2 delta^2 log2/(65536 C)>0.             (4)

The accepted L168 criterion therefore gives STRICT m(P)>m0(C,eta)>0 for this stated class.
All original roots, higher depths, powered-degree losses and the full single auxiliary t^n-1 are retained.

For an unrestricted actual selected inventory with the same fixed gamma,delta,C coverage, let epsilon be its mass fraction carried by orders with omega(o)>=4, and put kappa=delta-1+(1-epsilon)^3.
If kappa>0 then H_X>=kappa^2 W^2/(65536 X), with the analogous full income.
Along ANY HYPOTHETICAL m(P)->0 sequence with that actual coverage,

    liminf epsilon>=1-(1-delta)^(1/3).                    (5)

Every such higher-support order has efficiency>8.
This is a necessary mass escape under actual coverage, not automatic coverage, existence of a near-one sequence, general fixed-efficiency capture, or resolution of G0001.
The constants are deliberately safe and are not claimed sharp.

## Argument

<a id="prime-power-capacity-log-saving"></a>
## 1. Prime-power capacity with its elementary logarithmic saving

For real y>0 let

    F(y)=sum_(q prime,k>=1,q^k<=y)phi(q^k).

Set F(y)=0 for y<1.
For y>=1,

    F(y)<=y^2,
    F(y)<=14 y^2/log(2y).                                (6)

For the first bound, prime powers form a subset of the positive integers and sum_(n<=y)phi(n)<=floor(y)(floor(y)+1)/2<=y^2.
For each prime q<=y, summing all eligible powers gives q^e-1<=y.
Hence F(y)<=y*pi(y).
C100's fully retained elementary dyadic/binomial argument gives pi(y)<=7y/log y for y>=16.
Since log(2y)<=2log y on that range, the second bound follows with14.
For1<=y<16 the first bound implies it because log(2y)<log32<14.
Thus (6) holds at every needed real argument without an asymptotic or uncharged small range.

We also reuse the exact geometric identities, valid for every prime p and real h>0,

    sum_(j>=1,p^j<=h)phi(p^j)<=h,
    sum_(j>=1,p^j>h)phi(p^j)/p^(2j)<=1/h,
    sum_(j>e)phi(p^j)/p^(2j)=p^(-e-1) for e>=1.           (7)

They follow by summing phi(p^j)=p^j-p^(j-1).
They include empty ranges and h<1.
In particular, for any A,R>0 and any prime p,

    sum_(j>=1)phi(p^j) min(R,A/p^j)^2<=2 A R.             (8)

Split at p^j<=A/R and use the first two parts of (7).
Truncating the exponent range only lowers the left side.

<a id="two-prime-grid-logarithms"></a>
## 2. Two-prime exponent-grid estimates

Let p,q be DISTINCT primes and let D range over ALL numbers p^u q^v with u,v>=0.
Unique factorization prevents repeated labels.
For every real Z>=1,

    sum_(D<=Z) D/log(2D)<= (16/log2) Z,
    sum_(D>Z) 1/D <= (12/log2) log(2Z)/Z.                 (9)

For the first estimate, the shell2^k<=D<2^(k+1), k>=0, has at most2(k+2) labels: u has at most k+2 possible values because p>=2, and for each fixed u the permitted q^v lie in a half-open interval of ratio2, containing at most two powers.
Each term D/log(2D) is at most2^(k+1)/[(k+1)log2].
Thus one shell contributes at most (8/log2)2^k.
Sum the full shells up to k=floor(log_2 Z), permitting excess labels in the last shell.
Their geometric sum is less than2Z, giving the first assertion.

For the second estimate, shell2^k Z<=D<2^(k+1)Z contains at most2(log_2 Z+k+2) labels by the same argument.
A label contributes at most1/(2^k Z).
Summing all k>=0 gives

    (4log_2 Z+12)/Z
       <=12(1+log_2 Z)/Z
        =(12/log2)log(2Z)/Z.

Including a possible D=Z only enlarges this bound.
The sums of2^-k and k2^-k are the elementary geometric sums2 and2.
These estimates may be applied to a finite divisor grid by enlarging it to this infinite positive grid; no assumption about irrational distribution of logarithms is used.

<a id="three-prime-hard-two-shared-row"></a>
## 3. The new row type: two shared primes and one external prime

Fix integer N>=1, 1<=a<=N, and two distinct primes p,q dividing a.
Write

    a=p^e q^f c,   e,f>=1,  gcd(c,pq)=1,   R=N/a>=1.

Consider only neighbors

    b=p^j q^k r^l,  j,k,l>=1, r prime not dividing a,
    b<=a, lcm(a,b)<=N.

Their TOTAL phi(b) is at most805N.
The cases below partition them by whether j exceeds e and whether k exceeds f.
The extra prime r is kept outside a for the exact lcm and totient factorizations; it may then be included in the larger F sums when taking an upper bound.

**Both shared exponents below the anchor.**
Suppose j<=e and k<=f.
Put A=p^e q^f and g=p^j q^k, so the complementary divisor D=A/g is p^(e-j)q^(f-k).
Then

    lcm(a,b)=a r^l,
    r^l<=min(R,a/g)=min(R,cD),
    phi(g)<=g=A/D.

Thus the sum in this case is bounded by

    A sum_(D|A) F(min(R,cD))/D,                            (10)

where adding complementary exponents corresponding to omitted g only increases the bound.
Put Z=R/c.

If Z<1, use F(R)<=R^2 and

    sum_(D|A)1/D <=(1-1/p)^(-1)(1-1/q)^(-1)<=4.

Then (10)<=4 A R^2<=4 A cR=4N.

If Z>=1, split at D<=Z.
In the lower range (6) and the first part of (9), together with c>=1, give

    A sum_(D<=Z)F(cD)/D
       <=14 A c^2 sum_(D<=Z)D/log(2cD)
       <=(224/log2) A c^2 Z
        =(224/log2) N.                                  (11)

In the upper range, the second part of (9) gives

    A F(R)sum_(D>Z)1/D
       <=(168/log2) A R^2 log(2Z)/[Z log(2R)]
       <=(168/log2) N,                                  (12)

because Z=R/c<=R.
Therefore (10) is at most (392/log2)N<800N.
The last safe numerical comparison follows from log2>1/2, since the integral of1/x on[1,2] is strictly greater than1/2.
This also covers the earlier Z<1 case.
No size of e,f,c or R has been hidden in a constant.

**Exactly the p exponent exceeds the anchor.**
Write j=e+u with u>=1 and x=p^u, while1<=k<=f.
Put Q=q^f and g=q^k.
Exact factorization now gives

    lcm(a,b)=p^j q^f c r^l,
    r^l<=min(R/x,Qc/(xg)).

Since phi(p^j)<=p^e x and phi(b)=phi(p^j)phi(g)phi(r^l), the sum over k,r,l for fixed x is at most

    p^e x sum_(1<=k<=f)phi(q^k)
                         min(R/x,Qc/(xq^k))^2
       <=(p^e/x) 2QcR=2N/x,                             (13)

by (6)'s first bound and (8).
Summing x=p^u, u>=1, costs at most sum p^-u=1/(p-1)<=1, so this entire case contributes at most2N.
The case with only the q exponent exceeding f contributes at most2N by the same calculation with the two primes interchanged.

**Both shared exponents exceed the anchor.**
If j>e and k>f, then lcm(a,b)=c b.
Hence b<=Y:=min(a,N/c).
Applying the first part of (6) and the exact tails in (7) gives

    sum_(j>e,k>f)phi(p^j)phi(q^k)F(Y/(p^j q^k))
       <=Y^2 p^(-e-1)q^(-f-1)
       <=N/(pq)<=N.                                    (14)

Here Y^2<=a*(N/c)=p^e q^f N.
Adding the four exponent cases gives at most800N+2N+2N+N=805N.
Terms with F argument below1 are automatically zero; no empty range has been treated as positive mass.

<a id="three-prime-entire-row-and-pairs"></a>
## 4. Every remaining row type and all ordered pairs

Now assume omega(a)<=3 and consider every b in B_N^(3)(a).
Partition by the relationship of its prime support to that of a.

1. If every prime factor of b divides a, [C97](Yin_C_G0097_v1.md#statement) covers the anchor's oriented star with at most (4*3+3)^3=3375 divisor sets at actual integers<=N.
   Each set has total phi-capacity at most sum_(d|n)phi(d)=n.
   This type contributes at most3375N.
   For a1 the direct singleton case is included in the safe bound.
   The global union of primes is not bounded by this local use.
2. If gcd(a,b)=1, then b<=min(a,N/a)<=sqrt N, so the full integer totient capacity contributes at mostN.
3. If b shares exactly ONE prime p with a but has at least one external prime, write b=p^j m with m>1 coprime to a, and a=p^e c.
   The external m may have one or two prime factors.
   Dropping that restriction only increases sum_(m<=y)phi(m)<=y^2.
   For j<=e, the exact lcm is a*m, and (8) bounds the sum by2N.
   For j>e, the exact lcm is c*b, and (7) bounds it byN as in C102.
   Thus this type contributes at most3N for each of at most three p, hence9N in total.
4. If b shares exactly TWO primes with a and has an external prime, omega(b)<=3 forces it to be precisely the type in Section3.
   There are at most three unordered shared-prime pairs.
   Its total is at most3*805N=2415N.

These types cover the row: if a noncoprime b is not fully supported on a, it has at most two shared primes because it has at least one external prime and omega(b)<=3.
Assign b1 to the first type to avoid overlap, or observe that an upper bound remains valid with it counted twice.
Every other representation uses its unique shared support.

The combined bound is

    B_N^(3)(a)<= (3375+1+9+2415)N=5800N<=8192N,

proving (1).
The slack is deliberate.

For real Y>=1, put N=floor Y.
Orders>N contribute nothing to P_2(Y).
The exact ordered-pair identity is

    P_2(Y)=2 sum_(a<=N)w_a
                  sum_(b<=a,lcm(a,b)<=N)w_b
             -sum_(a<=N)w_a^2.

Using w_b<=phi(b), (1), and the nonnegative diagonal correction proves (2).
This includes repeated labels, arbitrary real capacities, and an empty eligible set.
If0<Y<1, the pair mass is zero separately.

<a id="three-prime-density-and-efficiency"></a>
## 5. No-loss triple capture and the efficiency-eight boundary

The precise [C102 residual proof](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) does not use its support restriction after inserting a short-pair constant.
For completeness, with L=lcm(a,b), partition eligible c by lcm(L,c)=Lj.
Every bucket has weight at most H_X, and there are at most X/L buckets.
Therefore

    U_X(a,b)<=min(W,XH_X/L).

Split pairs at L<=epsilon W.
Equation(2) bounds the lower part's probability by16384epsilon when epsilon W>=1, and that part is empty otherwise.
The upper part contributes at most XH_X/(epsilon W^2).
Choose epsilon=delta/32768 to obtain

    delta<=16384epsilon+XH_X/(epsilon W^2),

and hence (3).
This is the original C91 logical reduction applied to a proved restricted premise, not reuse of its refuted universal constant.

The elementary efficiency support bound has the useful general form

    omega(o)>=r+1 => o/ord_o(p)>2^r,  for r>=1, p coprime to o.  (15)

For odd o with k distinct prime factors, each prime-power totient is even.
Their lcm is at most phi(o)/2^(k-1), so o/ord_o(p)>=2^(k-1)o/phi(o)>2^(k-1).
For o=2u with u odd and k-1 distinct odd prime factors, k>=2, the modulus2 contributes order1.
The remaining even totients give ord_o(p)<=phi(u)/2^(k-2), whence o/ord_o(p)>=2^(k-1)u/phi(u)>2^(k-1).
If v2(o)>=2, all k prime-power totients are even and the first argument applies directly.
These cases prove (15); the unit order1 is harmless.

Taking r3 proves that efficiency<=8 forces omega(o)<=3, with endpoint8 retained because (15) is strict.
No distribution of primitive roots, actual full-capacity assertion or bound on the union prime pool is used.
Equation(15) itself does not provide the needed row theorem at arbitrary r, so no general fixed-efficiency capture follows from it alone.

<a id="three-prime-original-norm-and-escape"></a>
## 6. Full actual norm income and necessary mass escape

Let P, alpha, d and p satisfy the Statement.
Complete actual reduced-root order groups have integer counts w_o<=phi(o), each irreducible reduction factor counted by its degree once, and every order is prime to p.
These are the unchanged [L159](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) conventions.
Under W>=gamma*d, X<=C*d and fixed triple density, (3) gives one n<=X with h(n)>=gamma^2 delta^2 d/(65536 C).
Replacing n by the lcm of its nonempty captured selected orders preserves precisely those groups and only decreases n; thus n may be taken prime to p.

Retain the full original signed norm

    D_n=Norm_(Q(alpha)/Q)(alpha^n-1)=Res(P,t^n-1),
    C_n=|D_n| in Z_(>0),
    A_p(n)=(log p)sum_(ALL d original p-adic roots alpha_i)
                                            v_p(alpha_i^n-1).

The accepted [C256 same-time floor](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) gives

    log C_n>=A_p(n)>=h(n)log p>=eta*d,

with eta in(4).
Every original root, every initial/exceptional/deeper valuation, and other-prime nonnegative income remain.
No depth is replaced by1 in the original norm, no smaller powered field is used, and no income at different times is added.
Nontorsion ensures that the norm is nonzero.

The SINGLE auxiliary t^n-1 has actual degree n<=Cd, content1 and squared coefficient norm2.
There is no rational coefficient or indexed-weight denominator, matrix-trace normalization, time inflation or discarded factor.
[L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) therefore supplies STRICT m(P)>m0(C,eta)>0 with its inherited full norm tower and accepted Pri11 statement/applicability scope.
No source-original proof audit is added.

For unrestricted actual inventories let W_low=(1-epsilon)W be the mass on orders with omega<=3.
The weight of all ordered triples touching a discarded label is exactly W^3-W_low^3.
Hence their remaining compatible triple mass is at least kappa W^3.
If kappa>0, its own normalized density delta_low=T_low/W_low^3 lies in(0,1], and (3) gives

    H_X>=delta_low^2 W_low^2/(65536 X)
        >=kappa^2 W^6/(65536 X W_low^4)
        >=kappa^2 W^2/(65536 X).                         (16)

The same original-norm transfer applies.
If epsilon were bounded a fixed positive amount below1-(1-delta)^(1/3) along a subsequence, kappa would be bounded below, contradicting m(P)->0 by the finite L168 criterion.
This proves (5).
Each discarded order has efficiency>8 by(15), so the same lower bound holds for mass with efficiency>8; the converse implication is not claimed.

This is a genuinely larger covered class and a stronger necessary mass escape than C102: individual support3 and efficiency8 replace support2 and efficiency4.
Actual existence of the selected positive-density inventories, a uniform bound on efficiency for near-one inputs, ordinary pair-only capture, and the unrestricted positive gap are still not established.

<a id="three-prime-controls-contributions"></a>
## 7. Author checks, earlier failures and contribution boundary

The author checked both ranges of the prime-power logarithmic bound, unique two-prime grid labels, every dyadic endpoint and constant, the Z<1 branch, c>=1 in the denominator comparison, all four shared-exponent cases and both exact lcm formulas, absence of double counting in shared-support choices, all row types, the complete diagonal correction, and the real small-threshold case in the residual argument.
The efficiency proof was checked separately for odd o, v2(o)1 and v2(o)>=2, including the strict endpoint8.
The original norm and deleted-triple mass arguments retain the same complete costs as C102.
These are author checks, not independent review.

The initially tempting repetition of C102 with only the crude y^2 capacity was insufficient at the two-shared-prime case: two-dimensional geometric shells have a logarithmic count.
The successful proof keeps the prime-power logarithmic saving and pays that count explicitly.
It does not assert that the failed crude estimate yields a counterexample, and makes no claim about the corresponding higher-dimensional row without a new estimate.
L395's false individual-support cover, C96's unrestricted averaged failure and the new correlated-product sharp-constant obstruction retain their own domains; none is contradicted by this bounded-support theorem.

The delegated author supplied all new arguments, constants, case partitions and deductions in this file.
Root received the candidate summary and coordinated the goal but supplied no proof step.
No native mathematical computation, continuing code, J program, new source theorem, source record, global T/E/S edit or Git operation was performed by this author.
Independent review of the complete actual artifact and any selected fixed form remains to be arranged by root.

<a id="three-prime-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T19:42.
ENTIRE author-complete artifact frozen for independent review: responsible question and bounded reuse/source screen; complete Statement and Argument; Sections1--7/equations1--16; all prime/grid estimates, four exponent cases, whole row and ordered-pair accounting, efficiency8 endpoint, actual norm costs and higher-complexity mass escape; every method/source/contribution limitation.
The optional scoped material check returned checked1, which verifies structure only.
No independent acceptance, original near-one coverage or G0001 completion is asserted.
Root may retain this entire original at a fixed C with its actual statement/argument anchors and arrange a noncontributor whole review of that actual fixed material.

## Fixed organization

The entire author-frozen original above is retained without a shortened mathematical wrapper, including all estimates, failed approaches, source interfaces and contribution limits.
This actual artifact awaits a separate noncontributor whole review.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:43 |
| status | open |
| reason | Retain individual three-prime capacity rows, efficiency-eight triple capture and conditional actual norm income for independent whole review. Actual near-one coverage and the unrestricted Task remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Entire argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Finite anchor cover](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Elementary prime capacity](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Two-prime residual interface](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Actual order capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Original norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:48 |
| status | proved |
| reason | Adopt R460's complete independent review of the actual fixed statement, entire argument and six direct dependencies. Individual three-prime rows and efficiency-eight triple-density income with the stated mass-escape consequence are established. Automatic near-one coverage and the unrestricted Mahler gap remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Entire argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Finite anchor cover](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Elementary prime capacity](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Two-prime residual interface](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Actual order capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Original norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0796_v1.md#three-prime-whole-independent-finding) | Entire actual statement and argument, all finite grid/exponent boundaries, direct inputs and complete original-norm/escape scope. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Dependency](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Dependency](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#three-prime-whole-independent-finding) | Entire actual statement and argument, all finite grid/exponent boundaries, direct inputs and complete original-norm/escape scope. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Exact retained argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Exact retained dependency](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#three-prime-whole-independent-finding) | Entire actual statement and argument, all finite grid/exponent boundaries, direct inputs and complete original-norm/escape scope. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Exact retained argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Exact retained dependency](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#three-prime-whole-independent-finding) | Entire actual statement and argument, all finite grid/exponent boundaries, direct inputs and complete original-norm/escape scope. |

### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Complete row, pair, triple, efficiency-eight, actual norm and mass-escape statements. |
| argument | [Exact retained argument](#argument) | All retained estimates, exponent cases, logical transfers and boundary checks. |
| dependency | [Exact retained dependency](Yin_C_G0097_v1.md#statement) | Shared anchor prime-pool star only. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Elementary prime-count proof and prime-power telescoping; all-range logarithmic form rederived here. |
| dependency | [Exact retained dependency](Yin_C_G0102_v1.md#two-prime-triple-residual-transfer) | Prior residual-bucket mechanism rederived using the new proved row constant. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Complete original good-prime root groups and exact capacity. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Same-time income retaining all roots and depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict class-specific positive measure with original-field norm and inherited Pri11 scope. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0106-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |
