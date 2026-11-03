---
author: Yin
---

# G0001: a quantitative limit on cyclotomic compression of net-trace repair

Date: 2026-10-07.
Direct argument by assigned AI ms25_source for Yin, continuing [L G0039](Yin_L_G0039_v1.md#finite-minimum-repair-program).
This gives a sharp prime-support comparison between the canonical cycle budget and every cyclotomic repair.
It does not introduce a new realization theorem or a Lehmer gap.
The proof is elementary and uses no new external source; no novelty claim is asserted.

The complete reusable budget/comparison statements and proofs are owned by [C250](../claims/Yin_C_G0250_v1.md#argument); the original bounds, method limits and historical fixed input remain here.

<a id="logarithmic-repair-comparison"></a>
## Scope and conclusion

Use the Perron-unit scope of [L G0034](Yin_L_G0034_v1.md#finite-nettrace-repair): p is monic irreducible integral with constant coefficient +1 or -1, and has a positive root lambda>1 strictly larger in modulus than every other root.
Write

    b_n(p)=(1/n) sum_(j|n) mu(n/j) sum_(alpha root of p) alpha^j,
    D(p)=sum_(n>=1) n max(0,-b_n(p)).

The integers b_n(p) are eventually positive.
Thus D(p) is finite and is the degree of the canonical cycle repair.
Let R_*(p) be the least degree of a monic cyclotomic product c for which all b_n(pc) are nonnegative.
Existence follows from the canonical repair.
If D(p)=0 then R_*(p)=0; if D(p)>0 then R_*(p)>=1.

For R>=1, let ell_1=2, ell_2=3,... be the increasing primes and define

    k(R)=max{k>=1: product_(j=1)^k (ell_j-1)<=R},
    K(R)=(1+product_(j=1)^k(R) (ell_j+1)/(ell_j-1))/2. (1)

Then every cyclotomic repair c of degree R>=1 satisfies

    D(p)<=K(R) R <= R(2+(3/2)log_2 R).                 (2)

Consequently, whenever D=D(p)>0,

    D/[2+(3/2)log_2 D] <= R_*(p) <= D.                (3)

The more precise lower test retains the step function in (1):

    R_*(p)>=min{r>=1: r is an integer and r K(r)>=D}.   (4)

Both lower bounds (3) and (4) depend only on the original negative net-trace budget.
Optimization cannot reduce a large canonical budget by a power of that budget.
This is an arithmetic comparison, not an estimate of D in terms of logarithmic Mahler measure.

<a id="prime-support-repair-budget"></a>
## The exact positive correction budget of one cyclotomic factor

Write any cyclotomic repair as

    c=product_(m>=1) Phi_m^(e_m),       e_m>=0,
    R=deg c=sum_m phi(m)e_m.

Only finitely many multiplicities are nonzero.
As in L G0039,

    f_n=b_n(c)=sum_(m: n|m) mu(m/n)e_m.                (5)

If b_n(p)<0, feasibility gives f_n>=-b_n(p)>0.
The positive part of a sum is at most the sum of its positive parts.
Therefore

    D(p)
      <=sum_n n max(0,f_n)
      <=sum_m e_m sum_(n|m, mu(m/n)=1) n.              (6)

Every sum involving f_n is finite, so no convergence argument is involved.
The first inequality is valid without counting the positive original b_n twice or assuming that they vanish.
The second permits cancellation between different cyclotomic factors and can only enlarge the right side.

Put

    S_+(m)=sum_(n|m, mu(m/n)=1) n.

Since the indicator of mu=1 is (|mu|+mu)/2,

    S_+(m)
      =(sum_(n|m) n |mu(m/n)| + sum_(n|m) n mu(m/n))/2
      =(m product_(ell|m)(1+1/ell)+phi(m))/2.          (7)

The first divisor sum follows by replacing n by m/d and summing over square-free d.
The second is the usual formula for phi.
Dividing by phi(m) gives the exact ratio

    S_+(m)/phi(m)
      =(1+product_(ell|m)(ell+1)/(ell-1))/2.            (8)

It depends only on the distinct prime divisors of m.
Equations (6)--(8) give a more informative version of (2) when the actual factorization of a repair is known:

    D(p)<=sum_m e_m phi(m)
                 (1+product_(ell|m)(ell+1)/(ell-1))/2. (9)

For example, if every cyclotomic order in a repair uses only the primes 2 and 3, its improvement over the canonical degree is at most 7/2.
With only the prime 2, the factor is at most two.
These are upper bounds on the possible improvement, not statements that every permitted repair achieves them.

## The exact maximum ratio under a degree budget

Any factor used in a repair of degree R has phi(m)<=R.
If the distinct prime divisors of m are q_1<...<q_s, then

    product_(i=1)^s (q_i-1)<=phi(m)<=R.

Because q_i>=ell_i, the first s primes also have totient product at most R.
Thus s<=k(R).
The function (x+1)/(x-1) decreases for x>1, so

    product_(ell|m)(ell+1)/(ell-1)
      <=product_(i=1)^s (ell_i+1)/(ell_i-1)
      <=product_(i=1)^k(R) (ell_i+1)/(ell_i-1).        (10)

Equality in this maximum is attained for the square-free primorial m=product_(j=1)^k(R) ell_j, whose totient is at most R.
Hence K(R) is the exact maximum of S_+(m)/phi(m) over every cyclotomic order with phi(m)<=R.
This does not assert that a repair of total degree exactly R can always devote all its degree to that factor, or that an algebraic-unit polynomial realizes equality for every R.
Summing (10) with weights e_m phi(m) proves the first inequality of (2).

An elementary upper bound needs no estimate for the distribution of primes.
For j>=2, ell_j is an odd integer and ell_j>=2j-1.
Consequently

    product_(j=1)^k (ell_j+1)/(ell_j-1)
      <=3 product_(j=2)^k j/(j-1)=3k.                (11)

Also product_(j=1)^k(ell_j-1)>=2^(k-1), so k(R)<=1+log_2 R.
Substituting this into (1) and (11) gives K(R)<=2+(3/2)log_2 R, completing (2).
The canonical repair gives R_*<=D.
Applying (2) to an optimal repair and replacing R_* by D inside the increasing logarithm proves (3).
Formula (4) follows directly from the exact first inequality of (2).

A stronger elementary integer cutoff is available if useful: product_(j=1)^k(ell_j-1)>=2^(k-1)(k-1)!.
Inserting the largest k permitted by this inequality into (11) improves the simple logarithmic bound.
The exact K(R) is preferable when the few relevant prime factors are known; no asymptotic prime theorem is needed here.

## Equality already occurs for the retained actual unit examples

Two existing irreducible-unit examples attain the exact comparison at its first two budgets.
These are not invented net-trace sequences.

For the Salem family in [L G0038](Yin_L_G0038_v1.md#family-repair), take any N>=16 with N=10 modulo 12, for example N=22.
Its canonical repair is t^2-1, so D=2, while its unique required negative index can be repaired by Phi_2=t+1, giving R_*=1.
Formula (1) gives K(1)=(1+3)/2=2; hence D=K(1)R_*.
The family has E(p_N)=3, L(p_N)=6 and limiting Mahler measure theta_0, as established there.

For the degree-22 small reciprocal core in [L G0039](Yin_L_G0039_v1.md#degree22-small-core-counterexample), the canonical degree is D=7 and the unique minimum repair Phi_6 has R_*=2.
Formula (1) gives K(2)=(1+3*2)/2=7/2; again D=K(2)R_*.
In this case the positive cyclotomic corrections occur exactly at indices 1 and 6 and consume the positive original counts at indices 2 and 3.
The retained example has M(p)<theta_0, exactly three expanding conjugates, all-power degree preservation, E(p)=2 and L(p)=5.
No new computation is required to reuse these fixed facts.

Thus it is already false, in the stated unit scopes, that a canonical repair is always within a factor smaller than two, or always within a factor smaller than 7/2 once degree-two repairs are allowed.
The general upper comparison (2) also prevents arbitrarily large canonical-to-optimal ratios at a fixed optimized degree.

## Consequence for realization size and the next entropy question

Suppose a primitive nonnegative integer matrix A has characteristic polynomial t^z p c, with c cyclotomic, as in L G0034.
Its dimension is N=deg p+deg c+z.
Since its normalized net traces are nonnegative, c is a feasible repair.
Thus the same argument imposes an unavoidable extra-dimension bound

    N-deg p >= R_*(p) >= D(p)/[2+(3/2)log_2 D(p)]      (12)

when D(p)>0, with the sharper inverse bound (4) available.
Adding zero eigenvalues does not evade this lower bound.
It does not bound the nonnegative edge excess e from below: dimension and edge excess are different quantities, and the graph realization theorem supplies no converse estimate between them.

For the primary algebraic-entropy strategy, the useful changed boundary is that an entropy-uniform bound on optimized neutral degree cannot arise from signed cyclotomic cancellation while the original canonical budget grows without bound.
The quantitative obstruction is R_*(p)>=D(p)/O(log D(p)), not merely a finite-order search cutoff.
No family with a growing canonical budget and bounded Mahler measure is asserted here.

In particular, the polynomial upper budget in [L G0037](Yin_L_G0037_v1.md#degree-only-repair-budget) is only an upper bound.
It cannot be inserted as a lower bound into (3), and it does not show that actual Salem repair degrees grow.
L G0038's unbounded-degree family in fact has D<=2.
What remains necessary for an entropy conclusion is a new estimate linking the actual weighted negative budget D(p), rather than its worst-case degree upper bound, to m(p), followed by control of graph realization complexity.
Further optimization of cyclotomic factors is useful for individual examples but cannot by itself remove that missing relation.
This result supplies no lower bound on Shannon or maximum-atom entropy.

<a id="bounded-order-followup"></a>
## A sufficient reduction for the bounded-excess follow-up

There is one immediate conditional mechanism.
Suppose a primitive nonnegative integer realization A has nonnegative edge excess e and characteristic polynomial t^z p c.
Suppose, in addition, that every cyclotomic order occurring in c is at most B, for an integer B>=1.
Then

    deg c <= U(e,B):=(2^(e+1)-1) sum_(m=1)^B phi(m),
    R_*(p)<=U(e,B),       D(p)<=U(e,B)K(U(e,B)).        (13)

Here the coefficient bound ||det(tI-A)||_1<=2^(e+1) is [L G0034](Yin_L_G0034_v1.md#graph-excess-length-bound), valid also when z>0.
A polynomial with s nonzero monomials has multiplicity at most s-1 at any nonzero root.
To prove this, write it as sum_(i=1)^s a_i t^(n_i), with distinct n_i and nonzero a_i.
A nonzero root rho of multiplicity at least s would annihilate (t d/dt)^j P at rho for j=0,...,s-1.
This gives

    sum_i n_i^j a_i rho^(n_i)=0,       j=0,...,s-1.

The Vandermonde matrix in the distinct exponents n_i is invertible, forcing all a_i rho^(n_i)=0, a contradiction.
Since the characteristic polynomial has integer coefficients, its number of monomials s is at most its coefficient length.
Since p is irreducible noncyclotomic, the multiplicity of a primitive m-th root is exactly its multiplicity in c, and is therefore at most 2^(e+1)-1.
Summing these multiplicity bounds over m<=B proves the first bound in (13); (2) proves the rest.
This reduction uses no vanishing-sum classification.

The narrowly formulated open step is whether, for each e, every all-power-degree-preserving reciprocal p with 1<M(p)<theta_0 that admits some positive primitive realization of edge excess at most e admits one such realization whose cyclotomic orders are at most a bound B(e) independent of dimension.
An order bound of this kind would imply a uniform repair bound via (13).
It is not proved here, and it is unnecessary to demand that every redundant realization satisfy the order bound.
A bound on the set of prime divisors alone would not finish this argument, because their exponents could still grow.
No new branch or literature search for this open step has been started.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0010_v1.md#review-boundary), with its original inspected scope and relationship.
