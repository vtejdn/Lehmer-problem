---
author: Yin
---

# Independent review of the integer moment table at conductor 19683

<a id="whole-19683"></a>
## Finding on all fixed-norm inputs and the complete lift

At 2026-11-09T08:49 UTC a separately assigned agent reviewed the fixed C882 v3 statement, all four argument sections and their necessary mathematical and computational inputs for Yin.
The reviewer took no part in their development and received only the fixed-input paths, review scope, applicable rules and execution conditions, without inherited proof-generation dialogue, author explanations or prior mathematical verdicts.
The reviewer formed the findings below before comparing R1107 v7, whose conductor-6561 conclusion was not used as evidence for the changed conductor.
The inspected C882 v3 and the two conductor-19683 programs were the working revisions available at this review minute; subsequent substantive changes require their own applicable inspection.

The rational logarithm series bounds give \(19683/1991<9\log3<19683/1990\), hence the cut is exactly 1990.
The recurrence \(H_i=uH_{i-1}-v^2H_{i-2}\), with \(H_0=1,H_1=u+v\), represents \(v^iB_i(u/v)\).
The interlacing recurrence counts roots above the tested rational by sign variations, omitting zeros.
Replaying both separators gave 7851 variations and the strict final inequalities \(19683|H_n|>2v^n\).
The successive terminal-block counts, layer sign parities, norm exponent 4391 and constructed valuations \((5,4,3,2,2,2,2,1,0)\) agree with the sign-product construction.
I checked its required full-grid sign basis, unit factors and layer norm payments in L464 v8; no existence of a prescribed moment hit follows from that construction.

The layer argument applies to every integral \(h\) with the prescribed pure two-power norm.
Doubling acts transitively on primitive indices modulo sign, making each \(F_\ell\) irreducible modulo two.
Dividing a reduced integral representative by its largest coefficient power of two leaves odd absolute norm, which must be one because all layer norms are integral and their product is a power of two.
Thus \(h=2^{t_\ell}f_\ell\) on each layer with an integral unit \(f_\ell\), and \(\sum d_\ell t_\ell=4391\).
The top degree 6561 forces \(t_9=0\); its odd negative-count parity fixes the common signed norm modulo three as \(-1\), yielding every displayed valuation parity.
This deduction imposes no unstated restriction to the constructed representative or its unit orbit.

The integral basis \(1,T_1,T_2,\ldots\) and primitive-root sums show that the trace divided by \(d_\ell\) of every integral polynomial value is integral.
All five polynomial products used for the linear-separator bounds are strictly positive at every layer node, because \(y\) lies in the sign-change gap and \(2\pm b>0\).
Their norms have exactly the factors \(3,3,9,9,27\), so arithmetic-geometric mean followed by integer rounding gives the stated ceiling-root bounds without a rounding-direction error.
The cubic has negative discriminant and opposite signs at the two rational separators, hence exactly one real zero inside the same gap.
Its positive products therefore satisfy the same normalized-trace argument.
For its resultant computation, multiplication by \(A^d+V_d\) in the monic cubic quotient has determinant \(A^{3d}\prod_{H(\alpha)=0}F_\ell(\alpha)\); division by \(A^{2d}\) gives the required absolute resultant.
I checked the quotient reduction, determinant orientation, recurrence, integral division and ceiling-root routine.

The dynamic program retains the least cost for each accumulated norm exponent because future admissibility and cost depend only on that exponent and the remaining layers.
The displayed valuation vector is feasible and supplies an incumbent, while all costs are positive and the next-layer cost increases with its valuation.
Consequently neither retaining only the least cost nor the incumbent cutoff can remove a better feasible vector.
As an additional check independent of this state compression, I enumerated the Cartesian product of permitted valuations subject only to the individual-term incumbent bounds and the total exponent equation.
This leaves respectively 24, 24, 24, 16 and 16 candidate vectors for the unweighted, \(c=3\), \(c=9\), \(c=27\) and cubic costs.
Direct summation gives the same minima \(15407,1562883,1580979,1623531,219942\), all attained at the displayed vector.
Any vector excluded by an individual-term bound already exceeds its incumbent in that positive term alone.
These optimizations cover a necessary superset of globally realizable layer data, which is sufficient for the asserted lower bounds.

