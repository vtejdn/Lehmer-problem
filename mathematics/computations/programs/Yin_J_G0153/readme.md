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

<a id="reciprocal-factor-measures"></a>
## Complete measures of the split reciprocal factors

The existing 72-label factor inventory has 24 cyclotomic outputs, 37 outputs with exactly one noncyclotomic reciprocal irreducible factor of multiplicity one, eight outputs with two nonreciprocal noncyclotomic factors, and three outputs with two reciprocal noncyclotomic factors.
The complete measure of a reducible parent alone does not bound each positive factor from below.
The separate [reciprocal_factor_measures.py](reciprocal_factor_measures.py) therefore certifies all six positive factors of those last three fixed inputs.
It regenerates their original seeded sites and sign lists, constructs the full integer matrices with the complete \(DE\) term, and computes the exact characteristic polynomials.
The regenerated inputs, full coefficients and exact factor lists agree with the retained original records.
No new labels are sampled.

| Original label \((g,k,s)\) | Factor degree | Certified complete factor measure |
| --- | --- | --- |
| \((12,8,3)\) | 8 | \(2.36920540709246<M<2.36920540709247\) |
| \((12,8,3)\) | 12 | \(2.82838463404120<M<2.82838463404121\) |
| \((48,8,2)\) | 40, 40 | Each lies in \((3.20572542701166,3.20572542701167)\). |
| \((48,8,6)\) | 40, 40 | Each lies in \((3.20572542701166,3.20572542701167)\). |

