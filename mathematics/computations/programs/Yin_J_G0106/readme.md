---
author: Yin
---
# Exact four-digit-overlap carry graphs and true midpoint energies

## Question and scope

Exactly six inputs n=5,6,7,8,9,10 use the original quartic P=1-t-t^2-t^3+t^4, b=2, N=2n and k=n-2.
The complete original ternary weights are1,2,1 before normalization by4 per digit.
The [fixed analytic statement and complete proof](../../../claims/Yin_C_G0170_v1.md#statement) gives the exact overlap graph, true midpoint marks and conditional energy; its entire finite protocol is retained in [record.md](record.md).
This is a new finite discriminator, not an extension of an old numerical scan.
No state box, additional overlap, eigenvalue computation or asymptotic inference is included.

The entropy_attainment_bridge agent authors main.py and the analytic candidate.
The loglog_cyclic_review agent separately authors verify.py, imports no author helper and retains its actual non-blind arrangement in [verify_protocol.md](verify_protocol.md).
Root authorized preparation and the subsequent bounded execution gates.

The initial resource-configuration failure and separately authorized equivalent-guard correction are retained below.
The corrected first mathematical author batch and the separate independent verifier both completed the declared scope.

## Files

- [inputs.json](inputs.json) fixes every mathematical input and cap.
- [main.py](main.py) owns the exact author calculation and guarded launcher.
- [record.md](record.md) retains the complete six-input protocol and stopping distinctions.
- [verify.py](verify.py) and [verify_protocol.md](verify_protocol.md) own separate verification, including direct all-word checking at n=5.

Generated data use `mathematics/computations/outputs/Yin_J_G0106/author/` and a separate verifier output directory under the same J home.
Complete author and verifier outputs are linked in the results below.

## Reproduction and resource enforcement

From the repository root, after the execution gate, run:

```powershell
python mathematics/computations/programs/Yin_J_G0106/main.py
```

Use ordinary Python3 on Windows, without optimization flags; only the standard library and Windows APIs are used.
The program refuses a nonempty author output directory, avoiding implicit overwrite of a preceding run.
The internal `--worker` entry is not a reproduction command.
Default paths are resolved from the actual containing J directory, independently of the caller's working directory.

The aggregate author wall-clock cap is60seconds from worker creation through calculation and output publication.
The parent timeout terminates the worker's Job Object at the cap; post-stop status collection performs no further mathematics.
The mathematical worker has512MiB process/job commit limits and an explicitly enabled, read-back512MiB hard working-set maximum before receiving its start handshake.
A failed resource-control call stops before mathematical execution.
The lightweight parent monitor is outside the worker memory cap; this distinction is recorded in execution.json.
The working-set flag follows the primary [Microsoft SetProcessWorkingSetSizeEx documentation](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex).

All author output, including atomic-write intermediates and final execution status, is limited to64MiB.
Mathematical payload publication reserves64KiB for status, counts bytes before writing and removes an interrupted temporary file.
Only a completed case is atomically published; a cap or exception leaves earlier completed cases and an honest incomplete status.
No limit or scope escalation is automatic.
The separate verifier has its own declared full limits and awaits author output plus root's go.

## Public exact schema

All beta coordinates are ordered `(1,beta,beta^2,beta^3)` in O=Z[beta].
A rational is `[numerator,denominator]` with positive denominator.
A quadratic-field pair is `[rational_A,rational_B]` and means A+B*u for u=(1-sqrt13)/2 in the neutral embedding.
No decimal approximation is used by the author calculation.

`counts.json` has schema `g106-counts-v1` and a `tables` object indexed by strings0 through10.
Each table is a lexicographically sorted list `[a0,a1,a2,a3,integer_weight]` of ALL supported endpoints with their original weighted counts.

Each `case_nXX.json` has schema `g106-case-v1`, n,N,b,k and the following fields:

- `left`, `right`: lexicographically sorted positive-marginal endpoint beta-coordinate arrays.
- `row_mass`, `column_mass`: the complete integer marginals.
- `row_mark_sum_beta`, `column_mark_sum_beta`: integer weighted midpoint-coordinate sums before dividing by the corresponding marginal.
- `edges`: sorted arrays `[left_index,right_index,weight,y0,y1,y2,y3,theta0,theta1,theta2,theta3]`, retaining every positive edge, its exact midpoint and its unique four middle digits.
- `components`: sorted by their left vertex list; each contains complete `left`, `right`, `edges` index lists, `mass_integer`, rational `probability`, four-rational `mean_beta`, and quadratic `mean_square_pair`, `second_moment_pair`.
- `S`, `moment_numerator_pair`: the full return count and two integer neutral-moment numerators.
- `m_pair`, `D_pair`, `rayleigh_upper_pair`: exact true midpoint moment, update energy and D/m, respectively.
- `half_word_S`, `half_word_moment_numerator_pair`: the author's separate L335 half-word check.
- `checks`: finite arithmetic identities and actual degree maxima; these do not replace independent verification.

The component mark fields are conditional on that complete component and retain its original probability separately.
The Rayleigh ratio is an UPPER bound for the global gap, never a lower bound or a certified second singular value.
`results.json` records complete versus partial six-input coverage and actual candidate-edge lookup count.
`execution.json` records the launch result, cap/exception state and available resource observations.
An output file is not by itself a correctness oracle.

<a id="complete-six-case-results"></a>
## Results and limits

The corrected first mathematical author batch completed all six declared inputs, and the separately implemented native verification passed every complete mathematical payload.
There was no mathematical rerun, changed input, expanded overlap, state-box substitution or resource escalation.
The author and verifier each made405972 candidate edge lookups, below the declared796068 bound.

Put u=(1-sqrt13)/2.
The displayed moments are exact elements of Q(u), not decimal estimates.
Each native case file retains the complete exact D_pair and Rayleigh UPPER bound D/m together with every edge and conditional mean.

| Half-length n | Endpoints per side | Edges | Components | Complete weighted return sum S | Exact true midpoint moment m_n |
| --- | --- | --- | --- | --- | --- |
| 5 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n05.json`) | 9 | 29 | 3 | 1532 | (154-60u)/383 |
| 6 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n06.json`) | 15 | 75 | 3 | 7296 | (115-49u)/228 |
| 7 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n07.json`) | 19 | 95 | 3 | 35120 | (1324-547u)/2195 |
| 8 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n08.json`) | 25 | 141 | 1 | 170848 | (3672-1560u)/5339 |
| 9 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n09.json`) | 35 | 247 | 1 | 835448 | (79982-34589u)/104431 |
| 10 (`mathematics/computations/outputs/Yin_J_G0106/author/case_n10.json`) | 47 | 331 | 1 | 4119392 | (111909-48309u)/128731 |

For n=5,6,7 there is one sign-symmetric central component of midpoint mean zero and two further components.
Each further component has constant actual midpoint algebraic value +(2-beta^2) or -(2-beta^2), so its conditional variance is zero and its squared neutral modulus is3-2u=2+sqrt13.
The original conditional mass of EACH such component is respectively1/383,1/456 and4/2195; the two signed components have twice those masses together.
These are actual positive-mass marked components, so the four-digit-overlap global gap is zero at these three finite lengths despite the absence of the rational-span invariant.
For n=8,9,10 the complete graph is connected and the midpoint is globally centered.
This establishes connectivity only at those three lengths, with no eventual or uniform spectral-gap conclusion.

The exact author count tables (`mathematics/computations/outputs/Yin_J_G0106/author/counts.json`), coverage record (`mathematics/computations/outputs/Yin_J_G0106/author/results.json`) and guarded execution record (`mathematics/computations/outputs/Yin_J_G0106/author/execution.json`) preserve all original multiplicities and actual run limits.
Author checks matched S and m_n with the separate L335 half-word formula, checked the exact quadratic-field inequalities0<=D<=min(m_n,4), centering and both degree maxima.
A true moment or Rayleigh ratio at six lengths is not a proof of diffusive growth, infinite mean, finite mean or a Mahler gap.
The early disconnections do not refute the explicitly EVENTUAL contraction criterion of C170.
The next selected mathematical question must explain the actual weighted connectivity and contraction; an enlarged scan is not automatic.

## Complete independent native verification

The independent verification result (`mathematics/computations/outputs/Yin_J_G0106/verifier/verification.json`) and verifier execution record (`mathematics/computations/outputs/Yin_J_G0106/verifier/execution.json`) report one complete declared run.
The separate verifier count tables (`mathematics/computations/outputs/Yin_J_G0106/verifier/counts.json`) and six corresponding case_nXX.json files preserve its reconstructed finite payloads.
The actual methods are specified in [verify_protocol.md](verify_protocol.md): binary-endpoint autocorrelation, descending polynomial reduction, opposite-side edge construction, right-half marks, independent component traversal and complete half-word checks.
Every endpoint, count, edge, middle word, algebraic midpoint, marginal, weighted mean, component, moment, energy and Rayleigh pair agrees.
At n=5 the verifier additionally enumerated all59049 original ternary words, found29 returned words with total integer weight1532, and directly grouped COMPLETE tail words to check both conditional-variance terms.

The arrangement is non-blind and imports no author helper.
Both implementations use standard Python integer/Fraction arithmetic and the same Windows host; this shared runtime is disclosed rather than treated as independent arithmetic hardware or formal verification.
The complete analytic theorem has [R803 whole review](../../../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding), and the complete final native record has [R412 whole review](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding).
Those actual fixed findings preserve separate analytic and finite-computation scopes; Task/Claim adoption remains at the responsible decisions.

Both runs stayed inside their own60second,512MiB worker and64MiB output caps.
Author parent wall time was0.7717362seconds, with peak worker commit20504576bytes and peak job commit21778432bytes; its complete output occupies457298bytes.
Verifier parent wall time was1.3468295seconds, with peak worker commit26976256bytes and peak job commit28250112bytes.
The small parent monitors are excluded from the declared worker-memory caps and perform no mathematical reconstruction.
These runtime observations do not certify any untested input or replace the native mathematical checks.

## Resource-launch correction before mathematical execution

The first author launch stopped before worker creation when SetInformationJobObject returned WinError1314 (required privilege not held).
No endpoint, table, graph or scalar calculation had begun, and no mathematical output was produced.
Root inspected the primary [Job Object contract](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_basic_limit_information) and retained the separate [hard process working-set contract](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex).
Root removed only the redundant Job Object working-set flag0x1, preserving the512MiB process and aggregate job commit limits, kill-on-close, the separate hard512MiB working-set setting/readback, and the original time/output caps.
No privilege was enabled and no numerical limit was relaxed.
An idle-child guard-only probe then passed with job flags8960, both commit limits536870912 bytes, read-back working-set maximum536870912 bytes and flags6.
That probe ran no mathematics and is not a second mathematical batch.
Root separately authorized the corrected guarded first mathematical launch after a fresh usage reading.
That first mathematical batch completed within the unchanged caps, followed by the separately authorized independent verifier; no further mathematical batch or cap escalation occurred.

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
| `author/case_n05.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/case_n06.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/case_n07.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/case_n08.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/case_n09.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/case_n10.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/counts.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `author/results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n05.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n06.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n07.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n08.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n09.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/case_n10.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/counts.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
| `verifier/verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) |
