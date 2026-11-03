---
author: Yin
---

# Whole review of the single-Haar finite lower certificate and four exact controls

Date and attribution: 2026-10-11T11:08.
Human record author: Yin.
The integer_bundle_research AI was separately assigned this noncontributor whole-proof and computation review of [D_G0004](../../ledger/Yin_L_G0358_v1.md#frozen-author-account) and [J84](../../computations/programs/Yin_J_G0084/readme.md).
The reviewer supplied none of the root regularization proof, Chebyshev derivation, candidate selection, author implementation or initial results.
Root's assignment and the author's frozen text/results were available; no previous independent conclusion was supplied or consulted.
Shared repository context and the author's self-check are disclosed, so this is a nonblind separately organized review rather than a claim of completely separate information.
The reviewer first worked backward from the lower-certificate assertion and explicit scope, then checked the forward argument and full retained program.

The inspected revision is D_G0004's 2026-10-11 Sections 1--6, equations (1)--(7), its declared four-case freeze, and the unchanged J84 main.py/data.json/readme.md author artifacts.
All original polynomial degrees, coefficient heights, error terms and arithmetic normalization are within this review.
This is not G0001 completion, a full source audit, root-isolation review of Lehmer, or an independent implementation of every author routine.
The exact native reproduction calls the existing author's mathematical functions read-only after separately inspecting them; that shared implementation boundary is explicit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole restricted review](#whole-restricted-review) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole restricted review](#whole-restricted-review) | [D4 domain](../../ledger/Yin_L_G0358_v1.md#single-haar-moment-lower-certificate) | Whole domain, original integer scale, all Sections 1--6, formulas (1)--(7), finite results and remaining obligations. |
| [Whole restricted review](#whole-restricted-review) | [D4 global root error](../../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Complete bound, repeated/circle roots, d=0 branch, sufficient precision cost. |
| [Whole restricted review](#whole-restricted-review) | [D4 finite moment certificate](../../ledger/Yin_L_G0358_v1.md#chebyshev-integer-moments) | Chebyshev sign and normalization, uniform tail, exact integer recurrence, polynomial complexity and correctly directed lower estimate. |
| [Whole restricted review](#whole-restricted-review) | [D4 exact tail obstruction](../../ledger/Yin_L_G0358_v1.md#precision-obstruction) | All hypotheses, constants, and the limitation to the displayed worst-case certificate. |
| [Whole restricted review](#whole-restricted-review) | [J84 declaration and outcomes](../../computations/programs/Yin_J_G0084/readme.md) | Entire four-case scope at epsilon=1/4, N=64; program and all native mathematical fields. |
| [Whole restricted review](#whole-restricted-review) | [J84 program](../../computations/programs/Yin_J_G0084/main.py) | Complete program inspection, interval directions, binomial checks, all controls reproduced without invoking its file-writing main(). |
| [Whole restricted review](#whole-restricted-review) | [BGMP24-U001](../literature/BGMP24/Yin_U001.md#bgmp24-u001) | Statement/applicability of optional one-variable coefficient-normalized regularization estimate only; underlying multivariate sublevel proof not re-audited. |
| [Whole restricted review](#whole-restricted-review) | [Output of the recorded run](../../computations/programs/Yin_J_G0084/readme.md#recorded-runs) | Every full moment array and exact outward series/tail/error/lower-certificate interval compared, with source inputs and status scopes. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0084/data.json`; this target locates that original run's computation account. |


## Whole restricted review

**Verdict.**
The complete restricted argument and declared finite controls pass.
No mathematical repair is requested.
The globally valid lower-certificate direction is correct and includes the full degree-dependent error at circle zeros.
The precision obstruction applies to this particular general error/tail pair, not to the original problem or all analytic methods.
The actual Lehmer control remains a vacuous negative lower-certificate value.
It is not a negative Mahler measure or an unrestricted result.

### 1. Original scale, roots and global regularization error

I checked the stripped Laurent monomial factor, actual exponent span d, nonzero integer leading factor, all root multiplicities, and the separate monomial d=0 branch.
For d>=1, division by M(P)^2 gives exactly product x_i, and delta^(2d)=epsilon^2/M(P)^2.
Expanding product(x_i+delta^2) retains the two required nonnegative terms, with all mixed terms nonnegative.
The resulting logarithmic integral inequality has the upper direction asserted; each original normalized root contributes logarithmic integral zero, including a unit-circle zero with its integrable logarithmic singularity.

For one root the circle distribution is |1-rz|^2, 0<=r<=1.
I independently substituted the stated lambda into lambda|1-(r/lambda)z|^2, checked lambda>r for epsilon>0, and used the convergent logarithm series for its zero logarithmic integral.
With y=r^2, the discriminant identity (A^2-4y)-(A-2)^2=4delta^2 proves that lambda increases strictly with y.
Its value at y=1 has half-log asinh(delta/2).
This proves the bound at every repeated or simple circle root, with no separation or invertibility requirement.
The integer step M(P)>=1 is correctly isolated; an arbitrary small complex scalar would invalidate only that last absolute-scale simplification.

Solving d asinh(epsilon^(1/d)/2)<=r gives precisely epsilon<=[2sinh(r/d)]^d.
This is sufficient precision for the bound being used, not a necessary precision for the actual polynomial.
That distinction is stated.
The monomial formula and its log2 integer positive gap are correct and are not substituted for the unit hard core.

### 2. Finite lower direction, Chebyshev moments and source

Substitution gives B+epsilon^2=C(1+2rho s+rho^2), with 2C rho=H^2/2 and C(1-rho)^2=epsilon^2.
Both log factors have uniformly convergent series because epsilon>0 implies rho<1.
The factor one-half, alternating sign (-1)^(k+1), leading log((t+epsilon)/2) and the moment mu_k=integral T_k(s) all match.
The absolute omitted sum is at most rho^(N+1)/((N+1)(1-rho)).
Thus S_N-tau_N is a minorant for m_epsilon, and subtracting an UPPER regularization error gives the claimed lower bound for m.
Neither a restricted trial-weight infimum nor an epsilon=0 interchange is used.

The reviewer separately opened the primary [NIST DLMF18.12.9](https://dlmf.nist.gov/18.12.E9) on2026-10-11.
It states the logarithmic generating identity for |z|<1; the page's source note identifies Szego(1975), (4.7.25).
The z=-rho substitution is exact.
This is checked attribution for the local series proof, not an inspected original Szego proof or a new source acquisition.

I derived the integer recurrence by multiplying the ordinary Chebyshev recurrence by H^(2k+2).
Its second term is H^4 R_(k-1), exactly as stated.
The support [-kd,kd], rational constant coefficients and Fourier coefficient bound H^(2k) follow from the pointwise |T_k|<=1.
The bit bound O(k log(2H)) and the O(N^2 d^2) direct convolution operation count correctly retain growing precision and are not a polynomial-time assertion in a superpolynomially required N.
Coefficient phases are retained because every moment is produced from the same original Laurent autocorrelation symbol.

### 3. The precise tail-cost obstruction and optional sparse interface

Under epsilon<=H/4, y=epsilon/t<=1/4 and atanh y<=y/(1-y^2)<=4y/3.
Since y<=epsilon/H, log rho>=-(8/3)epsilon/H.
The additional N+1<=H/(4epsilon) gives rho^(N+1)>=exp(-2/3) and (N+1)(1-rho)<=1/2, hence tau_N>=2exp(-2/3)>1.
I checked the last strict logarithm comparison by the integral of1/t on[1,2].
The proof and its constants are valid.
Combining the sufficient epsilon from Section2 with this necessary cost for the DISPLAYED tau bound gives a superpolynomial generic depth at fixed target error; it does not claim lower complexity for the actual determinant or rule out signed-tail cancellation.

I read the complete existing BGMP24-U001 statement/interface.
In one variable its constant is12k^2/(1-alpha).
For P/A, the maximum coefficient is1, the identity monomial map has rho=infinity, and substituting source regularizer epsilon^2/A^2 yields exponent (epsilon/A)^((1-alpha)/(k-1)).
Every support and positivity hypothesis matches for k>=2.
Thus optional formula(7) is supported at the source unit's accepted statement/applicability scope; the underlying multivariate sublevel theorem was not re-proved.
The source's questioned later Theorem4.1 constant does not enter.
The optional bound is not a premise of the root proof or four executed generic controls.

### 4. Full program inspection and exact read-only native reproduction

I read every line of J84 main.py.
Its integer Laurent convolution and recurrence preserve all coefficients; the through-eight explicit binomial formula for T_k supplies a distinct finite algebraic cross-check.
This internal author check is not described as an independent reviewer implementation.
The root bisection uses integer n-th-power comparisons at100binary bits with outward endpoints, including a valid initial upper bound.
Interval products enumerate all endpoint products; divisions require positive denominators; signed logarithm range reduction handles negative dyadic exponents through interval multiplication.
The128-term atanh tail starts at power257 and uses denominator257(1-t^2), with the upper direction required.
All interval operations therefore enclose their mathematical expressions despite dependency widening.
The outward decimal rounding uses floor for the lower endpoint and ceiling for the upper endpoint, including negative values.

The reviewer reproduced exactly the declared four cases, epsilon=1/4 and N=64, through an ephemeral read-only Python invocation importing main.py via importlib.
It called moments(), certificate() and outward() for each original polynomial, compared EVERY stored moment numerator/denominator and the complete regularized_series, chebyshev_tail, global_root_error and mahler_lower_certificate intervals, and checked original coefficient arrays, degree, coefficient_l1 and exact scope parameters.
It did not call main(), so data.json was not written or replaced.
No new input, parameter, optimization, root scan or numerical quadrature was run.
The command completed successfully and printed all four native intervals:

| Input | Exact reproduced lower-certificate interval |
| --- | --- |
| z-1 | [-0.000000006371739922,-0.000000006371739921] |
| z^2+z+1 | [-0.351574168904568570,-0.351574168904568569] |
| z^2-3z+1 | [0.475476702547483780,0.475476702547483781] |
| Original Lehmer degree ten | [-3.908887255960695643,-3.908887255960695642] |

The reviewer separately checked the two cyclotomic negative upper endpoints and enclosed log((3+sqrt5)/2), confirming that the positive quadratic lower interval lies strictly below the exact measure.
The Lehmer lower interval is negative, as claimed, and receives no exact-measure assertion.
The internal moments()/certificate() routines remain author code reused for reproduction; whole mathematical validity also rests on the independent proof reconstruction above and the reviewed interval logic, not output agreement alone.

### 5. Outcome, minor presentation note and limits

The opening allocation-era 'Work in progress / No finite program has been executed' sentence should be labelled historical or superseded by Section6 to prevent a current-status ambiguity.
The author was notified before fixed retention.
This is an editorial chronology clarification and does not change any proof formula, program result, domain or review verdict.

All substantive obligations of the frozen proof and the complete declared finite mathematical payload have been checked.
The old L4 comparison remains contextual and was not rerun.
No whole-source proof audit of BGMP24, formal verification, root classification of new inputs, original Lehmer optimality, near-one uniformity or Task completion is asserted.
The two outstanding mathematical obligations remain the actual integer-structure improvement of the regularization/sublevel bound and a usable signed-tail or structured-minorant estimate.
Increasing N with unchanged worst-case costs is not a new general mechanism.

## Relationship clarification during proof-home construction

The original account discloses shared context and the author's self-check without establishing the complete contents and order of exposure before the first findings.
It therefore does not establish the independence initially recorded; it also does not by itself establish a contributing or self-review relationship.
The relationship is unknown.
Reading the native author implementation and result data is part of the necessary declared proof and computation input and does not alone determine this relationship.
The original mathematical finding, source-reading depth, finite controls, date and all fixed-input bindings remain as recorded.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
