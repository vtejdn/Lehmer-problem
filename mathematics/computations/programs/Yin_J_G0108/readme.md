---
author: Yin
---
# Exact three-entry coefficient slice and its first odd-prime test

## Question and scope

This protocol continues the two-adic realization toward the still-open integral problem.
Its original fixed input is [L412](../../../ledger/Yin_L_G0412_v1.md#two-adic-complete-realization), with the actual [R419 review](../../../audits/reviews/Yin_R_G0419_v1.md#two-adic-rank-seven-whole-independent-finding).
The current complete analytic result is [C525](../../../claims/Yin_C_G0525_v1.md#statement), adopted with [R732](../../../audits/reviews/Yin_R_G0732_v1.md#current-c533-v1-complete-independent-finding).
Keep the complete target T=(t+1)Phi6 P4 and all entries of the first J107 integer matrix U_* fixed EXCEPT positions(0,2),(3,4),(4,6).
The three variables x,y,z are the ACTUAL entries at those positions, with starting values0,2,0; they are not additive corrections.
This program derives their complete integer coefficient map and tests exactly prime3, which divides the nonzero reduced endpoint Phi6(-1)P4(-1)=9.
It does not assert a general odd-prime obstruction or change the rank-seven target.
Root authors this finite protocol and its calculation.

<a id="three-entry-exact-protocol"></a>
## Exact complete interpolation and declared finite domain

For U(x,y,z), write det(tU+U^t)=[1,a,b,c,c,b,a,1] in ascending order.
Every one of x,y,z occurs in precisely two matrix entries of the pencil, so each determinant coefficient has degree at most2 in EACH variable, without a total-degree assumption.
Consequently the27 integer evaluations on{0,1,2}^3 determine a,b,c EXACTLY over Q by the tensor product of the three degree-two Lagrange bases.
The bases are(1-x)(2-x)/2, x(2-x), x(x-1)/2, and likewise for y,z.
The actual determinant has integer polynomial coefficients; reconstruction checks that every final coefficient is integral.
These bounds close the entire three-parameter symbolic domain, not merely a bounded integer search.
All evaluated complete degree-seven polynomials and every reconstructed monomial are retained.

The author uses exact Bareiss determinants at t=0,...,7 and rational finite-difference interpolation to obtain each entire pencil.
The independent verifier must reconstruct the full symbolic polynomial by a different exact method, without the author's interpolation or mathematical helpers, and check every native coefficient and27 evaluation payloads.
For example full signed permutation expansion with formal x,y,z exponents provides that independent method.
The complete target triple is(-1,-1,0).

The same27 representatives exhaust all x,y,z modulo3.
Retain EVERY solution of the full target congruence, and the complete residual triple for every excluded representative.
At any solution compute and retain the formal3-by3 coefficient Jacobian modulo3 and its determinant, distinguishing singular from nonsingular starting points.
No higher3-power lift or exact integer existence follows solely from singular modular compatibility.
A nonsingular local implication would require its own written argument rather than an unrecorded scan.
If no residue solution exists, the resulting obstruction applies to EVERY integer point of this SPECIFIC affine slice, including the L412 modulo4 neighborhood, but not to all rank-seven upper matrices.
If an evaluated integer representative happens to give the full target exactly, retain that actual matrix and its entire negative-absolute and literal-cover polynomials; no factor or cost may be discarded.
If none is exact, the finite cube alone is not an integer nonexistence certificate.

One author batch and one independent batch each have an aggregate30-second wall cap,256MiB worker commit and hard-working-set caps, and32MiB complete output cap including serialization.
The small parent monitor is excluded from worker memory.
The already corrected Windows Job mechanism is reused operationally from J107, with these explicitly smaller caps and no unguarded fallback.
A failed or capped batch is incomplete.
No second odd prime, modulus9, larger variable set, coefficient box or Groebner/elimination calculation is selected.
The complete exact coefficient map may support a later separately written analytic argument; none is presumed now.

## Files and reproduction

The actual [inputs.json](inputs.json) fixes the matrix, actual-entry variables, target,27-point domain, prime3 and resource caps.
The [main.py](main.py) reuses J107 exact Bareiss/interpolation helpers as author code, not as independent evidence.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0108/main.py
```
The default output is this actual J's home under mathematics/computations/outputs/.
No prior generated result is required; the actual starting matrix is supplied explicitly in inputs.json and linked to the independently verified L412/J107 source above.
Arithmetic is integer and rational only, without floating-point roots or numerical tolerances.

## Results and limits

The declared first author batch completed within its unchanged30-second,256MiB and32MiB caps.
Its exact whole coefficient map and all27 prime3 residuals have NO solution; the separately authored full formal-determinant verification has now completed and agrees.
The scope remains one exact three-entry affine family and one complete prime3 residue test.
The accepted two-adic existence and the original integral/absolute-cost obligations remain distinct.

<a id="three-entry-author-results"></a>
## Exact author map and a short prime-three obstruction

The complete author result (`mathematics/computations/outputs/Yin_J_G0108/author/result.json`) and guard outcome (`mathematics/computations/outputs/Yin_J_G0108/author/execution.json`) are retained.
The successful author batch took0.172 seconds with peak worker commit11096064 bytes and peak job commit13209600 bytes.
There was no cap failure, rerun, other prime or higher-modulus calculation.
No evaluated integer cube point has the exact target, and no residue point modulo3 has its full congruence.
The full symbolic map, not a fitted approximation, is

    a=-1-z^2+2y-yz-y^2-x-xz+xyz-x^2,
    b=-1+z+2y-yz-2y^2+2xz+xz^2-xy+xyz
                            +x^2z^2-x^2y+x^2y^2,
    c=-2-2z+3z^2+y+2yz-2y^2+x-xz-xz^2-xy+xyz
                            +x^2-x^2z^2+x^2y+2x^2y^2.

The required complete coefficient equations are a=-1,b=-1,c=0.
Here is an additional short AUTHOR algebraic check of their modulo3 inconsistency, derived from that exact map and not a new native execution.
Work throughout F3 and define epsilon(z)=1 if z=1 and0 if z=0 or2.
The sum of the three residuals simplifies to

    a+b+c+2 = 1-z+2z^2-y+y^2+xy
             =1+epsilon(z)-y+y^2+xy.

For y=0 this cannot vanish.
For y=1 its vanishing forces x=2-epsilon(z), and for y=2 it forces x=epsilon(z).
Substitution into a+1 leaves only the two candidates

    (x,y,z)=(1,1,1) or(0,2,0).

At those two points b+1 equals respectively1 and2 modulo3, so neither solves the target equations.
This proves a modulo3 obstruction on the ENTIRE integer affine slice, using the exact symbolic coefficient map; the independent full formal-determinant reconstruction has now checked that computational premise and this simplification.

Consequently the specified18 fixed entries cannot be retained while choosing the other three as integers to realize the full target, even though the same slice has the accepted L412 solution over Z2.
The obstruction also rules out a solution over Z3 in this slice.
It does not exclude a rational point with a denominator divisible by3, an integer matrix with additional entries changed, or any unrestricted rank-seven realization.
No conclusion about the other J107 target, complete companion optimization or Mahler gap follows.
The original L412 two-adic theorem remains correct; a local solution at one prime does not supply the integral construction.

The new map and this short all-parameter inference have completed the independent native checks below; the complete fixed whole review is linked below and remains distinct from the native verification.

<a id="three-entry-independent-results"></a>
## Independent complete symbolic verification

The independent [verify.py](verify.py) and [verification protocol](verify_protocol.md) implement a full5040-permutation FORMAL determinant with x,y,z exponents, independent of the author interpolation helpers.
A separate scalar permutation expansion reconstructs all27 entire integer pencils.
The complete symbolic coefficient map, every integer pencil/residual, all27 formal Jacobians, the empty prime3 solution set and the short displayed F3 identity/remaining candidates agree exactly.
The complete independent payload (`mathematics/computations/outputs/Yin_J_G0108/verifier/verification.json`) and guard outcome (`mathematics/computations/outputs/Yin_J_G0108/verifier/execution.json`) are retained.
The independent batch ran once in0.25 seconds, with peak worker commit12283904 bytes and peak job commit14409728 bytes, within the same30-second/256MiB/32MiB caps.
No rerun, cap relaxation, modulus9 or additional prime test occurred.
The original and independent implementations share Python integer arithmetic and the Windows host and were nonblind; the verifier imports no author mathematical helper.
Only the operational guard mechanism is reused.
No independent runtime audit or formal proof is claimed.

From the repository root after the complete author run:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0108/verify.py
```

The positive exact-integer-cube cost branch had no input because there were no such witnesses.
Its empty output is not evidence of unrestricted integer nonexistence; that stated all-slice nonexistence follows from the COMPLETE prime3 obstruction.
The complete [R422 whole independent finding](../../../audits/reviews/Yin_R_G0422_v1.md#three-entry-j108-whole-independent-finding) binds the final symbolic map, all native payloads and the all-integer fixed-slice inference.
Root adopted that exact reviewed scope in S1/S3/S6.

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
| `author/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0422_v1.md#three-entry-j108-whole-independent-finding) |
| `author/result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0422_v1.md#three-entry-j108-whole-independent-finding) |
| `verifier/execution.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0422_v1.md#three-entry-j108-whole-independent-finding) |
| `verifier/verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0422_v1.md#three-entry-j108-whole-independent-finding) |
