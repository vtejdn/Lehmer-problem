---
author: Yin
---

# Actual endpoint Hardy/Blaschke limit and surviving posterior correction

This retains the complete original2026-10-07 [L101 proof](../ledger/Yin_L_G0101_v1.md), including its full unit-circle cyclicity and actual Salem specialization.
The assigned review_matrix_completion agent authored the reconstruction.
The coordinator and assess_shortness_route supplied the Wiener mechanism; the latter also supplied the Salem specialization.
Those actual contributions and old checking scopes remain in the formal review linked by L101.
No source, computation or Task is newly executed.

## Statement

Let P be the monic irreducible polynomial of a nonzero algebraic integer alpha, of degree d,with m=log M(P)>0.
For N=d+k let a^(N) be the last row of the actual power-matrix row projection, reversed and zero-extended.
Let P*(z)=z^d P(1/z).
For each expanding alpha_i put beta_i=1/alpha_i and

    B(z)=product_(abs(alpha_i)>1) (abs(beta_i)/beta_i)(beta_i-z)/(1-conj(beta_i)z),
    s=B(0)=exp(-m), l=1-s².

The closure in coefficient H2 of P* times polynomials is exactly B H2, including the factors arising from unit-circle roots.
Then a^(N) converges strongly in l2 to the real coefficient sequence of A(z)=1-sB(z).
In particular a0=l,sum a_j²=l and its fourth/sixth sums converge to s4=sum a_j^4,s6=sum a_j^6.
No uniform rate in P or convergence of the endpoint posteriors is asserted.

Set D=6l³-18l s4+16s6-4s4²/l.
The actual Blaschke coefficients satisfy abs(b_k)<=l for k>=1,so l³-s4>=l^4(1-l)>0.
Consequently D>0 and the finite cubic posterior tests pass to the actual Shannon rate h1 with
gamma=4(s4-l³)²/D,0<gamma<=1-l and

    h1>=max(f(l+gamma),F(l)+gamma/2),
    gamma>=gamma0=(2/3)l^5(1-l)²,
    h1>=E(m):=max(f(l+gamma0),F(l)+gamma0/2)>D0(m).

Here f(t)=g(sqrt(t)),F(t)=t/2+t²(3-2t)^4/324 and D0(m)=max(f(l),F(l)) is the prior comparison, separately from the cubic denominator D.
The general gamma0 is O(m^5),so this strict fixed-input rate correction gives no common positive Mahler gap.

For a Salem number alpha=lambda>1, beta=lambda^(-1)=s and

    A(z)=l/(1-beta z), a_k=l beta^k,
    s4=l³/(2-l), s6=l^5/(3-3l+l²),
    gamma>=(2/3)l³((1-l)/(2-l))².

