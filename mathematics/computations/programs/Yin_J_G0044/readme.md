---
author: Yin
---
# Actual quartic lifts of a finite Fourier stationarity relaxation

## Question and fixed input

The complete current mathematical proof is [C501](../../../claims/Yin_C_G0501_v1.md#quartic-finite-character-certificate), whose 2026-10-22T04:51 decision selected [the new whole independent finding](../../../audits/reviews/Yin_R_G0726_v1.md#current-stationary-fourier-whole-independent-finding).
The earlier R857 whole SELF at 09:56 and C501 adoption at 09:57 retain their actual separate chronology.
The [original L208 fixed input](../../../ledger/Yin_L_G0208_v1.md#quartic-finite-character-certificate) and original review/program reading history remain unchanged.
It constructs sixteen actual order states representing O/2O in a strict real safe box, retains all original successors, and checks exact quotient stationarity with a separately visible failure of actual measure stationarity.
The input is P=t^4-t^3-t^2-t+1, its expanding Salem root beta, and O=Z[beta].
Its irreducibility and narrow co-return premise are the fixed [complete C396 input](../../../claims/Yin_C_G0396_v1.md#quartic-infinite-core-theorem); the complete strict-strip description follows from [C400](../../../claims/Yin_C_G0400_v1.md#exact-salem-return-strip).

The original digits have probabilities1/4,1/2,1/4 at-1,0,1.
No changed probabilities, actual stationary law, exhaustive core enumeration or general Mahler gap is asserted.

## Native files and reproduction

- [verify.py](verify.py) uses only integer and Fraction arithmetic for rational root isolation, bounded representative construction, exact real enclosures, integer transition arithmetic, all finite character equations and total variation.
- verification.json (`mathematics/computations/outputs/Yin_J_G0044/verification.json`) retains every representative and successor, rational coordinate intervals, all sixteen character values and the executed construction counts.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0044/verify.py
```

The current certificate checker uses Python and passed.
It writes its output only after every assertion passes.
Its bounded construction varies a_2,a_3 by shells up to an explicit cap200 and tests nine nearby rational nearest-integer candidates for the other coefficients.
It completed at shell20 after15129 candidate visits.
No floating-point discovery filter or unchecked decimal inequality is used.
The stated count is the executed visit count, not an assertion of minimality or general complexity.

## Exact result

There is one representative of each of the16 parity classes with both real coordinates in(-1/8,1/8).
Every one of its48 original successors lies strictly in the actual core's two real strips.
The uniform initial measure has weight1/16 per representative.
At common denominator64, each original row contributes successor weights1,2,1.
Before and after the step, each parity class has total numerator4.

The complete sixteen-character check gives numerator64 for the trivial character and0 for all other parity characters for both laws.
Thus every function of the finite quotient has equal expectations before and after.
The actual measures on O are nevertheless different: their exact total variation is15/16, and the successor measure has48 distinct states.

## Proof and review boundary

D74 proves the all-q actual-coset density, full finite-character algebra obstruction, safe finite-horizon condition, necessary neutral escape and a genuine expanding-character detector.
Those general statements are not computational extrapolations from this example.
The program verifies one concrete finite lift and its exact failure of full stationarity.

The program and D74 are author work; the complete separate review is linked below.
The coordinating agent supplied the route question and allocation coordination, not this derivation or program.

## Author correction of character-value types

The original separately organized reviewer found that the original expression `(-1)**dot_product` returned floating-point signs for negative integer dot products:29 of the32 saved before/after character numerators had floating type, all equal to0.0.
Those signs and sums were exactly representable at the executed sizes, so no mathematical value was wrong; the original blanket integer/Fraction-only description was inaccurate for that execution.

The exact original bytes are retained as [historical_author_verify.py](historical_author_verify.py) and historical_author_verification.json (`mathematics/computations/outputs/Yin_J_G0044/historical_author_verification.json`).
These are historical evidence, not the current reproduction target; the historical program retains its original output filename.

The current expression uses integer parity branching, returning1 for an even dot product and-1 otherwise.
The repaired complete check passed with all32 character numerators of integer type.
The previous and new parsed certificates agree in every mathematical value, including all representatives, rational enclosures,48 successors, character numerators,15129 candidate visits and total variation15/16.
The [original R726 whole and correction account](../../../audits/reviews/Yin_R_G0726_v1.md#original-stationary-fourier-review-account) preserves its actual 04:08 inspection of the one-expression repair and both certificate versions; the mathematical proof was unchanged.
The original independent declaration remains a historical claim; the original whole, initial type finding and final type closure retain UNKNOWN initial arrangements, and the [complete original author checks](../../../audits/reviews/Yin_R_G0726_v1.md#stationary-fourier-original-author-check-finding) remain SELF at their original day precision.


## Original complete review and fixed inputs

The [complete original R726 noncontributor account](../../../audits/reviews/Yin_R_G0726_v1.md#original-stationary-fourier-review-account) preserves its full written proof, initial and repaired programs and evidence, and all dependency/source limits.
The independently implemented [review_certificate.py](review_certificate.py) uses radical root bounds, termwise intervals and companion arithmetic, without importing author code or repeating its search.
The initial reviewer result (`mathematics/computations/outputs/Yin_J_G0044/review_before_integer_repair.json`) preserves the successful mathematical check with the initial type flag; the final reviewer result (`mathematics/computations/outputs/Yin_J_G0044/review_result.json`) checks the repaired certificate with integer types.
Both verify16 actual representatives,48 successors,128 real bounds,all16 characters and exact total variation15/16.

The reviewer program reads the [retained L208 proof](../../../ledger/Yin_L_G0208_v1.md#stationary-fourier-fixed-scope), still labelled D74 in historical output.
Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0044/review_certificate.py` from the repository root after the current author certificate is available.
Its replay after that argument-path update matched the final reviewer result; that earlier maintenance check did not enlarge the original review or establish its missing initial arrangement.
Earlier retention maintenance read the full author/historical/reviewer code and four native accounts without executing a producer, checker or search.
The later R726 whole review records one authorized existing-checker replay at the same quartic/q2 domain in 0.0093739 seconds: all twelve saved report fields matched, no actual file mutation occurred and all nine fixed-file guards agreed.
That event ran no author producer or representative search and supplied no newly implemented checker.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
