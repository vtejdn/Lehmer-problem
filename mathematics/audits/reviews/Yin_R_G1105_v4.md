---
author: Yin
---

# Trace separators on the Chebyshev grid and the positive resolvent

At 2026-11-08T02:13 UTC a separately assigned agent reviewed the fixed ledger inputs for Yin.
The reviewer took no part in their proof development and received the mathematical texts and requested scope without proof-generation dialogue, author explanations of the proofs or previous review findings.
The two findings below concern the specified ledger arguments for [G0001](../../tasks/Yin_T_G0001_v1.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Limits of separators](#torsion-limit-review) | independently reviewed |
| [Positive resolvent](#positive-resolvent-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Limits of separators](#torsion-limit-review) | [L464 v2 limiting separators](../../ledger/Yin_L_G0464_v2.md#torsion-limits) | Entire argument including growing degree, arbitrary separators and the strict positivity condition on the final escape rate. |
| [Limits of separators](#torsion-limit-review) | [L464 v2 boundary phase](../../ledger/Yin_L_G0464_v2.md#boundary-phase) | Finite atomicity at an interior nontorsion separator, given the cyclotomic coefficient limit. |
| [Limits of separators](#torsion-limit-review) | [L462 v2 signed matching](../../ledger/Yin_L_G0462_v2.md#central-sign-test) | Strict signs, left endpoint and three bounded moments used for compactness. |
| [Limits of separators](#torsion-limit-review) | [L464 v1 angular midpoint](../../ledger/Yin_L_G0464_v1.md#angular-midpoint-resultant) | Derivative product and angular midpoint value used in the weighted product. |
| [Positive resolvent](#positive-resolvent-review) | [L464 v1 positive fractions](../../ledger/Yin_L_G0464_v1.md#positive-resolvent) | Root count, measure, residues and endpoint inequalities. |
| [Positive resolvent](#positive-resolvent-review) | [L464 v1 mesh estimates](../../ledger/Yin_L_G0464_v1.md#moving-gap-mesh) | Arithmetic midpoint, bounded exterior radius, left endpoint and interior mesh. |
| [Positive resolvent](#positive-resolvent-review) | [L464 v1 arithmetic test](../../ledger/Yin_L_G0464_v1.md#angular-midpoint-resultant) | Angular midpoint, resultant and both arithmetic lower bounds. |

<a id="torsion-limit-review"></a>
## Limits of arbitrary separators

On the original grid \(B=U_{d-1}(t/2)\), with both residue blocks strictly signed in increasing order and \(Q(-2)/B(-2)<0\), the torsion-trace conclusion holds for \(d\to\infty\) and \(M(P)\to1\).
Either type of exceptional pair is allowed.
Indeed the \(n-2\) same-sign gaps and the first endpoint gap furnish \(n-1\) distinct real roots for matching.
The two unmatched trace roots satisfy \(|q|\le 5/2\) once \(M(P)\le2\), by writing \(q=\lambda+\lambda^{-1}\) with \(1\le|\lambda|\le2\).
The matched differences of \(t^h\), \(h=1,2,3\), have total absolute value at most the variation of \(t^h\) on the trace interval.
The Laurent coefficients in the signed matching calculation therefore bound \(k=\sum r_i\) and \(l=\sum b_i r_i\), giving bounded mass \(l-ck\) for any separator.

At the angular midpoint \(c\), \(\prod_i |b_i-c|=|B(c)|\ge1\), while \(\prod_i|B'(b_i)|=(2d)^{d-1}/d^2\) by the sine product.
Multiplying \(\mu_i=(b_i-c)Q(b_i)/B'(b_i)>0\) recovers the stated resultant formula, since strict residues rule out common roots.
Thus \((d-1)(\prod_i\mu_i)^{1/(d-1)}\ge(d-1)/(2d)\).
For a closed interval \(I\) of positive length strictly inside any given open subinterval, the angle parametrization gives a limiting grid proportion strictly between zero and one.
If mass in \(I\) tended to zero on a subsequence, the two-block arithmetic-geometric mean upper bound would tend to zero there since total mass stays bounded.
For each subsequential weak limit the closed-set inequality gives \(\mu_*(I)\ge\limsup\mu_d(I)>0\) along that subsequence.
This also puts the endpoints in the support.

Under the [cyclotomic limit result](../../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix), the upper-half-plane branch approaches \(e^{-i\theta}\) at \(u=2\cos\theta\).
The imaginary part of the Cauchy transform has the required nonpositive sign, so \(\operatorname{Im}(F_*(e^{-i\theta})e^{i\theta})\) vanishes at an interior nontorsion cut by continuity from both sides.
Here \(F_*\) is finite and nonzero, and its reversal identity gives \(\sigma\zeta^{2-D}=1\), forcing \(D=2,\ \sigma=1\).
The resulting invariant rational function belongs to \(\mathbb R(z+z^{-1})\), so the transform is rational with poles confined to the finitely many pole traces.
At each such \(v\), multiplying by \(i\eta\) at \(v+i\eta\) gives the atomic mass by bounded convergence and excludes a higher-order pole.
Removing these atoms leaves a proper rational transform without poles, hence the zero measure by its moments.
This contradicts full support.
Every original separator in the same gap differs from the midpoint by at most \(2\pi/d\), so an arbitrary sequence of separators with a prescribed accumulation point has a midpoint subsequence with exactly that limit.
The product estimate itself uses the angular midpoints.
The endpoint traces are \(2\) and \(-2\).
The additional divergence for each fixed limiting torsion trace follows from the [fixed-weight escape condition](../../claims/Yin_C_G0880_v2.md#moving-cut) when \(0<\log M(P)\to0\).
The source theorem behind the coefficient limit and the fixed-weight gap were used at their stated scopes.

One family separates the degree condition from the strict positivity condition.
For odd \(d\ge3\), set \(Q=t(B+U_{d-2}(t/2))\).
Then \(r_i=2b_i\sin^2(\pi i/d)/d\), \(Q(-2)/B(-2)=-2/d\), and \(P=(1+z^2)\sum_{j=0}^{2d-2}z^j\) has \(M(P)=1\).
At fixed \(d=3\), the separator \(1/2\) lies between \(-1\) and \(1\) and is not a torsion trace, since every rational torsion trace is an integer.
With odd \(d\to\infty\), the constant choice \(c=0\) is a separator, so \(|c-c_*|\sum|r_i|=0\) along this sequence.
The reviewed text imposes \(d\to\infty\) for the torsion conclusion and strict positivity for the escape rate.

<a id="positive-resolvent-review"></a>
## The positive resolvent and its two midpoint choices

All three sections of L464 v1 hold with the stated nonreal exceptional pair and strict endpoint sign.
The \(n-1\) located real roots and the conjugate pair exhaust the degree with multiplicity.
The real roots lift to the unit circle and each nonreal trace contributes one exterior root of modulus \(\rho\), giving \(M(P)=\rho^2\).
Cancellation of the pair in \(H\) leaves its constant one and simple residues \(w_i=(b_i-c)r_i/|b_i-q|^2>0\).
Expansion at infinity gives \(W=2x-a-c\) and \(J=K+ac-|q|^2+2xW\).
The identity \(H(c)=0\) gives \(\sum_i r_i/|b_i-q|^2=1\), and at \(-2\) the endpoint sign gives \(H(-2)>0\).
Consequently \(\sum_i w_i/(2+b_i)<1\) and \(W<4\).

At the arithmetic midpoint, division of \(|b_i-q|^2\) by \(|b_i-c|\) gives the stated variation bound, using \(|b_i-c|<4\).
For the remaining sum the two bounds follow from \(|b_i-c|\ge\Delta/2\) and \(2+b_i\le |b_i-c|+2+c\).
Under a fixed ellipse bound the terms independent of \(\Delta^{-1}\) stay bounded, yielding both divergence tests whenever \(V\to\infty\).
The Chebyshev gap formula gives \(\Delta\asymp(2k+1)/d^2\) for bounded \(k\), while \(2+c=O((k+1)^2/d^2)\), as needed at the left endpoint.
On a compact interior interval \(\Delta\asymp d^{-1}\), giving the stated \(\sqrt d\,|q-c|\) condition.
The [positive whole-measure gap](../../claims/Yin_C_G0880_v1.md#statement) is used precisely to require \(V\to\infty\) for integral inputs with positive measures tending to zero.

At the angular midpoint the weighted product above is divided by \(\prod_i|q-b_i|^2=|B(q)|^2\), and \(|B(q)|\le d\rho^{d-1}\) gives the lower bound \((d-1)/(2dM(P))\) after taking the geometric mean and multiplying by \(d-1\).
Monic integral division supplies \(K\in\mathbb Z\).
For real \(s\), each \(1-sb_i+s^2\) is positive and their product is \(\sum_{h=0}^{d-1}s^{2h}\ge1\), including \(s=0\).
Thus \(W-sJ+s^2W\) exceeds or equals the same lower bound and its minimum occurs at \(s=J/(2W)\).
The nonreal pair is essential to the definition of these \(w_i\).
The preceding torsion finding uses the weights \(\mu_i\) and applies also to real exceptional roots.
