---
author: Yin
---

# Review of the strict finite moment bound and continuous radial mass

An agent outside the development of C345v5 reviewed the complete fixed claim for Yin on 2026-11-16T13:20 UTC.
The assignment supplied the fixed target and scope without proof-development discussion or a prior verdict.

<a id="strict-moment-review"></a>
## Saturation, Schur reconstruction and radial limits

The strict bound (1) holds simultaneously for all the asserted nonzero indices on a fixed positive-constant branch.
The lower bound for the continuous mass and the three necessary first-branch shapes have the stated probability normalization.

### Integer reflection and the rational extension

The coefficient comparison in L462v39 applies to positive and negative indices by conjugation symmetry, and its mass at zero is \(2j\).
With \(n=\lfloor b\sqrt q\rfloor\), its error is at most \(C_j(b^2+1/q)\), allowing \(2E+2\sqrt{jE}<1\) independently of the proposed saturation index \(L\).
In particular integer coefficients cannot exceed \(2j\) in absolute value.
If \(A(L)=2j\tau\), then \(2-2\tau\Re\int v^L\,d\lambda_q\le E/j\).
Multiplication by \(v^k\) preserves modulus for every integer \(k\), so Cauchy–Schwarz gives the shift error \(2\sqrt{jE}\) for the moments of \(2j\lambda_q\).
The two approximation errors leave a total strictly below one, proving integer equality wherever both indices are in the window.
Taking the starting index \(-k\) gives \(A(L-k)=\tau A(k)\), including the forced zero at \(k=L/2\) for even \(L\) and \(\tau=-1\).

The proposed numerator \(N\) of \(K_*\) satisfies \(z^LN(1/z)=\tau N(z)\) and the denominator \(W=1-\tau z^L\) satisfies \(z^LW(1/z)=-\tau W(z)\).
This proves the negative inversion identity as a rational identity, also when factors cancel.
The coefficient at zero of \(K_*\) is \(j\), the coefficient at \(L\) is \(2j\tau\), and the coefficient recurrence reproduces all positive indices through \(n\).
These facts cover \(L=1\) and both signs and account for the distinct convention \(A(0)=2j\).

### Analyticity and uniqueness

