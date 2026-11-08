---
author: Yin
---

# Conditional shell probabilities and distinct irreducible measures

Both findings are independent whole-argument reviews for Yin, performed on 2026-11-08 at 02:06 UTC.
The reviewer received the two fixed texts, their dependency locators and the requested scope, took no part in their development and consulted no development dialogue, author explanations or prior findings on either text.

<a id="conditional-sublevel-finding"></a>
## Conditional probability at fixed \(R>1\)

The [claim](../../claims/Yin_C_G0870_v2.md#statement) holds for the stated uniform sublevel law.
The elementary symmetric sum bounds put every sublevel polynomial in a finite covering box, and the neutral example makes the conditioning denominator positive.
For a cyclotomic product of even degree, constant one forces even multiplicity at \(1\), and degree parity then forces even multiplicity at \(-1\).
For an unrestricted product of odd degree exactly one of these exponents is odd.
Deleting one copy of the corresponding factor and counting the two inverse choices proves \(c(2n+1)=2Z_n\), including \(n=0\).

I checked the unrestricted counting definition and Euler product against pp. 9–10 of the retained MPV98 author version and visually checked the formula following (3.12) against the [source unit](../literature/MPV98/Yin_U002.md#unrestricted-cyclotomic-products).
The unrestricted count satisfies \(c(d)\sim A e^{B\sqrt d}/(d\sqrt{\log d})\).
The adjacent multiplicity-at-most-two theorem concerns another count.
For \(0\le h\le\sqrt n\), the smaller index \(2(n-h)+1\) grows uniformly and the difference of square roots is at most \(\sqrt2\).
Bounding the relative asymptotic factors between \(1/2\) and \(3/2\) gives \(Z_{n-h}/Z_n\ge e^{-\sqrt2 B}/3=\kappa\) for all sufficiently large \(n\).
This uses Boyd and Montgomery's asymptotic as reported by MPV98, without inspection of its original proof.

The trace substitution doubles each endpoint multiplicity because \(x+x^{-1}\mp2=(x\mp1)^2/x\).
Cyclotomic removal therefore gives a monic reciprocal core \(F\) of positive even degree \(2r\).
A root of unity cannot have a non-torsion \(j\)-th power, and grouping the \(j\) roots above each root of \(F\) preserves its Mahler factor.
Unique removal recovers the entire \(F(x^j)\), whose degree distinguishes \(j\), and then recovers each neutral multiplier.
The injection gives a conditional neutral probability at most \((1+\kappa\lfloor\sqrt n/r\rfloor)^{-1}\), with \(r\) fixed by the selected witness for this \(R\).
The empty-shell case gives zero positive probability in every degree.
I checked the unrestricted equivalence by applying the [reciprocal reduction](../../claims/Yin_C_G0870_v1.md#argument) in arbitrarily small shells below the plastic number, which suffices for all larger thresholds by inclusion.
A rerun of the [degree-ten height-one control](../../computations/programs/Yin_J_G0144/readme.md) returned the two sign-related strict hits among 243 inputs at \(R=6/5\).
All mass produced by this injection at fixed \(R\) has the original witness's single measure.

<a id="distinct-ternary-measures-finding"></a>
## Distinct measures and the fixed-degree controls

The [ledger result](../../ledger/Yin_L_G0462_v3.md#different-measures-one-degree) holds on its sequence of even degrees, together with its separately quantified benchmarks.
I checked the delay shift \(Q_N=P_{N+1}\), the coefficient blocks, the unit-circle comparison, the exterior-root sign and monotonicity argument, and the unique positive-factor inference in [C578](../../claims/Yin_C_G0578_v1.md#plastic-tree-all-root-cost).
The [McM02 identification](../literature/McM02/readme.md#three-arm-tree-attribution-20261010) supplies the classical tree attribution.
The signed minimal-block lemma in [C262](../../claims/Yin_C_G0262_v2.md#minimal-vanishing-order) applies to the six terms even when two formal points give the same root of unity.
For the changed signs, a vertical rank-one partition would force \(f\) to vanish on the circle, while a nonvertical rank-one partition would translate the column sums by three times an integer.
The sums 4 and 5 rule this out.
The [C270 lattice argument](../../claims/Yin_C_G0270_v1.md#rank-two-cyclotomic-bound) then gives order dividing 30 or \(6h\) for \(1\le h\le6\), and every such order divides 360.
As a direct base check, the binary polynomial Euclidean algorithm gives \(\gcd(Q_8\bmod 2,x^{360}-1)=1\), excluding a common monic factor over \(\mathbb Z\).
On the specified progression, \(F_N\) takes the values of \(F_8\) on these roots and \(F_N'(1)=7-N\), so division by \(x-1\) removes the only cyclotomic zero.

The elementary binomial bound leaves at least \(12k\) eligible primes in the indicated interval for large \(k\).
The common invertible residue and the single choice of \(a\) give \(d_S\equiv10\bmod360\) for every subset of size \(\lfloor k/2\rfloor\).
All these degrees tend uniformly to infinity.
For \(\beta=u^p\) in \(K\), both \(u\) and \(u^{-1}\) are integral over the algebraic integers and \(\mathbb Q(u)=K\), so \(d h(u)=\log\beta/p\).
I checked [Voutier's normalization and theorem](../literature/JT26/Yin_U001.md#external-inputs) on pp. 1 and 3 of the retained author version.
Its lower bound exceeds \((\log\theta)/k^4\) for large \(k\) because \(\log D\le\log360+5k\log k\), which excludes every \(p\mid h_S\) simultaneously.
For a degree-\(j\) proper factor of \(x^h-\beta\), the root product divided by \(\beta^{j/h}\) is a real root of unity in the chosen embedding.
Hence \(\beta^{j/h}\in K\), and Bézout forces a forbidden prime power in \(K\).
The degree tower proves irreducibility at degree \(D\).
Root grouping preserves measure, and strict monotonicity distinguishes the measures at the distinct base degrees.
The central binomial coefficient is at least \(2^k/(k+1)\), and \(\log D\asymp k\log k\), giving the claimed exponent and probability after division by \(3^{D/2}\).
Strict increase to \(\theta\) together with the growing minimum base degree gives the one-sided concentration.

For \(D=2t\ge22\), I checked the \(t-10\) nonoverlapping shifts and the additional unshifted input of distinct measure.
At \(b=6/5\), the two cross-multiplication margins \(271\cdot5^8-59\cdot6^8=6762031\) and \(59\cdot6^9-271\cdot5^9=65287189\) select only \(N=8\) from the plastic family.
The cited [fixed-seed comparison](../../claims/Yin_C_G0376_v2.md#irreducible-lehmer-radical-control) applies to prime exponents greater than 40.
For separated binomials the least exponent after seed cancellation recovers each successive factor.
The slack choices give \(2^{k(k+1)/2}\) products of the required degree, with \(k=\log_2D+O(\log\log D)\).
At a given length \(l\), the upper bound follows from \(D\ge2^{l-j}u_j\) at every position, and maximizing the resulting quadratic gives the same leading constant \(1/(2\log2)\).
The separated products all have measure \(\lambda_8<6/5\).
The different irreducible measures in the subsequence approach \(\theta\).
The height argument accepts Voutier's theorem at statement level, without a new review of its proof.
The existence of Mahler measures arbitrarily close to one from above remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conditional probability](#conditional-sublevel-finding) | independently reviewed |
| [Distinct measures](#distinct-ternary-measures-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conditional probability](#conditional-sublevel-finding) | [Statement](../../claims/Yin_C_G0870_v2.md#statement) | Whole fixed-\(R\) conditional law, alternative, rate, \(6/5\) and unrestricted equivalence. |
| [Conditional probability](#conditional-sublevel-finding) | [Neutral count](../../claims/Yin_C_G0870_v2.md#neutral-count) | Exact generating series and odd-degree identity, MPV98 interface and uniform square-root window. |
| [Conditional probability](#conditional-sublevel-finding) | [Amplification](../../claims/Yin_C_G0870_v2.md#amplification) | Deflation, substitution, disjoint injection, fixed-witness constant and scope as \(R\) varies. |
| [Distinct measures](#distinct-ternary-measures-finding) | [Statement](../../ledger/Yin_L_G0462_v3.md#different-measures-one-degree) | Ternary law, subsequence, distinct irreducible measure count, concentration and probability. |
| [Distinct measures](#distinct-ternary-measures-finding) | [Base progression](../../ledger/Yin_L_G0462_v3.md#minus-delay-progression) | Sparse signs, height, all-root input, order bound and irreducibility on the stated progression. |
| [Distinct measures](#distinct-ternary-measures-finding) | [Degree alignment](../../ledger/Yin_L_G0462_v3.md#same-degree-radicals) | Prime supply, simultaneous congruences, moving-degree height bound, binomial irreducibility and count. |
| [Distinct measures](#distinct-ternary-measures-finding) | [Benchmarks](../../ledger/Yin_L_G0462_v3.md#fixed-degree-benchmarks) | Every-even-degree count, \(6/5\) threshold, separated-binomial count and limits. |
