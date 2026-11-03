---
author: Yin
---
# Fractional-moment capture for arbitrary squarefree inventories over comparable primes

Date: 2026-10-15.
Human author Yin.
New bounded G0001 author round by g_bridge_audit.
The preceding C127 and D39 remain fixed/frozen.
Root suggested retaining the actual a-dependent time X<=CaV while comparing a thinned law to the full layer; that suggestion is a contributed mechanism if used below.
No independent review is claimed.

## Responsible question

For any same-scale prime pool Q in(P,2P], initially one k-layer and arbitrary0<=w_A<=phi(o_A), seek fixed positive-proportion capture from original positive triple density and X<=CW WITHOUT assuming a fixed retained fraction of the complete layer capacity.
A true refutation must retain the capacities, fixed C and delta, and vanishing capture on each fixed enlarged window.
Failure of one domination estimate is not a counterexample to capture.

## Initial bounded reuse and candidate leap

Read C127's actual full-layer law and a^3 domination, C126v2's original-time structure, C99's exact complete-threshold domain and C114's paid core kernel.
None is assumed to control an arbitrary thinned law's covariance.
Root's sharper time suggestion is being checked at its exact scope.

A different candidate is a finite tensor bound for the normalized gcd kernel: for0<s<1 put q=2/(2-s), z_A=w_A/o_A^(s/2), and K(A,B)=product_(p in A symmetric-difference B)p^(-s/2).
If a two-point l^q quadratic-form bound with factor1+O_s(1/p) tensorizes, its product cost is bounded on(P,2P] by an elementary reciprocal sum.
Since capacities imply sum z_A^q<=W, this could supply the actual weak L1 fractional moment for ALL squarefree orders in that pool, without a retained-mass or single-layer assumption.
This is a candidate, not an adopted inequality.
Existing L396's false unrestricted strong form and L211/L223's finite tensorization were read before developing the new bound; no numerical program or J is proposed.

<a id="squarefree-harmonic-reuse"></a>
## Completed reuse screen and contribution boundary

