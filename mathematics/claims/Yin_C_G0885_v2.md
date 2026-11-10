---
author: Yin
---

# A uniform Mahler gap for two transvections over arbitrary positive integral lattices

<a id="statement"></a>
## Statement and scope

Let \(H\) be any positive definite symmetric integral \(g\times g\) matrix, \(g\ge1\), and let
\[
R\in\operatorname{GL}_g(\mathbb Z),\qquad R^{\mathsf T}HR=H.
\]
On \(\Lambda=\mathbb Z^g\oplus U\), use the form \(H\) on the first summand and the hyperbolic basis \(e,f\) with \((e,e)=(f,f)=0\), \((e,f)=1\), the summands being orthogonal.
Extend \(R\) by the identity on \(U\).
For \(v,w\in\mathbb Z^g\) with even \(H\)-squared norms, including zero vectors, put
\[
T_{e,v}(x)=x-(v,x)e+(e,x)v-\tfrac12(v,v)(e,x)e,
\qquad A=R T_{e,v}T_{f,w},
\qquad P_A(z)=\det(zI-A).
\]

There is an absolute constant \(\eta>0\), independent of \(g,H,R,v,w\), such that the complete logarithmic Mahler measure satisfies
\[
                         m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta.       \tag{1}
\]
Moreover, with \(s=\|v\|_H\|w\|_H\),
\[
                 s\ge650\quad\Longrightarrow\quad M(P_A)>2.             \tag{2}
\]
When either vector is zero, \(P_A(z)=\det(zI-R)(z-1)^2\) and \(M(P_A)=1\).

