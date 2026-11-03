---
author: Yin
---

# Dimension-free small-ball bounds and stationary diffusion-scale escape

The current exact theorem and complete argument are [C531](../claims/Yin_C_G0531_v1.md#statement), with its actual current selection at that responsible C.
The [current complete independent finding](../audits/reviews/Yin_R_G0793_v1.md#small-ball-current-independent) records the new isolated inspection of the entire current mathematical input.
The [earlier complete whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g220-whole-self-finding) and [complete original author account](../audits/reviews/Yin_R_G0735_v1.md#original-g220-author-self-finding) retain their distinct actual dates and scopes.
The [original R793 whole](../audits/reviews/Yin_R_G0793_v1.md#small-ball-excursion-complete-independent-review) keeps its original frozen L/J/source inputs, conclusions and reading/execution limits; its missing relationship declaration does not establish isolation or shared target mathematics.


Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="small-ball-quantile-fixed-scope"></a>
## Original restricted scope and mathematical limits

A reproduced classical Hilbert-space separated-sum argument gives a dimension-free block small-ball estimate for the original three-digit noise.
Charging the full original path information yields necessary positive-mass stationary radii of order sqrt(s/I), uniformly over actual units with s selected unit-circle embeddings, without finite-moment or finite-support assumptions.
For I<=2m it gives vanishing mass at every radius o(sqrt(s/m)), removing L216's logarithmic loss.
A precise excursion-occupation and size-biased-time consequence is proved.
An actual alpha=-1 stationary control realizes that scale at low information cost, so an additional nontorsion arithmetic or return constraint is still required; units with no unit-circle embeddings and the unrestricted gap remain outside this conclusion.


<a id="complete-retained-proof-and-review"></a>
## Complete retained original author argument

## Excursion occupation under stationary quantile escape

Date: 2026-10-10.
Starting question: Investigate whether L216 bulk radial escape yields a stronger necessary actual excursion-time or information cost through L201/L212.
Seek a fully charged occupation-return constraint or a concrete discriminator, without assuming attainment, uniform tails, or a second-moment-to-probability implication.



### Reuse, source and changed mechanism

[L216](Yin_L_G0216_v1.md#stationary-quantile-fixed-scope) obtained a near-one stationary probability bound by repeated finite-quotient mixing, Shannon entropy and integer-norm counting.
Its radius was sqrt(s)/(sqrt(m)(log(1/m))^A) for fixed A>1/2.
The present route instead bounds the original neutral displacement directly, uniformly in dimension and the starting state, and then charges the full stationary path information.
This removes the logarithmic restriction, yields a positive-quantile lower bound on the scale sqrt(s/I), and applies beyond Salem inputs whenever unit-circle embeddings are present.
The excursion question then receives a rigorous occupation consequence without converting it into an unsupported mean-return or gap assertion.

A bounded local screen of the retained G ledgers found the existing inverse-concentration, rank/time and finite-quotient bounds, but not this direct block small-ball deduction.
This is not a literature-wide novelty claim.
The geometric subset-sum mechanism is classical Kleitman, verified in the primary-author exposition [GK78, Section9, printed74--76](../literature/pdf/GK78.pdf).
[GK78-U001](../audits/literature/GK78/Yin_U001.md#gk78-u001) records the exact strict-diameter convention, dimension independence, primary-source access and selected proof-inspection boundaries.
A complete version of the needed elementary argument is included below.
Fixed-dimension asymptotic small-ball results are not substituted for a uniform theorem.
No computational experiment or new J is needed.

<a id="hilbert-separated-subset-sum-proof"></a>
### 1. The classical dimension-free sign bound, with endpoints explicit

Let v_1,...,v_N belong to a real Hilbert space with norms at least a>0.
The2^N indexed subset sums can be partitioned into binom(N,floor(N/2)) blocks, each having pairwise distances at least a.
Repeated sums are still different indexed choices; none can lie together in a separated block.
Here is the full geometric induction used in GK78, with the counting step written explicitly.

Start with the one singleton block at N=0.
Given a separated block B of k points and the next vector v, consider B and B+v as indexed collections.
Choose x in B maximizing the real inner product <x,v>.
Transfer x+v from B+v into B.
For every y in B,

    ||x+v-y||^2
       =||x-y||^2+||v||^2+2<x-y,v> >=a^2.              (1)

Both resulting blocks are separated, have sizes k+1 and k-1, and the latter is discarded when empty.
Translation preserves all other distances.
By induction the number of blocks of length N-2j+1 is binom(N,j)-binom(N,j-1), for0<=j<=floor(N/2), where binom(N,-1)=0.
Indeed the k+1/k-1 rule gives Pascal's recurrence, with the zero-length blocks omitted at the endpoint.
Summing this telescopes to binom(N,floor(N/2)).
This proves the claimed partition without importing an uninspected symmetric-chain enumeration.

Consequently a set of diameter strictly smaller than a contains at most one point of each block.
For independent fair signs epsilon_i in{-1,1} and vectors y_i with ||y_i||>r, this implies, for every center c,

    Pr{sum_i epsilon_i y_i in closed B(c,r)} <= beta_N,
    beta_N=2^(-N) binom(N,floor(N/2)) <=1/sqrt(N+1).      (2)

Use subset coefficients2y_i, translate by minus their sum, and choose a between2r and their minimum norm.
For N=0 the bound is1.
The last estimate is elementary: for N=2j, beta_(2j)=binom(2j,j)/4^j and the recurrence ratio(2j+1)/(2j+2), together with (2j+1)(2j+3)<(2j+2)^2, proves beta_(2j)<=1/sqrt(2j+1).
For odd N, beta_(2j+1)=beta_(2j)(2j+1)/(2j+2)<=1/sqrt(2j+2).
No dimension enters (1) or (2).

The source's motivating sphere wording has an endpoint ambiguity, and printed76 repeats k+1 in an introductory sentence before correctly giving k-1 and k+1 in the actual construction.
The strict convention and explicit recurrence above avoid both issues.
This is a reproduction and application of the classical mechanism, not a new attribution claim.

<a id="dimension-free-neutral-small-ball"></a>
### 2. Large-radius small-ball estimate for the actual digit noise

Let a>0 and let deterministic vectors v_j in a real Hilbert space satisfy ||v_j||=a.
Let eta_j be independent, with probabilities1/2 at0 and1/4 at each of-1,+1, and put S_n=sum_(j=1)^n eta_j v_j.
For every n>=1, r>=0 and every center c,

    Pr{S_n in closed B(c,r)}
       <=min(1,sqrt[(24+96r^2/a^2)/n]).                  (3)

The vectors need not span the ambient space, be orthogonal, or satisfy a separation assumption.
In particular the constant is independent of the ambient dimension and all relative angles.

To prove (3), first consider any consecutive block of ell vectors and its symmetric displacement Y.
Independence and E eta=0, E eta^2=E eta^4=1/2 give

    E||Y||^2=ell a^2/2,
    E||Y||^4<=3(ell a^2/2)^2.                            (4)

For the second inequality expand the squared inner-product expression: the pair contribution is (a^4/2)+<v_i,v_j>^2<=3a^4/2 for each i<j, and the single-index contribution is ell a^4/2.
The sum is at most3ell^2 a^4/4.
Applied to ||Y||^2, Cauchy--Schwarz gives the usual elementary second/fourth-moment estimate

    Pr{||Y||^2 >=ell a^2/4} >=1/12.                       (5)

For completeness, for a nonnegative Z with mean b, write b<=b/2+E[Z 1_(Z>=b/2)] and use Cauchy--Schwarz; here E Z^2<=3b^2.

Choose ell=1+ceil(8r^2/a^2), and K=floor(n/ell) full independent blocks.
Their remaining incomplete block can be conditioned on.
Each full block is symmetric.
Choose a deterministic orientation for every pair of its opposite possible nonzero values, and write it as an independent fair sign times its oriented representative; an extra irrelevant fair sign may be attached to zero.
This is legitimate because each block has finite symmetric support, and different blocks remain independent.
Call a representative good if its norm is greater than r.
Since ell a^2/4>r^2, (5) says its good probability is at least1/12.

Condition on all oriented representatives, the remainder, and the signs of bad blocks.
If G good blocks remain, (2) bounds the conditional small-ball probability by1/sqrt(G+1).
For independent good indicators with probabilities p_b>=1/12,

    E[1/(G+1)]
       =integral_0^1 product_(b=1)^K(1-p_b+p_b t) dt
       <=12/(K+1).

Cauchy--Schwarz therefore gives E[1/sqrt(G+1)]<=sqrt(12/(K+1)).
Since K+1>n/ell and ell<=2+8r^2/a^2, this is bounded by the right side of (3).
The same reasoning covers K=0 through the trivial bound1, and r=0 without any ball-boundary ambiguity.

<a id="stationary-neutral-concentration-cost"></a>
### 3. Fully charged stationary concentration cost

Consider the actual original algebraic process X_(j+1)=alpha X_j+eta_j on O=Z[alpha], where alpha is an algebraic unit.
Choose s>=1 embeddings sigma_1,...,sigma_s with |sigma_l(alpha)|=1, and write

    Z(x)=(sigma_1(x)...,sigma_s(x)) in C^s,
    rho(x)=||Z(x)||_2,
    a=sqrt(s).

One may choose one embedding from each unit-circle conjugate pair.
More generally the argument works for any specified such collection, including a single real unit-circle embedding in a torsion control.
Regard C^s as a real Hilbert space.
Multiplication by alpha gives a diagonal unitary U and the digit increment vector is v=(1,...,1), of norm a.
Thus the original n-step neutral displacement from any fixed state is a translate of sum_(j=0)^(n-1)eta_j U^j v, exactly of the form in (3).
Its coefficients all have norm a; no spectral independence or equidistribution is assumed.

Let Q be any admissible irreducible positive recurrent chain on a subset of the actual return core containing zero, with invariant probability pi and original-digit information

    I=sum_x pi(x) sum_eta q_x(eta) log(q_x(eta)/p_eta),
    p_0=1/2, p_+=p_-=1/4.                                (6)

This is precisely the class of L201/L212.
Compare a stationary Q path of length n with the full original iid-digit process started from the same pi.
The relative entropy is exactly nI, by the path chain rule and stationarity.
Every original digit has positive probability, and row entropy is at most log4, so the required finite-time integrability is immediate.
Paths of the original process may leave the return core; they are not discarded or renormalized.

Data processing to the endpoint and the elementary Pinsker inequality give total variation at most sqrt(nI/2).
One proof of that inequality groups the positive and negative parts of the difference into a two-set partition, uses log-sum, and bounds binary relative entropy below by twice the squared mass difference, since its second derivative in the first argument is1/[u(1-u)]>=4.
This proof extends by approximation to the countable paths in use here.
The neutral image and any ball are measurable.
Averaging (3) over the original starting state and using Q stationarity proves, simultaneously for all c in C^s, r>=0 and integers n>=1,

    pi{||Z(x)-c||<=r}
       <=min(1,sqrt[A_r/n]+sqrt(nI/2)),
    A_r=24+96r^2/s.                                      (7)

Infinite support, infinite full-state entropy and infinite moments are permitted.
The estimate compares the actual path law; it does not assume that a projected law is Markov.
It also does not use finite quotients, lattice-point counting, a full-strip theorem or a Salem-specific premise.

There is no admissible I=0 law when such an embedding is present: taking n to infinity in (7) makes every finite-radius ball have zero mass, but their increasing union contains every state.
For I>0 choose n=ceil(sqrt(2A_r/I)).
The elementary inequality sqrt(u+v)<=sqrt(u)+sqrt(v) yields

    pi{||Z(x)-c||<=r}
       <=2(A_r I/2)^(1/4)+sqrt(I/2)
       <=6[I(1+r^2/s)]^(1/4)+sqrt(I/2).                  (8)

The optimization charges actual chronological time n of order sqrt(A_r/I).
It is not a free repeated-block or stationary reweighting operation.

If a closed ball has mass at least u>0 and I<=u^2/8, then sqrt(I/2)<=u/4.
Rearranging (8) gives the finite positive-quantile lower bound

    r^2/s >= u^4/(4096I)-1.                              (9)

Constants are convenient universal choices, not asserted sharp.
For every fixed u>0, the required radius is therefore at least a positive u-dependent constant times sqrt(s/I) for all sufficiently small I.
This genuinely attains that quantile scale, in contrast to a lower second-moment statement.

<a id="near-one-quantile-without-log-loss"></a>
### 4. Near-one consequence and exact excursion occupation

For any hypothetical sequence of actual units with m=log M tending to zero, at least s>=1 selected unit-circle embeddings, and admissible laws I<=2m, (8) implies uniformly in the centers

    r=o(sqrt(s/m))  implies
    sup_c pi{||Z(x)-c||<=r} ->0.                          (10)

For example, for any function g(m) tending to infinity, not necessarily a power of a logarithm,

    sup_c pi{||Z(x)-c||<=sqrt(s)/(sqrt(m) g(m))}
       <=6[2m+2/g(m)^2]^(1/4)+sqrt(m) ->0.                (11)

This includes Salem inputs with d=2s+2 and removes L216's condition A>1/2.
Formula (9) also gives a constant-times-sqrt(s/m) necessary radius for every fixed positive mass.
It does not assert that the probability at every fixed multiple of this scale tends to zero.
The theorem applies to all the actual finite approximants supplied by L201 as well as infinite admissible laws.
For nontorsion inputs with no unit-circle embedding this particular neutral argument supplies no conclusion.

The original excursion question has a precise consequence.
Let tau be the Q first-return time to zero and mu=E_0 tau=1/pi(0).
For a realized excursion and0<=j<=tau,

    rho(X_j)<=sqrt(s) min(j,tau-j).                       (12)

The forward bound sums j increments of norm at most sqrt(s); the backward bound uses X_tau=0 and the inverse unitary for the remaining increments.
For any integer t>=0, at least min(tau,2t+1) of its departure states j=0,...,tau-1 lie in the ball of radius sqrt(s)t.
The normalized excursion occupation identity consequently gives

    E_0 min(tau,2t+1)/mu
       <=pi{rho<=sqrt(s)t}
       <=6[I(1+t^2)]^(1/4)+sqrt(I/2).                    (13)

No unknown weighted-return asymptotic or critical attainment is used.
Define the length seen by a stationary randomly selected excursion time by Pr{tau_star=k}=k Pr_0{tau=k}/mu.
Then

    Pr{tau_star<=2t+1}
       <=E min(1,(2t+1)/tau_star)
       =E_0 min(tau,2t+1)/mu.                            (14)

Thus t=o(I^(-1/2)) forces this size-biased short-length probability to vanish.
This is an occupation/size-biased-time assertion.
It is not a claim that every excursion is long, that the unweighted mean has this scale merely from size bias, or that these necessary bounds contradict the exact L212 frontier.
Existing lower mean bounds from the zero-state information constraint remain separate.

<a id="actual-torsion-diffusive-scale-control"></a>
### 5. An actual algebraic control showing why the scale alone is compatible

The scale in (9) cannot by itself contradict every low-information stationary law.
Use the actual unit alpha=-1, whose return core is Z, choose its single embedding in C, and let0<t<=1.
Put r_0=exp(-t) and

    pi_t(x)=[(1-r_0)/(1+r_0)] r_0^|x|,  x in Z.           (15)

Every integer belongs to the actual core: repeated appropriate digits reach it, and reciprocal reversed words return.
Alternatively the two-step original noise is an irreducible lazy nearest-neighbor-containing walk on Z.

Define a nearest-neighbor Metropolis kernel L_t by

    L_t(x,x+epsilon)=(1/4)min(1,pi_t(x+epsilon)/pi_t(x)),
          epsilon in{-1,+1},
    L_t(x,x)=1-L_t(x,x-1)-L_t(x,x+1).

Detailed balance follows by writing each edge flow as (1/4)min(pi_t(x),pi_t(y)).
Hence pi_t L_t=pi_t.
Reflection R:x->-x preserves pi_t, so

    Q_t(x,y)=L_t(-x,y)                                   (16)

also preserves it and uses precisely the original digit edges y=-x+eta.
Its allowed nearest choices are positive; two-step paths give irreducibility and the positive zero self-loop gives aperiodicity.
The invariant probability yields positive recurrence, so it is a legitimate L201/L212 competitor, not a continuous or unrelated model.

Let u_t=1-exp(-t).
At a nonzero state, relative to p, one outward digit probability decreases by u_t/4 and the zero-digit probability increases by u_t/4; the other is unchanged.
At zero both outward probabilities decrease by u_t/4 and the zero-digit probability increases by u_t/2.
The elementary inequality D(q||p)<=sum(q-p)^2/p, obtained from log z<=z-1, and the Pinsker lower bound show at every row

    u_t^2/8 <=D(q_x||p)<=u_t^2.

Consequently

    u_t^2/8<=I(Q_t)<=u_t^2<=t^2.                          (17)

For t<=1, u_t>=t/2, so t^2/32<=I(Q_t)<=t^2.
The tail is exact:

    pi_t{|x|>=N}=2r_0^N/(1+r_0),   N>=1.                 (18)

Every fixed positive quantile of |x| therefore has order1/t, and hence order I(Q_t)^(-1/2).
For a fixed c>0, pi_t{|x|<=c/t} tends to1-exp(-c), not zero.
This is an actual torsion comparison at m=0.
It does not refute any theorem restricted to nontorsion near-one inputs, but proves that the generic neutral small-ball/information mechanism is compatible with its own diffusion-scale requirement.
A further arithmetic or actual-return constraint is needed for a positive Mahler gap.

### Author verification and remaining target

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g220-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.

The new result strengthens a necessary low-information geometry theorem, including a radius at the full diffusion scale and a wider input class.
It does not establish an opposing radius bound, prohibit the actual Salem critical competitors, solve general compact termination, or cover reciprocal units having no unit-circle embeddings.
The next discriminating step is a genuinely arithmetic or original-return constraint on diffusion-scale occupation, beyond the generic stationary information mechanism whose actual torsion compatibility has been exhibited.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0793_v1.md#small-ball-excursion-complete-independent-review), with its original inspected scope and relationship.
