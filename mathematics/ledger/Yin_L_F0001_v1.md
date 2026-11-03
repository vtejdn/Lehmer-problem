---
author: Yin
---

# Affine Variational Formulas: Independent General Formula and Spectrum

Updated: 2026-09-13.
Author: root.

## Historical Frontier, 2026-09-12

The following sections describe the initial offline checkpoint before Yin_C_F0082.
Their open-problem descriptions and route priorities are historical; current dispositions belong to the strategy index.

<a id="signed-schur-linearization"></a>
## A Signed Schur Linearization of Every Regularized Determinant

There is a direct algebraic reduction that motivates a further route.
For any bounded S in M_m(M) and epsilon>0, set
\[
 L_\varepsilon=
 \begin{pmatrix}\varepsilon^2I_m&S\\S^*&-I_m\end{pmatrix},
 \qquad Q_\varepsilon=SS^*+\varepsilon^2I_m>0.
\]
The Schur factorization is
\[
 L_\varepsilon=
 \begin{pmatrix}I_m&-S\\0&I_m\end{pmatrix}
 \begin{pmatrix}Q_\varepsilon&0\\0&-I_m\end{pmatrix}
 \begin{pmatrix}I_m&0\\-S^*&I_m\end{pmatrix}.
                                                               \tag{1}
\]
The triangular outer factors have Fuglede-Kadison determinant one: along their affine paths from the identity, the logarithmic derivative is the trace of an off-diagonal square-zero matrix and vanishes.
Applying the same bounded invertible determinant multiplicativity as in the [local foundations](Yin_L_F0002_v1.md), and keeping the trace normalized on size 2m, gives
\[
 \Delta_{\operatorname{tr}_{2m}\otimes\tau}(L_\varepsilon)
 =\exp\!\left(\frac12\varphi_m\log Q_\varepsilon\right)
 =\Delta_\varepsilon(S).
                                                               \tag{2}
\]
All factors are invertible at positive epsilon.
Equality of the singular-value distributions of SS* and S*S identifies the last expression with Yin_C_F0002's regularization convention.

If S=a_0+sum a_j s_j, then L_epsilon is itself a selfadjoint affine semicircular pencil, with constant block matrix [[epsilon squared I,a_0],[a_0*,-I]] and noise blocks [[0,a_j],[a_j*,0]].
Equation (1) presents it with one positive and one negative Schur block.
This is a direct use of the usual Schur-complement factorization, not a newly designated project theorem.

The reduction preserves the unresolved issue: the pencil L_epsilon is indefinite, so the positive-pencil minimum cannot be applied to it.
A valid variational principle for this structured indefinite class would give every positive-epsilon regularized determinant in the general problem; taking epsilon down to zero would then recover the requested determinant.
It remains necessary to prove the appropriate ordered minimum/maximum, feasible domains and physical-branch comparison for that class.

