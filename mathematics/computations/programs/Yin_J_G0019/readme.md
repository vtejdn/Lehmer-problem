---
author: Yin
---
# Compact quartic enumeration and continuation certificates

## Native input availability

The complete 259-state compact input is retained at [inputs/compact.json](inputs/compact.json), and the original 259 state/word continuations are retained at [inputs/paths.json](inputs/paths.json).
The compact set was deterministically reconstructed and matched against J21's distinct exact enumeration of all 22275 coefficient tuples, 841 expanding-strip tuples and 259 retained states.
The path payload was extracted from the author's retained original calculation; the current radius-twelve discovery independently produced the same complete integer witness list, but the retained input is the original selected payload.
verify_paths.py and J21 now check the single tracked state/word list, with complete coverage and maximum length 25.
The floating search-region pruning is used only by discovery, not by either exact verifier.

## Question and scope

Enumerate a certified finite superset of the compact residual K from [fixed quartic descent](../../../claims/Yin_C_G0396_v1.md#quartic-neutral-descent), then check actual finite paths to zero.
The responsible new argument is [fixed compact argument](../../../claims/Yin_C_G0396_v1.md#quartic-compact-termination).

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0019/`, independently of the caller's directory.
The adopted compact list and original path list are read from this group's tracked inputs/.
Optional enumeration and discovery still write replaceable outputs; neither automatically replaces an adopted input.

## Files and reproduction

- [enumerate.py](enumerate.py) uses the reviewed J G0018 Fraction root intervals, exact adjugate/determinant inverse bounds, and outward integer-scaled embedding intervals.
- [inputs/compact.json](inputs/compact.json) retains the certified coefficient bounds and all 259 candidates, a finite superset of K.
- [paths.py](paths.py) discovers backward paths with floating-point search-region pruning; its selected region is not a proof premise.
- [inputs/paths.json](inputs/paths.json) retains all integer start states and original-digit continuations.
- [verify_paths.py](verify_paths.py) checks complete candidate coverage and every forward integer recurrence, importing no discovery helper or approximate embedding code.
- verification.json (`mathematics/computations/outputs/Yin_J_G0019/verification.json`) records the successful exact path check.

From the repository root:

```powershell
python -B mathematics/computations/programs/Yin_J_G0019/enumerate.py
python -B mathematics/computations/programs/Yin_J_G0019/paths.py --radius 12
python -B mathematics/computations/programs/Yin_J_G0019/verify_paths.py
```

All three programs use only the standard library.
Enumeration and verification require no floating-point package.

## Results and limits

The exact inverse bounds are (5,7,7,4).
The complete expanding-coordinate slicing examined 841 tuples and retained 259 candidates.
Candidates ambiguous at a tested boundary are retained, so this is a complete superset rather than a numerical assertion of exact membership.

The radius-twelve reverse search visited 433 states and found a continuation for every candidate before its node cap.
The longest retained path has 25 digits.
All 259 forward paths verified exactly, with complete candidate coverage.
No discovery-bound optimality, exhaustive full graph or minimal path-length conclusion is asserted.

The [fixed combined proof](../../../claims/Yin_C_G0396_v1.md#quartic-infinite-core-theorem) supplies the complete enumeration logic, the co-return consequence, and the separate reciprocity/pigeonhole argument for an infinite actual core at this fixed quartic input.
Those mathematical deductions are not proved merely by the discovery log.
Its [whole-chain SELF review](../../../audits/reviews/Yin_R_G0068_v1.md#quartic-full-chain-review) and [corrected consolidation review](../../../audits/reviews/Yin_R_G0068_v1.md#quartic-consolidation-review) are complete, with independently implemented verification in J G0021.
No unrestricted Lehmer-gap conclusion is asserted.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