I expanded the five sums to check \(T,s_0,J,W,E\), and expanded the cubic sum to obtain \(13N-41L+49K-58U\).
The endpoint identity is \(P(-1)=2+2x+U\), with \(U\) integral because \(B(-2)=(-1)^n\).
The expansion of the monic integral quotient \(C/B\) proves integrality of \(K,L,N\).
The positive weights for \(s_0,s_1,s_2\) have distinct nodes and are all nonzero, so Cauchy-Schwarz is strict.
The stated upper bound for \(U\) and the lower and upper bounds for \(N\) follow from the positive sums with \(2+y=39/100>0\), and therefore contain every admissible integer pair.
Exact replay of the rational tests over those complete ranges reproduces every row of the necessary table.
The cubic inequality excludes \(x=-1,U=1,N=6\), and substitution of \(N=6+2x^2\) leaves exactly the two profiles stated in C882 v3.

For \(x=-1\), the strict endpoint forces one root in the interval from \(-2\) to the least pole; each of the \(n-2\) same-sign gaps supplies another distinct root.
Pairing these \(n-1\) roots with their right poles leaves precisely \(b_*\) and two trace roots counted with multiplicity.
The disjoint interval integrals bound the matched differences by the total negative variation.
Here \(y<b_*<-1\), since the smallest positive-residue pole has decreasing-grid index 7851, which exceeds \(p/3=6561\).
Direct logarithmic expansion gives trace differences \((-2,-2,-2,18-4N)\) through degree four.
Factoring the derivative of \(f\) gives the critical points \(-3/4,1/2,3/2\), and evaluation gives \(V_-(f)=2953/768\) and \(\max_{\mathbb R}f=387/256\).
Strict monotonicity between \(y\) and \(b_*\) makes the exceptional-root contribution strictly larger than \(B_N\).
For \(N=9,10\) this exceeds \(2\max_{\mathbb R}f\), ruling out two real roots, including repeated real roots.
Reality of \(Q\) then makes the remaining two roots a conjugate pair; the degree count accounts for every root.

The expansion in \(T_j\) gives exactly the displayed boundary polynomial \(g_R\).
The signed Euclidean remainder chains at \(R=5/4,7/5\) have the stated nonzero endpoint signs, two variations at each endpoint and positive values at zero.
Their nonzero constant last members also verify squarefreeness.
Thus each quartic is positive throughout the closed interval.
The real part of \(f\) is harmonic on and inside the corresponding ellipse, so its boundary upper bound holds throughout the filled ellipse.
Conjugacy gives equal real parts at the exceptional roots, and the strict lower bound excludes each from that filled ellipse.
Both semiaxes of the trace ellipse increase strictly with its exterior lift radius, so this exclusion gives \(\rho>R\).
All paired trace roots lift to the unit circle, and the conjugate exceptional traces have equal exterior radius; hence the complete multiplicative measure is exactly \(M(P)=\rho^2\).
This verifies the strict bounds \(25/16\) and \(49/25\) for the stated branches.

The two exact negative values in the remaining-cases section also reproduce.
They establish failure of those particular inherited certificates at \(N=8\), without refuting the corresponding Mahler lower bound or supplying an admissible counterexample.
The review supports the conditional necessary table and the two complete-measure implications at the fixed conductor and norm.
It supplies no realization of a table entry, no complete-measure bound for \(N=7,8\), and no conclusion about arbitrarily small positive whole measures along growing conductors.

## Source applicability and computational limits

For the maximum-principle input I checked Axler, Bourdon and Ramey, *Harmonic Function Theory*, second edition, printed p. 7, Theorem 1.8 and Corollary 1.9, in the retained [ABR01 original](../../literature/pdf/ABR01.pdf).
The bounded open ellipse and the continuous real harmonic polynomial on its closure meet the corollary's hypotheses.
For Sturm's theorem I checked Narkawicz and Muñoz, [NASA/TM-2014-218548](https://ntrs.nasa.gov/api/citations/20150001256/downloads/20150001256.pdf), Section 2, printed p. 3, formulas (3)–(4) and Theorem 1.
The negative-remainder chains and nonvanishing endpoints meet its exact root-count hypotheses; the final zero term in that convention can be omitted when counting variations.
These are checked established inputs, without a claim to re-audit the books' or report's full proofs, priority, or formal implementations.
The other invoked inequalities and polynomial identities were checked directly at their finite stated scope.

