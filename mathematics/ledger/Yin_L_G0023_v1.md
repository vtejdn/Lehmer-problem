---
author: Yin
---

# G0001: quantitative metric rigidity for integral entropy models

Date: 2026-10-06.
The current complete mathematical home is [the matrix realization and metric theorem](../claims/Yin_C_G0227_v1.md#argument), with [actual complete self-review](../audits/reviews/Yin_R_G0512_v1.md#current-matrix-realization-finding).
The original mathematical body remains here as its dated review input and substantive exploration.
This tests a concrete additional condition on the positive metric in [L G0022](Yin_L_G0022_v1.md#stable-lattice-metric-boundary).
The conclusion is restricted and does not assert that such a metric or basis exists for arbitrary small-entropy objects.
The matrix gap is the accepted external [MS12 Corollary2](../audits/literature/MS12/readme.md); the estimates below are elementary direct calculations, with no novelty claim.

<a id="metric-rigidity"></a>
## Integer skew part versus a well-conditioned metric

Let A be an integer N-by-N matrix and G a real symmetric positive definite matrix such that GA=A^T G.
Write kappa=lambda_max(G)/lambda_min(G), and rho=rho(A).
All norms below are Euclidean operator norms.
The symmetric matrix S=G^(1/2) A G^(-1/2) satisfies ||S||=rho, so

    ||A|| <= sqrt(kappa)*rho.

Scale G by the midpoint of its smallest and largest eigenvalues, writing the result I+E.
Then

    ||E||=(kappa-1)/(kappa+1)=epsilon,
    A-A^T=A^T E-EA.

Consequently

    ||A-A^T|| <= 2 epsilon sqrt(kappa) rho.              (1)

A nonzero integer matrix has operator norm at least one, since some entry has absolute value at least one.
Therefore

    2*(kappa-1)/(kappa+1)*sqrt(kappa)*rho < 1
       implies A=A^T.                                  (2)

No bound on N, integrality of G, or determinant condition on G is needed.
The condition is invariant under multiplying G by a positive scalar, but is not invariant under arbitrary integral changes of basis.

<a id="conditioned-matrix-gap"></a>
## A dimension-independent restricted entropy gap

Let R_A(t)=t^N det((t+t^(-1))I-A), which is monic integral and reciprocal.
Its measure M=M(R_A) is at least one.
Since the eigenvalues theta of A are real, their reciprocal quadratic factors show

    rho <= M+M^(-1).

Indeed, for |theta|<=2 this follows from M+M^(-1)>=2.
Otherwise the corresponding factor has measure u>1 with |theta|=u+u^(-1), and u<=M.

If kappa<=3/2 and M<sqrt(3/2), then epsilon<=1/5 and monotonicity of x+x^(-1) on [1,infinity) gives

    2 epsilon sqrt(kappa) rho
      < (2/5)*sqrt(3/2)*(sqrt(3/2)+sqrt(2/3)) = 1.

Thus A is an ordinary integer symmetric matrix.
MS12 supplies M=1 or M>=lambda_0, where lambda_0 is Lehmer's number.
If instead M>=sqrt(3/2), the same lower bound already holds because lambda_0<sqrt(3/2).
Hence every such conditioned model satisfies

    h_alg([[A,-I],[I,0]])=0 or >=log(lambda_0).           (3)

The exact entropy identity is the characteristic-polynomial calculation in L G0021.
There is no rank normalization.
Equation (3) is not an unconditional gap for G-self-adjoint integer matrices: L G0022 gave no upper bound on kappa in an integral basis.

## A quantitative obstruction for the existing excluded example

For the P,Q of [L G0021](Yin_L_G0021_v1.md#no-neutral-symmetric-completion), consider any integral model A with chi_A=Q*r and neutral r, and any positive metric G making A self-adjoint.
If kappa<=4/3, then M(R_A)=M(P)<13/10 and

    2 epsilon sqrt(kappa) rho
       < (2/7)*(2/sqrt(3))*(13/10+10/13)
       = 538/(455*sqrt(3)) < 1.

It would follow that A is symmetric, contradicting L G0021.
Thus every such neutral integral model, in every integral basis, has kappa(G)>4/3 for every self-adjointness metric.
This uses only the accepted exact upper bound M(P)<1.3, not rounded table entries.
It gives a real obstruction to attempting to improve the L G0022 metric arbitrarily close to Euclidean; it does not show that condition numbers must diverge along a hypothetical vanishing-entropy family.

## Search and review boundary

Local reuse inspected L G0021--22 and MS12's accepted gap.
Bounded web searches on 2026-10-06 for symmetrizable integer matrix gaps and almost-symmetric integral self-adjoint matrices returned the known matrix literature, but no exact version of (2) was adopted.
This is not an absence or novelty claim.
Positive diagonal symmetrization is more restrictive than a general positive metric and was not silently substituted for it.

The original2026-10-06 formal author check is retained at [its exact finding](../audits/reviews/Yin_R_G0512_v1.md#original-metric-estimate-check).
The next question is whether a useful low-entropy subclass admits a uniform integral-basis metric bound or a different lattice invariant with a proven gap implication.
No such existence theorem is claimed, and the full nonreal-trace core remains outside this symmetric model.
