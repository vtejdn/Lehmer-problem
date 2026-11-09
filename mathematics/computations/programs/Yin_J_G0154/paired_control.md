---
author: Yin
---

# Complete small-energy exclusion for the fixed paired-filter class

<a id="scope"></a>
## Conductor 81, terminal cut nine and filter pair \((1,2)\)

[paired_control.py](paired_control.py) reconstructs exactly the paired input supplied by the frozen call `signed_filters.construct([1, 2])`.
This uses \(p=81\), \(k=9\), \(n=40\), and the [existing balanced base](balanced.md)
\[
 h_*=h_{0,81}U_2^6U_1^{-1}(T_3/T_{15})^2,\qquad U_a=2+T_a.
\]
Write
\[
 V_a=T_{5a}+T_{4a}-T_{2a}-T_a-1,\qquad
 h_{\rm pair}=h_*qV_1V_2.
\]
The paired rectifier \(q\) is chosen by the fixed [unit-signature construction](signed_filters.md#rectifier), with no descent or selection of a new seed.
The tested family consists of every
\[
 h=h_{\rm pair}v^2\bmod B_{40},\qquad
                   v\in\mathbb Z[t]/B_{40}.
\]
All integer square multipliers are included, whether they are units, nonunits, or have zero components.
The only tested energies are \(0<E\le2\), where \(E=3K+2L\).
The prescribed joint moment targets are \((E,K)=(1,3)\) and \((2,6)\), corresponding to \((K,L)=(3,-4)\) and \((6,-8)\).
Other pairs, other conductors and energies greater than two are outside this computation.

<a id="input-certificate"></a>
## Integral input and positive-definite matrix certificates

The frozen constructor performs the exact cyclic unit-inverse checks, 512-bit Arb checks of positivity at all 40 nodes, and the original 31-positive, 9-negative cut check.
This new control also checks the ordinary polynomial identity \(q q^{-1}=1\bmod B_{40}\) and \(\lvert\operatorname{Res}(B_{40},q)\rvert=1\).
The deterministic paired unit has no initial minus sign and is
\[
 q=\prod_{a\in A}\frac{T_a}{T_{3^{v_3(a)}}},\qquad
 A=\{2,5,7,10,11,17,20,21,22,24,26,28,29,30,31,35,36,37,38\}.
\]
Each displayed quotient is an integral unit in the trace order, as certified by the retained inverse identities.
The multiplier \(qV_1V_2\) is strictly positive at every node and has exact norm \(163^2=26569\).
The input absolute resultant is
\[
                 \lvert\operatorname{Res}(B_{40},h_{\rm pair})\rvert
                    =32\cdot163^2=850208.
\]
The retained [modular witnesses](signed_filters.md#nonsquare) prove that this positive multiplier is nonsquare despite its square total norm.
At primitive indices 4 and 8, the multiplier values modulo \(163^2\) are 489 and 14670, respectively, each with exactly one factor of 163.

The reconstructed base has
\[
 K=3773266954904580051188677,\qquad
 L=146337342773058078636538,
\]
\[
 E=11612475550259856310839107,\qquad
 U=1850745065855084728085735.
\]
Its formal endpoint values \(2+2x+U\) for \(x=-2,-1,0,1,2\) are retained in the generated data, but the base does not satisfy either moment target.

Use the retained [integer matrix representation](low_energy_shell.md#scope) with Jacobi matrix \(J\) and monic second-kind Chebyshev basis.
Set
\[
 H=h_{\rm pair}(J),\qquad G=(2J+3I)H.
\]
The exact Sturm separator check places \(-3/2\) between nodes 31 and 32.
The source checks symmetry, agreement of \(H_{00},(JH)_{00},G_{00}\) with the reconstructed moments, and all positive fraction-free leading pivots of \(G\).
It obtains
\[
 \det H=-850208,\qquad \det(2J+3I)=-638639601137,
\]
\[
 \det G=542976498003486496
       =163^2\cdot20436467236384.
\]
The determinant is \(163^2\) times that of the [original balanced square class](two_energy_shell.md#exact-enumeration).

Exact Gram LLL gives \(G'\) and an integer change matrix \(A\).
The program verifies \(\lvert\det A\rvert=1\), \(G'=AGA^T\), positive pivots for \(G'\), and equality of determinants.
The actual change matrix has \(\det A=1\).
The retained exact rational checks also verify all size bounds \(\lvert\mu_{ji}\rvert\le51/100\) and Lovász inequalities with \(\delta=3/4\).
The largest absolute coefficient in this run is \(378673259009777164/752586800729766883<51/100\).
Thus the integer-coordinate change preserves the entire tested lattice.

<a id="complete-result"></a>
## Complete traversal at energies one and two

The program reuses the frozen [exact traversal](two_energy_shell.py), whose [fraction-free recurrence](low_energy_shell.md#exact-traversal) uses integer square roots and checks every division for zero remainder.
The highest nonzero reduced coordinate is positive, selecting one representative of each pair \(v,-v\).
Every leaf would receive direct integer evaluations of \(E,K,L\) in the reduced matrices.
The fixed stopping limits are 5,000,000 recursive tree nodes or 120 seconds, whichever comes first.
The timer begins after construction and LLL.

The actual traversal exhausted all branches after 862 nodes, taking about 0.002 seconds.
Neither limit was triggered.
The output records `complete: true` and `stop_reason: complete`.

| Energy | Nonzero integer classes modulo simultaneous sign | Prescribed joint moment hits |
| ---: | ---: | ---: |
| 1 | 0 | 0 |
| 2 | 0 | 0 |

Hence
\[
          v^TGv\notin\{1,2\}\quad\text{for every }v\in\mathbb Z^{40}
\]
for this particular \(p=81,k=9,(a,b)=(1,2)\) input.
Both prescribed moment targets are empty in its integer-square family.
This finite-energy exclusion does not cover all sign-compatible inputs, all paired labels, or arbitrary positive multipliers outside the specified square family.
It provides no arbitrary-\(\varepsilon\) positive-probability conclusion.

The candidate-checking branch is defined in this new program with base norm 850208.
It does not call the single-filter candidate checker whose base norm is 5216.
A joint hit would first require \(\operatorname{Res}(B_{40},v)\ne0\), then reconstruction of \(h,C,Q,P\), verification of both moments and the norm \(850208\,\operatorname{Res}(B_{40},v)^2\), and a strict endpoint \(P(-1)>0\).
A survivor would receive a complete Mahler enclosure from every complex root with its multiplicity.
There were no nonzero leaves, so no candidate polynomial, candidate-specific resultant or endpoint check, or Mahler computation was produced.
This downstream branch was not exercised in the actual run.

<a id="reproduction"></a>
## Reproduction and retained mathematical data

From the repository root, run with Python, python-flint, SymPy and NumPy:

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/paired_control.py
~~~

The run used the existing Python 3.14.7 and python-flint 0.9.0 environment.
The program reads no generated JSON.
It imports the frozen constructor, matrix operations, LLL checks, polynomial conversion and energy-two traversal through explicitly named helpers, without invoking their other main programs.
It writes `mathematics/computations/outputs/Yin_J_G0154/paired_control_81.json`.
The output retains the exact input and rectifier words, inverse, modular witnesses, base polynomial, original positive pivots, integral change matrix, reduced Gram matrix and pivots, exact LLL certificate, scope, limits, completion flag, leaves, moment counts and target counts.
Different valid reduced bases may change traversal order and node count, while the integral equivalence checks and exhaustive termination establish the stated coverage.
The [independent paired-control finding](../../../audits/reviews/Yin_R_G1107_v15.md#paired-control-review) checks the original construction, matrices and complete traversal at this scope.
