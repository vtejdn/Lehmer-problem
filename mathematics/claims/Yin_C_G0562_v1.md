---
author: Yin
---

# Complete nonlinear original endpoint profiles and unconditional real finite-tail bounds

This retains the entire [L298](../ledger/Yin_L_G0298_v1.md) argument and its real source/exploration limits without a new research or computational run.

<a id="statement"></a>
## Complete statement

Use independent ORIGINAL digits with probabilities1/4,1/2,1/4 on{-1,0,1}.
For every real d-by-B matrix X, B>=1, endpoint law mu and Q=XX^T, let E(z)=z^T Q^+z be the squared minimum REAL preimage norm.
Define
    I(x)=(1+x)log(1+x)+(1-x)log(1-x), -1<=x<=1,
    J(v)=I(sqrt(v)), 0<=v<=1,
with0log0=0.
Every actual endpoint satisfies0<=E(z)<=B and mu(z)<=exp[-B J(E(z)/B)], even for singular Q.
No conditional independence or asymptotic large-deviation theorem is assumed.

For INTEGER X, put p=mu(0), a=log2, c=a-1/2, kappa=2-2a and r=log(1/p)/B in[0,a].
Let v_r be the unique solution in[0,1) of J(v_r)-v_r/2=r, and Psi(r)=r-c v_r.
Then for every endpoint
    mu(z)<=exp[-B Psi(r)] exp[-a E(z)]<=p^kappa exp[-a E(z)].
Psi is continuous and strictly increasing, Psi(0)=0, Psi'(r)>=kappa, and
    kappa r<Psi(r)<r (r>0), lim_(r->0+)Psi(r)/r=kappa.
The exact envelope identity
    min_(0<=v<=1)[max{r+v/2,J(v)}-av]=Psi(r)
limits only what follows by combining the two proved estimates mu<=p exp(-E/2) and the absolute J bound.
It neither asserts attainment by actual integer maps nor refutes the sharp C1 profile.

For EVERY ACTUAL nonzero algebraic integer alpha, including torsion, nonunits and all neutral/complex roots, let P be its actual monic minimal of degree d, m=log M(P), M multiplication by alpha in the full integer power basis and v represent1.
For any i>=0 and B>=d set
    z_j=-M^(d+j)v, A_i=[z_0,...,z_(i-1)],
    W_i=(I+A_i A_i^T)^(-1), X=[z_i,...,z_(i+B-1)],
    Q=XX^T>0, D=(W_i^(-1)+Q)^(-1),
    Delta_i=det(I+A_i A_i^T), Delta_0=1,
    G_(i,B)(u)=exp[a u^T D u] E exp[-a(X eta+u)^T W_i(X eta+u)].
For the ENTIRE u in R^d,
    p_B<=G_(i,B)(0)<=sup_u G_(i,B)(u)
       <=K_d sqrt(Delta_i) exp[-B Psi(log(1/p_B)/B)]
       <=K_d sqrt(Delta_i) p_B^kappa,
    K_d=2^(d/4)(2pi/log2)^(d/2).
The POSITIVE completion factor is canceled exactly, never omitted.
For i>=1 the entire logarithmic cost is at most log K_d+mi+(d/2)log(i+d)-(1/2)log|disc P|+m(d-1).
At i=0 the exact cost is log K_d, with |disc P|=1 at d=1.

At FIXED P and every integer i_B=o(B), let g_B=-(1/B)log sup_u G_(i_B,B)(u) and h=lim -(1/B)log p_B in[0,log2].
Then
    Psi(h)<=liminf g_B<=limsup g_B<=h.
At h=0 this forces g_B to0; at h>0 the lower bound is strictly greater than kappa h, but no existence/equality of the full limit is claimed.
The ratio Psi(h)/h tends to kappa<1 near zero.
C311's stronger hyperbolic fixed-prefix rate remains applicable in its actual domain.
All source-discovery leads remain unadopted, and no new source, J, numerical computation, C1 theorem, lossless neutral rate or uniform Mahler gap is asserted.

