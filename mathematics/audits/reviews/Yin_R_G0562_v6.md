---
author: Yin
---

# Review of one-sided isolation of the mass at the identity

An agent outside the development of C345v6 reviewed its complete fixed statement and argument for Yin on 2026-11-16T13:40 UTC.
The assignment supplied the claim and its scope without proof-development discussion or prior findings on this argument.

<a id="atom-isolation-review"></a>
## One-sided isolation

The proof establishes the absence of infinite strictly increasing sequences of identity masses for each fixed mass bound, with no restriction on the orders of the cyclic groups.

### Fourier normalization and the source theorem

For \(f(k)=\int v^k\,d\nu(v)\) on \(\mathbb Z/N\mathbb Z\), orthogonality gives \(N^{-1}\sum_k f(k)\xi^{-k}=\nu(\{\xi\})\) for every \(\xi\in\mu_N\).
Consequently \(\|f\|_{A}=\nu(\mu_N)\) by positivity.
I checked the normalization and the finite-group statement in Section 1 of [Sanders's published article](https://link.springer.com/article/10.1007/s00041-020-09732-y).
Theorem 1.1 bounds the total absolute value of integer coset coefficients uniformly in the group, so repetition gives a uniformly bounded number of signed indicators.
The source hypothesis \(M\ge1\) suffices because \(f(0)\) is a nonnegative integer, and a measure with mass less than one must be zero.
This review uses Sanders's theorem at statement level.

Each subgroup of index \(d\mid N\) consists of multiples of \(d\).
Summing \(\xi^{-k}\) over a translated subgroup \(r+d\mathbb Z\) gives zero unless \(\xi^d=1\), in which case the normalized sum is \(\xi^{-r}/d\).
This verifies the support, phase and coefficient of every term in (1), including the cases \(d=1,N\).

### Positivity for each class of growing denominators

The finite subsequence extraction fixes the signs and makes each reduced numerator and denominator of \(d_i/d_l\) either constant or divergent.
The pairs for which both are bounded are precisely those with a fixed rational ratio, so they form equivalence classes.
Clearing denominators and dividing by the gcd in a class gives a fixed primitive vector of positive integers \((k_i)\) and a common scale \(D\) equal to the gcd of the \(d_i\) in the class.
At the identity its contribution is exactly \(b/D\), where \(b=\sum_i\epsilon_i/k_i\) is fixed.

For a class with \(D\to\infty\), the translates of points in a single populated box of phases provide at least \(D/B\) distinct points of \(\mu_D\), where the number of boxes \(B\) depends only on the class size and \(\eta\).
Indeed division of points by one fixed point in the box is injective and puts every phase within \(\eta\) of one, even if the phase map has a kernel.
For a foreign index let \(g=\gcd(D,d_l)\).
When \(g/D\to0\), the term can occur at only \(o(D)\) of these points, since its support meets \(\mu_D\) in exactly \(g\) points.
Otherwise extract so that \(D/g\) is bounded.
If \(d_l/D\) had a bounded subsequence too, then \(d_l/g\) and \(k_iD/g\) would be bounded there for every \(i\) in the class.
Since \(g\) divides \(\gcd(k_iD,d_l)\), the two corresponding reduced ratios would both be bounded, contrary to the initial extraction and the choice of \(l\).
Thus \(d_l/D\to\infty\) in this case, and its contribution at any point has modulus at most \(1/d_l=o(1/D)\).

Removing the finitely many intersections of size \(o(D)\) leaves a test point at which the real part of \(D\) times the mass differs from \(b\) by at most \(s\eta+o(1)\).
Choosing \(\eta\) after fixing the class excludes every \(b<0\) by positivity.
This step rules out a genuine failure mode for signed measures.
For example, \(\delta_1\) minus uniform probability on \(\mu_N\) has integer Fourier coefficients and identity mass \(1-1/N\), but each other point of \(\mu_N\) has negative mass for \(N>1\).

### Limit and interval

On the extracted subsequence the identity masses are a fixed constant plus finitely many nonnegative terms that tend to zero.
A strictly increasing sequence with this limit must have every term strictly below it, contradicting that decomposition.
If every left neighbourhood of \(a\) contained an attainable mass strictly below \(a\), successive choices in the intervals between the last mass and \(a\) would give a strictly increasing sequence.
These arguments also cover the zero measure and a subsequence with no growing classes.

## Review relationships

| Review | Relationship |
| --- | --- |
| [One-sided isolation](#atom-isolation-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [One-sided isolation](#atom-isolation-review) | [C345v6 statement](../../claims/Yin_C_G0345_v6.md#statement) | All mass bounds, arbitrary finite cyclic support and the left interval for every real endpoint. |
| [One-sided isolation](#atom-isolation-review) | [C345v6 coset inversion](../../claims/Yin_C_G0345_v6.md#cosets) | Integer input, uniform term count, dual normalization, support and translated-coset phase. |
| [One-sided isolation](#atom-isolation-review) | [C345v6 growing denominators](../../claims/Yin_C_G0345_v6.md#isolation) | Class extraction, gcd scales, positive density of test points, separation of all foreign indices, positivity and the final limit. |
| [One-sided isolation](#atom-isolation-review) | [Sanders's finite abelian theorem](../literature/San20/Yin_U001.md#san20-u001) | Section 1 normalization and uniform signed-coset representation from the published Theorem 1.1, checked at statement and application level. |
