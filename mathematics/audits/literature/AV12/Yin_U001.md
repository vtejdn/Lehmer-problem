---
author: Yin
---

# Height outside torsion cosets of a rational hyperplane

<a id="av12-u001"></a>
## Theorem 1.1 and the torsion locus

In the [published edition](readme.md#published), pages 355–357 (PDF pages 1–3), Amoroso and Viada use the absolute logarithmic projective height of \((1:x_1:\cdots:x_n)\).
For a proper \(\mathbb Q\)-irreducible subvariety \(V\) of \(\mathbb G_m^n\), let \(V^*\) be the complement in \(V\) of every torsion translate of a subtorus contained in \(V\), including isolated torsion points.
<a id="degree-of-definition"></a>
Definition 2.1(iii) on page 360 assigns a projective variety defined over \(K\subset\overline{\mathbb Q}\) the least integer \(\delta_K(V)\) bounding the degrees of a family of \(K\)-hypersurfaces whose intersection equals \(V\) as a set.
The unsubscripted \(\delta(V)\) uses \(K=\overline{\mathbb Q}\), with a torus variety represented by its closure in \(\mathbb P^n\) under the indicated embedding.

For \(n\ge2\), \(d=\dim V\) and every algebraic point \(x\in V^*\), Theorem 1.1 on page 357 gives
\[
 h(1:x_1:\cdots:x_n)\ \ge
 \delta(V)^{-1}\bigl(935n^5\log(n^2\delta(V))\bigr)^{-(d+1)(n+1)^2}.
\]
Corollary 1.4 on pages 358–359 identifies the Zariski closure of the points of height at most this threshold with the union of the maximal contained torsion translates.
The overbar in the printed corollary denotes this closure.

For a relation \(\sum_{i=1}^s c_i u_i=0\) with \(s\ge3\), \(c_i\in\mathbb Q^*\) and \(u_i\in\overline{\mathbb Q}^{\,*}\), divide by \(u_1\) to put the projective vector \((u_1:\cdots:u_s)\) in the affine chart of a rational hyperplane.
Its torus part is irreducible, with \(n=s-1\), \(d=s-2\) and \(\delta(V)=1\).
On a contained torsion translate the coordinate ratios \(u_i/u_1\), including \(1\), are products of torsion constants and characters.
Terms belonging to each distinct character must sum to zero because different Laurent characters are linearly independent.
With all \(c_i\ne0\), each resulting group therefore contains two or more terms whose ratios are torsion.
Consequently the theorem gives a height floor independent of the rational coefficients whenever every pairwise ratio is nontorsion.
If the projective height is strictly below the threshold and the relation has no nonempty proper vanishing subsum, all the ratios are torsion.
This checks the applicability of Theorem 1.1 to rational hyperplanes at statement level.
The authors' proof of the general theorem was not audited.

<a id="example"></a>
## A family with growing dimension

On pages 359–360 (PDF pages 5–6), the authors take the \(n\ge3\) roots \(a_1,\ldots,a_n\) of \(X^n-2X-6\).
Eisenstein at two gives irreducibility, and the vanishing coefficient of \(X^{n-1}\) gives \(\sum_i a_i=0\).
Writing \(h_0=h(1:a_1:\cdots:a_n)\), the componentwise identity \(a_i^n=2a_i+6\) and the projective height inequalities give \(nh_0\le h_0+\log24\).
If \(u=a_i/a_j\) were torsion for distinct roots, subtraction of their equations would give \((1+u+\cdots+u^{n-1})a_j^{n-1}=2\).
The geometric sum is integral and belongs to \(\mathbb Q(a_j)\) by this identity.
Taking norms would force three to divide a power of two since \(|\operatorname{Norm}(a_j)|=6\).
Thus all pairwise ratios are nontorsion while the joint height is at most \(\log(24)/(n-1)\).
The same upper bound holds for each \(h(a_i/a_j)=h(a_i:a_j)\) by projecting the projective vector onto those two nonzero coordinates.
The example and its proof were checked directly.
