---
author: Yin
---

# A uniform whole-measure gap for two cyclic Eichler transvections

<a id="statement"></a>
## Statement and exact family

Let \(g\ge1\), let \(R_g\) cyclically permute the standard basis of \(\mathbb Z^g\), and extend it by the identity on the hyperbolic plane \(U=\mathbb Ze\oplus\mathbb Zf\).
The lattice \(\Lambda=\mathbb Z^g\oplus U\) has the standard positive dot product on \(\mathbb Z^g\), with
\[
(e,e)=(f,f)=0,\qquad(e,f)=1,
\]
and the two summands are orthogonal.
For \(v,w\in\mathbb Z^g\) with even squared norms, including the zero vector, define
\[
T_{e,v}(x)=x-(v,x)e+(e,x)v-\tfrac12(v,v)(e,x)e,
\qquad
A=R_gT_{e,v}T_{f,w}.
\]
Put \(P_A(z)=\det(zI-A)\), and let \(m(P_A)=\log M(P_A)\) be its complete logarithmic Mahler measure, with every root and multiplicity included.

There is an absolute constant \(\eta>0\), independent of \(g,v,w\), such that
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta.                 \tag{1}
\]
More concretely, writing \(s=\|v\|\|w\|\), one has
\[
s\ge650\quad\Longrightarrow\quad M(P_A)>2.                \tag{2}
\]
If \(v=0\) or \(w=0\), then
\[
P_A(z)=(z^g-1)(z-1)^2,\qquad M(P_A)=1.                   \tag{3}
\]
If \(v,w\ne0\) and \(M(P_A)\le2\), their numbers of nonzero coordinates are at most
\[
B=211250.
\]
In that case \((z^g-1)P_A(z)\) has at most
\[
K=(B^2+4)^2+(B^2+2)^2                                  \tag{4}
\]
nonzero terms and the same complete measure as \(P_A\).

This covers arbitrary integer entries and support in the displayed two-transvection family, without a degree bound or a prescribed correlation between \(v\) and \(w\).
It does not cover additional transvections, a growing negative index or arbitrary integral lattice isometries.
The constant supplied by the fixed-support theorem is not effective here, so (1) does not exclude every value below \(6/5\).

<a id="argument"></a>
## Argument and inputs

