---
author: Yin
---

# Single-Haar finite integer-moment lower certificate and its precision costs

The complete necessary proof is now owned by [C379](../claims/Yin_C_G0379_v1.md#argument).
The original fixed author/review inputs below retain their historical scope; their activity descriptions do not authorize present execution.

Date: 2026-10-11.
Root coordinating AI for Yin fixes this restricted exploration under the renewed G0001 authorization after the separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0184_v1.md#whole-restricted-review).
The adopted scope is exactly the complete retained author account below, with its hypotheses, costs, failures, source boundaries and review limits.
It supplies no unrestricted Mahler gap and does not complete G0001.

<a id="resumed-batch-fixed-scope"></a>
## Fixed scope and preservation

The entire original author account and subsequent author response/review notices follow, with only navigation relocated.
Allocation-era unrun or pending-review statements are historical and are superseded for the exact inspected scope by the linked fixed review.
No canonical Claim is registered by this retention.
The Task and all eight routes remain active and unresolved; continued work has a separate draft home.

## Complete retained account


## Arithmetic scale and a global finite lower certificate for the single-Haar determinant

Date: 2026-10-11.
Human author: Yin; developed by the assigned single-Haar AI agent under the current unrestricted G0001 research authorization.
This draft is not a Claim or independently reviewed proof.


## Assigned question and first candidate

For a nonzero integer polynomial P, seek a correctly directed finite lower certificate for m(P)=log Delta(P(U)) through the regularized determinant, with an explicit bound on the small-singular-value error that remains valid at unit-circle zeros.
Retain integer normalization and all degree/height costs.
The first candidate combines exact one-root regularization, a product inequality and a certified finite moment expansion of log(B+epsilon^2).
A finite trial weight is never used as a lower bound.
The candidate may yield only degree/height dependent certificates; determining that cost and its obstruction is part of the question.

The responsible elementary formulation is [scalar weight baseline](Yin_L_G0431_v1.md#single-haar-formulation).
The [L4 Gram bound](Yin_L_G0004_v1.md#gram-lower-certificate) and its finite upper Schur residuals are prior input, not new findings.
[S3](../strategies/Yin_S_G0003.md#single-haar-analytic-focus) supplies the integer application.
No free independence of powers, bounded inverse, degree normalization or reduction of actual conjugates is permitted.

## Historical allocation state

At allocation no finite program had been executed and no quantitative theorem was asserted.
The completed derivations and later executed controls are preserved below; Section6 owns the author freeze and its actual verification scope.

<a id="single-haar-moment-lower-certificate"></a>
## 1. Precise domain, prior work and source attribution

Let P be a nonzero member of Z[z,z^-1].
Strip its monomial factor and write P(z)=a product_(i=1)^d(z-alpha_i), with P(0) nonzero, d the actual exponent span and a nonzero integer.
Multiplicities count.
The case d=0 is a monomial: m(P)=log|a| and E_epsilon(P)=(1/2)log(1+epsilon^2/|a|^2), with the elementary positive gap log2 when |a|>=2.
Assume d>=1 below.
Put B(z)=P(z)P(z^-1)=|P(z)|^2 on the circle, and H=sum_j|a_j|>=1.
Thus B is an integral real-symmetric Laurent polynomial and 0<=B<=H^2.
All traces and circle integrals are Haar probability integrals, with no degree or matrix normalization.

The exact needed input is a global quantitative regularization bound at circle zeros and a polynomial MINORANT for log(B+epsilon^2).
Local searches of Claims, ledgers, drafts and source audits found L4's Toeplitz/discriminant certificate and BGMP24-U001's coefficient-count regularization input.
The latter is discussed in Section5 and is not a premise of Sections2--4.
Searches of the local bibliography and a bounded primary-source web search found no exact matching combined certificate.
This does not establish novelty.
The log-Chebyshev expansion is standard: [NIST DLMF18.12.9](https://dlmf.nist.gov/18.12.E9), checked online on2026-10-11, states -log(1-2xz+z^2)=2 sum_(n>=1)T_n(x)z^n/n for |z|<1; its note attributes the formula to Szego(1975), equation4.7.25.
That is attribution for the elementary expansion proved below, not a claim of new Chebyshev theory.
The root regularization computation is given completely; no priority claim is made.

<a id="zero-compatible-root-error"></a>
## 2. A global zero-compatible error with its full degree cost

For epsilon>0 let m_epsilon(P)=(1/2)integral log(B+epsilon^2), E_epsilon(P)=m_epsilon(P)-m(P).
Then

    0<=E_epsilon(P)
      <=d asinh((epsilon/M(P))^(1/d)/2)
      <=d asinh(epsilon^(1/d)/2).                   (1)

The last step uses M(P)=|a| product_i max(1,|alpha_i|)>=1, precisely where integer normalization enters.
It is not valid with the same absolute epsilon after arbitrary small complex scalar rescaling.
The preceding inequality remains valid for arbitrary nonzero complex polynomials with their actual M(P).

Proof.
Put R_i=max(1,|alpha_i|), x_i(z)=|z-alpha_i|^2/R_i^2 and delta=(epsilon/M(P))^(1/d).
Then B/M(P)^2=product_i x_i and integral log x_i=0, including |alpha_i|=1.
Expanding a product of nonnegative terms gives

    product_i(x_i+delta^2)>=product_i x_i+delta^(2d).

Consequently

    E_epsilon(P)<=sum_i (1/2)integral log(x_i+delta^2).

The distribution of x_i on the circle equals that of |1-r_i z|^2 for r_i=min(|alpha_i|,|alpha_i|^-1) in[0,1], with the natural r_i=0 convention.
Set y=r_i^2, A=1+y+delta^2 and lambda=(A+sqrt(A^2-4y))/2.
Since delta>0, lambda>sqrt(y), and

    1+y+delta^2-2r_i cos(theta)
       =lambda |1-(r_i/lambda)e^(i theta)|^2.

The second factor has logarithmic average zero by the convergent geometric log series, so the half-log integral equals(1/2)log lambda.
Its derivative with respect to y is positive: lambda'=(1+(A-2)/sqrt(A^2-4y))/2>0, since

    (A^2-4y)-(A-2)^2=4delta^2>0.

Hence its maximum on[0,1] occurs at y=1 and equals asinh(delta/2).
Summing proves(1).
No root separation, nonvanishing on the circle, irreducibility or squarefreeness was used.
The result covers the Salem hard core, but the coarse bound does not exploit its simple roots.

This is a quantitative error estimate, not a lower bound for m by itself.
A target error r>0 is guaranteed by the last bound in(1) precisely when

    epsilon <= [2 sinh(r/d)]^d.                    (2)

For fixed r and unbounded d this sufficient arithmetic-scale guarantee requires epsilon of order(constant/d)^d.
It would be incorrect to call(2) a necessary precision for the actual polynomial: it is the cost of using this general bound.

<a id="chebyshev-integer-moments"></a>
## 3. A correctly directed finite lower certificate

Let T_k(cos theta)=cos(k theta).
Define

    s(z)=2B(z)/H^2-1 in[-1,1],
    mu_k=integral T_k(s(z)),
    t=sqrt(H^2+epsilon^2),
    rho=(t-epsilon)/(t+epsilon) in(0,1),
    C=(t+epsilon)^2/4,
    tau_N=rho^(N+1)/((N+1)(1-rho)), N>=0.

All mu_k are rational and |mu_k|<=1.
The regularized log determinant obeys

    |m_epsilon(P)-S_(N,epsilon)(P)|<=tau_N,
    S_(N,epsilon)(P)
      =log((t+epsilon)/2)
         +sum_(k=1)^N (-1)^(k+1) rho^k mu_k/k.      (3)

In particular the directionally valid lower certificate is

    m(P)>=S_(N,epsilon)(P)-tau_N
                  -d asinh(epsilon^(1/d)/2).       (4)

One can replace the last term by any separately justified sharper upper bound for E_epsilon(P).
Formula(4) is global, as a polynomial minorant integrated against the actual circle law; it is not an infimum restricted to trial weights, and its direction differs from finite Schur residual upper bounds in L4.

Proof.
The identity

    B+epsilon^2=C(1+2rho s+rho^2)

holds by direct substitution: 2C rho=H^2/2 and C(1-rho)^2=epsilon^2.
For s=cos theta the two factors 1+rho exp(+/-i theta) have absolute value bounded away from zero.
Their absolutely uniformly convergent log series yield

    (1/2)log(B+epsilon^2)
      =(1/2)log C
        +sum_(k>=1)(-1)^(k+1)rho^k T_k(s)/k.

This is the DLMF18.12.9 specialization with z=-rho.
Since |T_k(s)|<=1, the omitted absolute sum is bounded by sum_(k>N)rho^k/k<=tau_N.
Integrating proves(3), and subtracting(1) proves(4).
Uniform convergence is used only at epsilon>0.
Neither interchange at epsilon=0 nor bounded invertibility of P(U) is assumed.

The integer recurrence producing the complete moments is

    R_0=1, R_1=2B-H^2,
    R_(k+1)=2(2B-H^2)R_k-H^4 R_(k-1),
    R_k=H^(2k) T_k(s),
    mu_k=constant_coefficient(R_k)/H^(2k).          (5)

It retains every coefficient phase and autocorrelation.
The mu_k are not independently free parameters: they are linked by the same integral B and its Laurent convolution.
The support of R_k lies in[-kd,kd].
Since |T_k(s)|<=1 pointwise, every Fourier coefficient of R_k has modulus at most H^(2k); the numerator and denominator thus have O(k log(2H)) bits.
A direct sparse multiplication by B over all k<=N uses at most O(N^2 d^2) integer arithmetic operations with those growing bit sizes.
No dimension factor is divided out of the target.

<a id="precision-obstruction"></a>
## 4. Exact cost obstruction for this particular tail control

The Chebyshev tail improves the elementary Taylor-log tail: its exponential scale is N epsilon/H, instead of N epsilon^2/H^2.
It still cannot be advertised as a degree-linear finite certificate with the general error(1).

A precise lower cost follows directly from the tail being used.
Suppose0<epsilon<=H/4 and N+1<=H/(4epsilon).
Put y=epsilon/t<=1/4.
Then rho=(1-y)/(1+y) and

    log rho=-2 atanh y>=-(8/3)y>=-(8/3)epsilon/H.

Here atanh y=integral_0^y (1-u^2)^-1 du<=y/(1-y^2)<=4y/3.
Therefore rho^(N+1)>=exp(-2/3), while (N+1)(1-rho)<=1/2.
It follows that

    tau_N>=2 exp(-2/3)>1.                         (6)

The last inequality follows from exp(2/3)<2, for example log2=integral_1^2 dt/t>2/3 by strict convexity of1/t and its midpoint value2/3.
Thus demanding this displayed worst-case tail be less than1 forces N+1>H/(4epsilon).
Combining(2) with any fixed small target error gives a superpolynomial generic moment depth in d.
This is an obstruction to the present general certificate cost, not a lower bound on the true determinant's complexity and not a refutation of another structured minorant.

In particular integer moments alone have not produced a gap: integrality gives exact finite data and M(P)>=1, while all useful arithmetic information needed to improve the tail/sublevel bound remains to be supplied.
A useful next construction must couple the actual coefficient relation to cancellation of the Chebyshev tail or an improved sublevel estimate.
Merely increasing N for the same worst-case tail repeats this quantified cost.

## 5. Sparse-source comparison and controls

[BGMP24-U001](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001) retains Proposition4.10 with its original proof-inspection boundary.
In its one-variable identity-map specialization, for k>=2 nonzero coefficients and coefficient maximum A>=1, substitute P/A and regularizer epsilon^2/A^2.
The displayed accepted statement gives, for0<alpha<1,

    E_epsilon(P)<=12k^2/(1-alpha)
                       (epsilon/A)^((1-alpha)/(k-1)). (7)

The identity monomial map has infinite rho and satisfies the source support condition.
This is an ordinary parameter substitution, not a new theorem or independent audit of its underlying multivariate sublevel input.
Its constants are large; for fixed k it can remove exponent dependence on d.
For unrestricted dense inputs k may grow with d, so this fact supplies no uniform gap.
The pointwise minimum of(1) and(7) can be substituted in(4), but neither is presumed to be sharp.
The questioned later constant in that source's Theorem4.1 is not used.

Named controls were fixed before execution: P=z-1 and P=z^2+z+1 (cyclotomic zeros), P=z^2-3z+1 (a positive reciprocal unit), and the actual degree-ten Lehmer polynomial from L4 (positive measure with circle zeros).
No parameter scan or unbounded-degree extrapolation was intended or run.
[J84](../computations/programs/Yin_J_G0084/readme.md) retains the exact integer moments and rational interval evaluation; no floating output certifies positivity.

<a id="frozen-author-account"></a>
## 6. Frozen author account, finite controls and remaining obligation

On2026-10-11 the author-side AI ran exactly the four declared controls at epsilon=1/4 and N=64, with integer/Fraction moments,100-bit algebraic bisection and128-term range-reduced rational atanh enclosures.
The native output (`mathematics/computations/outputs/Yin_J_G0084/data.json`) retains the full moment arrays.
Independent explicit-binomial Chebyshev moment calculations through8 matched the integer recurrence; all moment and Fourier-coefficient bounds through64 passed.
Rational interval certificates prove

    m(z^2-3z+1)>=0.475476702547483780>0.

The exact measure log((3+sqrt5)/2) was separately enclosed, and the retained finite lower bound lies strictly below it.
The two cyclotomic lower certificates remain negative, giving no false positive.
The Lehmer input's bound is in[-3.908887255960695643,-3.908887255960695642], demonstrating that this parameter choice plus the generic root error is vacuous even on the actual degree-ten hard core.
It is a lower-certificate value, not the polynomial's Mahler measure.
No root scan, arbitrary numerical quadrature or false statement of global testing is involved.

The author proof in Sections2--4 is complete at the stated scope.
The source-specialized optional estimate(7) retains its existing external-input boundary.
The finite program was inspected by its author for arithmetic mode, interval directions, log-tail index, exact moment normalization and output completeness; there is no independent project review at this freeze.
No canonical Claim or unrestricted gap is asserted.
Root owns any promotion to fixed support and separate review arrangement.

The changed conclusion is a globally directed, coefficient-exact single-Haar lower certificate, together with an explicit obstruction to using its WORST-CASE regularization and tail costs at degree-linear scale.
This does not improve L4 universally and no numerical competition with L4 is claimed.
Its advantage for the requested analytic/arithmetic interface is that every finite moment comes from the actual integer autocorrelation symbol, and the two independently charged analytic errors are visible.

The next useful question is whether the integer relation or reciprocal irreducibility can control the actual signed tail sum, or strengthen the small-value bound in a manner that beats(2),(6) uniformly on near-one inputs.
Simple roots alone do not supply a uniform derivative lower bound; proving a new such control must keep all degree/height costs.
Recomputing higher N with the same generic bounds or merely repeating fixed-input convergence is not a new exploration round.
This draft is ready for root's noncontributor scrutiny and fixed retention, with no edits required outside its own D/J scope.
