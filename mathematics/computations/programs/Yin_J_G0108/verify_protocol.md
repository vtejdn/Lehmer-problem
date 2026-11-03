# Independent verification protocol

The angular_envelope_review agent independently implements the complete J108 verifier.
Root authored the analytic finite protocol, interpolation program and manual prime3 obstruction; this reviewer supplied no proof repair or author-program step.
The verification is nonblind: the author source/schema, reported zero-solution result and manual reduction were visible before execution.
The complete symbolic reconstruction does not import or call any author mathematical helper.
Both calculations use standard Python exact integers on the same Windows host; this is not independent arithmetic hardware or formal proof.
Only the Windows Job/working-set launcher is copied operationally from the author program's already reused J107 guard.

## Fixed mathematical batch

The fixed inputs are exactly inputs.json.
The variables are the actual entries at(0,2),(3,4),(4,6), not additive increments from their starting values0,2,0.
The verifier expands ALL5040 signed permutations of the full7-by7 pencil in Z[t,x,y,z].
It preserves every coefficient of t^0,...,t^7, checks full reciprocity and unit endpoints, and compares all three nontrivial coefficient polynomials with the author's payload.
For each of the27 integer representatives on{0,1,2}^3 it independently expands the scalar univariate pencil by permutations, checks agreement with formal evaluation, and compares every complete polynomial and prime3 residual.
Formal polynomial differentiation computes all27 full Jacobians over F3, including any roots, using a separate six-term3-by3 determinant.
The same fixed batch checks the supplied manual sum identity as an exact coefficient-polynomial identity over F3 and checks its two surviving a-equation representatives and their b residuals.
No other prime, modulus, matrix-entry set, coefficient box or elimination method is selected.
The author result file is read only after the formal polynomial and all27 scalar/Jacobian payloads have been independently computed in the worker.

## Resource and preservation boundary

One independent batch has an aggregate30-second wall cap,256MiB worker commit and hard-working-set caps, and32MiB complete verifier output cap.
The small parent monitor is excluded only from worker memory.
The parent timer includes guard setup, worker input/output/comparison, payload serialization/publication and preservation IO; a late preservation check reports failure rather than a complete accepted batch.
The worker reserves64KiB for execution status, checks the deadline before and after payload publication, and has no unguarded fallback.
A failed or capped execution is incomplete, and an existing verifier output directory is never overwritten implicitly.
No mathematical run occurred while preparing or syntax-parsing this verifier.

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0108/verify.py
```

The actual output belongs to mathematics/computations/outputs/Yin_J_G0108/verifier/.
The full symbolic polynomial, every integer pencil/residual, all27 Jacobians and exact comparison results are retained in verification.json; execution.json owns the resource outcome.
Whole fixed J review follows the actual completed verification and final README, rather than being inferred prospectively from this protocol.

## Actual completed independent batch

The single declared verifier batch completed successfully within all caps.
It reconstructed the entire symbolic pencil from5040 formal signed permutations and separately checked all27 integer pencils, all27 residual triples and all27 formal Jacobians modulo3.
Every author coefficient and evaluation payload agreed exactly; there are zero prime3 solutions and zero exact integer target points in the cube.
The supplied manual sum identity over F3 also agreed coefficientwise, and its two intermediate survivors are(0,2,0) and(1,1,1), with respective b+1 residuals2 and1.
This verification makes the complete prime3 obstruction apply to every integer point of this fixed affine slice; it does not expand the slice or exclude all rank-seven matrices.

The actual parent wall observation was0.25 seconds, peak worker commit12283904 bytes and peak job commit14409728 bytes.
The complete verifier payload and execution-status files total25475 bytes, below the32MiB output limit.
No guard failure, second batch, higher modulus, additional prime, author-helper import or scope-changing fallback occurred.
The nonblind/shared-Python limits stated above remain in force.
The actual files are verification.json (`mathematics/computations/outputs/Yin_J_G0108/verifier/verification.json`) and execution.json (`mathematics/computations/outputs/Yin_J_G0108/verifier/execution.json`).
