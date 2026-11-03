---
author: Yin
---

# HP03: The Unital Operator Jensen Input

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [arXiv:math/0204049](https://arxiv.org/pdf/math/0204049), visibly v1, 3 April 2002, 12 pages; identity.

Passages: Theorem 2.1(ii), printed/PDF p.3; proof of (i) implies (ii), pp.6–7; Lemma 3.1, p.6; column construction, p.5.

Inspection: 2026-09-13, the affine-source reader: audited within the consumed finite-dimensional implication.


Neither all equivalences nor the full paper were audited.

<a id="hp03-u001"></a>
## HP03-U001: Positive-Interval Matrix Jensen Inequality

Recorded and directly inspected 2026-09-13 by the affine-source reader.
Bibliographic identity and artifact provenance: HP03 intake.
Primary artifact: [arXiv:math/0204049](https://arxiv.org/pdf/math/0204049), visibly v1 dated 3 April 2002, 12 pages.
Theorem 2.1(ii), printed/PDF p.3, and the proof of (i) implies (ii), pp.6-7, were checked; Lemma 3.1 p.6 and the column construction p.5 were inspected.
Coverage: audited within the consumed finite-dimensional implication; neither all equivalences nor the full paper were audited.

For a continuous operator-convex function \(f\) on an interval, the theorem gives
\[
 f\left(\sum_j a_j^*x_ja_j\right)
 \le\sum_j a_j^*f(x_j)a_j,\qquad \sum_j a_j^*a_j=I,
\]
for bounded selfadjoint inputs whose spectra lie in that interval.
The source proof extends the column to a unitary, averages diagonal phase conjugations to pinch block matrices, and uses operator convexity before taking the relevant corner.
In finite dimensions the column extension also follows directly by completing an orthonormal basis.
These steps were reconstructed.
Corollary 2.3's contractive statement has additional assumptions at zero and is not the input used here.

### Application checked separately from the source

In the circular comparison, write the completely positive subunital map as \(\Phi(X)=\sum_j k_jXk_j^*\).
Choose \(a_j=k_j^*\), give each corresponding input the same matrix \(U>0\), and append
\[
 a_0=(I-\Phi(I))^{1/2},\qquad x_0=I.
\]
This is a unital column.
For \(h(t)=t-\log t-1\), \(h(1)=0\), the theorem yields
\[
 h(I+\Phi(U-I))\le\Phi(h(U)).
\]
There is no evaluation at zero.

The elementary operator-convexity check was also completed locally.
The Schur complement of a convex combination of \(\left(\begin{smallmatrix}A&I\\I&A^{-1}\end{smallmatrix}\right)\ge0\) proves convexity of the inverse on positive matrices.
Integrating
\[
 -\log t=\int_0^\infty\big((t+s)^{-1}-(1+s)^{-1}\big)\,ds
\]
proves operator convexity of \(-\log\); on each compact positive spectral interval the integral converges in norm.
Adding the affine function \(t-1\) gives the required \(h\).
Trace pairing with any positive weight preserves the resulting operator inequality.

This established theorem is accepted as a resolved external input at this exact scope.
The noncommutative entropy comparison and the resulting determinant minimum are project deductions, reviewed in the consuming proof audit.
They are not attributed to HP03.
No new project Claim is needed merely to accept the known Jensen theorem.
