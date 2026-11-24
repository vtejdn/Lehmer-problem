---
author: Yin
---

# Short relations among the exponents of both rows at bounded support

<a id="statement"></a>
## An alternative uniform in the substitution exponent and coefficients

Fix an integer \(k\ge5\) and a real \(K\ge1\).
Suppose \(F=A(X^p)+XC(X^p)\) has \(k\) occupied terms, \(p\ge2\) is an integer, and its two nonzero integer rows are coprime over \(\mathbb Q\) and have degrees at most \(b\).
Suppose \(\Delta_0=AA^\iota-CC^\iota\ne0\), where \(\iota\) replaces each variable by its inverse.
Let \(\alpha\) be a nontorsion unit with reciprocal minimal polynomial of degree \(d\) dividing \(F\) at least twice, and assume \(b\le Kd\).
In each row subtract the least occupied row exponent from all the others.
Collect the resulting \(n=k-2\) positive differences into a vector, let \(s\) be their gcd, and divide by \(s\) to obtain the primitive vector \(m\in\mathbb Z^n\).

There is a nonzero \(v\in\mathbb Z^n\) such that
\[
 m\cdot v=0,\qquad
 \|v\|_2\le K(n+1)^2 n^{(n-1)/2}(n-1)^{(n-1)/2}.
\]
Moreover there is a finite list, depending only on \(k,K\), of substitutions of Laurent monomials for the \(n\) variables, obtained by successively taking quotients by primitive relations on the exponents.
Either a nonzero power of \(\alpha\) has degree bounded in terms of \(k,K\), or in one of these substitutions the specialized horizontal determinant has a repeated geometric Laurent factor vanishing at the powered point.
The determinant is nonzero on the parametrized one-dimensional torus as a Laurent polynomial throughout.
Thus the remaining obstruction at fixed support can be examined on bounded lists of exponent patterns with a repeated factor, with unrestricted coefficients.
The argument supplies neither a bound on \(k\) for the ordinary test nor a gap in the repeated-factor case.

<a id="field"></a>
## The horizontal coordinates recover the power field

