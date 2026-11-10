---
author: Yin
---

# Exact zero jets and six derivative branches in the conductor-2003 cell

<a id="statement"></a>
## Statements and original domain

Retain the [adopted v5 results](Yin_C_G0881_v5.md#decision-integer-jets-grid-exclusion) unchanged.
The new conclusions concern the zero profile in [C881 v3's full odd-grid domain](Yin_C_G0881_v3.md#original-domain).
Thus \(p=2n+1\) is odd, \(b_j=2\cos(2\pi j/p)\), \(r_j=\nu_jh(b_j)\), \(\nu_j=(4-b_j^2)/p\), and
\[
h=\sum_{i=0}^{n-1}a_iE_i,\quad C=B_{n-1}h\bmod B_n,\quad
Q=tB_n+C,\quad P=z^{n+1}Q(z+z^{-1}).
\]
Assume the strict single-cut signs, a negative separator
\(b_{n-\kappa+1}<c<b_{n-\kappa}\), and the zero-profile prefix through \(2\le L\le n+1\).
Let \(m\ge2\) satisfy \(4m-1\le L\), and set
\[
A_m=\frac{2m^2+1}{3m^3}.
\]

For every such real input,
\[
 |Q(0)|\le\frac{2/|c|+2/\beta}{m^3}
 \quad\text{whenever}\quad
 0<\beta\le\min_j|b_j|.                                      \tag{1}
\]
In particular, for integer coefficients, \(c\le-1\) and \(m^3>p+2\) imply \(Q(0)=0\).
This conclusion needs no endpoint assumption.

When \(Q(0)=0\), there is an explicitly defined probability distribution on the original nodes for which
\[
 \mathbb E(1/b)=-1/c,\qquad
 \frac{Q'(0)}{B_n(0)}
       =A_m-\frac2{m^3}\mathbb E(1/b^2).                    \tag{2}
\]
Consequently, if real numbers \(a<d\) strictly enclose all reciprocals \(1/b_j\), then
\[
 A_m-\frac2{m^3}\left(\frac{a+d}{|c|}-ad\right)
 <\frac{Q'(0)}{B_n(0)}<A_m.                                \tag{3}
\]
These are necessary bounds, not an integer-existence assertion.

At \(p=2003,n=1001,\kappa=1,L=140\), every integer input in the strict sign chamber satisfies
\[
             Q(0)=0,\qquad Q'(0)\in\{-6,-5,\ldots,0\}.     \tag{4}
\]
If the strict endpoint \(P(-1)>0\) also holds and the complete measure is greater than one, only
\[
                          Q'(0)\in\{-6,\ldots,-1\}         \tag{5}
\]
remain.
The six complete affine integer branches are described below.
No integer feasibility, infeasibility or new positive measure is asserted for them.

<a id="argument"></a>
## Inputs and proof arrangement

The argument uses [v3's exact prefix moment identity](Yin_C_G0881_v3.md#prefix-cut-compatibility), its [original partial fractions](Yin_C_G0881_v3.md#original-domain), and [v5's explicit Fejer polynomial and two exact moments](Yin_C_G0881_v5.md#fejer-jets).
The endpoint consequence uses the [complete double-factor obstruction](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction).
All new estimates and the affine lattice calculation were developed by the main research agent with ordinary proof and construction collaborators.
They require a separately organized review before adoption.
The numerical extrema and searches in [J159](../computations/programs/Yin_J_G0159/readme.md#results) are not premises.

<a id="positive-weight-jets"></a>
## A linear multiplier removes the cut denominator

Write \(d\alpha=dt/(\pi\sqrt{4-t^2})\), and use
\[
g_m(t)=\frac1{m^2}
 \left[m+\sum_{\ell=1}^{m-1}(m-\ell)(-1)^\ell T_{2\ell}(t)\right].
\]
The fixed inputs give
\[
 \sum_jr_j f(b_j)=\int t^2f(t)\,d\alpha
       \quad(\deg f\le L-2),
 \qquad
 \int g_m^2\,d\alpha=A_m,\quad
 \int t^2g_m^2\,d\alpha=\frac2{m^3}.
\]
Here \(g_m\) is even, has degree \(2m-2\), and \(g_m(0)=1\).
Define
\[
 \mu_j=(b_j-c)r_j>0,\qquad
 S_m=\sum_j\mu_jg_m(b_j)^2=-\frac{2c}{m^3}>0,
 \qquad
 w_j=\frac{\mu_jg_m(b_j)^2}{S_m}.
\]
The formula for \(S_m\) uses the polynomial \((t-c)g_m^2\), whose degree \(4m-3\) is at most \(L-2\).
The weights are nonnegative and sum to one; they may vanish at zeros of \(g_m\).
Expectations below use these weights on the original nonzero grid nodes.

Set
\[
                  g(t)=(1-t/c)g_m(t).
\]
This polynomial has \(g(0)=1\), \(g'(0)=-1/c\) and degree \(2m-1\).
It need not be even.
The polynomial \((g^2-1)/t\) has degree at most \(4m-3\), so the prefix identity and partial fractions give
\[
\begin{aligned}
 \frac{Q(0)}{B_n(0)}
 &=\int t g(t)^2\,d\alpha-\sum_j\frac{r_jg(b_j)^2}{b_j}\\
 &=-\frac4{cm^3}
   -\frac{S_m}{c^2}\mathbb E\left(\frac{b-c}{b}\right)\\
 &=-\frac2{cm^3}-\frac2{m^3}\mathbb E(1/b)
  =\frac2{m^3}\left(\frac1{|c|}-\mathbb E(1/b)\right).       \tag{6}
\end{aligned}
\]
The integral in the second line uses evenness of \(g_m\); only the term \(-2t^2g_m^2/c\) survives.
Since \(|B_n(0)|=1\), equation (6) proves (1).

For every odd \(p\), the closest angular distance of a node to \(\pi/2\) is \(\pi/(2p)\).
Hence
\[
 \min_j|b_j|=2\sin\frac{\pi}{2p}>\frac2p,
\]
where the strict inequality follows from strict concavity of sine between zero and \(\pi/2\).
Equation (6) therefore gives
\[
             |Q(0)|<\frac{p+2/|c|}{m^3}.
\]
When \(c\le-1\) and \(m^3>p+2\), an integer \(Q(0)\) must vanish.
The monic integer remainder convention ensures this integrality.

Now suppose \(Q(0)=0\).
Equation (6) gives the first identity in (2).
To obtain the derivative formula without treating \(g\) as even, use the polynomial
\[
                   f(t)=\frac{1-g(t)^2+2g'(0)t}{t^2}.
\]
Both its constant and linear numerator coefficients vanish, and its degree is at most \(4m-4\).
Also \(\sum_jr_j/b_j=0\), by the original partial fractions and \(Q(0)=0\).
Thus the linear correction contributes zero on the discrete side and has zero arcsine integral after multiplication by \(t^2\).
The prefix identity gives
\[
 \sum_j\frac{r_j}{b_j^2}
 -\sum_j\frac{r_jg(b_j)^2}{b_j^2}
 =1-\int g^2\,d\alpha.
\]
Differentiating \(Q/B_n\) after \(Q(0)=0\), and using
\(\int g^2\,d\alpha=A_m+2/(c^2m^3)\), now yields
\[
\begin{aligned}
 \frac{Q'(0)}{B_n(0)}
 &=A_m+\frac2{c^2m^3}
   -\frac{S_m}{c^2}\mathbb E\left(\frac{b-c}{b^2}\right)\\
 &=A_m+\frac2{c^2m^3}
   +\frac2{cm^3}\mathbb E(1/b)
   -\frac2{m^3}\mathbb E(1/b^2)\\
 &=A_m-\frac2{m^3}\mathbb E(1/b^2).
\end{aligned}
\]
This proves (2).
Every reciprocal is nonzero, so its squared expectation is strictly positive.
If \(a<1/b_j<d\) for every node, then
\[
 (1/b_j)^2<(a+d)/b_j-ad.
\]
Averaging this strict inequality and using (2) proves (3), including both strict signs.

<a id="six-derivatives"></a>
## Entire integer jet range at conductor 2003

Take \(m=35\) and \(c=-199999/100000\).
The elementary inequalities \(3<\pi<22/7\) and cosine Taylor bounds give
\[
 b_{1001}+2<\left(\frac{22}{7\cdot2003}\right)^2
                  <\frac1{100000},
\]
and
\[
 b_{1000}+2>
 \left(\frac9{2003}\right)^2
 -\frac1{12}\left(\frac9{2003}\right)^4
                  >\frac1{100000}.
\]
Thus \(c\) is in the required last gap, with \(-2<c<-1\).
All bounds are strict rational comparisons after the displayed Taylor estimates.
Since \(4m-1=139\le140\) and \(m^3=42875>2005=p+2\), equation (1) forces \(Q(0)=0\).

The closest positive node is
\(b_{500}=2\sin(3\pi/(2p))\), while the closest negative node is
\(b_{501}=-2\sin(\pi/(2p))\).
Sine Taylor bounds, with \(p=2003\), give
\[
 b_{500}>\frac9p-\frac{729}{24p^3}>\frac1{223},
 \qquad
 |b_{501}|>\frac3p-\frac{27}{24p^3}>\frac1{668}.            \tag{7}
\]
The lower sine-polynomial is increasing on the small intervals used here, so substituting the lower bound \(\pi>3\) preserves these inequalities.
Monotonicity of the grid proves
\[
                         -668<1/b_j<223
\]
for every node.
With \(a=-668,d=223\), equation (2), \(|c|<2\), and the quadratic chord inequality give
\[
 \mathbb E(1/b^2)
 <-445\,\mathbb E(1/b)+148964
 <148964-\frac{445}{2}
 =\frac{297483}{2}.
\]
Moreover \(B_{1001}(0)=1\).
Consequently
\[
 -7<
 -\frac{889998}{128625}
 =\frac{2451}{128625}-\frac{297483}{42875}
 <Q'(0)<\frac{2451}{128625}<1.                             \tag{8}
\]
The derivative is an integer, so (8) proves (4).
If \(Q'(0)=0\), the already forced \(Q(0)=0\) gives \(t^2\mid Q\).
With the strict endpoint the complete double-factor obstruction yields \(M(P)=1\).
This proves (5) without promoting a numerical LP range to an exact bound.

<a id="complete-affine-branches"></a>
## Exact integer coordinates on all six remaining branches

The fixed prefix leaves
\[
 Q_{\rm fix}=tB_{1001}+2B_{1000}
                 +4\sum_{r=1}^{69}B_{1000-2r},\qquad
 C_{\rm free}=\sum_{i=139}^{1000}a_iB_{1000-i}.
\]
The monic integer polynomials \(B_0,\ldots,B_{861}\) form a triangular integer basis with determinant one.
Thus the free tail is exactly all of \(\mathbb Z[t]_{\le861}\).

The formulas
\[
 B_j(0)=(-1)^{\lfloor j/2\rfloor},\quad B'_0(0)=0,\quad
 B'_{2r}(0)=(-1)^{r-1}r,\quad
 B'_{2r+1}(0)=(-1)^r(r+1)
\]
give \(Q_{\rm fix}(0)=-2\) and \(Q'_{\rm fix}(0)=861\).
Indeed \(\sum_{r=1}^{69}(-1)^r=-1\) and
\(\sum_{r=1}^{69}r(-1)^r=-35\), so the derivative is
\(1-1000+1860=861\).

For each \(k\in\{1,\ldots,6\}\), the complete integer branch \(Q(0)=0,Q'(0)=-k\) is therefore
\[
       C_{\rm free}=2-(861+k)t+t^2R,\qquad
       R\in\mathbb Z[t]_{\le859}.                          \tag{9}
\]
The necessity follows by subtracting the required constant and linear terms and dividing by the monomial \(t^2\) over the integers.
The converse follows by evaluation and differentiation at zero.
There is no coefficient box or sublattice restriction in (9).

Writing \(R=\sum_{j=0}^{859}u_jB_j\) preserves the entire integer lattice.
The affine baseline is
\((863+k)B_0-(861+k)B_1\).
The multiplication columns are
\[
\begin{aligned}
 t^2B_0&=B_2-B_1+2B_0,\\
 t^2B_1&=B_3+2B_1-B_0,\\
 t^2B_j&=B_{j+2}+2B_j+B_{j-2}\qquad(j\ge2).
\end{aligned}
\]
The first two follow from \(B_0=1,B_1=t+1,B_2=t^2+t-1\) and \(B_3=t^3+t^2-2t-1\); the others follow by applying the recurrence twice.
Both exceptional columns are required for the complete lattice.

The exact endpoint is
\[
       P(-1)=2004+2k+4R(-2)
            =2004+2k+4\sum_{j=0}^{859}(-1)^ju_j.           \tag{10}
\]
This follows either by evaluating \(Q\) at \(-2\), or by the original identity
\(P(-1)=280+\sum_{i=139}^{1000}(-1)^ia_i\).
Thus a positive integer endpoint is at least two for odd \(k\) and at least four for even \(k\).
The original strict signs and complete nonneutrality remain additional requirements.

<a id="limits"></a>
## Construction consequences and remaining scope

The conductor-2003 zero jet is now an analytic integer consequence, not a branch selected only by floating extrema.
Every nonneutral admissible integer input in this fixed cell must occur in one of the six affine lattices (9).
The estimates do not force the derivative to be minus one, nor do they certify any integer point satisfying all signs.
The rational witness and bounded local repair on that one branch in J159 have their separate finite evidence and review scopes.
Failure of that repair does not exclude the branch or the other five branches.
The unrestricted G0001 contract remains unresolved.

## Current assessment

[Selected decision](#decision-positive-weight-jets)

## Assessment history

### Decision positive-weight-jets

| Field | Value |
| --- | --- |
| date | 2026-11-10T06:57 |
| status | proved |
| reason | Complete independent review verifies both positive-weight identities, the sufficient integer zero-jet condition, every strict conductor-2003 comparison, all six full affine branches and the precise endpoint/nonneutrality qualification. Integer completion remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | General real bounds, integer zero-jet implication, complete conductor-2003 derivative range and six nonneutral branches. |
| argument | [Whole argument and inputs](#argument) | Complete fixed proof and actual dependency scope. |
| argument | [Positive-weight identities](#positive-weight-jets) | Non-even multiplier, both quotient polynomials, all degree bounds, exact moments and strict inequalities. |
| argument | [Conductor-2003 range](#six-derivatives) | Exact separator, node bounds, integer derivative list and endpoint consequence. |
| argument | [Full affine branches](#complete-affine-branches) | Entire integer tail, exact fixed jets, both exceptional columns and endpoint congruence. |
| dependency | [Retained v5 adoption](Yin_C_G0881_v5.md#decision-integer-jets-grid-exclusion) | Unchanged earlier statements and adopted scope. |
| dependency | [Fejer polynomial](Yin_C_G0881_v5.md#fejer-jets) | Explicit even polynomial and both exact moments. |
| dependency | [Original domain](Yin_C_G0881_v3.md#original-domain) | Partial fractions, original residues and complete reciprocal lift. |
| dependency | [Prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Original integer basis and prefix/endpoint identity. |
| dependency | [Prefix moments](Yin_C_G0881_v3.md#prefix-cut-compatibility) | Full-grid identity at every permitted test degree. |
| dependency | [Double-factor obstruction](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction) | Complete measure one when the two jets vanish and the strict endpoint holds. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v32.md#positive-weight-jets-six-branches-review) | Entire fixed statement and proof, all actual inputs and complete integer-coordinate coverage. |
