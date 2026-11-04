---
author: Yin
---

# Stable packing certificates, cubic concentration time and trace Fourier costs

This retains the complete original direct mathematics of the2026-10-07 [L100 record](../ledger/Yin_L_G0100_v1.md).
The already adequate [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001) owns the exact arXivv4 strictness proof, zero/zero-set corrections and original pure-type boundary.
Its recorded10/7 pages19–21 whole-proof/visual reread is historical evidence, not a new source inspection in this construction.
The assigned ms25_source agent developed the explicit certificate and concentration-time comparison.
No source, numerical computation or Task is newly executed.

## Statement

Let P be monic irreducible,alpha an algebraic unit of degree d,no conjugate of modulus1,m=log M(P)>0.
Its stable space is R^r times C^c of real dimension s=r+2c,1<=s<d.
For stable beta put r_beta=abs(beta)<1 and let K_N be the product of real intervals[-r_beta^N,r_beta^N] and complex discs of radius r_beta^N.
With all expanding roots counted at complex multiplicity2,define

    V0=2^r pi^c, vol(K_N)=V0 exp(-mN),
    T=max_stable 1/(1-abs(beta)),
    a=(product_expanding(abs(beta)-1))^(1/s),
    gamma=(a/2)^s V0, C=(1+2T/a)^s.

Let Y_N and Y be the finite and infinite stable fair-bit sums.
Then H(Y_N)=H_N of the original algebraic sum, Y_N is in T K0 and Y-Y_N is in T K_N.
Their distinct finite atoms have disjoint(a/2)K_N translates,so |supp(Y_N)|<=C exp(mN).

For a compact A with P(Y in A)>=1-epsilon,0<=epsilon<=1/2,if some integer N>=1 and0<u<1 satisfy
vol(A+(T+a/2)K_N)<=gamma u,put

    kappa=(1-epsilon)log(1/u)-h_bin(epsilon)-epsilon log C.

Then Nm-H_N>=kappa and m-h1>=kappa/N.
If D(m) is the exact cubic posterior lower comparison, every such certificate satisfies

    kappa<=N[m-D(m)].

This is valid without division by a possibly zero bracket.
For kappa>0 the bracket is positive; near zero,

    m-D(m)=(20/3)m³+O(m^4),
    N>=(3/20+O(m)) kappa m^(-3).

For the retained BV20 strictness domain alpha nonzero,M(P)<2,no unit-circle conjugate, its qualitative singularity plus retained external pure-type interface supplies such an A and eventual certificate with kappa>1 by
u=exp(-4),epsilon=min(1/4,1/[4(1+log C)]).
It supplies no uniform waiting time.
A fixed delta>0 and certificates with kappa/(N m³)>20/3+delta for every sufficiently small positive input would exclude only this no-unit-circle branch.
In particular fixed kappa>=kappa0>0 and N<=C0 m^(-b),b<3,would suffice.
Uncontrolled degree dependence, a substituted height m/d or a critical exponent without constants does not suffice.

For u_j the sum of stable alpha^j conjugates and v_j the expanding sum, the retained trace-frequency Fourier nondecay has positive product

    c(P)=product_(j<0) abs(cos(2pi v_j)) product_(j>=0) abs(cos(2pi u_j)).

Let sigma=max(max_stable abs(beta),max_expanding abs(beta)^(-1))<1 and choose integer J>=0 with d sigma^(J+1)<=1/(4pi).
Then

    c(P)>=product_(j=-J)^J abs(cos(2pi u_j))
       exp[-4pi² d² sigma^(2(J+1))/(1-sigma²)].

The zero set is1/4+(1/2)Z; algebraic integrality excludes each zero.
The bound retains spectral and finite-cosine input dependence and gives no uniform concentration-time estimate.

