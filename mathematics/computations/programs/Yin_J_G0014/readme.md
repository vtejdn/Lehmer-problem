---
author: Yin
---
# Exact radical-lift powered-resultant diagnostics

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), [fixed argument C G0007](../../../claims/Yin_C_G0007_v1.md).

## Question and scope

Check the full powered resultant under F_q(t)=P(t^q), including q divisible by the powered exponent.
Compare the linear and quadratic degree normalization in actual reciprocal-unit seed controls.
Exact integer arithmetic only.
The linked Claim owns irreducibility and limiting arguments; these computations do not establish a near-one family or a uniform gap.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Direct FLINT composition resultants and a second full-powered-polynomial representation through SymPy. |
| results.json (`mathematics/computations/outputs/Yin_J_G0014/results.json`) | Exact inputs and 36 completed resultants, including 18 second-representation comparisons. |

## Reproduction

From the repository root, run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0014/main.py`.
The calculation uses python-flint and SymPy.
No random seed, floating tolerance or prior output is used.
Output is written to `mathematics/computations/outputs/Yin_J_G0014/`, independently of the caller's directory.
Inputs are the three ascending coefficient lists retained in the program and results, p in {2,3}, q in {1,2,3,5,7,41}.
The second representation is run for q<=3.
Larger-q irreducibility is justified in C G0007 (the complete retained D G0010 argument), not inferred from this program.

Generated data are retained locally and excluded from Git; a clone can lack them.
Required verification inputs remain explicit, without automatic producer execution or a substituted result.

## Results and limits

The coordinating Codex agent for Yin checked all 36 exact identities R_(1,p)(P(t^q))=R_(1,p)(P)^q in absolute value and Frobenius divisibility checks passed; all 18 full-powered-polynomial comparisons passed.
The base values are (2^10,3^10) for Lehmer, (144,1296) for the quartic Salem seed, and (16,225) for t^2-3t+1.
Small-q polynomials are not assumed irreducible.
The run includes powers that lower degree, with full multiplicities retained.

This is a same-author cross-check using two algebraic representations, not a separately authored independent verification.
It certifies the stated finite integer calculations; the general identity, actual irreducible sequences and their scope are in C G0007 (the complete retained D G0010 argument).
No numerical roots, new scalar gap, family of measures approaching one, or all-power degree-preserving control was obtained.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
