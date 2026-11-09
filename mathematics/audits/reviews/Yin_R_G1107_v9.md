---
author: Yin
---

# Independent review of the fourth-moment and whole-measure bound at conductor 19683

<a id="fourth-moment-whole-19683"></a>
## Finding on every fixed-norm input and its complete Mahler measure

At 2026-11-09T12:10 UTC a separately assigned agent reviewed C882 v4, its new exact program and the necessary mathematical and computational dependencies for Yin.
The reviewer did not develop the proof and received fixed input paths, the review scope, applicable rules and execution conditions, without proof-development dialogue, exploration notes or additional author explanations.
Initial findings were formed from the fixed claim and its direct dependencies before reading R1107 v8.
The published assessment attached to the necessary C882 v3 dependency was visible when that claim was read; its review was consulted afterward to confirm the boundary of the already accepted table and other branches.
The present finding concerns the working C882 v4 and program revisions available at this review minute, at the exact paths and anchors bound below.

No mathematical gap was found in the stated fourth-moment bound, strict complete-measure conclusion or moving-cut obstruction.
The conclusion covers every integral input with the specified signs, norm and moments, rather than only the displayed valuation vector or one unit orbit.
The full measure bound uses the strict endpoint and is independent of which allowed endpoint integer \(U\) is realized.
It asserts neither realization of an input nor a conclusion about arbitrarily small positive measures along growing conductors.

