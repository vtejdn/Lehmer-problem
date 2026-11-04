---
author: Yin
---

# Exact finite-box quartic returns with complete truncation cost

Exact actual-quartic rational-theta computation supporting [C559](../../../claims/Yin_C_G0559_v1.md#complete-finite-quartic-argument).
The complete omitted-tail and original-law costs belong to that proof; these finite calculations establish no general finite-core claim or unrestricted gap.

<a id="shortest-first-hit-discriminator"></a>
## Complete shortest-first-hit levels and an arithmetic row discriminator

The continuing author question is [D9's shortest-hit test](../../../drafts/Yin_D_G0009.md#shortest-first-hit-preparation): can W_lambda(x)=lambda^(-d(x)), for the actual shortest first-hit length d, satisfy a strict original killed-row certificate?
[shortest_first_hit.py](shortest_first_hit.py) is a new scope in this existing quartic original-law group; it does not modify the earlier graph, return or midpoint programs.
It is prepared for exact reverse breadth-first search from zero through depth24, with at most100000 retained states and a120-second mathematical computation limit, and no independent neutral-radius cutoff.
Its state coordinates are ascending powers(1,beta,beta^2,beta^3), with the forward and inverse maps given explicitly in the program.
The inspected [J33 core.py](../Yin_J_G0033/core.py) supplies the reusable root-isolation and strict-strip method; the new implementation uses150 rational bisections and integer common-denominator interval numerators and imports no earlier mathematical helper.
It certifies membership in C400's actual strict core using B=beta^3-beta-2, S=beta^3-beta-1 and reciprocal conjugation, including rejection of exact boundary equality.
An unresolved sign stops the calculation instead of making a floating-point decision.

Every completed level retains every state, its shortest distance, the total shortest-word mass as an integer numerator over4^d, and a chosen shortest successor.
Only rows with ALL legal successor distances known enter the reported Laurent-polynomial patterns; other rows remain explicitly unknown.
The row polynomial uses all unchanged original digit weights and excludes the zero successor exactly as B_0 requires.
Complete output is published only after the declared search and row analysis finish; a stopped calculation writes a separately labelled incomplete output containing only completed levels and its actual analysis scope.
The declared depth24 search and row analysis completed with417 states,354 fully known rows and62 explicitly unknown rows, producing26 exact Laurent-polynomial patterns.
All completed levels, distances, shortest-mass numerators, chosen shortest successors and row coverage are retained in shortest_first_hit_24.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_24.json`).

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/shortest_first_hit.py
```

A certified finite violating row can reject an unmodified parameter candidate, or an exact pattern inequality can reject all lambda in its proved range.
It does not reject finite-exception repairs, supply an all-state successor-pattern bound, decide R_f>R or classify the critical mean.
The decisive witness is x=beta^2-beta-1, whose two legal successors have distances1 and4 while d(x)=2.
Its raw row is(lambda+2lambda^(-2))/4, with exact minimum3/(4*cuberoot(2))>10/17, so it rejects the unmodified family for every lambda>0 and every t>=17/10, in particular every t>R.
The complete symbolic reasoning and finite-repair limitation are retained in [D9](../../../drafts/Yin_D_G0009.md#shortest-distance-row-counterexample).

[verify_shortest_witness.py](verify_shortest_witness.py) imports no BFS helper and checks this instance by direct unrestricted word enumeration through length4, generic polynomial reduction, and coarse exact rational strict-core enclosures.
It certifies the unique shortest words and masses at all three required states and the rejected third successor, then checks the polynomial factorization and rational comparison in the all-lambda minimum proof.
shortest_first_hit_witness_check.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_witness_check.json`) records its passed result.
This is a distinct exact author check of the tiny witness, not independent-agent review or a whole depth24 reproduction.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_shortest_witness.py
```

The verifier requires the declared author JSON above only for its final witness-data comparison; its polynomial, word and interval calculations are separate.
No larger search or tail classification is justified by these finite patterns.

### Multiplicity-aware two-row test

The proposed refinement is W_(lambda,theta)(x)=lambda^(-d(x))M(x)^theta, with lambda>0 and real theta.
Inspection of the existing certified rows found an exact two-row obstruction, so no numerical optimization or new graph was needed.
[verify_multiplicity_pair.py](verify_multiplicity_pair.py) uses the retained generic polynomial/direct-word routines, independently of the BFS implementation, to enumerate all words through length7 at u=beta-2 and its two legal successors.
It certifies distances7,6,7 and shortest masses1/2048,1/1024,1/8192, together with all legality tests, and compares these facts to the existing data.
The passed shortest_multiplicity_pair_check.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_multiplicity_pair_check.json`) and [D9 proof](../../../drafts/Yin_D_G0009.md#shortest-multiplicity-two-row-obstruction) retain the exact all-real-parameter conclusion.
Together with the earlier distance2 row, these facts reject the unmodified two-parameter family for every lambda>0, every real theta and every t>=17/10; they do not exclude finite-exception repairs.
This is an author symbolic proof with a distinct direct-word check, not an independent-agent review or a new all-time tail result.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_multiplicity_pair.py
```

The command requires the two declared earlier author/check JSON files for its comparison and input-scope checks; its new distance and mass enumeration is separate.

<a id="geodesic-first-deviation-cost"></a>
### First-deviation accumulation and a complete-level certificate

[geodesic_detour_cost.py](geodesic_detour_cost.py) folds only the existing417-state distance DAG, without constructing another graph.
With g_t=t^d M, it normalizes geodesic transitions by G(x,y)=pi_e M(y)/M(x) and charges each nongeodesic edge by pi_e M(y)t^(1+d(y)-d(x))/M(x).
It accumulates these costs over the entire geodesic continuation, rather than checking only the current row.
The exact rational points are t0=68883/40000 and t=173/100.
Known nongeodesic terms produce a lower polynomial when other targets are unknown; an exact flag requires all local terms and all geodesic descendant costs to be known.
The complete geodesic_detour_cost_24.json (`mathematics/computations/outputs/Yin_J_G0052/geodesic_detour_cost_24.json`) contains265 exact cost states including zero, with separately marked lower bounds elsewhere.

[verify_geodesic_level9.py](verify_geodesic_level9.py) checks the decisive complete level by a distinct exact author method, importing no BFS or DAG-fold function.
Direct enumeration through length9 certifies all57 states of distance at most9 and their shortest masses.
Unrestricted split-word endpoint sums with halves of length at most8 then verify the73 required states, including nongeodesic successors of distance at most15; the largest half-word endpoint set has2901 elements.
Explicit averaging over every shortest word at each of the ten level9 states independently reproduces its full accumulated-cost polynomial.
The verifier retains the100000-item/120-second bound, and its passed geodesic_level9_check.json (`mathematics/computations/outputs/Yin_J_G0052/geodesic_level9_check.json`) records all target distances/masses, shortest words, polynomials and exact scope.
This is a distinct author verification of the finite certificate, not independent-agent review or a new actual-core graph.

The exact level9 minimum at t0 is36193899689180879400344643/26214400000000000000000000>69/50.
The complete operator, word-decomposition and all-distance proof are fixed in [adopted C833](../../../claims/Yin_C_G0833_v1.md#decision-whole-reviewed-2026-10-28), through [whole independent mathematical/native R1053](../../../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding).
That review inspected the full native methods and reran the decisive distinct verifier, covering all57 states through9, all73 required d/M values through15 and the five exact cost polynomials; it did not rerun the depth24 graph.
The nonnegative geodesic recursion propagates that lower bound to every actual state with d>=9 and every t>=t0.
It obstructs a subunit row budget for the unchanged full first-deviation operator outside any finite set of starting states.
Killing intermediate or terminal contributions at a finite core, or resumming them, changes the operator and is not excluded.
No unboundedness of the row costs, critical-mean classification or first-return-radius equality/separation follows.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/geodesic_detour_cost.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_geodesic_level9.py
```

The fold requires shortest_first_hit_24.json; the verifier additionally requires geodesic_detour_cost_24.json for final comparison after its own word calculation.
The helper verify_shortest_witness.py supplies only its separate generic polynomial and rational-interval routines to the two later author verifiers.

<a id="finite-core-resummation"></a>
## Complete distance-eight core resummation at one supercritical point

[finite_core_resummation.py](finite_core_resummation.py) evaluates the [D9 finite-core question](../../../drafts/Yin_D_G0009.md#finite-core-resummed-geodesic-test).
It uses only shortest_first_hit_24.json and geodesic_level9_check.json, all417 existing states, the complete46-state nonzero core d<=8 and t=173/100.
The program checks a positive rational core solution, the exact nonnegative inverse and an eight-step strict substochastic contraction before treating the inverse as a convergent original chronological series.
It then extends that core baseline along original weighted geodesic paths and pays both outside first deviations and all within-core paths followed by exit.
Unknown successor terms supply labelled lower bounds only; a finite fit supplies no all-state upper estimate or critical-mean conclusion.
The resource limit is120 seconds with no new graph or parameter scan.
The declared calculation completed:46 core states,10 exit targets and strict eight-step normalized core survival below893/1000.
It retained218 exact outside cost rows; rows with missing terms remain lower bounds.
At t=173/100 every one of the20 complete distance14 costs is exact and their exact minimum exceeds11/10.
The separate [D9 argument](../../../drafts/Yin_D_G0009.md#finite-core-resummed-geodesic-test) proves propagation for the NEW normalized operator to every d>=14 at this single parameter, without a mean or R_f classification.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/finite_core_resummation.py
```

The existing two JSON inputs are required; default paths resolve from this actual J group.
Complete output was published only after all declared exact checks passed, at finite_core_resummation_8.json (`mathematics/computations/outputs/Yin_J_G0052/finite_core_resummation_8.json`).
The full core matrix, inverse, positive baseline, exit feedback, strict survival certificate and finite costs are retained there.

[verify_core_resummation.py](verify_core_resummation.py) imports no BFS or resummation routine.
Using the retained generic quotient and interval helper, it checks all417 supplied states through24 by1143 complete predecessor-closure probes, actual decreasing continuations and the full shortest-mass recursion; it builds no larger graph.
Exact matrix residuals and full geodesic-prefix averages at all20 distance14 states give a distinct author check of the result, with at most2 six-step prefixes per state.
Its passed core_resummation_check.json (`mathematics/computations/outputs/Yin_J_G0052/core_resummation_check.json`) records the exact minimum, all20 tuples/costs and finite scope.
This is author verification, not independent-agent review.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_core_resummation.py
```

The verifier requires the existing shortest data and the new core result; it has the same120-second bound and checks the fixed parameter only.

## Completed author scope and reproduction

[C559](../../../claims/Yin_C_G0559_v1.md#executed-quartic-finite-box-results) owns the complete current mathematical proof and limitations.
The original frozen [L243](../../../ledger/Yin_L_G0243_v1.md#complete-retained-proof-and-review) remains the actual input of R142.
[experiment.py](experiment.py) uses P=t^4-t^3-t^2-t+1, theta=0 and1/2, times4,5,16,32,64 and boxes2,4,7,12,19.
The n=4,5 cases are inherited exact controls.
Every traversal completed below the100000-state per-graph cap.
No larger scan, infinite spectral estimate or general-input theorem was computed.

The predeclared original-p_64 omitted-error target is1/16 at theta=1/2.
Rational beta and derivative bounds prove C_0<6/5,C_1<11/30.
The returned-prefix equals negative suffix identity gives the complete finite-time heights4,7,12 for n=16,32,64; no global finite core follows.
Every boxed return also meets two proved real-embedding strip inequalities.
Sign-aware outward rational coefficient enclosures only discard impossible states.
Forward graph reachability and then backward reachability of zero preserve exactly all boxed returned paths.
Integer dynamic programming uses denominator4 or8 and the complete original/normalized weights, without renormalizing killed mass.
All assertions and output fractions are exact; labeled decimal stdout fields are non-evidential displays.

A rational Taylor-series remainder certificate encloses each exponential in the COMPLETE error term.
Its lower endpoint proves conservative Gaussian height18 cannot meet the chosen tolerance, and its upper endpoint proves height19 does.
This claim concerns the sufficiency of the chosen bound: actual omitted mass is already zero at the certified length-specific height12.
The output records both sides of every such comparison.

initial_result.json (`mathematics/computations/outputs/Yin_J_G0052/initial_result.json`) retains the first mathematical payload.
result.json (`mathematics/computations/outputs/Yin_J_G0052/result.json`) adds direct original binary endpoint enumeration at n=16 and exact rational display intervals.
Every first-run mathematical field agreed with the final result; no failed computation or mathematical correction occurred.
The current program reproduces the final mathematical output.

Run the author program, supplying a separate destination to preserve both retained author outputs:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/experiment.py --output mathematics/computations/outputs/Yin_J_G0052/reproduction.json
```

The program uses only Python's standard library.
An author replay is reproduction; independent verification uses the distinct implementation below.

## Exact outcome and limits

| H | Full box | Forward reached | Can return inside graph | Edges |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 625 | 155 | 151 | 255 |
| 4 | 6561 | 549 | 533 | 911 |
| 7 | 50625 | 1585 | 1557 | 2669 |
| 12 | 390625 | 4485 | 4379 | 7549 |
| 19 | 2313441 | 10927 | 10675 | 18473 |

The exact full original p_64 is121338835637214357477/2658455991569831745807614120560689152, between4.5642e-17 and4.5643e-17.
The normalized theta=1/2 b_64 lies between1.0611e-8 and1.0612e-8.
The complete original-p_64 upper bound from Gaussian height19 lies between0.05104 and0.05105; replacing its omitted term by the proved zero value still gives a converted positive-theta bound between2.8977e-5 and2.8978e-5.
The latter is between10^11 and10^12 times the actual original probability.
All stated intervals have rational assertions in the program/output; these are comparisons for the fixed selected law and time, not an optimization or a universal inferiority claim.

Both laws' height7 and complete-height12 entries coincide at length64.
Height4 has strictly positive exact omission, with relative fractions below2.079e-9 and2.702e-19 for theta0 and1/2 respectively.
These finite relative statements come from exact complete sums, not from treating the absolute Gaussian tail as relative.
The n=16 original binary control groups65536 words into35662 endpoints, has170848 colliding ordered pairs, and agrees with the quotient result5339/134217728.
This is a distinct author cross-control only; no independent reviewer or n=32/64 direct binary enumeration is claimed.

The current outcome supports a changed question about bridge-conditioned omitted mass and full original-law block costs.
Neither the finite matrices nor these values prove an infinite-time relative tail, a global finite cutoff, a uniform pressure separation, or a Lehmer gap.
The complete current author proof is C559; the actual original authoring/review/provenance records remain this J and the original L243/R142 inputs.

## Complete independent inspection

The separately assigned orbit_research reviewer inspected the entire [original frozen D110 proof](../../../audits/reviews/Yin_R_G0780_v1.md#finite-box-complete-independent-review), all author program logic and both outputs.
No mathematical defect or author correction was found.
The reviewer contributed neither this proof nor this program; its earlier quartic contributions and L235/L239 review roles are disclosed in the complete nonblind finding.

The new [reviewer_orbit_verify.py](reviewer_orbit_verify.py) uses no author mathematical function for its independent calculation: it enumerates all allowed lattice points by exact three-coordinate slicing, uses forward/inverse-map depth-first reachability, evaluates backward terminal dynamic programming for both laws, and derives Taylor intervals with direct factorial/power expressions.
A direct Gray-code traversal of all65536 binary words independently supplies the original n=16 endpoint control.
reviewer_orbit_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_orbit_result.json`) retains its actual result, expanded graph counts, exact entries and mathematical comparison scope.

Run the independent checker from the repository root:

~~~powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/reviewer_orbit_verify.py
~~~

The independent checker passed after making draft presence an optional observation.
The retired draft supplies no mathematical input.

All975 final scalar mathematical fields and exact types, all930 initial fields, all50 entries and all30 comparisons agree.
A separate actual author replay intercepted its output in memory and also reproduced975 fields; this is reproduction, distinct from independent implementation.
The independent graph intersections have151,533,1557,4379,10675 states and255,911,2669,7549,18473 edges.
The direct binary control gives35662 endpoints and170848 colliding ordered pairs.
The complete proof checks establish why these finite calculations cover exactly the stated boxed returns and why heights4,7,12 give full returns at the three selected times.

The complete finding records the actual review and mathematical comparison scope.
All finite-time and input-specific limits remain in force.

## Fixed retention and current proof home

[C559](../../../claims/Yin_C_G0559_v1.md#finite-box-salem-experiment-fixed-scope) retains the complete current author proof; its responsible assessment selects the actual adopted review.
[L243](../../../ledger/Yin_L_G0243_v1.md#complete-retained-proof-and-review) remains the original dated review input of R142.
D110 denotes the original authoring phase.
Fixed adoption does not broaden this finite scope or complete G0001.

The earlier complete internal mathematical inspection, completed at 2026-10-22T19:13 UTC, is [R744 SELF](../../../audits/reviews/Yin_R_G0744_v1.md#current-complete-whole-self-finding).
It reuses the old different implementation and author replay at their actual distinct scopes, without rerunning either or supplying a missing original whole-review relationship declaration.

<a id="complete-original-midpoint-continuation"></a>
## Complete original midpoint continuation through length 256

The selected complete return and first-return arrays through512 are retained once at [inputs/return_weights_512.json](inputs/return_weights_512.json), with513 integers in each array and their exact original polynomial and digit-law scope.
They were recovered by the unchanged H95 construction and matched by the distinct reviewer implementation, including every aligned254775-state forward/backward pair and all513 return/first-return coefficients.
This is current exact reproduction of the adopted finite object, not recovery of an original execution file or a new formal review.
The two512 continuation programs use the exact first257 entries of this same input for their earlier-prefix comparison, while critical_mean_bounds.py and reviewer_critical_mean_verify.py read its complete513 entries.
The scalar arrays do not contain or replace the four midpoint sums, intervals and counts below.
Those are completely reproduced by `python -B mathematics/computations/programs/Yin_J_G0052/midpoint_continuation.py`, whose fixed H48 graph and integer dynamic program require no older generated input.
For a complete current512 reproduction and the subsequent critical-time checks, run:

```powershell
python -B mathematics/computations/programs/Yin_J_G0052/return_midpoint_512.py
python -B mathematics/computations/programs/Yin_J_G0052/reviewer_return512_verify.py
python -B mathematics/computations/programs/Yin_J_G0052/critical_mean_bounds.py
python -B mathematics/computations/programs/Yin_J_G0052/reviewer_critical_mean_verify.py
```

The graph/vector outputs remain reproducible ignored results; only the indispensable scalar arrays are fixed as tracked input.

The separately retained [midpoint_continuation.py](midpoint_continuation.py) is new author work by original_law_continuation for Yin.
It reuses the original program's exact graph, rational strips and constants without editing that program or replacing its earlier outputs.
The earlier reviews above do not cover this new calculation.
The complete reduction, exact true midpoint mark, quantitative radius consequence and limits are [adopted C776 MC1--MC7](../../../claims/Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26), through [independent whole R996](../../../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius).

The declared question is the full original return probability at every time1--256 and the full true midpoint second moment at midpoint times16,32,64,128, together with D_n=p_(2n)/p_n^2.
The original digit weights are1,2,1 with denominator4, including all earlier zero visits and all complete word multiplicities.
The C559 deterministic bound C_0+(floor(t/2))C_1<6/5+(11/30)128<49 puts every returned path with t<=256 inside integral height48.
There is zero omitted original return mass in this finite range.
The graph has68211 forward-reached states and65893 returning states, below the unchanged100000-state cap.
Its114445 directed digit edges are not part of that state count.
The original graph's rational strip and reachability pruning retains every such returned path.

Forward and backward integer dynamic programs agree at zero through128; their full midpoint products sum exactly to the time2n return weight at all four declared n.
The original p16,p32,p64 controls agree exactly.
The complete quotient-to-original reverse edge map is checked on zero and all basis vectors, and the actual squared neutral mark is retained exactly in Q(sqrt13).
The final rational enclosures use a bracket for sqrt13 checked by squaring, with its coefficient sign retained.
Every weighted quotient-coordinate mean is exactly zero; this is global centering only and does not assume centering on an update component.
The complete first-return integer weights are obtained by exact renewal inversion and are nonnegative at every computed time.

| Midpoint time n | Complete D_n interval | Complete M_n/n interval |
| ---: | --- | --- |
|16|(2.211245,2.211246)|(0.144025,0.144026)|
|32|(3.728176,3.728177)|(0.176933,0.176934)|
|64|(8.004156,8.004157)|(0.212920,0.212921)|
|128|(18.166305,18.166306)|(0.227137,0.227138)|

Here M_n is the actual E[|X_n(zeta)|^2 given X_(2n)=0], with both real neutral coordinates.
In particular M64>64/5 and M128>128/5 are exact finite inequalities.
The complete return and first-return lists, exact Q(sqrt13) moments, rational interval endpoints, old control checks and decisive radius certificate are in midpoint_continuation.json (`mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`).
Its output is reproducible and may be replaced by this same command; the original J52 outputs remain separate.

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/midpoint_continuation.py
```

Only Python's standard library is required, together with the declared same-group experiment.py import.
The default destination is resolved from the containing J group independently of the working directory; --output selects an explicit replacement destination.
The script publishes its JSON only after every asserted finite check succeeds and retains the same state cap; this completed run required no cap increase.
The JSON contains exact data, while labeled terminal decimal values are display only.

For every t=1,...,256, the exact test p_t(1723/1000)^t<1 proves that the individual-return sufficient crossing p_t>beta^(-t) fails throughout the computed range.
The distinct complete first-return sufficient test also fails: the monotone exact beta bracket gives0.948616<sum_(j<=256)f_j beta^j<0.950835<1.
These finite failures supply no converse and do not establish R=beta or a critical-mean branch.

The exact p256 and the existing C673 dyadic overlap argument give the adopted C776 theorem R>1687/1000, with h_2(beta)>log(1687/1000).
C776 supplies the full analytic tail payment G_m<(55/2)m for every m>=256 and R^256 p256>=1/(55*256); the output records the exact product(55*256)p256(1687/1000)^256<1.
Thus this lower-radius assertion uses the full original infinite-time theorem with an exact finite input, not a finite extrapolation.
The independent native and mathematical inspection is retained in R996 and the verification section below, at its exact declared scope.
The increasing finite midpoint ratios do not establish positive limsup, diffusion, finite or infinite critical mean, near-one uniformity or the unrestricted G0001 objective.

<a id="independent-complete-midpoint-verification"></a>
## Independent verification of the complete midpoint continuation

The fixed whole mathematical/native finding is [R996](../../../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius), bound to [C776 Statement](../../../claims/Yin_C_G0776_v1.md#statement) and [Complete argument](../../../claims/Yin_C_G0776_v1.md#complete-argument).
The separately assigned reviewer developed [reviewer_midpoint_verify.py](reviewer_midpoint_verify.py) without importing author mathematical functions or reading D37 development, proof-generation dialogue, persistent memory or an earlier review of this new calculation before its initial findings.
The checker uses the same fixed mathematical cutoff and rational strip enclosures, with a distinct native implementation.
It enumerates allowed lattice points by exact three-coordinate slicing, changes to original chronological coordinates, uses forward and inverse depth-first reachability, evolves predecessor-gather integer weights, counts first returns by killing paths at their first positive zero visit, and derives the neutral norm from the symmetric-power recurrence in Q(sqrt13).
The author JSON is read only after independent calculation, for exact comparison.
This is independent implementation of the stated finite model and reproduction of its values, not an author replay or formal verification of Python.

The completed graph calculation found71135 strip-allowed lattice points,66777 original-forward and68211 original-backward reached points,65893 states in their intersection and114445 retained digit edges.
Original-backward reachability corresponds to the author's quotient-forward count under the exact integral reverse map.
Both searches respect the unchanged100000 reached-state cap.
All257 return weights including time0, all256 first-positive-return weights, the five selected probabilities, all four midpoint integer sums and intervals, positive midpoint counts, both finite pressure tests and the exact radius certificate agree.
The direct killed first-return calculation checks the author's different renewal-inversion route.
The explicit p128/p256 fractions and the strict open interval endpoints in C776 were also checked.

reviewer_midpoint_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_midpoint_result.json`) retains the independent exact values and comparison scope.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/reviewer_midpoint_verify.py
```

The program uses only Python's standard library.
It computes without author native code, then requires the retained same-group midpoint_continuation.json for comparison; --author-input and --output provide explicit paths when needed.
Default paths resolve from the containing J group independently of the working directory.
The complete result is published atomically only after successful checks.
No range beyond256 or larger cap was run, and the old programs and outputs remain separate.
R996 records the full analytic tail review; C776's adopted decision explicitly selects the narrow existing C534 upper-radius input.
Neither native agreement nor the increasing finite moments establishes the positive-limsup premise, an actual critical-mean branch, R=beta, R<beta or the unrestricted G0001 objective.

<a id="complete-original-midpoint-profile"></a>
## Complete original midpoint radial profiles

[Adopted C779](../../../claims/Yin_C_G0779_v1.md#decision-whole-reviewed-2026-10-26) retains the complete same-scope MP1--MP4 statement, proof and finite tables, supported by whole independent R999 below.
The author [midpoint_profile.py](midpoint_profile.py) reconstructs the unchanged original graph and bridge weights, then calculates fourth moments, six non-strict radial events at each midpoint, grouped weighted median/90-percent quantiles and the true C301 signed coefficient/real-place companion.
All field comparisons and weights are exact; labeled decimals serve only as displays.
Its separate midpoint_profile.json (`mathematics/computations/outputs/Yin_J_G0052/midpoint_profile.json`) preserves every exact field sum, weight, probability, quantile bracket and certificate.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/midpoint_profile.py
```

The program uses Python's standard library and declared same-group experiment.py and midpoint_continuation.py helpers; it does not invoke their old mains or consume old generated results.
The unchanged height48, total time<=256, four midpoint times and100000 reached-state cap apply.
Finite radial mass and negative signed ratios do not establish the unbounded sequence required for a critical-mean conclusion.

<a id="independent-complete-profile-verification"></a>
## Independent verification of the complete radial-profile supplement

[R999](../../../audits/reviews/Yin_R_G0999_v1.md#complete-profile-and-signed-diagnostic) records the new whole review of [C779](../../../claims/Yin_C_G0779_v1.md#statement), its complete MP1--MP4 argument and finite tables, and [midpoint_profile.py](midpoint_profile.py) with its separate author output (`mathematics/computations/outputs/Yin_J_G0052/midpoint_profile.json`).
The reviewer reuses its earlier C776/R996 graph and exact-mark evidence only at the unchanged scope, and inspected the new proof and native program separately without D37 development, author profile-generation dialogue or a prior new profile finding.
The new [reviewer_profile_verify.py](reviewer_profile_verify.py) imports the unchanged same-group independent reviewer_midpoint_verify.py helpers and no author mathematical module.
It rebuilds the graph and original-coordinate forward/terminal weights through128, obtaining the complete returns through256 needed by the four midpoint products.
It reconstructs every field of the four profile rows before reading the author output and separately checks every literal strict interval in the three C779 tables.

The new comparisons use integer square roots for exact Q(sqrt13) signs, retain >= threshold semantics, group equal radial marks before weighted quantiles, and verify strict-below/at-or-below quantile masses.
All24 declared threshold equality masses are zero; that finite observation does not replace the non-strict event definition.
The n16 median is exactly1/16, and all other displayed quantile intervals are strict.
Fourth moments, all tail probabilities and tail first-moment contributions, both contribution inequalities at every declared time, and the complete signed C301 coefficients agree exactly.
The checker forms the signed coefficient directly from original-coordinate cross-correlations and the real-place product from its conjugate-field recurrence.
It also verifies J(Jx)=x and B_n(x)=F_n(Jx) at each positive bridge midpoint, confirming the actual reciprocal-fiber interpretation rather than only renaming an output scalar.
Negative real-place products remain signed.

The completed exact result is reviewer_profile_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_profile_result.json`), including the independent threshold-boundary counts.
Run from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/reviewer_profile_verify.py
```

Only Python's standard library and the explicitly named independent helper are required.
No old generated midpoint result is needed; midpoint_profile.json is required for the final comparison, with --author-input available for an explicit path.
The default --output destination resolves from the containing J group, and the complete JSON is published atomically after successful checks.
The original graph height48, four midpoint times, total time<=256 and100000 reached-state cap remain unchanged.
Old programs and results remain intact.
This distinct implementation and whole supplement review do not establish an unbounded sequence, a critical-mean branch, R=beta, R<beta or the unrestricted Task objective.

<a id="complete-original-return-midpoint-512"></a>
## Complete original returns through 512 and midpoint 256

The finite statement and full FC1--FC6 reduction are [adopted C793](../../../claims/Yin_C_G0793_v1.md#decision-whole-reviewed-2026-10-26), through [independent whole mathematical/native R1012](../../../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding).
The new author [return_midpoint_512.py](return_midpoint_512.py) declares the actual quartic P=t^4-t^3-t^2-t+1, unchanged independent digit weights1,2,1 divided by4, all complete return and first-return times0--512, and only the true midpoint second moment at n256.
The full C559/C776 height argument gives6/5+(11/30)256=1426/15<96, hence integral height95 with zero omitted return mass through512.
The new program copies the original bounded graph logic with an explicit local500000 reached-state cap; experiment.py and its old100000 cap remain unchanged.
It imports only the original author successor, allowed-state, rational-constant, coordinate and neutral-mark helpers, not reviewer mathematics.
The original real-strip screens retain the outward10^6 coefficient rounding and beta bracket861/500<beta<1723/1000.
Finite pressure and first-return tests use40 exact rational bisections within that same certified bracket.
No larger graph, later time, radial profile, radius theorem or critical-mean conclusion is selected.

Before running, the declared live memory stops are a process working set at least4GiB or available physical memory below1GiB, checked every4096 graph states and16 dynamic-program steps, including graph pruning and final checks.
Unavailable memory monitoring or a reached-state cap stops incomplete rather than changing the limit.
The checks use standard-library Windows APIs; they are periodic safeguards rather than a hard allocator limit.
There is no artificial elapsed-time limit.
Progress is printed during graph construction and every16 forward/backward steps.
Any failed native check publishes only the separate return_midpoint_512.incomplete.json with its actual failure and useful completed return prefix; it does not publish or replace a complete result.

The required earlier-prefix input is now the accepted [tracked513-entry scalar input](inputs/return_weights_512.json), compared by its exact prefix at every return and first-return weight from0 through256.
The new complete output is separately and atomically published as return_midpoint_512.json (`mathematics/computations/outputs/Yin_J_G0052/return_midpoint_512.json`) only after all checks succeed.
It preserves every return and first-return integer weight, exact p512, the quotient-state ordering and aligned boxed forward256/backward256 vectors, true Q(sqrt13) midpoint integer sums and rational coefficients, both neutral coordinates through their squared norm, positive midpoint count, D256, and finite crossing tests.
The product of the two boxed vectors gives the complete original bridge law; unconditional endpoint weights at states unable to participate in that bridge are not claimed complete.
All author calculations use integers and rational arithmetic; the certified sqrt13 enclosure has its coefficient sign retained.
Old programs and results remain unchanged.

Run from the repository root on Windows with Python's standard library:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/return_midpoint_512.py
```

The optional --prefix-input and --output arguments choose explicit input/output paths; defaults resolve from the actual containing J group.
The declared native calculation completed without changing any bound, with269715 reached states,254775 returning states and443125 directed digit edges.
All257 old return weights and all257 old first-return entries including their time0 conventions agree exactly with the accepted prefix.
The true midpoint has58669 positive-weight states,36.968603<D256<36.968604 and0.228798<M256/256<0.228799, with rational strict endpoints.
Every individual-return crossing fails for1<=t<=512, and the refined exact beta bracket gives0.954048<sum_(j=1)^512 f_j beta^j<0.954049<1.
These finite failures imply no converse about later times, the true radius or critical mean.
Its results require a fresh whole independent mathematical/native review before adoption; previous J52 reviews cover only their actual earlier scopes.

## Independent verification of complete returns through 512

The fresh whole mathematical and native finding is [R1012](../../../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding).
The new [reviewer_return512_verify.py](reviewer_return512_verify.py) imports no author mathematical module and runs exactly height95, all return and first-return times0--512, midpoint256 and reached-state cap500000.
It reuses only the earlier independent reviewer's unchanged integral coordinate/transition maps, rational utilities and Chebyshev norm helper; the old height48 calculation and result are not transferred to this scope.
Its new integer strip slicing and original-coordinate depth-first searches enumerate the graph, and predecessor gathering with zero killing computes first returns directly instead of the author's renewal inversion.
The full254775-state comparison explicitly swaps forward and backward roles under the original/quotient reversal and checks every saved vector entry, including zeros.

Run from the repository root with the author output and accepted old prefix already present:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/reviewer_return512_verify.py
```

The explicit --old-prefix-input option defaults to inputs/return_weights_512.json, using its exact first257 entries; --author-input and --output default to this same J group's output home.
The independent native run completed and atomically wrote reviewer_return512_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_return512_result.json`).
It independently reproduced all513 return and first-return weights, all257 entries of both accepted old prefixes, every aligned midpoint vector pair, all exact midpoint fields, the exact p512 and both refined-root finite-pressure fractions.
The graph enumeration found285171 allowed lattice points,258715 original-forward states,269715 quotient-forward states,254775 returning states and443125 edges.
The completed positive midpoint count is58669, with the exact strict D256 and M256/256 intervals in C793.
Periodic live memory monitoring uses the same4GiB working-set stop and1GiB available-memory floor, with separate incomplete output on failure; no cap, height or time was increased.
The complete independent result and R finding certify only the declared finite mathematics subject to the recorded native verification boundary, without an asymptotic conclusion.

## Exact critical-time arithmetic from the adopted complete prefix

[critical_mean_bounds.py](critical_mean_bounds.py) evaluates the complete adopted C793 return and first-return arrays through512 together with C796's exact paid Green bound.
The complete analytic result is [adopted C800](../../../claims/Yin_C_G0800_v1.md#decision-whole-reviewed-2026-10-26), through [whole independent mathematical/native R1020](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding); the native arithmetic and conditional-probability/critical-limit proof scopes are separately retained there.
The sole fixed mathematical input is [inputs/return_weights_512.json](inputs/return_weights_512.json), retaining just the necessary complete W/V arrays and their original-law scope.
Its status, original digit law, exact0--512 scope,513-entry arrays, every renewal equality and exact p512 control are checked before rational Horner evaluation.
No author graph module is imported, and no state, height cap or later return time is constructed.
The declared source-file cap is16MiB, with a20000-digit integer parser limit; all arithmetic uses Python's standard-library integers and fractions.

Run with that adopted input already present:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/critical_mean_bounds.py
```

The --input and --output options choose explicit paths; defaults resolve from this actual containing J group.
The completed run atomically wrote critical_mean_bounds.json (`mathematics/computations/outputs/Yin_J_G0052/critical_mean_bounds.json`), retaining exact finite polynomials, late masses/transforms, all rational coarse inequalities and the displayed threshold certificates.
The checked512-prefix lower expression is2097+75308737880088962253/881000000000000000000; the checked30000-step tail lower expression exceeds1/350 by3312757947/36444595250000.
The file also retains the Green-only1939 and10000-step certificates and the actual positive-phase, stationary-scope and mixed-dual arithmetic.
Decimal fields are display-only; every mathematical comparison is exact.
The whole independent review and adoption of these new analytic consequences remain separate from C793's already adopted finite completeness.
Old programs and outputs remain unchanged, and no finite/infinite critical-mean classification is claimed.

## Independent verification of critical-time arithmetic

The new [reviewer_critical_mean_verify.py](reviewer_critical_mean_verify.py) imports no author functions and computes no graph or coefficient after time512.
It compares all513 W/V entries with the earlier independent reviewer_return512_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_return512_result.json`), rechecks every renewal identity and the adopted p512, and evaluates all512 terms of the needed polynomials through ascending common-denominator integer sums rather than the author's Horner routine.
It independently checks every displayed rational difference certificate and every exact mathematical payload field in critical_mean_bounds.json.
The analytic conditional-probability, infinite-mean, true-phase and canonical-dual steps are separately covered by [whole R1020](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding).

Run from the repository root with the three declared existing inputs present:

```powershell
.venv/Scripts/python.exe -B -S mathematics/computations/programs/Yin_J_G0052/reviewer_critical_mean_verify.py
```

The --input option defaults to inputs/return_weights_512.json.
The --independent-prefix and --author-result options default respectively to reviewer_return512_result.json and critical_mean_bounds.json in this J output home, produced in the current reproduction order above.
The --output option remains in that home and defaults to reviewer_critical_mean_result.json (`mathematics/computations/outputs/Yin_J_G0052/reviewer_critical_mean_result.json`).
The independent command completed successfully, matched all exact payload values and published its result atomically after those checks.
Each input is capped at16MiB and integer parsing at20000 digits; a failed check has a separate incomplete result.
The native comparison reuses C793's unchanged accepted finite completeness and its prior independent result, while the new mean, tail, phase and convolution arithmetic is independently recomputed.
No new graph, larger source range or critical-mean branch classification is asserted.

<a id="distance-eight-existing-boundary-channels"></a>
## Existing-state distance-eight boundary channels

The complete deterministic reproduction from a checkout without generated output is:

```powershell
python -B mathematics/computations/programs/Yin_J_G0052/shortest_first_hit.py
python -B mathematics/computations/programs/Yin_J_G0052/geodesic_detour_cost.py
python -B mathematics/computations/programs/Yin_J_G0052/verify_geodesic_level9.py
python -B mathematics/computations/programs/Yin_J_G0052/finite_core_resummation.py
python -B mathematics/computations/programs/Yin_J_G0052/boundary_channels_existing.py
python -B mathematics/computations/programs/Yin_J_G0052/verify_boundary_channels_existing.py
```

These unchanged standard-library programs construct the ordered417-state depth24 domain, reconstruct the complete through9 classifications and then supply the original core/exit comparison before constructing and checking the boundary certificate.
The core inverse, full cost table and level9 polynomials are reproducible intermediates; they are not additional indispensable retained boundary inputs.
The producer and checker retain their original three and four explicit input interfaces, strict strip, weights, finite domain and resource limits.
This sequence has been replayed successfully with all142 positive and182 zero channels,648 checked words and60 transfer terms.
This is current reproduction of the same mathematical object, not recovery of the original execution bytes or a new R finding.

The complete statement and DC1--DC7 proof are fixed in [C846](../../../claims/Yin_C_G0846_v1.md#complete-argument), [adopted](../../../claims/Yin_C_G0846_v1.md#decision-whole-reviewed-2026-10-28) through [whole independent mathematical/native R1066](../../../audits/reviews/Yin_R_G1066_v1.md#whole-distance-eight-boundary-finding), using [adopted C841](../../../claims/Yin_C_G0841_v1.md#decision-whole-reviewed-2026-10-28).
The completed [producer](boundary_channels_existing.py) uses exactly the existing417 supplied shortest-hit states, with a combined16MiB input cap and120-second bound.
Its three native inputs are shortest_first_hit_24.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_24.json`), geodesic_level9_check.json (`mathematics/computations/outputs/Yin_J_G0052/geodesic_level9_check.json`) and finite_core_resummation_8.json (`mathematics/computations/outputs/Yin_J_G0052/finite_core_resummation_8.json`).
The accepted complete distance-through9 scope from [R1053](../../../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) supplies the actual47-state K; the full417 distance24 calculation is only a supplied finite list here and is not labelled independently accepted.
The old full417 core-resummation author verifier is not an input to this calculation.

All three original successor and predecessor candidates are checked locally for every supplied tuple, with exact strict-strip tests and original probabilities1/4,1/2,1/4.
No new graph vertex is added.
Legal tuples outside the417-state set remain UNKNOWN frontier tuples and are never searched.
Complete local rows of K supply the full U and V, including V equal to the ten distance9 states.
Actual closed forward or backward first-A domains certify zero channels; finite induced nonreachability alone supplies no exclusion.

The completed boundary_channels_8_existing.json (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_existing.json`) retains A's18 tuples, full core/boundary successor and predecessor rows, all36 search domains and their unknown frontiers, all324 channel statuses, all positive first-A words and boundary reachability words, the exact finite polynomials, and the entire forced-first-step certificate.
The true exterior communicating relation restricted to A has one ten-state class I={47,48,49,50,53,54,55,56,75,82} and eight singleton classes.
This identifies classes on A, without claiming to enumerate the full possibly infinite exterior class containing I.
The142 positive first-A channels are100 within I,40 from{72,85,88,105} into I, and59->51 plus68->52.
The other182 channels are proved zero, and the two exceptional positive channels are exactly t/4.
All150 full reachability pairs, including empty identities, have positive words; all174 remaining ordered pairs are excluded by actual finite closure.

Each of the four source states has a complete outside successor row entering only{61,66,74,83,113,122}.
Actual positive connectors in both directions put these six states in I's true exterior communicating class.
The field forced_first_step contains all source rows, twelve anchor connector words and all60 chronological diagonal-transfer terms needed for the40 crossings into I.
Together with the two polynomials, these prove all boundary Green entries finite whenever the COMPLETE actual deleted-diagonal series D_K(t) is finite.
They do not prove a diagonal estimate.
With an actual t_*>R and D_K(t_*) finite, C846 invokes C841's separately paid finite coupling to obtain R_f>R; no general bound R_f>=1/alpha is claimed.

The distinct [author checker](verify_boundary_channels_existing.py) imports only the earlier generic exact polynomial/interval helper and does not import the producer or its graph searches.
It uses polynomial reduction for all local forward/inverse transitions, rational root isolation and strict-strip margins, depth-first closed-domain reconstruction and Boolean boundary reachability closure.
It rechecks all1251 successor and1251 predecessor probes, all324 channels, all648 saved word occurrences and all60 transfer terms.
Its completed boundary_channels_8_check.json (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_check.json`) retains four rational margin intervals for every one of the390 candidates at all65 core/boundary states, together with the complete counts, communication partition and limits.
The largest checked word has28 steps; the longest closing word in the60 transfer terms has21.
The76 unknown forward and52 unknown predecessor edges remain unknown; none is silently killed or used as an actual absence argument.
The checker remains author code; [R1066](../../../audits/reviews/Yin_R_G1066_v1.md#whole-distance-eight-boundary-finding) supplies the separate whole independent mathematical/code inspection and complete reproduction of both unchanged programs.
Both entire parsed JSON outputs agreed exactly before and after that reproduction, and the original three inputs remained unchanged.
The review covers all declared local rows, words, support and transfer terms, without promoting full417-state BFS completeness or proving the diagonal tail estimate.

Reproduction uses the repository Python environment and the three existing inputs, in this order:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/boundary_channels_existing.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_boundary_channels_existing.py
```

Both commands completed successfully within their unchanged417-state/16MiB/120-second limits and atomically published their own outputs.
The checker adds only the producer result as its fourth input.
The producer writes a separate incomplete result on a caught failure; neither a failed run nor an old result can substitute for a successful checked run.
No new graph, radius scan, height increase, later-time return generation or parameter grid was run.
The remaining mathematical input is a supercritical complete diagonal bound.
Root completed the whole author-side reading before fixing C846 and adopted its complete conditional statement after reading R1066.
For this K8, no additional cross-component convergence input remains once the complete diagonal series is finite; the more general C841 criterion keeps its crossing hypothesis.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.

## Recorded runs

The local output names below identify the particular recorded runs used by the linked fixed materials.
Those records retain the original inputs, parameters, known dates and checked scopes; the existing instructions above identify the programs and reproduction commands.
These links locate the original results and checks, without asserting verification of the present README or a new execution.
Generated output files remain local and are not synchronized.

| Local run output | Original result or check record |
| --- | --- |
| `critical_mean_bounds.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding); [Claim support and recorded result](../../../claims/Yin_C_G0800_v1.md) |
| `midpoint_continuation.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0996_v1.md#complete-midpoint-native-and-radius); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding); [Claim support and recorded result](../../../claims/Yin_C_G0776_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0793_v1.md) |
| `midpoint_profile.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0999_v1.md#complete-profile-and-signed-diagnostic); [Claim support and recorded result](../../../claims/Yin_C_G0779_v1.md) |
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0621_v1.md#conditional-gaussian-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0639_v1.md#isolated-conditional-gaussian-whole-finding); [Claim support and recorded result](../../../claims/Yin_C_G0419_v1.md) |
| `return_midpoint_512.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding); [Claim support and recorded result](../../../claims/Yin_C_G0793_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0800_v1.md) |
| `reviewer_critical_mean_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding) |
| `reviewer_return512_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1020_v1.md#whole-critical-time-finding); [Claim support and recorded result](../../../claims/Yin_C_G0793_v1.md) |
