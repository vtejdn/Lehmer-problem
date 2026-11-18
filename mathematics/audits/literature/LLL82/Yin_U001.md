---
author: Yin
---

<a id="lll82-u001"></a>
# Reduced lattice bases, Euclidean length bounds and integer complexity

<a id="reduction"></a>
## Reduction with parameter \(3/4\)

Let \(b_1,\ldots,b_n\) be a basis for a lattice in its Euclidean real span.
Write \(b_i=b_i^*+\sum_{j<i}\mu_{ij}b_j^*\), where \(b_i^*\) is perpendicular to the preceding basis vectors and \(\mu_{ij}=\langle b_i,b_j^*\rangle/\|b_j^*\|^2\).
Conditions (1.4)–(1.5) on PDF page 2 of the [article](readme.md#edition) define a reduced basis by \(|\mu_{ij}|\le1/2\) for every \(j<i\) and
\[
\|b_i^*\|^2+\mu_{i,i-1}^2\|b_{i-1}^*\|^2\ \ge\ \tfrac34\|b_{i-1}^*\|^2
\qquad(2\le i\le n).
\]
These imply \(\|b_{i-1}^*\|^2\le2\|b_i^*\|^2\).
Proposition (1.6), inequality (1.7) on PDF page 3, bounds the original basis vectors by
\[
\|b_j\|^2\le2^{i-1}\|b_i^*\|^2\qquad(1\le j\le i\le n).
\]
Indeed \(\|b_j\|^2=\|b_j^*\|^2+\sum_{t<j}\mu_{jt}^2\|b_t^*\|^2\le2^{j-1}\|b_j^*\|^2\), and iteration of the adjacent inequality supplies the remaining factor \(2^{i-j}\).
If \(i\) is the last index with nonzero integer coefficient in a lattice vector \(z=\sum_t m_tb_t\), its orthogonal component in the \(b_i^*\) direction is \(m_i b_i^*\).
Hence \(\|z\|\ge\|b_i^*\|\), as in the proof of Proposition (1.11) on PDF page 4.
In particular the first reduced basis vector is within a factor \(2^{(n-1)/2}\) of the shortest nonzero Euclidean length.

<a id="complexity"></a>
## Cost for an explicitly supplied basis

Algorithm (1.15) transforms the supplied basis into a reduced basis of the same lattice.
For a rank-\(n\) lattice in \(\mathbb Z^n\), take \(B\ge2\) with \(\|b_i\|^2\le B\) for all input basis vectors.
Proposition (1.26) on PDF page 8 bounds the number of integer arithmetic operations by \(O(n^4\log B)\) and their operand lengths by \(O(n\log B)\) bits.
The following remark gives \(O(n^6(\log B)^3)\) bit operations with classical arithmetic.
Remark (1.38) on PDF page 10 extends the analysis to an integral Gram matrix, so integer vectors in a higher-dimensional Euclidean space qualify by restricting to their span.
These statements concern explicit basis data.
An application that specifies the entries indirectly must account for their formation and bit lengths.

On 2026-11-18 the assigned agent inspected the two reduction conditions, the proof of (1.7) and the projection argument in (1.11).
The complexity assessment uses the statements of (1.26) and (1.38) and the classical bit bound accompanying (1.26).
The detailed complexity proof was outside this inspection.
The [two-residue estimator](../../../ledger/Yin_L_G0462_v151.md#reduction) derives its own admissible-vector bounds and estimates the size of the integer graph basis from its explicit input matrix.
