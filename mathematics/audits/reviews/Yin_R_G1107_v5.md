---
author: Yin
---

# Review of exterior costs from two residue moments and the two conductor-243 searches

On 2026-11-08 at 06:27 UTC a separately assigned agent reviewed the completed working revision of L464 v12 and the conductor-243 section and program of J150 for Yin.
The reviewer did not participate in their development and received the input locations and scope without development dialogue, author explanations or prior review conclusions.
The review used the cited odd-grid identities, arcsine profile and finite exclusions at their stated scopes.

<a id="exterior-cost-review"></a>
## Bounds for complete lifts

The expansion of \(C/B\) gives integral moments by monicity of \(B\).
In \(pW\), the positive summands are \((2-b)^2(2+b)(b-y)h(b)\), yielding the factors \(9A_\ell|F_\ell(y)|\) on a ternary layer and \(p^2\Delta|B(y)|\) on the full odd grid.
At the angular midpoint the latter exceeds \((p/(p-1))^n\), so \(W>1/2\), whereas matching \(N=6\) at \(x=0\) gives \(W=-4c-6\).
The resulting strict separator requirement fails for \(k/p\ge1/10\), including the seven stated logarithmic cuts, whose floors are \(8,18,44,110,284,746,1990\).
At \(243\) exact rational powering in the five layers gives the two strict lower bounds for \(24300 W\), namely \(23236\) and \(60127\).
The next moment is at most \(2\) or \(0\) respectively in these strata even before requiring the strict endpoint.
I also replayed the linked J151 quadratic resultant comparison excluding \(N=6\).

