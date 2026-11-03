---
author: Yin
---

# G0001: an elementary finite-time prime witness for cyclic-norm growth

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0260_v1.md#finite-cyclic-norm-prime-witness).
The original mathematical input below remains fixed; its full historical review account is retained at the review entrance below.
Direct proof by assigned AI assess_shortness_route for Yin.
The coordinator contributed the coprime-exponent Bezout identity and central-binomial prime-count interface.
This agent independently checked them and supplied the complete witness proof, explicit constants and time bounds.
No external theorem, numerical scan or source acquisition is a premise.

<a id="finite-cyclic-norm-prime-witness"></a>
## The finite-time statement

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial, d=deg P>=2, m=log M(P), and

    C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)|.

For every eta with 0<eta<=m, set

    D=d max(1,1/eta),
    J=ceil(64D),
    B=2J^2,
    L=ceil(2+2d log(2B)/eta).                                (1)

Then some rational prime p with L<=p<=B satisfies

    log C_p >= p m/2,
    [log C_p-d log 2]/p >= m/4 >= eta/4.                    (2)

In particular log C_p>=2d log 2, with a strictly positive margin after subtracting the usual d log 2 archimedean cost.
All conjugates on the unit circle are retained.
Neither a power-degree hypothesis nor a lower bound for the distance of an individual algebraic conjugate from a root of unity is used.

The explicit time bound is quadratic in d for fixed eta.
A sharper asymptotic consequence of the same proof is

    p=O_eta(d log^2(d+1)).                                  (3)

The exact finite condition giving (3) is stated below.
No linear or O_eta(d log d) time bound is claimed in this argument.

<a id="coprime-avoidance-lemma"></a>
## One root can obstruct at most one prime in a finite window

For an integer a>=1 write

    G_a(z)=1+z+...+z^(a-1).

Fix a real B>=2.
If |z|<=1, then among the rational primes p<=B at most one satisfies

    |G_p(z)|<1/(2B).                                       (4)

For z=1 this is immediate.
Otherwise, suppose distinct primes p,q both satisfy (4).
Choose integers a,b with

    ap-bq=1,    1<=a<=q-1,    0<=b<=p-1.

They exist by taking the inverse of p modulo q and then putting b=(ap-1)/q.
The exact polynomial identity is

    1-z=(1-z^p) sum_(i=0)^(a-1) z^(ip)
          -z(1-z^q) sum_(j=0)^(b-1) z^(jq).                (5)

When b=0 the last sum is zero.
Since |z|<=1, (5) and (4) imply

    |1-z| < (a+b)|1-z|/(2B) < |1-z|,

because a+b<=p+q-2<2B.
This contradiction proves the lemma.
It is a polynomial argument; no root separation or logarithmic form estimate is hidden in it.
In fact any family of pairwise coprime exponents at most B has the same property.

Now label the d conjugates alpha_i and normalize each to the closed unit disk by

    z_i=alpha_i if |alpha_i|<=1,
        alpha_i^(-1) if |alpha_i|>1.

None equals one.
Direct factorization gives, for every n>=1,

    C_n=M(P)^n product_i |1-z_i^n|.

In particular C_1 is a nonzero integer, so C_1>=1.
For a prime p, division of this identity by its n=1 instance gives

    C_p=C_1 M(P)^(p-1) product_i |G_p(z_i)|.                (6)

Among any d+1 primes at most B, one fails (4) for every one of the d normalized roots.
Consequently that prime satisfies

    log C_p >= (p-1)m-d log(2B).                            (7)

This is where actual integrality enters: an arbitrary list of complex numbers need not have C_1>=1, and cannot discard that factor from (6).
The proof does not require individual roots to stay uniformly away from one, nor does it drop the unit-circle factors when passing from (6) to (7).

For an explicit nonarithmetic control, take the reciprocal, conjugation-stable complex list e^eta,e^(-eta),e^(i epsilon), e^(-i epsilon).
Its total logarithmic Mahler weight is eta, but its formal cyclic product satisfies

    C_n<=exp(n eta)n^2 epsilon^2.

For any prescribed N, choosing 0<epsilon<exp(-N eta/2)/N makes all these products less than one for 1<=n<=N.
This list is not asserted to be the conjugate list of an integral irreducible polynomial; indeed its products violate exactly the nonzero-integral norm condition used above.
Reciprocal root geometry by itself cannot replace that condition.

<a id="elementary-prime-window"></a>
## Enough primes from an elementary binomial estimate

