---
author: Yin
---

# Dimension-free original-noise small balls, exact stationary quantiles and excursion occupation

The complete original L220 Sections 1--5/(1)--(18) are retained with every endpoint, ceiling, probability, chronological cost and actual torsion-control restriction.
The original [R793 whole](../audits/reviews/Yin_R_G0793_v1.md#small-ball-excursion-complete-independent-review) inspected that full chain on 2026-10-09T21:12 and retains its selected GK78 visual/source reading.
The existence of a direction summary before that old inspection does not identify its actual mathematical contents; its missing relationship declaration is preserved rather than recast as a known arrangement.

## Statement

<a id="small-ball-quantile-fixed-scope"></a>

Let v_1,...,v_N be vectors of norm at least a>0 in any real Hilbert space.
All 2^N indexed subset sums, including repeated values with multiplicity, partition into binom(N,floor(N/2)) blocks with pairwise distances at least a.
Consequently independent fair signs epsilon_i and coefficients ||y_i||>r satisfy, at every center c and closed ball radius r>=0,
\[
\Pr\{\sum_{i=1}^N\epsilon_i y_i\in\overline B(c,r)\}
\le \beta_N=2^{-N}\binom N{\lfloor N/2\rfloor}
\le1/\sqrt{N+1}.
\]
For N=0 the bound is 1.
The strict coefficient inequality is essential to the adopted closed-ball convention.
This is the classical GK78 separated-sum mechanism with its complete needed proof retained locally.

Let deterministic v_j in any real Hilbert space have common norm a>0 and let independent eta_j have probabilities 1/2 at 0 and 1/4 at each sign.
For every n>=1,r>=0 and center c,
\[
\Pr\{\sum_{j=1}^n\eta_jv_j\in\overline B(c,r)\}
\le\min(1,\sqrt{(24+96r^2/a^2)/n}).
\]
No dimension, angular separation, orthogonality or spanning hypothesis is imposed.

Now let alpha be any algebraic unit with s>=1 specified embeddings of modulus 1.
For Z(x)=(sigma_1(x),...,sigma_s(x)), rho(x)=||Z(x)||, the actual update is x->alpha x+eta on Z[alpha] with the original three digit probabilities above.
Let Q be an irreducible positive recurrent admissible law on a subset of the actual original return core containing 0, with invariant pi and original-row relative entropy I.
Finite state entropy, support, moments and a projected Markov property are not assumed.
For every n>=1,r>=0,c in C^s, writing A_r=24+96r^2/s,
\[
\pi\{||Z(x)-c||\le r\}\le
 \min(1,\sqrt{A_r/n}+\sqrt{nI/2}).
\]
The comparison uses the full original process started from the same pi, including paths leaving the core, with exact path entropy nI.
No such admissible law has I=0.
For I>0,
\[
\pi\{||Z(x)-c||\le r\}
\le2(A_r I/2)^{1/4}+\sqrt{I/2}
\le6[I(1+r^2/s)]^{1/4}+\sqrt{I/2}.
\]
If a closed ball has mass at least u>0 and I<=u^2/8, then r^2/s>=u^4/(4096I)-1.
Along any hypothetical sequence with 0<m=log M(alpha)->0 and admissible laws I<=2m,
r=o(sqrt(s/m)) implies sup_c pi{||Z(x)-c||<=r}->0.
More explicitly, for every g(m)->infinity the radius sqrt(s)/(sqrt(m)g(m)) has probability at most 6[2m+2/g(m)^2]^(1/4)+sqrt(m).
These are necessary quantile bounds, with no conclusion for inputs lacking selected unit-circle embeddings or for every fixed multiple of the scale.

Let tau be Q's first return to zero, mu=E_0 tau=1/pi(0), and Pr{tau_star=k}=kPr_0{tau=k}/mu.
Every returning path has rho(X_j)<=sqrt(s)min(j,tau-j).
For every integer t>=0,
\[
\frac{E_0\min(\tau,2t+1)}{\mu}
\le\pi\{\rho\le\sqrt{s}t\}
\le6[I(1+t^2)]^{1/4}+\sqrt{I/2},
\]
\[
\Pr\{\tau_\star\le2t+1\}
\le E\min(1,(2t+1)/\tau_\star)
=\frac{E_0\min(\tau,2t+1)}{\mu}.
\]
As I->0, t=o(I^(-1/2)) forces that size-biased short-length probability to vanish; no corresponding unweighted mean-return or every-excursion conclusion follows.

For the actual torsion unit alpha=-1 with core Z, every 0<t<=1 admits the explicit reflected Metropolis law with
\[
\pi_t(x)=\frac{1-e^{-t}}{1+e^{-t}}e^{-t|x|},\quad
L_t(x,x+\epsilon)=\tfrac14\min(1,\pi_t(x+\epsilon)/\pi_t(x)),\quad
Q_t(x,y)=L_t(-x,y).
\]
The remaining L_t mass is its holding probability.
This actual admissible law satisfies
(1-e^(-t))^2/8<=I(Q_t)<=(1-e^(-t))^2<=t^2 and t^2/32<=I(Q_t).
For every N>=1 its tail is 2e^(-tN)/(1+e^(-t)).
Fixed positive nontrivial quantile radii have order 1/t and I(Q_t)^(-1/2), and pi_t{|x|<=c/t}->1-e^(-c) for fixed c>0.
This m=0 control shows compatibility of the generic scale, not a nontorsion near-one counterexample or a Mahler gap.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:05 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All-dimensional strict separated indexed sums and closed-ball sign bound; exact three-digit Hilbert small balls; any actual algebraic unit with s>=1 selected circle embeddings and any admissible rooted stationary law, full path nI cost, positive quantiles/near-one limits and precise size-biased occupation; actual alpha=-1 control and every domain/limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(18), full partition-count induction, second/fourth block moments, independent sign orientations/good-block averaging, all ceiling and zero cases, full path/Pinsker comparison, infinite-support/moment quantifiers, occupation endpoint counts and exact reflected Metropolis control. |
| dependency | [Actual rooted stationary class](Yin_C_G0479_v1.md#statement) | Exact original-digit irreducible positive recurrent laws on actual return core containing zero, finite mean return/occupation and full original path likelihood; no attained critical competitor assumed. |
| dependency | [Prescribed-mass/occupation conventions](Yin_C_G0511_v1.md#statement) | Actual rooted return and stationary occupation interfaces, including finite approximants; no near-one critical classification. |
| support | [Classical separated sums](../audits/literature/GK78/Yin_U001.md#gk78-u001) | Precisely retained1978 Section9 pp74--76 strict-diameter mechanism and source access/selected-proof limits; the complete needed partition proof is local. |
| support | [Earlier logarithmic quantile bound](../ledger/Yin_L_G0216_v1.md#stationary-quantile-fixed-scope) | Comparison only to its actual fixed A>1/2 logarithmic loss; no finite quotient, counting or hypercontractive premise imported. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All-dimensional strict separated indexed sums and closed-ball sign bound; exact three-digit Hilbert small balls; any actual algebraic unit with s>=1 selected circle embeddings and any admissible rooted stationary law, full path nI cost, positive quantiles/near-one limits and precise size-biased occupation; actual alpha=-1 control and every domain/limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(18), full partition-count induction, second/fourth block moments, independent sign orientations/good-block averaging, all ceiling and zero cases, full path/Pinsker comparison, infinite-support/moment quantifiers, occupation endpoint counts and exact reflected Metropolis control. |
| dependency | [Actual rooted stationary class](Yin_C_G0479_v1.md#statement) | Exact original-digit irreducible positive recurrent laws on actual return core containing zero, finite mean return/occupation and full original path likelihood; no attained critical competitor assumed. |
| dependency | [Prescribed-mass/occupation conventions](Yin_C_G0511_v1.md#statement) | Actual rooted return and stationary occupation interfaces, including finite approximants; no near-one critical classification. |
| support | [Classical separated sums](../audits/literature/GK78/Yin_U001.md#gk78-u001) | Precisely retained1978 Section9 pp74--76 strict-diameter mechanism and source access/selected-proof limits; the complete needed partition proof is local. |
| support | [Earlier logarithmic quantile bound](Yin_C_G0523_v2.md#stationary-quantile-fixed-scope) | Comparison only to its actual fixed A>1/2 logarithmic loss; no finite quotient, counting or hypercontractive premise imported. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g220-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R793. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All-dimensional strict separated indexed sums and closed-ball sign bound; exact three-digit Hilbert small balls; any actual algebraic unit with s>=1 selected circle embeddings and any admissible rooted stationary law, full path nI cost, positive quantiles/near-one limits and precise size-biased occupation; actual alpha=-1 control and every domain/limitation. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(18), full partition-count induction, second/fourth block moments, independent sign orientations/good-block averaging, all ceiling and zero cases, full path/Pinsker comparison, infinite-support/moment quantifiers, occupation endpoint counts and exact reflected Metropolis control. |
| dependency | [Actual rooted stationary class](Yin_C_G0479_v1.md#statement) | Exact original-digit irreducible positive recurrent laws on actual return core containing zero, finite mean return/occupation and full original path likelihood; no attained critical competitor assumed. |
| dependency | [Prescribed-mass/occupation conventions](Yin_C_G0511_v1.md#statement) | Actual rooted return and stationary occupation interfaces, including finite approximants; no near-one critical classification. |
| support | [Classical separated sums](../audits/literature/GK78/Yin_U001.md#gk78-u001) | Precisely retained1978 Section9 pp74--76 strict-diameter mechanism and source access/selected-proof limits; the complete needed partition proof is local. |
| support | [Earlier logarithmic quantile bound](Yin_C_G0523_v2.md#stationary-quantile-fixed-scope) | Comparison only to its actual fixed A>1/2 logarithmic loss; no finite quotient, counting or hypercontractive premise imported. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0793_v1.md#small-ball-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:34, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

### Reuse, source and changed mechanism

[L216](../ledger/Yin_L_G0216_v1.md#stationary-quantile-fixed-scope) obtained a near-one stationary probability bound by repeated finite-quotient mixing, Shannon entropy and integer-norm counting.
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
