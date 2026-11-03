---
author: Yin
---

# Complete linear-moment Mahler cost, house bound and balanced Poisson bridge

This retains the entire original2026-10-07 [L86 argument](../ledger/Yin_L_G0086_v1.md).
Every hypothesis, complete derivation, actual countercontrol and unresolved uniform/source boundary is retained.
No source acquisition, native execution or Task resumption occurs.

## Statement

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d, O=Z[alpha], A its integral companion automorphism and m=log M(P)>0.
On the normalized dual torus let Z_n=sum_(j<n)exp(2pi i<y,A^j1>), A_(n,r)=integral|Z_n|^(2r) and a_(n,r)=A_(n,r)/n^(2r), the collision probability of r uniform orbit choices, not independent binary digits.

For every positive integer sequence r_n/n->kappa in(0,infinity), including any unbounded subsequence,

    liminf (1/n)log a_(n,r_n)>=-m.

If A_(n,r_n)<=(Cr_n n)^(r_n) along such a subsequence, with fixed C>0 and an optional exp(o(n)) factor, then
m>=kappa log(1/(Ckappa)) and C>=exp(-m/kappa)/kappa.
If the same C works at every slope, m>=1/(eC).
For C>=1 and r_n=floor(n/(16C)), the necessary cost is m>=log2/(4C); no such moment hypothesis is proved here.

For any conjugate beta with rho=|beta|>1, let a=ceil(log2/logrho).
For every n,r>=1,

    A_(n,r)<=(2e a n/r)^r(r!)²<=(2e a r n)^r.

The complete signed-dissociation, convex-product/Hölder and angular-series proof includes rho^a=2 and empty residue classes.
For n>=r the diagonal lower bound is r!(n)_r.
A common house lower bound gives a common C, but already directly gives a Mahler gap; no upper cost depending only on total m is inferred.

For fixed lambda>0 let N_j be independent Poisson(lambda), and let C_bal(n,lambda) be the collision probability of
(sum_(j<n)N_j alpha^j, sum_(j<n)N_j) in O direct-sum Z.
Put A_(n,0)=a_(n,0)=1 and p_r=exp(-lambda n)(lambda n)^r/r!.
Exactly,

    C_bal=sum_(r>=0)p_r² a_(n,r)
       =exp(-2lambda n)sum_(r>=0)lambda^(2r)A_(n,r)/(r!)²
       =exp(-2lambda n)integral I0(2lambda|Z_n|),

where I0(u)=(1/(2pi))integral exp(u cos theta)dtheta.
If r=floor(lambda n)>=1, then

    a_(n,r)<=4(ceil(2lambda n)+1)² C_bal(n,lambda).

A central coefficient bound alone does not bound the full series.
If instead a_(n,r)<=exp(-gamma n) throughout the integer window[(lambda-epsilon)n,(lambda+epsilon)n],0<epsilon<lambda, then

    C_bal<=exp(-gamma n)+2exp(-cn),
    c=min(I(lambda-epsilon|lambda),I(lambda+epsilon|lambda))>0,
    I(t|lambda)=tlog(t/lambda)-t+lambda.

Unconditionally C_bal<=exp[-n(2lambda-2a lambda²)] and
liminf (1/n)log C_bal>=-m, retaining the input-dependent a.

For C_orig the unaugmented Poisson collision and K=e²lambda,

    C_bal<=C_orig<=2(floor(Kn)+2)C_bal for every n>=1.

