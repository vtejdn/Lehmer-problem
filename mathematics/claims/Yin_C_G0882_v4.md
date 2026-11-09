---
author: Yin
---

# A complete Mahler bound for the positive-two profile at conductor 19683

<a id="statement"></a>
## Precise statement

Retain the full [conductor-19683 hypotheses and notation](Yin_C_G0882_v3.md#statement): \(p=19683\), \(n=9841\), \(b_j=2\cos(2\pi j/p)\), \(B=\prod_j(t-b_j)\), \(D=B_{n-1}\), and an integral \(h\) strictly positive at the first 7851 nodes and strictly negative at the last 1990 nodes, with \(\prod_j|h(b_j)|=2^{4391}\).
Put
\[
 r_j=(4-b_j^2)h(b_j)/p,\qquad C=Dh\bmod B,\qquad
 Q=(t-4)B+C,\qquad P=z^{n+1}Q(z+z^{-1}).
\]
Suppose
\[
 K=\sum_jr_j=6,\qquad L=\sum_jb_jr_j=-8,\qquad
 N=\sum_jb_j^2r_j=14,\qquad P(-1)>0.
\]
Then the integer fourth residue moment \(O=\sum_jb_j^3r_j\) satisfies \(O\ge-20\), and the complete multiplicative Mahler measure satisfies
\[
                         M(P)>5/4.
\]
This covers every integer input of the specified signs and norm, including all endpoint values \(U=\sum_jr_j/(2+b_j)\in\{-5,\ldots,13\}\) allowed by the preceding necessary table.
It does not assert realization of any table entry.
The earlier integer table and the \(x=-1,N=9,10\) bounds retain their [existing fixed proof](Yin_C_G0882_v3.md#decision-whole-19683-moment-chamber).
The \(x=-1,N=7,8\) complete-measure cases remain unresolved here.

<a id="layer-bound"></a>
## An integral fourth-moment separation

Take \(y=-161/100\), which lies strictly inside the specified sign-change gap by the [exact separator calculation](Yin_C_G0882_v3.md#argument).
The weights \(\mu_j=(b_j-y)r_j\) are strictly positive.
The given moments imply
\[
 \sum_j\mu_j=83/50,\qquad \sum_jb_j\mu_j=28/25,
 \qquad \sum_jb_j^2\mu_j=O+1127/50.
\]
Consequently
\[
 A=\sum_j\mu_j(b_j-2/3)^2=O+9803/450.
\]
Integrality of \(O\) follows from the Laurent expansion at infinity of \(C/B\), since both polynomials are integral and \(B\) is monic.

On primitive layer \(\ell\), let \(d_\ell=3^{\ell-1}\) and \(F_\ell=1+T_{d_\ell}\), with \(T_j(z+z^{-1})=z^j+z^{-j}\).
The [pure two-power norm decomposition](Yin_C_G0882_v3.md#argument) writes every allowed input as \(h=2^{t_\ell}f_\ell\) on that layer, with \(f_\ell\) an integral unit and
\[
 t_\ell\ge0,\qquad \sum_\ell d_\ell t_\ell=4391,\qquad
 (t_1,\ldots,t_9)\equiv(1,0,1,0,0,0,0,1,0)\pmod2.
\]
The trace divided by \(d_\ell\) of any integral polynomial in the layer coordinate is an integer.
Apply this fact and arithmetic-geometric mean to the positive layer values
\[
 (4-b^2)(100b+161)(3b-2)^2f_\ell(b).
\]
None vanishes, since \(2/3\) is not an algebraic integer, the separator misses every pole, and the unit is nonzero.
Since \(\left|\operatorname{Norm}_\ell(4-b^2)\right|=3\), their normalized trace is at least
\[
 I_\ell=\left\lceil\left(
 3|\operatorname{Res}(F_\ell,100t+161)|
 |\operatorname{Res}(F_\ell,3t-2)|^2
 \right)^{1/d_\ell}\right\rceil.
\]
Exact integer powering gives
\[
 (I_1,\ldots,I_9)=(4575,1216,1010,900,916,904,904,901,900).
\]
For reproduction, if \(u/v\) is a rational with positive denominator, the successive absolute resultants of \(vt-u\) are obtained by starting at \((u,v)\), recording \(|u+v|\), and replacing the pair by \((u^3-3uv^2,v^3)\).
This is the identity \(T_{3d}=T_d^3-3T_d\) applied to \(v^{d}F_\ell(u/v)\).
The [retained exact program](../computations/programs/Yin_J_G0151/higher_moments19683.py) evaluates both recurrences and the integer ceiling roots.
The exhaustive valuation minimization justified in the preceding [layer argument](Yin_C_G0882_v3.md#argument), with these new positive weights, gives
\[
 \sum_\ell d_\ell 2^{t_\ell}I_\ell\ge14032098.
\]
The minimum is attained at the admissible valuation vector \((5,4,3,2,2,2,2,1,0)\); this assertion concerns valuation vectors and does not construct a global moment hit.
Summing the layer traces yields
\[
 A\ge\frac{14032098}{900p}=\frac{779561}{984150}.
\]
At \(O=-21\), however, \(A=353/450<779561/984150\).
Thus integrality forces \(O\ge-20\).

<a id="whole-measure"></a>
## A fifth-degree test controlling every exterior root

The strict endpoint and the signs of the residues give \(n-1\) distinct trace roots in \((-2,2)\), using the leftmost interval and every same-sign gap as in the [root-pole pairing](../ledger/Yin_L_G0464_v12.md#pairing).
Pair each of these roots with the pole at the right end of its interval.
The unpaired pole is \(b_*=b_{7851}\), and there remain two trace roots \(v_1,v_2\), counted with multiplicity.
Because \(7851>p/3\), one has \(y<b_*<-1\).
For any real polynomial \(f\), write
\[
 \mathcal D(f)=\sum_{Q(q)=0}f(q)-\sum_{B(b)=0}f(b),
 \qquad V_-(f)=\int_{-2}^{2}\max\{-f'(t),0\}\,dt.
\]
The disjoint paired intervals imply
\[
 \operatorname{Re} f(v_1)+\operatorname{Re} f(v_2)
 \ge\mathcal D(f)+f(b_*)-V_-(f).
\]

Choose
\[
 f(t)=-(t-2)^2(t+1)^2(t+2)
      =-t^5+7t^3+2t^2-12t-8.
\]
Then \(f\le0\) on \([-2,2]\) and
\[
 f'(t)=-(t-2)(t+1)(5t^2+5t-6).
\]
The roots \(r_-\in(-2,-1)\) and \(r_+\in(0,1)\) of the quadratic are the two negative minima.
Since
\[
 f(t)\equiv(-248-116t)/25\pmod{5t^2+5t-6},
 \qquad r_-+r_+=-1,
\]
one has \(V_-(f)=-f(r_-)-f(r_+)=76/5\).
The quadratic is negative at \(y\), so \(r_-<y<b_*<-1\); hence \(f(b_*)>f(y)\).

Expanding the logarithm of
\[
 \frac{Q(t)}{tB(t)}=1-4t^{-1}+6t^{-2}-8t^{-3}+14t^{-4}+Ot^{-5}+O(t^{-6})
\]
gives
\[
 \bigl(\mathcal D(1),\mathcal D(t),\ldots,\mathcal D(t^5)\bigr)
       =(1,4,4,16,16,-56-5O).
\]
Therefore \(\mathcal D(f)=5(O+24)\ge20\), and
\[
 \operatorname{Re} f(v_1)+\operatorname{Re} f(v_2)
 >20+f(y)-76/5=\frac{29087946801}{10^{10}}.
\]

The exact Chebyshev expansion is \(f=-T_5+2T_3+2T_2-T_1-4\).
For each exceptional trace write \(v_i=\lambda_i+\lambda_i^{-1}\), choosing \(\lambda_i=\rho_i e^{i\theta_i}\) with \(\rho_i\ge1\).
All paired trace roots lift to the unit circle, so the complete measure is \(M(P)=\rho_1\rho_2\).
For \(E_j(s)=s^j+s^{-j}-2\), direct substitution gives
\[
 \left|\operatorname{Re}T_j(v_i)-T_j(2\cos\theta_i)\right|\le E_j(\rho_i).
\]
Moreover \(E_j(a)+E_j(b)\le E_j(ab)\) for \(a,b\ge1\), by the addition formula for \(\cosh\) with nonnegative arguments.
Using \(f(2\cos\theta_i)\le0\) thus gives
\[
 \operatorname{Re} f(v_1)+\operatorname{Re} f(v_2)
 \le E_5(M(P))+2E_3(M(P))+2E_2(M(P))+E_1(M(P)).
\]
This argument allows real as well as nonreal exceptional trace roots and counts both reciprocal pairs with multiplicity.
At \(M=5/4\) the right side is \(8847001/3200000\), smaller than the strict lower bound by \(360267169/2500000000>0\).
Each \(E_j\) is increasing on \([1,\infty\)), so \(M(P)>5/4\).
The displayed numerical rational bounds are reproduced by the retained program.

<a id="moving-cut"></a>
## A conductor-independent obstruction to fourth-moment matching

More generally, let an odd full trace grid carry nonzero residues with the same single-cut sign convention, and suppose its gap contains a separator \(y\ge-12/7\).
It cannot have simultaneously \((K,L,N,O)=(6,-8,14,-24)\).
Indeed every \(b_j\ne0\), and positivity gives
\[
 0<\sum_jb_j^2(b_j-y)r_j=O-yN=-24-14y\le0,
\]
a contradiction.
This four-moment obstruction does not require the specified norm or the strict endpoint.
The bound \(M(P)>5/4\) above uses both and remains specific to the conductor-19683 class.
Neither assertion excludes arbitrarily small positive measures along cuts whose separators tend to \(-2\).

## Assessment history

### Decision fourth-moment-whole-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T12:15 |
| status | proved |
| reason | Independent inspection verified the bound for every fixed-norm input, the exhaustive layer calculation, complete reciprocal-root cost and separate moving-cut obstruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Positive-two profile](#statement) | All specified integral inputs and the strict complete Mahler bound. |
| argument | [Fourth integral moment](#layer-bound) | Every valuation allocation and the integer separation O at least -20. |
| argument | [Whole exterior cost](#whole-measure) | Root pairing, exact fifth-degree test and both exceptional reciprocal pairs. |
| argument | [Moving-cut obstruction](#moving-cut) | Every odd full grid at the stated separator threshold, without a norm or endpoint assumption. |
| dependency | [Conductor-19683 inputs](Yin_C_G0882_v3.md#argument) | Exact cut, normalized layer integrality, valuation parities and exhaustive minimization. |
| dependency | [Root-pole pairing](../ledger/Yin_L_G0464_v12.md#pairing) | Disjoint real intervals and complete exceptional-root accounting. |
| review | [Independent fourth-moment finding](../audits/reviews/Yin_R_G1107_v9.md#fourth-moment-whole-19683) | Complete new statement and proof, exact program and necessary direct interfaces. |

## Current assessment

[Selected decision](#decision-fourth-moment-whole-19683)
