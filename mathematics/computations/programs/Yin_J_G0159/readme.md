---
author: Yin
---

# Long odd-grid prefix completion and validated grid obstructions

<a id="question"></a>
## Question and scope

This bounded construction test belongs to [S4](../../../strategies/Yin_S_G0004.md#post-commutator-allocation) and the unchanged [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract).
It uses the exact input and full-measure implication of [C881 v3](../../../claims/Yin_C_G0881_v3.md#statement).
Fix \(x=0\), one terminal negative residue and coefficient prefix length \(L=140\).
The first cell uses \(p=401,n=200\); the subsequent construction test uses \(p=2003,n=1001\) after the first cell's obstruction was identified.
In either cell the canonical coordinate is \(h=\sum_{i=0}^{n-1}a_iE_i\), with \(a_0=2\), odd \(a_i=0\), and positive even \(a_i=4\) through index 138.
There are respectively 61 and 862 free tail coefficients.
The later conductor-1009 test preserves this prefix and cut while reducing the free tail to 365 coefficients and its specified-jet branch to 363 dimensions.
Its separate inputs and necessary-jet calculation are retained [below](#p1009-branch).

The required signs are \(h(b_j)>0\) for \(1\le j<n\) and \(h(b_n)<0\), where \(b_j=2\cos(2\pi j/p)\).
The exact endpoint is
\[
P(-1)=280+\sum_{i=139}^{n-1}(-1)^ia_i,
\]
so its integer condition is that the displayed sum be at least \(-279\).
Any actual integer input satisfying these conditions has \(1<M(P)\le568^{1/35}<6/5\), using the [adopted endpoint-nontorsion theorem](../../../claims/Yin_C_G0881_v8.md#decision-endpoint-nontorsion-nonreal-pair) for the strict lower inequality.
That theorem excludes a cyclotomic integer output in this precise single-negative-node zero-profile domain; it does not supply an integer input or apply integer conjugacy to a nonintegral rational witness.
The known real obstruction in C881 v3 concerns three negative residues at conductor 401 and does not by itself exclude the one-negative-node cell.
The new [C881 v5 argument](../../../claims/Yin_C_G0881_v5.md#real-grid-certificate) supplies a separate one-negative-node obstruction, with its actual adoption and review owned by that Claim.

The first test is numerical linear feasibility in the unbounded real tail, followed at conductor 2003 by a bounded integer search in a stated coefficient box.
Use sine coordinates \(\sin(\theta_j)h(b_j)=\sum_i a_i\sin((i+1)\theta_j)\) to keep row coefficients bounded; \(\sin(\theta_j)>0\) throughout the grid.
A common positive sine margin is a sufficient numerical search target, not an exact replacement for every strict integer sign condition.
Numerical infeasibility is not an exact mathematical exclusion.
An integer candidate must be checked with interval signs, its exact endpoint and prefix, and its complete nonneutral core before being used as evidence of a new small value.

## Files

| File | Role |
| --- | --- |
| [prefix_cell.py](prefix_cell.py) | Fixed-cell numerical LP/MIP proposal and interval/exact candidate checks. |
| [Conductor-nine control](../../outputs/Yin_J_G0159/control.json) | Retained known chamber input, exact lift, endpoint and jet checks, and validated signs. |
| [Conductor-401 LP](../../outputs/Yin_J_G0159/prefix_cell_lp.json) | Unbounded real-tail optimization and complete numerical observations. |
| [grid_certificate.py](grid_certificate.py) and [certificate output](../../outputs/Yin_J_G0159/grid_certificate.json) | Exact root-index witness and validated negative functional, independent of the solver output. |
| [Independent grid checker](checks/grid_polynomial_independent.py) and [independent output](../../outputs/Yin_J_G0159/grid_independent.json) | Standard-library dyadic intervals, monomial expansion and exact arcsine moments, reviewed in [R1107 v30](../../../audits/reviews/Yin_R_G1107_v30.md#integer-jets-grid-certificate-review). |
| [Conductor-2003 real LP](../../outputs/Yin_J_G0159/prefix_cell_lp_p2003.json) | Positive numerical margin and validated rational proposal. |
| [Fixed rational coefficients](inputs/real_p2003_coefficients.json), [verify_real.py](verify_real.py) and [verification](../../outputs/Yin_J_G0159/real_p2003_verification.json) | The exact selected real witness and its optimizer-free sign, endpoint and prefix verification. |
| [Independent real-cell checker](checks/real_cell_independent.py) and [independent output](../../outputs/Yin_J_G0159/real_cell_independent.json) | Separate full-polynomial construction and 2048-bit Clenshaw verification, with the finite models and limits inspected in [R1107 v31](../../../audits/reviews/Yin_R_G1107_v31.md#j159-finite-real-evidence-review). |
| [Conductor-2003 integer test](../../outputs/Yin_J_G0159/prefix_cell_integer_p2003.json) | The first coefficient-box search with its actual timeout and absence of a valid solution. |
| [Specified-jet integer test](../../outputs/Yin_J_G0159/prefix_cell_integer_p2003_Q0_0_Qp_neg1.json) | The same box with Q0 equal to zero and Qprime equal to minus one; a second timeout without a valid solution. |
| [Q0 lower](../../outputs/Yin_J_G0159/prefix_cell_lp_p2003_q0-min.json), [Q0 upper](../../outputs/Yin_J_G0159/prefix_cell_lp_p2003_q0-max.json), [Qprime lower](../../outputs/Yin_J_G0159/prefix_cell_lp_p2003_qprime-min.json), [Qprime upper](../../outputs/Yin_J_G0159/prefix_cell_lp_p2003_qprime-max.json) | Numerical jet extrema, with Q0 fixed to zero in the two derivative tests. |
| [jet_lattice.py](jet_lattice.py), [configuration](inputs/jet_lattice.json) and [output](../../outputs/Yin_J_G0159/jet_lattice.json) | Exact selected-jet coordinates, a real branch LP and the completed six-start integer repair. |
| [Rational branch witness](inputs/jet_lattice_real.json) and [optimizer-free verification](../../outputs/Yin_J_G0159/jet_lattice_real_verification.json) | The retained exact rational point on Q0 equal to zero and Qprime equal to minus one, with all original signs and the endpoint checked. |
| [Conductor-1009 LP](../../outputs/Yin_J_G0159/prefix_cell_lp_p1009_Q0_0_Qp_neg1.json), [exact correction program](jet_p1009_witness.py), [corrected input](inputs/jet_p1009_witness.json) and [verification](../../outputs/Yin_J_G0159/jet_p1009_verification.json) | The separate lower-dimensional rational branch, exact last-two-coordinate correction and original-domain checks. |
| [Conductor-1009 integer test](../../outputs/Yin_J_G0159/prefix_cell_integer_p1009_Q0_0_Qp_neg1.json) | One bounded coefficient-box test on the verified rational branch, ending at the time limit without a valid solution. |
| [Independent jet-branch checker](checks/jet_branches_independent.py) and [independent output](../../outputs/Yin_J_G0159/jet_branches_independent.json) | Complete exact lifts, both rational branch witnesses, conductor-1009 applicability and strict interval counterexamples for the six saved repair points, with actual scope in [R1107 v34](../../../audits/reviews/Yin_R_G1107_v34.md#j159-jet-branches-review). |

## Reproduction

Run from the repository root with Python 3.14.7, NumPy 2.5.4, highspy 1.15.1 and python-flint 0.9.0 available.
The local test reuses the installed NumPy/HiGHS packages under the ignored J144 trace56_packages directory and python-flint under J156 packages, through PYTHONPATH.
The grid certificate and fixed real-witness verifier require only python-flint beyond the standard library.
The executed initial commands are:

    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode control
    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode lp
    python -B mathematics/computations/programs/Yin_J_G0159/grid_certificate.py
    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode lp --p 2003 --seconds 60
    python -B mathematics/computations/programs/Yin_J_G0159/verify_real.py
    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode integer --p 2003 --seconds 60 --coefficient-bound 16 --margin 0.0000001
    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode integer --p 2003 --seconds 60 --coefficient-bound 16 --margin 0.0000001 --q0 0 --qprime -1
    python -B mathematics/computations/programs/Yin_J_G0159/checks/grid_polynomial_independent.py --author-output mathematics/computations/outputs/Yin_J_G0159/grid_certificate.json

For the four completed jet optimizations, use the conductor-2003 LP command with --objective q0-min, q0-max, qprime-min or qprime-max.
The derivative objectives additionally impose the exact linear equality Q0 equal to zero in their numerical model.
The numerical sign inequalities for jet extrema are closed, and the endpoint is at least one; these relax the strict conditions needed by an integer candidate.
The second integer branch adds Q0 equal to zero and Qprime equal to minus one.
The independent grid checker requires only the Python standard library.

The program records actual dependency versions, solver controls, tolerances, requested jets and finite limits in its output.
It uses one solver thread, seed zero and primal, dual and mixed-integer feasibility tolerances of \(10^{-9}\).
The integer searches impose a sine margin of \(10^{-7}\), so they search a sufficient strict-sign subset of the coefficient box.
Their 60-second limit is a solver limit, not a strict end-to-end wall limit.
Exact integer proposals are rechecked at 256-bit Arb precision and would use the existing [complete J156 evaluator](../Yin_J_G0156/sampler.py) for all factors and root multiplicities.
No newly found integer proposal has reached that full-measure evaluation branch.
Default outputs belong to this J's ignored output home and do not depend on the caller's working directory.

<a id="results"></a>
## Results and limits

The conductor-nine control passes with \(h=2E_0+2E_3\), exact endpoint two and jets \(Q(0)=0,Q'(0)=-3\).
It is a retained small control, not a conductor-2003 input.

At conductor 401 the numerical optimal common sine margin is approximately \(-11.2668660289\).
The separate root-index certificate then gives the validated bound \(-56<\mathcal F<-55\), with the complete real-infeasibility argument retained in C881 v5.
Its complete [independent review](../../../audits/reviews/Yin_R_G1107_v30.md#integer-jets-grid-certificate-review) includes a separately implemented exact enclosure inside the author's reported aggregate ball.
That review does not cover the exploratory LP/MIP implementation or larger-conductor observations.
No integer search was launched in that cell.

At conductor 2003 the numerical optimized margin is approximately \(0.00097497898\).
The exact rational coefficients saved from that proposal pass every strict grid sign, the prescribed prefix and the positive endpoint under interval/exact verification.
Their endpoint is exactly \(3027458616443292296351/10^{19}\).
The free real coefficients lie approximately between \(-8.020\) and \(10.561\).
These coefficients are not all integers; clearing their denominators is not a construction with unchanged complete measure.
The [independent finite finding](../../../audits/reviews/Yin_R_G1107_v31.md#j159-finite-real-evidence-review) verifies every original sign, the complete polynomial and exact prefix/endpoint; all 862 free coefficients are nonintegral and the full polynomial's minimum denominator is exactly \(10^{19}\).
That finding also checks the two timeout records and four numerical extrema at their stated finite, uncertified-optimization scope.

The first integer search uses all 862 free integer coefficients in \([-16,16]\), with the stated positive sine margin and endpoint row.
It returns the solver time-limit status without a valid solution, after about 61.1 seconds for the model construction and solver call.
This is neither a certificate of integer infeasibility nor a completed enumeration of that box.

The four later numerical extrema are:

| Quantity | Numerical minimum | Numerical maximum | Added condition |
| --- | --- | --- | --- |
| \(Q(0)\) | approximately \(-0.00707159\) | approximately \(0.02128532\) | None beyond the closed sign and endpoint relaxation. |
| \(Q'(0)\) | approximately \(-4.49713591\) | approximately \(0.01404475\) | \(Q(0)=0\). |

These are floating-point observations, not validated enclosures or adopted bounds on every feasible input.
They motivate a direct integer search on the branch \(Q(0)=0,Q'(0)=-1\), without excluding other jets on numerical evidence.
That second search also returns the solver time-limit status without a valid solution, after about 61.6 seconds for model construction and the solver call.
It uses the same coefficient box, strict sine margin and endpoint condition, and supplies no integer infeasibility certificate.
This is an exploratory fixed-cell construction test, not an adaptive-sampling comparison, a proof of integer infeasibility, or a sequence of positive measures tending to one.
The interval and exact checks, once performed on an actual candidate, cover only that candidate.

<a id="jet-lattice-result"></a>
## Exact-coordinate branch and finite repair

The [proved complete affine coordinates](../../../claims/Yin_C_G0881_v6.md#complete-affine-branches) describe the entire selected integer branch as
\[
C_{\rm free}=2-862t+t^2R,\qquad
R=\sum_{j=0}^{859}u_jB_j\in\mathbb Z[t]_{\le859}.
\]
The parameterization enforces \(Q(0)=0,Q'(0)=-1\) exactly and imposes no original coefficient box.
Both exceptional multiplication columns at indices zero and one are included.
Its endpoint is \(P(-1)=2006+4\sum_j(-1)^ju_j\), so a positive integer endpoint is at least two.

The completed real LP in these coordinates supplies a rational point passing all 1001 original strict signs and both exact jets, with endpoint
\[
\frac{339957315800243528021}{250000000000000000}>0.
\]
The serialized witness has also passed an actual optimizer-free verification.
It proves nonemptiness of this rational branch, not integer supply.
The LP's reported margin near 0.000853632 is only a numerical proposal statistic.

The fixed configuration uses a 45-second LP limit, a 45-second soft repair limit, at most six starts, at most 400 descent iterations per start and eight kicks per start, with seed 20261110.
Integer coordinate changes preserve the two jets and alternate between the original squared negative-part loss and that loss after division by the squared trace nodes.
All six starts finish after 1118 accepted coordinate moves and approximately 14.01 repair seconds, each exhausting its permitted kicks.
No point satisfies all original signs.
The point selected by the common unscaled loss has maximum original coefficient magnitude 14, exact endpoint 1170 and 490 nonpositive numerical sign rows.
Its original Arb sign check also fails, so it is not an admissible candidate and no full Mahler evaluation is invoked.
The initial rounding has 456 failed rows: reducing this squared loss softens large violations but does not minimize the number of failed signs.
The complete finite observations are:

| Start | Loss scaling | Accepted moves | Minimum signed sine | Nonpositive sign rows | Exact endpoint |
| --- | --- | --- | --- | --- | --- |
| 0 | Original | 137 | -34.30286791 | 490 | 1170 |
| 1 | Divide by \(b_j^2\) | 94 | -63.56195582 | 515 | 1050 |
| 2 | Original | 186 | -23.35069022 | 512 | 1266 |
| 3 | Divide by \(b_j^2\) | 239 | -65.72332623 | 538 | 1234 |
| 4 | Original | 206 | -22.41653449 | 501 | 1174 |
| 5 | Divide by \(b_j^2\) | 256 | -58.01229654 | 539 | 1262 |

The selected start-zero loss is approximately 29077.49; selection uses neither the largest minimum margin nor the fewest failed rows.
The initial minimum signed sine is approximately -104.26.
The other five starts are also not admissible proposals.
The finite repair does not enumerate the branch or prove infeasibility.
The [independent branch finding](../../../audits/reviews/Yin_R_G1107_v34.md#j159-jet-branches-review) verifies this new rational witness and complete polynomial, and rigorously rejects all six saved repair points by interval counterexamples.
Its complete interval check of the selected point confirms exactly 490 opposite strict signs.
This finding is separate from R1107 v30's grid certificate and v31's earlier rational witness.

The exact numerical-conditioning identity is
\[
\sin\theta_k E_{n-1-j}(b_k)
 =(-1)^{k+1}\sin((j+1/2)\theta_k).
\]
It follows by substituting \((n-j)\theta_k=\pi k-(j+1/2)\theta_k\) in the E-basis sine formula.
Multiplication of the corresponding C column by \(t^2\) multiplies its value at a grid node by \(b_k^2\), giving the implemented closed column before the required residue sign is applied.
The actual comparison with the local integer transformation of the original sine matrix differs by at most \(2.718\cdot10^{-12}\); this is a floating implementation control, not a sign certificate.
Direct monomial controls check both boundary columns and the first seven ordinary columns, and an exact 860-coordinate integer round trip checks the transform, jets, endpoint and full reciprocal lift.
The repair's proposed finite coordinate moves need not include every improving integer displacement, so failure supplies no coordinatewise optimality theorem.

Run the retained configuration and the optimizer-free witness check from the repository root:

    $env:OPENBLAS_NUM_THREADS = '1'
    $env:OMP_NUM_THREADS = '1'
    python -B mathematics/computations/programs/Yin_J_G0159/jet_lattice.py
    python -B mathematics/computations/programs/Yin_J_G0159/jet_lattice.py --verify-real mathematics/computations/programs/Yin_J_G0159/inputs/jet_lattice_real.json

These were the environment settings used by both branch runs; the program additionally requests one HiGHS thread.
No separate runtime measurement of the BLAS thread pool was made.

<a id="p1009-branch"></a>
## Conductor 1009: the remaining nonneutral jet and a rational witness

Fix \(p=1009,n=504,x=0,\kappa=1,L=140\).
The following applicability calculation uses the [quadratic-kernel identities](../../../claims/Yin_C_G0881_v7.md#weighted-identities) with \(m=35\) and \(c=-49999/25000=-2+1/25000\).
The elementary node comparisons are
\[
b_{504}+2<\left(\frac{22}{7p}\right)^2<\frac1{25000},\qquad
b_{503}+2>\left(\frac9p\right)^2-\frac1{12}\left(\frac9p\right)^4>\frac1{25000}.
\]
Thus \(b_{504}<c<b_{503}\) and \(-2<c<-1\).
The zero-jet estimate gives \(|Q(0)|<3033/171465<1\), so an integer input must have \(Q(0)=0\).

Here the nearest positive and negative nodes are \(b_{252}=2\sin(\pi/(2p))\) and \(b_{253}=-2\sin(3\pi/(2p))\).
Using the elementary \(\pi>31/10\) proof in C881 v7 and the same sine Taylor inequalities gives
\[
b_{252}>\frac{31}{10p}-\frac{29791}{24000p^3}>\frac1{326},\qquad
|b_{253}|>\frac{93}{10p}-\frac{804357}{24000p^3}>\frac1{109}.
\]
The final rational comparisons reduce to
\(16\cdot2400p^2>29791\cdot326\) and \(47\cdot2400p^2>804357\cdot109\).
Every reciprocal \(X=1/b_j\) therefore satisfies \(-109<X<326\), hence \(X^2<35534+217X\).
The same probability weights have \(\mathbb EX=1/|c|<1\), giving \(0<\mathbb EX^2<35751\).
Since \(B_{504}(0)=1\), \(0<\mathcal A_{35}<1\), and \(\mathcal J_{35}=6/171465\),
\[
-2<-\frac{214506}{171465}
 <Q'(0)<1.
\]
Thus the only integer derivative values are \(-1,0\).
With the strict endpoint, the zero derivative forces complete measure one by the same double-factor argument.
Every nonneutral integer input in this fixed cell must consequently have exactly \(Q(0)=0,Q'(0)=-1\).
This calculation supplies a necessary restriction for the search; it does not assert that the branch contains an integer point.

The free tail is every integer polynomial in the basis \(B_0,\ldots,B_{364}\), with 365 coefficients.
The fixed part is
\[
Q_{\rm fix}=tB_{504}+2B_{503}+4\sum_{r=1}^{69}B_{503-2r},
\qquad Q_{\rm fix}(0)=2,\quad Q'_{\rm fix}(0)=365.
\]
The same value/derivative recurrences and alternating sums used in C881 v6 give these exact constants.
Subtracting the constant and linear terms therefore gives the entire 363-dimensional integer branch
\[
C_{\rm free}=-2-366t+t^2R,\qquad R\in\mathbb Z[t]_{\le362}.
\]
Its baseline is \(364B_0-366B_1\), and its exact endpoint is \(P(-1)=-450-4R(-2)\).
The negative sign here follows from \(P(-1)=-Q(-2)\), because \(n+1=505\) is odd.
No conductor-2003 coordinate vector or witness is transported into this different input.

One LP call with the original proposer returns a numerical positive margin near 0.0001238759751 and a directly recomputed minimum near 0.0001238759666.
The raw decimal-to-rational proposal has
\[
Q(0)=-\frac{624399}{50000000000000000},\qquad
Q'(0)=-\frac{199999999992496431}{200000000000000000}.
\]
The [correction program](jet_p1009_witness.py) changes only the last two free coordinates, which multiply \(B_1=t+1\) and \(B_0=1\):
\[
\Delta a_{502}=-\frac{7503569}{200000000000000000},\qquad
\Delta a_{503}=\frac{2000233}{40000000000000000}.
\]
These exact corrections force both jets, preserve the prescribed prefix and change the endpoint by \(\Delta a_{502}-\Delta a_{503}\).
The [saved corrected input](inputs/jet_p1009_witness.json) passes all 504 original strict signs at 256-bit Arb precision, with exact endpoint
\[
P(-1)=\frac{20721501956983266601}{50000000000000000}>0.
\]
Its coefficients are not all integers.
The preparation result is [retained](../../outputs/Yin_J_G0159/jet_p1009_preparation.json), and the serialized input has passed the [optimizer-free verification](../../outputs/Yin_J_G0159/jet_p1009_verification.json).
This proves real rational feasibility at the reduced dimension, without proving strict complete measure for this nonintegral witness or supplying an integer point.
For an actual integer input satisfying these same original conditions, [C881 v8](../../../claims/Yin_C_G0881_v8.md#construction-consequence) now supplies strict complete measure, so the necessary derivative minus one applies to every integer sign-and-endpoint solution in this cell.
This new structural implication has its own [complete independent review](../../../audits/reviews/Yin_R_G1107_v35.md#endpoint-nontorsion-nonreal-pair-review), separate from the finite witness review.

The actual LP and fixed-input verification commands are:

    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode lp --p 1009 --q0 0 --qprime -1 --seconds 60
    python -B mathematics/computations/programs/Yin_J_G0159/jet_p1009_witness.py

The verifier's optional --prepare-from mode reconstructs the selected last-two-coordinate correction from the actual LP output and refuses to overwrite an existing selected input.
Ordinary reproduction uses the already retained exact input and requires no new LP run or removal of that witness.
The [independent branch finding](../../../audits/reviews/Yin_R_G1107_v34.md#j159-jet-branches-review) checks the complete conductor-1009 applicability argument, full integer lattice, exact correction and every original strict sign.
It also verifies the entire polynomial, whose minimum common denominator is exactly \(2\cdot10^{17}\), and confirms that all 365 free canonical coefficients are noninteger.

After that rational verification, one integer test used all 365 free canonical coefficients in \([-16,16]\), requested jets \((0,-1)\), the positive endpoint row and common sine margin \(10^{-7}\).
It used the unchanged proposer's one HiGHS thread, seed zero, \(10^{-9}\) primal/dual/MIP tolerances and 60-second solver limit, with the same OPENBLAS_NUM_THREADS and OMP_NUM_THREADS settings above.
The [actual output](../../outputs/Yin_J_G0159/prefix_cell_integer_p1009_Q0_0_Qp_neg1.json) reports the time limit and no valid solution after approximately 60.13 seconds for model construction and the solver call.
No integer candidate was returned, so neither candidate interval checking nor the complete J156 evaluator ran.
This was one call, without a retry or a larger box, and proves no infeasibility of the finite box or the full branch.
The required numerical margin additionally restricts the original strict sign conditions.

    python -B mathematics/computations/programs/Yin_J_G0159/prefix_cell.py --mode integer --p 1009 --q0 0 --qprime -1 --seconds 60 --coefficient-bound 16 --margin 0.0000001

The completed comparisons leave simultaneous integer realization of the full original sign system as the next unresolved step.
The squared-loss repair did not supply a suitable margin, and the shorter cell's timeout does not justify simply enlarging its limit.