Each listed factor has multiplicity one.
The [J156 evaluator](../Yin_J_G0156/sampler.py) retains every root and multiplicity using exact factorization and 128-bit Arb enclosures, with unit-circle intersections contributing an enclosure of \(\max(1,|\alpha|)\).
The factor product and total root counts are checked, and exact rational comparisons put the saved dyadic measure endpoints strictly inside the displayed decimal bounds.
All six complete factor measures exceed \(6/5\).
The eight nonreciprocal pairs fall under the [Smyth bound at its retained source depth](../../../audits/literature/Smy08/Yin_U002.md#smy08-u002), while the sole positive factor of each of the other 37 outputs has the already certified complete parent measure.
Together with the original full-measure and factor diagnostics, this closes the proper-factor question below \(6/5\) for these 72 labelled inputs only.
It supplies no factor gap for the unbounded rotating-shear ensemble, the fixed-symbol theorem or the cluster-word theorems.

This additional finite diagnostic has ordinary author checking; it is outside the separate independent review of the twenty-four-cluster control below.
It uses Python 3.14.7 and python-flint 0.9.0, with the standard library and the explicitly named cross-J evaluator.
The generation command requires no previous generated output:

~~~text
python -B mathematics/computations/programs/Yin_J_G0153/reciprocal_factor_measures.py
~~~

The replaceable [reciprocal_factor_measures.json](../../outputs/Yin_J_G0153/reciprocal_factor_measures.json) retains all three original inputs, complete parent coefficients, every factor, all noncyclotomic root balls, complete parent and factor measure intervals, and threshold decisions.
It is published atomically only after all three fixed inputs have been processed successfully.

<a id="cluster-word-control"></a>
## Complete cost of the twenty-four-cluster trace control

The separate [cluster_word_control.py](cluster_word_control.py) evaluates exactly the globally balanced word in [C889 v2](../../../claims/Yin_C_G0889_v2.md#remaining-type-control), at \(g=72\).
Its twenty-four three-site clusters occupy the full 72 sites, with an inactive connecting edge between consecutive supports.
The matrix product, in the displayed order, is
\[
W(t)=E_+E_-E_+^2E_-^7E_+^5E_-^4E_+^4,\qquad
E_s(t)=\begin{pmatrix}t^2-3&s(2-t)\\-s(2+t)&1\end{pmatrix}.
\]
The physical cyclic cluster list is the reverse of this matrix-product list.
For a letter of sign \(s\), the original edge signs are \((a,b,c,d)=(s,s,-s,s)\).
There are twelve letters of each sign, so both original sign sums are zero.
This input tests the whole cost of a word whose trace enters \((-2,2)\); that local trace property does not assert small complete Mahler measure.

The program multiplies the two-by-two matrices over \(\mathbb Z[t]\), verifies \(T(2)=2\) and \(T\bmod(t^2-3)=-2\), and lifts their degree-48 trace to
\[
P(z)=z^{144}-z^{72}T(z+z^{-1})+1.
\]
It separately constructs the original 144-by-144 integral rotating-shear matrix, including \(DE\), from all 48 signed active edges.
Its exact characteristic polynomial agrees coefficient by coefficient with the trace lift.
The input is monic, reciprocal and has constant coefficient one.
No approximate matrix, numerical root screen or selected factor replaces this complete input.

The completed full-polynomial evaluation uses the [J156 evaluator](../Yin_J_G0156/sampler.py), at its recorded [implementation-review scope](../../../audits/reviews/Yin_R_G1111_v1.md#sampler-implementation-review), with exact FLINT factorization and 128-bit Arb root balls.
The factor product is checked, every factor multiplicity is retained, and the total root count is 144.
The resulting complete measure satisfies
\[
47.97469677926936<M(P)<47.97469677926937.
\]
The exact dyadic enclosure is
\[
\left[
255077240193189093249803440066446285365\,2^{-122},
255077240193189093249803440066446285945\,2^{-122}
\right],
\]
whose endpoints lie strictly inside the displayed rational decimal bounds.
The exact factorization is
\[
P(z)=(z-1)^2(z+1)^2(z^4+1)^2F_{132}(z),
\]
where the factorization implementation returns one irreducible noncyclotomic factor \(F_{132}\) of degree 132 and multiplicity one.
All other factors are cyclotomic, so the complete measure is also the measure of this sole noncyclotomic factor.
Irreducibility relies on the trusted FLINT factorization implementation in addition to the independently checkable factor product.
This one input therefore supplies neither a value below \(6/5\) nor a proper rational factor that could yield one.
The finding does not exclude other words, lengths or globally balanced cluster mixtures.

The separate [complete independent finding](../../../audits/reviews/Yin_R_G1115_v2.md#cluster-word-control-review) checks this actual input, native program and certificate.
Its [independent checker](checks/cluster_word_independent.py) imports neither the author program nor the J156 evaluator: it rebuilds the trace in a different formal variable and the original matrix by its action on basis vectors, then verifies every factor and all 132 noncyclotomic root boxes with fresh 256-bit enclosures.
The complete rational product lies strictly inside the saved author interval, and the total count includes all 144 roots with multiplicity.
FLINT characteristic-polynomial computation and irreducible factorization, and Arb root isolation and ball arithmetic, remain trusted backend implementations at the stated review scope.
This review covers neither the old 72 sampled inputs nor their separate six-factor diagnostic above.
It uses Python 3.14.7 and python-flint 0.9.0, with the standard library and the explicitly named cross-J evaluator.
It does not use NumPy, SymPy, a random seed or earlier generated output.
Run from the repository root with python-flint available:

~~~text
python -B mathematics/computations/programs/Yin_J_G0153/cluster_word_control.py
~~~

The replaceable [cluster_word_control.json](../../outputs/Yin_J_G0153/cluster_word_control.json) retains the actual sign lists, full trace and characteristic coefficients, exact factor coefficients, all noncyclotomic root balls, multiplicities, dyadic measure intervals and threshold decisions.
It is regenerated from the fixed program inputs and published atomically only after the complete calculation succeeds.
After generating that comparison input, run the separate verification command:

~~~text
python -B mathematics/computations/programs/Yin_J_G0153/checks/cluster_word_independent.py
~~~

The checker uses the existing python-flint installation at J156 outputs/packages and writes [cluster_word_independent.json](../../outputs/Yin_J_G0153/cluster_word_independent.json).
Its exact scope, independent arrangement and limitations belong to the linked finding.
