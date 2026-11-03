---
author: Yin
---

# Exact cyclic-norm content, finite local tables and all-exponent tail certificates

This retains the complete original 2026-10-07 proof of [L74](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm).
The native J11 computations stay in their existing responsible home and are not premises of this theorem.

## Statement

Let alpha be a nontorsion algebraic unit, K=Q(alpha), O=O_K, d=[K:Q], P its monic irreducible polynomial and m=log M(P)>0.
For every n>=1 put z_n=alpha^n-1, C_n=|Norm_(K/Q)z_n| and g_n=max{g>=1:z_n in gO}.
At prime ideals q|p with integer valuation ord_q and ramification/residue degrees e_q,f_q,

    v_p(g_n)=min_(q|p) floor(ord_q(z_n)/e_q),
    v_p(C_n)=sum_(q|p)f_q ord_q(z_n),
    g_n^d divides C_n,
    m>=[log C_n-d log2]/n>=d log(g_n/2)/n.

Content is precisely simultaneous identity periods modulo p^k O; its contribution must not be counted twice with the full ideal norm.
For distinct supplied prime ideals and certified w_q<=ord_q(z_n), let A(n)=sum_q f_q w_q logp_q.
Then m>=[A(n)-d log2]/n.
If fixed epsilon,C>0 give A(n)>=(1+epsilon)d log2 and n<=C A(n) for each input, then m>=epsilon/[(1+epsilon)C], yielding restricted finite capture with positive multiplicities.
Content g_n>=3 and n<=Cd logg_n is a separate sufficient condition, including the stated identity-period budgets with the explicit binary squaring cost.
Different exponents retain their sum-of-denominators cost.
For any fixed alpha and finite rational-prime set S, actual content and norm valuations obey

    log(g_n)_S<=B_(alpha,S)+logn,
    log(C_n)_S<=B'_(alpha,S)+d logn.

