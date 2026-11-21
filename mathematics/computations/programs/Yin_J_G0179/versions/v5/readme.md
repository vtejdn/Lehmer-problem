---
author: Yin
---

# Counting exterior roots for every middle coefficient of a reciprocal polynomial

<a id="pencil"></a>
## One rational circle for a family of integer polynomials

Let \(P_c(X)\in\mathbb Z[X]\) be reciprocal and monic of degree \(2h\), \(h\ge1\), with leading coefficients \(a_0=1,a_1,\ldots,a_{h-1}\), middle coefficient \(c\), and constant term one.
For any rational \(r>1\), the following count uses the same real root isolations for every \(c\).
It gives the number \(n_c(r)\) of roots outside \(|X|=r\), with multiplicities.
The roots of \(P_c\) are algebraic units.
If a root \(\alpha\) had modulus \(r\), the rational number \(\alpha\bar\alpha=r^2\) would be an algebraic unit greater than one, which is impossible.
This removes boundary exceptions at all rational radii above one.

Set \(x=\cos\theta\) and write
\[
 r^{-h}e^{-ih\theta}P_c(re^{i\theta})
   =c+A_r(x)+i\sin\theta\,D_r(x),
\]
where the Chebyshev polynomials give
\[
 A_r(x)=\sum_{j=1}^h a_{h-j}(r^j+r^{-j})T_j(x),\qquad
 D_r(x)=\sum_{j=1}^h a_{h-j}(r^j-r^{-j})U_{j-1}(x).
\]
The leading term at \(j=h\) makes \(D_r\) a nonzero polynomial of degree \(h-1\).
Let \(x_0=1>x_1>\cdots>x_s>x_{s+1}=-1\) consist of the endpoints and the distinct interior real zeros of \(D_r\).
Put \(u_j=\operatorname{sgn}D_r\) on \((x_{j+1},x_j)\) and \(I_j(c)=\mathbf1_{\{c+A_r(x_j)>0\}}\).
Then
\[
 n_c(r)=h-u_0 I_0(c)+u_s I_{s+1}(c)
                  -\sum_{j=1}^{s}(u_j-u_{j-1})I_j(c).
\]
Thus all integer middle coefficients can be treated by comparisons with a list of at most \(h+1\) real algebraic thresholds.

Indeed the winding number of the displayed curve is the number of roots inside the circle minus \(h\), by the argument principle.
Count its signed crossings of the positive real ray, counting passage from negative to positive imaginary part as \(+1\).
In the upper semicircle the sign on each intervening arc is \(u_j\).
An interior crossing and its complex conjugate contribute \(u_j-u_{j-1}\) together when \(I_j(c)=1\), including zero contribution from tangency.
Conjugation on the two sides of \(1\) and \(-1\) gives the endpoint contributions \(u_0 I_0(c)\) and \(-u_s I_{s+1}(c)\), including possible zeros of \(D_r\) at the endpoints themselves.
Subtracting the winding number from \(h\) gives the stated exterior count.
For general circle counts, Bistritz gives a separate sign-variation method for a fixed real polynomial. [Bistritz 1984](https://doi.org/10.1109/PROC.1984.12993)

<a id="measure"></a>
## Mahler bounds from several circles

For rational \(1=r_0<r_1<\cdots<r_m\) the root product gives
\[
                  M(P_c)\ \ge\ \prod_{i=1}^m(r_i/r_{i-1})^{n_c(r_i)}.
\]
Each root contributes the largest grid radius strictly below its modulus, or one if none occurs.
If \(n_c(r_m)=0\), the same product multiplied by \((\max_i r_i/r_{i-1})^h\) is an upper bound, since there are at most \(h\) exterior roots.
Refining the grid therefore gives two-sided enclosures of arbitrary precision.
Increasing the last radius past a coefficient root bound always makes the terminal count zero.

<a id="example"></a>
## Two middle coefficients in the degree-56 search

Let \(B=\Phi_{49}\Phi_{16}\Phi_9\), whose middle coefficient is 2, and compare \(B-X^{28}\), whose middle coefficient is 1.
Both polynomials have identical first 27 Newton sums and satisfy all [first-half trace bounds](../../readme.md#bounds), with \(s_{28}=-7\) and \(21\), respectively.
For direct verification the full sums for \(B\) are \(c_{49}(k)+c_{16}(k)+c_9(k)\), where \(c_m\) is the Ramanujan sum.
The first fifteen sums pass the [version-two cyclotomic tests](../v2/readme.md#sieve) because \(B\) has unit-circle roots and is coprime to all five tested cyclotomic polynomials.
Their support contains degrees with coprime differences, so neither is a power substitution.

| Polynomial | Roots above \(101/100\) | Roots above \(21/20\) | Roots above \(1089/1000\) |
| --- | ---: | ---: | ---: |
| \(B\) | 0 | 0 | 0 |
| \(B-X^{28}\) | 12 | 6 | 0 |

Thus the largest root modulus of the second polynomial is below \(1.089\), while six roots above \(1.05\) already give \(M>(21/20)^6>1.089\).
This shows how a necessary bound on each individual radius can leave a polynomial whose total measure is too large.
The [exact program](radial_counts.py) uses integer Chebyshev coefficients, rational isolation of the distinct real roots, and rational interval evaluations of the real part.
Run the following from the repository root with Python and SymPy.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v5/radial_counts.py
~~~

The program writes all six counts to \(\texttt{counts.json}\) in the v5 output directory.
