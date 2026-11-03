---
author: Yin
---

# Damped-root identities, coefficient-height bounds and growing-band localization

Date: 2026-10-10T14:17.
Human author: Yin.
Provenance: project deduction.

Context: [G0001](../tasks/Yin_T_G0001_v1.md), presently paused.
The user requested completed drafts to be placed in the material area matching their role.
This is result organization, not renewed exploration or a change to that Task decision.

## Current assessment
[Selected decision](#decision-current-confluent-proof-homes)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:17 |
| status | open |
| reason | Complete historical argument extracted for precise registration; current extraction-interface review and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the explicitly enumerated conclusions and hypotheses. |
| argument | [Argument](#argument) | The selected completed derivations retained below; speculative and computational-history passages are excluded as proof premises. |
| dependency | [Exact radial split](Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) | The original pair-specific damping, the exact log-resultant split and radial bound in the actual minimal-polynomial domain. |
| dependency | [Full mixed resultant](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Nonzero full doubling resultant and its Frobenius floor for a nontorsion algebraic unit. |


### Decision organized-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-10T14:24 |
| status | proved |
| reason | The precisely enumerated completed results have unchanged complete historical arguments and reviews; the fixed extraction finding checks the new statement and actual dependency interfaces. Original conjectures, finite discovery statistics and unchecked source generalizations are excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exactly the enumerated parts with all their separate hypotheses and exclusions. |
| argument | [Argument](#argument) | The complete selected retained derivations, with their explicit supporting inputs and historical review boundaries. |
| dependency | [Exact radial split](Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) | The original pair-specific damping, the exact log-resultant split and radial bound in the actual minimal-polynomial domain. |
| dependency | [Full mixed resultant](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | Nonzero full doubling resultant and its Frobenius floor for a nontorsion algebraic unit. |
| review | [Extraction finding](../audits/reviews/Yin_R_G0001_v1.md#c4-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |


### Decision current-confluent-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:11 |
| status | proved |
| reason | Select C231#mixed-power-resultant-identities as the complete current home of the identical original L59 full-root cross-exponent nonvanishing, multiplicity and exact resultant conventions at the unchanged used scope. The complete retained proof and actual current statement were read, including non-torsion and degree-drop boundaries; this is routine same-content interface adoption. Mathematical status, selected statement/argument/finding and every relation scope remain. Original dated decisions and R bindings retain their actual L59 inputs, and no new independent review or additional arithmetic surplus is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exactly the enumerated parts with all their separate hypotheses and exclusions. |
| argument | [Argument](#argument) | The complete selected retained derivations, with their explicit supporting inputs and historical review boundaries. |
| dependency | [Dependency](Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) | The original pair-specific damping, the exact log-resultant split and radial bound in the actual minimal-polynomial domain. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Nonzero full doubling resultant and its Frobenius floor for a nontorsion algebraic unit. |
| review | [Review](../audits/reviews/Yin_R_G0001_v1.md#c4-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |

## Statement

Retain every polynomial root with its multiplicity.
For a monic integer polynomial \(P\) of degree \(d\ge1\) with constant term \(\pm1\), write \(\alpha_i=e^{\ell_i+i\theta_i}\), \(m=\sum_i\max(\ell_i,0)\), \(s_n=\sum_i\alpha_i^n\), and
\[
 z_i=e^{-|\ell_i|+i\theta_i},\quad Q(w)=\prod_i(1-z_iw),\quad b_n=\sum_i z_i^n.
\]
For \(r\ge1\), let \(c_r(n)=\sum_{\zeta\ {\rm primitive}\ r}\zeta^n\).
For \(0<t<1\), \(N\ge1\), define
\[
 S_r(P,t)=\sum_{n\ge1}c_r(n)t^n b_n/n,\quad
 T_r(P,t,N)=S_r(P,t)-\sum_{n\le N}c_r(n)t^n b_n/n.
\]
For fixed \(N\) and a fixed prime \(q_0>N\), set \(E_N=\max_{1\le r\le N}(|T_r|,|T_{q_0r}|)\).
All these series converge absolutely for \(t<1\).

**A. Exact damped objects.**
\(Q\) has real coefficients, no zero in the open disk, and the logarithm with value zero at the origin is \(-\sum_{n\ge1}b_nw^n/n\).
For every \(n\ge1\),
\[
 |s_n-b_n|\le2ne^{nm}m.
\]
If \(P\) is a positive Salem polynomial of even degree \(D\), exterior root \(a>1\) and trace roots \(\beta\in(-2,2)\) other than \(a+a^{-1}\), then for \(\sigma=\pm1\), \(q\ge1\), \(F(x)=P(\sigma x^q)\),
\[
 Q_\sigma(w)=P(\sigma w)\frac{1-\sigma w/a}{1-\sigma aw}
 =(1-\sigma w/a)^2\prod_\beta(1-\sigma\beta w+w^2),\qquad
 Q_F(w)=Q_\sigma(w^q).
\]
The rational expression means the polynomial after cancellation.
With \(s=r/\gcd(r,q)\), \(e=\varphi(r)/\varphi(s)\), \(t=1-1/(Dq)\), \(u=t^q\), the exact signed sum is
\[
 S_r(F,t)=-e\log|\operatorname{Res}_x(\Phi_s(x),P(\sigma ux))|
          -e\log|\Phi_s(\sigma u/a)/\Phi_s(\sigma ua)|
\]
whenever the displayed resultant and denominator are nonzero; at a cancellation point use the pole-free product instead.
Also \(b_n(F)=0\) if \(q\nmid n\), and \(b_{qk}(F)=q\sigma^k[s_k(P)-(a^k-a^{-k})]\).
For each fixed seed, \(r,N\), the tails are bounded over all \(q\); once \(q>N\) the low part vanishes.
No irreducibility of \(F\) or decay of its fixed total \(m\) is asserted.

**B. Coefficient-height control.**
Put
\[
 B=\log\|P\|_{\mathbb T}-m,\quad \|P\|_{\mathbb T}=\max_{|w|=1}|P(w)|,\quad
 H=m-\tfrac d2\log t,\quad H_{\rm coeff}=\max_j|p_j|.
\]
Then \(B\ge0\), \(|b_n|\le2nB\), and \(|s_n|\le2nB+2ne^{nm}m\).
If additionally \(\operatorname{Res}(P,\Phi_r)\ne0\) at the order being tested,
\[
 -\varphi(r)B\le S_r\le\varphi(r)H,\qquad
 |T_r|\le\varphi(r)[H+(2N+1)B].
\]
For any sequence with \(d\to\infty\), \(m\to0\) and \(\log H_{\rm coeff}=o(\sqrt d)\), every fixed \(b_n,s_n=o(\sqrt d)\).
At \(t=1-1/d\), the same is true of \(E_N\), provided all its finitely many cyclotomic resultants are nonzero.
Conversely, \(|s_n|\ge c\sqrt d\) for fixed \(n\ge1,c>0\) implies
\[
 \log H_{\rm coeff}\ge c\sqrt d/(2n)-\log(d+1)+m-e^{nm}m.
\]

**C. Growing-band localization.**
Now restrict \(P\) to the monic minimal polynomial of a nontorsion algebraic unit and put \(L=\log\|P\|_{\mathbb T}\).
Use the actual pair-specific coefficients
\[
 C_n=\sum_{i,j}e^{-n|\ell_i-2\ell_j|}\cos(n(\theta_i-2\theta_j)).
\]
For every integer \(K\ge1\),
\[
 \left|\sum_{n\le K}C_n/n\right|\le4K(K+1)L^2+6Kdm.
\]
For each input first define the existing finite Abel limit \(\mathcal T_K=-\lim_{\rho\uparrow1}\sum_{n>K}\rho^n C_n/n\).
Then
\[
 \mathcal T_K\ge d\log2-3dm-4K(K+1)L^2-6Kdm.
\]
Along a hypothetical actual sequence with \(m\to0\) and \(L=o(\sqrt d)\), one can choose integers \(K\to\infty\) with \(KL/\sqrt d\to0\) and \(Km\to0\), obtaining \(\mathcal T_K\ge(\log2-o(1))d\).

These are explicit hypotheses of proved implications, not assumed conclusions about all near-one inputs.
No unconditional fixed-trace bound, coefficient-growth exclusion, high-frequency upper bound or Mahler gap is asserted.
J G0020's finite tables and the later AM01 screen are not premises of A--C.

## Argument

Parts A--C select the retained written equations (1)--(16), not the finite table as a premise.
The necessary D G0011 trace/cyclotomic/smoothing proof is fixed in the support appendix below; its original minimal-polynomial scope and historical review are preserved.
The broader polynomial applicability with explicit nonvanishing was already justified and reviewed in D G0015.
C G0001 and L G0059 supply the mixed-resultant interface.
This is an acyclic chain; there is no mathematical dependency on a mutable draft.
Its source-construction screen and unresolved conjecture are now preserved in [C G0008](Yin_C_G0008_v1.md#arbitrary-trace-construction-measure-screen).
This is a relocation/navigation link, not an added dependency; the selected fixed support appendix below remains unchanged.
The later AM01 screen is outside the 23:51 review and outside the Claim.

### Organization and extraction provenance

The entire text of Yin_D_G0015 dated 2026-10-09 is retained below, including its original title, derivations, equation labels, historical reviews, failed attempts, source boundaries and open questions.
Only heading depth and relocated link targets change.
Its historical statements that adoption was outstanding describe that date; the explicit Current assessment above owns the present judgment.
The source draft is extraction ancestry, not a mutable proof dependency.
Open questions and historical future plans remain historical/exploratory and do not authorize execution while G0001 is paused.
Programs and native certificates remain in their J homes.

### Certified cyclotomic signed tails for actual reciprocal inputs

Bounded arithmetic exploration of G0001.
Assigned AI resultant_research for Yin, 2026-10-09.
This working draft develops the exact damped-root object and retained computations of the finite signed tails from D G0011.
It is not a fixed result or an independent proof review.

#### Question and scope

For fixed N, can actual small-total-Mahler reciprocal inputs exhibit compensating signed tails at square-root degree scale?
Genuine low-measure seeds and radical lifts with fixed total measure will be distinguished.
Bounds claimed for particular instances will use exact algebraic isolation and validated logarithm enclosures; floating approximations alone will not certify them.

The first object check is essential: replacing the damped-root product by P evaluated at scaled roots of unity is generally wrong.
The exterior-root correction must be retained.

<a id="exact-damped-polynomial"></a>
#### The exact polynomial being evaluated

For a monic integer unit polynomial P of degree d, with conjugates alpha_i=exp(l_i+i theta_i), put m=sum max(l_i,0) and

    z_i=exp(-|l_i|+i theta_i),
    Q(w)=product_i(1-z_i w),
    b_n=sum_i z_i^n.

The coefficients of Q are real, but need not be rational or integral.
Its zeros lie outside the open unit disk.
The power series log Q(w)=-sum_(n>=1)b_n w^n/n is consequently valid throughout that disk, with log Q(0)=0.
The previous [trace comparison](#damped-cyclotomic-norm-inequalities) gives

    |s_n-b_n|<=2n exp(nm)m.                            (1)

Suppose first that P is a positive Salem polynomial of degree D with exterior root a>1, interior root a^(-1), and all remaining roots on the unit circle.
For sigma in {1,-1}, the roots of P(sigma x) are the sign twists of the roots of P.
Since P is reciprocal with constant coefficient one and D is even, the exact damped product is

    Q_sigma(w)=P(sigma w)(1-sigma w/a)/(1-sigma a w).  (2)

Equation (2) is a polynomial identity after the indicated linear factor has been cancelled.
One must not evaluate a zero denominator without cancellation.
A separately useful pole-free form is

    Q_sigma(w)=(1-sigma w/a)^2
                  product_beta(1-sigma beta w+w^2),   (3)

where beta ranges over the D/2-1 trace roots in (-2,2).
This also explains the sign twist without declaring the negative real root a Salem number in the usual positive-root convention.

Now use F(x)=P(sigma x^q), with every root retained.
Damping commutes with taking complete q-th root sets, so

    Q_F(w)=Q_sigma(w^q).                              (4)

For example, a root rho exp(i theta) gives q roots of modulus rho^(1/q); damping these gives precisely all q-th roots of its damped image.
The identity does not require irreducibility of F or coprimality conditions.

For r>=1, set s=r/gcd(r,q), e=phi(r)/phi(s), t=1-1/(Dq) and u=t^q.
Raising the primitive r-th roots to the q-th power gives each primitive s-th root exactly e times.
This follows from the surjection of unit residue classes modulo r onto those modulo s, followed by multiplication by q/gcd(r,q), which is invertible modulo s.
Hence the full smoothed sum used in D G0011 is

    S_r(F,t)=sum_(n>=1)c_r(n)t^n b_n(F)/n
            =-e log|Res_x(Phi_s(x),P(sigma u x))|
             -e log|Phi_s(sigma u/a)/Phi_s(sigma u a)|. (5)

The absolute-value cyclotomic product formula also holds for s=1; its sign is immaterial.
In the computed cases every displayed denominator and scaled resultant is nonzero, with a validated exclusion of zero.
Formula (3) supplies an alternative evaluation when cancellation is needed.
The first logarithm in (5) is the logarithm of an exact nonzero rational number; the correction is genuinely algebraic in a and is retained.

The low damped modes are also exact algebraic expressions:

    b_n(F)=0                                     if q does not divide n,
    b_(qk)(F)=q sigma^k[s_k(P)-(a^k-a^(-k))].           (6)

Thus for fixed N, the full sum equals its tail whenever q>N.
At any fixed r and along q coprime to r, t^q tends to exp(-1/D), so (4) and the pole-free product (3) give a finite seed-dependent limit for S_r.
More generally the finitely many possible gcd(r,q) give bounded subsequences.
There are no zeros of Q_sigma in |w|<1, so these limiting logarithms are finite.
This is an all-q bounded-tail statement for each fixed seed, not evidence that its unchanged total m tends to zero.

<a id="finite-certified-tail-inputs"></a>
#### Validated actual-input experiment

[J G0020](../computations/programs/Yin_J_G0020/readme.md) retains six explicit positive reciprocal seeds, their negative sign twists, q in {1,2,3,41,101,1009}, r in {1,2,3,4,6}, and cutoff N=2.
The first five seeds have exterior roots between 1.17 and 1.22, and the quartic is a larger-measure control.
The labels describe inputs; no ranking or completeness claim for the small-Salem tables is used.

The program checks seed irreducibility over Q by exact factorization.
It constructs P(x)=x^(D/2)R(x+x^(-1)) exactly, isolates every root of R in disjoint rational intervals, and checks that one is >2 and all others are in (-2,2).
Those checks establish the seed's Salem root configuration.
All q=1 sign twists are therefore genuine irreducible small-measure reciprocal inputs.
Higher-q inputs are complete radical controls; their irreducibility is not certified by this program.
The already reviewed Lehmer prime lifts q>40 can be read as genuine irreducible instances through [L G0159](../ledger/Yin_L_G0159_v1.md), with the sign-twisted odd-q instance obtained by x->-x.
Their total m still remains fixed.

Exact root intervals of width at most 2^(-240) feed 280-bit Arb arithmetic.
Every logarithm is applied to a real ball strictly separated from zero.
The stored intervals include propagated root-isolation, arithmetic and logarithm errors.
Each displayed ball also has a checked coarse rational enclosure with denominator 10^8; these are finite numerical certificates, conditional on the implementation of the exact/ball arithmetic libraries.
They involve no trace-series truncation.
For q<=3, a second calculation uses (3) at validated roots of unity, independently of the rational resultant representation in (5).

On 2026-10-09 the authoring AI ran the retained command successfully: 360 signed-tail intervals, 180 root-factor representation comparisons, and all 360 required upper bounds S_r<=phi(r)H passed, where H=m-(d/2)log t.
This was a same-author cross-check, not an independently authored verifier.

Representative q=1, sigma=1 tails T_r=S_r-sum_(n<=2)c_r(n)t^n b_n/n are shown below; decimals are rounded summaries of the retained intervals.

| Seed | m | T_1 | T_2 | T_3 | T_4 | T_6 |
| --- | --- | --- | --- | --- | --- | --- |
| Lehmer degree 10 | 0.162358 | 0.720797 | -0.778797 | -0.072560 | -0.796272 | 0.857084 |
| Degree 18 | 0.172581 | 0.225273 | 1.517508 | 0.403283 | -0.543440 | -0.373168 |
| Degree 14a | 0.182344 | 0.645600 | 0.402175 | 0.329313 | 0.268963 | -2.015552 |

The first two seeds have actual (s_1,s_2)=(-1,1) and (1,-1), respectively.
Opposite dyadic signs are realized at small positive total measure, but these traces have constant size and do not form a hypothetical m->0, sqrt(d)-scale family.
The displayed tails have both signs.
The computations therefore give no justification for a universal one-sided tail hypothesis.
The radical controls exhibit the predicted bounded limits, which can be nonzero.
Absolute height and total measure remain different parameters.

<a id="coefficient-size-tail-control"></a>
#### A direct coefficient-size theorem suggested by the exact object

The following written argument applies to every monic integer unit polynomial P, not only to Salem seeds or the computed cases.
Let

    ||P||_circle=max_(|w|=1)|P(w)|,
    B=log||P||_circle-m.

Then B>=0 and

    |b_n|<=2n B,
    |s_n|<=2n B+2n exp(nm)m.                          (7)

Here is a complete elementary proof.
If |alpha_i|>1, then its damped image is 1/conjugate(alpha_i), and on |w|=1,

    |1-alpha_i w|=|alpha_i| |1-z_i w|.

Inside/unit-circle roots are unchanged.
Multiplying proves

    |Q(w)|=exp(-m)|P(w)|,              |w|=1,          (8)

because the reversed polynomial w^d P(1/w)=product_i(1-alpha_i w) has the same circle supremum as P.
Equality at the same angle uses the real coefficients and conjugation; equality of suprema is sufficient.
The maximum-modulus principle yields Re log Q(w)<=B in the open disk.
The harmonic function

    U(w)=B-Re log Q(w)

is nonnegative and has circular mean B, since Q(0)=1.
For 0<rho<1, its n-th Fourier coefficient equals b_n rho^n/(2n) for n>=1 (up to conjugation under the alternative Fourier sign convention).
A Fourier coefficient of a nonnegative integrable function has absolute value at most its mean.
Thus |b_n|rho^n<=2nB, and rho->1 proves the first part of (7); (1) proves the second.
This is the standard positive-harmonic coefficient argument written directly, with no external sharp estimate assumed and no novelty claim.

The same bound controls the actual tails of D G0011 provided Res(P,Phi_r) is nonzero at every order being tested, as it is for an irreducible nontorsion unit or for the complete radical controls here.
This nonvanishing hypothesis is needed for the tail assertion, although (7) applies to arbitrary monic integer unit polynomials.
The integral cyclotomic resultant and smoothing inequality then give S_r<=phi(r)H.
Equation (8) and the maximum-modulus principle give the opposite bound S_r>=-phi(r)B.
Also |c_r(n)|<=phi(r), so for a cutoff N,

    |sum_(n<=N)c_r(n)t^n b_n/n|<=2N phi(r) B,
    |T_r|<=phi(r)[H+(2N+1)B].                        (9)

The bound is valid for each fixed r,N and t in (0,1).
It controls the exact full tail, with no truncation and no presumed sign.

If H_coeff=max_j|p_j|, then ||P||_circle<=sum_j|p_j|<=(d+1)H_coeff.
Consequently any sequence with d->infinity and m->0 satisfying

    log H_coeff=o(sqrt(d))                           (10)

has b_n,s_n=o(sqrt(d)) for every fixed n.
With the nonvanishing hypotheses above and t=1-1/d, (9) also proves E_N=o(sqrt(d)) for the finite set used in D G0011.
In particular polynomially bounded coefficient height suffices.
This is a genuine verification of that draft's tail hypothesis in a coefficient-growth class; it does not prove a Mahler gap on that class.
In the actual G0001 irreducible nontorsion domain, positive m->0 forces d->infinity: bounded d and bounded m give finitely many integer coefficient lists via the elementary symmetric coefficient bound, and finitely many positive m values cannot tend to zero.
The explicit d->infinity hypothesis prevents importing a fixed cyclotomic m=0 polynomial from the broader domain of (7).

Conversely a sequence with d->infinity, m->0 and |s_n|>=c sqrt(d) at a fixed n and c>0 must satisfy

    log H_coeff >= c sqrt(d)/(2n)-log(d+1)
                         +m-exp(nm)m.                (11)

Thus the opposite-dyadic square-root mechanism requires at least exponential-in-sqrt(d) coefficient height along the relevant subsequence.
Integrality and irreducibility do not currently rule out that coefficient growth.
The elementary general estimate H_coeff<=2^d exp(m) is much too large to do so.

<a id="growing-band-resultant-localization"></a>
#### A growing low-frequency band cannot supply the resultant floor in this class

For this section restore the domain of [D G0007](Yin_C_G0001_v1.md): P is the monic minimal polynomial of an irreducible nontorsion algebraic unit.
Its full doubling resultant R_(1,2) is nonzero and has the genuine arithmetic floor |R_(1,2)|>=2^d, by the retained all-conjugate convention in [C231 retained L59 proof](Yin_C_G0231_v1.md#mixed-power-resultant-identities).
The broader arbitrary-unit-polynomial domain of (7) alone would not ensure nonvanishing of this resultant.

Write L=log||P||_circle=B+m and A_n=sum_i exp(i n theta_i).
Since sum_i |l_i|=2m,

    |A_n-b_n|<=sum_i(1-exp(-n|l_i|))<=2nm,
    |A_n|<=2n L.                                     (12)

For the original, pair-specific radial damping of D G0007, define

    C_n=sum_(i,j) exp(-n|l_i-2l_j|)
                       cos(n(theta_i-2theta_j)).

No common radial damping has replaced these factors.
Comparing their finite sum to the undamped angular product gives

    |C_n-Re(A_n conjugate(A_(2n)))|
       <=n sum_(i,j)|l_i-2l_j|<=6ndm.                (13)

Therefore, for every integer K>=1, the first K terms of the actual mixed logarithmic expansion satisfy

    |sum_(n=1)^K C_n/n|
       <=8 L^2 sum_(n=1)^K n + 6Kdm
        =4K(K+1)L^2+6Kdm.                            (14)

This estimate addresses an actual growing finite band and retains the radial error explicitly.
It does not estimate the full infinite Fourier sum by termwise absolute values.

For each fixed input P first take the following Abel limit, with K fixed for that input:

    T_K=-lim_(rho->1 from below) sum_(n>K)rho^n C_n/n.

The limit exists.
Indeed there are finitely many root pairs, each pair factor in the nonzero resultant is nonzero, and its regularized logarithm converges to the corresponding finite logarithm.
Subtracting the finite first K terms preserves that limit.
D G0007's exact radial split consequently reads

    log|R_(1,2)|=B_rad-sum_(n<=K)C_n/n+T_K,
    0<=B_rad<=3dm.

Combining the arithmetic floor with (14) yields the quantitative residual-income requirement

    T_K >= d log 2-3dm-4K(K+1)L^2-6Kdm.             (15)

Only after these per-input Abel limits are defined do we take family asymptotics.
Along a hypothetical actual sequence with m->0 and L=o(sqrt(d)), choose integers K->infinity so that K L/sqrt(d)->0 and Km->0.
Such a choice exists; for example the integer part of

    min{(sqrt(d)/max(L,1))^(1/2), m^(-1/2)}

has these properties eventually.
Then (14) is o(d), while (15) forces

    T_K >= (log 2-o(1))d.                            (16)

Condition (10) implies the required bound on L.
Thus in that coefficient-growth class, the compulsory linear mixed energy must survive beyond a growing low-frequency cutoff.
This is a positive localization of the remaining conjugate-correlation problem, not a contradiction, a high-frequency upper bound, or permission to discard the remaining band.
It does not rule out a valid arithmetic mechanism acting at those higher frequencies.

#### Reuse, source and continuation boundary

The local search covered D G0007/G0011, L G0010, L G0012's known bounded-length/Mignotte gap and its coefficient cost, the existing Smy08 source audit, and G-line trace, height and power-sum interfaces.
The bounded-length gap requires a fixed length bound; (7)--(10) instead concern fixed Fourier modes for coefficient height growing as exp(o(sqrt(d))) and do not assert a gap.
No local fixed result with this exact damped-polynomial coefficient argument was found in that bounded search.
Standard analytic ingredients are proved above, and no novelty or exhaustive-literature claim is made.

Primary source search suggested some of the explicit seed polynomials; their exact admissibility is re-established by J G0020, and no table completeness or external ranking premise is used.
The implementation's interval semantics were checked against [FLINT's Arb documentation](https://flintlib.org/doc/arb.html) and the installed python-flint 0.9.0 docstrings.
No new research source was acquired in this round.

The next useful arithmetic question is what prevents or realizes the coefficient growth in (11) in a genuinely near-one irreducible family.
Within the complementary low-coefficient-growth scope, (16) directs the correlation question to frequencies beyond a growing cutoff, with the original pair-specific damping still present.
Further enlargement of the same fixed-seed tail table would not answer either question.
D G0011's unrestricted fixed-trace target, the mixed-resultant linear-energy problem and the full G0001 contract remain unresolved.
The authoring AI supplied the derivations; the coordinator's interim read prompted explicit degree-escape and resultant-domain guards before this final combined text.
The completed local review below covers this guarded revision; no fixed acceptance or Claim promotion is made here.

<a id="combined-arithmetic-local-review"></a>
#### Local review of the combined argument and computation

At 2026-10-09T15:51 the coordinating AI for Yin completed a separate local review of the whole displayed argument, equations (1)--(16), and the entire J G0020 program.
The reviewer assigned the questions and received author explanations, read earlier D G0007/G0011 arguments, and prompted the explicit degree-escape, cyclotomic-resultant nonvanishing and full-resultant domain guards before this final text.
It did not supply the author's derivations.
This is disclosed exploratory review with author interaction, not a blind assessment or formal verification.

The review checked the damped-root polynomial identity by pairing reciprocal roots, the sign twist and radical-substitution power conventions, the order and multiplicity of the image of primitive r-th roots under q-th powering, the scaled exact-resultant factors, and the all-q fixed-seed limit through the finitely many gcd classes.
It checked that all limiting arguments stay strictly inside the unit disk, where the damped polynomial has no zero.
The low-mode formula and cutoff therefore concern the full damped object, not an uncontrolled truncated logarithmic series.

For (7)--(11), the review checked the circle modulus equality, the zero-free analytic logarithm with value zero at the origin, the mean and Fourier coefficients of the nonnegative harmonic function, and the limit rho approaching one.
Both signs in (9) follow respectively from the maximum modulus bound and the nonzero integer cyclotomic resultant with the displayed smoothing inequality.
The finite-mode estimate uses |c_r(n)|<=phi(r); it does not presume a tail sign.
The coefficient-height implication needs d tending to infinity, explicitly present in the final text.
The elementary coefficient bound justifies this escape in the actual near-one irreducible nontorsion domain.
The converse (11) is the direct rearrangement and provides no upper bound on coefficient growth.

For (12)--(16), the review checked sum_i |l_i|=2m for a unit, the bound 1-exp(-a)<=a, the pair-specific radial comparison and its factor 6ndm, the factor 4K(K+1) in the finite sum, and the sign of the residual tail in the resultant decomposition.
Nonvanishing gives a finite Abel limit separately at each input before any family limit.
The displayed choice of K tends to infinity and makes both K L/sqrt(d) and Km tend to zero, including when L is bounded.
Thus the conclusion genuinely localizes a compulsory linear contribution beyond a growing band; it supplies no contradiction or upper bound for that band.

The coordinator independently reran `.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0020/main.py` under Python 3.12.14, SymPy 1.14.0 and python-flint 0.9.0; completion was observed at 2026-10-09T15:47.
All 360 signed-tail certificates and required cyclotomic upper bounds passed, together with all 180 root-factor representation comparisons.
The program checks all six seeds by exact factorization and trace-root isolation, builds Arb balls from rational enclosures, excludes zero from each logarithm argument, and verifies proposed coarse rational intervals against those balls.
This was a rerun and code review, not an independently implemented verifier.
No mathematical defect was found at the final stated scope.
No discovery search, software-library correctness proof, arbitrary-lift irreducibility check or unrestricted G0001 proof was performed.

#### Subsequent coefficient-bound source screen

The coordinator's [AM01 applicability screen](../audits/literature/AM01/readme.md#coefficient-growth-screen) checked a relevant known irreducible-polynomial bound after this local review.
Its complete adjustable right side remains at least of order sqrt(d) log d when m>=0, so optimizing that estimate cannot remove condition (10).
This is a separately self-checked source comparison, outside the earlier combined review; it neither strengthens the actual coefficient bound to (10) nor proves that large coefficients occur in a near-one family.
The source's full proof and external inputs have not been newly accepted.
Retain the high-frequency and large-coefficient alternatives above.


### Fixed support extracted from D G0011

The following complete historical subsection, equations (3)--(5), supplies the trace error, integer cyclotomic norm and exact smoothing inequality used above.
The Ramanujan and finite-tail definitions are explicit in this Claim statement.
The original subsection was written for actual minimal-polynomial inputs; the already reviewed generalization in the retained D G0015 text uses the same rootwise calculation and explicitly assumes nonzero cyclotomic resultants.
No other D G0011 conclusion is needed.
The equation numbers below are D G0011's historical numbering.

<a id="damped-cyclotomic-norm-inequalities"></a>
#### Exact smoothed inequalities for actual units

Now let alpha be a nontorsion algebraic unit with degree d, conjugates exp(l_i+i theta_i), and m=sum_i max(l_i,0).
Put

    z_i=exp(-|l_i|+i theta_i),
    b_n=sum_i z_i^n in R,             |z_i|<=1.

The b_n need not be integers.
They differ from the actual integer power sums s_n=sum_i alpha_i^n by

    |s_n-b_n|<=2n exp(nm)m.                           (3)

Indeed, for l_i<=0 the summands agree; for l_i>=0 use exp(nl_i)-exp(-nl_i)<=2n exp(nm)l_i and sum the positive l_i.
Reality follows from complex-conjugate pairing.

The cyclotomic resultant is a nonzero integer, and direct root factorization gives

    log|Res(P,Phi_r)|=phi(r)m
         +sum_i sum_(zeta primitive r)log|1-z_i conjugate(zeta)|
       >=0.                                             (4)

For l_i<0 the phase sign in the elementary factorization may reverse; conjugate symmetry of the complete primitive-root set makes the displayed total unchanged.
No individual value at a single nonreal primitive root is being declared rational or integral.

For 0<t<1 and |z|<=1,

    |1-tz|^2-t|1-z|^2=(1-t)(1-t|z|^2)>=0.

Thus replacing every z_i in (4) by t z_i decreases the total by at most -(d phi(r)/2)log t.
Expanding the now absolutely convergent logarithms yields the rigorous inequality

    sum_(n>=1) t^n c_r(n)b_n/n <=phi(r)H,
    H=m-(d/2)log t>0.                                (5)

The d log t term is a retained smoothing cost.
It is not discarded because total m is small.

### Retained D G0011 review and selected scope

The entire original 2026-10-09T15:25 review paragraph follows unchanged.
This Claim relies only on its examination of (3)--(5) and the needed definitions.
Its broader review description, including the MS05 screen, is preserved as historical disclosure and does not expand the present selected proof.

#### Local review of the self-contained calculations

At 2026-10-09T15:25 the coordinating AI for Yin separately checked equations (1)--(10) and their complete derivations.
It rechecked the coprime primitive-root multiplication and q>N guards, the descending finite-band argument, all four N=2 Ramanujan vectors, the damped-root/actual-trace difference, nonzero integral cyclotomic resultants, the exact smoothing inequality and retained d log t cost, both signed-tail inequalities, finite Mobius inversion and the fixed-N asymptotic implication.
It found no defect at this explicitly conditional scope.
The author supplied progress explanations and the draft; the reviewer had assigned the broad follow-up question but contributed no displayed derivation.
It also checked the algebraic implication from the displayed MS05 root equation to (11), without independently rereading that source's construction or verifying its trace assertion; that source interface retains the author's scoped reading.
The review establishes neither high-tail smallness nor arithmetic realization of a trace model.
It is a local exploratory check, not a fixed R/L finding or a Claim/Task adoption.
