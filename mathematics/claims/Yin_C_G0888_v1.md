---
author: Yin
---

# Complete Mahler growth for fixed periodic matrix symbols

<a id="statement"></a>
## Precise statement

For a monic complex polynomial \(F(z)=\prod_{j=1}^d(z-\alpha_j)\), use the total logarithmic Mahler measure
\[
m(F)=\sum_{j=1}^d\log\max\{1,|\alpha_j|\}.
\]
Every root is included with its algebraic multiplicity, including zero roots with contribution zero.

Fix an integer \(\ell\ge1\) and one matrix Laurent polynomial
\[
B(x)=\sum_{k=a}^{b}B_kx^k\in M_\ell(\mathbb Z[x,x^{-1}]),
\qquad a,b\in\mathbb Z,\quad a\le b.
\]
The matrix size, coefficient matrices and exponents are independent of \(q\).
For each integer \(q\ge1\), let \(T_qe_j=e_{j+1}\) on coordinates indexed by \(\mathbb Z/q\mathbb Z\), and set
\[
A_q=\sum_{k=a}^{b}T_q^k\otimes B_k,
\qquad P_q(z)=\det(zI_{q\ell}-A_q).
\tag{1}
\]
The matrix \(A_q\) is integral and \(P_q\) is monic of degree \(q\ell\).
No invertibility, reciprocity, diagonalizability or bound on the number of exterior roots is assumed.
Then the exact full-polynomial factorization is
\[
P_q(z)=\prod_{\zeta^q=1}\det(zI_\ell-B(\zeta)).
\tag{2}
\]
Define
\[
\nu_B(\theta)=m_z\bigl(\det(zI_\ell-B(e^{i\theta}))\bigr),
\qquad
c_B=\frac1{2\pi}\int_0^{2\pi}\nu_B(\theta)\,d\theta.
\tag{3}
\]
The function \(\nu_B\) is continuous, nonnegative and \(2\pi\)-periodic.
Exactly one of the following alternatives holds:

- \(c_B=0\), in which case \(\nu_B\) is identically zero and \(m(P_q)=0\) for every \(q\ge1\).
- \(c_B>0\), in which case
  \[
  m(P_q)=q c_B+o(q)\qquad(q\longrightarrow\infty).
  \tag{4}
  \]
  In particular \(m(P_q)\ge q c_B/2\) for every sufficiently large \(q\).

Consequently, for each fixed \(B\) there is an \(\eta_B>0\) such that \(m(P_q)=0\) or \(m(P_q)\ge\eta_B\) for every \(q\ge1\).
No constant uniform over \(B\) is asserted.

There is also the following explicit instance of the [rotating symplectic construction](../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law).
Let \(g\ge6\) be even, index the standard basis by \(i\in\mathbb Z/g\mathbb Z\), put \(S e_i=e_{i+1}\), and use every site with \(\epsilon_i=\eta_i=(-1)^i\).
Set
\[
\begin{aligned}
D&=\sum_{i=0}^{g-1}(-1)^i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},\\
E&=\sum_{i=0}^{g-1}(-1)^i(e_i+e_{i+1})(e_i+e_{i+1})^{\mathsf T},\\
R&=\operatorname{diag}(S,S),\qquad
A_g=R\begin{pmatrix}I&D\\0&I\end{pmatrix}
       \begin{pmatrix}I&0\\E&I\end{pmatrix},\\
P_g^{\rm alt}(z)&=\det(zI_{2g}-A_g).
\end{aligned}
\tag{5}
\]
Then \(A_g\) is integral symplectic and \(P_g^{\rm alt}\) is monic integral reciprocal of degree \(2g\), with constant coefficient one.
Its complete measure is
\[
m(P_g^{\rm alt})
=\frac12\sum_{j=0}^{g-1}
\operatorname{arcosh}\left(1+8\sin^4\frac{2\pi j}{g}\right),
\tag{6}
\]
where \(\operatorname{arcosh}u=\log(u+\sqrt{u^2-1})\) for \(u\ge1\).
It has exactly \(g-2\) exterior roots and \(g-2\) interior roots, counting algebraic multiplicities.
The remaining four roots are \(1\) and \(-1\), each with multiplicity two.
Along even \(g\to\infty\),
\[
\frac{m(P_g^{\rm alt})}{g}\longrightarrow
c_{\rm alt}:=\frac1{4\pi}\int_0^{2\pi}
\operatorname{arcosh}(1+8\sin^4\theta)\,d\theta
\ge\frac14\operatorname{arcosh}3>0.
\tag{7}
\]
Thus this exact balanced, growing-site instance has a growing number of exterior roots and linearly growing complete logarithmic cost.

