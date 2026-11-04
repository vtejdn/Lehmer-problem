---
author: Yin
---
# Neutral branch points and the radius of a disk at zero

<a id="neutral-disk"></a>
This working argument tests a necessary analytic hypothesis of the arithmetic holonomicity approach to the [Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract).
The estimates below are agent-S's argument for assessing a strategy and await mathematical review.

## Radius loss from one inner branch point

For a finite set \(B\) on the unit circle with at least five points, let \(R(B)\) be the supremum of \(|f'(0)|\) over holomorphic maps \(f:\mathbb D\to\mathbb C\) with \(f(0)=0\) and all preimages of every \(b\in B\) of even multiplicity.
Omitted values satisfy the condition.
The affine double cover \(y^2=\prod_{b\in B}(x-b)\) is hyperbolic by uniformization.
The projection \(\pi:\mathbb D\to\mathbb C\) from its universal cover, based over \(x=0\), realizes \(R(B)\) because every admissible map lifts by taking a holomorphic square root.
The inclusion of the open unit disk in the \(x\)-plane lifts to this cover, giving an inverse branch \(s:\mathbb D\to\mathbb D\) with \(s(0)=0\).

If \(0<|a|<1\) is an additional value with even preimages for \(f\), factor \(f=\pi\circ h\) with \(h(0)=0\).
The map \(h\) has even preimages at \(s(a)\), since \(\pi\) is unramified there.
Compose \(h\) with a disk automorphism sending \(s(a)\) to zero and take a holomorphic square root.
Schwarz--Pick at zero gives \(|h'(0)|\le 2\sqrt{|s(a)|}/(1+|s(a)|)\).
Schwarz's lemma gives \(|s(a)|\le |a|\), so
\[
 |f'(0)|\le R(B)\,\frac{2\sqrt{|a|}}{1+|a|}.
\]

<a id="regular-orbit"></a>
## A controlled comparison

Write \(\mu_N\) for the \(N\)-th roots of unity and fix \(N=5L\) odd.
If \(f\) is admissible for \(\mu_N\), then \(f^L\) is admissible for \(\mu_5\) and vanishes to order at least \(L\) at zero.
Lift \(f^L\) to the disk uniformizing the affine double cover for \(\mu_5\), which is hyperbolic since its compactification has genus two.
The order-\(L\) Schwarz lemma on the lift bounds the coefficient of \(z^L\) in \(f^L\) by \(R(\mu_5)\).
Thus \(R(\mu_N)\le R(\mu_5)^{1/L}\), also for a rotated polygon, by rotation invariance.
With an extra inner branch point of radius \(e^{-4u}\), the logarithm of the derivative is at most \(L^{-1}\log R(\mu_5)-\log\cosh(2u)\).
At \(u=(\log N)^{-2}\) this is strictly negative for large \(N\).

These constraints already occur in the real reciprocal configuration
\[
 (x-e^u)(x-e^{-u})(x^{2N}-2\cos(\theta)x^N+1),
 \qquad \theta/\pi\notin\mathbb Q .
\]
The second and fourth powers of its roots supply a rotated regular \(N\)-gon of simple branch points and the simple branch point \(e^{-4u}\).
This comparison uses free angles and has no claim to represent a single integral Galois orbit.

<a id="mesh-screen"></a>
## Transfer to a Salem conjugate set

A proposed extension bounds \(R(B)\) by \(1+C\Delta\) when the largest angular gap \(\Delta\), measured in radians, is small.
Here is the argument to check before using the extension to close the single-disk method.

At each point of the unit circle one can choose six members of \(B\) within \(O(\Delta)\), with pairwise distances at least \(c\Delta\), by choosing six separated arcs of length greater than \(\Delta\).
After translation and division by \(\Delta\), the six target values stay in a compact region and stay mutually separated.
Holomorphic maps of the disk based at zero with even preimages of these six normalized targets have uniformly bounded derivative at zero.
Indeed, a diverging derivative there gives a nonnormal family by Marty's criterion.
After taking a subsequence of target configurations, Zalcman's rescaling lemma would yield a nonconstant meromorphic function on \(\mathbb C\) whose preimages of each of the six distinct limits have even multiplicity by the argument principle.
The product of its six differences has only even zeros and even poles and therefore has a meromorphic square root on \(\mathbb C\).
The resulting map into the compact genus-two double cover lifts to the unit disk and is constant.
The classical rescaling input is the lemma of [Zalcman, pp. 814--815](https://www.math.stonybrook.edu/~bonifant/MAT402-s19/Zalcman.pdf).

Push forward the curvature-minus-one hyperbolic metric of the double cover to the plane with order-two cone points at \(B\).
The derivative bound just obtained gives density at least \(c'/\Delta\) along the unit circle by the covering characterization of the density, with divergence at a cone point.
For large absolute \(C\), the hyperbolic disk of radius \(1+C\Delta\) has smaller boundary density there.
The maximum principle on the unit disk compares the two densities since each satisfies \(\nabla^2\log\rho=\rho^2\) in its interior.
At zero the comparison gives \(R(B)\le 1+C\Delta\).

For a Salem number \(\lambda=e^u\) with \(0<u\le1\), take as \(B\) the unit-modulus roots of the polynomial with roots \(\alpha_i^2\), where the \(\alpha_i\) are the degree-\(d\) conjugates of \(\lambda\).
The powers remain distinct, and no square is a fourth power of another conjugate since their positive Weil heights differ.
Simplicity within each power also follows by sending one of two conjugates with torsion quotient to the unique expanding conjugate.
There are two real off-circle roots in the square orbit and the additional simple inner branch point \(a=e^{-4u}\) in the fourth-power orbit.
The squared polynomial is monic of measure \(e^{2u}\).
For \(d\ge55\) the compact Lipschitz discrepancy estimate in [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) gives \(\Delta=O((\log d/d)^{1/4}+1/d)\).
Indeed a unit-Lipschitz tent on a disk of radius comparable to the gap around its midpoint has circle integral \(\gg\Delta^2\) and its only possible root contributions are \(O(\Delta/d)\) from the two off-circle roots.
One may first cap the test radius at an absolute constant to exclude macroscopic gaps for large \(d\).

The proposed combined bound for maps supporting the unrotated radical is therefore
\[
 \log |f'(0)|\le O((\log d/d)^{1/4})-\log\cosh(2u).
\]
In particular the single chart would fail already at \(u\asymp(\log d)^{-2}\) for large \(d\), even when branching with even multiplicity is allowed.
The next check concerns the uniform moving-target estimate, its metric comparison and the finite discrepancy transfer.
This is a restriction on a specific complex analytic proof mechanism under the stated Salem hypotheses.
