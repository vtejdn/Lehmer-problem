---
author: Yin
---
# Complete integer Boolean rank-seven target enumeration

## Question and scope

Root authorizes one bounded first batch for the TWO complete rank-seven targets already named in [J107](../Yin_J_G0107/readme.md#rank-seven-mod-four-results).
The entropy_attainment_bridge agent authors this protocol, exact integer reduction and program.
Unlike J107's coefficient residues, the present domain is exactly all2^21 upper-unitriangular7-by7 matrices with strict-upper entries0 or1, over the integers.
There are no sign quotients, support filters, congruence screens, coefficient truncations or derivative corrections.
The bit order is row-major strict-upper: (0,1),(0,2),...,(0,6),(1,2),...,(5,6), low bit first.
Both full ascending target arrays are

    phi2_phi6_p4=(t+1)(t^2-t+1)(t^4-t^3-t^2-t+1)
                =[1,-1,-1,0,0,-1,-1,1],
    phi2_p6=(t+1)(t^6-t^5-t^3-t+1)
                =[1,0,-1,-1,-1,-1,0,1].

Reuse inspection found J107 exhaustive only modulo4 on this binary base domain, while [J65](../Yin_J_G0065/readme.md) exhausts the different rank-six domain.
[L226](../../../ledger/Yin_L_G0226_v1.md#explicit-integral-rank-seven-realization) already supplies an integer height4, energy87 realization of the second target, with a large full absolute cost.
Thus a negative Boolean result would not be an integer nonrealizability theorem.
The point is to decide the complete height-one nonnegative domain and retain all actual coefficient expenses of any witness.
[L210](../../../ledger/Yin_L_G0210_v1.md#rank-seven-integral-energy-obstruction) supplies the separate second-target energy>=13 condition, not a substitute for this enumeration.

<a id="integer-boolean-complete-protocol"></a>
## Exact reduction, arithmetic and costs

For any upper-unitriangular U of rank7,

    p_U(t)=det(tU+U^T)=[1,a,b,c,c,b,a,1]

in ascending coefficient order.
The constant/leading coefficients are det(U^T)=det U=1.
Reciprocity follows by transposing the determinant of tU+U^T and replacing t by1/t, including the t^7 factor.
The program nevertheless constructs all eight sparse coefficient polynomials and asserts these identities support by support before evaluating the three independent coefficients.

Expand all7! signed determinant permutations.
For one permutation let f be its fixed-point count, a its number of strict ascents, and S the set of strict-upper variables used in its nonfixed factors.
Its contribution on Boolean entries is exactly sign*t^a*(1+t)^f times product_(j in S)x_j, since x_j^2=x_j on{0,1}.
The support is not a congruence reduction.
Python integers accumulate the entire eight-coefficient vector at each S.
For every mask M, the full coefficient vector is the sum of those vectors over S subset M.
The subset-zeta recurrence evaluates these sums on all2097152 masks.
No modular reduction or floating-point arithmetic occurs.
Four declared direct determinant controls at masks0,2097151,7092,2323 check the full table polynomial inside this same batch; no old modular witness is treated as an integer target.

For each coefficient k and every partial zeta stage, its absolute value is at most7!*max_(0<=f<=7) binomial(f,k-a)<=7!*binomial(7,3)=176400 for k=1,2,3.
Indeed each partial sum contains a subset of distinct support terms, each of which is itself a signed sum of original permutation contributions; the triangle bound includes each permutation at most once.
The same bound covers the sparse accumulation, and every array addition stays inside signed32-bit range.
Python uses unbounded integers for sparse generation, exact determinant interpolation, counts and witness metadata.
The dense table has shape(2^21,3), dtype int32, exactly24MiB.

All eight target coefficients are compared through the proved and support-checked full reciprocal pattern.
For each target retain the full sorted uint32 mask array, its total count and exact support-energy histogram.
Select one minimum-energy witness, breaking ties by smallest mask, if any exists.
For it retain the original matrix, its negative-absolute companion (diagonal1, upper entries-|U_ij|), and the literal vertex-then-sheet rank14 cover.
A positive upper entry gives the off-sheet negative block; a negative entry would give the same-sheet negative block, although none occur in this domain.
Compute all three complete integer determinant polynomials independently of the zeta table by Bareiss determinants at all degree+1 integer nodes and exact rational forward differences.
Check the literal cover polynomial equals the product of original and absolute polynomials; do not infer it without the direct rank14 calculation.
Retain all original/absolute/cover ranks, heights and squared-entry energies.
No Mahler measure, factor cancellation or equivalence of those costs is assumed.

## Declared resource and output boundary

Exactly one author batch is authorized: aggregate300 seconds including runtime import and serialization,512MiB worker commit and hard working set, and64MiB total output.
No mathematical retry, escalation, changed target or larger entry box is selected.
The small parent monitor is excluded from worker-memory accounting.
The launcher copies the already corrected J107 Windows guard: process/job commit caps, SetProcessWorkingSetSizeEx hard maximum with readback, and no conflicting JOB_OBJECT_LIMIT_WORKINGSET flag.
No privilege enabling is attempted.
BLAS/OpenMP thread counts are set to one before NumPy import, retaining the useful J107 resource-failure lesson.
Mathematics starts only after JOB_READY is sent following guard verification.
A resource stop retains an honest incomplete result; it does not certify either target absence or complete counts.
The current task's usedPercent>=90 stop gate takes precedence before launch.

The dense three-coefficient table is24MiB.
Even two worst-case full matching-mask arrays add at most16MiB, leaving over23MiB for sparse coefficients, witnesses and metadata.
Witness payloads and the sparse formal map are explicitly bounded before publication, and all files remain under the declared aggregate cap.
The working table, match buffers and NumPy runtime are expected well below512MiB; the OS guard enforces the actual bound rather than relying on that estimate.

## Files and reproduction

[main.py](main.py) is the author implementation, and [inputs.json](inputs.json) fixes the targets, domain and caps.
It copies J107's exact Bareiss/forward-difference determinant helpers and corrected resource launcher, with explicit author-code reuse; this is not independent verification.
Its Boolean integer coefficient map and complete matching selection are newly authored for the changed domain.
It imports no generated J107 output and has no input dependency on a prior run.
The default output home is this J's identity under mathematics/computations/outputs, with an author child.
The retained native files are coefficients.npy, one matches_<target>.npy per target, sparse_coefficients.json, result.json and execution.json.
The three-column dense table determines every one of the eight complete coefficients by the stated exact pattern.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0110/main.py
```
No scope-changing command-line parameters are accepted.
The program refuses to overwrite an existing author output directory.
The separately authored full-domain verification is described below; no author self-check is called independent.

<a id="integer-boolean-complete-results"></a>
## Completed author result and exact limits

The author batch completed the entire2^21 domain.
Its complete result (`mathematics/computations/outputs/Yin_J_G0110/author/result.json`) and execution account (`mathematics/computations/outputs/Yin_J_G0110/author/execution.json`) report successful full coverage.
The native integer coefficient table (`mathematics/computations/outputs/Yin_J_G0110/author/coefficients.npy`) retains all2097152 rows, and sparse_coefficients.json (`mathematics/computations/outputs/Yin_J_G0110/author/sparse_coefficients.json`) retains all2461 nonzero support vectors with all eight coefficients.

| Complete target | Matrices evaluated | Exact integer matches | Complete matching set |
| --- | --- | --- | --- |
| (t+1)Phi6 P4 | 2097152 | 0 | Empty uint32 array (`mathematics/computations/outputs/Yin_J_G0110/author/matches_phi2_phi6_p4.npy`) |
| (t+1)P6 | 2097152 | 0 | Empty uint32 array (`mathematics/computations/outputs/Yin_J_G0110/author/matches_phi2_p6.npy`) |

All5040 determinant permutations and21 integer subset-zeta stages completed.
No matching witness exists in this author output, so minimum energy and selected witness are null and both22-bin energy histograms are zero.
The declared direct full-integer controls agree at masks0,2097151,7092,2323, with full arrays respectively

    [1,7,21,35,35,21,7,1],
    [1,1,1,1,1,1,1,1],
    [1,-1,-7,-12,-12,-7,-1,1],
    [1,2,1,-1,-1,1,2,1].

Those four controls are author cross-checks, not independent certification of all rows.
The final dense triples lie between-85 and35; the largest upper intermediate value is42, and all stages satisfy the proved176400 bound.
The full batch took0.485 seconds including guard/startup/serialization, with peak worker commit86876160 bytes and peak job commit88981504 bytes.
Its six retained output files total25416574 bytes, below64MiB.
NumPy2.3.5 performed only exact int32 array operations; all determinant interpolation and sparse generation used Python integers and Fraction.
There was no resource failure, retry, domain change or mathematical escalation in this J.
The copied corrected guards were verified before mathematics started.

This is a complete AUTHOR negative result for exactly the nonnegative height-one rank7 domain.
It does not exclude signed height-one matrices, arbitrary integer entries, other ranks or stabilizations.
In particular it does not contradict L226's actual height4 integer realization of the second target.
Neither target has an original/absolute/cover witness to retain from this finite domain; the declared positive-witness branch was not exercised and supplies no evidence.
No Mahler-gap conclusion or absolute-cover optimization follows.
The separate full-domain checker has now passed as recorded below; selected controls alone were not used to certify the absence claim.
The complete fixed [R431 independent finding](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) checks the protocol, exact reduction, complete native evidence and finite-negative scope without a required repair.
Strategy or Task adoption remains separate.


<a id="integer-boolean-independent-reconstruction"></a>
## Complete independent reconstruction

The noncontributor loglog_cyclic_review agent authored [verify.py](verify.py) and the [independent protocol](verify_protocol.md), with no import of author mathematical helpers.
Recursive polynomial Laplace expansion through all128 column-subset minors reconstructs every Boolean support's FULL eight-coefficient vector.
A descending-bit zeta transform on a transposed int64 table independently evaluates all2097152 matrices, after which all6291456 independent coefficient entries are compared with the author table.
The verifier reconstructs both entire matching-mask arrays, all energy histograms and null minimum/witness fields, and checks the four full control polynomials by triangular inversion and Newton identities.
This covers the complete negative domain, not a sample of rows or a positive-witness-only check.

The sole declared independent run passed within the same300-second,512MiB hard commit/working-set and64MiB output limits.
It took0.5905008 seconds, with peak worker commit134561792 bytes and peak job commit136683520 bytes.
Its native verification result (`mathematics/computations/outputs/Yin_J_G0110/verifier/verification.json`), execution (`mathematics/computations/outputs/Yin_J_G0110/verifier/execution.json`), transposed complete table (`mathematics/computations/outputs/Yin_J_G0110/verifier/coefficients.npy`), complete formal map (`mathematics/computations/outputs/Yin_J_G0110/verifier/sparse_coefficients.json`), first empty matching array (`mathematics/computations/outputs/Yin_J_G0110/verifier/matches_phi2_phi6_p4.npy`) and second empty matching array (`mathematics/computations/outputs/Yin_J_G0110/verifier/matches_phi2_p6.npy`) are retained.
All2461 nonzero full coefficient supports and all dense table entries agreed, and both complete target counts remain zero.

The review arrangement is nonblind and noncontributor: the verifier read the author protocol/output schema and used the same Windows host and NumPy arithmetic runtime.
The corrected J107 operational guard is shared reuse, not an independent mathematical algorithm or a formally audited runtime.
The generating determinant recurrence, transform orientation/data type and direct-control method differ from the author's.
No new target, entry domain, parameter scan or author rerun occurred during verification.
The unexercised positive-cost branch is not certified by this negative-domain run.

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
| `author/coefficients.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `author/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `author/matches_phi2_p6.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `author/matches_phi2_phi6_p4.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `author/result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `author/sparse_coefficients.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/coefficients.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/matches_phi2_p6.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/matches_phi2_phi6_p4.npy` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/sparse_coefficients.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
| `verifier/verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0431_v1.md#integer-boolean-whole-independent-finding) |
