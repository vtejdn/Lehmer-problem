---
author: Yin
---

<a id="gj24-u001"></a>
# The geometric filling root and trace-field degree

<a id="filling-polynomial"></a>
## Peripheral coordinates

In Sections 1.1, 2.1 and 2.2 of the [published article](readme.md), fix an orientable complete finite-volume hyperbolic three-manifold \(M\) with one torus cusp and a peripheral basis \(\mu,\lambda\).
The trace field \(K\) of a hyperbolic filling is generated over \(\mathbb Q\) by the traces of the geometric holonomy, using lifts to \(\mathrm{SL}_2(\mathbb C)\).
Changing a lift changes a trace only by a sign.
The coordinates \(m,\ell\) are peripheral dilations, the squares of simultaneous eigenvalues of \(\mu,\lambda\).
The authors use the curve obtained from the holonomy image of the gluing variety and write \(A(m,\ell)\) for its primitive integral equation, up to Laurent monomials and sign.
For coprime \(p,q\) the Dehn filling polynomial is the Laurent polynomial \(A_{p,q}(t)=A(t^{-q},t^p)\).
The geometric point of every sufficiently long filling lies on \(A=0\) and \(m^p\ell^q=1\) by the hyperbolic Dehn surgery theorem, as used in (15).
These holonomies converge to complete cusp holonomy, where the peripheral dilations are \((1,1)\) as in Theorem 2.1.
Other points of this intersection can correspond to other representations.

<a id="geometric-degree"></a>
## The two inequalities in Theorem 2.4

Theorem 2.4 compares \([\mathbb Q(t_0):\mathbb Q]\) with \([K:\mathbb Q]\) in both directions, with constants depending only on \(M\), when \(t_0\) gives the discrete faithful filling representation.
For \(ps-qr=1\), the inverse coordinate on the filling subtorus is \(t_0=m^r\ell^s\).
Thus \(\mathbb Q(t_0)=\mathbb Q(m,\ell)\).
The core class \(\gamma=\mu^r\lambda^s\) has dilation \(t_0\), with simultaneous inversion allowed.
Its lift has eigenvalues \(u,u^{-1}\), so \(t_0+t_0^{-1}=(\operatorname{tr}\gamma)^2-2\) belongs to \(K\).
The quadratic equation over \(K\) gives \([\mathbb Q(t_0):\mathbb Q]\le 2[K:\mathbb Q]\).
The sufficiently long filling has a loxodromic core, so \(|t_0|\ne1\) and the minimal polynomial of \(t_0\) is noncyclotomic.
Remark 3.5 also describes the modulus of the choice \(|t_0|>1\).
These calculations make the lower-bound direction explicit.
For the other direction, the published proof uses a finite set of trace generators and algebraic dependence on peripheral traces along the fixed geometric curve.
The stated upper comparison is accepted at Theorem 2.4, without a separate verification of its cited character-variety theorem.

<a id="newton"></a>
## Corners and edge directions

Theorem 2.2 states that the vertex coefficients of the primitive integral \(A\) are units and that every edge polynomial has cyclotomic factors only.
[Cooper and Long](../CL97/Yin_U001.md#cl97-u001) work in peripheral eigenvalues.
In those coordinates the canonical Newton polygon is also known to be two-dimensional by [Boyer and Zhang, Proposition 10.1](../BZ01/Yin_U001.md#bz01-u001).
The degree comparison here uses Garoufalidis and Jeon's dilation convention throughout.
Lemma 2.3 observes that equality of two distinct projected exponents \(-qi+pj\) restricts the primitive direction to a finite list determined by the support.
Away from tied extremal exponents the lowest and highest coefficients therefore both have modulus one.
After removing a Laurent monomial and choosing the sign, all irreducible factors are monic with unit constant term.
Only the geometric root is needed for the trace-field estimate.

<a id="prior-bounds"></a>
## Published scope and subsequent announcement

Theorems 1.2 and 2.5 assume Lehmer's conjecture for their global linear lower bounds on trace-field degree and on every noncyclotomic irreducible factor degree, respectively.
The upper bounds are unconditional.
Theorem 4.1 proves a linear lower bound unconditionally for positive coprime pairs with fixed \(S_A<S_1<p/q<S_2\) and positive \(S_1\), by combining Lemma 3.1(b) with Dimitrov's house bound.
Theorem 1.1 attributes qualitative finiteness at bounded degree to Hodgson, and Remark 2.6 records unconditional special families on the Whitehead link.
These statements, the proof of Theorem 2.4 and the short deduction of Theorem 4.1 were inspected.
The global conditional estimates in Sections 3 and 4 and the original proof of hyperbolic Dehn surgery were outside this inspection.

A [November 2024 lecture abstract](https://sites.rutgers.edu/dltg/lectures/) by Kathleen Petersen reports joint work with Paul Fili and Neil Hoffman giving an unconditional linear estimate for most slopes and a lower bound of order \(H^{1-\varepsilon}\) for all slopes at each fixed \(\varepsilon>0\), with \(H=\max(|p|,|q|)\).
The accessible abstract leaves the exact meaning of “most” unspecified and includes no proof.
