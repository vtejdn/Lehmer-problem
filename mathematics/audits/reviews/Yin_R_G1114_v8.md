---
author: Yin
---

# Independent review of the growing-cycle four-transvection commutator obstruction

## Review arrangement and fixed inputs

The review act is dated 2026-11-10T03:19, with Yin as the human record author.
A separately organized reviewer read the complete fixed L462 v15 argument and its necessary mathematical inputs without participating in development or receiving the main thread's derivation dialogue.
No substantive repair or extension was supplied.
The review covers the exact original-dimensional family, every characteristic-determinant reduction, every parameter case and the complete-measure conclusion.

Verification used ordinary exact hand algebra.
No numerical search, root calculation, sampling law, symbolic-algebra program or new computation program was run.
The earlier integral transvection and negative-index arguments were read at their actual invoked scopes.
C885 v2 and the short-word result are motivational context; C886 supplies the stated permutation-order interpretation, not the determinant obstruction proved here.
No original-source PDF or foundational source proof was newly inspected.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete commutator finding](#growing-cycle-commutator-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete commutator finding](#growing-cycle-commutator-review) | [L462 v15 question and scope](../../ledger/Yin_L_G0462_v15.md#question-and-current-scope) | Exact family and obstruction, author-checked input and absence of a numerical experiment or unrestricted conclusion. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Exact family](../../ledger/Yin_L_G0462_v15.md#candidate) | Every n at least one, N and g, binary coefficients, lattice norms and parity, fixed rightmost-first word and its specified block permutation. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Entire active polynomial](../../ledger/Yin_L_G0462_v15.md#active-polynomial) | Invariant rational decomposition, all seven complementary cyclic copies, integral active restriction, complete characteristic factorization and measure equality. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Four-dimensional word](../../ledger/Yin_L_G0462_v15.md#four-dimensional-word) | Projection and complementary kernel, both signed transvection matrices and all entries of their ordered product. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Complete determinant](../../ledger/Yin_L_G0462_v15.md#complete-determinant) | The full determinant lemma, every prefactor, normalized resolvent and finite cyclic correlation formulas, including both shift signs. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Two-dimensional test](../../ledger/Yin_L_G0462_v15.md#two-dimensional-exterior-test) | Exact rank-two factorization, all reduced matrix entries, complete determinant expansion, operator-norm estimates and every N at least eight. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Two small parameters](../../ledger/Yin_L_G0462_v15.md#two-small-parameters) | Exact N=2 cyclic correlations and rational values, N=4 weighted correlation product and positive shift ratio, and strict negativity in both cases. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Complete obstruction and limits](../../ledger/Yin_L_G0462_v15.md#complete-commutator-obstruction) | Positivity of all prefactors at two, an actual real root above two, complete Mahler measure above two for every n, and the exact nonconclusions. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Integral generator input](../../ledger/Yin_L_G0462_v13.md#integer-generators) | Formula, even-norm integrality, inverse and pairing preservation for the actual E8-block family and its active lattice. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Negative-index input](../../ledger/Yin_L_G0462_v13.md#negative-index-bound) | All generalized expanding multiplicities and reciprocal spectrum at negative index one, giving the complete-measure equality. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [C886 word-dependent bound](../../claims/Yin_C_G0886_v1.md#statement) | The specified presentation has a g-cycle and d=g; this supplies only that presentation's order-dependent gap and excludes no stronger alternative presentation. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Two-transvection context](../../claims/Yin_C_G0885_v2.md#statement) | Its stated family does not directly cover the new four-factor word; its gap is not a premise of the new sign calculation. |
| [Complete commutator finding](#growing-cycle-commutator-review) | [Short-word context](../../ledger/Yin_L_G0462_v14.md#short-word-reduction) | The earlier reduction covers at most three factors at the two cusps; no general four-factor obstruction is imported from it. |

<a id="growing-cycle-commutator-review"></a>
## Finding

No mathematical defect was found in the complete inspected L462 v15 argument.
For every \(n\ge1\), its exact original-dimensional matrix has a real eigenvalue strictly greater than two and satisfies
\[
M(P_A)=M(P_{\mathrm{act}})=\rho(A)>2.
\]
This rules out both shrinking positive measure and the finite \(6/5\) target for this specific commutator family.
The following checks preserve the distinction between its whole characteristic polynomial and the smaller determinants used to evaluate it.

### Admissibility and every neutral complementary factor

The binary subset sums in the coefficient product are unique, producing exactly \(N=2^n\) coefficients of magnitude one.
For \(N\ge2\), \(g=N^3+1>2N\); the two supports are therefore disjoint and have squared norms \(2N\), with zero mutual pairing.
Both signs of each vector satisfy the even-norm integral transvection hypotheses.
The common-basis cyclic identification is an integral positive isometry, and its block permutation is a genuine g-cycle.
Only this specified presentation is assigned that permutation order.

The positive root span has Gram \(2I_g\), and the stated basis together with \(e,f\) is preserved integrally by \(R\) and all four transvections.
Their restrictions and their negative-vector inverses are integral.
The rational orthogonal complement has dimension \(7g\), is fixed pointwise by every transvection and is cyclically permuted in seven identical copies by \(R\).
Its complete characteristic polynomial is \((z^g-1)^7\).
This proves equation (1) with degrees \(8g+2=7g+(g+2)\), without asserting an integral E8 root/complement splitting.

All these complementary factors have measure one.
The original and active forms both have negative index one, so the invoked generalized-eigenspace argument gives the complete-measure equality with spectral radius, including neutral possibilities before the later sign calculation.
No unexamined complementary eigenvalues are removed.

### Whole commutator and the original-dimensional determinant

The two positive vectors are nonzero and orthogonal, so \(\Pi S=I_4\).
The kernel of \(\Pi\) consists of positive vectors orthogonal to both and is fixed pointwise by the four transvections.
Their product preserves the span of \(v,w,e,f\), proving \(C|_W=I+S(C_N-I)\Pi\).
This statement is about \(C\); it does not incorrectly assume that \(R\) or \(A\) preserves that four-dimensional span.

Both signed matrices follow from the pairing formula, with half-norm \(N\) unaffected by the sign.
Multiplication was checked by applying the rightmost factors successively.
After \(F_+E_-F_-\), the four coordinates are
\[
\begin{aligned}
u'&=u-\beta-2Nt+N\alpha,\\
t'&=2Nu+(1-2N^2)t+N^2\alpha-N\beta,\\
\alpha'&=2Nu-2N^2t+(1+N^2)\alpha-N\beta,\\
\beta'&=-2N^2u+2N^3t-N^3\alpha+(1+N^2)\beta.
\end{aligned}
\]
Applying \(E_+\) gives all sixteen entries of the displayed \(C_N\), including both unchanged second and fourth rows.

Factoring \(zI-R|_W\) from the full matrix and using \(\det(I-XY)=\det(I-YX)\) gives precisely equation (3).
The prefactor is \((z^g-1)(z-1)^2\), since \(R\) cycles the \(g\) root coordinates and fixes both hyperbolic coordinates.
The resulting matrix is \(Q=\Pi(zI-R)^{-1}RS\), with the stated two correlation rows and the block \(kI_2\).
Commutation of \(K\) with \(R\), together with orthogonality of \(R\), makes its two diagonal correlation entries equal.
The identity is valid over the rational-function field and extends to the complete polynomial by equality with the original determinant.
Values at singular resolvent parameters are consequently understood by that polynomial identity, not by deleting possible factors.

In the coefficient basis the pairing contributes a factor two and the projection divides by \(2N\), leaving the denominator \(N(z^g-1)\) in every correlation formula.
The finite resolvent sum includes \(\ell=g\).
For \(x\) the exponent is \(\ell+N\), while for \(y\) it is \(\ell-N\), because the latter first moves \(R^N\) from the left vector by orthogonality.
Thus all cyclic signs, normalizations and endpoint terms in equation (4) agree with the actual original-dimensional action.

### Exact rank-two reduction and its complete expansion

Subtracting the identity from \(C_N\) makes rows three and four exactly minus \(N\) times rows one and two.
This verifies the complete \(BD\) factorization, including its third and fourth columns.
The second determinant lemma therefore gives \(\det(I_4-QBD)=\det(I_2-DQB)\) without additional factors.

At two, \(QB\) has top block \(\left(\begin{smallmatrix}s&x\\y&s\end{smallmatrix}\right)\) and bottom block \(-NI_2\).
Multiplying by \(D\) and subtracting from the identity gives all four entries of the displayed two-by-two matrix.
In its determinant, the coefficients of \(x,y,xy\) are respectively
\[
-2N(N^2+1),\qquad -2N(2N^2-1),\qquad -4N^2.
\]
The remaining coefficient is \(1+N^2(h^2-1)-2N^4\).
These checks verify the entire equation (5), including cancellation of the apparent sixth-degree terms, rather than only its leading sign.

The orthogonal Neumann series has norm at most \(\sum_{\ell\ge1}2^{-\ell}=1\).
Both input norms are \(\sqrt{2N}\), so normalization by \(2N\) gives \(|s|,|x|,|y|\le1\) and \(|h|\le3\).
The two linear error bounds sum exactly to \(6N^3\); the \(h\) term contributes at most \(8N^2\), and the mixed term at most \(4N^2\).
Hence
\[
F_N\le1-2N^4+6N^3+12N^2.
\]
For \(N\ge8\), \(N^2-6N-12\ge4\), making this at most \(1-N^4<0\).
No special sign or fine cancellation of the large-parameter correlations is used in that bound.

### Both small parameters and complete conclusion

For \(N=2,g=9\), the cyclic correlation support is exactly \(0,1,8\), with values \(2,-1,-1\).
The unnormalized numerators for \(s,x,y\) at two are respectively \(-256,-2,-64\); dividing by \(2(2^9-1)\) gives the three stated fractions.
It follows that \(h=255/511\), the \(h^2-1\) term and mixed term are strictly negative, and the two linear terms sum to \(916/511<2\).
Thus \(F_2<-29\), with the cyclic wrap included.

For \(N=4,g=65\), the nonzero unwrapped correlation lags lie in \([-3,3]\).
Their weighted sum is exactly
\[
\sum_j2^{-j}c_j=a(2)a(1/2)=9/8.
\]
The y-numerator is centered at \(\ell=N\), while the x-numerator is centered at \(\ell=g-N\); both ranges lie inside the finite resolvent sum.
This proves the two displayed formulas and the positive ratio \(x/y=2^{2N-g}\).
Consequently \(x,y>0\), all three remaining correlation terms in equation (5) are negative, and \(|h|\le3\) gives \(F_4\le-383<0\).
Together with the tail, these cases exhaust every \(N=2^n\) in the family.

At \(z=2\), the combined prefactor from the original and active polynomial identities is \((2^g-1)^8(2-1)^2>0\).
Therefore \(P_A(2)<0\).
The original characteristic polynomial is real and monic, so the intermediate value theorem gives an actual root greater than two.
Its factor in the complete monic Mahler measure already exceeds two; all other factors are at least one.
This proves the claimed obstruction directly, while the earlier negative-index equality additionally identifies the whole measure with the radius.

The conclusion concerns this exact family for every stated parameter.
It neither proves a general four-transvection gap nor excludes arbitrary parameter pairs or positive lattices.
Meeting C886's necessary growing-order condition supplies no small-radius guarantee, and a different word presentation is not ruled out.
The existing source and theorem inputs retain their previous inspection scopes; no new source claim or experiment is inferred from this hand verification.
The unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.
