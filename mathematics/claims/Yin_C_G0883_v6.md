---
author: Yin
---

# Two individually invertible coefficient positions can stay far apart

<a id="positions"></a>
For unbounded genus there exist monic irreducible reciprocal unit polynomials with two noncentral coefficient pairs, each at an invertible index modulo the genus, for which the optimized cyclic-position cost is exactly \(\sqrt g\).
At the single prime two the entire degree returns in \(d\) steps.
Thus individual invertibility and even a complete modular return do not bound the simultaneous cost in the [circle-of-handles construction](Yin_C_G0883_v5.md#positions).

Take \(m=2^k\), \(k\ge2\), \(g=m^2\), and \(d=2g\).
Use \(I=\{1,m+1\}\) and
\[
 P=X^{2g}+1+2\sum_{i\in I}(X^{2g-i}+X^i).
\]
All four indicated intermediate exponents are odd and distinct.
Both indices are invertible modulo \(g\).
For a unit \(u\bmod g\) choose least absolute residue representatives \(U,V\) of \(u,(m+1)u\).
Their difference is congruent to \(mu\bmod m^2\), so it is a nonzero multiple of \(m\) since \(u\) is odd.
Consequently \(|U|+|V|\ge m\).
At the unit \(u=m-1\) the residues are \(m-1,-1\), proving equality.

<a id="arithmetic"></a>
The polynomial has constant term one and cannot be a polynomial in a proper power since the coefficient of \(X\) is nonzero.
Reduction modulo two gives \(X^{2g}+1=(X+1)^{2g}\), and \(P(1)=10\).
Thus \(P(X+1)\) is Eisenstein at two, proving irreducibility.
At \(X=-2\) the leading term cancels the term of degree \(2g-1\), and the other odd powers together with the constant give \(P(-2)<0\).
Since the degree is even and the polynomial is monic it has a root less than \(-2\).
In particular \(M(P)>2\), whereas modulo two \(\bar P=X^d-1\) gives \(\deg\gcd(\bar P,X^d-1)=d\).
These polynomials are outside the small-measure record range.
Their growing position cost leaves open a smaller-volume realization of the same polynomials and a stronger simultaneous constraint for actual strict records.

<a id="many"></a>
## Cost when the number of occupied positions grows

For \(s=|I|\) and any unit \(u\bmod g\), the \(s\) residues \(ui\) are nonzero and distinct.
At most two lie at each positive integer distance from zero.
Consequently \(\sum_{i\in I}\|ui\|_g\ge\sum_{\ell=1}^s\lceil\ell/2\rceil\ge s(s+1)/4\), also after minimizing over \(u\).
Along a hypothetical sequence of reciprocal records with \(M(P)\downarrow1\), the [bounded-support gap](../audits/literature/Dob06/Yin_U001.md#sparse-measure) forces \(s\to\infty\), since the full polynomial has at most \(2s+3\) terms.
Thus the sum of separate handle distances cannot itself be bounded uniformly or even by \(O(s)\) on that sequence.
This bounds the arithmetic expression used in the construction; the infimum of actual realization volumes need not grow as fast as this expression.

## Assessment history

### Decision cost-of-two-positions

| Field | Value |
| --- | --- |
| date | 2026-11-27T12:38 |
| status | proved |
| reason | Explicit reciprocal units attain the claimed minimum even with a complete return modulo two, and counting distances bounds the construction cost from below when the number of occupied positions grows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two invertible indices](#positions) | An exact square-root cost after minimizing the two-position sum. |
| argument | [Reciprocal units](#arithmetic) | Noncompression, Eisenstein irreducibility, measure range and full modular return. |
| argument | [Growing support](#many) | Quadratic floor for the sum of separate position costs and its consequence on hypothetical shrinking records. |
| dependency | [Circle of handles](Yin_C_G0883_v5.md#positions) | The particular constructive bound whose arithmetic cost is tested. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1289.md#finding) | All three sections, including the bounded-support and volume interfaces. |

## Current assessment

[Selected decision](#decision-cost-of-two-positions)
