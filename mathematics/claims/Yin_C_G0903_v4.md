---
author: Yin
---

# Six-term double contacts and the degree of the power field

<a id="statement"></a>
## A bound independent of the coefficient heights

Let \(F(X)=A(X^p)+XC(X^p)\) have exactly six nonzero terms with rational coefficients, with \(p\ge2\) an integer and \(A,C\) nonzero coprime polynomials over \(\mathbb Q\).
Let \(\alpha\) be a nontorsion algebraic unit whose irreducible minimum is reciprocal and divides \(F\) twice.
Write \(g\) for the gcd of the occupied exponent differences, \(W\) for their span divided by \(g\), and \(d_*=\min_{j\ge1}[\mathbb Q(\alpha^j):\mathbb Q]\).
There are absolute constants \(p_0,C_0\) such that for \(p>p_0\) either \(d_*\le C_0\) or
\[
                  [\mathbb Q(\alpha^g):\mathbb Q]\le C_0\sqrt W .
\]
In particular \(d_*\ll\sqrt W\) in both cases.
All constants are independent of \(A,C\), including their coefficient sizes.
The proof uses both inverse tangencies to obtain a curve of bounded degree, before using the separation into two residue classes.

<a id="curve"></a>
## A curve from the four value and derivative equations

Index the exponents by \(0,\ldots,5\), choosing \(a_0\) in residue zero, and write \(b_i=(a_i-a_0)/g\), \(c_i=[X^{a_i}]F\).
Then \(b_0=0\), \(\gcd_i b_i=1\), \(|b_i|\le W\), and \(\gcd(g,p)=1\) because both residues occur.
Set \(\beta=\alpha^g\).
In the five-dimensional algebraic torus set \(z_0=1\) and impose the four rational equations
\[
               \sum_{i=0}^5 b_i^j c_i z_i^{\pm 1}=0,\qquad j=0,1 ,
\]
where \(b_i^0=1\).
The double roots at \(\alpha,\alpha^{-1}\) show that \(y=(\beta^{b_1},\ldots,\beta^{b_5})\) is a solution.
After clearing monomials all four equations have degree at most five.
Thus the number and sum of the projective degrees of their geometric components meeting the torus are bounded absolutely by successive applications of Bézout's inequality.

