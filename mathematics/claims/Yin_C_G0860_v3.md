---
author: Yin
---
# Exact fixed-center trace ranks and the paid return to the original polynomial

This project deduction strengthens the approximation-rank part of [C860 v2](Yin_C_G0860_v2.md#statement).
The complete original A--E conclusions remain at [v1](Yin_C_G0860_v1.md#statement), with their [selected assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04).
The complete M1--M9 conclusions remain at [v2](Yin_C_G0860_v2.md#statement), with their [selected assessment](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04).
Those fixed statements, proofs and reviews are preserved rather than copied here, and their acceptance is not transferred to the new statements.
The substantive change is an exact asymptotic rank theorem for the specified fixed binomial truncants, its original-input specialization, a complete paid comparison for supplied rational centers, and preservation of original poles by coherent rational centers of degree below the original degree.

The weighted-mask-return agent developed this argument for Yin, and the coordinating agent checked the development as a contributor.
Neither check is an independent review.
This new version has no selected assessment, no adopted review and no numerical proof input.
No rolling Draft is a mathematical premise.

## Statement

**A. General fixed-binomial-trace rank.**
Let \(M\ge1\), let \(S_i,Z_i\in\mathbb C(x)\) be regular at zero with \(S_i(0)=1\), \(Z_i(0)=0\), and put
\[
 c_v=\binom{1/2}{v},\qquad
 \mathcal P_t(z)=\sum_{v=0}^{t}c_vz^v,\qquad
 \mathcal F_t(x)=\sum_{i=1}^{M}S_i(x)\mathcal P_t(Z_i(x)).
\]
The collection of rational functions is fixed independently of the nonnegative integer \(t\).
Let \(\rho_t\) be the rank over \(\mathbb C\) of the infinite formal shifted Hankel matrix of \(\mathcal F_t=\sum_{n\ge0}a_{t,n}x^n\), whose \((i,j)\)-entry is \(a_{t,i+j+1}\), \(i,j\ge0\).
For every point of the projective line define
\[
 m_\beta=\max_{1\le i\le M}\max\{-\operatorname{ord}_\beta Z_i,0\},
 \qquad K_{\rm pole}=\sum_{\beta\in\mathbb P^1(\mathbb C)}m_\beta.
\]
The zero function has order infinity; only finitely many summands are nonzero.
Then
\[
                              \rho_t=K_{\rm pole}t+O(1).
\]
At every point with \(m_\beta>0\), the actual pole order of \(\mathcal F_t\) is \(m_\beta t+O(1)\).
These conclusions hold for all sufficiently large integers \(t\), rather than merely on a subsequence.
All constants may depend on the fixed rational functions.
Infinity is included and accounts for polynomial growth.

**B. Original uncentered masks.**
Let \(P\in\mathbb Z[x]\) be monic, irreducible, reciprocal and noncyclotomic of degree \(d\ge2\), with constant term one, and assume every positive power of a root has degree \(d\).
Use all original conjugates \(\alpha_i\), the total measure \(m=m(P)>0\), \(H=\max_i|\alpha_i|\), and \(P_n(x)=\prod_i(1-\alpha_i^nx)\).
For an odd prime \(q\), put \(K=\mathbb Q(\zeta_q)\), \(U=P_2\), \(V=P_4\).
Fix a nonempty mask \(I\subseteq\mathbb Z/q\mathbb Z\), its full Galois orbit \(O\), and
\[
 D_J=\prod_{j\in J}U(\zeta_q^jx),\quad
 N_J=\prod_{j\in J}V(\zeta_q^jx),\quad
 S=\bigcup_{J\in O}J,\quad b=d|S|.
\]
For the uncentered rational truncation
\[
                  \sum_{J\in O}\mathcal P_t(N_J/D_J-1)
\]
the exact shifted Hankel rank is \(bt+O(1)\).
Thus trace cancellation does not improve the asymptotic union-denominator slope of these particular truncations.
No claim is made about the best rank among all rational approximations at the same two-adic precision.

**C. Supplied rational centers, precision and return.**
For the same original input and mask \(I\), write \(D=D_I\), \(N=N_I\), \(n=d|I|\).
Suppose \(A,B\in\mathcal O_K[x]\), \(A(0)=0\), \(B(0)=1\), \(\deg A,\deg B\le r\), and set \(C=B+2A\).
Assume, at every place above two through the following polynomial divisibility, that
\[
 NB^2-DC^2=2^\lambda E,\qquad E\in\mathcal O_K[x],
 \qquad\lambda\ge3,\quad a=\lambda-2.
\]
Define \(T_t\) by (R4) in the complete argument, equivalently
\[
 T_t=\frac CB\,\mathcal P_t\!\left(\frac{NB^2}{DC^2}-1\right),
 \qquad
 F_t=\frac1u\sum_{\sigma\in\operatorname{Gal}(K/\mathbb Q)}\sigma(T_t),
 \quad u=|\operatorname{Stab}(I)|,\quad e=v_2(u).
\]
Let \(G_J=(N_J/D_J)^{1/2}\) have constant coefficient one and \(f=\sum_{J\in O}G_J\).
Then \(f\in\mathbb Z[[x]]\) is nonrational, and
\[
 f-F_t\in2^{a(t+1)+1-e}\mathbb Z_2[[x]],\qquad
 \rho_t\le t\bigl(b+2(q-1)r\bigr)\quad(t\ge1).
\]
The approximants have integral two-adic Taylor coefficients whenever \(a(t+1)+1-e\ge0\).
Their exact rank satisfies Part A with
\[
 Z_\sigma=\sigma\!\left(\frac{NB^2}{DC^2}-1\right),\qquad
 0<K_{\rm pole}\le b+2(q-1)r.
\]
For the shifted leading Hankel determinants \(\mathcal D_h\) of \(f\), put
\[
 r_s=\min\{\rho_t:t\ge1,\ a(t+1)+1-e\ge s\},\qquad s\ge1.
\]
Then
\[
 v_2(\mathcal D_h)\ge\sum_{s\ge1}\max(h-r_s,0),
 \qquad
 \log H\ge\frac{a\log2}{8K_{\rm pole}},\qquad
 m\ge\frac{a\log2}{8K_{\rm pole}}.
\]
Every limit in matrix size is taken with the original input and center fixed.
Uniform gap coverage would still require a uniform favorable ratio \(a/K_{\rm pole}\) on a covering class of genuinely near-one inputs; no such supply is asserted.

**D. Coherent centers below the original degree.**
In Part B suppose \(A_0,B_0\in\mathbb Q[x]\), \(A_0(0)=0\), \(B_0(0)=1\), \(C_0=B_0+2A_0\), and
\[
 \max(\deg B_0,\deg C_0)<d,\qquad
 S_J=\prod_{j\in J}\frac{C_0(\zeta_q^jx)}{B_0(\zeta_q^jx)}.
\]
For \(\sum_{J\in O}S_J\mathcal P_t(N_J/(D_JS_J^2)-1)\), Part A gives \(K_{\rm pole}\ge b\), because all original \(D_J\) poles persist.
This is a rank assertion without an automatic arithmetic divisibility premise.
If integral coherent centers also satisfy Part C's supplied residual-depth premise, its comparison applies; an automatic depth-three instance has \(a=1\), and its elementary-disk certificate is at most \((\log2)/(8b)\).
The theorem excludes neither higher residual precision, larger centers that move original poles, centers changing with \(t\), different rational approximants nor a different complex quadratic estimate.
It does not resolve the unrestricted Lehmer gap.

## Exact dependencies and source scope

| Role | Fixed input and exact use |
| --- | --- |
| Earlier family conclusions | [C860 v1 A--E](Yin_C_G0860_v1.md#statement), with its [selected assessment](Yin_C_G0860_v1.md#decision-whole-independent-review-2026-11-04), and [C860 v2 M1--M9](Yin_C_G0860_v2.md#statement), with its [selected assessment](Yin_C_G0860_v2.md#decision-whole-independent-review-2026-11-04), remain unchanged at their original scopes. The new proof specifically uses v1's scaled-binomial valuation and v2's [union denominator](Yin_C_G0860_v2.md#overlap-denominator). |
| Original trace and determinant inputs | [C858](Yin_C_G0858_v1.md#all-place-hankel-budget), at its [selected assessment](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04): power-stable branch noncollision and private zeros, nonrationality of the original normalized orbit sum, the finite rank-to-elementary-divisor argument, and infinitely many nonzero shifted leading determinants at its retained BNZ22 source scope. Its [disk comparison](Yin_C_G0858_v1.md#cauchy-radius-cost) supplies the unchanged radius \(H^{-4}\), Cauchy exponent and order of limits. |
| Formal rank convention | [BR10-U002](../audits/literature/BR10/Yin_U002.md#formal-hankel-rank) supplies the formal matrix convention. [Par88-U001](../audits/literature/Par88/Yin_U001.md#proof-mechanism-and-minimality) supplies the reduced rational-pole/minimal-recurrence identity at its retained Theorem 3.11 statement and proof-inspection scope, applied after the stated coefficient shift. No bounded infinite-operator assertion is used. |
| Noetherian input | [Stacks Tag 00FN, Lemma 10.31.1](https://stacks.math.columbia.edu/tag/00FN), in the [existing original HTML](../literature/pdf/The26b/00FM--20261101.html#00FN): finite-type extension and arbitrary localization preserve Noetherianity. The exact statement and its displayed proof were read for this argument; no whole-chapter or recursive source-proof review is claimed. This is an accepted standard input, not a new project theorem or novelty claim. |

The degree and center hypotheses in Part C are supplied data, not consequences imported from a rolling draft or a one-place Artin--Schreier relation.
Part A is proved below for the complete general rational-function domain stated there.
Parts B--D retain the original polynomial, original conjugates, total measure, Galois costs and actual finite-place conditions.

<a id="argument"></a>
## Complete argument

<a id="fixed-center-exact-slope"></a>
### Exact asymptotic rank of the fixed-center trace truncations

We first determine the rank slope for the complete rational-function domain of Part A and then apply it to the original polynomial.
For the original uncentered orbit sum it gives
\[
                              \rho_t=bt+O(1),               \tag{S1}
\]
where \(b=d|\bigcup_{J\in O}J|\) is precisely the union cost in C860 v2.
Thus cancellations after this particular trace can remove only a bounded number of pole orders at each fixed input, even when leading power sums vanish for infinitely many truncation indices.
This does not identify the best rank among all rational approximations at the same precision.

More generally, keep any one fixed collection of the rational centers in (R3)--(R4), independent of \(t\).
Write its full trace as
\[
 \mathcal F_t=\sum_{i=1}^{M}S_i(x)\mathcal P_t(Z_i(x)),\qquad
 \mathcal P_t(z)=\sum_{v=0}^{t}c_vz^v,\quad
 c_v=\binom{1/2}{v},
                                                               \tag{S2}
\]
where \(S_i(0)=1\), \(Z_i(0)=0\), and \(S_i,Z_i\in\mathbb C(x)\).
For the full Galois trace one has \(M=q-1\), \(S_i=\sigma(C/B)\), and \(Z_i=\sigma(NB^2/(DC^2)-1)\).
Dividing by the fixed stabilizer order changes no rank or pole order.
For \(\beta\in\mathbb P^1(\mathbb C)\), define
\[
 m_\beta=\max_i\max\{-\operatorname{ord}_\beta Z_i,0\},
 \qquad K_{\rm pole}=\sum_{\beta\in\mathbb P^1(\mathbb C)}m_\beta.
                                                               \tag{S3}
\]
The order of the identically zero rational function is infinity, so such a term contributes no pole.
Only finitely many summands in (S3) are nonzero.
Then the exact shifted Hankel rank satisfies
\[
                         \rho_t=K_{\rm pole}\,t+O(1)
                         \quad(t\longrightarrow\infty).      \tag{S4}
\]
The constants depend on the fixed input and centers; no uniform bound for those constants is asserted.
The pole at infinity counts polynomial growth and is included in (S3).

#### A finite-order cancellation argument valid at every integer index

Fix a point \(\beta\) with \(m=m_\beta>0\), choose local coordinate \(z=x-\beta\), or \(z=1/x\) at infinity, and first sum only over
\[
                         E=\{i:-\operatorname{ord}_\beta Z_i=m\}.
\]
For \(i\in E\), write
\[
 Z_i=z^{-m}a_i u_i(z),\qquad
 S_i=z^{s_i}v_i(z),\qquad
 a_i\ne0,\quad u_i(0)=1,\quad v_i(0)\ne0,
 \qquad s_*=\min_{i\in E}s_i.
\]
The power series \(u_i,v_i\) are convergent local rational expansions, although only their formal coefficients will be used.
Put
\[
 \Psi_t(z)=z^{mt-s_*}\sum_{i\in E}S_i\mathcal P_t(Z_i).
\]
This is regular at \(z=0\).
For \(k\ge0\), define the rational function
\[
 R_k(T)=\prod_{\ell=0}^{k-1}
                   \frac{T-\ell}{3/2-T+\ell},\qquad R_0=1.   \tag{S5}
\]
For every nonnegative integer \(t\), its denominators are nonzero, and
\[
 R_k(t)=
 \begin{cases}
 c_{t-k}/c_t,&0\le k\le t,\\
 0,&k>t.
 \end{cases}                                                \tag{S6}
\]
The second case is the zero factor \(T-t\) in the numerator; no coefficient with a negative binomial index is being used.
For fixed \(j\ge0\), the coefficient of \(z^j\) in \(\Psi_t/c_t\) is the specialization \(H_j(t,(a_i^t)_{i\in E})\), where
\[
 H_j(T,(X_i))=
 \sum_{i\in E}X_i
 \sum_{\substack{k\ge0\\j-(s_i-s_*)-mk\ge0}}
 R_k(T)a_i^{-k}
 [z^{j-(s_i-s_*)-mk}]
            \bigl(v_i(z)u_i(z)^{\,T-k}\bigr).                \tag{S7}
\]
For each fixed coefficient index, the formal binomial expansion of \(u_i^{T-k}\) makes that coefficient a polynomial in \(T\).
Each inner sum is finite, so every \(H_j\) belongs to the single ring
\[
 \mathscr R=
 \mathbb C[T,(X_i)_{i\in E}]
       [(3/2-T+\ell)^{-1}:\ell=0,1,2,\ldots].                \tag{S8}
\]
This ring is Noetherian, even though the multiplicative set being inverted is infinite.
The precise standard input is [Stacks Tag 00FN, Lemma 10.31.1](https://stacks.math.columbia.edu/tag/00FN), finite-type extension and arbitrary localization of a Noetherian ring; its statement and displayed proof were checked in the [existing original HTML](../literature/pdf/The26b/00FM--20261101.html#00FN).
Only this elementary Noetherian input is used; no whole-chapter review is claimed.

Consequently the ascending ideals \((H_0,\ldots,H_J)\) stabilize at some finite index \(J_\beta\).
If the first \(J_\beta+1\) coefficients of \(\Psi_t\) vanished at an integer \(t\), the evaluation homomorphism
\[
            T\longmapsto t,\qquad X_i\longmapsto a_i^t
\]
would annihilate every \(H_j\).
It is defined on all of (S8), since none of its inverted half-integer factors vanishes at an integer.
Equation (S7), including the zero rule in (S6), would then make \(\Psi_t\) the zero formal series.
This would say that the rational function \(\sum_{i\in E}S_i\mathcal P_t(Z_i)\) vanishes identically.
Its value at the original basepoint \(x=0\) is \(|E|\), a nonzero complex number, contradicting that conclusion.
The basepoint argument applies also when the local coordinate was chosen at infinity.
It follows that
\[
             0\le\operatorname{ord}_{z=0}\Psi_t\le J_\beta
                         \quad\hbox{for every integer }t\ge0.
                                                               \tag{S9}
\]
The maximal-pole group therefore has actual pole order \(mt+O(1)\).

Every omitted index has pole order of \(Z_i\) at most \(m-1\), or has \(Z_i\) regular there.
Its contribution has pole order at most \((m-1)t+C_\beta\), for a fixed constant determined by the prefactors \(S_i\).
For all sufficiently large \(t\), these terms cannot cancel the pole of order \(mt+O(1)\) just established.
Hence the complete sum (S2) has pole order \(m_\beta t+O(1)\) at every point with \(m_\beta>0\).
Where all \(Z_i\) are regular, only the fixed poles of the \(S_i\) can remain, of orders bounded independently of \(t\).
There are only finitely many relevant points, and the exact pole-plus-polynomial rank identity (R8) now proves (S4).

#### Apply the slope to the original units and rational centers

In the uncentered construction, \(S_J=1\) and \(Z_J=N_J/D_J-1\).
Every zero of \(D_J\) is a simple pole of \(Z_J\), by the original power-stable branch noncollision, and \(Z_J\) has no pole at infinity.
The union of these poles consists of the \(b\) original rotated \(P_2\) roots, giving (S1).
In particular cancellation of leading Laurent power sums does not conceal a smaller asymptotic rank slope for these fixed uncentered truncants.

There is an additional restriction for coherent centers formed from rational polynomials of degree below the original degree.
Suppose \(A_0,B_0\in\mathbb Q[x]\), \(A_0(0)=0\), \(B_0(0)=1\), \(C_0=B_0+2A_0\), and
\[
 \max\{\deg B_0,\deg C_0\}<d,\qquad
 S_J(x)=\prod_{j\in J}\frac{C_0(\zeta^jx)}{B_0(\zeta^jx)}.
                                                               \tag{S10}
\]
No zero of \(B_0\) or \(C_0\) is a \(q\)-th-root-of-unity rotation of any original \(P_2\) or \(P_4\) root.
Indeed, if \(\gamma=\zeta^k\alpha^{-a}\), with \(a=2\) or \(4\), were such a zero, then \(\gamma^q=\alpha^{-aq}\) would have degree \(d\), while
\[
 d=[\mathbb Q(\gamma^q):\mathbb Q]
       \le[\mathbb Q(\gamma):\mathbb Q]
       \le\max\{\deg B_0,\deg C_0\}<d,
\]
a contradiction.
Thus every factor of every \(S_J\) is finite and nonzero at all original rotated branch points.
Each recentered residual \(Z_J=N_J/(D_JS_J^2)-1\) retains the original simple \(D_J\) poles, and (S4) gives
\[
                                K_{\rm pole}\ge b.           \tag{S11}
\]
The condition (S10) includes any supplied coherent rational center with degrees at most \(d/2\); the proof here does not assume that such a center exists on every original input.
New center poles can increase the slope, and their cancellation is already measured exactly by (S3), without removing the original contribution (S11).
For a residual of depth \(\lambda\), the disk coefficient of this fixed-center construction is consequently governed by \(a/K_{\rm pole}\), where \(a=\lambda-2\).
An automatic depth-three lift has \(a=1\) and cannot obtain a uniform elementary-disk gain by trace cancellation or by these low-degree coherent centers.
Higher residual precision on the same actual inputs, centers of original degree or larger that move original poles, centers varying with precision, genuinely different rational approximants, and a different complex comparison remain separate possibilities.
This calculation supplies no lower bound for all possible approximation ranks and no resolution of the unrestricted Lehmer contract.

<a id="supplied-center-comparison"></a>
### Full trace and the cost of a supplied rational center

Under Part C's assumptions, write
\[
 NB^2-DC^2=2^\lambda E,\qquad \lambda\ge3,\qquad a=\lambda-2,
 \qquad \deg E\le n+2r.
\]
Here \(E(0)=0\), and \(C(0)=1\).
In the integral Taylor-series ring the normalized radical has the exact expression
\[
 G_I=\frac CB
       \left(1+\frac{2^\lambda E}{DC^2}\right)^{1/2}.
                                                               \tag{R3}
\]
Both sides have constant coefficient one and the same square, which proves the identity without a choice of analytic square-root signs.
Define its rational truncation
\[
 T_t=\frac CB\sum_{v=0}^{t}
         2^{\lambda v}\binom{1/2}{v}
                  \left(\frac E{DC^2}\right)^v,\qquad t\ge1.
                                                               \tag{R4}
\]
The [C860 binomial valuation](../claims/Yin_C_G0860_v1.md#statement) gives
\[
 G_I-T_t\in2^{a(t+1)+1}\mathcal O_K[[x]].                       \tag{R5}
\]
Indeed every omitted index \(v\ge t+1\) has scalar valuation \(av+s_2(v)\ge a(t+1)+1\), and all rational factors in (R4) have integral Taylor coefficients.
A common denominator for (R4) is \(BD^tC^{2t-1}\), with constant coefficient one.
Its degree and the degree of the resulting numerator are both at most \(t(n+2r)\).
This bound also holds if the top coefficient of \(C\) cancels; no assertion that \(T_t\) is proper at infinity is needed.

Let \(\Gamma=\operatorname{Gal}(K/\mathbb Q)\), let \(O\) be the original orbit of \(I\), and set \(u=|\operatorname{Stab}_\Gamma(I)|\), \(e=v_2(u)\).
There is no need to choose a lift \(A/B\) invariant under that stabilizer.
Use every conjugate of the chosen lift and set
\[
 F_t=\frac1u\sum_{\sigma\in\Gamma}\sigma(T_t),\qquad
 f=\sum_{J\in O}G_J.
\]
The corresponding full trace of \(G_I\) is exactly \(u f\), so
\[
 f-F_t\in2^{s_t}\mathbb Z_2[[x]],\qquad
                    s_t=a(t+1)+1-e.                         \tag{R6}
\]
This pays the stabilizer division even when \(u\) is even.
Reuse the [C860 union denominator](../claims/Yin_C_G0860_v2.md#overlap-denominator): set \(S=\bigcup_{J\in O}J\), \(Q_D=\prod_{j\in S}U(\zeta^jx)\), and \(b=d|S|\).
The polynomial
\[
 Q_D^t\prod_{\sigma\in\Gamma}
          \sigma(B)\sigma(C)^{\,2t-1}
\]
is an integer common denominator for \(F_t\), with constant coefficient one.
Its degree and the degree of the resulting numerator are both at most
\[
                         t\bigl(b+2(q-1)r\bigr).             \tag{R7}
\]
For the numerator bound, the contribution of one conjugate in (R4) has degree at most \(t(n+2r)\), the quotient \(Q_D^t/\sigma(D)^t\) has degree \(t(b-n)\), and the remaining \(q-2\) center-denominator factors contribute at most \(2t(q-2)r\).
Whenever \(s_t\ge0\), (R6) and the integral coefficients of \(f\) imply that \(F_t\) has integral two-adic Taylor coefficients.
Multiplying by the displayed integral unit denominator shows that its numerator is also two-adically integral, despite the intermediate division by \(u\).
These are the integral approximants needed for the finite elementary-divisor argument; integral rational coefficients at odd primes are not needed there.
No factor in (R7) has been declared minimal, and the original degree, center degrees, full Galois descent and division loss remain visible.

### Exact rational rank and all precision levels

Write the reduced rational function as \(F_t=P_t/Q_t\), with \(\gcd(P_t,Q_t)=1\) and \(Q_t(0)=1\).
For a nonconstant \(F_t\), its shifted formal Hankel rank is exactly
\[
 \rho_t=\max\{\deg P_t,\deg Q_t\}
       =p_t+\sum_\beta\nu_{\beta,t},                         \tag{R8}
\]
where \(\nu_{\beta,t}\) is the actual finite pole order and \(p_t=\max(0,\deg P_t-\deg Q_t)\) is the degree of its polynomial part, with constants contributing zero.
Set \(\rho_t=0\) when \(F_t\) is constant.
This is the reduced rational-pole/minimal-recurrence formula at the retained scope of [Par88-U001](../audits/literature/Par88/Yin_U001.md#proof-mechanism-and-minimality), with the formal convention of [BR10-U002](../audits/literature/BR10/Yin_U002.md#formal-hankel-rank).
The shift uses the coefficients of \((F_t-F_t(0))/x\); the polynomial contribution is essential and cannot be omitted when a center changes behavior at infinity.
For example, a polynomial of degree \(p>0\) contributes rank \(p\), even though it has no finite poles.

Let \(\mathcal D_h\) be the shifted leading Hankel determinants of the same original integral nonrational trace \(f\).
For each integer \(s\ge1\), let
\[
 r_s=\min\{\rho_t:t\ge1,\ s_t\ge s\}.
\]
The rank of each rational-coefficient Hankel matrix is unchanged on extending scalars from \(\mathbb Q\) to either \(\mathbb C\) or \(\mathbb Q_2\), since it is determined by its nonzero finite minors.
The set is nonempty, and the exact all-level comparison of [C858](../claims/Yin_C_G0858_v1.md#all-place-hankel-budget) gives
\[
 v_2(\mathcal D_h)\ge\sum_{s\ge1}\max(h-r_s,0).              \tag{R11}
\]
This comparison uses the actual reduced ranks, not only the unreduced degree (R7).
For example, if for this fixed original input and chosen construction one proves
\[
                       \rho_t\le\kappa t+O(1)
                       \quad(t\longrightarrow\infty),
                       \qquad\kappa>0,                     \tag{R12}
\]
then \(r_s\le(\kappa/a)s+O(1)\), with constants allowed to depend on that input.
Summing (R11) gives quadratic coefficient at least \(a/(2\kappa)\).
The unchanged elementary disk comparison for \(f\), whose branch radius is still \(H^{-4}\), therefore gives
\[
                         \log H\ge\frac{a\log2}{8\kappa}.
                                                               \tag{R13}
\]
The limit in \(h\) is taken for each fixed input before any sequence of polynomials is considered, so the fixed stabilizer loss \(e\) and the \(O(1)\) terms do not affect this coefficient.
A uniform lower bound \(a/\kappa\ge c>0\) for a covering family of genuinely near-one original inputs would contradict their positive total measures tending to zero.
The readily proved bound (R7) supplies only \(\kappa\le b+2(q-1)r\), which is not such a uniform conclusion.

The normalized series in (R3) is integral, and every conjugate has the same property, so the rational orbit sum has integer coefficients.
The private original branch points give the nonrationality and infinitely many nonzero shifted leading determinants by the exact C858 mechanism cited above.
Moreover \(K_{\rm pole}>0\): if every recentered residual had no pole on the projective line, each would be constant and hence zero by its value at the origin.
This would make \(N/D=(C/B)^2\), impossible because \(N/D\) has the original simple private zeros and poles.
Part A supplies (R12) with \(\kappa=K_{\rm pole}\), so (R13) is the stated exact-slope comparison of Part C.
The bound \(m(P)\ge\log H\) gives its total-measure consequence.
For Part D's integral coherent centers put \(B_I=\prod_{j\in I}B_0(\zeta_q^jx)\), \(C_I=\prod_{j\in I}C_0(\zeta_q^jx)\) and \(A_I=(C_I-B_I)/2\).
These are algebraic-integer polynomials with the required constant coefficients because \(C_0-B_0=2A_0\); under the stated residual-depth premise, Part C applies to this supplied center.
The degree restriction in Part D gives (S11), and therefore its depth-three certificate is at most \((\log2)/(8b)\).
No fixed-center conclusion here restricts centers that change with precision, or the minimum rank among unrelated rational approximants.

## Current assessment
