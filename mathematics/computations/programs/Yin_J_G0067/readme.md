---
author: Yin
---
# Changed scalar target and charged stabilization tests

## Question and scope

Before execution at 2026-10-10T04:09, [D150 Section3](../../../ledger/Yin_L_G0283_v1.md#four-by-four-paid-test-declaration) declared ALL integral4-by4 matrices B with squared-entry sum8, modulo independent row/column signs normalized along a deterministic spanning forest.
The full target for V=[[I4,-B],[0,I4]] is Phi2^2 Phi6 P4, equivalently chi_(B^T B)=s(s^3-8s^2+18s-9).
The declared domain was all12870 eight-unit supports and all21840 one-double/four-unit weighted supports, with EVERY cycle-edge sign, plus the120 two-double supports explicitly rejected by rank.
These are all square partitions of8.
No permutation quotient or arbitrary entry box is used.
All successful matrices and complete absolute-factor distribution were to be retained, including an empty result.
Explicit B5/B7 controls require their full original/absolute/proper-cover costs.
The aggregate author runtime cap was120 seconds; no further search was included.

The complete declared domain contains no target.
The [complete current proof](../../../claims/Yin_C_G0520_v2.md#minimum-bipartite-padding-cost) combines this certificate with an all-row-count analytic three-column classification.
It proves minimum rank8 within the rectangular bipartite class for Phi2^k Phi6 P4 and the unique more expensive companion at that minimum.
Non-bipartite rank7 realization remains outside this conclusion.

## Files

- [main.py](main.py) is the author program, using standard-library exact integer arithmetic.
  It normalizes signs along a deterministic spanning forest, enumerates all remaining sign choices, computes entire Gram characteristic polynomials by principal minors, and builds both proper integer controls and their literal covers.
  It imports no older project code or third-party package.
- result.json (`mathematics/computations/outputs/Yin_J_G0067/result.json`) is the completed native output: all support/sign-stage counts, complete cycle-sign histogram, empty target and companion-distribution lists, and actual matrices, Gram matrices, every full polynomial and all ranks/heights/energies for B5/B7.

The separate checker below is a noncontributor implementation.

## Reproduction

From the repository root, using Python:

```powershell
.\.venv\Scripts\python.exe mathematics/computations/programs/Yin_J_G0067/main.py
```

The program writes its completed output in this J output home, independently of the working directory.
No old output, draft file, material hash, network, random seed or optional dependency is needed.
Each candidate and equality is integer exact.
A cap exception does not publish a completed replacement output.
All mathematical inputs and the120-second cap are explicit in the program and the prior declaration.

## Results and limits

The eight-unit class has12870 supports and35256 normalized sign representatives, of which4752 have e2=18.
The one-double/four-unit class has21840 supports and24000 sign representatives, of which576 have e2=18.
None matches the COMPLETE required Gram polynomial.
The free-cycle count histogram, counting normalized representatives, is19680 at0,21168 at1,17160 at2 and1248 at3, summing59256.
All120 two-double supports are impossible by rank at most2, regardless of sign.
This certificate covers every integer4-by4 B compatible with the coefficient-forced energy8; it is not all-bases or all non-bipartite coverage.

The actual B5 control has proper rank8, full original Phi2^2 F and absolute Phi2^2 H, with F=Phi6 P4 and H=t^6-2t^5-3t^4-5t^3-3t^2-2t+1.
Its proper rank16 cover is the full product Phi2^4 F H.
The B7 control has proper rank10, both factors Phi2^4 F and proper rank20 cover Phi2^8 F^2.
Heights are1; original and companion strict-upper energy is8 and cover energy16 for both.
Complete coefficient arrays and every actual standard-lattice matrix are saved, not just these factorizations.

The program checks the actual original, absolute and proper-cover pencils at degree-plus-one distinct integers.
The two triples of counts are9/9/17 and11/11/21, totaling78 exact Bareiss determinant evaluations.
Together with the local sheet-decomposition proof these verify the entire polynomials, not a numerical spectral sample.
In D150 the trace cubic proves m(H)=log alpha with alpha>2>beta4, so rank8 full cost exceeds2log beta4; B7 has exactly that doubled cost.
Rank9's other partition is not tested and no general optimality conclusion follows.
The old L191 rank6 Phi2^2 P4 remains a smaller-target cheaper control.

## Inspection summary

Orbit_research AI for Yin authored the proof and this single finite implementation.
The root coordinator supplied only the broad task and allocation.
The three-column classification, all-integer coefficient reduction and all-parameter support constructor are written proofs; the4-by4 exhaustive test is an exact finite certificate under the documented reduction.
The actual complete noncontributor review is recorded below.
No new source theorem or source acquisition was used; the block, sign and cover interfaces reuse the explicitly cited L191/L234/D9 inputs.
No author computation failed or reached its cap.

## Complete independent inspection

The coordinating AI for Yin completed the entire frozen D150 Sections1--6/(1)--(14) review at 2026-10-10T04:26; see the [complete finding](../../../audits/reviews/Yin_R_G0136_v1.md#paid-stabilization-complete-independent-review).
It passed without author correction.
The separate [review_independent.py](review_independent.py) and review_result.json (`mathematics/computations/outputs/Yin_J_G0067/review_result.json`) use only row-first-sign normalization, squared B minors and complete inverse/Newton coefficient arrays, importing no author program or third-party package.
The entire same finite domain and both full controls passed.
Larger reviewer counts are due to the weaker sign quotient:237216 eight-unit and60480 one-double representatives, with zero complete targets.
All actual control matrices, full original/absolute/cover coefficients and costs match.
The written review separately verifies finite coverage, the full integral classification, all parameter-family costs and every scope limitation; this does not replace a whole mathematical review with one rerun.
The completed fixed retention is L283.

## Fixed retention

The complete current mathematical home is [C520v2](../../../claims/Yin_C_G0520_v2.md#statement), with its [actual maintaining whole SELF](../../../audits/reviews/Yin_R_G0728_v1.md#current-paid-stabilization-whole-self-finding).
This current organization runs no program and preserves the original pre-execution protocol, native bytes and 2026-10-10T04:26 independent review above.
[L283](../../../ledger/Yin_L_G0283_v1.md#complete-retained-proof-and-review) retains the full author proof and separate review.
G0001 remains unresolved.

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
| `result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0136_v1.md#paid-stabilization-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0728_v1.md#current-paid-stabilization-whole-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0520_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0520_v2.md) |
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0136_v1.md#paid-stabilization-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0728_v1.md#current-paid-stabilization-whole-self-finding); [Claim support and recorded result](../../../claims/Yin_C_G0520_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0520_v2.md) |
