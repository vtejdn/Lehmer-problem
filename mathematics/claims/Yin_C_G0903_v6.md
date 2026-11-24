---
author: Yin
---

# A uniform Mahler gap for six-term two-row graphs of width at most twice the seed degree

2026-11-24T18:45 UTC.

<a id="statement"></a>
## An exponential lower bound for all three row splits

Let \(p\ge3\) be an integer, and let \(F=A(X^p)+XC(X^p)\) have six occupied terms, with nonzero integral rows \(A,C\) of degrees at most \(b\).
Suppose the rows are coprime over \(\mathbb Q[Y]\) and \(A(Y)A(Y^{-1})-C(Y)C(Y^{-1})\ne0\).
Let a reciprocal monic irreducible polynomial of degree \(d\) divide \(F\) at least twice, and let \(\alpha\) be a nontorsion unit root of this factor.
Write \(g\) for the gcd of the differences of the six occupied exponents, put \(\beta=\alpha^g\), \(e=[\mathbb Q(\beta):\mathbb Q]\), and let \(m\) denote total logarithmic Mahler measure.
At least one of the following holds:

1. Some nonzero power of \(\alpha\) has degree at most 25.
2. The support of \(F\) is invariant under reflection and \(m(\alpha)\ge(\log2)/24\).
3. One has \(e\le100\lceil2\sqrt{b/g}\rceil\).

