---
author: Yin
---

# Angular moments of the smaller factor at prime 223

<a id="counts"></a>
## Complete representatives at degrees 56 and 58

For the [two possible degrees](../../../../../ledger/Yin_L_G0462_v264.md#frontier), the [angular-moment inequalities](../../../../../ledger/Yin_L_G0462_v268.md#angular) give additional tests on the first fifteen Newton sums of a polynomial with \(M(P)\le1089/1000\).
Apply them after the [version-two cyclotomic tests](../v2/readme.md#counts), counting full polynomial representatives under the same power exclusions and sign convention.
A polynomial that fails one of these necessary inequalities cannot be the smaller factor, and irreducibility and measure remain to be tested on the survivors.

| Degree | Entering from version two | Removed by Fejér tests | Further removals by the size-eleven matrix | Further removals by the size-sixteen matrix | Remaining |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 56 | 914,510,217 | 3,491,520 | 0 | 1,023,424 | 909,995,273 |
| 58 | 2,476,894,466 | 5,901,648 | 0 | 1,549,680 | 2,469,443,138 |

These tests remove 11,966,272 representatives that passed version two, leaving 3,379,438,411 across the two degrees.
The Fejér inequalities also reject 367,424 and 362,880 representatives, respectively, already rejected by the cyclotomic tests.

<a id="tests"></a>
## Exact Fejér and Toeplitz tests

At each horizon \(N=10,15\), test the Fejér inequality at all 23 cosines in
\[
  \{j/8:-8\le j\le8\}
   \ \cup\ \{\pm15/16,\ \pm31/32,\ \pm63/64\}.
\]
Starting from \(C_0=1,C_1=x\), the recurrence \(C_{k+1}=2xC_k-C_{k-1}\) gives \(\cos(k\theta)\) at \(x=\cos\theta\).
With the sign reversed to give an upper test, set \(w_k=-2(1-k/(N+1))C_k\) and use the cap \(D+\sum_k|w_k|(T^k+T^{-k}-2)\).
All entries are rational.
The code floors coefficients and caps at scale \(10^7\).
A score above the floored cap by more than \(\sum_{k\le N}B_k\) rejects, and one below or equal to the floored cap minus the same margin passes.
All other comparisons use the original integer numerators over a common denominator.
The sign action on polynomials corresponds to \(x\mapsto-x\), so each union of Fejér tests is invariant.

For the [full moment matrix](../../../../../ledger/Yin_L_G0462_v268.md#matrix) write \(S_N=(s_{|i-j|})_{0\le i,j\le N},\ s_0=D\).
The strict rational shifts \(167/100\) and \(271/50\) exceed the negative-eigenvalue budgets at \(N=10\) and \(N=15\), respectively.
Thus \(S_N+c_N I\) must be positive definite.
Multiplying by the positive denominator of \(c_N\) makes the matrix integral.
The sign action conjugates this matrix by the diagonal entries \((-1)^j\), preserving its eigenvalues.

For each prefix the [integer Schur complement recurrence](../../../../../ledger/Yin_L_G0462_v53.md#recursion) decides positive definiteness.
To append the scaled moment \(y_k\), let \(D_i\) denote the preceding leading determinants, initially \(D_0=1,D_1=y_0\).
The stored row \((a_0,\dots,a_{k-1})\) consists of \(D_{k-1}\) followed by the negatives of the previous adjugate predictor in the cited recurrence.
Set \(X=\sum_{j=0}^{k-1} a_j y_{k-j}\).
The next leading matrix is positive definite precisely when the preceding one passes and \(|X|<D_k\).
In that case the new determinant and row are
\[
 D_{k+1}=\frac{D_k^2-X^2}{D_{k-1}},\qquad
 a'_0=D_k,\quad
 a'_j=\frac{D_k a_j-Xa_{k-j}}{D_{k-1}}\ (1\le j<k),\quad a'_k=-X .
\]
All divisions are exact because these are determinants and adjugate entries of integer matrices.
The implementation uses Python integers for this recurrence.
Within a group with the first two sums fixed, digits \(s_k+B_k\) in bases \(2B_k+1\) encode the remaining prefix to share identical states.
The largest product of bases through 15 is \(60{,}268{,}312{,}129{,}921{,}875<2^{63}\), and restricting a coordinate to zero only reduces the range.

Version two supplies the [exact number of extensions](../v2/readme.md#extensions) of each prefix and its cyclotomic status.
The new tests keep the same degree, radial bound, caps and scale over each power-substitution intersection.
Inclusion and exclusion remove powers, after which division by two gives the number of sign representatives.
The program verifies that summing the output partition recovers both the starting counts and the numbers left by version two.
The [ten negative sixes](../../../../../ledger/Yin_L_G0462_v268.md#example) give a separate check on the part discarded by the Fejér test alone.

<a id="reproduction"></a>
## Reproduction

Generate the [version-two inputs and output](../v2/readme.md#reproduction), then run the [angular prefix program](angular_prefixes.py) using Python and NumPy.

~~~text
python mathematics/computations/programs/Yin_J_G0179/versions/v4/angular_prefixes.py
~~~

The [generated counts](../../../../outputs/Yin_J_G0179/versions/v4/results.json) distinguish the two earlier tests, their overlap, the successive additional matrix rejections and the surviving representatives.
