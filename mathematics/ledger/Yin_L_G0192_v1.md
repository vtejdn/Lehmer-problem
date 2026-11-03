---
author: Yin
---

# Full original hitting bounds and the infinite excursion-conditioned stationary law

Date: 2026-10-10.
The coordinating AI for Yin adopts the complete D G0058 proof and separate noncontributor review.
The coordinator proposed the hitting-probability bridge; resultant_research developed the complete conditional-law and Green arguments; orbit_research independently checked the entire combined proof.
These contributions are retained below, without relabelling author checks as independent review.

<a id="original-hitting-law-fixed-scope"></a>
## Adopted scope

For each fixed Salem beta in(1,2), the full original hitting law has the explicit exponential neutral-radius upper bound below.
When beta<phi and the complete compact-termination premise holds, L189 gives the matching fixed-input exponential lower scale and linear conditional hitting-time scale with a complete exponential tail.
The original Lehmer input satisfies that premise; no general compact-termination result is adopted here.

On the entire actual return core, the original Green potential gives a genuine infinite stochastic chain by conditioning each excursion on finite return.
Its exact stationary distribution, exceptional zero-row normalization, first-return law f_n/F(1), and full exponential radial tail are proved without finite-prime truncation.
This is an explicitly changed probability law, not the original walk or an infinite critical Perron normalization.

The complete weighted-return identity F(exp c)=exp(c)(1+H_c(1))/2 locates the missing common positive parameter.
The established fixed-input range is only c<gamma_beta<=log beta; every input-uniformity and unrestricted G0001 obligation remains open.
Historical pending-review wording is retained as chronology.
Only heading depth and relative navigation are transformed; no computation or new source belongs to this result.

<a id="retained-original-hitting-law-proof"></a>
## Original-law hitting probabilities and conditional return-time scale

Date: 2026-10-10.
Responsible arithmetic/probability author inquiry by resultant_research for Yin.
The coordinating agent proposed combining the deterministic lower bound n>=rho(x)/sqrt(s), L173's original maximum-atom inequality and its fixed-input exponential collision bound to estimate eventual hitting from a distant neutral state, then pairing this with [L189](Yin_L_G0189_v1.md)'s chosen-path lower bound.
That displayed bridge is a mathematical contribution and is disclosed.
The arithmetic agent verifies it and develops the conditional-law and complete weighted-return consequences directly below.
No new source or computation was needed.

The bounded reuse screen read L173's full-strip and actual-collision interfaces, L189's complete narrow-domain length theorem, L154's full renewal and weighted-tail obligation, L156's genuinely killed exit-law contrast, and the S7 current scope.
No actual hitting-time theorem of this exact form was located in that limited screen; this is not an exhaustive search or a novelty claim.
All original probabilities remain(1/4,1/2,1/4).
Compact termination and input-uniform constants remain explicit rather than inferred.
This is a proof draft awaiting complete noncontributor review, not a fixed result; G0001 remains unresolved.

### Conventions and the fixed-input exponential bound

Fix a Salem beta in(1,2), degree d=2s+2 with s>=1, the actual order O=Z[beta], and one neutral conjugate zeta_j from each pair.
Write

    rho(x)^2=sum_(j=1)^s |x(zeta_j)|^2,
    B=1/(beta-1),  S=beta/(beta-1),
    N={x in O: |x_+|<=1, |x_-|<=S}.

The original ambient process on O is X_(n+1)=beta X_n+eta_n, with independent probabilities p_0=1/2 and p_1=p_(-1)=1/4.
Its n-step zero-to-zero probability is p_n, with p_0=1; digit and time subscripts distinguish these uses.
The actual returning core D consists of states on original finite zero-to-zero words, and K is the original matrix killed outside D.
No equality of D with an ambient strip is assumed.
Every core state lies in |x_+|<B, |x_-|<S.

