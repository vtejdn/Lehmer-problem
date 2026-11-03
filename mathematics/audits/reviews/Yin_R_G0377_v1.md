---
author: Yin
---
# Independent finite review of the two-input balanced component-log screen

Date: 2026-10-18T09:11.
Human record author Yin.
The main agent separately assigned this review of the Stage1 balanced-H25 diagnostic on exactly the quartic Salem seed and degree-ten Lehmer polynomial.
The reviewer developed the separate J99 checker, did not develop the author program or C156 proof, and did not participate in the earlier balanced-weight strategy deduction.
This is a finite computational and interface review, not a Task-completion review or a new whole-proof audit of C156.

The arrangement is non-blind.
Shared task history supplied the proposed weighted family, the component Jensen identities, the required precision/time limits and the earlier J97/J98 context.
The reviewer read the C149 numerator formulas, the C156 candidate and its accepted decision, the F109 scalar Jensen interface, the original J97 input and the existing J98 checker as an implementation reference.
The reviewer waited for actual C156 acceptance before starting numerical work.
The independent original-numerator construction and complete Jensen calculations finished for both inputs before the reviewer read the new author program or its numerical payload.
The reviewer then inspected the whole author program, added exact mathematical-payload comparisons, reran the independent checker, and read the complete J99 README.
The README was corrected to distinguish the actual independent 512-bit escalation and the different internal radius thresholds before this finding was recorded.
Both programs use python-flint0.9.0 and its FLINT Arb/Acb primitives; the author also uses SymPy1.14.0 for exact trace algebra and finite input checks.
Independence concerns the separately organized reconstruction, code and distinct U integration/Jensen algorithms, not independent numerical libraries or formal verification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Two-input component finding](#two-input-component-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Two-input component finding](#two-input-component-finding) | [J99 completed account](../../computations/programs/Yin_J_G0099/readme.md#certified-results) | Entire completed account, both component logarithms on both original inputs, all displayed enclosures and decimals, actual escalation, all-positive-q consequence, skipped grid and stated limits. |
| [Two-input component finding](#two-input-component-finding) | [Original input](../../computations/programs/Yin_J_G0097/input.json) | Exactly the quartic_Salem_seed and Lehmer_degree10 ascending integer coefficient lists; the other two entries are excluded from this test. |
| [Two-input component finding](#two-input-component-finding) | [Author program](../../computations/programs/Yin_J_G0099/main.py) | Entire exact trace reconstruction, global unreduced defects, gcd positivity, analytic U quadrature, centered-f Jensen evaluation of V, bounded certification and reported quantities. |
| [Two-input component finding](#two-input-component-finding) | [Independent checker](../../computations/programs/Yin_J_G0099/verify.py) | Direct H23/H25/H35 construction, exact AU and H25 Jensen objects, complete root/multiplicity accounting, scalar normalization and exact/numerical payload comparisons. |
| [Two-input component finding](#two-input-component-finding) | [Accepted C156 gate](../../claims/Yin_C_G0156_v1.md#decision-whole-reviewed-2026-10-18) | Reused actual acceptance of the changed-value arithmetic and circle-screen theorem before numerical execution; no new whole-proof review. |
| [Two-input component finding](#two-input-component-finding) | [C156 logarithmic screen](../../claims/Yin_C_G0156_v1.md#logarithmic-screen) | Exact JU/JV normalization, integrable circle zeros and the all-positive-real-q lower envelope applied separately to each fixed P. |
| [Two-input component finding](#two-input-component-finding) | [C149 original numerators](../../claims/Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact integer H23/H25/H35 formulas and their supplied denominators. |
| [Two-input component finding](#two-input-component-finding) | [F109 scalar Jensen interface](../../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent identity retaining leading coefficients, complete root multiplicities and possible circle zeros. |
| [Two-input component finding](#two-input-component-finding) | [Prior R374 input eligibility](Yin_R_G0374_v1.md#fixed-2d-finite-finding) | Reused eligibility of the same quartic Salem and Lehmer inputs and their actual totally real trace fields; no prior generated data enters the new arithmetic. |
| [Two-input component finding](#two-input-component-finding) | [Whole C156 review](Yin_R_G0376_v1.md#balanced-weight-whole-independent-finding) | Accepted arithmetic and circle theorem reused at its recorded full scope, distinct from this new finite numerical finding. |
| [Two-input component finding](#two-input-component-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0099/readme.md#recorded-runs) | Both input objects and their six scalar enclosures, root evidence, rounded decimals, strict signs and zero weighted-grid evaluations. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0099/results.json`; this target locates that original run's computation account. |
| [Two-input component finding](#two-input-component-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0099/readme.md#recorded-runs) | Complete AU and H25 factors/root balls, scalar enclosures, failed 256-bit Lehmer attempt and successful 512-bit escalation, all exact and scalar comparison results. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0099/verification.json`; this target locates that original run's computation account. |

<a id="two-input-component-finding"></a>
## Component diagnostic verdict

**PASS at the exact two-input Stage1 scope.**
Both the author and separate checker certify JU+JV>0 on each original input.
The accepted C156 comparison consequently excludes I_bal(q)<log2 for every real q>0 on each of these two inputs, without a parameter grid.
Every displayed twelve-decimal quantity in J99 has certified absolute error below1e-10.
The operational target I_bal(q)<=log2-1/16 is therefore also impossible on these controls.
This is an all-parameter obstruction for this one family on two fixed inputs; it is not an all-input obstruction or a result about arbitrary positive quadratic forms.

| Original input | JU+JV | Lower envelope | Lower envelope minus log2 |
| --- | ---: | ---: | ---: |
| quartic_Salem_seed | 3.242875824944 | 2.314585093032 | 1.621437912472 |
| Lehmer_degree10 | 4.254495252414 | 2.820394806767 | 2.127247626207 |

Each row records lower_envelope=log2+(JU+JV)/2.
The strict signs are certified from enclosing balls, and the lower envelope is not asserted to be an attained minimum over constant q.
The two programs evaluate exactly four distinct component integrals; the checker reproduces the same four quantities with its separate construction.
No weighted-grid candidate or new weighted original norm was computed.

### Exact objects and mathematical interfaces

The independent checker constructs H23=9P(t^2)^3-8P(t^3)^2, H25=75P(t^2)^5-64P(t^5)^2 and H35=250P(t^3)^5-243P(t^5)^3 directly from the two original integer coefficient lists.
It forms AU=13500^2 t^(9d)H23^2+32^2 H35^2 and checks its exact degree30d, reciprocity and endpoint coefficients50176.
It checks H25 degree10d and leading coefficient11.
The Jensen expressions are JU=m(AU)-2log972000 and JV=2m(H25)-2log800; neither contains an erroneous division by d or an omitted scalar.

After independent arithmetic, the checker exactly reconstructs t^(d/2)T(t+t^(-1)) from the author's trace coefficients and checks equality with the original P.
For the unreduced rational global defects e,f,g, it checks the entire identities H23=-72t^(3d)e(t+t^(-1)), H25=-800t^(5d)f(t+t^(-1)) and H35=-30375t^(15d/2)g(t+t^(-1)).
It also reconstructs every coefficient of AU from e and g and checks the V centering shift and cleared scalar denominator.
These are circle-polynomial identities before reduction modulo T, so the check does not confuse original trace values with global circle functions.
The exact independent gcd(e,g) has degree zero on both inputs, justifying the author's strict-positive U integrand.

The author freshly checks reciprocal monic constant-one original inputs, irreducibility and noncyclotomic status, exact trace degree d/2 and the full count of simple real trace roots.
Prior R374 eligibility applies to these unchanged inputs; its generated calculations are not read as new arithmetic inputs.
The general C156 arithmetic norm theorem is reused from its actual independently reviewed acceptance.
This finite screen neither recomputes weighted original norms nor supplies a new arithmetic proof.

### Enclosing logarithms and complete Jensen accounting

For U the author integrates log(e^2+g^2) at theta=pi*u over u in[0,1], which equals the normalized circle integral by the real trace expression's evenness and periodicity.
The value of pi is enclosed, and the integrator's analytic flag is passed to the complex logarithm so branch and zero checks occur on integration boxes.
The returned complex ball is finite with imaginary part containing zero; its real part supplies the enclosing integral.
The positivity proof comes from the exact gcd, not from sampled positive values.

For V the author uses the exact centered trace-f polynomial and complete-root Jensen instead of applying strictly positive quadrature to a function with possible zeros.
The independent checker uses complete-root Jensen for both AU and H25.
Exact squarefree factors multiply back to the full integer polynomial, every returned isolated set has the factor's entire degree, and the root balls within each factor are pairwise disjoint.
All multiplicities contribute to the degree and to the Jensen sum.
The leading coefficient is included once for the complete polynomial.
Each log(max(1,abs(root))) uses an enclosing interval maximum, including root balls that meet the unit circle.

In the completed independent output, AU is squarefree of degree120 for the quartic input and degree300 for Lehmer.
Its isolated roots split respectively60/60 and150/150 inside/outside the unit circle, with no unresolved circle overlap.
H25 is squarefree of degrees40 and100.
Its root balls split18/18/4 and44/44/12 into inside/outside/unit-circle-overlapping classes.
These overlap counts are properties of the enclosures, not independently asserted exact circle-root counts, and no classification guess is needed for the logarithmic certification.

Both methods compare all six scalar quantities JU,JV,JU+JV,log2,the lower envelope and its excess over log2.
The checker parses the actual persisted balls, checks their finiteness and radii, verifies strict signs and enclosure overlap, and bounds every author decimal's error using its own independent enclosure.
The author requires persisted scalar radius below1e-12; the checker's radius threshold is below1e-10, with an additional strict absolute-error check below1e-10 for every displayed decimal.
Agreement alone is not the certificate: each algorithm's enclosing arithmetic and exact Jensen/integral reduction supply its own bound.

### Bounded execution, corrections and limits

The author succeeded at256 bits on both inputs.
The independent quartic calculation succeeded at256 bits.
The independent Lehmer root isolation did not converge at256 bits and succeeded at512 bits under the one predeclared escalation; the exact squarefree checks and polynomial scope were unchanged.
The failed attempt and final precision are retained in the completed verification payload.
The root-isolation maxprec never exceeds the current256/512-bit attempt, and each program has an actual300-second subprocess cap.
No tolerance scan, higher precision, new input, q-grid, regularization or replacement auxiliary was introduced.
An initial short reviewer message incorrectly described both independent calculations as256-bit successes; inspection of the retained attempt records corrected that description before this fixed finding and the final README.

The first independent arithmetic run preceded inspection of the new author code and numerical values.
The second run incorporated exact object and scalar comparison checks and completed successfully under the same declared bounds.
The complete README, including its final precision/radius corrections, was inspected before recording this review.
Its reproduction order correctly requires author output only for the subsequent comparison, while neither mathematical generator consumes older J97/J98 generated results.
Generated output is reproducible local evidence in the declared ignored output home and is not automatically transferred by a Git clone.

The shared FLINT exact algebra and Arb/Acb algorithms remain trusted computational primitives.
The two methods are not independently implemented numerical libraries, and this is not formal verification.
R376 owns the whole C156 proof review; this finding checks only its actual finite-use interface and the new component calculations.
It does not re-audit the full C149/C153/C155 dependency chains or the historical proof of scalar Jensen.
The result does not resolve small-positive-measure inputs, general reciprocal coverage, a uniform original-root/Haar transfer estimate, or the unrestricted G0001 contract.
The arithmetic-income theorem remains valid while this particular weighted family lacks a Haar-side margin on the two declared controls.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
