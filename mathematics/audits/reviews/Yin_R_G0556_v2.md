---
author: Yin
---

# The first uniform degree multiple for the plastic seed

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fourfold return](#fourfold-return) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fourfold return](#fourfold-return) | [Statement](../../claims/Yin_C_G0336_v2.md#statement) | Both signs, every sufficiently large delay, the original degree, both strict bounds, minimality and the limit of the measures. |
| [Fourfold return](#fourfold-return) | [Transfer](../../claims/Yin_C_G0336_v2.md#transfer) | Every fixed positive integer multiplier, phase partition, common torsion roots including repeated roots of the auxiliary polynomial, and uniform logarithmic error. |
| [Fourfold return](#fourfold-return) | [Fourth multiple](../../claims/Yin_C_G0336_v2.md#fourth) | Whole-measure coefficient comparison, all 31 indices, strict asymptotic margin and the inequality for the original polynomial. |
| [Fourfold return](#fourfold-return) | [Optimality](../../claims/Yin_C_G0336_v2.md#sharpness) | One positive-sign progression, its precise torsion quotient and the three cyclotomic factorizations. |
| [Fourfold return](#fourfold-return) | [Circle and torsion count](../../ledger/Yin_L_G0462_v24.md#all-delays) | Unique exterior root and its limit, irreducibility of the nontorsion quotient, finite set of simple torsion roots of degree at most twelve, and total torsion degree at most thirty. |
| [Fourfold return](#fourfold-return) | [Algebraic power estimate](../literature/Wus02/Yin_U001.md#unit-circle) | Accepted logarithmic-form theorem and its stated consequence for fixed nontorsion algebraic numbers of modulus one. |
| [Fourfold return](#fourfold-return) | [Integer certificate](../../computations/programs/Yin_J_G0161/readme.md#four-phase-certificate) | Complete independent integer recalculation, including leading-coefficient cancellation and the two minimum floors. |

<a id="fourfold-return"></a>
## The uniform bound and its optimality

At 2026-11-16T11:46 UTC an agent for Yin reviewed the entire written claim and its stated inputs.
The reviewer took no part in developing this argument and received the fixed proof without development dialogue or an author explanation.
The earlier review in this family concerns the different exponent selector in version one.

The circle count works for both signs because multiplying \(g\) by the sign preserves its modulus on the circle.
The unique exterior root is simple and tends to the real root \(\theta>1\) of \(f\) by the two real test points bracketing \(\theta\).
The monic irreducible factor containing that root has unit constant coefficient and must contain its inverse, the only interior root.
The other factors are cyclotomic, and \(M(S)\) equals the exterior root.
For the three possible conjugates of a torsion root, clearing the rational-function identities gives degrees at most \(12,12,6\).
The constant or linear terms at zero distinguish the two rational functions in each case for both signs and parities.
A multiple torsion root would determine \(N=\eta(g/f)'(\eta)/(g/f)(\eta)\) on a fixed finite set, so eventually all are simple.
These bounds give the entire range \(-3\le k=N-d\le27\).

On \(y^d=w\), the equality \(a-b=N-d\) gives \(Q(y)=y^bD(y)\).
The roots common to this phase and \(D\) belong to \(H\) because an irreducible factor containing the exterior root cannot have a root of unity.
At these nodes the logarithmic derivative formula for \(D'\), the nonvanishing of \(f,g\), and the finitely many nonzero values of \(H'\) give \(|S(\eta)|\asymp d\).
In the remaining product, a root \(r\) at a deleted node contributes the derivative magnitude \(d\), divided by the distances to the other deleted nodes, once for each occurrence of \(r\).
All other roots contribute \(|r^d-w|\) divided by their distances to those nodes.
The possible distances in the denominators and the nonzero leading coefficients belong to fixed finite sets for each \(j\).
Exterior roots give the leading growth, interior roots give a bounded logarithmic error, and a torsion root outside the deleted set stays a positive distance from the phase after taking powers.
For an algebraic nontorsion root on the circle the source estimate applies at \(p=jd\), and \(|r^{jd}-1|\le j|r^d-w|\).
This controls both the lower logarithmic error and its uniformity across the fixed list.
Restoring the deleted nodes, taking the product over all \(w^j=1\), and using monicity of \(S\) in the absolute resultant gives the claimed transfer.
The logarithmic-form theorem was accepted at the scope of the source unit, whose original proof was outside this review.

For the finite bound the reviewer formed each \(V_k\) from the two cubics in independent integer arithmetic.
At each squaring step the reviewer formed the full coefficient product \(P(z)P(-z)\), checked that every odd coefficient vanished, and retained the even coefficients.
This polynomial has the squared roots and absolute leading coefficient \(|\operatorname{lc}P|^2\), including at \(k=0\), where the initial degree is eleven and the leading coefficient is \(-4\).
After eight steps, division by the binomial coefficient and by \((41/20)^{256}\) gave floor \(2\) at \(k=1\) and minimum floor \(1264\) at \(k=-2\) among the other thirty cases.
The symmetric-function coefficient inequality therefore gives a strictly positive minimum gap in \(\log M(V_k)-\log(41/20)\).
After multiplication by \(d\) this gap absorbs the transfer error for all sufficiently large \(d\).
The product over the roots of \(S\) is at most \(2^dM(S)^{4d}\), giving the stated strict measure bound.

On the progression \(N\equiv-1\bmod L\) with positive sign, each torsion order divides \(L\), forcing \(f(\eta)=\eta g(\eta)\).
The roots \(1,-1\) both occur, so simplicity gives \(d=N+1\) and \(k=-1\).
The reviewer multiplied the three displayed factorizations and checked that each equals \(f^j-(zg)^j\) at its respective \(j\).
Every factor has measure one, including \(z^6-z^3+1\), whose product with \(z^3+1\) is \(z^9+1\).
Thus the normalized logarithms for all three smaller multipliers tend to zero along this one sequence, whereas the fourth eventually exceeds \(\log(41/20)>\log 2\) throughout the family.
The argument establishes both assertions of minimality and the claimed limit of the measures.
