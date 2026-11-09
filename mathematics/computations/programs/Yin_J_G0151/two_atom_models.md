---
author: Yin
---

# Two distinct unit atoms in every residual degree-seven model

<a id="scope"></a>
## Exact result and boundary

Use the five residual triples, trace functional \(\mathcal D\), and fixed cut bracket from [C882v6](../../../claims/Yin_C_G0882_v6.md#statement), at \(p=19683\), \(k=1990\), \(x=-1\), \((K,L,N,U)=(3,4,7,1)\), and the prescribed signs and norm \(2^{4391}\).
Put
\[
 \mathcal R=\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\},
 \qquad I=[-1609663/10^6,-1609662/10^6].
\]
For each triple there are two fixed distinct rational points \(-2<a<b<2\), independent of \(c\in I\), such that for every \(c\in I\) a step function \(0\le w_c\le1\) satisfies
\[
 \mathcal D(f)+f(c)=f(a)+f(b)-\int_{-2}^2w_c(t)f'(t)\,dt
 \tag{1}
\]
simultaneously for every real polynomial of degree at most seven.
The two atomic masses are exactly one each, and there is no mass variable in the new systems.
This strengthens the earlier positive-mass-two model by reinstating two distinct individual trace-root atoms.

| \((O,V,W)\) | \(a\) | \(b\) | Seven free occupancy indices |
| --- | --- | --- | --- |
| \((10,18,27)\) | \(-987/1024\) | \(-3777/4096\) | 0, 65, 110, 112, 159, 221, 253 |
| \((11,20,33)\) | \(-4981/4096\) | \(-1289/2048\) | 1, 12, 87, 164, 168, 207, 238 |
| \((11,20,34)\) | \(-4487/4096\) | \(-91/128\) | 2, 37, 64, 107, 176, 220, 253 |
| \((11,21,36)\) | \(-2603/2048\) | \(-1419/2048\) | 0, 24, 37, 109, 180, 229, 251 |
| \((11,21,37)\) | \(-2369/2048\) | \(-3079/4096\) | 1, 65, 99, 129, 192, 208, 246 |

The actual cut pole belongs to the interior of \(I\), as the exact recurrence confirms.
Both rational trace atoms lie in \((-2,2)\), so each lifts under \(t=z+z^{-1}\) to a reciprocal pair of unit-circle points.
Thus the model remains compatible with exterior radii equal to one after imposing two distinct unit atoms.
This is a statement about the relaxed moment-and-occupancy system, not a realization of an integral \(h\), an actual pairing of all poles, or a polynomial \(P\) of measure one.
The remaining occupation function may take fractional values and need not equal the indicator of intervals terminating at the actual poles.
No original residual branch is declared realizable or impossible.

<a id="certificate"></a>
## Fixed rational certificate

The [native program](two_atom_models.py) stores the five exact atom pairs, all fixed-one occupancy ranges and all free indices in `MODELS`.
Indices \(i=0,\ldots,255\) refer to cells with endpoints \(t_i=-2+i/64\) and \(t_{i+1}\).
The recorded integer ranges are inclusive; unlisted, nonfree coordinates have occupancy zero.
The free and fixed-one sets are disjoint.

Set \(q_j=T_j\) for \(1\le j\le7\), using \(T_j(z+z^{-1})=z^j+z^{-j}\), and form
\[
 A_{j,i}=q_j(t_i)-q_j(t_{i+1}),\qquad
 g_j(c)=\mathcal D(q_j)+q_j(c)-q_j(a)-q_j(b).
\]
The matrix \(A\) has seven rows and 256 occupancy columns.
Every atomic term is already an exact constant in the right side.
The constant-polynomial equation is identically \(\mathcal D(1)+1=1+1\), so it needs no occupancy row.
For other basis elements, \(A\omega=g(c)\) is exactly (1), since each column is the negative integral of \(q_j'\) over its cell.

Write \(c=c_0+10^{-6}s\), \(c_0=-1609663/10^6\), and express \(g(c)\) in the degree-seven Bernstein basis:
\[
 g(c_0+10^{-6}s)=\sum_{r=0}^7g^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
The program computes the controls exactly through the fixed polynomial and cut transformations in `negative_one_seven.relaxation_system`, subtracting the two fixed unit-atom values from every control.
For each control, subtract the columns fixed at one and solve the seven free columns over \(\mathbb Q\).
Exact elimination and substitution verify all forty \(7\times7\) systems.
Every free coordinate in every control satisfies
\[
               \frac1{1000}<\omega_i^{(r)}<\frac{999}{1000}.
\]
All other coordinates are exactly zero or one.
Taking the Bernstein convex combination of the solutions gives occupancies in \([0,1]\) with \(A\omega(c)=g(c)\) for every cut position in the entire interval.
The basis \(1,T_1,\ldots,T_7\) spans all real polynomials of degree at most seven, so (1) holds simultaneously on the whole required space.
This proves the exact stated result without a floating-point feasibility premise.

From (1) and \(0\le w_c\le1\) one obtains
\[
 \mathcal D(f)+f(c)-V_-(f)\le f(a)+f(b)\le2\max_{[-2,2]}f.
\]
Thus retaining two distinct unit atoms while allowing these occupancies still leaves a feasible model at radial cost zero for each residual triple.
The original seven-moment equations together with this two-atom restriction and \(0\le w\le1\) do not, by themselves, force a positive Mahler gap.
The finite actual pairing intervals, their pole endpoints, the global integer polynomial and its resultant are not reconstructed by the model.

<a id="reproduction"></a>
## Reproduction and bounded exploration

Run the fixed verifier from the repository root:

```powershell
python -B mathematics/computations/programs/Yin_J_G0151/two_atom_models.py
```

The default run uses only the standard library and frozen J151 helper functions.
It verifies the two cut counts, exact coverage of the five residual triples, distinct interior atoms, fixed/free coordinate separation, all forty rational systems and the strict occupancy control bounds.
The completed run passed all assertions in about 0.60 seconds.
It requires neither SciPy nor an exploratory output file.

The optional `--explore` mode proposes an equal-mass atom pair from the first two moments of the previous mass-two model, rounding the positions to rationals with denominator 4096.
For each triple it tries at most 25 pairs obtained by adding offsets in \(\{-2,-1,0,1,2\}/128\) to those two positions, trying the smallest total offset first.
Every LP fixes the two positions and their masses, leaving only the 256 occupancies as variables.
The search cap is 125 LPs or 60 seconds, with the remaining time passed to the LP solver.
The retained search found certified models for all five triples after 17 LPs and about 0.51 seconds in the solve loop.
Numerical failures in the tested neighborhood establish no infeasibility outside that finite search; only the ensuing exact rational checks support the result above.
No conductor, degree or parameter-window extension was used.
