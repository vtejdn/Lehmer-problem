---
author: Yin
---

# Exact reconstruction on sign grids for the first nonunit trace branch

<a id="solver"></a>
## One integer candidate on an arbitrary fixed grid

Put \(M=q(q+1)\), \(L=2q+1\), \(q\ge4\).
The [trace construction](../../../ledger/Yin_L_G0462_v324.md#pole) calls for a monic \(H\in\mathbb Z[x]\) of degree \(n\) with \(M^nH(1/M)=L^2\).
The following reconstruction permits any specified positive integer \(K=M^nH(1/M)\).
Write \(h=1/M\) and \(Q(x)=\prod_{i=0}^{n-1}(x-t_i)\), where \(-4=t_0<\cdots<t_{n-1}=0\).
Require \((-1)^{n-i}H(t_i)>0\) for every \(i\).
These signs and \(H(h)>0\) put one root strictly in every negative grid interval and the last root in \((0,h)\).
For each fixed grid and \(K\) there is at most one such \(H\), including reducible inputs.
For rational nodes its coefficients can be recovered or excluded using exact rational arithmetic with at most one candidate at each step.

Indeed \(r_i=-H(t_i)/Q'(t_i)>0\) and
\[
 \frac{H(x)}{Q(x)}=1-\sum_i\frac{r_i}{x-t_i}.
\]
At \(x=h\) this gives \(\sum_i r_i/(h-t_i)<1\), and hence \(0<s=\sum_i r_i<4+h\).
Denote by \(d_j,c_j\) the coefficients of \(x^{n-j}\) in \(Q,H\), respectively, taking \(d_0=c_0=1\).
Expansion at infinity gives the moments
\[
 \mu_{j-1}=\sum_i r_it_i^{j-1}
    =d_j-c_j-\sum_{\ell=1}^{j-1}d_\ell\mu_{j-1-\ell}.
\]
In particular \(c_1=d_1-s\) belongs to an interval of length \(4+h\).
For \(j\ge2\) let \(\phi_{j-1}(x)=2T_{j-1}((x+2)/2)\), where \(T_k\) is the Chebyshev polynomial of the first kind.
This is monic of degree \(j-1\) and has absolute value at most 2 on the grid.
Thus \(\sum_i r_i\phi_{j-1}(t_i)\) is an explicitly known number minus \(c_j\) once \(c_1,\ldots,c_{j-1}\) are known.
It lies strictly between \(-2s\) and \(2s\), since each of the two extremal level sets of this nonconstant polynomial of degree \(j-1<n\) omits at least one node.
Meanwhile \(K=1+\sum_{j=1}^n c_jM^j\) determines one residue class for \(c_j\bmod M\) from the preceding coefficients, and determines \(c_n\) exactly.
For \(q\ge4\) both interval lengths \(4+h\) and \(4s\) are strictly less than \(M\).
Starting at \(c_1\), at most one integer is possible at every step.
When all coefficients survive, direct evaluation at the grid nodes verifies the signs.
The bounds use only the positivity of \(K\), and the residue test uses its actual value.
The [program](trace_grid.py) obtains \(d_1,d_2,\ldots\) on demand using Newton's identities and builds the monic Chebyshev polynomials by their three-term recurrence.

More generally allow **any signed pole value** \(K\), and prescribe the positive root in \((0,2/q)\) as in the [full Salem signature](../../../claims/Yin_C_G0345_v883.md#statement).
Using \(H(2/q)>0\) in the partial fractions gives \(s<4+2/q\), with \(4(4+2/q)<M\) for every \(q\ge4\).
This proves the same uniqueness assertion, with a final positive endpoint check at \(2/q\).
In lower coefficient heights the procedure still applies whenever the intervals actually encountered contain at most one integer of the required residue.

<a id="lobatto"></a>
## Degree obstruction independent of the individual knots

Assume now \(K=L^2\), \(q\ge5\), \(n\ge6\), and suppose that the nodes satisfy
\[
 \sum t_i=-2n,\qquad 6n+2\le\sum t_i^2\le6n+3.
\]
This includes the shifted Chebyshev–Lobatto nodes \(t_i=-2-2\cos(\pi i/(n-1))\): their centered first moment vanishes by symmetry, and summing the double-angle cosine gives \(\sum(2+t_i)^2=2n+2\).
The same argument applies to rational grids with these moment bounds.
The first two coefficients of \(H=x^{n-1}(x+4)+(Mx-1)G\) have the form \(c_1=4+MA,\ c_2=MB-A\) with integral \(A,B\).
Write \(\mu=\sum r_it_i\).
Weighted Cauchy–Schwarz gives
\[
 s^2\le \left(\sum r_i(h-t_i)\right)\left(\sum\frac{r_i}{h-t_i}\right)<hs-\mu.
\]
The first factor is positive, and positivity at all nodes also gives \(\mu>-4s\).
Here \(s=2n-4-MA\) is an even integer in \((0,4+h)\), so \(s=2\) or \(4\).
By the node moments \(d_2=2n^2-3n-1-\varepsilon\) with \(0\le\varepsilon\le1/2\).
Consequently the integer
\[
 b=\mu+\varepsilon=2n^2-3n-1-2ns-c_2
\]
satisfies \(-4s<b<hs-s^2+\tfrac12\).
At \(s=4\) this permits no integer.
At \(s=2\) it gives \(b\in\{-7,-6,-5,-4\}\), \(n=3+MA/2\) and \(A>0\).
Reduction modulo \(M\) yields
\[
 b\equiv A-4-MA/2\pmod M .
\]
For even \(A\) the residue of \(A\) belongs to \(\{-3,-2,-1,0\}\bmod M\); for odd \(A\) it belongs to \(\{M/2-3,M/2-2,M/2-1,M/2\}\bmod M\).
In both cases
\[
 n\ge 3+\frac M2\left(\frac M2-3\right).
\]
For \(q=40\) this is \(n\ge669943\).
This bound concerns sign grids with the displayed node moments.
A polynomial with the desired roots could admit other interlacing nodes.

For a symmetric grid with \(\sum t_i^2=6n+2\), the first three centered coefficients of \(Q(x-2)\) below the leading term equal \(0,-(n+1),0\).
Thus \(d_3\) is integral as well.
The next residue moment \(\nu=\sum r_it_i^2\) is integral and obeys
\[
 \mu^2/s<\nu<-4\mu,\qquad
 \nu\equiv d_3-d_2s-d_1\mu+B\pmod M .
\]
The congruence follows from \(c_3=MC-B\) with integral \(C\), and the strict upper bound follows from \(t_i(t_i+4)<0\) at interior nodes.
For \(q=5,n=423\) the preceding test leaves \(s=2,\mu=-6,A=28,B=11831\).
Now \(18<\nu<24\) but \(\nu\equiv11\bmod30\).
This excludes all such symmetric grids at a degree that passes the first two residue tests.

<a id="uniform"></a>
## Equally spaced rational grids

For equally spaced nodes the integer \(H(-2)\) cannot vanish: otherwise \(x+2\) divides \(H\), so \(2M+1\) divides \(4M+1\), which is impossible.
If the signs hold, the root in \((0,h)\) and the negative interlacing roots give
\[
 1\le |H(-2)|<(2+h)U_m,\qquad
 U_m=\prod_{i=1}^{m}\max(|t_{i-1}+2|,|t_i+2|),\quad m=n-1.
\]
On increasing the number of intervals by two, the old grid rescales about \(-2\) by \(m/(m+2)\) and acquires one interval at each end with farthest distance two.
Thus \(U_{m+2}/U_m=4(m/(m+2))^m<1\) for \(m>2\), by the binomial expansion of \((1+2/m)^m\).
At \(q=5\), the upper bounds for \(n=16,17\) are \(1001423847424/1601806640625\) and \(403515/524288\), both below one.
All equally spaced grids are therefore excluded for \(q\ge5,\ n\ge16\).

<a id="runs"></a>
## Rational grids and reproduction

Run from the repository root with Python 3.10 or later:

~~~sh
python -B mathematics/computations/programs/Yin_J_G0185/trace_grid.py
~~~

The symmetric test uses \(n=4k+3\) rational nodes.
After shifting by two they consist of \(0,\pm2\) and the \(k\) quadruples \(\pm a,\pm b\) from
\[
 z=j/(3k+1),\qquad a=2(1-z^2)/(1+z^2),\qquad b=4z/(1+z^2),\qquad 1\le j\le k.
\]
Each pair has \(a^2+b^2=4\); the program checks distinctness and both moment identities over the rationals.
The four trials at \((q,n)=(5,63),(6,87),(40,1643),(5,423)\) fail the direct coefficient reconstruction at indices \(2,2,4,3\), respectively.
For a positive reconstruction control, the five nodes \(-4,-15/4,-3,-2,0\), modulus 30 and target 6762031 give exactly \(H=x^5+11x^4+43x^3+69x^2+36x-1\), the shifted trace polynomial of [Lehmer's number](readme.md#exclusion).
The program checks this coefficient vector, the pole value and all signs; this control uses a different pole value from the target branch.
On the three nodes \(-4,-2,0\), \(q=2\), and the signed pole target \(-5\), it also recovers the [actual section witness](witnesses.md#witness), \(H=x^3+5x^2+5x-1\).
Here the search uses \(H(1)>0\); the first residue interval gives \(s=1\), so the later interval widths are \(4<6\).

The additional trials replace each circular node \(t\) by \(t+\lambda t(t+4)/16\) with \(|\lambda|\le1\), which preserves strict ordering and the two endpoints.
The tested degrees at \(q=5,6\) are \(23,27,\ldots,123\); at \(q=40\) the degree is 1643.
For each degree, \(1\le A\le9\), and each \(s=1/2,1,\ldots,7/2\), choose \(\lambda=8(4+MA+s-2n)/(n-1)\) and retain it when \(|\lambda|\le1\).
Since the original sum of \(t(t+4)\) is \(-2(n-1)\), each retained grid passes the first coefficient test with \(c_1=4+MA\) and the specified mass \(s\).
Every subsequent count is from exact reconstruction.

| \(q\) | Grids | First failure \(c_2\) | \(c_3\) | \(c_4\) | \(c_6\) | \(c_7\) | Solutions |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 107 | 77 | 21 | 6 | 3 | 0 | 0 |
| 6 | 86 | 60 | 24 | 0 | 1 | 1 | 0 |
| 40 | 7 | 2 | 0 | 5 | 0 | 0 | 0 |

The 200 tested triples of height, degree and deformed grid are not a covering of all root configurations.
The general reconstruction reduces the remaining question to finding a set of nodes whose single possible coefficient vector passes the norm and sign checks.

<a id="pole-weights"></a>
## A sharper coefficient interval from the exact pole value

Use the same grid, signs and partial fraction expansion as in the [unweighted reconstruction](#solver).
Define \(b_i=r_i/(h-t_i)>0\) and \(\beta_j=\sum_i b_i t_i^j\).
The pole value determines their total mass exactly:
\[
 D=\beta_0=1-\frac{K}{M^nQ(h)}
           =1-\frac{K}{\prod_i(1-Mt_i)}.
\]
If \(D\le0\), the grid cannot work.
Otherwise \(\beta_j=h\beta_{j-1}-\mu_{j-1}\) for \(j\ge1\).
Given \(c_1,\ldots,c_{j-1}\), the unweighted recurrence expresses \(\mu_{j-1}\) as a known quantity minus \(c_j\).
Hence \(\beta_j\) is a known quantity plus \(c_j\).
Since \(\phi_j=2T_j((x+2)/2)\) is monic for \(j\ge1\), \(\sum_i b_i\phi_j(t_i)\) has the same form.
The bound \(|\phi_j|\le2\) puts \(c_j\) in an explicit closed interval of width \(4D\), including at \(j=1\).
When \(4D<M\), this interval intersects the required coefficient residue class in at most one integer.
For \(K>0\) the denominator in the expression for \(D\) is positive, so every feasible grid has \(0<D<1\).
This proves fixed-grid uniqueness and deterministic reconstruction for every \(q\ge2\) on the positive-pole branch.
For signed \(K\), intersecting the two coefficient intervals preserves the signed result of the unweighted reconstruction.

The program uses the original intervals by default and adds the pole-weighted interval when called with `pole_weights=True`.
It recovers both control polynomials in [the trials](#runs) with either choice.
On the same 200 deformed grids the additional bound excludes 99 of the 107 grids at \(q=5\) at \(c_2\) and the other 8 at \(c_3\).
At \(q=6\) the counts are 69 and 17, respectively, and at \(q=40\) all 7 fail at \(c_2\).
