---
author: Yin
---

# Intrinsic lattice scalar periods and complete exact modular control costs

This retains the complete original 2026-10-07 argument of [L70](../ledger/Yin_L_G0070_v1.md), together with the complete already retained [J10 mathematical exponent/orbit analysis](../computations/programs/Yin_J_G0010/readme.md).
Native programs/results stay in J10; only their existing proof interfaces and exact controls are used here.

## Statement

Let alpha be a nontorsion algebraic unit of degree d with monic irreducible polynomial P, K=Q(alpha), O=Z[alpha] and maximal integer order O_K.
For every alpha-invariant full rank-d lattice L in K, multiplication by alpha is an integral automorphism and its multiplier order B(L) satisfies O contained in B(L) contained in O_K.
For every rational prime p, integer a>=1 and scalar representative c not divisible by p,

    A_L^a=cI modulo p iff (alpha^a-c)/p belongs to B(L).

Some invariant full lattice realizes this congruence iff the quotient is an algebraic integer, iff O_K realizes it.
The same O_K realizes all eligible triples simultaneously; every intermediate order is itself such a multiplier order.
Basis change and homothety preserve these congruences; mere lattice inclusion gives no general monotonicity of multiplier orders.
All these lattices have the same total algebraic entropy m(P).

Let N_p(L) be the least scalar exponent, N_p^max=N_p(O_K) and N_p^comp=N_p(O); max denotes the maximal order, whose period is minimal.
Then N_p^max divides N_p(L), which divides N_p^comp.
Let U be the distinct nonzero roots of P modp, n_p their least common scalar exponent, r_L the largest Jordan-block size and e_p(r)=min{s>=0:p^s>=r}.
The exact formula is

    N_p(L)=n_p p^e_p(r_L),
    N_p^comp=n_p p^e_p(max_i m_i)

when P modp=product_i f_i^(m_i).
The prime-to-p n_p is lattice invariant; squarefree reduction forces N_p(L)=n_p for every lattice.
With kappa_p the largest p-primary elementary-divisor exponent of O_K/O,

    N_p^comp divides N_p^max p^kappa_p,
    N_p^comp/N_p^max divides p^min(kappa_p,e_p(max_i m_i)).

The conductor/binomial proof includes p=2 and distinguishes a power-order index prime from field ramification.
The complete index-three example alpha=2+3epsilon, epsilon^2-epsilon-1=0, P=t^2-7t+1 has N_3^comp=3 and N_3^max=1, outside the small-measure core.

For the two retained J10 inputs, the Lehmer degree10 polynomial and the degree22 quotient (t^24-t^17-t^12-t^7+1)/(t^2-t+1), squarefree mod2 reduction gives the invariant periods 31 and2047 for every full lattice.
A global scalar congruence on any integral extension containing a rational irreducible core restricts to that core lattice and forces its N_p^max to divide the exponent.
Using exactly the accepted common c_0=0.427800 coefficient, the best exponent-cost bound across lattices at a fixed p is m(P)>=c_0 d/N_p^max.
This optimality concerns that common coefficient only, without claiming optimality among stronger prime/scalar-specific or other auxiliary bounds.
The published numerical-margin boundary remains exactly that of C246; the lattice/period identities do not depend on its decimal evaluation.
A supplied fixed budget N_p^max<=Cd gives only a sufficient restricted gap c_0/C, without a theorem locating such a prime.

For the identity period T_p^max, if alpha^(N_p^max)=c_p modulo pO_K, then

    T_p^max=N_p^max ord_(F_p^*)(c_p),
    N_p^max divides T_p^max divides (p-1)N_p^max.

For p>=3, m(P)>=d log(p/2)/T_p^max.
The alternative supplied budget T_p^max<=C d logp at any prime gives the uniform bound

    m(P)>=(1/C) min{c_0/log2,log(3/2)/log3}.

