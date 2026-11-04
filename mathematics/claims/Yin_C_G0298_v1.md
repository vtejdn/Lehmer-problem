---
author: Yin
---

# Full-integer trace multipliers, uniform limiting spacing and recurrence caps

This retains the complete original2026-10-07 [L103 proof](../ledger/Yin_L_G0103_v1.md).
The assigned ms25_source agent supplied the multiplier and circle-norm arguments; the coordinator supplied the integer-recurrence sup-norm obstruction.
The complete old checks remain at their sufficient [R29 home](../audits/reviews/Yin_R_G0029_v1.md#contribution-and-review-scope).
No source, computation or Task is newly executed.

## Statement

Let alpha be an algebraic unit, K=Q(alpha),P its monic irreducible polynomial,with no unit-circle conjugate,and m=log M(P)>0.
For every fixed theta in O_K minus{0},including multipliers outside Z[alpha],define stable and expanding traces u_j(theta),v_j(theta) at every integer j,with both complex members.
The bilateral absolute cosine product c_P(theta) in the complete proof satisfies

    0<c_P(theta)<=1,
    c_P(-theta)=c_P(theta),
    c_P(alpha^k theta)=c_P(theta) for every integer k.

No invariance under arbitrary integer multipliers or unrelated units is asserted.
With tau the fastest stable modulus and rho the slowest,

    Lstar=floor(log4/(-log tau))+1,
    Leff=min(ceil(log4/(-log rho)),Lstar),

the actual Gaussian/smoothing argument gives m-h1>=g(c_P(theta))/Leff.
The denominator is independent of the fixed nonzero theta.
Its explicit finite t0 and smoothing boundary B_(eta,theta) may depend on theta.
No multiplier moving arbitrarily with N is inserted into that fixed-multiplier limit.

For every nonzero R in Z[t] divisible by P in Z[t],put A_R=sum abs(R_i)>=3 and Q_R=max_(abs(z)=1)abs(R(z)).
Nearest-integer errors e_j=2u_j(theta)-n_j have exponentially decaying tails,belong to l2(Z),and

    z=R(S)e=-R(S)n is a nonzero finite-support integer sequence,
    norm(e)_2²>=Q_R^(-2),
    c_P(theta)<=min(cos(pi/A_R),exp(-pi²/(2Q_R²)))<1.

Here S is the bilateral shift.
R may contain unit-circle factors: finite circle zeros give no l2 shift kernel.
Hyperbolicity is needed for P and the decaying errors.
No Mahler-preserving property of R/P is required.

For c_opt(P)=sup_(theta in O_K minus{0})c_P(theta),with no attainment assertion,

    0<c_P(1)<=c_opt(P)<=min(cos(pi/A_R),exp(-pi²/(2Q_R²)))<1,
    m-h1>=g(c_opt(P))/Leff,
    g(c_opt(P))/Leff<=m-E(m).

E(m) is the actual endpoint comparison.
These uniform upper caps do not provide the degree-uniform lower amplitude needed to contradict the small-m deficit.
All conclusions exclude unit-circle conjugates; their negative trace-error tail cannot be restored by discarding central coordinates.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:12 |
| status | open |
| reason | Complete original full-integer multiplier, finite-offset/rate and arbitrary annihilator recurrence-cap proof retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire nonzero O_K multiplier domain and exact sign/power invariance, uniform limiting spacing with nonuniform finite boundaries, every-integral-annihilator coefficient/circle caps and optimized supremum/E(m) interface with all hyperbolic limits. |
| argument | [Complete argument](#argument) | Full original1–14: trace integrality and product convergence/reindexing, every fastest weight and both offset conditions, actual finite Gaussian/smoothing bound and ordered limits, nonzero rounded integer defect, bilateral Fourier injectivity and both cap constants, exact supremum quantifiers. |
| dependency | [Complete Fourier/smoothing theorem](Yin_C_G0297_v1.md#argument) | Exact finite-prefix trace witness, Gaussian cross-term estimate, fixed-noise entropy boundary and fastest/slowest spacing methods, with the explicitly recomputed theta covector and offsets. |
| dependency | [Actual endpoint comparison](Yin_C_G0296_v1.md#wiener-endpoint-strict-correction) | Full fixed-input E(m)>D(m) comparison only, used as an accepted premise rather than a new whole audit here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:17 |
| status | proved |
| reason | Adopt the complete original full-integer multiplier theorem and both arbitrary-integral-annihilator recurrence caps after actual whole self-review, preserving exact power invariance, nonuniform finite offsets, uniform limiting denominator, nonzero integer defect and optimized-supremum quantifiers; an upper cap is not the missing amplitude lower bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire nonzero O_K multiplier domain and exact sign/power invariance, uniform limiting spacing with nonuniform finite boundaries, every-integral-annihilator coefficient/circle caps and optimized supremum/E(m) interface with all hyperbolic limits. |
| argument | [Argument](#argument) | Full original1–14: trace integrality and product convergence/reindexing, every fastest weight and both offset conditions, actual finite Gaussian/smoothing bound and ordered limits, nonzero rounded integer defect, bilateral Fourier injectivity and both cap constants, exact supremum quantifiers. |
| dependency | [Dependency](Yin_C_G0297_v1.md#argument) | Exact finite-prefix trace witness, Gaussian cross-term estimate, fixed-noise entropy boundary and fastest/slowest spacing methods, with the explicitly recomputed theta covector and offsets. |
| dependency | [Dependency](Yin_C_G0296_v1.md#wiener-endpoint-strict-correction) | Full fixed-input E(m)>D(m) comparison only, used as an accepted premise rather than a new whole audit here. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-multiplier-cap-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire nonzero O_K multiplier domain and exact sign/power invariance, uniform limiting spacing with nonuniform finite boundaries, every-integral-annihilator coefficient/circle caps and optimized supremum/E(m) interface with all hyperbolic limits. |
| argument | [Argument](#argument) | Full original1–14: trace integrality and product convergence/reindexing, every fastest weight and both offset conditions, actual finite Gaussian/smoothing bound and ordered limits, nonzero rounded integer defect, bilateral Fourier injectivity and both cap constants, exact supremum quantifiers. |
| dependency | [Dependency](Yin_C_G0297_v1.md#argument) | Exact finite-prefix trace witness, Gaussian cross-term estimate, fixed-noise entropy boundary and fastest/slowest spacing methods, with the explicitly recomputed theta covector and offsets. |
| dependency | [Dependency](Yin_C_G0296_v1.md#wiener-endpoint-strict-correction) | Full fixed-input E(m)>D(m) comparison only, used as an accepted premise rather than a new whole audit here. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-multiplier-cap-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0548_v1.md#f-g299) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="algebraic-trace-multiplier"></a>
### The multiplier domain and its exact invariance

Let \(\alpha\) be an algebraic unit, \(K=\mathbb Q(\alpha)\), and \(P\in\mathbb Z[t]\) its monic irreducible polynomial.
Assume that \(P\) has no unit-circle root.
Put \(m=\log M(P)>0\).
Write \(\mathcal O_K\) for the full ring of algebraic integers in \(K\).
Fix any \(\theta\in\mathcal O_K\setminus\{0\}\).
This scope includes \(\theta\in\mathbb Z[\alpha]\) but is not silently identified with that smaller order.

For every \(j\in\mathbb Z\), let
\[
 u_j(\theta)=\sum_{|\sigma(\alpha)|<1}\sigma(\theta\alpha^j),
 \qquad
 v_j(\theta)=\sum_{|\sigma(\alpha)|>1}\sigma(\theta\alpha^j),
\]
where both members of each complex pair are included.
These sums are real.
Since \(\alpha\) is a unit, \(\theta\alpha^j\) is integral and
\[
 u_j(\theta)+v_j(\theta)
      =\operatorname{Tr}_{K/\mathbb Q}(\theta\alpha^j)\in\mathbb Z.
\]
Define
\[
 c_P(\theta)=
   \prod_{j=-\infty}^{-1}|\cos(2\pi v_j(\theta))|
   \prod_{j=0}^{\infty}|\cos(2\pi u_j(\theta))|.           \tag{1}
\]

Every finite factor is nonzero: \(u_j(\theta)\) is an algebraic integer, whereas a zero of \(\cos(2\pi x)\) requires a nonintegral rational \(x\in1/4+(1/2)\mathbb Z\).
The two tails tend to zero exponentially before the cosine is applied.
The same convergent-product argument used in [C297](Yin_C_G0297_v1.md#trace-frequencies-and-finite-prefixes) therefore proves \(0<c_P(\theta)\le1\).

The trace identity allows every negative factor to be written using \(u_j(\theta)\).
Reindexing the absolutely convergent sum of negative logarithms consequently gives
\[
 c_P(-\theta)=c_P(\theta),\qquad
 c_P(\alpha^k\theta)=c_P(\theta)\quad(k\in\mathbb Z).       \tag{2}
\]
The latter follows also from \(u_j(\alpha^k\theta)=u_{j+k}(\theta)\).
Increasing a multiplier by powers of \(\alpha\) is thus not an optimization of (1).
No analogous invariance under arbitrary nonzero integers or other units is asserted.

<a id="multiplier-independent-asymptotic-spacing"></a>
### Rate spacing is independent of a fixed nonzero multiplier

Use the stable real embedding space \(\mathbb R^r\times\mathbb C^q\cong\mathbb R^s\) and its normal multiplication matrix \(A\), as in L G0102.
Put
\[
 \zeta_{\theta,0}
  =\bigl(\sigma(\theta)_{\rm real};
            (2\operatorname{Re}\sigma(\theta),
             -2\operatorname{Im}\sigma(\theta))_{\rm complex}\bigr),
 \qquad
 \zeta_{\theta,t}=A^{-\mathsf Tt}\zeta_{\theta,0}.
\]
The fair-sign finite law \(\mu_N\) then satisfies
\[
 |\widehat{\mu_N}(\zeta_{\theta,t})|
  =\prod_{j=0}^{N-1}|\cos(2\pi u_{j-t}(\theta))|
  \ge c_P(\theta) \qquad(N\ge1,\ t\ge0).                 \tag{3}
\]

Let \(\tau=\min_{|\beta|<1}|\beta|\), and fix
\[
 L_*=\left\lfloor\frac{\log4}{-\log\tau}\right\rfloor+1.
                                                               \tag{4}
\]
This number depends only on \(P\).
Every field embedding of nonzero \(\theta\) is nonzero, so the exact squared norm
\[
 \|\zeta_{\theta,t}\|^2
   =\sum_{\rm real}|\sigma(\theta)|^2|\sigma(\alpha)|^{-2t}
      +4\sum_{\rm complex}|\sigma(\theta)|^2
                                 |\sigma(\alpha)|^{-2t}
\]
has a nonzero contribution from every fastest stable root.
Its consecutive-\(L_*\) ratio therefore tends to \(\tau^{-L_*}>4\), independently of the size of those nonzero coefficients.

More explicitly, let \(A_\theta>0\) be the sum of weights \(|\sigma(\theta)|^2\) and \(4|\sigma(\theta)|^2\) at modulus \(\tau\), and \(W_\theta\) the sum at all other stable moduli.
Put \(\kappa_*=\tau^{-2L_*}-16>0\).
If \(W_\theta>0\), let \(\tau_2>\tau\) be the next stable modulus.
Choose \(t_0\ge0\) so that
\[
 16W_\theta(\tau/\tau_2)^{2t_0}\le A_\theta\kappa_*,
 \qquad A_\theta\tau^{-2t_0}\ge1.                        \tag{5}
\]
Omit the first condition when \(W_\theta=0\).
Exactly the squared-norm subtraction in L G0102 shows that the frequencies \(\zeta_{\theta,t_0+jL_*}\) have successive norm ratio at least four and norm at least \(4^j\), for \(j\ge1\).

The Gaussian cross-term bound in L G0102 now applies without change.
Its disjoint noise body does not depend on \(\theta\).
For each \(0<\eta<1\), only its smoothing boundary changes: choose \(B_{\eta,\theta}\ge0\) with
\[
 2\pi a\sqrt{s}\|\zeta_{\theta,0}\|
                 \rho^{B_{\eta,\theta}}\le\sqrt{2\eta},
 \qquad \rho=\max_{|\beta|<1}|\beta|.
\]
Here \(a\) and the entropy boundary constant \(C_P\) are precisely those of L G0102.
Thus the same proof gives
\[
 Nm-H_N\ge
 \left\lfloor
    \frac{(N-B_{\eta,\theta}-t_0)_+}{L_*}
 \right\rfloor
 g((1-\eta)c_P(\theta))-C_P-\log2.
                                                               \tag{6}
\]
First fix \(\theta,\eta\), then let \(N\to\infty\), and finally let \(\eta\downarrow0\).
We obtain
\[
 \boxed{\quad m-h_1\ge g(c_P(\theta))/L_*.\quad}          \tag{7}
\]

The limiting denominator is uniform over nonzero multipliers.
The finite boundaries \(t_0\) and \(B_{\eta,\theta}\) are not asserted uniform, and this proof does not insert a multiplier varying arbitrarily with \(N\) into the fixed-multiplier limit.
The slowest stable spacing from L G0102 is also valid after a finite norm-normalizing offset; thus (7) may use \(L_{\rm eff}=\min\{\lceil\log4/(-\log\rho)\rceil,L_*\}\).

<a id="uniform-multiplier-recurrence-cap"></a>
### A nonzero integer defect uniformly caps every multiplier

Fix any nonzero polynomial \(R\in\mathbb Z[t]\) divisible by \(P\) in \(\mathbb Z[t]\).
Denote
\[
 A_R=\sum_i|R_i|,\qquad
 Q_R=\max_{|z|=1}|R(z)|.
\]
Both are positive.
Moreover \(A_R\ge3\): an integral polynomial with coefficient length one is a monomial, and one with length two is either a monomial or a binomial with nonzero roots of unity.
Neither can vanish at the present nonzero nontorsion \(\alpha\).

For each \(j\in\mathbb Z\), choose a nearest integer
\(n_j\) to \(2u_j(\theta)\), and put
\[
 e_j=2u_j(\theta)-n_j,\qquad |e_j|\le1/2.
\]
In fact equality cannot occur, by the nonzero-cosine argument.
For large positive \(j\), \(e_j=2u_j(\theta)\); for large negative \(j\), trace integrality gives \(e_j=-2v_j(\theta)\).
Thus \(e\in\ell^2(\mathbb Z)\) and its tails decay exponentially.
Also
\[
 c_P(\theta)=\prod_{j\in\mathbb Z}\cos(\pi e_j).           \tag{8}
\]

Let \(S\) be the bilateral shift, \((Sx)_j=x_{j+1}\).
The trace sequence obeys \(P(S)u=0\), hence \(R(S)u=0\).
It follows that
\[
 z:=R(S)e=-R(S)n\in\mathbb Z^{\mathbb Z}
                                  \cap\ell^2(\mathbb Z).
                                                               \tag{9}
\]
In particular \(z\) has finite support.

We have \(e\ne0\).
Otherwise \(2u_j(\theta)\) would be integer for every \(j\) and, since it tends to zero, would vanish for every sufficiently large positive \(j\).
Consecutive stable-trace equalities and the Vandermonde matrix on the distinct stable conjugates would force every stable \(\sigma(\theta)\) to be zero.
This contradicts \(\theta\ne0\).

A nonzero polynomial of the bilateral shift has no kernel on \(\ell^2(\mathbb Z)\).
Indeed, the Fourier isometry, obtained by completing finite Parseval sums, turns \(R(S)\) into multiplication by \(R(e^{-2\pi it})\) on \(L^2(\mathbb T)\).
This polynomial vanishes at at most finitely many circle points, a set of measure zero.
Therefore (9) is a nonzero integer sequence and
\[
 \|z\|_2\ge1,\qquad
 \|z\|_2\le Q_R\|e\|_2,\qquad
 \|e\|_2^2\ge Q_R^{-2}.                                 \tag{10}
\]
This argument permits unit-circle factors in \(R\).
They give no \(\ell^2\) kernel; hyperbolicity is required for \(P\) and the decaying error tails, not for every annihilating multiple.

For \(|x|<\pi/2\), integration of \(\tan x\ge x\) gives \(\log\cos x\le-x^2/2\).
From (8)--(10),
\[
 c_P(\theta)\le\exp[-\pi^2/(2Q_R^2)].                    \tag{11}
\]

The coordinator's sup-norm version gives a complementary cap.
If \(|e_j|<1/A_R\) for every \(j\), each integer entry of \(R(S)e\) would have absolute value strictly less than one, hence would vanish.
This contradicts (9)--(10).
Thus some \(|e_j|\ge1/A_R\); its single factor in (8) yields
\[
 \boxed{\quad
 c_P(\theta)\le
 \min\{\cos(\pi/A_R),\ \exp[-\pi^2/(2Q_R^2)]\}<1.
 \quad}                                                \tag{12}
\]

This is a bound uniform over all nonzero algebraic integer multipliers.
It uses the actual integer recurrence, not merely bounded Fourier coefficients.
Taking \(R=P\) is always possible.
Every retained short integer completion of \(P\) gives another valid cap, including a completion with cyclotomic factors.
No Mahler-preservation hypothesis on the multiplier polynomial \(R/P\) is needed for (12).

<a id="optimized-trace-witness-boundary"></a>
### What multiplier optimization can and cannot supply

Define
\[
 c_{\rm opt}(P)=
   \sup_{\theta\in\mathcal O_K\setminus\{0\}}c_P(\theta).
\]
This is a supremum, with no claim of attainment.
By (1), (7) and (12), for every admissible \(R\),
\[
 0<c_P(1)\le c_{\rm opt}(P)
 \le\min\{\cos(\pi/A_R),e^{-\pi^2/(2Q_R^2)}\}<1,
 \qquad
 m-h_1\ge g(c_{\rm opt}(P))/L_{\rm eff}.                 \tag{13}
\]
The last passage is valid because the left side is fixed, the denominator is independent of \(\theta\), and \(g\) is continuous and increasing.
It does not claim uniformity of the finite bound (6).

The separately reviewed endpoint comparison in [C296](Yin_C_G0296_v1.md#wiener-endpoint-strict-correction) therefore imposes the strengthened necessary condition
\[
 g(c_{\rm opt}(P))/L_{\rm eff}\le m-E(m).                \tag{14}
\]
The degree-uniform lower control of the optimized amplitude needed to contradict this inequality is still unproved.
In particular, the explicit upper cap is not a positive lower bound for \(m-h_1\).
It rules out the tempting assertion that integral multiplier optimization can make the trace product arbitrarily close to one at a fixed input, and makes the coefficient/circle-norm cost of that obstruction explicit.

All arguments above exclude unit-circle conjugates.
The negative trace-error tail in (8) is precisely where that assumption is used; it cannot be extended by discarding the central trace.
Fixed and moving multiplier issues on that branch are a separate investigation, not a consequence of (7) or (12).
