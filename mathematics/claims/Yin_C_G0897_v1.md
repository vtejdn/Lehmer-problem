---
author: Yin
---

# Frequent excursions of the normalized residues on the angular grid

<a id="statement"></a>
## Oscillations on the scale of the matching prefix

Take the [strict integral odd-grid chamber](Yin_C_G0893_v1.md#statement) with \(p=2n+1\to\infty\) and whole Mahler measures \(1<M(P)\to1\).
On a subsequence with one of the five coefficient profiles \(x\), put \(\theta_j=2\pi j/p,\ b_j=2\cos\theta_j\) and \(U_j=p\rho_j/(b_j-x)^2\) wherever \(b_j\ne x\).
Let \(L\le n+1\) be any matching index tending to infinity for that profile.
For any \(2<s<t<4\), there is a fixed compact finite union \(K\) of angular intervals in \((0,\pi)\), avoiding \(2\cos\theta=x\), and positive constants \(c,C\), depending only on \(s,t,x\), with the following properties for all sufficiently large conductors on the subsequence.

* At least \(cn\) nodes in \(K\) have \(U_j>t\).
* Every consecutive run of nodes in any one interval of \(K\) on which \(U_j>s\) has at most \(Cp/L\) nodes.
* At least \(c' L\) distinct such runs contain a node above \(t\), for a constant \(c'>0\).
  In particular the sum of the absolute differences of consecutive normalized residues within the intervals of \(K\) is bounded below by a positive constant times \(L\).

At \(t=3\), the fraction above \(3\) on the entire half grid has lower limit strictly greater than \(1/32\).
These are necessary conditions on the actual integer inputs in a shrinking sequence.
The constants allow both prime and composite odd conductors.

<a id="high-tail"></a>
## A positive density above every level below four

Every subsequential marginal limit \(\eta\) of the \(U_j\) is supported on \([0,\infty)\), has first moment at most two and has \(\iint\log|u-v|\,d\eta(u)d\eta(v)\ge0\) by the [normalized arithmetic law](Yin_C_G0893_v1.md#statement).
For \(2<t<4\) put \(g_t(u)=0\) on \([0,t]\) and \(g_t(u)=\operatorname{arcosh}(2u/t-1)\) on \((t,\infty)\).
We show that
\[
       \tfrac12\log(4/t)\le\int g_t\,d\eta
                  \le q\log\big(8/(tq)\big),\qquad q=\eta((t,\infty)).       \tag{1}
\]
For \(N\ge2\), write the Vandermonde determinant of \(N\) independent samples in the monic basis with first member 1 and degree \(k\) member \(2(t/4)^k T_k(2u/t-1)\), \(1\le k<N\), where \(T_k(\cos\phi)=\cos(k\phi)\).
By the cosine and hyperbolic cosine formulas, \(|T_k(2u/t-1)|\le\exp(k g_t(u))\).
Factor \(2(t/4)^k\) from column \(k\ge1\) and \(\exp((N-1)g_t(u_i))\) from row \(i\).
The remaining entries have modulus at most one, so their determinant has modulus at most \(N!\).
Take logarithms, integrate and divide by \(N(N-1)/2\).
The expected logarithm on the left after division is the nonnegative logarithmic energy, which is finite by the first moment.
The right side tends to \(\log(t/4)+2\int g_t\,d\eta\), proving the first inequality.
For \(u>t\) one has \(g_t(u)\le\log(4u/t)\).
Jensen's inequality on this tail and \(\int u\,d\eta\le2\) give the second bound, with zero as the limiting value at \(q=0\).

In particular \(q\) is bounded below by a positive number depending only on \(t\), uniformly over the limit laws.
When \(t=3\), the upper bound in (1) is increasing on \(0<q\le1/32\) and at \(1/32\) is strictly less than \(\tfrac12\log(4/3)\), since \(256/3<(4/3)^{16}\).
Continuity gives a uniform lower bound strictly greater than \(1/32\).
Tightness from the arithmetic law and the open-set inequality for weak convergence give these same lower bounds for the lower limiting empirical proportions.
Choose \(K\) by removing sufficiently short open angular neighborhoods of \(0,\pi\) and the profile angle \(2\cos\theta=x\) from \([0,\pi]\), including the endpoints themselves in the removed neighborhoods.
The angular grid is asymptotically uniform, so the removed proportion can be made less than half the lower bound at \(t\).
A possible omitted node \(b_j=x\) does not affect any proportion.
This proves the first assertion.

<a id="grid-filter"></a>
## A positive kernel tests each run

Let \(a\) be the angular-midpoint trace separating the two signs, and put \(D_p(b)=(b-a)(b-x)^2\).
Extend \(X_j=p(b_j-a)\rho_j>0\) evenly to the nonzero indices modulo \(p\), and set \(b_0=2,\ X_0=0\).
Write \(Y_j=X_j-2D_p(b_j)\) on the full grid.
The moments through degree \(L-2\) obey
\[
     \sum_{j=1}^n \rho_j f(b_j)=\langle (b-x)^2 f(b)\rangle
                                 \qquad (\deg f\le L-2),
\]
where brackets mean the arcsine probability average.
Indeed the [prefix coordinates and discrete orthogonality](Yin_C_G0881_v3.md#prefix-coordinates) give the formula on each \(E_i,\ 0\le i\le L-2\): the mean of \((b-x)^2E_i(b)\) is \(2+x^2\) for \(i=0\), \(-4x\) for odd \(i\), and \(4+x^2\) for positive even \(i\), by the finite cosine expansion of \(E_i\).
Apply the identity to \(f=(b-a)V\) with \(\deg V\le L-3\).
The polynomial \(D_pV\) has degree at most \(L<p\), so its full grid and arcsine averages agree by summing each nonconstant Fourier mode.
Evenness then gives
\[
              \frac1p\sum_{j=0}^{p-1}Y_j e^{ik\theta_j}=0
                              \qquad (|k|\le L-3).                         \tag{2}
\]
The sine modes cancel, and the node zero in (2) includes the contribution of \(D_p(2)\).

Put \(m=L-2\) and \(F_m(v)=m^{-1}|\sum_{k=0}^{m-1}e^{ikv}|^2\).
This nonnegative trigonometric polynomial has degree \(m-1\), constant coefficient one and full-grid mean one under every translation.
For \(d(v,0)\in(0,\pi]\), where \(d\) denotes circular angular distance, \(F_m(v)\le\pi^2/(m\,d(v,0)^2)\) by the sine formula.
Uniformly in its center \(\phi\), for every \(R\ge1\) and \(m\le p\) one has
\[
        \frac1p\sum_{d(\theta_j,\phi)>R/m}F_m(\theta_j-\phi)\le C_0/R .     \tag{3}
\]
In the shell \(2^kR/m<d\le2^{k+1}R/m\) there are at most \(2+2^{k+1}pR/m\) grid points.
Multiplying this count by the displayed pointwise bound and summing the geometric series gives (3) with an absolute \(C_0\).

One has \(|D_p|\le64\) on the grid and \(D_p(b_j)\ge d_K>0\) on \(K\) eventually, since the [shrinking cut](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) has \(a\to-2\).
Thus \(Y_j\ge-128\) everywhere, whereas \(U_j>s\) on \(K\) implies \(Y_j=(U_j-2)D_p(b_j)>(s-2)d_K=:h_0\).
Choose a fixed \(R\) with \((128+h_0)C_0/R<h_0\).
If a run of the specified kind spans angular length at least \(2R/m\), center \(F_m\) at the midpoint of its first and last nodes.
Every node of distance at most \(R/m\) then belongs to the run, for large \(m\) since \(K\) avoids both angular endpoints.
The full-grid average of \(Y_jF_m(\theta_j-\phi)\) is at least \(h_0-(128+h_0)C_0/R>0\), contradicting (2).
This bounds the size of each run by \(1+pR/(\pi m)=O(p/L)\).
The positive proportion of nodes above \(t\) now requires at least \(c'L\) different runs.
Except for the first run in each of the finitely many intervals, each such run is preceded within its interval by a node at or below \(s\).
Counting the increase to its node above \(t\) on disjoint segments gives the asserted variation bound.

## Assessment history

### Decision normalized-excursions

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:31 |
| status | open |
| reason | Submit the positive density and angular excursion bounds on a shrinking integer sequence for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Repeated angular excursions](#statement) | Positive density, lengths of runs and variation on interior intervals across all five profiles. |
| argument | [Mass above the threshold](#high-tail) | Monic Chebyshev basis in the Vandermonde bound and the open-set passage to the grids. |
| argument | [Filtered grid moments](#grid-filter) | Exact full-grid cancellation and angular localization of the positive kernel. |
| dependency | [Arithmetic normalized distributions](Yin_C_G0893_v1.md#statement) | Tightness, first moment and nonnegative logarithmic energy. |
| dependency | [Prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Integral basis and the exact moments through the matching degree. |
| dependency | [Shrinking cut](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | The angular midpoint tends to the left trace endpoint. |


### Decision normalized-excursions-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:40 |
| status | proved |
| reason | Adopt the positive density of high normalized residues and the linear lower bound on the number of excursions with increasing prefix length. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Repeated angular excursions](#statement) | Positive density, lengths of runs and variation on interior intervals across all five profiles. |
| argument | [Mass above the threshold](#high-tail) | Monic Chebyshev basis in the Vandermonde bound and the open-set passage to the grids. |
| argument | [Filtered grid moments](#grid-filter) | Exact full-grid cancellation and angular localization of the positive kernel. |
| dependency | [Arithmetic normalized distributions](Yin_C_G0893_v1.md#statement) | Tightness, first moment and nonnegative logarithmic energy. |
| dependency | [Prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Integral basis and the exact moments through the matching degree. |
| dependency | [Shrinking cut](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | The angular midpoint tends to the left trace endpoint. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v72.md#excursion-review) | Independent review of the tail inequality, exact full-grid moments, localized kernel and counting argument for each limiting profile. |

## Current assessment
[Selected decision](#decision-normalized-excursions-reviewed)