To bound the component dimensions, put \(D(T)=\prod_{i=0}^5(T-b_i)\).
The [Euler interpolation formula](Yin_C_G0903_v2.md#interpolation) applies to each point of the torus solution set.
The four equations yield polynomials \(Q_+,Q_-\) of degrees at most three with \(Q_\pm(b_i)=c_i D'(b_i) z_i^{\pm1}\).
Their coefficients depend linearly on the corresponding six values.
Let \(S_0\) of degree at most five interpolate the six rational values \(c_i^2D'(b_i)^2\).
The nonzero product of the two cubics equals \(S_0+\lambda D\), with \(\lambda\) its coefficient of degree six.
For fixed \(\lambda\) this polynomial has only finitely many monic divisors of degrees at most three.
The monic normalization of \(Q_+\) determines its scale from \(Q_+(0)=c_0D'(0)\ne0\), and its values determine the five coordinates.
Hence the regular function \(\lambda\) has finite fibers and every component has dimension at most one.

<a id="characters"></a>
## Constant characters and the two residue classes

Write \(D_0\) for an absolute bound on the sum of the component degrees, enlarged to at least one.
An isolated component gives \([\mathbb Q(y):\mathbb Q]\le D_0\) by counting its rational conjugates.
Suppose \(y\) lies on a geometric curve component \(V\).
Its field of definition \(K\) has degree at most \(D_0\), because its Galois orbit consists of components of the same rational equations.
Any monomial \(z^v\) constant on \(V\), \(v\in\mathbb Z^5\), has constant in \(K\) by Galois invariance.
If \(b\cdot v\ne0\), evaluation gives \(\beta^{b\cdot v}\in K\), proving \(d_*\le D_0\).
We may thus assume that every constant character has \(b\cdot v=0\) and constant value one.

Let \(\Lambda\) be the lattice of these constant characters.
It has a basis with lengths bounded in terms of \(D_0\) alone.
Indeed on the normalization of the projective closure of \(V\), the zeros and poles of each coordinate ratio come from the six coordinate hyperplanes.
Each hyperplane cuts out an effective divisor of degree at most \(D_0\), and none contains the curve.
The lattice is the integral kernel of the matrix of orders of the five ratios at these at most \(6D_0\) points: a function on a complete irreducible curve with zero divisor is constant.
The matrix has entries of absolute value at most \(D_0\), so only finitely many such kernels occur.
It is saturated, being the kernel of an integer matrix.

Define the surjective weight \(w:\mathbb Z^5\to\mathbb Z\) by sending the \(i\)-th coordinate character to zero or one according to the residue class of \(a_i\).
For all \(v\) we have \(g\, b\cdot v\equiv w(v)\pmod p\).
Choose \(p_0\) larger than the weights in absolute value of every vector in the bounded bases just obtained, for all possible weights.
It follows that \(w\) descends to \(\mathbb Z^5/\Lambda\), as does \(b\).
The connected subtorus defined by \(z^v=1\) for \(v\in\Lambda\) contains \(V\) and has this quotient as its character lattice.

Its rank must be at least three.
In a basis with last coordinate of weight one the first value equation has the form \(P(Z)+TQ(Z)=0\).
Distinct original characters remain distinct since their pairings with \(b\) are distinct.
Both class sums are nonzero at \(y\): their vanishing would give the original coprime rows a common zero at \(\alpha^p\).
The derivative equation is the diagonal derivation with weights \(b_i\) applied to the first equation.
The [two-residue calculation](Yin_C_G0903_v1.md#lift) shows that these two equations have no common divisorial component through \(y\).
Indeed a divisor independent of \(T\) would divide both \(P,Q\).
A common divisor involving \(T\) would make \(P/Q\) on the weight-zero coordinates an eigenfunction of that derivation of weight \(b(v_1)\), where \(w(v_1)=1\).
Scaling by a primitive \(p\)-th root in the direction \(b\) fixes the weight-zero coordinates but acts nontrivially on this eigenfunction, since \(g\, b(v_1)\equiv1\bmod p\).
In rank at most two the two equations therefore cannot contain a curve through \(y\).
This proves \(\operatorname{rank}\Lambda\le2\).

<a id="degree"></a>
## A short character cutting the curve

Take an integer \(T=\lceil10\sqrt W\rceil\).
The map \(u\mapsto b\cdot u\) on \(\{0,\ldots,T\}^5\) has at most \(5WT+1\) values.
One fiber contains more than \((T+1)^2\) points, since \((T+1)^3>5WT+1\).
A translate of \(\Lambda\) contains at most \((T+1)^2\) points in this box, by projecting its rational span injectively onto at most two coordinate axes.
Subtracting two points in the fiber therefore gives \(v\notin\Lambda\) with \(b\cdot v=0\) and \(\|v\|_\infty\le T\).
The hypersurface \(z^v=1\) passes through \(y\), has degree at most \(5T\) after clearing monomials, and does not contain \(V\).
All \(K\)-conjugates of \(y\) lie in this finite torus intersection.
Bézout gives \([K(y):K]\le5TD_0\).
Since the \(b_i\) have gcd one, \(\mathbb Q(y)=\mathbb Q(\beta)\), proving the asserted bound.

More precisely, if the constant-character lattice has rank \(l\in\{0,1,2\}\), its translates meet the box in at most \((T+1)^l\) points.
Choosing \(T\) of order \(W^{1/(4-l)}\) gives \((T+1)^{5-l}>5WT+1\), hence
\[
                      [\mathbb Q(\beta):\mathbb Q]\ll W^{1/(4-l)}
\]
outside the bounded-power-degree alternative.
In particular, for a fixed \(K>0\), consider a sequence of six-term contacts with \(d=\deg\alpha=d_*\to\infty\), row degrees at most \(2d\), and \(p_0<p\le Kd\).
Then \(W\le2Kd^2+1\), so ranks zero and one would imply \(d\ll_K d^{2/3}\).
Consequently rank two is necessary eventually.
The five normalized exponent differences must obey two independent bounded integer relations, both of weight zero, from one of the finitely many bounded lattice bases above.
This restricts the support to finitely many rank-three quotient lattices while allowing arbitrary coefficient heights and varying directions inside each quotient.

In particular let \(d=\deg\alpha=d_*\) and suppose the row degrees are at most \(2d\).
Then \(W\le2pd+1\), so a six-term double contact at sufficiently large \(p,d\) requires \(d\ll p\), independently of the heights of the rows.
On an all-power degree-preserving shrinking sequence the [original-seed estimate](Yin_C_G0901_v5.md#short) permits primes \(p\to\infty\) with \(p/d\to0\): choose \(\theta\to0\) sufficiently slowly to satisfy both conditions there and take a prime in \([d\theta,2d\theta]\).
At these primes every qualifying graph of row width at most \(2d\) has at least seven terms.
Indeed the smaller supports already obey the [five-term power-degree bound](Yin_C_G0903_v2.md#statement).
Whether the least possible number of occupied terms tends to infinity at these primes remains open.

<a id="multiplicity"></a>
## The first support size beyond finite interpolation for higher multiplicity

More generally fix \(r\ge2\) and let the ordinary coprime two-row graph have \(k=2r+2\) occupied terms and a reciprocal nontorsion factor of multiplicity at least \(r\).
There are constants \(C_r,p_r\) depending only on \(r\) such that, for \(p>p_r\), either \(d_*\le C_r\) or \([\mathbb Q(\alpha^g):\mathbb Q]\le C_r\sqrt W\).
At smaller support sizes \(k\le2r+1\), the [interpolation bound](Yin_C_G0903_v2.md#statement) already bounds the latter degree in terms of \(r\) alone whenever a contact is possible.

For \(k=2r+2\) the ambient torus has dimension \(n=k-1\).
Impose the two sets of Euler equations of orders \(0,\ldots,r-1\) on the six-term model above with \(k\) coordinates including \(z_0=1\).
Their degrees after clearing monomials are at most \(n\), uniformly in the exponent weights.
Now the two interpolating polynomials have degrees at most \(k-r-1=r+1\).
Their product has degree at most \(2r+2=k\), and its prescribed \(k\) values again leave exactly the pencil \(S_0+\lambda D\) as the possible products, where \(D\) is monic of degree \(k\).
Each fiber is finite by the same monic-divisor and pivot-value argument.
The resulting variety has dimension at most one and bounded degree in terms of \(r\).
The field and divisor-matrix arguments apply with \(n+1\) coordinate hyperplanes, so either some nonzero power has bounded degree or all constant characters have value one and admit a bounded basis.
For \(p>p_r\) the weight descends to the quotient.
The equations of orders zero and one alone exclude a curve on a quotient torus of dimension at most two, as above.
The constant-character lattice therefore has rank at most \(n-3\).
A box of side \(T\) now has \((T+1)^n\) points, at most \(nWT+1\) values of \(b\cdot u\), and at most \((T+1)^{n-3}\) points in a translate of the constant-character lattice.
Taking \(T=\lceil(n+1)\sqrt W\rceil\) gives \((T+1)^3>nWT+1\), hence a character outside that lattice which cuts the curve at \(y\) and has degree at most \(nT\).
Bézout proves the bound with constants depending only on \(r\).

## Assessment history

### Decision curve-degree-for-double-contacts

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:35 |
| status | proved |
| reason | The interpolation curve has bounded degree and admits a short character cutting its component at the section point. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The six-term degree bound and its extension at support size twice the multiplicity plus two. |
| argument | [curve](#curve) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [characters](#characters) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [degree](#degree) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [multiplicity](#multiplicity) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0903_v2.md#interpolation) | The dual Vandermonde interpolation gives the polynomial pencil. |
| dependency | [Input](Yin_C_G0903_v1.md#lift) | The two residue classes exclude a curve of double contacts on a quotient torus of rank at most two. |
| dependency | [Input](Yin_C_G0901_v5.md#short) | The shrinking-seed test permits a sublinear prime and near-degree row width. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1050.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-curve-degree-for-double-contacts)