The integral-isometry identity and exterior determinant were developed in [L462 v13](../ledger/Yin_L_G0462_v13.md#integer-generators), with [its independent review](../audits/reviews/Yin_R_G1114_v1.md#orthogonal-whole-review).
The Eichler formula is attributed there to GHS13, arXiv v2, Section 8.3, equation (49); its different modular-group hypotheses are not used.
The proof below derives the full polynomial identity and a uniform estimate allowing all vector pairs, instead of the earlier disjoint-support family.
Its only non-elementary input is the [accepted univariate consequence of DS17 Theorem 2](../audits/literature/DS17/Yin_U001.md#ds17-u001): for each fixed \(K\), positive complete logarithmic measures of nonzero integer polynomials with at most \(K\) nonzero terms have a positive lower bound \(\eta_K\).
That source is used at its recorded statement and applicability depth, without a new audit of its foundational proofs.

### Exact characteristic polynomial identity

The displayed transvections preserve the lattice pairing and have inverses \(T_{e,-v}\) and \(T_{f,-w}\).
For example, with \(s_x=(e,x)\), \(t_x=(v,x)\), \(a=\|v\|^2/2\), the change in a pairing is
\[
s_xt_y+s_yt_x-(t_x+as_x)s_y-(t_y+as_y)s_x
       +2as_xs_y=0.
\]
Even squared norms make their coefficients integral.
Thus \(A\) is an invertible integer matrix and \(P_A\) is a nonzero monic integer polynomial.

Write
\[
a=\|v\|^2/2,\quad b=\|w\|^2/2,\quad c=v^{\mathsf T}w,
\quad q(z)=z^g-1,\quad K_R(z)=(zI-R_g)^{-1}R_g.
\]
For \(z>1\), define
\[
V=v^{\mathsf T}K_Rv,\quad W=w^{\mathsf T}K_Rw,\quad
X=v^{\mathsf T}K_Rw,\quad Y=w^{\mathsf T}K_Rv.
\]
Then
\[
P_A(z)=q(z)D(z),\qquad
D(z)=
\det\begin{pmatrix}
z-1+c+X&z(a+V)\\
b+W&z-1+zY
\end{pmatrix}.                                          \tag{5}
\]

For an exact determinant verification, write a vector as \(x+\alpha e+\beta f\).
After the first transvection \(T_{f,w}\), its last coordinate is
\(\beta'=\beta-w^{\mathsf T}x-b\alpha\).
In the rows of \(zI-A\), add the appropriate multiples of the last row to replace \(\beta'\) by \(z\beta\); explicitly subtract \(R_gv\) times that row from the positive-coordinate rows and add \(a\) times it to the \(e\)-coordinate row.
These determinant-preserving operations produce
\[
\begin{pmatrix}
zI-R_g&-R_gw&-zR_gv\\
v^{\mathsf T}&z-1+c&az\\
w^{\mathsf T}&b&z-1
\end{pmatrix}.
\]
Taking its Schur complement proves (5), since \(\det(zI-R_g)=q(z)\).
This establishes an identity of rational functions and hence the polynomial identity after clearing denominators; it is not merely an exterior-root correspondence.
If either vector vanishes, (5) immediately yields (3).

### A uniform negative determinant at two

The following calculation uses only that \(R_g\) is real orthogonal.
Fix real \(z>1\), and set
\[
u=(zI-R_g)^{-1}v,\qquad t=(zI-R_g)^{-1}w,
\quad h=u^{\mathsf T}t,\quad k=t^{\mathsf T}R_gu,
\quad E=\|u\|\|t\|.
\]
Direct expansion of \(v=(zI-R_g)u\) gives
\[
a+V=\frac{z^2-1}{2}\|u\|^2,\qquad
b+W=\frac{z^2-1}{2}\|t\|^2,
\]
and
\[
c+X=z(zh-k),\qquad Y=zk-h.
\]
Both \(|h|\) and \(|k|\) are at most \(E\).
Putting \(r=(h+k)/2\) and \(d=(h-k)/2\) therefore gives
\[
\begin{aligned}
(c+X)Y
 &=z\bigl((z-1)^2r^2-(z+1)^2d^2\bigr)\\
 &\le z(z-1)^2E^2.
\end{aligned}
\]
Consequently
\[
(c+X)Y-(a+V)(b+W)
 \le-\frac{(z-1)^4}{4}E^2
 \le-\frac{(z-1)^4}{4(z+1)^4}\|v\|^2\|w\|^2,            \tag{6}
\]
where the second inequality uses
\(\|(zI-R_g)u\|\le(z+1)\|u\|\) and the corresponding inequality for \(t\).

At \(z=2\), the convergent geometric resolvent or the reverse triangle inequality gives
\[
\|K_R(2)\|\le1,\qquad \|I+K_R(2)\|\le2.
\]
Thus \(|Y|\le s\) and \(|c+X|\le2s\).
Expanding (5) and applying (6) gives
\[
D(2)=1+(c+X)+2Y+2\bigl((c+X)Y-(a+V)(b+W)\bigr)
 \le1+4s-\frac{s^2}{162}.                               \tag{7}
\]
The final expression is decreasing for \(s\ge650\) and equals \(-569/81<0\) at \(s=650\).
For every fixed input, \(D(z)\) is continuous on \(z>1\) and \(D(z)=z^2+O(z)\) as \(z\to+\infty\).
Therefore \(D\) has a real zero greater than two when \(s\ge650\).
Equation (5) makes this a root of the complete \(P_A\).
All remaining factors in its Mahler product are at least one, proving (2) without discarding other exterior roots.

### Bounded vectors give a bounded-support cyclotomic multiple

Now suppose \(M(P_A)\le2\) and both vectors are nonzero.
By (2), \(s<650\).
Their positive even squared norms satisfy
\[
\|v\|^2\|w\|^2<422500,\qquad
\|v\|^2,\|w\|^2<211250.
\]
Every nonzero integer coordinate contributes at least one to its squared norm.
Hence both support sizes are at most the fixed \(B\) in (4).

For any integer vectors \(r,t\), define the correlation polynomial
\[
U_{r,t}(z)=\sum_{j=1}^{g}z^{g-j}r^{\mathsf T}R_g^jt.
\]
The identity
\[
q(z)K_R(z)=\sum_{j=1}^{g}z^{g-j}R_g^j
\]
follows by multiplication by \(zI-R_g\) and \(R_g^g=I\).
If the support sizes of \(r,t\) are \(b_r,b_t\), then \(U_{r,t}\) has at most \(b_rb_t\) nonzero terms.
Indeed, each ordered pair of occupied coordinates contributes at exactly one cyclic lag \(j\in\{1,\ldots,g\}\); collisions and cancellations can only reduce that count.

Using \(qP_A=q^2D\) in (5) now gives the exact identity
\[
\begin{aligned}
qP_A
={}&\bigl((z-1+c)q+U_{v,w}\bigr)
       \bigl((z-1)q+zU_{w,v}\bigr)\\
 &-z\bigl(aq+U_{v,v}\bigr)\bigl(bq+U_{w,w}\bigr).         \tag{8}
\end{aligned}
\]
The first two factors have at most \(4+B^2\) terms each, and the last two have at most \(2+B^2\) terms each.
The sum of the two product bounds is exactly (4).
The polynomial \(qP_A\) is nonzero and integral, and \(M(q)=1\), so
\[
m(qP_A)=m(P_A).
\]
The accepted fixed-support theorem applies to this whole polynomial, with no restriction on degree or coefficient height.

If \(m(P_A)>0\) and \(M(P_A)\le2\), it follows that \(m(P_A)\ge\eta_K\).
If \(M(P_A)>2\), then \(m(P_A)>\log2\).
Taking \(\eta=\min(\eta_K,\log2)>0\) proves (1), including all vector and degree choices in the stated family.

<a id="research-scope"></a>
## Consequence for the construction

The earlier [fixed disjoint-support test](../ledger/Yin_L_G0462_v13.md#first-family-obstruction) ruled out one explicit scaling.
The new determinant estimate does not use its disjoint support, signs, order of vanishing, parity of \(g\), or chosen relation between \(g\) and the vector norms.
It rules out a positive-to-one sequence throughout the displayed cyclic two-transvection family, even with growing support and arbitrarily large entries.
No classification as a canonical Coxeter word is needed for this conclusion.

The result leaves other integral-isometry constructions and the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) unresolved.
It gives no effective numerical gap at \(6/5\), and says nothing about a family with an unbounded number of transvections.
The [independent whole-argument finding](../audits/reviews/Yin_R_G1114_v2.md#cyclic-two-transvection-gap-review) verifies the exact family, full polynomial identity, uniform estimate, support reduction and source applicability.

## Assessment history

### Decision cyclic-two-transvection-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T00:44 |
| status | proved |
| reason | The complete independent review found no gap in the uniform exterior estimate, full characteristic-polynomial identity or measure-preserving fixed-support reduction for the entire stated family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact cyclic two-transvection family](#statement) | An absolute positive total-logarithmic gap for all degrees and all even-norm integer vector pairs, with the stated explicit norm threshold and support bound. |
| argument | [Complete argument](#argument) | Full determinant normalization, uniform negative determinant at two, zero cases, bounded cyclic correlations and the complete-measure reduction. |
| dependency | [Accepted DS17 fixed-support theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Positive total logarithmic measures of nonzero integer polynomials with at most the fixed K terms have a positive lower bound; the source's original foundational proofs are not newly audited. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1114_v2.md#cyclic-two-transvection-gap-review) | Exact statement, whole argument, actual source interface and all unbounded-parameter and scope qualifications. |

## Current assessment

[Selected decision](#decision-cyclic-two-transvection-gap)
