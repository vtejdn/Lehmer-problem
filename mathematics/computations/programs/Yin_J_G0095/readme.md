---
author: Yin
---
# Complete squarefree divisor-ideal half-moment optimization

## Question and declared mathematical scope

The `g_bridge_audit` author calculation implements the bounded scope in [fixed C111](../../../claims/Yin_C_G0111_v1.md#finite-ideal-native-predeclaration).
Fix N=2*3*5*7*11=2310, s=1/2, t=3/2 and precision 96 bits.
Enumerate all ideals of the 32-label Boolean divisor lattice, including empty for completeness and excluding it from the quotient.
Every full-totient energy uses its exact 32-entry ordered lcm-coefficient vector.
A unique maximum requires strict rational interval separation; retain possible ties/nonseparation otherwise.
Independently generate all 32 numeric-threshold ideals.

For each removed prime, optimize over the four-prime squarefree subambient.
Within the same complete enumeration, classify nested nonempty slice pairs at theta=9/10,99/100 and mass-ratio caps 1/4,1/2.
Retain every possible member, ambiguity and correlation upper bound, and the full maximizer's five slice records.
The recurrence/bijection, interval directions, classification and limitations are proved in C111 before execution.
This is a finite structural discriminator, not a universal weak constant, other-ambient classification, density/noncapture, polynomial-realization or Mahler-gap result.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Author nested-pair enumeration and exact rational certificate. |
| [verify.py](verify.py) | Separately implemented predecessor enumeration and exact reconstruction. |
| certificate.json (`mathematics/computations/outputs/Yin_J_G0095/certificate.json`) | Every author candidate, kernel, threshold, base, classification and required cross record. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0095/verification.json`) | Complete independent candidates, correlations, maxima, classifications and coarse bounds. |

Generated evidence is retained locally at `mathematics/computations/outputs/Yin_J_G0095/`, outside Git.
Completed finite results need no continuing checkpoint.

## Reproduction

From the repository root, with the Python standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0095/main.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0095/verify.py
```

The author command generates the fixed-scope certificate; verification requires that actual certificate and never imports or calls the author program.
Both commands resolve the J output home independently of the caller's directory.
Live 180-second subprocess limits and direct failure reporting remain.
Complete results publish atomically after mathematical success.
Verification compares complete mathematical payloads; it requires no historical execution file, stdout copy, invocation counter or empty-stderr assertion.
A fresh clone may lack the certificate; missing evidence is reported without automatic calculation or a success claim.
Reproduction instructions neither resume a Task nor authorize a larger scope.

## Results and limits

### Current state

The completed author enumeration has counts 2,3,6,20,168,7581 for zero through five primes.
All 7,580 nonempty candidates and 8,636 required correlations remain in the certificate.
The unique full and numeric-threshold optimizer is the proper-divisor ideal of 2310, mask 2147483647 and mass 1830.
Strict separation is certified rationally, not by decimal ordering.
Every 99%-of-base-optimum box at either mass cap is empty.
For removed primes 2,3,5,7,11, the 90% member counts at caps 1/4 and 1/2 are respectively (1485,2502), (1259,1974), (730,1218), (651,1198), (703,1739).
All classifications have zero interval ambiguity; full member keys and exact bounds remain retained.

## Independent verification declaration

The separately assigned `strategy_critique` reviewer did not contribute to the author program or analytic proof.
Author inputs and the finite scope were fixed before the reviewer wrote and ran the verifier; shared context and saved results made this non-blind.
R347 now declares the actual whole/native finding self-reviewed for the supplied target-author explanations and discloses the reviewer's necessary pre-fixed nonempty-domain repair.
The separately implemented algorithm and complete outputs remain as recorded; they do not establish context isolation.
The verifier enumerates topologically using immediate predecessors rather than nested pairs.
It computes ordered gcd/lcm coefficients rather than bitwise maximum/symmetric accumulation, and uses bisection of sqrt(1/d) and sqrt(W^3) rather than reciprocal isqrt and W*sqrt(W).
Original endpoints are checked through exact integer square inequalities.
Every candidate, all 32 thresholds, all five bases, 20 tests, required correlations and optimizer slices are checked and retained.

### Actual independent execution and result

On 2026-10-15 the declared native reproduction completed at exactly this scope.
All 7,580 original nonempty candidates, 8,636 correlations and classifications passed both interval constructions with zero ambiguities.
Independent bounds give 1342/1000<C*<1343/1000 and strict separation>1/250.
All 99% boxes are empty; every 90% possible member satisfies rho<15/16 at cap 1/4 and rho<49/50 at cap 1/2.
The output retains every independent row and required correlation, not only a winning mask or agreement flag.
The original headings retain their historical designation; the current R347 whole/native relationship is self-reviewed and the repaired analytic guard still requires independent re-review at the stated affected scope.
The execution date, fixed parameters, distinct algorithms and complete mathematical outputs are unchanged, with no new run or review performed here.
This historical review relationship does not claim a new review of storage maintenance.

The [R347 whole finding](../../../audits/reviews/Yin_R_G0347_v1.md#finite-discriminator-actual-whole-independent-finding) separately reviews fixed C111, including analytic extensions and the disclosed pre-fixed nonempty-ambient guard correction.
Its non-blind arrangement and actual contribution boundaries remain in that review; C111's decision controls adoption.
Native success alone supplies no universal bound, untested ambient result or actual polynomial realization.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0347_v1.md#finite-discriminator-actual-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0521_v1.md#c111-current-independent-whole-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0347_v1.md#finite-discriminator-actual-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0521_v1.md#c111-current-independent-whole-finding) |
