---
author: Yin
---

# Sparse two-row polynomials with a double zero at one nontorsion point

2026-11-24T18:00 UTC.

<a id="statement"></a>
## A bound for a minimal subsum at a double root

Fix \(m\ge3\) and a rational \(\varepsilon>0\).
Let \(G(X)=A(X^p)+XC(X^p)\) for two nonzero integral polynomials and an integer \(p\ge2\).
Suppose the graph has at most \(m\) occupied terms, let \(H=\max(\|A\|_1,\|C\|_1)\), and write \(G=\sum_i c_iX^{a_i}\) using only its occupied terms.
Suppose \(\alpha\ne0\) is a nontorsion algebraic number with \(G(\alpha)=G'(\alpha)=0\).
Call a set \(I\) of term indices minimal if it is nonempty, the sums of \(c_i\alpha^{a_i}\) and \(a_i c_i\alpha^{a_i}\) over \(I\) both vanish, and no nonempty proper subset has both properties.
Suppose the sum over the residue-zero terms in \(I\) is nonzero at \(\alpha\).
The residue-one terms then have the opposite nonzero sum.
Put
\[
 g_I=\gcd_{i,j\in I}|a_i-a_j|,\qquad
 R_I=(\max_{i\in I}a_i-\min_{i\in I}a_i)/g_I .
\]
For \(p>p_0(m,\varepsilon)\), every such \(I\) satisfies
\[
 \max\{p,\,2[\mathbb Q(\alpha^{g_I}):\mathbb Q]\}
 \ \le\ R_I\ \le\ C(m,\varepsilon)(1+\log H)^{|I|-2+\varepsilon}.       \tag{1}
\]
Both constants are effective.
If \(A,C\) are coprime, at least one such set occurs in every partition of the support into minimal sets.
Indeed, remove minimal sets successively using the two vanishing sums for the whole graph.
Since \(A(\alpha^p)=-\alpha C(\alpha^p)\), coprimality makes both values nonzero and at least one block must contribute a nonzero residue-zero sum.

This applies to single-node double contacts in the [ordinary two-row test](Yin_C_G0901_v3.md#statement).
The [earlier two-residue estimate](Yin_C_G0345_v483.md#statement) concerned vanishing at \(\alpha,\alpha^2\).
Here the Euler derivative at \(\alpha\) supplies the second equation, with an additional logarithmic cost that depends only on \(R_I\).

<a id="lift"></a>
## The graph and its derivative on the torus

Fix a minimal set \(I\) as in the statement, put \(k=|I|\) and \(g=g_I\), and use a pivot \(i_0\) from residue zero.
Vanishing of both sums for two distinct exponents is impossible by the invertibility of the two-by-two matrix with columns \((1,a_i)\), so \(k\ge3\).
Take the free character lattice on the \(k-1\) differences from the pivot, and write \(h_i\) for its support vectors, with \(h_{i_0}=0\).
Define homomorphisms \(E,W\) to \(\mathbb Z\) by \(E(h_i)=a_i-a_{i_0}\) and \(W(h_i)\in\{0,1\}\) the residue label.
Thus \(E\equiv W\bmod p\), \(E\) has image \(g\mathbb Z\), and \(W\) is surjective.
A mixed difference is one modulo \(p\), so \(\gcd(g,p)=1\).
Throughout the proof we may quotient the lattice by a primitive vector killed by both \(E\) and \(W\).
The projected supports still generate the lattice by differences, and all are distinct because their \(E\)-values are distinct.

In any resulting lattice of rank \(r\), use \(v_1,\ldots,v_{r-1}\) spanning \(\ker W\) and \(v_r\) of weight one as a basis.
Let \(F=\sum_{i\in I}c_i Z^{h_i}=P(Z')+TQ(Z')\), where \(Z'\) are the first \(r-1\) variables and \(T\) the last.
The diagonal derivation \(\mathcal D_E\) sends \(Z^h\) to \(E(h)Z^h\).
At the point \(x=(\alpha^{E(v_j)})_j\), both \(F\) and \(J=g^{-1}\mathcal D_E F\) vanish.
The first equation divides the original value by \(\alpha^{a_{i_0}}\).
The second divides the Euler derivative minus \(a_{i_0}\) times the value by \(g\alpha^{a_{i_0}}\).
The same identities on any subset show that simultaneous minimality is preserved.
The coefficient multipliers \(E(h_i)/g\) are integers of absolute value at most \(R_I\).
Both \(P\) and \(Q\) are nonzero at the respective coordinates of \(x\).

We verify that no geometric component through \(x\) of \(F=J=0\) has codimension one.
In the Laurent polynomial ring over \(\overline{\mathbb Q}\), a common irreducible factor independent of \(T\) would divide \(P,Q\) and therefore cannot vanish at \(x\).
Over the field of rational functions in \(Z'\), the only possible nonunit common factor depending on \(T\) is \(T+P/Q\).
Putting \(T=-P/Q\) in \(\mathcal D_E F\) would then give
\[
       \mathcal D_{E|_{\ker W}} (P/Q)=E(v_r)(P/Q).
\]
For an indeterminate \(s\), this equation implies
\[
 (P/Q)(s^{E(v_1)}Z_1,\ldots,s^{E(v_{r-1})}Z_{r-1})
 =s^{E(v_r)}(P/Q)(Z').
\]
Indeed, after division of the left side by \(s^{E(v_r)}\), its derivative in \(s\) is zero in characteristic zero, and evaluation at \(s=1\) gives its constant value.
At a primitive \(p\)-th root of unity for \(s\), all variables on the left are fixed while \(E(v_r)\equiv1\bmod p\).
This contradicts \(P/Q\ne0\).

No positive-dimensional translate of a subtorus through \(x\) lies in this intersection.
On the translate, group the terms of \(F\) by equality of their characters restricted to the underlying subtorus.
Linear independence of distinct characters shows that each group gives a zero sum at \(x\).
The identical grouping works for the equation \(J=0\), allowing terms having zero derivative coefficient.
Minimality therefore forces all terms into one group.
Every support difference would then vanish on the underlying subtorus, which must be trivial since the differences generate the character lattice.

<a id="bound"></a>
## Descent and the derivative height

Use [Amoroso, Sombra and Zannier, Theorem 2.3 and Remark 2.4](../audits/literature/ASZ17/Yin_U001.md#intersection) with rational defining equations.
The coefficient-height dependence in this theorem allows the coefficients of both \(G\) and its derivative to vary.
The [proper-subsum clause in Theorem 2.6](../audits/literature/ASZ17/Yin_U001.md#gcd) motivates passing to simultaneous minimal sets.
Theorem 1.1 of the [inspected edition](../audits/literature/ASZ17/readme.md#edition) takes a fixed coefficient vector and its constants alone do not supply (1).

For each initial number \(k\le m\), take \(\eta=\varepsilon/(k-2+\varepsilon)\).
At a given lattice presentation put \(u=(E(v_j)/g)_j\), a primitive vector, and use the nontorsion parameter \(\alpha^g\).
Thus \(x\) lies on the corresponding injective one-parameter subgroup.
The preceding section gives codimension at least two and excludes every positive-dimensional coset through \(x\) even over \(\overline{\mathbb Q}\).
Clearing Laurent monomials gives rational defining equations with ordinary degrees bounded by the support coordinates of the presentation and logarithmic heights at most \(\log H+\log R_I+O_m(1)\).
The theorem either bounds \(\|u\|_\infty\) by a constant times \((1+\log H+\log R_I)^{(r-1)/(1-\eta)}\) or supplies a bounded nonzero relation in \(\ker E\).
The relation bound depends on the rank, defining degree bound, field degree one and \(\eta\), independently of the equation heights.

For completeness, use the finite tree of [bounded quotients that preserve the residue weights](Yin_C_G0345_v483.md#bounds).
Start with the finitely many configurations of at most \(m\) labels and their two weights.
At each presentation, consider all primitive relations within the bound in the second alternative, and for each such candidate of weight zero fix an integral basis of the quotient adapted to its induced weight.
The depth is at most \(k-2\), as each quotient lowers the rank.
Choose \(p_0\) larger than the absolute weights of all candidate relations in this finite tree, for every initial size and choice of labels.
At \(p>p_0\) every relation supplied during the actual descent, after passage to its primitive part, has weight zero because \(E\equiv W\bmod p\).
Consequently all support coordinates encountered are bounded in terms of \(m,\varepsilon\).
Rank one cannot occur, since its surjective weight would be an isomorphism while the \(k\ge3\) distinct support vectors have only two weights.
The descent therefore reaches the bounded-\(\|u\|_\infty\) alternative.

At that node the normalized exponent differences are pairings of bounded support vectors with \(u\), and \(r\le k-1\).
Taking \(K=k-2+\varepsilon\) gives
\[
               R_I\ll_{m,\varepsilon}(1+\log H+\log R_I)^K .
\]
The term \(O_{m,\varepsilon}((\log R_I)^K)\) after expanding the bound is at most \(R_I/2\) for all sufficiently large \(R_I\), which gives the upper bound in (1).
Some two terms share a residue, so their nonzero exponent difference divided by \(g\) is still a multiple of \(p\).
This gives \(R_I\ge p\).
After translating by the least exponent and dividing the differences by \(g\), the block yields a nonzero polynomial of degree \(R_I\) with \(\alpha^g\) as a double zero.
Indeed the monomial substitution \(X\mapsto X^g\) has nonzero derivative at \(\alpha\ne0\).
Separability over \(\mathbb Q\) now gives \(R_I\ge2[\mathbb Q(\alpha^g):\mathbb Q]\).

<a id="two-variables"></a>
## A coefficient-independent degree bound for a two-variable template

More explicitly, suppose a block with both row values nonzero is
\[
 X^{r_0}P(X^s)+X^{r_1}Q(X^s),
\]
where \(s>0\) is a multiple of \(p\), \(r_0\not\equiv r_1\bmod p\), and integral \(P,Q\) have nonzero constant coefficients.
Let \(e=r_1-r_0\) and \(g'=\gcd(s,e)\).
At any double zero \(\alpha\ne0\) put \(z=\alpha^s\) and \(y=\alpha^e=-P(z)/Q(z)\).
The Euler derivative after removal of the first monomial gives
\[
                     s z(P'Q-PQ')(z)-e(PQ)(z)=0 .
\]
The polynomial on the left has nonzero constant term \(-eP(0)Q(0)\) and degree at most \(\deg P+\deg Q\).
Bézout's identity for \(s,e\) and the row value equation give \(\mathbb Q(\alpha^{g'})=\mathbb Q(z,y)=\mathbb Q(z)\).
Hence \([\mathbb Q(\alpha^{g'}):\mathbb Q]\le\deg P+\deg Q\), irrespective of the coefficient heights.
If \(s\) is the gcd of all within-row differences, \(g'=g_I\).
A bounded horizontal span thus bounds the surviving power degree on a rank-two template.

<a id="primitive"></a>
## Consequences for primitive graphs and for their repeated factors

Let \(d=[\mathbb Q(\alpha):\mathbb Q]\).
If both row values are nonzero and the entire support is simultaneously minimal with exponent-difference gcd one, (1) bounds \(2d\), irrespective of the degrees of powers.
For a graph with coprime rows the same bound with exponent \(m-2+\varepsilon\) holds without simultaneous minimality whenever every positive power of \(\alpha\) generates its field.
In either case, if \(p\to\infty\) grows at most as a fixed power of \(\log d\) and \(H\le2^p\), the number of occupied terms must tend to infinity with \(d\).
Indeed any bounded subsequence of term counts in (1) would bound \(d\) by a fixed power of \(\log d\).

For the [degree inflation in the prescribed-prime test](Yin_C_G0901_v3.md#primitive), an irreducible repeated factor \(P_0(X^n)\) with \(n>1\) has a different consequence.
Every joint zero subsum \(F\) at a root has \(P_0(X^n)^2\mid F(X)\).
Write \(F(X)=\sum_{r=0}^{n-1}X^rF_r(X^n)\).
Since \(\mathbb Q[X]\) is free over \(\mathbb Q[X^n]\) on these residue monomials, \(P_0^2\) divides every \(F_r\).
Thus each occupied residue component is itself a joint zero subsum, and every minimal block lies in one residue modulo \(n\).
A primitive parent with this factor occupies more than one such residue, so it has a proper joint zero subsum even though its own exponent-difference gcd is one, and \(n\mid g_I\) in every minimal block.

Even an irreducible factor whose own exponent differences have gcd one can lose degree on powering.
For example, for \(\beta=(3+\sqrt5)/2\) and a primitive cube root of unity \(\omega\), the unit \(\alpha=\omega\beta\) has minimal polynomial \(X^4+3X^3+8X^2+3X+1\).
Indeed \(\alpha^3=\beta^3\) generates \(\mathbb Q(\sqrt5)\), so adjoining \(\alpha\) also adjoins \(\omega\), and multiplication over the four conjugates gives the displayed polynomial.
Its cube has degree two.
The all-power representatives of [the same Mahler measure](Yin_C_G0345_v421.md#norm) are available before imposing graph conditions.
Replacing a root of a given graph by such a representative need not preserve its double contact.
The constants in (1) depend on the number of occupied terms, and the prescribed-prime construction allows that number to grow with the degree.

## Assessment history

### Decision sparse-double-contact

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:04 |
| status | proved |
| reason | The two residue classes rule out a common moving divisor, so the bounded-degree torus intersection theorem applies at each reduction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A normalized exponent span and a power-degree bound for a mixed minimal simultaneous subsum at a double root. |
| argument | [Lift](#lift) | Lift of the two equations and exclusion of codimension-one components and positive-dimensional cosets. |
| argument | [Bound](#bound) | Descent, height cost, span and double multiplicity. |
| argument | [Two-variables](#two-variables) | The horizontal-span bound in two variables. |
| argument | [Primitive](#primitive) | Scope of the primitive parent and power-field assumptions. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1046.md#finding) | The precise statement and proof at the stated dependency interfaces. |

## Current assessment

[Selected decision](#decision-sparse-double-contact)