This is an alternative identity budget, not a claimed weakening of the scalar budget.
A supplied completely split prime has T_p^max dividing p-1, and a supplied p<=B d logd suffices with C=max(B,1/log2); no split-prime existence theorem is adopted.

In a simple direct sum of positive rational unit blocks of finite entropy, a common linear bound on each block's scalar exponent, with primes/scalars allowed to vary, implies finite positive spectrum and entropy capture with multiplicities.
For any such direct sum and invariant block lattices, every modp reduction automatically has zero algebraic entropy, without a period or degree-ratio bound.
Neutral permutation blocks give zero or captured positive entropy with no finite common global scalar period; no hypothetical uncaptured positive family is constructed.

The complete retained J10 mathematical analysis is also included: for precisely the two accepted inputs at p=2, all positive exponents reduce without loss in the positive-part collision certificate to divisors of N=31 or2047, and r=1 optimizes all r>=1.
Their irreducible reciprocal GF2 factors have odd prime degrees5 or11 and full root orders N=2^f-1.
The direct orbit proof gives nu(a)=d unless N divides a, when nu(a)=d^2, for every a>=1; it asserts no infinite family of actual small-core inputs with this pattern.
The exact best first-layer certificates are

    m(P_Lehmer)>=[80log2-10log5]/1767,
    m(P_22)>=[440log2-22log11]/264063.

