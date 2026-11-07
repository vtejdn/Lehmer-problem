---
author: Yin
---

# Positive factors of fixed templates with measure-one outer coefficients

This project deduction extends the [quadratic template result](Yin_C_G0879_v1.md#statement) to unequal outer coefficients and any fixed degree in the specialization variable.

<a id="statement"></a>
## Factor bounds and the dyadic family

Let \(F(z,t)=\sum_{j=0}^{s} A_j(z)t^j\) belong to \(\mathbb Z[i][z,t]\), with \(s\ge1\) and \(M(A_0)=M(A_s)=1\).
For fixed \(F\) there are \(c,\eta>0\) such that for all sufficiently large integers \(N\), each positive-measure monic irreducible Gaussian factor \(g\) of \(F(z,z^N)\) satisfies
\[
                   \deg g\ge cN,\qquad m(g)\ge\eta.
\]
The same bounds, after changing constants, hold for the positive-measure monic irreducible rational factors of its coefficient norm.
All measures are total and include multiplicity.
The constants can depend on the full template.

<a id="outer-coefficient-bound"></a>
## Radial bounds from the two ends

Each outer coefficient is a Gaussian unit times a power of \(z\) times a monic polynomial whose roots all have modulus one, by the [constant-term argument in v1](Yin_C_G0879_v1.md#root-moments).
For sufficiently large \(N\), the nonzero coefficients at the two extremes of \(F(z,z^N)\) come respectively from \(A_0\) and \(A_s z^{sN}\).
Removing the zero root and normalizing the leading unit gives a monic polynomial \(P_N\) with constant unit, degree \(sN+O_F(1)\), bounded coefficient one-norm and a bounded number of terms.
The Cauchy bounds for \(P_N\) and its reversal put all its roots in a fixed annulus around the unit circle with positive inner radius.

Write \(z=re^{i\theta}\) for such a root, \(v=|\log r|\), and \(w=z^N\).
The roots on the unit circle have \(v=0\).
For \(r>1\), division of \(A_s(z)w^s=-\sum_{j<s}A_j(z)w^j\) by \(|w|^{s-1}\) in absolute value gives
\[
                  e^{Nv}=|w|\le \frac{\sum_{j<s}|A_j(z)|}{|A_s(z)|}.
\]
For \(r<1\), the identity \(A_0(z)=-\sum_{j>0} A_j(z)w^j\) gives \(e^{Nv}=|w|^{-1}\le\sum_{j>0}|A_j(z)|/|A_0(z)|\).
Both denominators used here are nonzero on their stated domains.
The numerators are bounded on the fixed annulus.

Let \(S\) consist of the unit-circle zeros of the two outer coefficients, and let \(k\) be the larger of their degrees.
For \(S\ne\varnothing\), let \(\delta\) be the least circular angular distance from \(\theta\) to \(S\).
For each \(\omega\in S\), the identity \(|z-\omega|^2=(r-1)^2+r|e^{i\theta}-\omega|^2\) gives \(|z-\omega|\ge c_F\max(v,\delta)\).
The factors at zero are bounded away from zero on this annulus.
Taking logarithms in the preceding two inequalities, and separating \(v<1/N\) from \(v\ge1/N\), gives
\[
       Nv\le C_F+kX,\qquad X=\min\{\log N,\log^+(1/\delta)\}.
\]
At \(\delta=0\) use \(X=\log N\), and when \(S\) is empty the same bound holds with \(X=0\).

<a id="all-roots-to-factors"></a>
## Moments over the whole specialization and transfer to factors

The [sector count in v1](Yin_C_G0879_v1.md#angular-count) applies to \(P_N\) with multiplicities because its degree is \(O_F(N)\) and its number of terms is bounded.
The union of arcs at distance at most \(e^{-u}\) from \(S\) therefore contains \(O_F(Ne^{-u}+1)\) roots for \(0\le u\le\log N\).
For \(j=2,3\), integration against \(ju^{j-1}\,du\) bounds \(\sum X^j\) by \(O_F(N+(\log N)^j)=O_F(N)\).
Thus \(\sum v^2=O_F(N^{-1})\) and \(\sum v^3=O_F(N^{-2})\).
The coefficient norm \(P_N\overline{P_N}\) has the same bounds with twice the constants.

For each positive-measure rational irreducible factor \(f\) of that norm, its roots are nontorsion units and its degree \(d\) is \(O_F(N)\).
The [degree-weighted square bound](Yin_C_G0855_v2.md#statement) gives \(d\sum_{f(\alpha)=0}|\log|\alpha||^2\ge1/10\).
The upper square bound then gives \(d\gg_F N\).
Put \(v_\alpha=|\log|\alpha||\).
Because \(f\) has constant unit, \(\sum v_\alpha=2m(f)\), so
\[
    (10d)^{-2}\le\left(\sum v_\alpha^2\right)^2
       \le 2m(f)\sum v_\alpha^3 \ll_F m(f)N^{-2}.
\]
This proves the factorwise positive floor.
For a positive monic irreducible Gaussian factor \(g\), the rational minimal polynomial of a root is \(g\) or \(g\bar g\), as in the [field passage in v1](Yin_C_G0879_v1.md#factor-bounds).
Both its degree and its logarithmic measure are at most twice the corresponding quantity for \(g\).
The scalar and zero-root factors removed in normalization have measure one.

<a id="dyadic-application"></a>
## The dyadic deletion factors

For \(n=2^k\), \(k\ge2\), put \(N=n/2\) and use the [rotated dyadic polynomial and its completion](../ledger/Yin_L_G0458_v5.md#dyadic-rational-rotation).
The exact identity
\[
 (z^2-1)Q_n(z)=F(z,z^N),\qquad
 F(z,t)=(z^2-1)(t^4+1)-zt(t^2-1)
\]
has both outer coefficients \(z^2-1\).
Every positive-measure rational irreducible factor of \(Q_n\) therefore has degree \(\gg n\) and logarithmic measure \(\ge\eta>0\), uniformly in \(k\).
Finitely many small indices can be included by decreasing the constants over their finitely many positive factors.
By additivity the same positive floor holds for every positive-measure integral divisor of \(Q_n\).
Consequently even an additional arithmetic factorization of these \(Q_n\) cannot yield a sequence of divisors with positive measures tending to zero.
The assertion does not determine their irreducibility or factorization.

For the separate question of rotational symmetry, a complete orbit \(z,\omega z,\omega^2z\) of zeros of \(Q_n\), with \(\omega\) a primitive cube root, consists of roots of unity.
Indeed averaging the six-term completion at these three points retains only degrees divisible by three.
The average is \(z^{n/2+1}-1\) if \(n\equiv1\bmod3\), and \(z^{2n+2}-1\) if \(n\equiv2\bmod3\).
A product \(V(\omega z)V(\omega^2 z)\) can contain only two members of an orbit, as \(V(z)=z-2\) illustrates.
The factorwise floor applies irrespective of such partial orbits.

## Assessment history

### Decision general-template-whole

| Field | Value |
| --- | --- |
| date | 2026-11-07T18:06 |
| status | proved |
| reason | Independent review checked the general factor bounds and their dyadic application. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Factor bounds](#statement) | Linear factor degrees and positive total logarithmic measures at fixed template. |
| argument | [Radial estimates](#outer-coefficient-bound) | Uniform control from the two outer coefficients. |
| argument | [Moment transfer](#all-roots-to-factors) | Full root moments and both coefficient fields. |
| argument | [Dyadic consequence](#dyadic-application) | Exact quartic completion and the uniform positive divisor gap. |
| dependency | [Arithmetic square bound](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) | Part A at the full rational degree of the nontorsion unit. |
| dependency | [Fixed-template sector estimate](Yin_C_G0879_v1.md#angular-count) | Angular count with multiplicities for a bounded number of nonzero terms. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1104_v2.md#general-template-whole) | Entire v2 statement, proofs and application at the stated source scope. |

## Current assessment

[Selected decision](#decision-general-template-whole)
