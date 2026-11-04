---
author: Yin
---
# Averaged capacity and positive-density localization beyond row bounds

Date: 2026-10-14T20:30.
Human author Yin.
Root assigned the positive averaged-pair/triple-density direction after the fixed-efficiency row obstruction D34; it has not supplied a proof step for this new round.

## Responsible question

Seek a genuinely positive mass-averaged short-lcm or triple-density capture estimate beyond the efficiency-eight row boundary, with fixed efficiency K>8 or without an efficiency restriction.
A possible useful result is a uniform constant depending on bounded individual prime support, a weaker fractional estimate that retains paid costs, or direct positive-density localization.
Re-proving row failure and merely adding a finite test are not the main objectives.
Preserve full original weights, repeated-label triples, full degree/norm income costs and any truly failed mechanism.
Substantive programs require a separate declared J before execution.

## Reuse screen and active ownership

The g_bridge_audit AI authors this round.
It authored C104/C105/C108/C111 and contributed D34, so those are dependencies rather than independent evidence.
The author has read the relevant retained interfaces: C96 refutes the unrestricted LINEAR averaged-pair bound; C99 treats exactly full squarefree threshold ideals and establishes their triple-density capture; C101 and L396 retain the unrestricted d/log d capture estimate, the actual scale-mass cost and failure of the stronger norm shortcut; C102/C106 give the individual support2/3 row and actual income results.
C103/C107/C110 concern distinct coefficient-Gram arithmetic rather than this capacity average.
C104/C105/C108/C111 distinguish multiplicative weak moments, exact full-ideal reduction, nested no-gap examples and the remaining near-global arithmetic inverse.
D34 now refutes all uniform-prime-base row extensions at fixed efficiencyK>8, while its normalized triple density tends to zero.

A bounded fresh local screen and primary-source web search looked for bounded-prime-support gcd/lcm average estimates.
A Reading-hosted Gal-type GCD-sum paper was located as a possible comparison; no new theorem from it has been adopted and the previously recorded stronger-kernel counterexample remains in force.
Search failures establish no novelty or absence claim.
Develop every new deduction and useful failed attempt below.

<a id="averaged-heavy-prime-discovery"></a>
## Change of mechanism and source boundary

The initial attempt to bound each oriented row is abandoned at the exact C112 boundary.
The following positive argument instead discards a controlled probability of PAIRS sharing an infrequent prime and proves a fractional estimate only on the remaining pairs.
The probability law throughout is the ORIGINAL mass law w_a/W.
It is never renormalized after pairs are removed, and the density lost is explicitly paid.
Heavy primes refer to mass incidence, not size of the primes.

The author rechecked C104's exact lcm kernel, C105/C111's extremal-domain limits and C108's nested Cauchy obstruction.
None supplies the new truncation.
The complete finite inverse-moment packing, core-kernel row-sum calculation and probability estimate are given below.
They use elementary sums, 2xy<=x^2+y^2, geometric series and the union bound; no new external theorem or matrix spectral estimate is imported.
A fresh reading of Gou's arXiv2604.21122v1, Theorem1.5 and §3.3, confirmed that its direct high-dimensional counting retains a scale-epsilon/divisor loss; it is a comparison only, not a mathematical input.
The old GW21/C101 theorem is also not a premise of this new proof.
All actual norm deductions reuse only the already accepted L159/L74/L168 interfaces and C106's elementary efficiency support inequality.

## Statement

Let S be a finite nonempty set of positive integers and attach arbitrary REAL capacities0<w_a<=phi(a).
Put

    W=sum_a w_a>0,
    mu(a)=w_a/W,
    pi_p=sum_(a:p|a)mu(a),
    R_mu=sum_p pi_p=sum_a mu(a) omega(a).                (1)

The sum over primes is finite.
It is the MASS-WEIGHTED MEAN number of distinct prime factors, not the number of primes in their union or the largest individual support.
Define all ordered repeated-label statistics by

    P_2(Y)=sum_(a,b:lcm(a,b)<=Y)w_a w_b,
    h(n)=sum_(a:a|n)w_a,
    H_X=max_(integers1<=n<=X)h(n),
    T_X=sum_(a,b,c:lcm(a,b,c)<=X)w_a w_b w_c.            (2)

Here Y>0 is real and X>=1 is integer.
Orders above X remain in W; they simply do not contribute compatible triples.

**A. A positive averaged estimate for ANY prescribed finite prime core.**
Fix0<s<1 and ANY finite set Q of primes, and let

    B_s=(1+2^(-s/2))/(1-2^(-s/2))>1.

