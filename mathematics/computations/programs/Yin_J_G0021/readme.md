---
author: Yin
---
# Independent exact replay of quartic return-core certificates

## Native input availability

The checker reads [J18's original tracked triangles](../Yin_J_G0018/inputs/triangles.json), [J19's compact list](../Yin_J_G0019/inputs/compact.json) and [J19's original path list](../Yin_J_G0019/inputs/paths.json).
The current full replay passed all fifty cells and 150 words, the complete 22275-tuple enumeration with 841 expanding-strip tuples and 259 candidate states, and all 259 continuations of maximum length 25.
replay_authors.py also passed from those tracked inputs and checks their actual finite assertions without requiring old ignored verification reports.
These current executions do not change the original full-chain/SELF review scopes or supply a new independent-agent review.

## Scope

Separately organized review computation for the fixed quartic return-core argument originally developed in the now-retired D G0013 and D G0014, retained in [L G0169](../../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-theorem).
The reviewer contributed none of those proofs or discovery programs.
Shared progress and prior review accounts were read before this review; it is not blind.
This computation independently reconstructs interval enclosures, the full coefficient box enumeration and integer polynomial continuation checks.
It does not assert an unrestricted Lehmer gap.

The full reasoning and actual review relationship are recorded in [fixed complete review](../../../audits/reviews/Yin_R_G0068_v1.md#quartic-full-chain-review).
The current complete mathematical home is [C396](../../../claims/Yin_C_G0396_v1.md#quartic-infinite-core-theorem).
This directory owns the continuing review programs and their executed evidence.

Generated results and verification data use `mathematics/computations/outputs/Yin_J_G0021/`, independently of the caller's directory.
All indispensable data are read directly from their responsible tracked input homes named above.
Only newly generated review reports use ignored outputs.

## Files and execution

- [review.py](review.py) imports no author interval, enumeration or discovery code.
  It isolates beta by exact sign bisection, constructs independently coded outward integer intervals, checks every saved triangle and word, bounds the inverse embedding matrix by interval Gaussian elimination, exhaustively checks the whole coefficient box, and verifies continuations by integer polynomial long division.
- verification.json (`mathematics/computations/outputs/Yin_J_G0021/verification.json`) records that independent implementation's result.
- [replay_authors.py](replay_authors.py) reruns the three exact author programs, intercepting only output writes and preserving them here.
  It compares the regenerated compact input with the complete tracked compact list and checks the original declared finite triangle and path assertions.
- author_replay.json (`mathematics/computations/outputs/Yin_J_G0021/author_replay.json`) records those comparisons.
  The redirected outputs are J18 verification (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0018_verification.json`), J19 compact enumeration (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0019_compact.json`) and J19 path verification (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0019_verification.json`).

From the repository root, using only the standard library:

```powershell
python -B mathematics/computations/programs/Yin_J_G0021/review.py
python -B mathematics/computations/programs/Yin_J_G0021/replay_authors.py
```

All checks passed.
The independent enclosure scale is 10^25; all 50 cells and 150 words pass with maximum word length nine and minimum margin at least 1114267/1000000.
The independently derived coefficient bounds are (5,7,7,4).
Testing all 22,275 tuples retains 841 expanding-strip tuples and exactly the same 259 candidate states as the author's enumeration.
All 259 whole-word polynomial identities vanish modulo P; the longest path is 25 digits.
The historical author replays reproduced the then-retained outputs.
The current repaired replay instead checks the tracked inputs and their complete stated finite scope, without an ignored-output baseline dependency.

## Boundaries

The independent implementation uses the same mathematical certificate and reads the saved author digit lists.
Its independence is in arithmetic, inverse computation, exhaustive rather than sliced enumeration, and endpoint verification; it is not independent discovery of the witnesses.
Soundness of interval enclosures and completeness of the finite domain are explained in the retained full review from D G0016.
Script success alone is not offered as that explanation.
Discovery floats, optimization and the source's earlier different-quartic table are not proof premises.
Neither numerical discovery script was rerun.
The review programs themselves are reviewer evidence and are not formally verified libraries.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
