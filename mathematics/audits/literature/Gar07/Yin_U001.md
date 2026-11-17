---
author: Yin
---

# Gar07-U001: the real-conjugate height bound

<a id="gar07-u001"></a>
## Source and scope

The agent-S researcher for Yin inspected the [published edition](readme.md#journal), Theorem 1 on printed p.385, the height convention on p.386, and its complete proof in §2 on pp.386–388.
These four pages were rendered and inspected visually, and the product-formula calculation was reconstructed below.
This is an author-side source inspection, not an isolated independent project review.
Theorem 2, Corollary 3 and their applications are not adopted here.
No recursive audit of the references or claim about a current best bound is made.

<a id="real-conjugates"></a>
## Theorem 1, with the printed logarithm resolved

Let \(a\) be an algebraic number other than \(0,1,-1\), of degree \(d\), and suppose a positive fraction \(R\) of its distinct conjugates are real.
Use the [absolute logarithmic height convention](../Smy08/Yin_U001.md#smy08-height-normalization), so \(\log M(a)=d h(a)\) for the primitive integer minimal polynomial.
The bound proved at the end of §2, printed p.388, is
\[
 h(a)\ge f(R):=\frac R2\operatorname{arsinh}(2^{-1/R}),
 \qquad
 M(a)\ge
 \left(\frac{2^{1-1/R}+\sqrt{4^{1-1/R}+4}}2\right)^{dR/2}.
                                                        \tag{1}
\]
Integrality is not a hypothesis.
The introduction's Theorem 1 on p.385 prints an additional \(\log\) between the inequality and the powered expression for \(M(a)\).
This is present in the page image, not merely in extracted text.
The stronger formula (1) is explicitly the conclusion of the proof on p.388; the calculation below verifies that it is the formula supported by the argument.
The adopted input is precisely this proved formula, with that source discrepancy disclosed.

For clarity, if \(z=2^{-1/R}\), then the base of the power is \(z+\sqrt{1+z^2}\), explaining the inverse-hyperbolic-sine form.
Set \(f(0)=0\) when using (1) as a vacuous bound for a number with no real conjugates.

<a id="proof"></a>
## Product-formula check

Take \(K=\mathbb Q(a)\), let \(d_v\) be the local degree, and let \(\lVert\cdot\rVert_v\) extend the usual real or \(p\)-adic absolute value without a local-degree exponent.
The normalized height weights its logarithm by \(d_v/d\).
For each place put
\[
 b_v=\frac{\lVert1-a^2\rVert_v}{\max(1,\lVert a\rVert_v^2)},
 \qquad B=\prod_v b_v^{d_v/d}.
\]
The numerator is nonzero by the hypotheses.
The product formula gives \(\log B=-2h(a)\).
At a finite place \(b_v\le1\), and at a complex archimedean place \(b_v\le2\).
For each real conjugate \(\gamma\), let \(t_\gamma=\min(|\gamma|,|\gamma|^{-1})\in(0,1)\); its local factor is \(1-t_\gamma^2\).
The absolute logarithm identity over all places implies
\[
 \prod_{\gamma\ \mathrm{real}} t_\gamma^2\ge e^{-4dh(a)}.
\]
Arithmetic and geometric means therefore give
\[
 \prod_{\gamma\ \mathrm{real}}(1-t_\gamma^2)
 \le\left(1-e^{-4h(a)/R}\right)^{dR},
 \qquad
 e^{-2h(a)}=B\le
 2^{1-R}\left(1-e^{-4h(a)/R}\right)^R.
\]
With \(Y=e^{2h(a)/R}\), the latter inequality is
\[
                      Y^2-2^{1-1/R}Y-1\ge0.
\]
Its positive root proves (1), without the extra logarithm in the introductory display.
The elementary argument uses the ordinary product formula and arithmetic-geometric mean inequality; it needs no uninspected theorem from the later sections.

<a id="reciprocal"></a>
## Reciprocal specialization used in the project

For a monic irreducible reciprocal nontorsion unit polynomial of degree \(2m\), suppose its \(e\ge1\) exterior roots are all real and every other root off the unit circle is their reciprocal.
Its real-root fraction is \(R=e/m\), and (1) becomes
\[
                     \log M(P)\ge e\operatorname{arsinh}(2^{-m/e}).
                                                        \tag{2}
\]
This is a direct normalization of Garza's result, not a new project lower bound.
The separate signed-monomial comparison is developed in the [continuing project calculation](../../../drafts/Yin_D_G0033.md#barrier).
