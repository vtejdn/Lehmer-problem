---
author: Yin
---
# Rotated integral square roots and a possible contribution from the prime two

<a id="rotated-radicals"></a>
On 2026-11-04 agent-S compared mechanisms for the [unrestricted Lehmer gap](../tasks/Yin_T_G0001_v1.md#contract).
The proposed input is a family of integral power series of large linear rank over \(\mathbb Q(x)\) constructed from a single polynomial.
The comparison below is an exploratory assessment and its project deductions have not received a separate proof review.

## The arithmetic rank is supplied by the original polynomial

Near zero it suffices to consider monic irreducible reciprocal units \(P\) for which all positive powers of a root preserve its degree.
The descent in [C231, part D](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) sends any putative sequence to this class without increasing its positive logarithmic measure.
This is an existence reduction for the full gap question.

Write \(P_n(x)=\prod_i(1-\alpha_i^n x)\) and \(F(x)=\sqrt{P_2(x)P_4(x)}\) with \(F(0)=1\).
Reciprocity identifies these reversed polynomials with the monic powered polynomials in [Dimitrov, Lemma 2.1 and Proposition 2.2, pp. 3--4](https://arxiv.org/pdf/1912.12545v1#page=3).
The coefficient congruence \(P_4\equiv P_2\bmod 4\) gives \(F\in\mathbb Z[[x]]\).

For an odd prime \(q\) and a primitive \(q\)-th root \(\zeta\), use \(F_j(x)=F(\zeta^j x)\) for \(0\le j<q\).
Rotation keeps every branch radius fixed.
Within one powered level, a coincidence between different roots after rotation would give a torsion quotient of distinct conjugates, contrary to preservation of degree under every power.
Across the two levels a coincidence up to a root of unity would give \(2h(\alpha)=4h(\alpha)\) for the positive absolute Weil height.
Thus each radicand has a simple zero private to it.
Parity of vanishing orders gives independent square classes over \(\mathbb Q(\zeta)(x)\), and the \(2^q\) square-root products indexed by subsets are linearly independent there.
The empty subset contributes the constant 1.
Summing the distinct products in each orbit under \({\rm Gal}(\mathbb Q(\zeta)/\mathbb Q)\) gives rational Taylor coefficients that are algebraic integers.
The orbit sums are independent because their supports in the product basis are disjoint.
This gives at least \(2^q/(q-1)\) independent series over \(\mathbb Q(x)\) in \(\mathbb Z[[x]]\).

## What a complex analytic argument would have to buy

The useful input from [Calegari, Dimitrov and Tang, published Theorem 2.0.1 and (2.0.3), pp. 634--635](https://www.math.uchicago.edu/~fcale/papers/UDC.pdf#page=8) is the dimension bound with \(p(x)=x\) and \(x(t)=t\).
For one holomorphic \(\varphi\) on a neighborhood of the closed unit disk, fixing zero with \(|\varphi'(0)|>1\), the rank of these series, if all their pullbacks extend holomorphically there, is at most
\[
 H(\varphi)=\frac{e\int_{\mathbb T}\log^+|\varphi|\,d\mu}{\log|\varphi'(0)|},
\]
where \(\mu\) is Haar probability.
Even preimages or omission of all the simple branch values suffice for the pullbacks.
A construction from small \(m(P)\) with \(H(\varphi)<2^q/(q-1)\) would give a contradiction.
For instance \(q\) between \(4\log_2 d\) and \(8\log_2 d\) makes an upper bound \(d^3\) sufficient for large \(d\).
The extra \(q\) sets of branch points, the derivative and the numerator all enter the cost.
The theorem about uniformization of the punctured plane for roots of unity in Section 5 uses a different branch set.

Two comparisons change the recommendation.
The unrestricted radial sets in [van Ittersum, Ringeling and Zudilin, Section 2, Theorems 1--2](https://arxiv.org/pdf/2105.14837v1#page=2) admit capacity-one configurations with product of the expanding spine lengths tending to one.
More specifically, the [regular polygon comparison](../drafts/Yin_D_G0011.md#regular-orbit) prevents even the unrotated radical from using an expanding disk chart at \(u=(\log d)^{-2}\) on a free Salem-shaped configuration.
The [mesh argument](../drafts/Yin_D_G0011.md#mesh-screen) gives a draft-level reason to expect the obstruction on actual large-degree Salem inputs at that scale.
The regular polygon calculation concerns a real model, and the extension to actual roots uses their arithmetic discrepancy.
The algebraic family remains available even if this analytic application fails.

<a id="first-binary-layer"></a>
## A different use of the same functions at 2

Set \(U=P_2\) and \(W=(P_4-P_2)/4\).
Since \(U(0)=1\), the normalized germ \(F/U=1+2h\) has \(h\in\mathbb Z[[x]]\) and satisfies \(h^2+h=W/U\).
For a place over 2 of \(\mathbb Q(\zeta)\), write \(k\) for its residue field, \(\xi\) for the reduction of \(\zeta\) and \(\wp(v)=v^2+v\).
Here \(\xi\) has order \(q\).
The first nontrivial binary information is the rank \(r_q\) over \(\mathbb F_2\) of the classes of
\[
 r_j(x)=\overline W(\xi^j x)/\overline U(\xi^j x)
 \quad\text{in } k(x)/\wp(k(x)).
\]
For a mask \(I\), the product of its normalized germs is \(1+2\sum_{j\in I}h(\zeta^jx)\bmod4\).
Its first correction is rational over \(k(x)\) exactly when \(\sum_{j\in I}r_j\) vanishes in this quotient, since the two roots of \(v^2+v=b\) differ by 1.
The space of such masks has dimension \(q-r_q\).
This tests the same original arithmetic input in both characteristics.

In the squarefree case each \(r_j\) is proper and has only simple poles.
A rational Artin--Schreier coboundary with poles has even highest pole order at each pole, so a sum of these \(r_j\) is a coboundary precisely when its simple-pole residues all cancel.
For the reciprocal Salem control \(P=x^4-x^3-x^2-x+1\), one has \(U=x^4-3x^3+x^2-3x+1\) and \(W=-x^3-4x^2-x\).
Thus \(r_0=(x+x^2+x^3+x^4)/(1+x^5)\) in characteristic two, with poles at the four nontrivial fifth roots.
For \(q\ne5\) the rotated pole sets are disjoint and \(r_q=q\).
For \(q=5\) the five rotated functions have common denominator \(1+x^5\), and canceling the four numerator coefficients leaves exactly the all-ones relation.
This example isolates both outcomes without inferring that small measure forces either of them.

<a id="paid-lifting"></a>
## The first research question

Can a subspace of masks whose dimension grows with \(q\) retain rational approximations modulo increasing powers \(2^s\) with sufficiently low degrees on a specified unbounded-degree class?
Track both numerator and denominator degrees, a unit denominator at zero, the degree \(d\), the rotation prime \(q\), and descent of the chosen combinations to rational integral series.
The squarefree residue test supplies an algebraic starting point and identifies inputs with no first-layer gain.
Repeated reduction factors require a separate pole analysis.

A quantitative reason to ask this question is that a rational approximation modulo \(2^s\) of Hankel rank at most \(b_s\), with integral lifts, forces a \(k_0\)-row Hankel determinant to have valuation at least \(s(k_0-b_s)\) when \(k_0>b_s\), by multilinearity.
Here \(k_0\) is a matrix size and the valuation is normalized by \(v_2(2)=1\).
Linear growth of \(b_s\) with \(s\) can give a quadratic valuation, but its coefficient must retain the true degree and rotation costs.
An isolated mod-4 relation supplies no such coefficient.

One concrete first family has \(\overline U=\Phi_\ell\) for an odd prime \(\ell\), so \(d=\ell-1\).
If there is any pole, rotations at a prime \(q\ne\ell\) have disjoint pole sets, while at \(q=\ell\) all denominators can be written \(1+x^\ell\).
Write \(B(x)=(1+x)\overline W(x)\) in the latter case.
For each exponent \(t\) occurring in \(B\), cancellation requires \(\sum_{j\in I}\xi^{jt}=0\), which gives the exact binary kernel from the coefficient support.
The numerator must come from the original integral \(P\), and the useful overlapping rotation already costs \(q=d+1\).
This is a test of whether a structural gain survives those costs, with neither existence of small Salem numbers in this class nor coverage of the general core presupposed.

A useful next result would either exhibit a scalable family and its cost, or give a structural obstruction showing why the available masks never pay enough.
A theorem combining that finite-place information with the complex analytic loss, and coverage of the unrestricted inputs or a complementary treatment, would still be needed.

The closest existing routes are [S4](../strategies/Yin_S_G0004.md#route) and [S8](../strategies/Yin_S_G0008.md#route), which price arithmetic at selected powers and cyclic norms, and [S5](../strategies/Yin_S_G0005.md#route), which prices Fourier data in finite windows.
Here the proposed comparison concerns function-field monodromy and rational approximation to integral Taylor series.
The common input from S8 is the power-degree descent, while the criterion and the obstacle differ.
This assessment uses the eight route descriptions, selected fixed interfaces and the primary passages cited above at statement and applicability scope.
It assigns no priority claim in the wider literature, no new Mahler lower bound and no independent review.
