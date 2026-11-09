---
author: Yin
---

# A bounded low-energy integer-square search at conductor 81

<a id="scope"></a>
## The exact base and integer search domain

Take \(p=81\), \(n=40\), the full odd trace grid, and the terminal cut of nine negative residues.
Use exactly the [balanced base](balanced.md#descent-81)
\[
 h_*=h_{0,81}U_2^6U_1^{-1}\bigl(J_5(T_3)^2\bigr)^{-1}.
\]
The [program](low_energy_shell.py) regenerates this word from the sign-column construction and the displayed units.
It checks \((K,L,U)=(-3,10,-30)\) and \(|\operatorname{Res}(B,h_*)|=32\).
Its required inputs are the retained native programs, so existing generated JSON files are optional.

In the [integral monic orthonormal basis](../../../ledger/Yin_L_G0464_v10.md#moment-ellipsoid), form
\[
 H=h_*(J),\qquad G=(2J+3I)H.
\]
The separator \(-3/2\) has exactly 31 grid poles above it, certified by the integer recurrence.
The program checks symmetry, positive fraction-free pivots of \(G\), and
\[
                        \det G=20436467236384.
\]
Thus the prescribed base has its strict signs, also directly certified by diagonalizing the positive matrix \(G\) at the grid poles.
For every integer vector \(v\), its polynomial in this basis gives
\[
 h=h_*v^2\bmod B,\qquad
 K(v)=v^THv,\qquad L(v)=v^TJHv,\qquad
 E(v)=v^TGv=3K(v)+2L(v).
\]
The search domain consists of all integer vectors with \(0<E(v)\le6\), identified under simultaneous negation.
Unit status is an output test.
The three selected moment targets are

| \(x\) | \((E,K)\) | \((K,L)\) |
| ---: | --- | --- |
| 0 | \((6,2)\) | \((2,0)\) |
| 1 | \((1,3)\) | \((3,-4)\) |
| 2 | \((2,6)\) | \((6,-8)\) |

This integer-square domain contains all square multiples of the specified base, including nonunits.
Its relation to the entire strict sign class would require a separate representation argument.

<a id="exact-traversal"></a>
## Reduction, traversal and stopping boundary

FLINT is called with `G.lll(transform=True, rep='gram', gram='exact')`.
For its returned matrix \(A\) and Gram matrix \(G'\), exact checks give
\[
 \det A=1,\qquad G'=AGA^T.
\]
Positive fraction-free pivots of \(G'\) are also checked, with the final pivot equal to \(\det G\).
The program uses the [existing fraction-free elimination](../Yin_J_G0151/shell.py) and implements its solid-ball extension.
It evaluates the original moments using \(AHA^T\) and \(AJHA^T\), independently checking \(3K+2L=E\) at every returned vector.

Write \(D_i\) for the leading minors of \(G'\), with \(D_0=1\), and \(c_{ij}\) for the mixed minors in the fraction-free rows.
The exact completed-square contribution of coordinate \(i\) is
\[
       \frac{(D_i z_i+\sum_{j>i}c_{ij}z_j)^2}{D_iD_{i-1}}.
\]
At remaining budget \(s/D_i\), the traversal includes every integer satisfying
\[
 \left|D_i z_i+\sum_{j>i}c_{ij}z_j\right|
 \le\left\lfloor\sqrt{sD_{i-1}}\right\rfloor.
\]
It subtracts the square with an exact divisibility check and descends to the next coordinate.
The initial budget is \(6D_{40}\), and the final budget gives the integer energy of each leaf.
Coordinates are traversed from last to first, requiring the highest nonzero coordinate to be positive, so exactly one representative of each pair \(\{v,-v\}\) is eligible.
The zero vector is omitted.

The traversal is capped at \(10^6\) recursive tree nodes or 120 seconds, whichever occurs first.
Both caps are fixed in the program.
The elapsed-time boundary begins after matrix construction and reduction and includes the traversal and its leaf processing.
A cap interruption records `complete: false` and the actual completed-prefix counts.
The unvisited portion remains unresolved.

For a target hit, the program recovers the original polynomial \(v\) using \(zA\) and evaluates \(\operatorname{Res}(B,v)\).
If this resultant is nonzero, all values \(v(b_j)^2\) are strictly positive, proving preservation of the base signs.
It reconstructs \(h,C,Q,P\), checks both original moments and
\[
             |\operatorname{Res}(B,Q)|=32|\operatorname{Res}(B,v)|^2,
\]
and evaluates the strict endpoint \(P(-1)>0\).
The retained complete-root product routine encloses \(\prod_\lambda\max(1,|\lambda|)\) over every root of the original lift, counting multiplicities and verifying the full degree.
The present traversal reached no target hit, so these downstream checks were not exercised on a new candidate.

<a id="partial-result"></a>
## The completed prefix at the node limit

The traversal stopped at exactly \(1{,}000{,}000\) tree nodes, before its time cap.
It found four nonzero classes under simultaneous negation in that prefix, all at energy six.

| \(E\) | \(K\) | \(L\) | Classes encountered |
| ---: | ---: | ---: | ---: |
| 6 | 0 | 3 | 1 |
| 6 | 8 | \(-9\) | 1 |
| 6 | 12 | \(-15\) | 1 |
| 6 | 16 | \(-21\) | 1 |

The prefix contained zero joint hits at the three selected targets.
The traversal is partial, so it leaves the existence of further low-energy vectors and joint hits unresolved.
In particular, these counts give no emptiness conclusion for energies one through five or for the three complete target shells.
The result supplies a certified setup and a bounded finite prefix of the integer-square search.

<a id="reproduction"></a>
## Reproduction and native dependencies

Run from the repository root with Python, python-flint and SymPy.
The latter is needed by the existing J151/J150 imports.

~~~text
python -B mathematics/computations/programs/Yin_J_G0154/low_energy_shell.py
~~~

The program imports the balanced-word unit constructors and the cyclic operations from this J, plus the explicitly named J151 Jacobi, matrix-polynomial, fraction-free and polynomial-recovery routines.
It writes the replaceable local output `mathematics/computations/outputs/Yin_J_G0154/low_energy_shell_81.json`.
That output includes the reconstructed base, exact change matrix, reduced Gram matrix, positive leading minors, completed-prefix counts, stopping reason and any target witnesses.
The actual reduced basis and traversal prefix can depend on the FLINT implementation, while the determinant, congruence and positive-pivot checks certify the returned basis in each run.
The observed reduced Gram diagonal is
\[
 (7,9,9,10,10,10,11,10,13,9,13,12,11,14,14,13,11,13,12,13,
 10,13,14,10,11,12,14,8,8,8,11,10,10,10,9,8,7,10,11,13).
\]
The checks reported here are author-level computational checks.