On the ORIGINAL law, let beta_Q be the probability that two independent labels share a prime outside Q.
Then beta_Q<=sum_(p outside Q)pi_p^2.
The remaining good pairs have

    E_s^good:=sum_(a,b:gcd(a_(Q-free),b_(Q-free))=1)
                         w_a w_b/lcm(a,b)^s
               <=4 B_s^|Q| W^(2-s).                   (3)

Consequently, for EVERY Y>0 and integer X>=1,

    P_2(Y)/W^2 <= beta_Q+4 B_s^|Q| (Y/W)^s
    T_X/W^3 <= beta_Q+4 B_s^|Q| (X H_X/W^2)^s.          (4)

In both inequalities B_s^|Q| may be replaced by the sharper product B(Q,s) in(11).
In particular, if T_X>=delta W^3 and beta_Q<delta, then

    H_X>=[(delta-beta_Q)/(4B(Q,s))]^(1/s) W^2/X.        (4a)

A uniform bound B(Q,s)<=B0 and a fixed positive gap delta-beta_Q>=lambda give the positive uniform capture constant[lambda/(4B0)]^(1/s), even without a bounded mean omega or a bounded cardinality of Q.
The condition |Q|<=J is one sufficient special case, with B0=B_s^J.
The stronger sufficient overlap condition sum_(p outside Q)pi_p^2<=delta-lambda is also available.
None of these core-cost or small-tail hypotheses is inferred automatically from positive density.

The heavy-prime choice Q={p:pi_p>=epsilon},0<epsilon<=1, is a useful specialization: |Q|<=R_mu/epsilon and beta_Q<=epsilon R_mu.
It gives the explicit averaged bound epsilon R_mu+4B_s^(R_mu/epsilon)(Y/W)^s in place of the right side of the first inequality(4).
The beta_Q term is essential.
This is NOT the false unrestricted linear averaged-pair estimate and does not assert a full-kernel fractional moment bound without a pair truncation.

**B. Positive triple-density capture from bounded MEAN prime support.**
Suppose0<delta<=1, T_X>=delta W^3 and R_mu<=R for a fixed real R>=1.
Put

    M=ceil(2R^2/delta),
    c(s,R,delta)=[delta/(8 B_s^M)]^(1/s)>0.

Then

    H_X>=c(s,R,delta) W^2/X.                            (5)

In particular X<=C W with fixed C>0 implies H_X/W>=c(s,R,delta)/C.
There is no restriction on the union of order primes, their sizes, prime-power exponents, or individual support beyond the displayed MEAN bound.
A finite upper bound on every omega(a) is sufficient but not necessary.
The case R_mu=0 is separately trivial: only label1 can have positive mass, and H_X=W,T_X=W^3 for every X>=1.

**C. Actual same-time arithmetic income.**
Let P be ACTUAL monic irreducible nontorsion in Z[t], with constant coefficient+/-1, ORIGINAL degree d and a GOOD prime ell not dividing its polynomial discriminant.
Select COMPLETE occurring residue-order groups, with their full original-root counts w_o and W>=gamma d for fixed0<gamma<=1.
Suppose an integer1<=X<=C d has T_X>=delta W^3 and the same selected original-mass law has R_mu<=R, with fixed C>0,0<delta<=1,R>=1.
Then one integer n<=X has full original local income at least

    A_ell(n)>=eta d,
    eta=c(s,R,delta) gamma^2 log(2)/C>0.                (6)

The accepted L168 finite criterion gives STRICT total m(P)>m0(C,eta)>0.
Every original root, full norm, unselected group and higher/exceptional depth is retained; the auxiliary is the actual t^n-1 at full degree n, content1 and squared coefficient norm2.

The widest proved core-cost version replaces the bounded-mean premise by the existence, for each actual input, of a finite Q with B(Q,s)<=B0 and beta_Q<=delta-lambda, where s,B0 and lambda>0 are fixed.
It replaces c(s,R,delta) in(6) by[lambda/(4B0)]^(1/s).
No uniform cardinality bound on these finite Q is necessary.
This is an explicitly assumed paid-core certificate, not automatic coverage.

In particular any fixed pointwise efficiency cap o/ord_o(ell)<=K is sufficient to bound R_mu, so this supplies a positive density-to-income theorem for EVERY fixed finite K, including K>8 where C112 rules out the whole-row method.
The actual coverage, good-prime selection and positive-density assumptions remain independent hypotheses; their existence near one is not inferred.
Under fixed actual gamma,delta,C, any hypothetical sequence with m(P)->0 and such density certificates must have R_mu->infinity.

