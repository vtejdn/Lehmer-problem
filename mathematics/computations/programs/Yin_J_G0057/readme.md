---
author: Yin
---

# Adjacent actual centered-column edge elimination

## Question and scope

Exact author pilot supporting the complete [C438 adjacent-window theorem](../../../claims/Yin_C_G0438_v1.md#statement), with the [original L257 author history](../../../ledger/Yin_L_G0257_v1.md#adjacent-edge-reuse-and-domain) retained.
The declared scope was twelve actual input/window pairs and a120-second total cap.
Both adjacent centered projections are rebuilt over Q in each row.
The scope is a changed coupled auxiliary, not an enlargement of J56's derivative table or a proof of higher-degree uniform sign.

## Files

- [verify.py](verify.py): author program, with the rational projection recipe explicitly reused from J56 and both windows independently reconstructed from each input's coefficients; it does not import author outputs or a supplied edge formula.
- verification.json (`mathematics/computations/outputs/Yin_J_G0057/verification.json`): complete native output of the sole successful author execution, including full coefficient vectors, primitive scalars, both edges, zero cases, actual quotient content/degree, trace cofactors, signed resultants, coefficient energies and exact margin signs.

The separate checker and its actual scope are recorded below.

## Reproduction

From the repository root, run `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0057/verify.py`.
The program requires SymPy.
The program refuses to overwrite an existing verification.json; preserve the original and redirect review executions or intercept only their intended output write.
No network, random choices, floating root isolation or environment-sensitive discovery is needed.

## Declared inputs and exact checks

The quartic t^4-t^3-t^2-t+1, degree-six t^6-t^5-t^3-t+1 and original Lehmer polynomial each use j=d-1,d,2d-1.
The quadratic t^2-3t+1 uses j=1,4.
The actual irreducible radical t^4-4t^2+1 uses j=4.
Each row reconstructs the pair at j and j+1, so the author pilot contains twelve pairs rather than twelve single projections.
The actual irreducibility of each declared input, reciprocal coefficients and a positive real root beyond1 are checked exactly.

The program checks monic remainder equality, projection orthogonality and centered norm; independent primitive clearing in each window; both complete reciprocal edge identities; exact division by the ORIGINAL P; formal anti-reciprocity and degree at most d; nonvanishing in every nonzero case; the complete original-root coupled-value identity; triangular integral trace extraction and coefficient content; weighted arcsine-moment energy; the exact signed full norm P(1)P(-1)Res(Q,V)^2; full content scaling; and the exact sign comparison Res(P,C_primitive)^2 versus S_2(C_primitive)^(2d).
No approximate Mahler value decides a sign.
The true zero row is retained and has the corresponding shifted projection plateau.

## Results and limits

All twelve pairs passed.
Eleven coupled quotients are nonzero; the radical j=4 quotient is zero.
Both quadratic controls and quartic j=4 have positive net margin; the other eight nonzero rows have negative margin.
L257 proves the all-window quadratic collapse and exact radical plateau formulas; the twelve rows alone give no all-input extension.

The quartic j=4 result has primitive C=8t^4-7t^3+7t-8, content32 before normalization, energy226 and signed resultant-118803=-3*199^2.
Its positive net margin is exactly(1/4)log(118803/51076).
The [complete C438 quartic argument](../../../claims/Yin_C_G0438_v1.md#adjacent-edge-quartic-positive-control) retains its full leading coefficient, actual p-adic root depths and fixed-positive original measure.
No proof of a positive gap, near-one coverage, general higher-degree negativity or numerical enumeration beyond the declared cases is claimed.
A complete independent review remains separate from these author checks.

## Independent inspection

The adopted [C438 proof](../../../claims/Yin_C_G0438_v1.md#argument) has its [complete isolated R653 finding](../../../audits/reviews/Yin_R_G0653_v1.md#adjacent-edge-isolated-whole).
The original 2026-10-10T01:04 R156 whole finding remains UNKNOWN because its initial target context is unestablished, as retained in [R653's later historical comparison](../../../audits/reviews/Yin_R_G0653_v1.md#adjacent-edge-isolated-whole).
The distinct original implementation/execution below remains true without an agent-isolation inference.
A present stdout-only replay of that same fixed twelve-pair reviewer matched its complete result and every native mathematical field, with its sole write intercepted; no author producer or program/native file changed.

The coordinating noncontributor independently reconstructed all twelve pairs using standard-library Fraction row-space projection, quotient-ring determinants and rational-node trace interpolation in [review_independent.py](review_independent.py).
It imports no author program.
The result (`mathematics/computations/outputs/Yin_J_G0057/review_result.json`) agrees on every mathematical field, including the zero quotient and all eleven nonzero margins.
That original whole finding also covered the analytic argument separately; its exact scope is retained in the later historical comparison above.
Earlier J56 implementation and upstream roles are disclosed; no near-one uniformity or Task completion follows.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0641_v1.md#adjacent-edge-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0653_v1.md#adjacent-edge-isolated-whole) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0641_v1.md#adjacent-edge-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0653_v1.md#adjacent-edge-isolated-whole); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0656_v1.md#trace-order-whole-self-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0669_v1.md#trace-order-whole-independent-finding); [Claim support and recorded result](../../../claims/Yin_C_G0438_v1.md); [Claim support and recorded result](../../../claims/Yin_C_G0451_v1.md) |
