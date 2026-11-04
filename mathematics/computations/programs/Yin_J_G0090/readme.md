---
author: Yin
---

# Independent exact reconstruction of the saved Phase B Lehmer primal packet

<a id="pre-run-declaration"></a>
## Native input availability

The indispensable selected native input is [J89's original basis/packet certificate](../Yin_J_G0089/readme.md#native-input-availability), which is unavailable in this checkout.
verify.py still preserves the historical multi-file checking interface and cannot currently replay it.
Its future input adaptation must reuse one minimum tracked J89 certificate, retaining all actual packet/congruence/negative-witness checks and the capped-failure boundary rather than requiring whole solver logs or inventing a new failed run.

## Question and scope

This is a targeted native review of [J89](../Yin_J_G0089/readme.md), not a solver rerun or a whole review of the upstream lattice arguments.
The periodic_packet_author_finish reviewer authored the upstream D2 work; that contribution is disclosed in [R232](../../../audits/reviews/Yin_R_G0232_v1.md#lehmer-primal-native-certificate-finding).
The separately assigned whole reviewer owns [the original R790 account retained in R790](../../../audits/reviews/Yin_R_G0790_v1.md#original-g0321-account).

The domain is the original Lehmer polynomial, degree 10, eleven original coefficient positions and saved basic columns, ten positive final packet records, all ten lags and allowed width T=10.
[verify.py](verify.py) reconstructs all eleven equality rows directly and solves them by Fraction elimination, retaining the zero basic weight before omitting it.
Companion-matrix Horner evaluation and separately formed Sylvester determinants independently verify each full signed norm and resultant.
It imports no author mathematical code and uses no SymPy or HiGHS.

## Command and evidence

[main.py](main.py) supervises the standard-library verifier with a live 60-second timeout; the worker checks its 58-second deadline.
From any working directory, invoke the program through its actual path; the repository-root command is:

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0090/main.py
```

Required J89 outputs are highs_result.json (`mathematics/computations/outputs/Yin_J_G0089/highs_result.json`), highs_lead.json (`mathematics/computations/outputs/Yin_J_G0089/highs_lead.json`), matrix.json (`mathematics/computations/outputs/Yin_J_G0089/matrix.json`), progress.json (`mathematics/computations/outputs/Yin_J_G0089/progress.json`) and failure.json (`mathematics/computations/outputs/Yin_J_G0089/failure.json`).
The progress file is the completed atom-generation input, not a disposable console record.
The verifier writes its distinct certificate.json (`mathematics/computations/outputs/Yin_J_G0090/certificate.json`).
Missing required output is reported as missing; the verifier does not regenerate the source family or solver result.

## Actual sole review execution and result

The separately declared check completed on 2026-10-12, after the author packet account and before the targeted finding.
It confirms E=680/681, q=9, M=2043, ME=2040, S=18360/227 and actual width 10.
The ten signed residue norms are (1,1,1,1,1,1,1,1,1,-269), and the full copied product is -269*9^20430.
Every coefficient, weight, residue, lag, least denominator, content, width and multiplicity was calculated before comparison with the author's values.

The exact matrix check independently verifies H0=A^T H A, the saved invertible rational congruence with determinant -1 and diagonal (2,2,3/2,3/2,4/3,4/3,1,1/4,-1,1/4), the negative witness of H-value -4 and one ternary witness of H-value 0.
It does not certify integral lattice equivalence or replay the complete ternary minimum.
Selected generator membership is checked from the original companion recurrence and actual saved anchor recipes, not by re-enumerating all 762,150 atoms.

Rows 1--7 and 9 satisfy the old C24 family restrictions; row 8 fails its energy bound because 14/3>4, and row 10 has nonternary residue and energy 164.
Their old finite-functional values are (1,1,1,1,1,2,2,3,1,-14), with exact weighted average 680/681.
The Phase A 3,000-pivot truncation and missing final floating basis/objective remain explicit; no result or infeasibility conclusion is supplied for that failed search.
Phase B is an exact feasible primal certificate, not a proof of numerical or global optimality.
The complete calculated matrices and rows remain in the independent certificate and its fixed R232 scope.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0232_v1.md#lehmer-primal-native-certificate-finding) |
