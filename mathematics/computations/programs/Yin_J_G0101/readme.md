---
author: Yin
---
# Two separated phase sets close the buffered Lehmer shear screen

## Question and scope

This is one fixed-input certificate for the [two-set logarithmic correction](record.md#two-set-correction) under the continuing G0001 instruction.
It uses only the original Lehmer degree-ten input in [J97](../Yin_J_G0097/input.json), the accepted [C157v2 circle envelope](../../../claims/Yin_C_G0157_v2.md#statement) and the retained [J100 component sum](../Yin_J_G0100/readme.md#certified-results).
The quartic all-parameter exclusion is already complete and is not recomputed.

For T=E/G, certify unions A and B of entire normalized phase cells with T>=4 on A and T<=-4 on B.
Writing eta=min(mu(A),mu(B)), the direct two-set argument gives Delta=eta log9 for every real shear s.
Thus I_(s,q)>=log2+(S+Delta)/2 for every real s and q>0, where S is the existing certified J_G+J_V+log2.
This is a circle obstruction for the whole real parameter family, not an arithmetic assertion for noninteger parameters or a new original-root/Haar transfer theorem.

## Files

[main.py](main.py) owns the author certificate and [verify.py](verify.py) owns the separately authored interval verification.
The actual author result is results.json (`mathematics/computations/outputs/Yin_J_G0101/results.json`).
The completed independent result is verification.json (`mathematics/computations/outputs/Yin_J_G0101/verification.json`).
The explicitly required prior input is J100 author output (`mathematics/computations/outputs/Yin_J_G0100/results.json`); it is read, not recomputed.
Independent verification uses J100 independent output (`mathematics/computations/outputs/Yin_J_G0100/verification.json`) at its retained R524 scope.
Missing prior files are an execution limit; no alternate file or rounded-decimal substitution is allowed.
Generated evidence lives in the ignored output home and may be absent from a Git clone.

## Reproduction

From the repository root with python-flint0.9.0:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0101/main.py
    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0101/verify.py

The author command precedes verification because the checker certifies the retained cell-index witness and compares all four output quantities.
Both explicit J100 outputs and the original J97 input must be present; their producing programs are not rerun by J101.

The finite author domain is exactly8192 closed phase cells [k/8192,(k+1)/8192], k=0,...,8191, precision192 bits, thresholds+4 and-4, and a120-second subprocess cap.
The author constructs centered P at multiples2,3,5 directly from the original reciprocal coefficient vector using Arb cosine enclosures over each WHOLE cell.
Division by an interval containing zero is never used for certification.
Unclassified cells contribute zero measure to the certificate and cause no completeness claim about the sign sets.
Cell boundaries overlap only in finitely many Haar-null points.
The interval indices, exact counts, prior enclosing ball and final enclosing bounds are retained; output is marked complete only after every claimed sign, binding and positive margin passes.
No shear/weight grid, optimization, original norm or additional component integral is computed.

A preliminary interactive4096-midpoint double-precision observation suggested that separated ranges exist (threshold4 gave a minimum observed proportion0.154296875).
That observation chose the fixed certificate target only and supplies no certified interval measure or result.

The independent checker reconstructs the exact trace polynomial T_P(X)=X^5+X^4-5X^3-5X^2+4X+3 by triangular binomial elimination from the original P.
It checks the complete polynomial identities P(t)=t^5 T_P(t+t^(-1)), -72 t^30 E(t)=H23(t) and -30375 t^75 G(t)=H35(t), with their exact degrees, leading coefficients and supplied scalar denominators.
It evaluates T_P at 2cos(2pi k x), k=2,3,5, by interval Horner arithmetic, separately from the author's Fourier sum, and imports no author helper.
Every retained original cell is certified, permitting only dyadic subdivision of that same cell, at fixed256-bit precision, a maximum depth10 and a120-second subprocess cap.
This changes neither the witness unions nor their normalized measures.
The checker propagates the actual J100 independent screen ball, including its uncertainty, and checks exact input/normalization bindings and its agreement with the declared author-prior ball.
No component integral or J100 root isolation is recomputed.

<a id="certified-results"></a>
## Results and limits

The author calculation completed at192 bits over the declared8192 cells without precision escalation or refinement.
It certified2062 cells with T>4 and1206 cells with T<-4, hence eta=1206/8192=603/4096.
The enclosing correction is Delta=0.3234683642904639374567055067696694335461..., with S+Delta=0.2463614566100635271966822961558738655644...>0.
The resulting complete-parameter lower bound is I_(s,q)>=0.8163279088649770730155732695361135008577..., exceeding log2 by0.1231807283050317635983411480779369327822....
These decimals summarize the retained Arb enclosures; strict positivity follows from those enclosures, not decimal agreement.
The independent checker completed at256 bits and certified all2062 positive and1206 negative retained original cells.
Of the3268 certified original cells,3208 needed no refinement,58 were bisected, and2 were divided into16 pieces; the actual maximum depth was4, below the fixed cap10.
There were3433 interval evaluations including failed coarser attempts, with no s/q parameter-grid evaluations.
All four independently propagated scalar balls overlap the author's enclosing balls and are strictly positive.
The exact interval comparisons also certify the simpler rational statements I_(s,q)>0.8163279088 and I_(s,q)-log2>0.1231807283 for every real s and every positive q on this input.

The arrangement is non-blind: the separate reviewer was supplied the analytic reduction and reported counts, and read the author program and payload before writing the checker.
Independence concerns the separately constructed trace polynomial, exact numerator checks, interval expression and native verification code; both programs share python-flint0.9.0 and FLINT Arb interval/trigonometric primitives.
The accepted C157v2/R523 analytic interface and J100/R524 component certificate are reused at their recorded scopes, rather than claimed as fresh whole-proof or numerical reviews here.
The completed [R390 independent finding](../../../audits/reviews/Yin_R_G0390_v1.md#two-set-lehmer-finding) covers the full two-set reduction, all retained cells, source and scalar bindings, independent program and completed account.
This tests only the stated buffered family on one input, and cannot rule out different quadratic forms, different original polynomials or the unrestricted Lehmer objective.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0390_v1.md#two-set-lehmer-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0390_v1.md#two-set-lehmer-finding) |
