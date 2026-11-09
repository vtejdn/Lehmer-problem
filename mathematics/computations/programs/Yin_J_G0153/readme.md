---
author: Yin
---

# Complete spectra of rotating symplectic shear products

This computation tests the [coupled rotating-shear candidate](../../../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law) in Yin's [G0001 counterexample investigation](../../../tasks/Yin_T_G0001_v1.md#contract).
It compares the complete logarithmic Mahler cost with the largest root modulus and the number of expanding roots.

<a id="finite-sample"></a>
## Matrices and the exact finite scope

For each \(g\in\{12,24,48\}\), \(k\in\{2,4,8\}\) and sample index \(s\in\{0,\ldots,7\}\), Python's pseudorandom generator uses seed \(196830000+10000g+100k+s\).
Choose \(k\) distinct sites, sort them, and independently shuffle two lists containing \(k/2\) signs of each kind.
Both shears use this same site set, as in the proposed law.
The program records the actual sites and both sign lists.
With subscripts taken modulo \(g\), put
\[
 D=\sum_i\epsilon_i(e_i-e_{i+1})(e_i-e_{i+1})^t,\qquad
 E=\sum_i\eta_i(e_i+e_{i+1})(e_i+e_{i+1})^t.
\]
If \(S\) is the cyclic permutation matrix, the tested matrix is
\[
 A=\begin{pmatrix}S&0\\0&S\end{pmatrix}
   \begin{pmatrix}I&D\\0&I\end{pmatrix}
   \begin{pmatrix}I&0\\E&I\end{pmatrix}.
\]
The symmetry of \(D,E\) and orthogonality of \(S\) give \(A^tJA=J\) for the standard integral symplectic form.
Every sampled matrix is also checked against this exact integer identity.
The matrix entries and intermediate products in this finite range fit within the signed 64-bit integer representation used to construct them.
FLINT computes its exact monic integer characteristic polynomial, and the program checks its reciprocal coefficient list.
The sample consists of 72 labelled parameter choices, with repeated polynomials allowed.

<a id="full-measures"></a>
## Full root products and finite results

For all 72 characteristic polynomials, FLINT at 256-bit precision encloses every complex root with multiplicity.
The product uses \(\max(1,|\lambda|)\) for every root and checks the total multiplicity \(2g\) and a final measure radius below \(10^{-30}\).
Clipping both endpoints of each nonnegative radius enclosure at one preserves enclosure of that factor.
For every final ball that does not prove \(M>1\), exact factorization over \(\mathbb Z\) verifies that every irreducible factor is cyclotomic, giving \(M=1\) exactly.
The exploratory NumPy spectra select an ordering for comparison, while interval separation verifies the reported strictly positive minimum against all other positive outputs.

Exactly 24 sampled outputs have \(M=1\), and 48 have \(M>1\).
The smallest strictly positive output occurs at \((g,k,s)=(12,8,6)\), with
\[
 1.75487766624669<M(P)<1.75487766624670.
\]
Its polynomial is
\[
 \begin{aligned}
 P(t)={}&t^{24}+2t^{22}-t^{20}-7t^{18}-6t^{16}+5t^{14}+12t^{12}\\
        &+5t^{10}-6t^8-7t^6-t^4+2t^2+1.
 \end{aligned}
\]
Its numerical house is about \(1.15096393\), with six roots numerically outside the unit circle.
The complete measure is established by the full ball product above.
The numerical near-zero costs include a value around \(1.85\cdot10^{-5}\) caused by multiple unit-circle roots, which the exact cyclotomic test resolves to zero.
For the uniform law on these 72 labelled inputs, every strict shell below the displayed minimum has probability zero.
The unbounded random-matrix family and a possible positive probability for every arbitrarily small strict shell remain unresolved.

<a id="factor-diagnostics"></a>
## Exact irreducible-factor diagnostics

[factor_diagnostics.py](factor_diagnostics.py) factors the complete characteristic polynomials for the same 72 labelled inputs over the integers.
It checks that the factors with their multiplicities multiply back to the original polynomial.
An irreducible factor is classified as reciprocal when its reversed coefficient list agrees with its coefficient list up to sign.
Cyclotomic classification is exact.
Since the full polynomials are monic with constant one, Kronecker's theorem makes the presence of a noncyclotomic factor equivalent to strictly positive whole Mahler measure.

Of the 48 positive outputs, eight contain a nonreciprocal noncyclotomic factor and 40 have only reciprocal noncyclotomic factors.
The eight labels \((g,k,s)\) are
\[
 (12,4,3),\ (12,8,6),\ (24,4,0),\ (24,4,5),\ (24,8,1),
 (48,4,3),\ (48,4,5),\ (48,8,4).
\]
At the previously certified minimum \((12,8,6)\), the exact factorization is
\[
 P(t)=(t-1)^2(t+1)^2(t^2-t+1)(t^2+t+1)(t^2+1)^2
       (t^6-t^2-1)(t^6+t^4-1).
\]
The last two factors are reciprocal to each other up to sign and are obtained by substituting \(t^2\) in \(t^3-t-1\) and its reciprocal.
The cubic has one real root \(\vartheta>1\) and two conjugate roots of modulus \(\vartheta^{-1/2}<1\), since its discriminant is \(-23\) and its root product is one.
Substitution by \(t^2\) and reversal each preserve Mahler measure, so \(M(P)=\vartheta^2\) exactly.
Thus this minimum does not exhibit a small whole measure hidden by the root-product calculation.

The labels \((12,2,2)\), \((24,2,0)\), \((24,2,7)\) and \((48,2,1)\) each have one noncyclotomic irreducible factor, reciprocal and of respective degrees \(20,44,44,92\).
All their other factors are cyclotomic.
Consequently a universal decomposition of this ensemble into nonreciprocal factor pairs is already contradicted within the finite window.
These factor diagnostics neither find a shrinking sequence nor exclude one in the unbounded ensemble.

<a id="replay"></a>
## Reproduction

Run [rotating_shears.py](rotating_shears.py) with Python, NumPy, SymPy and python-flint.
The executed versions were Python 3.14.7, NumPy 2.5.4, SymPy 1.14.0 and python-flint 0.9.0.

~~~text
python -B mathematics/computations/programs/Yin_J_G0153/rotating_shears.py
~~~

The reproducible output is `mathematics/computations/outputs/Yin_J_G0153/rotating_shears.json`.
It contains every sampled input, numerical summary, exact characteristic polynomial and certified measure ball.
It is regenerated by the program and remains local.

Run the exact factor diagnostics with the same dependencies:

~~~text
python -B mathematics/computations/programs/Yin_J_G0153/factor_diagnostics.py --recompute
~~~

The executed `--recompute` path reconstructs all 72 matrices from the original seeded generator and recomputes every exact characteristic polynomial before factorization.
Without that option the program reads `rotating_shears.json` when it exists, checks all labels and seeded sites/signs, and otherwise uses the same exact regeneration fallback.
It writes the complete factor coefficient lists and the finite summary to `mathematics/computations/outputs/Yin_J_G0153/factor_diagnostics.json`.
The factorization computation supplies no new numerical root certification; the whole-measure balls remain the responsibility of the original program.
