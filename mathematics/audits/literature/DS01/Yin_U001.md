---
author: Yin
---

<a id="ds01-u001"></a>
# Powers in the classification of algebraic units on two circles

<a id="power"></a>
## The squared radius

Lemma 4.3 starts with a positive real algebraic number \(b\).
Some positive power \(b^m\) is the only conjugate of that power having absolute value \(b^m\).
For a conjugate \(b'\ne b\) with \(|b'|=b\), the identity \(b'\overline{b'}=b^2\) and Lemma 4.2 force \(b'/b\) to be a root of unity.
Taking a common multiple of the individual orders removes all such collisions. [Lemmas 4.2–4.3, pp. 7–8](../../../literature/pdf/DS01.pdf#page=7)

Assume that half of the conjugates of a degree-\(d\) algebraic number \(a\) have absolute value \(R>1\), and the remaining half have absolute value \(R^{-1}\).
Lemma 8.1 provides a positive integer \(n\) for which \(R^{2n}\) is a reciprocal quadratic or an extended Salem number.
Its degree is at most \(d_n=\deg(a^n)\) if \(a^n\) is reciprocal, and at most \(d_n+2\) otherwise.
The proof chooses an exterior conjugate and applies Lemma 4.3 to isolate the exterior radius after powering; it permits further doubling to make real conjugates of the powered radius positive.
Every conjugate of the resulting squared radius is a product of two conjugates of the powered input.
The product formula for the norm then leaves a unique interior conjugate, its reciprocal, with all remaining conjugates on the unit circle.
The degree bound counts the available pairs of conjugates, excluding reciprocal pairs with product one in the reciprocal case. [Lemma 8.1 and proof, pp. 12–13](../../../literature/pdf/DS01.pdf#page=12)

<a id="half-norm"></a>
## The unit classification

An extended Salem number is real, greater than one and of degree at least four, with a conjugate equal to its inverse and every remaining conjugate on the unit circle; integrality specializes this to a Salem number.
For such a number or a reciprocal quadratic, a Salem half-norm is the product of one chosen element of each reciprocal pair of conjugates. [Definitions, pp. 2–3](../../../literature/pdf/DS01.pdf#page=2)

Theorem 2.1′ takes an algebraic unit with its conjugates on exactly two circles.
In the unequal-population alternative the multiplicities have ratio one to two, and after the choice of conjugate made in Theorem 2.1 some power is a real, non-totally-real cubic unit.
In the equal-population alternative the radii are reciprocal and some positive power of the unit is a Salem half-norm associated to a Salem number or a reciprocal quadratic.
The final argument removes a unit-circular unit factor by raising to its torsion order. [Theorem 2.1′, p. 4](../../../literature/pdf/DS01.pdf#page=4) · [Unit specialization, p. 15](../../../literature/pdf/DS01.pdf#page=15)

The published degree bound controls the degree of the powered radius and allows a nontrivial exponent even when the input is reciprocal.
The hypothesis that all powers of the input generate the original field gives \(d_n=d\); inserting this equality in the published bound supplies no value for \(n\).
Any claim about \(R^2\) itself at a power-stable reciprocal minimum needs an additional argument addressing peripheral conjugates of the squared radius and the sign of the interior real conjugate.
The inspection checked the statements and the exponent-selection steps of the two lemmas and the final unit specialization, using the half-norm classification at theorem level. [Inspected edition](readme.md#edition)
