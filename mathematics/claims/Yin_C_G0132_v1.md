---
author: Yin
---
# Harmonic-cost capture with arbitrary prime exponents

Date: 2026-10-15T09:08.
Human author Yin.
Root authors the new prime-power chain proof below under the continuing G0001 authorization.
The squarefree harmonic-cost mechanism was developed by g_bridge_audit and is fixed in C129; its separate R485 review has an unknown relationship.
Root cannot independently review the present extension.
No numerical or native mathematical program is used.

## Responsible question and bounded reuse

Can the squarefree two-point norm mechanism of [C129](Yin_C_G0129_v1.md#statement) be extended to arbitrary prime exponents without paying the largest exponent or changing the original weights?
The necessary new step is a dimension-independent lq-to-lq' estimate for the finite geometric chain.
The rest of the mechanism is rederived below, so no pending C129 acceptance is silently assumed.

The actual [C114 core argument](Yin_C_G0114_v1.md#good-pair-core-fractional-estimate) already factors the arbitrary-exponent normalized gcd kernel, but its l2 row-sum price is of order p^(-s/2).
[C104](Yin_C_G0104_v1.md#product-fractional-moment-statement) covers prime-power PRODUCT profiles with a sharper universal weak constant; arbitrary correlated arrays are not its domain.
[C108v2](Yin_C_G0108_v2.md#nested-slice-continuation-statement) concerns componentwise Cauchy losses and initial-segment saturation, not the present chain norm.
[L211](../ledger/Yin_L_G0211_v1.md#cyclic-noise-tensor-contraction) supplies the finite Minkowski norm-exchange mechanism.
[L396](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) refutes a prime-independent strong estimate; the present bound retains every reciprocal-prime cost.
These exact local interfaces and C129's complete tensor proof were inspected before this extension.
No new literature theorem or novelty assertion is needed for the finite estimates proved here.

The substantive new contribution is the dominant-coordinate/remaining-mass argument for a geometric chain, uniform in its length.
It exploits the strict lq-to-l2 deficit away from a coordinate vector and separately pays the interaction with the largest coordinate.
The tensor mechanism, capacity substitution and residual-bucket transfer are credited to the preceding materials, with their complete calculation retained here for the actual new domain.

<a id="statement"></a>
## 1. Finite statement and constants

Fix 0<s<1 and define

    q=2/(2-s), q'=2/s, c=1-2^(s-1),
    rho_max=2^(-s/2), rho_0=c/8,
    A_s=(q-1)(c/2)[8/(q*c)]^(q'),
    B_s=[2*rho_max/(1-rho_max)]*rho_0^(-q'),
    C_s=max(A_s,B_s).                                      (1)

Thus 1<q<2<q', 1/q+1/q'=1, 0<c<1/2, and 0<rho_0<rho_max<1.
Constants are deliberately not optimized.
All norms use finite COUNTING measure.

**A. Arbitrary-length chain.**
For every integer e>=0, every real vector x indexed by 0,...,e, and 0<=rho<=rho_max, let K_rho(i,j)=rho^|i-j|, with K_0 the identity.
Then

    x^T K_rho x <=(1+C_s*rho^(q')) ||x||_q^2,
    ||K_rho x||_(q') <=(1+C_s*rho^(q')) ||x||_q.             (2)

The constant does not depend on e.

**B. Arbitrary finite capacities.**
Let Q be any finite set of primes and N=product_(p in Q)p^(e_p), with arbitrary positive integers e_p.
On all divisors of N let 0<=w_a<=phi(a), including arbitrary omissions, and W=sum w_a>0.
Put

    D_s(Q)=product_(p in Q)(1+C_s/p),
    E_s(w)=sum_(a,b|N)w_a*w_b/lcm(a,b)^s.

Then

    E_s(w)<=D_s(Q) W^(2-s),
    D_s(Q)<=exp(C_s*sum_(p in Q)1/p).                       (3)

Every nonnegative function f on the divisors also satisfies the PAID strong form

    sum_(a,b|N)phi(a)phi(b)f(a)f(b)/lcm(a,b)^s
       <=D_s(Q)[sum_(a|N)phi(a)f(a)^q]^(2/q).              (4)

No uniform bound in unrestricted Q is claimed.
The weak inequality in fact holds under 0<=w_a<=a; Euler capacities are the intended original-root case.

**C. Original-time capture.**
For integer X>=1 define

    T_X=sum_(a,b,c|N:lcm(a,b,c)<=X)w_a*w_b*w_c,
    H_X=max_(integer 1<=n<=X)sum_(a|n)w_a,
    delta_X=T_X/W^3.

The sums are ordered and include repeated labels.
If delta_X>0, then

    H_X >= (delta_X/D_s(Q))^(1/s) W^2/X.                   (5)

In particular, if sum_(p in Q)1/p<=L, X<=C W and delta_X>=delta>0, then

    H_X/W >= exp(-C_s*L/s)*delta^(1/s)/C.                  (6)

For ANY real P>=2 and Q contained in (P,2P], one can take L=log(5/2).
All prime exponents, all mixtures of layers, arbitrary correlations and arbitrary capacity reductions are permitted.
Capture remains in the original window, B=1.
This removes the squarefree restriction from the same-scale interface; it does not prove any actual good-prime coverage hypothesis.

<a id="argument"></a>
## 2. Geometric-chain positivity and coarse row bounds

For 0<rho<1, define vectors in Euclidean space with basis u_0,...,u_e by

    v_j=rho^j*u_0 + sqrt(1-rho^2)*sum_(r=1)^j rho^(j-r)*u_r.

Their squared norms are rho^(2j)+(1-rho^2)sum_(r=1)^j rho^(2j-2r)=1.
For i<=j, their scalar product is rho^(j-i), since the coordinates through i of v_j are rho^(j-i) times those of v_i.
Hence K_rho is their Gram matrix and is positive semidefinite.
At rho=0 it is the identity, also positive semidefinite.
Its entries are nonnegative.

For every row the off-diagonal sum is at most 2rho/(1-rho).
Symmetry and 2|x_i*x_j|<=x_i^2+x_j^2 give, for every real vector,

    |x^T(K_rho-I)x| <= [2rho/(1-rho)] ||x||_2^2,
    x^T K_rho x <= [(1+rho)/(1-rho)] ||x||_2^2.           (7)

The finite row bound includes boundary rows and arbitrary e; no infinite vector or limiting operator is used.
Also ||x||_2<=||x||_q for q<2: after normalizing sum |x_i|^q=1, each |x_i|<=1 implies sum |x_i|^2<=1.

When rho>=rho_0, (7) gives

    x^T K_rho x <= [1+2rho_max/(1-rho_max)]||x||_q^2
                  <=(1+B_s*rho^(q'))||x||_q^2.           (8)

Thus only 0<=rho<=rho_0 needs a sharper argument.

<a id="prime-power-chain-deficit"></a>
## 3. Largest-coordinate deficit for small rho

It is enough to consider x>=0, because the entries of K are nonnegative and the q norm is unchanged on replacing x by |x|.
The zero vector is immediate.
Normalize sum x_i^q=1, choose a largest coordinate A=x_i0, and set t=1-A^q.
All other coordinates form a tail y with sum y_j^q=t.
The case e=0 is included, with t=0.
For rho<=rho_0<1/2, 2rho/(1-rho)<=4rho and 4rho<=c/2.

First suppose A^q<=1/2, or t>=1/2.
Then

    sum_i x_i^2 <= A^(2-q) sum_i x_i^q
                <=(1/2)^((2-q)/q)=2^(s-1)=1-c.

By (7) the entire off-diagonal contribution is at most 4rho*sum x_i^2<=4rho<=c/2.
Therefore

    x^T K_rho x <=1-c/2<=1.                              (9)

Now suppose A^q>=1/2, so 0<=t<=1/2.
Since 2/q=2-s>1,

    sum_i x_i^2 <=(1-t)^(2/q)+t^(2/q)
       <=1-t + 2^(s-1)*t =1-c*t.                        (10)

The first bound uses ||y||_2^2<=||y||_q^2=t^(2/q), and the second uses t^(2/q-1)<=2^(s-1).
The tail-tail off-diagonal contribution, even with the missing i0 position, is bounded by the same row estimate:

    y^T(K_tail-I)y <=4rho*||y||_2^2
                         <=4rho*t<= (c/2)*t.            (11)

Here K_tail is the principal submatrix on the remaining coordinates; its row sums can only decrease.
The interaction between i0 and the tail is at most, by Holder and A<=1,

    2A sum_(j != i0)rho^|j-i0| x_j
       <=2[2rho^(q')/(1-rho^(q'))]^(1/q') t^(1/q)
       <=4rho*t^(1/q).                                  (12)

Indeed rho<=rho_max and rho_max^(q')=1/2; the bracket is at most 4^(1/q')rho<=2rho because q'>2.
For rho=0 the expression is directly zero, so no singular division occurs.

Combining (10)--(12), then writing r=t^(1/q), gives

    x^T K_rho x <=1-(c/2)*t+4rho*t^(1/q)
       <=1+max_(r>=0){4rho*r-(c/2)*r^q}
       =1+A_s*rho^(q').                                 (13)

For rho>0 the maximizing r is [8rho/(q*c)]^(1/(q-1)), and the maximal value is (q-1)(c/2)[8rho/(q*c)]^(q').
At rho=0 its maximum is zero.
Maximizing over all r>=0 enlarges the allowed interval, so no unstated optimizer restriction is needed.
Equations (8), (9), (13), and homogeneity prove the first part of (2), uniformly in every chain length.

For arbitrary real x,y, Cauchy--Schwarz for the positive semidefinite form, not entrywise positivity alone, gives

    |y^T K_rho x| <=(1+C_s*rho^(q'))||y||_q||x||_q.

Taking the supremum over ||y||_q=1 yields the second part of (2) by finite Holder duality.
The same constant is retained, not its square root.

## 4. Tensorization for arbitrary exponent arrays

For a finite array g and q<=q', the counting-measure Minkowski inequality is

    ||g||_(l^(q')_j(l^q_i)) <= ||g||_(l^q_i(l^(q')_j)).   (14)

To verify it, raise both sides to q and apply the triangle inequality in l^(q'/q) to the functions |g_(i,.)|^q.
If U,V have lq-to-lq' norms at most A,B, applying U in the first coordinate, exchanging mixed norms by (14), and applying V in the second gives

    ||(U tensor V)f||_(q')
       <=A||(Id tensor V)f||_(l^(q')_j(l^q_i))
       <=A||(Id tensor V)f||_(l^q_i(l^(q')_j))
       <=AB||f||_q.                                     (15)

Finite induction handles any number of prime coordinates.
This is an operator estimate for arbitrary arrays f, with no product-law or independence assumption on f.

Write a|N as its full exponent vector.
Then

    G_s(a,b)=gcd(a,b)^s/(ab)^(s/2)
       =product_(p in Q)p^(-s*|v_p(a)-v_p(b)|/2)
       =tensor_(p in Q)K_(p^(-s/2))(a,b).                (16)

Every rho_p=p^(-s/2) lies in (0,rho_max], and rho_p^(q')=1/p.
Equations (2), (15) therefore give

    ||G_s z||_(q') <=D_s(Q)||z||_q,
    z^T G_s z <=D_s(Q)||z||_q^2.                         (17)

The second inequality is Holder.
All exponents and tensor dimensions are finite but otherwise unrestricted; there is no charge depending on them.

## 5. Exact original-weight conversion and strong-form boundary

Set z_a=w_a/a^(s/2).
Since lcm(a,b)*gcd(a,b)=ab,

    E_s(w)=sum_(a,b|N)z_a*z_b*G_s(a,b).

The exact identity q-1=sq/2 and w_a<=phi(a)<=a imply

    z_a^q=w_a*(w_a/a)^(q-1)<=w_a,
    sum_(a|N)z_a^q<=W.                                  (18)

At w_a=0 interpret the term directly as zero.
Insert (18) in (17), and use 2/q=2-s, to prove (3).
Taking logarithms and log(1+x)<=x gives its paid exponential bound.

For (4), use z_a=phi(a)f(a)/a^(s/2), without any upper bound on f.
Then

    z_a^q=phi(a)f(a)^q*[phi(a)/a]^(q-1)
          <=phi(a)f(a)^q.

Thus the same proof gives precisely the paid strong form.
L396's unbounded prime-pool counterfamily is consistent with it: D_s(Q) is allowed to diverge and has not been replaced by a universal constant.
Nor is this claimed to recover C104's sharper universal product-profile constant.
The present gain is the arbitrary dependence of the inventory at a paid harmonic prime cost.

The empty Q has the single order 1, empty tensor/product equal to 1, and 0<W=w_1<=1.
Its energy inequality W^2<=W^(2-s) is correct.
Zero total mass makes the energy inequality trivial but normalized triple density undefined; it is excluded only where normalized quantities are used.

## 6. Original triple buckets and automatic comparable-prime cost

For an ordered pair a,b put L=lcm(a,b).
If L>X, its compatible-third mass is zero.
Otherwise group every compatible c by r=c/gcd(c,L), so lcm(c,L)=L*r<=X and c divides the one integer L*r.
Each bucket has mass at most H_X, with at most floor(X/L) buckets.
Its mass is also at most W.
Consequently

    U_X(a,b)/W <=min(1,X*H_X/(W*L))
                    <=[X*H_X/(W*L)]^s.                  (19)

This holds also when H_X=0, by its direct nonnegative meaning.
Multiplying by w_a*w_b/W^2 and summing over all pairs gives

    delta_X <=(X*H_X/W)^s*E_s(w)/W^2
             <=D_s(Q)*(X*H_X/W^2)^s.                    (20)

Positive delta_X forces H_X>0 and allows rearrangement to (5).
This retains the original W, original X, all repeated labels and one actual integer capture time.

If Q is contained in (P,2P], P>=2, let b=floor(P)>=2.
Then

    sum_(p in Q)1/p
       <=sum_(n=b+1)^floor(2P)1/n
       <=integral_b^floor(2P) dt/t
       <=log((2b+1)/b)<=log(5/2).                        (21)

Empty sums are zero.
This includes real P and missing primes, and uses no prime distribution result.
More generally, a union of r such intervals has reciprocal-prime sum at most r*log(5/2), even if they overlap; for FIXED r this gives another uniform class.
This additional conclusion is a union bound, with its full dependence on r retained.
No fixed bound is asserted for arbitrarily many scales.

For X<=CW and delta_X>=delta>0, (20) and (21) give (6) with L=log(5/2).
The constant can be replaced by its minimum with 1 when describing a capture fraction; if the displayed lower bound exceeds 1, those parameter premises cannot occur.

## 7. Conditional full original-polynomial consequence and remaining target

Let F be an actual monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d, root alpha, and full field K=Q(alpha).
At one GOOD prime ell select COMPLETE occurring reduced-root order groups.
Their original weights satisfy w_a<=phi(a) by [L159](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity).
Suppose their finite prime support Q obeys sum_(p in Q)1/p<=L, and suppose

    W>=gamma*d, integer 1<=X<=C*d, T_X>=delta*W^3,

for fixed positive gamma,C,delta and finite L.
Arbitrary exponents of every order are permitted.
Equation (5) gives ONE original n<=X capturing at least

    exp(-C_s*L/s)*delta^(1/s)*gamma^2*d/C

original selected roots.
[C256](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) therefore gives, for the entire original norm,

    C_n=|Norm_(K/Q)(alpha^n-1)|=|Res(F,t^n-1)| in Z_(>0),
    log C_n>=(log ell)*v_ell(C_n)>=eta*d,
    eta=exp(-C_s*L/s)*delta^(1/s)*gamma^2*log(2)/C>0.      (22)

All original roots and every nonnegative local-depth contribution remain; no powered-field degree or thinned norm replaces them.
The auxiliary t^n-1 has actual degree n<=Cd, content 1 and squared coefficient norm 2.
[L168](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), at its accepted Pri11 applicability scope, then supplies a strict positive Mahler lower bound depending on C and eta.

This is conditional on ACTUAL coverage.
A bound on the harmonic support, or the more restrictive common prime interval, is not established for every near-one input.
General prime pools with diverging harmonic mass are not closed; neither is a uniform unrestricted weak fractional moment.
No near-one sequence or unconditional G0001 resolution follows.
The finite chain argument removes an exponent restriction from one genuine positive mechanism, without removing the remaining arithmetic realization and coverage duties.

<a id="prime-power-chain-entire-author-freeze"></a>
## Entire author check and freeze

2026-10-15T09:08.
Root freezes the entire present account for separate fixed review: Statement A--C, all Sections 2--7 and 22 numbered formulas, exact finite constants and domains, independent-length chain deficit, PSD/duality/tensor interfaces, original capacity conversion, paid strong form, original-time bucket transfer, finite-interval union cost and full original-polynomial conditional expense.
The actual author check reconstructed every inequality, including q/q' conjugacy, rho_0 and rho_max endpoints, missing tail position, t=0 and t=1/2, the tail l2 deficit, scalar maximization, row bounds, empty tensor and zero weights.
No unresolved proof gap was found by this author self-check.
Mathematical independence is not claimed; a material-format check cannot replace it.

Root supplied all new chain estimates.
C129's squarefree author supplied the prior harmonic-cost tensor mechanism, which is explicitly credited and rederived here; the current chain proof has not been supplied by another agent.
The prospective reviewer must disclose any earlier contribution to the fixed inputs separately from contribution to this new proof.
No new source theorem, numerical calculation, native program, J or unrestricted completion claim is used.

## Fixed organization

Retain the complete arbitrary-exponent harmonic-cost chain proof and all stated costs.
Root is its proof contributor and cannot serve as its independent reviewer.
The squarefree mechanism is credited and completely rederived; no pending predecessor acceptance is assumed.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:10 |
| status | open |
| reason | Retain the dimension-independent prime-power chain estimate and its original-capacity original-time capture at paid harmonic prime cost. Automatic actual coverage and unrestricted prime pools remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Arbitrary prime-exponent statement](#statement) | Entire A--C, explicit constants, paid strong and weak forms, original-window capture and conditional norm scope. |
| argument | [Complete chain and tensor proof](#argument) | All Sections2--7 and22 equations, boundaries, exact costs, source and contribution limits. |
| dependency | [Actual original capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Conditional complete actual good-prime order-group capacities only. |
| dependency | [Full original norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional captured original-root count to complete norm, with all depths retained. |
| dependency | [Original finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual linear time and complete original norm; accepted Pri11 input scope is unchanged. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T09:18 |
| status | proved |
| reason | Adopt R353 actual whole review by a noncontributor to the new prime-power chain proof, with prior squarefree-mechanism authorship disclosed. Arbitrary exponent arrays have original-window capture at explicit harmonic prime cost; same-scale supports and fixed finite unions receive an automatic uniform constant. General diverging harmonic support and automatic actual good-prime coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Arbitrary prime-exponent statement](#statement) | Entire A--C, explicit constants, paid strong and weak forms, original-window capture and conditional norm scope. |
| argument | [Complete chain and tensor proof](#argument) | All Sections2--7 and22 equations, boundaries, exact costs, source and contribution limits. |
| dependency | [Actual original capacities](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Conditional complete actual good-prime order-group capacities only. |
| dependency | [Full original norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional captured original-root count to complete norm, with all depths retained. |
| dependency | [Original finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual linear time and complete original norm; accepted Pri11 input scope is unchanged. |
| review | [Actual whole arbitrary-exponent finding](../audits/reviews/Yin_R_G0353_v1.md#prime-power-harmonic-whole-independent-finding) | Entire fixed proof and22 equations, new chain argument independently reconstructed with antecedent authorship disclosed; full original costs and remaining harmonic-support/coverage limits. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--C, explicit constants, paid strong and weak forms, original-window capture and conditional norm scope. |
| argument | [Argument](#argument) | All Sections2--7 and22 equations, boundaries, exact costs, source and contribution limits. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) | Conditional complete actual good-prime order-group capacities only. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional captured original-root count to complete norm, with all depths retained. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual linear time and complete original norm; accepted Pri11 input scope is unchanged. |
| review | [Review](../audits/reviews/Yin_R_G0353_v1.md#prime-power-harmonic-whole-independent-finding) | Entire fixed proof and22 equations, new chain argument independently reconstructed with antecedent authorship disclosed; full original costs and remaining harmonic-support/coverage limits. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--C, explicit constants, paid strong and weak forms, original-window capture and conditional norm scope. |
| argument | [Exact retained argument](#argument) | All Sections2--7 and22 equations, boundaries, exact costs, source and contribution limits. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Conditional complete actual good-prime order-group capacities only. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional captured original-root count to complete norm, with all depths retained. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional actual linear time and complete original norm; accepted Pri11 input scope is unchanged. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0353_v1.md#prime-power-harmonic-whole-independent-finding) | Entire fixed proof and22 equations, new chain argument independently reconstructed with antecedent authorship disclosed; full original costs and remaining harmonic-support/coverage limits. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--C, explicit constants, paid strong and weak forms, original-window capture and conditional norm scope. |
| argument | [Exact retained argument](#argument) | All Sections2--7 and22 equations, boundaries, exact costs, source and contribution limits. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#frobenius-inversion-capacity) | Conditional complete actual good-prime order-group capacities only. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional captured original-root count to complete norm, with all depths retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Conditional actual linear time and complete original norm; accepted Pri11 input scope is unchanged. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0353_v1.md#prime-power-harmonic-whole-independent-finding) | Entire fixed proof and22 equations, new chain argument independently reconstructed with antecedent authorship disclosed; full original costs and remaining harmonic-support/coverage limits. |
