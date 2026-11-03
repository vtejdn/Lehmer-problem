---
author: Yin
---
# Alternating-kernel obstruction to integral cyclotomic cancellation

This group supplies the original finite controls for the [complete C521 common-stabilizer theorem](../../../claims/Yin_C_G0521_v1.md#stable-cancellation-fixed-scope); its original D81 input remains fixed in [L214](../../../ledger/Yin_L_G0214_v1.md#stable-cancellation-fixed-scope).
It retains a bounded exact verification of the actual eight-dimensional P6 realization, its full primitive integer alternating kernel, the restricted form and its nonsingular quotient modulo5.
The written all-common-stabilizer proof is separate from these finite controls; no matrix search or rank-seven realization is asserted.
The current C521 adoption uses [R730 complete whole SELF](../../../audits/reviews/Yin_R_G0730_v1.md#current-integral-cancellation-whole-self-finding), with no new program run.
The [original complete R110 whole](../../../audits/reviews/Yin_R_G0110_v1.md#independent-review-stable-cancellation) retains its 2026-10-09T20:48 written-proof inspection and actual read-only replay; its initial extra mathematical context/order is unestablished, so its relationship is UNKNOWN.

## Program and reproduction

Run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0046/verify.py` from the repository root.
The checker uses Python with SymPy and passed.
Its verification.json (`mathematics/computations/outputs/Yin_J_G0046/verification.json`) records only exact integers, polynomial coefficients expressed symbolically, residue-field data and explicit scope statements.
No floating eigenvalue or numerical factorization is used.

The checker rebuilds the actual rank-eight V from the literal five-by-three B, computes its complete determinant and the leading coefficient at minus one, and verifies the displayed kernel equations.
A unit-determinant minor proves rank B=3; the parameterization and coordinate projection establish that the two integral vectors generate the entire kernel, not just a finite-index sublattice.
They are extended to a full basis of determinant1.
In this basis the six-dimensional alternating quotient has determinant1, and the restricted symmetric Gram matrix is exactly[[3,1],[1,2]].
A displayed invertible basis change modulo5 reduces that Gram matrix to diag(3,0).

The program's model diag(5,1) is only the necessary kernel form of a hypothetical rank-seven Z plus[1], as proved by the [complete leading-coefficient argument](../../../claims/Yin_C_G0521_v1.md#minus-one-leading-coefficient-kernel).
It is not an exhibited Z or a computation of an unknown realization.
The resulting one-dimensional quotient has square discriminant, while the actual V8 quotient has nonsquare discriminant.

Five finite stabilizer controls use no block, the unit path of size2, size5, size9, and the direct sum of sizes5 and9.
Their full determinant polynomials are retained and equal the geometric sums1+t+...+t^n, or their stated product.
Thus they are genuinely neutral.
Size2 has no alternating kernel; size5 has restricted norm3, a nonsquare modulo5; size9 has restricted norm5, so its nonzero integral kernel becomes entirely radical modulo5; their direct sum has both a radical and a nonzero quotient.
Every control preserves the predicted opposite square classes on the two proposed stabilized sides.
This demonstrates the implemented degenerate cases, while the all-W conclusion comes from the [complete quotient/direct-sum proof](../../../claims/Yin_C_G0521_v1.md#kernel-mod-prime-stable-obstruction), not from five samples.

The residue-field routine uses exact symmetric elimination and explicitly handles the case where all diagonal entries vanish but an off-diagonal entry is nonzero.
A three-dimensional hyperbolic-plus-radical form checks that branch.
It only inverts a nonzero field element and returns determinant class1 for the zero-dimensional quotient.
The separately retained original and cover polynomials, energies7 and14, and hypothetical norm5 agree with the written full-cost account.
The cover polynomial is checked through the already proved full factorization; the program does not claim a new direct determinant of a16-dimensional cover.

## Scope and review boundary

The original V8, J45 evidence and its completed review remain at their own responsible home.
This program does not rerun J45 or enlarge its capped search.
The general splitting criterion, coefficient/Pfaffian identity, basis independence, all-common-W obstruction and arbitrary-input prime condition are proved in the [complete current argument](../../../claims/Yin_C_G0521_v1.md#argument).
No symbolic sample substitutes for those proofs, and no absolute Mahler bound for an unknown Z is inferred from a kernel invariant.

## Original complete review and read-only replay

The coordinating noncontributor reviewer checked the full D81 proof and every line of this program, then reran verify.py with its sole JSON write intercepted.
The complete parsed output matched verification.json.
All five neutral controls and exact symbolic assertions passed.
This reviewer replay is distinct from the author run and does not convert the finite controls into an all-W proof.
The complete original mathematical review remains at [R110 with its actual fixed D81/L214 input](../../../audits/reviews/Yin_R_G0110_v1.md#independent-review-stable-cancellation).
The [complete original author checking](../../../audits/reviews/Yin_R_G0730_v1.md#original-integral-cancellation-author-whole-self-finding) is separately SELF; the original author run, later reviewer replay and present constructor whole SELF remain distinct, with all original finite scope and dates preserved.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
