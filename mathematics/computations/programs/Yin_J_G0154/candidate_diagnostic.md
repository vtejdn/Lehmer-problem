---
author: Yin
---

# Full Mahler diagnostic of the unique failed-endpoint candidate

<a id="scope"></a>
## One fixed polynomial and its original constraints

[candidate_diagnostic.py](candidate_diagnostic.py) diagnoses only the degree-82 polynomial recorded in [the energy-six single-filter candidate](energy_six.md#single-candidate).
Its native input is exactly the saved list \((a_0,\ldots,a_{41})\), completed by reciprocity \(a_{82-i}=a_i\).
No generated JSON, new candidate search, new filter label or larger energy range is used.
The earlier strict-endpoint failure remains in force.
This additional calculation checks the original goal directly through factorization and full Mahler measure, even though the polynomial fails the selected chamber's endpoint test.

The program verifies all 83 integer coefficients, degree 82, reciprocal symmetry, leading and constant coefficients one, and \(P(-1)=-104\).
It recovers the trace polynomial through the exact identity
\[
 Q(t)=a_{41}+\sum_{j=1}^{41}a_{41+j}T_j(t),\qquad
                  P(z)=z^{41}Q(z+z^{-1}),
\]
and checks the lifted polynomial equals the input.
For \(B=B_{40}\), it sets \(C=Q-tB\), verifies \(\deg C=39\), and recovers the original moments from the top coefficients:
\[
 K=C_{39}=2,\qquad L=C_{38}-B_{39}K=0.
\]
The signed resultant and endpoint are
\[
 \operatorname{Res}(B,Q)=-5216,\qquad
                  -Q(-2)=P(-1)=-104.
\]
Using the exact integral inverse of \(D=B-T_{40}\) modulo \(B\), it also reconstructs \(h=D^{-1}C\bmod B\).
The cyclic moments agree with \((K,L)=(2,0)\), the absolute norm is 5216, and the endpoint parameter is \(U=-106\).
At 512-bit precision, Arb balls verify the original 31-positive, 9-negative cut at all 40 nodes.
These independent identities bind the diagnostic to the previously recorded candidate.

<a id="factorization"></a>
## Exact integer factorization

FLINT's exact factorization over the integers returns two monic irreducible factors, each with exponent one:
\[
                         P(z)=(z^2+1)R(z),
\]
where \(R\) has degree 80.
The program multiplies the exact factors back to \(P\) and checks that the degrees with multiplicity sum to 82.
The quadratic factor is \(\Phi_4(z)\), with exact Mahler measure one.
The degree-80 factor is not cyclotomic.

Write \(R(z)=\sum_{i=0}^{80}r_i z^i\).
Its complete coefficient list is specified by \(r_{80-i}=r_i\) and
\[
\begin{aligned}
 (r_0,\ldots,r_{40})={}&
 (1,1,3,3,1,4,4,5,4,5,6,6,5,7,6,8,\\
 &6,8,9,9,8,11,10,13,9,12,13,13,11,13,13,15,\\
 &11,15,15,15,14,17,16,18,14).
\end{aligned}
\]
Thus removing the cyclotomic factor leaves a single noncyclotomic factor whose full measure is the same as that of \(P\).

<a id="full-measure"></a>
## All-root Mahler enclosure

The computation uses 512-bit Arb complex balls for every root of each exact factor.
All root multiplicities are included, and the total checked root count is 82.
For a modulus ball strictly below one the contribution is exactly one.
For a modulus ball strictly above one the contribution is that ball.
For a ball meeting one, the union of that ball with the point one encloses the required value \(\max(1,|\alpha|)\).
No root is omitted from the product.
For the cyclotomic quadratic, the exact cyclotomic classification then replaces its root-product enclosure by the exact measure one.

| Exact factor | Degree | Multiplicity | Modulus certified below one | Modulus certified above one | Modulus ball meeting one |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(z^2+1\) | 2 | 1 | 0 | 0 | 2 |
| \(R\) | 80 | 1 | 3 | 3 | 74 |

The 74 balls in the last column for \(R\) are not classified as exact unit-circle roots by this diagnostic.
Their full contributions remain enclosed in the product.
The resulting measure enclosure has reported radius at most \(5.17\cdot10^{-151}\), and the program explicitly verifies the convenient strict decimal bounds
\[
\boxed{
 3.72242552293746802492690401570893
 <M(P)=M(R)<
 3.72242552293746802492690401570894.
}
\]
The logarithmic measure is enclosed near
\[
                 \log M(P)=1.31437547810589046031965077398209845\ldots.
\]
This is the complete Mahler product, including every root and its multiplicity, rather than only a maximum root modulus.

The full measure of this fixed polynomial is therefore well above one, and discarding \(\Phi_4\) does not reduce it.
The endpoint screen did not hide a near-one Mahler input in this particular candidate.
The exact endpoint remains negative, so this diagnostic does not change the candidate's rejection in the strict chamber or add a successful candidate to the energy-six run.
No claim about other candidates or arbitrary \(\varepsilon>0\) is made.

<a id="reproduction"></a>
## Reproduction and retained mathematical data

Run from the repository root with Python, python-flint, SymPy and NumPy:

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/candidate_diagnostic.py
~~~

The successful run used the existing Python 3.14.7 and python-flint 0.9.0 environment.
Factorization and all factor-root calculations took about 0.04 seconds after input reconstruction.
The output is `mathematics/computations/outputs/Yin_J_G0154/candidate_diagnostic_82.json`.
It retains the input polynomial, reconstructed \(Q,C,h\), moments and resultant, failed endpoint, exact factor coefficients and multiplicities, every root ball and its contribution, factor measures, full measure and logarithm, precision, and checked decimal bounds.
The native input and exact reconstruction suffice to regenerate the output.
The original energy-six source and description remain unchanged.
The [independent diagnostic finding](../../../audits/reviews/Yin_R_G1107_v17.md#candidate-diagnostic-review) checks the original candidate binding, exact factorization and complete all-root enclosure.