In particular, changing the positive lattice, its determinant, its basis or the finite-order positive isometry does not produce a positive-to-one sequence from this two-transvection construction.
The assertion concerns whole characteristic polynomials, with all roots and multiplicities included.
It does not cover more transvections or general isometries of an indefinite lattice, and gives no effective lower bound at the finite target \(6/5\).
The [earlier cyclic standard-lattice theorem](Yin_C_G0885_v1.md#decision-cyclic-two-transvection-gap) retains its more explicit support count and independent proof review.

<a id="argument"></a>
## Argument and reused inputs

The new issue is that bounded \(H\)-norm need not bound the number of occupied coordinates in an arbitrary integral basis.
The proof replaces the coordinate-support step of [v1](Yin_C_G0885_v1.md#argument) with the bounded Fourier-algebra norm of the four actual cyclic correlation functions.
It uses [Sanders Theorem 1.1](../audits/literature/San20/Yin_U001.md#san20-u001) and the [DS17 univariate fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) at their existing accepted statement and applicability scopes.
The signed-coset clearing mechanism in [C880 v1](Yin_C_G0880_v1.md#sparse-completion) supplies related project provenance; the new correlation inputs and complete determinant identity are checked explicitly below.
No source's original foundational proof is newly audited.

### Finite positive isometry and complete determinant

The group of integral \(H\)-isometries is finite.
Indeed each column \(j\) of such a matrix has \(H\)-squared norm \(H_{jj}\); positive definiteness bounds its Euclidean coordinates, so only finitely many integer columns and hence matrices are possible.
Every power of \(R\) belongs to this finite group, so \(R^N=I\) for some \(N\ge1\).
Thus
\[
\chi_R(z)=\det(zI-R)
\]
is a monic integer polynomial with only roots of unity and \(M(\chi_R)=1\).

The transvection pairing identity in [L462 v13](../ledger/Yin_L_G0462_v13.md#integer-generators) uses only the integral pairing, isotropic vector and even squared norm.
It therefore applies to this \(H\) and makes both transvections integral isometries with their stated negative-vector inverses.
Their standard formula retains the GHS13 attribution recorded there.
In particular \(P_A\) is a nonzero monic integer polynomial.

Write
\[
a=(v,v)/2,\quad b=(w,w)/2,\quad c=(v,w),\qquad
K_R(z)=(zI-R)^{-1}R,
\]
and, with every pairing now taken using \(H\),
\[
V=(v,K_Rv),\quad W=(w,K_Rw),\quad
X=(v,K_Rw),\quad Y=(w,K_Rv).
\]
The determinant-preserving row operations used in v1 give the full block matrix
\[
\begin{pmatrix}
zI-R&-Rw&-zRv\\
v^{\mathsf T}H&z-1+c&az\\
w^{\mathsf T}H&b&z-1
\end{pmatrix}.
\]
Taking its Schur complement for real \(z>1\) proves the rational identity
\[
P_A(z)=\chi_R(z)D(z),\qquad
D(z)=
\det\begin{pmatrix}
z-1+c+X&z(a+V)\\
b+W&z-1+zY
\end{pmatrix}.                                                        \tag{3}
\]
No diagonalization of \(R\) over the integers or assertion about only the exterior factors is used.
If either vector is zero, this gives the claimed neutral polynomial directly.

### Small measure bounds the four correlation norms

Conjugate \(R\) by the real positive square root of \(H\), and replace \(v,w\) by their images under that same square root.
The resulting rotation is Euclidean orthogonal, all pairings in (3) are preserved, and the two-by-two determinant is unchanged.
The [uniform determinant calculation in v1](Yin_C_G0885_v1.md#argument) uses only real orthogonality: it does not use cyclic permutation, integrality or coordinate support.
Applied in these coordinates, it gives
\[
                         D(2)\le1+4s-s^2/162.
\]
For \(s\ge650\) this is at most \(-569/81<0\), while \(D(z)=z^2+O(z)\) as \(z\to+\infty\) for each fixed input.
Since \(\chi_R(z)\ne0\) on \(z>1\), continuity and (3) give a real root of \(P_A\) greater than two.
This proves (2) for every \(H,R\), with complete measure and no restriction on the other roots.

It remains to consider \(1<M(P_A)\le2\).
Neither vector is zero, and (2) gives \(s<650\).
The positive even integral squared norms are each at least two, so
\[
             \|v\|_H^2,\ \|w\|_H^2<211250=:B.                         \tag{4}
\]
For each ordered pair \((r,t)\) from
\[
                         (v,v),\quad(w,w),\quad(v,w),\quad(w,v),
\]
define the integer-valued function
\[
              f_{r,t}(j)=(r,R^jt)\qquad(j\in\mathbb Z/N\mathbb Z).
\]
Its Fourier algebra norm in the [normalized convention](../audits/literature/San20/Yin_U001.md#finite-abelian-fourier-algebra-norm) satisfies
\[
                         \|f_{r,t}\|_A\le\|r\|_H\|t\|_H.                \tag{5}
\]

For completeness, extend the positive inner product to the complex Hermitian space, conjugate-linear in its first entry.
The finite-order unitary operator \(R\) has mutually orthogonal eigenspaces, with orthogonal projections \(\Pi_\lambda\), \(\lambda^N=1\).
Then
\[
f_{r,t}(j)=\sum_{\lambda^N=1}\lambda^j
                   \langle\Pi_\lambda r,\Pi_\lambda t\rangle_H.
\]
Character orthogonality identifies these coefficients with the normalized Fourier coefficients.
Cauchy--Schwarz within each eigenspace and then over the eigenspaces gives
\[
\sum_\lambda|\langle\Pi_\lambda r,\Pi_\lambda t\rangle_H|
 \le\sum_\lambda\|\Pi_\lambda r\|_H\|\Pi_\lambda t\|_H
 \le\|r\|_H\|t\|_H,
\]
proving (5), including multiplicities of the eigenvalues.
Every \(f_{r,t}(j)\) is integral because \(H,R,r,t\) are integral.
Equations (4)--(5) bound all four algebra norms by the same absolute \(B\), regardless of the lattice basis or of \(N\).

### Signed cosets and an integer polynomial with unchanged complete measure

By the accepted Sanders theorem there is an integer \(L=L(B)\ge1\), independent of the cyclic group and input, such that each of the four functions is a signed sum of at most \(L\) subgroup-coset indicators.
Integer coefficients may be split into signed repetitions.
Each coset on \(\mathbb Z/N\mathbb Z\) has the form \(j\equiv u\pmod d\), with \(d\mid N\) and \(0\le u<d\).

For \(|z|>1\), the corresponding correlation resolvent is
\[
(r,K_R(z)t)=\sum_{j\ge1} f_{r,t}(j)z^{-j}.
\]
If \(\nu=u\) for \(u>0\) and \(\nu=d\) for \(u=0\), then
\[
              \sum_{\substack{j\ge1\\j\equiv u\pmod d}}z^{-j}
                      =\frac{z^{d-\nu}}{z^d-1}.                       \tag{6}
\]
The exponent \(d-\nu\) lies between zero and \(d-1\); this includes the zero-residue coset without a missing \(j=0\) correction.
Thus each of \(V,W,X,Y\) is a signed sum of at most \(L\) monomials divided by binomials \(z^d-1\).

Let \(\Delta\) be the product of all those denominator binomials, counting the denominators in all four expressions.
There are \(F\le4L\) factors; an empty product means one.
It is a monic integer polynomial of measure one with at most \(2^F\) terms.
Each of \(\Delta V,\Delta W,\Delta X,\Delta Y\) is an integer polynomial with at most \(L2^F\) terms.
This bound follows by multiplying every numerator monomial by the product of the other denominator factors; repeated denominators or cancellations do not increase the count.

Define the actual integer polynomial
\[
\begin{aligned}
U(z)= {}&
 \bigl((z-1+c)\Delta+\Delta X\bigr)
 \bigl((z-1)\Delta+z\Delta Y\bigr)\\
&-z\bigl(a\Delta+\Delta V\bigr)\bigl(b\Delta+\Delta W\bigr).
\end{aligned}
\]
Equation (3) gives the cross-multiplied polynomial identity
\[
                     \chi_R U=\Delta^2P_A.                           \tag{7}
\]
In particular \(U\ne0\).
The first two factors each have at most \((L+2)2^F\) terms, and the other two at most \((L+1)2^F\).
A uniform bound on the number of nonzero terms of \(U\) is therefore the absolute integer
\[
                         K=2(L+2)^2\,2^{8L}.                          \tag{8}
\]
Every leading coefficient, root and multiplicity is retained by (7).
Since \(M(\chi_R)=M(\Delta)=1\), multiplicativity gives exactly
\[
                              m(U)=m(P_A).
\]
This does not require \(U/P_A\) to be an integer polynomial.

The accepted DS17 theorem applied to the nonzero integer polynomial \(U\) supplies \(\eta_K>0\) whenever \(m(P_A)>0\) in the low-measure branch.
Combining this with \(m(P_A)>\log2\) outside that branch and the settled zero-vector cases proves (1), with
\[
                             \eta=\min(\eta_K,\log2)>0.
\]
All constants are chosen independently of \(H,R,g,v,w\).
Neither accepted theorem is assigned an effective numerical constant here.

<a id="research-scope"></a>
## Effect on the proposed lattice change

The new assertion is stronger than the cyclic standard-coordinate statement of v1: an arbitrary positive integral lattice can have short vectors with many occupied coordinates, so v1's literal sparsity argument cannot be transferred.
The actual substitute is the bounded Fourier algebra norm of integer cyclic correlations, followed by a uniform signed-coset decomposition.
The complete measure identity (7) avoids any unproved divisibility claim about the cleared polynomial.

This rules out a proposed escape through a changing positive lattice while retaining one positive isometry and these two transvections.
It neither represents every integral indefinite isometry in that form nor proves such a representation after stabilization.
No unrestricted [G0001 conclusion](../tasks/Yin_T_G0001_v1.md#contract), effective \(6/5\) exclusion or general bound for a growing product of transvections follows.
The [independent whole-argument finding](../audits/reviews/Yin_R_G1114_v3.md#positive-lattice-two-transvection-gap-review) checks the new lattice and Fourier interfaces, the complete polynomial identity, and the reused real-orthogonal estimate at their actual scopes.

## Assessment history

### Decision positive-lattice-two-transvection-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T01:05 |
| status | proved |
| reason | The complete independent review found no gap in the extension to arbitrary positive integral lattices, the normalized integer correlations, the uniform coset decomposition or the exact complete-measure reduction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact positive-lattice family](#statement) | An absolute positive total-logarithmic gap for all stated positive integral lattices, positive isometries and even-norm vector pairs, including the large-norm implication and neutral zero cases. |
| argument | [Complete argument](#argument) | Finite order, full determinant, transfer of the real-orthogonal estimate, bounded Fourier norms, signed cosets, uniform support bound and exact whole-measure identity. |
| dependency | [Real-orthogonal determinant estimate](Yin_C_G0885_v1.md#argument) | The determinant-preserving row operations and uniform estimate use only real orthogonality and transfer through the positive square root of H; no cyclic-coordinate sparsity is transferred. |
| dependency | [Integral transvection identity](../ledger/Yin_L_G0462_v13.md#integer-generators) | Pairing preservation, negative-vector inverse and integrality under the exact even-norm hypotheses, with the retained GHS13 attribution. |
| dependency | [Accepted Sanders theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Integer-valued functions on finite abelian groups with the fixed Fourier algebra norm bound admit uniformly bounded signed coset decompositions, at the recorded statement-level inspection depth. |
| dependency | [Accepted DS17 fixed-support theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) | The actual nonzero integer polynomial U has a fixed term bound and unchanged total logarithmic measure; no new foundational proof audit or effective numerical gap is claimed. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1114_v3.md#positive-lattice-two-transvection-gap-review) | Exact statement, whole argument, all necessary input interfaces and unbounded-parameter qualifications, without an unrestricted G0001 conclusion. |

## Current assessment

[Selected decision](#decision-positive-lattice-two-transvection-gap)
