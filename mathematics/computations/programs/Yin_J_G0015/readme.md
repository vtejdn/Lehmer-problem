---
author: Yin
---
# Actual return cores and low-height quotient experiments

## Native input availability

The selected pilot.json and lehmer-long.json native coefficient arrays are unavailable in this checkout and its selected local Git history.
The thirteen adopted witnesses and their original return times in [L354](../../../ledger/Yin_L_G0354_v1.md) do not determine the missing complete p/q/product arrays.
The verification-only command therefore cannot currently replay those original witnesses.
Retain the original selected arrays in this group's tracked inputs/ and point verify.py there when they are available; a new MILP witness would not identify this historical selection.

## Question and scope

For the quartic Salem, Mercat quartic, Lehmer and golden-ratio controls, find height-one integer multiples Pq with large quotient height.
This is finite evidence for [L G0157's returning-core question](../../../ledger/Yin_L_G0157_v1.md#return-core-quotient-height-equivalence), not a proof of unboundedness or an entropy estimate.

## Files

| File | Role |
| --- | --- |
| [probe.py](probe.py) | MILP witness discovery with a direct integer check before saving. |
| pilot.json (`mathematics/computations/outputs/Yin_J_G0015/pilot.json`) | Four inputs at quotient lengths 20,40,80; twelve feasible witnesses. |
| lehmer-long.json (`mathematics/computations/outputs/Yin_J_G0015/lehmer-long.json`) | Length 160 witness and failed length 320 attempt. |
| [verify.py](verify.py) | Separate standard-library polynomial division, Horner return and Bareiss state-norm verification; imports no author helper. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0015/verification.json`) | Exact verified finite payload. |

The mathematical source boundary and next experiments belong to [D G0008](../../../ledger/Yin_L_G0354_v1.md#large-quotient-pilot).

## Reproduction

Run from the repository root.
Discovery uses NumPy, SciPy and its bundled HiGHS MILP optimizer.
All q coefficients are integral with explicit bounds 50 or 200; product coefficients are constrained to [-1,1]; the objective maximizes q at index floor(N/2).
No random seed or optimality guarantee is used.
The `--seconds` option supplies the live per-instance wall-clock limit; another run may find a different witness.
Output paths use `mathematics/computations/outputs/Yin_J_G0015/` and require no previous output for discovery.

Discovery requires the stated NumPy and SciPy dependencies; the shared baseline dependency file does not include SciPy.
Use a compatible existing environment with normal package resolution.
The exact verification command retains its separately stated standard-library dependencies.

```powershell
python -B mathematics/computations/programs/Yin_J_G0015/probe.py --seconds 4
python -B mathematics/computations/programs/Yin_J_G0015/probe.py --cases lehmer --lengths 160,320 --seconds 8 --bound 200 --output mathematics/computations/outputs/Yin_J_G0015/lehmer-long.json
python -B mathematics/computations/programs/Yin_J_G0015/verify.py
```

The existing optional `--scipy-path` can select an external package directory when actually needed; its persistent machine locator belongs only in the responsible human's private setup.
Normally installed SciPy needs no such argument.
The verification-only command reads the two saved native JSON witness files and requires no SciPy/NumPy.
It compares mathematical arrays and identities rather than timestamps or file hashes.

Generated data are retained locally and excluded from Git; a clone can lack them.
Required verification inputs remain explicit, without automatic producer execution or a substituted result.

## Results and limits

The retained calculation found quotient heights 2,3,5 for the quartic t^4-t^3-t^2-t+1; 1,3,4 for the Mercat quartic t^4-2t^3+t^2-2t+1; 6,11,19 for Lehmer's polynomial; and 1,1,1 for the golden-ratio control.
The longer Lehmer run found height 30 at N=160 and no feasible witness within its N=320 time limit.
All thirteen retained witnesses passed independent-algorithm exact verification, including their endpoint returns and displayed intermediate norms.
This checking arrangement uses a separate implementation by the same agent, not an independent-agent review.

For Lehmer N=160 the largest saved state norm is 10323130327.
Its word has only the initial zero return at time 1 and final return at time 170, yielding a genuine first-return word after deleting that initial zero.
The verifier records every return time.
MILP time limits, finite q bounds and target-coordinate selection do not establish global optimality, infinity of the core, an entropy rate or a near-one family.
No optimizer failure has been recorded as mathematical infeasibility.

The coordinating reviewer read the complete verifier and separately reran it.
All thirteen witnesses reproduced the saved exact values.
This is an independent execution and code inspection of the author's verification algorithm, not a separately authored third algorithm or a rerun of MILP discovery.
The related source/domain review is recorded in D G0008.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
