---
author: Yin
---

# G0001: a degree-only cutoff for Salem net-trace repair

Date: 2026-10-06T17:19.
Working refinement of [L G0034](Yin_L_G0034_v1.md#finite-nettrace-repair) within the primary algebraic-entropy route.
The coordinator supplied the expanding-pair Jordan-function identity; the assigned AI review_matrix_completion checked it independently.
Both then independently identified the integrality cutoff below.
The detailed bounds and their limitations are written out here for further review.
No new external theorem or novelty claim is asserted.

The complete reusable budget/comparison statements and proofs are owned by [C250](../claims/Yin_C_G0250_v1.md#argument); the original bounds, method limits and historical fixed input remain here.

<a id="degree-only-repair-budget"></a>
## Scope and conclusion

Let p be a Salem minimal polynomial of degree d: monic irreducible integral, with roots lambda>1, lambda^(-1), and r=d-2 roots z_1,...,z_r on the unit circle.
Put h=log(lambda)>0.
The usual Salem scope has even d>=4 and r>=2.
Define, as in L G0034,

    s_n=lambda^n+lambda^(-n)+sum_i z_i^n,
    T_n=sum_(j|n) mu(n/j)s_j,       b_n=T_n/n in Z,
    a_n=max(0,-b_n),               c(t)=product_n(t^n-1)^(a_n).

Here T_n is the unnormalized net trace.
Let omega(n) count distinct prime divisors, with omega(1)=0.
All nonzero repair indices belong to the explicit degree-only set

    I_r={n>=1 : n<r 2^omega(n)}.

In particular, set

    N_r=ceil(8 r^2/3)-1.

Then a_n=0 for every n>N_r.
Neither this cutoff nor the bounds below depend on h.
For the canonical cycle repair above, its degree D and the number B of cycle factors counted with multiplicity satisfy

    D=deg c=sum_n n a_n=sum_n max(0,-T_n),
    B=sum_n a_n,

    D <= sum_(n in I_r) n floor((r 2^omega(n)-1)/n)
      <= r N_r H_(N_r) <= r N_r(1+log N_r),             (1)

    B <= sum_(n in I_r) floor((r 2^omega(n)-1)/n)
      <= r H_(N_r)^2 <= r(1+log N_r)^2,                (2)

where H_N=sum_(j=1)^N 1/j.
Thus D=O(r^3 log(r+1)) and B=O(r log^2(r+1)), with the displayed explicit constants.
The arithmetic set I_r and the finite sums in (1)--(2) are stronger than their closed-form upper bounds.
These are upper bounds for this particular repair; no optimality among all cyclotomic completions is claimed.

## The expanding pair has positive net trace at every index

Write T_n=E_n+U_n for the expanding real pair and unit-circle contributions.
For n>1, expand cosh in the finite divisor sum:

    E_n=2 sum_(j|n) mu(n/j) cosh(jh)
       =2 sum_(k>=1) h^(2k) J_(2k)(n)/(2k)!,          (3)

    J_k(n)=sum_(j|n) mu(n/j) j^k
          =n^k product_(ell prime, ell|n)(1-ell^(-k)).

The constant term vanishes because sum_(j|n) mu(n/j)=0 when n>1.
The positive-k product formula follows immediately by expanding over the distinct prime divisors of n.
Every J_(2k)(n)>0, so E_n>0 for every n>1.
For n=1 the omitted constant matters: E_1=2 cosh(h)>2, also strictly positive.
Formula (3) must not be used at n=1 without restoring that constant.

For optional h-sensitive refinements one has, for n>1,

    E_n>=h^2 J_2(n),       E_n>=cosh(nh)-1.            (4)

For the second inequality, J_(2k)(n)/n^(2k)>=1/2: each prime factor is at least 1-ell^(-2), and the product over a finite subset of integers at least two is at least the full product

    product_(m>=2)(1-m^(-2))=1/2.

The latter identity is the limit of the telescoping finite product (L+1)/(2L).
Inserting the bound in (3) proves (4).
These estimates can exclude additional small indices for a specified h; they are not needed for the h-independent cutoff.

<a id="integrality-cutoff"></a>
## Divisibility eliminates all sufficiently large negative net traces

The unit-circle contribution obeys

    |U_n|<=r sum_(j|n)|mu(n/j)|=r 2^omega(n).

Both contributions are real because the root multisets are conjugation invariant.
Since E_n>0,

    T_n> -r 2^omega(n)                                (5)

for every n>=1.
L G0034's integral formal Euler product proves T_n in n Z.
Consequently, if T_n<0, then

    n <= -T_n < r 2^omega(n).                         (6)

This use of divisibility, rather than eventual exponential domination alone, removes h from the cutoff.
Since -T_n is also an integer, (5)--(6) give the pointwise bound

    a_n <= floor((r 2^omega(n)-1)/n).                 (7)

When n is outside I_r, this right side is zero and a_n=0.
It is always nonnegative for the present r>=2.

To make I_r finite explicitly, prime factorization gives

    (2^omega(n))^2/n
      =product_(ell^a exactly divides n) 4/ell^a
      <=(4/2)(4/3)=8/3.                              (8)

Only the primes 2 and 3 can contribute factors larger than one; higher exponents and all primes at least 5 only reduce this upper bound.
It also holds at n=1.
Combining (6) and (8) yields n<(8/3)r^2, hence n<=N_r.
This proves the finite support statement and the first inequalities in (1)--(2).

An optional exact h-dependent filter follows from integrality in the same way: if E_n-r 2^omega(n)>-n, then T_n>=0.
The strict inequality is intentional; equality would only give T_n>=-n.
Thus (4) supplies a further sufficient test within I_r without changing the unconditional cutoff.

## Summing the repair budget

For every positive integer n,

    2^omega(n)=sum_(q|n) mu(q)^2.

Therefore

    sum_(n<=N) 2^omega(n)
      =sum_(q<=N) mu(q)^2 floor(N/q)
      <=N H_N.

Summing n a_n<r 2^omega(n) over repaired indices and discarding the index restriction proves D<=r N_r H_(N_r).
Likewise,

    sum_(n<=N) 2^omega(n)/n
      =sum_(qk<=N) mu(q)^2/(qk)
      <=H_N^2,

which proves B<=r H_(N_r)^2.
The familiar H_N<=1+log N follows by comparison with the integral of 1/x.
No asymptotic prime-distribution estimate is used.

At n=1 one can sharpen (7) separately: T_1>2-r, so the integer T_1 is at least 3-r and a_1<=max(r-3,0).
This refinement is optional and does not alter the displayed uniform budgets.

## A nearby extension and the main limitation

The same argument applies to a monic integral polynomial of degree d>=2 having a single positive real root lambda>1 and all other d-1 roots of modulus at most one.
Now separate only lambda and use, for n>1,

    sum_(j|n) mu(n/j) lambda^j
      =sum_(k>=1) h^k J_k(n)/k! >0.

At n=1 it is lambda>0.
With r=d-1, the identical cutoff and budgets follow.
This is an adjacent single-expanding-root observation; the Salem reciprocal pair is the main scope here, and pairing it improves r from d-1 to d-2.
No corresponding assertion is made for a general Perron unit with additional expanding conjugates.

For Salem p, the resulting c preserves m(p)=h.
The accepted KOR00 statement in L G0034 gives some primitive nonnegative integer A with characteristic polynomial t^z p c.
Bounds (1)--(2) now control the number and total degree of the explicitly added cycle factors.
They do not control the zero multiplicity z, the size of A, or its edge excess e.
In particular, the one-sided inequality L(p)<=2^(e+1) from L G0034 cannot be reversed to obtain an upper bound on e from a bound on D.

The dependence on the unknown h has disappeared from this repair step, but degree dependence remains.
A hypothetical sequence with h tending to zero can have unbounded degree, and no uniform compression of these repairs or their matrix realizations has been proved.
Degree-only finiteness therefore does not supply the dimension-independent positive entropy gap sought by G0001.
The substantive improvement is an explicit, polynomial degree budget for neutral spectral repair, not a resolution of the remaining matrix-complexity bottleneck.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0009_v1.md#review-boundary), with its original inspected scope and relationship.
