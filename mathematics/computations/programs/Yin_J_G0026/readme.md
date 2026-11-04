---
author: Yin
---
# Lehmer compact enumeration feasibility

## Native input availability

The selected enumeration and ancestry/path certificates are unavailable in this checkout and its selected local Git history, including the original797507-candidate list,1044588 ancestry nodes and70 exact exclusions.
The retained mathematical scope and old successful checks do not supply those missing native bytes.
The separate J28 enumeration and J29 continuation checks therefore cannot currently replay their original selected certificates.
Retain the indispensable original basis/enclosure and ancestry/coverage data at this group's tracked native input home when supplied; a different pruned path discovery is not identified as the original certificate.

## Scope

Estimate and, only if bounded and feasible, enumerate a certified finite superset of the radius-eight Lehmer compact residue.
Numerical count estimates are distinct from exact completeness certificates.

## Files and reproduction

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
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0026/prepare.py
& mathematics/computations/programs/Yin_J_G0026/run.ps1
python -B mathematics/computations/programs/Yin_J_G0026/verify_certificate.py
```

Preparation uses Python with SymPy solely to produce the integer LLL change of basis.
Its determinant and identity are checked exactly.
The certificate checker uses only the standard library.
The bounded traversal uses PowerShell `Add-Type` to compile the C# implementation.

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

Path discovery consumes the preceding enumeration.
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
python -B mathematics/computations/programs/Yin_J_G0026/classify_uncovered.py
python -B mathematics/computations/programs/Yin_J_G0026/verify_paths.py
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

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