## Complete argument

<a id="argument"></a>

### Reuse and changed long-window question

The full fixed L294 short-relation quotient, L290 exact one-relation proof, L286 actual finite-tail maximum, and L251 original endpoint Fourier moments were reread.
L294 settles all quadratic inputs only through length4 and composed quadratic windows through2d; its nontorsion class is hyperbolic.
The unresolved target here is arbitrary long ORIGINAL windows, including actual neutral nontorsion roots, or a genuine finite-map obstruction that changes the proposed general profile.
No new assertion follows from enlarging J73's box.

A bounded external discovery screen used Gaussian domination/Bernoulli relative concentration and discrete-Gaussian lattice/covariance terms.
Ordinary unconditioned tail estimates, reflection-positive Ising results and full untruncated lattice theta comparisons do not supply the required finite-cube profile at the actual zero atom; no external theorem, source acquisition or novelty claim is adopted.
In particular L251's weaker coefficient1/2 is an exact local premise, while coefficient log2 remains unproved in this generality.

The current alternate question is whether the actual FULL finite-tail maximum can be controlled in exponential rate without proving(C1) at every endpoint.
The precise finite object is

    G_(i,b)(u)=exp[a u^T D_b u] E exp[-a(S_b+u)^T W_i(S_b+u)],
    a=log2, Q_b=XX^T, D_b=(W_i^(-1)+Q_b)^(-1).

Every original digit retains probabilities1/4,1/2,1/4.
In the neutral directions the crude scaled support is order sqrt(b), unlike the bounded hyperbolic scaled support of L286, so its stationary-point argument only pays an order-b expense.
A new argument must address the tilt and joint support at its maximizing point, not omit the positive outside factor or take an unrestricted supremum through entrywise convergence.
Any exploratory calculation that becomes evidence will be declared and kept in a responsible J before running.


<a id="interpolated-profile-reuse"></a>
### 1. Changed unconditional route and exact premises

The sharp coefficient log2 relative to p_b is still open.
The new route keeps the weaker relative estimate and combines it with the EXACT original bounded-digit entropy cost.
This yields an unconditional full-tail bound for every actual input, including arbitrarily long neutral windows.
It deliberately retains a quantified loss in the power of p_b.

