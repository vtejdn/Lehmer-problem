---
author: Yin
---

# Complete original quartic returns through time 512 and the true midpoint at 256

Human author Yin.
The original_return_512 contributor developed this new bounded native calculation and its finite reduction.
The source graph logic, real-strip enclosures and original-coordinate quadratic mark are reused from the actual author programs of J52, with a separately declared new scope and reached-state cap.
The old programs, outputs and accepted C776/C779 conclusions remain unchanged.
No prior J52 review is transferred to this longer calculation.
This candidate is OPEN pending fresh whole independent mathematical and native review.

## Statement

Fix the actual quartic P(t)=t^4-t^3-t^2-t+1, its exterior root beta and either unit-circle conjugate zeta.
Use the full original chronological process X_0=0, X_(t+1)=beta X_t+e_(t+1), with independent digits of probabilities1/4,1/2,1/4 at-1,0,1.
Retain every original word representation, earlier zero visit, endpoint fiber and both real neutral coordinates.
Let p_t=Pr(X_t=0), let f_t be its first-positive-return probability at t, and set W_t=4^t p_t, V_t=4^t f_t, W_0=1 and V_0=0.
The exact native arrays in this material's selected J52 output give the COMPLETE original W_t and V_t at EVERY0<=t<=512, with zero omitted return mass.
Every old entry0<=t<=256 agrees exactly with accepted C776's complete return and first-return arrays.
The new probability is

    p512 = N512 / 2^1019,
    N512 = 5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399.

Put D256=p512/p256^2 and M256=E[|X256(zeta)|^2 given X512=0].
The actual complete midpoint law has58669 positive-weight states, and its exact integer/quadratic-field values satisfy

    36.968603 < D256 < 36.968604,
    0.228798 < M256/256 < 0.228799.

All displayed decimal endpoints are exact rationals and all inequalities are strict.
In particular M256>256/5.
Both neutral coordinates occur in the squared complex modulus; no single-coordinate projection substitutes for it.
At EVERY1<=t<=512, p_t<beta^(-t).
The distinct finite first-return quantity satisfies

    0.954048 < sum_(j=1)^512 f_j beta^j < 0.954049 < 1.

Thus neither finite sufficient crossing test succeeds within this declared range.
No converse about later times, positive limiting midpoint growth, finite or infinite critical mean, R=beta versus R<beta, a new radius bound, varying input family, uniform entropy estimate or the unrestricted G0001 conclusion is asserted.

## Complete argument

### Reused scope and deterministic completeness

