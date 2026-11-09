---
author: Yin
---

# Positive integer amplitudes in the central neutral-block deformation

<a id="scope"></a>
## Scope and exact inputs

This project deduction extends [v1's fixed-coefficient classification](Yin_C_G0884_v1.md#statement) to every positive integer amplitude, including amplitudes that grow with the prefix length.
The proof covers all permitted conductors and block lengths, with no numerical search or finite-conductor evidence used as a premise.
Its unchanged inputs are [v1's original domain and neutral trace](Yin_C_G0884_v1.md#inputs), [the full-grid residue-coordinate identity](Yin_C_G0884_v1.md#all-r-pole-values), and [the necessary amplitude and endpoint conditions](Yin_C_G0884_v1.md#fixed-amplitude).
The two final finite successes use [v1's exact length-three classification](Yin_C_G0884_v1.md#length-three).

<a id="statement"></a>
## Complete positive-integer-amplitude classification

Let \(n,m,L\) be integers, set \(p=2n+1\) and \(r=2m\), let \(s\) be an odd integer, and assume
\[
 r+s=p,\qquad 3\le L<\min(r,s),\qquad L\le n-1.
\]
Use \(E_{-1}=0,E_0=1,E_1=t,E_{k+1}=tE_k-E_{k-1}\), \(B_k=E_k+E_{k-1}\), and the full decreasing grid
\[
             \theta_j=2\pi j/p,\qquad
             b_j=2\cos\theta_j,\qquad 1\le j\le n.
\]
Define the neutral trace by
\[
 \frac{(1+z^2)^2(1-z^r)(1-z^s)}{(1-z)^2(1+z)}
       =z^{n+1}Q^{(0)}_{r,s,0}(z+z^{-1}),
\]
and for an amplitude \(\lambda>0\) set
\[
       Q=Q^{(0)}_{r,s,0}-\lambda tB_{n-L-1},
       \qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
Let \(h\) be the canonical residue coordinate of degree less than \(n\) in [v1's domain](Yin_C_G0884_v1.md#inputs).
The original strict sign chamber means that, for some \(1\le\kappa<n\), \(h(b_j)>0\) for \(j\le n-\kappa\) and \(h(b_j)<0\) for \(j>n-\kappa\).
The strict endpoint is \(P(-1)>0\), equivalently \(Q(-2)/B_n(-2)<0\).

For every real \(\lambda>0\), the strict sign chamber implies \(L=3\) and \(r=4\), independently of the endpoint.
For positive integer \(\lambda\), the strict sign chamber and strict endpoint hold if and only if
\[
 (p,r,s,L,\lambda)=(9,4,5,3,3)
       \quad\hbox{or}\quad(11,4,7,3,3).
 \tag{1}
\]
Both successes have \(\kappa=1\) and \(P(-1)=2\).
In particular no positive integer amplitude, even one growing with \(L\), supplies an unbounded admissible matching length in this one-term family.

This statement concerns the original full grid and the whole lifted polynomial.
It does not classify negative amplitudes or more general central perturbations, or assert a small positive Mahler measure.

<a id="reused-identities"></a>
## Unchanged full-grid interfaces

By linearity in the perturbation, [v1's all-\(r\) identity](Yin_C_G0884_v1.md#all-r-pole-values) gives
\[
 h(b_j)=U_j-\lambda V_j,\qquad
 U_j=b_j^2E_{m-1}(b_j)^2\ge0,\qquad
 V_j=b_jE_L(b_j).
 \tag{2}
\]
No condition \(r\le n-1\) is imposed; reduction modulo \(B_n\) preserves all these node values.
The residue weights \((4-b_j^2)/p\) are positive, so coordinate signs and residue signs agree.
Whenever \(V_j>0\), write \(T_j=U_j/V_j\).
Such a node is negative exactly when \(\lambda>T_j\), and positive exactly when \(\lambda<T_j\).
If \(V_j<0\), it is positive for every \(\lambda>0\).

The [last-pole and endpoint calculation in v1](Yin_C_G0884_v1.md#fixed-amplitude), with \(u=\pi/p\), gives
\[
 \begin{gathered}
 h(b_n)<0\ \Longrightarrow\
 L\ \text{odd},\qquad
 \lambda>
 \frac{2\cos u\,\sin^2(mu)}
      {\sin u\,\sin((L+1)u)}
 >\frac{L+1}{2},\\
 P(-1)=4m+2\lambda(-1)^L.
 \end{gathered}
 \tag{3}
\]
For odd \(L\), the strict endpoint is therefore equivalent to \(\lambda<2m\).
The proof below uses the endpoint only in its final integer selection.

<a id="threshold"></a>
## A threshold bound independent of the neutral block length

Even \(L\) is already impossible for \(\lambda>0\) by [C884's last-pole sign](Yin_C_G0884_v1.md#fixed-amplitude).
Write an odd \(L\) as \(L=2q-1\), so \(q\ge2\).
The parameter conditions give \(q\le m\), \(n\ge2q\), and \(p\ge4q+1\).
Last negativity requires \(\lambda>q\).

For a positive pole \(b_j=2\cos\theta_j>0\) with \(\sin(2q\theta_j)>0\), one has \(V_j>0\) and
\[
 T_j
 =\frac{2\cot\theta_j\,\sin^2(m\theta_j)}
         {\sin(2q\theta_j)}
 \le\frac{2\cot\theta_j}{\sin(2q\theta_j)}.
 \tag{4}
\]
Thus a pole with the right-hand side less than \(q\) is necessarily negative.
If a later pole has \(V_j<0\), it is strictly positive, contradicting a terminal negative block.

Put \(j_0=\lfloor p/4\rfloor\), the index of the positive pole closest to zero.
Let \(a=p-4j_0\in\{1,3\}\), \(u=\pi/p\), and
\[
 \theta_{j_0}=\frac\pi2-\delta_0,\qquad
 \delta_0=\frac{au}{2}.
 \tag{5}
\]
Earlier positive poles have \(\delta_k=\delta_0+2ku\) and index \(j_0-k\), as long as \(\delta_k<\pi/2\).

<a id="odd-q"></a>
## Odd \(q\ge3\)

At \(j_0\), one has
\[
 \sin(2q\theta_{j_0})=\sin(2q\delta_0)>0,
 \qquad 0<2q\delta_0<\frac{3\pi}{4},
 \qquad 0<\delta_0<\frac{\pi}{4}.
\]
Convexity of tangent on \([0,\pi/4]\) and concavity of sine on \([0,3\pi/4]\) give
\[
 \tan\delta_0\le\frac{4\delta_0}{\pi},\qquad
 \sin(2q\delta_0)\ge
       \frac{2\sqrt2}{3\pi}\,2q\delta_0.
\]
Consequently the threshold in (4) satisfies
\[
       T_{j_0}\le
       \frac{2\tan\delta_0}{\sin(2q\delta_0)}
       \le\frac{3\sqrt2}{q}<q.
 \tag{6}
\]
Its residue is therefore strictly negative.

The interval
\[
       \frac\pi2+\frac{\pi}{2q}
       <\theta<
       \frac\pi2+\frac{\pi}{q}
 \tag{7}
\]
lies inside \((0,\pi)\) and has length \(\pi/(2q)>2\pi/p\).
It contains an actual grid angle later than \(\theta_{j_0}\).
On this interval \(b=2\cos\theta<0\), while \(\sin(2q\theta)>0\) because \(q\) is odd.
Hence \(V=bE_{2q-1}(b)<0\), and that later residue is strictly positive.
This contradicts a terminal negative block.

<a id="phase-selection"></a>
## A phase selection for even \(q\)

For even \(q\), the pole \(j_0\) instead has \(V_{j_0}<0\), since
\[
 \sin(2q\theta_{j_0})=-\sin(2q\delta_0)<0.
\]
It is therefore strictly positive for every \(\lambda>0\).
To contradict a terminal negative block, it suffices to find an earlier positive pole with threshold less than \(q\).

Put \(d=4qu<\pi\).
At the earlier poles in (5), the phases \(x=2q\delta_k\) form the progression
\[
                        x_k=d(k+a/4).
 \tag{8}
\]
There is always a nonnegative integer \(k\) with
\[
          \pi<x_k<2\pi,\qquad
          -\sin x_k\ge\sin(\pi/14).
 \tag{9}
\]
If \(d\le\pi/2\), choose the first progression point at least \(5\pi/4\); it lies in \([5\pi/4,7\pi/4]\).
If \(d>\pi/2\) and \(a=1\), use \(k=1\) for \(d\ge6\pi/7\), and \(k=2\) otherwise.
The resulting ranges are respectively \([15\pi/14,5\pi/4)\) and \((9\pi/8,27\pi/14)\), each satisfying (9).
If \(d>\pi/2\) and \(a=3\), use \(k=1\) for \(d\ge2\pi/3\), and \(k=2\) otherwise.
The resulting ranges are \([7\pi/6,7\pi/4)\) and \((11\pi/8,11\pi/6)\), which also satisfy (9).
This proves the selection assertion directly.

For \(q\ge4\), a selected phase gives
\[
            0<\delta_k=\frac{x_k}{2q}<\frac{\pi}{q}
            \le\frac\pi4.
\]
It is therefore an actual positive pole earlier than \(j_0\), rather than a point outside the grid index range.
For even \(q\), \(\sin(2q\theta_{j_0-k})=-\sin x_k>0\), so (4) applies.

<a id="even-q"></a>
## Even \(q\ge6\)

For the selected pole, (4) and (9) give
\[
 T_{j_0-k}
 <\frac{2\tan(\pi/q)}{\sin(\pi/14)}
 \le\frac{2}{\sqrt3\,\sin(\pi/14)}
 <\frac{28}{3\sqrt3}<6\le q.
 \tag{10}
\]
Here \(\sin(\pi/14)>3/14\) follows from strict concavity of sine between zero and \(\pi/6\).
The selected residue is negative and the later residue at \(j_0\) is positive, excluding the strict terminal sign pattern.

<a id="q-four"></a>
## The remaining value \(q=4\)

Here \(p\ge17\).
For \(p\ge33\), one has \(d=16\pi/p<\pi/2\), and the first case of the phase selection gives \(-\sin x_k\ge\sqrt2/2\).
Thus \(T_{j_0-k}<2\sqrt2<4=q\), again yielding the same contradiction.

The only remaining odd conductors are \(17,19,21,23,25,27,29,31\).
The following exact grid choices all have \(\pi<x<2\pi\) and \(7\pi/6\le x\le11\pi/6\), where \(x=8(\pi/2-2\pi j/p)\):

| \(p\) | Earlier positive index \(j\) | \(x/\pi\) |
| --- | --- | --- |
| 17 | 3 | \(20/17\) |
| 19 | 3 | \(28/19\) |
| 21 | 3 | \(12/7\) |
| 23 | 4 | \(28/23\) |
| 25 | 4 | \(36/25\) |
| 27 | 4 | \(44/27\) |
| 29 | 5 | \(36/29\) |
| 31 | 5 | \(44/31\) |

Each row therefore has \(-\sin x\ge1/2\) and \(\delta=x/8<\pi/4\), giving \(T_j<4\) from (4).
Each selected index is earlier than \(j_0\), whose residue remains positive.
These rational angle comparisons complete the proof for \(q=4\); they are not numerical sign estimates.

The odd and even cases together exclude every \(q\ge3\), equivalently every odd \(L\ge5\).
Combined with the even-\(L\) last-pole obstruction, this excludes every \(L\ge4\) for positive amplitude.

<a id="length-three"></a>
## Length three and the integer endpoint

It remains to take \(L=3\), so \(q=2\).
At the first and last poles, (2) and the sine formula for \(E_k\) give the necessary inequalities
\[
 \lambda<T_1=
 \frac{2\cos(2u)\sin^2(2mu)}{\sin(2u)\sin(8u)},
 \qquad
 \lambda>T_n=
 \frac{2\cos u\sin^2(mu)}{\sin u\sin(4u)}.
\]
Their denominators are positive for \(p\ge9\).
If \(m\ge3\), then \(p\ge11\).
Since \(3u\le mu<\pi/2\),
\[
 \frac{T_1}{T_n}
 =\frac{\cos(2u)\cos^2(mu)}{\cos^2u\,\cos4u}
 \le
 \frac{\cos(2u)\cos^2(3u)}{\cos^2u\,\cos4u}<1.
 \tag{11}
\]
For the last strict inequality put \(z=\cos^2u\).
The elementary identities for double and triple angles give
\[
 \cos(2u)\cos^2(3u)-\cos^2u\,\cos4u
       =2z(z-1)(16z^2-20z+5).
\]
Since \(u\le\pi/11\) and \(\pi^2<10\),
\[
       \sin^2u<u^2\le\pi^2/121<10/121<1/12,
       \qquad z>11/12.
\]
The polynomial \(16z^2-20z+5\) is increasing for \(z\ge11/12\) and has value \(1/9\) at \(11/12\).
It is positive, whereas \(z-1<0\), proving (11).
First positivity requires \(\lambda<T_1\), while last negativity requires \(\lambda>T_n\), a contradiction.
Thus \(m=2\) is necessary.

Now last negativity requires \(\lambda>2\), and the separate strict endpoint requires \(\lambda<2m=4\).
For integer amplitude this forces \(\lambda=3\).
The [exact coefficient-three classification](Yin_C_G0884_v1.md#length-three) then leaves precisely the two cases (1), and its endpoint proof verifies both.
This completes the positive-integer-amplitude classification.

## Assessment history

### Decision positive-amplitudes-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-09T17:59 |
| status | proved |
| reason | Independent whole-proof review establishes the positive-real sign restriction and complete positive-integer-amplitude classification, including amplitudes growing with length; signed negative amplitudes remain outside this statement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Positive-amplitude classification](#statement) | All permitted parameters, positive-real sign necessity and positive-integer strict-sign-and-endpoint successes. |
| argument | [Reused exact identities](#reused-identities) | Original residues, positivity factors and strict endpoint. |
| argument | [Uniform threshold](#threshold) | Pointwise bounds independent of the neutral block length. |
| argument | [Odd q](#odd-q) | Forced negative and later positive grid values for every odd q at least three. |
| argument | [Even phase selection](#phase-selection) | Complete progression cases and actual earlier grid indices. |
| argument | [Large even q](#even-q) | Uniform threshold contradiction for every even q at least six. |
| argument | [q equal four](#q-four) | Complete remaining conductor ranges and eight exact angle rows. |
| argument | [Length-three endpoint](#length-three) | First/last threshold incompatibility for m at least three, integer amplitude selection and both successes. |
| dependency | [Original domain](Yin_C_G0884_v1.md#inputs) | Neutral trace and full original grid, including all permitted r. |
| dependency | [Pole coordinates](Yin_C_G0884_v1.md#all-r-pole-values) | Exact polynomial residue formula used at variable amplitude. |
| dependency | [Amplitude and endpoint](Yin_C_G0884_v1.md#fixed-amplitude) | Odd-length necessity, strict lower amplitude bound and endpoint upper bound. |
| dependency | [Final finite classification](Yin_C_G0884_v1.md#length-three) | Exact coefficient-three sign successes at conductors nine and eleven. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1110_v2.md#positive-amplitude-review) | Complete statement, every proof section and actual reused interfaces; no negative-amplitude or unrestricted Mahler conclusion. |

## Current assessment

[Selected decision](#decision-positive-amplitudes-reviewed)
