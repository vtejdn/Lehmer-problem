---
author: Yin
---

# A convex hull for one nonreal trace pair and a height-free degree-64 exclusion

<a id="statement"></a>
## The unrestricted coefficient cell

Suppose \(s_0<\cdots<s_m\) are real and \(Q\) is monic of degree \(m+2\), with one root in each open gap and one conjugate pair \(w,\bar w\) off the real axis.
Write \(S(t)=\prod_i(t-s_i)\).
If the coefficient vector \((-2\Re w,|w|^2)\) lies in a closed rectangle with corners \((a_j,b_j)\), then the vector of \(Q\) lies in the convex hull of the \(4(m+1)\) vectors of
\[
             (t^2+a_jt+b_j)\,S(t)/(t-s_i).
\]
This holds in monomial coordinates and in any affine change of coordinates on the monic coefficient space.

For \(m=30\), use the 31 [specified rational separators](../computations/programs/Yin_J_G0144/trace64_cell.py), from \(-2\) to \(2\).
Use the closed disk centered at \((-177624+8300i)/100000\) with radius \(1/10000\).
There is no monic polynomial \(Q\in\mathbb Z[t]\) of degree 32 with a root in each of these 30 open real gaps and an additional root in that disk.
Equivalently the specified configuration cannot occur in the trace polynomial of any monic reciprocal \(P\in\mathbb Z[z]\) of degree 64.
The integer coefficients may have arbitrary size.
The disk and all the real separators are fixed in this assertion.
[V1](Yin_C_G0876_v1.md#statement) retains the first height-three search with its separate certificate.

<a id="argument"></a>
## Interpolation, natural coordinate bounds and exact search

Let \(F=Q/((t-w)(t-\bar w))\).
This is monic with one root in each gap, so \(F(s_i)\) and \(S'(s_i)\) both have sign \((-1)^{m-i}\).
The interpolation weights \(\lambda_i=F(s_i)/S'(s_i)\) are strictly positive.
Evaluation at the nodes gives \(F=\sum_i\lambda_i S/(t-s_i)\), and the leading coefficients give \(\sum_i\lambda_i=1\).
Multiplying by a convex combination of the four corner quadratics proves the enclosure by taking products of the two sets of convex weights.

For the numerical cell use the constant polynomial one and the polynomials \(C_k(t)\) defined for \(k\ge1\) by \(C_k(z+z^{-1})=z^k+z^{-k}\).
They form a monic unitriangular integral basis in every finite degree.
Thus an integral monic \(Q\) corresponds bijectively to the integer free coefficient vector of \(P=z^{32}Q(z+z^{-1})\).
The [common vertex construction](../computations/programs/Yin_J_G0144/exact_cell_hull.py) encloses the closed disk in its coordinate rectangle and bounds \(-2\Re w\) and \(|w|^2\) from its respective extreme real and absolute coordinate values.
It expands the 124 vertices in the Chebyshev basis in descending frequency order, with integer vertex numerators \(v\) and common denominator \(D=1000^{30}100000^2\).
The [height-free verifier](../computations/programs/Yin_J_G0144/exact_cell_unbounded.py) initializes each coordinate with the two bounds
\[
             L_j=\left\lceil\min_v v_j/D\right\rceil,\qquad
             U_j=\left\lfloor\max_v v_j/D\right\rfloor .
\]
They follow from convexity and integrality alone.
For example they range from \(0\) to \(3\) for the highest free coefficient and from \(-48\) to \(41\) for the central coefficient.

For an integer normal \(h\) and fixed prefix \(p\) of length \(k\) the box maximum is
\[
 B(h,p)=\sum_{j<k}h_jp_j+\sum_{j\ge k}\max(h_j L_j,h_j U_j).
\]
If \(\min_v h\cdot v>D B(h,p)\), this prefix cannot meet the hull.
For a positive integer scale \(a\) and either sign \(\sigma\), every feasible integer vector with this prefix satisfies
\[
  \sigma x_k\le \left\lfloor
    \frac{D B(h,p)+\max_v(\sigma a v_k-h\cdot v)}{aD}
                    \right\rfloor.
\]
Indeed evaluate the linear form \(\sigma a x_k-h\cdot x\) on the hull and bound \(h\cdot x\) on the prefix box.
Taking a separate bound for each sign and visiting every integer child in the resulting interval retains every possible coefficient vector.
The [fixed natural-box certificate](../computations/programs/Yin_J_G0144/exact_cell_unbounded_proof.json.gz) supplies normals and scales for these exact checks.
The verifier recomputes the inequalities and visits all required branches using integer arithmetic.

After 2639 internal prefixes there are two leaves.
For the seed the constant term of \(Q(c+rs)\) in modulus exceeds the sum of the moduli of all its nonconstant coefficients, as certified by the stronger real-and-imaginary component inequality in the verifier.
Hence the seed has no root for \(|s|\le1\).
The other leaf has coefficient height four and \(Q(-2)=0\).
The required 30 distinct open-gap roots and conjugate pair already account for all 32 roots, so a root at the separator \(-2\) is impossible.
This excludes both leaves and proves the asserted empty cell.
The [computation record](../computations/programs/Yin_J_G0144/readme.md#degree64-cell) provides the exact input and reproduction instructions.

## Assessment history

### Decision entire-natural-box

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:06 |
| status | proved |
| reason | An independent review reconstructed the interpolation hull, the full unrestricted-height tree and both terminal exclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete unrestricted-height statement](#statement) | One-pair enclosure and the specified degree-64 cell for every integer height. |
| argument | [Complete interpolation and finite proof](#argument) | Natural coordinate bounds, exhaustive exact tree and terminal checks. |
| review | [Independent natural-box finding](../audits/reviews/Yin_R_G1101_v1.md#natural-box-finding) | Full fixed statement, argument and computational certificate. |

## Current assessment

[Selected decision](#decision-entire-natural-box)

