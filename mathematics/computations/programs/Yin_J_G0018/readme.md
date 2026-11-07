---
author: Yin
---
# Quartic Salem neutral-block search and exact certificates

## Native input availability

[inputs/triangles.json](inputs/triangles.json) retains all fifty original cell indices and their 150 selected integer words.
The minimal payload was extracted from the author's retained original triangles, without rerunning floating hull selection or retaining its numerical diagnostics.
The exact author verifier and J21's distinct complete checker now read this one native input.
Both current replays passed all fifty full closed cells and 150 words, with maximum length nine and the original drop bounds 557/500 and 1114267/1000000 at their respective arithmetic scales.

## Question and scope

Search and verify a finite family of original {-1,0,1}-digit blocks that makes neutral descent possible while returning to an expanding strip.
This is a geometric mechanism test, not a full weighted return estimate.

## Files

- [probe.py](probe.py): floating-point discovery enumerates ternary words of length at most ten, then uses planar convex hulls to choose a triangle over each of fifty cells.
- [inputs/triangles.json](inputs/triangles.json): the adopted integer digit words and rational cell indices, without discovery diagnostics.
- [verify.py](verify.py): separate standard-library Fraction interval verifier.
  It imports no discovery code and uses no floating-point arithmetic.
- verification.json (`mathematics/computations/outputs/Yin_J_G0018/verification.json`): the actually rerun exact result.

The responsible argument and exact domain are [fixed quartic descent](../../../claims/Yin_C_G0396_v1.md#quartic-neutral-descent).

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0018/`, independently of the caller's directory.
Required verification inputs are tracked in this group's inputs/ and reused there by J21.
Optional discovery writes a new triangles.json to the ignored output home; it does not replace the adopted native selection.

## Reproduction

From repository root:

Discovery requires the stated NumPy and SciPy dependencies; the shared baseline dependency file does not include SciPy.
Use a compatible existing environment with normal package resolution.
The exact verification command retains its separately stated standard-library dependencies.

```powershell
python -B mathematics/computations/programs/Yin_J_G0018/probe.py --max-length 10
python -B mathematics/computations/programs/Yin_J_G0018/verify.py
```

Discovery uses NumPy and SciPy.
The exact verifier needs only the standard library and the actual retained certificate.

## Results and limits

Discovery found a three-word certificate on every cell [j/100,(j+1)/100], j=50,...,99, for the expanding root of t^4-t^3-t^2-t+1.
The longest selected word has nine digits.
Numerical diagnostics suggested neutral radius ten suffices; the separate exact check proves it, with a uniform squared-neutral-magnitude drop at least 557/500.

All 150 block images lie strictly in (-1,1) across their complete closed cells.
Exact triangle orientation and edge-distance checks prove the neutral descent.
Fraction square-root intervals use integer square roots at scale 10^35.
The verifier recomputes the constants instead of accepting saved decimals.

The table covers positive expanding magnitude in [1/2,1].
Negating the state and all digits covers the negative cells.
Finite zero prefixes cover the remaining nonzero |x_+|<1/2; an actual algebraic state with x_+=0 is zero.
The contracting strip |x_-|<=beta/(beta-1) is invariant digit by digit.
The narrow expanding strip holds at block endpoints, and the whole path remains in the larger |x_+|<1/(beta-1) strip.

The table itself certifies geometric descent.
Complete compact termination and reciprocal reachability are now proved in the [fixed combined result](../../../claims/Yin_C_G0396_v1.md#quartic-infinite-core-theorem), using J G0019 as well as this certificate.
A full original-law return-tail estimate remains open.
The coordinating reviewer read the entire interval verifier and separately reproduced all 150 checks and the exact constant.
This is separate execution and mathematical code inspection of the author's verification implementation, not a third implementation or a discovery rerun.
The [fixed retention](../../../ledger/Yin_L_G0169_v1.md#quartic-preserved-local-reviews) preserves that complete local written review and the subsequent radius-dependent timing corollary with its contribution/review boundary.
The [whole-chain SELF review](../../../audits/reviews/Yin_R_G0068_v1.md#quartic-full-chain-review) and J G0021 supply the later complete inspection.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