Write the original row pivots as \(j_0,j_1\), and put \(t=1+p(j_1-j_0)\), \(\gamma=\alpha^{ps}\) and \(y=(\gamma^{m_1},\ldots,\gamma^{m_n})\).
Use one independent variable for every nonpivot position.
In these variables the pivot-normalized rows \(P,Q\) are affine linear, have nonzero constant terms and use disjoint sets of variables.
At \(y\) their values satisfy \(P(y)=-\alpha^t Q(y)\); both are nonzero by coprimality of the original rows.
The same nonvanishing holds at \(y^{-1}\).
As \(m\) is primitive, \(\mathbb Q(y)=\mathbb Q(\gamma)\).
Since \(\alpha^t\) also belongs to this field, Bézout's identity gives
\[
 \mathbb Q(y)=\mathbb Q(\alpha^g),\qquad
 g=\gcd(ps,|t|)=\gcd(s,|t|).
\]
Write \(e=[\mathbb Q(y):\mathbb Q]\).
As \(d\le ge\) and \(g\mid s\), we have
\[
                    \|m\|_2\le\sqrt n\, b/s\le\sqrt n\,K e.             \tag{1}
\]
Set \(\Delta=PP^\iota-QQ^\iota\) and \(\partial z^u=(m\cdot u)z^u\).
By [multiplying the two reciprocal contacts](Yin_C_G0903_v5.md#area), \(\Delta(y)=\partial\Delta(y)=0\).
Indeed the rational function \(-P/Q\), along \(z_i=X^{psm_i}\), agrees to order at least two with \(X^t\) at \(\alpha\) and at its inverse.
Multiplying with the inverse-variable identity gives the two zero jets, since \(ps\ne0\).
The Laurent polynomial \(\Delta(Z^{m_1},\ldots,Z^{m_n})\) is nonzero by the hypothesis on \(\Delta_0\).

<a id="sections"></a>
## Degrees after intersecting with all exponent relations

In a torus of dimension \(N\ge2\) consider any nonzero Laurent polynomial \(D\) over \(\mathbb Q\), a primitive exponent vector \(a\in\mathbb Z^N\), and \(x=(\gamma^{a_i})_i\) such that \(D(x)=\partial_a D(x)=0\).
Assume \(D(Z^a)\) is not identically zero and no repeated geometric Laurent factor of \(D\) vanishes at \(x\).
Clear monomial denominators in both \(D\) and \(\partial_aD\) with forms of affine degrees at most \(L\).
Then neither polynomial can have a common irreducible Laurent factor through \(x\) with the other.
In fact such a factor \(J\), simple in \(D\), would divide \(\partial_a J\).
The [Newton polytope argument](Yin_C_G0903_v5.md#intersection) makes \(J\) homogeneous for the weight \(a\), including the case \(\partial_aJ=0\).
Then \(J(Z^a)\) is a constant times a monomial, so its vanishing at \(\gamma\) would contradict \(D(Z^a)\ne0\).
In particular \(\partial_aD\) cannot be identically zero.
Remove the common factors over \(\mathbb Q\), including any coordinate factors introduced when clearing denominators.
All conjugates of \(x\) still lie in a variety of dimension at most \(N-2\) and degree sum at most \(L^2\), by Bézout.

The lattice \(\{v\in\mathbb Z^N:a\cdot v=0\}\) has rank \(N-1\) and Euclidean covolume \(\|a\|_2\).
Indeed a basis, extended by a vector paired to one with \(a\), has determinant of absolute value one and normal height \(1/\|a\|_2\).
Choose independent vectors attaining the Euclidean successive minima \(\lambda_1\le\cdots\le\lambda_{N-1}\).
Each defines \(z^v=1\) of cleared degree at most \(\sqrt N\|v\|_2\).
Together their equations cut out a finite union of translates of the parametrized torus \(Z\mapsto Z^a\), which is the identity component by primitivity and dimension.
The point \(x\) and each conjugate belong to this identity component.
There they are isolated after intersecting with \(D=0\), since \(D(Z^a)\ne0\).

Intersect the preceding variety successively with the \(N-1\) binomials.
At a component that a binomial contains, retain the component at its current degree.
At a proper section the dimension drops by one and the sum of the new degrees is at most the old degree times the binomial degree.
Along each surviving branch at most \(N-2\) proper sections can occur.
Induction on the remaining sections bounds the degree sum of the final isolated points by the initial degree sum times the product of the largest \(N-2\) degree bounds.
Indeed, at a retained component one omits the current multiplier, and after a proper section the remaining dimension budget is one smaller.
Torus components can be counted by their projective closures, discarding boundary components at every step.
By the [upper product inequality for successive minima](../audits/literature/Hen02/Yin_U001.md#hen02-u001), this gives
\[
 [\mathbb Q(x):\mathbb Q]
 \le L^2 N^{(N-2)/2}\prod_{i=2}^{N-1}\lambda_i
 \le L^2 N^{(N-2)/2}(N-1)^{(N-1)/2}\,\frac{\|a\|_2}{\lambda_1}.       \tag{2}
\]
An empty product is one.
In (2), an improper section consumes no degree factor even if other components at the same step are cut properly.

<a id="smooth"></a>
## The first relation does not require an exception

As \(k\ge5\), one row contains at least three terms.
Suppose this row is \(P\); exchanging the rows changes only the sign of \(\Delta\).
For a nonpivot variable \(z_i\) with coefficient \(c_i\) in \(P\) one has
\[
               \frac{\partial\Delta}{\partial z_i}
                     =c_i\bigl(P^\iota-P/z_i^2\bigr).
\]
If all these derivatives vanished at \(y\), two distinct nonpivot positions of this row would have the same squared coordinate, since \(P(y)P^\iota(y)\ne0\).
Their exponents are different and \(\gamma\) is nontorsion.
Thus \(\Delta\) is smooth at \(y\), in particular no repeated factor passes through \(y\).
Multiplication by the product of the \(n\) variables clears the denominators of \(\Delta,\partial\Delta\) to degrees at most \(n+1\).
Apply (2) with \(a=m,L=n+1\) and then (1).
The resulting upper bound on \(\lambda_1\) proves the stated first relation.

<a id="iteration"></a>
## Bounded quotient substitutions

Take the shortest relation primitive.
There are finitely many possibilities by the first bound.
For each possibility fix an integral basis of \(\mathbb Z^n\) containing that relation, and pass to the quotient character lattice by setting its character to one.
The point belongs to this subtorus and its transformed coordinates generate the same field by the integral basis change.
The new weights \(a\) are primitive and have norm at most \(C(k,K)e\) because the original change of basis lies on a fixed finite list.
The specialized Laurent support and its cleared degree are likewise bounded solely in terms of \(k,K\).
The specialized determinant along the original parametrization is still the same nonzero Laurent polynomial; its two zero jets persist.
If the new dimension is at least two and no repeated geometric factor passes through the point, apply (2) again.
This supplies a primitive relation of bounded length in the new basis, extending the earlier relations and reducing the dimension once more.
At every step the list of choices is finite and all bounds depend only on \(k,K\).
In dimension one the primitive weight is \(1\) or \(-1\), so the nonzero specialized determinant bounds \(e\) by its cleared degree.
This proves the alternative.
In the bounded-degree case the [power-field norm descent](Yin_C_G0903_v2.md#interpolation) gives a positive lower bound for the original total logarithmic measure depending only on \(k,K\).

## Assessment history

### Decision bounded-horizontal-relations

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:59 |
| status | proved |
| reason | Bounding the degrees of the isolated conjugates uses all exponent relations but at most one degree multiplier per drop in dimension. The initial determinant is smooth at the powered point. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A bounded first relation for every fixed term count and near-degree width, and a finite choice of quotient patterns leading to bounded power degree or a repeated horizontal factor. |
| argument | [field](#field) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [sections](#sections) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [smooth](#smooth) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [iteration](#iteration) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0903_v5.md#area) | The reciprocal contacts give two vanishing jets of the determinant. |
| dependency | [Input](Yin_C_G0903_v5.md#intersection) | An invariant simple factor through the point would vanish on the full parametrized torus. |
| dependency | [Input](../audits/literature/Hen02/Yin_U001.md#hen02-u001) | The upper bound for the product of the Euclidean successive minima. |
| dependency | [Input](Yin_C_G0903_v2.md#interpolation) | A bounded-degree power supplies a lower bound for the original measure. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1056.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-bounded-horizontal-relations)
