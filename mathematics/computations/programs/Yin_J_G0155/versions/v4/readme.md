---
author: Yin
---

# The zero-profile coefficient at index eight through conductor 107

<a id="exclusion"></a>
## Finite exclusion

No integral input in the [full zero-profile chart](../../../../../claims/Yin_C_G0881_v3.md#prefix-coordinates) has a strict terminal sign cut, strict endpoint, and agreement with \(P_{*,0}=(1+z^2)^2/((1-z)(1-z^2))\) through coefficient index eight at any odd conductor \(5\le p\le107\).
The [first-conductor and uniqueness calculation](../v3/readme.md#first-conductor) covers \(p\le55\) and attains index seven at \(55\).
The computation for Yin's [Lehmer Task](../../../../../tasks/Yin_T_G0001_v1.md#contract) on 2026-11-16 extends the exclusion to every odd \(57\le p\le107\), allowing both even and odd coordinates in the full proved coefficient box.
It leaves larger conductors open.

Put \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), \(B_n=E_n+E_{n-1}\), \(E_0=1,\ E_1=t,\ E_{i+1}=tE_i-E_{i-1}\).
The input is \(h=\sum_{i=0}^{n-1}a_iE_i\) with integral \(a_i\), trace \(Q=tB_n+\sum_i a_i B_{n-i-1}\), positive residues \((4-b_j^2)h(b_j)/p\) before the terminal block, negative residues throughout that block, and \(2+\sum_i(-1)^ia_i>0\).
Agreement through index eight is equivalent to
\[
              (a_0,a_1,a_2,a_3,a_4,a_5,a_6)=(2,0,4,0,4,0,4).
\]
The [quadrature bound](../../../../../ledger/Yin_L_G0464_v24.md#quadrature-bound) at \(L=8\) has \(D=3\) and permits only \(\kappa\) with \(6(2\kappa+1)\le p\), where \(\kappa\) is the number of negative residues.
This leaves 152 conductor and cut pairs, with 68, 39, 21 and 24 in the four consecutive intervals listed below.

Fifty-two complete coefficient vectors with cuts satisfied the rational outer inequalities.
Every one has a nonconstant exact \(\gcd(B_n,h)\), so at least one required strict sign vanishes.
For \(\kappa=1\) there were respectively \(1,2,3,4,5,6,7,8\) such leaves at \(p=57,63,69,75,81,87,93,99\).
There was one further leaf at each of \((p,\kappa)=(95,1),(95,2)\), with twelve at \((105,1)\) and two at \((105,2)\).
All other cases had no complete outer leaf.

<a id="certification"></a>
## Rigorous rows and pruning

The [native program](prefix_eight.py) reuses the [integer box and sign enclosure](../v2/readme.md#covering-box) and [integer dual certificate](../v2/readme.md#integer-bounds).
It proposes the ordered roots of \(B_n\) on a finer grid because the earlier starting radius can meet \(-2\) at these conductors.
For each proposed integer center \(c_j\), it checks opposite signs of \(B_n\) at \((c_j\pm1)/2^{96}\), checks that the intervals are disjoint in descending order and contained in \((-2,2)\), and exhausts all \(n\) roots by degree.
A 144-bit cosine approximation supplies only the centers.
At each midpoint it computes \(E_i\) exactly and rounds \(2^{40}E_i\) to an integer row, bounding the error by half a rounding unit plus \(2^{40-96}(i+1)i^2\), rounded upward.
The necessary inequalities include the exact integer endpoint row and the full bounds \(|a_i|\le\lceil p^2(i+1)/4\rceil\).
The program substitutes the seven fixed coordinates into these rows before branching.

The numerical simplex solver keeps its basis between successive coefficient bounds and proposes row multipliers for either sign of the next coordinate, or a ray when its model is infeasible.
For the remaining exact system \(Av\le b\), \(|v_i|\le K_i\), the checker rounds the sign-adjusted multipliers to nonnegative integers \(\lambda\).
For \(S=2^{80}\) and either signed first coordinate vector \(e\), it uses
\[
 S(e\cdot v)\le\lambda\cdot b+
                    \sum_i |(\lambda^\mathsf T A)_i-Se_i|K_i .
\]
For a proposed infeasibility ray the same right side with \(e=0\) must be strictly negative to discard that branch.
The previously chosen coordinates have already been substituted into \(b\).
If no ray certifies emptiness, the [earlier dual checker](../v2/fixed_prefix.py) or the full proved box supplies a covering range.
Every integer in the resulting range is visited.
Completed leaves undergo the exact grid test, including gcd tests at possible zero values.

<a id="reproduction"></a>
## Reproducing the degree-eight exclusion

The four disjoint intervals can be reproduced independently from the repository root.
The jobs option distributes conductor and cut pairs among processes and can be omitted for one worker.

~~~text
python -B mathematics/computations/programs/Yin_J_G0155/versions/v4/prefix_eight.py --start 57 --end 83 --jobs 4
python -B mathematics/computations/programs/Yin_J_G0155/versions/v4/prefix_eight.py --start 85 --end 95 --jobs 4
python -B mathematics/computations/programs/Yin_J_G0155/versions/v4/prefix_eight.py --start 97 --end 101 --jobs 4
python -B mathematics/computations/programs/Yin_J_G0155/versions/v4/prefix_eight.py --start 103 --end 107 --jobs 4
~~~

The author run used Python 3.14.3, SymPy 1.14.0, SciPy 1.17.1 with its bundled HiGHS bindings, NumPy 2.4.4 and mpmath 1.3.0.
Each command publishes the full list of cuts, leaf counts, and strict solutions only after all its cases have completed.
The results cover [57–83](../../../../outputs/Yin_J_G0155/prefix_eight_57_83.json), [85–95](../../../../outputs/Yin_J_G0155/prefix_eight_85_95.json), [97–101](../../../../outputs/Yin_J_G0155/prefix_eight_97_101.json), and [103–107](../../../../outputs/Yin_J_G0155/prefix_eight_103_107.json) and require no saved inputs or previous solver output.
