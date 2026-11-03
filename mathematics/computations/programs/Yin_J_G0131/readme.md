---
author: Yin
---

# Exact finite H-character classifications at normalized multiplicities24 and28

## Question and scope

This is one predeclared finite computation under the active [G0001 Task](../../../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Use [C655](../../../claims/Yin_C_G0655_v1.md#statement) T1,T3,T5 and the exact [C652 triangular character proof](../../../claims/Yin_C_G0652_v1.md#argument).
The TWO candidate sets are EVERY H in F_2[t] with H(0)=1 and degree at most5 (32 polynomials) for m=12,Q=32, and degree at most7 (128 polynomials) for m=14,Q=32.
No complete-factor hypothesis is imposed on the candidates.
These sets are nested; the program will compute the128 unique polynomial rows once and report the two exact case filters separately.
Both m are nondyadic, so epsilon=0 by the actual original layer rule, not by a freely chosen parity.
N=4m is48 or56 and the strict-next-power K_N is64 in both cases.
Multiplying C655 T5 by25 gives respectively10ell(H)=4 or26 modulo32, hence ell(H)=10 or9 modulo16 because5 inverse modulo16 is13.
The m=14,Q=64 branch is not a new scan: its degree bound is at most1 and its character condition is again9 modulo16, already refuted by the two known values ell(1)=0 and ell(1+t)=1.
No other m, Q, degree or character modulus is searched, and no cutoff is enlarged after seeing results.

All arithmetic is exact in F_2[t] or Z/16Z, with no random seed, floating-point tolerance or probabilistic sampling.
The explicit mathematical jet precision is modulo t^16.
C652 proves that this determines ell modulo16.
At each order j=1,...,15, eliminate a nonzero coefficient with1+t^j if j is a power of2, or with Theta(1+t^e) otherwise, where j=2^v*u, u odd>=3, e=2^v(u-2).
The latter generator has exact leading order j by C652 P2, and Theta(h)=h^5/h(chi), chi=t+t^3+t^5.
The selected power-of-two coefficients give the character a in{0,...,15}.
For every row retain the reconstructible certificate H=Theta(G)(1+t)^a modulo t^16, which a separate author verification program will check without rerunning the elimination algorithm.

Before publication require the following exact bounded controls: every leading-order generator for1<=j<=15; all B_n calibrations for odd1<=n<=63 against(1-chi4(n)n)/4 modulo16; and Theta(1+t^e) having character0 for1<=e<=15.
These are calibration controls, not additional candidate ranges or finite-group sufficiency assumptions.

For EVERY passing H, factor it completely in F_2[t], verify reconstruction and irreducibility, determine the primitive trace order of each irreducible factor, and test whether each order group is a full W_n at uniform multiplicity.
Here formal H completeness permits W_5 as well as other odd orders: C655 T1 does not forbid it, and C652's small-degree H list explicitly contains W_5.
A factor f of degree d<=7 has nonzero trace x in F_(2^d); the two roots of z^2+xz+1 are interchanged or fixed by the2^d Frobenius.
Their odd order therefore divides2^d+1 or2^d-1, so it is at most129.
This proves the finite order bound used by the factor check, rather than imposing a heuristic support cutoff.
Whole W_n are reconstructed exactly from B_n by proper-divisor division, and completeness is polynomial equality of each order group with a power of its full W_n.

## Files

- [inputs.json](inputs.json) owns the exact finite scope, candidate counts, character targets, precision and calibration lists.
- [main.py](main.py) generates every exact character reconstruction certificate and the complete passing-candidate factor data using integer bit-polynomial arithmetic.
- [verify.py](verify.py) uses separately written coefficient-set arithmetic to verify all128 candidate certificates, all bounded calibrations and every passing factor/order/whole-group assertion; it does not import main.py or rerun its elimination algorithm.
- Generated classification.json (`mathematics/computations/outputs/Yin_J_G0131/classification.json`) and verification.json (`mathematics/computations/outputs/Yin_J_G0131/verification.json`) are present after successful complete generation and author verification.
- [reviewer_check.py](reviewer_check.py) is the independent reviewer's bounded dense-coefficient verifier, with inverse-free character recomputation, quadratic-algebra orders and cyclotomic Laurent reconstruction of whole trace polynomials.
- Generated independent_verification.json (`mathematics/computations/outputs/Yin_J_G0131/independent_verification.json`) retains that separate reproduction's complete128-character list, passing factor/order/whole data and exact scope.

## Reproduction

From the repository root, run in this order:

    python mathematics/computations/programs/Yin_J_G0131/main.py
    python mathematics/computations/programs/Yin_J_G0131/verify.py

Use Python3 standard-library exact integer and polynomial operations only.
Generation requires the retained inputs.json and no previous output.
Verification-only requires the generated classification.json and the same native scope input; it does not regenerate a missing classification.
Both defaults resolve inputs and the output home mathematics/computations/outputs/Yin_J_G0131 from the containing J and repository, independent of the caller's working directory.
These two generated files are reproducible and may be atomically overwritten by the same commands; no fixed mathematical or review input is overwritten.
Generation must complete all finite rows, factor checks and controls before publishing its output.
Verification must inspect every candidate certificate, complete case coverage, factorization, exact order, completeness statement and calibration certificate before publishing its own result.
Any failure stops the run and is reported; it does not authorize a larger range or changed character condition.

## Results and limits

Status: complete exact generation and complete author verification succeeded at the predeclared scope.
All128 distinct constant-one polynomials have retained Theta reconstruction certificates, with32 eligible rows for m12 and128 for m14.
The m12,Q32 filter has exactly ONE passing mask37, namely1+t^2+t^5; it is an irreducible order31 trace factor and is not a whole W31.
The m14,Q32 filter has exactly EIGHT passing masks59,67,91,99,131,155,163,251.
Among these, only mask163=1+t+t^5+t^7=(1+t)(1+t^5+t^6)=W3 W21 is a complete product of odd-order W_n.
Every passing row's full factorization, trace order and exact whole-group comparison is retained in the classification output.
The separate coefficient-set verification checked all128 candidate reconstruction identities, all9 passing factor/order/completeness assertions,32 B_n calibration certificates,15 Theta controls and15 leading generators.
This verifies the mathematical payload, not a saved fingerprint or generator-reported zero exit code.
Original_law is the author of both programs, the reduction and these checks; separately written arithmetic is not independent mathematical review.
The result classifies only the specified formal H polynomials and necessary character.
Passing this filter will not supply the actual same-T canonical data, original q/layers, full gate, complete Y target, original P/T or characteristic-zero realization.
The complete classification and analytical reduction are fixed in [C670](../../../claims/Yin_C_G0670_v1.md#statement), with its [initial open decision](../../../claims/Yin_C_G0670_v1.md#decision-finite-h-classification-open) retained.
C670 was subsequently [adopted at its whole-reviewed decision](../../../claims/Yin_C_G0670_v1.md#decision-whole-reviewed-2026-10-24) through the complete independent finding below; the initial open decision remains historical.

Neither incomplete H nor incomplete Y is excluded by the original H domain; no passing candidate is removed because its separate factorization is not whole.

## Independent reviewer reproduction

The isolated reviewer declared the same finite128/nested32 candidate scope,32 B controls,15 Theta controls,15 leading generators, factor degree at most7 and proved order ceiling129 before execution.
The new verifier imports neither author program and uses dense coefficient tuples with exact Python3.13.15 standard-library arithmetic.
It recomputes every character by multiplying leading generators while maintaining a numerator/denominator pair, then directly checks every author certificate by cross multiplication modulo t^16.
It independently factors the passing polynomials with Frobenius/gcd irreducibility checks, computes exact orders by multiplication in the quadratic algebra z^2+xz+1, and recovers whole W_n from cyclotomic Laurent identities.
It also checks the full input scope, every case filter, all source witnesses and the author verification's declared counts and relationship.

From the repository root, after the author outputs above are available, run:

    python mathematics/computations/programs/Yin_J_G0131/reviewer_check.py

The executed check returned verified for all128 rows,9 passing factor/order/whole checks,32 B controls,15 Theta controls and15 leading generators.
Its passing lists are exactly mask37 and masks59,67,91,99,131,155,163,251; only163 is a complete product among those rows.
It reads inputs.json, classification.json and verification.json without changing them and atomically writes only independent_verification.json in this J's output home.
No candidate degree, character modulus or order bound was enlarged.
The complete mathematical and native review, its input bindings and realization limits are retained in [R891](../../../audits/reviews/Yin_R_G0891_v1.md#finite-h-classification-whole-independent-finding).

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
| `classification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0891_v1.md#finite-h-classification-whole-independent-finding) |
| `independent_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0891_v1.md#finite-h-classification-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0891_v1.md#finite-h-classification-whole-independent-finding) |