Local reuse was checked before this derivation: [L251](Yin_C_G0419_v1.md#original-relative-gaussian-atom-profile) proves the original relative endpoint bound, [L255](Yin_C_G0432_v1.md#complete-neutral-covariance-profile) optimizes its covariance form, [L211](../ledger/Yin_L_G0211_v1.md) already uses the original moment-generating function and relative-entropy variational estimate, and [L282](Yin_C_G0517_v1.md#finite-prefix-schur-remainder)/[L286](Yin_C_G0529_v1.md#conditional-sharp-profile-transfer) supply the ACTUAL finite matrices, translated lattice summation and exact positive completion.
The finite relative-entropy chain and its nonnegativity are existing elementary mechanisms, not a new external theorem.
The new combination, explicit nonlinear exponent, complete actual-tail consequence and precise envelope limitation are derived below.
No external source theorem, program, numerical root calculation or new J is used.

The coordinator authors this entire new argument.
Sibling D166--D168 arguments are not premises or proof contributions.
Source-discovery leads in the opening screen are not adopted.
This is an author argument pending complete separately organized noncontributor review.

<a id="exact-original-absolute-profile"></a>
### 2. An exact bounded-digit absolute endpoint cost

Let X be any real d-by-b column matrix, let eta_j be independent ORIGINAL digits with probabilities(1/4,1/2,1/4), and let mu(z)=Pr(X eta=z), p=mu(0).
Put Q=XX^T and
    E(z)=z^T Q^+ z,
where Q^+ is its inverse on its range and zero on its kernel.
Endpoints of positive probability lie in range Q.
The identity
    E(z)=min{||x||^2: Xx=z}
follows from orthogonal projection onto the row space of X: the minimizer is X^T Q^+z and the other preimages differ by ker X.

Define, continuously on[-1,1],
    I(x)=(1+x)log(1+x)+(1-x)log(1-x),
    I(0)=0, I(1)=I(-1)=2log2,
using0log0=0.
For every actual endpoint z,
    0<=E(z)<=b,
    mu(z)<=exp[-b J(E(z)/b)],
    J(v)=I(sqrt(v)), 0<=v<=1.                         (1)

Here is a direct finite-law proof, so no multivariate large-deviation duality or asymptotic approximation is assumed.
Condition the full digit word on X eta=z and call this law q, with marginal laws q_j and means x_j.
Since the original law pi^b has strictly positive mass at every ternary word,
    D(q||pi^b)=log(1/mu(z)).
Expansion of the finite logarithms gives
    D(q||pi^b)=D(q||product_j q_j)+sum_j D(q_j||pi)
                 >=sum_j D(q_j||pi).                 (2)
The product marginal vanishes only where q does, so this identity also holds when some q_j have zeros.
Nonnegativity follows from log u<=u-1, or the retained finite log-sum inequality.

For any one-digit q_j with mean x, comparison with the tilted law proportional to pi(e)exp(te) gives
    D(q_j||pi)>=t x-log E_pi exp(t eta)
                 =t x-2log cosh(t/2).
For |x|<1 its maximum is at t=2 artanh(x), giving exactly I(x); for x=+/-1 the marginal is the corresponding point mass and its divergence is log4=I(x).
Thus every term in(2) is at least I(x_j).
The conditioned mean satisfies Xx=z, so sum x_j^2>=E(z).

For0<v<1,
    J'(v)=artanh(sqrt(v))/sqrt(v)>=1,
and this derivative is strictly increasing.
Indeed for0<x<1,
    x/(1-x^2)-artanh(x)>0,
since this expression vanishes at0 and has derivative2x^2/(1-x^2)^2>0.
Hence J is increasing and strictly convex on[0,1], with the continuous endpoint values already stated.
Jensen's finite inequality and the minimum-norm property give
    sum_j I(x_j)=sum_j J(x_j^2)
        >=b J(sum_j x_j^2/b)>=b J(E(z)/b).
This proves(1), including boundary means and singular Q.
An actual ternary word is itself a preimage with squared norm at most b, proving E<=b independently.
No conditional independence has been used.

In particular J(v)>=v, strictly for v>0.
This recovers the weaker absolute Gaussian profile mu(z)<=exp(-E(z)), which also follows directly from the original cosh-squared moment generating function.
Formula(1) retains its exact nonquadratic bounded-digit improvement.

<a id="nonlinear-original-profile-envelope"></a>
### 3. Combining absolute entropy with the actual zero atom

Now X has INTEGER columns.
The existing full covariance optimization of L251 gives
    mu(z)<=p exp[-E(z)/2]                              (3)
at every actual endpoint, including singular Q.
To recall the optimization precisely, for any real row l the original Fourier estimate is
    exp(l z) mu(z)<=p exp(l Q l^T/2).
Take l=z^T Q^+ on the range to obtain(3).
This argument uses the full actual zero atom of this same map.

Write
    a=log2, c=a-1/2>0, kappa=2-2a>0,
    r=log(1/p)/b, 0<=r<=a.
The last bound follows from the original all-zero word, whose probability is2^(-b).
For every r in[0,a] define v_r as the UNIQUE solution in[0,1) of
    J(v_r)-v_r/2=r,
    Psi(r)=r-c v_r.                                   (4)
Existence and uniqueness require no numerical solver: the left side is continuous, starts at0, has derivative at least1/2, and at1 equals2a-1/2>a.
Thus v_0=0 and v_r>0 for r>0.

Equations(1),(3) yield the complete profile
    mu(z)<=exp[-b Psi(r)] exp[-a E(z)]                 (5)
for EVERY endpoint.
To prove it, put v=E(z)/b in[0,1].
The negative logarithm of mu(z), divided by b, is at least
    max{r+v/2,J(v)}.
For v<=v_r, subtracting a v from the first branch gives r-c v, which decreases to Psi(r).
For v>=v_r the second branch gives J(v)-a v, whose derivative is at least1-a>0, so its minimum on that interval is also Psi(r).
At their intersection both agree.
Consequently
    min_(0<=v<=1)[max{r+v/2,J(v)}-a v]=Psi(r).         (6)
This proves(5) exactly; the multiplier is exp[-b Psi(r)], not the unproved p.

The following explicit facts locate the loss:
    kappa r<Psi(r)<r for0<r<=a,
    Psi(0)=0, lim_(r->0+)Psi(r)/r=kappa.               (7)
Indeed J(v)>v for v>0 implies r>v_r/2, hence v_r<2r; substituting into(4) proves the strict lower bound.
The upper bound uses c v_r>0.
Finally J'(0)=1, so r/v_r tends to1/2 and the limit follows.
Psi is continuous and strictly increasing, since implicit differentiation gives
    Psi'(r)=1-c/(J'(v_r)-1/2)>=1-2c=kappa>0.
