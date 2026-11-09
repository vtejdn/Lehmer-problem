---
author: Yin
---

# Continuous endpoint duals for the first residual triple

<a id="scope"></a>
## Original question and continuous certificate

This calculation continues the conductor-19683, cut-1990, negative-one branch with K=3, L=4, N=7 and U=1.
It selects only the first residual triple (10,18,27); no computation for the other four triples is asserted here.
The [moving-pair reduction](../../../claims/Yin_C_G0882_v9.md#moving-pair) and [density-cap dual inequalities](../../../claims/Yin_C_G0882_v9.md#endpoint-duals) supply the mathematical interfaces.
The [exploration record](../../../ledger/Yin_L_G0464_v16.md#exact-dual-tests) retains their relation to the original goal.

Write u=(t+2)/4 and reuse the letter w for the transformed occupation density, so 0<=w<=1 on [0,1].
Its first seven moments are determined by the original trace differences and the two residual roots.
The original endpoint integral is J=integral w(u)/u du.
For any rational polynomial q of degree at most six, the two valid dual bounds are
\[
 J\ge\int_0^1q(u)w(u)\,du-\int_0^1(q(u)-1/u)_+\,du,
 \qquad
 0\ge\int_0^1q(u)w(u)\,du-\int_0^1q(u)_+\,du.
\]
The numerical optimization only proposes q; these inequalities concern the whole continuous interval and impose no piecewise-constant restriction on w.

The native [fixed input](inputs/endpoint_first_duals.json) retains four rational polynomials and their proposal locations.
[endpoint_dual.py](endpoint_dual.py) isolates all real roots of u q(u)-1 or q(u) exactly with SymPy, using rational intervals of width at most 10^-14.
On the intervals between consecutive root boxes, exact rational sign tests determine the positive components.
The verifier integrates q exactly by its primitive and encloses any logarithm with 256-bit Arb arithmetic.
On each root box it bounds the positive part above by the box width times an outward upper value, or zero when that upper value is nonpositive.
This also handles the first and last components and repeated roots; a root box crossing the domain boundary is rejected rather than silently clipped.
The resulting penalty is rounded upward to an exact point ball.
Only a strictly positive directed lower comparison certifies an exclusion.

Let F(u) be the primitive of q with F(0)=0, and put f(t)=F((t+2)/4).
The exact moment functional is
\[
 \int_0^1q(u)w(u)\,du
   =f(v_1)+f(v_2)-f(c)-\mathcal D(f).
\]
The rational number D(f) uses all seven original trace differences, with the constant term included.
This formula avoids reconstructing a new density or polynomial from an LP vector.

<a id="fixed-results"></a>
## Four fixed-position certificates

At d=0 and the indicated s, the final verifier proves the following conservative strict lower gaps over the entire inherited cut interval [-1609663/10^6,-1609662/10^6].
For an endpoint certificate the gap is the lower bound for J minus log((2+s)^2/(2+c)).
For the density-cap certificate it is the positive violation of the second dual inequality above.

| s | Certificate | Proved gap greater than |
| --- | --- | --- |
| -15/16 | Endpoint | 0.1709 |
| -489/500 | Density cap alone | 0.000793 |
| -239/250 | Endpoint | 0.00644 |
| -19/20 | Endpoint | 0.0000735 |

These exclude every continuous occupation density at those fixed double-root positions, not merely the earlier step witnesses.
They do not by themselves exclude moving nonreal roots or an entire original residual branch.
The first certificate strengthens the previous failure of one particular genuine-interval configuration.

<a id="moving-cover"></a>
## Moving-pair checks and unresolved cells

[endpoint_cover.py](endpoint_cover.py) evaluates these same four polynomials on moving roots v1,v2=s plus or minus sqrt(d).
On each s cell it shifts F to the exact rational midpoint and uses the symmetric-power recurrence
\[
 S_0=2,\quad S_1=2z,\quad
 S_j=2zS_{j-1}-(z^2-d/16)S_{j-2},
\]
where z is the interval displacement of (s+2)/4 from that midpoint.
Thus the complete sum F((v1+2)/4)+F((v2+2)/4) is enclosed for the same s,d box, including all dependencies and both conjugate roots.
The endpoint comparison uses log(((s+2)^2-d)/(2+c)).
An interval is discarded only when one continuous dual gap is strictly positive over its entire box.
Every unproved comparison leaves the cell unresolved.

The original target check uses 4096 equal closed s cells covering [-6/5,-1/3], the whole d interval [-1/10100,0], and the whole inherited cut interval.
Its first-success counts for the four polynomials are 3739, 203, 66 and 17.
It leaves 71 cells unresolved and does not exclude 1<M(P)<=101/100 for this triple.
The same fixed polynomials were then checked once on the smaller target R=1001/1000, using 16384 s cells, d in [-1/1001000,0], and the actual algebraic cut c=2 cos(2 pi 7851/19683), enclosed at 256 bits and checked inside the inherited interval.
That check has first-success counts 15012, 799, 315 and 172, leaving 86 cells unresolved.
Consequently it does not prove M(P)>1001/1000 either.
An unresolved cell asserts neither a feasible density nor an actual integer polynomial.

<a id="proposal-scope"></a>
## Actual proposal scope and limits

There were five numerical LP calls in total, each with 1000 midpoint nodes and a 15-second solver limit.
The endpoint objective succeeded at s=-15/16, -239/250 and -19/20; their rounded equality multipliers supplied the three endpoint polynomials.
The endpoint LP at s=-489/500 returned numerical infeasibility without a polynomial or a continuous-domain proof.
A separate density-cap separation LP at that same location succeeded and supplied the remaining polynomial.
That separation bounds seven shifted-Chebyshev coefficients by one in absolute value; this is a proposal normalization, not a restriction on original integer inputs.
All proposal coefficients were rounded at denominator 10^6 before exact continuous verification.
No further LP, conductor, triple, polynomial degree or proposal position was tried.
Numerical objective values and infeasibility were not adopted as exact optimum values or mathematical exclusions.

Intermediate two- and three-polynomial covers were used to select the two interior endpoint proposal locations.
The final four-polynomial results above supersede those partial coverage counts without changing the target domain.
An early cover reached no finite comparison because the installed Arb generic power operation returned NaN on a ball crossing zero.
The recurrence now uses interval multiplication for z squared and explicitly rejects nonfinite results.
The reported coverage counts come from the corrected implementation.

<a id="reproduction"></a>
## Solver-free reproduction

From the repository root, with Python 3.14.7, SymPy and python-flint 0.9.0:

~~~text
python -B mathematics/computations/programs/Yin_J_G0151/endpoint_dual.py verify-fixed
python -B mathematics/computations/programs/Yin_J_G0151/endpoint_cover.py
python -B mathematics/computations/programs/Yin_J_G0151/endpoint_cover.py --small-shell
~~~

These commands use the retained four-polynomial input and run no optimizer.
The optional propose, secondary, middle, final and separate commands reproduce the five individually bounded proposals, requiring NumPy 2.5.4 and SciPy 1.18.1; the verification commands do not require those libraries.
Generated records are replaceable local JSON files in mathematics/computations/outputs/Yin_J_G0151, including endpoint_dual_fixed_verification.json, endpoint_cover.json and endpoint_cover_small.json.
Every certificate input needed for these checks is retained in the native program directory.
The [independent finding](../../../audits/reviews/Yin_R_G1107_v25.md#fixed-dual-cover-review) checks the continuous verification and reproduces all three solver-free commands.
It does not independently replay the historical numerical proposals or change the two incomplete-cover conclusions.
