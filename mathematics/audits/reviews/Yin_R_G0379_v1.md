---
author: Yin
---
# Independent finite review of the buffered shear H35 logarithmic screen

Date: 2026-10-18T10:14.
Human record author Yin.
The main agent separately assigned the two-input J100 component diagnostic under the continuing G0001 authority.
The reviewer developed the independent J100 checker and had previously developed the J99 checker and R377 finding.
The reviewer did not develop the J100 author program, C157v2 proof, buffered-shear construction or all-parameter screen.
This is a new finite computational and application review, not a new whole-proof review of C157v2 or a completion review of G0001.

The arrangement is non-blind.
The assignment and shared history supplied the new buffered family, its proposed H35 screen, the earlier two-input results, the exact Jensen expression and the bounded certification requirements.
The reviewer read C157v2 and the applicable original numerator and scalar Jensen interfaces.
No numerical work began until the main agent confirmed actual C157v2 acceptance through R378.
The reviewer completed both independent direct-H35/Jensen calculations before reading the new author program or numerical payload.
Afterward the reviewer read the entire author program, added exact and scalar comparisons, and inspected the whole completed J100 README.
The final checker also verifies the README's operational-margin consequence directly from the same enclosing screen ball.

Both implementations use complete-root Jensen with python-flint0.9.0 and FLINT Arb/Acb; the author additionally uses SymPy1.14.0 for exact trace construction.
Independence here concerns the separately authored integer-numerator and rational-trace constructions and code, not distinct numerical algorithms, independent libraries or formal verification.
The reused JV values are previously certified enclosures from the two explicit J99 outputs accepted by R377, not new independent calculations in this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-input H35 finding](#two-input-h35-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-input H35 finding](#two-input-h35-finding) | [J100 completed account](../../computations/programs/Yin_J_G0100/readme.md#certified-results) | Entire completed account, original inputs, two new JG integrals, explicit JV reuse, all displayed quantities, screen consequences, actual bounded execution and limitations. |
| [Two-input H35 finding](#two-input-h35-finding) | [Original input](../../computations/programs/Yin_J_G0097/input.json) | Exactly the quartic_Salem_seed and Lehmer_degree10 integer coefficient lists; no new original input or use of the other two entries. |
| [Two-input H35 finding](#two-input-h35-finding) | [Author program](../../computations/programs/Yin_J_G0100/main.py) | Entire exact trace/global-g construction, centered scalar, complete-root Jensen sum, retained JV use, precision/time bounds and reported scalar certification. |
| [Two-input H35 finding](#two-input-h35-finding) | [Independent checker](../../computations/programs/Yin_J_G0100/verify.py) | Direct integer H35 construction, complete roots and multiplicities, prior-input checks, exact trace/g/scalar identities, scalar comparisons and rational operational-margin check. |
| [Two-input H35 finding](#two-input-h35-finding) | [Prior finite acceptance](Yin_R_G0377_v1.md#two-input-component-finding) | Reused J99 certification of exactly these JV quantities and their input/normalization scope, with its shared-library and finite-review limits. |
| [Two-input H35 finding](#two-input-h35-finding) | [Accepted C157v2 gate](../../claims/Yin_C_G0157_v2.md#decision-whole-reviewed-2026-10-18) | Actual accepted changed-value arithmetic and analytic theorem before numerical execution; no new full arithmetic proof is supplied here. |
| [Two-input H35 finding](#two-input-h35-finding) | [C157v2 analytic screen](../../claims/Yin_C_G0157_v2.md#logarithmic-screen) | JG scalar normalization and the all-real-s/all-positive-q lower bound with integrable circle zeros, applied separately to each fixed input. |
| [Two-input H35 finding](#two-input-h35-finding) | [Whole C157v2 review](Yin_R_G0378_v1.md#buffered-shear-whole-independent-finding) | Reused complete accepted proof and dependency interfaces, distinguished from the new finite numerical/application review. |
| [Two-input H35 finding](#two-input-h35-finding) | [C149 original numerator](../../claims/Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact H35=250P(t^3)^5-243P(t^5)^3 with degree15d, leading coefficient7 and supplied scalar30375. |
| [Two-input H35 finding](#two-input-h35-finding) | [F109 scalar Jensen interface](../../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent scalar identity retaining all root multiplicities, leading coefficient and possible circle zeros. |
| [Two-input H35 finding](#two-input-h35-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0100/readme.md#recorded-runs) | Both exact trace objects, factor/root evidence, six scalar enclosures, displayed decimals, actual precision and zero parameter-grid evaluations. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0100/results.json`; this target locates that original run's computation account. |
| [Two-input H35 finding](#two-input-h35-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0100/readme.md#recorded-runs) | Both original H35 polynomials, complete factor/root balls, prior JV evidence, attempt records, scalar certification, comparisons and the verified1/16 operational-margin exclusions. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0100/verification.json`; this target locates that original run's computation account. |
| [Two-input H35 finding](#two-input-h35-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0099/readme.md#recorded-runs) | Explicit already-certified JV enclosures and original input lists consumed by the author; no recomputation in J100. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0099/results.json`; this target locates that original run's computation account. |
| [Two-input H35 finding](#two-input-h35-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0099/readme.md#recorded-runs) | Complete independent certificate, original inputs, denominator/center normalization, actual JV balls and previous comparison result reused by the checker. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0099/verification.json`; this target locates that original run's computation account. |

## Two-input H35 finding

**PASS for the exact two-input component diagnostic and its stated consequences.**
Each displayed twelve-decimal scalar has certified absolute error below1e-10.
The two independent exact constructions and complete-root sums agree, including the full supplied denominator30375 and the factor2 in JG.
The reused JV uncertainty is propagated as an enclosing ball, rather than replacing the prior result by its displayed decimal.

| Original input | JG | Reused JV | S=JG+JV+log2 | All-parameter lower envelope | Envelope minus log2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| quartic_Salem_seed | -2.725047379018 | 2.363883636679 | 0.331983438221 | 0.859138899671 | 0.165991719111 |
| Lehmer_degree10 | -2.761495809192 | 1.991241720952 | -0.077106907680 | 0.654593726720 | -0.038553453840 |

The lower envelope is log2+S/2, equivalently3log2/2+(JG+JV)/2, for every real s and every real q>0 on the fixed original input.
The quartic row has S>0, so the entire real-s/positive-q family fails I_(s,q)<log2 on that input.
The Lehmer row has S<0, so this sufficient test does not exclude a smaller improvement below log2; it does not construct a successful parameter or prove that the bound is attained.
The checker also verifies S/2>-1/16 from the actual interval on both inputs.
Consequently both all-parameter families fail the earlier operational target I_(s,q)<=log2-1/16 when that resource-allocation margin is applied here.
This rational comparison is a consequence of the same two integrals and introduces no parameter search or extra integration.
The operational margin is not a necessary mathematical threshold for a useful future theorem.

### Exact construction, centering and normalization

The checker binds the two original coefficient lists and constructs P(t^3) and P(t^5) directly in integer polynomial arithmetic.
Its H35=250P(t^3)^5-243P(t^5)^3 is reciprocal of exact degree15d with leading and constant coefficient7.
The newly evaluated quantity is exactly JG=2m(H35)-2log30375.
The centering monomial has circle modulus one and contributes no logarithmic scalar.
There is no degree division, dropped leading coefficient, lost root multiplicity or scalar cancellation treated as free.

The author independently reconstructs the degree-d/2 trace polynomial T and forms the global rational g=T(C_5)^3/125-2T(C_3)^5/243 before any reduction modulo T.
It centers g at exponent15d/2, clears its rational denominator and computes the Mahler logarithm of the resulting integer polynomial with that denominator restored.
After its own arithmetic, the checker exactly verifies t^(d/2)T(t+t^(-1))=P(t), -30375t^(15d/2)g(t+t^(-1))=H35(t), and the full centered integer/scalar identity.
These are exact whole-polynomial identities, not evaluations at selected original roots.
The correct exponent is integral because the original degree d is even.

The author freshly checks the original reciprocal, monic, constant-one, irreducible and noncyclotomic properties and the full simple real-root count of the actual trace polynomial.
The unchanged original input eligibility and its prior accepted finite scope are consistent with R377's earlier reuse of R374.
The general buffered arithmetic theorem is reused from C157v2 and R378; no new weighted original norm or original-root/Haar transfer estimate is inferred from these calculations.

### Explicit prior JV dependency

The author reads exactly J99/results.json and the checker reads exactly J99/verification.json as retained generated inputs.
Both bind the same two original names and complete ascending coefficient arrays before using the existing JV balls.
The independent checker requires the prior complete and independent-complete flags, completed comparison status, reported error bound, degree, V denominator800^2 and centering exponent-10d, and the earlier successful JV comparison.
It reparses the actual ball at the current precision, verifies its finiteness, radius, sign and existing decimal-error bound, and propagates that uncertainty into the new screen.
The new author JV ball is also checked to contain its own earlier author enclosure.
No JV root isolation or integration is executed in J100.
Missing prior output remains a missing declared dependency; neither program searches for substitute inputs or silently recomputes it.

### Complete Jensen certification and comparison

Each program computes an exact squarefree factorization, checks that its factors multiply back to the entire polynomial, and checks that every factor is squarefree.
The successful Acb root call returns the complete isolated root set for each factor.
The verifier checks full degree, pairwise disjoint balls within each factor and the degree counted with multiplicity.
Each root contributes log(max(1,abs(root))) through an enclosing interval maximum, without guessing a side when a root ball meets the unit circle.
The leading coefficient enters the full Jensen formula explicitly.

The independent H35 polynomials are squarefree of degrees60 and150.
Their root balls split23/23/14 and61/61/28 into inside/outside/unit-circle-overlapping classes, respectively.
The overlapping counts describe enclosures and are not additional exact circle-root assertions.
The interval maximum includes these cases, so no singular-log regularization, root deletion or unjustified strictly positive quadrature is involved.

The checker compares all six new/reused scalar quantities with the author's persisted payload: JG,JV,log2,S,the all-parameter lower envelope and its excess over log2.
Both balls must be finite and narrow enough, their intervals must overlap, their signs must agree, and every author decimal must lie within strict error1e-10 of the independent enclosure.
The author's internal scalar-radius requirement is1e-12; the checker's is1e-10, with a separate decimal-error check.
Each method's enclosing arithmetic and exact Jensen reduction is its certificate; agreement is a consistency check in addition to those independent constructions.

### Actual limits and interpretation

Both author and independent calculations succeeded at256 bits on both inputs, with no failed numerical attempt or precision escalation in the completed records.
The implemented schedule allows only one escalation to512 bits, root maxprec is the current attempt's ceiling, and each full subprocess has a300-second cap.
All successful outputs are published atomically after their stated checks.
The first independent calculation preceded inspection of the new author code/output; subsequent bounded verification added exact/payload comparisons and the rational operational-margin consequence.
The full final README and its commands, table, dependency statements and distinctions between a negative sufficient screen and an actual success were inspected before this finding.

Only two distinct JG integrals are new.
The already certified JV values were reused, and zero s/q grid points, candidate original norms or other component integrals were evaluated.
The mathematical negative sign on Lehmer is certified; what remains inconclusive there is existence of any smaller sub-log2 improvement, not the numerical sign itself.
The result excludes the1/16 operational target on both controls and excludes every sub-log2 value only on the quartic control.
It is not an all-input obstruction or a refutation of all cross-term forms.
The accepted arithmetic theorem survives, while a successful fixed auxiliary, general-input coverage, a uniform transfer estimate and the unrestricted G0001 conclusion remain unresolved.

Both calculations share the same Jensen-root algorithm and FLINT Arb/Acb primitives, so this review does not supply algorithmic or numerical-library diversity.
The accepted R378 whole-proof scope, R377 prior-computation scope and F109 classical scalar interface are reused only as described; their complete historical proof chains are not re-audited here.
Task and execution decisions remain the main agent's responsibility.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
