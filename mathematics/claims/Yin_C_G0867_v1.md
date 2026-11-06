---
author: Yin
---
# A uniform first-Smith-layer ceiling for polynomial permutation matrices

This project deduction concerns the arithmetic random-matrix comparison for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
The root-order capacity mechanism in [L159](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) motivates the argument; the proof below includes the needed bound and treats repeated roots at every prime.
No claim of literature novelty is made.

## Statement

Let P be any monic integer polynomial of degree d>=1 with P(0) equal to 1 or -1.
For each N>=1 let Pi_N be a uniformly distributed permutation matrix of size N.
For a rational prime p put nu_p=dim_(F_p) ker P(Pi_N), and let H_N=sum_(k=1)^N 1/k.
No irreducibility, reciprocity, squarefree reduction or noncyclotomic hypothesis is imposed.
Then

    E nu_p <= (2+p^(-1/2)) sqrt(2d) H_N.              (FS1)

More exactly, let beta run over the distinct roots of P modulo p in an algebraic closure, e_beta their multiplicities and o_beta their multiplicative orders.
All these roots are nonzero, their orders are prime to p, and

    E nu_p = sum_(k<=N) (1/k)
             sum_(beta: o_beta divides k)
                  min(e_beta,p^(v_p(k))).             (FS2)

For any finite set S of primes, allowed to depend on P and d but selected independently of Pi_N, put

    Theta_S=sum_(p in S)log p,
    Z_N=(1/N)sum_(p in S)nu_p log p,
    c_0=2+1/sqrt(2).

Then

    E Z_N <= c_0 sqrt(2d) H_N Theta_S/N.               (FS3)

For every fixed a>0, at N=d this implies

    Pr(Z_d>=a)<=c_0 sqrt(2)H_d Theta_S/(a sqrt(d)).     (FS4)

In particular Theta_S=o(sqrt(d)/log(d+1)) implies Z_d tends to zero in probability, uniformly over the indicated polynomials.
The empty prime set is allowed and gives zero.
When P has no root of unity, P(Pi_N) is nonsingular over Q and its Smith normal form gives nu_p<=v_p(det P(Pi_N)).
Thus Z_N is a first-layer lower certificate for the normalized logarithmic absolute determinant, not an upper bound on that determinant or on its higher Smith layers.
No restriction on a permutation-dependent prime set is claimed, and no positive Mahler gap or near-one counterexample follows.

## Argument

### Cycle module and the exact mean

A k-cycle shift over F_p acts as multiplication by x on F_p[x]/(x^k-1).
For polynomials P and nonzero Q, multiplication by P on F_p[x]/(Q) has kernel dimension deg gcd(P,Q): write P=gP_1,Q=gQ_1 with gcd(P_1,Q_1)=1; Q divides Pf exactly when Q_1 divides f, and its residue multiples have dimension deg g.
Write k=p^s t with p not dividing t.
Then x^k-1=(x^t-1)^(p^s), and x^t-1 is squarefree by its nonvanishing derivative at every root.
Its roots are exactly those beta with o_beta dividing t, equivalently o_beta dividing k.
This proves the inner sum in FS2 for each cycle.
A uniform permutation has expected k-cycle count 1/k: count a chosen k-element set, its (k-1)! cyclic orders, and all (N-k)! permutations of the remaining elements, then divide by N!.
Adding the cycle nullities proves FS2 without any independence assertion about the cycle counts.

### Capacity of distinct root orders

For any finite set of n distinct nonzero elements of the algebraic closure of F_p, let w_o count its elements of order o.
Then sum w_o=n and w_o<=phi(o)<=o, where w_o=0 if p divides o.
Indeed the roots of x^o-1, for p not dividing o, form the cyclic group of order o and have phi(o) elements of exact order o.
For completeness the finite multiplicative subgroup is cyclic: if its exponent is E, element orders can be combined prime by prime to attain E, while x^E-1 has at most E roots; its cardinality is therefore E.
For any integer R>=0,

    sum_o w_o/o <= n/(R+1)
          +sum_(o<=R)phi(o)(1/o-1/(R+1))
       <= n/(R+1)+R/2.

For n>=1 take x=ceil(sqrt(2n)) and R=x-1.
The right side is sqrt(2n)-1/2+(x-sqrt(2n))^2/(2x)<=sqrt(2n).
The empty set gives zero separately.
Consequently the sum of reciprocal orders over any n distinct roots is at most sqrt(2n).

### Multiplicity strata and harmonic clocks

For a positive integer e put Delta_0(e)=1 and Delta_j(e)=min(e,p^j)-min(e,p^(j-1)) for j>=1.
Then min(e,p^s)=sum_(j=0)^s Delta_j(e), with only finitely many nonzero increments.
For a root of order o, prime to p,

    sum_(k<=N, o divides k) min(e,p^(v_p(k)))/k
      =sum_(j>=0) Delta_j(e)/(o p^j) H_floor(N/(o p^j))
      <=H_N sum_(j>=0) Delta_j(e)/(o p^j),

where H_0=0.
The j=0 contribution after summing roots is at most sqrt(2d)H_N, since there are at most d distinct roots.
For j>=1, Delta_j(e)=0 unless e>p^(j-1), and Delta_j(e)/p^j<=1-1/p.
The number n_j of such distinct roots is at most d/p^(j-1), because their positive multiplicities sum to at most d.
Applying the distinct-root capacity bound to each of these sets gives the remaining contribution at most

    H_N(1-1/p)sum_(j>=1)sqrt(2d/p^(j-1))
       =H_N sqrt(2d)(1+1/sqrt(p)).

Together with j=0 this proves FS1, including repeated reductions and p=2.
Summing nonnegative terms with weights log p gives FS3, and Markov's inequality gives FS4.
The harmonic estimate H_d<=1+log d proves the stated uniform convergence.
Finally, for an invertible integer matrix its Smith diagonal has nonzero entries s_i; its reduction has nullity equal to the count of p-divisible s_i, while the determinant valuation is sum_i v_p(s_i).
This proves the claimed first-layer interpretation and its exact limitation.

## Scope

The result bounds the amount certified solely by mod-p nullity for the selected prime budget.
It does not bound unusually deep divisibility, a growing sufficient prime budget, or a different ensemble with an original-measure return.
It is compatible with useful isolated large cyclic norms and with every unproved G0001 possibility.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:06 |
| status | proved |
| reason | Adopt FS1--FS4 and the conditional determinant interpretation after the independent whole finding R1089. The estimate includes every prime and repeated roots, with a fixed prime set for each permutation experiment; it bounds the first-layer certificate, not the full determinant or higher Smith layers. No positive Mahler gap or literature-novelty conclusion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | FS1--FS4, uniform convergence, empty prime set and the separately conditioned determinant interpretation. |
| argument | [Complete argument](#argument) | Cycle modules, exact cycle mean, distinct-root capacity, all multiplicity strata, weighted harmonic and probability bounds, and Smith-form interpretation. |
| support | [Root-order capacity context](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Attribution and motivating comparison; the entire required estimate is proved here. |
| support | [Integer PID interface](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | Standard integer invariant-factor input at its retained source-inspection scope; no fresh original-textbook audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1089_v1.md#whole-proof-finding) | Exact final statement and complete proof, all primes and multiplicities, fixed prime-budget quantifiers and the lower-certificate limitation. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
