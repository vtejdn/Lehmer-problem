---
author: Yin
---

# The two smallest independent signed rows at width nine

<a id="minima"></a>
## Ten coefficients at a quartic Salem number and its square

Let \(\delta>1\) be the Salem root of \(P=X^4-X^3-X^2-X+1\), and put \(P_2=X^4-3X^3+X^2-3X+1\), the minimal polynomial of \(\delta^2\).
For exponent \(n\), sign \(\varepsilon\) and formal width \(b\), set
\[
 F_{n,b}(A)=A(X^n)+\varepsilon X^{nb+1} A(X^{-n}).
\]
At \(b=9\) consider the lattice of all \(A\in\mathbb Z[Y]\) of degree at most nine satisfying \((PP_2)^2\mid F_{n,9}(A)\).
Write \(\lambda_1\) for the least one-norm of a nonzero row and \(\lambda_2\) for the least height at which two linearly independent rows both have one-norm at most that height.
At every tested exponent and sign the shortest row is unique up to sign, and the shortest row independent of it is also unique up to sign.
They form a basis of the integer lattice, use all ten coefficients, and satisfy \(A(c^n)\ne0\) at all eight roots \(c\) of \(PP_2\).

In the table, \(L(h)=1+\lfloor\log_2 h\rfloor\), and each pair gives the positive sign first.
Let \(H_9\) be the least one-norm of a nonzero width-nine row with a vanishing coefficient, and \(H_8\) the one-norm of the primitive width-eight row.
At width nine the cheapest omission was uniquely the constant coefficient for each sign and exponent.

| \(n\) | \(L(\lambda_1)\) | \(L(\lambda_2)\) | \(L(H_9)\) | \(\lfloor\log_2(H_9/\lambda_1)\rfloor\) | \(\lfloor\log_2(H_8/\lambda_1)\rfloor\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 118, 118 | 119, 120 | 204, 203 | 85, 85 | 78, 79 |
| 32 | 259, 259 | 261, 260 | 451, 450 | 191, 190 | 182, 181 |
| 64 | 521, 520 | 522, 522 | 900, 899 | 379, 378 | 368, 368 |
| 128 | 1068, 1067 | 1068, 1069 | 1845, 1845 | 776, 778 | 764, 765 |
| 256 | 2222, 2223 | 2225, 2225 | 3857, 3858 | 1634, 1634 | 1619, 1616 |

For example, the two exact shortest norms at \(n=16\) in sign order are
\[
 272978476515842613584148295119028710,\qquad
 186343884414936271411773206923651863.
\]
The nine-position comparisons at \(n\le128\) reproduce the [earlier circuit calculation](../v5/readme.md#sample).
The asymptotic growth of the two width-nine minima remains open in this computation.

<a id="enumeration"></a>
## Exhausting the rank-two lattice

The [integer kernel and Gauss reduction](../../readme.md#method) give a reduced basis \(u,v\) for each signed matrix of remainders modulo \((PP_2)^2\).
Write \(a=u\cdot u,\ b'=u\cdot v,\ c=v\cdot v\) and \(D=ac-(b')^2\).
The program checks that the \(2\times 2\) minors \(p_{ij}=u_iv_j-u_jv_i\) have gcd one and sum of squares \(D\), so \(\sqrt D\) is the Euclidean covolume of the saturated lattice in its plane.
The basis itself gives the upper bound \(H=\max(\|u\|_1,\|v\|_1)\) for both minima.
Every eligible \(iu+jv\) of one-norm at most \(H\) has Euclidean norm at most \(H\) and hence satisfies
\[
        (ai+b'j)^2+Dj^2\le aH^2 .
\]
One sign per nonzero row suffices, so take \(j>0\) or \(j=0,\ i>0\).
Integer square roots bound both coordinates in this ellipse, and filtering by the actual one-norm leaves between two and seven vectors in each of the ten lattices.
Sorting by norm gives the first minimum and the least norm among the vectors independent of that minimizer.
The gcd of the minors of these two witnesses is also one, which checks that they generate the full lattice.

For each coordinate \(j\) the nonzero row \(v_j u-u_j v\) spans the omitted-coordinate line.
Dividing by its content gives the primitive row, and its other nine coefficients are all nonzero in every sample.
For both minima and all ten omission lines, integer long division of the expanded \(F_{n,9}(A)\) gives zero remainder modulo each of \(P^2,P_2^2\).
The expanded \(A(X^n)\) gives a nonzero remainder modulo each of the irreducibles \(P,P_2\), which checks genuineness.

<a id="reproduce"></a>
## Reproducing the exact coefficients and covolumes

Run the [program](quartic_minima.py) from the repository root with Python 3.10 or later and its standard library.

~~~text
python -B mathematics/computations/programs/Yin_J_G0177/versions/v6/quartic_minima.py
~~~

The [generated data](../../../../outputs/Yin_J_G0177/versions/v6/results.json) contain the reduced bases, their Gram entries and exact squared covolumes, both attaining coefficient vectors in ascending degree order, the enumeration ceilings and counts, and the individual comparison norms.
