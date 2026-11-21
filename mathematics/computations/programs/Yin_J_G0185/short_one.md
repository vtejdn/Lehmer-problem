---
author: Yin
---

# Unit factors through degree 44 at short exponent one

<a id="classification"></a>
## Classification with common dilations

Let \(q\ge2,\ p=q+1,\ v>1,\ g\ge1\) be integers, with \(|a|=q,\ |b|=p\) and \(\epsilon=\pm1\).
For a nontorsion algebraic unit \(z\) satisfying
\[
a(1+\epsilon z^{g(v+1)})+b(z^g+\epsilon z^{gv})=0,
\]
call \(D=[\mathbb Q(z^g):\mathbb Q]\) its primitive degree.
For \(D\le44\), the complete list consists of \(q=2,\ v=13,\ \epsilon=+1\), and every \(z\) such that \(s z^g\) is a root of
\[
 S(X)=X^6-X^5-X^3-X+1,\qquad s=-\operatorname{sgn}(b/a).
\]
Each of these roots has primitive degree six.
The degree of a lift \(z\) itself may exceed 44.
The [explicit factorization and trace argument](witnesses.md#witness) show that \(S\) is the irreducible polynomial of a Salem number.
Every conjugate of that number is a nontorsion unit, as is every \(g\)-th root of its product with \(s\).

<a id="reduction"></a>
## The unique exterior root

After fixing \(a=q\) by an overall sign, set \(Y=s z^g\) and \(\eta=\epsilon s^{v+1}\).
The normalized polynomial is
\[
 P_\eta(Y)=q(1+\eta Y^{v+1})-p(Y+\eta Y^v).
\]
The relation \(Y^v=R(Y)\), with \(R(Y)=(pY-q)/[\eta(qY-p)]\), has no common zero of numerator and denominator.
On the unit circle \(R\) has modulus one and degree one, since its zero \(q/p\) lies inside the circle and its pole \(p/q\) lies outside.
Thus \(Y^v/R(Y)\) winds \(v-1\) times around zero and takes the value one at least \(v-1\) distinct times, by lifting its argument through a full turn of the source circle.
The reciprocal identity \(Y^{v+1}P_\eta(1/Y)=\eta P_\eta(Y)\) pairs each exterior root with an interior one.
Since \(P_\eta\) has degree \(v+1\), at most one root is exterior, counted with multiplicity.
This calculation applies at \(q=2\) as well as at larger heights.

By Kronecker's theorem the minimal polynomial of a nontorsion unit root has an exterior conjugate, and its unit norm gives an interior conjugate.
Uniqueness and complex conjugation force the exterior conjugate to be real.
At \(Y=-r,\ r>1\), the graph equation would require \(r^v(qr+p)=pr+q\), whereas \(r^v(qr+p)>r(qr+p)>pr+q\).
Thus the exterior root is \(\alpha>1\), its reciprocal is the interior conjugate, and every other conjugate lies on the circle.
The [strict radial bound](../../../claims/Yin_C_G0345_v869.md#radius) at short exponent one gives \(2<\alpha+\alpha^{-1}<2p/q\le3\).
The trace of a reciprocal quadratic unit is an integer, so this excludes degree two.
Every remaining case has \(\alpha\) a Salem number of degree \(D\).

For \(q\ge4\), the [pole-norm exclusion and catalogue completeness](catalogue.md#short-one) give \(D\ge46\).
For \(q=2,3\) and \(D\le44\), the [complete catalogue range](catalogue.md#catalogue) gives \(\alpha\ge13/10\), since its sole solution below \(13/10\) has short exponent three.

<a id="finite"></a>
## The long-exponent bound and exact factorizations

The algebraic integer \(q\alpha-p\) is nonzero because \(\alpha>1\) is a unit and \(p/q\) is rational.
Its conjugates other than \(q\alpha-p\) have modulus at most \(p+q\).
Its nonzero integral norm therefore gives
\[
 |q\alpha-p|\ge(p+q)^{1-D}.
\]
The radial bound above gives \(\alpha<3\), hence
\[
 (13/10)^v\le\alpha^v
 =\frac{p\alpha-q}{|q\alpha-p|}
 <(3p-q)(p+q)^{43}.
\]
Comparing the integer powers gives \(2\le v\le271\) at \(q=2\) and \(2\le v\le327\) at \(q=3\).
For each such \(q,v\) and both signs \(\eta\), the [factorization program](short_one.py) factors \(P_\eta\) over the integers and multiplies all the factors back with their multiplicities and content.
It selects monic irreducibles with constant term \(\pm1\) and degree at most 44, discarding cyclotomic factors by FLINT's exact cyclotomic test.
Among the 540 normalized parents at \(q=2\), only \(P_+\) at \(v=13\) has a selected factor, namely \(S\) with multiplicity one.
The 652 normalized parents at \(q=3\) have none.
Since \(v+1=14\) at the unique hit, the normalization gives \(\eta=\epsilon\) for either sign of \(b/a\).
This recovers all the signs and lifts in the classification.

Run the following command from the repository root with Python 3 and python-flint 0.9.0.

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/short_one.py
~~~
