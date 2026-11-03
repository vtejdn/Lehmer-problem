---
author: Yin
---

# Bounded primitive-trinomial doubling auxiliary pilot

## Scope and execution limit

The responsible [C412 complete argument](../../../claims/Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) owns the exact two-variable algebra and interpretation.
This pilot considers exactly 0<b<a<=12 with gcd(a,b)=1, with a 120-second execution cap.
It factors the normalized reciprocal residual over the integers, separates cyclotomic factors exactly, and uses exact trace-root counts where factors are reciprocal.
Approximate Mahler measures and phase balances are discovery values only until separately certified.

## Evidence

- [pilot.py](pilot.py) and pilot.json (`mathematics/computations/outputs/Yin_J_G0036/pilot.json`): Python with SymPy and NumPy; all 45 rows completed.
  Factorization/cyclotomic decisions and rational Sturm counts are exact.
  NumPy complex roots supply discovery-only Mahler estimates.
  No interval precision, certified sign/ranking, or general phase bound is inferred from them.
- [certify_structure.py](certify_structure.py) and structural-certificate.json (`mathematics/computations/outputs/Yin_J_G0036/structural-certificate.json`): exact two-variable identity, swap identity, all 45 stored polynomial reconstructions, seed-Phi_6 congruences, simple noncyclotomic counts, exact cyclotomic order identification, and an explicit rational/mod-two certificate for the (3,2) residual.
  All assertions passed.
  This second program uses the retained pilot rows but independently checks the key cubic trace certificate without factor_list(W); it is an author verification, not an independent review.

Actual finite result: two Salem rows, both the original Lehmer residual after removing the cyclotomic seed factor; 42 reciprocal multiple-expanding residuals; one nonmonic exception.
Every row has one simple noncyclotomic factor.
The retained exact cyclotomic orders are 6, 12 and 15.
All this is bounded to the stated 45 pairs.

Two author harness errors were corrected before the retained checks: structural equality was replaced by an expanded zero-difference test, and the degree-eight cyclotomic label was corrected from 30 to 15 after exact polynomial comparison.
Neither failed attempt supplied adopted mathematical output.
These corrections and their actual inspection are recorded in the [independent review](../../../audits/reviews/Yin_R_G0074_v1.md#trinomial-auxiliary-independent-review).

No unrestricted auxiliary-factor coverage, arbitrary Salem construction, or general graph realization is assumed.
D41 supplies the exact block-bipartite graph obstruction and all interpretation boundaries.

## Separate reviewer check

The assigned orbit_research reviewer authored [review_exact.py](review_exact.py) and retained its result in review-exact.json (`mathematics/computations/outputs/Yin_J_G0036/review-exact.json`).
For complete regeneration, run the author pilot and certificate check before the reviewer check from the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0036/pilot.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0036/certify_structure.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0036/review_exact.py
```

The reviewer checker can run directly when the author inputs are already available.

The reviewer check uses Python with SymPy and passed.
It verifies the exact complete set of45 pairs, direct polynomial/factor reconstructions and irreducibility, monicity exception, cyclotomic identities and rational isolating intervals for every noncyclotomic trace factor.
The intervals independently recover all stored root counts and the2/42/1 classification without treating the author's count_roots results or type labels as an oracle.
Both Salem residuals equal the original Lehmer polynomial exactly.
The output retains every review interval.

This separately authored checker shares SymPy's exact arithmetic/irreducibility library; it is not an independently implemented algebra system.
It does not rerun the author pilot, enlarge the parameter range, recompute Mahler decimals or certify any general positive phase-balance assertion.
The full written noncontributor review and exact mathematical limits are recorded in [L175 preserved argument](../../../audits/reviews/Yin_R_G0074_v1.md#trinomial-auxiliary-independent-review).

The complete D41 mathematics resides in [C412](../../../claims/Yin_C_G0412_v1.md#sparse-trinomial-auxiliary).
Its original fixed author account and exact historical whole-review inputs remain in [L175](../../../ledger/Yin_L_G0175_v1.md#sparse-trinomial-auxiliary), with actual review relationships declared in R.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