Both retained Python programs completed under Python 3.14 using only integer and rational arithmetic.
Program execution was accompanied by inspection of the mathematical reductions, complete search ranges and arithmetic implementations; output agreement alone was not used as a proof verdict.
No numerical root finder, formal prover or construction of an actual \(h\) satisfying the prescribed moments was used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole fixed chamber](#whole-19683) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole fixed chamber](#whole-19683) | [C882 v3 statement](../../claims/Yin_C_G0882_v3.md#statement) | Complete hypotheses, all necessary integer combinations, endpoint identity, matching-third-moment profiles, two whole-measure implications and stated limits. |
| [Whole fixed chamber](#whole-19683) | [C882 v3 argument](../../claims/Yin_C_G0882_v3.md#argument) | Exact cut, both separators, every layer valuation, normalized integral traces, ceiling roots and exhaustive cost minimization. |
| [Whole fixed chamber](#whole-19683) | [C882 v3 moment table proof](../../claims/Yin_C_G0882_v3.md#moment-table-proof) | Positive sums, strict Cauchy-Schwarz, cubic resultants and full finite ranges of U and N. |
| [Whole fixed chamber](#whole-19683) | [C882 v3 whole measure](../../claims/Yin_C_G0882_v3.md#whole-measure) | Every-root pairing, multiplicities, trace identities, nonreal pair, Sturm certificates and complete lift measure. |
| [Whole fixed chamber](#whole-19683) | [C882 v3 remaining cases](../../claims/Yin_C_G0882_v3.md#remaining-cases) | Exact failed-certificate values and distinction from a counterexample or a general impossibility theorem. |
| [Whole fixed chamber](#whole-19683) | [Moment program](../../computations/programs/Yin_J_G0151/conductor19683.py) | All arithmetic routines, cut and layer checks, exhaustive DP and complete integer-table replay. |
| [Whole fixed chamber](#whole-19683) | [Exterior program](../../computations/programs/Yin_J_G0151/exterior19683.py) | Exact polynomial arithmetic, variation and maximum values, failed inherited tests and both quartic certificates. |
| [Whole fixed chamber](#whole-19683) | [L464 v5 odd grid](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Grid polynomials, recurrence, derivative and residue normalization, and endpoint values used here. |
| [Whole fixed chamber](#whole-19683) | [L464 v8 sign basis](../../ledger/Yin_L_G0464_v8.md#cosine-sign-basis) | Doubling order, primitive-layer sign basis and full-grid sign realization supporting the specified norm. |
| [Whole fixed chamber](#whole-19683) | [L464 v8 representative](../../ledger/Yin_L_G0464_v8.md#integral-sign-representative) | Integral factors, layer norm payments and the exponent and valuation formulas used at 19683. |
| [Whole fixed chamber](#whole-19683) | [L464 v8 layer congruence](../../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) | Signed layer norm congruence modulo three; unrelated asymptotic lower bounds are outside this review. |
| [Whole fixed chamber](#whole-19683) | [L464 v11 pure two-power argument](../../ledger/Yin_L_G0464_v11.md#finite-exclusions) | Irreducibility modulo two and valuation decomposition for every integral input of the specified norm. |
| [Whole fixed chamber](#whole-19683) | [L464 v7 profile moments](../../ledger/Yin_L_G0464_v7.md#prefix-cut) | Arcsine moments giving K, L and N equal to \(x^2+2,-4x,6+2x^2\); broader prefix and shrinking-shell results are not re-audited. |
| [Whole fixed chamber](#whole-19683) | [L464 v12 pairing](../../ledger/Yin_L_G0464_v12.md#pairing) | Disjoint root-pole intervals, negative variation bound and complete reciprocal-lift accounting. |
| [Whole fixed chamber](#whole-19683) | [L464 v1 endpoint roots](../../ledger/Yin_L_G0464_v1.md#positive-resolvent) | Strict endpoint and same-sign gaps giving \(n-1\) distinct roots in \((-2,2)\); unrelated resolvent estimates are outside this review. |
