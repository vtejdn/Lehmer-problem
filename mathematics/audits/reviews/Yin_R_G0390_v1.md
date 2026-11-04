---
author: Yin
---
# Independent finite review of the two-set buffered Lehmer correction

Date: 2026-10-18T11:53.
Human record author Yin.
Root separately assigned this finite and analytic review after authoring the new two-set correction, J101 program and selected phase-cell witness.
The entropy_attainment_bridge AI did not contribute to that new correction, program or witness selection, and supplies the independent checker and this finding.
The reviewer had contributed to neighboring G0001 investigations and source-coverage materials; those roles do not supply a fresh review of their own earlier mathematics.
The accepted C157v2 and J100 results are reused only at their recorded scopes.

The arrangement is non-blind.
The assignment supplied the proposed correction, reported cell counts and margin; the reviewer read the author argument, program and output before writing the independent checker.
The new checker imports no author helper and reconstructs the exact trace polynomial and interval expression separately.
Both programs use python-flint0.9.0 and FLINT Arb, including shared interval and trigonometric primitives.
This is independent analytic/application checking and separately authored finite verification, not numerical-library diversity, a new independent audit of all C157 dependencies, or formal verification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [J101 analytic reduction](../../computations/programs/Yin_J_G0101/record.md#two-set-correction) | Complete identity, logarithmic integrability, two-set case split, normalized Haar measure, all-real-s/all-positive-q consequence, and finite-input limits. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [J101 completed account](../../computations/programs/Yin_J_G0101/readme.md#certified-results) | Entire completed README, exact witness counts, all displayed scalar bounds, reproduction commands, prior reuse, actual refinement and shared-library limits. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Author program](../../computations/programs/Yin_J_G0101/main.py) | Original coefficient/Fourier expression, all8192 whole-cell enclosures at192 bits, retained sign sets, author-prior input, eta and all four scalar quantities. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Independent checker](../../computations/programs/Yin_J_G0101/verify.py) | Triangular trace reconstruction, exact H23/H35 identities, separate trace-Horner interval expression, every retained cell, bounded refinement and all independent scalar/provenance checks. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Original input](../../computations/programs/Yin_J_G0097/input.json) | Only the exact Lehmer_degree10 ascending coefficient list; no substitute input or use of the other three entries. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Prior finite review](Yin_R_G0379_v1.md#two-input-h35-finding) | Accepted J100 complete component certificate and original eligibility/normalization, with its explicit J99/R377 reuse and shared-library limits; no new root isolation here. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [C157v2 selected acceptance](../../claims/Yin_C_G0157_v2.md#decision-whole-reviewed-2026-10-18) | Existing accepted buffered family, exact centered E/G/V functions, supplied denominators and distinction between integer arithmetic and real circle parameters. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [C157v2 analytic interface](../../claims/Yin_C_G0157_v2.md#logarithmic-screen) | Integrable circle zeros and I_(s,q)>=log2+(J_(U,s)+J_V)/2 for every real s and positive real q. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [C157v2 whole review](Yin_R_G0378_v1.md#buffered-shear-whole-independent-finding) | Reused whole theorem and dependency coverage; the present review does not re-audit its full arithmetic proof or source chain. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0101/readme.md#recorded-runs) | Complete exact positive/negative cell lists, counts, normalization, original input binding, declared prior ball and four enclosing scalar results. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0101/results.json`; this target locates that original run's computation account. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0101/readme.md#recorded-runs) | Complete trace/H23/H35 identities, certified cell/depth/slack evidence, precision/cap, prior independent ball, four enclosing scalars and author comparisons. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0101/verification.json`; this target locates that original run's computation account. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0100/readme.md#recorded-runs) | Exact Lehmer original input, complete status, H35 normalization, accepted JG/JV/log2/screen ball and prior comparison; reused without recomputing an integral. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0100/verification.json`; this target locates that original run's computation account. |
| [Two-set Lehmer finding](#two-set-lehmer-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0100/readme.md#recorded-runs) | Exact declared author-prior source and original coefficient binding; J101's stored prior screen equals this supplied quantity and overlaps the independent one. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0100/results.json`; this target locates that original run's computation account. |

## Two-set Lehmer finding

**PASS for the complete new analytic correction and the exact J101 finite certificate.**
All3268 retained original phase cells are independently certified at their asserted strict signs.
For the original Lehmer polynomial and the C157v2 buffered family, the result holds for every real shear s and every positive real weight q.
In particular the enclosing arithmetic proves

    I_(s,q)>0.8163279088>log2,
    I_(s,q)-log2>0.1231807283.

This excludes every sub-log2 Haar value in that entire two-parameter family on the one stated input.
It does not assert an attained optimum, a new full-norm computation, an original-root/Haar transfer theorem, or an obstruction for other forms or inputs.
No mathematical correction to the author reduction or retained witness is required.

### Analytic identity and every parameter

The accepted functions E and G are real on the circle, G is a nonzero Laurent polynomial, and U_s=(E+sG)^2+2G^2.
The independent exact H35 check also confirms G is nonzero on this input as a polynomial, since H35 has degree150 and leading coefficient7.
Its circle zero set is finite, so T=E/G is defined almost everywhere.
The almost-everywhere identity

    log U_s=log G^2+log2+log(1+(T+s)^2/2)

has integrable terms: C157v2 supplies integrability of log U_s and log G^2 through finite-order circle zeros.
Their difference is integrable and equals the nonnegative correction, even where the rational function has poles.
There is no truncation, unverified regularization or subtraction of divergent integrals.

For a>b and sets of Haar measure at least eta with T>=a and T<=b respectively, the split at s=-(a+b)/2 is exhaustive.
For s at or above that value the first set has T+s>=(a-b)/2; below it the second set has T+s<-(a-b)/2.
Monotonicity in the squared absolute value and nonnegativity elsewhere give the stated correction eta log(1+(a-b)^2/8).
This proves the inequality for every fixed real s without needing any uniform dominated-convergence assertion or parameter grid.

Here a=4,b=-4 and eta=1206/8192, so the factor inside the logarithm is exactly9.
Combining with the accepted all-positive-q arithmetic-geometric-mean envelope gives log2+(S+Delta)/2 with S=JG+JV+log2.
The extra correction is divided by2 exactly once.
The original arithmetic norm theorem retains its separate integer-s, integer-q>=1 domain; none is asserted for arbitrary real parameters.

### Independent exact expression and whole-cell verification

The original ascending vector is [1,1,0,-1,-1,-1,-1,-1,0,1,1].
The checker reconstructs the trace polynomial by removing t^5(t+t^(-1))^k from highest degree downward, using exact binomial coefficients.
It obtains

    T_P(X)=X^5+X^4-5X^3-5X^2+4X+3.

It independently constructs integer H23=9P(t^2)^3-8P(t^3)^2 and H35=250P(t^3)^5-243P(t^5)^3, then checks the complete rational-polynomial identities for E and G.
The identities use degrees60 and150, leading coefficients1 and7, centers30 and75, and the exact denominators72 and30375.
No remainder modulo the trace polynomial is substituted for a global circle identity.

For normalized phase x, it evaluates T_P(2cos(2pi kx)), k=2,3,5, by interval Horner arithmetic.
From these values u,v,w it forms E=v^2/9-u^3/8 and G=w^3/125-2v^5/243.
This differs from the author's reciprocal-coefficient Fourier sum and uses no author function or generated trace polynomial.
Both are checked against the same exact centered numerator formulas.

Every dyadic phase ball encloses both endpoints of its entire subinterval.
A division is allowed only when the G interval excludes zero.
A positive cell is accepted only if the entire ratio interval exceeds4; a negative cell only if it is below-4.
The independent checker verifies sorted unique indices, integer range0,...,8191, disjoint lists, exact input/scalar bindings and the retained counts2062 and1206.
Its fixed precision is256 bits, subdivision depth is capped at10, and the full process has a120-second cap.

The actual successful refinement histogram is3208 cells at depth0,58 at depth1 and2 at depth4.
Thus no original cell is discarded or replaced by a smaller certified subset.
The two depth4 cells are388 and7803 in the positive list.
There are3433 interval evaluations including unsuccessful coarser attempts; every claimed original cell is fully covered on success.
All subdivision boundaries are rational and adjacent overlaps have Haar measure zero.
Taking half-open representatives or removing the finite endpoint set makes the phase sets disjoint without changing their measures.
The normalized Haar measure is interval length on x in[0,1], so the minimum measure is exactly1206/8192=603/4096.

No assertion is made about the unclassified original cells or completeness of the full ratio sign regions.
Their contribution is discarded only because the logarithmic correction is nonnegative.
The preliminary point scan supplies no part of the interval certificate.

### Prior uncertainty and resulting enclosures

The verifier reads the exact named J100 independent output, with no alternate input search and no recomputation.
It checks complete/independent-complete status, completed comparison, original coefficients and degree, exact H35 coefficients, G denominator30375^2 and centering exponent-75.
It also checks the declared J99 source of the reused JV, finite narrow balls, source error and sign interfaces, component-sum consistency and earlier comparison results.
The original screen enclosure is reparsed and propagated, not replaced by its rounded decimal.
J101's declared author-prior quantity is checked against the actual named J100 author output and the independent enclosure.

The independent enclosing results are

    Delta=[0.3234683642904639374567055067696694335461117218589442966 +/- 2.00e-56],
    S+Delta=[0.2463614566100635271966822961558738655643651445868502966 +/- 6.24e-51],
    (S+Delta)/2=[0.1231807283050317635983411480779369327821825722934251483 +/- 3.12e-51],
    log2+(S+Delta)/2=[0.8163279088649770730155732695361135008576827066536804024 +/- 3.12e-51].

Each output string is checked to enclose its computed ball.
All four author balls are finite, have radius below1e-10, overlap these independently propagated balls and have the same positive sign.
These comparisons supplement the interval derivation; overlap alone is not used as a proof of the result.
The simpler rational bounds in the finding are also tested directly against the independent balls.

### Retention and scope

The complete reduction now lives in J101/record.md and the finite programs, witness and independent output stay in their responsible J101 homes.
The earlier D43 working address was retired after preservation and incoming-link migration; no older use of that recycled draft address is covered by this review.
This coherent single finite diagnostic needs no separate new Claim to retain its direct analytic reduction.

The checker completed within its fixed scope without precision escalation; actual refinement stayed below its predeclared cap.
No s/q parameter search, new component integral or original resultant/norm was computed.
The preceding quartic all-parameter exclusion remains J100's unchanged accepted result.
This new Lehmer exclusion and that quartic result still do not settle the unrestricted G0001 objective.
Task, route and execution adoption remain with the main agent.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
