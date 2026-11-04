---
author: Yin
---

# Weak fractional moments and alternative density mechanisms

Date: 2026-10-15.
Human author Yin.
Continuing author inquiry under the explicitly resumed G0001 goal.
This working material carries no independent review or adopted theorem.

## Responsible question and starting scope

Investigate the genuinely weaker L1 capacity fractional-lcm moment from L396 or a genuinely different fixed-positive-density mechanism.
Existing strong-norm and universal-K counterexamples are inputs, not targets to repeat.
Permit exploratory leaps beyond dyadic interpolation and keep every needed actual-capacity, realization and near-one limitation explicit.
Initial inputs: L396, C101, C99, C96 and C98.

## Current investigation

2026-10-14T19:14.
The delegated g_bridge_audit AI authors the mathematics below.
Root supplied the weak-moment question and independent allocation, not the prime-chain proof.
The general L1 capacity inequality remains open.
This round proves it, with the sharp universal constant for that class, on arbitrary prime-power PRODUCT profiles; it also proves a bounded-product-envelope extension, its no-log density consequence, and a uniform bound on the actual integer strong-norm counterexamples from L396.
These are author deductions awaiting independent whole review.
No native computation has been proposed or executed.

<a id="weak-fractional-reuse"></a>
## 1. Reuse, source screen and exact target

