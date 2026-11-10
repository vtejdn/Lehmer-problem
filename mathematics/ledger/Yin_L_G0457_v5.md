---
author: Yin
---

# Cyclotomic central perturbations: order localization and a failed endpoint repair

Date: 2026-11-10.
The main researcher developed these exact construction tests under the [unrestricted Task](../tasks/Yin_T_G0001_v1.md#contract).
The [earlier squarefree-parent closure](Yin_L_G0457_v4.md#integer-family) and its [phase formula](Yin_L_G0457_v4.md#residue-formula) supply the actual family; no numerical root approximation is used below.
The new upper-root implication uses the [all-cut boundary pivot](../claims/Yin_C_G0881_v10.md#boundary-pivot), whose assessment remains separate.
The [complete independent finding](../audits/reviews/Yin_R_G1107_v41.md#parent-localization-review) checks this final construction argument and its all-cut exclusion.

<a id="order-localization"></a>
## Every parent order must lie below the grid conductor

Take a squarefree product \(A\) of distinct cyclotomic polynomials of orders at least three, of degree \(2d\), with
\[
A(z)=1+3z^2+O(z^4),\qquad d\ge2.
\]
For odd \(r>2d+1\), put \(m=(r-1)/2\), \(N=m+d\), \(n=N-1\), \(p=2n+1=r+2d-2\), and
\[
P=A(z)\frac{1-z^r}{1-z}-z^N,
\qquad Q=C_A B_m-1,\qquad A=z^dC_A(z+z^{-1}).
\]
The earlier integer calculation gives \(Q=tB_n+C\) with \(C\in\mathbb Z[t]\), degree \(n-1\) and leading coefficient two.
Suppose this input satisfies any strict terminal-cut signs and the strict endpoint.
Then every cyclotomic order \(q\) appearing in \(A\) must satisfy \(q\le p\).

Indeed an order \(q>p\) gives a root \(\beta=2\cos(2\pi/q)>b_1\) of \(C_A\), hence \(Q(\beta)=-1\).
But \(Q(2)=rA(1)-1>0\), because \(A(1)\) is a positive integer.
The intermediate value theorem gives a root of \(Q\) in \((\beta,2)\), contrary to the all-cut upper-root exclusion.
The value \(q=p\) is not excluded by this argument, because a parent root need not remain a root of the perturbed polynomial.

<a id="parity-reduction"></a>
## Only odd trace-grid degree can remain

The [earlier last-pole argument](Yin_L_G0457_v4.md#terminal-phase-gate) says that even \(n\) requires a root of \(C_A\) in \((-2,b_n)\), and therefore an order \(q>p\).
This contradicts the localization above.
Thus every admissible input in this profile has odd \(n\).
Then \(N\) is even, and the strict endpoint requires
\[
P(-1)=A(-1)-1>0,
\]
so \(A(-1)>1\).
These are necessary conditions for every terminal-cut length, not a sufficient integer construction or an exclusion of all moving parents.

<a id="endpoint-repair-test"></a>
## A parent satisfying the new endpoint requirement still fails every terminal cut

Consider the smallest direct change of the previous three-factor pattern obtained by replacing one factor by \(\Phi_4\):
\[
A=\Phi_4\Phi_{60}\Phi_{84},\qquad 2d=2+16+24=42.
\]
Each factor has expansion \(1+z^2+O(z^4)\), so the required first coefficients hold.
Also \(A(-1)=2\), addressing the former endpoint-value-one defect.
Every allowed odd \(r>43\) has \(p=r+40\ge85\), so all parent orders are below \(p\).
Even \(n\) is excluded above; for odd \(n\) the endpoint is strictly positive.
Nevertheless no allowed \(r\) meets any strict terminal-cut chamber.

Write \(\theta=2\pi u\).
On
\[
\frac1{40}<u<\frac1{20},
\tag{1}
\]
exactly two roots of \(C_A(2\cos(2\pi u))\) have been crossed, at \(1/84\) and \(1/60\).
The next primitive angles for those two orders are \(5/84\) and \(7/60\), respectively, and the first order-four angle is \(1/4\); all exceed \(1/20\).
Since the initial sign is positive and the roots are simple, \(C_A(2\cos(2\pi u))>0\) on (1).
Here \(d-1=20\), so \(\sin((d-1)\theta)=\sin(40\pi u)<0\).
Consequently the exact phase function
\[
W_A(\theta)=C_A(2\cos\theta)\frac{\sin((d-1)\theta)}{\sin(\theta/2)}
\]
is negative throughout (1).

The interval \((p/40,p/20)\) has length \(p/40>2\), and therefore contains an odd integer \(j\).
It satisfies \(1\le j<n\), since \(p\ge85\) and \(p/20<(p-1)/2=n\).
The [complete residue formula](Yin_L_G0457_v4.md#residue-formula) then gives
\[
\rho_j=\frac{4\sin\theta_j\sin(\theta_j/2)}p\bigl(W_A(\theta_j)-1\bigr)<0.
\]
This already contradicts the single-terminal-negative-node chamber.
For an arbitrary cut, consider the later interval
\[
\frac3{40}<u<\frac1{10}.
\tag{2}
\]
Exactly three parent trace roots have been crossed here, at \(1/84\), \(1/60\), and \(5/84\); the next angles \(7/60\), \(11/84\), and \(1/4\) all exceed \(1/10\).
Thus \(C_A(2\cos(2\pi u))<0\) on (2), while \(\sin(40\pi u)<0\), and therefore \(W_A>0\).
The interval \((3p/40,p/10)\) again has length \(p/40>2\), so it contains an even integer \(\ell\).
It satisfies \(j<\ell<n\), and the residue formula gives
\[
\rho_\ell=\frac{4\sin\theta_\ell\sin(\theta_\ell/2)}p
\bigl(W_A(\theta_\ell)+1\bigr)>0.
\]
A negative residue at \(j\) followed by a positive residue at \(\ell\) is incompatible with every initial-positive, terminal-negative strict sign pattern.
The proof covers every allowed odd \(r\) and every cut, without a finite numerical scan or a Mahler approximation.
It does not exclude other moving squarefree parents or assert a whole-measure bound outside these chambers.

<a id="construction-return"></a>
## Consequence for construction selection

The endpoint repair \(A(-1)>1\) can be achieved in integer coefficients, but does not fix the interior phase inequalities.
The all-cut positivity theorem permits reconsidering larger terminal negative blocks for other parents, without a separate proof that a successful integer input has positive measure.
The present parent cannot benefit from that enlargement, because its later positive residue prevents every terminal cut.
For a moving-parent search in the prescribed coefficient profile, reject even \(n\), orders \(q>p\), and \(A(-1)\le1\) before further chamber work.
These exact restrictions reduce candidate supply but neither prove a general Mahler gap nor produce positive probability in an arbitrarily small shell.
