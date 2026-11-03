---
author: Yin
---
# Uniform logarithmic regularization for bounded-term integer auxiliaries

Date: 2026-10-15.
Human author Yin.
Root develops this argument under the continuing unrestricted G0001 authorization.
The source-only f_unitary_scope reader checked BS13 Theorem2.1 but supplied no project proof step.
The finite-logarithmic construction of the separate strategy_critique author is now fixed in C137v1 and is awaiting whole review; its mechanism is credited below and completely rederived here so that no unadopted theorem is silently selected.
This draft is not independently reviewed.
Root is a contributor and cannot supply independent review of the new argument.

## Responsible question and reuse boundary

The concrete question is whether a bounded number of nonzero terms makes the positive logarithmic regularization error uniformly small despite unbounded exponents and moving circle zeros.
This would turn a verified auxiliary Mahler-cost surplus into an original-field resultant certificate without rebuilding a two-phase argument for each family.
It does not construct the auxiliary or verify arithmetic divisibility automatically.

The bounded local screen examined the G claims/ledger and source records for Turan, Nazarov, Remez, small-value sets and sparse logarithmic regularization.
Existing C110 has degree-dependent regularization, C122 pays its particular phase geometry, and L229 supplies the original-degree finite angular estimate.
No matching retained uniform bounded-term input was located in those inspected passages; this is not a claim of novelty or an exhaustive search.
The established measurable-set inequality was subsequently checked in the primary BS13 Theorem2.1 and accepted at [BS13-U001](../audits/literature/BS13/Yin_U001.md#bs13-u001).
Its absolute constant, precise term count and pure-imaginary specialization are the only new external theorem input.
The classical original proof is not newly audited.

[C137v1](Yin_C_G0137_v1.md#argument) already supplies a finite positive-logarithm majorant with explicit matrix, coefficient, radial and frequency costs.
The present calculation retains that mechanism and its contribution attribution; the new extension is the uniform small-value/regularization estimate with all constants independent of exponent span, followed by the precise conditional class theorem.
Neither the known Turan--Nazarov inequality nor the elementary layer-cake argument is claimed as an original theorem.
C135's binomial-product family is a comparison, not a new premise or a coverage claim.

## Statement

Fix integers K>=2 and S>=1, a real C>0 and a real margin0<eta<=1.
There is a positive constant g(K,S,C,eta), depending also on the one fixed absolute Turan--Nazarov constant, with the following property.

Let P be ANY monic irreducible nontorsion polynomial in Z[t], with constant coefficient+/-1, original degree d and total logarithmic Mahler measure m(P)>0.
Suppose there exists an actual nonzero F in Z[t], of degree1<=T<=Cd, with at most K nonzero terms, coefficient l1 norm at most S, and an integer q>=2, such that

    F(alpha)/q is a NONZERO algebraic integer,
    m(F)<=log q-eta,                                  (1)

where alpha is an original root of P and m(F) is the ordinary logarithmic Mahler measure of F, including its content and all factors.
Then m(P)>g(K,S,C,eta).
There is no reciprocity, squarefree-reduction, fixed-q, frequency-spacing, circle-zero-separation or powered-degree preservation assumption.
Every original embedding is counted, and zero auxiliary values are excluded explicitly by(1).

The intermediate result is a uniform estimate for every such nonzero integer F, even without P or(1).
Put beta=1/(K-1), enlarge the absolute source constant A to at least1, and D_beta=1/beta+1/(2-beta).
For every delta>0,

    0<= integral_T (1/2)log(|F|^2+delta^2)-m(F)
                          <= A D_beta delta^beta.     (2)

The measure on the circle is normalized Haar measure.
The error bound is independent of degree, exponents, coefficient placement and circle-zero multiplicity.
Integer coefficients supply the required uniform scale.
This does not assert(2) for arbitrary small nonzero scalar multiples of F.

All constants, a finite majorant and a finite positive cutoff are specified below.
The source constant A has no numerical value in the inspected theorem, so no fully numerical universal value of g is claimed.
The supplied F, its divisibility, nonvanishing, sparsity, coefficient bound, linear degree and positive cost margin remain genuine hypotheses.
The unrestricted G0001 contract is not established.

<a id="argument"></a>
## 1. Uniform sublevel measure with the actual term count

Write F(t)=sum_(j=1)^N c_j t^(a_j), with distinct nonnegative integer exponents and nonzero integer c_j, after collecting equal exponents.
Then1<=N<=K and Parseval gives

    sup_(|z|=1)|F(z)| >= (sum_j c_j^2)^(1/2)>=1.      (3)

For N>=2 and0<t<=1 let E_t={x in[0,2pi]: |F(exp(ix))|<=t}.
This is measurable.
If its measure is positive, apply the exact BS13 theorem with a_j there equal to i times the present integer exponent a_j.
All real parts vanish, and ordinary supremum over E_t is at most t.
With mu normalized circle measure, (3) therefore implies

    1<= (A/mu(E_t))^(N-1)t,
    mu(E_t)<= A t^(1/(N-1))<=A t^beta.              (4)

If mu(E_t)=0 this bound holds without invoking the positive-measure theorem.
For t>1 use mu(E_t)<=1<=A t^beta.
If N=1, |F|=|c_1|>=1 on the circle; its sublevel measure is0 at t<1 and at most1 for t>=1.
Thus the single bound

    mu{|F|<=t}<=A t^beta, t>0,                      (5)

covers every N including the monomial case.
The larger exponent1/(N-1) is weakened only at0<t<=1; it is not incorrectly used for t>1.
The supremum scale in(3) is why the source's absolute constant stays uniform over these integer auxiliaries.
The number of terms, not the maximum exponent, enters beta.

## 2. A paid logarithmic regularization error

A nonzero one-variable polynomial has only finitely many circle zeros, of measure0.
Its usual logarithmic Mahler measure equals the circle integral; this is the accepted scalar Jensen/root normalization in [F109](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization), with content retained.
Integrability also follows directly here: (5) gives integral log^-|F|<=A/beta, while |F|<=S controls the positive part.

For x>0 the elementary identity

    (1/2)log(1+delta^2/x^2)
       =integral_(x to infinity) delta^2/[t(t^2+delta^2)] dt

follows by differentiation and the zero limit at infinity.
Apply Tonelli to the nonnegative integrand, ignoring only the zero-measure circle-zero set.
Formula(5) gives

    integral_T (1/2)log(1+delta^2/|F|^2)
       <= A integral_0^infinity delta^2 t^(beta-1)/(t^2+delta^2) dt
       = A delta^beta integral_0^infinity u^(beta-1)/(1+u^2) du
       <= A delta^beta [1/beta+1/(2-beta)].           (6)

In the last step integrate u^(beta-1) on(0,1) and u^(beta-3) on(1,infinity).
Both converge because0<beta<=1.
No exact beta-function identity, interchange of a signed singular Fourier series, or degree-dependent minimum modulus is needed.
Subtract the integrable log|F| to obtain(2).
The inequality is uniform for arbitrary exponents and does not need the coefficient-height bound S beyond positive-part integrability for the individual polynomial; S will pay the finite majorant and radial cost below.

## 3. Choose one finite majorant before varying F or P

Set D_beta as above, choose the integer

    L=ceil(max{1,(8A D_beta/eta)^(1/beta)}),
    delta=1/L, B=S^2+1,
    J=ceil(4B/(eta delta^2)).                        (7)

These quantities depend only on K,S,eta and the fixed A; delta is rational and B,J are positive integers.
In particular delta<=1, B>=||F||_1^2+delta^2 and A D_beta delta^beta<=eta/8.
Define on the circle the finite real Laurent polynomials

    H=|F|^2+delta^2, Y=1-H/B,
    Phi_J=(1/2)log B-(1/2)sum_(j=1)^J Y^j/j,
    c_J=constant coefficient of Phi_J.              (8)

Here0<=Y<=R:=1-delta^2/B<1.
The scalar log series has nonnegative omitted terms after changing its sign, so

    (1/2)log H<=Phi_J,
    0<=Phi_J-(1/2)log H
             <=R^(J+1)/[2(J+1)(1-R)]
             <=B/[2(J+1)delta^2]<=eta/8.            (9)

Equations(2),(7),(9) give the uniform finite coefficient estimate

    c_J<=m(F)+eta/4.                                (10)

This is an actual finite coefficient, not a value involving the unknown original polynomial P or its roots.
Apart from log B/2 its coefficients are rational.
No numerical evaluation or enumeration is asserted.
The source's unspecified absolute A makes the universal selection qualitative, but once an admissible A and margin are fixed, all displayed finite operations are well-defined.

The exact finite-matrix representation from C137's mechanism can be retained: if Y(z)=sum_(|k|<=T)y_k z^k, form the Hermitian matrix K_F=(y_(i-j)) on indices -JT,...,JT.
Then0<=K_F<=R I, by integrating Y times the squared modulus of a finite polynomial.
Every length-j, bandwidth-T path from0 to0 stays within this index interval for j<=J.
Hence

    c_J=(1/2)log B-(1/2)sum_(j=1)^J (K_F^j)_(0,0)/j. (11)

Its size is exactly2JT+1, not fixed or bounded independently of T.
This matrix and its path argument are credited to the C137 author; the current proof does not infer an upper pointwise bound from a lower Gram capacity.
The scalar finite polynomial(8) suffices without an executed matrix.

The Laurent coefficient l1 norm of Y is at most1+(||F||_1^2+delta^2)/B<=2.
Thus the sum of the absolute nonconstant coefficients of Phi_J is at most(1/2)sum_(j=1)^J 2^j/j<2^J; every frequency has absolute value at most JT.
These two prices are retained in the actual original-angle bound.

## 4. All original radial and angular costs

For the original P let r_i=|alpha_i|, z_i=alpha_i/r_i, m=m(P)>0 and h=Tm/d.
Since P is a unit, sum_i log^+r_i=m and sum_i|log r_i|=2m.
Normalize

    V_i=F(alpha_i)/max(1,r_i)^T.

Direct coefficient comparison gives |V_i-F(z_i)|<=S min{1,T|log r_i|}.
For expanding roots use r_i^(a_j-T), and for contracting roots use r_i^a_j; these numbers lie in[0,1], at distance at most min{1,T|log r_i|} from1.
No roots are removed.

The function x to(1/2)log(x^2+delta^2) on x>=0 has derivative at most1/(2delta).
Since all F(alpha_i) are nonzero by(1),

    log|Res(P,F)|/d
       =h+(1/d)sum_i log|V_i|
       <=(1+S/delta)h+(1/d)sum_i Phi_J(z_i).         (12)

The actual L229 input is [the finite original angular interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence).
With c=log2/4 and h0=c exp(-20), put

    b(u)=max{u,sqrt(u/c)log sqrt(c/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h0.

It is increasing and tends to0 with u.
For0<Jh<=h0, EVERY original angular average at nonzero frequency of absolute value at most JT has modulus at most epsilon(Jh).
Original power multiplicities and any loss of powered-field degree are already paid by that exact input; no degree preservation is assumed.
Combining with the finite coefficient price yields

    log|Res(P,F)|/d
       <=c_J+(1+S/delta)h+2^J epsilon(Jh).           (13)

This is the complete C137-type finite logarithmic estimate, reproduced with its author's contribution acknowledged.
The new uniform estimate(10) now makes its constant coefficient affordable whenever(1) holds.

## 5. Original integral income and a positive uniform cutoff

Let beta_alpha=F(alpha)/q be the nonzero algebraic integer in(1).
Its norm in the ORIGINAL degree-d field is a nonzero rational integer, regardless of index primes or reduction multiplicity.
Thus

    |Res(P,F)|=q^d |Norm(beta_alpha)|>=q^d.          (14)

There is no powered-subfield or selected-root substitution.
All original embeddings have the required integrality and nonvanishing because they are conjugates of the same beta_alpha.

Choose the least integer ell>=32 such that, for

    h_star=(c/J)2^(-ell),

one has (1+S/delta)h_star<=eta/4 and 2^J epsilon(Jh_star)<=eta/4.
Such an integer exists by epsilon(u)->0.
The domain is valid because ell>=32 implies ell log2>20, hence Jh_star<h0.
This is an exact finite positive constant selection using the displayed functions; no search or giant calculation is asserted to have run.
For0<h<=h_star, monotonicity and(1),(10),(13),(14) give

    log q<=log q-3eta/4+eta/4+eta/4
                            =log q-eta/4,

a contradiction.
Therefore h>h_star.
Since T<=Cd,

    m(P)>g(K,S,C,eta):=h_star/C>0.                 (15)

Every parameter of this positive constant was fixed before choosing F,P or q.
If only a margin eta0>1 is known, use eta=1.
A constant or monomial of degree0 can also be omitted without losing possible inputs: for a nonzero constant F=a, the full norm inequality q^d<=|a|^d contradicts m(F)=log|a|<=log q-eta.
Monomials of positive degree are already covered; alternatively their unit norm gives the same immediate contradiction.
No zero-value exception is silently repaired; the theorem explicitly requires nonzero F(alpha).

## 6. Consequences and remaining mathematical obligations

The theorem converts a uniform bounded-term, bounded-coefficient, linear-degree, positive auxiliary-Mahler margin into an original Mahler gap.
It requires no special phase decomposition, circle-zero separation, good reduction or finite-field order statistic.
The analytic error is now paid uniformly over all integer supports with those bounds.

For example, an actual product of a fixed number k of binomials t^(a_i)-1 has at most2^k terms after collection, l1 norm at most2^k and logarithmic Mahler measure0.
If its degree is at most C d and its value divided by2 is nonzero integral, the theorem applies with any fixed eta<=log2.
This overlaps the known C135 general binomial-product mechanism; C135's explicit bound is much stronger and no new gap is claimed for that already covered class.
The point of the current general criterion is that a product factorization and its direct dyadic-depth amplification are not hypotheses.

The actual auxiliary need not have coefficient energy below q^2.
C137's concrete six-term auxiliary illustrates why the logarithmic cost can be smaller than the second-moment cost, but its separate finite two-phase proof and zero-branch theorem are not replaced or enlarged by an unproved uniform estimate of m(A_N).
The present theorem only uses an independently supplied bound m(F)<=log q-eta.
It neither asserts that this bound holds for every sparse polynomial nor derives an auxiliary from small m(P).

The remaining unrestricted problem is substantive: find, for every possible near-one original input, an actual nonzero integral auxiliary quotient with uniform K,S,C,eta, or another mechanism that covers inputs without one.
If K, S or1/eta must diverge, the present cutoff can tend to0 and supplies no uniform gap.
An all-input auxiliary existence theorem without these quantitative controls would not complete the argument.
No growth bound, class separation, near-one realization or G0001 completion is inferred here.

## 7. Source and contribution scope

Direct mathematical inputs are BS13-U001's accepted pure-imaginary measurable-set inequality, L229's exact original finite angular estimate and F109's accepted scalar Jensen normalization.
The finite majorant, coefficient price, matrix path and radial transfer originate in the separate C137 author construction; they are reproduced completely and attributed.
No selected theorem in unadopted C137 is required to fill a missing proof step.
If adopted later, it can serve as that reusable interface at its exact physical version; this draft does not anticipate its review verdict.

The root author supplied equations(2)--(7), the uniformization of the finite coefficient bound and the final parameterized class theorem, together with their full domains and limitations.
The f reader supplied source identification and precise statement inspection only.
No mathematical program, numerical integral, matrix expansion or J has been run.
The source proof was not audited, and this author account is not independent project review.

<a id="bounded-term-entire-author-freeze"></a>
## Entire author self-check and freeze

2026-10-15T10:28.
Root freezes the complete present account, including the responsible question/reuse screen, exact uniform statement, Sections1--7 and all15 equations, source and contribution limits.
The author self-check reconstructed the normalized measurable-set conversion, N=1 and zero-measure cases, integer scale and the exponent direction at t<=1, nonnegative layer-cake identity and both integrable tails, rational regularization choice, logarithm-series upper direction and finite tail, coefficient and matrix prices, all original radial roots, exact L229 domain and finite cutoff, original nonzero integral norm and variable-q scope.
Every parameter is independent of F's exponents and P once the declared bounds are fixed.
No author check is independent evidence.
Source constant A is existential; no numerical universal constant or executed calculation is asserted.
Automatic auxiliary existence and the unrestricted goal remain unresolved.

## Fixed organization

Retain the whole frozen root-author account, all15 equations, finite matrix and coefficient/radial costs, source and contribution boundaries and explicit unresolved auxiliary coverage.
Root cannot be the independent reviewer.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:29 |
| status | open |
| reason | Retain the complete bounded-term logarithmic transfer at its exact conditional arithmetic scope; actual whole independent review pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire uniform statement](#statement) | Uniform regularization and original-field class theorem, all parameters and nonzero/divisibility premises. |
| argument | [Entire argument](#argument) | Sections1--7, all15 equations, finite constants and boundaries, source/contribution scope and author check. |
| dependency | [Absolute measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted established statement/applicability; original proof not audited. |
| dependency | [Finite original angular estimate](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain, monotonicity and original powered-field costs. |
| dependency | [Scalar Jensen formula](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Full logarithmic Mahler integral including content. |
| support | [Finite logarithmic mechanism attribution](Yin_C_G0137_v1.md#argument) | Majorant, finite compression and radial mechanism credited; entire needed proof rederived without assuming pending acceptance. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T10:37 |
| status | proved |
| reason | Adopt the actual whole noncontributor review: bounded-term integer auxiliaries have uniform logarithmic regularization independent of exponent span, yielding the stated conditional original-field positive gap. Auxiliary existence and uniform arithmetic coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire uniform statement](#statement) | Uniform regularization and original-field class theorem, all parameters and nonzero/divisibility premises. |
| argument | [Entire argument](#argument) | Sections1--7, all15 equations, finite constants and boundaries, source/contribution scope and author check. |
| dependency | [Absolute measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted established statement/applicability; original proof not audited. |
| dependency | [Finite original angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain, monotonicity and original powered-field costs. |
| dependency | [Scalar Jensen formula](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Full logarithmic Mahler integral including content. |
| support | [Finite logarithmic mechanism attribution](Yin_C_G0137_v1.md#argument) | Majorant, finite compression and radial mechanism credited; entire needed proof rederived without assuming pending acceptance. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0801_v1.md#uniform-bounded-term-whole-independent-finding) | Complete actual fixed statement and argument, all direct inputs, costs, exceptions, source and contribution limits. |


### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:52 |
| status | proved |
| reason | Select the newly performed isolated whole review of this exact fixed statement, complete argument and all selected input interfaces at their stated restricted scopes. Preserve the proved mathematical status, unchanged statement and argument, every nonreview relation and scope, and all historical decisions. The retained older unknown finding keeps its actual date, checks and limits; this new finding supplies new evidence at its actual date without certifying old isolation, backdating adoption, or completing or resuming G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire uniform statement](#statement) | Uniform regularization and original-field class theorem, all parameters and nonzero/divisibility premises. |
| argument | [Entire argument](#argument) | Sections1--7, all15 equations, finite constants and boundaries, source/contribution scope and author check. |
| dependency | [Absolute measurable-set inequality](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted established statement/applicability; original proof not audited. |
| dependency | [Finite original angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact epsilon, domain, monotonicity and original powered-field costs. |
| dependency | [Scalar Jensen formula](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Full logarithmic Mahler integral including content. |
| support | [Finite logarithmic mechanism attribution](Yin_C_G0137_v1.md#argument) | Majorant, finite compression and radial mechanism credited; entire needed proof rederived without assuming pending acceptance. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0801_v1.md#g0139-m04-isolated-whole-finding) | Complete exact fixed statement, whole argument, every selected input, all parameter/domain/original-degree costs, exceptional branches and source/noncompletion limits. |