Both normalized negative-log limits exist, agree and are at most m.
For0<lambda<=1/4 one also has Col_binary(n)<=C_orig(n,lambda).
Thus a balanced-Poisson exponential upper bound at such fixed lambda transfers to the binary collision with the same exponential rate and a polynomial prefactor.
These are exact probability comparisons, with no identification of an infinite-support Poisson law with a fixed finite algebraic-entropy alphabet, new uniform estimate or Lehmer proof.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:53 |
| status | open |
| reason | Register the complete original theorem/conditional implications and exact existing inputs; actual current whole review and adoption follow separately. No unproved estimate, uninspected source or old independent label is promoted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | All exact moment/linear-slope/subsequence cost assertions, full house-dependent all-order bound with its guards, complete balanced/unaugmented Poisson identities/central-window/tail/rate and guarded binary comparisons. |
| argument | [Entire original proof](#argument) | Entire original continuous small-body proof, strict highest-term dissociation, convex-product/Hölder/angular series, diagonal lower bound, exact Poisson conditioning/Bessel integral/mode/Chernoff bounds, polynomial total-coordinate removal and rate directions. |
| dependency | [Explicit real-block body](Yin_C_G0275_v1.md#actual-core-pointwise-fourier-obstruction) | Only the complete full-dimensional body construction, phase and volume factors; no finite dual-lattice argument or unproved Fourier/moment target is assumed. |
| support | [Moment definitions and conditional target](Yin_C_G0275_v1.md#faithful-high-moment-arithmetic-interface) | Original Haar energy and the precisely conditional common-C target only; every all-order/Poisson argument is proved here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:00 |
| status | proved |
| reason | Adopt the complete original small-body linear-moment cost, exact house-dependent all-order bound and full balanced/unaugmented Poisson identities, window/tail/rate and binary comparisons after actual whole self-review. All infinite-law, polynomial-loss, slope and uniformity guards remain; no new estimate, source or computation is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All exact moment/linear-slope/subsequence cost assertions, full house-dependent all-order bound with its guards, complete balanced/unaugmented Poisson identities/central-window/tail/rate and guarded binary comparisons. |
| argument | [Argument](#argument) | Entire original continuous small-body proof, strict highest-term dissociation, convex-product/Hölder/angular series, diagonal lower bound, exact Poisson conditioning/Bessel integral/mode/Chernoff bounds, polynomial total-coordinate removal and rate directions. |
| dependency | [Dependency](Yin_C_G0275_v1.md#actual-core-pointwise-fourier-obstruction) | Only the complete full-dimensional body construction, phase and volume factors; no finite dual-lattice argument or unproved Fourier/moment target is assumed. |
| support | [Support](Yin_C_G0275_v1.md#faithful-high-moment-arithmetic-interface) | Original Haar energy and the precisely conditional common-C target only; every all-order/Poisson argument is proved here. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0534_v1.md#current-moment-poisson-finding) | Entire current statement, complete original proof and every selected interface at the exact scope, self-reviewed; all old reviews keep their actual fixed inputs and relationship scopes. |

## Complete retained argument

<a id="argument"></a>

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d.
Put O=Z[alpha], m=log M(P)>0, and let A in GL_d(Z) be multiplication by alpha in the power basis.
For n,r>=1 define

    Z_n(y)=sum_(j=0)^(n-1) exp(2pi i<y,A^j1>),
    A_(n,r)=integral_(T^d) |Z_n(y)|^(2r) dy,
    a_(n,r)=A_(n,r)/n^(2r),                               (1)

where dy is normalized Haar measure on the continuous torus dual to O.
Equivalently A_(n,r) counts the ordered pairs of r-term lists from 1,alpha,...,alpha^(n-1) with equal sums.
Thus a_(n,r) is the collision probability of the sum of r independent uniform choices from those n orbit elements.
This is a different law from independent binary digits.
The exact finite primitive quotient representation, when desired, is supplied by [L G0084](Yin_C_G0275_v1.md#faithful-high-moment-arithmetic-interface).
None of the following arguments needs that finite model.

<a id="linear-moment-necessary-cost"></a>
### A linear-order moment estimate already contains an entropy gap

For every fixed input and every sequence r_n of positive integers with r_n/n -> kappa in (0,infinity),

    liminf_(n->infinity) (1/n) log a_(n,r_n)>=-m.           (2)

The same lower bound holds along any unbounded subsequence.
We prove it from the explicit adapted body in [L G0084](Yin_C_G0275_v1.md#actual-core-pointwise-fourier-obstruction), without using its finite dual lattice argument.
Its real diagonal-block construction gives a symmetric body K_n(delta) with

    K_n(delta) subset [-delta,delta]^d,
    |<y,A^j1>|<=delta for 0<=j<n,
    vol K_n(delta)=c_A delta^d exp(-nm),   c_A>0.           (3)

This volume identity follows by scaling each real eigenvalue block by max(1,|alpha_i|)^(-n); a complex conjugate pair is a rotation-dilation disk and contributes twice to the exponent.
Separability of P supplies the real block diagonalization.

For 0<delta<1/4, projection of the body into T^d is injective, and Re Z_n(y)>=n cos(2pi delta)>0 on it.
Consequently

    a_(n,r)>=c_A delta^d exp(-nm) cos(2pi delta)^(2r).      (4)

Take delta=n^(-1/2) for sufficiently large n.
The logarithm of its volume correction is O_A(log n), and 2r_n log cos(2pi/sqrt(n))=O_kappa(1).
Dividing (4)'s logarithm by n proves (2).
The elementary estimate log cos x=O(x^2) near zero suffices; it follows, for example, from cos x>=1-x^2/2 and log(1-u)>=-2u for 0<=u<=1/2.

Suppose now that along an unbounded sequence of such n,

    A_(n,r_n)<=(C r_n n)^(r_n),     r_n/n -> kappa>0,      (5)

with a fixed C>0.
Its normalized logarithm tends to at most kappa log(C kappa).
Comparing with (2) gives necessarily

    m>=kappa log(1/(C kappa)),
    C>=exp(-m/kappa)/kappa.                               (6)

The bound is informative when C kappa<1.
If an extra factor exp(o(n)) is allowed on the right of (5), the conclusion is unchanged.
If the same C works at every linear slope kappa, optimizing at kappa=1/(eC) gives

    m>=1/(eC),    C>=1/(em).                              (7)

For the particular L G0084 target C>=1 and r_n=floor(n/(16C)), the direct conclusion is

    m>=log(16)/(16C)=log2/(4C).                           (8)

This is a strict strengthening of that record's displayed Markov consequence under the same moment hypothesis: its gamma is log2/(16C).
No new moment hypothesis is proved by (8).
The argument simply reveals how much of the desired gap is already contained in the proposed linear-order bound.
It does not infer such a bound from fixed-order asymptotics.

<a id="elementary-house-moment-bound"></a>
### A full upper bound is available with a house-dependent constant

Choose any conjugate beta of alpha with rho=|beta|>1, and put

    a=ceil(log2/log rho)>=1.                              (9)

For all n,r>=1 one has the explicit bound

    A_(n,r)<=(2e a r n)^r.                                (10)

Here is a complete proof.
Partition the indices j<n by their residue classes modulo a.
In one class, no nonempty signed sum sum_j epsilon_j alpha^j with epsilon_j in {-1,0,1} and distinct indices can vanish.
Under the chosen embedding, the largest nonzero term has modulus strictly larger than the sum of the others, since rho^a>=2 and the finite preceding geometric sum is strictly smaller than its last term.
The corresponding torus characters therefore have no nonempty relation with coefficients in {-1,0,1}.

Let Z_b be the orbit sum in one residue class, containing k_b indices.
For real t and any real phase theta, convexity on [-1,1] gives

    exp(t x)<=cosh t+x sinh t,    -1<=x<=1.

Apply this to x=Re(exp(-i theta)chi_j(y)) and multiply over the class.
Every nonconstant term of the resulting product has zero torus integral: expanding its real parts produces exactly the signed relations just excluded.
Therefore

    integral exp(t Re(exp(-i theta)Z_b)) dy
       <=(cosh t)^(k_b)<=exp(k_b t^2/2).                  (11)

The last inequality follows by integrating tanh t<=t for t>=0 and using evenness.
There are a residue classes, including empty ones if needed.
Holder's inequality gives

    integral exp(t Re(exp(-i theta)Z_n)) dy
       <=product_b [integral exp(a t Re(exp(-i theta)Z_b))dy]^(1/a)
       <=exp(a n t^2/2).                                 (12)

Average over theta.
Expanding the exponential and retaining equal positive and negative angular powers gives the exact nonnegative series

    (1/(2pi)) integral_0^(2pi) exp(t Re(exp(-i theta)z)) dtheta
       =sum_(s>=0) t^(2s)|z|^(2s)/(4^s(s!)^2).            (13)

Tonelli's theorem, or uniform absolute convergence on the bounded range |Z_n|<=n, permits termwise averaging.
Thus

    t^(2r) A_(n,r)/(4^r(r!)^2)<=exp(a n t^2/2).

Take t^2=2r/(an).
It follows that

    A_(n,r)<=(2e a n/r)^r (r!)^2<=(2e a r n)^r,

proving (10).
This elementary character argument does not require all-power degree preservation or a result on S-unit equations.

For comparison, the diagonal equal-multiset relations give

    A_(n,r)>=r! n(n-1)...(n-r+1) for n>=r.                 (14)

Indeed each ordered list of r distinct indices admits r! permutations as its matching right list.
Hence for every fixed alpha and fixed r, (10) and (14) give A_(n,r)=Theta_(alpha,r)(n^r) as n tends to infinity.
This statement alone does not control constants when r grows linearly with n.
A fixed-order bound uniform in alpha would have a different quantifier and is not claimed from this proof.

If rho has a common lower bound greater than one, (9)--(10) give a common C at all orders.
But such a house lower bound already gives the simpler Mahler gap m>=log rho.
The value of (10) here is to identify an explicit sufficient arithmetic domain and its loss, not improve that elementary gap.
In the general target class the constant grows like 1/log rho as rho decreases to one.
The inequality m>=log rho does not bound this constant from above in terms of m alone; many expanding conjugates can contribute to m.
Passing to alpha^a in this proof pays for all a residue classes in (12).

<a id="balanced-poisson-moment-bridge"></a>
### Balanced Poissonization and exact return to linear moments

Fix lambda>0 and let N_0,...,N_(n-1) be independent Poisson variables of mean lambda.
In the additive group O direct-sum Z define

    Y_(n,lambda)=(sum_(j<n) N_j alpha^j, sum_(j<n) N_j).

The extra coordinate records the total number of chosen terms.
Its presence is essential for the next identity: without it, collisions with different list lengths would also be counted.
Write C_(n,lambda) for this law's collision probability and p_r=exp(-lambda n)(lambda n)^r/r!, r>=0.
Put A_(n,0)=a_(n,0)=1.
Conditioning on the two independent total counts yields

    C_(n,lambda)=sum_(r>=0) p_r^2 a_(n,r)
       =exp(-2lambda n) sum_(r>=0) lambda^(2r) A_(n,r)/(r!)^2.
                                                               (15)

Conditional on total r, the occupation counts are multinomial with r independent uniform index choices, so the conditional collision probability is exactly a_(n,r).
Equivalently define I_0(u)=(1/(2pi))integral_0^(2pi) exp(u cos theta)dtheta by its displayed integral.
Formula (13) gives

    C_(n,lambda)=exp(-2lambda n)
                   integral_(T^d) I_0(2lambda |Z_n(y)|) dy.      (16)

No asymptotic Bessel formula is used.
One may also obtain this identity by taking the Fourier transform on the full dual T^d times T: its squared modulus is exp[-2lambda n+2lambda Re(exp(2pi i s)Z_n(y))].

There is a polynomial-cost return from (15) to its central linear-order moment.
Put mu=lambda n, r=floor(mu)>=1 and K=ceil(2mu).
A Poisson(mu) variable has a mode at r, because the consecutive probability ratio is mu/(j+1).
Markov's inequality gives probability at least 1/2 in {0,...,K}.
Consequently p_r>=1/[2(K+1)], and (15) implies

    a_(n,floor(lambda n))
       <=4(ceil(2lambda n)+1)^2 C_(n,lambda).              (17)

Thus an exponential upper bound for the balanced Poisson collision gives a linear-order moment bound with the same exponential rate, losing only a polynomial factor.
Conversely, a bound at only the central r does not upper-bound the sum in (15); it controls just one of its nonnegative terms.

An exact sufficient converse uses a window.
Suppose 0<epsilon<lambda and, for every integer r in [(lambda-epsilon)n,(lambda+epsilon)n], one has a_(n,r)<=exp(-gamma n).
For t>0 put

    I(t|lambda)=t log(t/lambda)-t+lambda,
    c=min(I(lambda-epsilon|lambda),I(lambda+epsilon|lambda))>0.

The Poisson moment generating function E exp(sN)=exp(lambda n(exp(s)-1)), followed by Markov with s=log(t/lambda), bounds its lower and upper tails by exp[-n I(t|lambda)].
Since 0<=a_(n,r)<=1 and p_r^2<=p_r, (15) gives

    C_(n,lambda)<=exp(-gamma n)+2exp(-cn).                 (18)

This states explicitly the additional range required for the reverse implication, rather than silently substituting a fixed-order or one-coefficient estimate into a series.

Finally (12), averaged over its phase with t=2lambda, proves the unconditional but house-dependent bound

    C_(n,lambda)<=exp[-n(2lambda-2a lambda^2)].             (19)

For lambda=1/(2a) this gives exp[-n/(2a)].
On the other hand, (2), (15) and the same central-mode lower bound show, for every fixed lambda>0,

    liminf_n (1/n)log C_(n,lambda)>=-m.                    (20)

Thus any input-uniform exponential Poisson estimate at a fixed lambda would itself have to respect the Mahler cost.
These are exact probability comparisons for an infinite-support law, not an assertion that its entropy equals DGB16 algebraic entropy or that a Poisson alphabet is the fixed finite set in that definition.
Equations (15)--(20) explain precisely what this reparameterization retains and what new uniform estimate it would still require.

<a id="removing-poisson-total-coordinate"></a>
### Removing the total coordinate costs no collision exponent

Let C_orig(n,lambda) denote the collision probability of the unaugmented sum sum_j N_j alpha^j.
Marginalizing can only increase collision probability, so C_(n,lambda)<=C_orig(n,lambda).
The reverse comparison holds up to a polynomial factor.
Choose K=e^2 lambda and b=(e^2+1)lambda>lambda.
The preceding Chernoff calculation gives

    P(sum_j N_j>Kn)<=exp(-bn).

Write p(x,s) for the joint augmented mass, and split its marginal at L=floor(Kn).
The inequality (u+v)^2<=2u^2+2v^2, followed by Cauchy--Schwarz on the L+1 retained s-values, gives

    C_orig(n,lambda)
      <=2(L+1)C_(n,lambda)+2exp(-2bn).

The joint all-zero atom has probability exp(-lambda n), hence C_(n,lambda)>=exp(-2lambda n).
Therefore, for every n>=1,

    C_(n,lambda)<=C_orig(n,lambda)
       <=2(floor(Kn)+2)C_(n,lambda).                     (21)

This proves equality of their lower and upper normalized logarithmic collision limits.
In fact both limits exist: independent time blocks, with the injective maps A and A direct-sum I respectively, make collision probabilities supermultiplicative.
Their negative logarithms are subadditive and finite, since the all-zero atoms give the bound 2lambda n.
Equation (20) consequently bounds their common order-two entropy rate by m.
This is a direct probability and volume argument, with no infinite-alphabet algebraic-entropy theorem.

There is also an exact one-sided binary comparison.
In the notation S_n=sum_j sin^2(pi<y,A^j1>) of L G0084, the Fourier square for the unaugmented Poisson law is exp(-4lambda S_n).
For 0<lambda<=1/4 the binary Fourier square satisfies

    product_j cos^2(pi<y,A^j1>)<=exp(-S_n)
                                  <=exp(-4lambda S_n).

Integrating over T^d yields

    Col_binary(n)<=C_orig(n,lambda),    0<lambda<=1/4.     (22)

Thus an exponential upper bound for the balanced Poisson law at such a fixed lambda transfers, by (21), to a binary collision bound with the same rate and only a polynomial prefactor.
The order-two entropy rates have the reverse inequality.
Removing the total coordinate preserves the rate, but does not turn a single coefficient in (15) into control of its entire series.