The fixed [L173 separated-digit bound](Yin_L_G0173_v1.md#separated-digit-strip-norm), its actual-core restriction and its [maximum-atom argument](Yin_L_G0173_v1.md#core-operator-collision-sandwich) give the following explicit constants and inequalities:

    gamma=log2*log(beta)/log(1+beta)>0,
    q=exp(-gamma),  M=floor(2B)+1,
    C_beta=2M exp(gamma),  D_beta=C_beta/(1-q),
    ||K^n||_(2->2)<=C_beta q^n,   p_n<=C_beta q^n  (n>=1),
    Pr_x(X_n=0)<=p_n for every x in O.                  (1)

For the core restriction, every row path is among the original strip paths and the reciprocal edge reversal preserves D, so the same row, column and Schur bound applies.
Alternatively compress each full strip power using positivity.
The last inequality is ambient: the complete displacement law is the autocorrelation of the fair binary sum, whose largest atom is at zero by Cauchy--Schwarz.
It is not a statement about an arbitrarily reweighted digit law.
These fixed interfaces require neither general compact termination nor a newly proved entropy gap.

For x!=0 let tau=inf{n>=1:X_n=0}, and put

    H(x)=Pr_x(tau<infinity),   H(0)=1.

At zero H uses the time-zero hitting convention; positive first returns from zero will be defined separately.
Nonzero order elements have rho(x)>0 because a nonzero field element has no zero conjugate.
Put n_x=ceil(rho(x)/sqrt(s))>=1.

<a id="original-eventual-hit-spatial-bound"></a>
### 1. Upper bounds include every original hitting path

If a word of length n sends x to zero, its neutral displacement c_w satisfies z_x+c_w=0.
Each original digit contributes a vector of norm at most sqrt(s); therefore rho(x)<=n sqrt(s) and n>=n_x.
For each n, the first-hit event is a subset of the endpoint event.
Equation(1) consequently gives, for every x!=0 and every integer N>=1,

    Pr_x(tau>=N, tau<infinity)
       <=sum_(n>=max(N,n_x)) p_n
       <=D_beta q^max(N,n_x),
    H(x)<=min{1,D_beta exp(-gamma n_x)}.               (2)

These are bounds on the entire infinite original-law event, not a chosen word, a finite horizon or a finite-prime restriction.
No reachability of x from zero is required for(2); H may be zero.

For x in N, all words which hit zero obey the usual real-strip legality throughout: stable coordinates are bounded forward under every digit by beta^(-1)S+1=S, and their real coordinates are bounded backward from the final zero by the geometric suffix sum strictly below B.
Thus killing a path on exiting the natural strip removes no such hitting event.
If x belongs to D, every ambient path from x to zero is itself inside D: prepend any actual path from zero to x.
This proves that the hitting probabilities used below agree with the actual-core killed kernel when that kernel is invoked, rather than assuming all ambient states are returning states.

Now also assume beta<phi and the compact-termination premise of [L189](Yin_L_G0189_v1.md#conditional-linear-return-length-and-cost): every actual member of its finite residue has a zero continuation.
L189 supplies positive finite constants A,B_0, depending on this fixed input, such that each x in N has a zero-ending word of length at most A rho(x)+B_0.
Put

    a=A log4,   b=B_0 log4.

Following that one word gives the lower bound, which can now be combined with the full upper bound:

    exp(-a rho(x)-b)<=H(x)
        <=min{1,D_beta exp[-gamma rho(x)/sqrt(s)]}
                       for every nonzero x in N.            (3)

The positive constants can be enlarged harmlessly, so no sign issue arises at small radius.
The original degree-ten Lehmer input satisfies this premise by L170 and L189.
For a general beta<phi the premise remains conditional; without it only(2) is asserted universally.
On the unbounded narrow returning states already proved for Lehmer, -log H(x) is therefore bounded above and below by positive fixed-input multiples of rho, up to additive constants.
The upper hitting exponent has the explicit dimension factor1/sqrt(s), and no uniform conclusion as beta tends to one is implied.

<a id="conditional-original-hitting-time-tail"></a>
### 2. The law conditional on a hit has a linear time scale and a complete tail

Under exactly the additional assumptions for(3), condition the original law from x in N, x!=0, on tau<infinity.
Dividing(2) by the lower bound in(3) gives

    Pr_x(tau>=N | tau<infinity)
       <=min{1,D_beta exp[a rho(x)+b-gamma N]}.        (4)

Define the nonnegative integer

    t_x=ceil([a rho(x)+b+log D_beta]/gamma).

Here D_beta>1 and the chosen constants a,b are nonnegative.
For every integer k>=0,

    Pr_x(tau>=t_x+k | tau<infinity)<=q^k.             (5)

The deterministic lower bound tau>=n_x still holds under this conditioning.
Summing the complete tail, with all terms nonnegative, gives

    rho(x)/sqrt(s)
       <=E_x[tau | tau<infinity]
       <=t_x+q/(1-q)
       <=[a rho(x)+b+log D_beta]/gamma+1+q/(1-q).     (6)

In particular the conditional mean is O_beta(1+rho), and has matching linear order along any allowed sequence with rho tending to infinity.
There is also a radius-independent centered exponential-moment bound.
For 0<theta<gamma, let Y=(tau-t_x)_+.
The integer tail-sum formula and(5) give

    E_x[exp(theta Y) | tau<infinity]
       <=1+(exp(theta)-1)q/[1-exp(theta)q].           (7)

Indeed Pr(Y>k | hit)=Pr(tau>=t_x+k+1 | hit)<=q^(k+1), and summing the geometric series proves(7).
These are bounds for the entire original distribution after the explicitly stated event conditioning, not just a selected trajectory.
On sufficiently large radii(2) makes H(x)<1, so the unconditional extended expectation of tau, with tau=infinity on nonhit paths, is infinite.
Equation(6) does not assert otherwise.

The elementary hit-conditioned transition law can already be written on the co-returnable states: for x!=0 with H(x)>0,

    Q_hit(x,y)=p_eta H(y)/H(x),  y=beta*x+eta,

with zero absorbing and zero contribution when H(y)=0.
The first-step identity H(x)=sum_eta p_eta H(beta*x+eta) makes its row sum one.
Telescoping along a word which first reaches zero at time n gives its original probability divided by H(x).
The first-hit masses therefore sum to one, and this is exactly the original law conditional on eventual hitting.
There is no factor r(K)^(-n) in this transform.

<a id="full-core-green-hit-potential"></a>
### 3. The actual Green potential and reciprocal reversal

This and the next section require only the fixed Salem input beta in(1,2), not compact termination or beta<phi.
By(1) the operator series

    G=sum_(n>=0) K^n=(I-K)^(-1)

converges in l2 operator norm.
Its entries are the complete nonnegative path sums.
Let

    U=G(0,0)=sum_(n>=0)p_n<infinity.

The first positive return time from zero is tau_+=inf{n>=1:X_n=0}, with original masses f_n=Pr_0(tau_+=n).
Define the complete generating functions

    F(z)=sum_(n>=1) f_n z^n,
    U(z)=sum_(n>=0) p_n z^n.

Write F=F(1) and F'=F'(1) when no argument is displayed.
The [L154 complete renewal identity](Yin_L_G0154_v1.md#actual-first-return-paths) gives

    1/2<=F<1,   U=1/(1-F),
    1/2<=F'=sum_n n f_n<infinity.                    (8)

The first moment is finite because f_n<=p_n and(1) is exponentially summable.
All differentiation at z=1 below is justified by convergence in a neighborhood of1, not by a formal critical-radius substitution.

For x in D, decomposing complete x-to-zero visits at the first hit gives

    G(x,0)=H(x)U,
    h:=H|_D=G delta_0/U in l2(D).                    (9)

For x=0 this uses H(0)=1.
For x!=0 the equality follows coefficientwise from first-hit decomposition and then by nonnegative summation, or directly by the strong Markov property.
It implies

    (I-K)h=delta_0/U,
    (Kh)(x)=h(x) for x!=0,    (Kh)(0)=F.             (10)

All h(x) are strictly positive on the actual core because a finite co-return word exists by definition.

The reciprocal additive involution T(x)=beta^(-1)sigma(x), sigma(beta)=beta^(-1), preserves D and the neutral norm rho.
On each neutral conjugate it sends x_j to zeta_j^(-1) conjugate(x_j), so the norm is unchanged.
Reversing an edge replaces its digit by its negative with equal original probability, giving K(Ty,Tx)=K(x,y).
Consequently

    G(0,x)=G(Tx,0)=U h(Tx).                          (11)

This is the precise original-kernel reciprocity used below.
It does not assert ordinary reversibility K(x,y)=K(y,x).

<a id="complete-return-conditioned-excursion-chain"></a>
### 4. Conditioning each complete excursion gives an explicit stationary law

Define a new stochastic matrix on the entire actual core D by

    Q(x,y)=K(x,y)h(y)/h(x)            if x!=0,
    Q(0,y)=K(0,y)h(y)/F.                             (12)

Equation(10) proves every row sum is one.
The zero row is normalized separately; omitting its factor F would leave a substochastic row and would not define the claimed chain.
Every positive original core edge stays positive, so Q is irreducible.
Along an entire first-return excursion from zero, the h factors telescope, while the sole zero-row normalization contributes1/F.
Thus its exact first-return distribution is

    Pr_(Q,0)(tau_+=n)=f_n/F.                         (13)

This is conditioning each original excursion on finite return, not conditioning its time by an exponential weight.
It includes the length-one zero loop.
Its mean return time F'/F is finite, so this is a positive recurrent chain even if D is infinite.
Between successive visits to zero, its path law is precisely the original excursion law conditional on return.

Its stationary probability is explicitly

    pi(0)=F/F',
    pi(x)=h(x)h(Tx)/F' for x!=0.                     (14)

Here is both the normalization and invariance proof, including all infinite sums.
Since h is in l2 and T is a permutation, sum_x h(x)h(Tx) is finite.
Green convolution and(9)--(11), using nonnegative summation and the finite exponential bound, give

    U^2 sum_x h(x)h(Tx)
        =(G^2)(0,0)
        =sum_(n>=0)(n+1)p_n
        =U+U'(1).

Differentiating U(z)=1/(1-F(z)) at1 gives U'(1)=F' U^2.
Hence

    sum_x h(x)h(Tx)=1-F+F',
    F+sum_(x!=0)h(x)h(Tx)=F'.                       (15)

This proves that(14) sums to one.
For invariance, transpose(10) through the T permutation to obtain K^T(h o T)=h o T-delta_0/U.
For y!=0, insertion of(12)--(14) in sum_x pi(x)Q(x,y) yields h(y)(K^T(h o T))(y)/F'=pi(y).
For y=0 it gives (1-1/U)/F'=F/F'=pi(0).
All entries are nonnegative, and the finite total just proved justifies summation.
Thus (14) is indeed invariant and agrees with the mean return time in(13).

The stationary distribution also has a complete exponential neutral-radius tail.
For R>0 put n_R=ceil(R/sqrt(s)).
If rho(x)>=R and K^n(x,0)>0, neutral propagation forces n>=n_R.
Thus, using(1) before summing operator norms,

    ||1_(rho>=R) h||_2
       <=(1/U)sum_(n>=n_R)||K^n delta_0||_2
       <=(D_beta/U)q^n_R.

The same radial set is T-invariant.
Cauchy--Schwarz in(14), followed by F'>=1/2 and U>=1, proves

    pi{rho>=R}
       <=D_beta^2 q^(2n_R)/(U^2 F')
       <=2D_beta^2 exp[-2gamma R/sqrt(s)].           (16)

The probability is also at most one.
This includes the complete infinite state set without using lattice-point growth or a finite-prime truncation.
In particular every positive exponential moment of rho with exponent less than2gamma/sqrt(s) is finite under pi, by the usual nonnegative tail integration.
It makes no degree-uniform or beta-uniform assertion.

The chain(12) changes the law by explicit event conditioning.
Its positive recurrence and stationary tail are not claims about the original unrestricted walk.
Nor is h an eigenvector at the full critical spectral radius: equation(10) has a nonzero point source and eigenvalue one only away from zero.
The finite-core critical Perron transforms in L181/L186 and any proposed infinite critical transform are different objects.
Their normalization and mean-return obligations are not settled by(12)--(16).

<a id="hitting-transform-complete-weighted-return-boundary"></a>
### 5. Exact connection to the outstanding full weighted first-return gate

For x!=0 define the complete weighted first-hit mass

    H_c(x)=E_x[exp(c tau); tau<infinity],  H_c(0)=1.

For every fixed 0<=c<gamma, the same complete summation as in(2) yields

    H_c(x)
       <=C_beta exp[-(gamma-c)n_x]/[1-exp(-(gamma-c))]
                for x!=0.                          (17)

This bound alone gives neither compact termination nor a positive value at a state with no co-return.
On positive finite H_c states, the first-step identity makes exp(c)p_eta H_c(y)/H_c(x) an exactly normalized absorbing first-hit transform away from zero.
Its finite-path weights are the original hitting weights multiplied by exp(c tau)/H_c(x).
This is a deliberately changed law and is proved here only inside the displayed convergence range.

By sign symmetry H_c(-1)=H_c(1).
Decomposing the original first positive return from zero according to its first digit gives the exact extended-value identity

    F(exp c)=(exp c)/2 * [1+H_c(1)].                  (18)

It holds by nonnegative first-hit summation whenever c>=0, with infinity allowed, and contains every late excursion.
At c=0 it agrees with the zero-row normalization in(10)--(13).
A common positive c<log2 would reach the desired first-return gate precisely if one proved

    H_c(1)<2exp(-c)-1                               (19)

throughout the claimed input class.
A mere finite value of H_c(1), or conditioning its associated law to have mass one, is not the inequality(19).

The present fixed-input bounds do ensure F(exp c)<1 for c<gamma: (1) makes U(exp c) finite and L154's exact renewal identity then forces the strict inequality.
They do not improve the known rate scale.
L173 already gives

    gamma<=h_2(beta)<=m=log beta,
    gamma/m=log2/log(1+beta) tending to1 as beta tends to1.

Thus the proved exponential-moment range itself shrinks to zero along a hypothetical near-one Salem sequence.
For c>m with exp c<2, the already retained [L154 complete weighted-tail lower bound](Yin_L_G0154_v1.md#complete-weighted-return-tail-lower-bound) gives F(exp c)>=1.
No legitimate normalization of a conditional law can remove that full original-law obstruction or create a common c.

The improved spatial estimates and the conditional linear time scale are nevertheless genuine full-law consequences at each allowed fixed input.
They control all original hitting paths, identify a well-defined infinite return-conditioned process and its exact stationary distribution, and locate the missing uniform assertion in(19).
They do not imply compact termination for every small Salem beta, a full-critical normalization at c=h_2, original-law negative quadratic drift, or the unrestricted Lehmer gap.
The rate constants, the factor sqrt(s), and the possibly very large L189 chosen-control constants remain visible.

### 6. Contribution, self-check and review boundary

The coordinator supplied the candidate joining the deterministic minimum length, maximum-atom collision bound and exponential summation to an eventual-hit upper bound, and its comparison with L189's selected-path lower bound.
The arithmetic agent checked that bridge and derived the explicit complete conditional time tail and mean, the absorbing hit transforms, the reciprocal Green-potential identities, the full excursion-conditioned chain, its stationary normalization and radial tail, and the exact comparison with the complete weighted first-return gate.
These contributions are separated; a coordinator check alone would not be a noncontributor review of the combined result.

Self-check covered the original ambient versus actual-core path sets, nonzero/time-zero conventions, complete rather than truncated infinite sums, neutral finite propagation, every floor and tail offset, the conditional expectation and exponential-moment identities, preservation of rho under T, Green entry/transpose orientation, the exceptional zero-row normalization, the derivative identity(15), l2 tail projection before operator-norm summation, all conditional termination assumptions, and the direction and range of the weighted-return criterion.
The source inputs are precisely fixed L173/L189/L154 interfaces; no new external source, numerical test or J is needed.
Complete separate noncontributor review is pending.
G0001 remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0091_v1.md#complete-separate-noncontributor-proof-review), with its original inspected scope and relationship.

## Retention and review bindings

The [complete noncontributor finding](../audits/reviews/Yin_R_G0091_v1.md#original-hitting-law-independent-review) covers the entire [retained proof](#retained-original-hitting-law-proof), including all original paths, nonzero and time-zero conventions, strip boundaries, conditional tails and moments, infinite Green sums, reciprocal orientation, stochastic normalization, stationarity and the weighted gate.
Its author's earlier contributions to already fixed foundations are disclosed and are not represented as new independent re-audits of those foundations.

The complete D G0058 argument and its noncontributor finding are retained here at their original scopes.
Fixed adoption does not complete the Task.
