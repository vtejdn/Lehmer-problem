---
author: Yin
---

# Third moments and the full Mahler cost at conductor 6561

<a id="statement"></a>
## The negative-one profile on the logarithmic cut

For \(p=6561,\ n=3280,\ b_j=2\cos(2\pi j/p)\), \(1\le j\le n\), put \(B=\prod_j(t-b_j)\).
Let \(D=B_{n-1}\) in the [odd-grid convention](../ledger/Yin_L_G0464_v5.md#odd-grid-product).
Take any \(h\in\mathbb Z[t]\) positive at the first 2534 nodes and negative at the last 746, with \(\Delta=\prod_j|h(b_j)|=2^{1502}\).
Put \(r_j=(4-b_j^2)h(b_j)/p,\ C=Dh\bmod B,\ Q=(t+2)B+C,\ P=z^{n+1}Q(z+z^{-1})\).
Suppose \(\sum r_j=3,\ \sum b_jr_j=4,\ P(-1)>0\).
Then \(P(-1)=1\) and \(N=\sum b_j^2r_j\in\{8,9,10\}\).
Exactly two trace roots of \(Q\) are nonreal, forming a conjugate pair, and all its other roots lie in \((-2,2)\).
The complete multiplicative measure satisfies
\[
 N=8\ \Longrightarrow\ M(P)>2209/1600,\qquad
 N=9\ \Longrightarrow\ M(P)>16/9,\qquad
 N=10\ \Longrightarrow\ M(P)>49/25 .
\]
This applies to all integral inputs of the specified signs and absolute norm and does not assert existence.
The [earlier version](Yin_C_G0882_v1.md#statement) owns the general orbit test and five smaller conductors.

<a id="argument"></a>
## Integral traces and the exceptional pair

The separator \(-68/45\) and the integer endpoint give \(1\le U=\sum r_j/(2+b_j)<2\), so \(P(-1)=U=1\).
Another positive sum gives \(N\le10\).
The cubic \(H=t^3-2t^2-2t+5\) has its only real root in the prescribed gap.
On a primitive layer of degree \(d=3^{\ell-1}\), write \(h=2^{t_\ell}f_\ell\) for an integral unit \(f_\ell\) there.
The normalized trace of \((2-b)H(b)f_\ell(b)\) is an integer strictly greater than 2 by the layer norm and its resultant with \(H\).
The [eight layer certificates](../ledger/Yin_L_G0464_v13.md#cubic-layer-traces) give
\[
 N-5\ \ge\ \frac{3}{p}\sum_\ell d\,2^{t_\ell}
       \ \ge\ \frac{3(3280+1502)}{6561}>2 .
\]

The endpoint and the same-sign intervals pair \(n-1\) real trace roots with their right poles.
For \(f=-t^4+5t^3/3+3t^2/2-9t/4\), the first four trace differences and the negative variation of \(f\) bound the sum of \(f\) at the two remaining roots strictly above twice its maximum on the real line.
They are therefore nonreal conjugates.
For each possible \(N\), the [quartic Sturm certificate](../ledger/Yin_L_G0464_v13.md#ellipse-quartic) bounds the real part of \(f\) on the corresponding filled ellipse strictly below its real part at either exceptional root.
Each exterior radius exceeds the ellipse parameter and the complete lift has measure equal to its square.

## Assessment history

### Decision complete-cost-6561

| Field | Value |
| --- | --- |
| date | 2026-11-08T07:08 |
| status | proved |
| reason | Independent whole-proof review checked the endpoint, integral layer traces, Sturm certificates and complete root accounting for every input in the stated class. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete lift at conductor 6561](#statement) | The specified branch, signs, norm, two moments and strict endpoint. |
| argument | [From normalized layer traces to ellipses](#argument) | The three possible third moments, conjugate trace pair and whole-measure bounds. |
| dependency | [Integer cubic test](../ledger/Yin_L_G0464_v13.md#cubic-layer-traces) | All eight primitive layers and all valuation allocations with the stated total norm. |
| dependency | [Quartic and ellipse test](../ledger/Yin_L_G0464_v13.md#ellipse-quartic) | Negative variation, the three rational Sturm comparisons and both exterior roots. |
| review | [Independent whole argument](../audits/reviews/Yin_R_G1107_v7.md#whole-6561) | All assertions and hypotheses of this version, including the endpoint equality. |

## Current assessment

[Selected decision](#decision-complete-cost-6561)
