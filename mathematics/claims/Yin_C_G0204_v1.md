---
author: Yin
---

# Complete original midpoint convergence, finite capture and critical-mean alternatives

## Current assessment
[Selected decision](#decision-sufficient-covariance-home)

## Statement

<a id="midpoint-capture-fixed-scope"></a>

Fix the actual Salem quartic P(t)=t^4-t^3-t^2-t+1, its expanding root beta and one unit-circle conjugate zeta.
Use its entire actual zero-to-zero core D in O=Z[beta] and the ORIGINAL independent digit law p_0=1/2, p_1=p_(-1)=1/4, without deleting earlier zero visits or replacing original chronological time.
Let K(x,beta*x+eta)=p_eta on that core, p_n=K^n(0,0), and f_n the complete original first-positive-return probabilities.
R is the TRUE exponential return radius, with the established recurrence F(R)=sum_(n>=1)f_n R^n=1 and 2^(5/8)<=R<=beta<7/4; no identity R=beta is assumed.
Use the fixed complete first-hit harmonic functions H,L and occupation sigma of the [exact original setting](#actual-midpoint-occupation-reuse), so

    H(0)=L(0)=1, 0<H(x),L(x)<=1,
    Q(x,y)=R K(x,y)H(y)/H(x),
    sigma(x)=H(x)L(x), mu=sum_D sigma=sum_(n>=1)n R^n f_n in[1,infinity].

Q is the established recurrent irreducible chain with Q(0,0)=R/2>0.
For n>=1 put

    A_n(x)=K^n(0,x)/p_n, B_n(x)=K^n(x,0)/p_n,
    w_n(x)=A_n(x)B_n(x), D_n=p_(2n)/p_n^2=sum_D w_n,
    b_n(x)=w_n(x)/D_n.

b_n is the COMPLETE original state at chronological midpoint n conditioned on return at 2n.

**Finite-mean branch.** If mu<infinity, pi=sigma/mu is the stationary probability, and for every fixed x in D,

    A_n(x)->L(x)=H(Jx), B_n(x)->H(x), D_n->mu,
    sum_D |w_n(x)-sigma(x)|->0, ||b_n-pi||_TV->0,
    Jx=beta^(-1)iota(x), iota(beta)=beta^(-1).

The full fixed-word conditional probabilities converge as in equation (12), including each complete forced suffix and its original clock/weight cost (13).
Convergence is uniform on a fixed finite collection only; no joint limit for growing state, word length or degree is asserted.

At this actual recurrent quartic the following are equivalent: mu<infinity; D_n is bounded for all sufficiently large n; the all-late complete midpoint family is tight on the discrete actual core; and some ONE finite F subset D, delta>0 and finite N satisfy b_n(F)>=delta for EVERY n>=N.
The last condition gives mu<=|F|/delta.

Set B=1/(beta-1), S=beta B, b=B/beta, rho(x)=|x(zeta)| and C_r={x in D: |x_+|<=b, rho(x)<=r}.
Each C_r is finite, with both real embeddings still in their full original strip.
Equivalently, mu<infinity iff some finite r,N satisfy b_n(C_r)>=1/2 for EVERY n>=N; then mu<=2|C_r|.
For the real embedding matrix M whose jth column is (beta^j,beta^(-j),Re(zeta^j),Im(zeta^j))^t, j=0,...,3, put W=M^(-1).
With a_j=|W_(j,1)|b+|W_(j,2)|S and b_j=|W_(j,3)|+|W_(j,4)|, all four coefficient costs remain in

    |C_r|<=prod_(j=0)^3[2 floor(a_j+b_j r)+1].

**Unconditional original-time occupation.** For ANY N>=1 let E_N denote the complete original law conditioned on X_N=0, and V_N count central departure times k=0,...,N-1 with |(X_k)_+|<=b.
In E_N V_N below E_N denotes expectation, not the separate geometric expense Ebox_N.
For either mean branch,

    (E_N V_N)/N>=max{1/2, 1/C_R-log(Ebox_N)/(Nlog4)},
    C_R=log4/log(4/R)<7/4,
    Ebox_N=C_non[2+sqrt(2pi N)]^2,
    liminf_(N->infinity)(E_N V_N)/N>=1/C_R>4/7.

C_non is the full fixed-input nonneutral factor of the used same-kernel norm estimate; the exponent two retains both real neutral coordinates.
This is expected occupation at an averaged original time on an INFINITE central slab, not fixed-midpoint capture in a finite neutral box.

**Infinite-mean branch.** mu=infinity iff there exists ONE subsequence n_j->infinity such that b_(n_j)(F)->0 for EVERY fixed finite F subset D.
In the forward direction one can choose D_(n_j)->infinity, giving b_(n_j)(F)<=|F|/D_(n_j) simultaneously for all finite F, and hence escape of every fixed neutral-radius box along that same subsequence.
Neither D_n->infinity nor escape at every sufficiently late time is proved.
The actual quartic mean, a quantitative uniform mixing/onset estimate and near-one varying-input uniformity remain unresolved.

## Argument

The following complete Sections 1-6 retain every original-law formula (1)-(22), the full classical coupling proof, all geometric/clock costs and the finite/infinite branch limitations.
The classical convergence attribution remains at the actual selected LL10 scope; the qualitative proof is local, with no quantitative mixing or null-recurrence limit theorem imported.

<a id="actual-midpoint-occupation-reuse"></a>
### 1. Reuse and the actual original quantities

The repository entry, applicable knowledge-reuse/source rules and current assigned scope were read.
The bounded local screen examined the complete critical occupation and reciprocal interfaces of [L236](../ledger/Yin_L_G0236_v1.md#critical-fourier-positive-occupation), [L240](../ledger/Yin_L_G0240_v1.md), the true-radius recurrence in [L285](../ledger/Yin_L_G0285_v1.md#actual-critical-return-fixed-scope), the exact midpoint overlap and its one-way sufficient mean criterion in [L293](../ledger/Yin_L_G0293_v1.md#bounded-doubling-critical-mean-test), and the complete original/central clock comparison in [L322](../ledger/Yin_L_G0322_v1.md#central-clock-comparison-fixed-scope).
The latest [L324](../ledger/Yin_L_G0324_v1.md#central-affinity-fixed-scope) supplies the true-H square-root row identity and its strict boundary: a continuous real-coordinate weight alone cannot uniformly contract the complete central tail.
No such failed real-weight hypothesis is reinstated here.

The changed object is the COMPLETE midpoint distribution of an ORIGINAL returned word.
L293 deliberately avoided a pointwise renewal-limit theorem, and its corrected proof did not assert that finite critical mean makes its overlap bounded.
The classical missing convergence step is available in the already registered Lawler--Limic book: its retained author PDF, printed/PDF p.271, states countable irreducible aperiodic positive-recurrent transition convergence immediately before Proposition12.4.2.
Printed/PDF p.275 gives the coupling/total-variation framework.
Those statements were directly text-read.
Section2 below supplies a complete elementary proof for the needed positive-mean branch.
This is classical convergence, attributed to [LL10's precise selected scope](../audits/literature/LL10/readme.md#countable-convergence-attribution), not a new general Markov-chain theorem.
No quantitative mixing proposition, uniform Doeblin condition, infinite-mean renewal limit or source's maximal-coupling proof is imported.

Fix the actual primitive quartic

    P(t)=t^4-t^3-t^2-t+1, beta>1 its Salem root,
    O=Z[beta], D={actual zero-to-zero original states}.

All digits are ORIGINAL independent digits, with probability1/2 at0 and1/4 at each of+1,-1.
Set

    S_n=sum_(j=0)^(n-1) eta_j beta^j,
    m_n(x)=Pr(S_n=x), p_n=m_n(0), p_0=1,
    R=exp(h_2), a_n=R^n p_n,
    F(z)=sum_(n>=1) f_n z^n, mu=sum_(n>=1)n R^n f_n.       (1)

Here f_n is the complete original probability of a first positive return to zero at time n.
The notation m_n is a probability function, not logarithmic Mahler measure.
Write x_+,x_- for evaluation at beta,beta^(-1), choose one unit-circle conjugate zeta, and put rho(x)=|x(zeta)|, keeping both real neutral coordinates.
K is the ORIGINAL kernel K(x,beta*x+eta)=Pr(eta) restricted to D.
Every path between core endpoints stays in D, since the two missing endpaths can be attached.
Thus

    K^n(0,x)=m_n(x), K^n(x,0)=m_n(beta^n x), x in D.      (2)

L285 proves F(R)=1 for this actual quartic, without identifying R with beta.
The retained bounds are 2^(5/8)<=R<=beta<7/4.
L236 gives the complete first-hit harmonic function H, its dual L, and unnormalized excursion occupation sigma:

    H(0)=L(0)=1, 0<H(x),L(x)<=1 on D,
    Q(x,y)=R K(x,y)H(y)/H(x),
    sigma(x)=H(x)L(x), sum_D sigma=mu in[1,infinity].       (3)

The entire Q is recurrent and irreducible; Q(0,0)=R/2>0.
For finite mu, pi=sigma/mu is its stationary probability and pi(0)=1/mu.
Write Jx=beta^(-1) iota(x), where iota(beta)=beta^(-1).
This is the actual additive involution of O, preserves D and neutral radius, and L(x)=H(Jx).
These are fixed L240 premises, not new symmetry assumptions H=L.
The problem whether mu is finite remains open at this input before and after the results below.

Define the finite observables, for n>=1,

    A_n(x)=K^n(0,x)/p_n, B_n(x)=K^n(x,0)/p_n,
    w_n(x)=A_n(x)B_n(x),
    D_n=p_(2n)/p_n^2=sum_(x in D)w_n(x),
    b_n(x)=w_n(x)/D_n
          =K^n(0,x)K^n(x,0)/p_(2n).                       (4)

Here b_n is a probability on D: it is the actual state at original chronological time n, conditioned on a return to zero at time2n.
It is not an iid surrogate or the separately normalized central chain.
Autocorrelation of fair binary endpoint counts gives m_n(x)<=p_n for every x, so

    0<=A_n(x),B_n(x)<=1, 0<=w_n(x)<=1,
    w_n(0)=1, D_n>=1.                                     (5)

Everything in(4) is determined by complete finite ORIGINAL word probabilities; no R,H or numerical approximation is needed to define it.
The support has at most3^n states, but no claim of practical uniform complexity is made.
No program or J is used here.
Root supplied the broad question only; orbit_research's role was bounded source-locator checking, with no contribution to the arguments below.

<a id="positive-branch-coupling-proof"></a>
### 2. Complete classical positive-branch convergence, with no mixing-rate claim

We record the precise elementary argument to avoid hiding a uniformity or tail assumption.
Total variation here is one half of counting l1 distance between probability laws.
Let T be an irreducible stochastic matrix on a countable set E, with a state o satisfying T(o,o)>0, and with an invariant probability v positive at every state.
Then

    ||T^n(x,.)-v||_TV ->0 for every fixed x in E.           (6)

First, any irreducible chain possessing such a v is recurrent.
If o had return probability r<1, its expected number of visits starting at o would be1/(1-r).
From any x the expected number of visits to o is at most this value, by first hitting o.
Consequently T^n(x,o)->0 for every x.
Stationarity and bounded convergence against the probability v would give

    v(o)=sum_x v(x)T^n(x,o)->0,

a contradiction.
Thus o is recurrent.
Any fixed path from o to x has positive probability; applying the Markov property at repeated returns to o, or at a subsequence of returns separated by that finite path length, shows that x is reached almost surely from o.
A return path from x to o also has hitting probability one: otherwise following an o-to-x path and then avoiding o would give a positive probability of eventual nonreturn from o.
This proves recurrence and mutual almost-sure hitting at all states.
No finite expected hitting time is asserted by this paragraph.

The product chain T tensor T has invariant probability v tensor v, and is irreducible in this setting.
Indeed, each coordinate can travel through o between any pair of prescribed endpoints.
A sufficiently long common total length can be obtained by inserting o-to-o loops independently in the two coordinate paths.
Their two positive path probabilities multiply.
The preceding recurrence argument therefore applies to the product chain, so the hitting time M of(o,o) is almost surely finite from every fixed pair of initial states, and hence also from(x,Y_0) with Y_0 distributed as v.

Run the two copies independently until their first simultaneous visit to(o,o), and identically thereafter.
Both marginal chains still have transition T, while the second remains stationary.
The elementary coupling inequality gives

    ||T^n(x,.)-v||_TV <=Pr_(x,v)(M>n)->0.                 (7)

This proves(6).
The displayed bound is a full product-chain hitting probability, not a claimed explicit rate.
Its finite almost-sure value supplies no input-uniform moment or mixing-time estimate.

For Q in(3), finite mu supplies precisely v=pi.
Irreducibility follows from actual paths through zero and the loop Q(0,0)>0 pads lengths as required.
Consequently

    Q^n(x,y)->pi(y) for all fixed x,y in D,
    ||Q^n(x,.)-pi||_TV->0,
    a_n=Q^n(0,0)->1/mu.                                  (8)

The proof uses neither an external renewal-limit theorem nor a stationary probability in the infinite-mean branch.
It does not silently use a product-chain stationary probability before assuming mu finite.

<a id="true-harmonic-ratio-limits"></a>
### 3. True H ratios and full original midpoint occupation in the finite branch

The Doob telescoping identity is exact at every original time:

    Q^n(x,y)=R^n K^n(x,y)H(y)/H(x).                       (9)

Assume in this section that mu<infinity.
Combining(8)--(9) yields

    B_n(x)->H(x), A_n(x)->L(x)=H(Jx),
    w_n(x)->sigma(x), D_n=a_(2n)/a_n^2->mu.              (10)

For example, B_n(x)=H(x)Q^n(x,0)/Q^n(0,0).
Also A_n(x)=Q^n(0,x)/[H(x)Q^n(0,0)], whose limit is mu*pi(x)/H(x)=L(x).
Every denominator is positive.
The transition convergence concerns each FIXED state; it is not uniform over an expanding set of large neutral states.

More strongly, the FULL midpoint densities converge in counting l1:

    sum_D |w_n(x)-sigma(x)| ->0,
    ||b_n-pi||_TV ->0.                                  (11)

To verify the first conclusion without interchanging an unbounded sum, let F be a finite subset of D with sum_(D\F)sigma<epsilon.
On F there is termwise convergence.
Since sum w_n=D_n->mu=sum sigma, the mass of w_n outside F tends to the corresponding sigma mass.
Splitting the absolute difference into F and its complement therefore gives limsup at most2epsilon.
Let epsilon decrease to zero.
Normalization by D_n->mu>0 proves the second assertion.
This is convergence of the COMPLETE original bridge mass, including all paths which visit zero earlier; it is not merely convergence of individual matrix entries.

An exact row approximation now follows.
Fix y in the actual central set C, an allowed marked central label eta, its original digit segment v of length l=l_eta(y), and endpoint z=z_eta(y).
Let p(v) be the product of its original digit probabilities, including its complete forced nonzero suffix.
Under the original law from y conditioned to be at zero after n+l original steps, the event that its first l digits are exactly v has probability

    q_(v,n)(y)=p(v)K^n(z,0)/K^(n+l)(y,0)
              -> R^l p(v)H(z)/H(y)=q_eta(y).            (12)

For all sufficiently large n the denominator is positive by actual reachability and zero loops; indeed finite positive mean proves its positive asymptotic.
The left side uses exactly the original law and a fixed complete digit segment, not an independently selected mask or an uncharged central step.
Formula(12) is valid for any fixed actual finite word, not only a central label.

For central labels L319 gives

    p(v)=4^(-l)2^(1_(eta=0)),
    l<=1+L_b(rho(y)+1),
    L_b(r)=1+log_+[(2S/beta)(r+c0)^2]/log beta,          (13)

where B=1/(beta-1), S=beta B and c0=1/|zeta-1|.
This retains every real-boundary delay and original clock weight.
Convergence in(12) is uniform over any FIXED finite collection of such words, but neither (7) nor this argument provides a rate uniform in y, l, input degree, neutral radius or small Mahler measure.
In particular it does not settle whether the tail rows on L324's actual two-label patch stay separated from(2/3,1/3).
Using(12) for y=y_n escaping with n would require new uniform control.

<a id="complete-midpoint-tightness-test"></a>
### 4. A radius-free complete central capture discriminator

The preceding limits turn a qualitative Markov fact into an ORIGINAL-law arithmetic test with a quantitative mean consequence.
A family of probabilities is tight on this discrete set if for every epsilon>0 a single finite set captures at least1-epsilon of every probability in the family.
The following four statements are equivalent at the actual quartic:

    (i)   mu<infinity;
    (ii)  sup_(n>=N) D_n<infinity for some finite N;
    (iii) {b_n:n>=N} is tight on the discrete actual core
          for some finite N;
    (iv)  there exist a finite F subset D, delta>0 and N
          such that b_n(F)>=delta for EVERY n>=N.        (14)

The direction(i)=>(ii) is new relative to L293's deliberately one-way proof and follows from(10).
That source proves(ii)=>(i) using its complete dyadic identity and Abel argument, with recurrence a consequence even in a wider setting.
The limit(11) proves(i)=>(iii); a convergent probability sequence on a countable set is tight, by a finite-set split.
Tightness gives(iv), for example with delta=1/2.
Finally (5) gives the explicit finite-state inequality

    D_n b_n(F)=sum_(x in F)w_n(x)<=|F|.

Hence(iv) implies D_n<=|F|/delta at every n>=N, and the existing L293 theorem gives

    mu<=|F|/delta.                                     (15)

This estimate is quantitative although the all-late hypothesis has not been verified at the quartic.
It does not assume recurrence in this last implication: for any original input where (4)--(5) hold, such a hypothesis first proves recurrence and then the mean bound by L293.
For a transient critical chain, the potentially finite derivative RF'(R) alone is not the positive recurrence condition(i).

On the quartic one may restrict the capture set to a FINITE CENTRAL box and fix a numerical capture fraction.
Put

    C={x in D:|x_+|<=b}, b=B/beta,
    C_r={x in C:rho(x)<=r}, N_r=|C_r|.

The full real strip is |x_+|<B, |x_-|<S.
Since O is an actual rank-four Minkowski lattice, each C_r is finite and contains zero.
L322 proves pi(C)>=1/C_R>4/7 whenever mu is finite, with C_R=log4/log(4/R)<7/4.
Therefore some fixed r has pi(C_r)>1/2.
Applying(11), enlarging the original time onset if needed and keeping a margin strictly below pi(C_r), proves

    mu<infinity
      iff there exist finite r,N such that
             b_n(C_r)>=1/2 for EVERY n>=N.
    Under this hypothesis, mu<=2N_r.                   (16)

The strict pi(C_r)>1/2 is what makes the non-strict eventual bound1/2 valid.
This is a fixed central neutral radius, not the entire unbounded central slab, and b_n still records ORIGINAL chronological midpoint time n rather than central time.
Thus the complete clock comparison is paid before choosing the finite capture test.
No bound on just one compressed row or on a killed finite-core stationary law is substituted.

There is a fully explicit, if coarse, field/height cost for N_r.
Let M be the real4 by4 embedding matrix whose jth column, j=0,1,2,3, is

    (beta^j, beta^(-j), Re(zeta^j), Im(zeta^j))^T,

and write W=M^(-1), which exists because the four conjugates are distinct.
For x=sum_(j=0)^3 c_j beta^j in C_r, every integer coefficient satisfies

    |c_j|<=a_j+b_j r,
    a_j=|W_(j,1)|b+|W_(j,2)|S,
    b_j=|W_(j,3)|+|W_(j,4)|.

Consequently

    N_r<=prod_(j=0)^3 [2 floor(a_j+b_j r)+1].            (17)

The coordinate labels1--4 in W refer to the displayed real embedding coordinates, while coefficient j runs0--3.
The use of both Re and Im bounded by rho is conservative and valid; no single neutral coordinate or real boundary has disappeared.
Formula(17) is an explicit fixed-quartic O((1+r)^4) bound, not an optimal slab count or degree-uniform estimate.
The exact N_r or a sharper independently certified count can replace it without altering(16).

<a id="unconditional-return-bridge-central-clock"></a>
### 5. An unconditional original-bridge central occupation bound

There is also a useful actual-row constraint which does not assume finite mean.
Fix ANY N>=1 and condition the complete ORIGINAL length-N path from zero on X_N=0.
Denote this finite probability law by P_N and expectation by E_N.
At an observed state x at time k<N, its next-digit distribution is

    r_(k,N)(eta|x)
      =p_eta K^(N-k-1)(beta*x+eta,0)/K^(N-k)(x,0).       (18)

Only states with positive denominator are visited under P_N; impossible digits have probability zero.
Every returned path lies in the actual core.
At a noncentral state the L319 unique legal digit is nonzero, so that row is deterministic even under P_N.
At a central state, for its possibly time-dependent row r, put

    e(r)=-sum_eta r_eta log r_eta+r_0 log2
         =log4-D(r||p), 0<=e(r)<=log4,                  (19)

where p=(-1:1/4,0:1/2,+1:1/4), with0log0=0.
The relative entropy D(r||p) is nonnegative, since log u<=u-1 applied on the positive support gives this elementary inequality.
The lower bound in(19) follows directly from its first expression.
This is the same three-digit entropy inequality used in L322, now applied to the actual finite-horizon rows(18), not to Q or to a stationary approximation.

Let Z count all zero digits of the length-N path and V_N=sum_(k=0)^(N-1)1_(X_k in C) count its CENTRAL departure visits, including X_0=0.
Each path's original probability is4^(-N)2^Z.
Hence its conditional information -log P_N(path) equals Nlog4-Zlog2+log p_N.
The elementary finite entropy chain rule, proved by factoring each path probability into its conditional rows, and the deterministic noncentral rows give the exact identity

    cN+log a_N
      =Nlog4+log p_N
      =sum_(k=0)^(N-1) E_N[1_(X_k in C)e(r_(k,N)(.|X_k))]
      <=log4 E_N V_N, c=log(4/R).                      (20)

Every sum is finite: there are at most3^N original words.
No integrability of log H, stationary occupation, first-return time or an infinite entropy is involved.
These are ALL returned words, with earlier zero visits retained.
The zero digits of the original path occur only on central departures, which is why no zero-digit reward is dropped in(20).
Original time N, not compressed central time, is fixed throughout.

Since p_N>=2^(-N) by the all-zero word, (20) implies E_N V_N>=N/2 at EVERY N.
For the sharper true critical asymptotic, reuse the complete [C432 actual-core covariance expense](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm), the same mathematical interface used from L255 through L293/L285:

    1>=a_N>=1/Ebox_N,
    Ebox_N=C_non[2+sqrt(2pi N)]^2.

Here the exponent2 is the actual real neutral dimension of this quartic, and C_non is the full fixed-input nonneutral lattice factor of that theorem.
Combining with(20) gives

    (E_N V_N)/N >= max{1/2,
                1/C_R-log(Ebox_N)/(Nlog4)},
    liminf_(N->infinity)(E_N V_N)/N >=1/C_R>4/7.         (21)

This conclusion is unconditional at the actual quartic, including either possible critical-mean branch.
It retains the complete finite normalization loss log(Ebox_N), and makes no claim that R is beta or that C_non is degree-uniform.
Equivalently, if a time is chosen uniformly from0,...,N-1 independently AFTER sampling the returned path, its state has the displayed central capture lower bound.
It is NOT a fixed-midpoint statement, and C is an infinite neutral slab.
Neither its averaged time choice nor its unbounded spatial set meets the finite fixed-midpoint hypothesis(16).
Thus the true null branch in Section6, if realized, can escape in neutral space while still spending a positive fraction of original return time in the central real strip.
No concentration or finite neutral-box capture follows merely from (21).

<a id="null-branch-original-bridge-escape"></a>
### 6. A genuine null-branch escape conclusion and its exact limitation

If mu=infinity at this already recurrent quartic, the contrapositive of L293 gives an unbounded sequence D_n.
Each individual D_n is finite, so there is a subsequence n_j tending to infinity with D_(n_j)->infinity.
From(5), for EVERY finite F subset D,

    b_(n_j)(F)<=|F|/D_(n_j)->0.                         (22)

The same subsequence works simultaneously for all finite F.
Since the entire actual core has both real embeddings bounded, the sets D_r={x in D:rho(x)<=r} are finite and exhaust D.
Thus the original midpoint of a length2n_j returned word escapes in neutral radius in probability: for each fixed r, b_(n_j)(D_r)->0.
This is an actual ORIGINAL return-conditioned tail statement, with the full inverse/core arithmetic already imposed.
It is not a freely chosen measure on the same geometric strip.

Conversely, if a subsequence of these actual bridges escapes every finite set, mu cannot be finite, by the total-variation limit(11).
As recurrence is separately known, it follows that mu=infinity.
Equivalently, failure of tightness of the complete family is a true finite-versus-infinite mean discriminator here.
This does NOT claim that every null-recurrent bridge escapes at every late time, nor that D_n tends to infinity rather than merely having unbounded limsup.
Those stronger conclusions require additional return regularity not proved in this argument.

The argument also distinguishes an actual finite-state capture certificate from an early plateau.
A finite list of n, a bound depending on n, or capture on a box whose radius is allowed to grow without control does not meet(16).
The actual golden radical family in L293 has a long perfectly flat early D_n profile followed by exponentially large degree-scale values, even though each member has finite mean; this remains a relevant cost control, not a counterexample to the fixed-input equivalence(14).
No fixed-input onset or quantitative mixing rate was extracted from that family or from(7).

## Assessment history

### Decision retained-results

| Field | Value |
| --- | --- |
| date | 2026-10-20T22:11 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact branch theorem](#statement) | Actual recurrent quartic only, complete original midpoint law, exact finite-mean equivalences, unconditional averaged occupation and one common null-branch subsequence; no actual mean classification. |
| argument | [Complete argument](#argument) | Complete original Sections 1-6 and equations (1)-(22), product-chain coupling, fixed-state H/L ratios, full l1 mass, finite-set/central-box costs, finite bridge entropy and exact escape quantifiers. |
| dependency | [Critical occupation](../ledger/Yin_L_G0236_v1.md#critical-fourier-positive-occupation) | Complete first-hit H/L and unnormalized sigma, with infinite total mass permitted and stationary probability only in the finite-mu branch. |
| dependency | [Reciprocal actual core](../ledger/Yin_L_G0240_v1.md) | Actual additive involution, original kernel and L(x)=H(Jx), not an added H=L symmetry. |
| dependency | [True-radius recurrence](../ledger/Yin_L_G0285_v1.md#actual-critical-return-fixed-scope) | Established F(R)=1 and charged true-radius interval at the actual quartic; no R=beta premise. |
| dependency | [Overlap-to-mean implication](../ledger/Yin_L_G0293_v1.md#bounded-doubling-critical-mean-test) | Exact all-late bounded complete overlap implication, its dyadic/Abel proof and quantitative mean constant, not a finite-time certificate. |
| dependency | [Full same-kernel norm expense](../ledger/Yin_L_G0255_v1.md#full-covariance-state-cost-fixed-scope) | Full fixed-input nonneutral C_non and both real neutral coordinates in Ebox_N, without a degree-uniform constant. |
| dependency | [Actual central words](../ledger/Yin_L_G0319_v1.md#actual-forced-boundary-segments) | Unique nonzero boundary digits, all forced original lengths and digit probabilities. |
| dependency | [Paid central clock](../ledger/Yin_L_G0322_v1.md#central-count-complete-clock-comparison) | Finite-mean pi(C)>=1/C_R>4/7 at its actual normalization; no stationary law in the null branch. |
| review | [Original author check](../audits/reviews/Yin_R_G0496_v1.md#midpoint-occupation-author-self-check) | Actual 2026-10-10 complete author self-check recorded before the 2026-10-10T11:29 freeze, with no invented checking instant or independent relationship. |
| review | [Complete disclosed-context account](../audits/reviews/Yin_R_G0154_v1.md#midpoint-occupation-complete-independent-review) | Actual 2026-10-10T11:36 whole mathematical check, with shared author progress and the consumed prior clock/probability development disclosed as self-review under the current context rule. |
| review | [Retained interface check](../audits/reviews/Yin_R_G0496_v1.md#retained-midpoint-interface-check) | Current exact statement/proof retention and input-interface check, preserving finite/infinite, fixed-state/all-state and averaged-time/fixed-midpoint distinctions; no computation or independent re-review. |

### Decision sufficient-covariance-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:45 |
| status | proved |
| reason | Use the adopted complete C432 proof for the identical L255 full same-kernel Ebox_N=C_non[2+sqrt(2pi N)]^2 interface in equation21. Its exact original quartic/unit/core/N domain, all nonneutral and clock costs and whole SELF evidence were read. All midpoint/mean/occupation mathematics, every other input tuple and selected existing review remain unchanged; old dated decisions/R/L reading inputs retain their actual scopes, and no new convergence or recurrence assertion is added. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact branch theorem](#statement) | Actual recurrent quartic only, complete original midpoint law, exact finite-mean equivalences, unconditional averaged occupation and one common null-branch subsequence; no actual mean classification. |
| argument | [Complete argument](#argument) | Complete original Sections 1-6 and equations (1)-(22), product-chain coupling, fixed-state H/L ratios, full l1 mass, finite-set/central-box costs, finite bridge entropy and exact escape quantifiers. |
| dependency | [Critical occupation](Yin_C_G0563_v1.md#critical-fourier-positive-occupation) | Complete first-hit H/L and unnormalized sigma, with infinite total mass permitted and stationary probability only in the finite-mu branch. |
| dependency | [Reciprocal actual core](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Actual additive involution, original kernel and L(x)=H(Jx), not an added H=L symmetry. |
| dependency | [True-radius recurrence](Yin_C_G0526_v1.md#actual-critical-return-fixed-scope) | Established F(R)=1 and charged true-radius interval at the actual quartic; no R=beta premise. |
| dependency | [Overlap-to-mean implication](Yin_C_G0555_v1.md#bounded-doubling-critical-mean-test) | Exact all-late bounded complete overlap implication, its dyadic/Abel proof and quantitative mean constant, not a finite-time certificate. |
| dependency | [Full same-kernel norm expense](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Full fixed-input nonneutral C_non and both real neutral coordinates in Ebox_N, without a degree-uniform constant. |
| dependency | [Actual central words](Yin_C_G0601_v1.md#actual-forced-boundary-segments) | Unique nonzero boundary digits, all forced original lengths and digit probabilities. |
| dependency | [Paid central clock](Yin_C_G0593_v2.md#central-count-complete-clock-comparison) | Finite-mean pi(C)>=1/C_R>4/7 at its actual normalization; no stationary law in the null branch. |
| review | [Original author check](../audits/reviews/Yin_R_G0496_v1.md#midpoint-occupation-author-self-check) | Actual 2026-10-10 complete author self-check recorded before the 2026-10-10T11:29 freeze, with no invented checking instant or independent relationship. |
| review | [Complete disclosed-context account](../audits/reviews/Yin_R_G0154_v1.md#midpoint-occupation-complete-independent-review) | Actual 2026-10-10T11:36 whole mathematical check, with shared author progress and the consumed prior clock/probability development disclosed as self-review under the current context rule. |
| review | [Retained interface check](../audits/reviews/Yin_R_G0496_v1.md#retained-midpoint-interface-check) | Current exact statement/proof retention and input-interface check, preserving finite/infinite, fixed-state/all-state and averaged-time/fixed-midpoint distinctions; no computation or independent re-review. |

