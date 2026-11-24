---
author: Yin
---

# Double contacts when both rows use the same three exponent positions up to translation or reflection

<a id="statement"></a>
## A degree-six bound with arbitrary coefficients and exponents

Let \(p\ge2\) and let \(F(X)=A(X^p)+XC(X^p)\) have nonzero integral rows, coprime over \(\mathbb Q[Y]\), with \(A(Y)A(1/Y)-C(Y)C(1/Y)\ne0\).
Suppose that both row supports are contained in translates of the same three-element integer set, allowing either row to be reflected.
If \(F\) has a repeated monic reciprocal irreducible noncyclotomic unit factor with root \(\alpha\), some nonzero power of \(\alpha\) has degree at most six.
In particular,
\[
       m(\alpha)\ge(\log 2)/24,\qquad
       \max(\|A\|_1,\|C\|_1)\ge 2^{p/24}.
\]
The constants allow unbounded exponent differences and coefficient heights.
With both rows occupying all three positions the power in the proof can be taken to be the gcd of the exponent differences of \(F\).
The condition includes equal, untranslated three-point supports even when the three positions are not in arithmetic progression and the six-term parent support is not symmetric.

<a id="tangency"></a>
## Two horizontal variables

Write the triple as \(\{0,u,v\}\) after translation, with \(0<u<v\), reflecting the entire choice if needed to put the first row in this orientation.
Remove one monomial from the Laurent graph and put \(a=pu,\ b=pv\).
The graph has the form
\[
       P(X^a,X^b)+X^t Q(X^a,X^b), \qquad t\equiv1\bmod p.
\]
Here \(P\) is supported on a subset of \(\{1,Z,W\}\) and \(Q\) on a subset either of that set or of \(\{1,Z^{-1},W^{-1}\}\), using monomials as support labels.
At \(y=(\alpha^a,\alpha^b)\) and \(y^{-1}\) neither row vanishes, by the graph equation and coprimality of the original rows.
In the rational function field put \(R=-P/Q\) and write \(f^\iota(Z,W)=f(Z^{-1},W^{-1})\).
Set \(\partial=aZ\partial_Z+bW\partial_W\).
The value and first derivative at both \(\alpha\) and its inverse give
\[
 R(y)=\alpha^t,\quad R(y^{-1})=\alpha^{-t},\qquad
 (\partial R/R)(y)=(\partial R/R)(y^{-1})=t .
\]
The chain rule gives \(\partial(R^\iota)=-(\partial R)^\iota\).
Consequently both \(\Delta=PP^\iota-QQ^\iota\) and \(\partial\Delta\) vanish at \(y\), since \(\Delta=QQ^\iota(RR^\iota-1)\).
The specialization \(\Delta(X^a,X^b)\) is the nonzero reflected determinant of the original rows evaluated at \(X^p\), because the removed monomials cancel against their inverses.

<a id="intersection"></a>
## Isolating the point in a cubic intersection

The support of \(\Delta\) lies in
\[
 \{(0,0),\ \pm(1,0),\ \pm(0,1),\ \pm(1,-1)\}.
\]
Its coefficients at opposite exponents agree.
If its Newton polygon has dimension two then every edge has lattice length one: two nonopposite points from the six outer positions have primitive difference, and opposite vertices cannot form an edge of a centrally symmetric polygon with interior containing the origin.
In the Laurent ring over \(\overline{\mathbb Q}\) such a polynomial has no repeated nonmonomial factor.
Indeed Newton polygons of products are Minkowski sums, by multiplication of the leading faces in every direction.
An edge of a factor occurring twice would give a parallel edge of length at least two in the product; for a segment factor take its full segment as leading face in a perpendicular direction.

If an irreducible Laurent factor \(J\) of this squarefree \(\Delta\) divides \(\partial\Delta\), the product rule gives \(J\mid\partial J\).
When \(\partial J\ne0\) its support is contained in that of \(J\), so the Newton polygon of the quotient is the single point zero and \(\partial J\) is a constant times \(J\).
The same identity with constant zero holds if \(\partial J=0\).
All monomials of \(J\) therefore have the same \(a,b\) weight.
Along the entire original horizontal subtorus \(J(X^a,X^b)\) is a constant times a monomial.
If \(J(y)=0\), this specialization vanishes identically, contradicting \(\Delta(X^a,X^b)\ne0\).

In dimension one the symmetry and primitive outer directions give \(\Delta=c(T+T^{-1})+d\), \(c\ne0\), in one Laurent monomial \(T\) with primitive exponent vector.
Write \(w\) for its \(a,b\) weight.
If \(w=0\), the specialization is constant and cannot both vanish at \(y\) and be nonzero.
If \(w\ne0\), the equation \(\partial\Delta(y)=0\) would force \(T(y)^2=1\), whereas \(T(y)=\alpha^w\) is nontorsion.
A constant nonzero \(\Delta\) has no zero.
Thus \(y\) is an isolated intersection of the two equations in the torus in every possible case.

