---
author: Yin
---
# Independent finite-path and exclusion checks for the Lehmer core

## Scope

Review the saved compact-candidate coverage, exact parent-edge paths and all excluded candidates for the original Lehmer input.
The separately assigned reviewer did not author those programs or certificates.
Earlier author explanations and component review findings were available.
This group supplies separately implemented review computation and no proof of the unrestricted Lehmer gap.

The responsible review finding is [D G0025](../../../audits/reviews/Yin_R_G0069_v1.md#lehmer-path-and-coverage-review).
Complete enumeration is reused from D24/J28 at its actual independently reproduced scope; this program owns the new finite-path/exclusion interface.

The current complete mathematical home is [C399](../../../claims/Yin_C_G0399_v1.md#lehmer-infinite-core-proof).
The linked original R records the complete proof review as SELF after its actual earlier substantive target inputs; independently implemented arithmetic retains its separate scope.

## Program and reproduction

[verify.py](verify.py) imports no author code.
It explicitly decodes little-endian packed files, checks every parent edge by the full polynomial identity t*a+digit-parent=a_9*P, proves acyclicity through strict parent-index decrease, recomputes maximum path length, compares full coverage sets, and independently re-isolates the trace roots to exclude every remaining candidate using Fraction interval embeddings.

From the repository root, use Python with its standard library:

```powershell
python -B mathematics/computations/programs/Yin_J_G0029/verify.py
```

verification.json (`mathematics/computations/outputs/Yin_J_G0029/verification.json`) records the successful result:1044588 distinct path nodes,797507 initial distinct targets,797437 covered targets,70 excluded targets and maximum depth25.
Independent rational intervals exclude68 states by rho^2>=64 and two by strict failure of the contracting strip.
The result retains every excluded coefficient vector and its reason.
All reads are from J26's tracked inputs/: compact-states.bin.gz, path-nodes.bin.gz and uncovered.bin.
The checker explicitly decompresses and decodes those fixed native objects; no discovery report or ignored author output is required.
It writes only its own output.

## Boundaries

The code reads the same saved paths and candidate set as the author, so it is independent verification of finite evidence, not independent discovery.
No floating discovery condition is a premise.
Its fresh root/interval construction imports no J22/J24/J26 interval helper.
It does not re-enumerate the compact superset or independently rerun the earlier normalized geometry.
Those proof and certificate interfaces are identified explicitly in D25; no count or script success alone proves them.
The output does not itself establish infinite reachability, a quantitative return-tail estimate or the unrestricted Lehmer gap.

## Reproducing reviewed runs

The historical review findings retain their original scope and relationship.
The selected native inputs are now tracked, so the documented verification-only commands replay those mathematical objects without rerunning discovery.
Generated verification reports remain local and replaceable.
Current repair checks establish the stated finite replay results, not a new independent-agent proof review or independent maintenance acceptance.
