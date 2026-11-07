---
author: Yin
---
# Lehmer compact enumeration feasibility

## Native input availability

The original selected enclosing certificate, 797507-candidate superset and necessary 1044588-node ancestry are retained under [inputs/](inputs/).
The payload was extracted from the author's retained original calculation, not produced by a new pruned discovery.
Only the enclosing matrices/bounds, complete compact set, necessary ancestry closure, seventy outer states and concise fixed-scope metadata are retained; floating path parameters, the 4003565-state discovery store, runtime diagnostics and logs are not verification inputs.
[compact-states.bin.gz](inputs/compact-states.bin.gz) is the original little-endian candidate array compressed with gzip.
[path-nodes.bin.gz](inputs/path-nodes.bin.gz) concatenates the two original ancestry parts before compression, retaining every original 13-byte state/parent/digit record.
The original exact enclosure and path checks, J28's complete distinct traversal and J29's separate edge/exclusion checks all passed using these tracked inputs.
J28 reproduced all 797507 states and the complete original sequence, with 4818379 recursion nodes and 3077691 leaves; J29 checked all 1044588 edges, 797437 covered candidates and seventy exact exclusions at maximum depth 25.

## Scope

Estimate and, only if bounded and feasible, enumerate a certified finite superset of the radius-eight Lehmer compact residue.
Numerical count estimates are distinct from exact completeness certificates.

## Fixed inputs and verification

The verification-only commands below need Python with its standard library and no previous output:

```powershell
python -B mathematics/computations/programs/Yin_J_G0026/verify_certificate.py
python -B mathematics/computations/programs/Yin_J_G0026/classify_uncovered.py
python -B mathematics/computations/programs/Yin_J_G0026/verify_paths.py
```

They read [enumeration-certificate.json](inputs/enumeration-certificate.json), [enumeration.json](inputs/enumeration.json), the compressed compact set, [path-certificate.json](inputs/path-certificate.json), the compressed ancestry and [uncovered.bin](inputs/uncovered.bin).
The generated reports use the ignored output home.
The gzip format changes storage only; exact integers and full finite coverage are checked.

## Discovery programs and optional reproduction

