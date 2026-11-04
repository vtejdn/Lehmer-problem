---
author: Yin
---
# Correlated totient-capacity fractional-moment discrimination

## Question and scope

At s=1/2 and t=3/2, test whether the full-divisor-minus-maximum totient array exceeds C104's sharp product-profile constant K_(1/2)=zeta(3/2)/zeta(2).
The exact selected domain is every prime prefix through 97, exponent eight at each prime and all proper divisors of N=(product of the prefix primes)^8.
There are 25 candidates, with 96-bit outward rational square-root and term bounds and both even eta truncations 512 and 1024.
Signed first-omitted-term remainders bound the infinite reference constant.
Parameters were fixed before the author calculation; every separating and nonseparating row is retained.
The formulas, inequality directions and tail proof are in [C105](../../../claims/Yin_C_G0105_v1.md#half-moment-exact-constant-certificate).
No divisor-ideal enumeration, solver optimum or general asymptotic is inferred.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact author calculation with a live 180-second subprocess limit. |
| [verify.py](verify.py) | Separately authored exact reconstruction; no author-program import or invocation. |
| certificate.json (`mathematics/computations/outputs/Yin_J_G0094/certificate.json`) | Complete local author certificate: every candidate and exact intermediate. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0094/verification.json`) | Complete local independent term, constant and candidate intervals. |

Generated evidence is retained at `mathematics/computations/outputs/Yin_J_G0094/`, outside Git.
There is no continuing checkpoint need for these completed finite calculations.

## Reproduction

From the repository root, with the Python standard library:

```powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0094/main.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0094/verify.py
```

The first command generates the fixed-scope certificate; the second verifies an existing certificate and writes a distinct verification result.
Output paths derive from the actual repository/J location, independently of the caller's directory.
Both supervisors keep the 180-second operational limit and report failures directly.
Complete results are published atomically after all checks succeed, without an execution archive or a saved timing/platform gate.
A clone can lack the required certificate; the verifier reports its absence and does not run the author program.
These commands do not resume a Task or enlarge its authorized scope.

## Results and limits

The complete author result has 25 rows and 1,025 term records, including nonseparating earlier candidates.
At truncation 1024 the separating endpoints are 73,79,83,89,97, with 73 first; truncation 512 also separates that row.
The ratio lower endpoint is approximately 1.58867663837140234074 and the constant upper endpoint approximately 1.58816629610300950278.
Exact rational endpoints prove R73>7943/5000, K_(1/2)<7941/5000 and difference>1/2500.
Nonseparation is not a proof of the opposite inequality.
The certificate refutes extending the sharp product constant to arbitrary correlated capacities, not existence of a larger universal constant or the Mahler gap.
The e>=8 extension and positive-density/positive-capture identities are separate arguments in [C105](../../../claims/Yin_C_G0105_v1.md#correlated-half-moment-native-outcome).

<a id="independent-native-verification"></a>
## Independent verification: declared before execution

The separately assigned `strategy_critique` reviewer did not contribute to C105/J94's author proof or program.
Shared context and the saved author result were available, so the arrangement is non-blind.
The original correlated finding retained in [R797](../../../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding) declares an unknown whole/native review relationship because the precise initial author-summary context is not sufficiently established.
The separate verifier implementation and actual outputs remain as recorded; they do not establish context isolation.
The verifier's scope was fixed to the same 25 prefixes, exponent eight, 96 bits and truncations 512/1024 before its invocation.
It uses bisection instead of isqrt, direct square-root enclosures of n^-3 instead of reciprocal sqrt(n), paired alternating sums and maximum-level prime-chain increments instead of the author's closed factor formula.
Every author term/root record, complete constant enclosure, factor/root/energy intermediate, full integer N/phi(N)/mass row and comparison is checked.
No additional ideals or parameters are introduced.

<a id="independent-native-result"></a>
## Independent native result

On 2026-10-15 the separately organized native reproduction completed at the declared scope, with all 1,025 term/root records and 25 rows passing.
Both truncations reproduce the same decisions in every row; independent rational intervals certify the endpoint set and strict bounds above.
The original headings retain the recorded designation, while that original R797 correlated-finding relationship is unknown for the initial-context reason above.
The historical execution date, declared parameters, distinct algorithms and complete mathematical outputs are unchanged; no new run or review is performed here.
This historical checking relationship is distinct from later storage maintenance or reproduction commands.
The [R797 whole review](../../../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding) separately covers the complete proof, arbitrary-e extension and density identities.
C105's own decision controls adoption.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0797_v1.md#g0105-isolated-whole-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding) |