The odd-grid identities give \(D(b_j)/B'(b_j)=(4-b_j^2)/p\), so the specified residues are exactly those of \(C/B\).
Both \(B\) and \(C\) are integral and \(B\) is monic, hence the Laurent coefficients of \(C/B\), including \(O=\sum b_j^3r_j\), are integers.
The exact interlacing recurrence places \(y=-161/100\) in the gap after decreasing-grid index 7851; the retained program reproduces the 7851 sign variations and a nonzero final value.
Consequently \(\mu_j=(b_j-y)r_j>0\) at every node.
Direct expansion gives total mass \(83/50\), first moment \(28/25\), second moment \(O+1127/50\), and
\[
 \sum_j\mu_j(b_j-2/3)^2=O+9803/450.
\]

I checked the pure two-power decomposition for arbitrary \(h\) at the scope used here.
The order of two modulo \(3^\ell\), up to sign, is \(d_\ell\), so Frobenius acts transitively on the distinct primitive trace roots modulo two and \(F_\ell\) is irreducible there.
After dividing the reduced integral polynomial representative by its largest common coefficient power of two, the remaining norm is odd.
All absolute layer norms are positive integers whose product is a power of two, so that odd norm is one and the remaining representative is an integral unit.
Thus every allowed input has \(h=2^{t_\ell}f_\ell\) with \(t_\ell\ge0\) and \(\sum d_\ell t_\ell=4391\).
Direct counting of the specified negative nodes on each primitive layer gives \((0,1,0,1,1,1,1,0,1)\) modulo two.
Since \(d_9=6561>4391\), \(t_9=0\); the common signed norm modulo three is then \(-1\), giving exactly the stated valuation parities.
This argument supplies necessary restrictions on all inputs and requires no converse realization claim.

The monic integral basis \(1,T_1,T_2,\ldots\) and primitive-root sums show that every normalized layer trace is integral.
The products \((4-b^2)(100b+161)(3b-2)^2f_\ell(b)\) are strictly positive: the separator matches the signs, \(2\pm b>0\), the unit is nonzero, and the rational \(2/3\) cannot be a root of a monic integral layer polynomial.
The layer norms of \(2-b\) and \(2+b\) are 3 and 1, respectively, so their product contributes exactly 3.
Multiplicativity of the norm gives the two displayed linear resultants, the second squared, with no omitted scalar factor.
Arithmetic-geometric mean followed by the normalized trace's integrality justifies the ceiling root rather than a merely approximate lower bound.

The new program reproduces all nine ceiling roots.
As an independent arithmetic check, I computed each required \(v^dT_d(u/v)\) by the ordinary two-term Chebyshev recurrence through every degree up to \(d\), rather than using the program's triple-degree recurrence.
The resulting integer-power comparisons give
\[
 (I_1,\ldots,I_9)=(4575,1216,1010,900,916,904,904,901,900).
\]
The imported dynamic program correctly retains the least cost at each accumulated exponent, since subsequent admissibility and cost depend only on that exponent and the remaining layers.
Its incumbent is feasible, all terms are positive, and increasing a layer valuation strictly increases its cost, so its cost cutoff cannot discard a better feasible vector.
I additionally implemented the min-plus recursion in reverse layer order with no incumbent cutoff and no assumed minimizing vector.
It reproduced the minimum \(14032098\) at \((5,4,3,2,2,2,2,1,0)\).
The optimization covers a necessary superset of globally realizable layer data, which is sufficient for the universal lower bound.
Dividing by \(900p\) is correct because the two new integer factors contribute \(100\) and \(3^2\).
The exact comparison is \(353/450<779561/984150\); it excludes \(O=-21\) and every smaller value, and integrality gives \(O\ge-20\).

For the complete measure, the strict endpoint gives \(Q(-2)/B(-2)=-P(-1)<0\).
The leftmost pole has negative residue, so the quotient tends to positive infinity on its left and has a trace zero between \(-2\) and that pole.
Each same-sign gap has opposite infinite endpoint limits and supplies another trace zero.
These \(n-1\) disjoint intervals therefore contain distinct roots in \((-2,2)\), irrespective of any multiplicities of the other roots.
Pairing each chosen root with its right pole leaves exactly \(b_*=b_{7851}\) and two trace roots counted with multiplicity.
The index \(7851>19683/3\) and the separator give \(y<b_*<-1\).
Each paired difference is bounded above by the integral of the negative part of \(f'\) over its interval, and the intervals are disjoint.
Summing proves the stated lower bound on the real parts of the two exceptional contributions without assuming those roots are nonreal.

I directly expanded \(f=-(t-2)^2(t+1)^2(t+2)\), differentiated it and checked the derivative factorization.
On the closed trace interval the factorization gives \(f\le0\).
The quadratic critical roots lie in \((-2,-1)\) and \((0,1)\), and the derivative signs make them the two negative local minima, separated by the zero at \(-1\).
Reduction modulo \(5t^2+5t-6\) gives \((-248-116t)/25\); using the sum of the two roots proves \(V_-(f)=76/5\).
The quadratic is negative at \(y\), so \(r_-<y<b_*<-1\), and \(f\) is strictly increasing from \(y\) to \(b_*\).
This verifies the strict inequality \(f(b_*)>f(y)\).

The logarithmic expansion gives \(\mathcal D(1)=1\) and power sums \((4,4,16,16,-56-5O)\) through degree five.
I checked the recurrence in the program and independently expanded the truncated formal logarithm by polynomial multiplication.
At \(O=-20\) both computations give \((1,4,4,16,16,44)\), and the fifth power sum's dependence on \(O\) is exactly \(-5O\).
Thus \(\mathcal D(f)=5(O+24)\ge20\), and the strict pairing lower bound is exactly \(29087946801/10^{10}\).

The exact Chebyshev expansion is \(-T_5+2T_3+2T_2-T_1-4\).
For every exceptional trace one can choose a root of its reciprocal quadratic with modulus \(\rho_i\ge1\), also for real traces and repeated roots.
Every paired trace root contributes two unit-circle roots, so all roots of the monic reciprocal lift are accounted for and \(M(P)=\rho_1\rho_2\).
Direct substitution shows that the difference in real parts of \(T_j\) from the unit-circle projection is \((\rho_i^j+\rho_i^{-j}-2)\cos(j\theta_i)\).
Its absolute value is at most \(E_j(\rho_i)\), while nonpositivity of \(f\) on the projected interval controls the remaining term.
For \(a,b\ge1\), the hyperbolic addition formula gives \(E_j(a)+E_j(b)\le E_j(ab)\); both the product of the excess hyperbolic cosines and the product of the hyperbolic sines are nonnegative.
This proves the displayed upper bound in terms of the complete product measure, with no replacement by the house or by one exterior root.
At \(M=5/4\) the exact upper cost is \(8847001/3200000\), below the strict lower bound by \(360267169/2500000000>0\).
Each \(E_j\) is increasing for \(M\ge1\), establishing \(M(P)>5/4\) for every specified strict-endpoint input.

For the moving-cut assertion, every full odd-grid node is nonzero, since \(2\cos(2\pi j/p)=0\) would require four to divide the odd conductor.
All \((b_j-y)r_j\) are positive, so the sum of their products with \(b_j^2\) is strictly positive.
The prescribed moments would make that sum \(-24-14y\le0\) when \(y\ge-12/7\), including equality at the threshold.
This is a contradiction without a norm or endpoint hypothesis and without a restriction to conductor 19683.
It supplies no obstruction for separators tending to \(-2\).

## Computation, inherited boundaries and limits

The inspected `higher_moments19683.py` completed under Python 3.14 with exact standard-library integer and rational arithmetic.
Its directly imported routines in `conductor19683.py` and `exterior19683.py` were read at their actual used scope.
The additional independent calculations described above were short interactive checks of the retained certificates, not new mathematical inputs or a construction of \(h\).
No floating-point root finder or formal proof assistant was used.
The analytic deductions, exhaustive valuation coverage, root multiplicities and full-measure relation were checked directly rather than inferred from a zero exit code.

The initial text's general statement that the program checked every rational identity exceeded its explicit checks of the derivative factorization.
The factorization itself is correct by direct differentiation.
After this coverage point was reported, the claim's last sentence in `whole-measure` was narrowed to “The displayed numerical rational bounds are reproduced by the retained program.”
I read that actual resulting sentence; the program and mathematical argument were unchanged, and the corrected description matches the checks performed.

After forming the present conclusions, I compared the direct dependency boundaries with [R1107 v8](Yin_R_G1107_v8.md#whole-19683).
Its accepted conductor-19683 integer table, sign-construction norm and \(x=-1,N=9,10\) conclusions remain at that earlier review's exact scope.
The present argument needs the fixed norm as a hypothesis and does not need a construction realizing the prescribed moments.
The earlier table and other whole-measure branches are not newly claimed as re-audited here.
The bounds for \(x=-1,N=7,8\), simultaneous integral realization, and the unrestricted Lehmer objective remain unresolved by this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v4 statement](../../claims/Yin_C_G0882_v4.md#statement) | All specified integral inputs, signs, norm, moments, strict endpoint, fourth-moment and complete-measure conclusions, and stated limits. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v4 layer bound](../../claims/Yin_C_G0882_v4.md#layer-bound) | Moment integrality, all layer valuations, normalized traces, positive norm products, exact resultants and ceiling roots, exhaustive minimization and O at least -20. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v4 whole measure](../../claims/Yin_C_G0882_v4.md#whole-measure) | All-root pairing, polynomial and trace identities, negative variation, strict inequalities, complete reciprocal-root accounting and M(P) greater than 5/4. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v4 moving cut](../../claims/Yin_C_G0882_v4.md#moving-cut) | Every odd full grid, strict positivity, inclusive separator threshold, four-moment contradiction and scope limits. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [New exact program](../../computations/programs/Yin_J_G0151/higher_moments19683.py) | All routines, exact arithmetic certificate outputs, supplied mathematical reductions and reproduction at the stated conductor and moments. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Conductor program](../../computations/programs/Yin_J_G0151/conductor19683.py) | Imported constants, ceiling_root, minimum_weighted_sum and separator_certificate; other computations retain their existing review. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Polynomial arithmetic](../../computations/programs/Yin_J_G0151/exterior19683.py) | Imported add, scale, remainder and evaluate, including trim; the earlier quartic and ellipse arguments are not repeated. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v3 hypotheses](../../claims/Yin_C_G0882_v3.md#statement) | Exact conductor, node order, signs, fixed norm and residue construction imported by v4; existing table and other branches retain R1107 v8. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [C882 v3 layer argument](../../claims/Yin_C_G0882_v3.md#argument) | Separator recurrence, layer degrees, valuation equation and parities, integral normalized traces and DP exhaustiveness used by v4. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Odd grid](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | B and D identities, simple nodes, residue normalization and endpoint identity at the stated grid. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Doubling order](../../ledger/Yin_L_G0464_v8.md#cosine-sign-basis) | Order of two modulo powers of three up to sign, used for layer irreducibility modulo two; the full sign-basis construction is not re-audited. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Layer norm congruence](../../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) | Signed layer norms modulo three and direct negative-node counts required for valuation parities. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Pure two-power decomposition](../../ledger/Yin_L_G0464_v11.md#finite-exclusions) | Integral representatives, irreducibility modulo two and unit remainder for every allowed input; earlier conductor exclusions are outside this finding. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Complete root pairing](../../ledger/Yin_L_G0464_v12.md#pairing) | Disjoint paired intervals, negative variation and product of both exceptional exterior radii with multiplicity. |
| [Fourth moment and whole measure](#fourth-moment-whole-19683) | [Endpoint roots](../../ledger/Yin_L_G0464_v1.md#positive-resolvent) | Strict endpoint and same-sign gaps giving n-1 distinct trace roots; no assumption of a nonreal exceptional pair is used. |
