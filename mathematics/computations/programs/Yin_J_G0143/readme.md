---
author: Yin
---

# One exact dyadic defect input and its rational rotation

## Question and scope

This ordinary author computation for Yin tests only k=3 in the dyadic defect template
\[
 N=2^{k+1},\qquad r=2^{k-1}+1,\qquad
 C=(z^{2^k}-1)/(z^2+1),\quad D=z^N+1,\quad
 F=z^{2r}C^2+D^2.
\]
The intended parameter domain is k>=2, but this program constructs and factors only k=3.
The finite question is whether the first non-telescoping input is positive and whether it already produces several positive irreducible factors.
This is not a scan, a root approximation, an all-k factor theorem or a formal independent review.
The bottleneck-diagnosis delegate prepared this computation for Yin under the coordinating agent's bounded construction assignment.
The complete family argument, its zero-cost baseline and all-parameter Newton-sum positivity proof are retained in [L458 v4](../../../ledger/Yin_L_G0458_v4.md#dyadic-deletion-inputs).
This native record retains only the specified finite evidence.
The separate rotation control below uses the same k=3 input, preserves the original program and output, and factors the integer polynomial obtained from the symbolic rotation identity.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact ZZ construction, full factorization, input and output normalization checks, and coefficient product reconstruction for k=3 only. |
| [results.json](../../outputs/Yin_J_G0143/results.json) | Replaceable generated exact coefficients, factors, multiplicities, classifications, checks and software versions. |
| [rotation.py](rotation.py) | Exact rotation, full ZZ factorization of the degree-sixteen polynomial, trace return and real trace-root counts for the same k=3 input. |
| [rotation.json](../../outputs/Yin_J_G0143/rotation.json) | Replaceable generated rotation coefficients, factorization, trace polynomial, exact root counts and checks. |

All required input parameters and the explicit degree-28 comparison polynomial are embedded in the native program.
There are no external data files, random seeds, numerical precisions or tolerances.
The output directory is resolved from the actual containing J directory rather than the caller's working directory.
Generated output may be reproduced without any prior output.

## Reproduction

From the repository root, run

```
python mathematics/computations/programs/Yin_J_G0143/main.py
```

The retained program completed this command with Python 3.14.3 and SymPy 1.14.0.
It reproduced the initial interactive exact factorization over ZZ and completed all checks before publishing its results.
No k>3 or additional family input is included.
For the separate rotation control, run

```
python mathematics/computations/programs/Yin_J_G0143/rotation.py
```

This command also completed with Python 3.14.3 and SymPy 1.14.0.
It constructs its input directly and requires neither the earlier output nor execution of main.py.

## Results and limits

The exact input is N=16, r=5, C=z^6-z^4+z^2-1 and D=z^16+1.
The completed full factorization over ZZ gave
\[
 F=\Phi_{12}(z)H(z),\qquad\Phi_{12}=z^4-z^2+1,
\]
where
\[
 H=z^{28}+z^{26}-z^{22}-z^{20}+z^{18}+2z^{14}
     +z^{10}-z^8-z^6+z^2+1.
\]
Both returned multiplicities are one.
The degree-28 factor is irreducible and noncyclotomic according to the exact symbolic factorization and cyclotomic predicate.
Reconstruction of the complete coefficient polynomial, the explicit displayed product and the complete degree sum passed.
The input cyclotomic factorizations, coprimality, degree balance and reciprocal output were checked exactly.
The returned factor coefficient lists are complete, including every zero coefficient.
Thus this finite input has one positive irreducible factor and cyclotomic degree four, using the accepted [Kronecker characterization](../../../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) for the monic unit factors.
It establishes positivity of this input, not growth of the number of positive factors with k and not a numerical Mahler measure.
The symbolic-library irreducibility result is finite computational evidence, without a separate hand irreducibility proof or formal review.
The authored program, README and actual generated checks were inspected by their contributing author; this is an ordinary self-check.

The program also checks the complete-cost identity
\[
 (z^2+1)^2F(z)=G(z,z^{2^k}),\qquad
 G(z,w)=z^2w(w-1)^2+(z^2+1)^2(w^2+1)^2.
\]
The bivariate G has eleven nonzero terms and coefficient absolute sum sixteen.
The multiplier has zero measure and content one, so this identity preserves the full Mahler measure; its elementary upper bound is log(16).
That upper bound and the finite factorization do not imply a uniform positive lower bound on individual factors or growth of the positive-factor count as k increases.

<a id="rational-rotation-control"></a>
## Exact rotation and the degree-fourteen positive factor

Use n=2^k=8 here, so N=2n in the earlier notation, and put
\[
 Q_8(z)=z^{16}+1-z^5(z^6+z^4+z^2+1).
\]
The program verifies the exact identities
\[
 F(iz)=Q_8(z)Q_8(-z),\qquad
 (z^2-1)Q_8=z^{18}-z^{16}-z^{13}+z^5+z^2-1.
\]
Its complete factorization over ZZ is
\[
 Q_8=(z^2-z+1)R_{14},
\]
where
\[
 R_{14}=z^{14}+z^{13}-z^{11}-z^{10}-z^9-z^5-z^4-z^3+z+1.
\]
Both multiplicities are one, and the symbolic-library result identifies R_14 as irreducible and noncyclotomic.
The program also checks H(iz)=R_14(z)R_14(-z) for the earlier displayed degree-twenty-eight factor H.
Rotation preserves root moduli, and substitution z to -z preserves Mahler measure, so these exact products give
\[
                         m(R_{14})=m(H)/2=m(F)/2>0.
\]
This is an actual positive integer factor after rotation, with its full measure halved; it is not an arbitrarily small sequence or a repeated-halving result.
The all-k rotation mechanism and its limits are retained in [L458 v5](../../../ledger/Yin_L_G0458_v5.md#dyadic-rational-rotation).

The exact reciprocal trace identity is
\[
 R_{14}(z)=z^7T(z+z^{-1}),\qquad
 T(x)=x^7+x^6-7x^5-7x^4+13x^3+12x^2-4x-2.
\]
The program checks this coefficient identity, nonzero values at plus and minus two, and squarefreeness.
SymPy's exact real-root count returns zero roots below -2, four between -2 and 2, and one above 2, hence two nonreal trace roots.
Consequently R_14 has eight unit-circle roots, two positive real roots and four nonreal roots off the circle; it is not a Salem polynomial.
Indeed z+z^(-1) is real and lies in [-2,2] on the unit circle, and each trace root is lifted through z^2-xz+1=0.
Exactly three roots lie outside the circle: one positive real root and one nonreal conjugate pair.
The measure identity retains all three contributions, rather than only the positive real root.
No numerical Mahler value or approximate root calculation is used.

All exact rotation-control checks passed, including the complete factor product, earlier H return and the root-count partition.
The coordinating contributor prepared and read the saved program, README and actual output as an ordinary author check.
The source contributor separately read those saved materials and checked the rotation signs, trace recurrence, root geometry and complete measure identity without rerunning the computation.
The factorization and root counts are finite symbolic-library evidence, without a separate hand irreducibility certificate or an independent formal review.
