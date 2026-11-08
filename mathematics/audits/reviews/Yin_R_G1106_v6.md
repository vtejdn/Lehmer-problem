---
author: Yin
---

# Resultant ceiling on the full odd trace grid

<a id="resultant-ceiling-review"></a>
## Independent review of the ceiling and the uniform gap

At 2026-11-08T03:22 UTC, a reviewing agent outside proof development independently checked the complete argument of L464 v6 for Yin.
The mathematical inputs were the fixed text and its cited dependencies, without proof-generation dialogue, author explanations or earlier review findings.
For every sequence in the stated chamber with \(p=2n+1\to\infty\) and \(1<M(P)\to1\), the argument establishes \(\limsup\Delta^{1/n}<2\exp(-2^{-22})\).
The positive whole measures of inputs with \(\Delta^{1/n}\ge2\exp(-2^{-22})\) therefore have a uniform gap above one.

The hypotheses from L464 v5 require both sign blocks to be nonempty and strict, the endpoint ratio to be negative, and all nontrivial odd-conductor trace nodes to be present, including the imprimitive ones at composite conductors.
In particular every \(X_j\) is positive and the resultant is nonzero.
One can first select a subsequence witnessing failure of the limsup bound and then a further subsequence with one of the five profiles and \(c_p\to-2\).
The endpoint and profile input applies to the original whole measure and permits both types of exceptional roots.

For \(w=4-t^2\), the term \(w t H_x=-t(t-x)^2\) is integral, and the coefficient of \(z\) in \(w(t-2z)H_x\) is \(G=2(t-x)^2\), also when \(x=\pm2\).
Consequently the Laurent-coefficient argument of C881 v1 applies with this particular weight, and the odd-grid quadrature identifies the discrete reference moments.
With \(t=2\cos\theta\), the limiting angular density is \(2\sin^2\theta\,(t+2)G=(4-t^2)(t+2)(t-x)^2\).
Each factor \(\lvert t-v\rvert\) for \(v\in[-2,2]\) has zero angular logarithmic mean by the unit-circle mean formula, including the repeated roots at an endpoint.
This gives \(\langle\log f\rangle=0\), with only integrable logarithmic singularities.
The extra weight multiplies the v5 midpoint product by \(\lvert B(2)B(-2)\rvert=p\).
Thus its logarithmic mean is \(\log(n/p)+n^{-1}\log(\Delta p^2\lvert B(c_p)\rvert)\), where \(1\le\lvert B(c_p)\rvert\le p\).
Failure of the ceiling therefore gives a subsequential lower limit of at least \(-2^{-22}\) for the mean of \(\log X\).

For each fixed \(\epsilon>0\), weak convergence applies to \(1/(f+\epsilon)\), and ordinary equidistribution applies to \(\log(f+\epsilon)\).
Taking the grid limit first and then letting \(\epsilon\downarrow0\) gives the stated entropy bound because \(\log f\) is integrable.
The quadratic inequality for \(Y=X/(f+\epsilon)\) and Cauchy–Schwarz use \(\lim\mathbb E_pY\le1\), so the final mean absolute error is at most \(2\cdot256\sqrt{2^{-22}}=1/4\).
The discrete model \(n(b_j-c_p)G(b_j)\nu_j\) approaches \(f(\theta_j)\) uniformly, leaving the weighted residue error strictly below \(1/2\) eventually.
For each such conductor the first two cosine moments vanish, and integrality plus the recurrence with uniform error less than one forces all subsequent moments to vanish.
Polynomial interpolation at the distinct nodes now gives \(w(b_j)r_j=G(b_j)\nu_j\) for every \(j\).
Since \(\sum_j\nu_j=1\) and \(\max|G|\le32\), this contradicts the fixed-weight conclusion of C880 v2 for the nonzero integral polynomial \(w\).
At bounded conductors the elementary coefficient bounds leave finitely many monic integral lifts of measure at most two, which handles the remaining case in the uniform-gap assertion.

For the single J147 illustration I reconstructed the trace polynomial from the displayed reciprocal vector and obtained \(\operatorname{Res}(B,Q)=-4313\) by an exact Sylvester determinant.
Rational isolating intervals for the nine poles and Sturm counts for \(Q\) give one negative residue followed by eight positive residues in increasing trace order, with \(Q(-2)/B(-2)=-4\).
The degree-nine factor of \(Q=(t-2)T\) has eight roots in \((-2,2)\) and one above two, and the signs of \(P\) at the two stated rational bounds are negative and positive, respectively.
This check covers the displayed example at its fixed radius.
The previous profile and fixed-weight theorems enter through their stated interfaces, and the exhaustive enumeration of other degree-20 inputs lies outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Ceiling and gap](#resultant-ceiling-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Ceiling and gap](#resultant-ceiling-review) | [Statement](../../ledger/Yin_L_G0464_v6.md#norm-ceiling) | Strict subsequential bound, both root types and uniform positive-measure gap under the cutoff. |
| [Ceiling and gap](#resultant-ceiling-review) | [Weighted product](../../ledger/Yin_L_G0464_v6.md#weighted-product) | Exact moments, limiting density, angular logarithmic mean and all finite product factors. |
| [Ceiling and gap](#resultant-ceiling-review) | [Quantitative recovery](../../ledger/Yin_L_G0464_v6.md#quantitative-recovery) | Regularization, explicit error constant, exact residue recovery and contradiction. |
| [Ceiling and gap](#resultant-ceiling-review) | [Odd-grid product](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Full grid, positivity, quadrature weights and the unweighted midpoint product. |
| [Ceiling and gap](#resultant-ceiling-review) | [Coefficient and moment transfer](../../ledger/Yin_L_G0464_v5.md#five-cuts-and-original-profiles) | Interpretation of the limit of the original odd-grid quotient. |
| [Ceiling and gap](#resultant-ceiling-review) | [Left-endpoint profiles](../../ledger/Yin_L_G0464_v5.md#only-left-endpoint) | Applicability of the five profiles and the common cut limit to the selected subsequence. |
| [Ceiling and gap](#resultant-ceiling-review) | [Exact moments](../../claims/Yin_C_G0881_v1.md#moments) | Laurent-coefficient argument with the two integral cleared polynomials. |
| [Ceiling and gap](#resultant-ceiling-review) | [Integer recurrence](../../claims/Yin_C_G0881_v1.md#integer-recurrence) | First two moments and the uniform strict error needed for interpolation. |
| [Ceiling and gap](#resultant-ceiling-review) | [Fixed-weight gap](../../claims/Yin_C_G0880_v2.md#statement) | Fixed nonzero integral weight at simple poles and bounded variation on a positive shrinking sequence. |
| [Ceiling and gap](#resultant-ceiling-review) | [Degree-20 input](../../computations/programs/Yin_J_G0147/readme.md#unique-input) | Single polynomial, resultant, chamber and whole-measure interval. |
