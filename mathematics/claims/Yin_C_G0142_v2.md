---
author: Yin
---
# Uniform weak fractional lcm moments and original-window capture

Opened: 2026-10-15T10:41.
Human author Yin.
New delegated G0001 inquiry by g_bridge_audit under root's mathematical assignment.
Root supplies the question, not a proof step.
At opening, the preceding D40 was frozen in C138v1 and its owner was preparing the full-account v2 correction.
That is historical context, not a premise or a claim about its current adoption; no alteration of frozen D40 is made here.

Current outcome: Sections4--7 give an author-complete general weak fractional lcm moment bound and original-window capture, using the actually accepted GW21-U002 lemma.
In particular the original triple-to-four-coordinate target is answered with B=1, subject to independent whole review and responsible adoption.
Sections1--3 preserve the earlier valid gluing/polylogarithmic route and its then-unresolved constant-window limit.
Automatic positive-density coverage by actual polynomial root groups remains open.
The precise final theorem is at [the final statement](#statement).

## Exact target and original quantities

For finite distinct positive integer labels with real capacities0<w_a<=phi(a), total W>0, integer X>=1, X<=CW and original ordered triple density delta3_X>=delta>0, decide whether fixed constants B(C,delta)>=1 and delta'(C,delta)>0 always give delta4_(B X)>=delta'.
Every density uses the SAME original law w/W, with repeated labels and ineligible original mass retained.
A counterfamily would have to satisfy every capacity, linear-window and fixed-positive-triple premise.
An arbitrary hypergraph or an array with X/W diverging does not qualify.
A new auxiliary statistic by itself does not close the target.

## Bounded reuse

The opening reuse screen read the exact adopted C119 canonical-tree/chain interface, C121v2 merged capacity and original-lcm guard, C124 fixed-terminal-support capture, the then-current C138 positive proof and pending failure-account correction, C91's full pair-link decomposition, C96's refutation of the LINEAR short-pair bound, and the already inspected C104/C105/C108/C115 weak-moment boundaries.
C96's full-capacity divisor ideals have H/W tending to0 but no proved fixed-positive triple density; they are not counterexamples to this target.
The old false bound P2(Y)<=K YW cannot be reinstated.
C133's weaker fractional short-pair control is conditional on its actually paid prime core, not universal.

A targeted G-only search for overlapping triples, shared pairs, quadruple lifting and higher-order density found the current C138 and the old deepest-coordinate records, but no exact fixed-enlargement theorem in the inspected matches.
This is a bounded screen, not a novelty claim.
The initial route in Sections1--3 used elementary lcm identities and finite weighted Cauchy--Schwarz with existing interfaces; the later route explicitly added GW21-U002.
No native program or J is invoked.

## Historical first mechanism to test

Two compatible triples sharing a pair(a,b) have four-coordinate lcm at most X^2/lcm(a,b).
Thus a fixed-positive fraction of triple mass carried by pairs with lcm(a,b)>=epsilon X would lift into the fixed enlarged window X/epsilon.
At this initial stage the unresolved issue was whether the full capacity and linear-window assumptions force enough such pairs, or whether an alternative arithmetic argument can use the short-pair mass.
No one-time capture is assumed in establishing this lift, avoiding the circular argument from an already captured positive fraction.
Sections4--6 subsequently supply that alternative through the weak moment.

<a id="shared-prefix-lcm-gluing"></a>
<a id="argument"></a>
## 1. Exact original-law gluing through a shared prefix

For ANY finite nonempty positive weighted integer array, not yet using capacities, put mu(a)=w_a/W.
For real Z>0 and integer r>=2 define

    delta_r(Z)=Pr_(mu^r){lcm(a_1,...,a_r)<=Z}.

Every coordinate is sampled independently from the SAME original law, with replacements and ineligible labels included.
Define p2^Z(Y) as the original probability that a,b<=Z and lcm(a,b)<=Y.
For any integer r>=3, real Z>=1 and Y>0,

    delta_(r+1)(Z^2/Y)
       >=[delta_r(Z)-p2^Z(Y)]_+^2.                   (1)

Here a real window below1 gives zero density, consistently with the formula.
In a positive case Y<Z automatically follows from p2^Z(Y)<delta_r(Z).

To prove(1), fix an ordered prefix A=(a_1,...,a_(r-1)), let L(A) be its lcm, and let f(A) be the original-law probability that a final c satisfies lcm(A,c)<=Z.
Then0<=f<=1 and E f=delta_r(Z).
The contribution from L(A)<=Y is at most p2^Z(Y): whenever f>0 all prefix labels are eligible, and L(A)<=Y implies lcm(a_1,a_2)<=Y.
All other prefix coordinates have total probability1.
Therefore E[1_(L>Y) f]>=[delta_r(Z)-p2^Z(Y)]_+.

Conditional on A, choose independent c,e from the original law.
If both links are compatible at Z and L>Y, then

    lcm(A,c,e)
       =lcm(lcm(A,c),lcm(A,e))
       <=lcm(A,c)*lcm(A,e)/L < Z^2/Y.                (2)

The common factor L divides both integers, so the inequality is exact at every prime.
Weighted Cauchy--Schwarz on the prefix probability space gives

    E[1_(L>Y)f(A)^2]>=(E[1_(L>Y)f(A)])^2.

The left side counts a subset of(r+1)-tuples compatible at Z^2/Y by(2), proving(1).
Prefix repetitions, repeated final labels and equal original orders require no exclusion.
No arbitrary-hypergraph realization, common time capture or changed conditional law enters this proof.

For r=3 this is the requested shared-pair mechanism.
It shows exactly where a universal weak fractional pair bound would suffice: if some0<s<1 and K_s satisfy E_s<=K_s W^(2-s) for all original capacity arrays, choose Y=W(delta/(2K_s))^(1/s).
Then p2^X(Y)<=delta/2, and(1) gives delta4_(B X)>=delta^2/4 with fixed B=max{1,C(2K_s/delta)^(1/s)} when X<=CW.
At this stage the weak L1 capacity bound was still open; the displayed implication did not prove it or reintroduce C96's false linear bound.
Its later proof is in Section4, with the final unconditional-in-capacity statement in Section6.

<a id="unconditional-polylogarithmic-lift"></a>
## 2. Unconditional positive density at a logarithmically enlarged window

Now assume the ACTUAL real capacities0<w_a<=phi(a), W>0, integer X>=1, X<=CW and delta3_X>=delta>0.
Fix once epsilon0=1/2 in the accepted C101/GW21 bound and write

    beta=4/5, r0=3/5,
    B0=(4K_(1/2))^(2/5),
    Q(delta)=(2B0/delta)^(1/beta).                    (3)

The source constant K_(1/2)>=1 is precisely GW21-U001/C101's fixed finite constant.
It is not numerically evaluated or replaced by a constant uniform as the source epsilon goes to0.

Let W_j be the original eligible masses in the dyadic bands[2^j,2^(j+1)) up to X and let

    L_eff=(sum_j (W_j/W)^r0)^(2/beta),
    L=1+floor(log_2 X).

C101 gives0<L_eff<=L under the positive-density premise, while every ineligible label remains in W.
Choose the positive real threshold

    Y=(W/L_eff)*(delta/(2B0))^(1/beta).              (4)

Its ACTUAL weighted short-pair bound gives p2^X(Y)<=delta/2.
By(1),

    delta4_(Q(delta)*(X/W)*L_eff*X)>=delta^2/4.       (5)

The displayed real window is necessarily greater than X: otherwise Y>=X, which would force p2^X(Y)>=delta3_X>=delta, contradicting its upper bound.
Rounding the window UP preserves the density.
In particular, with the fixed constant

    A4=1+C Q(delta),

one has the unconditional same-original-law statement

    delta4_(ceil(A4*X*(1+floor(log_2 X))))
                               >=delta^2/4.         (6)

Indeed the window in(5) is at most C Q(delta) X L, and ceil is monotone; the harmless extra1 in A4 ensures a conventional factor at least1.
Formula(5) retains the already-defined actual scale-mass price; formula(6) requires no extra hypothesis or newly introduced complexity bound.

This preliminary deduction gives positive quantitative lifting at O_(C,delta)(X log(2X)) time.
By itself it does NOT prove the requested fixed-B(C,delta) result.
In particular its factor L cannot be renamed a constant, and no input-uniform Mahler gap follows from its unbounded auxiliary-degree cost.
C101's previous H_X bound alone would only imply a four-coordinate density tending to0; the shared-prefix calculation instead supplies a fixed positive fourth density at the explicitly enlarged window.
The subsequent independent change of argument in Sections4--6 addresses the remaining fixed-window problem.

<a id="polylogarithmic-lift-argument"></a>
## 3. Direct source/interface check and fixed higher-arity extension

The only non-elementary input to(5)--(6) is [C101's adopted weighted two-band/global estimate](Yin_C_G0101_v1.md#statement).
Its source is [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001), at its existing published Theorem1.1 statement/applicability scope.
The exact C101 global formula is

    P2^Z(Y)<=B0 Y^beta W^(2-beta) L_eff(Z)^beta       (7)

for arbitrary REAL Y>0 and the same original weights0<w_a<=a.
Our phi capacities imply that weaker upper bound.
C101 already handles empty bands, fractional weights, source D=max(1,AB/Y), diagonal pairs, Y<1 and the original denominator W.
Substitution of(4) into(7) gives delta/2 exactly.
No new weighted adaptation of the source or original proof audit is asserted.

The same mechanism supplies every FIXED higher arity at a paid polylogarithmic window.
Set d_3=delta and recursively

    d_(r+1)=d_r^2/4,
    d_r=4(delta/4)^(2^(r-3)), r>=3.                  (8)

There are fixed constants A_r>=1, depending only on r,C,delta and the fixed B0, such that

    delta_r(ceil(A_r X L^(2^(r-3)-1)))>=d_r.          (9)

One fully finite construction starts with an ACTUAL integer window Z_3=X and performs the following steps.
At Z_r, let L_r=1+floor(log_2 Z_r) and choose

    Y_r=(W/L_r)*(d_r/(2B0))^(1/beta),
    Z_(r+1)=ceil(Q(d_r)*Z_r^2*L_r/W).                (10)

Since L_eff(Z_r)<=L_r, (7) gives p2^(Z_r)(Y_r)<=d_r/2.
If delta_r(Z_r)>=d_r, then Y_r<Z_r by the same eligibility argument as before.
Hence the unrounded next window exceeds Z_r>=1, and (1) proves delta_(r+1)(Z_(r+1))>=d_(r+1).
This keeps the SAME original law even though additional original labels may become eligible at later windows.

For explicit growth constants put b_r=2^(r-3)-1, A_3=1 and

    D_r=2+log_2 A_r+b_r,
    A_(r+1)=max{1,2 C Q(d_r) D_r A_r^2}.             (11)

Inductively Z_r<=A_r X L^b_r.
Indeed L_r<=D_r L follows from log_2 X<L, log_2 L<=L and A_r,L>=1.
The unrounded expression in(10) is at least1, so ceiling costs at most a factor2.
Using X<=CW gives

    Z_(r+1)<=2 Q(d_r) D_r A_r^2 C X L^(2b_r+1)
                 <=A_(r+1) X L^b_(r+1).

This proves(9) at the displayed ceiling.
The constants grow rapidly with r, which is FIXED before varying the original array.
There is no uniform-in-r claim.
The first nontrivial exponent is b_4=1.
At X1, L1 and the same formulas remain valid; positive density ensures an eligible label, and every finite probability-space step still includes repeats.

<a id="weak-moment-concentration-working-breakthrough"></a>
## 4. A changed route: a minimal-counterexample weak moment

The source inspection moved beyond the already accepted GW21 Theorem1.1.
The actual published PDF was opened at its introduction and Sections2--3, and local PDF pages3--4 were text-extracted.
Lemma2.1 uses q=2+epsilon with0<epsilon<1, its CONJUGATE q'=q/(q-1)<2, finitely supported probability measure nu on Z^2, nonnegative vectors x,y of lq' norm1, c<=1 and lambda<=4/5.
Under nu(i,j)<=c lambda^|i-j| x_i y_j, it states c>=1/9 and concentration outside |i-k|+|j-k|<=1 bounded by an epsilon-dependent constant times lambda^(q+epsilon).
The PDF text extraction drops the prime on q'; the proof explicitly uses that conjugate exponent below2.
The initial derivation was recorded as source-conditional while root arranged an exact source-only check.
That condition is now resolved by actual GW21-U002 as documented in Section6.
Independent review of the project adaptation remains pending.

Proposition1.2 of that paper concerns a hypothetical minimum-prime-support counterexample to its own theorem, not an arbitrary dense gcd graph.
It cannot be imported here as an all-input structural theorem.
Instead the project must prove its own minimal-counterexample setup and then apply the GENERAL probability Lemma2.1 at its actual scope.

Fix2/3<s<1, put

    t=2-s, q=2/s, q'=2/(2-s), epsilon=q-2,
    rho_p=p^(-s/2),
    E_s(w)=sum_(a,b)w_a w_b/lcm(a,b)^s.              (12)

Then0<epsilon<1, rho_p<=2^(-1/3)<4/5, and rho_p^(q+epsilon)=p^(-(2-s))=p^(-t).
Let A_s be an admissible fixed concentration constant for the source lemma at this epsilon.
Choose a FIXED integer p0>=2 so large that

    A_s sum_(n>p0)n^(-t)<=1/2.                       (13)

Such a finite p0 exists because t>1; for example its integral tail is at most p0^(1-t)/(t-1).
The candidate uniform theorem is the stronger support-sensitive assertion

    E_s(w)<=8*10^(# {p<=p0:p divides some label})
                                  *W^(2-s)           (14)

for EVERY finite real phi-capacity array.
In particular the uniform constant8*10^pi(p0) would suffice, with no uncharged prime pool or tree complexity.

Assume a counterexample to(14) and select one with the LEAST possible number of occurring primes.
This uses a minimum positive integer among counterexamples, not an unproved compactness or extremizer over an infinite universe.
The prime-free case has only label1 and0<W<=1, so E_s=W^2<=W^(2-s) and is not a counterexample.
Let Q be the counterexample's finite prime pool and let m0 count its primes<=p0.

For any p in Q, write a=p^i n with p not dividing n.
Let W_i=sum_n w_(p^i n) and, on nonzero slices, define

    v_i(n)=w_(p^i n)/phi(p^i),
    V_i=sum_n v_i(n)=W_i/phi(p^i),
    mu_i=W_i/W.

Multiplicativity of phi gives0<=v_i(n)<=phi(n), and these arrays have fewer occurring primes.
By minimality they obey(14), with constant at most

    K_minus=8*10^(m0-1_(p<=p0)).

The existing C104 positive-semidefinite lcm kernel gives the corresponding bilinear bound E_s(v_i,v_j)<=K_minus (V_i V_j)^(t/2).
The EXACT normalized p-exponent marginal of the ORIGINAL ENERGY law

    nu(a,b)=w_a w_b/[E_s(w) lcm(a,b)^s]

is

    nu_p(i,j)=phi(p^i)phi(p^j)p^(-s max(i,j))
                           *E_s(v_i,v_j)/E_s(w).

Since E_s(w)>8*10^m0 W^t and phi(p^i)<=p^i, one obtains

    nu_p(i,j)<=10^(-1_(p<=p0))
                  *rho_p^|i-j|*mu_i^(t/2)*mu_j^(t/2).
                                                               (15)

Indeed substituting V_i=W mu_i/phi(p^i) leaves the factor phi(p^i)^(s/2)phi(p^j)^(s/2)p^(-s max(i,j)), which is at most p^(-s abs(i-j)/2).
Thus no unrecorded exponent normalization is used in(15).

The vector x_i=mu_i^(t/2), extended by0 to negative integers, has lq' norm1 because q'=2/t.
The source lemma applies at c=1/10 if p<=p0, contradicting c>=1/9.
Therefore the minimal counterexample contains NO prime<=p0, so its target constant in(14) is exactly8.

For each remaining p>p0 apply the lemma with c=1.
It gives a center k_p in Z such that the SAME energy law nu has bad-pair probability at most A_s p^(-t) for

    |v_p(a)-k_p|+|v_p(b)-k_p|>=2.

Use the union bound over the finite Q.
Equation(13) retains a set Omega of pairs with nu(Omega)>=1/2 and, for EVERY p in Q,

    |v_p(a)-k_p|+|v_p(b)-k_p|<=1.                    (16)

The set Omega is nonempty.
Since all actual exponents are nonnegative, (16) forces every k_p>=0; otherwise the sum at that prime would be at least2 for every pair.
Define the ACTUAL positive integer N=product_(p in Q)p^(k_p).

For an endpoint a of a pair in Omega put u(a)=a/gcd(a,N).
At each prime, (16) permits either two central exponents or exactly one exponent differing by1.
Consequently the following is an EXACT identity for every retained pair:

    lcm(a,b)=N*u(a)*u(b).                            (17)

In particular the two positive defects u(a),u(b) are coprime, and the negative defects cannot occur in both coordinates at one prime.
This arithmetic identity, rather than generic PSD concentration alone, is the next essential step.

Merge ALL endpoint weights by u and denote M_u=sum_(a endpoint,u(a)=u)w_a.
C121's exact fiber identity gives

    0<=M_u<=N phi(u), sum_u M_u<=W.                  (18)

No restriction of the original capacity to squarefree labels or unramified exponents has been imposed.
The endpoint subset is actual; off-center vertices that never occur in Omega are simply absent.
C114/C133's already proved packing estimate for0<=f_u<=phi(u) gives

    sum_u M_u/u^s<=2 N^(s/2)(sum_u M_u)^(1-s/2)
                    <=2 N^(s/2)W^(1-s/2).          (19)

Using(17), then dropping only a nonnegative pair restriction and applying(19), bounds the retained energy by

    E_s(w)/2 <=sum_((a,b) in Omega)w_a w_b/lcm(a,b)^s
       <=N^(-s)(sum_u M_u/u^s)^2
       <=4 W^(2-s).                                (20)

Thus E_s(w)<=8W^(2-s), contradicting the minimal counterexample.
This proves(14) using the exact source Lemma2.1, now accepted in GW21-U002.
The arithmetic fiber factor N is paid and cancels explicitly.
No original-law mass concentration is inferred from energy-law concentration, and none is needed for(18)--(20).

For a fixed s0 in(2/3,1), its uniform bound also gives every0<s<=s0 by the elementary concavity inequality under the original pair probability law:

    E_s(w)/W^2 <=[E_s0(w)/W^2]^(s/s0),
    E_s(w)<=K_s0^(s/s0)W^(2-s).                     (21)

For s>s0 use the same source argument directly at that fixed s.
With the exact source applicability now resolved, this gives the genuinely weak L1 capacity estimate for every0<s<1, without contradicting L396's false unrestricted strong norm or C96's critical linear short-pair bound.
The scalar moment coefficient K_s is finite but can be extremely large and is not claimed numerically known.

The new argument above is authored here.
The root supplied the broad tuple/weak-moment inquiry and has been notified of this candidate; it supplied no proof step.
The source reader will verify only the external statement/applicability and will not be treated as a project proof contributor on that basis.
Independent WHOLE review must reconstruct(12)--(21), especially the exact energy-law normalization and N-phi fiber cancellation, before any adoption.

<a id="general-capacity-capture-working-consequence"></a>
## 5. Consequence of the weak bound: original-window capture, with no tree hypothesis

Fix ANY0<s<1 and the uniform K_s supplied by Section4 using the accepted exact source interface.
The complete project proof remains subject to independent whole review.
No stopping-tree complexity is needed for the following implication.
Let the original finite real phi-capacity array have mass W>0 and integer X>=1.
Its ordered triple mass is T3_X=sum_(lcm(a,b,c)<=X)w_a w_b w_c, its density is delta3_X=T3_X/W^3, and its capture is H_X=max_(integer1<=n<=X)sum_(a|n)w_a.
For a pair let L=lcm(a,b).
When L>X its compatible third mass is0.
Otherwise partition third labels c by j=c/gcd(c,L).
Then lcm(a,b,c)=Lj, so each compatible bucket divides the ONE original integer Lj<=X and has total original mass at most H_X.
There are at most floor(X/L) buckets.
Consequently

    U_X(a,b)/W<=min(1,XH_X/(WL))
                       <=[XH_X/(WL)]^s.

This is precisely the retained C91/C133 residual-bucket interface, with all original labels and repeated coordinates.
Multiplying by original pair weights and summing, the weak moment gives

    T3_X<=K_s (XH_X)^s W^(3-2s),
    delta3_X<=K_s (XH_X/W^2)^s,
    H_X>=(delta/K_s)^(1/s)W^2/X
                 whenever delta3_X>=delta>0.          (22)

This conclusion itself does NOT assume X<=CW.
Under that additional original linear-window hypothesis it supplies H_X/W>=(delta/K_s)^(1/s)/C>0.
The maximum is attained at one actual integer n<=X.
No income or capture at different times is pooled.

The requested arity lift therefore holds with B=1.
Indeed every ordered four-tuple of original labels dividing that SAME n is compatible at X, and hence

    delta4_X >=(H_X/W)^4
       >=(delta/K_s)^(4/s)/C^4.                       (23)

One may take the minimum of the displayed constant and1 when stating a universal density parameter; if the raw lower bound exceeded1, the premises would simply describe an empty class.
This deduction from capture is NOT circular: (22) was proved from the independently derived weak moment, without assuming any arity-lifting or prior capture theorem.
Sections1--3 remain valid unconditional preliminary statements with their explicit larger time costs.

For an actual original monic irreducible nontorsion integer-unit P of degree d, let ell be a good prime and select COMPLETE residue-order groups of original mass W>=gamma d.
Assume ONLY integer1<=X<=Cd and fixed original triple density delta3_X>=delta>0.
L159 supplies the capacities, and(22) gives one n<=X with

    H_X>=(delta/K_s)^(1/s)gamma^2 d/C,
    log|D_n|>=v_ell(|D_n|)log ell
       >=(delta/K_s)^(1/s)(gamma^2/C)d log ell,        (24)
    D_n=Norm_(Q(alpha)/Q)(alpha^n-1)=Res(P,t^n-1).

Every original root and all deeper/exceptional valuations remain in the L74 floor.
Nontorsion makes the full norm nonzero.
The auxiliary t^n-1 has actual degree n<=Cd, content1 and coefficient squared norm2.
L168 therefore gives a STRICT positive Mahler bound with its exact original-degree and inherited source costs, using eta=(delta/K_s)^(1/s)gamma^2 log2/C.
No terminal omega, harmonic support, finite core, exponent restriction, scale-mass bound or enlarged time is needed for this conditional arithmetic consequence.

The actual good-prime mass/time/positive-triple-density hypotheses have NOT been established automatically for all hypothetical near-one inputs.
Even after independent project review and adoption of Section4, that arithmetic coverage remains a substantive unresolved G0001 obligation.
No abstract capacity array is asserted to be an irreducible nontorsion near-one polynomial.

<a id="weak-moment-source-resolved"></a>
## 6. Exact source resolved and final complete statement

2026-10-15T11:04.
The exact new source input is now ACTUALLY retained and accepted as [GW21-U002](../audits/literature/GW21/Yin_U002.md#gw21-u002).
The source-only f reader inspected the published PDF visually and reconstructed the COMPLETE Lemma2.1 proof; root registered the unit.
Its declared domain is exactly the one used in(12)--(16): fixed0<epsilon<1, q=2+epsilon, counting-measure lq' norms1, finite probability law,0<c<=1,0<lambda<=4/5.
Its conclusion is a tail outside the FIVE-POINT CROSS, not a single diagonal atom.
The unit accepts the fixed-epsilon constant and retains the proof-inspection limits for Proposition1.2 and the rest of the paper.
It supplies NO project phi-capacity mapping or global N for arbitrary arrays.

The author has read the actual unit and checked the local adaptation: in(15), x_i=mu_i^(t/2) really has counting-measure lq' norm1; nu_p is the exponent marginal of one finite energy probability law; c is1/10 or1; rho_p<=2^(-1/3)<4/5 because125<128; and epsilon=2/s-2 lies strictly in(0,1) for2/3<s<1.
The center may initially be in Z, but the NONEMPTY common good relation forces all its centers to be nonnegative, exactly as proved before defining N.
The source's unrelated minimal-counterexample proposition was not imported; the project established its own complete minimal-prime-pool induction.

Accordingly, the source-conditional status recorded in the history of Sections4--5 describes the actual earlier stage of this same derivation.
The needed source condition is now resolved at this exact accepted unit.
The project proof is author-complete and remains subject to a separately organized independent whole review; source acceptance alone is not project adoption.

<a id="general-weak-lcm-final-statement"></a>
<a id="statement"></a>
**Final theorem.**
For EVERY fixed0<s<1 there exists a finite positive K_s, depending only on s and the accepted fixed-parameter concentration constant, such that EVERY finite array of DISTINCT positive integers with arbitrary real0<=w_a<=phi(a) satisfies

    sum_(a,b) w_a w_b/lcm(a,b)^s
                  <=K_s (sum_a w_a)^(2-s).           (25)

Zero weights may be removed, and for total mass0 both sides are0.
There is no bound on the prime pool, prime-power exponents, number of labels, their order magnitudes, weights' denominators, product structure or any tree complexity.
This is the genuinely weak L1 capacity inequality, NOT the false unrestricted strong lq inequality.

One fully specified constant selection is the following.
Put sigma=max(s,4/5)<1 and let A_sigma>=1 be an admissible constant in GW21-U002 at epsilon=2/sigma-2.
Choose an integer p0>=2 with

    p0 >= [2A_sigma/(1-sigma)]^(1/(1-sigma)),
    K_sigma=8*10^pi(p0), K_s=K_sigma^(s/sigma).       (26)

The integral tail bound verifies(13) at sigma.
Sections4 and(21) then prove(25).
The intermediate sharper support-dependent factor(14) holds whenever2/3<s<1.
The source gives no numerical A_sigma, so no numerical value, sharpness or feasible computation of these large constants is claimed.

For the SAME original capacity law, integer X>=1 and positive ordered triple density delta3_X>=delta, its original divisor capture satisfies(22).
Therefore, if X<=CW,

    H_X/W >= (delta/K_s)^(1/s)/C,
    delta4_X >= min{1,(delta/K_s)^(4/s)/C^4}.         (27)

Thus the original triple-to-four-coordinate question has a positive author-complete answer with B=1.
Fixing s=4/5 makes the displayed parameter depend only on C,delta and the ONE fixed source constant.
Repeated labels and all original ineligible mass are retained.
More generally every fixed k>=1 has delta_k(X)>=(H_X/W)^k, by sampling the labels dividing the same maximizing integer.
This is a consequence of the newly proved moment/capture argument, not a circular assumption used to establish it.

For actual original-polynomial inputs, the exact positive-income statement is(24), with no additional tree or harmonic hypotheses.
The auxiliary, signed norm, original root counts, possible powered-degree drop, prime and full time costs are unchanged from that displayed argument.
Explicitly define the original full budget by U_C(P)=max_(1<=n<=floor(Cd)) log|D_n|/d, using exactly the norm in(24); the asserted range1<=X<=Cd makes this finite maximum nonempty.
L168 proves that this budget tends uniformly to0 as m(P) tends to0.
Since H_X log ell<=d U_C(P), the same local floor and(22) give the finite necessary bound

    delta3_X<=K_s [C U_C(P)/(gamma^2 log ell)]^s       (28)

whenever W>=gamma d and1<=X<=Cd.
This also covers U_C=0: then H_X=0 and delta3_X=0.
For each PREASSIGNED fixed C>0, gamma>0 and0<s<1, along any hypothetical sequence of original inputs with m(P) tending to0, the corresponding fixed-C budget U_C(P) tends to0.
Formula(28) therefore forces the original triple density to tend to0 uniformly over all complete selections with W>=gamma*d, all nonempty integer windows1<=X<=C*d and all good primes ell, using log ell>=log2.
This asymptotic conclusion does not allow C to grow, gamma to tend to0 or s to vary along the sequence; no uniform estimate in those moving parameters is asserted.
No assumption that such selections have positive density is manufactured.
The remaining unrestricted task is the ACTUAL arithmetic coverage problem, not this now author-complete abstract capacity implication.

<a id="weak-moment-self-check-and-dependencies"></a>
## 7. Author verification, precise dependencies and scope preservation

The central proof uses only the following exact fixed inputs: [GW21-U002's finite probability concentration](../audits/literature/GW21/Yin_U002.md#gw21-u002); [C104's finite PSD lcm kernel and Gram Cauchy inequality](Yin_C_G0104_v1.md#finite-product-envelope-extension); [C121v2's exact merged residual fiber capacity](Yin_C_G0121_v2.md#exact-merged-residual-capacity); and [C133's real-capacity inverse-moment packing](Yin_C_G0133_v1.md#argument), equation9 with its V<1 and V0 branches.
These inputs are used only at their stated elementary or source scopes.
C133's harmonic-core operator theorem is not an additional premise of(25).

For clarity, the packing used in(19) has f_u=M_u/N<=phi(u) and mass V=(sum M_u)/N.
If0<V<1 then sum f_u/u^s<=V<=V^(1-s/2).
If V>=1, splitting at sqrt(V) bounds the lower part by sum_(u<=sqrt(V))u^(1-s)<=V^(1-s/2) and the upper by V*(sqrt(V))^(-s).
Thus the factor2 and N^(s/2) are valid even when a normalized fiber mass is fractional or below1.
This is the already retained packing proof, displayed to make its exact new use reviewable.

The author checked the complete minimum-counterexample logic on arbitrary finite REAL arrays.
Prime support means primes in POSITIVE-WEIGHT ORDER LABELS; dividing weights by phi(p^i) introduces no new order primes.
Each nonzero slice really has smaller prime support and remains within its real phi-capacity box, including i0 with phi(1)=1.
The p-free Gram Cauchy bound is applied to the finite UNION of the two slice supports.
Zero slices have zero energy blocks and zero x_i.
The prime-free case W<=1 closes the induction without an integer lower bound on weights.

The SAME original energy law is used for all prime marginals, so the finite union bound is valid.
No independence of primes or equality between energy and original mass laws is asserted.
The large-prime tail bound leaves at least half the energy, not half the vertex mass.
Every center is nonnegative because a negative center would violate(16) for every nonnegative-exponent pair.
At each prime the five-point-cross condition, including its negative one-step deviations, yields(17); omitting those negative deviations or replacing the conclusion by single-atom concentration would change the proof.
After that exact identity is established ONLY on Omega, the factorized NONNEGATIVE expression may be enlarged to all pairs of its actual endpoints.
The kernel identity is not asserted for those added pairs.
Their phi capacities and the exact fiber equality supply(18); no arbitrary operator vector is treated as a saturated capacity array.
The remaining N factors in(19)--(20) cancel exactly.

The preliminary gluing/polylogarithmic proofs(1)--(11) retain their independently valid interfaces to [C101](Yin_C_G0101_v1.md#statement) and [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001).
They are preserved as the useful route before the later stronger deduction, not as the source of the uniform moment proof.
C119/C124/C138 motivate the arity question and are not needed to prove(25)--(28).
The source reader contributes the external theorem inspection only; the present author's adaptation supplied the actual probability law, induction constants, all arithmetic fibers and consequences.
Root supplied the inquiry and source registration, not these proof steps.

The actual-polynomial consequences additionally use [L159 complete good-prime capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity), [C256 full original local norm](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail), [L168 finite income](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) and [uniform original-budget decay](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape), with their inherited accepted source and degree-escape limits.
The C91/C133 third-coordinate bucket proof is reproduced in Section5.
It counts one original time per bucket and eventually takes one finite maximum; it never aggregates distinct norm incomes.

The new weak constant is not the SHARP product-profile constant of C104, so C105's proper-divisor strict improvement over that product constant remains valid.
The estimate has exponent2-s and keeps real phi capacities, so it does not imply C96's refuted linear P2(Y)<=KYW bound, nor repair L396's false unrestricted strong norm.
C108's local unrestricted-Cauchy loss is bypassed by the new energy-law concentration AND the arithmetic fiber identity, not by multiplying nonsummable local suprema or assuming an unproved scalar stability.
These precise former failures remain useful and are not withdrawn.

No native mathematical program, numerical prime cutoff, extremizer search, unregistered J, global source modification or actual near-one construction was performed.
The constants are deliberately qualitative and can be enormous.
Independent project review and responsible Claim adoption are still pending.
Even after such adoption, a positive good-prime original-density certificate for every sufficiently small-measure polynomial is a separate unproved arithmetic assertion; nothing here supplies it.

<a id="author-freeze-2026-10-15"></a>
## 8. Complete author freeze and review handoff

2026-10-15T11:12.
The author freezes this ENTIRE draft, Sections1--8 and equations(1)--(28), after the complete checks recorded above.
The retained statement anchor is [#statement](#statement), with the final weak moment(25)--(26), original-window capture and arity consequence(22)--(23)/(27), actual original-polynomial income(24), and finite/near-one budget consequence(28).
The argument anchor is [#argument](#argument), beginning with the complete earlier gluing and polylogarithmic deductions rather than omitting them.
The decisive new weak-moment proof is Section4; its exact accepted source and full final scope are Sections6--7.

The opening source-conditional and fixed-window-open stages are preserved as explicitly historical development; they are not current unresolved source conditions.
At freeze the author regards the project argument as complete but has NOT conducted or claimed an independent review.
Root's reading and source registration do not constitute such a review or a contribution to this adaptation.
The separate source-only reader checked GW21-U002 and did not supply this proof's phi-capacity mapping, minimum-counterexample induction, arithmetic fiber cancellation or original-window consequences.
Formal independent whole review must inspect the actual retained fixed artifact.
The unrestricted actual-polynomial positive-density coverage problem remains open.


<a id="weak-moment-v2-asymptotic-quantifiers"></a>
## Actual v2 asymptotic-quantifier clarification

2026-10-15T11:16.
Preserve physical v1 and the actual whole reviewer's observation that the finite inequalities and general weak/capture proof pass, but the final near-one sentence should explicitly fix all parameters needed by its limiting input.
Root now writes C>0, gamma>0 and s in(0,1) as preassigned fixed parameters, and states precisely that uniformity is over original complete selections, actual bounded windows and good primes.
The conclusion is not asserted for C growing, gamma tending to0 or varying s.
Equations(1)--(28), all finite statements, proof steps and constants are unchanged.
This explicit quantifier repair is root's contribution to the v2 wording; root did not supply the new weak-moment adaptation.
Actual independent inspection of this physical version remains required before adoption.
Neither the general capacity theorem nor this fixed-parameter necessary condition supplies automatic actual positive-density coverage.

## Fixed organization

Retain the complete frozen author original: all preliminary gluing and polylogarithmic consequences, the new general weak fractional moment and its exact probability/arithmetic proof, every original-window and full-norm consequence, all28 formulas, explicit source resolution and former-stage boundaries, source/contribution limits and self-check.
Root supplied direction and source organization but no new project proof step.
The general original arithmetic coverage obligation remains open.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:16 |
| status | open |
| reason | Retain the complete general weak moment and original-window consequences, with final near-one uniformity explicitly at fixed C,gamma,s; preserve v1 and the actual scope observation for whole-v2 review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Final complete theorem](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Entire proof](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Exact input](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Exact input](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Exact input](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Exact input](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Exact input](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Exact input](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:25 |
| status | proved |
| reason | Adopt actual R497 whole-v2 review. The general finite real phi-capacity weak fractional moment and original-window positive-triple-density capture are proved without support or tree complexity assumptions; arity lifting has B=1. Complete original norm and fixed-C,gamma,s density-budget consequences hold. Actual automatic positive-density polynomial coverage and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Final complete theorem](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Entire proof](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Exact input](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Exact input](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Exact input](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Exact input](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Exact input](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Exact input](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Exact input](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Exact input](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Exact input](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |
| review | [Actual whole-v2 finding](../audits/reviews/Yin_R_G0804_v1.md#general-weak-v2-whole-independent-finding) | Complete actual28-equation proof, all preliminary results and direct interfaces, source-only contribution distinction, energy/fiber cost restoration and fixed-parameter limit; original v1 scope observation retained. |

### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Argument](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Dependency](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Dependency](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Dependency](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Dependency](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Dependency](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |
| review | [Review](../audits/reviews/Yin_R_G0804_v1.md#general-weak-v2-whole-independent-finding) | Complete actual28-equation proof, all preliminary results and direct interfaces, source-only contribution distinction, energy/fiber cost restoration and fixed-parameter limit; original v1 scope observation retained. |

### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:28 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Exact retained argument](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Exact retained dependency](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Exact retained dependency](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Exact retained dependency](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0804_v1.md#general-weak-v2-whole-independent-finding) | Complete actual28-equation proof, all preliminary results and direct interfaces, source-only contribution distinction, energy/fiber cost restoration and fixed-parameter limit; original v1 scope observation retained. |

### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Exact retained argument](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Exact retained dependency](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Exact retained dependency](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Exact retained dependency](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0804_v1.md#general-weak-v2-whole-independent-finding) | Complete actual28-equation proof, all preliminary results and direct interfaces, source-only contribution distinction, energy/fiber cost restoration and fixed-parameter limit; original v1 scope observation retained. |

### Decision isolated-current-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T01:10 |
| status | proved |
| reason | Adopt the actual new isolated whole review of complete physical v2, all preliminary and final equations1--28, exact real-capacity/source interfaces and fixed C,gamma,s asymptotic scope. The earlier v1 scope observation and original UNKNOWN reviews remain at their actual historical inputs and relationships. This new acceptance adds independent evidence for the unchanged theorem; actual polynomial coverage and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | General weak moment for every fixed0<s<1, every finite real phi-capacity array, all original-window/density/norm/budget consequences, with the preliminary statements retained. |
| argument | [Exact retained argument](#argument) | Sections1--8 and all28 equations, complete old and new mechanisms, minimal-prime-pool proof, finite energy law, exact fibers and every cost/boundary. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U002.md#gw21-u002) | Exact finite probability concentration lemma at fixed open epsilon range; complete selected source-proof inspection and global-proposition boundary. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Finite PSD lcm kernel and its bilinear Gram Cauchy bound for the actual slice union. |
| dependency | [Exact retained dependency](Yin_C_G0121_v2.md#exact-merged-residual-capacity) | Exact sum of original totient capacities over a/gcd(a,N)=u, retaining the full N factor. |
| dependency | [Exact retained dependency](Yin_C_G0133_v1.md#argument) | Equation9 scalar inverse-moment packing for real phi capacities and small/zero mass; no harmonic-core theorem needed for the new general bound. |
| dependency | [Exact retained dependency](Yin_C_G0101_v1.md#statement) | Preliminary Sections2--3 only: full original-law weighted dyadic short-pair bound and actual scale-mass expense. |
| dependency | [Exact retained dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Preliminary fixed-epsilon C101 source constant at its existing Theorem1.1 statement/applicability scope. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original reduced-root group capacities. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | One actual time and full original local norm floor, all roots and depths. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Finite positive original norm income gives the strict conditional Mahler bound. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-budget decay and actual powered-degree limits for the quantitative density consequence. |
| review | [Actual complete isolated whole finding](../audits/reviews/Yin_R_G0802_v1.md#g0142v2-isolated-whole-finding) | Complete exact statement and entire mathematical account, including all preliminary results, direct interfaces, costs, exceptional branches and current source/reuse boundaries; independently reviewed in the actual isolated arrangement recorded by R802. |
