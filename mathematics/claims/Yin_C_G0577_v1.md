---
author: Yin
---

# Complete coordinate disclosure profiles, higher interactions and all-repeat sharp bounds

This common original integer-map disclosure/profile object retains BOTH entire [L302](../ledger/Yin_L_G0302_v1.md) and [L306](../ledger/Yin_L_G0306_v1.md) proof chains, with their different sufficient-test, negative-shortcut and exact-repeat domains.
The fixed original R201/R205 inputs and all real source/native/correction limits remain without new research.

<a id="statement"></a>
## Complete statement

Use the ORIGINAL independent digits eta_j in{-1,0,1} with probabilities1/4,1/2,1/4 throughout.
For EVERY integer-column map X=[a_1,...,a_b], b>=1, define S=X eta, mu(z)=Pr(S=z), p=mu(0), H=log(1/p), Q=XX^T and E(z)=z^T Q^+z.
For deleted coordinates J let p_(Jc) be the original zero atom on the complement, including empty-sum probability1.
For independent deletion parameters theta_j in[0,1], put
    K_X(theta)=sum_J p_(Jc)product_(j in J)theta_j product_(j outside J)(1-theta_j).
This is the actual fair-binary conditional-collision average, including revealed values.
Uniform theta gives K_X(theta)<=p^((1-theta)/(1+theta)), and coordinatewise smaller independent parameters give a no larger value.
For EVERY deterministic real r_j,t and integer z, R=max|r_j| and V=sum r_j^2,
    E[exp(t sum r_j eta_j)1_(S=z)]
       <=product_j cosh^2(t r_j/2) K_X(tanh^2(t r_j/2))
       <=p^sech(tR)product_j cosh^2(t r_j/2),
    E[exp(t sum r_j eta_j)1_(S=z)]/p
       <=exp[t^2(V+2HR^2)/4].
This retains the SAME original zero atom, all zero-column/zero-coefficient cases and the older exponent t^2V/2.
It is not conditional independence; at z=0 it is a return-conditioned moment bound.

Let ell_j=a_j^T Q^+a_j, ell_*=max ell_j and
    c_H=1/(1+2H ell_*), q_H=max(1/2,c_H).
The leverages lie in[0,1] and sum to rank r, including deficient rank.
For every row l with lQl^T>0 there is the directional bound
    mu(z)<=p exp[-(lz)^2/(lQl^T+2H max_j|l a_j|^2)].
For EVERY endpoint,
    mu(z)<=p exp[-q_H E(z)].
Rank zero/support{0} is direct.
All quantities are intrinsic under invertible real output changes.
With a=log2 and h_*=(1/a-1)/2, the sufficient condition H ell_*<=h_* proves sharp C1: mu(z)<=p exp[-aE(z)].
It is NOT a necessary condition for C1 or an optimal Gaussian coefficient for the actual map.
It necessarily pays b>=2a^2 r^2/(1-a), and q_H>1/2 necessarily pays b>2r^2a; these are costs of this test, not of C1.

Let J(v)=(1+sqrt(v))log(1+sqrt(v))+(1-sqrt(v))log(1-sqrt(v)),0<=v<=1.
For q in[1/2,1],r0 in[0,a], define Psi_q(r0)=r0 when q>=a.
For q<a let v_(r0,q) be the unique solution in[0,1) of J(v)-qv=r0 and set Psi_q(r0)=r0-(a-q)v_(r0,q).
Then
    min_(0<=v<=1)[max(r0+qv,J(v))-av]=Psi_q(r0),
    mu(z)<=exp[-b Psi_(q_H)(H/b)]exp[-aE(z)].
At q=1/2 this is exactly C562's old Psi.
For r0>0 and1/2<q<a it strictly improves with q, continuously reaching r0 at q=a.
No actual-map extremizer is claimed.

For EVERY ACTUAL nonzero algebraic integer alpha of degree d, including torsion/nonunits/neutral/complex roots, use C517's actual integer columns z_j=-M^(d+j)v, where M multiplies by alpha and v represents1.
For i>=0,b>=d define A_i=[z_0,...,z_(i-1)],W_i=(I+A_iA_i^T)^(-1),X=[z_i,...,z_(i+b-1)],Q_b=XX^T>0,D_b=(W_i^(-1)+Q_b)^(-1),Delta_i=det(W_i^(-1)),Delta_0=1.
The zero atom p_b and leverages are independent of i.
For the ENTIRE u in R^d retain the POSITIVE factor in
    G_(i,b)(u)=exp[a u^T D_b u]E exp[-a(X eta+u)^T W_i(X eta+u)].
One has
    p_b<=sup_u G_(i,b)(u)
       <=K_d sqrt(Delta_i)exp[-b Psi_(q_b)(log(1/p_b)/b)],
    K_d=2^(d/4)(2pi/a)^(d/2).
Under H_b ell_*<=h_* the last multiplier is p_b exactly.
For i>=1 the full logarithmic cost is at most log K_d+mi+(d/2)log(i+d)-(1/2)log|disc P|+m(d-1), with TOTAL m=log M(P); i=0 uses log K_d and d=1 uses discriminant1.
At FIXED P,i_b=o(b), eventual satisfaction of the sufficient test yields full real-tail rate h2.
If merely q_b->q, the lower liminf rate is at least Psi_q(h2) and upper limsup at most h2.
No general eventual nontorsion criterion is supplied.

For k repeats of a fixed finite integer block Y=[y_1,...,y_s], let L_l=sum_j|(y_j)_l|.
Then ell_*<=1/k and H ell_*<=[sum_l log(kL_l+1)]/k->0 at this FIXED block.
Every k passing this explicit test gives C1.
Thus an actual root of unity with a full period block has the profile at all sufficiently large multiple-period windows.
For alpha=1, b>=16 is a valid nonoptimal onset for this particular test.

