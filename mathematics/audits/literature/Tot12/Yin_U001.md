---
author: Yin
---

<a id="tot12-u001"></a>
# Prescribing a zero with small supremum norm

In the [published edition of Tot12](readme.md#published-edition), Theorem 4 on p. 3533 fixes a \(C^2\) Jordan curve \(\Gamma\) and a point \(z_0\) in its interior.
There is a constant \(C\), uniform over \(w\in\Gamma\) and integers \(n\ge1\), for which a complex polynomial \(P\) of degree at most \(n\) satisfies
\[
P(z_0)=1,\qquad P(w)=0,\qquad \max_{z\in\Gamma}|P(z)|\le 1+C/n .
\]
For the unit circle with \(z_0=0\), \(w=1\) and \(n=N-1\), the maximum modulus principle gives the same bound on the closed unit disk.
For \(N\ge2\), it is at most \(\exp(2C/N)\).

Corollary 5 on the same page allows \(1\le k\le n\) arbitrary points of \(\Gamma\).
It gives a degree-\(n\) polynomial with value one at \(z_0\), a zero at each prescribed point and supremum norm on \(\Gamma\) at most \(\exp(Ck^2/n)\), with \(C\) depending on \(\Gamma\) and \(z_0\).
Both statements prescribe zeros on the curve where the norm is measured.

<a id="halasz-attribution"></a>
## Halász's one-zero estimate on the unit circle

On p. 3531 Totik credits Halász [6] with a monic degree-\(n\) polynomial \(Q_n\) vanishing at 1 whose unit-circle supremum norm is at most \(\exp(2/n)\).
The reversal \(z^nQ_n(1/z)\), described on p. 3532, has constant term one, still vanishes at 1 and has the same circle supremum norm because \(z\mapsto1/z\) permutes the circle.
Totik again invokes [6] on p. 3538 for the disk polynomial used in the proof of Theorem 4.
Reference [6] on that page identifies the 1983 chapter Hal83, pp. 259–269.

The inspection covers the published statements, the unit-circle specialization and Totik's attribution.
The proof of Theorem 4 on pp. 3537–3538 uses exterior tangent lemniscates and the cited one-zero estimate.
The proof and its lemniscate inputs were not independently verified, and the Halász chapter was identified bibliographically without inspecting its proof.