The complete proof includes all ramification, initial cancellation, prime-to-p cofactors and p2.
At any fixed p, let O_p be the distinct reduced-root orders, w_o their total degrees including multiplicities, and R_p=min{k>=0:p^k>=d}+1.
With B_(o,r) the sum of normalized original-root depths at exponent op^r,

    B_(o,r)=B_(o,R_p)+w_o(r-R_p) for r>=R_p,
    B_(o,r)=v_p(C_(op^r))-sum_(o'<o,o'|o)B_(o',r) for 0<=r<=R_p,
    v_p(C_n)=sum_(o|n)[B_(o,min(v_p(n),R_p))+w_o max(v_p(n)-R_p,0)].

The complete finite modular determinant procedure terminates by nontorsion without a maximal-order basis; no uniform precision or efficiency is claimed.
The exact table yields nonnegative integer divisibility events, a computable H_S and the decreasing tail [H_S+d logn-d log2]/n.
A certified strictly positive incumbent then gives a finite all-n optimization of that actual S-part, without guaranteeing that such an incumbent exists.
For a finite nonempty set of good primes, use all original root multiplicities w_(p,o), k_p(n)=sum_(o|n)w_(p,o), and

    A_S(n)=sum_(p in S) k_p(n)(1+v_p(n))logp,
    log C_n>=A_S(n),
    B_S(n)=[A_S(n)-d log2]/n<=d log(Rn/2)/n,
    R=product_(p in S)p.

These are automatic floors, including p2 and all deeper actual contributions on the left, without a second residue-degree multiplier.
The complete integer event sieve, monotonicity threshold RX/2>e, strict certified tail cutoff, interval refinement and exact tie rule prove a conditional finite global maximum for every positive integer n.
No native execution, J11 numerical result, scalar-period coverage, uniform near-one arithmetic theorem or unrestricted Lehmer gap is a premise or result of this proof.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:36 |
| status | open |
| reason | Register the entire retained original proof with explicit statement and exact existing interfaces; current whole review and any adoption follow separately. This performs no source acquisition, native execution or research resumption and claims no independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | All exact content/ideal formulas, same-exponent sufficient criteria, fixed-prime actual growth, finite exact table/reconstruction/procedure and both full/floor event-sieve/global-tail statements. |
| argument | [Complete argument](#argument) | Every original proof and nonvanishing, ramification, multiplicity, p2, initial-cancellation, incumbent and interval/tie guard; J11 results are not proof premises. |
| dependency | [Elementary ramified lift](Yin_C_G0254_v1.md#ramified-valuation-capture) | Complete normalized-valuation binomial/capped-recurrence argument at the actual fractional depth; exact stable slope and all-n table are proved here. |
| dependency | [Finite capture](Yin_C_G0205_v1.md#capture-equivalence) | Common positive gap on positive irreducible constituents with multiplicity implies restricted finite capture. |
| support | [Neutral separation](Yin_C_G0252_v2.md#positive-whole-flow-neutral-obstruction) | Torsion identity exponents have zero norm and must be separated; no whole-flow neutral period target is imposed. |
| support | [Identity-period budget](Yin_C_G0251_v1.md#identity-period-log-prime-budget) | Only the existing sufficient budget inclusion, retaining explicit binary squaring and no optimal-constant claim. |
| support | [Mixed-resultant comparison](Yin_C_G0241_v1.md#frobenius-repetition-hypotheses) | Different existing repetition mechanism; current cyclic norm uses one actual exponent and complete original field. |
| support | [Powered Vandermonde comparison](Yin_C_G0242_v1.md#measured-nullity-cost-and-certificate) | Distinct earlier finite certificate with power-degree and exponent costs; none of its computations is a premise. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:40 |
| status | proved |
| reason | Adopt the complete original content/ideal aggregation, ramified growth, exact local-table reconstruction/procedure and both all-exponent event-sieve/tail proofs after actual whole current self-review. Full original norms, all depths, input-dependent cancellation, positive-incumbent and strict interval/tie conditions are retained; J11 results are not theorem premises and no native program was rerun. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All exact content/ideal formulas, same-exponent sufficient criteria, fixed-prime actual growth, finite exact table/reconstruction/procedure and both full/floor event-sieve/global-tail statements. |
| argument | [Argument](#argument) | Every original proof and nonvanishing, ramification, multiplicity, p2, initial-cancellation, incumbent and interval/tie guard; J11 results are not proof premises. |
| dependency | [Dependency](Yin_C_G0254_v1.md#ramified-valuation-capture) | Complete normalized-valuation binomial/capped-recurrence argument at the actual fractional depth; exact stable slope and all-n table are proved here. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Common positive gap on positive irreducible constituents with multiplicity implies restricted finite capture. |
| support | [Support](Yin_C_G0252_v2.md#positive-whole-flow-neutral-obstruction) | Torsion identity exponents have zero norm and must be separated; no whole-flow neutral period target is imposed. |
| support | [Support](Yin_C_G0251_v1.md#identity-period-log-prime-budget) | Only the existing sufficient budget inclusion, retaining explicit binary squaring and no optimal-constant claim. |
| support | [Support](Yin_C_G0241_v1.md#frobenius-repetition-hypotheses) | Different existing repetition mechanism; current cyclic norm uses one actual exponent and complete original field. |
| support | [Support](Yin_C_G0242_v1.md#measured-nullity-cost-and-certificate) | Distinct earlier finite certificate with power-degree and exponent costs; none of its computations is a premise. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0527_v1.md#current-cyclic-table-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; original findings retain their actual old inputs and scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="content-versus-ideal-norm"></a>
### Exact content and prime-ideal contributions

Let alpha be a nontorsion algebraic unit, K=Q(alpha), O=O_K, d=[K:Q], P its monic irreducible polynomial, and m=log M(P)>0.
All logarithms are natural.
For n>=1 put

    z_n=alpha^n-1,
    C_n=|Norm_(K/Q)(z_n)|,
    g_n=max{g in Z, g>=1 : z_n in g O}.

These are finite and nonzero because alpha is nontorsion.
The maximum is the positive gcd of the coordinates of z_n in any integral basis of O, so it does not depend on that basis.
At a prime ideal q above p, write e_q and f_q for its ramification index and residue degree, and ord_q for the integer valuation with ord_q(q)=1.
Unique factorization of nonzero ideals gives the exact formulas

    v_p(g_n)=min_(q|p) floor(ord_q(z_n)/e_q),
    v_p(C_n)=sum_(q|p) f_q ord_q(z_n).                         (1)

Indeed p^k O has q-exponent k e_q, while Norm(q)=p^f_q.
Also sum_(q|p) e_q f_q=d.
Thus g_n^d divides C_n.
The first formula retains the weakest direction over p, with a floor; the second retains every direction with its residue-degree weight.
Neither unramifiedness nor degree preservation by alpha^n is required.

Since alpha is a unit, its reduction in (O/p^k O)^* has a finite order T_(p^k).
Equivalently,

    p^k divides g_n  if and only if  T_(p^k) divides n.        (2)

This describes content as simultaneous identity periods.
Formula (1), in contrast, can detect contributions from a proper subset of the prime ideals over each p.
One must not multiply the content bound by the full ideal bound: the content contribution is already included in (1).

At the complex embeddings, |alpha_i^n-1|<=2 max(1,|alpha_i|)^n.
Consequently

    C_n<=2^d exp(nm),
    m>=[log C_n-d log 2]/n
       >=d log(g_n/2)/n.                                    (3)

Torsion inputs are excluded for a substantive reason: z_n is zero at their identity exponents, and neither a finite content nor a nonzero norm bound is available there.
Neutral constituents of a flow must first be separated as in [L G0071](Yin_C_G0252_v2.md#positive-whole-flow-neutral-obstruction).

<a id="aggregate-cyclic-norm-criterion"></a>
### A sufficient aggregate condition and its scope

Fix one n.
Suppose a finite set of prime ideals is supplied with certified lower bounds w_q>=0 for ord_q(z_n).
Set

    A(n)=sum_q f_q w_q log p_q.

The bounds may be real, although exact local valuations are integers.
Distinct ideals are counted once; at an ideal with several lower bounds, retain their maximum unless disjoint valuation layers have actually been proved.
Equations (1)--(3) give

    m>=[A(n)-d log 2]/n.                                     (4)

In particular, fix epsilon,C>0.
If every input in a class admits n and such local data with

    A(n)>=(1+epsilon)d log 2,    n<=C A(n),                    (5)

then every input in that class satisfies

    m>=epsilon/[(1+epsilon)C]>0.                             (6)

The primes and ideals can vary with the input, and no single prime need annihilate all reduced roots.
If all positive irreducible constituents of a finite-entropy rational flow, counted with multiplicity, satisfy (5) with common constants, (6) makes their number finite.
This is the restricted-class finite capture in [L G0002](Yin_C_G0205_v1.md#capture-equivalence).

For content alone, a convenient sufficient condition is

    g_n>=3,    n<=C d log g_n.

Then (3) gives m>=log(3/2)/(C log 3).
It includes the odd-prime identity budget T_p<=C d log p from [L G0070](Yin_C_G0251_v1.md#identity-period-log-prime-budget): take n=T_p and use g_n>=p.
At p=2, alpha^T-1 in 2O implies alpha^(2T)-1 in 4O, so n=2T also satisfies the displayed content budget when T<=C d log 2.
This inclusion is an implication between sufficient conditions, not a claim of optimal numerical constants.

The aggregate formula (4) applies even when g_n=1 and every prime contributes only partially.
It is a genuinely additional kind of finite certificate.
No family has here been proved to separate the corresponding *uniform coverage hypotheses* on irreducible units near Mahler measure one.
Allowing every prime ideal with its exact valuation merely sets A(n)=log C_n; it does not establish (5).
Different-exponent estimates cannot be multiplied without cost: generic bounds C_(n_i)<=2^d exp(n_i m) give a ratio of sums, hence a weighted average of the separate quantities [log C_(n_i)-d log 2]/n_i.
An improvement from such products needs additional joint archimedean information.

<a id="fixed-prime-actual-growth"></a>
### Fixed primes have only logarithmic actual valuation growth

For this fixed nontorsion alpha and any fixed finite set S of rational primes, there are finite constants B_(alpha,S) and B'_(alpha,S), independent of n, such that

    log (g_n)_S <= B_(alpha,S)+log n,
    log (C_n)_S <= B'_(alpha,S)+d log n.                      (7)

Here (a)_S=product_(p in S) p^v_p(a) is the S-part of a positive integer.
This includes ramified primes and p=2.

Proof.
Fix q|p and normalize v=ord_q/e_q, so v(p)=1.
Let t be the multiplicative order of the residue of alpha in (O/q)^*.
Then t is prime to p.
If t does not divide n, v(z_n)=0.
Otherwise write n=t p^s u, with u>=1 prime to p and s=v_p(n).
For x with v(x-1)>0, expansion gives

    v(x^p-1)>=min(v(x-1)+1,p v(x-1)),
    v(x^u-1)=v(x-1) if p does not divide u.                  (8)

In the second formula the linear term u(x-1) is the unique term of lowest valuation; all later terms have valuation at least 2v(x-1).
The first formula is the elementary lift used in [L G0072](Yin_C_G0254_v1.md#ramified-valuation-capture).

Put v_j=v(alpha^(t p^j)-1).
It is finite, and v_0>=1/e_q.
Let k be the least integer with p^k>=e_q, and h=k+1.
The first formula of (8), with its value capped at one, gives v_k>=1 and then v_h>=2.
Whenever v(x-1)>=2, the term p(x-1) is the unique lowest term of x^p-1: the middle terms have valuation at least 1+2v(x-1), and p v(x-1)>1+v(x-1).
Therefore

    v_j=v_h+j-h for every j>=h.

The finite nonnegative constant

    b_q=max(0, max_(0<=j<=h)(v_j-j))

thus satisfies v(z_n)<=v_p(n)+b_q for every n, including t not dividing n.
The constant records possible initial cancellation; it is not bounded merely by e_q.
For each p take b_p=max_(q|p) b_q.
Formula (1) now gives

    v_p(g_n)<=v_p(n)+b_p,
    v_p(C_n)<=d v_p(n)+sum_(q|p)e_q f_q b_q.

Summing over S, and using sum_(p in S)v_p(n)log p<=log n, proves (7), with explicit constants obtained from these finite initial valuations.
This completes the proof.

In particular the actual norm contribution from a fixed finite S has zero exponential rate as n tends to infinity.
These constants depend on alpha and S; (7) neither bounds finite-time certificates uniformly across inputs nor rules out a useful positive certificate at a small exponent.
A proposed asymptotic mechanism must control the initial depths or allow the prime set to change.
No assertion about a uniform rate over varying inputs follows from (7).

<a id="finite-exact-local-cyclic-table"></a>
### Finitely many exact norms determine the entire local sequence

The preceding eventual slope has a finite, effective description that does not require computing a maximal-order basis.
Fix any rational prime p, now allowing p to divide disc P.
Factor P modulo p.
Let O_p be the finite set of distinct multiplicative orders o of its nonzero roots, and let w_o be the total degree of all factors with that order, including their multiplicities in P modulo p.
The constant term of P is a unit, so all these orders are defined; they are prime to p, and sum_o w_o=d.

Choose a finite p-adic splitting field and label the original d roots alpha_i.
For o in O_p and r>=0 define

    B_(o,r)=sum_(i: order of residue alpha_i = o)
                    v(alpha_i^(o p^r)-1),
    R_p=min{k>=0:p^k>=d}+1.                                 (8a)

Each individual root generates a local field of degree at most d.
Its initial positive valuation is at least the inverse of that field's ramification index, hence at least 1/d.
A common splitting field need not have ramification index at most d; it is the individual root field that supplies this bound.
The proof of (8) therefore gives valuation at least two after R_p powerings and exact slope one thereafter.
In particular,

    B_(o,r)=B_(o,R_p)+w_o(r-R_p) for r>=R_p.                  (8b)

All finite initial entries can be recovered from cyclic norms:

    B_(o,r)=v_p(C_(o p^r))
               -sum_(o' in O_p: o'|o, o'<o) B_(o',r),
           0<=r<=R_p.                                     (8c)

To see this, a root contributes to C_(o p^r) exactly when its residue order o' divides o.
Then o/o' is prime to p, so its valuation equals that at exponent o'p^r by (8).
Processing o in increasing order proves (8c) and, in particular, proves that each B_(o,r) is an integer despite its definition as a sum of normalized valuations.
No irreducibility of P modulo p or separation of powered roots is being assumed.

For arbitrary n>=1 put r=v_p(n).
The exact reconstruction is

    v_p(C_n)=sum_(o in O_p: o|n)
        [B_(o,min(r,R_p))+w_o max(r-R_p,0)].                 (8d)

The same prime-to-p cofactor argument proves it.
Thus finitely many values C_(o p^r), used only through their p-valuations, determine the actual p-part for every n.

For completeness, those valuations themselves admit a terminating exact modular procedure.
In the free rank-d quotient by the monic polynomial P over Z/p^K Z, compute t^(o p^r)-1 by repeated squaring and take the determinant of its multiplication map.
The determinant is C_(o p^r) up to sign modulo p^K.
Increase K until it is nonzero modulo p^K.
Its p-valuation is then the exact valuation of the nonzero integer norm.
Nontorsion guarantees termination.
This is an exact finite procedure, not an assertion of a uniform efficient bound on the required initial precision or residue orders.

At a good odd prime one may replace R_p by zero: each initial valuation is at least one, already strictly larger than 1/(p-1), which makes the linear binomial term unique.
At a good prime p=2, R_p=1 suffices, because the first squaring raises valuation to at least two.
These sharper thresholds concern actual valuations, not just their automatic floors.

The table also provides a computable tail constant.
Put

    b_(p,o)=max_(0<=r<=R_p)[B_(o,r)-w_o r],
    H_p=sum_(o in O_p) b_(p,o),
    H_S=sum_(p in S) H_p log p.                             (8e)

Each b_(p,o)>0 because the r=0 entry is positive.
Equations (8b)--(8d) imply, for every n,

    log(C_n)_S<=H_S+d log n,
    [log(C_n)_S-d log 2]/n
           <=[H_S+d log n-d log 2]/n.                      (8f)

The right side decreases as soon as H_S/d+log n-log 2>1.
Any strictly positive certified incumbent, with a cutoff at which this decreasing upper bound lies below it, therefore reduces the exact all-n optimization to a finite set.
This conclusion applies to the actual S-part, not only to lower bounds for it.

An exact sieve is available here as well.
For each o take event weights B_(o,0) at o, B_(o,j)-B_(o,j-1) at op^j for 1<=j<=R_p, and w_o at op^j for j>R_p.
Add a weight whenever its event divides n, then multiply the p contribution by log p.
The weights are nonnegative integers by (8) and (8c); telescoping recovers (8d).
Only events at most the finite cutoff are needed.
Hence both the values and a terminating tail test are determined by a finite exact local table.
A positive incumbent is still a necessary hypothesis for this particular optimization argument; the theorem does not guarantee that an arbitrary S supplies one.

<a id="good-prime-aggregation-and-global-tail"></a>
### A finite exact search can certify the best first-layer bound

Let S be a finite nonempty set of good primes p, meaning p does not divide disc P.
The roots lift to units in an unramified splitting field.
For every multiplicative order o occurring among the reductions of the d roots, let w_(p,o) be its multiplicity, counting individual roots.
Thus sum_o w_(p,o)=d and p does not divide o.
Equivalently, each irreducible factor modulo p contributes its degree to the order of any one of its roots.
Set

    k_p(n)=sum_(o|n) w_(p,o),
    A_S(n)=sum_(p in S) k_p(n)(1+v_p(n))log p,
    B_S(n)=[A_S(n)-d log 2]/n.                              (9)

If o divides n, write n=o p^j u with p not dividing u.
The corresponding lifted root obeys v(alpha_i^o-1)>=1.
Repeated use of (8) gives v(alpha_i^n-1)>=1+j, also for p=2.
The valuations of all d roots sum to v_p(C_n), without an extra residue-degree factor when individual root indices are already being counted.
Different p contribute to the same integer C_n.
Hence

    log C_n>=A_S(n),    m>=B_S(n).                           (10)

These are automatic floors, not claimed exact valuations.
The good-prime assumption is used for the initial normalized depth one; the general ideal formula (4) remains valid without it.

There is an exact divisibility-event expansion

    A_S(n)=sum_(p,o) sum_(j>=0)
             w_(p,o) log p * 1_{o p^j divides n}.            (11)

For n<=X only events o p^j<=X matter.
This gives a finite integer sieve for each logarithm coefficient, followed by certified logarithm evaluation; it does not require approximating roots.

Put R=product_(p in S)p.
For every n>=1, k_p(n)<=d, so

    A_S(n)<=d(log R+log n),
    B_S(n)<=U(n):=d log(Rn/2)/n.                            (12)

Here the contribution d sum_(p in S)v_p(n)log p is at most d log n.
Differentiation yields

    U'(x)=d[1-log(Rx/2)]/x^2.

Therefore U decreases whenever Rx/2>e.
In particular R>=6 makes it decreasing for all x>=1.
Suppose an exactly certified positive incumbent b=B_S(n_0)>0 is available.
If X>=n_0 is an integer with R X/2>e and U(X)<b, then all n>X are strictly worse than that incumbent.
Verifying all values (9) for 1<=n<=X proves the global all-positive-integer maximum of B_S.
An interval proof may use a lower bound for the winning value and upper bounds for every competitor and U(X).
Any unresolved overlapping intervals require refinement or an exact comparison, rather than an assumed ordering.
Exact ties can be kept as ties; after clearing integer denominators their equality is an equality between products of powers of rational primes.
The positive-incumbent requirement is essential for this particular finite tail argument.

The retained computation [J G0011](../computations/programs/Yin_J_G0011/readme.md) applies this interface to the two polynomials from [J G0010](../computations/programs/Yin_J_G0010/readme.md).
Its exact residue orders, log intervals, winning exponents, tail cutoffs and independent verification belong to that computation.
They are not premises of the present proof.
A successful comparison there can show improved finite certificates on those same inputs despite long whole-order scalar periods; it cannot supply uniform coverage of all near-one irreducible units.
