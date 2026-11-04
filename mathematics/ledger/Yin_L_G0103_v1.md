---
author: Yin
---

# Algebraic multipliers of the trace witness and an arithmetic cap

The current complete mathematical proof is retained in [C298](../claims/Yin_C_G0298_v1.md#argument).
The original mathematical text below remains the fixed old input, with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded continuation of G0001 by the assigned AI ms25_source for Yin.
The coordinator contributed the integer-recurrence sup-norm cap; the assigned agent supplied the multiplier interface, its full scope and the circle-norm variant for all integral annihilating multiples.
No new source, computation or novelty claim is involved.

<a id="algebraic-trace-multiplier"></a>
## The multiplier domain and its exact invariance

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
The same convergent-product argument used in [L G0102](Yin_L_G0102_v1.md#trace-frequencies-and-finite-prefixes) therefore proves \(0<c_P(\theta)\le1\).

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
## Rate spacing is independent of a fixed nonzero multiplier

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
## A nonzero integer defect uniformly caps every multiplier

Fix any nonzero polynomial \(R\in\mathbb Z[t]\) divisible by \(P\) in \(\mathbb Z[t]\).
Denote
\[
 A_R=\sum_i|R_i|,\qquad
 Q_R=\max_{|z|=1}|R(z)|.
\]
Both are positive.
Moreover \(A_R\ge3\): an integral polynomial with coefficient length one is a monomial, and one with length two is either a monomial or a binomial with nonzero roots of unity.
Neither can vanish at the present nonzero nontorsion \(\alpha\).

For each \(j\in\mathbb Z\), choose a nearest integer \(n_j\) to \(2u_j(\theta)\), and put
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
## What multiplier optimization can and cannot supply

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

The separately reviewed endpoint comparison in [L G0101](Yin_L_G0101_v1.md#wiener-endpoint-strict-correction) therefore imposes the strengthened necessary condition
\[
 g(c_{\rm opt}(P))/L_{\rm eff}\le m-E(m).                \tag{14}
\]
The degree-uniform lower control of the optimized amplitude needed to contradict this inequality is still unproved.
In particular, the explicit upper cap is not a positive lower bound for \(m-h_1\).
It rules out the tempting assertion that integral multiplier optimization can make the trace product arbitrarily close to one at a fixed input, and makes the coefficient/circle-norm cost of that obstruction explicit.

All arguments above exclude unit-circle conjugates.
The negative trace-error tail in (8) is precisely where that assumption is used; it cannot be extended by discarding the central trace.
Fixed and moving multiplier issues on that branch are a separate investigation, not a consequence of (7) or (12).



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0029_v1.md#contribution-and-review-scope), with its original inspected scope and relationship.
