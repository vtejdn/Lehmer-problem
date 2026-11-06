---
author: Yin
---

# Two exact iterations of the cubic mixed all-pass pullback

## Question and scope

This ordinary author computation for Yin tests only n=1 and n=2 in
\[
 P_0=P_L=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,
 \qquad
 P_{n+1}=g^{\deg P_n}P_n(g^*/g),
\]
where
\[
 g=z^3-z-1,\qquad g^*=1-z^2-z^3,\qquad R=g^*/g.
\]
The question is whether these two actual outputs produce multiple positive-measure irreducible factors, with multiplicities counted within each input.
The bottleneck-diagnosis delegate prepared and inspected the native computation for Yin; the main research agent supplied the construction and its exact normalization identities.
This is a compositional pullback, distinct from a delay polynomial z^N g+g* and from the [J140 mixed-delay family](../Yin_J_G0140/readme.md).
No n=3 calculation, general factor-count theorem, independent review or Claim adoption is included.

## Construction and exact checks

The polynomial g has discriminant -23, exactly one real root greater than one, and two conjugate roots whose common modulus is the reciprocal square root of that real root.
It therefore has both inside and outside roots.
The program checks gcd(g,g*)=1 exactly, so a root of a cleared pullback cannot arise from a common numerator-denominator zero.
The actual endpoint identities are
\[
 g(0)=-1,\quad g^*(0)=1,\quad
 g(1)=g^*(1)=-1,\quad g(-1)=-1,\quad g^*(-1)=1.
\]
Thus R(0)=R(infinity)=-1, R(1)=1 and R(-1)=-1.
For an even-degree reciprocal source P with P(1)=-1 and P(-1)=1, the cleared polynomial has actual degree 3 deg P, leading and constant coefficients 1, and the same values at 1 and -1.
Reversal exchanges g with g*, and reciprocity of P consequently preserves reciprocity of the output.
Induction gives degree 10 times 3^n, monicity, constant coefficient one and the two endpoint values for the stated recursion.

The additional exact identities are
\[
 g+g^*=-z(z+1),\qquad
 g^*-g=-(z-1)(2z^2+3z+2).
\]
For an actual output root beta, alpha=R(beta) is a preceding-layer root.
Both alpha+1 and alpha-1 are units, as are beta+1 and beta-1, because the respective monic source polynomials have unit values at both endpoints.
Evaluating the two displayed identities then shows that g(beta) and 2 beta^2+3 beta+2 are units as well.
These are identities about the actual roots and normalization, not a short-period conclusion.

In characteristic two,
\[
 \overline g=z^3+z+1,\qquad
 \overline {g^*}=z^3+z^2+1,
\]
which are distinct.
In particular (g+g*)/2 is not an integer polynomial.
The sufficient mod-two-palindromic step used for the preceding quadratic mixed test is therefore unavailable here; this does not exclude the existence of some other arithmetic auxiliary.

The native construction uses homogeneous Horner evaluation over ZZ.
At each requested input it checks the actual degree, leading and constant coefficients, coefficientwise reciprocity, and the two endpoint values before exact factorization.
SymPy factor_list supplies the complete irreducible factorization over ZZ.
The returned factors, with their multiplicities, are multiplied back exactly and compared with the original input.
The sum of all factor degrees with multiplicity must equal the original degree.
Every factor is checked to be monic with constant coefficient 1 or -1.
SymPy's exact is_cyclotomic predicate classifies the returned factors; for these unit factors, the accepted [Kronecker characterization](../../../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) identifies every noncyclotomic factor as positive in Mahler measure.
No irreducibility or cyclotomic verdict is inferred from floating-point roots.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Native exact construction, full ZZ factorization, classification, reconstruction checks and all-root numerical diagnostics. |
| [results.json](../../outputs/Yin_J_G0141/results.json) | Completed n=1,2 results with 50-digit root calculations, full original and factor coefficient arrays, multiplicities and every computed root. |
| [n1_results.json](../../outputs/Yin_J_G0141/n1_results.json) | Completed n=1 result from the same 50-digit calculation. |
| [n2_results.json](../../outputs/Yin_J_G0141/n2_results.json) | Completed n=2 precision check with 80-digit root calculations, retaining the same exact input and factorization. |

