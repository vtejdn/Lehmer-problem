---
author: Yin
---

# Independent review of the full odd-conductor trace grid

At 2026-11-08T03:17 UTC a separately assigned AI reviewer for Yin inspected the complete fixed L464 v5, including its endpoint index estimate.
The reviewer had no part in developing the argument and used the proof and its cited mathematical materials without proof-generation dialogue, author explanations or earlier review conclusions about this transfer.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Odd-grid review](#odd-grid-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Odd-grid review](#odd-grid-review) | [Odd grid and product](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Full odd grid, quadrature degree, determinant and logarithmic bounds. |
| [Odd-grid review](#odd-grid-review) | [Five cuts and profiles](../../ledger/Yin_L_G0464_v5.md#five-cuts-and-original-profiles) | Transferred moment, equality and phase arguments and original lift. |
| [Odd-grid review](#odd-grid-review) | [Integral left endpoint](../../ledger/Yin_L_G0464_v5.md#only-left-endpoint) | One-sided inequality, unique limiting cut, five profiles and endpoint product. |
| [Odd-grid review](#odd-grid-review) | [Nonreal pair](../../ledger/Yin_L_G0464_v5.md#nonreal-pair-limit) | Pair location, all endpoint cases and normalized endpoint product. |
| [Odd-grid review](#odd-grid-review) | [Forbidden prefix](../../ledger/Yin_L_G0464_v5.md#odd-central-prefix) | Finite cutoff, filter constants, exact recovery and strict endpoint contradiction. |
| [Odd-grid review](#odd-grid-review) | [Conductor 29](../../ledger/Yin_L_G0464_v5.md#unit-signatures-and-bounded-offsets) | Entire binary signature image for the sampled generators and fixed-cut consequence. |
| [Odd-grid review](#odd-grid-review) | [Endpoint index exponent](../../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Near and far variation bounds, all fixed positive integer powers and logarithmic limit. |
| [Odd-grid review](#odd-grid-review) | [Fixed-radius unit heights](../../ledger/Yin_L_G0464_v5.md#fixed-radius-unit-magnitudes) | General matching bound, nonreal refinement and rejection criteria for prime-conductor units. |

<a id="odd-grid-review"></a>
## Finding on the complete argument

The statements follow under the strict sign transition and the endpoint condition in L464 v5, with the additional hypotheses on \(p\), whole measure and exceptional roots stated for each result.

**Grid and passage to a limit.**
The derivative of the sine quotient at a node and the paired products of the two sine factors give \(\prod_j|B'(b_j)|=p^{n-1}\) also for composite odd \(p\).
Discrete Fourier orthogonality gives the semicircle moments through \(p-3\), since \(h+2<p\) there.
The resultant identity then gives the geometric-mean bound, using \((p-1)\log(1-1/p)\ge-1\).
The two consecutive blocks of residue signs and the strict left endpoint supply the disjoint real-root matches, so the first three trace differences bound \(\sum\mu_j\).
The rational limit argument applies to \(F_p=P/B^*\) on compact subdisks, where \(B^*\) has no zero, and shrinking whole measure excludes interior zeros of the limit by reciprocity and Hurwitz's theorem.
The bounded-characteristic integrality theorem is used at the statement scope recorded for Cantor's Theorem 1. [Trace sums](../../ledger/Yin_L_G0462_v2.md#central-sign-test), [rational limits](../../ledger/Yin_L_G0464_v2.md#rational-prefix), [cyclotomic limits](../../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix), [Cantor source](../literature/Can63/Yin_U001.md#cantor-rationality).

For the fixed clearing polynomial, deleting its zeros loses at most \(O(\log p)\) from the needed lower bound for the sum of logarithms, since \(n\mu_j=O(p)\) and only boundedly many indices are deleted.
The remaining factors are controlled by the integral resultant with \(B/\gcd(A,B)\).
The exact moments and angular equidistribution give the continuous nonnegative density in the proof.
In the phase \(D_0\ne2\) its log mean equals the product threshold, and the entropy inequality gives the required mean absolute error tending to zero.
The first two cosine moments vanish, each moment is integral, and the uniform recurrence error is eventually below one, so induction recovers all residues after clearing.
This would bound the variation of the fixed nonzero weight \(A^2\) along a positive shrinking shell.
In the surviving phase the factor relating the original limit to the invariant function is \((1-z^2)/(1-z)=1+z\).
Positivity and integrability of \(-2(t-c_*)H\,d\nu\) off finitely many exceptional points give exactly the imported pole restrictions and interior sign order. [Moment comparison](../../claims/Yin_C_G0881_v1.md#moments), [saturation](../../claims/Yin_C_G0881_v1.md#saturation), [phase and recurrence](../../claims/Yin_C_G0881_v1.md#integer-recurrence), [five cuts](../../claims/Yin_C_G0881_v1.md#five-cuts), [interior cases](../../claims/Yin_C_G0881_v2.md#interior-list), [fixed-weight gap](../../claims/Yin_C_G0880_v2.md#statement).

**Left endpoint and profiles.**
Direct evaluation gives \(R_p(-2)=-P(-1)\le-1\), and \(S_p'(v)=-\sum_j\mu_j/(v-b_j)^2<0\) for \(v\le-2\).
These signs yield inequality (1) in its stated direction.
For \(c_*>-2\) a simple pole at \(-2\) has positive residue by the interior sign of \(H\), so \(R_*(v)\to+\infty\) from \(v<-2\), while regularity gives \(R_*(v)\to0\).
Sending \(p\) to infinity at fixed \(v\) before taking the endpoint rules out both cases.
At \(c_*=-2\), coprimality and even multiplicity of interior numerator zeros leave the two linear endpoint ratios and the three double-root ratios with \(x=-1,0,1\).
Expanding \(R_*=t-2x+O(t^{-1})\) fixes \(a_p=2x\) eventually on that profile.
The five reduced profiles have at most a simple left pole, which makes the right side of (1) tend to zero in the same order of limits.

**Nonreal pair.**
The positive-resolvent identity gives \(\sum\omega_j<4\), while the exterior radius tends to one, placing every pair limit \(y\) in \([-2,2]\).
If \(x\ne y\), division of the known interior density by \((t-y)^2\) gives a divergent integral on a punctured neighborhood of \(y\), including at either endpoint with the respective square-root factors of \(\nu\).
Thus \(y=x\), and the interior density alone contributes \(\int_{-2}^2 dt/(\pi\sqrt{4-t^2})=1\) to the weighted endpoint integral.
Lower semicontinuity allows further positive atoms, while the exact finite endpoint identity bounds this integral above by one in the limit.
This proves the ratio limit also for \(x=-2\), where its denominator tends to zero. [Positive resolvent and strict endpoint](../../ledger/Yin_L_G0464_v1.md#positive-resolvent).

**Finite prefix and conductor signatures.**
Agreement through index \(2047\) fixes \(a=-1\) and the signed moments through degree \(2045\), enough for the localization polynomial and the degree-\(2044\) filter multiplied by \(t-c_p\).
On the full odd grid the fourth powers of the roots are a permutation, and deleting the zero-angle term and pairing gives precisely the divisor \(p-1\).
At the smallest admissible \(p=8193\) the log correction is less than \(0.001417<1/600\), and the final error is at most \(0.436+2/8193+0.007<1/2\).
The integer recurrence therefore fixes \(r_j=b_j\nu_j\) and \(Q=t(B_n+B_{n-1})\), giving \(Q(-2)=0\).
The argument uses the strict endpoint and requires no measure ceiling. [Quadrature localization](../../ledger/Yin_L_G0464_v3.md#cut-localization), [filter](../../claims/Yin_C_G0881_v2.md#finite-filter), [product estimate](../../claims/Yin_C_G0881_v2.md#finite-product).

At \(p=29\) the reviewer enumerated the subgroup of binary vectors generated by the all-ones vector and the signs of \(\sin(2\pi aj/29)\) for \(2\le a\le14\).
It has \(2048\) elements, and multiplying each desired residue signature by the alternating derivative signs gives membership precisely at \(r=4,7,9\).
The three indicated rational multiples of \(29\) place \(+1,0,-1\) strictly in those gaps.
For any such fixed separator \(c\), positivity bounds \(\sum|(b_j-c)r_j|\) by the first three trace sums in a bounded shell, so the fixed-weight gap applies uniformly over the finite set of three weights. [Unit law](../../computations/programs/Yin_J_G0146/readme.md#unit-law), [conductor-29 calculation](../../computations/programs/Yin_J_G0146/readme.md#replay).

**Rate at the endpoint.**
Writing \(k=n-r\) gives \(\theta_c=\pi-2\pi k/p\), so \(k=o(p)\), \(\delta\asymp k^2/p^2\) and the nearer neighboring node is at distance \(\asymp k/p^2\) in trace, uniformly down to \(k=1\).
At the left endpoint, \(S_p(-2)=-\sum\mu_j/(2+b_j)\) recovers the stated identity, whose positive sum has an upper bound in terms of \(R\) because \(P(-1)\ge1\).
For \(2+b_j\le2\delta\), division by the minimum trace distance costs \(O(\delta/\Delta)=O(k)\) relative to this bound.
For \(2+b_j>2\delta\), division costs at most \(2/(2+b_j)\), giving bounded total variation there.
Multiplication by \((t+2)^h\) gives \(O_{R,h}(1+\delta^h k)\).
The fixed-weight gap forces \(\delta^h k\to\infty\) for every fixed \(h\ge1\), hence the ratio and logarithmic conclusions in the statement.
Bounded conductors cannot evade the final exclusion since bounded-degree monic integer polynomials in a bounded whole-measure shell have bounded coefficients.

**Unit magnitudes.**
The disjoint interval variation contributes at most \(2^{h+1}\), the unmatched pole at most \(2^h\), and each remaining trace at most \(R+R^{-1}\) in modulus.
Substitution in the three Newton identities gives the displayed \(A_R,K_R,T_R\).
For a nonreal pair its exterior radius is \(\sqrt{M(P)}\), and the strict mass bound four gives the claimed sharper estimate.
The derivative formula yields \(d_j\le8\), and \(\mathbb E\log^+(1/d_j)=\mathbb E\log^+d_j-\mathbb E\log d_j\le\log16\).
Using \(\mathbb E(d_j|C_j|)=T\) in Jensen's inequality gives the stated height bound, and the unit norm gives the factor of two in the sum of absolute logarithms.
These are necessary tests for the signed prime-unit law with arbitrary integral exponents. [Circular-unit conjugates](../literature/DDK19/Yin_U001.md#sine-signatures).

The cited source inputs support the uses above at their recorded statement and applicability scopes, including the [finite-group Fourier decomposition](../literature/San20/Yin_U001.md#san20-u001) and [fixed-support Mahler gap](../literature/DS17/Yin_U001.md#ds17-u001) underlying the fixed-weight theorem.
Their original source proofs were outside this review.
The result gives necessary profiles and growth conditions for a shrinking shell, together with finite exclusions and height tests.
The argument leaves open the existence of a shrinking shell on the entire odd grid.