The needed existing method is already fully retained in [adopted C776 MC1--MC3](Yin_C_G0776_v1.md#complete-argument), [C559's all-return height argument](Yin_C_G0559_v1.md#salem-complete-quotient-height-tail) and [C419's exact original integral reversal](Yin_C_G0419_v1.md#argument).
The actual [C779 profile scope](Yin_C_G0779_v1.md#statement) stops at total time256 and is not extrapolated or rerun here.
These existing fixed inputs suffice for the longer finite calculation; this work invokes no new external theorem or profile assumption.

For quotient states q=(q0,q1,q2,q3), put

    S_e(q)=(q1,q2,q3,-q0+q1+q2+q3+e),
    w_(-1)=w_1=1, w_0=2.

The existing complete-return bound gives, for EVERY returned word of length t<=512,

    ht(E/P)<6/5+(11/30)floor(t/2)
             <=6/5+(11/30)256=1426/15<96.                 (FC1)

Its quotient coefficients are integers, so every such returned path lies in height95.
The two original real-place strip bounds remain valid for every full original returned path.
The native helper forms sign-aware outward intervals at coefficient scale10^6 from861/500<beta<1723/1000; a rejected interval cannot contain a valid original core point.
The new program copies the original forward graph construction and backward reachability pruning, with its own explicit500000 reached-state cap and without modifying the old helper's100000 cap.
Forward reachability from zero and backward reachability to zero remove no boxed returned path.
Together these facts prove zero omitted original return mass at each t<=512, independently of the subsequent numerical counts.

The completed graph has269715 forward-reached states,254775 states that can return inside the box, and443125 retained directed digit edges.
The enclosing Cartesian box has1330863361 points; these are neither all enumerated nor substituted for actual graph vertices.
The declared cap counts reached states, not edges.
The graph completed within that fixed cap and the declared live memory limits.
There is no claim of a global finite core or completeness beyond time512.

### Integer recurrences and complete return coefficients

In this finite graph, F_t(q) is the integer weight of boxed paths from zero to q in t steps and B_t(q) is the integer weight of boxed paths from q to zero in t steps.
Initialize both at the delta mass at zero and use

    F_(t+1)(r)=sum_(q,e:S_e(q)=r) w_e F_t(q),
    B_(t+1)(q)=sum_(e:S_e(q) retained) w_e B_t(S_e(q)).    (FC2)

No killed mass is renormalized, and all intermediate zero visits remain in these recurrences.
By FC1, W_t=F_t(0) is the complete original integer return weight for0<=t<=512.
The native program evolves F through512 and B separately through256; B_t(0)=W_t is checked at every0<=t<=256.
Its new forward array agrees with every old accepted return entry0<=t<=256, not only selected controls.

Splitting a returned word at its first positive zero time gives the exact renewal identity

    W_t=sum_(j=1)^t V_j W_(t-j),
    V_t=W_t-sum_(j=1)^(t-1) V_j W_(t-j).                 (FC3)

The products have the same denominator4^t, so this inversion uses integers with the original probabilities.
The native program checks V_t>=0 at every1<=t<=512 and exact equality of every old first-return entry0<=t<=256.
It saves both full arrays, including W0=1,V0=0, and the exact reduced p512 displayed in the statement.
Nonnegativity is a consistency check; completeness follows from FC1--FC3, not merely that check.

### Exact actual midpoint and both neutral coordinates

Splitting every complete time512 returned word at256 gives

    w(q)=F256(q)B256(q),
    sum_q w(q)=W512,
    D256=W512/W256^2.                                  (FC4)

The output retains the quotient-state list and the entire aligned F256 and B256 vectors.
They are boxed endpoint weights; only their product is claimed to equal the full original conditioned bridge law.
This distinction matters at states that cannot participate in the time512 bridge.
The native product sum agrees exactly with the independently evolved forward W512.

Use the integral map

    Psi(q)=a0+a1 beta+a2 beta^2+a3 beta^3,
    (a0,a1,a2,a3)=(-q0+q1+q2+q3,-q1+q2+q3,-q2+q3,-q3).

It obeys beta Psi(S_e(q))-e=Psi(q).
The complete C419 reversal and digit-negation bijection preserves every original word probability and takes the quotient central state to the actual original central state Psi(q).
The implementation additionally checks the displayed linear identity on zero and the four basis vectors for all three digits; this finite algebra check supplements rather than replaces the full original-law bijection.

For s_l=sum_(j=0)^(3-l) a_j a_(j+l), put

    A(q)=2(s0+s2+3s3)+(s1+s2+s3),
    B(q)=-(s1+s2+s3).

As in C776, u=zeta+zeta^(-1)=(1-sqrt13)/2 obeys u^2-u-3=0, so zeta^2+zeta^(-2)=u+1 and zeta^3+zeta^(-3)=u+3.
Expansion of the full complex squared modulus gives

    |Psi(q)(zeta)|^2=(A(q)+B(q)sqrt13)/2,
    A_sum=sum_q w(q)A(q), B_sum=sum_q w(q)B(q),
    M256=(A_sum+B_sum sqrt13)/(2W512).                  (FC5)

The native output retains both exact integer sums and their two rational coefficients, not a rounded estimate.
It also checks that every weighted quotient-coordinate sum is zero, an actual global symmetry check that supplies no conditional-component centering claim.
Exactly58669 states have w(q)>0.

The strict rational bracket

    3605551275463989/10^15 < sqrt13 < 3605551275463990/10^15

is certified by squaring both endpoints.
It is substituted with the sign of B_sum retained, giving exact rational lower and upper bounds on M256, then divided by256.
Their enclosure in the statement's strict rational interval, together with the exact D256 interval from FC4, is checked in the native program.
This proves the finite midpoint assertions subject to the declared native/review boundary; no all-late lower bound follows from one additional time.

### Refined-root finite crossing tests

Within the existing beta bracket the polynomial is strictly increasing: P''(t)=12t^2-6t-2>0 for t>=3/2 and P'(3/2)=11/4>0.
Both original endpoints exceed3/2, with opposite polynomial signs.
Forty exact rational bisections therefore retain the actual beta between

    b_lo=1893451168414823/1099511627776000,
    b_hi=236681396051853/137438953472000.                 (FC6)

The native program checks P(b_lo)<0<P(b_hi).
At EVERY1<=t<=512 it checks the strict rational inequality

    (W_t/4^t)b_hi^t<1,

which implies p_t<beta^(-t).
The nonnegative complete first-return coefficients separately give

    sum_(j=1)^512 (V_j/4^j)b_lo^j
       <sum_(j=1)^512 f_j beta^j
       <sum_(j=1)^512 (V_j/4^j)b_hi^j.

The outer two exact fractions are retained in the native output and enclosed strictly between0.954048 and0.954049.
Strictness follows already from the positive time1 coefficient and b_lo<beta<b_hi.
Thus the finite first-return sum is less than1 at this same declared512 scope.
Failure of either finite sufficient test proves neither equality of the true radius with beta nor absence of a later crossing.
No unknown first-return tail is replaced by zero in an infinite-time assertion.

### Native reproduction and remaining review boundary

The program is [return_midpoint_512.py](../computations/programs/Yin_J_G0052/return_midpoint_512.py), with actual retained evidence return_midpoint_512.json (`mathematics/computations/outputs/Yin_J_G0052/return_midpoint_512.json`).
Run from the repository root on Windows:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/return_midpoint_512.py

Python's standard library suffices, with the explicitly selected same-group author helpers and accepted midpoint_continuation.json prefix input.
The output destination and prefix input have explicit command-line options and default to the actual containing J group's output home.
The scope, height95,500000 reached-state cap, original root strips and live memory stops were written in the program and J README before execution.
The live stops are a process working set at least4GiB or available physical memory below1GiB, checked every4096 graph states and16 recurrence steps, with further graph-pruning/midpoint/final checks.
Unavailable monitoring, a reached cap or a failed native check stops incomplete rather than silently enlarging the bound.
These are periodic operational safeguards, not a hard allocator limit or mathematical hypothesis.
There is no artificial elapsed-time limit.
The successful complete JSON is written through an atomic sibling replacement only after every declared check; failed execution has a separate clearly incomplete output.
The completed run required no cap or range change and left old programs and outputs intact.

These are author calculations reusing author mathematical helpers, not independent implementation or formal verification of Python.
Fresh independent whole inspection must cover FC1--FC6, the new graph cap/scope, native recurrences, saved vectors, complete old-prefix comparisons, exact p512, midpoint intervals and both finite tests before adoption.
The data can supply an exact input to a separately proved infinite-time radius estimate, but this Claim selects no such new estimate and makes no asymptotic conclusion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision return-midpoint-512-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T12:06 |
| status | open |
| reason | Fix the complete author native result at the predeclared time512 and midpoint256 scope, with zero omitted return mass, exact full arrays and old-prefix agreement. Fresh whole independent mathematical/native review remains required. All asymptotic and radius conclusions remain outside this finite statement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite statement](#statement) | Actual original quartic law; all0--512 return/first-return weights, exact p512, full true midpoint256 and D256, positive support count, strict rational intervals and both failed finite crossing tests, with all exclusions. |
| argument | [Complete FC1--FC6 argument](#complete-argument) | Deterministic completeness, graph preservation, integer recurrences/renewal inversion, actual original midpoint bijection and Qsqrt13 mark, exact rational enclosures and refined-root finite tests. |
| dependency | [Adopted complete height method](Yin_C_G0559_v1.md#decision-complete-isolated-whole-adoption) | Full original returned-path quotient height with C0<6/5 and C1<11/30, outward real-strip screens and boxed zero-return preservation, specialized only to time512 and height95. |
| dependency | [Adopted original reversal](Yin_C_G0419_v1.md#decision-complete-isolated-whole-adoption) | Complete integral reversal/digit-negation bijection and preservation of all original word weights and actual midpoint coordinates. |
| dependency | [Adopted original midpoint framework](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Complete original finite-weight conventions, exact neutral quadratic mark, accepted0--256 return and first-return prefix, and finite-test interpretations; no inherited review of the new scope. |
| support | [New native program](../computations/programs/Yin_J_G0052/return_midpoint_512.py) | Entire declared height95/time512 author calculation, explicit500000 cap and memory stops, all exact recurrences/enclosures and old-prefix comparisons. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Full513-entry return and first-return arrays, exact p512, quotient states and aligned forward256/backward256 vectors, both midpoint field sums, support count, D256, intervals and finite pressure tests. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/return_midpoint_512.json`; this target locates its run account. |
| support | [Original unchanged graph helpers](../computations/programs/Yin_J_G0052/experiment.py) | Actual successor, allowed-state and rational-strip/constant functions; its old100000 cap is preserved and not used as the new program's cap. |
| support | [Original unchanged coordinate helpers](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Original-coordinate and exact quadratic-mark functions, with the old main function and old output unchanged. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Declared comparison input for every return and first-return entry0--256, retaining W0=1 and V0=0. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`; this target locates its run account. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T12:26 |
| status | proved |
| reason | Root read the complete fixed FC1--FC6, new author program and whole independent mathematical/native R1012 and adopts the complete original time0--512 return/first-return arrays, exactp512, full midpoint256 and finite tests without substantive repair. The independent graph/recurrences/mark and all254775 statewise vector pairs match; every oldprefix entry is retained. This bounded finite statement supplies no asymptotic, radius, critical-mean or unrestricted Task conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete finite statement](#statement) | Actual original quartic law; all0--512 return/first-return weights, exact p512, full true midpoint256 and D256, positive support count, strict rational intervals and both failed finite crossing tests, with all exclusions. |
| argument | [Complete FC1--FC6 argument](#complete-argument) | Deterministic completeness, graph preservation, integer recurrences/renewal inversion, actual original midpoint bijection and Qsqrt13 mark, exact rational enclosures and refined-root finite tests. |
| dependency | [Adopted complete height method](Yin_C_G0559_v1.md#decision-complete-isolated-whole-adoption) | Full original returned-path quotient height with C0<6/5 and C1<11/30, outward real-strip screens and boxed zero-return preservation, specialized only to time512 and height95. |
| dependency | [Adopted original reversal](Yin_C_G0419_v1.md#decision-complete-isolated-whole-adoption) | Complete integral reversal/digit-negation bijection and preservation of all original word weights and actual midpoint coordinates. |
| dependency | [Adopted original midpoint framework](Yin_C_G0776_v1.md#decision-whole-reviewed-2026-10-26) | Complete original finite-weight conventions, exact neutral quadratic mark, accepted0--256 return and first-return prefix, and finite-test interpretations; no inherited review of the new scope. |
| support | [New native program](../computations/programs/Yin_J_G0052/return_midpoint_512.py) | Entire declared height95/time512 author calculation, explicit500000 cap and memory stops, all exact recurrences/enclosures and old-prefix comparisons. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Full513-entry return and first-return arrays, exact p512, quotient states and aligned forward256/backward256 vectors, both midpoint field sums, support count, D256, intervals and finite pressure tests. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/return_midpoint_512.json`; this target locates its run account. |
| support | [Original unchanged graph helpers](../computations/programs/Yin_J_G0052/experiment.py) | Actual successor, allowed-state and rational-strip/constant functions; its old100000 cap is preserved and not used as the new program's cap. |
| support | [Original unchanged coordinate helpers](../computations/programs/Yin_J_G0052/midpoint_continuation.py) | Original-coordinate and exact quadratic-mark functions, with the old main function and old output unchanged. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Declared comparison input for every return and first-return entry0--256, retaining W0=1 and V0=0. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/midpoint_continuation.json`; this target locates its run account. |
| support | [Distinct complete native checker](../computations/programs/Yin_J_G0052/reviewer_return512_verify.py) | Independently executed original-coordinate enumeration, predecessor and killed-first-return recurrences, exact norm and full payload comparison, with the declared unchanged reviewer-helper scope. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Exact independently reproduced arrays, graph/midpoint/pressure results and complete statewise-vector comparison facts at the same finite scope. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/reviewer_return512_result.json`; this target locates its run account. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1012_v1.md#whole-finite-finding) | Entire statement and FC1--FC6, deterministicheight95 completeness, distinct native reconstruction and all513 W/V entries, completeoldprefix/fullvector/mark checks, exactroot finite tests, declaredcap/resource/outputscopes and all exclusions. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0052](../computations/programs/Yin_J_G0052/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
