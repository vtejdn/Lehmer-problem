---
author: Yin
---

# Exact disjoint-edge transfer and a gap for balanced rotating shears

This project deduction concerns the disjoint active edges of the [rotating symplectic law](../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law).
The complete transfer identity makes neutral-gap placement irrelevant at fixed total length and cyclic sign order.
For the original balanced-sign law restricted to these edges, an explicitly computable integer distinguishes entirely cyclotomic outputs from outputs of complete Mahler measure at least four.
The complete contribution is adopted at the [selected decision](#decision-balanced-disjoint-edge-gap) after a [whole independent review](../audits/reviews/Yin_R_G1115_v1.md#balanced-disjoint-edge-transfer-review), with the source and scope limits retained there.
The [existing finite computation](../computations/programs/Yin_J_G0153/readme.md#factor-diagnostics) does not cover this unbounded disjoint-edge subfamily as a theorem.
The only analytic source input needed below is the one-variable Mahler/Jensen identity, including unit-circle zeros, in [Den09-U001](../audits/literature/Den09/Yin_U001.md#mahler-measure).

<a id="statement"></a>
## Statement and precise scope

Let \(g\ge3\), let \(S e_j=e_{j+1}\) with cyclic indices, and let the pairs \(\{i,i+1\}\), \(i\in I\), be pairwise disjoint.
Write \(k=|I|\), so \(2k\le g\).
For \(\epsilon_i,\eta_i\in\{-1,1\}\), put
\[
 v_i=e_i-e_{i+1},\quad w_i=e_i+e_{i+1},\quad
 D=\sum_{i\in I}\epsilon_i v_i v_i^{\mathsf T},\quad
 E=\sum_{i\in I}\eta_i w_i w_i^{\mathsf T},
\]
\[
 A=\operatorname{diag}(S,S)
 \begin{pmatrix}I&D\\0&I\end{pmatrix}
 \begin{pmatrix}I&0\\E&I\end{pmatrix},\qquad
 P_A(z)=\det(zI_{2g}-A).
\]
List the active edges in cyclic order as \(1,\ldots,k\); these labels index the active edges, rather than all coordinate sites.
Write
\[
 s_j=\epsilon_j\eta_j,\quad h=g-k,\quad
 H(z)=\prod_{j=1}^k(z^2+s_j),\quad \sigma=\prod_{j=1}^k s_j,
\]
\[
 F_j(z)=
 \begin{pmatrix}
 z(1+s_j)&-\epsilon_j(z-1)^2\\
 \eta_j(z+1)^2&z(1+s_j)
 \end{pmatrix}.
\]
The full characteristic polynomial is
\[
 \boxed{\quad
 P_A(z)=H(z)(z^{2h}+\sigma)-z^h\operatorname{tr}(F_k(z)\cdots F_1(z)).
 \quad}                                                     \tag{1}
\]
For \(k=0\), the products are empty and the trace is \(2\), so (1) gives \((z^g-1)^2\).
Formula (1) is a polynomial identity, including at \(z=0,\pm1,\pm i\), with every algebraic multiplicity retained.
It depends on the positions only through \(g\) and the cyclic order of the signed active edges.

Now impose the original law's two balancing conditions
\[
 \sum_{j=1}^k\epsilon_j=\sum_{j=1}^k\eta_j=0.
\]
They imply
\[
 n_{++}=n_{--}=a,\qquad n_{+-}=n_{-+}=b,\qquad k=2a+2b.
\]
For the chosen cyclic starting point let \(r_j\) be the number of preceding active edges with \(s=-1\), and define
\[
 c=\frac12\left|\sum_{j:s_j=1}\epsilon_j(-1)^{r_j}\right|.
                                                               \tag{2}
\]
Then \(c\) is an integer with \(0\le c\le a\).
Its value is unchanged by changing the cyclic starting point.
Put
\[
 \tau=(-1)^{b+c},\qquad
 G(z)=z^h(z+i)^{2c}-\tau(z-i)^{2c}.
\]
If \(\overline G\) denotes conjugation of the coefficients, without conjugating the variable, then
\[
 \boxed{\quad
 P_A(z)=(z^2+1)^{2a-2c}(z^2-1)^{2b}G(z)\overline G(z).
 \quad}                                                     \tag{3}
\]
In particular:

- If \(c=0\), then
  \[
  P_A(z)=H(z)\bigl(z^h-(-1)^b\bigr)^2
  \]
  is entirely cyclotomic and \(M(P_A)=1\).
- If \(c\ge1\), then the complete measure satisfies
  \[
  \boxed{M(P_A)\ge c^2 4^c\ge4,\qquad
  m(P_A)\ge2\log c+2c\log2.}                               \tag{4}
  \]

Thus \(c=0\) is also necessary for an entirely cyclotomic balanced output in this disjoint-edge subfamily.
The statement applies for every allowed \(g,k\), including unbounded \(k\) and \(k=o(g)\), provided the edges remain pairwise disjoint.
The empty-edge and one-edge controls are algebraic extensions; the original sampling law has even \(k\ge2\).
No conclusion about overlapping active edges is included.

<a id="local-transfer"></a>
## Local equations and the complete determinant

Disjoint supports give \(v_i^{\mathsf T}w_j=0\) for \(i\ne j\), while \(v_i^{\mathsf T}w_i=0\).
Consequently \(DE=ED=0\), and the shear product is \(\begin{pmatrix}I&D\\E&I\end{pmatrix}\).
Write the two coordinates at a site as \(u_j=(x_j,y_j)^{\mathsf T}\).
Multiplying \(zI-A\) on the left by \(\operatorname{diag}(S^{-1},S^{-1})\) preserves its determinant, since that matrix has determinant one.
The resulting equations use \(zu_{j+1}\), consistently with \(Se_j=e_{j+1}\).
This orientation also agrees with the actual construction in [J153](../computations/programs/Yin_J_G0153/rotating_shears.py).

For one active edge beginning at site \(j\), set
\[
 C=\begin{pmatrix}0&\epsilon\\\eta&0\end{pmatrix},\qquad
 Q=\begin{pmatrix}0&-\epsilon\\\eta&0\end{pmatrix},\qquad
 s=\epsilon\eta.
\]
The two site equations are exactly
\[
 (zI-Q)u_{j+1}=(I+C)u_j,\qquad
 zu_{j+2}=(I+C)u_{j+1}+Qu_j.                              \tag{5}
\]
At a neutral site the equation is \(zu_{j+1}=u_j\).
Since \(Q^2=-sI\), the first matrix in (5) has determinant \(z^2+s\).
For generic \(z\), elimination in (5) gives
\[
 zu_{j+2}=\frac{F(z)}{z^2+s}u_j,\qquad
 u_{j+2}=\frac{N(z+z^{-1})}{z^2+s}u_j,                    \tag{6}
\]
where \(F\) is the matrix in (1) and
\[
 N(t)=\begin{pmatrix}1+s&\epsilon(2-t)\\
                         \eta(2+t)&1+s\end{pmatrix},
 \qquad F(z)=zN(z+z^{-1}).
\]
For example, multiplying the numerator before division gives
\[
 (I+C)(zI+Q)(I+C)+(z^2+s)Q
 =z(1+s)I+2zC+(z^2+1)Q=F(z).
\]
Its determinant is
\[
 \det F(z)=z^2(1+s)^2+s(z^2-1)^2=s(z^2+s)^2.             \tag{7}
\]

Eliminate the internal variable \(u_{j+1}\) of every active edge using the first equation in (5).
These pivots involve disjoint variables, and contribute precisely the determinant factor \(H(z)\).
Reordering whole two-coordinate row or column blocks introduces no sign, because each interchange has even parity.
There remain \(h=g-k\) cyclic vertices with equations of the form
\[
 zu_{\ell+1}=W_\ell u_\ell.
\]
A neutral step has \(W_\ell=I\), and an active macro-step has \(W_\ell=F_j/(z^2+s_j)\).
For such a cycle, its determinant is
\[
 \det\bigl(z^h I_2-W_h\cdots W_1\bigr).                 \tag{8}
\]
Indeed, for \(z\ne0\), eliminating the first \(h-1\) forward equations contributes \(z^{2(h-1)}\), and leaves
\(zI_2-z^{-(h-1)}W_h\cdots W_1\).
The scalar powers cancel to give (8); the same identity holds identically in the entries after clearing any denominators.
It follows that
\[
 P_A(z)=H(z)\det\left(z^hI_2-\frac{F_k\cdots F_1}{H(z)}\right).
\]
Using (7), \(\det(F_k\cdots F_1)=\sigma H(z)^2\), and the two-dimensional determinant expansion gives (1).

This calculation first takes place away from \(z=0\) and the finitely many zeros of \(H\).
Both sides of (1) are polynomials and agree on that infinite set, so they agree identically.
No zeros of the pivot determinants have been removed from the final expression, and no extra roots have been added by an unaccounted denominator.
The leading term is \(z^{2g}\), and the constant term is \(\sigma H(0)=1\).
Thus \(z=0\) is never an eigenvalue, while values \(\pm1,\pm i\) are counted by the actual full polynomial.

The original matrices are integral and symplectic because \(D,E\) are symmetric and \(S\) is orthogonal.
Their determinant is one, and the symplectic identity makes \(A^{-1}\) similar to \(A^{\mathsf T}\).
Hence \(P_A\) is monic integral reciprocal of degree \(2g\), consistently with the complete determinant calculation.

<a id="one-two-edges"></a>
## One-edge and two-edge composition controls

For a single active edge, (1) gives
\[
 P_A(z)=(z^2+s)(z^{2g-2}+s)-2(1+s)z^g.                  \tag{9}
\]
For \(s=-1\) this is \((z^2-1)(z^{2g-2}-1)\), entirely cyclotomic.
The \(s=1\) case is the exact polynomial \((z^2+1)(z^{2g-2}+1)-4z^g\); a single edge is not a balanced input of the original law.

For two active edges, direct multiplication gives
\[
 \operatorname{tr}(F_2F_1)
 =2z^2(1+s_1)(1+s_2)
 -(\epsilon_2\eta_1+\eta_2\epsilon_1)(z^2-1)^2.          \tag{10}
\]
Equations (1) and (10) are the complete two-edge formula for every pair of sign choices and every allowed gap.
More explicitly, with \(\chi=\epsilon_1\epsilon_2\), they give
\[
\begin{array}{c|c}
\text{sign condition}&P_A(z)\\\hline
s_1\ne s_2&(z^4-1)(z^{2g-4}-1)\\
s_1=s_2=-1&(z^2-1)^2(z^{g-2}-\chi)^2\\
s_1=s_2=1,\ \chi=-1&(z^2+1)^2(z^{g-2}-1)^2\\
s_1=s_2=1,\ \chi=1&(z^2+1)^2(z^{g-2}+1)^2-16z^g.
\end{array}                                               \tag{11}
\]
In the balanced two-edge case, the second sign pair is the negative of the first, so \(s_1=s_2=s\) and \(\chi=-1\).
Thus every such input has
\[
 P_A(z)=(z^2+s)^2(z^{g-2}-s)^2,                           \tag{12}
\]
which is entirely cyclotomic.

For any number of disjoint edges, the composition criterion is the ordered matrix product in (1).
At fixed \(g\), two lists with the same multiset of \(s_j\) have the same characteristic polynomial if and only if their products \(F_k\cdots F_1\) have the same trace polynomial.
Neutral identity weights can be placed anywhere without altering that product.
In particular, a scalar product \(F_k\cdots F_1=\delta H I_2\), \(\delta\in\{1,-1\}\), forces \(\sigma=1\) and gives \(P_A=H(z^h-\delta)^2\).
This last condition is a sufficient scalar-product control, not a claimed characterization for arbitrary unbalanced lists.

<a id="balanced-word"></a>
## Reduction of a balanced cyclic word

For the remainder put \(t=z+z^{-1}\), and define
\[
 K(t)=\begin{pmatrix}0&2-t\\2+t&0\end{pmatrix},\qquad
 J(t)=\begin{pmatrix}0&2-t\\-(2+t)&0\end{pmatrix}.
\]
Direct multiplication gives
\[
 K^2=(4-t^2)I,\quad J^2=(t^2-4)I,\quad JK=-KJ,
 \quad(2I+K)(2I-K)=t^2I.                                  \tag{13}
\]
The four sign pairs give respectively
\[
 N_{++}=2I+K,\quad N_{--}=2I-K,\quad N_{+-}=J,\quad N_{-+}=-J.
\]
The two sign-sum equations first imply \(n_{++}=n_{--}\) and \(n_{+-}=n_{-+}\), proving the stated counts \(a,b\).
There are \(2b\) factors \(J\), and the \(b\) negative signs in \(-J\) give an overall scalar \((-1)^b\).
Move every \(J\) to the left of the factors \(2I\pm K\), using (13).
Crossing one \(J\) reverses the sign of \(K\) in such a factor, without another scalar sign.
Consequently, for some nonnegative \(p,q\) with \(p+q=2a\),
\[
 N_k\cdots N_1
 =(-1)^bJ^{2b}(2I+K)^p(2I-K)^q
 =(4-t^2)^b(2I+K)^p(2I-K)^q.                             \tag{14}
\]
In the product \(N_k\cdots N_1\), the factors to the right of \(N_j\) are precisely the preceding active edges in the chosen cyclic order.
Thus the sign of \(K\) remaining in its \(s_j=1\) factor is \(\epsilon_j(-1)^{r_j}\), and (2) equals \(|p-q|/2\).
This proves integrality and \(c\le a\).
Moving the cyclic starting point changes all these effective signs by one common sign: the total number \(2b\) of opposite-sign edges is even.
Therefore \(c\) does not depend on that starting point.

Pairing \(2I+K\) and \(2I-K\) in (14), and using that the traces of their equal powers agree, gives
\[
 \operatorname{tr}(N_k\cdots N_1)
 =(4-t^2)^b t^{2a-2c}\operatorname{tr}(2I+K)^{2c}.        \tag{15}
\]
Here equality of those traces follows by expanding and observing that the odd powers of the off-diagonal matrix \(K\) have trace zero.
This also proves (15) when \(p<q\), without choosing a diagonalization.

Writing \(w=z-z^{-1}\), one has \(4-t^2=-w^2\), and expansion of the same even powers yields
\[
 \operatorname{tr}(2I+K)^{2c}=(2+iw)^{2c}+(2-iw)^{2c}.
\]
The elementary identities
\[
 2+iw=iz^{-1}(z-i)^2,\qquad
 2-iw=-iz^{-1}(z+i)^2
\]
turn (15) into
\[
 \operatorname{tr}(N_k\cdots N_1)
 =\tau z^{-k}(z^2+1)^{2a-2c}(z^2-1)^{2b}
 \bigl((z-i)^{4c}+(z+i)^{4c}\bigr).                        \tag{16}
\]
Since \(F_j=zN_j\), (1) equivalently has its trace term \(z^g\operatorname{tr}(N_k\cdots N_1)\).
Substituting (16), with \(\sigma=1\), factors its remaining bracket as
\[
 (z^2+1)^{2c}(z^{2h}+1)
 -\tau z^h\bigl((z-i)^{4c}+(z+i)^{4c}\bigr)
 =G(z)\overline G(z).
\]
This proves (3), again first as a Laurent identity at \(z\ne0\) and then as a polynomial identity everywhere.
The prefactor has degree \(2k-4c\), while the two monic factors have total degree \(2h+4c\), so no degree or roots have been omitted.
The constant term of \(G\) is \((-1)^{b+1}\), and \(G\overline G\) has ordinary integer coefficients because it is a real polynomial with Gaussian integer coefficients.

<a id="whole-measure-gap"></a>
## Complete Mahler bound, including boundary zeros

For \(c=0\), (3) is exactly the displayed cyclotomic formula in the statement.
Suppose \(c\ge1\), write \(z=e^{i\theta}\), and put \(u=|\sin\theta|\).
The reverse triangle inequality gives
\[
 \begin{aligned}
 |G(e^{i\theta})|
 &\ge\left|(2+2\sin\theta)^c-(2-2\sin\theta)^c\right|\\
 &=2^c\bigl((1+u)^c-(1-u)^c\bigr)\\
 &=2^{c+1}\sum_{\substack{1\le j\le c\\j\ {\rm odd}}}\binom cj u^j
 \ge c2^{c+1}|\sin\theta|.
 \end{aligned}                                             \tag{17}
\]
The phase \(z^h\) and the sign \(\tau\) do not affect this estimate.
The logarithm of a nonzero polynomial is integrable on the circle, and the Jensen identity used here permits unit-circle roots; these are precisely the conventions retained in [Den09-U001](../audits/literature/Den09/Yin_U001.md#mahler-measure).
Applying that identity to \(1-z^2\) gives \(m(1-z^2)=0\).
Since \(|1-e^{2i\theta}|=2|\sin\theta|\), it also gives
\[
 \frac1{2\pi}\int_0^{2\pi}\log|\sin\theta|\,d\theta=-\log2.
\]
Thus no separate singular-integral formula or unverified limiting argument is needed.
Taking logarithms of (17) away from the two sine zeros, integrating the integrable functions, and using Jensen gives
\[
 m(G)\ge\log(c2^{c+1})-\log2=\log c+c\log2.
\]
Coefficient conjugation preserves Mahler measure, and all factors \(z^2\pm1\) have measure one.
Logarithmic Mahler measure is additive under polynomial products, directly from the integral definition or the full root-product formula.
Consequently \(m(P_A)=2m(G)\), proving (4) for the entire characteristic polynomial, rather than for a selected factor or exterior root.

<a id="exceptional-roots"></a>
## Unit-circle roots and their exact multiplicities

For \(c\ge1\), (17) shows that \(G\) has no unit-circle zero except possibly \(1\) and \(-1\).
Direct evaluation gives
\[
 G(1)=0\ \Longleftrightarrow\ b\ {\rm is\ even},\qquad
 G(-1)=0\ \Longleftrightarrow\ h\equiv b\pmod2.
\]
At either such zero, the two terms of \(G\) are nonzero and equal.
Their logarithmic-derivative difference is
\[
 \frac h z+\frac{2c}{z+i}-\frac{2c}{z-i}
 =\frac h z-\frac{4ci}{z^2+1}.
\]
At \(z=1\) and \(z=-1\) these values are \(h-2ci\) and \(-h-2ci\), respectively, and neither vanishes.
The possible roots are therefore simple in \(G\), and also simple in \(\overline G\).
Moreover \(G(i)=i^h(2i)^{2c}\ne0\) and \(G(-i)=-\tau(-2i)^{2c}\ne0\).
Formula (3) consequently gives the exact multiplicities
\[
 \begin{array}{c|c}
 \text{root}&\text{multiplicity in }P_A\\\hline
 1&2b+2\mathbf1_{\{b\ {\rm even}\}}\\
 -1&2b+2\mathbf1_{\{h\equiv b\ (2)\}}\\
 i,-i&2a-2c\quad\text{at each root}.
 \end{array}                                               \tag{18}
\]
There are no other unit-circle roots in this case.
Reciprocity then gives exactly
\[
 N_+(A)=h+2c-\mathbf1_{\{b\ {\rm even}\}}
                 -\mathbf1_{\{h\equiv b\ (2)\}}
\]
exterior roots, counted with multiplicity.
For \(c=0\), all multiplicities are instead given directly by the full binomial product in the statement, including any overlap of its factors.

<a id="placement-and-limit"></a>
## What gap placement can and cannot change

At fixed \(g\) and a fixed cyclic sequence of signed edges, arbitrary redistribution of the \(g-2k\) neutral sites leaves the whole polynomial unchanged.
For balanced inputs with fixed \(g,a,b\), the value \(c\) controls the full polynomial through (3).
The order can matter: take \(g=8\), \(I=\{1,3,5,7\}\), and assign the sign pairs in that cyclic order.
The list
\[
 (++),(--),(+-),(-+)
\]
has \(a=b=1,c=0\), while
\[
 (++),(+-),(--),(-+)
\]
has \(a=b=c=1\).
Both are actual balanced elementary outcomes of the original law.
The first has complete measure one, and the second has complete measure at least four.
For the latter, (3) gives explicitly
\[
 P_A(z)=(z^2-1)^2
 (z^{12}+2z^{10}-z^8+12z^6-z^4+2z^2+1).
\]
These are direct consequences of the proved formulas, not outputs of a numerical sweep or an independent computational certificate.

Increasing \(g\) at fixed word changes \(h\), so it need not preserve the nonneutral polynomial or act only by substitution in one fixed polynomial.
For example, the latter four-edge word at \(g=9\) has
\[
 G\overline G=(z^2+1)^2(z^{10}+1)-2z^5(z^4-6z^2+1).
\]
By (18) its only unit-circle factor is \((z+1)^2\).
After removing it, the degree-twelve nonneutral polynomial has leading terms \(z^{12}-2z^{11}+\cdots\), whereas the degree-twelve nonneutral polynomial at \(g=8\) displayed above is even.
Thus even this length change produces distinct nonneutral cores, with no proper power substitution between the two degree-twelve polynomials.
No equality or inequality between their particular measures is needed for this comparison.

Regardless of such core changes, (4) is uniform in \(g,k\), the gaps and the word.
Therefore a law supported on these balanced disjoint-edge inputs gives zero probability to every strict shell \(1<M<4\).
This removes the entire disjoint-edge dilution mechanism from a shrinking-complete-measure construction.
An overlapping-edge input has \(DE\) potentially nonzero and does not satisfy the local equations (5); the argument supplies no gap theorem for that remaining part of the original law.

## Assessment history

### Decision balanced-disjoint-edge-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T09:32 |
| status | proved |
| reason | Complete independent review verifies the exact full transfer determinant, every disjoint sign pattern, the balanced cyclic invariant, Gaussian norm factorization, all root multiplicities and the uniform complete-measure alternative M=1 or M>=c^2 4^c>=4. Overlapping edges remain outside the theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact transfer and gap statements](#statement) | Every allowed total length and disjoint signed edge set, full polynomial identity, balanced invariant, exact cyclotomic case and complete-measure lower bound. |
| argument | [Local transfer and determinant](#local-transfer) | Original matrix orientation, all pivots and scalar factors, full degree, exceptional spectral parameters and reciprocal normalization. |
| argument | [One-edge and two-edge controls](#one-two-edges) | All listed sign cases, balanced two-edge neutrality, ordered composition and gap-placement criterion. |
| argument | [Balanced-word reduction](#balanced-word) | All parity and sign counts, cyclic invariance of c, exact Gaussian norm, coefficients, degrees and constants. |
| argument | [Whole-measure bound](#whole-measure-gap) | Reverse triangle and binomial bounds, accepted Jensen interface with boundary zeros, full norm cost and strict-shell exclusion. |
| argument | [Exact unit roots](#exceptional-roots) | Every unit-circle root and multiplicity, possible endpoint simplicity and complete exterior-root count. |
| argument | [Placement and length consequences](#placement-and-limit) | Exact order and length controls, differing noncyclotomic residuals, complete probability conclusion and overlapping-edge boundary. |
| dependency | [Scalar analytic source](../audits/literature/Den09/Yin_U001.md#den09-u001) | Only the retained one-variable logarithmic integrability and Jensen/root-product identity with unit-circle zeros; original foundational proofs are not newly audited. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1115_v1.md#balanced-disjoint-edge-transfer-review) | Entire fixed contribution, actual source and model interfaces, all special cases, full multiplicities, parameter ranges and research limits. |

## Current assessment

[Selected decision](#decision-balanced-disjoint-edge-gap)