Let pi(x) count rational primes at most x.
For every even integer B>=2, the central binomial coefficient gives

    pi(B) >= [B log 2-log(B+1)]/log B.                      (8)

Indeed binom(B,B/2)>=2^B/(B+1), since the largest of B+1 binomial coefficients is at least their average.
For each prime ell, the factorial valuation formula expresses its exponent in binom(B,B/2) as a sum of at most floor(log_ell B) terms, each zero or one.
Thus that prime contributes at most log B to the logarithm of the binomial coefficient.
Summing proves (8).

For even B>=16 this implies the convenient weaker inequality

    pi(B)>=B/(4 log B).                                    (9)

For example, log 2>=1/2 and log(B+1)<=B/4 suffice.
The latter holds at B=16 because log 17<4, and its right side thereafter has the larger derivative.
These elementary inequalities need no prime number theorem or prime tables.

We check that (1) ensures pi(B)>=L+d.
Since d>=2, B>=16, log B>=1, and log(2B)<=2 log B,

    L+d <= 3+d+(4d/eta)log B
         <= [(5/2)d+4d/eta]log B
         <= (13/2)D log B.                                (10)

For every x>=1,

    (log x)^2 <= (16/e^2)sqrt(x) <3sqrt(x).                 (11)

The first constant is the maximum of u^2 exp(-u/2) for u>=0, at u=4.
Also sqrt(B)>=64sqrt(2)D>78D.
Hence

    B > 26D(log B)^2,
    B/(4 log B) > (13/2)D log B >= L+d.                    (12)

Together with (9), this proves the desired prime count.
At most L-1 primes are below the integer L, so at least d+1 primes lie in [L,B].
Applying the preceding avoidance lemma to those primes yields p>=L for which (7) holds.

Because m>=eta and p>=2+2d log(2B)/eta,

    (p/2-1)m>=d log(2B),

so (7) implies the first inequality of (2).
Also B>=2 gives log(2B)>=2 log 2, and therefore p>=4d log 2/eta.
It follows that d log 2<=p m/4.
Subtract this cost from log C_p>=p m/2 to obtain the second inequality of (2), and also log C_p>=2d log 2.
This completes the explicit proof.

<a id="near-linear-log-squared-time"></a>
## A smaller asymptotic window from the same finite criterion

The proof works for any even integer B>=16 satisfying

    B/(4 log B) >= ceil(2+2d log(2B)/eta)+d.                 (13)

Such integers exist, and (1) is one fully explicit choice.
For a fixed eta>0, take any constant A>8/eta, and round A d log^2(d+1) upward to an even integer.
As d tends to infinity, log B/log d tends to one; the two leading sides of (13), after division by d log d, tend to A/4 and 2/eta.
Thus (13) holds for all sufficiently large d.
Increasing an eta-dependent constant to cover the finitely many remaining degrees proves (3).
Equivalently, the least even B satisfying (13) is an exact, finite, evaluable bound with that asymptotic order.
The asymptotic observation does not conceal a claim of an explicit smaller constant valid in all degrees.

<a id="finite-escape-coverage-boundary"></a>
## What changes, and what remains a coverage problem

The cyclic-norm inequality in [L G0074](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion) turns the prime p supplied here into a certificate for at least one quarter of the input's actual positive entropy.
The factor of four is explicit.
Setting eta=m in (1) is legitimate and gives a pointwise bound depending on both d and m.
Supplying a common lower threshold eta gives a controlled search window depending only on that threshold and d.
This replaces the unquantified per-input cyclic-norm growth with an elementary finite-time statement.

It does not establish such a common eta in the first place.
In a hypothetical sequence m tending to zero, the explicit window also grows with 1/m; nothing in the argument contradicts that possibility.
Nor does the theorem bound the prime factors of C_p: the witness exponent p is a prime, but the arithmetic primes dividing that norm are unrestricted.
A fixed finite arithmetic prime set or a bounded residue-period condition is an additional constraint, not a conclusion of (2).

Thus the theorem is an exact bridge for testing controlled-time aggregate witnesses, rather than a new Lehmer gap.
It does not replace the finite-prime escape issue in L G0074, and is not an estimate for every n beyond a common threshold.
No Baker-type uniform constant, original Fejer/Blanksby proof, prime-asymptotic theorem or external all-n growth theorem is used.

<a id="finite-escape-review"></a>
## Actual verification

The complete original contribution, source-boundary and review account is retained in [R530](../audits/reviews/Yin_R_G0530_v1.md#historical-prime-author-finding).
The original date and inspected scopes remain unchanged; current findings are separate from the original reported relationship labels.