Only the retained r=1 computations were executed; the all-a/r result is the complete written finite-reduction proof.
These controls exclude only the particular no-exception coverage constants p_0=2,C=4,eta=1/2, without ruling out finite exceptions, smaller windows, other constants/primes, actual higher valuations or other methods.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:19 |
| status | open |
| reason | Register the complete original mathematical argument, exact domains and already retained evidence interfaces; actual current whole review and adoption follow separately. Registration performs no computation, source acquisition, numerical certification, research resumption or independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact statement](#statement) | All multiplier-order/Jordan/conductor/extension/identity-budget/blockwise entropy assertions and complete two-input all-a/r profile analysis, with source/numerical/coverage limits. |
| argument | [Entire retained arguments](#argument) | Full original L70 proof plus complete J10 finite-exponent/orbit/optimality analysis and exact control boundaries; all original formulas retained. |
| dependency | [Complete integral/all-prime scalar transfer](Yin_C_G0246_v1.md#gim%2B10-arbitrary-prime-scalar-transfer) | Only the common0.427800 bound for integral scalar quotients and its published numerical-input qualification; stronger coefficients are not included in exponent-cost optimality. |
| dependency | [Accepted total entropy](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Total monic integral/rational Mahler entropy without a dimension divisor; no fresh original-source proof audit. |
| dependency | [Integral-lattice transfer](Yin_C_G0236_v1.md#adjoint-entropy-comparison) | Complete finite-set denominator-clearing transfer from rationalization to any finite-rank invariant integral lattice. |
| dependency | [Rational finite capture](Yin_C_G0205_v1.md#capture-equivalence) | Only the displayed simple-block existence-reduction and positive-factor multiplicity/capture criterion, not a decomposition of arbitrary extensions. |
| dependency | [Exact retained native controls](../computations/programs/Yin_J_G0010/readme.md#results-and-limits) | Both complete inputs, GF2 factors/orders/minimality residues and divisor profiles, exact ratios/denominators and retained60 comparisons; no rerun or new irreducibility/measure claim. |
| dependency | [Complete first-layer finite certificate](Yin_C_G0242_v1.md#measured-nullity-cost-and-certificate) | Exact original two-level Vandermonde bound and prime-repetition nullity, with full exponent costs and original power-degree eligibility for these accepted controls. |
| dependency | [Accepted Lehmer control domain](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Exact irreducible Salem input, positive small measure and all-positive-power degree preservation; native modular evidence does not establish these facts anew. |
| dependency | [Accepted degree22 control domain](Yin_C_G0249_v1.md#degree22-small-core-counterexample) | Entire original reciprocal irreducibility/Perron/all-power proof and exact small-measure/three-expanding-conjugate control, without Salem or new numeric-root inference. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:25 |
| status | proved |
| reason | Adopt the entire original lattice/period/entropy proof and complete retained J10 all-exponent/orbit analysis after actual whole current self-review, full static reading of both native algorithms/JSONs and exact input-domain checks. The common-coefficient optimum and original precision reread remain correctly scoped; no program was rerun, numerical margin recertified, uniform coverage proved or independent review claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All multiplier-order/Jordan/conductor/extension/identity-budget/blockwise entropy assertions and complete two-input all-a/r profile analysis, with source/numerical/coverage limits. |
| argument | [Argument](#argument) | Full original L70 proof plus complete J10 finite-exponent/orbit/optimality analysis and exact control boundaries; all original formulas retained. |
| dependency | [Dependency](Yin_C_G0246_v1.md#gim%2B10-arbitrary-prime-scalar-transfer) | Only the common0.427800 bound for integral scalar quotients and its published numerical-input qualification; stronger coefficients are not included in exponent-cost optimality. |
| dependency | [Dependency](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Total monic integral/rational Mahler entropy without a dimension divisor; no fresh original-source proof audit. |
| dependency | [Dependency](Yin_C_G0236_v1.md#adjoint-entropy-comparison) | Complete finite-set denominator-clearing transfer from rationalization to any finite-rank invariant integral lattice. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Only the displayed simple-block existence-reduction and positive-factor multiplicity/capture criterion, not a decomposition of arbitrary extensions. |
| dependency | [Dependency](../computations/programs/Yin_J_G0010/readme.md#results-and-limits) | Both complete inputs, GF2 factors/orders/minimality residues and divisor profiles, exact ratios/denominators and retained60 comparisons; no rerun or new irreducibility/measure claim. |
| dependency | [Dependency](Yin_C_G0242_v1.md#measured-nullity-cost-and-certificate) | Exact original two-level Vandermonde bound and prime-repetition nullity, with full exponent costs and original power-degree eligibility for these accepted controls. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Exact irreducible Salem input, positive small measure and all-positive-power degree preservation; native modular evidence does not establish these facts anew. |
| dependency | [Dependency](Yin_C_G0249_v1.md#degree22-small-core-counterexample) | Entire original reciprocal irreducibility/Perron/all-power proof and exact small-measure/three-expanding-conjugate control, without Salem or new numeric-root inference. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0525_v1.md#current-lattice-profile-finding) | Entire exact current statement, complete retained argument and every selected interface, self-reviewed; old findings and precision predecessor retain their actual input/version scopes. |

## Complete retained argument

<a id="argument"></a>

## PartI: complete invariant-lattice and entropy proof

<a id="scalar-period-multiplier-order"></a>
### The exact invariant-lattice criterion

Let alpha be a nontorsion algebraic unit with monic irreducible minimal polynomial P of degree d.
Put K=Q(alpha), O=Z[alpha], and write O_K for the ring of all algebraic integers in K.
A full lattice L means a free abelian subgroup of K of rank d spanning K over Q.
Assume alpha L is contained in L.
Multiplication by alpha then has an integral matrix A_L of determinant Norm(alpha)=+1 or -1, so alpha L=L automatically.

The multiplier order of L is

    B(L)={x in K:xL is contained in L}.

It contains O.
Every member is integral, because its multiplication matrix on L satisfies a monic integer characteristic polynomial.
Hence

    O is contained in B(L), which is contained in O_K.             (1)

These are full-rank orders.
To see the needed finiteness directly, the trace pairing on K is nondegenerate and the trace-dual of O is a full rational lattice.
For x in O_K and y in O, xy is integral, so Tr(xy) is an integer.
Thus O_K lies in that trace-dual lattice and contains O; in particular [O_K:O] is finite.
This also shows that every intermediate additive group in (1) is a full lattice.

For every prime p, a>=1 and integer c not divisible by p,

    A_L^a=cI modulo p
      iff (alpha^a-c)L is contained in pL
      iff (alpha^a-c)/p belongs to B(L).                          (2)

It follows that the following are equivalent:

1. Some alpha-invariant full lattice has A_L^a=cI modulo p.
2. (alpha^a-c)/p is an algebraic integer in K.
3. The lattice O_K has that scalar congruence.

The same single lattice O_K realizes all eligible triples (p,a,c) simultaneously.
Conversely each order B between O and O_K is itself an alpha-invariant lattice and has B(B)=B, since xB contained in B implies x=x*1 is in B.
Thus the multiplier-order description is exact, not just a necessary condition on possible lattices.

An integral change of basis conjugates A_L by GL_d(Z) and leaves (2) unchanged.
Replacing L by uL for any u in K^* also leaves B(L) and all its scalar congruences unchanged.
Other finite-index changes can alter B(L), but have no freedom beyond the maximal-order condition above.
Inclusion of lattices alone is not a monotonicity rule for their multiplier orders; the actual orders in (2) control the comparison.
All these lattice flows retain the rational characteristic polynomial P and hence the same algebraic entropy m(P) under the monic integral interface of [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001), with the integral-lattice restriction as in [L G0061](Yin_C_G0236_v1.md#adjoint-entropy-comparison).

<a id="intrinsic-scalar-period"></a>
### Minimal periods and the maximal-order optimum

For an invariant full lattice define

    N_p(L)=min{a>=1:A_L^a=cI modulo p for some c in F_p^*}.

This exists, as A_L modulo p belongs to the finite group GL_d(F_p).
It is its projective order: the least positive exponent with scalar image.
Set

    N_p^max=N_p(O_K),       N_p^comp=N_p(O).

The notation max refers to the order O_K, not to the size of the period; its period is the minimum over all the allowed lattices.
More precisely (2) gives

    N_p^max divides N_p(L), which divides N_p^comp, for every L.   (3)

Indeed any exponent valid for O is valid for L by O contained in B(L), and any exponent valid for L is valid for O_K.
The exponents giving scalar powers of a finite matrix form the multiples of its projective order.
In particular choosing a different rational conjugacy that makes the matrix integral cannot beat N_p^max.

The exact power-basis criterion is

    A_O^a=cI modulo p
      iff P mod p divides t^a-c in F_p[t].                        (4)

This holds even with repeated factors: multiplication by t^a-c vanishes in F_p[t]/P exactly when it annihilates the identity.
The maximal-order criterion (2) can be weaker than (4) at primes dividing [O_K:O].
Conflating those two conditions would lose the only possible lattice improvement.

<a id="scalar-period-jordan-formula"></a>
### The prime-to-p part is invariant; the nilpotent part has an exact size

In an algebraic closure of F_p let U be the set of distinct roots of P modulo p.
All roots are nonzero.
Let n_p be the least a>=1 for which u^a is the same scalar for every u in U.
The common value belongs to F_p^*: Frobenius permutes U and thus fixes that value.
All elements of U have orders prime to p in finite multiplicative groups, so n_p is prime to p as well.
Equivalently it is the projective order of the semisimple reduced spectrum, with multiplicities omitted only for this definition.

Let r_L be the largest size of a Jordan block of A_L over the algebraic closure of F_p, and define

    e_p(r)=min{s>=0:p^s>=r}.

Then the complete scalar period is

    N_p(L)=n_p p^(e_p(r_L)).                                      (5)

To prove this, write any exponent a=p^s b with p not dividing b.
The eigenvalue condition for a scalar power implies n_p divides a, or equivalently n_p divides b.
For a Jordan block uI+J, the polynomial (uI+J)^b-u^b I is J times a polynomial in J with nonzero constant coefficient b u^(b-1).
It therefore has the same nilpotency index as J.
In characteristic p, taking a p^s-th power kills this nilpotent part exactly when J^(p^s)=0, namely when p^s is at least its block size.
Thus every admissible a is a multiple of the right side of (5), and that right side gives a scalar power.
This proves (5).

All integral realizations on full lattices have the same rational and integral characteristic polynomial P, hence the same U and n_p.
Only the last factor in (5) can change.
For the companion lattice, write

    P mod p=product_i f_i^(m_i)

with distinct monic irreducible f_i.
The companion matrix remains cyclic modulo p, so it has one Jordan block of size m_i for every root of f_i.
Consequently

    r_O=max_i m_i,
    N_p^comp=n_p p^(e_p(max_i m_i)).                              (6)

If P modulo p is squarefree, all r_L equal 1 and

    N_p(L)=n_p       for every invariant full lattice L.           (7)

If it is not squarefree, merely making all powered reduced roots equal c does not imply the scalar matrix congruence: the Jordan condition p^s>=r_L in (5) is still necessary.
Ramification or an order-index defect cannot be handled by deleting multiplicities from (4).

<a id="local-conductor-period-bound"></a>
### The local order index bounds every possible improvement

Let O_p=O tensor Z_p and K_p^int=O_K tensor Z_p, and put

    kappa_p=min{s>=0:p^s K_p^int is contained in O_p}.

This is the largest p-primary elementary-divisor exponent of O_K/O.
Equivalently p^kappa_p K_p^int is contained in the local conductor {x in K_p^int:x K_p^int is contained in O_p}.
No choice of an individual prime ideal above p is implicit in this definition.

Write a=N_p^max and choose its scalar c not divisible by p.
Then alpha^a=c+p eta for eta in K_p^int.
Applying binomial induction to alpha^a/c=1+p eta/c gives

    alpha^(a p^kappa_p)-c^(p^kappa_p)
       belongs to p^(kappa_p+1) K_p^int, hence to pO_p.

The quotient is local-integral in O_p, so the corresponding integral power-basis matrix is scalar modulo p.
Therefore

    N_p^max divides N_p^comp,
    N_p^comp divides N_p^max p^kappa_p.                           (8)

Combining (5)--(6), the ratio is a power of p satisfying

    N_p^comp/N_p^max divides
       p^min(kappa_p,e_p(max_i m_i)).                             (9)

In particular if p does not divide [O_K:O], kappa_p=0 and no lattice change can shorten the period.
This conclusion still holds when p ramifies in the field and P modulo p has repeated factors: equality of the two local orders removes the possible index-based improvement, but does not assert semisimplicity.
Distinguishing a field-discriminant prime from a power-basis index prime matters here.

There is a transparent genuine improvement, outside the small-Mahler core.
Let epsilon satisfy epsilon^2-epsilon-1=0 and put

    alpha=2+3epsilon,
    P(t)=t^2-7t+1,
    L=Z+Z epsilon.

On L multiplication by alpha has matrix

    [ 2 3 ]
    [ 3 5 ],

which has determinant 1 and becomes 2I modulo 3.
The sublattice O=Z+Z alpha has index 3 in L.
Its companion matrix modulo 3 has characteristic polynomial (t+1)^2 and a nonzero size-two Jordan block, so N_3^comp=3, whereas N_3(L)=N_3^max=1.
The minimum is 1 without needing to identify L separately as the maximal order.
The positive root of P is (7+3sqrt(5))/2>6, so this example proves possibility of the lattice effect, not its occurrence near M=1.

<a id="j10-lattice-invariance"></a>
### The two J G0010 exponents cannot be shortened this way

[J G0010](../computations/programs/Yin_J_G0010/readme.md) retains exact squarefree mod-2 checks and minimal orders for its two accepted small-core inputs.
Their companion orders are 31 in degree 10 and 2047 in degree 22.
Since F_2^* contains only 1, matrix order and projective scalar order agree.
Applying (7) gives, without rerunning any computation,

    N_2^max=N_2(L)=31       for the Lehmer control,
    N_2^max=N_2(L)=2047     for the degree-22 control,              (10)

for every invariant full lattice in the respective number field.
Passing to maximal orders, a rationally conjugate integral matrix, a finite-index lattice, or a homothetic lattice cannot bypass either of these exponent costs at p=2.
This does not constrain changing p.

Nor can adding other rational invariant factors make a global scalar congruence cheaper for a retained irreducible core.
Suppose an integral linear map on a full lattice Lambda in V has a rational invariant subspace W carrying multiplication by alpha.
Then Lambda intersect W is a full lattice in W, and

    p Lambda intersect W=p(Lambda intersect W).

Thus B^a=cI modulo p on Lambda restricts to the same congruence on that core lattice and forces N_p^max to divide a.
If P occurs in the characteristic polynomial, such a rational simple subspace exists inside ker P(B): this nonzero kernel is a vector space over Q[t]/P, and one of its one-dimensional subspaces over that field supplies W.
This is a statement about a global scalar congruence, not a prohibition on other useful extension or partial-collision constructions.

<a id="intrinsic-period-coverage-obligation"></a>
### What the arithmetic coverage strategy can now ask

Using L G0069's common coefficient 0.427800, the strongest bound obtainable by minimizing the scalar exponent over invariant lattices at a fixed p is

    m(P)>=0.427800 d/N_p^max.                                    (11)

Indeed O_K attains that period and (2) supplies exactly the integral quotient required there.
Every other full lattice has period a divisible by N_p^max, giving no stronger exponent cost with this common coefficient.
L G0069 also has stronger odd-prime/scalar-specific estimates; no optimality among those coefficients or all auxiliary polynomial bounds is asserted here.
The numerical constant retains precisely L G0069's published-input qualification; none of the lattice statements depends on its decimal evaluation.

A uniform coverage proof for this route may therefore ask for some prime p, depending on the input, with N_p^max<=Cd for a fixed C.
The result would give the gap 0.427800/C.
This is a sufficient arithmetic target, not asserted to follow from a Mahler gap or to be equivalent to it.
Changing representations cannot alter its intrinsic minimal period.
At index-bad primes it can remove only the bounded nilpotent factor specified above; at squarefree primes it removes nothing.
No theorem locating a suitable prime or bounding n_p has been proved here.

<a id="identity-period-log-prime-budget"></a>
### An alternative coverage criterion allows a logarithmic prime factor

There is a useful alternative when the congruence is specifically to 1.
Define the minimal maximal-order identity period

    T_p^max=min{a>=1:(alpha^a-1)/p is integral}.

This is the order of alpha in (O_K/pO_K)^*, rather than its projective order.
If alpha^(N_p^max)=c_p modulo pO_K, then

    T_p^max=N_p^max ord_(F_p^*)(c_p),
    N_p^max divides T_p^max, which divides (p-1)N_p^max.           (12)

Indeed any identity exponent must first be a scalar exponent, hence a multiple of N_p^max; after that division the remaining condition is exactly that the corresponding power of c_p is 1.

For p>=3 the nonzero value alpha^(T_p^max)-1 is divisible by p in O_K.
Its norm is at least p^d, while its archimedean norm is at most 2^d M(P)^(T_p^max).
Thus

    m(P)>=d log(p/2)/T_p^max.                                    (13)

Suppose, for some prime p depending on the input, that

    T_p^max<=C d log p                                           (14)

with C>0 fixed across the proposed class.
For odd p, (13) gives

    m(P)>=log(p/2)/(C log p)
          >=log(3/2)/(C log 3).

At p=2, (11) or directly L G0069's identity-congruence case gives m(P)>=0.427800/(C log 2).
Consequently (14) at any prime implies the uniform positive bound

    m(P)>=(1/C) min{0.427800/log 2, log(3/2)/log 3}.              (15)

This allows a larger identity exponent as the prime grows.
It relaxes the identity-period O(d) target, but is an alternative to, not a claimed weakening of, the earlier projective-scalar criterion N_p^max<=Cd: conversion from N_p^max to T_p^max can multiply the exponent by as much as p-1.
For a general scalar representative c of size comparable with p, the estimate uses log[p/(1+|c|)], not log(p/2); a large prime alone does not give the logarithmic gain in (13).

As a conditional illustration, if p splits completely in K, then O_K/pO_K is a product of copies of F_p and T_p^max divides p-1.
This remains true if P modulo p has repeated factors caused by its power-basis index.
Thus a supplied completely split prime with p-1<=C d log p would meet (14).
In particular a supplied bound p<=B d log d for d>=2 suffices after replacing C by max(B,1/log 2): if p>d use log p>=log d, and if p<=d use p/(d log p)<=1/log 2.
These are conditional implications, not an existence theorem for such a split prime or a new adoption of a splitting-prime result.
The missing prime/exponent coverage remains arithmetic information, rather than a choice of lattice.

<a id="blockwise-period-and-reduction-entropy"></a>
### Blockwise congruences and why zero reduction entropy gives no period bound

Consider a direct sum of simple rational unit flows

    V=direct_sum_i Q(alpha_i),

with monic irreducible unit polynomials P_i, positive weights m_i=m(P_i), and finite entropy sum_i m_i.
This is the simple-block existence-reduction scope in [L G0002](Yin_C_G0205_v1.md#capture-equivalence); it is not an identification of every original rational flow or its extensions with this displayed sum.

If for every positive block there exists a prime p_i and an exponent a_i<=C deg P_i satisfying the maximal-order scalar congruence, then (11) gives m_i>=0.427800/C.
There can be only finitely many positive blocks, and L G0002 gives finite entropy capture.
The primes and scalar residues may vary by block; a simultaneous reduction at one common prime is not required for this argument.
A common absolute exponent a is a still stronger sufficient condition, since deg P_i>=1 gives the uniform lower bound 0.427800/a.
Neither condition is inferred merely from existence of some finite period separately on each block.

For comparison, choose any invariant full lattice L_i for each unit block and set Lambda=direct_sum_i L_i.
For every fixed prime p, the reduced flow on Lambda/p Lambda automatically has algebraic entropy zero.
Each finite set is supported on finitely many finite-dimensional F_p blocks; its entire trajectory lies in a finite group, so its trajectory entropy is zero.
Taking the supremum over finite sets proves the assertion.
This proof imposes no bound on the block periods or their ratios to the block degrees.

If a hypothetical summable family of infinitely many distinct positive weights existed, it too would pass this zero-reduction-entropy test at every prime.
No such family is constructed here; its existence is the unresolved capture obstruction.
The point is that zero mod-p entropy does not distinguish it from a captured flow and cannot alone supply the missing quantitative periods.

Even a common period on the whole flow cannot follow from finite entropy and zero mod-p entropy in general.
Fix p and take a direct sum of integral cyclic permutation blocks of distinct prime lengths ell!=p.
Each block has entropy zero, so the sum does too, while its scalar period modulo p is exactly ell: a permutation matrix is scalar only when it is the identity.
There is no finite common exponent.
Adjoining one positive finite block gives a finite positive-entropy flow with the same failure of a common global period, even though its entropy is captured by that positive block.
Thus neutral blocks must not be used to formulate an unnecessarily strong common-period target for the positive-spectrum problem.

<a id="j10-complete-exponent-profile-proof"></a>
## PartII: complete retained J10 exponent and orbit analysis

The native programs, full JSON data and execution facts remain in J10.
The complete already retained mathematical reduction and result analysis follow verbatim; no computation is executed here.
The input-domain proofs are the selected C226 and C249 interfaces, while native original-input provenance remains unchanged.

### Original question, domain and complete finite reduction

For precisely these two existing inputs, computationally at p=2 and r=1, determine the order of the companion matrix modulo 2, every possible powered-root collision profile, and the best positive certificate

    m(P)>=log[2^nu/(2d)^d]/[3(2d-1)a].

The inputs are the standard degree-ten Lehmer polynomial and

    P_22=(t^24-t^17-t^12-t^7+1)/(t^2-t+1).

Both complete ascending coefficient vectors are retained in `result.json`.
Their irreducibility, reciprocal-unit scope, small Mahler measures, and preservation of degree under all positive powers are inherited from the cited fixed records, not newly asserted from modular evidence.
The degree-22 input has three expanding conjugates by the retained control, so this comparison does not merely repeat a Salem-only setting.

This is a complete finite reduction in the exponent a for these two inputs, not an arbitrary search cutoff.
If the reduced matrix has order N, all reduced root ratios have order dividing N.
Whether a pair has the same a-th power therefore depends only on gcd(a,N).
Replacing a by that divisor preserves nu and decreases the positive certificate's denominator.
All divisors of N are enumerated.
The unramified nullity is also independent of the repetition r>=1 by L G0065, while its exact denominator is (2d-1)a(1+2^r).
Thus r=1 is optimal whenever the numerator is positive; a nonpositive numerator gives positive part zero for every r.
Together these arguments prove the stated optimum over every a>=1 and r>=1 at this particular prime.
Only r=1 was executed.
Other primes, actual higher valuations, discriminant/index factors and other analytic bounds remain outside the optimization.

There is a direct explanation of these complete profiles.
Both reductions are a reciprocal pair of irreducible degree-f factors, where f is an odd prime (5 or 11), and each root has the certified order N=2^f-1.
After exponent a the root order is n=N/gcd(N,a).
If n>1, the order of 2 modulo n divides f and cannot be one, so it equals f.
Since f is odd, -1 does not lie in the subgroup generated by 2 modulo the odd integer n.
The two inverse Frobenius orbits therefore remain distinct and each has size f.
If n=1 all roots collapse.
This proves nu=d outside multiples of N and nu=d^2 at those multiples.
The conditional modular pattern has full-collapse cost 2^(d/2)-1; no infinite family of actual small-core integer inputs with that pattern is asserted here.

### Complete original exact result and scope analysis

The author program retained the following exact profiles:

| Input | d | GF(2) irreducible factor degrees | Matrix order N | Every divisor profile (a,nu) | Best a |
| --- | --- | --- | --- | --- | --- |
| Lehmer | 10 | 5,5 | 31 | (1,10), (31,100) | 31 |
| P_22 | 22 | 11,11 | 2047=23*89 | (1,22), (23,22), (89,22), (2047,484) | 2047 |

Both squarefree gcds are one, so 2 is unramified for the power-basis orders.
Exact remainder certificates show t^N=1 modulo P and t^(N/ell)!=1 for every prime ell dividing N.
Factorizations and all residual polynomial coefficients are stored, rather than inferred from approximate eigenvalues.

In both inputs nu(a)=d unless N divides a, when nu(a)=d^2.
Thus no proper-divisor partial collision gives a positive certificate here.
The positive exact lower bounds are respectively

    m(P_Lehmer)>=log(2^100/20^10)/1767
                =[80 log 2-10 log 5]/1767,
    m(P_22)>=log(2^484/44^22)/264063
            =[440 log 2-22 log 11]/264063.

The generating program certifies the underlying rational ratios are greater than one; no decimal approximation establishes their sign or the optimum.
The full-collapse exponent costs are a/d=31/10 and a/d=2047/22.
The second accepted small-core input therefore has a substantially larger exponent cost in this one-prime mechanism.
This does not rule out suitable uniform constants or coverage using other primes; no such theorem is assumed.

One specific all-input coverage assertion is excluded: the L G0065 condition with p_0=2, C=4 and eta=1/2 includes the Lehmer control (a=31<=40 and nu=100), but excludes this degree-22 control.
Its allowed a<=88 never reaches a multiple of 2047, so nu=22<242.
This is a counterexample to those particular constants with no finite exceptions.
It does not rule out an eventual-large-degree version, where this one degree could be handled separately, nor a smaller near-one measure window, different fixed constants or additional primes.
The conditional exponential pattern above identifies an unbounded-degree obligation; it is not an established infinite small-core counterfamily.
