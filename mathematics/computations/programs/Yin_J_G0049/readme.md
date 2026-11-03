---
author: Yin
---

# Integral root-basis realization checks

The complete current D93 mathematical argument is [C549](../../../claims/Yin_C_G0549_v1.md#rank-seven-realization-argument), with its [actual isolated whole review](../../../audits/reviews/Yin_R_G0776_v1.md#current-integral-rank-and-companion) and adopted scope.
The original frozen [L226](../../../ledger/Yin_L_G0226_v1.md#complete-retained-proof-and-review) remains the actual input of the dated R125 finding.
The [original complete noncontributor finding](../../../audits/reviews/Yin_R_G0776_v1.md#integral-realization-complete-independent-review) records the actual full replays and separate integer verification.

## Results and reproduction

The complete current [integer rank7 certificate](../../../claims/Yin_C_G0549_v1.md#explicit-integral-rank-seven-realization) is adopted in C549 after its isolated whole review at the unchanged exact scope.
It has exactly p_V=Phi2 P6, height4 and energy87, with an explicit unimodular integer root basis in the even lattice [2]+U+U+U.
The [full companion and cover](../../../claims/Yin_C_G0549_v1.md#rank-seven-realization-full-absolute-cost) are Phi2 R and Phi2^2 P6 R, with R=t^6-601t^5-84t^4+987t^3-84t^2-601t+1.
The cover has rank14, height4 and energy174.
The extra Salem root is between600 and602, so the realization improves the known neutral padding, not the current absolute-cover measure.
The original R125 complete noncontributor finding is retained at its current R home with its actual arrangement and input; C549 owns the current mathematical scope.

The checks passed; the exact certificate uses Python with SymPy.
Each command writes its named output under `mathematics/computations/outputs/Yin_J_G0049/`.
From the repository root:

```powershell
& .venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0049/search.py
& .venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0049/search_mixed.py
& .venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0049/verify.py
```

`search.py` and `search_result.json` preserve the first experiment: seed20261010,100 restarts with2000 proposals each, Gram height at most6, energy at most180, basis coordinates at most10000.
It uses partial root reflections and swaps.
All200000 proposals completed;66046 failed the Gram bounds,133954 were evaluated,34559 nonterminal moves were accepted, and no target was found among5317 distinct polynomials.
The best score8 candidate has energy47 and height3.
D93 subsequently proves a complete modulo4 obstruction for its entire matching-parity orbit, independent of every numerical cap.
The program/output remain the original finite experiment, not a retrospective exhaustive search claim.

`search_mixed.py` imports the exact basic routines from search.py without calling its main function or changing its output.
It starts from the explicitly changed integer root basis and uses seed20261011, the same upper caps and exact norm-preserving two-root proposals.
It stopped early at proposal14260 with one target, after7294 norm rejections,1935 Gram rejections,5031 evaluations and564 accepted nonterminal moves;2171 distinct polynomials were seen.
`mixed_result.json` retains the actual complete integer basis, Gram matrix and coefficients.
Both searches use floating annealing only to choose proposals.
Candidate arithmetic, lattice basis updates, integer bounds and polynomial coefficient computations are exact.

`verify.py` does not import or invoke the search coefficient routine.
It checks both saved candidates' actual integer bases and determinant, their complete Gram identities and all diagonal norms.
It calculates full polynomial determinants directly, including the successful original and absolute matrices, checks the companion trace cubic and every exact root/irreducibility claim, and constructs the entire signed cover.
Its full14-by-14 determinant is computed directly and also compared with the two sheet restrictions.
The written Newton traces, endpoint determinant, exact cubic signs and irreducibility modulo5 are checked.
The changed seed's parity graph is checked connected.
`verification.json` retains all these checks and every full polynomial.
The retained verifier includes the written trace, sign and modulo5 certificate.

## Scope, proof and provenance

D93 supplies the proofs of the general root-basis construction, both kinds of norm-preserving move, the all-parameter parity-component determinant congruence, the full first-orbit obstruction, the explicit rank7 realization and its minimum possible rank for P6, and the entire absolute-cover cost.
The first search is evidence of discovery only.
Existence is supported by the displayed finite integer certificate and its full polynomial proof; it does not depend on the annealing path, random-seed portability or a claim of exhaustive coverage.
The lower-rank exclusion uses the retained Pfaffian endpoint square, not a failed search.
The high-energy representative is not asserted optimal.

The assigned orbit_research AI authored all three implementations and the new arguments.
The coordinator supplied the broad task and allocation only.
The direct-determinant program is a second author verification route, not a noncontributor review.
The first experiment's program and output retain their distinct finite scope; source and proof review limits remain those recorded in D93.

## Original complete inspection and replay

The coordinating noncontributor AI fully inspected the author proof, all three programs and all three saved outputs, then independently replayed both searches and verify.py without writing files.
Output writes were intercepted in memory.
Each regenerated mathematical search payload agreed with its saved counterpart.
The verifier comparison omitted no fields.
This is complete replay of the author implementations, not independent authorship of those programs.

A separate one-off plain-integer implementation, using the matrices written in the proof rather than importing the author programs, also verified the full original and absolute polynomials by5040-term permutation expansions, det Q=-1 and every Gram-identity entry, energy87, and the full14-degree cover identity through exact integer determinants at15 distinct arguments.
The complete mathematical inspection, source-dependency boundary and explicit scope are recorded in [L226's full noncontributor review](../../../audits/reviews/Yin_R_G0776_v1.md#integral-realization-complete-independent-review).
No defect or author repair was found.

The earlier construction check is explicitly SELF in [R738](../../../audits/reviews/Yin_R_G0738_v1.md#current-g226-g230-postmaintenance-whole-self-finding).
It does not convert the original missing relationship declaration into known independence or replace the native replay and different integer implementation actually recorded in R125.
