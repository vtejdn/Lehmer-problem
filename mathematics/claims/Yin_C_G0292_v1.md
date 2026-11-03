---
author: Yin
---

# Saturated integer posterior models with a strict fourth-order Gram deficit

This retains the complete original2026-10-07 [L99 proof](../ledger/Yin_L_G0099_v1.md), authored by assess_shortness_route for Yin.
The actual old derivation and whole review remain in [R28](../audits/reviews/Yin_R_G0028_v1.md#contribution-and-review-scope).
No source, computation or Task is newly executed.
The normal channel below identifies a proved limit of exact finite integer models, rather than replacing their fibers by continuous noise.

## Statement

For positive integers M,c and independent fair signs xi0,...,xiM,observe
Y_(M,c)=c xi0+sum_(i=1)^M xi_i,with the noise columns first and distinguished c last.
Its integer row map is surjective and its relation lattice is saturated.
The endpoint leverage and Gram growth are

    l_(M,c)=c²/(M+c²),
    J_(M,c)=-(1/2)log(1-l_(M,c)).

Let I_(M,c)=I(xi0;Y_(M,c)) in natural logarithms.
For every fixed s>0 and every positive integer sequence c_M with c_M/sqrt(M) tending to s,

    l_(M,c_M) tends to l(s)=s²/(1+s²),
    I_(M,c_M) tends to I_G(s)<J(s)=(1/2)log(1+s²),

where I_G(s) is the information in s xi+Z for an independent standard normal Z.
A direct binomial-ratio, normalization and tail proof establishes this limit without importing a local limit theorem.
Moreover J(s)-I_G(s)=l(s)^4/12+O(l(s)^5) at zero.
There is a sequence of actual finite integer models with l_(M,c) tending to0 and

    J_(M,c)-I_(M,c)=l_(M,c)^4/12+o(l_(M,c)^4)>0.

For each finite model, with row projection Pi,linear predictor L=(Pi xi)_j and b=E[xi0 given Y],
E[b h(L)]=E[xi0 h(L)] for every polynomial h of every degree.
Thus even exact integer fibers, a saturated integer kernel, arbitrarily small leverage and all polynomial posterior identities do not imply I>=-(1/2)log(1-l).
The models are not algebraic-unit power orbits: many initial columns equal1,while the last chosen c>1.
Their J is a finite one-row Gram growth, not the Mahler measure of an irreducible unit polynomial.
They neither refute an improved comparison on the arithmetic core nor construct a near-one Mahler family.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:58 |
| status | open |
| reason | Full original exact finite model, direct binomial limit, strict Gaussian entropy and diagonal-selection proof retained; current complete checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire saturated integer-observation countercontrol, every fixed-s binomial posterior limit, strict information/Gram deficit and exact fourth-order finite diagonal family, preserving all polynomial identities and non-power-orbit limits. |
| argument | [Complete argument](#argument) | Full original1–9: exact parity/fiber ratios, compact binomial normalization and Chebyshev tails, Gaussian relative entropy with fourth-moment strictness, bounded-derivative Taylor remainder and finite-model diagonal selection. |
| support | [Generic posterior identities](Yin_C_G0287_v1.md#posterior-covariance-leverage) | Defines the exact row projection and posterior information framework being tested; the complete model and its limiting proof are self-contained. |
| support | [Cubic posterior test](Yin_C_G0290_v1.md#fourth-posterior-moment) | Existing mixed-polynomial hierarchy context only; no universal information/Gram inequality or arithmetic realization is assumed. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:03 |
| status | proved |
| reason | Adopt the whole original finite integer model, direct binomial limit, strict Gaussian deficit and diagonal family after actual complete self-review; retain every polynomial identity, parity/Taylor/tail normalization and the explicit absence of an algebraic power-orbit or Mahler counterexample. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire saturated integer-observation countercontrol, every fixed-s binomial posterior limit, strict information/Gram deficit and exact fourth-order finite diagonal family, preserving all polynomial identities and non-power-orbit limits. |
| argument | [Argument](#argument) | Full original1–9: exact parity/fiber ratios, compact binomial normalization and Chebyshev tails, Gaussian relative entropy with fourth-moment strictness, bounded-derivative Taylor remainder and finite-model diagonal selection. |
| support | [Support](Yin_C_G0287_v1.md#posterior-covariance-leverage) | Defines the exact row projection and posterior information framework being tested; the complete model and its limiting proof are self-contained. |
| support | [Support](Yin_C_G0290_v1.md#fourth-posterior-moment) | Existing mixed-polynomial hierarchy context only; no universal information/Gram inequality or arithmetic realization is assumed. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-integer-deficit-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire saturated integer-observation countercontrol, every fixed-s binomial posterior limit, strict information/Gram deficit and exact fourth-order finite diagonal family, preserving all polynomial identities and non-power-orbit limits. |
| argument | [Argument](#argument) | Full original1–9: exact parity/fiber ratios, compact binomial normalization and Chebyshev tails, Gaussian relative entropy with fourth-moment strictness, bounded-derivative Taylor remainder and finite-model diagonal selection. |
| support | [Support](Yin_C_G0287_v1.md#posterior-covariance-leverage) | Defines the exact row projection and posterior information framework being tested; the complete model and its limiting proof are self-contained. |
| support | [Support](Yin_C_G0290_v1.md#fourth-posterior-moment) | Existing mixed-polynomial hierarchy context only; no universal information/Gram inequality or arithmetic realization is assumed. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0539_v1.md#current-integer-deficit-finding) | Entire exact current statement, complete retained original argument and all selected interfaces, self-reviewed; original old checks retain only their actual old inputs and exact relationships. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0547_v1.md#f-g293) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="integer-fiber-gram-deficit"></a>
### An exact integer model and the conclusion

Let xi_0,xi_1,...,xi_M be independent fair signs.
For positive integers M,c observe the integer

    Y_(M,c)=c xi_0+sum_(i=1)^M xi_i.

Take the noise columns first and the distinguished column c last.
The one-row integer observation matrix has full row rank, maps Z^(M+1) onto Z, and has a primitive integer kernel.
Its endpoint leverage and Gram growth are exactly

    l_(M,c)=c^2/(M+c^2),
    J_(M,c)=(1/2)log[(M+c^2)/M]
           =-(1/2)log(1-l_(M,c)).                       (1)

Write I_(M,c)=I(xi_0;Y_(M,c)) in natural units.
For every fixed s>0, if c_M is a positive integer sequence with c_M/sqrt(M) tending to s, then

    l_(M,c_M) -> l(s):=s^2/(1+s^2),
    I_(M,c_M) -> I_G(s),
    I_G(s)<J(s):=(1/2)log(1+s^2).                       (2)

Here I_G(s) is the information in the auxiliary real channel Y=s xi+Z, where xi is a fair sign and Z is an independent standard normal variable.
That channel only identifies the limit; the countercontrols themselves have finite exact integer fibers and no added continuous noise.

In particular, for every sufficiently small prescribed positive limiting leverage, actual integer models satisfy I_(M,c)<J_(M,c).
More precisely there is a sequence of such models with l_(M,c) tending to zero and

    J_(M,c)-I_(M,c)=(1/12)l_(M,c)^4+o(l_(M,c)^4)>0.       (3)

Thus a universal inequality I>=-(1/2)log(1-l) cannot follow from integer fibers, the projection identities, and all their polynomial tests alone.

<a id="binomial-posterior-limit"></a>
### A direct binomial proof of the limit

Put S_M=sum_(i=1)^M xi_i and, for k congruent to M modulo 2,

    r_M(k)=P(S_M=k)=2^(-M) binom(M,(M+k)/2),

with r_M(k)=0 outside its support.
Conditional on xi_0=1, the observation is c+S_M.
Its posterior bias at c+k is

    b_(M,c)(c+k)
      =[r_M(k)-r_M(k+2c)]/[r_M(k)+r_M(k+2c)].            (4)

The denominator is positive at every value under this conditional law.
Reflection of all signs shows that the expectation of the even function

    g(x)=((1+x)/2)log(1+x)+((1-x)/2)log(1-x)

is the same under either conditional law.
Hence the finite information is exactly

    I_(M,c)=sum_k r_M(k) g(b_(M,c)(c+k)).                 (5)

These are finite rational probabilities and exact logarithmic expressions, not a numerical approximation to the fibers.

We give the needed binomial limit directly.
Let k_0 be 0 or 1 according to the parity of M.
The elementary ratio is

    r_M(k+2)/r_M(k)=(M-k)/(M+k+2).

For any fixed R, sum its logarithm from k_0 to k, using log(1+u)=u+O(u^2).
Symmetry handles negative k.
Uniformly for |k|<=R sqrt(M) on the permitted lattice, this gives

    r_M(k)/r_M(k_0)=exp[-k^2/(2M)+o_R(1)].               (6)

For example the sum of the quadratic remainder is O_R(M^(-1/2)); the harmless k_0^2/(2M) tends to zero.
Also E(S_M^2)=M, so P(|S_M|>R sqrt(M))<=R^(-2).

For completeness these facts determine the normalizing constant without invoking a local limit theorem.
Set a_M=sqrt(M) r_M(k_0)/2.
Equation (6) and the mesh 2/sqrt(M) express the mass in [-R,R] as a_M times a Riemann sum for exp(-z^2/2), up to a relative error tending to zero.
Taking one fixed R>1 bounds a_M above and below away from zero.
Every subsequential limit a satisfies

    1-R^(-2)<=a integral_(-R)^R exp(-z^2/2) dz<=1

for every R>1.
Letting R tend to infinity gives a=(2pi)^(-1/2).
Thus S_M/sqrt(M) converges to the standard normal law, with (6) uniform on every compact window.

If c_M/sqrt(M)->s, apply (6) at k and k+2c_M.
Uniformly for z=k/sqrt(M) in a fixed compact interval,

    r_M(k+2c_M)/r_M(k) -> exp[-2s(z+s)],
    b_(M,c_M)(c_M+k) -> tanh[s(z+s)].                   (7)

Since 0<=g<=log2, the same Chebyshev tail bound controls the complementary interval in (5).
The compact Riemann sums, followed by R tending to infinity, therefore prove

    I_(M,c_M) -> E[g(tanh(s(Z+s)))]=I_G(s).

The equality with the real-channel information follows also directly from its two normal conditional densities; their likelihood ratio at y is exp(2sy).
This proves the convergence in (2) with no external limit theorem.

<a id="strict-gaussian-information-deficit"></a>
### Strict loss and its small-leverage order

Let phi be the standard normal density.
The channel output has density

    q_s(y)=phi(y) exp(-s^2/2) cosh(sy),

mean zero and variance 1+s^2.
Its logarithm has at most quadratic growth, so the differential entropy computations below are integrable.
Let phi_(1+s^2) be the centered normal density of that variance.
A direct expansion of the logarithms in relative entropy gives

    J(s)-I_G(s)
      =integral q_s log[q_s/phi_(1+s^2)] >=0.            (8)

Nonnegativity follows from the elementary logarithm inequality, with equality only when the two densities agree almost everywhere.
Equality is impossible for s>0: the fourth moment of q_s is 3+6s^2+s^4, whereas the normal density of the same variance has fourth moment 3+6s^2+3s^4.
This proves the strict inequality in (2).

An explicit expansion identifies how small this loss can be.
Evaluating the conditional density ratio gives

    I_G(s)=s^2-E log cosh(sY),   Y=Z+s xi.

All derivatives of log cosh of positive order are bounded after the first, and the first is bounded as well.
Its Taylor formula through degree eight consequently has an absolute remainder O(|x|^10) on the real line.
Since E|Y|^10 is bounded for |s|<=1, termwise expectation is justified with remainder O(s^10).
Using

    log cosh x=x^2/2-x^4/12+x^6/45-17x^8/2520+O(x^10),
    E Y^2=1+s^2,
    E Y^4=3+6s^2+s^4,
    E Y^6=15+45s^2+15s^4+s^6,
    E Y^8=105+O(s^2),

one obtains

    I_G(s)=s^2/2-s^4/4+s^6/6-5s^8/24+O(s^10),
    J(s)-I_G(s)=s^8/12+O(s^10)
              =l(s)^4/12+O(l(s)^5).                    (9)

To obtain (3), choose any sequence s_j>0 tending to zero.
For each j, (2) permits an integer M_j and c_j with c_j/sqrt(M_j) sufficiently close to s_j that both the information error and the leverage error are at most l(s_j)^5.
The function -(1/2)log(1-l) has bounded derivative near zero.
Equation (9) therefore transfers to these finite integer observations and proves (3).

<a id="all-polynomial-tests-boundary"></a>
### What the model preserves, and what the orbit must add

For each finite model, let Pi be its row projection and let L be the j-th coordinate of Pi xi for the distinguished bit.
Then L is exactly measurable in the integer observation Y, and b=E[xi_0|Y] satisfies

    E[b h(L)]=E[xi_0 h(L)]

for every polynomial h, of every degree.
All quantities are finite, and every mixed fair-sign moment on the right is exactly determined by the row coefficients.
Thus the model obeys not only the cubic test behind L G0097 but the full hierarchy proposed by polynomial testing.
It also has a surjective integer observation and a saturated integer relation lattice.
Its strict deficit is therefore an actual obstruction to the universal generic linear-observation inequality, not an artifact of relaxing to real coefficients or of replacing exact fibers by a continuous model.

The construction deliberately does not supply an algebraic power orbit.
Its many initial columns equal 1, while its last column is c>1 for the chosen large indices.
Consecutive powers with alpha^0=alpha^1=1 would have alpha=1 and could not end with that last column.
In particular this is neither a positive irreducible unit example nor an all-power-stable near-one Mahler family.
Its J_(M,c) is a finite one-row Gram growth, not the Mahler measure of such a polynomial.

Accordingly the result does not refute an improved comparison or a gap on the arithmetic core.
It shows precisely that integer fibers, posterior polynomial identities and small leverage by themselves allow a fourth-order strict loss.
Any argument excluding that behavior for the core must use additional simultaneous power-orbit structure.
Continuing the polynomial hierarchy may sharpen L G0097 further, but cannot prove the generic identity it fails in (3).
