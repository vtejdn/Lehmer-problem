---
author: Yin
---

# Exact sign classification for a central neutral-block deformation

<a id="scope"></a>
## Scope and mathematical dependencies

This project deduction resolves the complete fixed-coefficient first test in [L462v12](../ledger/Yin_L_G0462_v12.md#first-test).
Its inputs are [v11's neutral residue formula](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) and [C881v3's original residue map and recurrence](Yin_C_G0881_v3.md#original-domain).
The proof covers every allowed parameter, with no finite scan.
It does not give a shrinking Mahler shell or resolve the unrestricted integer-completion problem.

<a id="inputs"></a>
## Exact question and input scope

Use the full odd-grid input and residue convention in [C881v3](Yin_C_G0881_v3.md#original-domain).
Thus \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), \(E_{-1}=0\), \(E_0=1\), \(E_1=t\), \(E_{k+1}=tE_k-E_{k-1}\), \(B_k=E_k+E_{k-1}\), and \(D=B_{n-1}\).
The canonical residue coordinate \(h\) has degree less than \(n\), and the actual residues are
\[
                     r_j=\nu_jh(b_j),\qquad
                     \nu_j=(4-b_j^2)/p>0.
\]
The required chamber has \(h(b_j)>0\) for \(1\le j\le n-\kappa\) and \(h(b_j)<0\) for \(n-\kappa<j\le n\), for some \(1\le\kappa<n\).
In particular it necessarily has \(h(b_1)>0\) and \(h(b_n)<0\).

Let \(r=2m\) be even and \(s\) odd, with
\[
 r+s=p,\qquad 3\le L<\min(r,s),\qquad L\le n-1.
 \tag{1}
\]
These conditions imply \(r\ge4\), \(s\ge5\), and \(p\ge9\).
Use [v11's exact neutral polynomial and trace](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply):
\[
 P^{(0)}_{r,s,0}(z)
 =\frac{(1+z^2)^2(1-z^r)(1-z^s)}{(1-z)^2(1+z)}
 =z^{n+1}Q^{(0)}_{r,s,0}(z+z^{-1}).
\]
The first-test deformation is
\[
 Q=Q^{(0)}_{r,s,0}-3tB_{n-L-1},\qquad
 P=z^{n+1}Q(z+z^{-1}).
 \tag{2}
\]
It is integral and preserves the exact \(x=0\) profile prefix through \(L\), as established at the linked first-test definition.
The argument below concerns this whole parameter family, including \(r>n-1\).
The negative-one rational-pole obstruction in [C881v4](Yin_C_G0881_v4.md#statement) has profile \(x=-1\) and is not used for this \(x=0\) statement.

<a id="statement"></a>
## Exact classification and fixed-amplitude obstruction

Under the parameters and definitions (1)--(2), the strict original terminal sign chamber is satisfied if and only if
\[
 (p,r,s,L)=(9,4,5,3)\quad\hbox{or}\quad(11,4,7,3).
\]
In either case \(\kappa=1\).
In particular \(h(b_n)>0\) for every \(L\ge4\), so the coefficient \(-3\) family has no sequence of admissible inputs with \(L\to\infty\).
Under the optional restriction \(r\le n-1\), only the conductor-11 sign case remains.

Every member of (1)--(2), including those outside the sign chamber, satisfies
\[
 P(-1)=4m+6(-1)^L>0.
\]
Both sign cases therefore have the separate strict endpoint, with \(P(-1)=2\).

More generally replace the perturbation in (2) by \(-A tB_{n-L-1}\), for a real \(A>0\), with all parameter conditions (1) unchanged.
If its last residue is strictly negative, then \(L\) is odd and, for \(u=\pi/p\) and \(c=\cos u\),
\[
 A>
 \frac{2c\sin^2(mu)}{\sin u\,\sin((L+1)u)}
 \ge\frac{c\tan((L+1)u/2)}{\sin u}
 >\frac{L+1}{2}.
\]
Consequently no fixed positive \(A\) supplies unbounded admissible \(L\).
For positive integer \(A\), terminal negativity requires \(A\ge(L+3)/2\).
In this odd-\(L\) case the independent strict endpoint is equivalent to \(A<2m=r\).
These necessary conditions make no assertion of feasibility for growing \(A\).

<a id="all-r-pole-values"></a>
## Pole values without a reduced-degree restriction

For \(\theta_j=2\pi j/p\), the neutral residue formula in [v11](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) gives
\[
 r_j^{(0)}=\frac{4b_j^2\sin^2(m\theta_j)}p.
\]
Since \(4-b_j^2=4\sin^2\theta_j\) and
\[
 E_{m-1}(2\cos\theta)=\frac{\sin(m\theta)}{\sin\theta},
\]
the canonical neutral coordinate has the values
\[
                    h^{(0)}(b_j)=b_j^2E_{m-1}(b_j)^2.
 \tag{3}
\]
This statement about values is valid for every permitted \(m\).
Only the assertion that the polynomial \(t^2E_{m-1}^2\) itself is already the reduced representative requires \(r=2m\le n-1\).
For larger \(r\), its remainder modulo \(B_n\) has the same values and the required degree.

The [exact recurrence congruence in C881v3](Yin_C_G0881_v3.md#prefix-coordinates) is
\[
                 DE_L\equiv B_{n-L-1}\pmod{B_n}.
\]
Multiplying it by \(-3t\) gives the actual residue-coordinate change in (2).
Combining it with (3), for every permitted \(r,s,L\) and every grid index,
\[
                 h(b_j)=b_j^2E_{m-1}(b_j)^2-3b_jE_L(b_j).
 \tag{4}
\]
No replacement of the original grid or coefficient domain is made.

<a id="last-pole"></a>
## A positive last residue excludes every \(L\ge4\)

Put \(u=\pi/p\) and \(c=\cos u>0\).
At the last pole \(b_n=-2c\), the parity of the Chebyshev polynomials gives
\[
 E_{m-1}(b_n)=(-1)^{m-1}\frac{\sin(mu)}{\sin u},
 \qquad
 E_L(b_n)=(-1)^L\frac{\sin((L+1)u)}{\sin u}.
\]
Consequently
\[
 h(b_n)
 =\frac{4c^2\sin^2(mu)}{\sin^2u}
   +\frac{6c(-1)^L\sin((L+1)u)}{\sin u}.
 \tag{5}
\]
The inequalities \(0<m<p/2\) and \(L+1\le n<p/2\) ensure that all displayed sine factors are strictly positive.
For even \(L\), both terms in (5) are therefore positive.

For odd \(L\ge5\), let \(q=(L+1)/2\ge3\).
Since \(L<2m\), we have \(q\le m\), while \(mu<\pi/2\).
Sine is increasing on that interval, so
\[
 \begin{split}
 h(b_n)
 &\ge \frac{4c^2\sin^2(qu)}{\sin^2u}
       -\frac{6c\sin(2qu)}{\sin u}\\
 &=\frac{4c\sin(qu)\cos(qu)}{\sin^2u}
                   \bigl(c\tan(qu)-3\sin u\bigr).
 \end{split}
 \tag{6}
\]
Strict convexity of tangent on \((0,\pi/2)\), together with \(\tan0=0\), gives \(\tan(qu)>q\tan u\) for \(q>1\).
Thus
\[
                    c\tan(qu)>q\sin u\ge3\sin u,
\]
and (6) is strictly positive.
Every integer \(L\ge4\) is either even or an odd integer at least five, proving
\[
                         h(b_n)>0\qquad(L\ge4).
 \tag{7}
\]
This violates the necessary strict last-pole sign before any endpoint or Mahler-measure argument.

<a id="length-three"></a>
## Complete classification at the sole remaining length

Suppose \(L=3\).
If \(m\ge3\), monotonicity of sine on \((0,\pi/2)\) gives \(\sin(mu)\ge\sin(3u)\).
Using
\[
 \frac{\sin3u}{\sin u}=4c^2-1,\qquad
 \frac{\sin4u}{\sin u}=4c(2c^2-1),
\]
equation (5) yields
\[
 \begin{split}
 h(b_n)
 &\ge4c^2\bigl((4c^2-1)^2-6(2c^2-1)\bigr)\\
 &=4c^2(16c^4-20c^2+7)\\
 &=4c^2\left(16\left(c^2-\frac58\right)^2+\frac34\right)>0.
 \end{split}
 \tag{8}
\]
Hence \(m=2\), equivalently \(r=4\), is necessary.

For \(m=2,L=3\), equation (4) simplifies at every pole to
\[
       h(b_j)=b_j^4-3b_j(b_j^3-2b_j)
             =2b_j^2(3-b_j^2).
 \tag{9}
\]
The odd grid has none of \(0,\sqrt3,-\sqrt3\): the corresponding angles in \((0,\pi)\) are \(\pi/2,\pi/6,5\pi/6\), and equality would require \(p\) divisible by four or twelve.
Thus no zero residue occurs in (9).

If \(p\ge13\), then \(2\pi/p<\pi/6\), so \(b_1>\sqrt3\) and \(h(b_1)<0\).
The first required positive sign fails.
The only allowed remaining odd conductors are \(p=9,11\).
For each of them,
\[
  b_1<\sqrt3,\qquad
  b_{n-1}=-2\cos(3\pi/p)>-\sqrt3,\qquad
  b_n=-2\cos(\pi/p)<-\sqrt3.
\]
All the first \(n-1\) poles therefore lie in \((-\sqrt3,\sqrt3)\setminus\{0\}\), and the last lies below \(-\sqrt3\).
Equation (9) proves the exact sign pattern \(+,\ldots,+,-\).

It follows that the full family (1)--(2) satisfies the strict original sign chamber if and only if
\[
                      (p,r,s,L)=(9,4,5,3)
                      \quad\hbox{or}\quad(11,4,7,3),
 \tag{10}
\]
with \(\kappa=1\) in either case.
Under the additional reduced-representative restriction \(r\le n-1\), only the conductor-11 case remains.

<a id="endpoint"></a>
## The endpoint passes independently

The whole family has a strict endpoint, despite the sign obstruction.
Factor the neutral polynomial as
\[
 P^{(0)}
 =(1+z^2)^2
   \frac{1-z^{2m}}{1-z^2}
   \frac{1-z^s}{1-z}.
\]
The two quotients are finite geometric sums.
At \(z=-1\), the first is \(m\), the second is one because \(s\) is odd, and \((1+z^2)^2=4\).
Hence \(P^{(0)}(-1)=4m\).
Using \(B_k(-2)=(-1)^k\) in the lifted perturbation gives
\[
 \begin{split}
 P(-1)
 &=4m-3(-1)^{n+1}(-2)(-1)^{n-L-1}\\
 &=4m+6(-1)^L>0,
 \end{split}
 \tag{11}
\]
since \(m\ge2\).
Both surviving sign cases in (10) have \(P(-1)=2\).
This endpoint statement is logically separate from the last-pole proof.

<a id="fixed-amplitude"></a>
## A necessary amplitude change for reopening this mechanism

The same last-pole argument extends to the otherwise identical perturbation \(-A tB_{n-L-1}\) with a fixed real \(A>0\).
Even \(L\) still makes \(h(b_n)>0\).
For odd \(L\), strict last negativity requires
\[
 A>
 \frac{2c\sin^2(mu)}{\sin u\,\sin((L+1)u)}
 \ge\frac{c\tan((L+1)u/2)}{\sin u}
 >\frac{L+1}{2}.
 \tag{12}
\]
Thus no fixed positive amplitude supplies unbounded \(L\).
Any growing-amplitude candidate in this one-term form must have odd \(L\) and \(A>(L+1)/2\); for integer \(A\), this means \(A\ge(L+3)/2\).
For this perturbation, the evaluation in (11) instead gives \(P(-1)=4m+2A(-1)^L\).
When \(L\) is odd, its separate strict endpoint is therefore equivalent to \(A<2m=r\).
These are only necessary conditions, not a sign construction or a sufficient feasibility test.

<a id="limits"></a>
## Consequences and remaining scope

The fixed first test does not cross the all-length integer-completion gap.
The proof uses exact trigonometric identities and inequalities for all permitted parameters, not a finite scan.
No numerical program or external theorem is needed.

The conductor-9 nonreal residual pair and positive complete Mahler measure remain the separate established result in [L462v12](../ledger/Yin_L_G0462_v12.md#nonreal-pair).
No nonreal-pair or complete-measure assertion is made here for conductor 11.
Neither finite case establishes a shrinking shell or \(M<1.2\).
No claim is made about more general central perturbations, growing-amplitude feasibility, the unrestricted affine integer count, or the original Lehmer goal.

## Assessment history

### Decision central-deformation-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-09T17:44 |
| status | proved |
| reason | Independent whole-argument review verifies the complete fixed-coefficient sign classification, endpoint identity and necessary positive-amplitude bounds; growing amplitudes and unrestricted integer completion remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact deformation statement](#statement) | All stated parameter ranges, both finite sign successes, endpoint and fixed-positive-amplitude exclusion. |
| argument | [Full-grid pole values](#all-r-pole-values) | Neutral and perturbed coordinate values for every allowed r, including unreduced representatives. |
| argument | [Last-pole exclusion](#last-pole) | All even lengths and every odd length at least five. |
| argument | [Length-three classification](#length-three) | Exact exhaustion of all remaining parameters and strict cut size. |
| argument | [Endpoint identity](#endpoint) | Strict positivity in the entire fixed-coefficient family. |
| argument | [Amplitude constraint](#fixed-amplitude) | Necessary real and integer amplitude bounds, fixed-amplitude length exclusion and separate endpoint. |
| dependency | [Original residue domain](Yin_C_G0881_v3.md#original-domain) | Exact grid, residue weights, integer coordinates and endpoint convention. |
| dependency | [Recurrence and prefix](Yin_C_G0881_v3.md#prefix-coordinates) | The recurrence congruence defining the coordinate perturbation. |
| dependency | [Neutral block supply](../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) | Integral trace lift and its exact neutral residue formula. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v29.md#central-deformation-review) | Complete statement, all arguments and actual dependency interfaces, without a Mahler or growing-amplitude existence conclusion. |

## Current assessment

[Selected decision](#decision-central-deformation-reviewed)