<a id="reuse-and-proof-scope"></a>
## Reuse, attribution and proof scope

This project deduction is adopted at the [selected decision](#decision-fixed-periodic-symbol-growth) after a [complete independent review](../audits/reviews/Yin_R_G1107_v38.md#periodic-symbol-and-alternating-review).
The argument below belongs to proof development; the separate finding owns the independent inspection and its exact limits.
The actual shear model and its integer probability-law interpretation are retained in [L462 v5](../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law), which is not changed by this Claim.
Its [separable control](../ledger/Yin_L_G0462_v5.md#separable-control) is a comparison, not a premise of the present proof.
The present instance has \(I\) equal to all sites and \(k=g\); it does not establish a conclusion for the proposed dilute regime \(k=o(g)\) or every sign assignment in that law.

The cyclic Fourier decomposition is the standard finite diagonalization of a permutation shift, and its complete argument is included below.
Continuity of monic polynomial measure is proved below by root compactness, without invoking a specialized Mahler-measure convergence theorem.
The remaining tools are elementary finite-dimensional linear algebra and Riemann integration.
No external arithmetic gap theorem, external source-proof adoption, numerical root calculation, sampling result or newly acquired source is a dependency.
This self-contained use of elementary facts is not a claim that Fourier diagonalization or root continuity is new.

<a id="argument"></a>
## Complete argument

The proof first establishes the general periodic-closure assertion, and then computes the full spectrum of (5).

<a id="finite-fourier-factorization"></a>
## Finite Fourier factorization with all multiplicities

For each \(q\)-th root of unity \(\zeta\), define the vector
\[
f_\zeta=\sum_{j=0}^{q-1}\zeta^{-j}e_j.
\]
A direct index shift gives \(T_qf_\zeta=\zeta f_\zeta\).
The geometric-sum identity gives orthogonality of these \(q\) vectors for distinct \(\zeta\), and each has squared norm \(q\).
They therefore form a basis of \(\mathbb C^q\), including the case \(q=1\).
The invariant subspace \(\mathbb C f_\zeta\otimes\mathbb C^\ell\) for (1) carries precisely the matrix \(B(\zeta)\), because the same eigenvalue relation holds for every negative as well as positive power of \(T_q\).
Thus \(A_q\) is similar over \(\mathbb C\) to the direct sum of the \(q\) matrices \(B(\zeta)\).
Their coefficient matrices need not commute, and the individual fiber matrices need not be diagonalizable.
Taking the characteristic polynomial of this actual direct sum proves (2), with every algebraic multiplicity.

Each factor in (2) is monic of degree \(\ell\).
The roots of a product are the union of the roots of its factors, with multiplicities added.
It follows directly from the definition of total logarithmic measure that
\[
m(P_q)=\sum_{\zeta^q=1}m_z(\det(zI_\ell-B(\zeta)))
=\sum_{j=0}^{q-1}\nu_B(2\pi j/q).
\tag{8}
\]
This is a sum of full fiber costs, not an average or a choice of one expanding eigenvalue.
The matrices \(T_q^k\) are integral permutation matrices for all integers \(k\), which also proves the integrality asserted after (1).

<a id="monic-measure-continuity"></a>
## Continuity at repeated roots and nonnegative fiber cost

Consider a convergent sequence of coefficient vectors of monic degree-\(\ell\) complex polynomials, with monic limit \(F\) of the same degree.
Their coefficients have a common absolute bound \(K\), and every root has modulus at most \(1+K\).
Indeed, for \(|z|>1+K\), the leading term \(z^\ell\) has modulus larger than the sum of the moduli of all remaining terms, by the finite geometric-sum bound.
Choose any ordering of each polynomial's roots, with multiplicity.
Every subsequence of these ordered root tuples has a convergent further subsequence by compactness of the closed disk in each coordinate.
The coefficients of the product of the limiting linear factors are the limits of the coefficients of the original products.
Hence the limiting tuple is exactly the root multiset of \(F\), with its algebraic multiplicities, in some order.

The function \(\sum_j\log\max\{1,|\alpha_j|\}\) is continuous and symmetric in the root tuple.
Consequently its limit on every convergent further subsequence is the same number \(m(F)\).
If the original measure sequence did not converge to \(m(F)\), a subsequence bounded away from that number would contradict this conclusion.
This proves continuity of measure on the space of monic polynomials of a fixed degree, including multiple roots, zero roots and roots crossing the unit circle.

The coefficients of \(\det(zI_\ell-B(e^{i\theta}))\) are continuous periodic functions of \(\theta\), and the polynomial remains monic of degree \(\ell\) at every phase.
The preceding argument proves the asserted continuity and periodicity of \(\nu_B\).
Every term in its root definition is nonnegative, so \(\nu_B\ge0\) without any arithmetic assumption on the individual fiber coefficients.
In particular no positive fiber contribution can cancel a negative fiber contribution in (8).

<a id="periodic-dichotomy"></a>
## The zero or linear-total-cost dichotomy

Uniform continuity of \(\nu_B\) on a period gives a modulus of continuity \(\omega_B(\delta)\) tending to zero as \(\delta\downarrow0\).
Compare its value at \(2\pi j/q\) with the values throughout the interval from \(2\pi j/q\) to \(2\pi(j+1)/q\).
After summing the integrals on those intervals, (8) gives
\[
\left|\frac{m(P_q)}q-c_B\right|
\le\omega_B(2\pi/q)\longrightarrow0.
\tag{9}
\]
If \(c_B=0\), a positive value of the nonnegative continuous function \(\nu_B\) would give a positive integral on a neighborhood.
Thus \(\nu_B\) is identically zero, and (8) gives \(m(P_q)=0\) for every \(q\).
If \(c_B>0\), (9) proves (4) and its stated eventual lower bound.

In the positive case choose \(q_0\) so that \(m(P_q)\ge q c_B/2\) for \(q\ge q_0\).
Take \(\eta_B\) to be the minimum of \(c_B/2\) and the positive members of the finite set \(\{m(P_q):1\le q<q_0\}\), omitting zero members.
If that finite positive subset is empty, use \(\eta_B=c_B/2\).
This is strictly positive and proves the fixed-symbol gap.
In the all-zero case any positive \(\eta_B\) satisfies the same vacuous positive-measure conclusion.
No effective modulus of continuity or uniformity over different symbols is needed or asserted.

<a id="alternating-identities"></a>
## Exact identities for the alternating rotating shears

Use the matrices in (5), and let \(\Delta=\operatorname{diag}((-1)^i)_{i=0}^{g-1}\).
Evenness of \(g\) makes these signs consistent around the cycle and gives \(S\Delta S^{-1}=-\Delta\).
At each vertex, the diagonal contributions to both \(D\) and \(E\) are \((-1)^i+(-1)^{i-1}=0\).
The off-diagonal entries along every edge have opposite signs in the two matrices.
For the stated \(g\ge6\) the edges and neighboring vertices are distinct, so their defining sums give
\[
E=-D,\qquad
D=\Delta(S-S^{-1}),\qquad
SDS^{-1}=-D.
\tag{10}
\]
The formulas are derived on the actual integral lattice, without a limiting or approximate sign pattern.
They imply
\[
D^2=-(S-S^{-1})^2=2I-S^2-S^{-2},
\qquad S^2D=DS^2.
\tag{11}
\]
The matrices \(D\) and \(E\) are real symmetric from their defining sums.
For the standard skew form \(\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\), direct block multiplication gives
\[
U(D)^{\mathsf T}\Omega U(D)=\Omega,
\qquad L(E)^{\mathsf T}\Omega L(E)=\Omega,
\qquad R^{\mathsf T}\Omega R=\Omega.
\]
Here the last equality uses \(S^{\mathsf T}S=I\).
All three matrices are integral and have determinant one, so the same is true of \(A_g\).
The relation \(A_g^{-1}=\Omega^{-1}A_g^{\mathsf T}\Omega\) pairs its eigenvalues reciprocally, with their multiplicities.
Together with its even degree and determinant one, this proves the stated reciprocal characteristic-polynomial normalization.

Put
\[
B_D=U(D)L(-D)=
\begin{pmatrix}I-D^2&D\\-D&I\end{pmatrix}.
\]
Symmetry of \(D\) gives \(B_{-D}=B_D^{\mathsf T}\), and (10) gives \(R^{-1}B_DR=B_{-D}\).
Therefore
\[
A_g^2=R B_D R B_D
=R^2B_D^{\mathsf T}B_D=R^2C_D,
\tag{12}
\]
where
\[
C_D=\begin{pmatrix}
I-D^2+D^4&-D^3\\-D^3&I+D^2
\end{pmatrix}.
\tag{13}
\]
The matrix \(C_D=B_D^{\mathsf T}B_D\) is real symmetric positive definite because \(B_D\) is invertible.
Equation (11) also gives \(R^2C_D=C_DR^2\).
These are exact identities; no spectral-radius estimate has replaced the full matrix.

<a id="alternating-complete-spectrum"></a>
## Complete root moduli and exterior multiplicity

The matrix \(R^2\) is orthogonal, hence unitary on the complexification.
Since it commutes with \(C_D\), it preserves each positive-eigenvalue eigenspace of \(C_D\).
Diagonalizing its unitary restriction on each such eigenspace shows that the eigenvalues of \(R^2C_D\) have moduli precisely the eigenvalues of \(C_D\), including multiplicities.
Thus (12) determines all root moduli of \(A_g^2\), not only its largest modulus.

Diagonalize the real symmetric matrix \(D\) orthogonally, with eigenvalues \(d_1,\ldots,d_g\).
Under the corresponding change of basis in both coordinate blocks, (13) is a direct sum of the matrices
\[
K(d)=\begin{pmatrix}
1-d^2+d^4&-d^3\\-d^3&1+d^2
\end{pmatrix}.
\tag{14}
\]
Their determinants are one and their traces are \(2+d^4\).
Their positive eigenvalues \(\mu_+(d)\ge\mu_-(d)>0\) satisfy
\[
\mu_+(d)\mu_-(d)=1,\qquad
\log\mu_+(d)=\operatorname{arcosh}(1+d^4/2).
\tag{15}
\]
For \(d=0\), both eigenvalues are one; for \(d\ne0\), exactly one is greater than one and the other is less than one.

The finite Fourier basis for \(S\), already established above, turns (11) into the multiset identity
\[
\{d_j^2:1\le j\le g\}
=\left\{4\sin^2\frac{2\pi j}{g}:0\le j<g\right\}.
\tag{16}
\]
Every eigenvalue is counted with its multiplicity, and the expression in (15) depends only on \(d^2\).
The eigenvalues of a matrix square are the squares of its eigenvalues with their algebraic multiplicities, as follows for example from an upper triangular form over \(\mathbb C\).
Consequently squaring doubles total logarithmic measure and leaves exterior and interior root counts unchanged.
Combining (12)--(16) gives
\[
2m(P_g^{\rm alt})
=m(\det(zI-A_g^2))
=\sum_{j=0}^{g-1}\operatorname{arcosh}
\left(1+8\sin^4\frac{2\pi j}{g}\right),
\]
which proves (6).

Because \(g\) is even, exactly the two indices \(j=0\) and \(j=g/2\) in (16) give zero.
Thus exactly \(g-2\) blocks (14) contribute one exterior and one interior eigenvalue each to \(A_g^2\), with the remaining four eigenvalues on the unit circle.
This proves the same exterior and interior counts for \(A_g\).
More precisely, (10) gives \(\ker D=\ker(S-S^{-1})\), the span of the constant and alternating coordinate vectors.
The shift \(S\) acts on these two vectors by \(1\) and \(-1\), respectively.
On \(\ker D\oplus\ker D\), the matrix \(B_D\) is the identity and \(A_g=R\).
This invariant four-dimensional subspace supplies \(1\) and \(-1\), each twice, and the preceding complete count leaves no other unit-circle eigenvalues or extra multiplicities at those two roots.

The function \(\operatorname{arcosh}(1+8\sin^4\theta)\) is continuous.
Applying the elementary Riemann-sum argument to (6) proves the limit in (7).
On the set \(\{\theta\in[0,2\pi]:|\sin\theta|\ge1/\sqrt2\}\), which has length \(\pi\), its value is at least \(\operatorname{arcosh}3\).
This proves the stated strictly positive lower bound for \(c_{\rm alt}\).

<a id="alternating-fixed-symbol"></a>
## The explicit two-site spatial symbol

For clarity, the alternating instance is also an actual instance of (1), with fixed matrix size four.
Write \(g=2q\) and group sites \(2r,2r+1\) into a cell indexed by \(r\in\mathbb Z/q\mathbb Z\).
In the two-component cell coordinates the shift and signed difference have symbols
\[
S_2(x)=\begin{pmatrix}0&x\\1&0\end{pmatrix},
\qquad
D_2(x)=\begin{pmatrix}0&x-1\\x^{-1}-1&0\end{pmatrix}.
\tag{17}
\]
Indeed the shift sends an even site to the odd site in the same cell and an odd site to the even site in the next cell.
The formula for \(D_2\) is \(\operatorname{diag}(1,-1)(S_2-S_2^{-1})\), matching (10).
The fixed Laurent symbol for the full four-component cell is
\[
\mathcal A(x)=
\begin{pmatrix}S_2(x)&0\\0&S_2(x)\end{pmatrix}
\begin{pmatrix}
I_2-D_2(x)^2&D_2(x)\\-D_2(x)&I_2
\end{pmatrix}
\in M_4(\mathbb Z[x,x^{-1}]).
\tag{18}
\]
After permuting the original basis into these cell coordinates, \(A_g\) is exactly (1) for \(B=\mathcal A\) and \(q=g/2\).
Therefore
\[
P_g^{\rm alt}(z)=\prod_{\zeta^q=1}\det(zI_4-\mathcal A(\zeta)).
\tag{19}
\]
The explicit root-modulus proof above identifies this symbol's positive-cost alternative and gives the stronger formula (6).
No omitted boundary term or exceptional selected phase is needed to identify the periodic closure.

<a id="research-scope"></a>
## Consequences and limits for the unrestricted objective

The general theorem concerns the actual whole characteristic polynomial for one fixed spatial symbol, not an individual factor extracted from that polynomial.
It proves that repeating this fixed periodic rule gives either measure one at every period or positive total logarithmic measure tending to infinity linearly.
It permits neutral exceptions and finite positive small values at short periods in the positive-cost case.
Its fixed-symbol positive gap depends on the symbol and supplies no uniform bound over all integer Laurent matrix symbols.
In particular, it does not settle the unrestricted [G0001 positive-gap question](../tasks/Yin_T_G0001_v1.md#contract).

The matrix size, Laurent exponents and coefficients must remain fixed in (1).
A symbol depending on \(q\), a growing primitive spatial period, a sparse nonperiodic defect, a changed boundary condition or an aperiodic gluing need not satisfy the same factorization with one fixed \(B\).
No conclusion for those classes follows merely by applying (9) separately at each varying symbol; both the limiting coefficient and the continuity error would then vary.
The [separable cyclic control](../ledger/Yin_L_G0462_v5.md#separable-control) has a single distinguished nonidentity weight and a constant positive whole measure in its hyperbolic branch, illustrating why the pure periodic-closure hypothesis cannot be dropped.

For the particular alternating sign assignment, (6) and the count \(g-2\) expose the complete exterior cost directly.
This rejects that fixed balanced pattern as a positive-to-one mechanism while leaving other sign patterns and the full growing symplectic ensemble unresolved.
An uncovered candidate still needs an actual integer input and a mechanism making the sum of all positive radial logarithms small.
A smaller largest radius, a small measure per site, or growth of displayed word length alone does not supply that conclusion.
No numerical experiment or new sampling campaign is part of this argument.

## Assessment history

### Decision fixed-periodic-symbol-growth

| Field | Value |
| --- | --- |
| date | 2026-11-10T09:18 |
| status | proved |
| reason | Complete independent inspection verifies the exact periodic factorization, all-zero or linear total logarithmic growth, the fixed-symbol gap, and the full spectrum and actual spatial symbol of the alternating rotating-shear instance. No uniform gap over varying symbols is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statements](#statement) | Every fixed integral Laurent matrix symbol, all positive periods, complete root multiplicities, fixed-symbol gap and the stated alternating family. |
| argument | [Complete proof](#argument) | Entire elementary argument and the exact link between the general periodic closure and the alternating instance. |
| argument | [Finite Fourier factorization](#finite-fourier-factorization) | Negative powers, period one, direct sums and every characteristic factor and multiplicity. |
| argument | [Continuity](#monic-measure-continuity) | All monic coefficient limits, repeated and zero roots, and roots crossing the unit circle. |
| argument | [Total-cost dichotomy](#periodic-dichotomy) | Nonnegative continuous fiber costs, Riemann sums, finite short-period exceptions and the symbol-dependent positive gap. |
| argument | [Alternating identities](#alternating-identities) | Integral symplectic normalization, signs and exact commuting squared-product identity. |
| argument | [Complete alternating spectrum](#alternating-complete-spectrum) | Every root modulus, exterior and interior counts, four unit roots and the positive limiting cost. |
| argument | [Actual fixed symbol](#alternating-fixed-symbol) | Exact two-site cell representation and its complete characteristic factorization. |
| argument | [Consequences and limits](#research-scope) | Whole-polynomial scope, dependence on the fixed symbol and the unresolved varying-pattern and unrestricted problem. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v38.md#periodic-symbol-and-alternating-review) | Entire fixed statement, proof, actual model interfaces, spatial symbol and research limits. |

## Current assessment

[Selected decision](#decision-fixed-periodic-symbol-growth)