For either Taylor series the first two transforms give \(Y(0)=F(0)=q\) and \(F'(0)=q^2-1+j>0\).
The actual \(Y=f/D\) gives \(F=f/g\) exactly.
For this input \(g\) has one simple disk zero and no boundary zeros, while \(|qg|>|f|\) on the boundary.
Rouché gives a unique simple zero of \(f-qg\) in the disk, necessarily the origin since \(g(0)=1\) and \(f(0)=q\).
The numerator in \(S\) has a compensating \(z\) and \(qf(0)-g(0)=q^2-1\ne0\).
The circle modulus equality then proves that \(S\) is Schur by the maximum principle.

For the extension, direct substitution into the formula for \(Y_*\) gives \(Y_*(1/z)=z-z^2Y_*(z)\).
Substitution into the next two transforms gives \(F_*(1/z)F_*(z)=S_*(1/z)S_*(z)=1\).
The value and nonzero first derivative of \(F_*\) exclude identically vanishing denominators or an identically zero last numerator.
In particular \(S_*(0)=(q^2-1)/(q^2-1+j)\) after cancellation.
At every regular circle point, real coefficients and the last rational identity give \(|S_*|=1\).
A genuine zero or pole on the circle would contradict this modulus by approaching it along regular circle points, so reduction leaves neither.
As an algebraic check I verified all three transformed inversion identities symbolically for \(q=2,\ j=1\), both signs at \(L=1,2\), and \(\tau=-1\) at \(L=3\).
The examples \(L=2,\tau=1,A(1)=2\) and \(L=3,\tau=-1,A(1)=1,A(2)=-1\) each cancel a factor from the presentation of \(K_*\).

Write \(S_*=P_*/Q_*\) in reduced form.
The degrees of its numerator and denominator are at most \(L+6\) by the three displayed transforms, beginning with degree at most \(L\) for \(K_*\).
Multiplication by the finite Blaschke product \(\beta\) for all interior poles, each with its full multiplicity, gives a boundary-unimodular function holomorphic on the closed disk.
Each canceled pole now has a finite nonzero value.
The remaining interior zeros are consequently among the zeros of \(P_*\) with their original orders.
Removing their Blaschke factors leaves a nonvanishing function and inverse both bounded in modulus by one, hence a unimodular constant.
Thus \(S_*=\alpha/\beta\) with \(\deg\alpha\le L+6\), and the argument includes constant Blaschke products.

Agreement through degree \(n\) of the \(K\)'s gives \(Y-Y_*=O(z^{n+2})\), and \(1-zY\) is a unit at the origin, preserving this order for \(F-F_*\).
The exact difference in the last transform is
\[
 S-S_*=\frac{z(1-q^2)(F-F_*)}{(F-q)(F_*-q)} .
\]
Both denominator factors have a simple zero, so the resulting agreement with \(S_*\) is through degree \(n\).
Multiplication by \(\beta\) gives that same agreement between a Schur function \(S\beta\) and the finite product \(\alpha\).
Each ordinary Schur reduction at their common value of modulus less than one removes one order of agreement and one Blaschke degree.
A common unimodular constant term forces an identically constant Schur function, and the reductions invert uniquely.
Thus agreement through degree \(\deg\alpha\) suffices.
For \(L\le n/2\) and large \(n\), \(L+6\le n\), yielding \(S\beta=\alpha\).
The rational transformations invert over the rational function field since \(q^2\ne1\), so this forces \(K_q=K_*\).
The pole of \(K_q\) at \(1/\sigma\in(0,1)\) cannot occur in \(K_*\), contradicting saturation.
Taking \(c_j=b/3\) accommodates the floor in \(n\).

### Measure and the first branch

The weighted radial probability has the L462v36 limiting normalization \(\mu/j\), so the integer Fourier sequence belongs to \(2\mu\), a measure of mass \(2j\).
Passing to a further convergent subsequence of the branch coefficients preserves a given weak limit of the weighted radial measures.
The eventual periodic integer sequence extends to all indices with integer values, and its difference from the full Fourier sequence has finite support and integer values.
These give the atomic part on a finite root-of-unity group and the continuous trigonometric-polynomial part by Fourier uniqueness and the uniqueness of the decomposition of a measure.
Each mass is an integer, its Fourier coefficient at zero.
If the continuous part were zero, a common order of the finitely many atoms would yield a nonzero moment of full mass \(2j\).
The actual integer coefficients eventually agree at that fixed index and (1) excludes it.
The continuous mass is therefore at least one for \(2\mu\), or at least \(1/(2j)\) for the radial probability.

At \(j=1\), if the atomic mass is zero then the mean-two classification gives density \(2\) or \(2\pm2\cos(kt)\) before normalization.
If the atomic mass is one, the mass-one density has all nonconstant integer Fourier coefficients of modulus strictly below one and therefore is constant.
The symmetric probability on the atomic part has coefficients \(0,\pm1\).
The indices attaining modulus one form \(h\mathbb Z\) since their characters are constant on the support and this subgroup contains a common torsion order.
The sign at \(h\) determines the uniform measure on \(v^h=1\) or \(v^h=-1\) by Fourier uniqueness.
Division by the total mass two gives exactly the three alternatives in the statement, as necessary conditions on limits.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Strict moment finding](#strict-moment-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Strict moment finding](#strict-moment-review) | [C345v5 statement](../../claims/Yin_C_G0345_v5.md#statement) | Strict finite window, normalized continuous-mass lower bound and necessary shapes on branch one. |
| [Strict moment finding](#strict-moment-review) | [C345v5 reflection](../../claims/Yin_C_G0345_v5.md#reflection) | Uniformity for varying \(L\), both signs, negative indices, reflection and antisymmetric extension. |
| [Strict moment finding](#strict-moment-review) | [C345v5 reconstruction](../../claims/Yin_C_G0345_v5.md#schur) | Schur property, all inversion identities, reduced rational functions, interior and boundary cancellations, degree, Taylor order, uniqueness and pole contradiction. |
| [Strict moment finding](#strict-moment-review) | [C345v5 radial limits](../../claims/Yin_C_G0345_v5.md#radial-limits) | Integer component masses, normalization by \(2j\), removal of pure atomic limits and first-branch cases. |
| [Strict moment finding](#strict-moment-review) | [L462v39 finite comparison](../../ledger/Yin_L_G0462_v39.md#coefficient-window) | Uniform coefficient error over the two-sided square-root window, including the mass at zero. |
| [Strict moment finding](#strict-moment-review) | [L462v36 series normalization](../../ledger/Yin_L_G0462_v36.md#limit) | Series coefficients, reconstruction of the actual quotient and convergence at fixed indices. |
| [Strict moment finding](#strict-moment-review) | [L462v36 integer transform and pole](../../ledger/Yin_L_G0462_v36.md#periodic) | Eventual integer periodicity, finite root-of-unity support of the atomic part, finite Fourier difference and genuine interior pole. |
| [Strict moment finding](#strict-moment-review) | [L462v36 radial weights](../../ledger/Yin_L_G0462_v36.md#weights) | The radial probability limit \(\mu/j\) on a convergent branch subsequence. |
| [Strict moment finding](#strict-moment-review) | [L462v38 first-branch mass](../../ledger/Yin_L_G0462_v38.md#mass) | Continuous masses one and two, subgroup and sign of the remaining atomic probability. |
| [Strict moment finding](#strict-moment-review) | [C403v1 mean-two symbols](../../claims/Yin_C_G0403_v1.md#integer-mean-two-classification) | Nonnegative even trigonometric polynomial with integer coefficients and mean two. |
| [Strict moment finding](#strict-moment-review) | [L462v38 opposite sign](../../ledger/Yin_L_G0462_v38.md#opposite-sign) | Comparison with exact negative-constant realizations at their stated scope. |
