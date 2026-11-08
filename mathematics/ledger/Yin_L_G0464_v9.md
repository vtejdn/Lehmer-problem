---
author: Yin
---

# Sampling tails at a logarithmic cut in the full odd grid

<a id="rare-shell"></a>
## The probability for unconditioned coefficient sampling

Use the [strict odd-grid chamber](Yin_L_G0464_v5.md#odd-grid-product), the original monic reciprocal \(P\) of degree \(p+1\), and the target of exactly \(k=\lfloor p/\log p\rfloor\) negative residues for growing odd \(p\).
Write \(E_p(\varepsilon)\) for a single draw satisfying the cut, the strict endpoint and \(1<M(P)<1+\varepsilon\).
Any additional condition on the resultant gives a subevent.

Suppose every free integer coefficient has the marginal tail bound
\[
               \mathbb P(|a_j|>t)\le C\exp(-c_0t^\alpha)
                    \qquad(t\ge1)
\]
with \(C,c_0,\alpha>0\) fixed for all \(p,j\).
Independence between coordinates, degrees or draws is unnecessary.
For every fixed \(b>0\) there exist \(\eta_b>0\) and \(p_b\) such that
\[
            \mathbb P(E_p(\eta_b))\le \exp(-2(\log p)^b)
                      \qquad(p\ge p_b).
\]
In particular for any deterministic \(\varepsilon_p\downarrow0\) the chance per draw is smaller than \(p^{-r}\) eventually for every fixed \(r>0\).
Almost surely, even with at most \(\lceil\exp((\log p)^b)\rceil\) draws at each conductor, the sampled admissible positive measures have an infimum strictly above one, with the convention that an empty set has infinite infimum.

Indeed for each \(A>0\), the family \(H(P)\le(\log p)^A\) at the stated cut has a uniform positive gap.
Otherwise a shrinking sequence has \(p\to\infty\), and its midpoint obeys
\[
          \delta=2+c_p=2-2\cos(2\pi k/p)\le 4\pi^2/(\log p)^2 .
\]
For an integer \(h>A/2\), this would give \(H(P)\delta^h\to0\), contradicting the [height necessity](Yin_L_G0464_v7.md#height-escape).
Choose \(A\) with \(A\alpha>\max(b,1)\).
Every success in a sufficiently small fixed positive shell must have a coefficient larger in magnitude than \((\log p)^A\).
A union bound on at most \(p+1\) coefficients gives at most \(C(p+1)\exp(-c_0(\log p)^{A\alpha})\), which proves the displayed bound for large \(p\).
For the multiple-draw assertion use that stronger bound before simplifying it: multiplication by \(\lceil\exp((\log p)^b)\rceil\) still leaves a summable series, since \(A\alpha>\max(b,1)\).
The union of successes over all \(p\ge N\) has probability bounded by the corresponding tail sum, tending to zero.
Thus only finitely many sampled positive measures fall below \(1+\eta_b\) almost surely, and the minimum of any finite nonempty set of such values exceeds one.

<a id="positive-support"></a>
## What strict positivity would establish

As a separate single-draw law, give each odd conductor positive probability and, conditional on it, draw its free integer coefficients independently with a two-sided geometric distribution positive at every integer.
Each admissible polynomial then has positive mass.
For every fixed \(\varepsilon>0\) the mixture assigns positive probability to the prescribed chamber and \(1<M(P)<1+\varepsilon\) exactly when that set contains a polynomial.
The same equivalence holds after requiring a nonunit resultant.
Each such set is a countable union of atoms.
The rare-event estimate supplies an upper bound on their unconditional probabilities at individual conductors and does not settle this nonemptiness for all \(\varepsilon\).
A proof by another law or by counting still needs a positive lower bound or a nonempty strict set at arbitrarily small radii.
For a fixed law the events with radii \(1/j\) decrease to the empty set, so their probabilities necessarily tend to zero, including when each one is strictly positive.