Clear both Laurent equations by \(ZW\), then homogenize to degree three in the projective plane.
The degree-three forms, when nonzero, both vanish at the three coordinate vertices because each possible homogenized monomial contains at least two of the coordinates.
In the dimension-two case \(\partial\Delta\ne0\), since otherwise the whole support would have zero weight.
If the two forms are coprime, Bézout gives at most six remaining isolated torus points, after counting the three vertices with their multiplicities at least one.
If they have common factors, none passes through \(y\) by isolation.
Removing their homogeneous gcd over \(\mathbb Q\) leaves forms of degree at most two and at most four isolated intersection points.
All rational conjugates of \(y\) occur in the same isolated intersection, proving \([\mathbb Q(y):\mathbb Q]\le6\).

<a id="measure"></a>
## Returning to the original factor

Since \(\alpha^t=R(y)\), the field \(\mathbb Q(y)\) is exactly \(\mathbb Q(\alpha^{g_0})\), with \(g_0=\gcd(a,b,|t|)\), by Bézout's identity for these integers.
If both rows have full support the differences in one row generate \(\gcd(a,b)\mathbb Z\), and the two row origins differ by \(t\), so \(g_0\) has the asserted support interpretation.
The [power-field norm descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) supplies a nontorsion unit in this field with total log measure at most \(m(\alpha)\).
The [house bound](Yin_C_G0345_v869.md#degree) in degree at most six gives \(m(\alpha)\ge(\log2)/24\).
Finally the [individual two-row bound](Yin_C_G0345_v408.md#lower) gives \(\log H\ge p\,m(\alpha)\): the value equation expresses \(\alpha\) in the field of \(\alpha^p\), and reflected elimination retains both copies of its minimum.
The argument does not control arbitrary two triangles with different sets of exponent differences.

<a id="area"></a>
## A mixed-area test for general horizontal rows

More generally let \(P,Q\) be nonzero rational Laurent polynomials in two variables, \(a,b,t\) integers with \(g_0=\gcd(|a|,|b|,|t|)>0\), and \(r\ge2\).
Suppose \(P(X^a,X^b)+X^tQ(X^a,X^b)\) vanishes to order at least \(r\) at both \(\alpha\) and \(\alpha^{-1}\), where \(\alpha\) is a nontorsion algebraic unit.
Assume the row values are nonzero at \(y=(\alpha^a,\alpha^b)\) and \(y^{-1}\), and \(\Delta(X^a,X^b)\not\equiv0\).
Write \(N\) for the Newton polygon of \(\Delta=PP^\iota-QQ^\iota\).
Then either \(y\) lies on a geometric Laurent factor of \(\Delta\) of multiplicity at least \(r\), or
\[
                 [\mathbb Q(\alpha^{g_0}):\mathbb Q]\le 2\,\operatorname{area}(N).
\]
This permits arbitrary coefficient heights and counts. In particular a squarefree horizontal determinant of bounded positive area gives a uniform positive measure bound for the unit by the same norm descent.

Indeed \(R(X^a,X^b)-X^t\) has the two prescribed zeros and \(R=-P/Q\) is regular at each of them on the parameter curve.
Composing one contact with inversion and multiplying gives vanishing of \(RR^\iota-1\) to order at least \(r\) at \(\alpha\).
It follows that \(\partial^j\Delta(y)=0\) for \(0\le j<r\).
For any irreducible factor \(J\) through \(y\), one has \(J\nmid\partial J\) by the weight argument in the cubic intersection above.
If \(J\) has multiplicity \(s<r\) in \(\Delta=J^s E\), then \(\partial^s\Delta\equiv s!(\partial J)^s E\bmod J\) is nonzero modulo \(J\).
When every factor through \(y\) has multiplicity less than \(r\), a rational linear combination \(L\) of \(\partial^j\Delta\), \(0\le j<r\), therefore avoids divisibility by each of those finitely many factors.
Such a choice exists since each divisibility condition is a proper linear condition and \(\mathbb Q\) is infinite.
Consequently \(y\) is an isolated common point of \(\Delta,L\), and so are its rational conjugates.
The Newton polygon of \(L\) lies in \(N\).
After common factors are removed, the [plane mixed-area bound](../audits/literature/BS02/Yin_U001.md#intersection-multiplicities) bounds the number of isolated torus points by at most \(2\operatorname{area}(N)\), by monotonicity and Minkowski additivity as in the [inverse-intersection calculation](Yin_C_G0345_v865.md#intersection).
The value equation gives \(\mathbb Q(y)=\mathbb Q(\alpha^{g_0})\), as before.

## Assessment history

### Decision triangular-row-gap

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:36 |
| status | proved |
| reason | The two tangencies isolate the powered point unless a factor of the requisite multiplicity survives in the horizontal determinant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A degree-six power and positive gap for aligned triangular row supports, with a repeated-factor or mixed-area alternative for general rows. |
| argument | [tangency](#tangency) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [intersection](#intersection) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [measure](#measure) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [area](#area) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | A bounded-degree power permits norm descent for the total measure of the original unit. |
| dependency | [Input](Yin_C_G0345_v408.md#lower) | Reflected elimination gives the exponential lower bound on the original rows. |
| dependency | [Input](../audits/literature/BS02/Yin_U001.md#bs02-u001) | The plane intersection bound controls the number of isolated conjugates after removal of common factors. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1052.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-triangular-row-gap)
