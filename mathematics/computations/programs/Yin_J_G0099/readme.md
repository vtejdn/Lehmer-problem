---
author: Yin
---
# Two-input balanced H25 component-log screen

Context: [S1 staged test](../../../strategies/Yin_S_G0001.md#b3-two-round-assessment-2026-10-18) under the [active resumption](../../../tasks/Yin_T_G0001_v1.md#decision-resume-balanced-weight-2026-10-18).
The [C156 gate](../../../claims/Yin_C_G0156_v1.md#decision-whole-reviewed-2026-10-18) was independently accepted through [R376](../../../audits/reviews/Yin_R_G0376_v1.md#balanced-weight-whole-independent-finding) before either numerical program ran.

## Question and scope

For exactly P=t^4-t^3-t^2-t+1 and P=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, certify the Stage1 component logarithms for

    U=|H23/72|^2+|H35/30375|^2,
    V=|H25/800|^2,
    B_bal,q=q U+q^(-1)V.

Here Hj are the original C149 polynomial numerators, not residues modulo the original P.
The original ascending coefficient lists are the quartic_Salem_seed and Lehmer_degree10 entries of [J97 input](../Yin_J_G0097/input.json).
Both programs explicitly select and check those two lists; the other two retained J97 entries are not new test inputs.
The [earlier J98 diagnostic](../Yin_J_G0098/readme.md#certified-results) supplies the existing q=1 baseline and is not recalculated here.
No earlier generated output is an arithmetic input.

C156 proves I_bal(q)>=log2+(J_U+J_V)/2 for every real q>0 on each fixed P, where J_U and J_V are normalized Haar logarithmic integrals.
Its separate arithmetic theorem applies to integer q>=1 on the actual totally-real trace domain and retains the changed value H_q/q and full q^d denominator.
A nonnegative certified component sum excludes the whole positive-q circle family on that input.
The declared q in{2,4,8,16,32,64} grid is conditional on surviving this screen.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Author trace reconstruction, direct analytic U integral, exact centered trace-f polynomial and complete-root Jensen evaluation of V. |
| [verify.py](verify.py) | Separate original-numerator construction and complete Jensen evaluation of both components, followed by exact object and scalar-payload comparisons. |
| [Original input](../Yin_J_G0097/input.json) | Explicit cross-J native input; exactly two named entries are selected and checked. |
| Author output (`mathematics/computations/outputs/Yin_J_G0099/results.json`) | Locally generated exact trace objects, root evidence, ball enclosures, rounded values and screen decisions. |
| Verification output (`mathematics/computations/outputs/Yin_J_G0099/verification.json`) | Locally generated original integer numerators, complete squarefree factors/root balls, independent enclosures and comparison results. |

Generated evidence uses the Git-ignored output home mathematics/computations/outputs/Yin_J_G0099/ and is reproducible from the native programs and explicit original input.
It is not automatically delivered by a Git commit or clone.

## Reproduction

From the repository root, using the local environment with SymPy1.14.0 and python-flint0.9.0:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0099/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0099/verify.py
```

Run the author command first so the checker can compare its independent mathematical reconstruction to the completed author payload.
Neither arithmetic generator consumes J97/J98 generated output.
Each batch has a300-second subprocess cap and uses256-bit ball arithmetic, with at most one escalation to512 bits for unresolved numerical enclosures.
Root isolation maxprec follows that same ceiling; no higher-precision retry or parameter expansion is allowed.
The author requires a persisted enclosing ball with radius below1e-12; both programs certify rounded-decimal absolute error below1e-10 and retain their actual enclosing balls.
Incomplete or failed results remain explicit partial output, never a completed replacement.
The final outputs may be overwritten by a valid reproduction of the same scope; required native inputs and programs must remain.

The author constructs the exact trace polynomial T and unreduced rational circle defects e,f,g from T(C_p)/p.
For both actual inputs gcd(e,g)=1, so U=e^2+g^2 is strictly positive on the real trace line.
The U integral uses theta=pi*u on[0,1], enclosing pi, analytic-flag forwarding to the complex logarithm, tolerance goals1e-18, evaluation limit200000 and depth limit30.
Actual finite ball radii, rather than the requested tolerance alone, certify the result.
For V the exact centered polynomial t^n f(t+t^(-1)), n=5d, is cleared of its scalar denominator and evaluated by Jensen with complete squarefree multiplicities.
It equals -H25/800 after centering, an identity checked independently.
This handles possible circle zeros without strict-positive quadrature or numerical regularization.

The separate checker constructs H23,H25,H35 directly from integer P(t^2),P(t^3),P(t^5), uses A_U=A23+A35 and H25, and certifies

    J_U=m(A_U)-2log972000,
    J_V=2m(H25)-2log800.

All factors multiply back, isolated-root counts include their full multiplicities, and each contribution log(max(1,|beta|)) uses an enclosing interval maximum even if a root ball meets the unit circle.
The author and checker share FLINT Arb/Acb primitives; independence concerns code, exact constructions and the U numerical method, not independent numerical libraries or formal verification.

<a id="certified-results"></a>
## Certified results and limits

The author completed both inputs at256 bits without escalation.
The independent quartic calculation completed at256 bits; the Lehmer root isolation returned insufficient precision at256 bits and succeeded at512 bits under the one allowed escalation.
That failed initial root-isolation attempt is retained in the verification output and did not change the input, tolerance, mathematical object or allowed precision ceiling.
Every displayed value below has certified absolute error below1e-10, including the derived lower envelope and its excess over log2.
The reference log2 is0.693147180560 at that same error bound.

| Original input | J_U | J_V | J_U+J_V | Lower envelope for every q>0 | Lower envelope minus log2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| quartic_Salem_seed | 0.878992188265 | 2.363883636679 | 3.242875824944 | 2.314585093032 | 1.621437912472 |
| Lehmer_degree10 | 2.263253531462 | 1.991241720952 | 4.254495252414 | 2.820394806767 | 2.127247626207 |

The signs are certified from enclosing intervals, not rounded decimals.
Thus every positive real q fails the target I_bal(q)<log2 on each of these two original inputs.
In particular no allowed grid value can achieve the operational margin1/16, so Stage2 is skipped under the declared stopping rule.
Exactly four distinct component integrals were evaluated; zero weighted-grid candidates or corresponding new original norms were computed.
The lower envelope is a proved lower bound and is not claimed to be an attained minimum over constant q.

The new full arithmetic-income theorem survives, but this entire one-parameter weighted family has no Haar-side margin on these controls.
This is stronger than failure of six sampled q values and weaker than an obstruction for every original P or every positive quadratic form.
The result neither refutes C155/C156 nor solves general reciprocal coverage, the small-positive-measure regime, original-root/Haar transfer, or the unrestricted G0001 objective.

The completed [R377 finite independent finding](../../../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding) covers the entire author program, separate checker, persisted mathematical payload, this account and the exact two-input all-positive-q consequence.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) |