**D. Escape beyond EVERY fixed complexity or efficiency threshold.**
Under that same hypothetical near-one sequence and fixed actual gamma,delta,C, put

    e_delta=1-(1-delta)^(1/3)>0.

For EVERY fixed integer J>=0 and EVERY fixed finite real K>=1,

    liminf mu{omega(o)>J}>=e_delta,
    liminf mu{e_ell(o)>K}>=e_delta.                     (18)

All laws and base primes here are those of the corresponding original selected arrays.
Consequently the mass-weighted means of omega(o), log e_ell(o) and e_ell(o) all tend to infinity.
When delta=1, (18) says the whole selected mass escapes every fixed threshold.
For0<delta<1 it proves the stated positive fraction e_delta, not full-mass escape.
The exact finite truncation loss and its original-norm transfer are proved in §7.

There is also a more direct necessary collision condition: for EVERY fixed integer J>=0, along that hypothetical sequence,

    liminf min_(Q finite, |Q|<=J) beta_Q >=delta.        (18a)

The minimum uses the actual array's original law and may choose a different Q for each input.
This is an escape from every bounded prime core; it does not assert automatic arithmetic realization of such arrays.

## Argument

<a id="original-law-heavy-prime-truncation"></a>
### 1. Original mass incidence and the exact bad-pair expense

For each prime p, pi_p is its incidence probability under mu.
Finite double counting gives(1): each label contributes once for every DISTINCT prime dividing it.
For the heavy-prime specialization Q={p:pi_p>=epsilon}, this gives

    epsilon |Q|<=sum_(p in Q)pi_p<=R_mu.

For two independently sampled labels A,B under the same original law, independence gives P(p|A and p|B)=pi_p^2.
For ANY finite Q, if their Q-free parts share a prime, at least one p outside Q divides both.
Thus the union-bound estimate beta_Q<=sum_(p outside Q)pi_p^2 is valid without a threshold assumption.
Specializing to heavy Q gives

    beta_Q<=sum_(p outside Q)pi_p^2
             <=epsilon sum_(p outside Q)pi_p
             <=epsilon R_mu.                           (7)

Using a weak inequality is harmless although the individual outside threshold is strict.
Repeated labels are included in this event, just as required by the original statistics.
No selection of one representative per order, conditioning or deletion/renormalization of root mass is made.

The contribution to T_X from bad first-two-coordinate pairs is at most beta_Q W^3, because the third-coordinate mass is at most W.
This pays the loss for every compatible triple in that class, including all diagonal and repeated-label cases.
One fixed pair position suffices; there is no uncharged assumption that every pair of a retained triple is good.

<a id="capacity-inverse-moment-packing"></a>
### 2. A direct capacity inverse-moment estimate

Let finitely many real numbers f_u satisfy0<=f_u<=phi(u)<=u, with total V=sum_u f_u.
For0<s<1 put r=1-s/2.
Then

    sum_u f_u/u^s<=2 V^r,                              (8)

with both sides zero when V=0.
If0<V<1, the left side is at most V<=V^r.
If V>=1, set Z=sqrt(V)>=1.
For u<=Z, use f_u<=u and the crude finite estimate

    sum_(u<=Z)u^(1-s)<=floor(Z) Z^(1-s)<=Z^(2-s).

For u>Z, use u^(-s)<=Z^(-s) and sum f_u<=V.
Adding gives at most Z^(2-s)+VZ^(-s)=2V^r.
Thus(8) holds for arbitrary real capacities and finite supports, including u1 and any omitted prime restrictions.
No distributional packing optimum or rounding theorem is needed.

<a id="good-pair-core-fractional-estimate"></a>
### 3. The finite heavy core and the good-pair fractional bound

Take ANY finite Q; no incidence threshold is needed in this section.
Write each label uniquely as a=g u, where all prime factors of g lie in Q and u has none in Q.
Then gcd(g,u)=1 and phi(a)=phi(g)phi(u).
Group the ORIGINAL masses by their exact Q-core:

    W_g=sum_u w_(gu),
    A_g=sum_u w_(gu)/u^s.

Missing labels have weight0, all sums are finite, and sum_g W_g=W.
For each fixed g the scaled capacities f_u=w_(gu)/phi(g) satisfy0<=f_u<=phi(u).
Applying(8) gives

    A_g<=2 phi(g)^(s/2) W_g^(1-s/2).                  (9)

