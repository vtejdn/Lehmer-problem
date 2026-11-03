---
author: Yin
---

# G0001: a uniform Frobenius-energy ceiling for arbitrary finite exponent levels

Current complete proof: [C232v2](../claims/Yin_C_G0232_v2.md#multilevel-degree-hypotheses), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input, with its exact quantifiers, failed/remaining scope and source limits.

Date: 2026-10-07.
Direct bounded calculation by assigned AI assess_shortness_route for Yin.
This extends the finite construction of [L G0057](Yin_L_G0057_v1.md#direct-confluent-vandermonde) and the optimization screen of [L G0058](Yin_L_G0058_v1.md#mat96-optimized-ceilings).
It permits multiplicities at every selected exponent level and counts every prime-power-ratio Frobenius floor between those levels.
No new source, computation, prime-distribution estimate or assumption that Lehmer is false is used.

The optimized positive part of the coarse finite certificate is at most 2/(e^2 log D).
Even with the exact full-block cost it is at most 4/[e^2 log(D/(4/sqrt(3)))].
Both tend uniformly to zero as D tends to infinity, independently of the exponent set and all its multiplicities.
These are ceilings on sufficient lower certificates that replace an additional positive integer arithmetic surplus by one.
They are not upper bounds on the actual entropy or on that discarded surplus.

<a id="multilevel-degree-hypotheses"></a>
## Selected levels and the precise degree guard

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2, with monic minimal polynomial P, conjugates alpha_1,...,alpha_d, Mahler logarithm h=log M(P), and

    Delta=|disc P|,       D=d/Delta^(1/d).

Choose a finite nonempty set A of positive integers and, for every a in A, a positive integer multiplicity m_a.
Assume explicitly

    deg(alpha^a)=d       for every selected a in A.      (1)

This is a hypothesis on exactly the selected levels, including any composite levels.
No implication from L G0014's prime-exponent endpoint to all composite powers is assumed.
Intermediate levels between selected exponents need not be included or satisfy an additional hypothesis.

For the existence question behind an entropy gap, the [norm descent in L G0059](Yin_L_G0059_v1.md#all-positive-power-existence-descent) permits replacing an input by an all-positive-power degree-preserving algebraic integer with no larger positive Mahler logarithm; units remain units.
Every finite exponent set is eligible on that replacement.
This is an existence reduction to a possibly different input and flow, not a pointwise strengthening of prime stability for the original alpha.
It does not remove condition (1) when applying the formulas to a specified unreplaced input.

Put

    P_a(t)=product_(i=1)^d (t-alpha_i^a),
    s=sum_a m_a,       q=sum_a m_a^2,
    H=sum_a a m_a,     N=ds.

The polynomials P_a are monic integral and squarefree by (1), and M(P_a)=M(P)^a.
The distinct exponent levels are disjoint: an equality alpha_i^a=alpha_j^b with a!=b, transported around a finite-order Galois automorphism taking alpha_i to alpha_j, would imply alpha_i^(a^r)=alpha_i^(b^r) for some r>0.
This would make alpha_i torsion, contrary to the hypothesis.
Thus every node used in the confluent construction is distinct except for its prescribed multiplicity.

<a id="prime-power-edge-floor"></a>
## Every prime-power-ratio floor can be counted simultaneously

Call (a,b) an edge when a,b belong to A and b/a=ell^r for a prime ell and an integer r>=1.
Its weight is log ell, not r log ell.
Define

    E=sum_(edges a->b) m_a m_b log ell.                 (2)

At such a pair, iterated coefficientwise Frobenius gives

    P_b=P_a modulo ell.

Indeed the roots at level b are the ell^r-th powers of the roots at level a; elementary symmetric functions commute with Frobenius modulo ell, and integer coefficients are fixed modulo ell.
This argument retains all d roots through intermediate powering, so it does not require degree preservation at the intermediate levels.
Consequently

    0!=Res(P_a,P_b) is divisible by ell^d.              (3)

Only this floor is asserted.
In particular ell^(rd) is not inferred from r Frobenius iterations.

For each level define the integral nonzero divided-difference product

    b_a=product_(i<j)
          (alpha_j^a-alpha_i^a)/(alpha_j-alpha_i).

Its integrality and nonvanishing follow exactly as in [L G0057](Yin_L_G0057_v1.md#confluent-arithmetic-lower-bound): it is a symmetric integral polynomial in the original roots, and (1) excludes zero.
Thus |disc P_a|=Delta b_a^2.

Use the normalized derivative columns of multiplicity m_a at every root of P_a.
The resulting square matrix V_conf has size N.
The direct confluent product formula gives

    |det V_conf|^2
      =product_a |disc P_a|^(m_a^2)
          product_(a<b) |Res(P_a,P_b)|^(2m_a m_b)
      =Delta^q exp(2dE) Q_arith,                       (4)

where the exact positive integer surplus is

    Q_arith=product_a b_a^(2m_a^2)
       * product_(edges a->b)
           [Res(P_a,P_b)/ell^d]^(2m_a m_b)
       * product_(nonedges a<b)
           Res(P_a,P_b)^(2m_a m_b) >=1.                (5)

Each ratio b/a that is a prime power has a unique underlying prime.
Hence no pair receives two floors.
Different edges may use the same prime, but their factors in (4) are separate resultants; the product divisibility follows from the displayed exact factorization.
No unproved extra divisibility for nonedges is used.

<a id="frobenius-prime-factor-energy"></a>
## A uniform graph-energy inequality

The decisive bound, independent of the number or spacing of levels, is

    E <= (2/e) sqrt(q s H).                            (6)

For a fixed upper level b, the possible predecessors b/ell^r are distinct.
Cauchy--Schwarz therefore gives

    sum_(ell^r|b, b/ell^r in A) m_(b/ell^r) log ell
      <=sqrt(q) sqrt(sum_(ell^r|b) (log ell)^2).

Writing v_ell(b) for the prime valuation, the last sum is

    sum_ell v_ell(b)(log ell)^2 <= (log b)^2.

For the inequality, expand the square of the sum of the nonnegative multiset consisting of v_ell(b) copies of log ell; its sum is log b.
Multiplying the previous bound by m_b and summing over b proves

    E<=sqrt(q) sum_b m_b log b.

Finally (log x)^2/x<=4/e^2 for x>=1, with maximum at x=e^2.
A second Cauchy--Schwarz inequality gives

    (sum_b m_b log b)^2
      <=(sum_b m_b)(sum_b m_b(log b)^2)
      <=(4/e^2)sH,

which is (6).
The level b=1 has no incoming edge and contributes log 1=0.
No prime asymptotic is hidden in this proof; the arithmetic input is just unique prime factorization of the integer b.

For every L>0, (6) implies

    2E-Lq <= E^2/(Lq) <=4sH/(e^2 L).                  (7)

The first inequality is equivalent to (E-Lq)^2>=0.
Thus the multiplicities and the exponent graph cannot produce an unbounded edge gain relative to the quadratic multiplicity penalty and the exponent cost.

<a id="multilevel-coarse-factorial"></a>
## Coarse and normalized-derivative certificates

Applying the column estimates of [L G0057](Yin_L_G0057_v1.md#exact-confluent-column-cost) at every level gives the coarse upper bound

    |det V_conf|^2<=N^(dq) M(P)^(2NH).

Combining this with (4) after replacing Q_arith by one yields the valid finite lower estimate

    h>=B_0:=[2E-q log(Ds)]/(2sH).                      (8)

For D>1 its numerator is at most 2E-q log D.
Hence (7) proves

    [B_0]_+<=2/(e^2 log D).                            (9)

The factorial-corrected column bound instead has normalized numerator

    2E-q log(Ds)+T,
    T=2 sum_a sum_(j=0 to m_a-1) log(j!),

and exact positive denominator

    D_der=(2/d)[(N-1)H
                   -(1/2)sum_a a m_a(m_a-1)].         (10)

The bound T<=sum_a m_a(m_a-1)log m_a<=q log s again leaves a numerator at most 2E-q log D.
If A has only one level then E=0, so the positive part is zero for D>1.
Otherwise each integer multiplicity satisfies m_a+1<=s.
Therefore

    D_der/(2sH)
      =1-[sum_a a m_a(m_a+1)]/(2dsH)
      >=1-1/(2d)>=3/4.

Using (7) once more, the exact factorial certificate satisfies

    [B_der]_+<=8/(3e^2 log D),       D>1.               (11)

The positive-part convention matters: denominator improvements are used only when the numerator is positive.
The underlying entropy estimates themselves can alternatively be derived directly from their respective determinant upper bounds, without manipulating a signed estimate.

<a id="multilevel-exact-block-ceiling"></a>
## Full block cost and its uniform optimized ceiling

For 1<=m<=N let the exact binomial block constant be

    A_(N,m)=product_(j=0 to m-1)
       [(N+j)!(j!)^2 / ((2j+1)(N-j-1)!((2j)!)^2)],
    a_(N,m)=m^2 log N-log A_(N,m).

The product formula and its finite-difference proof are retained in [L G0057](Yin_L_G0057_v1.md#exact-confluent-block-cost).
Applying that block bound separately to all nodes gives

    |det V_conf|^2
      <=[product_a A_(N,m_a)]^d
            M(P)^(2 sum_a a m_a(N-m_a)).              (12)

Let c_0=4/sqrt(3).
The elementary bound in [L G0058](Yin_L_G0058_v1.md#block-parameter-ceiling) applies to every selected block:

    a_(N,m_a)<=m_a^2 log(c_0 m_a).

For completeness, N=ds>=2m_a and each correction index j<m_a has j/N<1/2.
The exact product then gives

    a_(N,m_a)
      <=m_a^2 log(2m_a)
           +[m_a(m_a-1)/2]log(4/3)
      <=m_a^2 log(c_0 m_a).

Thus the full-block normalized numerator, with Q_arith replaced by one, is

    U=2E-q log(Ds)+sum_a a_(N,m_a)
      <=2E-q log(D/c_0).                              (13)

Its exact denominator is

    D_block=(2/d)sum_a a m_a(N-m_a)
       =2[sH-(1/d)sum_a a m_a^2]
       >=(1-1/d)2sH>=sH.                             (14)

Here m_a<=s implies sum_a a m_a^2<=sH.
Both the exact denominator and its comparison are positive.
For D>c_0, equations (7), (13) and (14) prove

    [B_block]_+=[U/D_block]_+
       <=4/[e^2 log(D/c_0)].                          (15)

The exact sum-binomial individual-column bound is covered too.
Its constant is at least the product of the corresponding block constants, and its entropy exponent exceeds the block exponent by sum_a a m_a(m_a-1).
Hence its positive part is no larger than [B_block]_+.

Equations (9), (11) and (15) are uniform over every finite exponent set, every collection of positive integer multiplicities, and every eligible selection of degrees satisfying (1).
They also bound the supremum when all those parameters depend on D or on the individual input.
Any auxiliary delta>=D makes the estimates only weaker.
Thus arbitrary finite layering, repeated prime-power Frobenius floors and these exact row-volume refinements do not evade the D-to-infinity decay.

<a id="multilevel-surplus-boundary"></a>
## The remaining arithmetic information is explicit

The result concerns the specific lower estimates obtained by using Q_arith>=1 in (4).
Keeping its actual value adds (log Q_arith)/d to each normalized numerator.
Neither (6) nor (15) bounds that contribution.
In particular the divided-difference indices, extra valuations beyond the single ell^d floor, and cross-resultants at non-prime-power ratios all remain visible in the exact product (5).

The [discriminant-escape conclusion in L G0015](Yin_L_G0015_v1.md#discriminant-escape) explains why a uniformly positive certificate in the D-to-infinity regime would matter for the reduced Lehmer route.
The present theorem proves that the enlarged family of floor-only formulas cannot supply it by parameter choice alone.
It does not construct a vanishing-entropy sequence, upper-bound the true h, refute Lehmer, or exclude a new arithmetic lower estimate on Q_arith.
It also does not assert that every composite exponent is available at an L G0014 endpoint: condition (1) stays explicit throughout.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0020_v1.md#actual-review-and-provenance), with its original exact scopes, known author/contributor checks and separately unknown initial review arrangements.
