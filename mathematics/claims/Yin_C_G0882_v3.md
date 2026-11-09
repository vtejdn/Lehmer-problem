---
author: Yin
---

# Integer moments and partial whole-measure bounds at conductor 19683

<a id="statement"></a>
## The logarithmic cut and its necessary integer combinations

Let \(p=19683=3^9\), \(n=9841\), \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), and \(B=\prod_j(t-b_j)\).
Use \(D=B_{n-1}\) in the [odd-grid convention](../ledger/Yin_L_G0464_v5.md#odd-grid-product).
The logarithmic cut is \(k=\lfloor p/\log p\rfloor=1990\).
Let \(h\in\mathbb Z[t]\) be strictly positive at the first 7851 nodes and strictly negative at the last 1990 nodes, with absolute norm \(\Delta=\prod_j|h(b_j)|=2^{4391}\).
This is the norm supplied by the [integral sign construction](../ledger/Yin_L_G0464_v8.md#integral-sign-representative) at this cut.
For \(x\in\{-2,-1,0,1,2\}\), put
\[
 r_j=\frac{(4-b_j^2)h(b_j)}p,\qquad
 C=Dh\bmod B,\qquad Q=(t-2x)B+C,\qquad
 P=z^{n+1}Q(z+z^{-1}).
\]
Suppose \(K=\sum r_j=x^2+2\), \(L=\sum b_jr_j=-4x\), and \(P(-1)>0\).
Then the integers \(U=\sum r_j/(2+b_j)\) and \(N=\sum b_j^2r_j\) belong to the following necessary table.
Every displayed integer interval includes both endpoints.

| \(x\) | \((K,L)\) | \(U\) | Necessary \(N\) |
| ---: | --- | --- | --- |
| \(-2\) | \((6,8)\) | 3 | \(17,\ldots,21\) |
| \(-1\) | \((3,4)\) | 1 | \(7,8,9,10\) |
| 0 | \((2,0)\) | \(-1\) | \(-2,\ldots,5\) |
| 0 | \((2,0)\) | 0 | \(-1,\ldots,5\) |
| 0 | \((2,0)\) | 1 | \(1,\ldots,5\) |
| 0 | \((2,0)\) | 2 | \(3,4,5\) |
| 1 | \((3,-4)\) | \(-3,-2,-1\) | \(5,6,7\) |
| 1 | \((3,-4)\) | \(0,\ldots,5\) | \(6,7\) |
| 2 | \((6,-8)\) | \(-5,\ldots,-1\) | \(10,\ldots,15\) |
| 2 | \((6,-8)\) | \(0,\ldots,10\) | \(11,\ldots,15\) |
| 2 | \((6,-8)\) | \(11,12\) | \(12,\ldots,15\) |
| 2 | \((6,-8)\) | 13 | \(13,14,15\) |

The endpoint value is exactly \(P(-1)=2+2x+U\).
If the third moment also matches the [limiting profile](../ledger/Yin_L_G0464_v7.md#prefix-cut), so \(N=6+2x^2\), the table leaves only \(x=-1,N=8,U=1\) and \(x=2,N=14,-5\le U\le13\).
The table asserts necessary conditions for all inputs of the specified signs and norm.
Realization of its entries is unresolved.

For \(x=-1\), the complete multiplicative Mahler measure satisfies
\[
 N=9\quad\Longrightarrow\quad M(P)>25/16,\qquad
 N=10\quad\Longrightarrow\quad M(P)>49/25.
\]
In these two cases exactly two trace roots are nonreal conjugates, and all other trace roots lie in \((-2,2)\).
The complete-measure conclusions for the remaining cases \(N=7,8\), including extension of the \(6561\) bound \(2209/1600\), remain unresolved by these certificates.

<a id="argument"></a>
## Exact cut, valuations and integral layer sums

Take \(y=-161/100\).
For a rational \(u/v\) with \(v>0\), the recurrence
\[
 H_0=1,\qquad H_1=u+v,\qquad H_i=uH_{i-1}-v^2H_{i-2}
\]
has \(H_i=v^iB_i(u/v)\).
Interlacing counts the poles above the rational by the sign variations of \(H_0,\ldots,H_n\), omitting zeros.
At \(y\) and at \(y'=-16099/10000\), this gives exactly 7851 poles and \(p|H_n|>2v^n\).
Thus both rationals are in the prescribed gap and \(p|B(y)|>2\).
The [integer program](../computations/programs/Yin_J_G0151/conductor19683.py) verifies these statements by the displayed recurrence.
It also certifies \(k=1990\) using
\[
 \log3=2\sum_{j\ge0}\frac{(1/2)^{2j+1}}{2j+1}.
\]
After the first 40 terms, the omitted positive tail is at most \(2(1/2)^{81}/(81(1-1/4))\).
The resulting rational bounds put \(9\log3\) strictly between \(p/1991\) and \(p/1990\).

On the primitive layer of order \(3^\ell\), put \(d_\ell=3^{\ell-1}\) and \(F_\ell=1+T_{d_\ell}\), where \(T_d(z+z^{-1})=z^d+z^{-d}\).
The terminal-block counts divisible by successive powers of three are
\[
 (1990,663,221,74,25,8,3,1,0,0).
\]
Their successive differences, read from the bottom layer upwards, give negative-count parities
\[
 (\eta_1,\ldots,\eta_9)=(0,1,0,1,1,1,1,0,1).
\]
The sign-construction formula \(\sum_{e:\eta_{e+1}\ne\eta_e}(3^e-1)/2\), with \(\eta_0=0\), gives 4391.
Its representative has layer valuations \((5,4,3,2,2,2,2,1,0)\).

The [pure two-power layer argument](../ledger/Yin_L_G0464_v11.md#finite-exclusions) writes every input of the specified norm as \(h=2^{t_\ell}f_\ell\) on each layer, where \(t_\ell\ge0\) is integral and \(f_\ell\) is an integral unit there.
This uses irreducibility of \(F_\ell\) modulo two and the absence of odd prime factors in its norm.
The exponents satisfy \(\sum d_\ell t_\ell=4391\).
Since \(d_9=6561>4391\), one has \(t_9=0\).
The signed layer norm congruence modulo three then gives
\[
 (t_1,\ldots,t_9)\equiv(1,0,1,0,0,0,0,1,0)\pmod2.
\]
For any integral polynomial \(A\), \(d_\ell^{-1}\operatorname{Tr}_\ell A(b)\) is integral.
Indeed the monic polynomials \(1,T_1,T_2,\ldots\) form an integral basis for integral polynomials, and the primitive-root sums giving \(\operatorname{Tr}_\ell T_j\) lie in \(\{0,-d_\ell,2d_\ell\}\).

Apply this integrality and arithmetic-geometric mean to positive layer values of
\[
 (4-b^2)(100b+161)f_\ell(b),\quad
 (2-b)(100b+161)f_\ell(b),\quad
 (2-b)^2(100b+161)f_\ell(b),
\]
and of \((2-b)(4-b^2)(100b+161)f_\ell(b)\) and \((2-b)^3(100b+161)f_\ell(b)\).
Their absolute norms use respectively the factors \(3,3,9,9,27\), since \(\prod(2-b)=3\) and \(\prod(2+b)=1\) on a primitive layer.
Writing \(R_\ell=100^{d_\ell}|F_\ell(y)|\), the corresponding normalized traces are at least
\(I_{c,\ell}=\lceil(cR_\ell)^{1/d_\ell}\rceil\).
The exact values needed here are

| \(c\) | \((I_{c,1},\ldots,I_{c,9})\) | Minimum of \(\sum d_\ell2^{t_\ell}I_{c,\ell}\) |
| ---: | --- | ---: |
| 3 | \((183,171,109,106,100,101,101,101,101)\) | 1562883 |
| 9 | \((549,247,123,110,101,102,101,101,101)\) | 1580979 |
| 27 | \((1647,355,139,114,103,102,101,101,101)\) | 1623531 |

These integer roots are checked by integer powering, with \(T_{3d}=T_d^3-3T_d\) computing the successive \(R_\ell\).
All three minima over the stated parity and total-exponent constraints occur at \((5,4,3,2,2,2,2,1,0)\).
The program computes them by dynamic programming over the accumulated exponent, retaining the least cost for each exponent after each layer.
The displayed representative supplies an incumbent cost, so any partial cost exceeding it can be discarded.
For fixed earlier exponents, the next cost increases with the next exponent, making this cutoff exhaustive.
The same calculation with all weights one gives \(\sum d_\ell2^{t_\ell}\ge15407\).

<a id="moment-table-proof"></a>
## The endpoint, positive moments and cubic separator

Let
\[
 a_3=\frac{1562883}{1968300},\qquad
 a_9=\frac{1580979}{1968300},\qquad
 a_{27}=\frac{1623531}{1968300}.
\]
The preceding layer bounds give
\[
 \begin{aligned}
 T&=L-yK\ge a_3,\\
 s_0&=K-(2+y)U\ge a_3,\\
 J&=(4+y)K-L-4(2+y)U\ge a_9,\\
 W&=(2+y)L-2yK-N\ge a_9,\\
 E&=N-yL-6(L-yK)+16\{K-(2+y)U\}\ge a_{27}.
 \end{aligned}
\]
Here \(T,s_0,J,W,E\) are the sums of the five positive polynomial values above, divided by \(100p\) and with \(h=2^{t_\ell}f_\ell\) on each layer.
The value \(U\) is integral because \(B(-2)=(-1)^n\) and \(Q(-2)/B(-2)=-2-2x-U\).
The strict endpoint is equivalent to \(U\ge-1-2x\), and \(P(-1)=2+2x+U\).
The moments \(K,L,N\) are integral by the expansion of the integral rational function \(C/B\) at infinity.

Use the positive weights \((2-b_j)(b_j-y)h(b_j)/p\).
Their moments of orders zero, one and two are
\[
 s_0=K-(2+y)U,\qquad
 s_1=L-(2+y)K+2(2+y)U,\qquad
 s_2=N-(2+y)L+2(2+y)K-4(2+y)U.
\]
Their support has distinct nodes and every weight is positive, so strict Cauchy-Schwarz gives \(s_0s_2>s_1^2\).

The cubic \(H(t)=13t^3-15t^2-33t+40\) supplies one further integral inequality.
Its discriminant is \(-13851\), and
\[
 H(-161/100)=-4153/10^6<0,
 \qquad H(-16099/10000)=7485412113/10^{12}>0.
\]
Its unique real zero is consequently inside the prescribed gap, so \((2-b_j)H(b_j)h(b_j)>0\) at every node.
The normalized layer traces of \((2-b)H(b)f_\ell(b)\) are positive integers at least
\[
 (135,15,17,15,14,14,14,14,14).
\]
These bounds are the ceilings of \((3|\operatorname{Res}(F_\ell,H)|)^{1/d_\ell}\).
Their verification in the program uses only cubic quotient rings and integer determinants.
For \(H=At^3+at^2+bt+c\), replace \(t\) by \(s/A\) and use the monic polynomial \(s^3+as^2+Abs+A^2c\).
If \(V_d\) is the remainder of \(A^dT_d(s/A)\), the multiplication determinant of \(A^d+V_d\), divided by \(A^{2d}\), has absolute value \(|\operatorname{Res}(F_\ell,H)|\).
The recurrence \(V_{3d}=V_d^3-3A^{2d}V_d\) is taken in that quotient ring.
The nine absolute resultants have binary lengths \((6,10,35,102,304,920,2755,8263,24788)\), with the actual ceiling-root inequalities checked against their full integer values.
Optimization over all permitted layer valuations gives a weighted sum at least 219942.
Since the first four moments of \((2-b)h(b)/p\) are \(U,K-2U,L-2K+4U,N-2L+4K-8U\), this proves
\[
                  13N-41L+49K-58U\ge\frac{219942}{19683}.
\]

To obtain the necessary table, substitute each of the five pairs \((K,L)\) into these rational inequalities and enumerate integers \(U,N\).
There are explicit finite bounds
\[
 -1-2x\le U\le
 \left\lfloor\frac{(4+y)K-L-a_9}{4(2+y)}\right\rfloor,
\]
and, for each such \(U\),
\[
 \left\lceil a_{27}+yL+6T-16s_0\right\rceil
 \le N\le
 \left\lfloor(2+y)L-2yK-a_9\right\rfloor.
\]
Testing \(T,s_0,J,W,E\), strict Cauchy-Schwarz and the cubic inequality yields exactly the displayed necessary combinations.
Before the cubic inequality, the \(x=-1,U=1\) row also contains \(N=6\).
There its left side is \(13N-75\), which is 3 at \(N=6\), less than \(219942/19683\).
Substitution of \(N=6+2x^2\) gives the two remaining matching-third-moment profiles in the statement.

<a id="whole-measure"></a>
## The complete exterior cost for the larger third moments

Now set \(x=-1\).
The moment table gives \(U=1\) and \(N\in\{7,8,9,10\}\).
Let \(b_*\) be the smallest pole with positive residue, of decreasing-grid index 7851.
The separator and this index give \(y<b_*<-1\).
The [strict endpoint and same-sign pairing](../ledger/Yin_L_G0464_v12.md#pairing) choose \(n-1\) distinct roots of \(Q\) in \((-2,2)\), paired with the right poles of disjoint intervals.
They leave the pole \(b_*\) and two trace roots \(v_1,v_2\), counted with multiplicity.
For a real polynomial \(f\), write \(\mathcal D(f)=\sum_{Q(q)=0}f(q)-\sum_{B(b)=0}f(b)\).
The paired contribution is at most the negative variation \(V_-(f)\) on \([-2,2]\), so
\[
 \operatorname{Re}f(v_1)+\operatorname{Re}f(v_2)
 \ge\mathcal D(f)+f(b_*)-V_-(f).
\]

Take \(f(t)=-t^4+5t^3/3+3t^2/2-9t/4\).
Expansion of \(\log(Q/(tB))\) gives \(\mathcal D(t)=-2\), \(\mathcal D(t^2)=-2\), \(\mathcal D(t^3)=-2\), \(\mathcal D(t^4)=18-4N\), and hence \(\mathcal D(f)=73/6+4(N-8)\).
The derivative has roots \(-3/4,1/2,3/2\), yielding \(V_-(f)=2953/768\) and \(\max_{\mathbb R}f=387/256\).
Because \(f\) increases to the left of \(-3/4\), the pairing bound is strictly greater than
\[
 B_N=\frac{26972673}{12500000}+4(N-8).
\]
For \(N=9,10\), this exceeds \(2\max_{\mathbb R}f\).
Thus the two remaining trace roots are nonreal conjugates.
All matched roots lift to the unit circle, so the full lift has \(M(P)=\rho^2\), where \(\rho>1\) is the exterior radius of either remaining conjugate trace.

For \(R>1\), on the ellipse \(Re^{i\theta}+R^{-1}e^{-i\theta}\), the real part of \(f\) equals
\[
 g_R(t)=-3+\frac12\sum_{j=1}^4c_j(R^j+R^{-j})T_j(t),
 \qquad t=2\cos\theta,
 \qquad(c_1,c_2,c_3,c_4)=(11/4,-5/2,5/3,-1).
\]
The maximum principle for the harmonic function \(\operatorname{Re}f\) applies on the filled ellipse.
If \(B_N-2g_R\) is positive on \([-2,2]\), the conjugate traces lie outside that ellipse, and \(M(P)>R^2\).
The [exact quartic program](../computations/programs/Yin_J_G0151/exterior19683.py) gives the following Sturm certificates for this positivity.
Each sequence consists of the quartic, its derivative and the successive negative remainders.

| \(N\) | \(R\) | Signs at \(-2\) | Signs at \(2\) | Value at zero |
| ---: | ---: | --- | --- | --- |
| 9 | \(5/4\) | \(+,-,+,+,+\) | \(+,+,+,-,+\) | \(342366317/50000000\) |
| 10 | \(7/5\) | \(+,-,+,+,+\) | \(+,+,+,-,+\) | \(360468427873/30012500000\) |

The equal endpoint variations exclude roots of each quartic on the interval, and its positive value at zero fixes its sign.
This proves the two strict complete-measure bounds in the statement.

<a id="remaining-cases"></a>
## The scope of the failed inherited certificate

For \(N=8\), the same polynomial gives \(B_8-2\max_{\mathbb R}f=-43281183/50000000<0\).
At the old ellipse parameter \(R=47/40\), the quartic \(B_8-2g_R\) has value
\[
 -\frac{3772705508166056991}{1998717337600000000}
\]
at \(t=-3/4\).
Consequently that particular certificate does not establish the \(6561\) bound at the new conductor.
The existence of an admissible input with \(M(P)\le2209/1600\) remains unresolved.
Realization of the two remaining profiles \(x=-1,N=8\) and \(x=2,N=14\) at this conductor is unresolved.
Their possible use along growing conductors still requires a proof controlling the complete measure in arbitrarily small strict positive shells.

## Assessment history

### Decision whole-19683-moment-chamber

| Field | Value |
| --- | --- |
| date | 2026-11-09T08:54 |
| status | proved |
| reason | Independent review verified the complete necessary integer table over every fixed-norm input, the finite arithmetic certificates and both whole-measure implications, retaining the unresolved realization and remaining-measure cases. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conductor 19683 chamber](#statement) | Every specified integral input, all necessary integer combinations, strict endpoint and the two conditional complete-measure bounds. |
| argument | [Cut and integral layer sums](#argument) | Exact separator and norm, normalized traces and exhaustive valuation minimization. |
| argument | [Complete integer sieve](#moment-table-proof) | Positive sums, endpoint, cubic separator and all integer ranges. |
| argument | [Complete exterior measure](#whole-measure) | Every-root pairing, nonreal conjugacy and both rational ellipse certificates. |
| review | [Independent whole review](../audits/reviews/Yin_R_G1107_v8.md#whole-19683) | All statement and argument sections, direct inputs and both retained exact programs. |

## Current assessment

[Selected decision](#decision-whole-19683-moment-chamber)