For \(1\le k<n\), the strict left endpoint and the two signs give \(n-1\) disjoint intervals with a real interior trace root.
Pairing each with its right pole leaves precisely \(b_*\) and two residual traces counted with multiplicity.
The sum of the matched differences \(f(q)-f(b)\) is at most the integral of the negative part of \(f'\) over the disjoint intervals.
Each matched trace lifts to the unit circle, and for the residual pair the outer moduli satisfy \(\rho_1\rho_2=M\), including real, conjugate and repeated traces.
The inequality \(\cosh u+\cosh v\le1+\cosh(u+v)\) follows from the addition formula, so each total Chebyshev projection error is bounded in absolute value by \(E_j=M^j+M^{-j}-2\).
These estimates allow both residual pairs to contribute to the measure.

For \(x=0\), the logarithmic expansion gives \(\mathcal D(T_4)=26-4N\), and the two decreasing portions give negative variation \(8\).
The ordered-pole recurrence locates \(b_*>-41/50\) at \(243\) with \(b_*<0\), on the increasing branch of \(T_4\).
I checked both strict comparisons at \(83/50\) and \(199/100\).
For \(t^3-2t^2\) the sole decreasing interval is \((0,4/3)\), giving negative variation \(32/27\).
Its Chebyshev coefficients yield \(E_3+2E_2+3E_1=20w+8w^2+w^3\).
Exact sign variations give respectively \(254\) and \(809\) poles above the separators at \(729\) and \(2187\).
The cubic comparison at the rational separators therefore proves \(M>7/5\) and \(M>7/6\) for all strict \(x=0\) hits at these conductors.

For \(x=-1\), the identity for \(E\) and the integer endpoint \(U\ge1\) give \(E\le N-8-2y\), while the summands of \(pE\) have product \(p^3\Delta |B(y)|\).
The rational separator tests give \(N\ge7\) at \(729\) and \(6\le N\le10\) at \(2187\), the last upper bound using \(W=8-2y-N\).
At \(2187\) the strict Cauchy–Schwarz inequality applies to positive masses at distinct poles, with \(\sum\mu_j(2+b_j)=N+8-10y\) positive and \(\sum\mu_j/(2+b_j)\le1-y\).
For \(N=6\) the resulting upper bound falls below \((4-3y)^2\) by \(89/729\).
The next arcsine moment at \(x=-1\) is \(8\).

Expanding \(\log(Q/(tB))\) at \(x=-1\) gives \(\mathcal D(t^j)=-2\) for \(j=1,2,3\) and \(\mathcal D(t^4)=18-4N\).
I expanded the three test quartics in the Chebyshev basis and evaluated them at all their critical points and endpoints.
For \(u=1/2,1\) the two negative variations are \(625/256,81/16\), and the lower bounds exceed the projected increases at \(M=6/5\) by \(4593679/12960000\) and \(23681407/2657205000\) at the least permitted \(N\) for each test.
For the last \(N=7\) quartic, the consecutive values at \(-2,-3/4,7/8,7/4,2\) are \(-373/16,657/256,-9261/4096,-343/256,-27/16\).
They give the claimed maximum and both decreasing portions of the variation, and the nonconstant coefficients of \(T_4,T_3,T_2,T_1\) are \(-1,5/2,-25/8,93/32\).
After subtracting twice the maximum, the lower bound \(234637667/2176782336\) exceeds the projected increase \(59280474179/714025000000\) at \(M=26/25\).
All three comparisons use \(y<b_*<-1\), on increasing portions of the corresponding test functions.
This proves the \(x=-1\) bounds of \(6/5\) at \(729\) and \(26/25\) at \(2187\), with the stronger \(6/5\) bound at \(2187\) for \(N\ge8\), conditional only on the prescribed moments, signs and strict endpoint at nonzero resultant.

<a id="two-box-review"></a>
## Exact word counts at 243

In the native cyclic product, shifting each input by a constant vector preserves its quotient class, and \(243(\max a-\min a)(\max b-\min b)\) bounds every nonnegative cyclic coefficient strictly below the packing radix.
Reduction of the packed product modulo the radix to the \(243\)rd power minus one implements cyclic wraparound, with an all-maximal digit vector and zero representing the same normalized word.
The odd-order alternating inverse, integral division, sign parity and norm tests give the two stated centers, and every axis and its inverse preserve signs and absolute norms.
Direct one-step costs for all nonconstant generator directions put the displayed 16th and following 17th at \(9099,9169\) and \(7171,7254\) respectively in the scale \(40L+33K\).
The 1,000-start heuristic is reported construction provenance.
I checked its fixed outputs and ranking without replaying its random search.

I replayed the complete native search and separately reconstructed the two centers and units by polynomial arithmetic modulo \(1+z+\cdots+z^{242}\), using rational extended gcd followed by integral coefficient checks.
An independent traversal split the odd- and even-numbered axes into two groups, projected their products modulo \(8{,}000{,}009\) and verified candidate integer dot products.
All modular dot products have nonnegative entries and sums below \(121(8{,}000{,}009)^2<2^{53}\), and positivity makes the residue of \(40L+33K\) a lower bound for its exact value.
The native modulus likewise satisfies its signed 64-bit accumulator bound.
Across \(43{,}046{,}721\) words in each box, \(114,137\) words respectively have \(K=2\), the corresponding signed minima \(L=353,403\) are each unique, and no such word has \(L=0\).
The unique minima of \(40L+33K\) are \(5535,4514\), attained by the centers \((-25,159)\), \((778,-529)\).
The counts refer to exponent words in the displayed boxes.
Existence of a strict two-moment hit elsewhere in either entire orbit is open in these inputs.

<a id="claim-assembly"></a>
## Scope and assembly of C882 v1

At 06:29 UTC on the same date I separately checked the [registered statement](../../claims/Yin_C_G0882_v1.md#statement) and its [complete argument](../../claims/Yin_C_G0882_v1.md#argument) against their fixed inputs.
For the earlier components I used the [review of the full ternary signature calculation](Yin_R_G1107_v3.md#three-power-review), the [square and moment-form finding](Yin_R_G1107_v4.md#square-moment-review) and the [finite exclusion and descent finding](Yin_R_G1107_v4.md#finite-cuts-review) after checking their bindings and hypotheses.

For \(m\ge2\), the \(m-1\) independent parity relations on the full grid give the required signature dimension.
The common reduction at three prohibits independent component torsion signs, so the two possible roots of a totally positive unit differ by global negation.
The pure-two-power hypothesis enters the descent of ratios with equal layer norms.
For a separately specified orbit the square assertion and quadratic test hold for any \(h_0\) with the stated nonvanishing and signs.
Multiplication by \(h_0\) is injective by its nonzero determinant.
For all integral \(K,L\) the eigenvalues \(e(b_j-d/e)h_0(b_j)\) are strictly positive, and the shell equation and the \(K\)-equation imply the \(L\)-equation because \(e>0\).
The determinant test selects exactly the units, and a nonpositive shell target admits none.
This proves the asserted finiteness for elements of the specified orbit in \(\mathcal O\).

For the finite deductions, multiplication by \(D=B_{n-1}\) has determinant \(\pm1\), so the absolute norm of the input equals the absolute resultant in the cited sieves.
The logarithmic cuts used here all have two nonempty sign blocks.
The strict endpoint excludes the five profiles at \(27,81\) for the prescribed norms, and at \(243\) the two surviving strata exhaust the obligatory \(x=0\) case at \(\Delta=2^{53}\).
The smaller of their two strict exterior lower bounds is \(83/50\).
At \(729,2187\) the only profiles allowed by the endpoint test are \(0,-1\), and the strict lower bounds common to both profiles are \(6/5,26/25\), respectively.
Integrality of the actual third moment and the two original prescribed moments suffice for the split into cases.
This verifies both parts of C882 v1, including the second \(243\) stratum, for precisely its stated norms and cuts.
The two sampled boxes play no role in this deduction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Exterior costs](#exterior-cost-review) | independently reviewed |
| [Two boxes](#two-box-review) | independently reviewed |
| [C882 assembly](#claim-assembly) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Exterior costs](#exterior-cost-review) | [Third moment](../../ledger/Yin_L_G0464_v12.md#third-moment) | Layer and full-grid products, midpoint obstruction and two integral bounds at 243. |
| [Exterior costs](#exterior-cost-review) | [Exterior pairing](../../ledger/Yin_L_G0464_v12.md#pairing) | All roots with multiplicity, variation and full-lift bounds on both orbits. |
| [Exterior costs](#exterior-cost-review) | [Cubic test](../../ledger/Yin_L_G0464_v12.md#cubic) | Both larger conductors at \(x=0\) and any nonzero resultant. |
| [Exterior costs](#exterior-cost-review) | [Negative profile](../../ledger/Yin_L_G0464_v12.md#negative-one) | Endpoint and product, strict Cauchy–Schwarz, quartic comparisons and all surviving \(N\) at 729 and 2187. |
| [Two boxes](#two-box-review) | [Conductor-243 results](../../computations/programs/Yin_J_G0150/readme.md#two-orbits-243) | Fixed axes and centers, both complete boxes, counts, signed minima and uniqueness. |
| [Two boxes](#two-box-review) | [Conductor-243 program](../../computations/programs/Yin_J_G0150/ternary243.py) | Integral quotient arithmetic, center norms, exhaustive modular screens and exact candidate verification. |
| [C882 assembly](#claim-assembly) | [C882 statement](../../claims/Yin_C_G0882_v1.md#statement) | Entire fixed statement, including arbitrary prescribed orbit, two-power layer classification and all five finite cases. |
| [C882 assembly](#claim-assembly) | [C882 argument](../../claims/Yin_C_G0882_v1.md#argument) | Complete argument, applicability of the earlier fixed signature, square, norm and endpoint findings, and exterior bounds established above. |