This scaling is the full exact factor phi(g); no core mass is removed for free.
In the residual integer orders below, the factors u are only auxiliary summation variables and do not replace the actual original-root counts.

For a good pair a=g u,b=h v, the external parts u,v are coprime, and both are coprime to every prime in g,h.
Hence

    lcm(a,b)=lcm(g,h) u v.

Dropping the coprimality restriction only AFTER replacing the good-pair denominator by this exact product enlarges the sum, because every summand is nonnegative.
It follows that

    E_s^good<=sum_(g,h) A_g A_h/lcm(g,h)^s
      <=4 sum_(g,h) K_Q(g,h) W_g^r W_h^r,

where

    K_Q(g,h)=[phi(g)phi(h)]^(s/2)/lcm(g,h)^s
      <=(gh)^(s/2)/lcm(g,h)^s
      =product_(p in Q) p^(-s|v_p(g)-v_p(h)|/2).       (10)

The last equality follows prime by prime from max(e,f)-(e+f)/2=|e-f|/2.
All Q-smooth positive integers correspond to exponent vectors in Z_(>=0)^|Q|.
For any fixed vector e, the sum of the upper kernel in(10) over every nonnegative vector f is at most

    B(Q,s):=product_(p in Q)[(1+p^(-s/2))/(1-p^(-s/2))]
                  <=B_s^|Q|.                          (11)

Indeed each one-dimensional row is bounded by the two-sided convergent geometric series sum_(j in Z)p^(-s|j|/2).
This verifies convergence uniformly in every exponent and includes p2.
If Q is empty, there is just the core g1, and the empty product B(Q,s)=1.

For z_g=W_g^r>=0, symmetry and2z_g z_h<=z_g^2+z_h^2 imply directly

    sum_(g,h) K_Q(g,h)z_g z_h
       <=B(Q,s) sum_g z_g^2
       =B(Q,s) sum_g W_g^(2-s)
       <=B(Q,s) W^(2-s).                              (12)

The finite support justifies every rearrangement.
The last inequality uses2-s>1 and positivity, not a false strong-norm interpolation.
Equations(9)–(12) prove(3), even with the slightly better constant4B(Q,s).
The divergent-prime issue has been confined to the finite, paid set Q.

<a id="averaged-small-lcm-and-residual-transfer"></a>
### 4. Averaged pairs and full repeated-label triples

For a good pair with lcm(a,b)<=Y, one has1<=Y^s/lcm(a,b)^s.
The total good short-pair mass is therefore at most Y^s E_s^good.
The bad-pair mass is at most beta_Q W^2 regardless of Y.
This proves the first part of(4), including Y<1 where the actual short-pair sum is zero.

For triples use the EXACT accepted residual-bucket argument, restated to expose all masses and the time budget.
For any a,b, let L=lcm(a,b).
If L>X the compatible-third mass U_X(a,b) is zero.
If L<=X, partition its compatible third orders c by

    j(c)=c/gcd(c,L), 1<=j(c)<=floor(X/L).

Every order in a fixed bucket divides the ONE integer n=L j<=X, since lcm(L,c)=L j.
The total original mass of that bucket is thus at most H_X.
It follows that

    U_X(a,b)<=min(W, X H_X/L),
    U_X(a,b)/W<=min(1,X H_X/(W L))
                      <=[X H_X/(W L)]^s.               (13)

The last inequality holds for all nonnegative arguments because0<s<1.
No capacity assumption is needed for the bucket step itself, and no floor is replaced by an equality.
The auxiliary quotient j(c) labels a bucket only; the bucket keeps every original c and its full w_c.

Summing bad pairs costs beta_Q W^3 by §1.
Applying(13) to good pairs and then(3) gives

    T_X/W^3
      <=beta_Q+(XH_X/W)^s E_s^good/W^2
      <=beta_Q+4B(Q,s)(XH_X/W^2)^s,                    (14)

which is the second part of(4).
Both sides remain meaningful if H_X=0: then no eligible positive label exists, so T_X=0; positive density cannot hold in that case.
No division by H_X has occurred.

<a id="bounded-mean-prime-support-capture"></a>
### 5. An explicit positive capture constant

For an arbitrary prescribed Q with beta_Q<delta, equation(14) immediately gives(4a), since its positive gap can be divided by4B(Q,s) and raised to the power1/s.
A fixed gap lambda and B(Q,s)<=B0 yield the constant[lambda/(4B0)]^(1/s).
The sufficient cardinality bound |Q|<=J yields B0=B_s^J.
This is the wider direct interface.

