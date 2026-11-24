---
author: Yin
---

# An explicit decomposition test for six-term reciprocal double contacts

<a id="statement"></a>
## Pole data and the power degree

Let \(F(X)=\sum_{i=0}^5 c_i X^{a_i}\) have six distinct occupied exponents and nonzero rational coefficients.
Suppose \(\alpha,\alpha^{-1}\) are double roots, with \(\alpha\) nontorsion.
Set \(g=\gcd_{i,j}|a_i-a_j|\), \(b_i=(a_i-a_0)/g\), \(W=\max b_i-\min b_i\), and \(\beta=\alpha^g\).
Write \(D(T)=\prod_i(T-b_i)\) and define the rational function
\[
 f(T)=\frac{S_0(T)}{D(T)}
     =\sum_{i=0}^5\frac{\rho_i}{T-b_i},\qquad
 \rho_i=c_i^2D'(b_i),
\]
where \(S_0\) has degree at most five and \(S_0(b_i)=c_i^2D'(b_i)^2\).
There is an absolute \(C\) such that
\[
                        [\mathbb Q(\beta):\mathbb Q]\le C W^{1/4}
\]
unless at least one of the following rational tests succeeds.

1. A partition into pairs is exchanged by a single Möbius involution \(\tau\): for each pole \(b_i\) its partner \(b_j=\tau(b_i)\) satisfies \(\rho_j=\tau'(b_i)\rho_i\).
2. There is a partition into triples \(A,B\) for which \(c_i^2D_A'(b_i)^2\) is constant on \(A\), and \(c_i^2D_B'(b_i)^2\) is constant on \(B\), where \(D_A=\prod_{i\in A}(T-b_i)\) and \(D_B=\prod_{i\in B}(T-b_i)\).

There are 15 pair partitions and ten unordered partitions into triples.
For each pair partition the proposed Möbius map is determined by its images at three poles.
Together the two tests characterize exactly the decomposition of \(f\) as a composition of rational functions of degrees greater than one over \(\overline{\mathbb Q}\).
They impose no bound on the coefficient heights.
A successful test leaves open whether the original polynomial has such a double root.

<a id="orbit"></a>
## Incidence at the six poles

Use the [interpolation curve](Yin_C_G0903_v4.md#curve) with coordinates \(z_0=1,z_1,\ldots,z_5\).
The point \(y_i=\beta^{b_i}\) lies on it.
The geometric components have bounded total degree independently of the data.
Any isolated component already gives bounded degree over \(\mathbb Q\).
On each curve component the parameter \(\lambda\) in \(Q_+Q_-=S_0+\lambda D\) is nonconstant, since its fibers are finite.
At generic \(\lambda\) the product has six simple roots.
Its splitting group \(G\) over \(\overline{\mathbb Q}(\lambda)\) is transitive because the rational map \(-f\) has degree six.
In particular the generic equation gives the degree-six extension \(\overline{\mathbb Q}(T)/\overline{\mathbb Q}(f(T))\).

A generic point of the curve is specified by three roots, namely the zeros of the monic normalization of \(Q_+\).
The value \(Q_+(b_0)=c_0D'(b_0)\) fixes its scale.
Conversely each triple gives the coordinates from \(Q_+(b_i)=c_iD'(b_i)z_i\), and the complementary cubic gives the inverse coordinates and their Euler equations.
Thus the generic points of a component correspond to a \(G\)-orbit \(\mathcal O\) of triples.
At \(\lambda=\infty\), put \(s=1/\lambda\).
The roots of \(D+sS_0\) have distinct expansions \(T_i=b_i-sS_0(b_i)/D'(b_i)+O(s^2)\) with real first coefficients and nonzero linear terms.
These expansions label the roots by the poles in the splitting field at one place above infinity.
At its conjugate places the resulting triples run through \(\mathcal O\).
The order of a coordinate \(z_i\) corresponding to a triple \(I\) is \({\bf1}_{i\in I}-{\bf1}_{0\in I}\), by evaluation of the monic cubic at \(b_i\) and \(b_0\).

If \(G\) is primitive, it is transitive on unordered pairs.
Otherwise an orbit of unordered pairs, or its complement, would define a nonempty regular graph of degree one or two on the six labels.
Degree one gives an invariant partition into edges.
In degree two the graph is a six-cycle or two triangles; its antipodal pairs or the two components then give an invariant partition.
For a triple orbit of size \(h\), transitivity on points and pairs makes its incidence Gram matrix have diagonal \(h/2\) and off-diagonal \(h/5\).
It acts by the nonzero scalar \(3h/10\) on the sum-zero subspace of \(\mathbb Q^6\).
The order formula at infinity now excludes every nontrivial constant character on the curve: adjoining the zeroth coefficient to make the sum zero, such a vector would have sum zero on every triple in \(\mathcal O\).

The map \(u\mapsto\sum_{i=1}^5 b_i u_i\) on \(\{0,\ldots,L\}^5\) takes at most \(5WL+1\) values.
Take \(L=\lceil 3 W^{1/4}\rceil\); then \((L+1)^5>5WL+1\).
Two points give a nonzero difference \(v\) in its kernel.
The character equation \(z^v=1\) of degree at most \(5L\) therefore cuts the component properly at \(y\).
The [component and orbit degree argument](Yin_C_G0903_v4.md#degree) gives \([\mathbb Q(y):\mathbb Q]\ll L\), using the absolute degree bound for the original equations and the component field of definition.
Since \(\gcd b_i=1\), \(\mathbb Q(y)=\mathbb Q(\beta)\).
It remains to describe the imprimitive case.

<a id="pairs"></a>
## A block of size two

An imprimitive transitive group on six objects has blocks of size two or three.
Any decomposition of \(f\) of degrees greater than one gives a block system by equality of the inner function on a generic fiber.
We now prove directly that conversely each possible block size gives the corresponding rational test and a decomposition.
At the chosen place at infinity a system of size-two blocks pairs the six poles.
The mate of a generic root \(x\) is fixed by its stabilizer in \(G\), so is a rational function \(\tau(x)\) over \(\overline{\mathbb Q}\).
Applying the pairing twice gives \(\tau^2(x)=x\); thus \(\tau\) is Möbius, \(f\circ\tau=f\), and it exchanges the poles in the indicated pairs.
It has rational coefficients since it takes three distinct rational points to three distinct rational points.
Comparison of residues gives \(\rho_{\tau(i)}=\tau'(b_i)\rho_i\), writing \(\tau(i)\) for the partner of \(i\).
Conversely, an involution with these pole and residue conditions makes \(f\circ\tau-f\) regular on the projective line: at all six simple poles the principal parts agree, and there are no other poles.
Its constant value must be zero because applying \(\tau\) negates the difference.
One of \(T+\tau(T)\) and \(T\tau(T)\) is nonconstant and has degree at most two.
It is invariant under the nonidentity \(\tau\), so has degree exactly two and generates the invariant field, giving the required decomposition.

<a id="triples"></a>
## A block of size three

For two blocks of size three label their specializations at the chosen place at infinity by \(A,B\) and set \(u=D_A/D_B\).
For generic roots \(x_i,x_j\) in the same block, \(u(x_i)/u(x_j)\) has neither zeros nor poles on the smooth projective splitting curve.
At a finite value of \(f\), no root can take a pole value \(b_i\); a root at \(T=\infty\) gives \(u(\infty)=1\).
Above \(f=\infty\), both roots specialize to the same block of poles at each place by invariance of the partition.
The simple root expansions show that the two \(u\)-values have the same order, either \(1\) or \(-1\).
Their ratio is therefore constant and real, as seen from their leading coefficients in the indicated expansions.
The setwise block stabilizer acts transitively on its three labels.
On their three \(u\)-values, each of its elements acts by a common real scalar, since all pairwise ratios are constants fixed by \(G\).
These finite-order scalars are \(1\) or \(-1\); a multiset of three nonzero values cannot be stable under negation.
It follows that \(u\) has the same value on each root in a block.
Thus \([\overline{\mathbb Q}(T):\overline{\mathbb Q}(f,u)]\ge3\), and \(\deg u=3\) gives \(f=V(u)\).
The outer function \(V\) has degree two and has simple poles only at \(0,\infty\).
Consequently \(V(s)=a s+b+c/s\) with \(ac\ne0\).
At a pole in \(A\), the identity \(S_0=aD_A^2+bD_AD_B+cD_B^2\) forces \(c=c_i^2D_A'(b_i)^2\), and at a pole in \(B\) it forces \(a=c_i^2D_B'(b_i)^2\).
Conversely if these two tests hold, \(S_0-aD_A^2-cD_B^2\) vanishes at all six poles and has degree at most six, hence is a rational scalar multiple of \(D_AD_B\).
This supplies the rational decomposition explicitly.

In this case, at a parameter for which \(S_0+\lambda D\) factors into two cubics of the form \(D_A-sD_B\) up to scalar, \(Q_+\) cannot be proportional to either full cubic at a nontorsion contact.
Indeed \(s\ne0\) by the nonzero prescribed values.
At the three poles of \(A\), the interpolation identity would give \(z_i\) proportional to \(1/(c_iD_A'(b_i))\).
Their squares would be equal, contradicting that the \(b_i\) are distinct and \(\beta\) is nontorsion.

## Assessment history

### Decision decomposition-of-six-pole-pencil

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:56 |
| status | proved |
| reason | At infinity, the triple-orbit incidence matrix rules out constant characters in the primitive case. Simple-pole expansions recover the inner functions for the two possible block sizes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rational tests for both decompositions of the six-pole pencil and the fourth-root bound for the degree of the normalized power when both tests fail. |
| argument | [orbit](#orbit) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [pairs](#pairs) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [triples](#triples) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0903_v4.md#curve) | The interpolation pencil and its generic factorization coordinates. |
| dependency | [Input](Yin_C_G0903_v4.md#degree) | Bounding the field degree of a proper character intersection. |
| dependency | [Input](Yin_C_G0903_v2.md#interpolation) | Reciprocal Euler interpolation. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1055.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-decomposition-of-six-pole-pencil)
