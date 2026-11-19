---
author: Yin
---

<a id="hen02-u001"></a>
# Minkowski's upper bound for the product of successive minima

Henk states Minkowski's second theorem for any full-rank lattice \(\Lambda\) in \(\mathbb R^r\) and any full-dimensional compact convex body \(K=-K\).
Here \(\det\Lambda\) is the volume of a fundamental parallelepiped, and \(\operatorname{vol}_r\) uses the same Lebesgue measure. [Theorem 1.3 on preprint page 2](../../../literature/pdf/Hen02--arxiv-v1.pdf#page=2)

<a id="minima"></a>
## Successive minima

For \(1\le i\le r\), the \(i\)-th successive minimum \(\lambda_i(K,\Lambda)\) is the least \(t\ge0\) such that \(tK\) contains \(i\) linearly independent lattice points. [Definition on preprint page 1](../../../literature/pdf/Hen02--arxiv-v1.pdf#page=1)
For the Euclidean unit ball these are the successive Euclidean lengths of independent lattice vectors.

Theorem 1.3 gives
\[
  \operatorname{vol}_r(K)\prod_{i=1}^r\lambda_i(K,\Lambda)\le 2^r\det\Lambda.
\]
A rank-\(r\) lattice in an ambient Euclidean space meets the full-rank hypothesis in its real span, with the induced Euclidean volume.
In orthonormal coordinates the Euclidean unit ball contains the cube \([-1/\sqrt r,1/\sqrt r]^r\), which gives \(\prod_i\lambda_i\le r^{r/2}\det\Lambda\).
The inspection covered the definitions, the theorem statement and this specialization in the [author preprint](readme.md#edition).
The theorem is used as an established input, with Henk's proof in Section 3 outside this inspection.
