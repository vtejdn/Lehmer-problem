---
author: Yin
---

# Signed amplitudes in the central neutral-block deformation

<a id="scope"></a>
## Scope and exact dependencies

This project deduction closes the signed-amplitude extension of [v2's positive-amplitude classification](Yin_C_G0884_v2.md#statement).
The new argument excludes all negative amplitudes for every permitted even matching length, even when the amplitude is real and the endpoint is not imposed.
It uses [v1's neutral trace and original domain](Yin_C_G0884_v1.md#inputs), [its full-grid coordinate identity](Yin_C_G0884_v1.md#all-r-pole-values), and the exact endpoint evaluation retained in [v1's amplitude comparison](Yin_C_G0884_v1.md#fixed-amplitude).
The positive-amplitude part and the two final integer successes remain the separate fixed result in v2.

<a id="statement"></a>
## Signed-real necessity and signed-integer classification

Let \(n,m,L\) be integers, put \(p=2n+1\) and \(r=2m\), let \(s\) be an odd integer, and assume
\[
             r+s=p,\qquad 3\le L<\min(r,s),\qquad L\le n-1.
\]
Use \(E_{-1}=0,E_0=1,E_1=t,E_{k+1}=tE_k-E_{k-1}\), \(B_k=E_k+E_{k-1}\), and
\[
             b_j=2\cos(2\pi j/p),\qquad 1\le j\le n.
\]
The neutral trace is defined by
\[
 \frac{(1+z^2)^2(1-z^r)(1-z^s)}{(1-z)^2(1+z)}
       =z^{n+1}Q^{(0)}_{r,s,0}(z+z^{-1}).
\]
For any real amplitude \(\lambda\), including zero, set
\[
       Q=Q^{(0)}_{r,s,0}-\lambda tB_{n-L-1},
       \qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
Let \(h\) be the canonical residue coordinate of degree less than \(n\) in [v1's original domain](Yin_C_G0884_v1.md#inputs).
A strict terminal sign chamber means that, for some \(1\le\kappa<n\),
\[
 h(b_j)>0\quad(1\le j\le n-\kappa),\qquad
 h(b_j)<0\quad(n-\kappa<j\le n).
\]
The strict endpoint is \(P(-1)>0\), equivalently \(Q(-2)/B_n(-2)<0\).

For every real \(\lambda\), the strict sign chamber necessarily implies
\[
                         L=3,\qquad r=4,\qquad \lambda>2.
\]
If the strict endpoint also holds, then \(2<\lambda<4\).
For integer \(\lambda\), the strict signs and endpoint hold if and only if
\[
 (p,r,s,L,\lambda)=(9,4,5,3,3)
       \quad\hbox{or}\quad(11,4,7,3,3).
\]
Both successes have \(\kappa=1\) and \(P(-1)=2\).
Thus no signed integer amplitude, even one growing with the matching length, supplies unbounded admissible \(L\) in this single-term family.

The statement preserves the original full grid and all polynomial factors and multiplicities.
It does not concern more general central perturbations or supply a shrinking Mahler shell.

<a id="signed-reduction"></a>
## Exact signed reduction from the last pole and endpoint

By [v1's all-\(r\) coordinate identity](Yin_C_G0884_v1.md#all-r-pole-values) and linearity in the perturbation,
\[
 h(b_j)=U_j-\lambda V_j,\qquad
 U_j=b_j^2E_{m-1}(b_j)^2\ge0,\qquad
 V_j=b_jE_L(b_j).
\]
No restriction \(r\le n-1\) is needed: reduction modulo \(B_n\) preserves these node values.
The residue weights are positive.
At \(\lambda=0\), every coordinate is nonnegative and the strict chamber fails.

For a nonzero amplitude, put \(u=\pi/p\).
The last-pole identity is
\[
 h(b_n)=
 \frac{4\cos^2u\,\sin^2(mu)}{\sin^2u}
 +\frac{2\lambda(-1)^L\cos u\,\sin((L+1)u)}{\sin u}.
\]
All unsigned factors are positive.
Last negativity therefore forces
\[
                    \lambda=(-1)^{L+1}\beta,\qquad \beta>0.
\]
With \(q=(L+1)/2\), possibly half-integral, the hypotheses give \(q\le m<p/2\) and \(L+1\le n<p/2\).
Monotonicity of sine and strict convexity of tangent, with \(\tan0=0\), give
\[
 \beta>
 \frac{2\cos u\,\sin^2(mu)}
      {\sin u\,\sin((L+1)u)}
 \ge\frac{\cos u\,\tan(qu)}{\sin u}>q.
\]
This is the signed form of [v1's amplitude comparison](Yin_C_G0884_v1.md#fixed-amplitude).
The endpoint calculation, which is algebraic in \(\lambda\), gives
\[
             P(-1)=4m+2\lambda(-1)^L=4m-2\beta.
\]
On this necessary signed parity, the strict endpoint is equivalent to \(\beta<2m\).
The new exclusion below uses only the pole signs.

<a id="negative-even-proof"></a>
## Analytic exclusion of every negative-amplitude even-length input

The remaining negative-amplitude case has even \(L\) and \(\lambda=-\beta\) with real \(\beta>0\).
No such input has the strict terminal sign chamber, independently of the endpoint.
The argument uses no finite census or numerical sign estimate.

Put
\[
 q=(L+1)/2\ge5/2,\qquad u=\pi/p,\qquad
 \sigma=\sin(q\pi)\in\{1,-1\}.
\]
The parameter conditions give \(p\ge4q+1>4q\) and \(q\le m<p/2\).
Last negativity forces \(\beta>q\) by the preceding last-pole comparison.
Write \(V_j=b_jE_L(b_j)\), so \(h(b_j)=U_j+\beta V_j\).
Whenever \(V_j>0\), the residue is strictly positive.
Whenever \(V_j<0\), it is strictly negative as soon as \(\beta>U_j/(-V_j)\).

<a id="offset-bound"></a>
## Values at an offset from the central angle

For an angle \(\theta=\pi/2\pm\delta\), with \(0<\delta<\pi/2\), put \(x=2q\delta\) and \(b=2\cos\theta\).
Then
\[
 \sin(2q\theta)=\sigma\cos x,\qquad
 E_L(b)=\frac{\sigma\cos x}{\cos\delta}.
\]
If \(\tau=\operatorname{sign}(b)\), this gives
\[
 V=2\tau\sigma\tan\delta\cos x,\qquad
 U=4\tan^2\delta\,\sin^2(m\theta).
\]
Consequently, at any selected node with \(V<0\),
\[
                 \frac{U}{-V}
                 =\frac{2\tan\delta\,\sin^2(m\theta)}
                         {|\cos x|}
                 \le\frac{2\tan\delta}{|\cos x|}.
\]

Let \(j_0=\lfloor p/4\rfloor\) and \(a=p-4j_0\in\{1,3\}\).
The actual positive-side offsets from \(\pi/2\) are
\[
                      au/2,\ au/2+2u,\ au/2+4u,\ldots,
\]
and the negative-side offsets are
\[
                      (4-a)u/2,\ (4-a)u/2+2u,\ldots.
\]
All offsets used below are less than \(\pi/2\), so they correspond to actual grid indices.

<a id="positive-witness"></a>
## A later automatically positive node

On the negative-\(b\) side, \(V>0\) exactly when \(\sigma\cos x<0\).
For \(\sigma=1\), select a grid phase in
\[
                         \pi/2<x<3\pi/2.
\]
For \(\sigma=-1\), select one in
\[
                         3\pi/2<x<5\pi/2.
\]
Each interval has angle width \(\pi/(2q)>2\pi/p\), so it contains an actual grid node.
Both corresponding angle intervals lie strictly below \(\pi\): the largest offset is \(3\pi/(4q)<\pi/2\) in the first case and \(5\pi/(4q)<\pi/2\) in the second.
Here \(\sigma=1\) allows \(q\ge5/2\), while \(\sigma=-1\) has \(q\ge7/2\).
The selected residue is strictly positive for every \(\beta>0\).
The negative nodes constructed next occur earlier than these witnesses, as verified in each case.

<a id="direct-parities"></a>
## The two direct parity combinations

If \((\sigma,a)=(1,3)\), use the nearest negative-\(b\) node, whose offset is \(\delta=u/2\).
If \((\sigma,a)=(-1,1)\), use the nearest positive-\(b\) node, with the same offset.
In both cases \(V<0\), because \(x=qu<\pi/4\).
The threshold satisfies
\[
 \frac{U}{-V}
 <2\sqrt2\tan(u/2)
 <2\sqrt{2/3}<2<q,
\]
using \(u/2\le\pi/22<\pi/6\).
Thus \(\beta>q\) makes this node negative.
For \(\sigma=1\) its phase \(x<\pi/4\) is before the positive-witness interval; for \(\sigma=-1\) the node is on the positive-\(b\) side and hence before every negative-\(b\) witness.
The strict terminal pattern is impossible in both combinations.

<a id="opposite-low"></a>
## Opposite parities with \(p<6q\)

The combinations remaining are \((\sigma,a)=(1,1)\) and \((-1,3)\).
They satisfy \(p-6q\equiv2\pmod4\).
Indeed, writing \(q=k+1/2\), one has \(\sigma=(-1)^k\); \(6q\equiv3\pmod4\) when \(\sigma=1\) and \(6q\equiv1\pmod4\) when \(\sigma=-1\).
In particular \(p=6q\) cannot occur in these combinations.

Suppose first that \(p<6q\).
Use the offset \(\delta=5u/2\), on the positive-\(b\) side when \(\sigma=1\), and on the negative-\(b\) side when \(\sigma=-1\).
These are actual nodes from the offset lists above.
The phase satisfies
\[
                         5\pi/6<x=5qu<5\pi/4,
\]
so \(\cos x<0\), \(|\cos x|>\sqrt2/2\), and \(V<0\) on the selected side.
Hence
\[
                         \frac{U}{-V}
                         <2\sqrt2\tan(5u/2).
\]
For \(q\ge7/2\), one has \(p\ge15\), so \(5u/2\le\pi/6\) and the right-hand side is at most \(2\sqrt{2/3}<2<q\).

For \(q=5/2\), this case has \(\sigma=1\) and \(a=1\), forcing \(p=13\).
Now \(5u/2=5\pi/26<2/3\).
For \(0<t<2/3\), the elementary bounds \(\sin t<t\) and \(\cos t>1-t^2/2\) imply
\[
                         \tan t<\frac{t}{1-t^2/2}<\frac67.
\]
It follows that
\[
                         \frac{U}{-V}
                         <\frac{12\sqrt2}{7}<\frac52=q.
\]
Thus the selected node is negative in every case.
For \(\sigma=1\) it is on the positive-\(b\) side; for \(\sigma=-1\) its phase is less than \(5\pi/4<3\pi/2\).
In either case the automatically positive witness occurs later, again contradicting a terminal negative block.

<a id="opposite-high"></a>
## Opposite parities with \(p>6q\)

Now \(p-6q\ge2\), by the parity calculation above.
Use the offset \(\delta=3u/2\), on the negative-\(b\) side when \(\sigma=1\), and on the positive-\(b\) side when \(\sigma=-1\).
These are again actual nearest nodes on the indicated sides.
Their phase \(x=3qu\) lies in \((0,\pi/2)\), giving \(V<0\).
Moreover
\[
 \cos(3qu)
 =\sin((p-6q)u/2)\ge\sin u.
\]
The threshold is therefore bounded by
\[
 \frac{U}{-V}
 \le\frac{2\tan(3u/2)}{\sin u}
 <\frac{3}{\cos(3u/2)}
 <2\sqrt3<\frac72.
\]
The middle strict inequality follows from strict concavity of sine, which gives \(\sin(3u/2)<(3/2)\sin u\).
The next uses \(p>6q\ge15\), hence \(p\ge17\) and \(3u/2<\pi/6\).
If \(q\ge7/2\), then \(\beta>q\ge7/2\) already makes this node negative.

It remains to justify a stronger last-pole bound when \(q=5/2\), where \(m\ge3\).
Put \(c=\cos u\) and
\[
                  D_0=\frac{\sin5u}{\sin u}
                     =16c^4-12c^2+1>0.
\]
Since \(p\ge17\) and \(\pi^2<10\),
\[
                 c>1-\frac{5}{289}
                  =\frac{284}{289}>\frac{35}{36}.
\]
Also
\[
              D_0-5c^2=(c^2-1)(16c^2-1)<0.
\]
Monotonicity of sine for \(3u\le mu<\pi/2\), together with the last-node negativity condition, now gives
\[
 \begin{split}
 \beta
 &>\frac{2c\sin^2(mu)}{\sin u\,\sin5u}\\
 &\ge\frac{2c\sin^2(3u)}{\sin u\,\sin5u}
   =\frac{2c(4c^2-1)^2}{D_0}\\
 &=2c\left(1+\frac{4c^2}{D_0}\right)
   >\frac{18c}{5}>\frac72.
 \end{split}
\]
This proves the necessary negative node even at \((L,p)=(4,17)\), without any finite computational premise.
For \(\sigma=1\) its phase is before \(\pi/2\); for \(\sigma=-1\) it is on the positive-\(b\) side.
The positive witness therefore follows it in both cases.
This last contradiction completes the negative-even exclusion for every positive real magnitude.

<a id="signed-classification"></a>
## Consequence for the complete signed family

At zero amplitude all coordinate values are nonnegative, so no strict negative block exists.
For nonzero real amplitude, the signed parity condition and the negative-even exclusion leave only positive amplitude and odd \(L\).
The [positive real necessity in C884v2](Yin_C_G0884_v2.md#statement) then forces \(L=3\), \(r=4\), and last negativity gives \(\lambda>2\).
With the endpoint, one additionally has \(\lambda<4\).
For integer amplitude, the only strict sign-and-endpoint inputs are consequently
\[
 (p,r,s,L,\lambda)=(9,4,5,3,3)
       \quad\hbox{or}\quad(11,4,7,3,3),
\]
and their sufficiency, cut size and endpoint values are established by [C884v2](Yin_C_G0884_v2.md#statement).
All new negative-amplitude exclusions are analytic and hold for real amplitudes.
No finite census, numerical program or complete-measure computation is a premise of this argument.

## Assessment history

### Decision signed-amplitudes-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-09T18:12 |
| status | proved |
| reason | Independent whole-proof review verifies the complete analytic negative-even exclusion and its assembly with the positive-amplitude theorem, leaving exactly the two stated integer inputs in the whole signed single-term family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Signed-amplitude classification](#statement) | Every permitted real amplitude, the strict-sign necessity and the complete integer-plus-endpoint classification. |
| argument | [Signed reduction](#signed-reduction) | Zero amplitude, necessary parity, half-integral amplitude lower bound and endpoint. |
| argument | [Negative-even domain](#negative-even-proof) | Precise remaining domain and the sign-threshold mechanism. |
| argument | [Offset identities](#offset-bound) | Exact node values, threshold estimates and actual grid offsets. |
| argument | [Later positive witness](#positive-witness) | Both sign intervals, actual grid-node existence and ordering. |
| argument | [Direct parity cases](#direct-parities) | Both direct combinations and strict threshold contradictions. |
| argument | [Opposite low branch](#opposite-low) | Congruence, all conductors below six q and the smallest boundary. |
| argument | [Opposite high branch](#opposite-high) | All larger conductors and the strengthened smallest-q last-pole comparison. |
| argument | [Full signed assembly](#signed-classification) | Exhaustive combination with the positive predecessor and both final successes. |
| dependency | [Original neutral domain](Yin_C_G0884_v1.md#inputs) | Full grid, neutral trace and original strict sign/endpoint conventions. |
| dependency | [Original coordinate identity](Yin_C_G0884_v1.md#all-r-pole-values) | Pole values for every allowed r and linear amplitude dependence. |
| dependency | [Amplitude and endpoint formula](Yin_C_G0884_v1.md#fixed-amplitude) | Exact last-pole comparison and algebraic endpoint identity. |
| dependency | [Positive-amplitude theorem](Yin_C_G0884_v2.md#statement) | Complete positive-real necessity and positive-integer sufficiency and necessity. |
| review | [Independent complete signed finding](../audits/reviews/Yin_R_G1110_v3.md#signed-amplitude-review) | Entire stated scope and every proof interface, with no finite census premise or unrestricted Mahler conclusion. |

## Current assessment

[Selected decision](#decision-signed-amplitudes-reviewed)