A distinct stronger all-repeat theorem holds without an eventual test.
If the nonzero columns partition into signed parallel classes of k_j>=1 copies of real-linearly independent INTEGER vectors v_j, with zero columns allowed, then every endpoint z=sum_j s_j v_j satisfies
    mu(z)<=p exp[-sum_j gamma_(k_j)s_j^2/k_j]<=p exp[-aE(z)],
    E(z)=sum_j s_j^2/k_j,
    gamma_1=log2, gamma_k=2k/(2k+1) for k>=2.
All ranks/multiplicities/column sizes and deficient ambient ranks are allowed.
The exact binomial law is4^-k binom(2k,k+s), with ALL |s|<=k.
For actual alpha=1,-1 and primitive2dth roots with d=2^h, h>=0, this proves the original sharp profile at EVERY b>=1 and prefix; t^d+1 is proved to be the actual irreducible minimal.
It does not cover every torsion input or any arbitrary nontorsion power sequence.
For b>=d the same FULL real-tail upper bound has multiplier p_b and every degree/prefix/discriminant cost retained.

The first-order-only anisotropic shortcut
    K_X(theta)/p<=product_j(1+d_j theta_j), d_j=p_(-j)/p-1 in[0,1],
is FALSE.
For X=(1,1),p=3/8,d_1=d_2=1/3, the exact excess is8theta_1 theta_2/9.
Two copies of each of r independent basis columns give deficit ratio
    [(1+2theta/3+theta^2)/(1+theta/3)^2]^r,
equal to(3/2)^r at theta=1.
No rank-independent correction rescues that specific product.
This refutes a proposed bound on the nonnegative Fourier expression, not C1 or the original moment.

The separate J78 abstract sign-column domains r=2,3,4,5 retain9,65,1537,140673 endpoints and142284 exact comparisons, all original native types/fields/timings and complete different-method review.
Ranks2/3 are injective/one-relation controls; only ranks4/5 introduce new overlapping nullities4/11.
The actual2026-10-10T08:34 scope clarification and complete original review2026-10-10T08:36 remain.
These finite observations are not premises of either theorem or actual nontorsion algebraic-orbit tests.
ODo07 remains the precise already-inspected attribution for C534's locally proved Boolean input, not a newly imported source proof.
No new native/program/source run, universal C1, lossless general neutral exponent, near-one entropy floor or unrestricted gap is asserted.

## Complete argument

<a id="argument"></a>

## Complete disclosure, leverage and finite-tail argument

<a id="disclosure-gaussian-current-reuse"></a>
### 1. Exact reuse, contribution and changed mechanism