In particular, whenever \(b\le2d\), one has
\[
               m(\alpha)\ \ge\ \frac{\log2}{720000},\qquad
               \max(\|A\|_1,\|C\|_1)\ \ge\ 2^{p/720000}.                 \tag{1}
\]
This includes the row splits \(1+5,\ 2+4,\ 3+3\) in either order, with arbitrary coefficient sizes and exponent-difference gcd.
Only the \(3+3\) split permits the reflection in the second alternative.
The [five-term bound](Yin_C_G0903_v2.md#statement) covers smaller supports.
Thus any sequence of [ordinary graphs of near-degree width](Yin_C_G0901_v5.md#short) with normalized log heights tending to zero must eventually use at least seven terms, uniformly over \(p\ge3\).

<a id="pencil"></a>
## The six roots over the parameter line

Let \(a_i\), \(0\le i\le5\), be the six exponents with coefficients \(c_i\ne0\), and put \(B_i=(a_i-a_0)/g\).
Thus \(B_0=0\) and the \(B_i\) have gcd one.
Use projective coordinates \(z_0,\ldots,z_5\), and work first on the torus where all are nonzero, normalizing \(z_0=1\).
For \(j=0,1\) impose \(\sum_i B_i^j c_i z_i=0\) and \(\sum_i B_i^j c_i/z_i=0\), with zeroth weights all one.
The point \(y_i=\beta^{B_i}\) satisfies them by double contact at \(\alpha,\alpha^{-1}\).
The forward equations are linear, and the inverse equations have degree five after multiplication by \(\prod_i z_i\).
Bézout's inequality gives a bound \(1\cdot1\cdot5\cdot5=25\) for the sum of degrees of the geometric components of the torus intersection, measured on their projective closures.
One can intersect successively, retaining a component when it is contained in the next hypersurface and bounding the total degree of its sections otherwise.

Recall the [cubic interpolation](Yin_C_G0903_v4.md#curve).
Put \(D(x)=\prod_i(x-B_i)\), and let \(S_0\in\mathbb Q[x]\) of degree at most five take values \((c_iD'(B_i))^2\) at the six nodes.
At any point of the intersection there are polynomials \(Q_+,Q_-\) of degrees at most three with values \(Q_\pm(B_i)=c_iD'(B_i)z_i^{\pm1}\).
Consequently \(Q_+Q_-=S_0+\lambda D\), where \(\lambda\) is the coefficient of \(x^6\) in the product.
This regular parameter has finite fibers, since there are finitely many monic divisors of each nonzero product and \(Q_+(B_0)=c_0D'(0)\) fixes the scale of the chosen divisor.
Thus each positive-dimensional component \(V\) is a curve on which \(\lambda\) is nonconstant.
If \(y\) belongs to a zero-dimensional component, its rational conjugates give \(e=[\mathbb Q(y):\mathbb Q]\le25\), as the \(B_i\) generate \(\mathbb Z\).
Otherwise choose a curve component \(V\) through \(y\).

Over the function field of \(V\) the two interpolants have degree three because \(\lambda\) is nonconstant.
Pass to a finite extension splitting \(S_0+\lambda D\), and use its smooth projective curve over \(\overline{\mathbb Q}\).
For three roots \(s_1,s_2,s_3\) comprising the factor \(Q_+\), with its leading coefficient canceled, one has
\[
 \frac{z_i}{z_j}=\frac{c_jD'(B_j)}{c_iD'(B_i)}
                 \prod_{\nu=1}^3\frac{B_i-s_\nu}{B_j-s_\nu}.
\]
At any place where \(\lambda\) is finite, a finite limit of a root cannot equal any \(B_i\), since \(S_0(B_i)\ne0\).
A root tending to infinity contributes a ratio tending to one.
Thus every coordinate ratio has neither a zero nor a pole over the finite parameter line.

At \(\lambda=\infty\), write \(u=1/\lambda\).
The polynomial \(D+uS_0\) has six simple roots at \(u=0\), and the branch tending to \(B_j\) is
\[
                        B_j-uS_0(B_j)/D'(B_j)+O(u^2).
\]
Its linear coefficient is nonzero.
At each place above infinity the three roots of \(Q_+\) therefore select three distinct nodes, with label set \(I\).
For an integral vector \(v\) of coordinate sum zero the character \(z^v=\prod_i z_i^{v_i}\) has order
\(\operatorname{ord}(u)\sum_{i\in I}v_i\) there.
The ratios above already account for all places.
A rational function on the smooth complete curve with zero divisor is constant, and constancy after field extension is equivalent to constancy on \(V\).
It follows that the lattice \(\Lambda\) of constant characters on \(V\) is exactly
\[
     \left\{v\in\mathbb Z^6:\ \sum_i v_i=0,\quad
           \sum_{i\in I}v_i=0\text{ for every triple occurring above infinity}\right\}.       \tag{2}
\]

<a id="cube"></a>
## Rank two forces reflection of the entire support

The field of definition of \(V\) has degree at most 25 since its conjugates are geometric components of the rational intersection.
For \(v\in\Lambda\) the constant \(z^v\) lies in that field, by invariance under the stabilizer of \(V\).
Its value at \(y\) is \(\beta^{\sum_i v_iB_i}\).
If this exponent is nonzero for any such \(v\), the first alternative follows.
We may henceforth assume \(B=(B_i)_i\) is orthogonal to \(\Lambda\).

Write \(l=\operatorname{rank}\Lambda\).
Center each incidence row from (2) by writing \(s_I=2\mathbf 1_I-\mathbf1\), which has three entries of each sign.
The span of these rows in the space of vectors of sum zero has dimension \(5-l\).
Choose a basis of \(5-l\) rows from the occurring triples.
The six columns of this matrix must be distinct, since equality of columns \(i,j\) would give the constant character \(z_i/z_j\), and hence \(B_i=B_j\).
There are only \(2^{5-l}\) possible sign columns, so \(l\le2\).

When \(l=2\), six distinct vertices of the three-dimensional sign cube occur.
The two omitted vertices are opposites, since each row contains three entries of each sign whereas the full cube contains four of each.
The remaining six vertices thus form three opposite pairs.
By (2) and orthogonality, \(B\) is a linear combination of \(\mathbf1\) and these three sign rows.
The sum of \(B_i,B_j\) over either member and its opposite is twice the coefficient of \(\mathbf1\), the same for all three pairs.
The original six exponents \(a_i\) are therefore paired by a single reflection.

For \(p\ge3\) such a reflection must interchange the two occupied residues \(0,1\bmod p\), since fixing them both would make the reflection sum congruent both to zero and to two modulo \(p\).
Hence both rows have three terms.
Proportionality of \(F\) with its reflection would interchange the two rows up to sign, reversal and translation, forcing their products with their inverses to agree.
The nonzero reflected determinant excludes this, so the [six-term reflection estimate](Yin_C_G0903_v3.md#statement) gives the second alternative.

<a id="within"></a>
## Intersecting with a character from within the rows

It remains to treat \(l\le1\).
Let \(i_h\) index the least exponent in residue \(h\) for \(h=0,1\).
For each of the four other indices \(i\) in its row \(h\), take \(v_i=\mathbf e_i-\mathbf e_{i_h}\).
These four vectors are independent.
Both residues occur, so \(\gcd(g,p)=1\).
Writing \(a_i=h+pj_i\), we see that
\[
       B\cdot v_i/p=(j_i-j_{i_h})/g
\]
is an integer in \([0,b/g]\).
In particular \(b/g\ge1\), since one row contains at least two distinct exponents.

Set \(T=\lceil2\sqrt{b/g}\rceil\).
The \((T+1)^4\) vectors \(v=\sum_i k_i v_i,\quad 0\le k_i\le T\), have at most \(4(b/g)T+1\) distinct integer values of \(B\cdot v/p\).
As \((T+1)^3>4(b/g)T+1\), some fiber contains more than \(T+1\) vectors.
Its intersection with any single coset of \(\Lambda\) has at most \(T+1\) vectors.
Indeed a nontrivial affine line in their four-dimensional span has some coefficient coordinate that is injective on it.
Thus the difference \(v\) of two vectors in the fiber has \(B\cdot v=0\) and \(v\notin\Lambda\).
The equation \(z^v=1\) passes through \(y\) and is nonconstant on \(V\).
In homogeneous coordinates, clearing negative powers gives a binomial of degree at most \(4T\), since each of the four difference coefficients has absolute value at most \(T\) and each \(v_i\) has total positive part one.
The same rational binomial cuts every conjugate of \(V\) in finitely many points.
Their total degree is at most 25, so Bézout gives
\[
                      e\le 100T\le 300\sqrt{b/g}.
\]

If \(b\le2d\), then \(d\le ge\) by adjoining a root of \(X^g-\beta\), whence \(e\le300\sqrt{2e}\) and \(e\le180000\) in this third case.
In the first case an actual power has degree at most 25.
The [power-field norm and house bound](Yin_C_G0903_v2.md#interpolation) give \(m(\alpha)\ge(\log2)/(4D)\) whenever a nonzero power has degree \(D\).
Combining these estimates with the reflection case yields the measure bound in (1).
Finally the [ordinary two-row determinant estimate](Yin_C_G0345_v408.md#lower) gives \(\log\max(\|A\|_1,\|C\|_1)\ge p\,m(\alpha)\), completing the proof.

<a id="multiplicity"></a>
## The same gap at the first support size beyond finite interpolation

Fix an integer \(r\ge2\) and a real \(K\ge1\).
Under the same hypotheses on the two rows and the reciprocal unit factor, assume multiplicity at least \(r\), row width \(b\le Kd\), and at most \(k=2r+2\) occupied terms.
Then there exists \(c(r,K)>0\) such that \(m(\alpha)\ge c(r,K)\) and \(\log\max(\|A\|_1,\|C\|_1)\ge p c(r,K)\) for every \(p\ge3\).
We give explicit constants in the argument.

At at most \(2r+1\) terms the [finite interpolation and norm estimate](Yin_C_G0903_v2.md#statement) gives \(m(\alpha)\ge(\log2)/(4\binom{2r}{r})\) whenever contact is possible.
For exactly \(k=2r+2\) terms repeat the [higher-multiplicity equations](Yin_C_G0903_v4.md#multiplicity) in projective dimension \(k-1\).
There are \(r\) linear Euler equations and \(r\) inverse Euler equations of degree \(k-1\) after clearing denominators, with orders \(0,\ldots,r-1\) in both sets.
Thus we may take \(D_r=(k-1)^r\) for the sum of the degrees of the components of the intersection.
The [dual Vandermonde interpolation](Yin_C_G0903_v2.md#interpolation) gives \(Q_\pm\) of degrees at most \(r+1\).
Their product takes the \(k\) prescribed nonzero squares at the distinct nodes \(B_i\).
As \(2(r+1)=k\), the product is \(S_0+\lambda D\), where \(\deg S_0<k\), \(D(x)=\prod_i(x-B_i)\), and \(S_0,D\) are coprime.
Again the scale is fixed at the pivot, and all fibers are finite.
The degree of the field of definition of a curve component is at most \(D_r\).
The isolated and nontrivial constant-character cases give a power degree of at most \(D_r\), exactly as above.

In the remaining case put \(s=k-1-\operatorname{rank}\Lambda\), with \(\Lambda\) the lattice of constant characters of sum zero on the chosen component.
The proof of (2) applies to \(r+1\) selected roots instead of three.
At every place over finite \(\lambda\) the coordinate ratios have zero order.
At every place over infinity each of the \(k\) branches of roots has a distinct limiting node, and exactly \(r+1\) of the nodes belong to \(Q_+\).
Thus the centered sign rows span dimension \(s\), each row has equally many entries of each sign, and the \(k\) columns of a basis are distinct.
If \(s\le3\), at most eight labels can occur.
The case \(k=6\) gives the opposite pairs proved above, while for \(k=8\) all vertices of the three-dimensional sign cube occur.
In either case \(B\) is a constant vector plus a linear combination of the sign rows, so the pairs of opposite vertices again give a reflection of the exponent support.
For \(k>8\) the case \(s\le3\) is impossible.

For reflection-invariant support, the rows must interchange at \(p\ge3\), and nonzero reflected determinant again excludes proportionality.
The polynomial \(F\) and its reflected polynomial \(X^{\min a_i+\max a_i}F(X^{-1})\) both have the prescribed contacts to order at least \(r\).
Take a rational linear combination canceling one occupied coefficient.
It is nonzero by nonproportionality and has at most \(2r+1\) occupied terms, so the finite interpolation bound applies directly to \(\alpha\).

Finally suppose \(s\ge4\).
There are \(h=k-2\) independent within-row differences, giving at most \(h(b/g)T+1\) values of \(B\cdot v/p\) on the corresponding coefficient box \(\{0,\ldots,T\}^h\).
A single coset of \(\Lambda\) contains at most \((T+1)^{k-1-s}\) points in this box, by projection of its intersection with the span of these differences onto suitable coefficient axes.
Since \(h-(k-1-s)=s-1\ge3\), taking \(T=\lceil\sqrt{h b/g}\rceil\) gives a fiber that is larger.
The resulting nonconstant character cuts the curve and its rational conjugates in degree at most \(hT D_r\).
As \(1\le b/g\le Ke\), we obtain
\[
           e\le hD_r(\sqrt h+1)\sqrt{Ke},\qquad
           e\le K h^2D_r^2(\sqrt h+1)^2 .
\]
Hence one may take \(c(r,K)\) to be \((\log2)/4\) divided by the maximum of \(\binom{2r}{r},D_r,K h^2D_r^2(\sqrt h+1)^2\).
The norm descent and the ordinary determinant estimate apply in the same way as at multiplicity two.

## Assessment history

### Decision six-term-near-degree-gap

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:52 |
| status | proved |
| reason | The balanced subsets control constant characters. A within-row exponent relation cuts the remaining components, bounding a power degree at near-degree width. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The six-term alternatives and uniform positive gaps for integer exponents at least three and row width at most twice the seed degree, including the stated higher-multiplicity extension. |
| argument | [pencil](#pencil) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [cube](#cube) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [within](#within) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [multiplicity](#multiplicity) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0903_v4.md#curve) | The cubic interpolation pencil. |
| dependency | [Input](Yin_C_G0903_v2.md#statement) | The smaller-support degree and measure estimates. |
| dependency | [Input](Yin_C_G0903_v3.md#statement) | The reflection estimate. |
| dependency | [Input](Yin_C_G0345_v408.md#lower) | The individual height lower bound. |
| dependency | [Input](Yin_C_G0901_v5.md#short) | Near-degree witnesses on a shrinking sequence. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1054.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-six-term-near-degree-gap)
