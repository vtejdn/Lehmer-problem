---
author: Yin
---

<a id="can63-u001"></a>
# Cantor's rationality theorem for integral Laurent expansions

<a id="bounded-characteristic"></a>
## Bounded characteristic in the unit disk

On printed p. 362 of the [published article](../../../literature/pdf/Can63.pdf), Cantor calls a meromorphic function $f$ of bounded characteristic in $\mathbb D=\{z\in\mathbb C:|z|<1\}$ if $f=g/h$ for bounded holomorphic functions $g,h$ on $\mathbb D$, with $h$ not identically zero.
For $f$ holomorphic throughout $\mathbb D$, the same page gives the equivalent condition
$$
\limsup_{r\uparrow1}\int_0^{2\pi}\log^+|f(re^{i\theta})|\,d\theta<\infty,
$$
where $\log^+ x=\max(0,\log x)$ for $x>0$ and $\log^+0=0$.
Multiplying this integral by $1/(2\pi)$ gives the same finiteness condition for the angular mean.
The condition controls means as the radius tends to one and requires no extension to the boundary circle.
The quotient definition also covers functions with poles in the open disk.

<a id="cantor-rationality"></a>
## Theorem 1

On printed p. 365, Cantor proves that a function of bounded characteristic in $\mathbb D$ is rational if every coefficient of its Laurent expansion about $0$ lies in $\mathbb Z$.
The hypothesis permits a pole at the origin, since multiplication by a suitable nonnegative power of $z$ clears its finite principal part and preserves integrality.
For a function holomorphic at the origin, the coefficient hypothesis applies to its entire Taylor series.

The given proof clears the pole at zero, applies Lemma 1 to the Hankel determinants of the remaining Taylor coefficients and uses their integrality to conclude that they eventually vanish.
It then invokes Kronecker's rationality criterion.
The definition, the holomorphic integral criterion and Theorem 1 were checked on rendered pages 362 and 365 of the [journal scan](readme.md).
The estimates proving Lemma 1 and the cited results of Nevanlinna and Kronecker were not independently rederived.