The last lower bound may replace gamma0 in the rate formula.
It gives the conditional small-m Salem comparison h1>=m-6m³+O(m^4).
No sequence of Salem numbers tending to1, optimal cubic constant, further restriction on allowable Blaschke products or uniform degree-linear onset is asserted.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:10 |
| status | open |
| reason | Entire original finite reversal, Hardy closure, strong endpoint limit, Wiener estimate and Salem proof retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire actual nonzero-algebraic-integer endpoint Hardy/Blaschke theorem including unit-circle factors, strong coefficient/moment convergence, strict surviving cubic correction and exact Salem specialization with all fixed-input/uniformity limits. |
| argument | [Complete argument](#argument) | Full original1–15: finite reversal/projection, direct outer cyclicity and product closure, closed isometric inner range, strong limit/moment continuity, finite-posterior rate passage, root-average Schwarz/Wiener and exact denominator, geometric Salem sums and cubic constant. |
| dependency | [Exact posterior and Gram identities](Yin_C_G0287_v1.md#argument) | Full finite power-matrix projection, endpoint leverage and nonlinear posterior information; no asymptotic posterior or determinant claim is imported. |
| dependency | [Fourth-moment comparison](Yin_C_G0290_v1.md#fourth-posterior-moment) | Exact F(l) lower bound and previous every-time D0(m) comparison with its retained cubic Taylor error. |
| dependency | [Finite cubic projection certificate](Yin_C_G0291_v1.md#cubic-orthogonal-posterior-certificate) | Exact rational finite denominator, gamma and zero-denominator inequality, plus R_N<=1-l_N; no vanishing arithmetic bound is mistaken for a rate correction. |
| dependency | [Finite relation-space basis](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact monic polynomial-division kernel span P,zP,..., used before reversal; no Toeplitz or source-proof limit is required. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:17 |
| status | proved |
| reason | Adopt the entire original actual endpoint/Hardy/Blaschke theorem, strong moment/rate passage, Wiener strictness and exact Salem specialization after actual whole self-review; the positive fixed-input correction still vanishes near zero and no uniform onset or limiting posterior is assumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire actual nonzero-algebraic-integer endpoint Hardy/Blaschke theorem including unit-circle factors, strong coefficient/moment convergence, strict surviving cubic correction and exact Salem specialization with all fixed-input/uniformity limits. |
| argument | [Argument](#argument) | Full original1–15: finite reversal/projection, direct outer cyclicity and product closure, closed isometric inner range, strong limit/moment continuity, finite-posterior rate passage, root-average Schwarz/Wiener and exact denominator, geometric Salem sums and cubic constant. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Full finite power-matrix projection, endpoint leverage and nonlinear posterior information; no asymptotic posterior or determinant claim is imported. |
| dependency | [Dependency](Yin_C_G0290_v1.md#fourth-posterior-moment) | Exact F(l) lower bound and previous every-time D0(m) comparison with its retained cubic Taylor error. |
| dependency | [Dependency](Yin_C_G0291_v1.md#cubic-orthogonal-posterior-certificate) | Exact rational finite denominator, gamma and zero-denominator inequality, plus R_N<=1-l_N; no vanishing arithmetic bound is mistaken for a rate correction. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact monic polynomial-division kernel span P,zP,..., used before reversal; no Toeplitz or source-proof limit is required. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-endpoint-limit-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire actual nonzero-algebraic-integer endpoint Hardy/Blaschke theorem including unit-circle factors, strong coefficient/moment convergence, strict surviving cubic correction and exact Salem specialization with all fixed-input/uniformity limits. |
| argument | [Argument](#argument) | Full original1–15: finite reversal/projection, direct outer cyclicity and product closure, closed isometric inner range, strong limit/moment continuity, finite-posterior rate passage, root-average Schwarz/Wiener and exact denominator, geometric Salem sums and cubic constant. |
| dependency | [Dependency](Yin_C_G0287_v1.md#argument) | Full finite power-matrix projection, endpoint leverage and nonlinear posterior information; no asymptotic posterior or determinant claim is imported. |
| dependency | [Dependency](Yin_C_G0290_v1.md#fourth-posterior-moment) | Exact F(l) lower bound and previous every-time D0(m) comparison with its retained cubic Taylor error. |
| dependency | [Dependency](Yin_C_G0291_v1.md#cubic-orthogonal-posterior-certificate) | Exact rational finite denominator, gamma and zero-denominator inequality, plus R_N<=1-l_N; no vanishing arithmetic bound is mistaken for a rate correction. |
| dependency | [Dependency](Yin_C_G0209_v1.md#gram-lower-certificate) | Exact monic polynomial-division kernel span P,zP,..., used before reversal; no Toeplitz or source-proof limit is required. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-endpoint-limit-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0548_v1.md#f-g297) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
Let P be the monic irreducible polynomial of a nonzero algebraic integer alpha, of degree d, with m=log M(P)>0.
The principal application is the nontorsion algebraic-unit core.
Write V_N for its d-by-N matrix of power remainders, Pi_N=V_N^T(V_NV_N^T)^(-1)V_N, and let a^(N) be the LAST row of Pi_N with its N entries reversed and then extended by zeros.
Thus a_0^(N)=l_N is the endpoint leverage.
The reversal is part of the definition, not a change to the observed binary fibers.

We reuse the exact finite posterior and Gram identities in [C287](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy), the fourth-moment function in [C290](Yin_C_G0290_v1.md#fourth-posterior-moment), and the finite cubic projection calculation in [C291](Yin_C_G0291_v1.md#cubic-orthogonal-posterior-certificate).
The limiting row is proved here, including its unit-circle boundary case.

<a id="endpoint-row-hardy-closure"></a>
### 1. Reversal and the exact closed relation space

Use H^2 as the Hilbert space of square-summable coefficients of analytic power series on the unit disk.
Polynomials are dense and their coefficient norm equals the circle L2 norm by Parseval.
Put

    P*(z)=z^d P(1/z),       P*(0)=1.

For N=d+k, the finite integral relation space is spanned by P,zP,...,z^(k-1)P.
Reversing N coefficients sends it to the span of P*,zP*,...,z^(k-1)P*.
Hence

    a^(N)=1-Proj_(E_k)1,
    E_k=span{P*,zP*,...,z^(k-1)P*}.                     (1)

This is the usual real Euclidean projection, viewed in the complex coefficient Hilbert space; all the vectors and projections in (1) are real.

For each root alpha_i of P with |alpha_i|>1 put beta_i=1/alpha_i and define

    b_beta(z)=(|beta|/beta)(beta-z)/(1-conj(beta)z),
    B(z)=product_(|alpha_i|>1)b_(beta_i)(z),
    s=B(0)=product_i |beta_i|=exp(-m),   l=1-s^2.         (2)

Every beta_i is nonzero and inside the disk.
The rational function B is analytic on a neighborhood of the closed disk, has modulus 1 on the unit circle, and has real Taylor coefficients: real roots contribute real factors and conjugate roots contribute conjugate pairs.
The normalization s>0 fixes the phase.

The factorization is

    P*=B O,
    O(z)=M(P) product_(|alpha_i|>1)(1-conj(beta_i)z)
                  product_(|alpha_i|<=1)(1-alpha_i z).  (3)

Thus O is a polynomial all of whose factors have the form 1-cz with |c|<=1, apart from its nonzero scalar constant.
This formula retains unit-circle roots; they are not discarded by an unproved invertibility assertion.

Here is a direct cyclicity proof for those factors.
If |c|<1, truncating the convergent geometric series approximates (1-cz)^(-1) in H^2, so 1 lies in the closure of (1-cz) times the polynomials.
If |c|=1, use instead

    q_n(z)=sum_(j=0)^n (1-j/(n+1)) c^j z^j,
    (1-cz)q_n(z)=1-(1/(n+1))sum_(j=1)^(n+1)c^j z^j.

The error norm is exactly (n+1)^(-1/2).
A product of cyclic polynomial factors is cyclic: approximants g q_n to 1 imply f g q_n tends to f because multiplication by a polynomial f is bounded on H^2; invariance under multiplication by z then puts all f times polynomials in the closed product range.
Induct over the factors.
Consequently the closure of O times the polynomials is H^2, including repeated unit-circle factors.

Multiplication by B is an isometry: first use |B|=1 and Parseval on polynomials, then extend by density.
Its range is closed.
Therefore

    closure(union_k E_k)=B H^2.                         (4)

No spectral-factorization or Toeplitz-limit theorem is needed for this step.

<a id="strong-endpoint-coefficient-limit"></a>
### 2. Strong coefficient convergence and the rate interface

Projections on the increasing E_k converge strongly to projection on their closed union.
One direct proof is that, for nested projections, the squared norm of their difference at a fixed vector equals the difference of their squared projected norms; these norms increase to a finite limit.
The limit vector belongs to the closed union and has the required orthogonality.

The vectors B,zB,z^2B,... are an orthonormal basis of B H^2.
Only B has a nonzero inner product with 1.
Equations (1)--(4) consequently give

    a^(N) -> a in l2,
    A(z):=sum_(j>=0)a_j z^j=1-sB(z),
    a_0=l=1-exp(-2m),       sum_j a_j^2=l.               (5)

In particular l_N tends to l, and, for q=4,6,

    sum_j (a_j^(N))^q -> s_q:=sum_j a_j^q.              (6)

Indeed l2 convergence implies lq convergence for q>=2, since ||x||_q<=||x||_2; continuity of the lq norm proves (6).
No rate of convergence uniform in P is asserted.

For each finite N>d, define the cubic-test data

    D_N=6l_N^3-18l_N s_(4,N)+16s_(6,N)-4s_(4,N)^2/l_N,
    gamma_N=4(s_(4,N)-l_N^3)^2/D_N

when D_N>0, and gamma_N=0 for a zero denominator.
The companion finite proof gives R_N=E(b_N-L_N)^2>=gamma_N, and R_N<=1-l_N.
Equivalently, even in the zero-denominator case,

    4(s_(4,N)-l_N^3)^2<=D_N(1-l_N).                    (7)

Here b_N is that window's endpoint posterior; we do not assert convergence of the posteriors or of their conditioning sigma-algebras.
The coefficient convergence alone yields

    D_N -> D=6l^3-18l s4+16s6-4s4^2/l.                 (8)

If s4 differs from l^3, (7) forces D>0, gamma_N tends to gamma=4(s4-l^3)^2/D, and 0<gamma<=1-l.
The finite information bounds then pass directly to the decreasing-increment limit h_1:

    h_1>=max{ f(l+gamma), F(l)+gamma/2 },                (9)

where f(t)=g(sqrt(t)) and F(t)=t/2+t^2(3-2t)^4/324 are exactly the functions in L G0094 and L G0097.
The first inequality uses the full posterior variance; the second uses the same variance correction in the quadratic term while retaining L G0097's separate fourth-moment estimate.

<a id="wiener-endpoint-strict-correction"></a>
### 3. An actual endpoint constraint makes the correction positive

Write B(z)=sum_(j>=0)b_j z^j, b_0=s.
For every k>=1,

    |b_k|<=1-s^2=l.                                    (10)

For completeness, average B(omega^j z) over all kth roots of unity omega^j.
The result is H(z^k), where H(w)=sum_(q>=0)b_(qk)w^q, and |H(w)|<=1 on the disk: choose any kth root z of w and use the average.
Now H(0)=s, H'(0)=b_k.
The disk map (H-s)/(1-sH) vanishes at zero; Schwarz's lemma gives |b_k|/(1-s^2)<=1.
Schwarz's lemma here follows from the maximum principle applied to the disk map divided by z, followed by radii tending to 1.
This proves (10) without an uninspected coefficient theorem.

Equation (5) gives a_0=l and a_k=-s b_k for k>=1, so

    |a_k|<=s l  (k>=1),   sum_(k>=1)a_k^2=l(1-l),
    s4<=l^4+s^2 l^2[l(1-l)]
       =l^3(1-l+l^2),
    l^3-s4>=l^4(1-l)>0.                                (11)

Thus the hypothesis for (9) holds for every actual input with m>0.
Also s6<=l s4, simply because each a_k^2<=sum_i a_i^2=l.
Substitution in (8) shows D<=6l^3.
Combining this with (11) gives the explicit surviving correction

    gamma>=gamma_0:=(2/3)l^5(1-l)^2>0,
    h_1>=max{ f(l+gamma_0), F(l)+gamma_0/2 }.             (12)

The argument already proves gamma_0<=1-l, so the f argument lies in its stated domain.
Alternatively this follows immediately from its displayed formula.
In particular (12) is strictly larger than max{f(l),F(l)} for each fixed m>0.
This differs from the finite denominator lower bound whose correction vanishes with the observation length: the projection limit retains a positive cubic-test correction at a fixed input.

Nevertheless gamma_0=O(m^5) as m tends to zero.
The displayed universal estimate does not remove the leading cubic comparison error in L G0097 and supplies no positive Mahler gap.
The real additional structure is the constrained endpoint row A=1-sB and its Wiener bound; generic integer linear observations need not satisfy that structure.

<a id="salem-endpoint-geometric-control"></a>
### 4. The actual Salem specialization

For a Salem number alpha=lambda>1, there is just one root of P outside the unit circle.
All its unit-circle roots belong to the cyclic factor O already treated in (3).
With beta=lambda^(-1)=s, the normalized functions are

    B(z)=(beta-z)/(1-beta z),
    A(z)=(1-beta^2)/(1-beta z),
    a_k=l beta^k,
    s4=l^3/(2-l),
    s6=l^5/(3-3l+l^2).                                 (13)

These are coefficients of the actual endpoint limit, independent of the number of neutral conjugates.
Geometric-series summation proves the two moment formulas.
In particular

    l^3-s4=l^3(1-l)/(2-l),
    gamma>=(2/3)l^3[(1-l)/(2-l)]^2.                     (14)

Substitution of this value for gamma_0 in (12) is valid.
It gives a correction of order m^3 in the Salem class, rather than the general lower estimate of order m^5.
For example, since gamma's displayed lower bound is l^3/6+O(l^4), the F branch gives

    h_1>=m-6m^3+O(m^4)                                 (15)

as a conditional small-m comparison within that class.
This is not an assertion that a sequence of Salem numbers tending to 1 exists.
It does not exclude one either.
The cubic coefficient in (15) is not claimed optimal; the exact D and gamma are still available from (8) and (13).

### Scope and actual review

All finite matrices and posteriors here come from the original algebraic power orbit.
The reversed coefficient limit is not a replacement by arbitrary moment data, and no existence of a limiting posterior is used.
Integrality supplies the original algebraic setup; the closure, Wiener estimate and positive correction work analytically once the finite Gram relation space is fixed.
No further arithmetic constraint on the allowable Blaschke products, their zero locations or their denominators has been proved here.
In particular the positive rate correction still tends to zero with m.