The derivative at zero is understood by its limit.
In particular(5) implies the simpler all-map bound
    mu(z)<=p^kappa exp[-a E(z)].                       (8)

This is also an exact limitation of the TWO displayed estimates: formula(6) is an attained minimum at v_r.
No larger universal exponent than Psi(r) follows by merely taking the better of(1),(3) and paying a E.
This does not assert that actual integer maps attain the envelope or that(C1) is false.
Actual endpoints may have additional arithmetic restrictions, and exploiting them would be a genuinely stronger step.

<a id="unconditional-complete-finite-tail"></a>
### 4. Full actual finite-tail theorem, including neutral roots

Take an ACTUAL nonzero algebraic integer alpha, its monic minimal polynomial P of degree d, and total logarithmic Mahler measure m.
Torsion, nonunits, neutral roots and complex embeddings are all allowed.
Use precisely the ORIGINAL integer power-basis columns of L282:
    z_j=-M^(d+j)v,
    A_i=[z_0,...,z_(i-1)],
    W_i=(I+A_i A_i^T)^(-1),
    X=[z_i,...,z_(i+b-1)],
    Q_b=XX^T, D_b=(W_i^(-1)+Q_b)^(-1),
with i>=0 and b>=d.
Here M is multiplication by alpha in its full power basis, and v represents1.
Because alpha is nonzero, M is invertible over R and each d consecutive power columns is independent.
Therefore Q_b>0.
Also X eta is an invertible fixed field-linear image of the length-b algebraic endpoint, so its zero probability is the SAME p_b for every i, including nonunits.

For every u in the ENTIRE R^d, retain the exact finite object
    G_(i,b)(u)=exp[a u^T D_b u]
                   E exp[-a(X eta+u)^T W_i(X eta+u)].
Set r_b=log(1/p_b)/b and Delta_i=det(I+A_i A_i^T), Delta_0=1.
Then
    p_b<=G_(i,b)(0)<=sup_u G_(i,b)(u)
       <=K_d sqrt(Delta_i) exp[-b Psi(r_b)]
       <=K_d sqrt(Delta_i) p_b^kappa,                  (9)
where
    K_d=2^(d/4)(2pi/log2)^(d/2).
No coefficient-height, hyperbolicity, finite-window or unproved sharp-profile hypothesis is imposed.

For completeness the cancellation is as follows.
Put H0=W_i+Q_b^(-1) and z0=-H0^(-1)W_i u.
Direct expansion, with matrix order retained, gives
    (z+u)^T W_i(z+u)+z^T Q_b^(-1)z
      =(z-z0)^T H0(z-z0)+u^T D_b u.                 (10)