Now assume additionally R_mu<=R with R>=1.
Choose epsilon=delta/(2R), which lies in(0,1].
Then(7) gives beta_Q<=delta/2 and

    |Q|<=R_mu/epsilon<=2R^2/delta<=M.

Equation(14) therefore yields

    delta/2<=4 B_s^M (XH_X/W^2)^s.

Rearrangement is legitimate because every displayed fixed factor is positive; it gives(5).
The maximum H_X is attained on a finite nonempty integer range, so this is an actual one-time capture, not an average over different times.
If the resulting lower bound would exceed W, the chosen hypotheses simply cannot all hold; no separate assumption X>=W is introduced.

For example choose s=1/2 once and for all.
With

    B=(1+2^(-1/4))/(1-2^(-1/4)),

the entirely explicit safe constant is

    c(1/2,R,delta)=delta^2/[64 B^(2 ceil(2R^2/delta))].  (15)

It is small but strictly positive and independent of W,X, all prime sizes, all exponents and the number of occurring groups.
No claimed optimization of this constant is needed.

The cases omitted by the probability notation are elementary.
Zero weights may be removed.
If all weights are zero, W=H_X=T_X=P_2(Y)=0; there is no positive-mass probability law or nontrivial capture assertion.
If W>0 and R_mu=0, positive weights can occur only at order1, so H_X=W,T_X=W^3 for X>=1.
Statement B may either use this direct conclusion or any allowed R>=1.
All good/bad calculations also work with Q empty.

<a id="actual-bounded-mean-support-income"></a>
### 6. Actual original-norm income and fixed efficiency

