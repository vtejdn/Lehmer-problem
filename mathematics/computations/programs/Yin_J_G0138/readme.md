---
author: Yin
---

# Cyclotomic central-perturbation full-measure probes

## Question and scope

This computation group tests actual integer polynomials Phi_n(z)-c*z^(phi(n)/2) for the unrestricted [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract).
The [growing-profile calculation](#growing-profile-resultant) additionally tests one specified product of cyclotomic factors with a central subtraction, using an exact whole-measure lower bound.
The minus-two program uses c=2 at n=15,105,1155 and compares complete logarithmic Mahler measure with the small positive real exterior root.
The minus-one program uses c=1 at n=35,105,1155, extracts every cyclotomic factor exactly, and estimates the complete remaining measure.
Neither probe assumes Salem geometry or irreducibility.
The assigned external_structural_lead agent developed and inspected this ordinary author computation for Yin.
The original boundary-grid probes have no independent review or certified numerical root isolation.
The later exact trace-root count below is a separate calculation, with its actual inspection scope stated there.

## Minus-two files and reproduction

Run `python mathematics/computations/programs/Yin_J_G0138/main.py` from the repository root.
The retained native program is [main.py](main.py).
The program requires NumPy and SymPy and records their actual versions with the Python version in its generated result.
The retained reproduction used Python 3.14.3, NumPy 2.4.4 and SymPy 1.14.0.
It uses exact integer cyclotomic coefficients and exact factorization only for n=15,105.
It evaluates shifted boundary grids with 2^17, 2^19 and 2^21 points using complex double-precision FFTs.
For degrees at most 48 it also computes floating-point roots, treating modulus greater than 1+1e-7 as exterior and imaginary part less than 1e-7 in magnitude as numerically real.
These thresholds are numerical screens, not certified root counts.
There is no randomness or required prior output.
The replaceable generated result is [results.json](../../outputs/Yin_J_G0138/results.json).

## Minus-two results and limits

The completed interactive probe gave approximate total logarithmic measures 0.64456923, 0.94244 and 1.15160 at the three inputs.
The first two numerical root sums agreed with those approximate totals; their positive real exterior roots contributed approximately 0.32228462 and 0.04671623.
The n=15 polynomial factors exactly as (z^4-z^3-1)(z^4+z-1), while the n=105 factorization returned one irreducible degree-48 factor.
A slow attempted factorization at n=1155 was stopped and supplies no irreducibility conclusion.
The retained program reproduces only the completed factorization scopes and does not repeat that unfinished attempt.
The boundary samples and root calculations have no interval error bounds; mesh refinement is not an error certificate or an asymptotic assertion.
The rigorous no-cyclotomic-factor and total-measure lower bounds belong to [L457](../../../ledger/Yin_L_G0457_v1.md#complete-exterior-root-cost) and do not depend on these numerical observations.

## Minus-one files and reproduction

Run `python mathematics/computations/programs/Yin_J_G0138/center_one.py` from the repository root.
The retained native program is [center_one.py](center_one.py), with its own replaceable output [center_one_results.json](../../outputs/Yin_J_G0138/center_one_results.json).
This program was run successfully with Python 3.14.3, NumPy 2.4.4 and SymPy 1.14.0; it records actual dependency versions in each generated output.
Its only inputs are n=35,105,1155, with c=1 and the exact exponent phi(n)/2.
It records full integer coefficients of the original polynomial and the residual after removing all cyclotomic factors, as well as the complete cyclotomic orders and multiplicities.

For input degree D, an integer totient sieve lists all k<=2D^2 with phi(k)<=D.
The exact bound phi(k)^2>=k/2, proved in the program docstring and [L457 v2](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test), makes this order list exhaustive.
The program generates each possible cyclotomic polynomial over Z and rejects it only when its reduction does not divide the original polynomial modulo two.
Monicity preserves degree and nonvanishing on reduction, so an actual integer cyclotomic divisor cannot be rejected by that filter.
Each modular pass is tested by repeated exact integer division on the residual, and exact multiplication checks reconstruction of the original input.
All actual multiplicities are retained; modular passes alone are never called factors.
Complete rational factorization is then run only on residuals of degree at most 48, covering n=35,105 and excluding n=1155.

The residual is evaluated on shifted boundary grids with 2^17, 2^19 and 2^21 points using double-precision FFTs.
For residual degrees at most 48, floating-point roots are also computed and modulus greater than 1+1e-7 is the exterior screen.
There is no randomness, required prior output, certified numerical interval or certified root count.
The original minus-two program and its results.json output remain separate and unchanged.

## Minus-one results and limits

The completed exact extraction gives cyclotomic degree 14 at n=35 and 105, and degree 34 at n=1155.
The corresponding residual degrees are 10,34,446.
The first two residuals each have one irreducible factor, whereas that original probe did not determine the exact number of irreducible factors of the degree-446 residual.
Its exhaustive cyclotomic exclusion proves that every irreducible factor of that residual has positive measure; its nonzero degree proves there is at least one.
All degrees and factor counts retain multiplicity.
The complete blocks, their justification and the exact trace reduction showing the absence of all exterior real roots belong to [L457 v2](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-trace-reduction).

The finest residual-grid estimates are approximately 0.24965569, 0.41441535 and 0.74500526 respectively.
The first two numerical root sums are approximately 0.2496548880 and 0.4144129341, with two and eight exterior roots in those screens.
Removing cyclotomic factors preserves total logarithmic Mahler measure exactly, but these numerical estimates have no error certificates.
The original probe performed no root computation or complete rational factorization for the degree-446 residual.
The finite estimates establish neither monotonicity nor a positive-to-zero sequence nor a gap throughout the unbounded-prime-count family.
The separately proved bounded-prime-count exclusion is the [sparse completion in L457 v2](../../../ledger/Yin_L_G0457_v2.md#bounded-prime-count-completion), using the existing accepted DS17 statement rather than numerical evidence.

<a id="degree446-exact-root-shape"></a>
## Exact root shape of the degree-446 residual

The retained [core_shape.py](core_shape.py) separately tests the necessary exterior-root count for the [C881 v8 integer prefix cell](../../../claims/Yin_C_G0881_v8.md#nonreal-exterior-pair).
Its complete input is
\[
F(z)=
\frac{\Phi_{1155}(z)-z^{240}}
{\Phi_1^2\Phi_2^2\Phi_3\Phi_4\Phi_5\Phi_6\Phi_8\Phi_{10}\Phi_{12}\Phi_{24}}.
\]
The specified block comes from [L457 v2's exact extraction](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test).
The new program regenerates all coefficients over the integers, verifies exact division and multiplication back to the numerator, and obtains degrees \(480,34,446\) for numerator, block and quotient.
It does not depend on the historical center_one_results.json, which was absent at this calculation's inspection.
The exterior-root conclusion would remain valid even if a cyclotomic factor were omitted from the specified block, because such a factor contributes only unit-circle roots.

The quotient is monic reciprocal with constant coefficient one.
The program constructs \(T\in\mathbb Z[t]\) with
\[
F(z)=z^{223}T(z+z^{-1})
\]
using \(z^k+z^{-k}\), and separately reconstructs every coefficient of \(F\) from the binomial expansion of this lift.
It checks a squarefree decomposition by multiplication, derivative gcds and pairwise gcds, restoring every factor multiplicity in the final count.
For each squarefree factor it forms the exact signed Euclidean Sturm chain.
The applicable standard theorem and positive-scaling convention are [PRT22-U001](../../../audits/literature/PRT22/Yin_U001.md#prt22-u001), restricted to squarefree polynomials and nonzero endpoint values.
It clears only positive rational denominators and positive coefficient contents, so every resulting chain element is a positive scalar multiple of the corresponding ordinary Sturm element.
Zeros in sign lists are deleted before counting variations.
Signs at infinity use the exact leading coefficient and degree; no approximate root or angular grid is used.

The completed run, with Python 3.14.7 and python-flint 0.9.0, found one squarefree trace component of degree 223 and multiplicity one.
Its endpoint values are \(T(-2)=-576\) and \(T(2)=192\).
The exact variations are
\[
\begin{array}{c|rrrr}
t&-\infty&-2&2&+\infty\\ \hline
V_T(t)&171&171&52&52.
\end{array}
\]
Consequently all 119 real trace roots lie in \((-2,2)\), and the remaining 104 trace roots are nonreal.
A real trace in \((-2,2)\) lifts to two unit-circle roots.
A nonreal trace lifts to reciprocal roots whose moduli straddle one, since a unit-circle root would have real trace.
The lift is nonsingular away from \(z=\pm1\), which are excluded by the endpoint values.
Thus the complete quotient has exactly
\[
\boxed{104\text{ exterior roots},\quad104\text{ interior roots},
       \quad238\text{ unit-circle roots}},
\]
counting multiplicities.

This rejects this entire quotient as an input for C881 v8, whose original integer conditions force exactly two exterior roots.
For every positive integer \(k\), every sign \(\varepsilon\) and every cyclotomic product \(H\), the actual polynomial \(H(z)F(\varepsilon z^k)\) has \(104k\) exterior roots and fails the same necessary condition.
This statement concerns complete products, not a selected unknown factor of \(F\).
The root-count calculation uses no irreducible factorization of \(F\), exact Mahler value or conductor-dependent endpoint comparison, and asserts no conclusion for another \(N\).
The separate factorization and complete-measure follow-up are recorded below.
The failure therefore supplies no universal exclusion of the unbounded-prime-count family.

<a id="core-shape-controls"></a>
## Small trace controls and reproduction

The same program checks the exact trace inputs
\[
\begin{split}
T_{10}(t)&=t^5-t^4-5t^3+4t^2+5t-1,\\
T_{18}(t)&=t^9+t^8-8t^7-8t^6+20t^5+19t^4-16t^3-13t^2+2t+1.
\end{split}
\]
They correspond to the [degree-ten central-minus-one factor](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test) and the [degree-eighteen J144 control](../Yin_J_G0144/trace_control.py).
The exact chain counts are respectively three and seven real trace roots, all in \((-2,2)\), with one nonreal conjugate trace pair in each case.
The program also verifies \(\operatorname{disc}(T_{10})=-18583\), the derivative coefficient bounds
\[
\sum_{j\ge1}j|[t^j]T_{10}|2^{j-1}=193,\qquad
\sum_{j\ge1}j|[t^j]T_{18}|2^{j-1}=10902,
\]
and the integer inequalities \(484\cdot193<49\cdot45^2\) and \(484\cdot10902<49\cdot329^2\).
These controls do not repeat the existing J144 Rouché full-measure certificate.

With python-flint available, run the following from the repository root.

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/core_shape.py
~~~

It uses no randomness, NumPy, SymPy or prior generated output.
The replaceable [core_shape.json](../../outputs/Yin_J_G0138/core_shape.json) retains all original, block, quotient and trace coefficient vectors, squarefree factors with multiplicities, exact chain degree and sign lists, controls and dependency versions.
The rational remainder chains are regenerated from those exact inputs rather than retained as large coefficient arrays.
The output is published atomically only after the assertions succeed.
The [independent root-shape finding](../../../audits/reviews/Yin_R_G1107_v36.md#degree446-root-shape-review) checks the complete calculation, both controls and the stated product exclusions.
Its [separate checker](checks/core_shape_independent.py) regenerates the integer input by Möbius products, extracts the trace by triangular subtraction, and uses positive-pivot integer pseudo-remainders without importing the author program.
The actual [independent output](../../outputs/Yin_J_G0138/core_shape_independent.json) retains the regenerated coefficients and exact chain data.

<a id="degree446-factor-and-measure"></a>
## Complete factorization and Mahler enclosure of the same quotient

The separate [core_factors.py](core_factors.py) resolves whether an individual rational factor of this rejected whole quotient might need a different small-measure test.
It regenerates the same numerator and specified block exactly, verifies division and reconstruction, and calls FLINT's complete integer polynomial factorization.
The completed calculation returns one monic irreducible factor of degree 446 with multiplicity one and content one.
The multiplication check verifies the returned product; the irreducibility assertion additionally relies on FLINT's factorization implementation, not on multiplication alone.
This updates the earlier unresolved factor-count question for this fixed input without altering the recorded scope of the old probe.

The optional complete-measure mode reuses the [J156 evaluator](../Yin_J_G0156/sampler.py), whose full-product mechanism has an [existing implementation review](../../../audits/reviews/Yin_R_G1111_v1.md#sampler-implementation-review).
It evaluates every root with multiplicity using Arb at 128 bits, contributing the modulus for an exterior ball, one for an interior ball, and the union of the modulus ball with one whenever that ball meets one.
It verifies that all 446 roots are accounted for.
The new completed evaluation gives
\[
2.10642510401468<M(F)<2.10642510401469.
\]
The exact dyadic enclosure endpoints in the generated certificate are
\[
\left[
11199676877121866471859162193023596083\,2^{-122},
44798707508487465887436648772094384723\,2^{-124}
\right].
\]
Both endpoints lie strictly between the displayed decimal rationals.
In particular, this entire irreducible input has \(M>6/5\), independently of its failure of the prefix cell's root count.
There is no proper rational factor to recover as a separate small-measure candidate.
The existing J156 review covers the reused method, not this newly evaluated input or its numerical result.
The [independent factorization and measure finding](../../../audits/reviews/Yin_R_G1107_v36.md#degree446-factor-measure-review) checks these new results on independently regenerated coefficients.
It matches all 446 root enclosures at 256 bits and combines the exact root count with the 104 strictly exterior moduli to enclose the complete measure strictly inside the original dyadic interval.
The factorization and root-isolation backends remain shared trusted FLINT/Arb inputs, not independently verified implementations.

The two normalized reproduction commands are

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/core_factors.py --timeout 60
python -B mathematics/computations/programs/Yin_J_G0138/core_factors.py --measure --timeout 60
~~~

The completed runs used Python 3.14.7 and python-flint 0.9.0.
The child computation has a 60-second cap; a timeout yields no completed factorization or measure conclusion.
The factor-only and complete-measure outputs are respectively [core_factors.json](../../outputs/Yin_J_G0138/core_factors.json) and [core_measure.json](../../outputs/Yin_J_G0138/core_measure.json), published atomically.
Both are generated from the program's fixed exact input, with no prior output required.
The complete-measure mode additionally requires the retained cross-J evaluator named above.
It records all exact factor coefficients, root balls, complete dyadic measure intervals, multiplicities and dependency versions.

<a id="growing-profile-resultant"></a>
## Exact whole-measure rejection of a changed neutral profile

The separate [growing_profile_resultant.py](growing_profile_resultant.py) evaluates only
\[
 A(z)=\Phi_{60}(z)\Phi_{84}(z)\Phi_{140}(z),\qquad
 P(z)=A(z)(1+z+\cdots+z^{922})-z^{505}.
\]
It regenerates all coefficients over the integers, obtains degree \(1010\), checks monicity and reciprocity, and verifies \(P(1)=922\), \(P(-1)=2\).
The first four coefficients are \((1,1,4,4)\), and \((1-z)P-A\) vanishes through coefficient index \(504\).
Thus \(P\) agrees with the changed rational neutral reference \(A/(1-z)\) through that index; this is not a claim that it agrees with the original fixed zero profile at every index.

For \(m=2053\) the program computes the exact integer
\[
 R=\left|\operatorname{Res}(P,z^m-1)\right|>0.
\]
Writing every root of \(P\), with multiplicity, as \(\alpha_i\), the elementary bound
\[
 |\alpha_i^m-1|\le2\max\{1,|\alpha_i|\}^m
\]
gives \(R\le2^{1010}M(P)^m\).
The completed exact integer comparison is
\[
 R\,4^{2053}>2^{1010}11^{2053},
 \qquad\text{hence}\qquad M(P)>11/4>6/5.
\]
This lower bound charges the complete original polynomial and every factor multiplicity.
No factor was discarded, and no root approximation or quadrature is used.
The computation does not determine the individual measures of proper rational factors.

As a separate author control, the program constructs the integer trace \(Q\) from \(P=z^{505}Q(z+z^{-1})\), then verifies that lift by direct binomial expansion of every trace monomial.
It builds the monic grid polynomial \(B_{1026}\) by \(B_0=1,B_1=t+1,B_k=tB_{k-1}-B_{k-2}\), and checks
\[
 R=922\operatorname{Res}(B_{1026},Q)^2.
\]
Indeed the nontrivial \(2053\)-rd roots of unity occur in inverse pairs; their two evaluations of \(P\) multiply to \(Q(\zeta+\zeta^{-1})^2\), while the remaining root \(1\) contributes \(P(1)=922\).
Both resultant computations use the trusted FLINT implementation; agreement of these transformed calculations is an ordinary author check, not an independent implementation audit.

The output also checks the integer comparison \(2108\cdot5^{126}<6^{126}\) for the conditional neutral-prefix upper bound.
It does not certify that upper bound's strict residue-sign premise.
Its whole-measure rejection above is independent of that premise.
The result concerns this one input and supplies no exclusion of all changing cyclotomic profiles or of their proper factors.
The [construction and exact phase obstructions](../../../ledger/Yin_L_G0457_v4.md#integer-family) retain the wider family, the final-pole restriction and the theorem application separately.

Run the following with python-flint available.

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/growing_profile_resultant.py
~~~

The completed run used Python 3.14.7 and python-flint 0.9.0.
The replaceable [growing_profile_resultant.json](../../outputs/Yin_J_G0138/growing_profile_resultant.json) contains every input and trace coefficient, both exact resultant integers, the comparison parameters, scope and dependency versions.
It requires no prior generated output or randomness and is published atomically after all assertions pass.
The [independent finding](../../../audits/reviews/Yin_R_G1107_v40.md#growing-profile-resultant-review) verifies this fixed input and its complete lower bound.
Its [separate checker](checks/growing_profile_independent.py) constructs the cyclotomic factors by integer binomial quotients, builds \(Q=C_AB_{461}-1\), reconstructs every original coefficient and compares the full exact resultant and both integer inequalities.
It also checks two prime-field resultants by a Python Euclidean recurrence and the exact phase signs at indices 9, 11 and 504.
The full resultant still uses the shared trusted FLINT backend; the two modular controls do not certify that backend or the complete integer on their own.
After generating the author output, run the following to reproduce the independent check.

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/checks/growing_profile_independent.py
~~~

The replaceable [growing_profile_independent.json](../../outputs/Yin_J_G0138/growing_profile_independent.json) contains its exact reconstructed inputs, comparison margins and checking limits.

<a id="all-length-degree-60"></a>
## All geometric lengths for squarefree parents of degree at most 60

For the [central construction](../../../ledger/Yin_L_G0457_v4.md#integer-family), the exact enumeration excludes every strict terminal cut with the required endpoint when \(2d=\deg A\le60\) and \(r>2d+1\) is odd.
Here \(A\) is a squarefree product of cyclotomic polynomials of orders at least three with \(A(z)=1+3z^2+O(z^4)\), and the perturbation subtracts \(z^N\) with \(N=(r-1)/2+d\).
The [native program](central_parent_screen.py) uses integer arithmetic and the Python standard library.
Run it from the project root without other inputs:

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/central_parent_screen.py
~~~

To enumerate the possible orders, the program uses \(\varphi(q)^2\ge q/2\), proved in the [cyclotomic extraction bound](../../../ledger/Yin_L_G0457_v2.md#central-minus-one-exhaustive-cyclotomic-test).
Consequently \(\varphi(q)\le60\) implies \(q\le7200\).
An integer totient sieve finds every such order, and successive monic divisions of \(z^q-1\) by the proper divisor polynomials give each \(\Phi_q\).
The enumeration visits each subset of distinct factors within the degree bound once, multiplying coefficients through degree three and evaluating the full product at \(-1\).
An extension in the ordered subset traversal can only increase degree.

For a given \(p=r+2d-2\), put \(n=(p-1)/2\).
The [order and endpoint restrictions](../../../ledger/Yin_L_G0457_v5.md#parity-reduction) require odd \(n\), \(A(-1)>1\), and \(q\le p\) for every parent order.
At each remaining grid point \(u=j/p\), \(1\le j\le n\), the [residue identity](../../../ledger/Yin_L_G0457_v4.md#residue-formula) gives an immediate obstruction whenever \(W_A(2\pi u)\le0\) at an odd index assigned a positive residue, or \(W_A(2\pi u)\ge0\) at an even index assigned a negative residue.
The sign of \(W_A\) starts positive, reverses upon crossing each primitive parent angle \(a/q\) and each interior sine zero \(k/(2d-2)\), and is zero at exact coincidences with the grid.
The program records crossings and zeros separately using integer division and bit masks.
A cut after \(c\) positive residues must satisfy \(1\le c<n\), with \(c\) at least the last index forced positive and strictly before the first index forced negative.

For each parent, the following finite reduction bounds all lengths that can survive this sign test.
Use \(L=\operatorname{lcm}(2d-2,\{q:\Phi_q\mid A\})\) and list the sign reversals in \((0,L/2)\) in units of \(1/L\).
Cancel paired parent and sine events at the same position, retaining the neighboring weak signs through a common zero.
For each negative interval followed by a positive interval, take the smaller of their two integer lengths, and let \(g\) be the maximum of these values.
The program verifies \(g>0\) for every endpoint-eligible parent enumerated.
If \(p>2L/g\), both open intervals have length greater than two after scaling by \(p/L\).
They therefore contain an odd integer and a later even integer respectively, both in \(1,\ldots,n\).
At the odd index the residue is strictly negative, and at the later even index it is strictly positive, including when the selected grid point hits a common zero.
This excludes every cut for those \(p\).
The program checks the initial range \(2d+1<r\le8d\) in full and extends its loop when the individual ceiling \(\lfloor 2L/g\rfloor\) leaves additional odd lengths.

The author run on Python 3.14.3 found 41,268 parents with the prescribed prefix, all with \(A(-1)>1\).
The initial range contained 3,363,666 parent and length pairs, of which 1,669,258 passed the endpoint, order and parity restrictions.
The sign test rejected every remaining pair before an amplitude calculation was needed.
The largest individual conductor ceiling was 168, and each parent's own ceiling required zero additional odd lengths beyond its initial range.
The [regenerable output](../../outputs/Yin_J_G0138/central_parent_screen.json) gives the aggregate counts and their degree breakdown.
The [independent enumeration](../../../audits/reviews/Yin_R_G1107_v43.md#all-length-screen-review) checks these counts, the sign inversions and the argument covering all remaining lengths.
The exclusion concerns this squarefree central construction and the specified sign and endpoint conditions.
It supplies no measure lower bound for its outputs and leaves parents of higher degree open.

<a id="p21-cubic-witness"></a>
## A conductor-21 cubic correction with matching coefficients through degree seven

Take \(F_2(z)=(1+z^2)^3\), \(r=17\), \(m=8\), \(p=21\), \(n=10\), and use the trace recurrence and poles \(b_j=2\cos(2\pi j/21)\) of [C881 v10](../../../claims/Yin_C_G0881_v10.md#statement).
For \(Q(t)=t^3B_8(t)+t-t^3\) and \(P(z)=z^{11}Q(z+z^{-1})\), the ten residues \(Q(b_j)/B'_{10}(b_j)\) are positive for \(1\le j\le9\) and negative for \(j=10\).
The endpoint ratio is \(Q(-2)/B_{10}(-2)=-2\), and \(Q-tB_{10}\) has degree nine and leading coefficient two.
The reciprocal lift has the exact form
\[
P(z)=F_2(z)\sum_{k=0}^{16}z^k-z^8-2z^{10}-2z^{12}-z^{14}.
\]
Thus \(P-F_2/(1-z)=-z^8+O(z^9)\).

For a rational certificate of the cut, take the disjoint intervals \(((a_j-1)/1000,(a_j+1)/1000)\) in decreasing order, with
\[
(a_1,\dots,a_{10})=(1911,1652,1247,731,149,-445,-1000,-1466,-1802,-1978).
\]
The degree-ten \(B_{10}\) changes sign across every interval, so each contains exactly one \(b_j\) and the derivative there has sign \((-1)^{j-1}\).
Rational root counting finds zero roots of \(Q\) in each interval, and its signs at the left endpoints are \(+,-,+,-,+,-,+,-,+,+\).

The factorization \(P=\Phi_4\Phi_5K\) has
\[
K(z)=z^{16}+2z^{14}+z^{12}+z^{11}+2z^9-z^8+2z^7+z^5+z^4+2z^2+1.
\]
The [exterior-root count](../../../claims/Yin_C_G0881_v10.md#nonreal-pair) gives precisely one exterior conjugate pair, with multiplicity.
Exact complex root counting places one root \(\alpha\) of \(K\) in the rectangle
\[
[-0.05427783,-0.05427782]+i[1.26621203,1.26621204].
\]
Squaring the coordinate bounds gives the whole-polynomial measure \(1.60623898<M(P)=|\alpha|^2<1.60623902\).

The [earlier signed-amplitude family](../../../claims/Yin_C_G0884_v3.md#statement) contains the same neutral lift at its block lengths \((4,17)\).
Its matching parameter must then be \(L=3\), so its correction is \(-\lambda tB_6\), of degree seven for nonzero \(\lambda\), whereas the present correction is \(t-t^3\).
The two integer successes in that classification have conductors 9 and 11.
The computation here certifies the single input above.

From the repository root, run the [native checker](p21_cubic_witness.py) with Python and SymPy (author run with Python 3.14.3 and SymPy 1.14.0).

~~~text
python -B mathematics/computations/programs/Yin_J_G0138/p21_cubic_witness.py
~~~

The checker uses rational endpoints for both real and complex root counts and publishes the [exact residue signs, polynomial and measure bounds](../../outputs/Yin_J_G0138/p21_cubic_witness.json) after all assertions pass.
The [independent certificate](../../../audits/reviews/Yin_R_G1107_v48.md#p21-integer-review) checks the signs by polynomial substitution and locates the exterior root in a rational disk, tightening the full measure enclosure to \(1.6062390014<M(P)<1.6062390015\).
The [degree obstruction at \(p=21\)](../../../ledger/Yin_L_G0457_v8.md#three-node-test) checks that every integral perturbation with a longer prefix fails some required residue sign.
