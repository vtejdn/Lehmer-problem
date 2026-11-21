---
author: Yin
---

# Geometric Brascamp–Lieb data and the Gaussian frame inequality

<a id="bcct08-u001"></a>
<a id="geometric-data"></a>
## Definition and source normalization

In Definition 1.1 let \(H,H_1,\ldots,H_n\) be finite-dimensional real Euclidean spaces with their Lebesgue measures, \(B_j:H\to H_j\) linear, and \(p_j\ge0\).
A datum is nondegenerate when all \(B_j\) are onto and their common kernel is zero.
For a nondegenerate datum the Brascamp–Lieb constant \(\operatorname{BL}(\mathbf B,\mathbf p)\) is the least \(C\), allowing \(+\infty\), for which
\[
 \int_H \prod_j f_j(B_jx)^{p_j}\,dx
      \le C\prod_j\left(\int_{H_j} f_j(y)\,dy\right)^{p_j}
\]
for all nonnegative measurable inputs with positive finite integrals.
Zero exponents may be omitted.
Definition 2.1 calls the datum geometric when \(B_jB_j^*=I_{H_j}\) for every \(j\) and \(\sum_j p_j B_j^*B_j=I_H\).
Each \(B_j^*\) then identifies \(H_j\) isometrically with a subspace of \(H\), with \(B_j\) acting as its orthogonal projection under this identification. [Definition 1.1, pp. 1–2](../../../literature/pdf/BCCT08--author.pdf#page=1) · [Definition 2.1 and Remark 2.2, p. 9](../../../literature/pdf/BCCT08--author.pdf#page=9)

<a id="gaussian-frame"></a>
## The constant for projections onto lines

Proposition 2.8 gives \(\operatorname{BL}(\mathbf B,\mathbf p)=1\) for geometric data, with Gaussian extremisers.
The paper attributes the geometric inequality to Ball and Barthe.
Example 1.6 states it for orthogonal projections onto subspaces resolving the identity. [Example 1.6, p. 3](../../../literature/pdf/BCCT08--author.pdf#page=3) · [Proposition 2.8, p. 12](../../../literature/pdf/BCCT08--author.pdf#page=12)

For unit vectors \(u_j\in\mathbb R^r\) and weights \(c_j>0\) with \(\sum_j c_j u_ju_j^{\mathsf T}=I_r\), take \(B_jx=\langle u_j,x\rangle\) and \(p_j=c_j\).
These maps are surjective and the identity gives a trivial common kernel.
With \(G_r\) a standard Gaussian in \(\mathbb R^r\) and \(g\) standard Gaussian in \(\mathbb R\), the resulting normalized inequality reads
\[
 \mathbb E\prod_j h_j(\langle u_j,G_r\rangle)^{c_j}
            \le\prod_j\big(\mathbb E h_j(g)\big)^{c_j}
\]
for nonnegative bounded measurable \(h_j\).
Indeed apply the Lebesgue inequality to \(f_j(y)=h_j(y)e^{-y^2/2}\).
The frame identity gives \(\sum_jc_j\langle u_j,x\rangle^2=\|x\|^2\), and taking its trace gives \(\sum_j c_j=r\), so the Gaussian normalizing constants agree.
A zero Gaussian integral means that the corresponding factor vanishes almost everywhere.

This inspection checked the stated constants, exponent placement, adjoints and Gaussian normalization in the [author edition](readme.md#edition).
The geometric inequality is accepted at statement scope.
Its heat-flow proof and the results for arbitrary Brascamp–Lieb data were outside the inspection.
