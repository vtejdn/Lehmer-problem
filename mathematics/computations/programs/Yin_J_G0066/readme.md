---
author: Yin
---
# Small-total-measure auxiliary certificate

## Question and scope

[Complete C515](../../../claims/Yin_C_G0515_v1.md#argument) owns the entire current argument; the author program has a120-second live cap.
The exact inputs are the quartic t^4-t^3-t^2-t+1, sextic t^6-t^5-t^3-t+1 and original degree-ten Lehmer polynomial.
Compute their exact integral-Chebyshev-coordinate trace norm forms and spherical moments k=1,2 only.
The deterministic directional test uses the s coordinate vectors, all-one and alternating-sign vectors, each with exactly16 gradient steps; each next vector is rounded to the fixed coordinate grid of maximum magnitude1024, then divided by its gcd.
Retain every step.
This is not a global optimization certificate.
For the best declared witness on each input, verify the full original resultant, content, degree and trace roots.
No extra input, expanded coefficient box or higher moment is part of this declaration.

## Files

- [derive.py](derive.py): complete author implementation; integral trace reconstruction, symbolic resultant norm form, exact sparse moments, predetermined gradient directions and full witness checks.
- derivation.json (`mathematics/computations/outputs/Yin_J_G0066/derivation.json`): final native output, including every state, exact rational moments, root intervals and complete costs.

No reviewer program is imported by the author code.
Reviewer-owned files, if subsequently added, are separate evidence.

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0066/derive.py
```

The author program writes derivation.json in this J output home.
The separate reviewer consumes the completed mathematical output.

## Results and limits

The final certificate distinguishes degree_energy_mean from rho_l1_over_l2_squared=S1^2/E after a reviewer notation reminder.
That correction changed no norm, energy, direction path or moment.
Exact rational strict-advantage and root-cost assertions are included at the original finite scope.

The actual polynomials and their trace forms, both k=1,2 moments, all68+85+119 states and exact witnesses are retained.
Floats explicitly labelled discovery are not rigorous intervals.
The final strict inequalities use integer/Fraction arithmetic against exact rational isolating endpoints.
The sextic has exp(d(B-m))>21/20; the original Lehmer input has exp(d(B-m))>7/5.
The quartic k=1 whole-class moment bound is225/32 for exp(4B), strictly below its beta^4.
No directional-search global optimum is claimed.

All chosen witnesses are primitive and have actual degree equal to the original degree.
Sextic and quartic auxiliary Mahler measures equal512 from complete trace-root counts and leading coefficients.
The Lehmer auxiliary has leading magnitude384 and one exterior reciprocal pair, giving1152<M(C)<1248.
Exact S1^2/E values and distinct degree-energy means are retained.
Local valuation distribution is not inferred from total resultant divisibility.

The full theoretical hierarchy and its uniform-accuracy/detection interpretation are proved in [C515](../../../claims/Yin_C_G0515_v1.md#trace-norm-moment-hierarchy).
These are three fixed small-positive-measure controls; no m-to-zero family, uniform coverage, whole-gap proof or centered-window origin is asserted.

## Complete review and fixed adoption

The entire current proof and exact controls are retained in [C515](../../../claims/Yin_C_G0515_v1.md#statement), with the actual current [whole SELF finding](../../../audits/reviews/Yin_R_G0725_v1.md#current-complete-trace-moment-self-finding).
The original [finding](../../../audits/reviews/Yin_R_G0133_v1.md#trace-moment-complete-independent-review) retains its complete old formula/native/source/cost coverage and UNKNOWN relationship.
The reviewer discloses an extra task summary, direct developing-proof reading and the rho-label reminder, with no mathematical derivation supplied.
The extra summary content and initial mathematical order are unestablished; no shared substantive development or isolated context is invented.

The independently authored [review_independent.py](review_independent.py) and native review_result.json (`mathematics/computations/outputs/Yin_J_G0066/review_result.json`) are distinct from the author implementation.
The independent implementation completed the entire declared domain.
It imports neither the author code nor SymPy.
It reconstructs norm forms through integer companion/multiplication matrices and Leibniz determinants, differentiates by determinant columns, computes exact Gaussian/radial moments, and uses independent rational Sturm counts and modular trace irreducibility.
It checked all3,9,125 nonzero norm-form terms, all six k=1,2 moments, all272 deterministic states and chosen witnesses, complete original resultants, exact surplus inequalities, every stored rational root interval and the full leading/root/content/coherence costs.
Floating discovery fields were compared only as display checks; mathematical inequalities used integers or Fraction.

DGT20 attribution and the near-one, height and complexity limits belong to the responsible proof.
The checker uses native mathematical data and needs no retired draft.

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
| `derivation.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0133_v1.md#trace-moment-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0725_v1.md#current-complete-trace-moment-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0515_v1.md) |
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0133_v1.md#trace-moment-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0725_v1.md#current-complete-trace-moment-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0515_v1.md) |
