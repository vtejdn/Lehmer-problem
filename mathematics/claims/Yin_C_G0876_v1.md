---
author: Yin
---

# A convex hull for one nonreal trace pair and the degree-64 exclusion

<a id="statement"></a>
## Enclosure and finite application

Let \(m\ge0\), \(s_0<\cdots<s_m\) be real separators and \(Q\) a real monic polynomial of degree \(m+2\) with one real root in each open gap and one nonreal pair \(w,\bar w\).
Suppose the real coefficient pair \((-2\Re w,|w|^2)\) belongs to a rectangle with vertices \((a_j,b_j)\).
Write \(S(t)=\prod_{i=0}^m(t-s_i)\).
In any fixed monic polynomial coefficient representation related affinely to the usual coefficients, the vector of \(Q\) belongs to the convex hull of the \(4(m+1)\) vectors of
\[
 (t^2+a_j t+b_j)\,\frac{S(t)}{t-s_i}.
\]
No integrality or coefficient-height hypothesis is needed for this inclusion.

For \(m=30\), take the 31 rational separators in [the exact cell data](../computations/programs/Yin_J_G0144/trace64_cell.py), from \(-2\) to \(2\), and the closed disk centered at \((-177624+8300i)/100000\) of radius \(1/10000\).
There is no monic reciprocal integer polynomial \(P\) of degree 64 and height at most three whose monic trace polynomial \(Q\), determined by \(P(z)=z^{32}Q(z+z^{-1})\), has a real root in each of the 30 gaps and a root in that disk.
This finite exclusion keeps both the specified disk and all the prescribed gaps.
It is independent of the sufficient Rouché test used in the [original search proposal](../ledger/Yin_L_G0462_v1.md#complex-trace-cells).

<a id="argument"></a>
## Interpolation and the finite certificate

Set \(F(t)=Q(t)/((t-w)(t-\bar w))\).
This is monic of degree \(m\) with one simple root in each gap.
The signs of \(F(s_i)\) and \(S'(s_i)\) both equal \((-1)^{m-i}\).
Ordinary polynomial interpolation, or evaluation at all \(m+1\) nodes, gives
\[
 F(t)=\sum_i\lambda_i\, S(t)/(t-s_i),\qquad \lambda_i=F(s_i)/S'(s_i)>0 .
\]
Comparing leading coefficients gives \(\sum_i\lambda_i=1\).
The quadratic factor is a convex combination of the four corner quadratics by affine dependence on \((a,b)\).
Multiplying the two representations yields convex weights given by the products of the two sets of weights, proving the enclosure.

For the finite instance use \(C_k(z+z^{-1})=z^k+z^{-k}\) for \(k\ge1\).
The constant polynomial one followed by \(C_1,\ldots,C_{32}\) is a monic triangular integral basis.
The 32 free coordinates are exactly the central coefficient and the 31 independent noncentral coefficients below the leading term of \(P\).
Every height-three input therefore corresponds to one integer vector in \([-3,3]^{32}\).
The [verifier](../computations/programs/Yin_J_G0144/exact_cell_hull.py) constructs the rectangle by bounding the real and imaginary parts of the closed disk, then computes the 124 integer vertex numerators with common denominator \(D=1000^{30}\,100000^2\).
All subsequent vectors are ordered from the highest free frequency to the constant.

For a prefix \(p\) of length \(k\) and integral normal \(h\), the maximum of \(h\cdot x\) on that prefix box is
\[
 B(h,p)=\sum_{j<k}h_j p_j+3\sum_{j\ge k}|h_j|.
\]
If \(\min_v h\cdot v>D B(h,p)\) for the vertex numerators \(v\), the entire box is disjoint from the convex hull.
For any positive integer \(a\) and sign \(\sigma\), every vector in the intersection satisfies
\[
 \sigma x_k\le
 \left\lfloor
 \frac{D B(h,p)+\max_v(\sigma a v_k-h\cdot v)}{aD}
 \right\rfloor
\]
when \(x_k\) is integral.
This follows from applying the convex-hull maximum to the linear form \(\sigma a x_k-h\cdot x\).
Two such bounds give the entire necessary integer range for the next coordinate.
Starting at the empty prefix and visiting every integer child in that range loses no potential input.

The [fixed integer certificate](../computations/programs/Yin_J_G0144/exact_cell_hull_proof.json.gz) supplies the normals and scales, whose inequalities are recomputed directly at every prefix.
The verifier exhausts the tree after 959 internal prefixes and one leaf, with no outstanding branch.
That leaf is the degree-18 control multiplied by \(\Phi_{47}\), the seed of the inverse search.
Writing its \(Q(c+rs)=\sum_k b_k s^k\), exact evaluation gives
\[
 \max(|\Re b_0|,|\Im b_0|)>\sum_{k\ge1}(|\Re b_k|+|\Im b_k|).
\]
Thus \(Q\) has no zero on the closed disk \(|s|\le1\).
Combined with the necessary enclosure, this excludes every vector initially in the height-three box.
The [finite computation instructions](../computations/programs/Yin_J_G0144/readme.md#degree64-cell) identify the selected files and reproduction command.
Floating-point suggestions for the normals play no role in verifying the tree.