For actual length-N binary fibers f_N put U_N=product f_N(x)^(f_N(x)).
A separately certified rational lower bound q0=a0/b0<=M(P),with positive integers a0,b0,satisfying
U_N a0^(N2^N)>(2b0)^(N2^N)
certifies a positive finite deficit at least N log q0-H_N.
It gives no uniform saving or bound on the first such time.
All source, unit-circle, dimension, complex-rotation, fixed-input and qualitative/quantitative boundaries remain explicit.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:00 |
| status | open |
| reason | Complete original explicit stable-packing, cubic waiting-time and Fourier-tail arguments retained; current whole checking and adoption follow separately, with historical source proof depth unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire unit/no-unit-circle stable packing and quantitative entropy certificate, cubic necessary time and sufficient uniform criterion, exact trace Fourier tail and finite positive-integer test, preserving all pure-type, spectral, degree and source boundaries. |
| argument | [Complete argument](#argument) | Full original2–12: rotation-invariant complex bodies and strict norm separation, mass/volume and two-part entropy constants, compact-null-set waiting time, exact cubic comparison, both cosine tails/zero set and rational finite-deficit test. |
| dependency | [Retained source strictness proof](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Exact arXivv4 Propositions7/17 and Lemma18 with nonzero/unit-circle and cosine-zero corrections, base2 conversion and retained external pure-type interface; no original pure-type proof audit or quantitative singularity rate. |
| dependency | [Cubic all-time comparison](Yin_C_G0290_v1.md#cubic-mahler-comparison-error) | Exact every-N H_N>=N D(m) and absolute local expansion m-D(m)=(20/3)m³+O(m^4), with no new uniform arithmetic exclusion. |
| support | [Exact integer-fiber entropy certificate](Yin_C_G0283_v1.md#first-entropy-drop-height-one) | Existing binary fiber-product method; the local12 uses a separately certified positive rational lower bound for M(P), without execution or a first-time guarantee. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:03 |
| status | proved |
| reason | Adopt the complete original stable packing, quantitative entropy certificate, cubic waiting-time criterion, exact Fourier tails and finite rational test after actual whole self-review; retain the original source/pure-type depth and qualitative waiting-time boundary, with no new source audit or uniform concentration theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire unit/no-unit-circle stable packing and quantitative entropy certificate, cubic necessary time and sufficient uniform criterion, exact trace Fourier tail and finite positive-integer test, preserving all pure-type, spectral, degree and source boundaries. |
| argument | [Argument](#argument) | Full original2–12: rotation-invariant complex bodies and strict norm separation, mass/volume and two-part entropy constants, compact-null-set waiting time, exact cubic comparison, both cosine tails/zero set and rational finite-deficit test. |
| dependency | [Dependency](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Exact arXivv4 Propositions7/17 and Lemma18 with nonzero/unit-circle and cosine-zero corrections, base2 conversion and retained external pure-type interface; no original pure-type proof audit or quantitative singularity rate. |
| dependency | [Dependency](Yin_C_G0290_v1.md#cubic-mahler-comparison-error) | Exact every-N H_N>=N D(m) and absolute local expansion m-D(m)=(20/3)m³+O(m^4), with no new uniform arithmetic exclusion. |
| support | [Support](Yin_C_G0283_v1.md#first-entropy-drop-height-one) | Existing binary fiber-product method; the local12 uses a separately certified positive rational lower bound for M(P), without execution or a first-time guarantee. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-concentration-time-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire unit/no-unit-circle stable packing and quantitative entropy certificate, cubic necessary time and sufficient uniform criterion, exact trace Fourier tail and finite positive-integer test, preserving all pure-type, spectral, degree and source boundaries. |
| argument | [Argument](#argument) | Full original2–12: rotation-invariant complex bodies and strict norm separation, mass/volume and two-part entropy constants, compact-null-set waiting time, exact cubic comparison, both cosine tails/zero set and rational finite-deficit test. |
| dependency | [Dependency](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Exact arXivv4 Propositions7/17 and Lemma18 with nonzero/unit-circle and cosine-zero corrections, base2 conversion and retained external pure-type interface; no original pure-type proof audit or quantitative singularity rate. |
| dependency | [Dependency](Yin_C_G0290_v1.md#cubic-mahler-comparison-error) | Exact every-N H_N>=N D(m) and absolute local expansion m-D(m)=(20/3)m³+O(m^4), with no new uniform arithmetic exclusion. |
| support | [Support](Yin_C_G0283_v1.md#first-entropy-drop-height-one) | Existing binary fiber-product method; the local12 uses a separately certified positive rational lower bound for M(P), without execution or a first-time guarantee. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-concentration-time-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0547_v1.md#f-g294) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="explicit-stable-packing-deficit"></a>
### Explicit stable packing and a finite deficit

Let \(P\) be monic irreducible of degree \(d\), let \(\alpha\) be a unit, and suppose no conjugate has modulus one.
Write the stable embedding space as \(\mathbb R^r\times \mathbb C^c\), with one member of each nonreal conjugate pair and real dimension \(s=r+2c\).
Then \(1\le s<d\).
Use \(\iota\) for this embedding map.
For each stable conjugate \(\beta\), let \(r_\beta=|\beta|<1\), and put

\[
 K_N=\prod_{\beta\ {\rm real,stable}}[-r_\beta^N,r_\beta^N]
       \ \times\!\prod_{\beta\ {\rm complex,stable}}
                         \{z:|z|\le r_\beta^N\},
\]
\[
 V_0=2^r\pi^c,\quad \operatorname{vol}(K_N)=V_0 e^{-mN},
 \quad T=\max_{\beta\ {\rm stable}}\frac1{1-|\beta|},
 \quad a=\left(\prod_{|\beta|>1}(|\beta|-1)\right)^{1/s},
\]
\[
 \gamma=(a/2)^s V_0,\qquad C=(1+2T/a)^s.                 \tag{2}
\]

The expanding product includes both members of each complex pair.
The volume identity uses the unit norm and includes the same multiplicities.
Complex discs make the body exactly invariant under the relevant rotations.
In particular, \(\iota(\alpha)^N K_0=K_N\) under coordinatewise multiplication; no square is incorrectly treated as rotation-invariant.

For independent fair bits \(X_j\), define

\[
 Y_N=\sum_{j<N}X_j\iota(\alpha^j),\qquad
 Y=\sum_{j\ge0}X_j\iota(\alpha^j).
\]

The infinite sum converges absolutely.
Deterministically, \(Y_N\in TK_0\) and \(Y-Y_N\in TK_N\).
Stable projection preserves all algebraic fibers, since each field embedding is injective; thus \(H(Y_N)=H_N\) for the original walk.

Here is an explicit separation bound.
If distinct length-N sums have difference \(x\ne0\), then \(\alpha^{-N}x\) is a nonzero algebraic integer, and for each expanding conjugate,

\[
 |\beta^{-N}x(\beta)|
 \le\sum_{l=1}^{N}|\beta|^{-l}<\frac1{|\beta|-1}.
\]

If \(\iota(x)\in aK_N\), the product of its normalized stable absolute values, with complex multiplicity two, would be at most \(a^s\).
The absolute field norm of \(\alpha^{-N}x\) would then be strictly less than \(a^s\prod_{|\beta|>1}(|\beta|-1)^{-1}=1\), impossible.
Therefore distinct atoms differ by a vector outside \(aK_N\).
Their translates of \((a/2)K_N\) are disjoint, and are contained in \((T+a/2)K_0\).
Comparing volumes gives

\[
 |\operatorname{supp}(Y_N)|\le C e^{mN}.                 \tag{3}
\]

Now let \(A\) be a compact set with \(\mathbb P(Y\in A)\ge1-\varepsilon\), where \(0\le\varepsilon\le1/2\).
Suppose that for some \(N\ge1\) and \(0<u<1\),

\[
 \operatorname{vol}\bigl(A+(T+a/2)K_N\bigr)\le\gamma u.
                                                               \tag{4}
\]

The selected atoms \(\operatorname{supp}(Y_N)\cap(A+TK_N)\) carry mass at least \(1-\varepsilon\).
Their disjoint \((a/2)K_N\) translates lie in the set in (4), so they number at most \(u e^{mN}\).
Let \(p\le\varepsilon\) be the remaining mass.
Conditioning on membership in the selected set and bounding conditional entropy by log cardinality give

\[
 H_N\le Nm+h_{\rm bin}(p)+(1-p)\log u+p\log C,
 \quad h_{\rm bin}(p)=-p\log p-(1-p)\log(1-p).
\]

The expression after \(Nm\) increases for \(0\le p\le\varepsilon\le1/2\), since its derivative is \(\log((1-p)C/(pu))\ge0\).
Empty complementary sets are handled by \(p=0\).
Consequently, with

\[
 \kappa=(1-\varepsilon)\log(1/u)
             -h_{\rm bin}(\varepsilon)-\varepsilon\log C,
\]
\[
 \boxed{\ Nm-H_N\ge\kappa,\qquad
             m-h_1\ge\kappa/N.\ }                       \tag{5}
\]

The second assertion uses subadditivity, \(h_1\le H_N/N\), not a limit of strict finite inequalities.
Formula (5) is useful when \(\kappa>0\).
It displays separately the high-mass error, relative volume, total packing cost, and waiting time.

<a id="strictness-concentration-time-barrier"></a>
### The cubic comparison forces slow concentration

Let \(D(m)\) denote the explicit lower entropy function in [C290](Yin_C_G0290_v1.md#cubic-mahler-comparison-error):

\[
 D(m)=\max\left\{g(\sqrt{1-e^{-2m}}),
       F(1-e^{-2m})\right\},\qquad
 F(l)=l/2+l^2(3-2l)^4/324.
\]

For every \(N\), that record proves \(H_N\ge ND(m)\).
Thus every occurrence of (4)--(5) necessarily satisfies

\[
 \boxed{\ \kappa\le N\,[m-D(m)].\ }                    \tag{6}
\]

This statement is valid without dividing by a possibly zero quantity.
If \(\kappa>0\), then the bracket must be positive and \(N\ge\kappa/[m-D(m)]\).
For sufficiently small positive \(m\), the fourth-moment branch is the larger one and

\[
 m-D(m)=\tfrac{20}{3}m^3+O(m^4),\qquad
 N\ge\left(\tfrac3{20}+O(m)\right)\kappa m^{-3}.          \tag{7}
\]

The absolute local Taylor constants and the nonlinear comparison are exactly those of L G0097.
Equation (7) is a necessary scale for a prescribed entropy saving; it does not assert that this scale is attainable.

To make the qualitative singularity argument concrete, set

\[
 u=e^{-4},\qquad
 \varepsilon=\min\{1/4,\,[4(1+\log C)]^{-1}\}.
                                                               \tag{8}
\]

Then \(\kappa\ge3-\log2-1/4>1\).
Under [the retained source domain](../ledger/Yin_L_G0100_v1.md#strict-deficit-source-scope), with \(\alpha\ne0\), \(M(P)<2\) and no conjugate of modulus one, the retained singularity statement supplies a compact Lebesgue-null set \(A\) of mass at least \(1-\varepsilon\), by regularity of the probability law on its compact support.
The compact sets \(A+(T+a/2)K_N\) decrease to \(A\).
They have finite volume, so continuity from above makes (4) eventually true.
This proves existence of a certificate with \(\kappa>1\), but (6)--(7) show that its first possible time is at least order \(m^{-3}\).
The compact set and its required mass also depend on the input through \(C\).

For the no-unit-circle branch, a sufficient new uniform input would be: every sufficiently small positive \(m\) admits (4) with

\[
 \frac{\kappa}{Nm^3}>\frac{20}{3}+\delta                 \tag{9}
\]

for one fixed \(\delta>0\).
This would contradict (6) for all sufficiently small \(m\).
In particular, fixed \(\kappa\ge\kappa_0>0\) and a uniform bound \(N\le C_0m^{-b}\) with \(b<3\) would suffice.
A bound with extra uncontrolled degree dependence does not suffice: the degree is unbounded, and the height \(m/d\) cannot be silently substituted for \(m\).
A bound proportional to \(m^{-3}\) needs its constants compared with (9).
Even a successful proof of this criterion would cover only the branch with no unit-circle conjugate; the full Lehmer problem includes the excluded branch.

<a id="trace-fourier-quantitative-boundary"></a>
### What the trace Fourier product actually controls

The inspected source proof uses fair signs; their infinite stable sum is an affine image of \(Y\), so singularity is equivalent.
Let \(u_j\) be the sum of all stable conjugates of \(\alpha^j\), with both members of each complex pair, and \(v_j\) the sum of all expanding conjugates.
For every integer \(j\), \(u_j+v_j\in\mathbb Z\).
The trace frequencies \(\zeta_t\) of source p.19 satisfy

\[
 |\widehat\mu(\zeta_t)|\ge c(P),\qquad
 c(P)=\prod_{j=-\infty}^{-1}|\cos(2\pi v_j)|
             \prod_{j=0}^{\infty}|\cos(2\pi u_j)|>0.
                                                               \tag{10}
\]

Here \(\|\zeta_t\|\to\infty\).
Each finite factor is nonzero: \(u_j\) is an algebraic integer, whereas a zero of \(\cos(2\pi x)\) requires the nonintegral rational number \(x\in1/4+(1/2)\mathbb Z\).
This uses the retained correction to the source's stated zero set.

There is an explicit tail estimate, but it retains further input dependence.
Put

\[
 \sigma=\max\{\max_{|\beta|<1}|\beta|,
                      \max_{|\beta|>1}|\beta|^{-1}\}<1,
\]

and choose \(J\ge0\) with \(d\sigma^{J+1}\le1/(4\pi)\).
For \(|x|\le1/2\), \(\cos x\ge e^{-x^2}\): integrate \(\tan x\le2x\), which follows from \(\sin x\le x\) and \(\cos x\ge1-x^2/2\).
The positive and negative tails in (10) are bounded using \(|u_j|\le s\sigma^j\) and \(|v_{-j}|\le(d-s)\sigma^j\).
Since \(s^2+(d-s)^2\le d^2\),

\[
 c(P)\ge
 \left(\prod_{j=-J}^{J}|\cos(2\pi u_j)|\right)
 \exp\left[-\frac{4\pi^2d^2\sigma^{2(J+1)}}{1-\sigma^2}\right].
                                                               \tag{11}
\]

For negative indices the finite factors may be expressed using \(u_j\) because the integral trace identifies their cosines with those of \(v_j\).
Formula (11) makes the archimedean separation from the unit circle and the finite cosine factors visible.
The proof establishes their positivity, not an input-uniform lower bound for the finite product.
Nor does (10) or (11) itself estimate the high-mass null set's neighborhood volume in (4).
The source's passage from Fourier nondecay to pure singularity, and then to a compact null set, is qualitative.

Consequently the retained trace construction does not currently discharge (9).
This is a boundary of the checked argument, not a theorem that such a quantitative deduction is impossible.
No new search or additional article was needed: the decisive missing item is a uniform relation between that Fourier information and the specific concentration cost \(\kappa/N\).

### Finite arithmetic interface

If the fibers of the length-N binary sum have integer sizes \(f_N(x)\), put \(U_N=\prod_x f_N(x)^{f_N(x)}\), as in L G0092.
Then \(H_N=N\log2-2^{-N}\log U_N\).
Given a separately certified rational lower bound \(q_0=a_0/b_0\le M(P)\), where \(a_0,b_0\) are positive integers, the condition

\[
 U_N a_0^{N2^N}>(2b_0)^{N2^N}                            \tag{12}
\]

certifies a positive finite deficit, of size at least \(N\log q_0-H_N\).
This exact integer test does not provide a uniform saving or bound its first time.
It is included only to connect (5) to an actual finite certificate, not as the new quantitative conclusion.
