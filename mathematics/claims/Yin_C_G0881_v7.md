---
author: Yin
---

# A quadratic Fourier kernel leaves four integer derivative branches

<a id="statement"></a>
## Scope and strengthened statements

Retain the [v6 results and exact affine coordinates](Yin_C_G0881_v6.md#statement) at their stated scopes.
This version strengthens the conductor-2003 derivative range using another explicit even polynomial.
Use the same full odd-grid zero-profile domain, negative strict separator \(c\), prefix length \(L\), and integer \(m\ge2\) with \(4m-1\le L\).
There is a polynomial \(\phi_m\) of degree \(2m-2\), even and equal to one at zero, whose moments are
\[
 0<\mathcal A_m:=\int\phi_m^2\,d\alpha<1,\qquad
 \mathcal J_m:=\int t^2\phi_m^2\,d\alpha
            =\frac6{m(4m^2-1)}.                           \tag{1}
\]
Its construction is explicit below; no optimality assertion is needed.

For every real input in this domain and every
\(0<\beta\le\min_j|b_j|\),
\[
 |Q(0)|\le\mathcal J_m(1/|c|+1/\beta).                   \tag{2}
\]
Thus integer coefficients, \(c\le-1\), and
\[
                  m(4m^2-1)>3(p+2)
\]
force \(Q(0)=0\).
Under \(Q(0)=0\), nonnegative probability weights on the original grid give
\[
 \mathbb E(1/b)=1/|c|,\qquad
 Q'(0)/B_n(0)=\mathcal A_m-\mathcal J_m\mathbb E(1/b^2).
                                                                    \tag{3}
\]

At \(p=2003,n=1001,\kappa=1,L=140\), every integer input with the required strict signs has
\[
                 Q(0)=0,\qquad Q'(0)\in\{-4,-3,-2,-1,0\}.             \tag{4}
\]
With the positive endpoint and \(M(P)>1\), only the four negative derivatives remain.
Consequently every such nonneutral integer input belongs to one of the four complete affine lattices
\[
 C_{\rm free}=2-(861+k)t+t^2R,\qquad
 k\in\{1,2,3,4\},\quad R\in\mathbb Z[t]_{\le859}.          \tag{5}
\]
No actual integer completion or small positive measure is asserted.

<a id="argument"></a>
## Mathematical inputs and proof scope

The proof uses [C881 v3's original domain](Yin_C_G0881_v3.md#original-domain), [exact prefix moments](Yin_C_G0881_v3.md#prefix-cut-compatibility), and [exact prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates).
The explicit conductor-2003 separator and complete affine-lattice calculation are retained in [v6](Yin_C_G0881_v6.md#six-derivatives) and [its branch argument](Yin_C_G0881_v6.md#complete-affine-branches).
The zero-derivative endpoint consequence is the [complete double-factor obstruction](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction).
The main researcher and an ordinary proof collaborator developed this kernel and its estimates.
The numerical LP extrema and local integer repair are not proof inputs.
The current assessment owns the actual review and adoption status.

<a id="quadratic-kernel"></a>
## Explicit Fourier coefficients and exact energy

For \(-m<\ell<m\), put
\[
 \alpha_\ell=\frac{3(m^2-\ell^2)}{m(4m^2-1)},
\]
and put \(\alpha_\ell=0\) outside this range.
These coefficients are symmetric and strictly positive on their support.
The elementary sum
\[
 \sum_{\ell=-m+1}^{m-1}(m^2-\ell^2)=\frac{m(4m^2-1)}3
\]
shows that \(\sum_\ell\alpha_\ell=1\).
Define
\[
 \phi_m(t)=\alpha_0+
       \sum_{\ell=1}^{m-1}\alpha_\ell(-1)^\ell T_{2\ell}(t).
\]
This is a real even polynomial of degree \(2m-2\), and \(\phi_m(0)=1\).

With \(t=2\cos\theta\) and \(u=e^{2i(\theta-\pi/2)}\), it has the symmetric Laurent form
\[
                    \phi_m=\sum_\ell\alpha_\ell u^\ell.
\]
The arcsine integral traverses one complete \(u\)-circle and extracts its constant coefficient.
Symmetry and real coefficients give
\[
                    \mathcal A_m=\sum_\ell\alpha_\ell^2.
\]
There is more than one positive coefficient, so
\(0<\mathcal A_m<(\sum_\ell\alpha_\ell)^2=1\).

Also \(t^2=|1-u|^2\), so
\[
 \mathcal J_m=\sum_{\ell\in\mathbb Z}
                         (\alpha_\ell-\alpha_{\ell-1})^2.
\]
Writing \(K=3/[m(4m^2-1)]\), the nonzero differences are
\(K(1-2\ell)\) for \(-m+1\le\ell\le m\), including both boundary differences.
Therefore
\[
\begin{aligned}
 \mathcal J_m
 &=2K^2\sum_{j=1}^m(2j-1)^2\\
 &=2K^2\,\frac{m(4m^2-1)}3
  =\frac6{m(4m^2-1)}.
\end{aligned}
\]
This proves every assertion in (1) directly.

<a id="weighted-identities"></a>
## Both jets for the new kernel

Write \(A=\mathcal A_m,J=\mathcal J_m\), and define
\[
 \mu_j=(b_j-c)r_j>0,\qquad
 S=\sum_j\mu_j\phi_m(b_j)^2=-cJ>0.
\]
The identity for \(S\) uses the prefix moment at the polynomial
\((t-c)\phi_m^2\), of degree \(4m-3\le L-2\).
Use the probability weights
\(w_j=\mu_j\phi_m(b_j)^2/S\).
Weights may be zero, but their sum is one and every original node is nonzero.

Set \(g=(1-t/c)\phi_m\).
Then \(g(0)=1,g'(0)=-1/c\), and
\[
 \int tg^2\,d\alpha=-2J/c,\qquad
 \int g^2\,d\alpha=A+J/c^2.
\]
The quotient \((g^2-1)/t\) has degree at most \(4m-3\).
Applying the prefix identity to it and using the original partial fractions gives
\[
\begin{aligned}
 Q(0)/B_n(0)
 &=-2J/c-(S/c^2)\mathbb E(1-c/b)\\
 &=-J/c-J\mathbb E(1/b)
  =J(1/|c|-\mathbb E(1/b)).
\end{aligned}
\]
Since \(|B_n(0)|=1\), this proves (2).
The original odd-grid bound
\(\min_j|b_j|=2\sin(\pi/(2p))>2/p\) gives
\[
 |Q(0)|<J(1/|c|+p/2)
       \le\frac{3(p+2)}{m(4m^2-1)}
             \quad\text{when }c\le-1.
\]
The stated sufficient condition forces an integer \(Q(0)\) to vanish.

Under that vanishing, the displayed identity gives \(\mathbb E(1/b)=-1/c\).
Use
\[
                 \frac{1-g^2+2g'(0)t}{t^2},
\]
which is a polynomial of degree at most \(4m-4\).
Its linear correction has zero discrete contribution because \(\sum_jr_j/b_j=0\), and zero arcsine contribution because \(\int t\,d\alpha=0\).
Differentiating \(Q/B_n\) after the zero jet, and applying this prefix identity, gives
\[
\begin{aligned}
 Q'(0)/B_n(0)
 &= A+J/c^2-(S/c^2)\mathbb E(1/b-c/b^2)\\
 &= A+J/c^2+(J/c)\mathbb E(1/b)-J\mathbb E(1/b^2)\\
 &= A-J\mathbb E(1/b^2).
\end{aligned}
\]
This proves (3) without an evenness assumption on the multiplied polynomial \(g\).

<a id="four-derivatives"></a>
## Pure rational bounds at conductor 2003

Take \(p=2003,m=35,c=-199999/100000\).
The [fixed elementary separator argument](Yin_C_G0881_v6.md#six-derivatives) gives
\(b_{1001}<c<b_{1000}\) and \(-2<c<-1\).
The new zero-jet estimate is
\[
                  |Q(0)|<\frac{6015}{171465}<1,
\]
so every integer input has \(Q(0)=0\).

For a slightly better elementary node bound, use
\[
 \pi>12\sin(\pi/12)=3(\sqrt6-\sqrt2)>31/10.
\]
The first strict inequality is \(\sin x<x\) at \(x=\pi/12\).
For the last, \(\sqrt6>2449/1000\) and \(\sqrt2<1415/1000\), as squaring these positive rational numbers verifies.
Thus \(3(\sqrt6-\sqrt2)>3102/1000>31/10\).

The closest positive and negative nodes remain
\(b_{500}=2\sin(3\pi/(2p))\) and
\(b_{501}=-2\sin(\pi/(2p))\).
Monotonicity of sine on these short intervals and its cubic Taylor lower bound imply
\[
 b_{500}>
  \frac{93}{10p}-\frac{804357}{24000p^3}>\frac1{216},
 \qquad
 |b_{501}|>
  \frac{31}{10p}-\frac{29791}{24000p^3}>\frac1{647}.        \tag{6}
\]
The final inequalities are strict rational comparisons at \(p=2003\).
For example, after positive multiplication they reduce respectively to
\(58\cdot2400p^2>804357\cdot216\) and
\(27\cdot2400p^2>29791\cdot647\).
Therefore every reciprocal \(X=1/b_j\) lies strictly between \(-647\) and 216.

The strict chord inequality is
\[
                        X^2<139752-431X.
\]
Averaging with the nonnegative weights, using
\(\mathbb EX=1/|c|>1/2\), gives
\[
                 0<\mathbb EX^2<\frac{279073}{2}.
\]
Here \(B_{1001}(0)=1\), and \(J=6/171465\).
Equation (3) now gives
\[
 -5<-\frac{837219}{171465}
       <A-\frac{837219}{171465}<Q'(0)<A<1,               \tag{7}
\]
where \(837219<5\cdot171465=857325\).
The integer derivative is consequently one of \(-4,-3,-2,-1,0\).

With the strict endpoint, the zero derivative forces the complete neutral double factor exactly as in v6.
For a nonneutral input the four remaining negative values select the corresponding \(k=1,\ldots,4\) instances of the complete affine-lattice argument there.
That argument preserves every integer coefficient and gives
\[
                      P(-1)=2004+2k+4R(-2).
\]
It imposes no coefficient box or loss of lattice index.
This proves (4)--(5).

<a id="limits"></a>
## Construction boundary

The four branches exhaust the necessary integer jet values for this one conductor, prefix and cut.
The proof does not assert that each branch has a strict real point or an integer point, and it does not establish nonneutrality from the derivative alone.
The earlier rational minus-one branch and failed finite repair keep their own evidence and limits.
Neither that failure nor this necessary four-branch cover resolves the original integer-completion question or the unrestricted G0001 contract.

## Current assessment

[Selected decision](#decision-quadratic-kernel-four-branches)

## Assessment history

### Decision quadratic-kernel-four-branches

| Field | Value |
| --- | --- |
| date | 2026-11-10T07:04 |
| status | proved |
| reason | Complete independent review verifies the explicit Fourier kernel and both moments, all general weighted identities and integer conditions, every conductor-2003 strict comparison and the four complete necessary affine branches. No branch feasibility or unrestricted gap resolution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statements](#statement) | New kernel, real bounds, integer zero-jet criterion and four-branch conductor-2003 consequence, retaining the earlier v6 results. |
| argument | [Whole argument and inputs](#argument) | Complete fixed proof with actual dependency scope. |
| argument | [Explicit kernel](#quadratic-kernel) | Every support endpoint, normalization and exact energy computation. |
| argument | [Weighted identities](#weighted-identities) | Both jets, possible zero weights, non-even multiplier and all degree conditions. |
| argument | [Four derivative branches](#four-derivatives) | Exact elementary comparisons and full affine/endpoint consequence. |
| dependency | [Retained v6 statement](Yin_C_G0881_v6.md#statement) | Earlier proved results at their unchanged scopes. |
| dependency | [Conductor-2003 separator](Yin_C_G0881_v6.md#six-derivatives) | Fixed last-gap separator and closest-node identities. |
| dependency | [Complete affine coordinates](Yin_C_G0881_v6.md#complete-affine-branches) | Entire integer lattice, both exceptional columns and endpoint, restricted to k from one through four. |
| dependency | [Original domain](Yin_C_G0881_v3.md#original-domain) | Exact residues, partial fractions and complete reciprocal lift. |
| dependency | [Prefix coordinates](Yin_C_G0881_v3.md#prefix-coordinates) | Original integer remainder and prefix. |
| dependency | [Chebyshev normalization](Yin_C_G0881_v3.md#newton-baseline) | Trace polynomial convention used in the Laurent expansion. |
| dependency | [Prefix moments](Yin_C_G0881_v3.md#prefix-cut-compatibility) | Full-grid zero-profile identity and normalized arcsine integral. |
| dependency | [Double-factor obstruction](../ledger/Yin_L_G0462_v11.md#double-factor-obstruction) | Complete neutral consequence with the strict endpoint. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v33.md#quadratic-kernel-four-branches-review) | Entire fixed statement and proof, actual dependencies and complete four-branch transfer. |
