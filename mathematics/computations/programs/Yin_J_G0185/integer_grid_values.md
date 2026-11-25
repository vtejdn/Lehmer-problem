---
author: Yin
---

# Integer evaluations on neighborhoods of five adaptive interlacing grids

<a id="test"></a>
## Projecting the sign conditions onto an integer value

Let \(M=q(q+1)\), \(K=4M+1\), \(h=1/M\), and take a monic integral \(H\) on [the positive-pole branch](trace_grid.md#pole-weights) with \(M^nH(h)=K\).
For every positive integer \(a\),
\[
 H(-a)\equiv (-a)^n K\pmod{1+aM}.
\]
Indeed \(M^nH(1/M)\equiv M^n H(-a)\) in this residue ring, where \(M^{-1}\equiv-a\).
This test uses all coefficients, regardless of how many leading coefficients have passed reconstruction.

For an interlacing grid \(t_0,\ldots,t_{n-1}\), let \(Q(x)=\prod(x-t_i)\), \(Q_i=Q/(x-t_i)\), and \(\delta=K/\prod_i(1-Mt_i)\).
At every real \(x\) the [positive moment identity](../../../claims/Yin_C_G0345_v888.md#moments) reads
\[
 H(x)=\delta Q(x)+\sum_i b_i(x-h)Q_i(x),\qquad b_i>0,\quad\delta>0,\quad\delta+\sum_i b_i=1 .
\]
It suffices to enclose \(Q(-a)\) and all \((-a-h)Q_i(-a)\) in a common interval and compare its integers with the required residue.
For instance a zero value at \(-1,-2\) or \(-3\) would require \(1+aM\mid 4-a\), which is impossible for \(q\ge2\).

<a id="trials"></a>
## Simultaneous perturbations of the rational trial grids

Use the five rational grids of the [adaptive leading-coefficient experiment](adaptive_grid.md#trials).
Keep the endpoints fixed and allow each interior node to move by at most \(2^{-16}\) in the **trace coordinate** \(t\).
Keep the nodes in increasing order in \([-4,0]\).
The bounds below include the entire box of such choices.
The middle column encloses every possible integer value of \(H(-a)\) under the sign and positive-pole conditions before applying the displayed congruence.

| \(q\) | \(n\) | Coefficients passed on the central grid | \(-a\) | Possible integers in the enclosure | Required residue |
| ---: | ---: | ---: | ---: | :--- | :--- |
| 5 | 121 | 4 | -3 | \(-6,\ldots,0\) | \(1\bmod91\) |
| 5 | 481 | 9 | -2 | \(0\) | \(2\bmod61\) |
| 5 | 981 | 16 | -1 | \(0\) | \(3\bmod31\) |
| 6 | 643 | 13 | -1 | \(0\) | \(3\bmod43\) |
| 40 | 1643 | 4 | -2 | \(0\) | \(2048\bmod3281\) |

None of the five boxes can support a monic integral polynomial with the stated signature and pole value.
The free-grid prefix theorem gives no restriction placing its grids inside these boxes.

For a reproducible enclosure take the common denominator \(B=2^{40}\) of the central nodes and put each \(B(-a-t_i)\) in its integer-endpoint interval \(I_i\).
Write \(u_i=\max_{s\in I_i}|s|\) and \(P=\prod_i u_i\).
At scale \(MB^n\) the absolute bounds for the convex combination's entries are \(MP\) and \((1+aM)B(P/u_i)\), respectively.
The program permits both signs if a factor interval contains zero, and otherwise counts the wholly negative factors, with one extra negative sign for \(-a-h\).
It rounds the outer bounds inward to test the integer values.
The candidate centers are generated numerically and rounded to the rational nodes as in the original experiment; all enclosure and residue operations then use integers.
Run the [certificate](integer_grid_values.py) from the repository root:

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/integer_grid_values.py
~~~