These generated files are replaceable local outputs in the responsible J output directory.
All inputs are constructed by the retained program; no previous output or external data is required.

## Reproduction

Both commands below were run successfully from the repository root, in this order.

```
python mathematics/computations/programs/Yin_J_G0141/main.py
python mathematics/computations/programs/Yin_J_G0141/main.py --n 2 --digits 80
```

The first command processes exactly n=1,2 using the default 50 decimal digits and writes the combined results.json plus the two per-input files.
The second independently reconstructs n=2, repeats its exact factorization and writes n2_results.json with 80-digit diagnostics, leaving the combined 50-digit results.json unchanged for comparison.
Thus the command order reproduces the currently recorded precision comparison without adding another iteration.
The program permits only n=1 or n=2 through its --n option.
Its output directory is derived from the actual containing J directory, independently of the caller's working directory.
Each completed file is published atomically, and numerical failure is recorded separately from a completed exact factorization.

The completed calculations used Python 3.14.3, SymPy 1.14.0, NumPy 2.4.4 and mpmath 1.3.0.
There is no randomness.
For each exact factor, NumPy roots computes all roots in double precision, and SymPy nroots computes all roots with the selected decimal precision and maxsteps=200.
Every computed root contributes log(max(1,abs(root))) with no exterior tolerance or cutoff.
Known cyclotomic factors would contribute exact zero to the classified total, while their unadjusted numerical root sums remain separately recorded; neither tested input has such a factor.
Both methods retain the complete root list and scaled polynomial residuals.
High-precision outputs also retain every individual positive logarithmic contribution.
The displayed measures and residuals have no certified error intervals, and precision agreement is not an interval certificate.

## Results and limits

Both assigned inputs completed full factorization over ZZ.
Each is itself irreducible, noncyclotomic, and appears with multiplicity one.
The exact cyclotomic degree is zero at both inputs, and the positive-factor count with multiplicity is one at both inputs.

| n | Actual degree | Cyclotomic degree | Positive-factor degrees | Positive-factor count | High-precision numerical total m | Double-precision numerical total m |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 30 | 0 | 30 | 1 | 2.1726446024448405073 | 2.1726446027452502 |
| 2 | 90 | 0 | 90 | 1 | 5.6695962331572073973 | 6.4742959546062471 |

Because each input has one positive factor, its minimum positive-factor measure is the same as its total measure.
The maximum absolute integer coefficient is 765 for n=1 and 62309463 for n=2.
The output retains all coefficients, including zeros, so the entire finite factorization is reproducible without a shortened polynomial presentation.

The n=2 double-precision measure is numerically unstable: it differs from the 50-digit result by approximately 0.8046997214490397.
This substantial discrepancy persists despite a small scaled polynomial residual, so that residual must not be treated as a forward root-accuracy certificate.
The additional 80-digit calculation returned all 90 roots and agreed with the 50-digit measure to an absolute difference of approximately 2.0123 times 10^-50.
The exact input coefficients and full factorization were also compared and agreed between those two precision levels.
This supports the high-precision value as an exploratory diagnostic, but supplies no certified numerical enclosure.
The n=1 double-precision and 50-digit measures differ by approximately 3.0041 times 10^-10; no additional n=1 precision run was needed for the observed finite conclusion.

The two actual inputs show no within-input production of multiple positive factors.
They establish no all-n irreducibility result, no asymptotic factor-count bound and no general measure estimate for the recursion.
The larger high-precision numerical total at n=2 is a finite observation, not a proved divergence theorem.
No n=3 calculation was performed.

## Inspection summary

The author delegate inspected the actual native program, both completed finite factorization classifications, exact reconstruction and degree checks, all-root counts and numerical precision comparison.
Both n=2 root lists were checked to contain 90 entries, and their exact input coefficients, factor coefficients and total measures were explicitly compared.
This is ordinary author computation and inspection, not an independent factorization certificate or formal review of a general theorem.
