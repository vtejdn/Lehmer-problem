---
author: Yin
---

# Integer perturbations at a quadratic zero of the grid phase

<a id="statement"></a>
## Local bounds from a strict cut

Let \(p=2n+1\) be odd, \(\theta_j=2\pi j/p\), \(b_j=2\cos\theta_j\), and \(M=\lfloor p/100000\rfloor\ge4\).
Let \(H\) be a real polynomial of degree at most \(M\), and suppose that the numbers
\[
                    w_j+(-1)^{j+1}H(b_j),\qquad 1\le j\le n,
\]
are strictly positive through some \(1\le c<n\) and strictly negative thereafter.
Assume \(|w_j|\le K b_j^2\) at every node in \(\pi/4\le\theta_j\le3\pi/4\), for some \(K\ge0\).
Then
\[
                 |H(0)|\le20K/M^2,\qquad |H'(0)|\le2010K/M.       \tag{1}
\]
The phase need only satisfy the displayed bounds at the specified nodes and may change sign there.
If \(H\in\mathbb Z[t]\) and \(M>2010K\), both integers vanish.

For the [exceptional parent](Yin_C_G0890_v2.md#statement) \(F_s=(1+z^2)^2(1-z^{2s})/(1-z^2)\) with any \(s\ge2\), every integral trace perturbation satisfying the strict cut and endpoint at \(p\ge2\cdot10^9\) therefore has degree greater than \(p/100000\).
The constants here give an explicit range; their optimal values are open.
The [fixed-degree exclusion](../ledger/Yin_L_G0457_v7.md#effective-cutoff) uses derivatives on a fixed real interval.
The main researcher obtained (1) by localizing both the polynomial and the derivative estimate at the middle of the angular grid.

<a id="samples"></a>
## Small values on adjacent nodes

Write \(t(\theta)=2\cos\theta\), \(\Delta=2\pi/p\).
For any angle \(\theta\in[\pi/3,2\pi/3]\), select two consecutive grid nodes in the same sign block, both within \(2\Delta\) of \(\theta\).
Start with an enclosing pair, choosing either incident pair when \(\theta\) is a node.
If this pair straddles the cut, replace it by the adjacent pair on its left.
The cut in this case is in the indicated middle part of the grid, so the replacement exists.
The chosen nodes lie in \([\pi/4,3\pi/4]\).

Within either sign block their opposite parities give an upper bound for \(H\) at one node and a lower bound at the other.
Both bounds have absolute value at most \(K\max_{\rm pair}|b_j|^2\).
By continuity there is an angle \(\zeta\) between the nodes with
\[
 |H(t(\zeta))|\le K\max_{\rm pair}|b_j|^2
                 \le K(|t(\zeta)|+2\Delta)^2,\qquad
 |\zeta-\theta|\le2\Delta.                                      \tag{2}
\]
This also applies at an exact phase zero.

First bound \(H\) on the full interval \([-2,2]\).
Use the \(M+1\) targets \(-1/2+i/M\) for \(0\le i\le M\).
For each target apply (2) at its inverse angle to select an intermediate trace \(x_i\).
Both node traces are within \(4\Delta\) of the target, so \(|H(x_i)|\le K\), and \(|x_i-(-1/2+i/M)|\le4\Delta\).
Since \(p\ge100000M\), it follows that \(|x_i-x_j|\ge |i-j|/(2M)\) for \(i\ne j\).
Lagrange interpolation, using \(|t-x_j|\le3\) for \(t\in[-2,2]\), gives
\[
 \|H\|_{[-2,2]}\le K(6M)^M\sum_{i=0}^{M}\frac{1}{i!(M-i)!}
          =K(12M)^M/M!\le K36^M.                               \tag{3}
\]
The final estimate follows from \(M!\ge(M/e)^M\).

<a id="localization"></a>
## A localized trigonometric polynomial

Define \(u=\theta-\pi/2\), and use the continuous values at the removable singularities in
\[
 T(\theta)= H(2\cos\theta)\sin^{64M}\theta\,
                      \left(\frac{\sin(Mu)}{M\sin u}\right)^2.
\]
This is a trigonometric polynomial of degree at most \(D=67M\), by the finite geometric sum for the sine quotient.
The squared quotient is at most \(\min(1,4/(M^2t^2))\) for \(t=2\cos\theta\ne0\), with value one at \(t=0\).
It is an even polynomial in \(\cos u=\sin\theta\), since \(\sin(Mu)/\sin u\) has definite parity as a polynomial in \(\cos u\).
Thus \(T(-\theta)=T(\theta)\), and its global supremum \(S\) on the real line is attained on \([0,\pi]\).

For any trigonometric polynomial of degree at most \(D\) and real-line supremum \(S\), one has \(\|T'\|_\infty\le eDS\).
Indeed, with \(z=e^{i\theta}\), apply the maximum principle to the polynomial \(z^D T\) on the unit disk and to \(z^{-D}T\) in the exterior, including infinity.
This bounds \(|T(\theta+iv)|\) by \(S e^{D|v|}\).
Cauchy's derivative estimate on the circle of radius \(1/D\) around each real argument gives the stated bound.

If \(|t|\ge1\), then \(\sin^{64M}\theta=(1-t^2/4)^{32M}\le(3/4)^{32M}\).
From (3), \(36(3/4)^{32}<1/2\) and \(M\ge4\), it follows that \(|T(\theta)|\le K2^{-M}\le K/M^2\).
At a point of maximum with \(|t|<1\), take \(\zeta\) from (2).
Multiplying its bound by the squared sine quotient gives
\[
 |T(\zeta)|\le 2K\big(4/M^2+(2\Delta)^2\big)\le10K/M^2,
\]
also for \(t(\zeta)=0\).
Since \(2\Delta eD<1/2\), the derivative estimate yields
\(S\le10K/M^2+S/2\) in this case.
We have proved \(S\le20K/M^2\) in both cases.
The two weights equal one and have zero derivative at \(\pi/2\).
Thus \(T(\pi/2)=H(0)\) and \(T'(\pi/2)=-2H'(0)\).
Using \(e<3\) gives both bounds in (1).

<a id="arithmetic"></a>
## Consequence for integral trace polynomials

In the [repeated-parent construction](Yin_C_G0890_v2.md#statement), the grid phase at the exceptional parent is
\[
 w_j=\frac{b_j^2\sin^2(s\theta_j)}{\sin\theta_j\,\sin(\theta_j/2)} .
\]
On the stated central arc, \(\sin\theta_j\ge\sin(\pi/4)>1/2\) and \(\sin(\theta_j/2)\ge\sin(\pi/8)>1/4\), so \(K=8\) works for every \(s\).
If \(p\ge2\cdot10^9\) then \(M\ge20000>2010K\).
An integral perturbation of degree at most \(M\) with the required signs must therefore have a double zero at zero, in the sense \(t^2\mid H\), including \(H=0\).
The neutral trace \(C_{F_s}B_m=t^2 E_{s-1} B_m\) also has this factor.
Under the strict endpoint \(Q(-2)/B_n(-2)<0\), the [trace division and root count](../ledger/Yin_L_G0457_v7.md#effective-cutoff) apply, since \(M\le n-2\).
They give only simple real roots for the perturbed trace \(Q=C_{F_s}B_m+H\), a contradiction.

The same local test applies whenever a different neutral trace in the [all-cut integer domain](Yin_C_G0881_v10.md#statement) already contains \(t^2\) and its grid phase obeys the displayed local majorant with \(K=o(p)\).
More precisely, for a sequence with the stated signs, endpoint and integral \(Q=tB_n+C\) with leading remainder coefficient two and degree \(n-1\), an integral perturbation of degree at most \(p/100000\) would then contradict the simplicity of its real roots for all sufficiently large \(p\).
For parents without the phase majorant or the double trace factor, this argument does not bound the perturbation degree.

## Assessment history

### Decision local-phase-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:04 |
| status | open |
| reason | Retain the local inequalities and their arithmetic application for independent proof inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Value and derivative bounds](#statement) | Local quadratic control of the phase at the middle grid nodes, with any strict cut. |
| argument | [Sampling](#samples) | Same-block parity, interpolation and full-interval growth. |
| argument | [Localization](#localization) | Trigonometric weights, derivative control and integer jets at the center. |
| argument | [Integer trace consequence](#arithmetic) | Linear degree requirement on the exceptional family and the assumptions for other inputs. |
| dependency | [Exceptional-parent trace division](../ledger/Yin_L_G0457_v7.md#effective-cutoff) | Grid phase and leading remainder coefficient on the exceptional family. |
| dependency | [All-cut root count](Yin_C_G0881_v10.md#nonreal-pair) | Simplicity of every real root under all the integer hypotheses. |


### Decision linear-degree-obstruction-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:10 |
| status | proved |
| reason | Adopt the local bounds and the resulting linear perturbation-degree obstruction under the checked integer trace hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Value and derivative bounds](#statement) | Local quadratic control of the phase at the middle grid nodes, with any strict cut. |
| argument | [Sampling](#samples) | Same-block parity, interpolation and full-interval growth. |
| argument | [Localization](#localization) | Trigonometric weights, derivative control and integer jets at the center. |
| argument | [Integer trace consequence](#arithmetic) | Linear degree requirement on the exceptional family and the assumptions for other inputs. |
| dependency | [Exceptional-parent trace division](../ledger/Yin_L_G0457_v7.md#effective-cutoff) | Grid phase and leading remainder coefficient on the exceptional family. |
| dependency | [All-cut root count](Yin_C_G0881_v10.md#nonreal-pair) | Simplicity of every real root under all the integer hypotheses. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v46.md#local-phase-review) | Entire local estimate with an arbitrary strict cut, numerical constants, both arithmetic applications and the imported real-root count. |

## Current assessment
[Selected decision](#decision-linear-degree-obstruction-reviewed)
