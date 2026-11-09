---
author: Yin
---

# Complete energy-one and energy-two exclusion in the first rectified nonsquare class

<a id="scope"></a>
## Fixed conductor, cut and single-filter input

[nonsquare_control.py](nonsquare_control.py) uses only \(p=81\), cut \(k=9\), and filter index \(a=1\).
It reconstructs the [single-filter input](signed_filters.md#rectifier) through the frozen native call `signed_filters.construct([1])`, without loading generated JSON.
Write
\[
 B=B_{40},\qquad
 h_*=h_{0,81}U_2^6U_1^{-1}(T_3/T_{15})^2,\qquad
 V_1=T_5+T_4-T_2-T_1-1,
\]
and
\[
 q=-\prod_{a\in A}\frac{T_a}{T_{3^{v_3(a)}}},\qquad
 A=\{6,10,11,12,13,17,18,23,25,28,29,30,34,37,38\}.
\]
Here \(U_a=2+T_a\), \(T_a(z+z^{-1})=z^a+z^{-a}\), and the quotients define integral units in \(\mathbb Z[t]/B\).
The new base is \(h_{\rm new}=h_*qV_1\).
Its multiplier \(qV_1\) has norm 163 and is positive at all 40 nodes, so this is a sign-compatible class outside the previously tested family \(h_*v^2\).

The present variables are all integer elements \(v\in\mathbb Z[t]/B\), and the tested family is
\[
                        h=h_{\rm new}v^2\bmod B.
\]
Every integer square multiplier is eligible, including nonunits and elements vanishing at some nodes.
The test completely covers \(0<E\le2\), with \(E=3K+2L\), in this family.
Its two prescribed moment targets are \((E,K)=(1,3)\) and \((2,6)\), equivalently \((K,L)=(3,-4)\) and \((6,-8)\).
The computation does not cover other filter indices, the paired-filter input, arbitrary positive multipliers, or larger energies.

<a id="input-certificate"></a>
## Reconstructed input and exact matrix certificates

The construction checks the integer cyclic inverse of \(q\), and this control additionally verifies its ordinary polynomial inverse identity modulo \(B\).
It checks \(\lvert\operatorname{Res}(B,q)\rvert=1\).
The construction uses 512-bit Arb balls to certify strict positivity of \(qV_1\) at every node, and verifies the original 31-positive, 9-negative sign pattern of \(h_{\rm new}\).
No interval containing zero is accepted.
The exact multiplier norm is 163 and the exact absolute input resultant is \(32\cdot163=5216\).
The retained construction also supplies the [nonsquare witness](signed_filters.md#nonsquare): at the primitive trace \(15707\bmod163^2\), the multiplier is \(978\bmod163^2\), divisible by 163 exactly once.

The reconstructed base has
\[
 K=21027435559692867443,\quad
 L=815499961442697404,\quad
 E=64713306601963997137.
\]
These base moments do not meet either target.
Its endpoint parameter is \(U=10313720993588788164\), with the formal profile endpoint values \(2+2x+U\) retained for \(x=-2,-1,0,1,2\).
Those values alone do not make the base admissible, because its moments fail.

Use the retained monic basis \(U_i(t/2)\), \(0\le i<40\), and its integral Jacobi matrix \(J\).
In this sentence \(U_i(t/2)\) denotes the second-kind Chebyshev basis, rather than the positive units \(U_a=2+T_a\) above.
Define
\[
 H=h_{\rm new}(J),\qquad G=(2J+3I)H.
\]
The program checks symmetry and the identities \(K=H_{00}\), \(L=(JH)_{00}\), and \(E=G_{00}\) for the reconstructed base.
The separator \(-3/2\) is checked by the retained exact Sturm routine to lie between nodes 31 and 32.
All fraction-free leading pivots of \(G\) are positive, giving an exact positive-definiteness certificate.
The determinant identities are
\[
 \det H=-5216,\qquad
 \det(2J+3I)=-638639601137,
\]
\[
 \det G=3331144159530592
       =163\cdot20436467236384.
\]
Thus the new Gram determinant is exactly 163 times the [original square class determinant](two_energy_shell.md#exact-enumeration).

FLINT exact Gram LLL returns an integer matrix \(A\) and reduced Gram matrix \(G'\).
The program verifies
\[
                  |\det A|=1,\qquad G'=AGA^T
\]
and positive fraction-free pivots of \(G'\) with the same determinant.
The actual change matrix has \(\det A=1\).
It additionally checks all Gram–Schmidt size bounds \(\lvert\mu_{ji}\rvert\le51/100\) and the Lovász inequalities with \(\delta=3/4\), using exact rational arithmetic.
The largest absolute coefficient in this run is \(3255641/6453919<51/100\).
The integer change of coordinates is therefore a certified bijection; a numerical approximation is not used to decide eligibility.

<a id="complete-result"></a>
## Complete traversal and its finite conclusion

The program imports the frozen [energy-one and energy-two traversal](two_energy_shell.py).
It uses the [fraction-free completed-square recurrence](low_energy_shell.md#exact-traversal), exact integer square roots, and divisions checked for zero remainder.
The highest nonzero reduced coordinate is positive, giving one representative of each pair \(v,-v\).
Each leaf would be checked directly against the reduced integer matrices for \(E,K,L\).
The fixed stopping bounds are 5,000,000 recursive tree nodes or 120 seconds, whichever comes first.
The timer starts after construction and LLL.
As a small implementation control, the retained source compares the same recurrence with direct scans on the integer box \([-3,3]^2\) for Gram matrices \(\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), and \(\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\).
The returned vector-and-energy sets agree in all three cases, including energies one and two and nonzero cross terms.

The actual run exhausted every branch after 895 tree nodes and about 0.003 seconds of traversal, triggering neither limit.
It returned `complete: true` and `stop_reason: complete`.

| Energy | Nonzero integer vectors modulo simultaneous sign | Prescribed joint moment hits |
| ---: | ---: | ---: |
| 1 | 0 | 0 |
| 2 | 0 | 0 |

Consequently
\[
 v^TGv\notin\{1,2\}
       \quad\text{for every }v\in\mathbb Z^{40}
\]
for this fixed \(p=81,k=9,a=1\) input.
Both prescribed moment targets are empty in its integer-square family.
This is a complete finite-energy exclusion in the new class, not an exclusion of all sign-compatible inputs or all Galois labels.
It gives no conclusion about a positive-probability construction for every \(\varepsilon>0\).

For a joint hit, the retained downstream branch would reconstruct \(v,h,C,Q,P\), compute \(\operatorname{Res}(B,v)\), and reject a zero resultant.
For a nonzero resultant it would check the exact norm \(5216\,\operatorname{Res}(B,v)^2\), both moments, and the strict endpoint \(P(-1)>0\).
A strict-endpoint survivor would receive a complete Mahler enclosure using every complex root and its multiplicity.
The actual enumeration had no nonzero leaf, so it produced no candidate \(P\) and invoked no candidate-specific endpoint or Mahler calculation.
The downstream branch is retained but was not exercised by this run.

<a id="reproduction"></a>
## Reproduction, retained data and review status

Run from the repository root with the existing Python, python-flint, SymPy and NumPy environment:

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/nonsquare_control.py
~~~

The run used Python 3.14.7 and python-flint 0.9.0.
The source depends on the named same-group construction and traversal functions and their retained J150/J151 arithmetic helpers.
It reads no preexisting generated JSON and does not call either paired-filter construction or a larger-energy traversal.
It writes the replaceable output `mathematics/computations/outputs/Yin_J_G0154/nonsquare_control_81.json`.
That output retains the exact base and rectifier words, integral inverse, modular witness, base polynomial, original positive pivots, complete change matrix, reduced Gram matrix and pivots, exact LLL checks, limits, completion flag, and counts.
Different valid reduced bases can change traversal order or node count, while exact integral equivalence and exhaustive termination determine the stated coverage.
These are author-level computational checks; an independent review is separate.
