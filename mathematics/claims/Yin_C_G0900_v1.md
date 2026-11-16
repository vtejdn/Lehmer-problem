---
author: Yin
---

# A uniform Mahler gap above a prescribed vertex coefficient

<a id="statement"></a>
## The gap

For integers \(K,m\ge1\) there exists \(\varepsilon(K,m)>0\) such that the following holds in every finite dimension \(s\ge1\).
Let \(P\in\mathbb Z[X_1^{\pm1},\dots,X_s^{\pm1}]\) be nonzero with at most \(K\) nonzero terms.
Suppose a vertex of the convex hull of its exponent vectors has coefficient of absolute value \(m\).
For the multiplicative Mahler measure \(M(P)=\exp\int_{\mathbb T^s}\log|P(X)|\,dX\), using Haar probability, one has
\[
                      M(P)=m\qquad\text{or}\qquad M(P)\ge m+\varepsilon(K,m).
\]
In one variable either endpoint coefficient suffices.
The bound is independent of the dimension, all exponents and all other coefficients.
The [endpoint investigation](../ledger/Yin_L_G0462_v97.md#endpoint) arose from a trace product with a nonmonic reciprocal factor.
The [fixed-support theorem of Dobrowolski and Smyth](../audits/literature/DS17/Yin_U001.md#ds17-u001) isolates multiplicative measure one in the unrestricted bounded-term class.
Here the vertex condition specifies the level \(m\).

<a id="endpoint"></a>
## Specialization and equality in the endpoint bound

In one variable remove an initial monomial and use reversal if the specified coefficient is at the lower endpoint.
The highest coefficient now has modulus \(m\), so the root product gives \(M(P)\ge m\).
For a monomial this is equality.
If there were no positive uniform gap, a sequence \(P_i\) with \(M(P_i)>m\) would have \(M(P_i)\to m\).
By the [sparse height inequality](../audits/literature/DS17/Yin_U002.md#sparse-height-bound), each polynomial with \(k\ge2\) terms has coefficient height at most \(2^{k-2}M(P_i)\).
Extract one \(k\le K\) and a fixed tuple \(a_0,\ldots,a_{k-1}\) of nonzero integer coefficients indexed by strictly increasing exponents, with constant \(a_0\) and \(|a_{k-1}|=m\).

Write \(\mathbf n_i\in\mathbb Z^{k-1}\) for the tuple of positive exponents.
Pass to a diagonal subsequence such that for each \(r\in\mathbb Z^{k-1}\), the relation \(r\cdot\mathbf n_i=0\) holds eventually or fails eventually.
The eventual relations form a saturated subgroup \(R\).
Their quotient \(\Gamma=\mathbb Z^{k-1}/R\) is free abelian of positive rank, and for large \(i\) evaluation at \(\mathbf n_i\) gives a homomorphism \(\lambda_i:\Gamma\to\mathbb Z\) because \(R\) is finitely generated.
In a fixed basis of \(\Gamma\), the shortest nonzero relation on the evaluation vector tends to infinity in maximum norm, allowing infinity for the empty set.
Indeed a bounded relation along a subsequence would repeat one fixed nonzero vector, contradicting stabilization.
Let \(v_0=0\) and let \(v_1,\ldots,v_{k-1}\) be the classes of the standard basis elements.
They are distinct, and \(F(X)=\sum_{j=0}^{k-1}a_j X^{v_j}\) specializes under \(\lambda_i\) to \(P_i\).
[Lawton's theorem](../audits/literature/Den09/Yin_U002.md#den09-u002) therefore gives \(M(F)=m\).

Fix such an \(i\) and let \(X\) vary over the dual torus \(\widehat\Gamma\).
The translated specialization
\[
                   P_{i,X}(z)=\sum_{j=0}^{k-1}a_j X^{v_j}z^{\lambda_i(v_j)}
\]
has distinct exponents and leading coefficient of absolute value \(m\) at every \(X\).
Hence \(\log M(P_{i,X})\ge\log m\) everywhere, and the left side is continuous in \(X\) by continuity of the roots at fixed degree with nonvanishing leading coefficient.
For fixed \(|z|=1\), multiplication by the character \(v\mapsto z^{\lambda_i(v)}\) preserves Haar probability on \(\widehat\Gamma\).
Apply this to \(\log|F|\), whose absolute value is integrable for the nonzero Laurent polynomial \(F\).
Translation and Fubini yield
\[
                \int_{\widehat\Gamma}\log M(P_{i,X})\,dX=\log M(F)=\log m .
\]
A continuous function bounded below by its mean on a torus is constant.
At the trivial character this gives \(M(P_i)=m\), contradicting the sequence.
Thus a single positive gap works for every allowed univariate polynomial.

<a id="vertex"></a>
## The same constant in arbitrary dimension

For a nonmonomial \(P\) in dimension \(s\) choose an integral functional \(u\) uniquely maximized at the marked vertex on its finite support.
Such a functional exists by strict separation, rational approximation and denominator clearing.
For positive integers \(t\) take the specialization vector
\[
                       b(t)=t^s u+(1,t,\ldots,t^{s-1}).
\]
For every nonzero \(r\in\mathbb Z^s\), the scalar \(r\cdot b(t)\) is a nonzero polynomial in \(t\), since its coefficients of degrees \(0,\ldots,s-1\) are the entries of \(r\).
Thus all support terms are eventually distinct and the shortest nonzero relation tends to infinity.
The marked vertex gives the unique top exponent eventually, as the term \(t^s u\) strictly separates it from the other exponents.
Lawton's theorem makes the specialized measures converge to \(M(P)\).
The univariate result places these measures in the same closed set \(\{m\}\cup[m+\varepsilon(K,m),\infty)\).
It also contains their limit, proving the dimension-independent claim.

## Assessment history

### Decision sparse-endpoint-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:04 |
| status | open |
| reason | Submit the uniform gap above a fixed vertex-coefficient modulus at bounded support, including all finite ambient dimensions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Vertex gap](#statement) | Positive gap depending only on the endpoint modulus and term count in any finite dimension. |
| argument | [Endpoint equality](#endpoint) | Sparse height, stabilization of frequency relations, Lawton convergence and equality for every torus translation. |
| argument | [Exposed specialization](#vertex) | A sequence of exposing integer functionals with shortest relation tending to infinity gives the same univariate gap in every dimension. |
| dependency | [Endpoint investigation](../ledger/Yin_L_G0462_v97.md#translations) | Stabilized polynomial and torus-translation endpoint bound for every actual specialization. |
| dependency | [Exposed vertex argument](../ledger/Yin_L_G0462_v97.md#vertex) | Explicit specializing vectors, distinct exponents and uniform endpoint modulus. |
| support | [Sparse heights](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Theorem 1 bounds univariate coefficient heights in terms of term count and bounded Mahler measure. |
| support | [Lawton specialization](../audits/literature/Den09/Yin_U002.md#den09-u002) | Theorem 14, fixed Laurent polynomial and increasing shortest sup-norm relation, in both limiting arguments. |

### Decision sparse-endpoint-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:07 |
| status | proved |
| reason | Independent review verifies isolation above a fixed vertex coefficient at bounded term count by equality under torus translations, with the same gap in every finite dimension. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Vertex gap](#statement) | Positive gap depending only on the endpoint modulus and term count in any finite dimension. |
| argument | [Endpoint equality](#endpoint) | Sparse height, stabilization of frequency relations, Lawton convergence and equality for every torus translation. |
| argument | [Exposed specialization](#vertex) | A sequence of exposing integer functionals with shortest relation tending to infinity gives the same univariate gap in every dimension. |
| dependency | [Endpoint investigation](../ledger/Yin_L_G0462_v97.md#translations) | Stabilized polynomial and torus-translation endpoint bound for every actual specialization. |
| dependency | [Exposed vertex argument](../ledger/Yin_L_G0462_v97.md#vertex) | Explicit specializing vectors, distinct exponents and uniform endpoint modulus. |
| support | [Sparse heights](../audits/literature/DS17/Yin_U002.md#ds17-u002) | Theorem 1 bounds univariate coefficient heights in terms of term count and bounded Mahler measure. |
| support | [Lawton specialization](../audits/literature/Den09/Yin_U002.md#den09-u002) | Theorem 14, fixed Laurent polynomial and increasing shortest sup-norm relation, in both limiting arguments. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v87.md#endpoint-gap) | Entire statement and both arguments, including both direct source inputs and the equality case for all torus phases. |

## Current assessment

[Selected decision](#decision-sparse-endpoint-reviewed)