The developed proof below uses the normalized gcd kernel already factored in [C114 equations10--11](Yin_C_G0114_v1.md#good-pair-core-fractional-estimate), but replaces its l2 geometric row-sum estimate by a different finite lq-to-lq' bound.
Its prime price is1/p rather than p^(-s/2).
The tensor mixed-norm mechanism is already supplied in [L211](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction): it is the finite Minkowski norm exchange, not a claim that the original inventory is a product law.
The exact counting-measure calculation required here is restated in Section3, with q' in place of L211's exponent2.
[L223/ODo07's classical hypercontractivity attribution](../audits/literature/ODo07/readme.md#boolean-hypercontractivity-attribution) is background; its normalized noise theorem is not invoked for the new local constant.

The exact unrestricted stronger inequality and its counterfamily in [L396](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) were read.
Its divergence uses growing prime reciprocal sum; the result below explicitly pays that sum, so does not repeat the false unrestricted inference.
C104's [residual-bucket density transfer](Yin_C_G0104_v1.md#product-envelope-density-capture) is used at its exact scope and rederived in Section6.
C126v2 and C127 motivate the same-scale question but are not theorem premises below.
The earlier source screens for the normalized gcd kernel, finite norm tensorization and fractional-lcm route supply sufficient reusable evidence for these elementary finite calculations; no new external theorem or program is required, and no novelty claim is made for the general norm mechanisms.

Root supplied the question and the optional a-dependent full-law comparison.
Section8 checks that proposed direction and records its actual failure.
The tensor bound and its capture proof in Sections1--7 were developed by this author, without a root proof step.
No thinned-law covariance or source negative-association statement is used.

<a id="statement"></a>
## 1. Exact finite theorem and its automatic comparable-prime specialization

Fix0<s<1 and put

    q=2/(2-s), q'=2/s, A_s=1-s,
    c_s=(q-1)A_s [2/(A_s q)]^(q'),
    K_s(Q)=product_(p in Q)(1+c_s/p).                    (1)

Here q' is the Holder conjugate of q, so1<q<2<q' and2/q=2-s.
Let Q be ANY finite prime pool, N=product_(p in Q)p, and let0<=w_a<=phi(a) for a|N, omitting zero weights.
Assume W=sum_a w_a>0.
Orders are squarefree and can occupy ANY subset of ANY layers.
Define

    E_s(w)=sum_(a,b|N)w_a w_b/lcm(a,b)^s,
    T_X=sum_(a,b,c|N:lcm(a,b,c)<=X)w_a w_b w_c,
    H_X=max_(integer1<=n<=X)sum_(a|n)w_a,
    delta_X=T_X/W^3.

All sums are ordered and include repeated labels.
Then

    E_s(w)<=K_s(Q) W^(2-s),
    K_s(Q)<=exp(c_s sum_(p in Q)1/p).                   (2)

More generally, for every nonnegative f on the finite divisor set,

    sum_(a,b|N)phi(a)phi(b)f(a)f(b)/lcm(a,b)^s
       <=K_s(Q)[sum_(a|N)phi(a)f(a)^q]^(2/q).            (3)

The Q-dependent constant is essential; (3) is NOT an unrestricted prime-independent strong inequality.

For every integer X>=1 with delta_X>0, the SAME original inventory satisfies

    H_X>=(delta_X/K_s(Q))^(1/s) W^2/X.                  (4)

Now suppose Q is contained in(P,2P] for ANY real P>=2.
Then, automatically,

    sum_(p in Q)1/p<=log(5/2),
    K_s(Q)<=(5/2)^(c_s).                                (5)

In particular choose s=1/2, for which q=4/3,q'=4,c_s=27/2.
For ANY fixed C>0,0<delta<=1,

    X<=CW, T_X>=delta W^3
       ==> H_X/W>=delta^2(2/5)^27/C.                   (6)

One may replace the right side by its minimum with1 when naming a capture fraction.
This is B=1 capture with NO fixed retained fraction, NO fixed k, NO bound on the number of orders or prime factors per order, and NO assumptions on correlations of the original mass law.
The same-scale prime hypothesis makes the cost in(5) automatic; it is not an additional requested certificate on these inputs.
General prime pools retain the exact paid product(1), without any automatic bound on it.

<a id="argument"></a>
## 2. The two-point quadratic-form estimate

For0<=rho<=1 let

    M_rho = [[1,rho],[rho,1]].

For any nonnegative two-vector x=(x0,x1), we prove

    x^T M_rho x <= (1+c_s rho^(q')) ||x||_q^2,           (7)

where every norm in this proof uses finite COUNTING measure, not normalized probability measure.
The zero vector is immediate.
By swapping coordinates, divide by the square of the larger positive coordinate and put r in[0,1] for the smaller-to-larger ratio.
The left-to-norm ratio is

    (1+r^2+2rho*r)/(1+r^q)^(2/q).

Convexity gives(1+r^q)^(2/q)>=1+(2-s)r^q.
Since r^2<=r^q on[0,1], subtracting the denominator from the numerator bounds the excess by

    2rho*r-(1-s)r^q.                                    (8)

For rho>0 this expression on ALL r>=0 has its maximum at

    r_*=[2rho/((1-s)q)]^(1/(q-1)),

with value c_s rho^(q').
At rho=0 its maximum is0.
Extending the maximization interval from[0,1] to[0,infinity) only enlarges the bound, even when r_*>1.
Because the original denominator is at least1, (8) proves(7).
All constants in(1) follow from this explicit scalar maximization; no local asymptotic approximation is used.
Substituting s=1/2 gives c_s=(1/6)*3^4=27/2 exactly.

The matrix M_rho is positive semidefinite: its eigenvalues are1+rho and1-rho.
Its entries are nonnegative.
Therefore(7) also bounds the quadratic form of any real vector, by replacing it with its coordinatewise absolute value.
Cauchy--Schwarz for the positive semidefinite form gives, for any real x,y,

    |x^T M_rho y|^2
       <=(x^T M_rho x)(y^T M_rho y)
       <=(1+c_s rho^(q'))^2 ||x||_q^2 ||y||_q^2.          (9)

This is the precise use of positive semidefiniteness; entrywise positivity alone would not imply the first inequality.
Finite Holder duality now yields the OPERATOR estimate

    ||M_rho x||_(q') <=(1+c_s rho^(q')) ||x||_q.          (10)

The constant is the same as in(7), not its square root: take the supremum of |y^T M_rho x| over ||y||_q=1 in(9).
Conversely any(10) gives(7) by Holder.
This checks the quadratic/operator interface needed for tensorization, including rho0 andrho1.

<a id="squarefree-harmonic-tensorization"></a>
## 3. Finite tensorization with the correct mixed-norm direction

For a finite array g_(i,j) and exponents q<=q', Minkowski's inequality gives

    ||g||_(l^(q')_j(l^q_i))
       <=||g||_(l^q_i(l^(q')_j)).                        (11)

Explicitly, raise both sides to q and apply the triangle inequality in l^(q'/q) to the nonnegative functions |g_(i,.)|^q.
This also proves the endpoint equality when q=q'; in our application q<q'.
It is valid for counting measure and introduces no dimension factor.

If finite matrices U,V have lq-to-lq' operator norms at most A,B, apply U in the i-coordinate for each fixed output j, use(11) to exchange the mixed norms, and then apply V in each remaining input-coordinate row.
This gives

    ||(U tensor V)f||_(q')
       <=A ||(Id tensor V)f||_(l^(q')_j(l^q_i))
       <=A ||(Id tensor V)f||_(l^q_i(l^(q')_j))
       <=AB ||f||_q.                                    (12)

Induction proves the product of the individual bounds for ANY finite number of matrices.
The array f may have arbitrary dependence among its coordinates; tensorization concerns the OPERATOR, not a product assumption on f.
The zero-factor operator is the identity on a one-point space and has norm1.

Identify squarefree divisors a|N with their0/1 prime-membership vectors.
The normalized gcd kernel is exactly

    G_s(a,b)=gcd(a,b)^s/(ab)^(s/2)
       =product_(p in Q)p^(-s|1_(p|a)-1_(p|b)|/2)
       =tensor_(p in Q) M_(p^(-s/2))(a,b).               (13)

Since(p^(-s/2))^(q')=1/p, (10)--(12) imply

    ||G_s z||_(q')<=K_s(Q)||z||_q,
    z^T G_s z<=K_s(Q)||z||_q^2.                          (14)

The second inequality is Holder.
Every operator is finite, so no limiting tensor or infinite-support argument is hidden.

<a id="squarefree-harmonic-capacity"></a>
## 4. Restore the original lcm energy and capacity normalization

Set z_a=w_a/a^(s/2), with z_a=0 at omitted orders.
The elementary identity lcm(a,b)*gcd(a,b)=ab gives

    E_s(w)=sum_(a,b|N) z_a z_b G_s(a,b).                 (15)

Since q-1=sq/2 and0<=w_a<=phi(a)<=a,

    z_a^q=w_a*(w_a/a)^(q-1)<=w_a,
    sum_a z_a^q<=W.                                    (16)

The expression at w_a=0 is0, interpreted directly rather than by division by w_a.
Equations(14)--(16) prove(2).
In fact this weak estimate uses only the looser bound w_a<=a; the stated Euler capacities satisfy it.

For(3), put w_a=phi(a)f(a) without assuming f<=1.
Then

    z_a^q=phi(a) f(a)^q *[phi(a)/a]^(q-1)
         <=phi(a)f(a)^q.                                (17)

Insert(17) in(14).
Thus the paid strong form holds for every nonnegative finite f on this divisor set.
Its restriction to f=w/phi in[0,1] also yields the weak form, but the simpler actual-capacity identity(16) already proves exactly the desired original-W inequality.

Finally log(1+x)<=x for x>=0 gives K_s(Q)<=exp(c_s sum1/p).
There is no assumption that this cost remains bounded over all finite prime pools.
L396's actual product counterfamily has unbounded reciprocal-prime sum and is consistent with this paid inequality.
The estimate does not contradict C105's failure of the sharp product-only universal constant, because K_s(Q) here is different and retains its full pool dependence.

<a id="squarefree-harmonic-comparable-primes"></a>
## 5. Automatic bounded cost on a comparable-prime interval

Let Q be contained in(P,2P], P>=2, and put b=floor P>=2.
Every prime in Q is among the integers b+1,...,floor(2P).
Using1/n<=integral_(n-1)^n dt/t,

    sum_(p in Q)1/p
       <=sum_(n=b+1)^floor(2P)1/n
       <=log(floor(2P)/b)
       <=log((2b+1)/b)<=log(5/2).                        (18)

This uses only floor(2P)<=2b+1 and b>=2.
It covers real P, missing primes and the empty pool, with the empty sum0.
No prime-number estimate or asymptotic statement is used.
Equations(2) and(18) give(5), in particular

    E_(1/2)(w)<=(5/2)^(27/2) W^(3/2).                  (19)

All squarefree divisors, arbitrary subsets and arbitrary real lowered capacities are allowed.
Different cardinality layers may be mixed with no extra charge.
The former positive-retention hypothesis has been removed on this entire same-scale squarefree domain, not replaced by another assumed indicator; its cost is bounded by the interval condition already in the question.

<a id="squarefree-harmonic-density"></a>
## 6. Exact return to ordered triple density and original capture

The following is the existing C104/C91 residual-bucket mechanism, here written with its full original masses.
For a pair a,b put L=lcm(a,b), and let U_X(a,b) be the total weight of third orders c such that lcm(L,c)<=X.
If L>X, U_X(a,b)=0.
Otherwise write

    r=c/gcd(c,L), so lcm(L,c)=Lr.

For each possible integer r<=X/L, every c in that bucket divides Lr.
Since Lr is an actual integer at most X, the whole bucket weighs at most H_X.
There are at most floor(X/L) possible r.
Also U_X(a,b)<=W.
Consequently, with H_X>=0,

    U_X(a,b)/W<=min(1,XH_X/(WL))
               <=[XH_X/(WL)]^s.                         (20)

The last bound uses0<s<1 and holds also at0.
If L>X it still bounds the zero left side.
Multiply by w_a w_b/W^2 and sum over ALL ordered pairs, including their diagonals:

    delta_X<= (XH_X/W)^s E_s(w)/W^2
             <=K_s(Q)(XH_X/W^2)^s.                      (21)

If delta_X>0 then H_X>0, and rearrangement gives(4).
When delta_X=0 there is no positive-capture conclusion and no division by it.
Under delta_X>=delta and X<=CW, (4)--(5) give

    H_X/W>=[delta/(5/2)^(c_s)]^(1/s)/C.

At s=1/2 this is(6).
No auxiliary change of law, loss of an ancestor mass, changed window, or averaging over different capture times appears.

The empty pool Q has just the order1.
If W>0 and X>=1 then H_X=W and T_X=W^3; (2) reduces to W^2<=W^(2-s), valid because W<=phi(1)=1.
The density estimate(4) remains valid since X>=1>=W.
If all weights are0, the energy inequality is trivially true but normalized density is undefined; it was excluded from the statement.
These cases also check the0-factor tensor convention.

<a id="squarefree-harmonic-actual-income"></a>
## 7. Actual original-polynomial application and remaining scope

Let F be an ACTUAL monic irreducible nontorsion integer-unit polynomial of original degree d, root alpha, and field K=Q(alpha).
Choose a GOOD prime ell and COMPLETE occurring reduced-root order groups of weights w_o.
Require every selected order to be squarefree and supported on some Q contained in(P,2P], P>=2; Q and P may vary with the input.
Require the existing separate coverage premises

    W>=gamma*d,  integer1<=X<=C*d,  T_X>=delta W^3,

with fixed gamma>0,C>0,delta>0.
No retained fraction of an ambient layer is required.
The actual Frobenius capacities w_o<=phi(o) are the same [L159 interface](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity); absent orders receive no artificial roots.

Equations(4)--(5) at s=1/2 give ONE actual integer n<=X capturing at least

    delta^2(2/5)^27 W^2/X
       >=delta^2(2/5)^27 gamma^2*d/C                    (22)

original selected roots.
The existing [C256 original-root norm interface](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) yields

    D_n=Norm_(K/Q)(alpha^n-1)=Res(F,t^n-1),
    C_n=|D_n| in Z_(>0),
    log C_n>=(log ell)v_ell(C_n)>=eta*d,
    eta=delta^2(2/5)^27 gamma^2*log2/C>0.                 (23)

The full original field and ALL original roots and nonnegative local-depth contributions remain; no thinned norm or powered-field degree replacement is made.
The auxiliary t^n-1 has original degree n<=Cd, content1 and squared coefficient norm2.
[L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), with its accepted Pri11 statement/applicability scope, gives its strict positive Mahler bound depending on C and eta.
This does not establish the actual good-prime coverage premises or construct a near-one realization.

The finite paid product in(1) also gives a conditional positive consequence on more general squarefree prime pools whenever that actual product is uniformly bounded.
No automatic comparison with every C114 paid-core certificate, every C124 terminal-support class, or arbitrary C127 input outside the same-scale domain is asserted.
On the common same-scale squarefree domain, the result explicitly removes the retained-mass and single-layer assumptions of the preceding inquiry.
General prime powers and unrestricted multi-scale pools are NOT covered by this two-point proof: higher exponents require a different chain operator, and the unrestricted strong form remains false by L396.

<a id="squarefree-harmonic-failed-domination"></a>
## 8. Why keeping a in the full-law time does not by itself repair domination

Root suggested retaining X<=CaV rather than weakening it to CV in the full-law comparison from C127.
The suggestion is mathematically sensible, but the following finite construction shows that the specific desired comparison T_v(CaV)=o(a^3 V^3) cannot hold uniformly even on a first layer.
This is a failure of that domination route, NOT a failure of capture.

Let P>4 and take any nonempty pool Q of m>=1 primes in(P,2P].
On its k=1 full layer put v_p=p-1,V=sum_p v_p.
Let q0=max Q, retain ONLY the single weight w_(q0)=q0-1, and put

    W=q0-1, a=W/V, X=2W=2aV.

Then1/m<=a<=3/m.
Every pool prime is at most q0<=X, while the product of two distinct pool primes is greater than P^2>4P>X.
Thus the full inventory has ONLY diagonal compatible triples at this actual time, and

    T_v(X)=sum_(p in Q)(p-1)^3,
    T_v(X)/(a^3 V^3)=T_v(X)/W^3
       >=m(P-1)^3/(2P)^3>=m/64.                        (24)

The retained inventory has T_w(X)=W^3, original density1, X=2W, and H_w(X)=W.
Hence even the strengthened time-aware full-law domination can be arbitrarily expensive relative to a^3, while the desired capture is already perfect.
This rules out a uniform bound tending to0 for that normalized full-law ratio; it does not exclude more refined full-law arguments that also track concentration or capture.

For unbounded versions of this check one needs pools with m->infinity; such pools exist without a prime asymptotic.
Otherwise a uniform bound on the number of primes in every dyadic interval(2^r,2^(r+1)] would imply convergence of the prime reciprocal sum, contradicting the already proved elementary divergence retained at [C220](Yin_C_G0220_v1.md#discriminant-divergence).
Choose dyadic intervals whose prime counts tend to infinity, and hence P->infinity, and take their full pools.
This merely certifies the method-obstruction sequence; it supplies no actual polynomial or near-one counterexample.
Its perfect capture shows why a pure full-law small-probability comparison is too crude for arbitrary thinning.

<a id="squarefree-harmonic-author-freeze"></a>
## Author check and entire freeze

2026-10-15T08:51.
The g_bridge_audit author freezes this ENTIRE account for fixed retention and separate whole review.
Statement1 contains the finite paid strong and weak estimates for arbitrary squarefree divisor inventories, the automatic comparable-prime cost, and original-window positive-density capture.
Sections2--6 give the full finite proof; Section7 retains actual original-polynomial costs and unresolved coverage; Section8 preserves the useful failed time-aware domination attempt and its complete positive-capture control.
The original proposal paragraph remains exploratory history, superseded in scope by the precise statement and full argument.
Root supplied the question and Section8's investigated direction, but not the tensor mechanism or main proof.
No independent review is asserted here.

Author self-check covered the entire0<s<1 range and constants, zero vectors, rho0/1, the r<=1 normalization and unrestricted scalar maximum, PSD rather than entry positivity in(9), finite Holder duality and the unchanged operator constant, mixed-norm direction and counting-measure normalization, arbitrary tensor count and empty product, exact normalized-gcd/lcm identities, actual w capacity conversion with zeros, paid strong-form compatibility with L396, real-P floor endpoints, original ordered triple buckets and X/H/W zero guards, original n/degree/full-root norm costs, and every inequality of the Section8 method obstruction.
No new native mathematical code, J or external theorem was used.
The scoped material check returned checked1; this is structural evidence only.
The unrestricted multi-scale and prime-power capacity problems, actual automatic good-prime coverage, and unrestricted G0001 remain open.

## Fixed organization

The entire frozen author account is retained without mathematical abridgment.
The entire squarefree harmonic-cost tensor proof, original-capacity and original-window capture, strong-form costs, complete actual-norm application and failed time-aware domination control.
General prime powers and automatic actual coverage remain open.
Root supplied direction and the failed comparison question, not the principal tensor proof.
Actual fixed whole independent review is pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:00 |
| status | open |
| reason | The entire squarefree harmonic-cost tensor proof, original-capacity and original-window capture, strong-form costs, complete actual-norm application and failed time-aware domination control. General prime powers and automatic actual coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete squarefree harmonic-cost capture](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete squarefree harmonic-cost capture](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact body-used input](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |

### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Dependency](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Exact retained argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact retained dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Exact retained argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact retained dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |

### Decision current-complete-mixed-norm-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T03:02 |
| status | proved |
| reason | Locate only the existing finite mixed-norm exchange at the complete same-object C508v2 home after reading this consumer statement and full counting-measure tensor argument against the complete retained input. C129 still explicitly derives its conjugate-exponent/counting-measure version and imports no different cyclic-noise constant, actual stationary law or new independence premise. Every other field except this date/reason, all nonmatching relation/review tuples and scopes, every old decision and the complete mathematical text remain unchanged. R485 and all original author/reviewer readings retain their actual fixed L211 inputs and are not represented as having inspected later C508; no new whole review or isolated coverage is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Exact retained argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Exact retained dependency](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact retained dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |

### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Exact retained argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Exact retained dependency](Yin_C_G0508_v2.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact retained dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g129-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:12 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt the complete noncontributor R485 finding. Arbitrary same-scale squarefree capacity inventories have original-window capture with explicit harmonic prime cost. Record all body-used inputs omitted from the initial table; no proof premise changed. Unrestricted prime powers and automatic actual coverage were not proved in this version. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete squarefree harmonic-cost capture](#statement) | Entire exact statement, all domains, finite and limiting guards, and stated controls. |
| argument | [Complete frozen argument](#argument) | The entire author proof, direct input interfaces, costs, boundary cases, comparisons and contribution limits. |
| dependency | [Direct accepted interface](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) | Finite mixed-norm exchange, explicitly restated for counting measure and conjugate exponents. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Actual complete good-prime root-group capacities. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and local-depth capture at one original time. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual linear-time finite-income consequence with inherited Pri11 scope. |
| dependency | [Exact body-used input](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Elementary divergence only, for the unbounded dyadic pool sequence in the failed domination control. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0798_v1.md#squarefree-tensor-whole-independent-finding) | Entire fixed mathematical account, exact original costs, all boundaries and disclosed contribution limits. |
