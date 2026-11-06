---
author: Yin
---

<a id="br06-u001"></a>
# Rational dynamical small-point equidistribution and its complex measure

Inspection date: 2026-11-06.
The source is the [published edition](readme.md#yins-source-edition) of Baker and Rumely, *Equidistribution of Small Points, Rational Dynamics, and Potential Theory*, AIF 56(3) (2006), 625--688.
This ordinary source inspection for Yin accepts the precise established statements below as external inputs.
It does not claim an independent audit of their proofs.
The original PDF, rather than a search-result excerpt, was read at the cited passages.

<a id="br06-height-and-measure"></a>
## Heights and the complex canonical measure

Let k be a number field and phi in k(z) have degree d>=2, acting everywhere on the projective line, including its poles and infinity.
Write h for the absolute logarithmic Weil height and hat h_phi for the canonical height.
Printed pp.628--629 give
\[
 \widehat h_\phi(x)=\lim_{n\to\infty}d^{-n}h(\phi^n(x)),\qquad
 \widehat h_\phi\circ\phi=d\widehat h_\phi,\qquad
 \widehat h_\phi=h+O_\phi(1).
\]
Canonical height is invariant under Gal(kbar/k), is nonnegative, and vanishes exactly at preperiodic points.
For phi(z)=z^2 it equals h.
The compatible local normalization is also retained at [Smy08](../Smy08/Yin_U004.md#smy08-canonical-height).

At an archimedean place, where C_v is C, Theorem 2.1(B), printed p.629, characterizes mu_phi as the atomless Borel probability measure satisfying
\[
                         \phi^*\mu_\phi=d\mu_\phi.
\]
The source states this equality as an equality of (1,1)-currents.
The pullback counts preimages with their local algebraic multiplicities.
In measure notation, its action on a continuous test function f is
\[
 \int f\,d(\phi^*\nu)
  =\int\sum_{\phi(x)=y} e_x(\phi)f(x)\,d\nu(y).
\]
This is the pullback convention, not the pushforward identity obtained by testing f composed with phi.
Section 2.1 identifies this measure with the usual complex dynamical canonical measure supported on the Julia set; printed p.626 identifies it with the archimedean measure in the main theorem.
Theorem 2.1(A) separately concerns entire backward fibers of a nonexceptional complex point.
That nonexceptional-point hypothesis belongs to the entire-fiber statement and is absent from the arithmetic theorem below.

<a id="br06-galois-small-point-equidistribution"></a>
## Full Galois orbits of distinct small points

Theorem 2.3, printed p.631 and restated on p.659, assumes distinct x_j in P^1(kbar) with hat h_phi(x_j) tending to zero.
If S_j is the complete Gal(kbar/k) orbit of x_j, put
\[
                 \nu_j=|S_j|^{-1}\sum_{x\in S_j}\delta_x.
\]
At every place v, nu_j converges weakly to the canonical probability measure mu_(phi,v) on the Berkovich projective line over C_v.
At an archimedean place this is weak convergence on the ordinary Riemann sphere to the measure described above.
Weak convergence here means convergence of integrals against continuous functions on that compact space.

The theorem imposes neither irreducibility of an entire inverse-image polynomial nor equality between S_j and an entire backward fiber.
It does require the full orbit over the chosen field k, rather than one selected root or an arbitrary subset of conjugates.
For simultaneous use with ordinary heights, choosing k=Q makes this the orbit of the minimal polynomial over Q.
Theorem 4.6, p.656, explicitly deduces |S_j| tending to infinity from Northcott's theorem, distinctness and small canonical height; growing degree is not an additional theorem hypothesis.
Preperiodic points are permitted: Corollary 4.7's proof on pp.657--658 explicitly uses an infinite sequence of distinct such points.
Thus zero canonical height of a source point does not invalidate this theorem.

For phi=z^2, Theorem 2.4 on p.631 gives the corresponding ordinary-height conclusion: distinct algebraic points whose h tends to zero have their complete Q-Galois orbit measures converging to normalized angular measure on the unit circle.
The source explicitly presents this as the archimedean specialization of Theorem 2.3 and attributes the previously known statement to Bilu.
Using that specialization requires no identification of a selected root with an entire dynamical fiber.

<a id="br06-inspection-limit"></a>
## Actual source and proof limits

The bounded search sought the exact rational-map small-canonical-height theorem needed to compare two limiting measures.
It located this primary published article, whose full statements and their surrounding hypotheses on pp.628--631 were read; the restatement on p.659, the degree-growth sentence on p.656 and the preperiodic-point use on pp.657--658 were also read.
The 65-page file contains a cover followed by 64 article pages, so printed page p is physical PDF page p-623.
There is no supplied contents list in the inspected edition.
The title pages and a whole-text contents-marker search were checked, without claiming that every mathematical section was audited.

Theorem 2.1 is explicitly credited by this article to Lyubich and Freire--Lopes--Mane; those earlier original proofs were not read in this inspection.
Theorem 2.3 is the article's own theorem.
Its full proof, the energy-minimization results and the potential-theory dependencies in Sections 3--6 were not audited.
The displayed statements are accepted at the established-external-theorem level, with no claim of effective convergence rates or explicit height constants.
The search stopped once this single published edition supplied the exact arithmetic theorem and the required complex pullback balance; no comparison with an arXiv edition or general classification of rational maps was undertaken.
