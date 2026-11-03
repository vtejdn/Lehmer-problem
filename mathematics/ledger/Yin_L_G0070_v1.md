---
author: Yin
---

# G0001: the intrinsic scalar period and what an invariant lattice can change

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0251_v1.md#scalar-period-multiplier-order).
The original mathematical input below remains fixed; its historical review account is retained at the review entrance below.
Bounded direct work by assigned AI review_matrix_completion for Yin, following the coordinator's question about replacing the power-basis order by another invariant lattice.
The mathematical input is the scalar-congruence estimate of [L G0069](Yin_L_G0069_v1.md#gim%2B10-arbitrary-prime-scalar-transfer), including its expressly accepted GIM+10 numerical constant.
The exact lattice and period comparisons below are proved directly.
No source search, computation or new numerical evaluation is used.

The maximal order realizes every scalar congruence that any invariant full lattice can realize.
Changes of lattice can remove a p-primary nilpotent cost, but cannot change the prime-to-p period of the reduced root set.
In particular they leave both squarefree mod-2 periods in J G0010 unchanged.
These statements isolate a real arithmetic coverage question; they do not establish the required linear period bound.

<a id="scalar-period-multiplier-order"></a>
## The exact invariant-lattice criterion

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
All these lattice flows retain the rational characteristic polynomial P and hence the same algebraic entropy m(P) under the monic integral interface of [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001), with the integral-lattice restriction as in [L G0061](Yin_L_G0061_v1.md#adjoint-entropy-comparison).

<a id="intrinsic-scalar-period"></a>
## Minimal periods and the maximal-order optimum

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
## The prime-to-p part is invariant; the nilpotent part has an exact size

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
## The local order index bounds every possible improvement

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
## The two J G0010 exponents cannot be shortened this way

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
## What the arithmetic coverage strategy can now ask

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
## An alternative coverage criterion allows a logarithmic prime factor

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
## Blockwise congruences and why zero reduction entropy gives no period bound

Consider a direct sum of simple rational unit flows

    V=direct_sum_i Q(alpha_i),

with monic irreducible unit polynomials P_i, positive weights m_i=m(P_i), and finite entropy sum_i m_i.
This is the simple-block existence-reduction scope in [L G0002](Yin_L_G0002_v1.md#capture-equivalence); it is not an identification of every original rational flow or its extensions with this displayed sum.

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

<a id="scalar-period-lattice-review"></a>
## Actual review and boundary

The complete original review account, actual contributions and finding-specific relationships are retained in [R525](../audits/reviews/Yin_R_G0525_v1.md#historical-lattice-author-finding).
The original date, mathematical review scopes and stated limits are unchanged; the current claim has its own actual full self-review and adoption.
No uniform intrinsic-period coverage, small-Mahler counterfamily or resolution of G0001 is claimed.
