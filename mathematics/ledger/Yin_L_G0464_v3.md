---
author: Yin
---

# A fourth-root bound on agreement with a cyclotomic prefix

<a id="central-control"></a>
## A neutral comparison in the strict sign chamber

Use the [one-transition Chebyshev model](Yin_L_G0464_v2.md#rational-prefix), \(B=U_{d-1}(t/2)\), \(P=z^dQ(t)\), \(F=P/B^*\).
For odd \(d\ge3\) take \(Q_0=t(B+U_{d-2}(t/2))\).
At the grid points \(b_j=2\cos(j\pi/d)\) the residues are \(2b_j\sin^2(j\pi/d)/d\), and \(Q_0(-2)/B(-2)=-2/d\).
The residues therefore have a strict single transition at zero.
The finite lift is \((1+z^2)(1-z^{2d-1})/(1-z)\) by the sine formula, hence \(M(P_0)=1\).
Its coefficient limit is \(P_*=(1+z^2)/(1-z)\), and the normalized limit is \(F_0=(1-z^2)P_*=(1+z)(1+z^2)\).
This supplies an exact control for agent-S's proposal to test whether new positive measures can hide after a long central prefix.

<a id="fourth-root"></a>
## A necessary scale for the first differing coefficient

Consider any sequence of integral inputs on the same grid, with strictly negative then strictly positive residues in increasing order, the left endpoint condition, \(d\to\infty\), and \(0<\log M(P)\to0\).
Let \(L\le d\) be the length in the following convention: \(P\) agrees with \(P_*\) through degree \(L\), or equivalently \(F\) agrees with \(F_0\) through that degree since \(B^*=(1-z^{2d})/(1-z^2)\).
Then \(L=o(d^{1/4})\).
In particular placing the first difference at distance comparable to the fourth root of the trace degree cannot refute Lehmer in this chamber.

Take \(c\) at the arithmetic midpoint of the transition gap, \(\sigma=\sum_i r_i\delta_{b_i}\), \(\mu=(t-c)\sigma\ge0\), and \(V=\sum |r_i|\).
It suffices to consider subsequences with \(L\to\infty\).
Expanding
\[
 F=1-az+z^2+z^2\int(1-tz+z^2)^{-1}\,d\sigma(t)
\]
and comparing with \(F_0=1+z+z^2+z^3\) shows \(a=-1\) and \(\int U_j(t/2)d\sigma=\mathbf 1_{j=1}\) for \(0\le j\le L-2\).
With \(d\nu(t)=\sqrt{4-t^2}\,dt/(2\pi)\) on \([-2,2]\), the substitution \(t=2\cos\theta\) and sine orthogonality give \(\int U_j(t/2)t\,d\nu=\mathbf 1_{j=1}\).
Therefore \(\sigma\) and \(t\nu\) agree on every polynomial through degree \(L-2\).
In particular \(\mu([-2,2])=\int(t-c)t\,d\nu=1\).

<a id="cut-localization"></a>
### Exact localization of the moving cut by quadrature

Choose the largest odd \(h\) with \(2h\le L+1\).
The \(h\)-node quadrature for \(\nu\) has nodes \(u_j=2\cos(\pi j/(h+1))\), weights \(2\sin^2(\pi j/(h+1))/(h+1)>0\), and is exact through degree \(2h-1\).
Indeed divide by \(U_h(t/2)\); the multiple has zero integral by orthogonality and vanishes at the nodes, and the remainder is integrated by discrete sine orthogonality.
These nodes include zero and its two nearest neighbors \(\pm v\), \(v=2\sin(\pi/(h+1))\).
Choose a polynomial \(g\) of degree \(h-2\) vanishing at every node except \(0,v\) and nonzero at \(v\).
Since \(2h-3\le L-2\), positivity and moment agreement give
\[
 0\le\int g^2\,d\mu=\int g^2(t)(t-c)t\,d\nu(t).
\]
Only the \(v\) term survives quadrature, so \(c\le v\).
Using \(0,-v\) instead yields \(c\ge-v\), hence \(|c|\le v=O(1/L)\).

<a id="localized-mass"></a>
### Mass near the cut and the complete rate

Choose an odd \(m\asymp L\) with \(4(m-1)+1\le L-2\) and \(m|c|\le1/2\); a sufficiently small fixed fraction of \(L\) works by the preceding bound.
The even polynomial
\[
 G_m(t)=\frac{T_m(t/2)}{m\,t/2}
\]
has degree \(m-1\), with its removable value at zero.
Writing \(t/2=\sin s\) gives \(|T_m(t/2)|=|\sin(ms)|\), so
\[
 |G_m(t)|\le\min(1,2/(m|t|)),\qquad |G_m(t)|\ge 2/\pi\quad(|t|\le1/m).
\]
For the lower bound use \(m|\arcsin(t/2)|\le\pi/2\) on this range and \(|\arcsin(t/2)|\ge|t|/2\).
Moment agreement applies to \((t-c)G_m^4\).
Splitting at \(|t|=1/m\), the displayed upper bound and the bounded density of \(\nu\) give
\[
 \int G_m^4\,d\mu
 \le \int G_m^4 (t^2+|c||t|)\,d\nu
 \ll m^{-3}+|c|m^{-2}\ll m^{-3}.
\]
The lower bound on \(G_m\) thus bounds \(\mu([-1/m,1/m])\) by \(O(m^{-3})\).
For large \(L\) the cut is interior near zero, so the width of its Chebyshev gap is bounded below by a constant times \(1/d\); the arithmetic midpoint is at least half that width from every pole.
On the complement of this inner interval, \(|b_i-c|\ge1/(2m)\).
Consequently
\[
   |c|V=|c|\sum_i\frac{\mu_i}{|b_i-c|}
      \ll |c|(d\,m^{-3}+m)\ll 1+d/L^4 .
\]
On a positive shrinking-shell sequence the [fixed weight \(A(t)=t\)](../claims/Yin_C_G0880_v2.md#moving-cut) requires \(|c|V\to\infty\).
Thus \(d/L^4\to\infty\) on every subsequence with \(L\to\infty\), proving the result.
The argument does not bound the first differing coefficient for another cyclotomic prefix or supply new positive values when the prefix is shorter.
