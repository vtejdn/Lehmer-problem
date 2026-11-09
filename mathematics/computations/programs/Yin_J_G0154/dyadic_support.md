---
author: Yin
---

# Exact dyadic joint support and the integer obstruction in the fixed paired class

<a id="scope"></a>
## The fixed pair and the two moment equations

[dyadic_support.py](dyadic_support.py) uses exactly the conductor-81, cut-nine input reconstructed by signed_filters.construct([1,2]).
The base \(h_{\rm pair}=h_*qV_1V_2\) has absolute resultant \(850208=2^5\,163^2\), with the strict signs and nonsquare multiplier retained in the [paired construction](paired_control.md#input-certificate).
In the monic second-kind basis, put \(H=h_{\rm pair}(J)\) and \(T=JH\).
Both are symmetric integer matrices of size 40.
The equations considered here are only
\[
                  v^{\mathsf T}Hv=K,\qquad v^{\mathsf T}Tv=L.
\]
They do not impose the unit, nonvanishing, strict endpoint or Mahler conditions.
The five target pairs are \(K=x^2+2,L=-4x\), for \(x=-2,-1,0,1,2\).
No other pair of Galois labels is enumerated by this program.

<a id="exact-gauss"></a>
## Exact Fourier inversion by integral block elimination

Let \(\zeta=\exp(2\pi i/8)\).
Arithmetic is performed in \(\mathbb Z[\zeta]\), represented by four integer coefficients with the reduction rule \(\zeta^4=-1\).
For a symmetric matrix \(A\) modulo \(m\in\{1,2,4,8\}\), define
\[
 G_m(A)=\sum_{v\in(\mathbb Z/m)^{r}}
                   \zeta^{(8/m)v^{\mathsf T}Av}.
\]
At modulus one this sum is one.
At an empty matrix it is also one.

If a diagonal entry is odd, it gives an invertible one-dimensional block.
An invertible change modulo \(m\) completes its square and leaves the Schur complement.
The sum factors as the directly summed block times the sum on that complement.
If every diagonal is even but an off-diagonal entry is odd, the associated two-dimensional block
\[
               B=\begin{pmatrix}a&b\\b&c\end{pmatrix}
\]
has odd determinant.
The change \(x\mapsto x+B^{-1}Dy\) removes its cross terms and leaves \(C-D^{\mathsf T}B^{-1}D\).
Its block sum has at most \(8^2\) terms.
If all matrix entries are even, then
\[
                        G_m(2A)=2^rG_{m/2}(A),
\]
because the phase depends only on the vector modulo \(m/2\).
These three operations terminate and preserve the complete sum over the original finite module.
They require no diagonalization over a field of characteristic two and no square root or floating-point evaluation.

The 64 computed sums give every joint count by character orthogonality:
\[
 N_8(K,L)=\frac1{64}\sum_{a,b\bmod8}
                 \zeta^{-aK-bL}G_8(aH+bT).
\]
The program checks that every result is a nonnegative integer, with zero coefficients of \(\zeta,\zeta^2,\zeta^3\).
It checks conjugate symmetry of the sums and that all 64 counts add to \(8^{40}\).
Eight fixed matrices of dimensions one through three are compared with direct vector enumeration at moduli two, four and eight, giving 24 separate exact controls.
These include odd diagonal pivots, even blocks with odd cross terms, matrices divisible by two and singular matrices.

Modulo two, the two quadratic forms are the linear forms given by their diagonals.
The two diagonal vectors here are nonzero and distinct, so their joint linear map has rank two.
Each parity target therefore has \(2^{38}\) vectors modulo two and \(4^{40}2^{38}=2^{118}\) lifts modulo eight.
The four aggregated count checks reproduce this independently derived parity total.

<a id="joint-counts"></a>
## The complete counts and the five targets

Among all 64 residue targets, four counts equal \(2^{114}-2^{80}\), 56 equal \(2^{114}\), and four equal \(2^{114}+2^{80}\).
The specific five targets have:

| \(x\) | \((K,L)\) | Exact \(N_8(K,L)\) |
| ---: | --- | --- |
| \(-2\) | \((6,8)\) | \(2^{114}-2^{80}\) |
| \(-1\) | \((3,4)\) | \(2^{114}\) |
| \(0\) | \((2,0)\) | \(2^{114}+2^{80}\) |
| \(1\) | \((3,-4)\) | \(2^{114}\) |
| \(2\) | \((6,-8)\) | \(2^{114}-2^{80}\) |

Thus every target count is strictly greater than \(2^{86}\).
Under the uniform law on vectors modulo eight, these are genuine finite congruence probabilities \(N_8/8^{40}\).
They are not counts or probabilities of integer solutions of the exact equations.

<a id="lifting"></a>
## What the threshold proves at the prime two

Since \(v_2(\det H)=5\), the kernel of \(H\bmod2\) has dimension at most five.
The Jacobi matrix is invertible modulo two, as its determinant is odd.
Its subdiagonal entries equal one, so \(e_1,Je_1,\ldots,J^{39}e_1\) form a basis over every field.
In particular each eigenspace has dimension at most one.
Over \(\mathbb F_2\), the vectors \(Hv,JHv\) are dependent only if \(Hv=0\) or \(Hv\) lies on the eigenline for eigenvalue one.
There are at most \(2^5\cdot2=2^6\) such vector parities.
Their lifts modulo eight number at most \(2^6\,4^{40}=2^{86}\).
Each target therefore has a solution modulo eight with \(Hv,JHv\) linearly independent modulo two.

Suppose \(v\) solves the two equations modulo \(2^s\), \(s\ge3\), and has that independent parity.
For either symmetric form \(A\in\{H,T\}\),
\[
 (v+2^{s-1}w)^{\mathsf T}A(v+2^{s-1}w)
       \equiv v^{\mathsf T}Av+2^s v^{\mathsf T}Aw
                   \pmod{2^{s+1}}.
\]
The two linear forms in \(w\bmod2\) are independent, so both next error bits can be prescribed.
This step preserves the quadratic equations modulo \(2^s\) and the vector modulo \(2^{s-1}\), although it need not preserve the vector modulo \(2^s\).
Its successive increments tend to zero in \(\mathbb Z_2^{40}\).
The resulting Cauchy sequence has a limit satisfying both exact equations, with the independent parity unchanged.
Consequently all five targets are realizable over \(\mathbb Z_2\) and modulo every power of two.
No positive ambient Haar measure for the exact equality locus is asserted.

<a id="real-and-global-boundary"></a>
## Real feasibility and the separate integer obstruction

The program independently runs the retained exact separator recurrence at \(4/3,-3/2,-4/3\).
The respective numbers of grid nodes above these values are \(10,31,29\).
Hence
\[
               b_1>4/3,\qquad -3/2<b_{31}<-4/3.
\]
In the orthogonal evaluation coordinates, the positive form \(G=(2J+3I)H\) is diagonal and the generalized eigenvalues of \((H,G)\) are \(1/(2b_j+3)\).
The two displayed nodes give
\[
 \frac1{2b_1+3}<\frac3{17}
       \le \frac K{3K+2L}
       \le3<\frac1{2b_{31}+3}
\]
for every prescribed target.
Positive weights on these two coordinates realize the required ratio and then the required positive energy.
Small nonzero weights on the other coordinates, followed by adjustment of the first two, also give a real solution with every evaluation coordinate nonzero.
This is real feasibility of the two moments, without an endpoint or whole-measure assertion.

The [odd-prime analysis](../../../ledger/Yin_L_G0462_v8.md#odd-prime-count) supplies nonsingular solutions of the same moment equations at every odd prime for all paired labels.
Together with the exact two-adic calculation, the present fixed pair has joint moment solutions over the reals and every \(\mathbb Z_q\).
The [separate complete small-energy traversal](energy_six.md#complete-result), however, finds no integer vector with energy from one through six in this fixed paired class.
It therefore excludes global integer solutions of the three targets \(x=0,1,2\), despite their local and real feasibility.
This is a concrete obstruction to inferring the required integer count from local support alone.
The targets \(x=-2,-1\), with energies 34 and 17, have not been globally enumerated here.
No strict small-Mahler event or counterexample to the original Task is produced by this calculation.

<a id="reproduction"></a>
## Native execution and retained data

Run from the repository root with Python, python-flint, SymPy and NumPy:

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/dyadic_support.py
~~~

The executed environment is the existing Python 3.14.7 and python-flint 0.9.0 environment used by the constructor.
All finite sums, count checks and separator checks use exact integer arithmetic.
The constructor retains its strict Arb sign checks; no generated JSON is read.
The replaceable output mathematics/computations/outputs/Yin_J_G0154/dyadic_support_81.json contains the fixed base polynomial, both matrices modulo eight, all 64 exact Gauss sums, all 64 counts, parity and small-dimensional controls, target counts and threshold comparisons.
The [independent dyadic finding](../../../audits/reviews/Yin_R_G1107_v18.md#dyadic-support-review) checks this complete fixed calculation and its exact local and global boundaries.
