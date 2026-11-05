---
author: Yin
---
# Exact degree-sixteen Salem half-product certificate

## Question and scope

Test the specified degree-sixteen polynomial from the coordinator's inspection of retained Dub02, printed p.202/PDF p.7, against the full 32-sign half-product polynomial of the actual degree-ten Lehmer source.
The canonical [Dub02 source record](../../../audits/literature/Dub02/Yin_U001.md#dub02-u001) owns that inspection and its limits.
The native test uses exact integer polynomial arithmetic, five-dimensional multiplication determinants and Newton identities for n=1,...,32.
No numerical roots or numerical factorization are used.

## Files

[inputs.json](inputs.json) retains the ascending coefficients of the original trace polynomial and the supplied q16, the exact range and source locator.
[certificate.py](certificate.py) is the complete standard-library generator and finite identity checker.
The actually generated full result is [certificate.json](../../outputs/Yin_J_G0135/certificate.json).
Its selected native payload is also retained as [inputs/positive_case.json](inputs/positive_case.json) for the failed positive-sign test.
It includes all 32 Chebyshev remainders, power sums, Q32, P16, quotient, remainder and check results.

## Reproduction

Run from the repository root with `python -X utf8 mathematics/computations/programs/Yin_J_G0135/certificate.py`.
The program resolves its exact input and output paths from its own J directory and requires only the Python standard library.
The actual run used CPython 3.13.15.
It computes Res(F,C_n) as the determinant of multiplication by C_n in Z[y]/(F), using exact Bareiss divisions, and then constructs Q32 by exact Newton identities.
It forms P16 from the even and odd parts of q16 and performs monic integer polynomial division.
Rerunning may replace the generated output; the selected positive-case payload remains a retained input.

## Actual result and limits

The positive-sign certificate was executed and failed: P16(Y) does not divide Q32(Y).
The remainder has degree 15 and leading coefficient -5096; its entire integer coefficient list is preserved in the native result.
The exact q(z)q(-z)=P16(z^2) identity, degree and monicity checks, all asserted Bareiss/Newton integral divisions, and quotient/remainder reconstruction passed.
The two specified elementary integer inequalities for the proposed root-size bound also passed, but they do not establish the missing measure identity for q16.
No irreducibility, actual two-circle placement, M(q16)=tau^4 or lower-measure counterexample has been certified by this failed divisibility test.
Failure of this proposed positive-sign certificate is not a finding that the published source's mathematical assertion is false.
The proposed negative-sign check P16(Y) dividing Q32(-Y) was not executed, and no phase-check program or result is claimed.
No additional powers or other torsion cases were tested.
The algebraic implications and current author-working limitation are retained in [D1](../../../drafts/Yin_D_G0001.md#dub02-degree16-positive-certificate-test).
This computation has no independent mathematical review or adopted Claim.