For the actual inputs of Statement C, the accepted [L159 good-prime Frobenius/capacity interface](../ledger/Yin_L_G0159_v1.md#frobenius-inversion-capacity) gives positive integer COMPLETE group counts w_o<=phi(o).
Their sum is the actual selected original-root count W, even if some original groups are not selected.
Apply(5) with exactly these counts.
Since W>=gamma d and X<=C d, there is a single integer n<=X with

    h(n)>=c(s,R,delta) gamma^2 d/C.

Write the ACTUAL original norm as

    D_n=Norm_(Q(alpha)/Q)(alpha^n-1)
       =Res(P,t^n-1)=product_(all d original roots)(alpha_i^n-1),
    C_n=|D_n| in Z_(>0),
    A_ell(n)=(log ell)v_ell(C_n).

Nontorsion irreducibility makes D_n nonzero.
At the good prime ell, every captured original root has actual normalized valuation at least1, and every other original-root contribution is nonnegative.
Therefore the accepted [C256 original-norm inequality](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) is

    A_ell(n)>=h(n)log ell>=h(n)log2>=eta d,

with eta in(6).
This is a LOWER floor for the complete local income.
All higher, initial and exceptional depths, including ell2 cases, remain on the left; no equality at depth1 or proper selected subnorm is asserted.
The auxiliary t^n-1 has full degree n<=C d, content1 and squared coefficient norm2.
Thus the existing [L168 finite norm-tower/degree-escape criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) applies with those exact C,eta and yields strict m(P)>m0(C,eta)>0.
No new proof of its external discrepancy input is claimed.

[C106's elementary order-divisibility calculation](Yin_C_G0106_v1.md#three-prime-density-and-efficiency) gives, for every positive order o coprime to ell, a safe uniform relation

    omega(o)<=1+log_2(e_ell(o)),
    e_ell(o)=o/ord_o(ell)>=1,                           (16)

with order1 interpreted as omega(1)=0,e_ell(1)=1.
For o>1 its stronger strict form follows from the cyclic odd-prime-power factors and the actual2-primary case; the inequality written here is sufficient.
Hence a pointwise cap e_ell(o)<=K bounds R_mu by1+log_2 K.
One may use R=max(1,1+log_2 K) in(5)–(6).
This proves the asserted positive class at arbitrary fixed finite K, without trying to revive the false C112 row extension.

More generally, a bounded MASS-WEIGHTED MEAN efficiency is sufficient: if sum_o mu(o)e_ell(o)<=K, concavity of log gives

    R_mu<=1+sum_o mu(o)log_2 e_ell(o)<=1+log_2 K.        (17)

Thus the theorem permits even unbounded individual efficiencies when their mean under the same original selected-mass law is uniformly bounded.
This does not assert that such a mean bound holds for arbitrary actual polynomials or follows from small Mahler measure.

Finally, along any hypothetical sequence with m(P)->0 and fixed actual gamma,delta,C satisfying the same coverage/density assumptions, R_mu must tend to infinity.
Otherwise an infinite subsequence would have R_mu<=R for some fixed finite R, contradicting the same positive m0(C,eta).
Equation(16) also forces the mean log efficiency, and hence the mean efficiency, to diverge.
No existence of that sequence or of its coverage certificates is supplied.

Exactly the same actual-norm argument applies under the more general finite-core hypothesis B(Q,s)<=B0 and beta_Q<=delta-lambda, with fixed B0>=1 and lambda>0: replace c(s,R,delta) by[lambda/(4B0)]^(1/s).
The chosen finite Q, its cardinality and prime sizes may vary with the input; only this ACTUAL product cost and the ORIGINAL-law overlap gap are uniformly bounded.
The condition |Q|<=J is the sufficient special case B0=B_s^J.
There is no assumption about the norm of a divided-core polynomial, because no such polynomial is introduced.

<a id="all-fixed-threshold-mass-escape"></a>
### 7. Exact finite truncation and escape beyond every fixed threshold

Take any subinventory S_low formed by retaining COMPLETE groups according to a specified order condition.
Let its mass be V=nu W,0<=nu<=1.
The full mass of ordered triples that have at least one discarded coordinate is exactly W^3-V^3 before compatibility is imposed.
Thus its surviving compatible triple mass obeys

    T_low>=T_X-(W^3-V^3)
            >=[delta-1+nu^3]W^3.                     (19)

This is the same elementary complete-group deletion mechanism used in C106, now applied at an arbitrary threshold; no independence of compatibility events is assumed.
Put kappa=delta-1+nu^3.
If kappa>0, then V>0 and

    T_low/V^3>=delta_low:=kappa/nu^3 in(0,1].

For S_low={o:omega(o)<=J}, J a fixed nonnegative integer, its own normalized original-group mass law has mean omega at most J.
Theorem B with R_J=max(1,J) therefore gives the finite bound

    H_X>=H_X^low
         >=c(s,R_J,delta_low)nu^2 W^2/X.              (20)

When J=0 the direct order1 argument also applies, but the safe R_J1 bound remains valid.
For the efficiency truncation S_low={o:e_ell(o)<=K}, the same conclusion holds with R_J replaced by R_K=max(1,1+log_2 K), using(16).
No actual original root is partly discarded within an order group, and the final norm still retains ALL d roots; H_X^low is only a valid lower contribution at the chosen time.

Now consider a hypothetical near-one sequence with the fixed actual coverage/density constants.
Let epsilon_J=1-nu be the discarded fraction at threshold J.
If its liminf were less than e_delta=1-(1-delta)^(1/3), there would be a fixed eta0>0 and an infinite subsequence such that

    epsilon_J<=e_delta-eta0,
    nu>=(1-delta)^(1/3)+eta0>=eta0.

On that subsequence,

    kappa>=kappa0:=((1-delta)^(1/3)+eta0)^3-(1-delta)>0,
    delta_low>=kappa>=kappa0.

Apply Theorem B to the surviving array using the WEAKER fixed density premise kappa0, not a varying density constant.
Its mass is at least eta0 gamma d, so(20) and the full norm transfer give a fixed positive eta*d income and then a fixed positive lower bound for m(P), a contradiction.
This proves the first part of(18).
The efficiency cutoff proof is identical with fixed R_K, yielding its second part.

To obtain the mean conclusions explicitly, for any fixed J>=1,

    R_mu>=J mu{omega(o)>J}.

Its liminf is at least J e_delta, and J is arbitrary, so R_mu tends to infinity.
Likewise for any fixed K>1 the mean natural-log efficiency is at least(log K)mu{e_ell(o)>K}, and its liminf is at least e_delta log K; letting the fixed threshold K grow proves divergence of that mean.
The mean efficiency also diverges, either by the same tail argument or by(17).
This is a limit statement along the assumed sequence, not a rate as a function of m(P) and not a construction of a near-one family.

For(18a), Q may be restricted to the finite union of prime supports in the actual array: removing other primes changes neither beta_Q nor any core of a selected order, and cannot increase its cardinality.
The minimum is therefore attained among finitely many subsets.
If its liminf at a fixed J were below delta, choose a fixed lambda>0 and a minimizing Q on an infinite subsequence with beta_Q<=delta-lambda.
The wider finite-core income statement just proved would again force a fixed positive Mahler measure, a contradiction.
This proves(18a) with its full quantifier over varying bounded-size Q.

<a id="averaged-positive-controls-and-failures"></a>
## Useful failed candidates and why the positive estimate survives them

The universal LINEAR short-pair estimate is already false in C96.
Nothing here restores it: in(4), choosing epsilon small costs a number of heavy primes of order R_mu/epsilon and an exponential core constant.
The conclusion is a uniform small-pair-probability modulus when the mean R_mu is bounded, which is sufficient for the separate positive TRIPLE-density inference.

A preliminary fixed-core/external-prime Cauchy attempt led to the scalar expense

    (sum_j V_j^(1-s/2)/u_j^(s/2))^2
       <=(sum_j V_j)^(2-s)(sum_j1/u_j)^s.

This inequality follows from Holder with exponents1/(1-s/2) and2/s.
Taking u_j through external primes gives an unbounded reciprocal factor.
That is a failure to close this estimate, not a counterexample to the target.
The successful proof retains all original masses, charges the overlap event directly, and keeps only a FINITE mass-heavy prime set in the geometric core kernel.

The unrestricted strong weighted norm proposed in L396 remains false.
Equations(8)–(12) do not assert it: the packing estimate uses actual scalar capacities after a coprime core factorization, and the only kernel with a uniform row-sum bound is the FINITE Q-core kernel.
Even(3) applies only to good pairs, not all lcm pairs.
There is consequently no contradiction with the C105 correlated obstruction to the sharp product constant or C108's nested Cauchy examples.

The accepted C112 finite stars have bounded individual omega but vanishing normalized triple density.
Theorem B is fully consistent with them: its constant depends on a strictly positive lower density delta, and no such lower bound is present along those stars.
In particular their unbounded row does not negate the averaged probability estimate(4), and their vanishing H_X/W does not negate(5).

This is a positive theorem beyond bounded union-prime support and beyond the efficiency-eight whole-row threshold.
It still does not prove automatic actual positive-density coverage or a uniformly bounded mean complexity/efficiency for arbitrary near-one inputs.
Those are independent arithmetic questions, with explicit necessary escape now given by(18).
No unrestricted weak-moment constant or general unrestricted positive-density theorem is asserted.

<a id="averaged-positive-contributions-and-checks"></a>
## Actual contributions and author checks

Root assigned the averaged positive direction and later asked whether the resulting theorem could strengthen the old fixed-threshold mass escape.
It supplied no proof step for the heavy-prime truncation, packing, finite core estimate, residual transfer or new arbitrary-threshold deduction.
The delegated g_bridge_audit AI supplied those arguments and their constants.
C106 is credited for the prior deletion-loss method and elementary efficiency inequality; C91/L74/L159/L168 retain their existing residual, root-capacity and full-norm scopes.
Source comparisons above are not mathematical imports.
No numerical or symbolic program, J run or new source theorem occurred in this author inquiry.

Root also requested a check of whether the already-written core calculation needed the threshold definition of Q.
The author verified that it did not and retained its full arbitrary-finite-Q quantifier in A/(4a), with its actual gap and bounded-core collision consequence.
This is an explicit scope clarification of the author's displayed proof, not an unproved automatic-core localization hypothesis.

The same scope check retains B(Q,s)<=B0 itself as the maximal displayed paid-core sufficient hypothesis; bounded |Q| is only a convenient specialization.
This follows directly from the already proved product in(11)–(14), not from a new prime-selection theorem.

The author checks the ORIGINAL-law normalization and exact pair event; all repeated labels and bad-pair triple loss; zero/real capacities, V<1 and V>=1 packing; exact phi(g) scaling and all coprimality restrictions; empty Q and p2 in the geometric row sum; every exponent and finite rearrangement; good-only rather than full fractional energy; L>X and H_X0 in the residual formula; s in(0,1), epsilon and ceiling constants; bounded MEAN rather than union-support quantifiers; efficiency order1 and odd/2-primary scope through C106; full original norms and same-time income; and the exact finite threshold loss, delta1 endpoint and positive-fraction versus full-mass escape.
No unresolved gap was found by these author checks, which are not independent review.

<a id="averaged-positive-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T20:46.
Freeze the ENTIRE author-complete original for fixed retention and independent whole review: responsible question and reuse/source limits; exact original mass law; arbitrary finite-core and heavy-prime specializations; Statements A–D and all displayed costs; full packing, good-pair, core-geometric and third-coordinate residual proofs; actual original-norm income under either bounded mean or the wider paid product/gap condition; all fixed threshold and bounded-core collision escapes; zero/real capacities, empty Q, R_mu0, H_X0 and repeated-label boundaries; useful failed shortcuts; actual contributions and unchanged unrestricted/near-one coverage limits.
The scoped material check returned checked1 and is not mathematical acceptance.
No J or new external theorem was needed.
Root's later fixed identity and noncontributor whole review remain separate from this author freeze.

## Fixed organization

The ENTIRE author-frozen original above is retained, with original law and all real/zero/repeated-label boundaries, arbitrary finite-core and heavy-prime specializations, complete packing/kernel/residual proofs, actual full-norm transfer, every fixed-threshold/collision escape, useful failed arguments and source/contribution limits.
Root supplied direction and requested checks of the displayed proof's quantifiers; the author supplied the mathematical arguments.
This actual fixed artifact awaits separate whole independent review.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:46 |
| status | open |
| reason | Retain the complete positive good-pair/core-cost estimate, bounded mean prime-support capture, actual conditional income at every fixed efficiency and all-threshold escape for whole independent review. Actual near-one coverage and the unrestricted goal remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Entire proof](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Residual bucket interface](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Efficiency support and earlier deletion method](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Good-prime full-group capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Full original local income](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Finite original norm criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:53 |
| status | proved |
| reason | Adopt [R800 original heavy-prime-positive](../audits/reviews/Yin_R_G0800_v1.md#heavy-prime-positive-whole-independent-finding) complete independent review of actual A--D and all direct inputs. The good-pair finite-core estimate gives positive triple-density capture under bounded mean prime support or the wider paid core/gap condition, with actual norm income for every fixed efficiency and precise all-threshold escape. Automatic near-one coverage and the unrestricted goal remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Entire proof](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Residual bucket interface](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Efficiency support and earlier deletion method](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Good-prime full-group capacities](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Full original local income](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Finite original norm criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0800_v1.md#heavy-prime-positive-whole-independent-finding) | Entire actual statement, complete retained argument, direct dependency interfaces, source/contribution limits and exact conditional/nonconclusion scope. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Argument](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Dependency](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Dependency](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Dependency](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |
| review | [Review](../audits/reviews/Yin_R_G0800_v1.md#heavy-prime-positive-whole-independent-finding) | Entire actual statement, complete retained argument, direct dependency interfaces, source/contribution limits and exact conditional/nonconclusion scope. |


### Decision current-short-order-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:25 |
| status | proved |
| reason | Select the complete C376v2 proof home for the identical originally used L159 capacity, root-count, prime-budget or prime-radical interfaces at their unchanged exact anchors and scopes. Preserve this Claim statement, argument, status, every other input and the existing review scope. Those reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C376 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Exact retained argument](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Exact retained dependency](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0800_v1.md#heavy-prime-positive-whole-independent-finding) | Entire actual statement, complete retained argument, direct dependency interfaces, source/contribution limits and exact conditional/nonconclusion scope. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Exact retained argument](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Exact retained dependency](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0800_v1.md#heavy-prime-positive-whole-independent-finding) | Entire actual statement, complete retained argument, direct dependency interfaces, source/contribution limits and exact conditional/nonconclusion scope. |

### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:18 |
| status | proved |
| reason | Adopt the separately arranged isolated whole inspection of this exact fixed Statement and complete Argument in R800, with all necessary mathematical interfaces and decisive finite controls checked at their actual scopes. Preserve the fixed mathematics, original source depth, existing self-review and historical unknown/negative findings at their true inputs and dates; no broader gap or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--D, arbitrary paid finite Q, bounded mean specializations and every original-law/density/actual-input/escape quantifier. |
| argument | [Exact retained argument](#argument) | Complete original §§1--7, every finite packing/core/bad-pair/residual calculation, zero cases, actual norm costs and truncation/collision limits. |
| dependency | [Exact retained dependency](Yin_C_G0104_v1.md#product-envelope-density-capture) | Exact third-coordinate original-mass grouping, fully restated locally; no unrestricted fractional moment imported. |
| dependency | [Exact retained dependency](Yin_C_G0106_v1.md#statement) | Elementary actual order/omega inequality with odd and2-primary guards, and prior bounded-threshold deletion-loss mechanism; new all-threshold transfer proved locally. |
| dependency | [Exact retained dependency](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Actual complete original-root order counts, phi capacity and Frobenius constraints at good primes. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original norm and positive integral valuation floor; every initial/higher/exceptional contribution retained. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive total Mahler consequence of actual n<=Cd and eta*d income, with original degree and inherited source scope. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0800_v1.md#fresh-c114-whole) | Entire exact fixed Statement and complete Argument, necessary interfaces, every stated boundary and actual finite/source limits; independently reviewed in the isolated M04 arrangement. |