The coordinator authored this argument without contribution from the separately assigned D170--D172 authors.
Read the precise finite collision-disclosure theorem [L223, Section3/(9)--(11)](Yin_C_G0534_v1.md#partial-mask-collision-information-retention), the complete complex-Fourier endpoint proof [L251, Section1](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments), and [L298's full nonlinear endpoint/tail theorem](Yin_C_G0562_v1.md#statement).
The new connection is to use the former to estimate the exact subset sum arising in the latter Fourier expansion, instead of charging every deleted digit separately.
It pays actual collision information and maximal column leverage.
This is different information from L298's two scalar envelopes.

The classical ingredient is exactly Boolean hypercontractivity already identified, locally proved and reviewed in L223, with attribution to [ODo07's inspected statement and convention](../audits/literature/ODo07/readme.md#boolean-hypercontractivity-attribution).
No new source theorem or source-wide audit is adopted.
A bounded web discovery screen on Bernoulli point probabilities and peakedness produced no adopted mathematical premise.
The present proof is finite algebra/inequalities plus the retained L223 statement; no new computation or J is required.
[L290](Yin_C_G0547_v1.md#statement) remains the stronger exact theorem on its one-relation/disjoint-support scopes.
The target here is arbitrary overlapping relations and their actual, checkable complete-tail expense.

<a id="anisotropic-deletion-moment"></a>
### 2. Coordinate disclosure controls the exact Fourier deletion law

Fix b>=1 integer columns a_j in Z^D and independent ORIGINAL eta_j with masses1/4,1/2,1/4 on-1,0,1.
Put
    S=sum a_j eta_j, mu(z)=Pr(S=z), p=mu(0), H=log(1/p).
For a subset J of deleted positions, write p_(Jc) for the zero probability of the original digits on the other positions; the empty sum has probability1.
Let epsilon_j be independent fair0/1 bits and Y=sum a_j epsilon_j.
The difference of two independent copies of Y has exactly the original law, so Col(Y)=p.
Upon revealing the bits in J, the remaining endpoint distribution is a translation of sum_(j outside J) a_j epsilon_j.
Its collision probability is therefore p_(Jc), independent of the revealed values.
Applying the FULL L223 disclosure theorem directly to these bits (not to a carry mask) yields
    E_(J iid Bernoulli theta) p_(Jc)
                 <=p^((1-theta)/(1+theta)), 0<=theta<=1.       (1)
There is no degree or carry-boundary loss in this application.

Deletion only increases p_(Jc).
Indeed adjoining one fair bit to a binary endpoint probability vector f changes it to (f+T_a f)/2, where T_a is translation.
Its squared l2 norm is at most ||f||_2^2 by the triangle inequality and translation invariance.
This holds also when a=0.
Couple independent deletion indicators with independent uniform[0,1] thresholds.
Thus, if 0<=theta_j<=theta coordinatewise, the anisotropic expectation of p_(Jc) is no greater than the uniform-theta expectation in(1).

Given any deterministic real coefficients r_j and real t, L251's exact Fourier identity and triangle inequality give
    E[exp(t sum r_j eta_j) 1_(S=z)]
       <=sum_(J subset[b]) p_(Jc) product_(j in J) sinh^2(t r_j/2).
Factor the sum as product_j cosh^2(t r_j/2) times the expectation of p_(Jc) under independent deletions with probabilities
    theta_j=tanh^2(t r_j/2).
Let R=max_j |r_j|.
Their maximum is theta=tanh^2(tR/2), and
    (1-theta)/(1+theta)=sech(tR).
Consequently, for every integer z and every real t,
    E[exp(t sum r_j eta_j) 1_(S=z)]
       <=p^sech(tR) product_j cosh^2(t r_j/2).                  (2)
The exponent notation means p raised to sech(tR), with sech x=1/cosh x.
All probabilities are those of the SAME original integer map.
This is not a conditional independence statement or a replacement of its digits.
At tR=0, the disclosure parameter is0 and(2) includes the maximum-atom bound mu(z)<=p.

Write V=sum r_j^2.
For every real x,
    2log cosh(x/2)<=x^2/4,   1-sech x<=x^2/2.
The first follows by integration of tanh u<=u.
For the second, cosh x-1<=(x^2/2)cosh x: compare the nonnegative even power coefficients, using (2k)(2k-1)>=2 for k>=1, and divide by cosh x.
Dividing(2) by p proves
    E[exp(t sum r_j eta_j) 1_(S=z)]/p
              <=exp[t^2(V+2HR^2)/4].                         (3)
At z=0 this is a genuine return-conditioned exponential-moment bound.
The old L251 bound exp(t^2 V/2) still applies, so the better variance proxy may be used.
Improvement is strict whenever V>0 and2HR^2<V.
No improvement is asserted for concentrated coefficients failing that condition.

<a id="leverage-relative-profile"></a>
### 3. Complete relative endpoint profile with an explicit leverage charge

Let X have the a_j as columns, Q=XX^T, and Q^+ be its real symmetric pseudoinverse.
Put
    E(z)=z^T Q^+z,
    ell_j=a_j^T Q^+a_j, ell_*=max_j ell_j,
    c_H=1/(1+2H ell_*), q_H=max{1/2,c_H}.                     (4)
Here 0<=ell_j<=1 because X^T Q^+X is an orthogonal projection; its trace is the real rank r of X.
The zero-rank case has ell_*=0, p=1 and support{0}; all assertions below are direct there.
Only endpoints in range X need be considered; outside it mu(z)=0.

For any row l with V=lQl^T>0, use r_j=l a_j in(3).
On S=z the exponential is constant.
Minimizing t^2(V+2HR^2)/4-t lz gives
    mu(z)<=p exp[-(lz)^2/(V+2HR^2)].                           (5)
If V=0, the row vanishes on the support, and no division is needed.
For z in range X with E(z)>0, choose l=z^T Q^+.
Then lz=V=E(z).
Cauchy--Schwarz in the Q^+ semidefinite form gives
    R^2=max_j (z^T Q^+a_j)^2<=ell_* E(z).
Combining(5) with L251's full relative coefficient1/2 proves
    mu(z)<=p exp[-q_H E(z)]                                  (6)
for EVERY z.
In particular, for a=log2 and
    h_*= (1/a-1)/2,
the explicit sufficient condition
    H ell_*<=h_*                                             (7)
implies the sharp profile(C1), mu(z)<=p 2^(-E(z)), over the entire support.
The coefficient q_H and sufficient condition are intrinsic under every invertible real change of output coordinates.
For full row rank, (TX)^T(TQT^T)^(-1)(TX)=X^TQ^(-1)X; in deficient rank use the fact that both are the projection onto the same row space.
H is unchanged because T is injective on endpoints.

There is a stronger directional version(5), and the exact nonlinear expression(2) is stronger still.
Replacing either by ell_* is an explicit simplification.
The theorem does not claim necessity of(7) for(C1), nor optimality of q_H for the actual map.

<a id="leverage-crossover-complete-tail"></a>
### 4. Improved crossover and the whole real-tail sum

Even if(7) fails, (6) can improve L298.
For a finite map put r_b=H/b in[0,a], and use L298's independently proved absolute profile
    mu(z)<=exp[-b J(E(z)/b)],
    J(v)=(1+sqrt v)log(1+sqrt v)
                +(1-sqrt v)log(1-sqrt v), 0<=v<=1.
Every supported E(z)<=b, J(0)=0, J(1)=2a, J'(v)>=1.
For q in[1/2,1], define
    Psi_q(r)=r,                                  if q>=a;
    Psi_q(r)=r-(a-q)v_(r,q),                     if q<a,       (8)
where v_(r,q) is the unique solution in[0,1) of J(v)-qv=r.
In the latter case J(v)-qv is strictly increasing, starts at0, and at1 equals2a-q>a>=r, so the definition is valid.
The same two-branch calculation as in L298 gives
    min_(0<=v<=1){max(r+qv,J(v))-av}=Psi_q(r)                  (9)
for q<a.
For q>=a, r+qv-av>=r, with equality at v=0, and the other branch at0 is0<=r, so(9) holds as well.
Thus
    mu(z)<=exp[-b Psi_(q_H)(r_b)] exp[-a E(z)].               (10)
For q=1/2 this is exactly L298's Psi.
For r>0 it is strictly larger when1/2<q<a: implicit differentiation gives
    partial_q Psi_q(r)
       =v_(r,q) [1-(a-q)/(J'(v_(r,q))-q)]>0.
For q>=a it is r; the function is continuous through q=a.
This improvement uses the NEW leverage/disclosure input; it is not a reoptimization of the old two unchanged envelopes.

Now take every actual nonzero algebraic integer alpha, monic minimal P of degree d, total logarithmic Mahler measure m, i>=0, b>=d, and the EXACT L282/L298 matrices
    z_j=-M^(d+j)v, A_i=[z_0,...,z_(i-1)],
    W_i=(I+A_iA_i^T)^(-1), X=[z_i,...,z_(i+b-1)],
    Q_b=XX^T, D_b=(W_i^(-1)+Q_b)^(-1),
    Delta_i=det(I+A_iA_i^T), Delta_0=1.
M is the integral multiplication-by-alpha matrix and v represents1.
No unit, non-torsion or hyperbolicity hypothesis is imposed.
Each d consecutive columns is independent, so Q_b>0.
The zero atom p_b and all column leverages depend on b and P but are independent of i: multiplying every column by the same invertible -M^(d+i) leaves the endpoint equality and projection unchanged.
Define q_b from(4) using H_b=log(1/p_b), and retain the FULL finite object for every u in R^d,
    G_(i,b)(u)=exp[a u^T D_b u]
                   E exp[-a(X eta+u)^T W_i(X eta+u)].
Then
    p_b<=sup_(u in R^d) G_(i,b)(u)
       <=K_d sqrt(Delta_i) exp[-b Psi_(q_b)(H_b/b)],
    K_d=2^(d/4)(2pi/a)^(d/2).                              (11)
In particular, under(7),
    p_b<=sup_u G_(i,b)(u)<=K_d sqrt(Delta_i) p_b.             (12)

To verify every tail and positive factor, put B0=W_i+Q_b^(-1), z0=-B0^(-1)W_i u.
The exact noncommutative square completion is
    (z+u)^T W_i(z+u)+z^TQ_b^(-1)z
        =(z-z0)^T B0(z-z0)+u^T D_b u.
It follows from W_i-W_i B0^(-1)W_i=(W_i^(-1)+Q_b)^(-1).
Multiply(10) by the original Gaussian and the POSITIVE exponential in G: the latter cancels exactly.
Extend the nonnegative endpoint sum to all Z^d.
Since B0>=W_i and W_i<=I, the translated-cube estimate in L298 yields at most
    sum_(z in Z^d)exp[-a(z-z0)^T W_i(z-z0)]
            <=2^(d/4)(2pi/a)^(d/2)/sqrt(det W_i).
For its complete cost, if x is in the unit cube centered at z-z0, the squared-norm inequality gives (z-z0)^TW_i(z-z0)>=x^TW_i x/2-d/4; integrate over cubes of volume1 and evaluate the Gaussian integral.
This proves(11) for the whole UNBOUNDED real tail, not merely a selected tail or a finite box.
The entire zero-endpoint fiber at u=0 gives the lower bound.

No prefix or degree expense is suppressed.
The retained full-root L282/L298 estimate gives, for i>=1,
    log(K_d sqrt Delta_i)
      <=log K_d+m i+(d/2)log(i+d)
                    -(1/2)log|disc P|+m(d-1).               (13)
For i=0 the exact expense is log K_d; for d=1 the discriminant is1.
At fixed P and i_b=o(b), if(7) holds for every sufficiently large b, (12) forces the full real-tail rate to equal the original h2(P).
More generally, if q_b converges to q, continuity of(8) and the original collision rate give lower limiting tail rate at least Psi_q(h2(P)) and upper limiting rate at most h2(P).
These statements are conditional on the stated leverage behavior; no eventual version is asserted for arbitrary nonzero-entropy neutral inputs.
At fixed hyperbolic input and fixed prefix, L286's already established lossless rate remains available without this criterion.

<a id="leverage-criterion-domain-cost"></a>
### 5. What the sufficient condition costs, and an actual eventual domain

The condition is checkable but has a significant dimension expense.
For every rank-r integer map, select r real-linearly independent columns.
The original difference law on these columns has maximum atom2^(-r), since all its3^r endpoints are distinct and each digit's maximum mass is1/2.
Convolution with all remaining independent digits cannot increase the maximum atom.
Hence
    H>=r log2, ell_*>=r/b,
    H ell_*>=r^2 log2/b.                                  (14)
Therefore(7) NECESSARILY requires
    b>= [2(log2)^2/(1-log2)] r^2.                           (15)
Similarly, q_H>1/2 requires b>2r^2 log2.
These are necessary conditions for this particular sufficient test or its strict Gaussian improvement, not necessary conditions for(C1) itself.
In actual degree-d windows r=d.
Thus this criterion alone cannot certify sharpness in b<=C d windows at unbounded degree.
That limitation is explicit, rather than hidden by calling ell_* small.

The criterion is nonvacuous on genuine original algebraic inputs with arbitrarily many overlapping relations.
More generally fix a finite integer block Y=[y_1,...,y_s] of any positive rank and repeat it k times, X_k=[Y,...,Y].
Then Q_k=k YY^T and every leverage is at most1/k.
For output coordinate l let L_l=sum_j |(y_j)_l|.
A binary endpoint of X_k has at most
    N_k=product_(l=1)^D (k L_l+1)
possible values: its l-th coordinate lies in an integer interval of length k L_l.
Cauchy--Schwarz on the entire finite support implies p_k=Col(binary endpoint)>=1/N_k.
Consequently
    H_k ell_*(X_k)<= [sum_l log(k L_l+1)]/k ->0.             (16)
Zero L_l contribute log1=0.
Every k satisfying the displayed explicit bound<=h_* therefore satisfies(C1), regardless of how many relations overlap.

For an ACTUAL root of unity alpha of order s, the full power-basis sequence alpha^j repeats every s steps; every full window b=ks consists of k copies of an integer period block, up to a fixed invertible multiplication and permutation.
Its power columns span the degree-d order.
Formula(16) thus proves(C1) and (12) for all sufficiently large such windows with an explicit finite k-test.
This is a torsion demonstration of the mechanism, not a source of a positive non-torsion gap; torsion h2=0.
As an elementary example, alpha=1 gives D=1,L_1=1 and H_b ell_*<=log(b+1)/b.
For all b>=16 this is at most log17/16<3/16<h_*.
The last inequalities follow from e^3>17 (sum its nonnegative series through degree5 already exceeds17) and log2<7/10, which imply h_*>3/14>3/16.
The function log(b+1)/b decreases for b>0 by differentiation.
This example is not asserted to be the optimal onset or a new special-case binomial inequality.

There is NO transfer from repeated torsion blocks to arbitrary irreducible non-torsion power sequences.
In particular, some expanding boundary columns can have much larger leverage than a repeated-block heuristic predicts, and H_b retains the complete original return loss.
The new theorem identifies an actual sufficient route and its quadratic-window expense.
The remaining sharp question is to exploit the exact anisotropic deletion expression(2), directional information(5), or actual power-sequence arithmetic beyond the single worst-column charge, in a way compatible with all tail directions and varying degree.
The unrestricted Task and all candidate routes remain active.

Author self-check includes the binary-difference normalization, revealed-value independence, monotonicity/coupling directions, exact deletion factor and sech identity, all zero/degenerate supports, original p normalization, pseudoinverse range and leverage covariance, crossover domain/strict derivative, prefix invariance, full positive completion and translated lattice sum, all root/discriminant costs, quadratic necessity and complete repeated-block/torsion support bound.
No computational data or source novelty claim is a premise.
The entire author body is ready for separately organized whole noncontributor review; adoption remains separate.





## Complete higher-interaction obstruction and all-repeat argument

<a id="anisotropic-disclosure-reuse"></a>
### 1. Exact question and knowledge reuse

The coordinator is the sole author of this branch.
L302's [exact deletion and disclosure identity](#anisotropic-deletion-moment) gives a sufficient sharp profile with the charge H times maximal column leverage, necessarily requiring a quadratic-rank window.
The new question is whether the actual coordinatewise disclosure increments remove that expense without controlling their higher interactions.
The answer below is negative, already for original rank-one repeated columns, with an exponential obstruction after independent tensorization.
In the same examples the sharp endpoint inequality itself holds in every window.
Thus this is an obstruction to a proposed proof shortcut, not to the sharp profile.

The precise prior inputs inspected are L251's full Fourier subset proof, L223's collision/disclosure proof and its already checked [ODo07 attribution](../audits/literature/ODo07/readme.md#boolean-hypercontractivity-attribution), L290's exact truncated-section formulation and disjoint-relation theorem, L294's digit-accessible reduction and all-quadratic short windows, and L286/L302's complete tail and cost interfaces.
The existing J71 finite domain reaches rank two; J73 tests bounded actual polynomial windows.
Neither covers the higher-rank sign-column domain below.
Local ledger/source-home searches for anisotropic disclosure, truncated Gaussian domination and relative profiles found no retained theorem controlling arbitrary higher-order deletion interactions by the first-order increments.

A bounded web discovery screen on2026-10-10 used the exact phrases discrete Gaussian domination Bernoulli, lattice truncated Gaussian shift maximum theta, and Bernoulli sums relative point probabilities Gaussian.
Its returned material did not supply a matching finite-cube, actual-zero-atom theorem; no source theorem, acquisition or novelty assertion is adopted.
The following negative test and binomial comparison are direct finite identities and elementary inequalities.
The ordinary binomial mass formula is derived rather than asserted as a new special-function theorem.
The previously identified hypercontractivity theorem remains attribution only for the retained L223 premise; no new use of its source proof occurs here.

<a id="anisotropic-marginal-obstruction"></a>
### 2. Exact anisotropic deletion polynomial and a failed marginal shortcut

Let X have b integer columns a_j, let independent ORIGINAL digits eta_j have probabilities1/4,1/2,1/4 on-1,0,1, and write p=Pr(X eta=0).
For J contained in[b], let p_(Jc) be the zero atom with precisely the coordinates J deleted.
For independent coordinate-disclosure probabilities theta_j in[0,1], define

    K_X(theta)=sum_J p_(Jc) product_(j in J)theta_j
                                 product_(j outside J)(1-theta_j).

This is exactly the expected collision probability after revealing those bits of the original fair-binary endpoint, by L302.
In particular K_X(0)=p, and its actual first derivatives at0 are p_(-j)-p.
Put

    d_j=p_(-j)/p-1,   0<=d_j<=1.                         (1)

The lower bound uses collision monotonicity under adjoining an independent bit.
The upper bound uses the original event eta_j=0, of probability1/2, followed by a return of the remaining digits, so p>=p_(-j)/2.
No law is changed.

A tempting coordinatewise replacement for the global H charge would be

    K_X(theta)/p <= product_j(1+d_j theta_j).             (M)

The first derivatives and the constant coefficient on both sides agree exactly, but(M) is FALSE.
Take the actual original scalar columns X=(1,1).
Direct expansion of(2+z+z^-1)^2 gives p=6/16=3/8, and p_(-1)=p_(-2)=1/2.
Therefore d_1=d_2=1/3, and

    K_X(theta_1,theta_2)/p
           =1+(theta_1+theta_2)/3+theta_1 theta_2,
    product_j(1+d_j theta_j)
           =1+(theta_1+theta_2)/3+theta_1 theta_2/9.       (2)

Their difference is8theta_1 theta_2/9.
This refutes(M) for every pair of strictly positive disclosure probabilities; no numerical test is needed.

For r>=1, take TWO copies of each of r independent integer basis columns.
The original endpoint coordinates are independent and all relevant zero atoms factor, so K_X/p is the product of the r two-coordinate expressions in(2).
At uniform theta>0, the ratio of the true expression to(M)'s proposed right side is

    [ (1+2theta/3+theta^2)/(1+theta/3)^2 ]^r >1.          (3)

At theta=1 it is(3/2)^r.
Hence no correction constant independent of rank can make(M) valid on all original integer maps, even at this fixed two-copies-per-direction multiplicity.
This conclusion concerns the specifically displayed marginal product; it does not exclude an estimate using higher interactions, conditional increments, a different functional form or actual algebraic-orbit structure.

There is a direct connection to L302's complex Fourier estimate.
For arbitrary real r_j and t, the exact nonnegative bound there is

    E[exp(t sum_j r_j eta_j)1_(X eta=z)]
       <= product_j cosh^2(t r_j/2) K_X(theta),
    theta_j=tanh^2(t r_j/2).                             (4)

Thus the false step(M) cannot be inserted into(4), even when all probabilities come from actual real tilts: choose t nonzero and both scalar tilt coefficients nonzero in(2).
The bad inequality is the proposed upper bound on the nonnegative Fourier expression itself.
Failure of this upper estimate does NOT imply failure of the original moment or the endpoint profile, since(4) may already have slack.
For example the endpoint profile on these same columns is proved next.

<a id="all-repeat-sharp-profile"></a>
### 3. All multiplicities in independent parallel classes

**Theorem.** Suppose the nonzero integer columns of X can be partitioned into r nonempty classes, with the j-th class consisting of k_j>=1 copies of v_j or -v_j, where v_1,...,v_r are real-linearly independent.
Zero columns are allowed separately.
Put Q=XX^T and let Q^+ be its symmetric pseudoinverse.
Every original endpoint satisfies

    mu(z) <= mu(0) exp[-sum_(j=1)^r gamma_(k_j) s_j^2/k_j]
           <=mu(0) 2^(-z^T Q^+ z),                    (5)
    z=sum_j s_j v_j,  s_j integer, |s_j|<=k_j,
    gamma_1=log2,  gamma_k=2k/(2k+1) for k>=2.

There is no bound on r, the multiplicities, the column lengths or the prefix transformation.
Endpoints outside this finite set have zero probability and satisfy the final upper bound trivially.

Changing a column sign preserves its symmetric original law, and zero columns have no effect on either the endpoint law or Q.
Each scalar coordinate sum of k digits has generating function

    4^-k(z^-1+2+z)^k=4^-k z^-k(1+z)^(2k).

Consequently its mass at s is4^-k binom(2k,k+s), and the ratio to its central mass is

    R_k(s)=binom(2k,k+s)/binom(2k,k)
           =product_(l=1)^|s| (k-l+1)/(k+l).             (6)

For x>=1, log x>=2(x-1)/(x+1): both sides agree at1 and the derivative of their difference is(x-1)^2/[x(x+1)^2]>=0.
For k>=2 apply this to x=(k+l)/(k-l+1), for1<=l<=|s|<=k, obtaining

    -log R_k(s)>=sum_l 2(2l-1)/(2k+1)
                  =2s^2/(2k+1)=gamma_k s^2/k.          (7)

Also gamma_k>=4/5>log2.
To check the last strict numerical comparison without an approximation, the positive series gives e^(4/5)>1+4/5+(4/5)^2/2>2.
For k=1 the three masses have ratios1,1/2,1/2, so(5) holds with gamma_1=log2 exactly.
The s=0 empty product case is included.

The independent scalar class sums determine the output uniquely because the v_j are linearly independent.
Thus all endpoint masses and the central mass multiply across classes.
To see the metric exactly, among real preimages giving coefficient s_j in a class of k_j signed equal columns, Cauchy--Schwarz gives least squared norm s_j^2/k_j, attained by equal signed entries.
Zero-column coordinates are set to zero in the minimum.
Different classes have independent linear constraints.
Therefore

    z^T Q^+z=min_(Xu=z)||u||^2=sum_j s_j^2/k_j.          (8)

This proves the entire theorem, including rank deficiency in an ambient larger output space.
It is not an independence assumption on arbitrarily chosen ambient coordinates.

For the two-copy rank-r example of Section2, p=(3/8)^r, H=r log(8/3), and every nonzero column leverage equals1/2.
Therefore H ell_*=r log(8/3)/2.
L302's global criterion fails already at r=1 and increasingly with rank, whereas(5) gives the stronger coefficient4/5 in every direction and b=2r.
To verify the r=1 failure, log(8/3)>log2>=2/3 (integrate the convex function1/x on[1,2] and use its midpoint bound), so H ell_*>1/3; meanwhile (1/log2-1)/2<=1/4.
This is a concrete linear-rank family showing the expense of that particular global entropy criterion, while retaining genuine overlapping relations when a class has at least3 copies.
The two-copy example alone has disjoint one-dimensional relations and was already within L290; the present theorem's all multiplicities extend that earlier scope.
No new universal sharp coefficient is inferred.

<a id="all-repeat-actual-input-and-tail"></a>
### 4. Actual power-window consequence and full costs

The theorem immediately applies to alpha=1 and alpha=-1 at EVERY length.
A growing-degree actual family is alpha a primitive2d-th root of unity with d=2^h, h>=0.
Its minimal polynomial is t^d+1.
For completeness, irreducibility follows by shifting t=x+1: modulo2, (x+1)^(2^h)+1=x^d, since iterating squaring in characteristic2 removes all mixed terms; the constant term is2, not divisible by4.
The elementary Eisenstein argument at2 says that a hypothetical monic factorization would reduce modulo2 to two positive-degree powers of x, making both integer constants even and their product divisible by4, a contradiction.
Such integer monic factors exist from a rational factorization by the usual primitive-polynomial denominator clearing (Gauss lemma).
Thus the displayed polynomial is the actual minimal polynomial, not a reducible quotient control.
The h=0 case t+1 is also immediate.

In its integer power basis, alpha^(j+d)=-alpha^j; hence EVERY finite consecutive power window consists of signed repeated members of the independent basis1,alpha,...,alpha^(d-1), with any missing classes simply absent when b<d.
The actual original profile(5) therefore holds at EVERY b>=1 and EVERY prefix i>=0.
More generally, multiplication by any nonzero scalar in the field and any faithful invertible real output change preserve the fiber probabilities and the minimum real preimage energy in(8), as in L290.
This explains the arbitrary-prefix and full-Minkowski versions directly.
It is not a statement for all roots of unity, whose basis classes need not be parallel.

For actual b>=d, use exactly L286/L302's full-tail convention: A_i contains the first i integral remainder columns, W_i=(I+A_i A_i^T)^-1, X contains the next b columns, Q_b=XX^T, D_b=(W_i^-1+Q_b)^-1 and Delta_i=det(W_i^-1).
With a=log2 and S=X eta, define

    G_(i,b)(u)=exp(a u^T D_b u)
                  E exp[-a(S+u)^T W_i(S+u)].

The original zero atom is p_b.
The now-proved(C1) gives

    p_b<=sup_(u in R^d)G_(i,b)(u)
          <=K_d sqrt(Delta_i) p_b,
    K_d=2^(d/4)(2pi/log2)^(d/2).                         (9)

The lower bound uses the zero endpoint at u=0.
For the whole upper bound, set B=W_i+Q_b^-1 and c=-B^-1 W_i u.
Direct expansion gives

    (z+u)^T W_i(z+u)+z^T Q_b^-1 z
        =(z-c)^T B(z-c)+u^T D_b u.

The last term cancels the POSITIVE factor in G.
Enlarge the remaining nonnegative sum to all z in Z^d and use B>=W_i.
For x in the unit cube centered at z-c, the inequality W_i<=I gives
(z-c)^T W_i(z-c)>=x^T W_i x/2-d/4.
Integrating the whole cube tiling and the real Gaussian yields precisely K_d/sqrt(det W_i).
No unbounded tail or positive factor is omitted.

At i>=1, the full retained root estimate gives

    log(K_d sqrt(Delta_i))
       <=log K_d+m i+(d/2)log(i+d)
            -(1/2)log|disc P|+m(d-1).                  (10)

At i=0 use Delta_0=1 separately.
These are exactly the full original costs; (9) is not a degree-free estimate.
For the stated torsion inputs m=0 and h2=0.
The point of this consequence is to remove L302's eventual-multiplicity test on a precise all-window actual class.
It supplies no positive non-torsion gap and no assertion for an irreducible near-one neutral input.

<a id="orthogonal-sign-profile-test"></a>
### 5. A distinct higher-rank complete discriminator

Before executing, [J78](../computations/programs/Yin_J_G0078/readme.md) declared exactly ranks r=2,3,4,5 and the complete column family(1,e_2,...,e_r) with every e_j in{-1,1}; b=2^(r-1) and Q=b I.
Ranks4 and5 introduce genuinely overlapping relation spaces of nullities4 and11, beyond the prior rank-two domains and the parallel-class theorem above.
Rank3 has b=4 and nullity1, so it remains a control already covered by L290; rank2 is injective.
No new theorem domain is attributed to those two controls.
It is not an actual polynomial-orbit test.

The sole standard-library Python3.12.14 author run completed on2026-10-10T08:18 in0.8394625000073574seconds, below its declared aggregate120-second cap.
The four complete distributions have9,65,1537 and140673 endpoints, respectively, totaling142284.
Every original count has denominator4^b; every endpoint z was tested by the exact integer comparison

    count(z)^b 2^(sum_i z_i^2) <= count(0)^b.             (11)

The payload retains all columns, complete Gram matrices, counts, squared lengths, booleans, failures, normalization and symmetry checks.
No failure occurred; no author run failed, no output was overwritten and no domain was expanded.
These finite observations do not prove(C1), do not settle the anisotropic interaction question and are not premises of Sections2--4.
Complete different-method verification remains separate from author construction.

### 6. Outcome, uncertainty and next useful discriminator

The mathematical advance is a precisely refuted marginal-disclosure replacement, with an exponential-in-rank obstruction at fixed multiplicity, together with an all-multiplicity sharp profile on independent parallel classes and its exact all-window torsion consequence.
The finite higher-rank domain remains favorable but inconclusive.
A useful next proof must retain higher disclosure interactions or use arithmetic of the actual orbit; matching the first-order increments alone does not justify a multiplicative bound.
Conversely the failure of that shortcut supplies no counterexample to the sharp profile.

The unresolved frontier remains arbitrary overlapping non-torsion power relations with complete real-tail costs.
No independently reviewed universal(C1), non-torsion all-window theorem, degree-uniform gap, or full G0001 solution is claimed.
All candidate routes remain active.
The entire author text and J78 author files are now frozen for whole separately organized noncontributor written review and complete different-method payload verification.
Root authored all new material above and the author program; no sibling contributed a proof step.




## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:37 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete collision disclosure theorem](Yin_C_G0534_v1.md#partial-mask-collision-information-retention) | Independent coordinate selectors AND actually revealed values of iid fair bits, with complete local Boolean proof and exact ODo07 attribution boundary; no carry loss imported. |
| dependency | [Original Fourier endpoint mechanism](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Exact original integer-character subset expansion and relative coefficient1/2. |
| dependency | [Complete absolute entropy/envelope](Yin_C_G0562_v1.md#statement) | Same-map exact J cost, all singular endpoints and full nonlinear finite-tail expense, not actual-map attainment or sharp C1. |
| dependency | [Complete actual finite matrices](Yin_C_G0517_v1.md#statement) | Actual power-basis columns, invertible nonunit prefix, ordered positive completion and full determinant/discriminant cost. |
| dependency | [Complete sharp-profile transfer](Yin_C_G0529_v1.md#statement) | Only whole-real-tail implication at the actual proved profile and full paid constants. |
| support | [One-relation/disjoint-support comparisons](Yin_C_G0547_v1.md#statement) | Prior exact restricted scopes, so rank2/3 sign tests are not falsely new overlapping theorem domains. |
| support | [Original full J78 evidence](../computations/programs/Yin_J_G0078/readme.md) | Four complete abstract domains, all142284 comparisons, native program/output and complete existing R205 verification without rerun. |
| support | [Original disclosure proof/input](../ledger/Yin_L_G0302_v1.md#complete-retained-proof-and-review) | Complete Sections1--5/equations1--16, original author/source/no-program/negative limits and R201. |
| support | [Original anisotropic/all-repeat proof/input](../ledger/Yin_L_G0306_v1.md#complete-retained-proof-and-review) | Complete Sections1--6/equations1--11, actual2026-10-10T08:34 scope clarification, original full J78/source/native/negative limits and R205. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:40 |
| status | proved |
| reason | Adopt the exact complete disclosure/profile object after actual whole current SELF of the published Statement and BOTH full Arguments, retaining sufficient-test, negative shortcut, exact-repeat, finite-native and source boundaries; no isolated review or research resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete collision disclosure theorem](Yin_C_G0534_v1.md#partial-mask-collision-information-retention) | Independent coordinate selectors AND actually revealed values of iid fair bits, with complete local Boolean proof and exact ODo07 attribution boundary; no carry loss imported. |
| dependency | [Original Fourier endpoint mechanism](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Exact original integer-character subset expansion and relative coefficient1/2. |
| dependency | [Complete absolute entropy/envelope](Yin_C_G0562_v1.md#statement) | Same-map exact J cost, all singular endpoints and full nonlinear finite-tail expense, not actual-map attainment or sharp C1. |
| dependency | [Complete actual finite matrices](Yin_C_G0517_v1.md#statement) | Actual power-basis columns, invertible nonunit prefix, ordered positive completion and full determinant/discriminant cost. |
| dependency | [Complete sharp-profile transfer](Yin_C_G0529_v1.md#statement) | Only whole-real-tail implication at the actual proved profile and full paid constants. |
| support | [One-relation/disjoint-support comparisons](Yin_C_G0547_v1.md#statement) | Prior exact restricted scopes, so rank2/3 sign tests are not falsely new overlapping theorem domains. |
| support | [Original full J78 evidence](../computations/programs/Yin_J_G0078/readme.md) | Four complete abstract domains, all142284 comparisons, native program/output and complete existing R205 verification without rerun. |
| support | [Original disclosure proof/input](../ledger/Yin_L_G0302_v1.md#complete-retained-proof-and-review) | Complete Sections1--5/equations1--16, original author/source/no-program/negative limits and R201. |
| support | [Original anisotropic/all-repeat proof/input](../ledger/Yin_L_G0306_v1.md#complete-retained-proof-and-review) | Complete Sections1--6/equations1--11, actual2026-10-10T08:34 scope clarification, original full J78/source/native/negative limits and R205. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0756_v1.md#disclosure-interactions-all-repeat-whole-self) | Entire Statement and both complete Arguments, every true dependency interface and all original finite/native/source/correction limits. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete collision disclosure theorem](Yin_C_G0534_v1.md#partial-mask-collision-information-retention) | Independent coordinate selectors AND actually revealed values of iid fair bits, with complete local Boolean proof and exact ODo07 attribution boundary; no carry loss imported. |
| dependency | [Original Fourier endpoint mechanism](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Exact original integer-character subset expansion and relative coefficient1/2. |
| dependency | [Complete absolute entropy/envelope](Yin_C_G0562_v1.md#statement) | Same-map exact J cost, all singular endpoints and full nonlinear finite-tail expense, not actual-map attainment or sharp C1. |
| dependency | [Complete actual finite matrices](Yin_C_G0517_v1.md#statement) | Actual power-basis columns, invertible nonunit prefix, ordered positive completion and full determinant/discriminant cost. |
| dependency | [Complete sharp-profile transfer](Yin_C_G0529_v1.md#statement) | Only whole-real-tail implication at the actual proved profile and full paid constants. |
| support | [One-relation/disjoint-support comparisons](Yin_C_G0547_v1.md#statement) | Prior exact restricted scopes, so rank2/3 sign tests are not falsely new overlapping theorem domains. |
| support | [Original full J78 evidence](../computations/programs/Yin_J_G0078/readme.md) | Four complete abstract domains, all142284 comparisons, native program/output and complete existing R205 verification without rerun. |
| support | [Original disclosure proof/input](../ledger/Yin_L_G0302_v1.md#complete-retained-proof-and-review) | Complete Sections1--5/equations1--16, original author/source/no-program/negative limits and R201. |
| support | [Original anisotropic/all-repeat proof/input](../ledger/Yin_L_G0306_v1.md#complete-retained-proof-and-review) | Complete Sections1--6/equations1--11, actual2026-10-10T08:34 scope clarification, original full J78/source/native/negative limits and R205. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-disclosure-and-all-repeat) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