Read [L396](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) in full, the weighted-band and density transfer of [C101](Yin_C_G0101_v1.md#nonlinear-triple-weighted-two-band), [C99's full squarefree downset theorem](Yin_C_G0099_v1.md#statement), [C100's actual-input conventions](Yin_C_G0100_v1.md#statement), and [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001).
The proposed weak estimate is precisely

    E_s(w):=sum_(a,b) w_a w_b/lcm(a,b)^s
          <=K_s W^(2-s),  W=sum_a w_a, 0<s<1,                 (1)

on finite arrays with0<=w_a<=phi(a).
Integer positive weights are the actual arithmetic specialization; zero weights are omitted.
L396's FALSE strong L^q estimate has a smaller right side and does not refute(1).
C99 covers FULL squarefree threshold downsets, not arbitrary thinnings.
C100 covers prime-power supports, not arbitrary multiplicative products of prime-power levels.
None is silently enlarged here.

A bounded primary-source search on2026-10-15 queried totient-weighted fractional lcm energies, GCD sums and subset inequalities.
The actual Cambridge-hosted preprint [Bloom--Walker, GCD sums and sum-product estimates, arXiv:1806.07849v1](https://api.repository.cam.ac.uk/server/api/core/bitstreams/dd9d0c20-1346-4aa4-830b-9fa6b518aa4b/content) was read at the definition and Theorems1--2, pp.1--2: it controls a different normalized GCD kernel, with coefficient and multiplicative-energy hypotheses, and does not state(1).
The primary arXiv abstract of [Bondarenko--Hilberdink--Seip, Gál-type GCD sums beyond the critical line](https://arxiv.org/abs/1512.03758) states a distinct-integer GCD-sum estimate with a logarithmic factor; its Reading-hosted PDF returned access denied.
The publisher endpoint for Curtin--Pourgholi's *An Euler totient sum inequality* failed; its university repository identifies a power-graph/clique subject, but its theorem body was not read.
These are screened related leads only, not adopted proof inputs.
No exact general capacity inequality was located in this bounded screen; no novelty or nonexistence claim follows.

The following proof is finite elementary algebra: packing on one prime-power chain, exact product factorization and an explicitly constructed positive-semidefinite lcm kernel.
Euler-product convergence is proved below without a prime asymptotic.
The totient identity sum_(j=0)^e phi(p^j)=p^e is the same elementary identity used in the fixed C99/C100 arguments.
No new external theorem, literature registration or source-proof upgrade is needed for the deductions.

<a id="product-fractional-moment-statement"></a>
## Statement of the bounded result

Fix ANY0<s<1 and t=2-s.
Define the finite positive constant

    K_s=product_(all primes p) (1-p^-2)/(1-p^-t).

**A. Sharp product class.**
A finite product profile is any array of the form(7), with arbitrary real local masses0<=u_(p,j)<=phi(p^j), finitely many primes and finite prime-power ranges.
For every such nonzero profile of mass V,

    sum_(a,b) v_a v_b/lcm(a,b)^s<=K_s V^t.

For a fixed prime-power ambient N, the sharper constant is product_(p^e||N)K_(p,e) from(2); it is attained by the full array v_a=phi(a) on ALL divisors of N.
The constant K_s is optimal uniformly over all finite product profiles.
All small primes, zero local levels, arbitrary real thinning and the empty ambient are included.
No independence of arbitrary capacity arrays is asserted.

**B. Controlled product majorants.**
Suppose a finite nonzero nonnegative array w of mass W is dominated by L nonzero product profiles of masses V_1,...,V_L with sum V_j<=A W.
Then

    E_s(w)<=K_s (sum_j V_j^(t/2))^2
          <=K_s L^s A^t W^t.

The existence of uniformly bounded L,A is an ADDITIONAL hypothesis, not a conclusion.

**C. Positive-density capture and actual arithmetic use.**
For the full ordered triple mass and peak divisor mass in(13), positive delta=T_X/W^3 and the hypotheses of B imply

    H_X>=(delta/[K_s L^s A^t])^(1/s) W^2/X.

Thus fixed positive density at X=O(W), with fixed L,A, forces fixed positive-proportion capture.
Applied to ACTUAL complete good-prime root groups with W>=gamma d and X<=Cd, it supplies the full original norm income(17), hence the existing L168 class-specific positive Mahler consequence.
All these actual coverage assumptions remain essential and unproved automatically near one.

**D. Exact old-counterfamily control.**
The real product and the all-positive floor/dilation integer arrays used to refute L396's stronger L^(2/t) inequality satisfy, respectively, E_s<=K_s W^t and E_s<=2^t K_s W^t.
Therefore those SAME families do not refute the weaker L1 form.
No new fixed-positive-density or near-one family is asserted.

<a id="product-fractional-moment-argument"></a>
## Complete argument

<a id="prime-chain-sharp-capacity"></a>
## 2. A sharp one-prime chain inequality

Fix0<s<1 and write t=2-s in(1,2).
Let p be prime, e>=0 an integer, c_0=1 and c_j=phi(p^j)=p^j-p^(j-1) for j>=1.
For arbitrary real0<=u_j<=c_j put

    M=sum_(j=0)^e u_j,
    F_s(u)=sum_(i,j=0)^e u_i u_j p^(-s max(i,j)),
    A_(p,e)=1+(1-p^-2)sum_(j=1)^e p^(t j),
    K_(p,e)=A_(p,e)/p^(t e),
    K_p=(1-p^-2)/(1-p^-t).                                  (2)

Empty sums are0; in particular K_(p,0)=1.
Then

    F_s(u)<=K_(p,e) M^t<=K_p M^t.                           (3)

For each fixed p,e the first constant is optimal, attained by u_j=c_j for EVERY0<=j<=e.
This is a statement about actual local masses, including partial or zero levels, not an L^q functional bound.

**Packing proof.**
The assertion is immediate for M=0.
Given M>0, use an interval of length M with its length measure.
Partition it into successive intervals of lengths u_0,u_1,...,u_e and denote the corresponding level function by j_u(x).
For every k, the mass in levels<=k is at most min(M,p^k).
The packed allocation fills lower levels to their capacities before using a higher level, so its cumulative mass in levels<=k is EXACTLY min(M,p^k).
Its analogous function j_*(x) therefore satisfies j_*(x)<=j_u(x) for every x outside finitely many endpoints.
Consequently

    p^(-s max(j_*(x),j_*(y)))
        >=p^(-s max(j_u(x),j_u(y)))

on the entire square apart from a measure-zero finite union of lines.
Integrating proves F_s(u)<=F_s(u_*).
This integral is simply a finite sum over rectangles; no infinite rearrangement theorem is imported.

If0<M<=1, the packed mass lies at level0, so F_s(u_*)=M^2<=M^t.
If M>1, choose1<=k<=e with

    A:=p^(k-1)<=M<=p^k.

The packed allocation is full through level k-1 and has remaining mass M-A at level k.
Pairs with maximum level j have total full-capacity mass p^(2j)-p^(2j-2).
Thus the full prefix energy is A_(p,k-1), and

    F_s(u_*)=A_(p,k-1)+p^(-s k)(M^2-A^2).                 (4)

On the closed interval[A,pA], the derivative of the ratio in(4) to M^t has the sign of

    s p^(-s k) M^2-t[A_(p,k-1)-p^(-s k) A^2].             (5)

This expression increases strictly with M.
Hence the ratio has no strict interior maximum; it is monotone or decreases and then increases.
Its maximum lies at an endpoint.
At the endpoints it equals K_(p,k-1) or K_(p,k).

A finite geometric-series calculation gives

    K_(p,j)=K_p+(1-K_p)p^(-t j).                          (6)

Since K_p>1, these constants increase from1 to K_p.
Every endpoint through level e is therefore at most K_(p,e).
Together with the M<=1 case, this proves(3).
At full capacity M=p^e, the value is exactly A_(p,e), proving optimality.
No estimate of phi(p^j) by p^j replaces its exact capacity in this argument.

<a id="multiplicative-fractional-moment"></a>
## 3. Product profiles, arbitrary prime powers, and the optimal constant

Call v a product profile if, for some finite set of primes P and integers e_p>=0, it has the form

    v_a=product_(p in P) u_(p,v_p(a))  if a divides N,
    v_a=0 otherwise,
    N=product_(p in P) p^e_p,
    0<=u_(p,j)<=phi(p^j), 0<=j<=e_p.                       (7)

Here v_p(a) in the subscript means the p-adic exponent, not the profile value.
To avoid ambiguity in implementation one may denote it ord_p(a).
The empty prime set is permitted and gives v_1=1.
A zero profile has mass0 and is harmless.
All nonzero profiles satisfy0<=v_a<=phi(a); local factors need not be integers.
Missing lower levels, missing order1 and arbitrarily many prime factors are allowed.

Write V=sum_a v_a.
Since lcm is coordinatewise maximum on the prime exponents, finite product expansion gives EXACTLY

    V=product_p M_p,
    E_s(v)=product_p F_s(u_p).

Thus Section2 proves

    E_s(v)<=[product_p K_(p,e_p)]V^t<=K_s V^t,
    K_s:=product_(all primes p) (1-p^-2)/(1-p^-t)<infinity. (8)

The convergence assertion is elementary: every local factor exceeds1 and

    0<log K_p<=K_p-1
      =(p^-t-p^-2)/(1-p^-t)
      <=p^-t/(1-2^-t).

The sum of the last expression over primes is at most its sum over integers>=2, which converges for t>1 by the integral test.
This supplies a fully finite upper constant depending only on s.
The familiar Euler-product notation identifies K_s with zeta(2-s)/zeta(2), but this identification is not required by any estimate.

The constant K_s is OPTIMAL over the entire product-profile class.
For a fixed finite prime set, take all local capacities full and send their finite exponent bounds to infinity; equation(6) makes the ratios tend to the product of its K_p.
Then enlarge the finite prime set.
Each input remains a finite INTEGER totient array on ALL divisors of an actual integer N, with V=N.
This approaches K_s and proves that any constant valid for all capacity arrays in(1), if such a constant exists, must be at least K_s.
No infinite array or passage from abstract weights to a polynomial is involved.

For comparison, on squarefree product profiles the sharper exact finite factor is

    K_(p,1)=1+(p^s-1)/p^2.

Writing y=(p-1)x for the local mass at p, the one-prime ratio is

    [1+(2y+y^2)/p^s]/(1+y)^t, 0<=y<=p-1,

whose derivative has the sign of s y^2+2s y+2-t p^s.
Its only possible interior critical point is a minimum.
This was the starting calculation; Section2 includes arbitrary prime powers and removes the unnecessary assumption that the order1 local mass equals1.

<a id="finite-product-envelope-extension"></a>
## 4. Positive lcm kernel and controlled product envelopes

The kernel K(a,b)=lcm(a,b)^(-s) is positive semidefinite on EVERY finite set of positive integers.
Here is an explicit finite proof, included because a Cauchy--Schwarz bound for an arbitrary positive-entry matrix would be invalid.

Choose a common finite prime-power ambient N containing the support.
At one prime with maximum exponent e, set

    d_k=p^(-s k)-p^(-s(k+1)) for0<=k<e,
    d_e=p^(-s e).

All d_k are positive, and for0<=i,j<=e,

    p^(-s max(i,j))=sum_(k=0)^e d_k 1_(i<=k)1_(j<=k).    (9)

This is the Gram matrix of vectors with coordinates sqrt(d_k)1_(i<=k).
Taking tensor products of these FINITE vectors over primes gives Gram entries product_p p^(-s max(v_p(a),v_p(b)))=K(a,b).
This proves positive semidefiniteness directly.
Its Gram inner product therefore gives, for finite real arrays x,y,

    |sum_(a,b) x_a y_b K(a,b)|<=sqrt(E_s(x)E_s(y)).        (10)

Let a nonnegative actual array w be pointwise dominated by a finite sum of L nonzero product profiles,

    w_a<=sum_(j=1)^L v_a^(j),
    V_j=sum_a v_a^(j),
    sum_j V_j<=A W,  W=sum_a w_a>0, A>=1.                (11)

Profiles may overlap and may use different prime sets or exponent caps.
No product decomposition or envelope is asserted to exist with uniformly bounded L,A for all arrays.
Positivity of each kernel entry, then(10) and(8), gives

    E_s(w)<=E_s(sum_j v^(j))
       <=(sum_j sqrt(E_s(v^(j))))^2
       <=K_s (sum_j V_j^(t/2))^2
       <=K_s L^s (A W)^t.                               (12)

The last inequality is the elementary finite concavity bound for exponent t/2=1-s/2.
The earlier expression retaining every V_j is sharper; the bound by L^s records its full component-count cost.
This does NOT repeat L396's false strong-norm estimate: the profiles in(11) obey their exact multiplicative capacity structure, and no arbitrary function is substituted for them.
In particular(12) alone gives no uniform constant when the component count or envelope mass ratio diverges.

<a id="product-envelope-density-capture"></a>
## 5. No order-scale loss for covered positive-density arrays

Let w be a nonzero finite nonnegative capacity array, W its mass, X>=1 an integer, and

    H_X=max_(integer1<=n<=X)sum_(a|n)w_a,
    T_X=sum_(lcm(a,b,c)<=X)w_a w_b w_c,
    delta=T_X/W^3>0.                                    (13)

Every tuple is ordered and repeated labels are included.
We retain the OLD residual-bucket mechanism of C91/L396, with its short proof to make the exact new interface transparent.
For fixed a,b put L=lcm(a,b).
For a compatible third order c, set r=c/gcd(c,L).
Then lcm(c,L)=Lr<=X, and c divides Lr.
For each fixed r its entire third-order mass is at most H_X, since Lr<=X.
There are at most floor(X/L) such positive integers r.
Therefore the third mass is at most min(W,XH_X/L).
For0<s<1, min(1,z)<=z^s for z>=0, so

    T_X<=W (XH_X/W)^s E_s(w).                            (14)

No good-prime assumption is used in this purely finite arithmetic statement.

If w satisfies the product-envelope condition(11), then(12)--(14) give

    H_X >= (delta/[K_s L^s A^t])^(1/s) W^2/X.             (15)

In particular, for fixed positive delta0,C0 and fixed finite L,A, every such array with T_X>=delta0 W^3 and X<=C0 W satisfies

    H_X/W >= C0^-1 (delta0/[K_s L^s A^t])^(1/s)>0.        (16)

This has NO number-of-dyadic-scales factor and no bound on the union of order primes.
The constant depends on the explicitly supplied product-envelope complexity and excess mass.
The pure product case has L=A=1.
One may fix s=1/2, giving K_(1/2)=zeta(3/2)/zeta(2) and the fully displayed constant; no optimization or limiting choice of s is needed.

**Actual norm consequence, conditionally on this coverage.**
Let P be the ACTUAL monic irreducible nontorsion integer-unit minimal polynomial, with original degree d, root alpha and original field K.
At an ACTUAL good prime p not dividing disc(P), select COMPLETE order groups of reduced roots with integer masses w_a.
They satisfy w_a<=phi(a), with the separate Frobenius multiplicity condition still enforced.
Assume W>=gamma d for fixed gamma>0, integer X<=Cd, triple density at least delta0>0, and a product envelope with fixed L,A.
Then one actual n<=X captures at least eta0 d, where

    eta0=(gamma^2/C)(delta0/[K_s L^s A^t])^(1/s)>0.

Since every captured original p-adic root has positive integral valuation in alpha_i^n-1 at this unramified good prime, its valuation is at least1.
The original full norm therefore satisfies

    log|Norm_(K/Q)(alpha^n-1)|
       >=(log p) v_p(Norm_(K/Q)(alpha^n-1))
       >=eta0 d log2.                                  (17)

Every original embedding, additional root/depth, other prime contribution, signed resultant, and possible degree drop after powering remains in this original-field norm.
The auxiliary t^n-1 has its actual degree n, content1 and squared coefficient norm2.
This is exactly the existing [L168 finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), giving its class-specific positive Mahler lower bound with the inherited source-inspection limits.
The lower norm income uses actual selected roots; real profiles serve only as a proved majorant for their mass array.
No profile is assumed to be a possible Frobenius inventory merely because it meets phi capacities.

The new combinatorial class is nonempty at the actual-input level: the old control P=t^2-3t+1 at good prime2 has only order3 mass2.
It is a product profile with local factors u_(3,0)=0,u_(3,1)=2.
At X=3 its triple density is1 and H_X=W=2; its actual signed norm is-16, as already proved in C100.
This repeats an established control to verify the interface, not as a new construction or near-one family.
No automatic coverage of near-one polynomials is proved.

<a id="strong-failure-weak-control"></a>
## 6. The old strong-norm counterexamples obey a uniform weak bound

L396's finite counterexample fixes the SAME s and t=2-s, an odd squarefree Q, and real masses

    r_a=phi(a)a^(-t) for a|Q, otherwise0.

These are product profiles: u_(p,0)=1 and u_(p,1)=(p-1)p^(-t).
Hence they satisfy the weak estimate(8) with the uniform constant K_s, while the different strong L^(2/t)-norm ratio in L396 diverges.
This explains, by a positive theorem rather than a mere logical possibility, why that real family does not refute the weak question.

The EXACT integer transfer from L396 retains the same conclusion with a uniform factor.
Let v=2^k, c=phi(v)=2^(k-1), and choose k large enough that EVERY value

    R_(va)=c phi(a)a^(-t), a|Q,

is at least1; define w_(va)=floor(R_(va)), with zero weights elsewhere.
R itself is a product profile on2^k Q: its2-coordinate is zero except at exponent k, where it equals c, and its odd-prime coordinates are as above.
Every w is a positive INTEGER within phi(va), and for every x>=1, floor(x)>=x/2.
Thus

    R/2<=w<=R pointwise,
    sum R<=2 sum w,
    E_s(w)<=K_s (sum R)^t<=2^t K_s (sum w)^t.             (18)

This is uniform in BOTH the finite Q and every sufficiently large k for which L396's all-positive construction is defined.
It is not just a fixed-Q limiting argument.
Its strong-norm ratio can still diverge exactly as L396 proved.
Equation(18) does not assert a fixed positive triple density or an actual polynomial lift; neither was supplied by that counterexample.
It proves that the already retained strong-norm obstruction cannot be repurposed as a weak-moment counterfamily.

<a id="product-cover-unresolved-boundary"></a>
## 7. Scope, remaining obstruction and next discriminator

The general inequality(1) for arbitrary correlated capacity arrays is STILL unproved and unrefuted.
The sharp product theorem does not make arbitrary prime exponent coordinates independent.
The explicit tensor factorization in Section3 applies only when the weights themselves factor.
Replacing a correlated array by a product with the same one-prime marginals has no established energy comparison here.

Likewise Section4 does not remove its L^s or excess-mass A^t costs.
The elementary single-order decomposition of an arbitrary array supplies finitely many product pieces, but its growing count does not solve the desired uniform estimate.
No theorem of uniformly bounded product-cover complexity is asserted.
Proving that positive triple density forces a useful bounded-cost cover or a captured divisor mass, or finding a genuinely positive-density array escaping every such localization, is a concrete next question.
The former L396 equal-band example has vanishing density and does not answer it.

C99's COMPLETE squarefree threshold downset theorem and this arbitrary-prime-power PRODUCT theorem have different domains.
A threshold cut a<=X generally correlates prime coordinates and need not preserve product factorization.
Conversely product weights can be partial and need not form a complete threshold downset.
No dominance between these two existing/new mechanisms is claimed.

The attempted broad route through a generic strong L^q inequality stays refuted.
The present proof avoids it rather than repairs it.
A naive componentwise Cauchy extension produces exactly the explicit complexity factor in(12), which is the unresolved cost, not a hidden general proof.
The full account contains no fixed-positive-density counterexample, no near-one realization, no uniform automatic root coverage and no completion of G0001.

Current author checks reconstructed the finite packing coupling, all boundary M=0/M<=1/e=0 cases, the derivative sign and endpoint ratios, exact prime-capacity products and Euler convergence, the finite tensor Gram proof, the component-count exponent, residual bucket grouping, every actual original norm convention, and the uniform floor factor in(18).
These are author checks only.
The record is being prepared for a separate noncontributing whole review; no Claim registration or acceptance is asserted.

<a id="product-fractional-entire-author-freeze"></a>
## Entire bounded-round author freeze

2026-10-14T19:20.
The complete original artifact is frozen for a noncontributing WHOLE review: the exact statement A--D, Sections1--7 and equations(1)--(18), finite sharp constants and global sharpness, p=2 and all local degeneracies, every component/envelope cost, the actual original-root conditional transfer and inherited L168 scope, the direct control of L396's SAME integer counterfamily, source screening and all unresolved limits.
The explicit statement and argument anchors above permit direct fixed retention without a separate mathematical wrapper.
The scoped material check passed for this one D; it is structural validation, not a proof check.
No mathematical program, J, empirical test or new source adoption was performed by this author.
Subsequent substantive changes require an explicit correction or distinct continuing material; this freeze is author completion, not independent acceptance or completion of G0001.

## Fixed organization

The entire author original above is retained at its actual final freeze, including source searches, contributor accounts, unsuccessful methods and all limitations.
Author-stage wording records history.
This actual fixed artifact, including the exact statement and complete argument, awaits a separately organized noncontributor whole review.
Allocation asserts no accepted mathematics.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

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
| statement | [Exact statement](#product-fractional-moment-statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#product-fractional-moment-argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) | Precise weak-versus-strong question and retained actual counterfamilies. |
| dependency | [Exact input](Yin_C_G0100_v1.md#statement) | Actual good-prime root-count, norm and fixed quadratic-control interfaces. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure consequence. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:31 |
| status | proved |
| reason | Adopt [R797 original product-fractional](../audits/reviews/Yin_R_G0797_v1.md#product-fractional-whole-independent-finding)'s separately organized complete review of this actual statement, entire retained proof and selected inputs. Sharp product-profile constants, controlled product-envelope capture, full actual-norm conditional transfer and uniform weak bounds for the retained strong counterfamilies are proved at their exact scopes. General correlated capacities, automatic near-one coverage and the original unrestricted gap remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#product-fractional-moment-statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Complete argument](#product-fractional-moment-argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact input](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) | Precise weak-versus-strong question and retained actual counterfamilies. |
| dependency | [Exact input](Yin_C_G0100_v1.md#statement) | Actual good-prime root-count, norm and fixed quadratic-control interfaces. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure consequence. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0797_v1.md#product-fractional-whole-independent-finding) | Entire actual A--D and argument, all finite and limiting cases, source boundaries and complete original-norm interface. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#product-fractional-moment-statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact retained argument](#product-fractional-moment-argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0396_v1.md#subcritical-capacity-moment-and-failed-strong-form) | Precise weak-versus-strong question and retained actual counterfamilies. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#statement) | Actual good-prime root-count, norm and fixed quadratic-control interfaces. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure consequence. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0797_v1.md#product-fractional-whole-independent-finding) | Entire actual A--D and argument, all finite and limiting cases, source boundaries and complete original-norm interface. |

### Decision current-strong-norm-counterexample-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:42 |
| status | proved |
| reason | Select newly adopted C472 as the complete same-object home of exactly the already-used L396 weak-versus-strong distinction and original counterfamilies. Every mathematical conclusion, current status, complete proof, source depth, existing review and all other relations/scopes stay unchanged. This current locator maintenance does not move old dated reading facts, establish historical isolation or import C142 as a dependency. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#product-fractional-moment-statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact argument](#product-fractional-moment-argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact dependency](Yin_C_G0472_v1.md#subcritical-capacity-moment-and-failed-strong-form) | Precise weak-versus-strong question and retained actual counterfamilies. |
| dependency | [Exact dependency](Yin_C_G0100_v1.md#statement) | Actual good-prime root-count, norm and fixed quadratic-control interfaces. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure consequence. |
| review | [Exact review](../audits/reviews/Yin_R_G0797_v1.md#product-fractional-whole-independent-finding) | Entire actual A--D and argument, all finite and limiting cases, source boundaries and complete original-norm interface. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:38 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. Sharp finite and infinite product-class constants, controlled product-envelope capture, complete original-norm transfer and the exact old-counterfamily weak bounds are supported at their stated domains. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#product-fractional-moment-statement) | All enumerated conclusions at their stated domains and limits. |
| argument | [Exact argument](#product-fractional-moment-argument) | All retained proofs, controls, boundaries and actual source interfaces. |
| dependency | [Exact dependency](Yin_C_G0472_v1.md#subcritical-capacity-moment-and-failed-strong-form) | Precise weak-versus-strong question and retained actual counterfamilies. |
| dependency | [Exact dependency](Yin_C_G0100_v1.md#statement) | Actual good-prime root-count, norm and fixed quadratic-control interfaces. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Actual original-norm positive-measure consequence. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0104-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. |