The responsible proof is [C399 compact enumeration](../../../claims/Yin_C_G0399_v1.md#lehmer-compact-complete-enumeration).

- [estimate.py](estimate.py), estimate.json (`mathematics/computations/outputs/Yin_J_G0026/estimate.json`): exact coefficient bounds and discriminant, with separately labelled volume diagnostics.
- [prepare.py](prepare.py), enumeration-certificate.json (`mathematics/computations/outputs/Yin_J_G0026/enumeration-certificate.json`): integer basis, unimodular reduction, exact rational LDL and outward triangular rounding enclosure.
- [Enumerate.cs](Enumerate.cs), [run.ps1](run.ps1): bounded checked-integer recursive traversal and conservative embedding filters.
- compact-states.bin (`mathematics/computations/outputs/Yin_J_G0026/compact-states.bin`), enumeration.json (`mathematics/computations/outputs/Yin_J_G0026/enumeration.json`): all retained candidates, completed-run report.
- [verify_certificate.py](verify_certificate.py), certificate-verification.json (`mathematics/computations/outputs/Yin_J_G0026/certificate-verification.json`): separately organized exact recomputation of the enclosure, transformation and filter bounds, plus output integrity and uniqueness checks.
  It imports neither prepare.py nor the compiled traversal.

Reproduction from repository root:

```powershell
python -B mathematics/computations/programs/Yin_J_G0026/estimate.py
python -B mathematics/computations/programs/Yin_J_G0026/prepare.py
& mathematics/computations/programs/Yin_J_G0026/run.ps1
```

Preparation uses Python with SymPy solely to produce the integer LLL change of basis.
Its determinant and identity are checked exactly.
The certificate checker uses only the standard library.
The bounded traversal uses PowerShell `Add-Type` to compile the C# implementation.
These optional producer commands write discovery outputs, while the verification-only commands deliberately check the tracked adopted inputs.
A new discovery result is not automatically adopted or identified as an original historical certificate.

## Completed enumeration and limits

The dense coefficient box contains 108561184875 tuples.
The certified containing ellipsoid instead required 4818379 recursion nodes and 3077691 full leaves, yielding 797507 distinct retained candidates.
Both caps remained unhit.
The exact rational certificate checker and binary integrity/range/uniqueness checks passed.

The candidate binary encodes little-endian uint64 values; a_i is nibble i minus eight.

The result is a complete superset of the radius-eight compact residue.
The volume estimate did not prove completeness; the exact enclosure and full integer traversal did.
No zero path, infinite actual core, or full-law estimate is asserted by this enumeration.
The [complete SELF enumeration review](../../../audits/reviews/Yin_R_G0069_v1.md#lehmer-compact-enumeration-review) and [J G0028](../Yin_J_G0028/readme.md) check the complete finite superset; their scope excludes the following paths and exclusions.

## Exact path certificate

Optional path discovery consumes the preceding generated enumeration.
The verification-only command instead consumes the tracked adopted compact set and ancestry described above.
Its files are:

- [prepare_paths.py](prepare_paths.py), path-parameters.json (`mathematics/computations/outputs/Yin_J_G0026/path-parameters.json`): floating search-region data only.
- [Paths.cs](Paths.cs), [run_paths.ps1](run_paths.ps1): bounded reverse path discovery, allowing the full expanding strip rather than only K_8.
- paths-r8/discovery.json (`mathematics/computations/outputs/Yin_J_G0026/paths-r8/discovery.json`): uncapped discovery outcome and retained path parts.
- paths-r8/path-nodes-000.bin (`mathematics/computations/outputs/Yin_J_G0026/paths-r8/path-nodes-000.bin`), paths-r8/path-nodes-001.bin (`mathematics/computations/outputs/Yin_J_G0026/paths-r8/path-nodes-001.bin`): retained ancestry nodes.
- paths-r8/uncovered.bin (`mathematics/computations/outputs/Yin_J_G0026/paths-r8/uncovered.bin`), [classify_uncovered.py](classify_uncovered.py), uncovered-classification.json (`mathematics/computations/outputs/Yin_J_G0026/uncovered-classification.json`): seventy initially uncovered candidates and their exact exclusions from K_8.
- [verify_paths.py](verify_paths.py), path-verification.json (`mathematics/computations/outputs/Yin_J_G0026/path-verification.json`): separate integer recurrence, acyclic ancestry, full target coverage and exact exclusion checks.

```powershell
python -B mathematics/computations/programs/Yin_J_G0026/prepare_paths.py
& mathematics/computations/programs/Yin_J_G0026/run_paths.ps1
```

The reverse search visited 4003565 states below its 6000000-node cap and covered 797437 original candidates.
All seventy others were exactly excluded from actual K_8: sixty-eight by its strict neutral ball, two by its contracting strip.
The entire initial 797507-candidate superset is preserved.

The ancestry certificate has 1044588 nodes and maximum path length 25.
Each little-endian 13-byte record is `<QIB`: a uint64 state key, uint32 parent index, and byte digit code.
Coefficient a_i is the five-bit field i minus sixteen; the digit is the code minus one.
The verifier checks all integer edges, every strictly decreasing nonzero parent index, unique keys, full candidate coverage apart from the exact exclusions, and the final maximum depth.

All checks passed.
Therefore every actual K_8 state has a finite original-digit continuation to zero of at most 25 steps, conditional only on the separately checked completeness of the initial enumeration.
This path conclusion has its own scope in [C399 compact continuations](../../../claims/Yin_C_G0399_v1.md#lehmer-compact-exact-zero-continuations); the [complete SELF path review](../../../audits/reviews/Yin_R_G0069_v1.md#lehmer-path-and-coverage-review) and [J G0029](../Yin_J_G0029/readme.md) check this separate interface.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
