---
author: Yin
---

# Binary entropy increments, exact punctured matching and effective affine costs

This retains the complete original2026-10-07 [L92 proof](../ledger/Yin_L_G0092_v1.md).
Its [old actual checking account](../audits/reviews/Yin_R_G0024_v1.md#contribution-and-actual-review-scope) retains the exact old inputs and separately classified relationships.
Original inspection phrases inside the retained argument concern those old checks and supply no independent review of this new C.
No source, computation or Task is newly executed.

## Statement

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d, O=Z[alpha], A multiplication by alpha and m=log M(P)>0.
For independent fair bits let S_n=sum_(j<n)xi_j alpha^j,mu_n its law,mu0=delta0,H_n=H(mu_n),H0=0 and Delta_n=H_n-H_(n-1).
Use natural logarithms and ell=log2.
Then

    ell=Delta1>=Delta2>=...>0,
    Delta_n decreases to h1=lim H_n/n,
    c_B min(m,ell)<=h1<=min(m,ell).

Every increment is an upper certificate for the rate, not a lower certificate for its limit.

For finite laws p,q put JS=H((p+q)/2)-(H(p)+H(q))/2 and TV=(1/2)sum|p-q|.
Their exact elementary estimates are TV²/2<=JS<=ell TV.
Convolution contracts both.
Both endpoint recursions give

    Delta_n=JS(mu_(n-1),tau_(alpha^(n-1))mu_(n-1))
       =JS(A_*mu_(n-1),tau1 A_*mu_(n-1)).

For0<=j<N let mu_(N,minus j) omit the jth bit and I_(N,j)=H_N-H(mu_(N,minus j)).
Then I_(N,j)=JS(mu_(N,minus j),tau_(alpha^j)mu_(N,minus j)) and

    I_(N,j)<=min(Delta_(j+1),Delta_(N-j))
       <=Delta_ceil((N+1)/2).

The same JS upper bound holds for mu_N and its alpha^j translate.
If Delta_k<=delta and N>=2k-1, both punctured and full laws have those TV errors at most sqrt(2delta).
For the punctured integer fibers f,

    sum_x min(f(x),f(x-alpha^j))
       >=(1-sqrt(2delta))2^(N-1).

This is the exact maximal matching size between two labeled copies, not an assertion of disjoint underlying word sets.
For N=2k-1, centering by A^(-(k-1)) gives a single law nu on powers|j|<=k-1 whose translation errors are at most sqrt(2Delta_k).
For v=sum c_j alpha^j in that window,

    TV(nu,tau_v nu)<=min(1,sum|c_j|sqrt(2Delta_k)).

The endpoint mixture comparison also gives

    TV(mu_n,mu_(n+1)),TV(A_*mu_n,mu_(n+1))
       <=sqrt(Delta_(n+1)/2),
    TV(mu_n,A_*mu_n)<=sqrt(2Delta_(n+1)).

The same centered law nu therefore has A-pushforward and A-inverse error at most sqrt(2Delta_k); compositions pay the sum of the individual errors.

Exactly Delta_n<ell iff P divides a monic integer polynomial of degree exactly n-1 with coefficients in{-1,0,1}.
For n<=d,Delta_n=ell.
At the first collision time N, if s counts the intersection of the preceding uniform prefix support with its alpha^(N-1) translate, then Delta_N=ell(1-s/2^(N-1)).
Existence alone gives only a vanishing-scale deficit ell/2^(N-1), not a common positive rate.
Let f_n count all length-n binary fibers and U_n=product_(f_n(x)>0)f_n(x)^(f_n(x)),U0=1.
Then

    exp(2^n Delta_n)=2^(2^n)U_(n-1)^2/U_n.

Every comparison with(log a)/b for positive integers a,b is an exact positive-integer-power test from polynomial remainders, certifying an increment and an upper bound on h1, never all later lower bounds.

The complete norm-grid theorem gives |T_n|<=(4n)^d exp((n-1)m), hence
Delta_n<=H_n/n<=m+dlog(4n)/n.
For0<epsilon<=1 choose

    k=ceil[(2d/epsilon)log(8d/epsilon)],N=2k-1.

Then Delta_k<=m+epsilon.
For nu=A_*^(-(k-1))mu_N,

    TV(nu,tau_(alpha^j)nu),TV(nu,A_*nu)<=sqrt(2(m+epsilon))
       for|j|<=k-1,
    log|supp nu|<=(m+epsilon)N.

For0<m<=1,epsilon=m gives all those errors at most min(1,2sqrt m),

    N<(4d/m)log(8d/m)+1,
    log|supp nu|<=2mN<8dlog(8d/m)+2m.

This approaches the upper level m effectively, without assuming h1=m or giving a convergence rate to h1.

Qualitative affine approximate invariants exist for every A in GL_d(Z), without small Mahler measure.
For integers K,R>=0 let u_R be uniform on[-R,R]^d intersect Z^d and nu_(K,R)=(2K+1)^(-1)sum_(t=-K)^K A_*^t u_R.
For finite W, put D=max_(|t|<=K,w in W)||A^(-t)w||1,D=0 if W is empty.
Exactly,

    TV(A_*nu,nu)<=1/(2K+1),
    TV(u_R,tau_z u_R)=1-product_i max(0,1-|z_i|/(2R+1)),
    TV(nu,tau_w nu)<=D/(2R+1),
    |supp nu|<=(2K+1)(2R+1)^d.

Choosing K then R makes all fixed finite errors arbitrarily small even for the positive-Mahler unit t²-3t+1.
That control does not concern the particular binary laws or their resource bounds above.
On a full k-cyclic induction the exact probability product gives Delta_n^(k)=Delta_ceil(n/k), so degree-free convergence is delayed; it gives no counterexample on the all-power-stable small reciprocal core.
No universal resource bound, arithmetic mass-matching obstruction, common entropy gap or proof of a near-zero sequence is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:17 |
| status | open |
| reason | Register every complete original increment/punctured-law/arithmetic/effective-cost theorem and exact fixed input; actual current whole review and adoption follow separately. No qualitative-invariance-to-gap inference or unproved uniform resource bound is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire original1–23 on the exact nontorsion-unit domain: increment/JS/TV identities and constants, all punctured/full/centered matching and action errors, finite arithmetic certificates, effective binary time/support, full arbitrary-law affine control and induction/uniformity boundaries. |
| argument | [Entire original proof](#argument) | Complete original submodularity/concavity, elementary g(z) divergence proof, both punctured marginal and convolution arguments, labeled fiber matching, endpoint triangle/centering, strict first-drop and integer-product derivations, full grid-based rounding/cost proof, box averaging and exact probability-induction argument. |
| dependency | [Complete entropy submodularity](Yin_C_G0282_v1.md#entropy-set-function-thinning) | Exact independent partial-sum monotonicity/submodularity and deterministic information framework, no concentration theorem. |
| dependency | [Accepted fair-binary rate input](Yin_C_G0280_v1.md#mahler-to-binary-min-entropy) | Exact symbolic BV20 Shannon/min/collision comparison and total-support upper bound, preserving all fairness/sign/log-base and source-depth guards. |
| dependency | [Complete absolute norm grid](Yin_C_G0281_v1.md#norm-grid-support-bound) | Full strict real/complex cell construction and absolute(4n)^d M^(n-1) bound, with no discriminant/covolume/maximal-order or computation premise. |
| dependency | [Complete cyclic coordinates](Yin_C_G0206_v1.md#argument) | Exact full-coordinate cyclic induction, without irreducibility; the independent binary coordinate laws give the stated repeated-increment formula. |
| support | [Retained full probability-product interface](Yin_C_G0212_v1.md#radical-collision-control) | Complete support/collision/Shannon product under the exact full relative-degree guard, compatible with the formal full-coordinate induction used here; no selected-factor or core inheritance. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:21 |
| status | proved |
| reason | Adopt the complete original increment/JS/TV/punctured matching and integer-certificate theorem, effective binary near-invariance costs, full arbitrary-law control and induction delay after actual whole self-review. R24 retains only its old fixed inputs and split relationships; the old anchor correction supplies no mathematical repair debt, and no qualitative-invariance-to-gap inference is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire original1–23 on the exact nontorsion-unit domain: increment/JS/TV identities and constants, all punctured/full/centered matching and action errors, finite arithmetic certificates, effective binary time/support, full arbitrary-law affine control and induction/uniformity boundaries. |
| argument | [Argument](#argument) | Complete original submodularity/concavity, elementary g(z) divergence proof, both punctured marginal and convolution arguments, labeled fiber matching, endpoint triangle/centering, strict first-drop and integer-product derivations, full grid-based rounding/cost proof, box averaging and exact probability-induction argument. |
| dependency | [Dependency](Yin_C_G0282_v1.md#entropy-set-function-thinning) | Exact independent partial-sum monotonicity/submodularity and deterministic information framework, no concentration theorem. |
| dependency | [Dependency](Yin_C_G0280_v1.md#mahler-to-binary-min-entropy) | Exact symbolic BV20 Shannon/min/collision comparison and total-support upper bound, preserving all fairness/sign/log-base and source-depth guards. |
| dependency | [Dependency](Yin_C_G0281_v1.md#norm-grid-support-bound) | Full strict real/complex cell construction and absolute(4n)^d M^(n-1) bound, with no discriminant/covolume/maximal-order or computation premise. |
| dependency | [Dependency](Yin_C_G0206_v1.md#argument) | Exact full-coordinate cyclic induction, without irreducibility; the independent binary coordinate laws give the stated repeated-increment formula. |
| support | [Support](Yin_C_G0212_v1.md#radical-collision-control) | Complete support/collision/Shannon product under the exact full relative-degree guard, compatible with the formal full-coordinate induction used here; no selected-factor or core inheritance. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0535_v1.md#current-binary-increment-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings retain their actual fixed inputs and relationship scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="decreasing-binary-entropy-increments"></a>
### The increments decrease exactly to the Shannon rate

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d, O=Z[alpha], and A multiplication by alpha.
For independent fair bits xi_j put

    S_n=sum_(j=0)^(n-1) xi_j alpha^j,
    mu_n=law(S_n),  mu_0=delta_0,
    H_n=H(mu_n),  H_0=0,
    Delta_n=H_n-H_(n-1)  for n>=1.                       (1)

All logarithms are natural, and ell=log 2.
For a finite index set I, write F(I)=H(sum_(j in I) xi_j alpha^j).
This is the monotone submodular function of [L G0090](Yin_C_G0282_v1.md#entropy-set-function-thinning).
Shifting every index by the same integer preserves its entropy, because multiplication by the corresponding power of alpha is injective.
Applying submodularity to the intervals [0,n-1] and [1,n] gives

    2H_n>=H_(n-1)+H_(n+1),
    ell=Delta_1>=Delta_2>=...>=0,
    Delta_n decreases to h_1(alpha)=lim_n H_n/n.           (2)

For the last equality, the decreasing nonnegative increments have a limit, and their Cesaro averages are H_n/n.
This also shows Delta_n>=h_1 at every n.
By the retained entropy comparison,

    c_B min(m,ell)<=h_1<=min(m,ell),    m=log M(P),         (3)

with exactly the symbolic BV20 constant in [L G0089](Yin_C_G0280_v1.md#mahler-to-binary-min-entropy).
The increment is a decreasing upper certificate for the rate, not a finite-time lower certificate for its limiting value.

<a id="binary-increment-js-divergence"></a>
### Exact translation divergence and elementary constants

For a group element v let tau_v mu denote translation of a law by v.
For two finite laws p,q define

    JS(p,q)=H((p+q)/2)-(H(p)+H(q))/2,
    TV(p,q)=(1/2)sum_x |p(x)-q(x)|.

Equivalently, JS is the mutual information between a fair label and a sample whose conditional laws are p and q.
The binary recursions give

    mu_n=(mu_(n-1)+tau_(alpha^(n-1))mu_(n-1))/2,
    Delta_n=JS(mu_(n-1),tau_(alpha^(n-1))mu_(n-1)).         (4)

There is also the initial-bit expression Delta_n=JS(A_*mu_(n-1),tau_1 A_*mu_(n-1)).
Both component entropies equal H_(n-1).
These identities require no absence of internal collisions.

Here are all divergence estimates used below, with natural-log normalization:

    TV(p,q)^2/2<=JS(p,q)<=ell TV(p,q).                    (5)

To verify them without an external Pinsker theorem, put w=(p+q)/2 and z=(p-q)/(p+q) where p+q>0.
Then

    JS(p,q)=sum_x w(x) g(z(x)),
    g(z)=((1+z)/2)log(1+z)+((1-z)/2)log(1-z),
    TV(p,q)=sum_x w(x)|z(x)|.

The endpoint convention is 0 log 0=0.
Since g is even, g(0)=g'(0)=0, and g''(z)=1/(1-z^2)>=1 in (-1,1), g(z)>=z^2/2.
Cauchy--Schwarz proves the lower bound in (5).
Convexity on [0,1] and g(1)=ell give g(z)<=ell|z|, proving the upper bound.
Convolution cannot increase JS: add independent noise to the labelled sample and apply data processing for mutual information, as in L G0090.
Convolution also contracts TV, directly by the triangle inequality.

<a id="punctured-binary-near-invariance"></a>
### One law and all the powers in its time window

For 0<=j<N let mu_(N,minus j) be the law with its jth bit omitted, and define its bit information by

    I_(N,j)=H_N-H(mu_(N,minus j))
           =JS(mu_(N,minus j),
                tau_(alpha^j)mu_(N,minus j)).             (6)

Submodularity compares this marginal first with its left interval [0,j-1] and then with its right interval [j+1,N-1].
Translation of index intervals preserves entropy.
Hence

    I_(N,j)<=min(Delta_(j+1),Delta_(N-j))
             =Delta_(max(j+1,N-j))
             <=Delta_(ceil((N+1)/2)).                    (7)

The individual blocks need not be independent after conditioning on the full sum; (7) uses independent input bits and submodularity of unconditional partial-sum entropy.

Convolving both laws in (6) with the jth Bernoulli digit gives mu_N and tau_(alpha^j)mu_N.
Therefore the same upper bound holds for JS(mu_N,tau_(alpha^j)mu_N).
In particular, if Delta_k<=delta and N>=2k-1, then for every 0<=j<N,

    TV(mu_(N,minus j),tau_(alpha^j)mu_(N,minus j))
                    <=sqrt(2delta),
    TV(mu_N,tau_(alpha^j)mu_N)<=sqrt(2delta).              (8)

The punctured-law statement is the stronger arithmetic interface: the translation in it is the missing digit, so its overlap does not merely come from toggling a digit already present in the law.

To make its mass content exact, let f_(N,minus j)(x) count the 2^(N-1) binary words with the jth bit omitted, evaluated at x.
Then

    sum_x min(f_(N,minus j)(x),
              f_(N,minus j)(x-alpha^j))
       >=(1-sqrt(2delta)) 2^(N-1).                       (9)

The left side is the maximal number of matches between subsets of two labelled copies of the punctured word set, with evaluation values differing by alpha^j.
Matching within each pair of fibers proves this interpretation.
A word may occur in different roles in the two copies; no disjointness of their underlying unlabelled word sets is claimed.
A bound (9) near full mass is substantially more information than the existence of one vanishing polynomial.

If N=2k-1, push mu_N forward by A^(-(k-1)), obtaining a single law supported on sums with powers from -(k-1) to k-1.
It is within sqrt(2Delta_k) in TV of each of its translates by those powers.
For an integer combination v=sum_j c_j alpha^j in this range, translation invariance and the triangle inequality give

    TV(mu,tau_v mu)<=min(1, (sum_j |c_j|)sqrt(2Delta_k)).  (10)

Negative coefficients use that TV(mu,tau_-v mu)=TV(mu,tau_v mu).

<a id="binary-flow-pushforward-invariance"></a>
### Multiplication by alpha has the same small-increment control

There are two exact endpoint descriptions of the next law:

    mu_(n+1)=(mu_n+tau_(alpha^n)mu_n)/2
             =(A_*mu_n+tau_1 A_*mu_n)/2.                 (11)

Both JS gains equal Delta_(n+1).
Distance from either component to its half-mixture is half the distance between the components.
Equation (5) therefore gives

    TV(mu_n,mu_(n+1))<=sqrt(Delta_(n+1)/2),
    TV(A_*mu_n,mu_(n+1))<=sqrt(Delta_(n+1)/2),
    TV(mu_n,A_*mu_n)<=sqrt(2Delta_(n+1)).                 (12)

For the centered law after (9), multiplication by A commutes with the centering map.
Thus the same single law is within sqrt(2Delta_k) of its A-pushforward and of its translates by every power in the centered window.
Inversion of A preserves the same TV bound.
Telescoping consequently controls compositions of these actions, with the explicit sum of their individual errors; it provides no error bound independent of word length.

<a id="first-entropy-drop-height-one"></a>
### Exact finite arithmetic certificates and their limited force

For all n, Delta_n>0.
Indeed JS in (4) is zero exactly when its two finite laws coincide, which would make a nonempty finite support invariant under the nonzero element alpha^(n-1) of the torsion-free additive group O.
That is impossible.
Also JS in (4) equals ell exactly when its component supports are disjoint.
It follows that

    Delta_n<ell
      if and only if P divides a monic polynomial R in Z[t]
      of degree exactly n-1 with coefficients in {-1,0,1}. (13)

For an overlap, subtract the two prefix words and move alpha^(n-1) to one side to obtain such an R.
Conversely the positive and negative coefficient masks of R give an overlap between those two supports.
Monic division by the minimal polynomial is exact over Z.
For n<=d the integral power basis precludes any overlap, so Delta_n=ell.

Thus the first strict entropy drop is exactly one plus the least degree of a monic height-one multiple.
The existence of such multiples when M(P)<2 is already a retained mechanism; (13) does not itself bound its degree or give a large drop.
For example, if N is the first collision time, the preceding law is uniform on 2^(N-1) distinct prefix values.
Writing s for the intersection cardinality with its alpha^(N-1)-translate,

    Delta_N=ell(1-s/2^(N-1)).                            (14)

An existence proof gives only s>=1, and hence guarantees only the deficit lower bound ell/2^(N-1), which tends to zero as N grows.
No positive increment lower bound follows from that observation.

Every individual increment also has an exact integer-log test.
If f_n(x) counts the binary length-n words at x, put

    U_n=product_(x:f_n(x)>0) f_n(x)^(f_n(x)).

Since H_n=n ell-2^(-n)log U_n, one has

    exp(2^n Delta_n)=2^(2^n) U_(n-1)^2/U_n.              (15)

Counts can be defined entirely by polynomial remainders modulo P; no approximate conjugates are needed.
For positive integers a,b, comparison of Delta_n with (log a)/b reduces to comparing the corresponding positive integer powers in (15).
This is a finite certificate for that increment and the upper bound on h_1 in (2).
It is not a finite certificate that all subsequent increments stay above a proposed positive constant.

<a id="effective-binary-near-invariance-time"></a>
### An effective degree-and-measure time for the actual binary law

The companion [norm-grid proof](Yin_C_G0281_v1.md#norm-grid-support-bound) establishes the height-free finite support bound

    |T_n(alpha,{0,1})|<=(4n)^d M(P)^(n-1).                (16)

Its proof was independently checked during this derivation: two algebraic integers in a common sufficiently small embedding grid cell would have nonzero integral norm of absolute value less than one.
Its full cell construction belongs to that companion argument and is not repeated here.
Combining (16) with monotonicity of the increments gives

    Delta_n<=H_n/n<=m+d log(4n)/n.                        (17)

For 0<epsilon<=1 choose the explicit integer

    k=ceil[(2d/epsilon)log(8d/epsilon)],   N=2k-1.

Then Delta_k<=m+epsilon.
To check the constant, set x=8d/epsilon and k_0=(2d/epsilon)log x.
Here x>=8, and log(4t)/t is decreasing for t>=k_0.
Moreover

    d log(4k_0)/k_0
      =epsilon (log x+log log x)/(2log x)<=epsilon.

The ceiling can only improve this inequality.
This is an effective approach to the upper level m, not a convergence rate to h_1: equality h_1=m is not assumed.

Let nu=A_*^(-(k-1))mu_N.
Equations (8), (10), (12) and (17) give, for every |j|<=k-1,

    TV(nu,tau_(alpha^j)nu)<=sqrt(2(m+epsilon)),
    TV(nu,A_*nu)<=sqrt(2(m+epsilon)),
    log|supp nu|<=(m+epsilon)N.                           (18)

For the support estimate apply (16) at N>=k and again use the monotonicity of log(4t)/t.
A TV bound exceeding one may of course be replaced by one.

In particular, for 0<m<=1 take epsilon=m.
These are actual binary laws, with

    max(TV(nu,A_*nu), max_(|j|<k) TV(nu,tau_(alpha^j)nu))
           <=min(1,2sqrt(m)),
    N< (4d/m)log(8d/m)+1,
    log|supp nu|<=2mN<8d log(8d/m)+2m.                   (19)

Thus a hypothetical sequence m tending to zero supplies a quantified family of binary approximate invariants, including its time and dimension-dependent support cost.
This conclusion holds without a power-degree assumption.
It does not assert that the same costs are bounded independently of d or m.

<a id="arbitrary-law-affine-invariance-boundary"></a>
### Arbitrary affine approximate invariants exist at every measure

Here is the coordinator's direct construction showing why the specific law and its resource costs in (18)--(19) matter.
For any A in GL_d(Z), integer R>=0, let u_R be uniform on B_R=[-R,R]^d intersect Z^d.
For integer K>=0 put

    nu_(K,R)=(2K+1)^(-1) sum_(t=-K)^K A_*^t u_R.

All but the two endpoint terms cancel when comparing A_*nu with nu.
As TV between two probability laws is at most one,

    TV(A_*nu_(K,R),nu_(K,R))<=1/(2K+1).                  (20)

For z in Z^d, counting the intersection of two boxes gives

    TV(u_R,tau_z u_R)
      =1-product_(i=1)^d max(0,1-|z_i|/(2R+1))
      <=min(1,||z||_1/(2R+1)).                           (21)

For any finite set W of translations, define D=max_(|t|<=K,w in W)||A^(-t)w||_1, with D=0 if W is empty.
Convexity of TV and its invariance under an integral automorphism yield

    TV(nu_(K,R),tau_w nu_(K,R))<=D/(2R+1) for w in W,
    |supp nu_(K,R)|<=(2K+1)(2R+1)^d.                     (22)

Choose K first and then R to make (20) and all the translation errors smaller than any given positive number.
This works for every integral automorphism and every finite W.
For example, the companion automorphism of t^2-3t+1 is an actual irreducible algebraic-unit flow of positive Mahler entropy and admits all these approximate invariants.

This example disproves an inference from qualitative existence of such laws alone to small or zero entropy.
It is not a counterexample about the particular binary laws in (18), nor about small positive Mahler measure.
Its parameter D may be large and its support cost is not a uniform degree-and-measure bound comparable to (19).

<a id="increment-uniformity-boundary"></a>
### The remaining uniformity obligation

An actual near-zero sequence of Mahler measures, if it existed, would have h_1 tending to zero by (3).
Equations (18)--(19) now give an effective choice of binary laws and their costs at the scale m+epsilon.
The eventual approach of Delta_k to h_1 itself still has no rate supplied here when h_1<m.
Any contradiction must use more than the qualitative invariance already available for arbitrary laws in (20)--(22).

There is also a precise inherited delay.
On a complete k-fold cyclic induction, independent coordinate laws give

    H_(kq+s)^(k)=s H_(q+1)+(k-s)H_q,
    Delta_n^(k)=Delta_(ceil(n/k)).                        (23)

Thus each base increment repeats k times.
This reuses the full-coordinate identity of L G0003 and its probability-law counterpart; it is not a new support formula.
It excludes a degree-free uniform convergence time on complete induced families, but those families lose degree under a positive power.
It does not refute a degree-dependent assertion or one on the all-power-stable small reciprocal core.

The genuinely stronger target exposed by this calculation is an arithmetic restriction on the mass matching in (9), or on the resources of these specific binary near-invariant laws.
Reproving a single height-one relation, qualitative approximate invariance, or the already available m-proportional rates of L G0089--L G0090 would not supply the missing uniform gap.