For the constant identity use
    W_i-W_i H0^(-1)W_i=(W_i^(-1)+Q_b)^(-1).
Multiply(5) by the actual Gaussian weight and its POSITIVE completion factor.
Equation(10) cancels that factor exactly, leaving
    G_(i,b)(u)<=exp[-b Psi(r_b)]
                   sum_(z in Z^d)exp[-a(z-z0)^T H0(z-z0)]
       <=exp[-b Psi(r_b)]
                   sum_(z in Z^d)exp[-a(z-z0)^T W_i(z-z0)].
Only nonnegative sums were enlarged; every original atom and its normalization were preserved.
The last translated Gaussian sum is at most K_d/sqrt(det W_i).
To recall the full lattice cost, tile R^d by unit cubes centered at z-z0.
If x is in such a cube, W_i<=I and the squared norm inequality give
    (z-z0)^T W_i(z-z0)>=x^T W_i x/2-d/4.
Integrating over each cube, summing and evaluating the ordinary Gaussian integral proves exactly the displayed K_d factor.
Since det W_i=Delta_i^(-1), the upper bounds in(9) follow.
The zero atom at u=0 proves the lower bound.
This covers the unbounded real tail space and hence any actual bounded-digit tail collection that contains zero.
No passage of a supremum through matrix limits, support restriction or existence of a maximizing point is needed.

All degree and prefix expenses remain explicit.
The retained L282 full-root determinant bound gives, for i>=1,
    log(K_d sqrt(Delta_i))
      <=log K_d +m i+(d/2)log(i+d)
               -(1/2)log|disc P|+m(d-1).             (11)
For i=0 the exact cost is log K_d.
For d=1 use |disc P|=1.
This is the actual existing determinant estimate at its original scope, not a newly audited proof or a uniform root-separation claim.

<a id="complete-tail-rate-bracket-and-boundary"></a>
### 5. Unconditional rate bracket and the remaining sharp question

For a FIXED actual P and any integer prefix sequence i_b>=0 with i_b=o(b), put
    g_b=-(1/b)log sup_(u in R^d) G_(i_b,b)(u),
    h=h2(P)=lim_(b->infinity) -(1/b)log p_b.
The finite-dimensional original collision limit is the existing one; neither h=m nor its evaluation is assumed.
The explicit expense in(11), divided by b, tends to zero, including bounded or zero prefixes.
Equations(9) and continuity of Psi yield
    Psi(h)<=liminf g_b<=limsup g_b<=h,
    Psi(h)>=kappa h.                                  (12)
The range h in[0,a] follows from p_b>=2^(-b).
At h>0 the first lower bound is strictly larger than kappa h by(7).
When h=0 the bracket forces g_b to tend to0.
For h>0 the argument does NOT prove that g_b has a limit or that its limit equals h.

This removes a prior hypothesis for a quantified comparison over all finite tail directions on arbitrary actual neutral inputs and arbitrary long original windows.
It does not settle(C1), the lossless neutral-tail rate, or the unrestricted Mahler gap.
In particular Psi(h)/h tends to kappa<1 as h tends to0; the present bound cannot create an input-uniform positive gap from h tending to0.
The nonlinear bounded-digit improvement is real at fixed positive r, but does not remove that asymptotic loss.
At hyperbolic fixed inputs and fixed prefixes L286's already proved rate h is stronger and remains the preferred result.

The discriminating next step is now precise: either obtain additional arithmetic endpoint information near energy E approximately b v_(r_b), where the two retained bounds meet, or control the full maximizing sum more efficiently than paying a E endpoint by endpoint.
Merely interpolating the same two envelopes more cleverly cannot improve Psi, by(6).
An actual map counterexample or stronger estimate in that crossover regime would change the question; enlarging the earlier short-window box alone would not establish the missing long-window theorem.
No candidate route is paused or closed by this local limitation.

