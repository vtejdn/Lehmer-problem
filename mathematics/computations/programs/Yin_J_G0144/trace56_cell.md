# One fixed degree-56 all-real trace cell

This prepares the [selected S10 fixed-cell test](../../../strategies/Yin_S_G0010.md#primitive-fixed-cell-test) in the existing J144 group.
It adapts the interpolation argument and integer bounds of [C876v2](../../../claims/Yin_C_G0876_v2.md#argument) to an all-real trace polynomial of degree 28.
The old degree-64 exclusion concerns different nodes and a nonreal trace pair and supplies no exclusion here.
The mathematical input and exact preparation have passed the [independent preparation finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-preparation-review).
The numerical implementation, complete-measure interface and actual controls have passed the [independent implementation finding](../../../audits/reviews/Yin_R_G1111_v14.md#fixed-cell-implementation-review), within its stated library and journal boundaries.
The [single formal numerical test](#formal-result) has now completed without a candidate; its infeasibility status remains a numerical observation, with no exact exhaustive integer exclusion.

## Fixed parent, coordinates and source

The selected source is the parent of J156's committed DP seed-32 proposal 448, retained as observation 11542 with its exact parent and mutation in [primitive_root_diagnostics.json](../Yin_J_G0156/inputs/primitive_root_diagnostics.json).
Apply `z -> -z` to the entire parent and its actual child.
With ascending coefficients

\[
F=[1,-1,0,1,-1,1,-1,1,0,-1,1],
\]

the resulting parent is

\[
P_0(z)=F(-z)\Phi_6(z)\Phi_4(z)\Phi_{14}(z)
       \Phi_{12}(z)\Phi_{15}(z)\Phi_{30}(z)\Phi_{60}(z).
\]

Exact multiplication agrees with the sign-transformed source coefficients; the parent has degree 56 and height two.
The retained actual mutation adds one to coefficient 28.
Because 28 is even, its transformed child is still `P0 + z^28`.
It is a preparation control, not a new sampled candidate.

For `k>=1`, use `C_k(z+z^-1)=z^k+z^-k`, and use the constant basis element one.
The recurrence is `C_0=2`, `C_1=t`, `C_k=t C_(k-1)-C_(k-2)` when constructing the positive-index elements; replace the constant basis element by one afterwards.
This reuses J144's existing [Chebyshev-basis implementation](trace64_cell.py), not the U-type basis of the separate affine search.
Every `C_k` is monic integral of degree `k`, so this basis is unitriangular over the integers.
Consequently

\[
Q=C_{28}+a_1C_{27}+\cdots+a_{27}C_1+a_{28}
\]

is integral exactly when its 28 free coefficients are integral.
The associated polynomial is

\[
P=z^{28}Q(z+z^{-1})
 =z^{56}+a_1z^{55}+\cdots+a_{27}z^{29}+a_{28}z^{28}
  +a_{27}z^{27}+\cdots+a_1z+1.
\]

Thus `a_i in [-4,4]` is exactly the reciprocal coefficient-height-four box.
All native coordinate rows and vertices use descending free order `a1,...,a28`, corresponding to `C27,...,C1,1`.

## Deterministic separators and exact root shape

[trace56_cell.py](trace56_cell.py) and [trace56_cell.json](trace56_cell.json) own the prepared fixed input.
The trace of `P0` has 27 simple roots in `(-2,2)` and one root in `(2,61/30)`, verified by its exact rational Sturm chain and degree.
For each target count `i=1,...,26`, start a separate bisection at `[-2,2]`.
At each dyadic midpoint, compute the exact number of parent roots to its left using Sturm variations.
Choose the first midpoint that is not itself a parent root and has count `i`.
If the midpoint is a parent root, zero-skipping Sturm variations count it on the left; when that count is `i`, continue to its right.
All other steps retain the half containing the desired gap.
This fixed rule is independent of any solver outcome; the preparation cap is 256 steps per gap, and this input used at most eight.

The resulting ordered nodes `s0,...,s28` are

\[
\begin{split}
(&-2,-63/32,-31/16,-15/8,-7/4,-3/2,-95/64,-11/8,\\
 &-5/4,-1,-3/4,-1/2,-1/4,-1/8,1/8,1/4,7/16,1/2,\\
 &7/8,15/16,5/4,11/8,3/2,7/4,29/16,15/8,63/32,2,61/30).
\end{split}
\]

The native input stores the exact rational pairs, bisection counts and Sturm variations at every node.
The parent has exactly one root in each of the 28 open gaps and is nonzero at all nodes.
The fixed cell imposes all 29 strict conditions

\[
(-1)^i Q(s_i)>0,\qquad 0\le i\le28.
\]

Each native sign row is obtained by a positive rational scaling of this expression, followed by division by its positive integer coefficient gcd.
It has integer coefficients in `(a1,...,a28,1)`, so the exact strict condition is equivalent to its value being at least one.
The parent passes all rows.
The observed central-plus-one child fails rows 5, 7, 13, 15, 17, 19 and 23, using zero-based node indices.
This verifies that the selected cell distinguishes the actual successful root configuration of the parent from that observed mutation's exterior-root proliferation.

## Complete measure bound from the cell

The signs alternate at consecutive nodes, so the intermediate value theorem supplies a real root in each open gap.
The gaps are disjoint and there are 28 of them, which accounts for the entire degree.
Every root is therefore simple, and no additional real or nonreal root is available.
Twenty-seven trace roots lie strictly between `-2` and `2`; the last is a real number `tau` with `2<tau<61/30`.
For an interior trace root `t`, both roots of `z^2-tz+1` lie on the unit circle.
For `tau>2`, the two roots are positive reciprocals, with exactly one exterior root

\[
\rho=(\tau+\sqrt{\tau^2-4})/2>1.
\]

All leading coefficients are one, so the complete Mahler measure of `P` is exactly `rho`.
The map `rho -> rho+rho^-1` is strictly increasing for `rho>1`, and

\[
6/5+5/6=61/30.
\]

Hence every exact integer member of this cell has the complete bound

\[
1<M(P)=\rho<6/5.
\]

This argument concerns the original whole polynomial and includes every root and every multiplicity.
It does not replace the selected candidate's separate exact-input checks and complete factor/root certification.
The latter supplies an independently inspectable full-measure certificate and the actual irreducible-factor and primitive-degree classification.

## Exact open simplex and integer bounds

Let `S(t)=product_(i=0)^28(t-s_i)` and `V_i=S/(t-s_i)`.
The sign of `S'(s_i)` is `(-1)^(28-i)=(-1)^i`.
For a monic degree-28 polynomial in the strict cell, the Lagrange weights

\[
\lambda_i=Q(s_i)/S'(s_i)
\]

are all strictly positive.
Interpolation gives `Q=sum_i lambda_i V_i`, and comparison of leading coefficients gives `sum_i lambda_i=1`.
Conversely, positive weights summing to one give a monic polynomial with every required strict sign, since `V_j(s_i)=0` for `j!=i` and `V_i(s_i)=S'(s_i)`.
The interpolation map is an affine bijection between the monic degree-28 coefficient space and the hyperplane `sum lambda_i=1`.
Thus the cell is exactly the open 28-simplex with these 29 rational vertices.
There is no quadratic corner factor in this all-real adaptation.

Expand every vertex in the same descending free Chebyshev coordinates, writing it as `v_i`.
Every cell member belongs to their closed convex hull, so integrality and the coefficient box give the valid coordinate bounds

\[
L_j=\max(-4,\lceil\min_i v_{ij}\rceil),\qquad
U_j=\min(4,\lfloor\max_i v_{ij}\rfloor).
\]

Using the closed hull only enlarges the bounding set and does not discard a strict-cell input.
The first seven bounds are `[-2,1]`, `[0,4]`, `[-4,1]`, `[-1,4]`, `[-4,2]`, `[-3,4]`, `[-4,3]`; all remaining coordinates retain `[-4,4]`.
The input contains all 29 rational vertices and all bounds, so they can be recomputed exactly without a solver.
It also retains the parent's 29 positive Lagrange weights; their sum is exactly one and their weighted vertex vector is exactly the parent vector.
The general C876 prefix normal and coordinate-bound inequalities remain valid for these new vertices and bounds, but no exact prefix tree has been run or claimed here.

## Removing both complete known-value fibers

The positive-exterior Lehmer trace, reconstructed from `F(-z)`, is

\[
q_L=t^5+t^4-5t^3-5t^2+4t+3.
\]

The second known core `H` is read from the actual degree-18 core group in [degree_core_mass_states.json](../Yin_J_G0156/inputs/degree_core_mass_states.json).
Its exact ascending coefficients and its trace are retained in the fixed input.
The positive-exterior trace is

\[
q_H=t^9-t^8-8t^7+7t^6+20t^5-14t^4-17t^3+8t^2+4t-1.
\]

Exact factorization verifies that both trace cores are irreducible over the rationals.
Sturm counts give four inner roots and one positive outer root for `qL`, and eight inner roots and one positive outer root for `qH`.
For both, the positive outer root lies in `(2,61/30)` and there is no negative outer root in the reflected interval.
The monic trace of `H(-z)` instead has one negative outer root and none in `(2,61/30)`.
This determines the sign convention from the actual integer core rather than from a guessed sign pattern.

Within this cell there is exactly one exterior root of `P`, and it is positive.
If its value equals either known value, the corresponding trace `rho+rho^-1` is a root of `Q` and its irreducible minimal polynomial `qL` or `qH` divides `Q`.
Conversely, either divisibility supplies that core's positive outer trace root, which must be the cell's unique outer trace root, so the complete measure equals that known value.
Therefore `qL` not dividing `Q` and `qH` not dividing `Q` remove the complete two known-value fibers in this cell, including all their possible neutral completions.
This is stronger than excluding only the original parent vector and does not assert literature novelty beyond the two supplied references.

Division by either monic integral core yields an integral remainder vector

\[
r_j(a)=c_j+\sum_{k=1}^{28}A_{jk}a_k.
\]

The program computes the constant remainder of `C28` and each free basis remainder exactly.
It checks these affine maps by independent division for the zero vector and every basis vector; by linearity the maps then apply to every coefficient vector.
The condition that a remainder vector is nonzero is the finite disjunction of `r_j>=1` and `-r_j>=1` over its components.
This supplies ten branches for `qL` and eighteen for `qH`.
The two disjunctions are imposed separately, with at least one selected branch in each family.

On the valid coordinate box, exact affine bounds are

\[
\ell_j=c_j+\sum_k\min(A_{jk}L_k,A_{jk}U_k),\qquad
u_j=c_j+\sum_k\max(A_{jk}L_k,A_{jk}U_k).
\]

For a branch of sign `sigma`, put `m_j=ell_j` when `sigma=1` and `m_j=-u_j` otherwise, and `M_j=max(0,1-m_j)`.
With a binary selector `b`, the inequality

\[
\sigma r_j(a)-M_jb\ge1-M_j
\]

is automatic on the box when `b=0` and enforces the desired signed nonzero remainder when `b=1`.
Conversely, any nonzero integral remainder permits at least one such selector to be one.
The formulation is therefore exactly equivalent on the valid integer box.
All remainder coefficients, component bounds and branch constants are retained as integers; the actual big-M values range from 57 to 239 for `qL` and from 57 to 943 for `qH`.
The original parent has zero `qL` remainder and is excluded by this condition despite lying strictly inside the cell.

## Preparation controls and reproduction

The exact preparation used Python 3.14.7 and python-flint 0.9.0 and made no Mahler root call.
It reads only the two declared J156 native inputs, reconstructs the fixed parent and both trace cores, and writes the standalone J144 mathematical input.
The installed numerical dependencies for the later suggestion interface are HiGHS 1.15.1 through highspy and NumPy 2.5.4, confined to the ignored `mathematics/computations/outputs/Yin_J_G0144/trace56_packages` directory.
They are not required by the exact cell checker.

From the repository root, using the existing FLINT runtime, the commands are:

~~~text
python -B mathematics/computations/programs/Yin_J_G0144/trace56_cell.py prepare
python -B mathematics/computations/programs/Yin_J_G0144/trace56_cell.py check --output mathematics/computations/outputs/Yin_J_G0144/trace56_cell_controls_recheck.json
~~~

Preparation refuses to replace the existing fixed input, and check outputs require fresh destinations.
The actual check output is `mathematics/computations/outputs/Yin_J_G0144/trace56_cell_controls.json`.
It verifies the deterministic nodes, all exact integer rows and scalings, the rational vertices, natural bounds, affine remainders, parent signs and central-child rejection.
The native input additionally records the exact parent interpolation weights and core sign controls.
These checks establish the finite preparation described here; they do not establish that the filtered integer cell is nonempty or empty.

## Numerical suggestion and formal-run boundary

[trace56_milp.py](trace56_milp.py) supplies the numerical suggestion interface independently of the fixed mathematical input.
Its selected formal identity has seed 56003, one thread, node cap 100000 and one total 120-second wall budget from prelaunch.
The preparation controls preceded the single formal search reported below and receive no formal discovery credit.
Model initialization, input checks, numerical work, candidate retention, exact checks, complete factor/root certification and result writes must all be charged to that clock.
No later verification can acquire retrospective on-time yield.

For a noninteger reduced rational node `p/q`, a monic integral `Q` cannot vanish there by the rational-root theorem.
Thus the nonnegative sign condition is equivalent to the strict one for exact integer candidates at such nodes.
Only the integer nodes, indices 0, 9 and 27 with values `-2`, `-1` and `2`, require a positive integral threshold in the suggestion model.
Every final candidate is nevertheless checked with all 29 original cleared-denominator integer rows at threshold one.
This distinction avoids assigning numerical strictness to a rescaled rational threshold far below solver tolerance.
Floating feasibility remains a suggestion and floating infeasibility remains unresolved; neither numerical tolerance nor a timeout is an exact exclusion certificate.

The model has 28 integer free coefficients and 28 binary remainder selectors, with 59 inequalities: 29 signs, 28 signed-remainder branches and two selector-family constraints.
It minimizes the constant zero objective as a feasibility problem, without a warm start, objective sweep, candidate-rejection restart or separator change.
Each numerical row is divided by a positive integer scale to keep magnitudes bounded.
For an exact scaled row `u*x>=v`, let its stored double coefficients be `u_tilde` and let `b_j=max(|L_j|,|U_j|)` for every free or binary variable.
The exact rational conversion bound

\[
E=\sum_j |\widetilde u_j-u_j|b_j
\]

implies that every exact feasible vector satisfies `u_tilde*x>=v-E` on the bounded variable box.
The floating lower bound is rounded down from `v-E`.
Coefficients at or below the declared HiGHS small-matrix threshold are explicitly dropped before computing this bound, so their entire error is included.
This makes the stated row conversion an outer relaxation; the backend's own floating-point operations still supply no exact infeasibility proof.
Actual tolerances, scales, rational error bounds, floating rows and any dropped columns are retained with the run.

The formal `run` command starts the wall clock immediately before launching a fresh child, so its imports and exact input rechecks are charged.
The child constructs the model and makes exactly one `Highs.run()` call, with its time limit set to the remaining wall time and the fixed node cap.
The supervisor kills that child at the overall deadline even if model construction or root certification has not returned.
The worker first journals raw numerical columns, rounded integer coefficients and the complete proposed polynomial, then performs exact cell and remainder checks.
An observational HiGHS improving-incumbent callback also flushes any candidate it receives before `Highs.run()` returns, preserving that input if a hard interruption occurs inside the solver.
The callback changes no constraints, objective, random choices or solver decisions and performs no exact polynomial check or root computation.
If they pass with time remaining, it calls J156's unchanged complete evaluator and structural diagnostics.
A verified target additionally requires a lower measure bound strictly above one and the original evaluator's certified upper bound below 6/5.
The full certificate is flushed before the predeadline verified-commit marker is considered.
Post-run summary writing is only transcription of already observed events and supervisor facts; it performs no solver, polynomial or certificate work.
The formal output stem is `mathematics/computations/outputs/Yin_J_G0144/trace56_fixed_cell_s56003`, and existing JSON or JSONL output prevents repeating that identity.

Any interruption after candidate retention leaves the exact proposed coefficients available with its actual verification stage.
A certificate without an observed predeadline verified-commit marker receives no on-time target credit.
An invalid exact candidate stops this one suggestion attempt, rather than silently triggering a different numerical problem.
The supervisor and later summary distinguish worker failure, numerical failure or infeasibility, rejected suggestions, pending certification and an on-time verified target.

The actual model-building controls used HiGHS 1.15.1 and NumPy 2.5.4, built all 56 variables and 59 rows, and made zero solver-run calls, zero real child-control launches and zero new root certifications.
They checked the row error bounds over all declared variable boxes, exact big-M deactivation, integer-node handling, rounding of a parent suggestion, rejection of that parent by the full qL fiber condition, nonfinite suggestions and mechanical failure/deadline retention states.
Missing and after-deadline commit markers give no target credit in those controls.
The final model/control output is `mathematics/computations/outputs/Yin_J_G0144/trace56_milp_controls_v3.json`; the earlier outputs remain preserved.
The actual smallest nonzero floating matrix magnitude is approximately 0.001060445, and no coefficient was dropped.
Actual callback registration and a mechanical incumbent event check the pre-return retention interface.
Synthetic complete verification stages with a predeadline commit receive bookkeeping credit, while otherwise identical missing or late commit markers do not.
These mechanical statuses do not assert a mathematical certificate or discovery.

The hard supervisor is new code in this dedicated entry point, with a shared `supervise_child` function and `Journal` writer used by the formal path and a separate lifecycle control.
That actual control launched one nonmathematical child with a 0.75-second budget, flushed a synthetic pending candidate at approximately 0.200 seconds and was killed at approximately 0.755 seconds of supervisor time.
The intended postdeadline marker was absent, the exact pending coefficients survived parsing and no target credit was assigned.
A separate actual `Popen` call with a deliberately absent executable exercised startup failure without starting another process.
The retained lifecycle observations are `mathematics/computations/outputs/Yin_J_G0144/trace56_supervisor_control.json` and its JSONL journal.
The lifecycle control made no solver call and no root calculation and has an explicitly nonformal identity.
The full mathematical candidate-certification branch has not been invoked on a new trial during this preparation; it remains an inspected call to the existing complete evaluator.

With Python 3.14.7 selected as `python` and the stated local dependencies prepared, the environment invocation from the repository root is:

~~~powershell
$env:PYTHONPATH = (Join-Path (Get-Location) 'mathematics/computations/outputs/Yin_J_G0144/trace56_packages') + [IO.Path]::PathSeparator + (Join-Path (Get-Location) 'mathematics/computations/outputs/Yin_J_G0156/packages')
python -B mathematics/computations/programs/Yin_J_G0144/trace56_milp.py controls --output mathematics/computations/outputs/Yin_J_G0144/trace56_milp_controls_recheck.json
python -B mathematics/computations/programs/Yin_J_G0144/trace56_milp.py lifecycle-control --output mathematics/computations/outputs/Yin_J_G0144/trace56_supervisor_control_recheck.json
~~~

With an equivalently provisioned Python runtime, the prepared formal command is:

~~~text
python -B mathematics/computations/programs/Yin_J_G0144/trace56_milp.py run
~~~

This command was executed once for the fixed identity; the existing-output guard prevents an automatic repetition.
The exact preparation, model checks and formal search retain their separate scopes.

<a id="formal-result"></a>
## Actual single-run result

On 2026-11-10 the main agent executed the fixed `trace56_fixed_cell_s56003` identity once with the unchanged input, program and settings.
The original observations are `mathematics/computations/outputs/Yin_J_G0144/trace56_fixed_cell_s56003.json` and its JSONL journal.
The [native observation](trace56_observation.json) retains the complete original summary and all six journal events, including the full actual model, rational conversion bounds, floating rows and charged clocks.
Its 184712-byte JSON payload preserves the original integer and floating-point values without compressing mathematical fields.
No second solver run, replacement seed, separator change, larger box or additional candidate attempt was made.

| Observed quantity | Actual result |
| --- | --- |
| Solver status | `Infeasible` |
| Reported MIP nodes | 13013 |
| Reported solver time | 3.6667940999905113 seconds |
| Solver-start clock | 0.4871909999928903 seconds from prelaunch |
| Solver-return clock | 4.154277800000273 seconds from prelaunch |
| Total supervisor clock | 4.175340000016149 seconds |
| Deadline termination | No |
| Worker return code and stderr | Zero; empty stderr |
| Observed improving incumbents | Zero |
| Returned candidate, exact candidate check, complete certificate and verified commit | All absent |
| On-time verified target | False |

The complete event sequence is configuration, exact-input check, model, solver start, solver return and finish.
All six events are complete JSON records; no truncated final record or failed worker stage was observed.
The solver stopped before both the 120-second wall cap and the 100000-node cap.
Its node count is a reported numerical MIP count, not a count of integer polynomials exhaustively checked by an exact verifier.
No new polynomial factorization or root certification was reached in this run.

The reported outcome is `numerical_status_without_candidate_unresolved`.
The outer row conversion and checked implementation do not convert the backend's infeasibility status into a proof that the integer cell is empty after the two known-value exclusions.
There is no retained candidate requiring postdeadline certification and no target or novelty claim.
The main agent checked the actual original summary, all event kinds and clocks and the native preservation.
The [independent actual-result finding](../../../audits/reviews/Yin_R_G1111_v15.md#fixed-cell-result-review) verifies the entire original summary and six-event history, the complete native retention and this numerical-unresolved interpretation.
This completed the declared single numerical test without settling exact finite feasibility or G0001.
The separately generated and independently checked [exact tree](trace56_tree.md) subsequently proves that this fixed closed simplex in the height-four integer box contains only the original parent.
That later proof closes the finite filtered-cell question without altering the numerical observation or completing G0001.
