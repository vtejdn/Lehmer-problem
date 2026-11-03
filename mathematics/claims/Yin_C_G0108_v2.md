---
author: Yin
---
# Nested divisor slices and the cost of unrestricted Cauchy recursion

Date: 2026-10-14T19:44.
Human author Yin.
Root authors this continuing mechanism analysis under the resumed G0001 goal.
The general weak fractional moment remains open.
C105's new divisor-ideal reduction is currently under independent review; its status is not silently promoted here.

The opening root account records its initial state and proposed continuations.
The [subsequent delegated statement](#nested-slice-continuation-statement) and proofs below own the new outcomes: mass-only stability is now disproved, actual local Cauchy saturation is established, and one exact excluded-prime deficit cancels the nonsummable term.
The general near-extremal inverse problem remains open.

## Responsible question

Can one bound the fractional lcm energy on arbitrary full-capacity divisor ideals by a constant depending only on the exponent?
The first discriminator is the exact cost of removing one prime coordinate.
A useful proof must retain more information than a separate energy bound and unrestricted Cauchy--Schwarz on every pair of slices.

<a id="nested-slice-complete-argument"></a>
## Exact two-slice interface

Fix0<s<1 and t=2-s.
Let p be a prime outside a finite base prime pool.
Let D0 and D1 be nonempty divisor ideals in that base with D1 contained in D0.
Their union D=D0 union pD1 is a divisor ideal.
Write V_i=sum_(a in D_i)phi(a), E_i=sum_(a,b in D_i)phi(a)phi(b)/lcm(a,b)^s, and E01 for the corresponding bilinear energy on D0 times D1.
Set q=p-1.
Multiplicativity of phi and the exact p-exponent in the lcm give

    W=V0+q V1,
    E_s(D)=E0+2q p^(-s) E01+q^2 p^(-s) E1.       (1)

These are exact identities, including ordered cross pairs and diagonal terms.
C104's explicit positive-semidefinite kernel implies E01<=sqrt(E0 E1).
If a recursive argument uses ONLY E_i<=C V_i^t and that Cauchy bound, it yields, with x=V1/V0 in(0,1],

    E_s(D)/W^t <= C F_(p,s)(x),
    F_(p,s)(x)=[1+2q p^(-s)x^(t/2)+q^2 p^(-s)x^t]
                                      /(1+qx)^t.       (2)

This inequality is a valid relaxation.
It does not assert that all three energy bounds can be sharp simultaneously for actual nested slices of the specified mass ratio.

## A nonsummable loss in that relaxation

At the admissible scalar value x=p^(-2), equation(2) has

    numerator=1+2/p-2/p^2+(1-1/p)^2 p^(-t),
    denominator=(1+1/p-1/p^2)^t.

Because t>1, multiplication of the numerator-minus1 by p tends to2.
The mean-value theorem applied to y^t at y=1 gives p times denominator-minus1 tending to t.
Dividing the two positive expressions therefore proves

    lim_(p to infinity) p [F_(p,s)(p^(-2))-1]=2-t=s>0.   (3)

Thus the relaxed local supremum is at least1+s/(2p) for all sufficiently large primes.
A method that merely multiplies these separate worst-case factors cannot obtain a finite uniform global constant: their finite products diverge.
For completeness, sum_p1/p diverges because if it converged, the products product_(p<=Y)(1-1/p)^(-1) would be uniformly bounded (use -log(1-u)<=2u for u<=1/2), whereas their positive geometric expansions contain sum_(n<=Y)1/n, which is unbounded by dyadic grouping.
Then log(1+s/(2p))>=s/(4p) for all sufficiently large p proves the claimed product divergence.

This is an obstruction ONLY to an unrestricted scalar-Cauchy induction.
It is not a construction of nested ideals attaining the relaxed supremum, not an unbounded-energy counterfamily and not a failure of the actual weak inequality.
In particular x=p^(-2) is a permitted number in the relaxed interval, but the exact finite ideal realization and simultaneous near-equality conditions have not been supplied.
C104's product-profile theorem remains consistent: its cross energy is not freely replaced by equality in Cauchy.

## Next live obligations

A productive continuation could establish quantitative loss in E01<=sqrt(E0 E1) when nested slices have very different masses; exploit the fact that a full divisor ideal containing a contains all its divisors and hence has mass at least a; or abandon prime recursion for a direct positive-density localization mechanism.
None is proved here.
General prime-power slices, a useful stability inequality, actual polynomial order inventories and automatic near-one coverage remain open.

This working derivation is entirely root-authored.
Its identities, limit and elementary prime reciprocal divergence were checked symbolically, without a native mathematical run.
It needs later full independent review before adoption as a fixed result.
The exact accepted input is [C104's finite kernel Gram construction](Yin_C_G0104_v1.md#product-fractional-moment-argument); no new external theorem or numerical evidence is used.

<a id="nested-slice-author-continuation"></a>
## Delegated author continuation and source boundary

2026-10-14T19:54.
The delegated g_bridge_audit AI continues this SAME responsible material.
The entire initial identity/relaxed-factor/nonsummable-loss argument above is root's contribution and is preserved.
The delegated author supplies the following actual nested constructions, rectangular convolution proof, local sharpness result and excluded-prime cancellation.
Root's initial request suggested coupled stability as one possible discriminator, but supplied none of these subsequent proofs.
All results below are author deductions awaiting a separate noncontributing whole review.
No mathematical native code or J run is proposed.

The local reuse screen read C104's exact kernel/product formulas, C105's proper-divisor calculations, C91's extremal method and the root derivation above.
C105 was initially still under review; the new analytic arguments below do not use its numerical witness or extremal theorem.
Its selected decision is now independently reviewed, but no prospective acceptance was assumed while deriving these formulas.
The complete general weak inequality remains unresolved.

The rectangular mean calculation was recognized as a classical absolute-convolution mean-value mechanism.
A bounded primary-source search located Noboru Ushiroya, *Mean-Value Theorems for Multiplicative Arithmetic Functions of Several Variables*, INTEGERS12(2012),A33.
The actual [journal-hosted PDF](https://math.colgate.edu/~integers/m33/m33.pdf) was read at Theorem1 and its proof, printed pp.3--4, and Theorem4 on p.5.
Theorem1 gives a multivariable Wintner theorem under absolute convergence of the convolution divided by the coordinate product; its proof uses finite divisor expansion and a controlled tail.
This is checked attribution for the recognized METHOD, not an imported theorem supplying the weighted rectangular limit below.
The present specific triple expansion, absolute majorant, weighted-multiple limit, p-free specialization and constants are all proved directly.
No whole-paper/source-chain audit or literature-wide novelty claim is made, and no new global source record is edited.
The primary arXiv survey1310.7053 was also located as context; no theorem from that survey is used.
The prime reciprocal divergence needed for the finite construction is the already retained L17/root argument, without a distribution rate.

<a id="nested-slice-continuation-statement"></a>
## Statement of the additional findings

Fix0<s<1, t=2-s.
The correlation of two nonempty finite weighted divisor ideals is

    rho(D0,D1)=E01/sqrt(E0 E1).

**A. No mass-only Cauchy stability.**
For any fixed x in(0,1) there are actual finite nested FULL-totient divisor ideals D1 subset D0, avoiding any prescribed finite set of primes, whose mass ratio tends to x and whose rho tends to1.
There are also such sequences with mass ratio tending to0 and rho tending to1.
Thus a uniformly positive Cauchy gap cannot follow merely from nestedness and very unequal masses.
The explicit proper-divisor construction below keeps its normalized-energy imbalance visible; it does not attain all the relaxed bounds simultaneously.

**B. Rectangular ideals give a stronger local saturation.**
There is an explicit finite positive constant R_s, defined in(17) below, such that the full initial-segment ideals have normalized energy tending to R_s.
The bilinear energy of two such initial segments has the exact separated leading term(14) whenever BOTH cutoffs tend to infinity, without any bounded-ratio assumption.
Consequently rho tends to1 even when their mass ratio tends to0, while BOTH normalized energies tend to the SAME positive R_s.

For each fixed prime p, the p-free initial segments have the corresponding constant

    R_(s,p)=R_s/[(1+1/p)^s B_(p,s)],
    B_(p,s)=1+(p^s-1)/[(p^2-p^s)(1+1/p)^2].              (4)

Taking D0={a<=T:p does not divide a} and D1={a<=T/p:p does not divide a} gives actual nested ideals in a prime pool excluding p.
As T tends to infinity, their mass ratio tends to p^-2, both normalized energies tend to R_(s,p), rho tends to1, and the normalized energy of D0 union pD1 tends EXACTLY to

    R_(s,p) F_(p,s)(p^-2).                              (5)

Thus the root's local relaxed factor is genuinely attained in a limiting finite-ideal sense with the two slice constants matched.
This does not assert attainability of a global worst-case constant.

**C. The arithmetic deficit cancels the nonsummable term in this actual family.**
At fixed s and p tending through primes,

    R_(s,p)/R_s=1-s/p+O_s(p^(-t)),
    F_(p,s)(p^-2)=1+s/p+O_s(p^(-t)),
    R_(s,p)F_(p,s)(p^-2)/R_s=1+O_s(p^(-t)).              (6)

Since t>1, the remaining local error is summable over primes.
This is an exact discriminator: in this family the Cauchy loss is not repaired by a uniform correlation gap; the required information is the lower normalized energy caused by forbidding the prime before adding it back.
The result does not prove a comparable deficit for arbitrary near-extremal divisor ideals.

At s1/2, R_(1/2) is STRICTLY less than the sharp product-profile constant K_(1/2) of C104.
Therefore the locally saturating initial-segment family is not globally extremal even against the already proved product class.
No unbounded-energy family, fixed-positive-density capture counterexample, actual polynomial lift or near-one sequence is supplied.

<a id="proper-divisor-cauchy-saturation"></a>
## 1. An explicit finite construction disproving mass-only stability

Let N be squarefree and write

    c=phi(N)/N, y=1-c,
    R=E_s(full divisors of N)/N^t=1+r.

Take D0 to be ALL divisors of N and D1 its proper divisors, with full phi weights.
Both are finite divisor ideals, D1 subset D0, and their masses are N and yN.
The exact full-row calculation at N gives

    E0=N^t(1+r),
    E01=N^t(y+r),
    E1=N^t(y^2+r),
    1-rho^2=r(1-y)^2/[(1+r)(y^2+r)].                    (7)

The formulas follow by deleting the maximal order from one or both energy sums, retaining its diagonal.
They also follow directly by expanding the difference between the denominator and numerator of rho^2.
Here r>=0 by C104's exact full-product factors.

For any INTEGER cutoff H>=2, choose N from primes strictly greater than H.
C104's squarefree factor formula gives

    0<=log R
      =sum_(q|N)log[1+(q^s-1)/q^2]
      <=sum_(n>H)n^(-t)
      <=H^(1-t)/(t-1).                                 (8)

This bound is independent of the number of chosen primes.
Fix x in(0,1), and take the shortest initial product of primes exceeding H for which c<=1-x.
It exists because the corresponding product of1-1/q tends to0, by the retained elementary reciprocal-prime divergence.
Immediately before the last prime the product exceeds1-x, and that last prime exceeds H.
Hence

    x<=y<x+(1-x)/H.                                    (9)

As H tends to infinity, y tends to x and r tends to0 by(8), so rho tends to1 by(7).
Excluding any fixed finite prime set is achieved by putting H above it.
Every member is an actual full INTEGER capacity array; no arbitrary real weights or unattained finite optimization are used.

For a sequence with vanishing mass ratio, put x_j=1/j, j>=2, and choose INTEGER H_j>=j^(4/(1-s)), for example by taking the ceiling of the displayed real threshold.
Equations(8)--(9) give y_j~1/j and r_j=O_s(j^-4), hence r_j/y_j^2 tends to0.
Equation(7) again gives rho_j tending to1 while V1/V0=y_j tends to0.
The normalized energies satisfy

    E0/V0^t=1+r_j ->1,
    [E1/V1^t]/y_j^s=1+r_j/y_j^2 ->1.                   (10)

Thus this explicit family has no correlation gap, but its small slice has a vanishing normalized energy.
It does NOT show that both estimates E_i<=C V_i^t are almost sharp with the same C.
The next construction addresses that distinction.

<a id="rectangular-fractional-convolution"></a>
## 2. Complete rectangular energy asymptotic

Let mu denote the Mobius function: it is0 on integers divisible by a square and(-1)^k on products of k distinct primes.
Define J_s multiplicatively by J_s(1)=1 and

    J_s(q^e)=q^(se)-q^(s(e-1)), e>=1.

Finite prime-factor expansion proves

    phi(n)/n=sum_(k|n)mu(k)/k,
    gcd(a,b)^s=sum_(d|a,d|b)J_s(d).                      (11)

In particular J_s(d)>0.
Let

    U_X(m)=sum_(n<=X,m|n)n^(t-1),
    E_s(X,Y)=sum_(a<=X,b<=Y)phi(a)phi(b)/lcm(a,b)^s.

For every m>=1 and X>0,

    0<=U_X(m)/X^t<=1/m,
    U_X(m)/X^t ->1/(tm) as X->infinity with m fixed.     (12)

The upper bound follows from sum_(j<=u)j^(t-1)<=u^t; the limit follows from upper/lower integral comparisons for that increasing power.
There is no requirement that X be integral.
Expanding(11) in the finite sums gives the EXACT identity

    E_s(X,Y)=sum_(d,k,l>=1) J_s(d)mu(k)mu(l)/(kl)
                 *U_X(lcm(d,k))*U_Y(lcm(d,l)).          (13)

For fixed X,Y, only finitely many terms are nonzero.
The following absolute-convergence check justifies taking BOTH cutoffs to infinity independently.

Set C_plus=product_q(1+q^-2)<infinity.
For each fixed d, multiplicativity and positive geometric products give

    sum_k |mu(k)|/[k lcm(d,k)]
       =(C_plus/d) product_(q|d)(1+1/q)/(1+1/q^2).

Therefore the absolute majorant after using(12) is

    sum_d J_s(d) [sum_k |mu(k)|/(k lcm(d,k))]^2
     =C_plus^2 product_q [1+h_q (q^s-1)/(q^2-q^s)]<infinity,
    h_q=[(1+1/q)/(1+1/q^2)]^2<=9/4.

Indeed each local excess is at most(9/4)q^-t/(1-2^-t), whose sum converges because t>1.
Every use of an infinite product here is the monotone limit of its finite nonnegative expansion, bounded by the exponential of a convergent sum.
This proves absolute convergence of the displayed triple series, rather than assuming a general mean-value theorem.

Now fix any tolerance, truncate the ABSOLUTE triple series to a finite part with small remaining tail, apply the fixed-m limit(12) to that finite part, and bound the rest by the same absolute majorant.
This proves, whenever X AND Y tend to infinity,

    E_s(X,Y)/(X^t Y^t) -> M_s/t^2,                     (14)
    M_s=sum_(d,k,l>=1)J_s(d)mu(k)mu(l)
                     /[kl lcm(d,k)lcm(d,l)].

No bounded ratio of X and Y is needed.
To evaluate the positive constant, put A=product_q(1-q^-2)=1/zeta(2)>0.
The signed inner sum, now justified by absolute convergence, is

    sum_k mu(k)/[k lcm(d,k)]
       =(A/d)product_(q|d)(1+1/q)^(-1).

Thus

    M_s=A^2 product_q B_(q,s),
    B_(q,s)=1+(q^s-1)/[(q^2-q^s)(1+1/q)^2].             (15)

Every local factor exceeds1 and is1+O_s(q^-t); hence the product is finite and positive.
The identity A=1/zeta(2) is the same absolutely convergent finite-prime geometric expansion already proved in C105; it can equally be kept as the positive Euler product here.

For completeness, the mass W(X)=sum_(a<=X)phi(a) satisfies

    W(X)/X^2 -> A/2=:b.                                (16)

Expand the first identity in(11), write a=kj, and use sum_(j<=u)j/u^2->1/2.
The dominating coefficients are |mu(k)|/k^2, summable.
This is the one-variable version of the SAME finite-part/tail argument, not an unproved totient asymptotic.
Consequently the normalized initial-segment energy tends to

    R_s:=M_s/[t^2 b^t]
        =(2^t/t^2)A^s product_q B_(q,s)>0.              (17)

Equations(14)--(16) show that E_s(X,Y)/sqrt(E_s(X,X)E_s(Y,Y)) tends to1 whenever both X,Y tend to infinity.
For example X_j=j^2,Y_j=j gives nested FULL-totient integer divisor ideals with mass ratio tending to0, correlation tending to1, and BOTH normalized energies tending to R_s.
This refutes a mass-only gap even after imposing a common positive limiting normalized energy.
It does not assert that R_s is a global extremal constant.

<a id="prime-free-coupled-constants"></a>
## 3. Excluding the new prime: the exact coupled arithmetic constants

Fix a prime p.
Restrict all orders in the preceding sums to p-free integers.
Write W_p(X), E_(s,p)(X,Y) for the resulting mass and bilinear energy.
For m prime to p, the multiple sum with p-free terms equals

    U_X^(p)(m)=m^(t-1)
       [sum_(j<=X/m)j^(t-1)-p^(t-1)sum_(j<=X/(mp))j^(t-1)].

It is nonnegative, at most U_X(m), and its ratio to X^t tends to(1-1/p)/(tm).
If m is divisible by p the restricted sum is zero.
Thus the SAME absolutely convergent proof applies after restricting d,k,l to p-free integers.
Removing the one local factor in(15) gives

    E_(s,p)(X,Y)/(X^t Y^t)
      ->(M_s/t^2)*(1-1/p)^2/[(1-p^-2)^2 B_(p,s)].       (18)

Likewise the mass calculation, using the first identity in(11) with p-free k and j, gives

    W_p(X)/X^2 ->b/(1+1/p).                            (19)

Division of(18) by the t-th power of(19)'s constant proves(4).
Every limit is for FIXED p; no uniform error as p varies is being asserted by these calculations.

For T>=p, take the actual finite ideals

    D0(T,p)={a<=T:p does not divide a},
    D1(T,p)={a<=T/p:p does not divide a}.

Their base prime pool is finite and excludes p.
They are nested and contain1.
Equations(18)--(19) prove, at fixed p as T tends to infinity,

    V1/V0 ->p^-2,
    E0/V0^t ->R_(s,p), E1/V1^t ->R_(s,p),
    E01/sqrt(E0 E1) ->1.                              (20)

The root's exact identity(1) now gives(5).
The union D0 union pD1 is exactly the full-totient ideal of integers a<=T with v_p(a)<=1.
Thus all these statements concern finite actual INTEGER capacities, not a hypothetical matrix or arbitrary mass assignment.
The limit in(20) demonstrates local saturation of all three ingredients at the COMMON constant R_(s,p), while leaving global extremality unproved.

<a id="excluded-prime-deficit-cancellation"></a>
## 4. Cancellation of the nonsummable term, with limit order retained

From(15), B_(p,s)=1+O_s(p^-t).
The elementary Taylor estimate for(1+u)^(-s) on0<=u<=1/2 gives

    R_(s,p)/R_s=1-s/p+O_s(p^-t).

Here a p^-2 error is absorbed into p^-t because1<t<2.
For the root factor at x=p^-2, its exact numerator is

    1+2/p-2/p^2+(1-1/p)^2p^-t,

and its denominator is(1+1/p-1/p^2)^t.
Taylor expansion with a bounded second derivative on the fixed positive interval gives

    F_(p,s)(p^-2)=1+s/p+O_s(p^-t).

Multiplying these two estimates proves all of(6).
Constants in O_s depend only on the fixed exponent, not on p.
Since sum_p p^-t converges, this actual local excess has a summable bound.
The first-order1/p gain is offset by the normalization deficit of the p-free slice class BEFORE the new prime is inserted.

The conclusion is an ITERATED limiting statement: first T tends to infinity for each fixed p, then p grows.
If desired, it yields actual finite diagonal examples by choosing, for each p, a sufficiently large integer T(p) so that all the finitely many ratios in(20) and the union energy lie within p^-3 of their stated limits.
Such a finite choice exists by the proved fixed-p limits.
No effective uniform cutoff, evaluated T(p), native computation or simultaneous unproved uniform limit is claimed.

This proves neither that every nested ideal has the same arithmetic deficit nor that all possible prime-step errors are summable.
It shows exactly why a mass/correlation-only repair is insufficient, and identifies a coupled quantity that actually cancels the root's nonsummable term on a substantial correlated family.

<a id="interval-energy-not-global-extremum"></a>
## 5. Half-moment comparison and the remaining inverse problem

At s1/2,t3/2, C104's local optimal product factor is

    K_q=(1-q^-2)/(1-q^-t),
    K_q-1=(q^s-1)/(q^2-q^s)>0.

Hence B_(q,s)=1+(K_q-1)/(1+1/q)^2<K_q at EVERY prime, and both infinite products converge.
Their product inequality is strict already at q2.
The remaining scalar factor in(17) is also less than1 at s1/2: its square is128/[81 zeta(2)].
The elementary integral comparison gives

    zeta(2)=1+1/4+sum_(n>=3)n^-2
             >1+1/4+integral_3^infinity x^-2 dx
             =19/12>128/81.

Therefore

    R_(1/2)<K_(1/2).                                   (21)

Full product profiles can approach K_(1/2), by the proved C104 sharpness construction, so the locally saturating initial-segment profiles are NOT globally extremal.
The stronger C105 obstruction to extending the product constant remains separate; it is not needed to prove(21).

The meaningful next inverse question is consequently narrower than the abandoned mass-only gap: can simultaneous NEAR-GLOBAL-EXTREMALITY of two nested slices, together with near equality in Cauchy, force a structural or excluded-prime cost sufficient for summable recursion?
Neither(7) nor(20) answers that question negatively, because their normalized slice values have the explicit deficits described above.
Conversely the root's original scalar relaxation is now known to be locally saturable at some common slice constant, so dismissing its nonsummable factor as automatically unrealizable would be incorrect.

No full weak fractional bound, divergent normalized-energy family, positive-density/no-capture counterexample, actual Frobenius inventory, original norm income or near-one Mahler family has been produced by this round.
The progress is a rigorous boundary for stability approaches and an exact cancellation mechanism with its costs and limit order.
All finite ideals, integer capacities, mass ratios and correlations used above are explicitly defined; their asymptotic evaluation is analytic, not experimental.

<a id="nested-slice-author-checks-and-freeze"></a>
## Complete author checks and bounded-round freeze

2026-10-14T19:57.
The delegated author checked the root identity and relaxed factor as supplied, preserved their root attribution, and checked every new step independently within its contributor role: exact proper-divisor bilinear/diagonal correction and correlation defect; shortest finite prime-product selection and its overshoot; all small-mass errors in(8)--(10); both finite divisor identities; the absolute triple-series Euler majorant and finite-part/tail limit with independently growing cutoffs; the signed local factors and positive arithmetic constants; p-free weighted-multiple and mass limits; actual finite slice identities; the fixed-p-first limit order; cancellation of the two1/p terms; and the strict half-moment comparison using only a rational integral lower bound for zeta(2).
These are complete AUTHOR checks, not independent review.

Freeze the entire root account, delegated statement A--C, all five continuation sections/equations4--21, source-attribution account, failed stability routes, explicit finite ideals, limiting constants and restrictions for a separately organized noncontributing WHOLE review.
The scoped material check passed for this D; it does not prove the mathematics.
The selected statement entrance is #nested-slice-continuation-statement and the complete retained argument begins at #nested-slice-complete-argument.
No mathematical native program, J, numerical measurement or formal proof was performed by this delegated author.
Both root and this author are contributors and cannot supply independent acceptance of this whole artifact.
General correlated weak control, near-global-extremal slice stability and actual near-one coverage remain unresolved.

## Version 2 auxiliary-cutoff correction

2026-10-14T20:04.
During the separately organized whole review, the noncontributing strategy_critique reviewer identified that the tail comparison sum_(n>H)n^(-t)<=H^(1-t)/(t-1) in the proper-divisor construction requires INTEGER H, whereas v1 had allowed an arbitrary real cutoff.
Root independently verifies the comparison on each integer interval and makes H and H_j explicitly integer above.
Every sequence and finite-prime exclusion used in the argument permits these integer choices; the stated A--C conclusions and all subsequent rectangular real cutoffs are unchanged.
The earlier v1 remains the complete pre-correction physical version.
This is a correction of the auxiliary parameter domain, not a claim that the v1 displayed inequality held at every real H.
The reviewer's observation and recommended guard are disclosed; no new theorem or native computation is introduced.

## Fixed organization

The complete authored account is retained with the explicitly identified version2 cutoff correction.
The pre-correction original remains in C108 v1.
All other arguments, useful failures, source and contribution accounts retain their original scope.
This actual corrected artifact awaits complete separately organized review; revision is not acceptance.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:04 |
| status | open |
| reason | Correct the auxiliary H/H_j cutoff domain to integers after the actual v1 review observation and submit this complete v2 argument for whole review. Nested-slice correlation, exact rectangular means and excluded-prime cancellation, with no universal weak bound asserted. The original G0001 goal remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#nested-slice-continuation-statement) | Complete A--C, actual finite nested ideals, local saturation, cancellation and exact unresolved limits. |
| argument | [Entire root and delegated proof](#nested-slice-complete-argument) | Initial two-slice identities and nonsummable relaxation plus every subsequent proof, limit, constant and source boundary. |
| dependency | [Product/kernel input](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite positive-semidefinite kernel, full-divisor product factors and exact sharp product comparison. |
| support | [Earlier prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Existing classical prime-reciprocal divergence and source attribution; elementary proof retained locally as well. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:11 |
| status | proved |
| reason | Adopt R345 complete independent review of the actual corrected v2. The preserved v1 unrestricted-real cutoff defect is resolved by explicit integer H/H_j; all A--C and independently growing rectangular cutoffs retain their exact scopes. Nested local saturation and excluded-prime cancellation do not prove a global weak bound. The unrestricted G0001 objective remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#nested-slice-continuation-statement) | Complete A--C, actual finite nested ideals, local saturation, cancellation and exact unresolved limits. |
| argument | [Entire root and delegated proof](#nested-slice-complete-argument) | Initial two-slice identities and nonsummable relaxation plus every subsequent proof, limit, constant and source boundary. |
| dependency | [Product/kernel input](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite positive-semidefinite kernel, full-divisor product factors and exact sharp product comparison. |
| support | [Earlier prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Existing classical prime-reciprocal divergence and source attribution; elementary proof retained locally as well. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0345_v1.md#nested-slice-v2-whole-independent-finding) | Entire actual statement/argument and all direct inputs, exact correction or construction boundaries and preserved source limits. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#nested-slice-continuation-statement) | Complete A--C, actual finite nested ideals, local saturation, cancellation and exact unresolved limits. |
| argument | [Entire root and delegated proof](#nested-slice-complete-argument) | Initial two-slice identities and nonsummable relaxation plus every subsequent proof, limit, constant and source boundary. |
| dependency | [Product/kernel input](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite positive-semidefinite kernel, full-divisor product factors and exact sharp product comparison. |
| support | [Earlier prime divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Existing classical prime-reciprocal divergence and source attribution; elementary proof retained locally as well. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0345_v1.md#nested-slice-v2-whole-independent-finding) | Entire actual statement/argument and all direct inputs, exact correction or construction boundaries and preserved source limits. |

### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:55 |
| status | proved |
| reason | The new isolated whole review actually covers complete A--C and every proof/interface, including the integer H/H_j correction and full affected construction/limit chain. The old v1 cutoff failure and original source/limit evidence remain distinct; no unrestricted inequality or Mahler gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#nested-slice-continuation-statement) | Complete A--C, actual finite nested ideals, local saturation, cancellation and exact unresolved limits. |
| argument | [Entire root and delegated proof](#nested-slice-complete-argument) | Initial two-slice identities and nonsummable relaxation plus every subsequent proof, limit, constant and source boundary. |
| dependency | [Product/kernel input](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite positive-semidefinite kernel, full-divisor product factors and exact sharp product comparison. |
| support | [Earlier prime divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Existing classical prime-reciprocal divergence and source attribution; elementary proof retained locally as well. |
| review | [Fresh complete independent finding](../audits/reviews/Yin_R_G0520_v2.md#current-nested-slice-v2-whole-finding) | Complete current statement, entire argument and every necessary selected interface at the exact retained scopes; actually isolated independent review, with the old negative scope compared only after initial mathematical findings. |