Author self-check covered the finite relative-entropy decomposition with zero marginals, exact Legendre maximum and endpoint means, Jensen direction, minimum real preimage and singular support, the full L251 covariance optimization, r<=log2, unique crossover and all derivative signs, the strict and limiting bounds, matrix inverse order and positive completion, translated-cube normalization, nonunit/torsion/d=1/i=0 cases, growing-prefix and liminf/limsup quantifiers, and the restriction of envelope optimality to the two retained estimates.
No computation or numerical evidence is being called a proof.
The whole author body is now ready for separately organized noncontributor review; fixed adoption remains separate.




## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:18 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C419 exact relative Gaussian profile](Yin_C_G0419_v1.md#statement) | The original integer-column moment bound and full actual zero atom, coefficient1/2 only. |
| dependency | [C432 singular covariance optimization](Yin_C_G0432_v1.md#statement) | Inverse-on-range Gaussian optimization at the exact original law; no unit-only operator conclusion imported into nonunit finite matrices. |
| dependency | [C517 complete finite matrices](Yin_C_G0517_v1.md#statement) | Exact actual columns, all real-tail span, positive Schur completion and full-root determinant/discriminant expense. |
| dependency | [C529 completion interface](Yin_C_G0529_v1.md#statement) | Exact ordered quadratic completion and translated lattice sum, now using the independently derived nonlinear multiplier. |
| support | [Original complete proof/input](../ledger/Yin_L_G0298_v1.md#complete-retained-proof-and-review) | All original Sections1--5/equations1--12, full entropy, envelope, lattice proof, source/exploration/native and R197 boundaries. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:20 |
| status | proved |
| reason | Adopt the complete retained theorem after actual entire published Statement and Argument SELF, at its exact original domains, all finite costs and source/native/negative limits; no isolated review or research resumption is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C419 exact relative Gaussian profile](Yin_C_G0419_v1.md#statement) | The original integer-column moment bound and full actual zero atom, coefficient1/2 only. |
| dependency | [C432 singular covariance optimization](Yin_C_G0432_v1.md#statement) | Inverse-on-range Gaussian optimization at the exact original law; no unit-only operator conclusion imported into nonunit finite matrices. |
| dependency | [C517 complete finite matrices](Yin_C_G0517_v1.md#statement) | Exact actual columns, all real-tail span, positive Schur completion and full-root determinant/discriminant expense. |
| dependency | [C529 completion interface](Yin_C_G0529_v1.md#statement) | Exact ordered quadratic completion and translated lattice sum, now using the independently derived nonlinear multiplier. |
| support | [Original complete proof/input](../ledger/Yin_L_G0298_v1.md#complete-retained-proof-and-review) | All original Sections1--5/equations1--12, full entropy, envelope, lattice proof, source/exploration/native and R197 boundaries. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0748_v1.md#nonlinear-profile-whole-self) | Complete Statement and entire Argument, every selected interface and original finite-evidence/source/negative qualification. |


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
| dependency | [C419 exact relative Gaussian profile](Yin_C_G0419_v1.md#statement) | The original integer-column moment bound and full actual zero atom, coefficient1/2 only. |
| dependency | [C432 singular covariance optimization](Yin_C_G0432_v1.md#statement) | Inverse-on-range Gaussian optimization at the exact original law; no unit-only operator conclusion imported into nonunit finite matrices. |
| dependency | [C517 complete finite matrices](Yin_C_G0517_v1.md#statement) | Exact actual columns, all real-tail span, positive Schur completion and full-root determinant/discriminant expense. |
| dependency | [C529 completion interface](Yin_C_G0529_v1.md#statement) | Exact ordered quadratic completion and translated lattice sum, now using the independently derived nonlinear multiplier. |
| support | [Original complete proof/input](../ledger/Yin_L_G0298_v1.md#complete-retained-proof-and-review) | All original Sections1--5/equations1--12, full entropy, envelope, lattice proof, source/exploration/native and R197 boundaries. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-nonlinear-entropy-tail) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

