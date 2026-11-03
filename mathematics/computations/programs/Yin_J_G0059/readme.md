---
author: Yin
---
# Three-column and exterior-square realization tests

## Question and scope

The responsible complete proof is [C456](../../../claims/Yin_C_G0456_v1.md#argument), with the actual [whole SELF finding](../../../audits/reviews/Yin_R_G0662_v1.md#exterior-sextic-whole-self-finding).
The completed author calculations distinguish genuine three-column changes of the conference path basis from a new exterior-square bilinear constructor.
Neither completed finite test achieved an upper-unitriangular target.
The latter constructor nevertheless realizes every reciprocal sextic with the stated two endpoint conditions as an explicit integral determinant-one bilinear form.
It retains zero diagonal, so it is a relaxed realization, not a solution of the stronger basis problem.
The original declarations, meaningful unsuccessful exploration and contribution/checking history remain fixed in [L262](../../../ledger/Yin_L_G0262_v1.md#exterior-square-sextic-fixed-scope).

## Files

- [search.py](search.py) and search_result.json (`mathematics/computations/outputs/Yin_J_G0059/search_result.json`): all729 root vectors,114 norm-two roots,57 sign representatives,20 position triples and all3703860 ordered replacement triples.
  All per-position counts, energy/Pfaffian/residue histograms and complete target lists are retained.
- [exterior.py](exterior.py) and exterior_result.json (`mathematics/computations/outputs/Yin_J_G0059/exterior_result.json`): the actual F=Phi6 P4 exterior-square matrices, integral bilinear form, and bounded positive-unit-pivot tree, including actual call counts, largest intermediate entry86 and the first20 dead forms with paths.
- [costs.py](costs.py) and costs_result.json (`mathematics/computations/outputs/Yin_J_G0059/costs_result.json`): all-parameter integer matrix/characteristic identities, complete full-entry absolute factor and two actual controls, including their full degree12 lift polynomials, determinant signs, ranks, entry heights and squared-entry sums.

The separately implemented checker below is distinct from the three author programs; algorithmic separation does not establish the review relationship.

## Reproduction

From the repository root, using Python with SymPy:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0059/search.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0059/exterior.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0059/costs.py
```

All three commands were actually run on2026-10-10.
They write their semantic result in this J output home; no draft or saved output is a mathematical input.
There is no randomness or floating arithmetic in the mathematical decisions.
search.py uses ordinary integer minors/Pfaffians/triangular inversion.
exterior.py uses exact SymPy identities followed by integer recursive congruences.
costs.py uses symbolic polynomial identities and26 scalar integer determinants of the literal rank12 lifts.
The last program was rerun at the same two-control scope after adding the general symbolic absolute factor, with the earlier control values unchanged.

The complete root/triple domain and120-second cap were declared before search.py ran.
The changed exterior test was declared separately before execution: all sign-normalized norm-one vectors in the current cube{-1,0,1}^n, specified coordinate completion and left-orthogonal clearing, lexicographic order after support size, exact-form memoization,20000 recursive calls and120 seconds.
These are finite algorithmic scopes, not all integer bases.

## Results and limits

The complete three-column counts are1759698 singular minors,1034514 nonzero nonunit minors,909648 unit minors, then63116 discarded old controls and846532 genuine replacements.
Both complete target lists are empty.
The even-first-coefficient residue test had no escape, but this observation is not an all-three-column congruence theorem.
The energy histogram ranges from17 to90 and sums to846532; all six coefficient-residue counts appear in the native output and responsible proof.
Discarded controls are not included in this new negative conclusion.

The separate exterior pivot tree completed6670 calls.
It merged4500 repeated forms and found300 new forms without a permitted small norm-one pivot; no full triangular basis was reached.
No runtime/node cap was hit.
This does not exclude larger integer pivots, a different completion or another bilinear realization.

The all-parameter constructor has det V=1, V+V^T equal to the explicit even unimodular hyperbolic pairing, and the full prescribed sextic.
The full-entry absolute matrix B=-|V| and the explicitly defined double-sheet lift have determinants-1; this is a separately proved nontriangular construction with zero diagonals, not an application of an upper-unitriangular theorem beyond its hypotheses.
Both actual controls have complete relaxed cover measure greater than twice their original measure.
The achieved proper L191 comparison remains better; no scalar factor is silently deleted.

Author self-check inspected the complete count partitions, endpoint reductions, sign normalization, exterior conventions, actual integer bases, pivot completeness and limits, full symbolic absolute factor, all control ranks/factors and exact root intervals.
No failed or capped mathematical run occurred.
No new source theorem was introduced; prior HPM22 attribution covers only the reused conference seed.
The actual separate review is described below.

## Inspection summary

At 2026-10-10T01:35, the separately assigned structural_research reviewer completed the whole author proof and native computation review, with no defect or correction.
The exact scope and disclosed upstream roles are retained in [L262's complete finding](../../../audits/reviews/Yin_R_G0121_v1.md#three-column-exterior-complete-independent-review).
Its current explicit whole relationship is UNKNOWN because the exact initial proof-relevant progress context and ordering are not established; prior D9 authorship and upstream reviews alone imply neither contribution to this proof nor sufficient isolation.
This nonblind AI review is not an independent human or formal proof verification.

The maintaining-agent whole SELF replay used only the original reviewer scope with its sole result write intercepted, reproduced the entire old native report in1.827seconds and left all9 program/native files unchanged at the check.
It supplies no fresh isolated coverage, enlarged finite domain, all-integer basis obstruction or Task/E resumption.

The reviewer-only [review_independent.py](review_independent.py) and actual review_result.json (`mathematics/computations/outputs/Yin_J_G0059/review_result.json`) use no author-program imports.
Independent permutation polynomials and Pfaffians reproduce every one of the 3703860 triple candidates, every per-position/count/energy/residue histogram, and the empty full target lists.
Newton traces and a Cayley--Hamilton resolvent verify the full two-parameter constructor and complete absolute formula.
Fractional Newton traces verify both entire rank12 polynomials, with 26 direct determinant values; a breadth-first rank-one child construction separately reproduces the entire 6670-call pivot graph and all 20 saved dead paths.
Its declared 240-second cap and explicit fixed-width integer overflow bound are retained.

The reviewer additionally checked the old path diagonal without changing its mathematical result.
The retired draft is not a mathematical input.

Reproduce from the repository root:

~~~powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0059/review_independent.py
~~~

This writes only the reviewer report at the existing path.
The negative conclusions remain exactly the prescribed finite domains; the general theorem remains an integral bilinear realization, with actual unitriangular basis and useful total cover cost still unresolved.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0121_v1.md#three-column-exterior-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0662_v1.md#exterior-sextic-whole-self-finding) |
