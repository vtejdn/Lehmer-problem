---
author: Yin
---

# Degree-seven full-measure certificates and their exact residual obstruction

<a id="scope"></a>
## Scope and finite result

This native J151 supplement continues the [negative-one branch at conductor 19683](../../../claims/Yin_C_G0882_v5.md#whole-measure).
Use all its hypotheses: \(p=19683\), \(n=9841\), \(k=1990\), the prescribed signs of the integral representative \(h\), \(|\operatorname{Res}(B,h)|=2^{4391}\), \(x=-1\), \((K,L)=(3,4)\), and the strict endpoint.
Write \(r_j=(4-b_j^2)h(b_j)/p\), and restrict to \(N=\sum b_j^2r_j=7\).
The endpoint and preceding necessary conditions give \(U=1\) and the eighteen necessary integer triples \((O,V,W)=(\sum b_j^3r_j,\sum b_j^4r_j,\sum b_j^5r_j)\) in C882v5.
No integer realization of those triples is assumed or asserted.

The [new native program](negative_one_seven.py) proves \(M(P)>26/25\) for eleven triples and \(M(P)>101/100\) for two more triples.
Consequently a member of this branch with \(M(P)\le101/100\) must have one of
\[
 (10,18,27),\quad(11,20,33),\quad(11,20,34),\quad(11,21,36),\quad(11,21,37).
\]
For each of these five residual triples the program gives an exact relaxed model with \(M=1\) at the level of every degree-at-most-seven test in the negative-variation and \(2\max f\) interface.
Thus this interface cannot prove a positive uniform gap over all eighteen triples, even if its numerical search is replaced by an exact optimizer.
The relaxed models are not integral representatives, actual trace-root multisets, or counterexamples to the original problem.
This supplement is an author computation and proof record, awaiting independent review and any claim adoption by the responsible main agent.

<a id="full-measure-certificates"></a>
## Thirteen strict complete-measure bounds

Let \(\mathcal D(f)=\sum_{Q(v)=0}f(v)-\sum_{B(b)=0}f(b)\), with multiplicity.
The trace differences for this branch are
\[
\begin{split}
 D_0&=1,\qquad D_1=D_2=D_3=-2,\qquad D_4=-10,\\
 D_5&=48-5O,\qquad D_6=-44+12O-6V,\\
 D_7&=-7O+14V-7W-2.
\end{split}
\]
They follow from the formal logarithm of
\[
 Q/(tB)=1+2/t+3/t^2+4/t^3+7/t^4+O/t^5+V/t^6+W/t^7+\cdots.
\]
The program recomputes them by the exact Newton recurrence.

Pair the \(n-1\) real roots supplied by the same-sign intervals and the left endpoint with their right poles, as in the [complete-root argument](../../../claims/Yin_C_G0882_v5.md#whole-measure).
Only \(b_*=b_{7851}\) remains unpaired; the other two trace roots \(v_1,v_2\) may be real, nonreal, or repeated.
For \(V_-(f)=\int_{-2}^2\max(0,-f')\), disjointness of the pairing intervals gives
\[
 \sum_{i=1}^2\operatorname{Re}f(v_i)
 \ge\mathcal D(f)+f(b_*)-V_-(f).
\]
The exterior radii of the remaining two reciprocal pairs satisfy \(M(P)=\rho_1\rho_2\); all paired trace roots lift to the unit circle.
With the convention \(T_j(z+z^{-1})=z^j+z^{-j}\), let \(f=\sum_{j=1}^7c_jT_j\).
If \(M(P)\le R\), then
\[
 \sum_{i=1}^2\operatorname{Re}f(v_i)
 \le2\max_{[-2,2]}f+
 \sum_{j=1}^7|c_j|(R^j+R^{-j}-2).
\]
Indeed the radial errors add to at most the error at the product radius, by superadditivity of \(\cosh(a)-1\) for nonnegative arguments.
This is a bound for the entire Mahler measure and uses no assumption that the two exceptional trace roots are nonreal.

Use \(y=-161/100\), \(z=-1006/625\), for which the exact recurrence gives \(y<b_*<z\).
The following table lists integer Chebyshev coefficients and a strict integer lower bound \(m_0\) for
\[
 \mathcal D(f)+\min_{[y,z]}f-V_-(f)
 -2\max_{[-2,2]}f
 -\sum_{j=1}^7|c_j|(R^j+R^{-j}-2).
\]
Every positive lower bound contradicts \(M(P)\le R\).
The constant terms of the even Chebyshev polynomials are included through \(D_0=1\).

| \((O,V,W)\) | \(R\) | \((c_1,c_2,c_3,c_4,c_5,c_6,c_7)\) | \(m_0\) |
| --- | --- | --- | ---: |
| \((10,17,25)\) | \(26/25\) | \((15314,-36720,21298,-5411,1201,11500,-8556)\) | 43320 |
| \((10,17,26)\) | \(26/25\) | \((0,-29710,20986,0,0,26010,-23294)\) | 147611 |
| \((10,18,26)\) | \(101/100\) | \((29758,-25680,19735,-12851,7585,-3203,1188)\) | 1125 |
| \((10,18,28)\) | \(26/25\) | \((0,-45036,26448,0,7315,6543,-14658)\) | 65839 |
| \((11,19,30)\) | \(26/25\) | \((0,-15282,10757,-4795,0,38237,30928)\) | 242102 |
| \((11,19,31)\) | \(26/25\) | \((-11460,-4342,31154,0,0,33406,19637)\) | 63475 |
| \((11,19,32)\) | \(26/25\) | \((23252,-28362,21851,-6555,-6239,9692,-4048)\) | 16844 |
| \((11,20,32)\) | \(26/25\) | \((-6946,0,39625,-13878,0,10776,28774)\) | 83851 |
| \((11,20,35)\) | \(101/100\) | \((32512,-28224,19621,-5385,-2892,6428,-4937)\) | 208 |
| \((12,22,39)\) | \(26/25\) | \((0,0,3728,0,-11941,20332,64000)\) | 399582 |
| \((12,22,40)\) | \(26/25\) | \((0,0,31714,-8155,-24787,11895,23449)\) | 133229 |
| \((12,23,42)\) | \(26/25\) | \((0,0,37803,-13400,-24145,-1108,23544)\) | 112108 |
| \((12,23,43)\) | \(26/25\) | \((-47375,0,26188,-2254,-14467,-2269,7447)\) | 9696 |

The verification uses the rational Bernstein bounds described in [C882v5](../../../claims/Yin_C_G0882_v5.md#rational-certificates), on 1024 equal rational subintervals of \([-2,2]\).
An interval where the derivative has certified sign contributes its exact variation and endpoint maximum.
On the remaining intervals, derivative Bernstein bounds give an upper bound for negative variation, and polynomial Bernstein bounds give an upper bound for the maximum.
A separate Bernstein lower bound over \([y,z]\) handles \(f(b_*)\).
All arithmetic in this verification is exact, including the radial cost at the stated rational \(R\).

<a id="exact-relaxed-models"></a>
## Five exact obstructions to this separation interface

The obstruction is stronger than a sampled LP returning zero.
For every residual triple and every
\[
 b\in[a,a+10^{-6}],\qquad a=-1609663/10^6,
\]
the program constructs a positive measure \(\nu_b\) of total mass two on \([-2,2]\), and a step function \(0\le w_b\le1\) on \([-2,2]\), such that
\[
 \mathcal D(f)+f(b)=\int_{-2}^2 f\,d\nu_b
                   -\int_{-2}^2w_b(t)f'(t)\,dt
 \tag{1}
\]
for every real polynomial of degree at most seven.
The odd-grid recurrence counts 7851 poles above \(a\) and 7850 above \(a+10^{-6}=-804831/500000\), so this whole-interval statement applies to the actual \(b_*\).

Here is a finite rational specification of the construction and verifier.
Put \(t_i=-2+i/64\), \(0\le i\le256\), and use the basis \(q_0=1\), \(q_j=T_j\) for \(1\le j\le7\).
Introduce nonnegative masses \(\alpha_i\) at \(t_i\), and occupancies \(\omega_i\in[0,1]\) on \([t_i,t_{i+1}]\).
Let \(A\) be the \(8\) by \(513\) rational matrix with
\[
 A_{j,i}=q_j(t_i)\quad(0\le i\le256),\qquad
 A_{j,257+i}=q_j(t_i)-q_j(t_{i+1})\quad(0\le i<256).
\]
Then (1) is exactly \(Au=g(b)\), where \(g_j(b)=\mathcal D(q_j)+q_j(b)\), \(u_i=\alpha_i\), and \(u_{257+i}=\omega_i\).
The row \(j=0\) enforces \(\sum_i\alpha_i=2\).

For each residual triple, the native `RELAXATIONS` table specifies the occupancy indices fixed at one, in inclusive integer ranges, and exactly eight free columns of \(A\).
All other coordinates are zero.
Expand the eight components of \(g(a+10^{-6}s)\) in the degree-seven Bernstein basis:
\[
 g(a+10^{-6}s)=\sum_{r=0}^7g^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
Each \(g^{(r)}\) is rational and is constructed from the shifted monomial coefficients with
\(\beta_r=\sum_{j=0}^r A_j\binom rj/\binom7j\).
After subtracting the fixed-one columns, solve the same eight-column rational system for each of these eight control vectors.
Exact Gaussian elimination and direct substitution verify all forty systems.
Every free coordinate is strictly greater than \(1/40\), and every free occupancy coordinate is strictly less than \(19/20\).
The following free-column table is included for locating the full finite certificates in the native source.

| \((O,V,W)\) | Eight free columns, numbered from zero |
| --- | --- |
| \((10,18,27)\) | 64, 68, 72, 257, 368, 413, 478, 510 |
| \((11,20,33)\) | 4, 53, 79, 260, 343, 424, 448, 493 |
| \((11,20,34)\) | 53, 79, 261, 338, 385, 435, 488, 506 |
| \((11,21,36)\) | 37, 53, 79, 260, 405, 454, 487, 504 |
| \((11,21,37)\) | 53, 79, 258, 355, 384, 459, 478, 500 |

Taking the Bernstein convex combination of these solutions gives \(u(b)\) for every \(b\) in the whole bracket.
Nonnegativity, the occupancy bounds, and \(Au(b)=g(b)\) are preserved by that convex combination.
Thus (1) is an exact identity for all polynomials in the stated space, not a statement confined to a sampled grid of polynomial tests or cut positions.

For every such \(f\), equation (1) implies
\[
 \mathcal D(f)+f(b)-V_-(f)
 =\int f\,d\nu_b-\int w_bf'-V_-(f)
 \le\int f\,d\nu_b
 \le2\max_{[-2,2]}f.
\]
The first inequality uses \(-\int w_bf'\le\int\max(0,-f')\), which follows pointwise from \(0\le w_b\le1\).
Hence no real degree-at-most-seven polynomial can make this complete-root separation margin positive even at \(R=1\).
Subtracting the nonnegative radial cost for any \(R>1\) cannot restore separation.

The obstruction identifies information discarded by this interface.
The measure \(\nu_b\) has total mass two but need not be two unit atoms at actual exceptional trace roots, and the step occupancy need not be an indicator of actual finite-pole pairing intervals.
The construction does not recover an integral \(h\), impose its full resultant, or realize the entire polynomial \(Q\).
A stronger argument using those constraints, or independently justified higher moments, remains possible.
No claim about impossibility of the original five branches follows from (1).

<a id="reproduction"></a>
## Reproduction and checked scope

Run from the repository root:

```powershell
python -B mathematics/computations/programs/Yin_J_G0151/negative_one_seven.py
```

The default run needs only the Python standard library and existing J151 native helper programs.
It verifies both pole brackets, recomputes the eighteen necessary triples, checks that the thirteen strict certificates and five residual models partition them exactly, verifies every strict rational margin, and checks all forty rational relaxed-model systems.
The completed default run passed all assertions and printed thirteen complete-Mahler bounds and five exact relaxed-model confirmations.
The optional `--explore` and `--relax` modes use SciPy only to propose polynomial coefficients or bases; their numerical outputs are not accepted as proofs.
Neither optional mode is needed to verify the retained certificates.
No higher degree, larger conductor, or additional enumeration window was used in this finite supplement.
