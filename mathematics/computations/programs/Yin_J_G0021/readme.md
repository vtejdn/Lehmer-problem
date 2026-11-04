---
author: Yin
---
# Independent exact replay of quartic return-core certificates

## Native input availability

The exact259-state enumeration input is now reused from [J19's tracked compact list](../Yin_J_G0019/inputs/compact.json), and this program's enumeration_check has matched that entire set by its distinct exact construction.
The [selected J18 triangle payload](../Yin_J_G0018/readme.md#native-input-availability) and [selected J19 path payload](../Yin_J_G0019/readme.md#native-input-availability) remain unavailable.
Those two concrete inputs prevent the complete current replay; the old full-chain and SELF review scopes are not converted into a new execution or a different relationship.

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
The adopted compact list is read directly from J19's tracked inputs/compact.json; the missing triangle and path selections retain their historical output locators until those native payloads are supplied.
These retained outputs are local and Git-ignored; a clone can lack them.
Verification reports unavailable inputs without automatically rerunning discovery or substituting other results.

## Files and execution

- [review.py](review.py) imports no author interval, enumeration or discovery code.
  It isolates beta by exact sign bisection, constructs independently coded outward integer intervals, checks every saved triangle and word, bounds the inverse embedding matrix by interval Gaussian elimination, exhaustively checks the whole coefficient box, and verifies continuations by integer polynomial long division.
- verification.json (`mathematics/computations/outputs/Yin_J_G0021/verification.json`) records that independent implementation's result.
- [replay_authors.py](replay_authors.py) reruns the three exact author programs, intercepting only output writes and preserving them here.
  It checks that regenerated mathematical outputs equal the retained originals, on their complete mathematical payloads.
- author_replay.json (`mathematics/computations/outputs/Yin_J_G0021/author_replay.json`) records those comparisons.
  The redirected outputs are J18 verification (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0018_verification.json`), J19 compact enumeration (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0019_compact.json`) and J19 path verification (`mathematics/computations/outputs/Yin_J_G0021/Yin_J_G0019_verification.json`).

From the repository root, using only the standard library:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0021/review.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0021/replay_authors.py
```

All checks passed.
The independent enclosure scale is 10^25; all 50 cells and 150 words pass with maximum word length nine and minimum margin at least 1114267/1000000.
The independently derived coefficient bounds are (5,7,7,4).
Testing all 22,275 tuples retains 841 expanding-strip tuples and exactly the same 259 candidate states as the author's enumeration.
All 259 whole-word polynomial identities vanish modulo P; the longest path is 25 digits.
Author replays reproduce the retained outputs.

## Boundaries

The independent implementation uses the same mathematical certificate and reads the saved author digit lists.
Its independence is in arithmetic, inverse computation, exhaustive rather than sliced enumeration, and endpoint verification; it is not independent discovery of the witnesses.
Soundness of interval enclosures and completeness of the finite domain are explained in the retained full review from D G0016.
Script success alone is not offered as that explanation.
Discovery floats, optimization and the source's earlier different-quartic table are not proof premises.
Neither numerical discovery script was rerun.
The review programs themselves are reviewer evidence and are not formally verified libraries.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
