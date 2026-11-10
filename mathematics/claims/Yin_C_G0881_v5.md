---
author: Yin
---

# Integer jets and grid certificates for long odd-grid prefixes

<a id="statement"></a>
## Exact statements and their distinct scopes

Retain the [adopted negative-one integer-pole theorem](Yin_C_G0881_v4.md#decision-integer-pole-prefix) unchanged.
The new statements concern the zero profile in [v3's original odd-grid domain](Yin_C_G0881_v3.md#original-domain).
Write \(p=2n+1\), \(b_j=2\cos(2\pi j/p)\), \(\nu_j=(4-b_j^2)/p\), \(r_j=\nu_jh(b_j)\), and
\[
h=\sum_{i=0}^{n-1}a_iE_i,\quad C=B_{n-1}h\bmod B_n,\quad
Q=tB_n+C,\quad P=z^{n+1}Q(z+z^{-1}).
\]
A zero-profile prefix through \(L\), where \(2\le L\le n+1\), means
\(a_0=2\), \(a_i=0\) for odd \(i\), and \(a_i=4\) for positive even \(i\), through \(i=L-2\).
Assume a strict single cut and choose a negative separator \(b_{n-\kappa+1}<c<b_{n-\kappa}<2\), \(c<0\).

First suppose all \(a_i\) are integers.
For any integer \(m\ge2\) with \(4m-1\le L\), set
\[
A_m=\frac{2m^2+1}{3m^3},\qquad S_m=-\frac{2c}{m^3},
\]
and choose positive bounds
\[
D_1\ge\max_j\frac1{|b_j(b_j-c)|},\qquad
D_2\ge\max_j\frac1{b_j^2|b_j-c|}.
\]
If
\[
D_1S_m<1,\qquad A_m+D_2S_m<1,                         \tag{1}
\]
then \(Q(0)=Q'(0)=0\).
If in addition \(P(-1)>0\), the complete measure is \(M(P)=1\).
This is a sufficient exclusion criterion, not an integer-existence result when (1) fails.

At \(p=401,n=200,\kappa=1,L=140\), one may take
\[
c=-19997/10000,\quad m=35,\quad D_1=5000,\quad D_2=10400.
\]
Thus the integer criterion excludes nonneutral outputs in that cell.

The stronger separate conclusion is that at these same \(p,n,\kappa,L\), there is no real coefficient input \(h\) satisfying the prescribed prefix and strict signs at all.
This conclusion requires neither integrality nor the endpoint.
It is proved below by a degree-138 grid polynomial and a validated finite enclosure.
It does not assert infeasibility at a larger conductor.

<a id="argument"></a>
## Mathematical inputs and review scope

The proof uses [v3's exact prefix moment and full-grid orthogonality](Yin_C_G0881_v3.md#prefix-cut-compatibility), its original partial-fraction identity, and the [whole double-profile-factor argument](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction).
The integer-jet calculation was developed by an ordinary complementary proof collaborator.
The grid certificate and its assembly were developed by the main research agent.
These author contributions are separate from the required independent review.

The [J159 numerical proposal](../computations/programs/Yin_J_G0159/readme.md#question) motivated the finite root-index certificate.
Its solver status is not a premise of the proof.
The [retained grid checker](../computations/programs/Yin_J_G0159/grid_certificate.py) uses only the displayed exact indices and validated Arb arithmetic; it does not read a solver output or use floating trigonometry.

<a id="fejer-jets"></a>
## An even Fejer polynomial controls two integer jets

Let \(d\alpha(t)=dt/(\pi\sqrt{4-t^2})\).
The prefix gives
\[
\sum_jr_j f(b_j)=\int t^2f(t)\,d\alpha(t)
                         \quad(\deg f\le L-2).            \tag{2}
\]
Use \(T_k(z+z^{-1})=z^k+z^{-k}\), and define
\[
g_m(t)=\frac1{m^2}\left[m+
 \sum_{\ell=1}^{m-1}(m-\ell)(-1)^\ell T_{2\ell}(t)\right].
\]
This is even of degree \(2m-2\), and \(g_m(0)=1\).
Its exact moments are
\[
\int g_m^2\,d\alpha=A_m,\qquad
\int t^2g_m^2\,d\alpha=\frac2{m^3}.                       \tag{3}
\]

To check (3), put \(t=2\cos\theta\), \(\phi=\theta-\pi/2\), \(u=e^{2i\phi}\), and \(S(u)=1+\cdots+u^{m-1}\).
Then \(g_m=|S(u)|^2/m^2\), \(t^2=|1-u|^2\), and the arcsine integral extracts the constant Laurent coefficient over one full \(u\)-circle.
The constant coefficient of \(|S|^4\) is
\[
m^2+2\sum_{\ell=1}^{m-1}(m-\ell)^2
=\frac{m(2m^2+1)}3.
\]
For the other integral, \((1-u)S=1-u^m\), and the constant coefficient of \(|1-u^m|^2|S|^2\) is \(2m\).
Dividing by \(m^4\) proves (3).

The strict cut gives \(\mu_j=(b_j-c)r_j>0\).
Since \(\deg((t-c)g_m^2)=4m-3\le L-2\), (2), (3) and oddness give
\[
\sum_j\mu_j g_m(b_j)^2
=\int(t-c)t^2g_m(t)^2\,d\alpha(t)
=S_m.                                                     \tag{4}
\]
Every odd conductor has no zero grid node, and \(B_n(0)=(-1)^{\lfloor n/2\rfloor}\).
From \(Q/B_n=t+\sum_jr_j/(t-b_j)\),
\[
\frac{Q(0)}{B_n(0)}=-\sum_j\frac{r_j}{b_j}.
\]
The odd polynomial \((g_m^2-1)/t\) has a vanishing moment in (2), so
\[
\frac{Q(0)}{B_n(0)}
=-\sum_j\frac{r_jg_m(b_j)^2}{b_j}
=-\sum_j\frac{\mu_jg_m(b_j)^2}{b_j(b_j-c)}.
\]
Therefore \(|Q(0)|\le D_1S_m<1\).
Its integrality forces \(Q(0)=0\).

After that vanishing, differentiation of the same rational identity gives
\[
\frac{Q'(0)}{B_n(0)}
=1-\sum_j\frac{r_j}{b_j^2}
=A_m-\sum_j\frac{r_jg_m(b_j)^2}{b_j^2}.                  \tag{5}
\]
The last equality uses (2) with the polynomial \((1-g_m^2)/t^2\).
These polynomial divisions are valid because \(g_m\) is even and \(g_m(0)=1\); their degrees are within the prefix range.
By (4), the absolute value in (5) is at most \(A_m+D_2S_m<1\).
Again integrality gives \(Q'(0)=0\).

Thus \(t^2\mid Q\).
With the strict endpoint, division by \(t^2\) preserves every original residue sign and the endpoint sign, since no grid node is zero.
The degree-\((n-1)\) quotient has one root in each of the \(n-2\) same-sign gaps and one between \(-2\) and the smallest node.
Those roots exhaust its degree, so every trace root of \(Q\), including the two zeros, lies in \([-2,2]\).
All roots of the complete reciprocal lift lie on the unit circle, proving \(M(P)=1\).

<a id="integer-401"></a>
## Exact arithmetic of the conductor-401 jet test

The elementary inequalities \(3<\pi<22/7\), together with sine and cosine Taylor bounds, give
\[
b_{200}+2<(22/2807)^2<1/10000,
\]
and
\[
b_{199}+2>(9/401)^2-\tfrac1{12}(9/401)^4>1/2000.
\]
Hence \(c=-19997/10000\) is in the required gap and
\[
c-b_{200}>1/5000,\qquad b_{199}-c>1/5000.                 \tag{6}
\]
The closest node to zero is \(b_{100}=2\sin(\pi/802)\), and
\[
|b_j|\ge2\sin(\pi/802)>
 3/401-9/802^3>1/134.                                   \tag{7}
\]

For \(|b_j|\ge1\), (6) controls both products in the denominator of (1).
For \(|b_j|<1\), one has \(b_j-c>9/10\), so (7) gives \(|b_j(b_j-c)|>1/5000\).
For \(1/4\le|b_j|<1\), also \(b_j^2(b_j-c)>(1/16)(9/10)>1/10400\).
Finally, when \(|b_j|<1/4\), one has \(b_j-c>87/50\), and
\[
b_j^2(b_j-c)>\frac{87}{50\cdot134^2}
             =\frac{87}{897800}>\frac1{10400}.
\]
Thus the stated \(D_1,D_2\) are valid upper bounds.

With \(m=35\), the two tests are
\[
D_1S_m=\frac{19997}{42875}<1,
\]
and
\[
A_m+D_2S_m
<\frac{2451}{128625}+\frac{41600}{42875}
=\frac{127251}{128625}<1.
\]
This proves the integer conclusion without using a numerical solver or the stronger grid certificate.

<a id="real-grid-certificate"></a>
## A finite grid polynomial excludes the entire real cell

For this section fix \(p=401,n=200\).
Let \(U\) be the following 62 indices:
\[
\begin{split}
U=\{&
2,5,8,13,16,19,22,25,28,31,36,39,42,45,48,51,54,59,62,65,68,\\
&71,74,77,82,85,88,91,94,97,102,105,108,111,114,117,120,125,128,\\
&131,134,137,140,143,148,151,154,157,160,163,166,171,174,177,180,\\
&183,186,189,192,195,198,200\}.
\end{split}
\]
Put \(Z=\{1,\ldots,200\}\setminus U\), and define the exact real polynomial
\[
G(t)=-\prod_{j\in Z}(t-b_j),\qquad \deg G=138.
\]
The [native checker](../computations/programs/Yin_J_G0159/grid_certificate.py) retains exactly this complementary root list.

Because the \(b_j\) strictly decrease with \(j\), the sign at a nonzero node is
\[
\operatorname{sgn}G(b_j)
=-(-1)^{\#\{i\in Z:i<j\}}.
\]
All gaps between successive members of \(U\setminus\{200\}\) are odd, the first member is two, and its last member is 198.
Consequently \(G(b_j)>0\) on \(U\setminus\{200\}\), \(G(b_{200})<0\), and \(G(b_j)=0\) on \(Z\).
Thus every proposed strict-cut \(h\) would satisfy
\[
\sum_{j=1}^{200}\nu_jG(b_j)h(b_j)>0.                    \tag{8}
\]

But write
\[
h_{\mathrm{fix}}=2E_0+4\sum_{\substack{2\le i\le138\\i\ {\rm even}}}E_i.
\]
The remainder \(h-h_{\mathrm{fix}}\) is a linear combination of \(E_{139},\ldots,E_{199}\).
Since \(G\) has degree 138, the exact full-grid orthogonality gives
\[
\sum_j\nu_jG(b_j)h(b_j)
=\sum_j\nu_jG(b_j)h_{\mathrm{fix}}(b_j)=:\mathcal F.       \tag{9}
\]
This step works for arbitrary real free coefficients and imposes no coefficient box.

The retained validated calculation encloses the explicit finite functional by
\[
                         -56<\mathcal F<-55.            \tag{10}
\]
It evaluates only the 62 nonzero terms.
For each such node it uses
\[
\nu_jG(b_j)h_{\mathrm{fix}}(b_j)
=\frac4{401}\sin\theta_j\,G(b_j)
 \left[2\sin\theta_j+
       4\sum_{\substack{2\le i\le138\\i\ {\rm even}}}
          \sin((i+1)\theta_j)\right].
\]
At the other nodes the product has an exact zero factor, so no uncertain interval zero is discarded.
The calculation uses 512-bit Arb enclosures for \(\pi\), sine, cosine and all arithmetic and checks both rational bounds in (10).
It obtains a ball centered near \(-55.8029788490444239\), with radius below \(7\cdot10^{-148}\).
The finite input, complete program and reproducible [output](../computations/outputs/Yin_J_G0159/grid_certificate.json) remain in J159.
The strict negative bound contradicts (8), proving real infeasibility.

<a id="limits"></a>
## Consequences for construction

This closes the proposed conductor-401, one-negative-node, length-140 cell before an integer search.
It complements the earlier three-negative-node obstruction rather than extending that old proof by assertion.
The general integer-jet criterion retains a useful parameter-sensitive test at other conductors; failure of its inequalities establishes no feasible point.
The distinct [J159 larger-conductor proposal](../computations/programs/Yin_J_G0159/readme.md#question) must be checked on its own actual input.
Neither a real feasible tail nor a finite integer search supplies a nonneutral integer input automatically.
The unrestricted G0001 contract remains unresolved.

## Current assessment

[Selected decision](#decision-integer-jets-grid-exclusion)

## Assessment history

### Decision integer-jets-grid-exclusion

| Field | Value |
| --- | --- |
| date | 2026-11-10T06:32 |
| status | proved |
| reason | Complete independent review verifies the general sufficient integer-jet criterion, the exact conductor-401 application and the stronger real-cell exclusion; a separately implemented exact interval calculation certifies the decisive negative functional. Larger-conductor integer supply and the unrestricted gap remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statements](#statement) | General integer criterion, its complete-measure consequence with the endpoint, the conductor-401 application, separate real infeasibility and unchanged negative-one theorem. |
| argument | [Whole proof and inputs](#argument) | Complete mathematical chain, including every degree bound and the validated finite functional. |
| argument | [Integer jets](#fejer-jets) | Exact moments, sequential integer vanishing and the complete double-factor consequence. |
| argument | [Conductor-401 arithmetic](#integer-401) | Exact separator, denominator bounds and both strict rational tests. |
| argument | [Real grid exclusion](#real-grid-certificate) | Exact grid-polynomial signs, full-tail annihilation and strict negative enclosure. |
| dependency | [Retained negative-one theorem](Yin_C_G0881_v4.md#decision-integer-pole-prefix) | Unchanged adopted integer-pole statement, retaining its own hypotheses. |
| dependency | [Original domain](Yin_C_G0881_v3.md#original-domain) | Full grid, partial fractions, original multiplicities and endpoint. |
| dependency | [Exact prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Original integer remainder and permitted coefficient range. |
| dependency | [Prefix moments](Yin_C_G0881_v3.md#prefix-cut-compatibility) | Exact full-grid quadrature and arcsine identity at every stated degree. |
| dependency | [Double-factor obstruction](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction) | Complete measure one after both jets vanish and the strict endpoint holds. |
| dependency | [Fixed grid certificate](../computations/programs/Yin_J_G0159/grid_certificate.py) | Exact finite input and validated negative functional, independently checked by a different arithmetic method. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v30.md#integer-jets-grid-certificate-review) | Entire fixed statement and proof, all actual dependencies, native aggregate certificate and its exact independent enclosure. |
