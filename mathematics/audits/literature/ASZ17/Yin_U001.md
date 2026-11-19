---
author: Yin
---

<a id="asz17-u001"></a>
# Torsion curves on a codimension-two intersection of bounded degree and varying height

<a id="intersection"></a>
## Theorem 2.3 on a one-parameter subgroup

Let \(n\ge2\) and \(0<\eta<1\).
Let \(X\subset\mathbb G_m^n\) be cut out over a number field of degree \(\delta\) by equations of ordinary degree at most \(d_0\) and logarithmic height at most \(h_0\).
Let \(W\) be a geometric irreducible component of codimension at least two.
The source writes \(W^\circ\) for the complement in \(W\) of every positive-dimensional translate of a subtorus contained in \(W\), with arbitrary translating point.
Suppose \(u\in\mathbb Z^n\) is primitive, \(\xi\in\overline{\mathbb Q}^{\times}\) has infinite order and \((\xi^{u_i})_i\in W^\circ\).
There is an effectively computable \(B=B(n,d_0,\delta,\eta)\) such that either
\[
               \|u\|_\infty^{(1-\eta)/(n-1)}\le B(1+h_0)
\]
or there is a nonzero \(v\in\mathbb Z^n\) with \(\|v\|_\infty\le B\) and \(v\cdot u=0\).
The constant is uniform in the allowed heights and in the chosen component.
The theorem allows general torsion curves and gives a torsion hypersurface through the point on the second branch.
Remark 2.4 treats the injective homomorphism \(t\mapsto(t^{u_i})_i\).
The torsion hypersurface then imposes \(\xi^{v\cdot u}=\omega\) for a root of unity \(\omega\), forcing \(v\cdot u=0\) and \(\omega=1\).
Example 2.5 exhibits a positive-dimensional coset where the alternatives can both fail. [Coordinate conventions](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=3) [Theorem 2.3, Remark 2.4 and Example 2.5](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=5)

<a id="gcd"></a>
## Simultaneous proper subsums in Theorem 2.6

For several univariate Laurent sums with common exponent list \(0,a_1,\ldots,a_N\), take \(N\ge2\), \(\gcd(a_i)=1\), \(D=\max_i|a_i|\), and let \(h_0\) be the largest logarithmic height of an individual coefficient in the fixed degree-\(\delta\) coefficient field.
Assume at least one sum is nonzero.
Under \(D^{1/(2(N-1))}>B'(1+h_0)\), an injective monomial change into the original torus has size bounded by \(B'(N,\delta)\).
Pulling the gcd of the transformed equations back to the original parameter produces a divisor of the univariate gcd.
Every nontorsion root of the residual quotient forces some common nonempty proper subset of \(\{1,\ldots,N\}\) whose terms together with the constant term vanish in each original sum.
For the multiple-root application the authors address vanishing proper subsums by decomposing the terms into pieces minimal for the relevant equations. [Theorem 2.6](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=6) [Decomposition in Section 5](../../../literature/pdf/ASZ17--arxiv-v2.pdf#page=12)

The inspection covered the statements, coordinate and height conventions, the exceptional coset and subsum conditions, and this decomposition.
It accepts Theorem 2.3 as a published external input.
The codimension, coset exclusion, and control of the defining equations after any monomial restrictions have to be established in each application. [Inspected edition](readme.md#edition)
