---
author: Yin
---

# Gaussian one-kick cyclic norm polynomials

## Question and finite scope

This bounded experiment serves the unrestricted [G0001 contract](../../../tasks/Yin_T_G0001_v1.md#contract), looking for a complete integer Mahler measure in the strict interval (1,6/5).
It tests only m=1,...,12 and the fixed central parameter b=1 in the explicit Gaussian polynomial
\[
g_m=(z^m-1)(z^2+(1-i)z-1)+2z,
\qquad P_m=g_m\overline{g_m}.
\]
The conjugation acts on coefficients, so P_m is a monic integer polynomial of degree 2m+4 with constant coefficient one.
The entire norm polynomial, every factor and every multiplicity must be included.
This is a finite discriminator of a concrete one-kick cyclic family, not an assumption that unitary groups supply arbitrarily small measure.
The completed author run returns one neutral input at \(m=1\) and eleven positive inputs, all strictly above \(6/5\).
There is no hit in the requested strict interval.

<a id="polynomial-input"></a>
## Exact polynomial and matrix motivation

Write
\[
A_m=(z^m-1)(z^2+z-1)+2z,\qquad B_m=-z(z^m-1).
\]
Then \(g_m=A_m+iB_m\) and \(P_m=A_m^2+B_m^2\).
The program constructs this identity over \(\mathbb Z[z]\) and checks the degree, leading and constant coefficients, and reciprocity before evaluation.
In particular \(P_1=(z^2+1)(z^4+1)\), providing an exact neutral control.
No displayed degree or Gaussian field normalization divides the total measure.

For the matrix interpretation, let \(R_m\) be the permutation matrix of an \(m\)-cycle, \(v=(1+i)e_1\), and \(q=-1+i\).
On coordinates \((e,H,f)\), set
\[
K=\begin{pmatrix}0&0&1\\0&I_m&0\\1&0&0\end{pmatrix},
\quad
T=\begin{pmatrix}1&-v^*&q\\0&I_m&v\\0&0&1\end{pmatrix},
\quad
J=\begin{pmatrix}0&0&1\\0&I_m&0\\1&0&0\end{pmatrix}.
\]
The entries are Gaussian integers.
The identities \(q+\overline q=-v^*v=-2\), \(T^*KT=K\) and \(J^*KJ=K\) follow by block multiplication.
The diagonal matrix \(\operatorname{diag}(1,R_m,1)\) also preserves \(K\).
For their product
\[
U_m=TJ\operatorname{diag}(1,R_m,1)
=\begin{pmatrix}q&-v^*R_m&1\\v&R_m&0\\1&0&0\end{pmatrix},
\]
block elimination gives
\[
\det(zI-U_m)
 =\det(zI-R_m)\left(z^2-qz-1
              +zv^*R_m(zI-R_m)^{-1}v\right).
\]
The cycle identities are \(\det(zI-R_m)=z^m-1\) and
\[
v^*R_m(zI-R_m)^{-1}v=\frac{2}{z^m-1}.
\]
They prove the displayed formula for \(g_m\); the rational identity holds away from the cycle eigenvalues and hence gives the same polynomial identically.
This is an author calculation of the connection, not an independently reviewed structural classification of unitary words.
The actual computation evaluates the explicitly stated \(P_m\) regardless of that interpretation.

<a id="finite-results"></a>
## Complete finite results and limits

The exact factorization and 128-bit Arb evaluator from [J156](../Yin_J_G0156/sampler.py) are reused for all twelve complete polynomials.
Its [existing implementation review](../../../audits/reviews/Yin_R_G1111_v1.md#sampler-implementation-review) covers the all-root measure mechanism, not these new evaluated inputs.
Each factor product is reconstructed, and all roots and multiplicities enter the full measure.
A modulus ball meeting one is combined with one before multiplying, so uncertain unit-circle roots are not discarded.
The output retains exact dyadic enclosure endpoints in addition to the displayed ball strings.

| Parameter \(m\) | Degree | Complete \(M(P_m)\), approximate display |
| --- | --- | --- |
| 1 | 6 | 1, exactly |
| 2 | 8 | 4.11086964772560 |
| 3 | 10 | 3.26441716669129 |
| 4 | 12 | 2.83097660999536 |
| 5 | 14 | 3.17409753228909 |
| 6 | 16 | 2.62052139594555 |
| 7 | 18 | 3.00704379910140 |
| 8 | 20 | 2.83089228434845 |
| 9 | 22 | 2.91031305423820 |
| 10 | 24 | 2.89235475999564 |
| 11 | 26 | 2.88275871360428 |
| 12 | 28 | 2.89762041115981 |

The smallest positive complete measure in this finite set occurs at \(m=6\) and satisfies
\[
2.62052139594555<M(P_6)<2.62052139594556.
\]
Every positive input has one noncyclotomic irreducible factor of multiplicity one; all other factors are cyclotomic.
Thus selecting a factor from these inputs does not yield a smaller positive value.
The finite result is author-checked, with no new independent review claimed.
It excludes neither another central parameter, another Gaussian translation vector, a different positive rotation, nor any longer word.
It supplies no asymptotic conclusion or uniform lower bound over all \(m\).
The explicit polynomial \(P_m=A_m^2+B_m^2\) has a number of monomials bounded independently of \(m\), so this particular family also falls under the already accepted [DS17 fixed-support gap](../../../audits/literature/DS17/Yin_U001.md#ds17-u001).
That non-effective theorem is not used to certify the displayed finite \(6/5\) exclusions.

## Reproduction and retained evidence

Run the following with python-flint available, from the repository root.

~~~text
python -B mathematics/computations/programs/Yin_J_G0160/one_kick.py
~~~

The retained [program](one_kick.py) uses only fixed exact parameters \(m=1,\ldots,12\), \(b=1\), the Python standard library, python-flint and the explicitly linked cross-J evaluator.
The actual run used Python 3.14.7 and python-flint 0.9.0.
It has no random seed, prior generated input or numerical exclusion before the certified evaluation.
The generated [one_kick.json](../../outputs/Yin_J_G0160/one_kick.json) contains both Gaussian coefficient parts, all integer norms, factor coefficients, root balls, multiplicities, complete measure intervals and threshold decisions.
It is replaceable from these inputs and published atomically only after all twelve evaluations finish.

<a id="small-degree-boundary"></a>
## Exhaustive small-degree boundary of the analytic exclusion

The later boundary mode evaluates exactly
\[
m=1,2,3,4,\qquad b=0,1,\ldots,m+2,
\]
using \(g_{m,b}=(z^m-1)(z^2+(1-ib)z-1)+2z\) and the entire \(P_{m,b}=g_{m,b}\overline{g_{m,b}}\).
These are 22 inputs.
The actual finite-range reduction, including negative \(b\) and the separate analytic argument for every \(m\ge5\), belongs to the [adopted C887 theorem](../../../claims/Yin_C_G0887_v1.md#decision-gaussian-one-coordinate-gap).
Its complete proof and the finite boundary have an [independent finding](../../../audits/reviews/Yin_R_G1107_v37.md#gaussian-one-kick-gap-review), which does not cover the earlier twelve-input exploration or matrix motivation.

The boundary run uses the same exact factorization and full-root evaluator as the initial twelve-input test.
It returns three neutral nonnegative-parameter inputs, \((1,0),(1,1),(3,0)\), and nineteen positive inputs, every one strictly above \(6/5\).
The neutral factorizations are
\[
\begin{split}
P_{1,0}&=(z+1)^2(z^2-z+1)^2,\\
P_{1,1}&=(z^2+1)(z^4+1),\\
P_{3,0}&=(z+1)^2(z^4-z^2+1)^2.
\end{split}
\]
The squared factors in the first and third identities retain multiplicity two in the measure calculation.
The smallest positive value among the 22 inputs is at \((4,1)\), with
\[
2.83097660999535<M(P_{4,1})<2.83097660999537.
\]
This finite range is exhausted, without numerical screening or a missed root contributing zero.

| \(m\) | Tested nonnegative \(b\) | Neutral \(b\) | Smallest positive complete measure, approximate |
| --- | --- | --- | --- |
| 1 | 0 through 3 | 0, 1 | 5.10981333907131 at \(b=2\) |
| 2 | 0 through 4 | None | 3.26441716669129 at \(b=2\) |
| 3 | 0 through 5 | 0 | 3.26441716669129 at \(b=1\) |
| 4 | 0 through 6 | None | 2.83097660999536 at \(b=1\) |

Run the boundary calculation with the same dependencies and working directory.

~~~text
python -B mathematics/computations/programs/Yin_J_G0160/one_kick.py --boundary
~~~

Its separate replaceable [boundary.json](../../outputs/Yin_J_G0160/boundary.json) contains all 22 parameter pairs, exact Gaussian parts and integer polynomials, all factor coefficients, complete root balls and dyadic measure intervals.
The actual boundary run used Python 3.14.7 and python-flint 0.9.0 and completed all 22 inputs.
It has no prior-output dependency and publishes its complete output atomically.
The independent [checker](checks/boundary_independent.py) generates the Gaussian coefficient pairs separately, convolves them with their conjugates, verifies all factors and multiplicities, and obtains fresh 256-bit root enclosures without importing the author evaluator.
Its [completed output](../../outputs/Yin_J_G0160/boundary_independent.json) verifies all 22 complete polynomials and their threshold and minimum comparisons.
The root isolation and factorization implementations remain explicitly trusted FLINT/Arb inputs.
