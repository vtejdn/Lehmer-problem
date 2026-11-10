---
author: Yin
---

# Exact rotating-shear transfer for adjacent two-edge clusters and a balanced-word gap

This project deduction extends the exact local arithmetic interface of the [rotating-shear law](../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law) to two adjacent active edges on three sites.
The [disjoint-edge theorem](../claims/Yin_C_G0889_v1.md#local-transfer) supplies the cyclic determinant bookkeeping but not the local equations: the full product \(DE\) must now be retained.
The complete three-site transfer below covers all sixteen sign choices and composes when distinct cluster vertex supports are disjoint.
An internally balanced subfamily has only monomial pivots and a two-letter unimodular matrix interface.
For every word of \(m\ge1\) clusters in that subfamily, the argument below proves the complete bound \(M(P_A)\ge\max\{2,\sqrt m\}\).
Other cluster types and their globally balanced mixtures remain outside that measure bound.
The [selected assessment](#decision-adjacent-cluster-transfer-and-gap) adopts the complete contribution after its [independent review](../audits/reviews/Yin_R_G1115_v2.md#adjacent-cluster-transfer-review), at the finding's actual dependency and context scope.
The disjoint-edge contribution and its selected assessment remain at [v1](../claims/Yin_C_G0889_v1.md#decision-balanced-disjoint-edge-gap), without transferring that review to the adjacent-cluster extension.
The [fixed-periodic closure result](../claims/Yin_C_G0888_v1.md#statement) does not supply this nonperiodic local interface.
The formulas were derived by exact hand elimination, with no numerical sampling, symbolic program or root computation.

<a id="statement"></a>
## Standalone statement

Let \(g\ge3\), and let \(Se_j=e_{j+1}\) on \(\mathbb Z^g\), with cyclic indices.
Choose \(m\ge0\) clusters whose three-site supports \(\{j,j+1,j+2\}\) are pairwise disjoint, and activate exactly the two edges starting at \(j\) and \(j+1\) in each cluster.
Thus \(3m\le g\); any sites outside these supports are neutral, and there are no other active edges.
For the active edges set \(v_i=e_i-e_{i+1}\), \(w_i=e_i+e_{i+1}\), and choose arbitrary signs \(\epsilon_i,\eta_i\in\{1,-1\}\).
Define
\[
 D=\sum_i\epsilon_i v_iv_i^{\mathsf T},\qquad
 E=\sum_i\eta_i w_iw_i^{\mathsf T},\qquad
 A=\operatorname{diag}(S,S)
 \begin{pmatrix}I&D\\0&I\end{pmatrix}
 \begin{pmatrix}I&0\\E&I\end{pmatrix}.
\]
Write \(P_A(z)=\det(zI_{2g}-A)\), and for a monic polynomial \(P\) use the complete measure \(M(P)=\prod_{P(\lambda)=0}\max\{1,|\lambda|\}\), counting every root with its algebraic multiplicity.
Its logarithmic measure is \(m(P)=\log M(P)\).
List the clusters in cyclic order, and write their signs as \((a_j,b_j,c_j,d_j)=(\epsilon_j^{(1)},\epsilon_j^{(2)},\eta_j^{(1)},\eta_j^{(2)})\).
For each cluster put
\[
 \rho_j=b_jc_j,\quad
 \kappa_j=a_jc_j+b_jd_j+a_jd_j+a_jb_jc_jd_j,\quad
 \delta_j=1+\kappa_j,
\]
\[
 \alpha_j=a_j+b_j(1+a_jc_j),\qquad
 \beta_j=d_j+c_j(1+b_jd_j),\qquad
 N_j(t)=\begin{pmatrix}
 \delta_j-\rho_j(t^2-4)&\alpha_j(2-t)\\
 \beta_j(2+t)&\delta_j
 \end{pmatrix}.
\]
Then the complete monic integral reciprocal characteristic polynomial is
\[
 \boxed{\quad
 \det(zI_{2g}-A)
 =z^{2g-2m}\prod_{j=1}^m(z^2+\kappa_j)
 -z^g\operatorname{tr}\bigl(N_m(z+z^{-1})\cdots N_1(z+z^{-1})\bigr)
 +\prod_{j=1}^m(1+\kappa_jz^2).
 \quad}                                                     \tag{S}
\]
Although its middle term is written using Laurent notation, (S) is a polynomial identity of degree \(2g\) with constant term one, valid at every spectral parameter and retaining all algebraic multiplicities.
The [local transfer](#complete-local-transfer) specifies the exact internal pivot \(\Delta_j=z^2(z^2+\kappa_j)\), its primitive matrix numerator \(F_j=z^2N_j(z+z^{-1})\), and the complementary determinant \(\Psi_j=1+\kappa_jz^2\), for all sixteen sign choices.
No local pivot root is separately declared an eigenvalue.
At fixed \(g\) and cyclic cluster data, redistributing the neutral intervals leaves the full polynomial unchanged.
The empty-product case \(m=0\) is \((z^g-1)^2\).

If \(m\ge1\) and each cluster has signs \((e_j,-e_j,-e_j,e_j)\), \(e_j\in\{1,-1\}\), then both original sign vectors are balanced, \(\kappa_j=0\), and
\[
 N_j(t)=C_{e_j}(t)=\begin{pmatrix}5-t^2&e_j(2-t)\\e_j(2+t)&1\end{pmatrix},\qquad
 \det C_{e_j}=1.
\]
For every such word and every \(g\ge3m\), its full characteristic polynomial satisfies
\[
 P_A(z)=z^{2g}-z^g\operatorname{tr}(C_{e_m}(z+z^{-1})\cdots C_{e_1}(z+z^{-1}))+1,
 \qquad \boxed{M(P_A)\ge\max\{2,\sqrt m\}.}
\]
For general cluster signs, belonging to the original balanced law instead requires only \(\sum_j(a_j+b_j)=\sum_j(c_j+d_j)=0\); the measure bound is not asserted for every such globally balanced word.
The full arbitrary-sign polynomial (S) has at most \(6m+3\) nonzero monomials, independently of the neutral length.
No additional measure gap is inferred here merely from that monomial count.
The [remaining-type control](#remaining-type-control) supplies a globally balanced twenty-four-cluster word among the other \(\kappa=0\) types for which the trace is strictly between \(-2\) and \(2\) on a nonempty real interval.
It disproves extension of the trace-positivity premise used below to all globally balanced monomial-pivot words, without asserting any small complete measure.

<a id="dependencies"></a>
## Exact reused inputs

The algebraic proof reuses only the [cyclic two-coordinate determinant identity in v1](../claims/Yin_C_G0889_v1.md#local-transfer): a cyclic system \(zu_{j+1}=W_ju_j\) has determinant \(\det(z^hI_2-W_h\cdots W_1)\), with its explicit scalar-pivot accounting.
The present local equations retain \(DE\) and are proved below; v1's disjoint-edge equations, sign reduction and measure bound are not premises for them.
The analytic proof reuses [Den09-U001, Mahler conventions and singularities](../audits/literature/Den09/Yin_U001.md#mahler-measure), only for integrability of the logarithm of a nonzero one-variable polynomial and the Jensen/root-product identity with unit-circle zeros.
Its original foundational proof is not newly audited here.
The L462 law and J153 source establish the exact matrix definition and rotation orientation; no finite sampled output or root certificate from J153 is used in the proof.
C888 is a comparison identifying the fixed-periodic scope, not a proof dependency.

<a id="cluster-data"></a>
## A primitive cluster and the full local matrix

Use \(Se_j=e_{j+1}\), as in the actual [J153 matrix construction](../computations/programs/Yin_J_G0153/rotating_shears.py).
A primitive two-edge cluster has active edges \(\{1,2\}\) and \(\{2,3\}\), with their four signs written
\[
 (a,b,c,d)=(\epsilon_1,\epsilon_2,\eta_1,\eta_2)\in\{1,-1\}^4.
\]
In local site coordinates,
\[
 D=\begin{pmatrix}a&-a&0\\-a&a+b&-b\\0&-b&b\end{pmatrix},\qquad
 E=\begin{pmatrix}c&c&0\\c&c+d&d\\0&d&d\end{pmatrix}.
\]
Set \(p=ad\) and \(\rho=bc\).
The cross term is
\[
 DE=\begin{pmatrix}0&-p&-p\\
                    \rho&p+\rho&p\\
                    -\rho&-\rho&0\end{pmatrix}.             \tag{1}
\]
In particular this term is nonzero for every one of the sixteen sign choices.
The local shear product is \(B=\begin{pmatrix}I+DE&D\\E&I\end{pmatrix}\), with determinant one.
After grouping coordinates as \(u_j=(x_j,y_j)^{\mathsf T}\), its two-by-two site blocks are
\[
\begin{array}{lll}
B_{11}=\begin{pmatrix}1&a\\c&1\end{pmatrix},&
B_{12}=\begin{pmatrix}-p&-a\\c&0\end{pmatrix},&
B_{13}=\begin{pmatrix}-p&0\\0&0\end{pmatrix},\\[3mm]
B_{21}=\begin{pmatrix}\rho&-a\\c&0\end{pmatrix},&
B_{22}=\begin{pmatrix}1+p+\rho&a+b\\c+d&1\end{pmatrix},&
B_{23}=\begin{pmatrix}p&-b\\d&0\end{pmatrix},\\[3mm]
B_{31}=\begin{pmatrix}-\rho&0\\0&0\end{pmatrix},&
B_{32}=\begin{pmatrix}-\rho&-b\\d&0\end{pmatrix},&
B_{33}=\begin{pmatrix}1&b\\d&1\end{pmatrix}.
\end{array}                                                   \tag{2}
\]
Multiplying \(zI-A\) on the left by \(\operatorname{diag}(S^{-1},S^{-1})\) preserves its determinant.
The three local equations are therefore exactly
\[
 zu_2=B_{11}u_1+B_{12}u_2+B_{13}u_3,
\]
\[
 zu_3=B_{21}u_1+B_{22}u_2+B_{23}u_3,
\]
\[
 zu_4=B_{31}u_1+B_{32}u_2+B_{33}u_3.                       \tag{3}
\]
Here \(u_4\) is the next site outside the cluster; in a three-site cyclic system it means \(u_1\).
Equations (3), not the disjoint-edge equations, are the starting point.

<a id="complete-local-transfer"></a>
## Exact local transfer and arithmetic normalization

Define the integer parameters
\[
 \kappa=ac+bd+ad+abcd,\qquad \delta=1+\kappa,
 \qquad \alpha=a+b(1+ac),\qquad \beta=d+c(1+bd).
                                                               \tag{4}
\]
They satisfy
\[
 \alpha\beta=\kappa+\rho(1+\kappa).                         \tag{5}
\]
The complete pivot, numerator matrix and complementary determinant are
\[
 \Delta(z)=z^2(z^2+\kappa),\qquad \Psi(z)=1+\kappa z^2,
\]
\[
 F(z)=
 \begin{pmatrix}
 \delta z^2-\rho(z^2-1)^2&-\alpha z(z-1)^2\\
 \beta z(z+1)^2&\delta z^2
 \end{pmatrix}.                                            \tag{6}
\]
For \(\Delta(z)\ne0\), the exact transfer is
\[
 \boxed{\quad zu_4=\frac{F(z)}{\Delta(z)}u_1.\quad}        \tag{7}
\]
The normalization includes the full pivot factor, and
\[
 \boxed{\det F(z)=\Delta(z)\Psi(z).}                        \tag{8}
\]
For a trace parameter \(t=z+z^{-1}\), put
\[
 N(t)=\begin{pmatrix}
 \delta-\rho(t^2-4)&\alpha(2-t)\\
 \beta(2+t)&\delta
 \end{pmatrix}.
\]
Then \(F(z)=z^2N(z+z^{-1})\), and (7) can equivalently be written
\[
 zu_4=\frac{N(z+z^{-1})}{z^2+\kappa}u_1,
 \qquad
 u_4=\frac{N(z+z^{-1})}{z(z^2+\kappa)}u_1.                \tag{9}
\]
This Laurent notation does not permit omission of the factors at \(z=0\).
The corresponding determinant is
\[
 \det N(t)=\kappa t^2+(\kappa-1)^2.                        \tag{10}
\]

To verify (6)--(7), eliminate the internal variables \((u_2,u_3)\) using the first two equations of (3).
Their pivot matrix, input matrix and output matrix are
\[
 K(z)=
 \begin{pmatrix}
 z+p&a&p&0\\
 -c&z&0&0\\
 -(1+p+\rho)&-(a+b)&z-p&b\\
 -(c+d)&-1&-d&z
 \end{pmatrix},\qquad
 C=\begin{pmatrix}B_{11}\\B_{21}\end{pmatrix},\qquad
 L=\begin{pmatrix}B_{32}&B_{33}\end{pmatrix}.
\]
Writing \(u=ac\), \(v=bd\), the two diagonal two-by-two block determinants are
\[
 R_1=z^2+pz+u,\qquad R_2=z^2-pz+v.
\]
The upper-right block of \(K\) has rank one, and its direct determinant expansion gives
\[
 \begin{aligned}
 \det K
 &=R_1R_2+p\bigl((1+p+\rho)z^2+(u-v)z-\rho\bigr)\\
 &=z^2(z^2+u+v+p+uv)=\Delta(z),
 \end{aligned}                                             \tag{11}
\]
using \(p^2=1\) and \(uv=p\rho\).
There is no assumption that either \(R_1\) or \(R_2\) is nonzero in the final identity.
The output numerator is exactly
\[
 F=\Delta B_{31}+L\operatorname{adj}(K)C.                  \tag{12}
\]
Expanding this bounded matrix expression using the sign squares equal to one gives (6).
The following internal-coordinate formulas make that expansion directly reproducible:
\[
 \Delta x_2
 =z\bigl(z^2-(\kappa-v)z+v\bigr)x_1
   +az^2(z-1)y_1,
\]
\[
 z\Delta x_3
 =z\bigl(\rho z^3+(1+\rho+\kappa-v)z^2-(v+\rho)z-\rho\bigr)x_1
   +z^2(z-1)(\alpha-az)y_1,                               \tag{13}
\]
\[
 zy_2=cx_1+cx_2+y_1,\qquad
 zy_3=cx_1+(c+d)x_2+dx_3+y_2.
\]
They solve the first two equations of (3) at generic \(z\); substituting them into the third gives (6)--(7).
Finally, (5) verifies the determinant independently of those divisions:
\[
 \begin{aligned}
 \det F
 &=z^2\left(\delta^2z^2+(\alpha\beta-\rho\delta)(z^2-1)^2\right)\\
 &=z^2\left((1+\kappa)^2z^2+\kappa(z^2-1)^2\right)\\
 &=z^2(z^2+\kappa)(1+\kappa z^2).
 \end{aligned}
\]
Thus all intermediate divisions have explicit polynomial certificates.

<a id="sixteen-signs"></a>
## All sixteen choices

The following eight rows take \(a=1\).
The other eight rows are obtained by replacing \((a,b,c,d)\) with \((-a,-b,-c,-d)\).
This keeps \(\rho,\kappa\) fixed and changes \((\alpha,\beta)\) to \((-\alpha,-\beta)\), which conjugates \(F,N\) by \(\operatorname{diag}(1,-1)\).
This is a rule for completing the table, not permission to flip arbitrary individual clusters without changing their combined ordered product.

| \(a\) | \(b\) | \(c\) | \(d\) | \(\rho\) | \(\kappa\) | \(\alpha\) | \(\beta\) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 4 | 3 | 3 |
| 1 | 1 | 1 | -1 | 1 | -2 | 3 | -1 |
| 1 | 1 | -1 | 1 | -1 | 0 | 1 | -1 |
| 1 | 1 | -1 | -1 | -1 | -2 | 1 | -1 |
| 1 | -1 | 1 | 1 | -1 | 0 | -1 | 1 |
| 1 | -1 | 1 | -1 | -1 | 2 | -1 | 1 |
| 1 | -1 | -1 | 1 | 1 | 0 | 1 | 1 |
| 1 | -1 | -1 | -1 | 1 | -2 | 1 | -3 |

Consequently \(\kappa\in\{4,2,0,-2\}\), occurring respectively for two, two, six and six of the sixteen choices.
For \(\kappa\ne0\), the local pivot has a double zero at zero and simple roots of \(z^2+\kappa\).
For \(\kappa=0\), it is \(z^4\).
These are poles of a generic local elimination, not automatically roots of a completed cyclic characteristic polynomial.

No scalar factor of \(\Delta\) can be cancelled simultaneously from every entry of \(F\).
Indeed \(F_{11}(0)=-\rho\ne0\), and for \(\kappa\ne0\), \(\Psi\) is nonzero at the roots of \(z^2+\kappa\), since there it equals \(1-\kappa^2\ne0\).
By (8), those roots are simple zeros of \(\det F\), precluding their occurrence in every entry of \(F\).
Also \(F_{11}(0)=\pm1\) makes its scalar integer content one.
This establishes the stated primitive arithmetic normalization of the common matrix denominator.

<a id="cluster-composition"></a>
## Composition of separated clusters with all pivot roots retained

Let there be \(m\) clusters of two adjacent active edges on a cyclic set of \(g\) sites.
Require that their three-site vertex supports are pairwise disjoint and that there are no other active edges.
For a nonempty cluster list, this separation means that each cluster is separated from the next by an inactive connecting edge and possibly \(n_j\ge0\) neutral sites, with
\[
 3m\le g,\qquad \sum_{j=1}^m n_j=g-3m.
\]
Zero neutral sites are allowed: the inactive connecting edge already separates the vertex supports.
The cluster matrices \(D_j,E_j\), and hence their products, are block diagonal across these supports.
Therefore (3) is the exact local equation for every cluster, with no missing cross-cluster term in \(DE\).
If two proposed clusters share a vertex, this condition fails and their contributions must instead be combined into a larger component; formulas (6)--(9) cannot simply be composed.

List the clusters in cyclic order, and let their data carry subscripts \(j\).
Put
\[
 h=g-2m,\qquad H(z)=\prod_{j=1}^m\Delta_j(z),\qquad
 Q(z)=\prod_{j=1}^m\Psi_j(z).
\]
Eliminating the two internal site vectors of every cluster contributes exactly \(H(z)\), and leaves \(h\) cyclic site vectors.
A contracted cluster has weight \(F_j/\Delta_j\) in an equation \(zu_{\ell+1}=W_\ell u_\ell\); a neutral site has weight \(I_2\).
The [cyclic two-coordinate determinant identity](../claims/Yin_C_G0889_v1.md#local-transfer) then gives, at generic \(z\),
\[
 P_A(z)=H(z)\det\left(z^hI_2-\frac{F_m(z)\cdots F_1(z)}{H(z)}\right).
\]
The determinant term in this two-by-two expansion is fully paid by (8):
\[
 \frac{\det(F_m\cdots F_1)}{H}
 =\prod_{j=1}^m\Psi_j=Q.
\]
Thus the complete polynomial, with no remaining division, is
\[
 \boxed{\quad
 P_A(z)=H(z)z^{2h}-z^h\operatorname{tr}(F_m(z)\cdots F_1(z))+Q(z).
 \quad}                                                     \tag{14}
\]
Equivalently,
\[
 \boxed{\quad
 P_A(z)=z^{2g-2m}\prod_{j=1}^m(z^2+\kappa_j)
 -z^g\operatorname{tr}\bigl(N_m(z+z^{-1})\cdots N_1(z+z^{-1})\bigr)
 +\prod_{j=1}^m(1+\kappa_jz^2).
 \quad}                                                     \tag{15}
\]
Each side of (14) is a polynomial and the generic equality extends identically to all complex \(z\).
This retains every algebraic multiplicity, including at all the local pivot roots; it neither inserts nor removes those roots from the full polynomial.
In (15) the trace has Laurent exponents between \(-2m\) and \(2m\), so the displayed factor \(z^g\) clears them because \(g\ge3m\).
For \(m>0\), (14) has leading term \(z^{2g}\), its middle term has degree at most \(g+2m<2g\), and its constant term is \(Q(0)=1\).
The original integral symplectic matrix gives the same reciprocal normalization.
For \(m=0\), the empty-product interpretation gives \((z^g-1)^2\).

For example, a single cluster on any \(g\ge3\) has the completely explicit polynomial
\[
 P_A(z)=z^{2g-2}(z^2+\kappa)
 -z^{g-2}\bigl(2(1+\kappa)z^2-\rho(z^2-1)^2\bigr)
 +(1+\kappa z^2).                                        \tag{16}
\]
At a nonzero root \(z_0\) of its pivot, where \(z_0^2=-\kappa\), this evaluates to
\[
 P_A(z_0)=1-\kappa^2
 +z_0^{g-2}\bigl(2\kappa(1+\kappa)+\rho(1+\kappa)^2\bigr).
\]
Thus even the single-cluster formula requires the complete cyclic expression to decide whether a pivot root is an eigenvalue.
It is not legitimate to append the pivot factors to a separate transfer characteristic equation.

At fixed \(g\) and fixed cyclic cluster data, changing the individual neutral intervals leaves (14) unchanged.
For the original balanced law the additional conditions are exactly
\[
 \sum_{j=1}^m(a_j+b_j)=0,\qquad
 \sum_{j=1}^m(c_j+d_j)=0.
\]
The unrestricted transfer formulas do not impose balance on each cluster separately.

<a id="balanced-monomial-pivot"></a>
## Internally balanced controls and a monomial-pivot subfamily

An internally balanced cluster has
\[
 (a,b,c,d)=(e,-e,f,-f),\qquad s=ef.
\]
Then
\[
 \rho=-s,\quad \kappa=s+1,\quad
 \alpha=-es,\quad\beta=fs,\quad
 \Delta=z^2(z^2+s+1).
\]
This verifies the double-zero/nonunit factor \(z^2(z^2+2)\) for \(s=1\), and the fourth-order monomial \(z^4\) for \(s=-1\).
Both still use the full nonzero cross term (1).

In the second case, \(f=-e\), so \(\rho=1,\kappa=0,\alpha=\beta=e\).
The trace-parameter matrix becomes
\[
 C_e(t)=\begin{pmatrix}5-t^2&e(2-t)\\e(2+t)&1\end{pmatrix}
 =\begin{pmatrix}1&e(2-t)\\0&1\end{pmatrix}
  \begin{pmatrix}1&0\\e(2+t)&1\end{pmatrix},\qquad \det C_e=1.
                                                               \tag{17}
\]
Its local transfer is exactly \(zu_4=z^{-2}C_e(z+z^{-1})u_1\).
For any cyclic sequence \(e_1,\ldots,e_m\in\{1,-1\}\) of separated clusters of this type, each cluster is already balanced in both original sign vectors.
The whole input therefore belongs to the original law with \(k=2m\), and (15) simplifies to
\[
 \boxed{\quad P_A(z)=z^{2g}
 -z^g\operatorname{tr}\bigl(C_{e_m}(z+z^{-1})\cdots C_{e_1}(z+z^{-1})\bigr)+1,
 \qquad 3m\le g.\quad}                                    \tag{18}
\]
There is no nonmonomial local pivot cost in (18), and no missing scalar determinant or zero-root factor.
In particular \(P_A(0)=1\).
This exact input admits the following complete-measure bound for arbitrary growing words in these two cluster types.

<a id="cluster-word-gap"></a>
## Complete cost of the internally balanced monomial-pivot words

For every \(m\ge1\), every \(e_1,\ldots,e_m\in\{1,-1\}\), and every integer \(g\ge3m\), the full polynomial (18) satisfies
\[
 \boxed{\quad M(P_A)\ge\max\{2,\sqrt m\}.\quad}            \tag{19}
\]
This estimate uses the one-variable integral/root-product identity, including unit-circle zeros, at the exact interface of [Den09-U001](../audits/literature/Den09/Yin_U001.md#mahler-measure).
It is a bound on all roots of the degree-\(2g\) polynomial, not a normalized cost or a selected factor.

For real \(-2<t<2\), put
\[
 x=4-t^2>0,\qquad
 D_t=\operatorname{diag}(\sqrt{2-t},\sqrt{2+t}),\qquad
 H_0=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
The same two changes of basis work for every sign in the word:
\[
 D_t^{-1}C_e(t)D_t
 =\begin{pmatrix}1+x&e\sqrt x\\e\sqrt x&1\end{pmatrix},
\]
\[
 H_0^{-1}D_t^{-1}C_e(t)D_tH_0
 =\begin{pmatrix}1+x/2+e\sqrt x&x/2\\
                  x/2&1+x/2-e\sqrt x\end{pmatrix}.        \tag{20}
\]
All four entries in (20) are positive.
In particular, the smaller diagonal entry is
\(1-\sqrt x+x/2=((\sqrt x-1)^2+1)/2>0\).
Write
\[
 A_x=1+\sqrt x+x/2,\qquad D_x=1-\sqrt x+x/2,
 \qquad A_xD_x=1+x^2/4.
\]
If the word has \(p\) plus signs and \(q\) minus signs, \(p+q=m\), then expansion of the trace of the product of (20) is a sum of nonnegative products of entries.
Keeping only the two terms that remain at the same matrix index through the whole word gives
\[
 \begin{aligned}
 T(t)&:=\operatorname{tr}(C_{e_m}(t)\cdots C_{e_1}(t))\\
 &\ge A_x^pD_x^q+D_x^pA_x^q
 \ge2(A_xD_x)^{m/2}
 =2(1+x^2/4)^{m/2}.                                      \tag{21}
 \end{aligned}
\]
The last inequality is \(u+v\ge2\sqrt{uv}\) for positive \(u,v\).
For \(m\ge2\), the derivative of \((1+y)^{m/2}\) for \(y\ge0\) is at least \(m/2\), so (21) implies
\[
 T(t)-2\ge \frac m4 x^2.                                  \tag{22}
\]
No condition on the order of the signs was used.
Although \(D_t\) is singular at \(t=\pm2\), the trace is polynomial in \(t\), so the inequality extends there by continuity.
Directly, \(C_e(2)\) and \(C_e(-2)\) are triangular unipotent matrices, of one common triangular orientation at each endpoint, and their product has trace two.

On \(z=e^{i\theta}\), one has \(t=2\cos\theta\), \(x=4\sin^2\theta\), and (18) gives
\[
 |P_A(e^{i\theta})|
 =T(2\cos\theta)-2\cos(g\theta)
 =(T-2)+V(\theta),\qquad
 V(\theta)=4\sin^2(g\theta/2).                            \tag{23}
\]
The absence of an absolute-value sign on the right follows from \(T\ge2\).
For \(m\ge2\), use (22), followed by the same two-term arithmetic-geometric inequality:
\[
 |P_A(e^{i\theta})|
 \ge \frac m4 x^2+V
 \ge2\sqrt{\frac m4 x^2V}.                               \tag{24}
\]
Both factors on the right are strictly positive except at finitely many angles.
The Jensen identity for \(1-z^2\) and \(1-z^g\) gives
\[
 \frac1{2\pi}\int_0^{2\pi}\log x\,d\theta=0,\qquad
 \frac1{2\pi}\int_0^{2\pi}\log V\,d\theta=0,
\]
since \(x=|1-e^{2i\theta}|^2\) and \(V=|1-e^{ig\theta}|^2\).
Their logarithms, as well as that of the nonzero polynomial \(P_A\), are integrable with the unit-circle zeros included.
Taking logarithms of (24) off the finite exceptional set and integrating therefore yields
\[
 m(P_A)\ge\log2+\tfrac12\log(m/4)=\tfrac12\log m.
                                                               \tag{25}
\]
This uses neither a principal value nor a limit interchange.

The small values \(m=1,2,3\) give the remaining uniform factor two.
For \(m=1\), \(T-2=x\).
For \(m=2\), multiplication gives
\[
 T-2=x^2+2(1+e_1e_2)x\ge x^2.
\]
For \(m=3\), let \(S=e_1e_2+e_1e_3+e_2e_3\in\{-1,3\}\).
Expansion of the product gives
\[
 T-2=(3+2S)x+(3+S)x^2+x^3\ge x.                          \tag{26}
\]
For instance, in the symmetric matrices before the \(H_0\) change of basis, the zero-off-diagonal choice contributes \((1+x)^3+1\), each chosen pair of off-diagonal terms contributes \(e_ie_jx(2+x)\), and the odd choices have zero trace, which gives (26).
In (23), apply \(x+V\ge2\sqrt{xV}\) for \(m=1,3\), and \(x^2+V\ge2\sqrt{x^2V}\) for \(m=2\).
The same zero means of logarithms give \(m(P_A)\ge\log2\).
For \(m\ge4\), (25) already gives \(\sqrt m\ge2\).
This proves (19) for every word and every allowed length.

<a id="remaining-type-control"></a>
## An exact scope control for the other monomial-pivot types

For the other \(\kappa=0\) types define
\[
 E_s(t)=\begin{pmatrix}1-x&s(2-t)\\-s(2+t)&1\end{pmatrix},
 \qquad x=4-t^2,\qquad s\in\{1,-1\}.
\]
The actual cluster type \((a,b,c,d)=(1,1,-1,1)\) gives \(E_+\), with balance contribution \((a+b,c+d)=(2,0)\).
Its full sign reversal \((-1,-1,1,-1)\) gives \(E_-\), with contribution \((-2,0)\).
Both have \(\kappa=0,\rho=-1\) and determinant one.
Consider the ordered matrix word
\[
 W(t)=E_+E_-E_+^2E_-^7E_+^5E_-^4E_+^4.                  \tag{27}
\]
It contains twelve copies of each type.
Realize the factors in reverse order along the physical cyclic list of clusters, so that the product \(N_m\cdots N_1\) is exactly (27).
For every \(g\ge72\), their twenty-four three-site supports can be disjoint, both original sign vectors are balanced, and their actual complete polynomial is
\[
 P_g^W(z)=z^{2g}-z^g\operatorname{tr}W(z+z^{-1})+1.        \tag{28}
\]
This is an exact input specification, not an executed numerical experiment.

At \(t=\sqrt3\), \(x=1\), and the same diagonal matrix \(D_t\) used in (20) gives
\[
 D_t^{-1}E_+(t)D_t=A=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\qquad
 D_t^{-1}E_-(t)D_t=B=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
\]
Direct multiplication yields \(A^3=B^3=-I\), so \(A^6=B^6=I\).
Writing \(X=AB\), \(Y=A^2B^2\), the specialized word is
\[
 AB A^2B^7A^5B^4A^4
 =AB A^2B A^{-1}B^{-2}A^{-2}
 =XYX^{-1}Y^{-1}.
\]
The matrices are explicitly
\[
 X=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad
 Y=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
 XYX^{-1}Y^{-1}=\begin{pmatrix}5&-6\\6&-7\end{pmatrix}.
\]
Hence \(\operatorname{tr}W(\sqrt3)=-2\).
At \(t=2\), each \(E_s\) is \(\begin{pmatrix}1&0\\-4s&1\end{pmatrix}\), and the equal plus and minus counts make their product the identity.
Thus \(\operatorname{tr}W(2)=2\).

The trace is a real polynomial in \(t\).
By continuity it takes the value zero at some point of \((\sqrt3,2)\), and therefore lies in \((-2,2)\) on a nonempty open subinterval.
Consequently the universal inequality \(T\ge2\) in (21) is false for the enlarged class of globally balanced \(\kappa=0\) words.
In particular the common nonnegative-entry mechanism cannot be extended to this entire class: any nonnegative two-by-two matrix of determinant one has trace at least two, since its diagonal product is at least one.
The control neither changes the internally balanced theorem (19) nor gives a small complete measure for (28).

<a id="return-boundary"></a>
## Present result and remaining question

The local calculation is complete for all sixteen sign choices, and (14)--(15) give its cyclic composition with all exceptional spectral parameters and multiplicities retained.
The bound (19) excludes a shrinking positive complete measure for every growing word in the internally balanced \(\kappa=0\) types; in fact it diverges at least as \(\sqrt m\).
This does not cover every type with a monomial pivot.
The table also contains four \(\kappa=0,\rho=-1\) choices after including the global sign reversals, and those clusters are not internally balanced.
They may occur in globally balanced mixtures, but their matrices do not have the common positive-entry transformation (20).
The explicit control (27)--(28) proves failure of the resulting trace premise even on an actual globally balanced word.
The remaining concrete question concerns globally balanced words using these other types, \(\kappa\ne0\) types, or their mixtures, with the complete polynomial (14) retaining the nonmonomial pivot cancellations.
Larger connected active-edge components are also outside the two-edge interface.

For fixed \(m\), the first and third terms of (15) each have at most \(m+1\) monomials, and the middle Laurent trace has at most \(4m+1\).
Thus the complete polynomial has at most \(6m+3\) monomials before any coincidences or cancellations, independently of the neutral length.
This is the proved support-count conclusion; no broader fixed-support Mahler-gap theorem is invoked here.

## Assessment history

### Decision adjacent-cluster-transfer-and-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T10:27 |
| status | proved |
| reason | Complete independent review verifies the original three-site equations with DE, all sixteen signs, the full cyclic determinant and spectral multiplicities, and M>=max(2,sqrt(m)) for every internally balanced monomial-pivot word. The exact remaining-type word disproves extension of the trace-positivity premise; other mixtures and larger connected components remain outside the measure bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete adjacent-cluster statements](#statement) | Arbitrary allowed g and m, all signs on disjoint three-site supports, full polynomial, empty case, internally balanced whole-measure bound and fixed-m support count. |
| argument | [Exact original cluster data](#cluster-data) | Full D, E and DE, original matrix orientation and all local equations. |
| argument | [Complete local transfer](#complete-local-transfer) | Four-dimensional pivot, internal coordinates, all numerator entries, determinant identities and generic-division continuation. |
| argument | [All sixteen types](#sixteen-signs) | Sign table, reversal, pivot roots, primitive common denominator and integer content. |
| argument | [Cyclic composition](#cluster-composition) | Every scalar factor, contracted cycle, all exceptional spectral values and multiplicities, neutral gaps, empty input and balance conditions. |
| argument | [Internally balanced types](#balanced-monomial-pivot) | Exact unimodular matrices and complete characteristic polynomial for every such word. |
| argument | [Complete word bound](#cluster-word-gap) | Common positive-entry transformations, ordered trace bound, unit-circle identity, scalar Jensen with zeros, all small-m cases and the uniform lower bound. |
| argument | [Remaining-type control](#remaining-type-control) | Actual globally balanced 24-cluster word, exact commutator and trace interval; failure only of the extended positivity premise, with no small-measure assertion. |
| argument | [Return boundary](#return-boundary) | Other types and mixtures, larger connected components and the exact support-count limit. |
| dependency | [Reused cyclic identity](../claims/Yin_C_G0889_v1.md#local-transfer) | Only the cyclic two-coordinate determinant and scalar-pivot accounting, not the disjoint-edge local equations or gap. |
| dependency | [Scalar Mahler input](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the retained one-variable logarithmic integrability and Jensen/root-product identity with unit-circle zeros; no new audit of foundational proofs. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1115_v2.md#adjacent-cluster-transfer-review) | Entire final fixed contribution, actual model and dependency interfaces, all boundary cases and the clarified nonempty interval description, at its recorded review relationship and context scope. |

## Current assessment

[Selected decision](#decision-adjacent-cluster-transfer-and-gap)

