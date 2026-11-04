---
author: Yin
---

# A sharp temporal moment obstruction for the actual quartic return law

Human author Yin.
Phase_bands derived the temporal Hankel obstruction and sharp relative-error control while investigating the actual S2/S7 critical-mean question.
Root selected that inquiry and requested exact spectral-measure, operator-domain and asymptotic boundaries.
This is author development, not independent review.
The original finite counts are existing adopted mathematics, not a new calculation or numerical experiment.

## Statement

Fix the actual irreducible Salem quartic

    P(t)=t^4-t^3-t^2-t+1

and its real exterior root beta.
Let O=Z[beta], let D be its entire original zero-to-zero core, and use the ORIGINAL independent digit probabilities

    Pr(eta=0)=1/2, Pr(eta=1)=Pr(eta=-1)=1/4.

The chronological process is X_(j+1)=beta X_j+eta_j, with K its original kernel killed on leaving D.
For integers n>=0 let

    p_n=K^n(0,0)=Pr(sum_(j=0)^(n-1)eta_j beta^j=0), p_0=1.

Every original returned word and its complete weight is retained, including earlier zero visits.
The exact existing counts give

    p_4=1/16, p_5=17/512, p_6=9/512,
    p_4p_6-p_5^2=-2^-18.                              (TM1)

For EVERY real scale lambda>0 put a_n(lambda)=lambda^n p_n.
Then

    det [[a_4(lambda),a_5(lambda)],
         [a_5(lambda),a_6(lambda)]]=-lambda^10/2^18<0,  (TM2)
    289lambda^2 a_4(lambda)-1088lambda a_5(lambda)
                          +1024a_6(lambda)=-lambda^6/16. (TM3)

Consequently there is NO positive finite Borel measure nu on the REAL line with finite sixth absolute moment such that

    integral t^j dnu(t)=a_j(lambda), j=4,5,6.           (TM4)

The measure need not be a probability, and its support need not be positive or bounded.
The impossibility already concerns these three moments; no uninspected spectral representation theorem is invoked.
On the operator side, no bounded selfadjoint operator T on any complex Hilbert space and vector v can satisfy

    <v,T^j v>=a_j(lambda), j=4,5,6.                    (TM5)

No claim about unbounded operators without specified domains is made.

The quantitative obstruction is sharp.
Define

    epsilon_*=(17-12sqrt2)/(17+12sqrt2)
             =577-408sqrt2 in(0,1/33).                 (TM6)

For every positive finite Borel measure nu with finite sixth moment, write m_j=integral t^j dnu(t) for j=4,5,6.
Its simultaneous relative error satisfies

    max_(j=4,5,6) abs(m_j-a_j(lambda))/a_j(lambda)
                                                 >=epsilon_*. (TM7)

For EVERY lambda>0 equality in(TM7) is attained by the explicit TWO-ATOM PROBABILITY

    x_lambda=3lambda/(4sqrt2),
    w_*=64(1+epsilon_*)/81 in(0,1),
    nu_lambda=(1-w_*)delta_0+w_*delta_(x_lambda).         (TM8)

In fact its moments satisfy

    m_4=(1+epsilon_*)a_4(lambda),
    m_5=(1-epsilon_*)a_5(lambda),
    m_6=(1+epsilon_*)a_6(lambda).                       (TM9)

Thus epsilon_* is the exact infimum, and a minimum, even when the comparison class is restricted to probabilities.
It is a finite three-moment approximation statement, not a claimed approximation to all times.

### Exact original and critical consumers

For lambda=1 the actual original return sequence is not log-convex at its fifth term:

    p_5^2>p_4p_6,
    p_5/p_4=17/32>9/17=p_6/p_5.                       (TM10)

Write f_n for the complete original first-positive-return probabilities and F(z)=sum_(n>=1)f_n z^n.
For the TRUE critical radius R of this actual quartic, the adopted C204 interface supplies

    2^(5/8)<=R<=beta<7/4,
    F(R)=1,
    H(0)=1, H(x)>0,
    Q(x,y)=R K(x,y)H(y)/H(x),
    Q^n(0,0)=R^n p_n.

These premises do not identify R with beta and do not decide whether the critical mean mu=sum_(n>=1)n R^n f_n is finite.
Taking lambda=R in(TM2)--(TM7) excludes an exact positive real spectral-moment representation of this ACTUAL recurrent Doob return sequence in either possible mean branch.
The same sharp approximation obstruction applies at its moments4,5,6.
Here x_R<21/(16sqrt2)<1, so the attaining comparison probability(TM8) can even be supported in[0,1].
This does not turn that comparison measure into the original return law or a Markov model for it.

In particular, no reversible stochastic kernel on a countable state space, with a strictly positive invariant measure finite at each state, can have a distinguished state's return probabilities exactly a_n(lambda) for n=4,5,6.
This excludes such a different reversible realization as well as reversibility of the actual Q.
The invariant measure in this statement is allowed to have infinite total mass.

The result concerns exact times4,5,6 and any positive exponential scale.
It does NOT refute eventual log-convexity, an asymptotic spectral approximation whose initial moments differ, a nonselfadjoint transfer mechanism, or positivity of the distinct spatial correlation functions on O.
It does not decide the actual finite/infinite critical mean, prove all-late escape or an improved original weighted flow, identify R=beta, or resolve the unrestricted Lehmer Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Complete argument

### 1. Focused reuse and exact original counts

The actual core and critical-mean scope are those of [C204](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse).
The existing [C445 statement](Yin_C_G0445_v1.md#statement) gives p_N=2^-N for N<=degree(P), and its [complete six-digit control](Yin_C_G0445_v1.md#quartic-center-versus-lower-row-control) gives p_6=9/512 with every original coefficient constraint and weight retained.
The five-digit value also occurs in [C300](Yin_C_G0300_v1.md#quartic-uniform-positive-covariance).
The bounded local reuse search for log-convexity, temporal return Hankel matrices and selfadjoint return representations found C572's warning not to assume log-convexity and these exact counts, but no existing account of(TM2)--(TM9).
C445 owns its coupled-center/lower-row loss; the present conclusion is a separate temporal scalar-moment obstruction derived from those same original counts.
The general Gram nonnegativity used below follows directly from an integral of a square or a squared Hilbert norm.
No general moment-representation, spectral, Tauberian or reversible-chain convergence theorem is a proof input.

For completeness the full count interpretation can be checked in the actual polynomial coordinates without enumeration.
A returned length-N digit polynomial E with coefficients in{-1,0,1} is divisible by the monic irreducible P.
For N=4 its degree is at most3, so only E=0 returns and p_4=2^-4.
For N=5 a nonzero E must be P or-P, whose five digits are all nonzero; together with E=0 their complete probability is

    p_5=2^-5+2*4^-5=17/512.

For N=6 write E=P(u+vt).
Its entire coefficient vector is

    (u,v-u,-u-v,-u-v,u-v,v).

The first and last entries force u,v in{-1,0,1}.
If both are nonzero, equal signs violate abs(u+v)<=1 and opposite signs violate abs(u-v)<=1.
Exactly five possibilities remain: (0,0),(1,0),(-1,0),(0,1),(0,-1).
The zero word has probability2^-6; each of the other four has five nonzero digits and one zero, hence probability4^-5/2.
Thus p_6=2^-6+4*(4^-5/2)=9/512.
These are the already retained C445/C300 counts, with no deleted zero visit, chosen tail representative, changed law or numerical execution.

### 2. A negative temporal Gram block at every exponential scale

The actual unscaled block is

    [[p_4,p_5],[p_5,p_6]]=(1/512)[[32,17],[17,9]].

Its determinant is(288-289)/512^2=-2^-18.
Multiplying entry(i,j), i,j in{2,3}, by lambda^(i+j) multiplies the determinant by lambda^10 and proves(TM2).
Its quadratic value at(17lambda,-32) is

    289lambda^2(lambda^4/16)
      -1088lambda(lambda^5*17/512)+1024(lambda^6*9/512)
      =lambda^6(289-578+288)/16=-lambda^6/16,

which proves(TM3).

If a positive finite real-line measure had the three claimed moments, the left side would equal

    integral t^4(17lambda-32t)^2 dnu(t)>=0.

Finite sixth moment and finiteness of the measure ensure all these integrals exist.
This contradicts(TM3), independently of the sign of t or of the total mass of nu.

For a bounded selfadjoint T, the same quadratic expression equals

    ||17lambda T^2v-32T^3v||^2>=0.

Selfadjointness moves the powers between the two inner-product slots, giving exactly the moments4,5,6.
Thus(TM5) fails without needing to invoke an operator spectral representation.
These proofs establish the claimed finite obstruction even for a hypothetical surrogate on an entirely different state space.

### 3. Exact optimal relative error and explicit probability control

Every positive real measure with finite sixth moment satisfies

    m_5^2<=m_4m_6,

by Cauchy--Schwarz applied to t^2 and t^3.
Let epsilon be the maximum relative error in(TM7).
If epsilon>=1, the desired lower bound is immediate, so assume0<=epsilon<1.
All target a_j(lambda) are positive, and the relative error inequalities give

    (1-epsilon)^2 a_5(lambda)^2
       <=m_5^2<=m_4m_6
       <=(1+epsilon)^2 a_4(lambda)a_6(lambda).

Cancelling the positive lambda^10/512^2 gives

    289(1-epsilon)^2<=288(1+epsilon)^2.

Taking positive square roots and solving yields

    epsilon>=(17-12sqrt2)/(17+12sqrt2)=epsilon_*.

Rationalization gives epsilon_*=577-408sqrt2.
It is positive since17^2>288.
Since12sqrt2>16, its numerator is less than1 and denominator greater than33, so epsilon_*<1/33.
Therefore

    0<w_*=64(1+epsilon_*)/81<64*34/(81*33)<1.

This proves that(TM8) is a genuine probability for EVERY lambda>0; its weights do not depend on lambda.
Its support is finite, so it has every absolute moment.
Since x_lambda^2=9lambda^2/32 and x_lambda^4=81lambda^4/1024,

    w_*x_lambda^4=(1+epsilon_*)lambda^4/16,
    w_*x_lambda^6=(1+epsilon_*)9lambda^6/512.

The defining equality17(1-epsilon_*)=12sqrt2(1+epsilon_*) gives

    w_*x_lambda^5=(1-epsilon_*)17lambda^5/512.

These are exactly(TM9), so every relative error is epsilon_* and the bound is attained.
The added atom at zero makes total mass1 without changing moments4,5,6.
No matching of the original moments1,2,3 or later times is asserted.

### 4. Critical Doob law, reversible realizations and the precise boundary

The chronological monotone-ratio failure(TM10) follows by dividing the positive values in(TM1).
Indeed17/32-9/17=1/544>0.
Multiplication by lambda^n multiplies each ratio by lambda and does not repair the failure.
It also multiplies p_4p_6-p_5^2 by lambda^10, so no positive exponential normalization restores this temporal Gram condition.

C204 proves true-radius recurrence F(R)=1 and constructs the actual stochastic Q on all of D using the complete first-hit H.
Its exact telescoping identity is

    Q^n(x,y)=R^n K^n(x,y)H(y)/H(x).

At x=y=0 this is precisely a_n(R)=R^n p_n, without any finite-mean hypothesis.
Thus the obstruction applies to the actual critical law in BOTH possible mean branches.
Using only R<7/4 gives x_R<21/(16sqrt2)<1, because441<512, proving the stated[0,1] support property of the sharp comparison probability.

To verify the reversible consequence directly, let T be a stochastic matrix on a countable set, reversible for a strictly positive measure m with0<m(x)<infinity at each state.
Detailed balance implies invariance by nonnegative summation, even if sum m is infinite.
For finitely supported f, Jensen's inequality gives

    sum_x m(x)abs(Tf(x))^2
       <=sum_(x,y)m(x)T(x,y)abs(f(y))^2
       =sum_y m(y)abs(f(y))^2.

Therefore T extends to a bounded contraction on l2(m).
Detailed balance makes it selfadjoint, first on finitely supported vectors and then by continuity.
Its operator powers on a point indicator agree with the original kernel powers by nonnegative finite truncation and pointwise convergence of l2(m) limits at each state of positive finite mass.
For a distinguished state o, the unit vector v=1_{o}/sqrt(m(o)) has

    <v,T^jv>_(l2(m))=T^j(o,o).

If its three return values were a_j(lambda), this would contradict(TM5).
No recurrence, finite total invariant mass or stationary probability is assumed in this implication.

The existing C203 already proves nonnormality of the original full-strip operator; that fact alone would not exclude a different selfadjoint scalar-moment realization.
The three-time calculation above excludes the latter as well.
C563's positive definiteness is instead indexed by differences of spatial elements in O and concerns actual endpoint or harmonic/occupation functions.
It supplies no positivity for the temporal matrix(p_(i+j)), which(TM1) shows is false here.
This distinction is why spatial autocorrelation positivity cannot simply be turned into a one-variable positive real spectral law for chronological returns.

The argument uses only times4,5,6 and imposes no condition at arbitrarily large times.
It therefore gives no conclusion about eventual log-convexity, late-time monotone ratios, asymptotic spectral surrogates or either critical-mean branch.
The full original endpoint products, C645's linear D_n bound, C698v2's restricted short-witness certificates and all original weighted flow/clock costs remain unchanged.
No new all-late mass or congestion estimate is supplied.

## Source and reuse boundary

The exact finite counts and their symbolic original-law proof are reused from C445 and C300 at their adopted scope.
The new deductions are the scale-uniform temporal Gram obstruction, its exact positive-real-measure and bounded-selfadjoint scope, and the sharp three-entry multiplicative tolerance with its explicit probability realization.
The proof is finite algebra and nonnegativity of squares; no new named moment theorem or external source is required or asserted.
C204 supplies the actual true-R Doob identity only, with its recurrent but unresolved mean status preserved.
C203 and C563 supply distinct existing operator/spatial-positivity context, not a substitute model for the original return sequence.
No native calculation or additional original counts were executed, and no source inspection depth is enlarged.

## Assessment history

### Decision temporal-moment-obstruction-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:37 |
| status | open |
| reason | Register the complete actual quartic temporal Gram obstruction at moments4,5,6 for every positive exponential normalization, exact positive-real-measure and bounded-selfadjoint exclusions, sharp relative-error minimum and explicit two-atom probability, and the actual critical-Doob/reversible consumers. Existing full original counts are reused; fresh independent whole review remains required. No eventual asymptotic or critical-mean classification, new count run, source-depth expansion or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire temporal obstruction](#statement) | TM1--TM10, every lambda>0, all positive finite real measures with finite sixth moment, bounded selfadjoint and reversible scopes, sharp probability control and precise original/critical limitations. |
| argument | [Complete finite proof and consumers](#complete-argument) | Sections1--4, exact original counts, negative temporal Gram/square, optimal relative tolerance and full probability verification, actual Doob telescoping and bounded reversible realization argument. |
| dependency | [Original six-digit count](Yin_C_G0445_v1.md#quartic-center-versus-lower-row-control) | Actual full coefficient feasibility and original weighted p6=9/512; its statement also gives p_N=2^-N for N<=degree(P). No new experiment or coupled-rate theorem is claimed. |
| dependency | [Original five-digit count](Yin_C_G0300_v1.md#quartic-uniform-positive-covariance) | The exact legal returned words0,+P,-P and p5=17/512 under the original digit law. |
| dependency | [Actual critical Doob interface](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Full original core and law, true-R recurrence/range, positive H and exact Q construction; no mean branch or R=beta assertion. |
| dependency | [Exact Doob telescoping](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | Formula9 at every chronological time; its finite-mean limits are not used. |
| support | [Distinct original operator nonnormality](Yin_C_G0203_v1.md#statement) | Existing full-strip norm/nonnormality only, distinguished from the new impossibility of a different scalar selfadjoint moment realization. |
| support | [Spatial positive-definite account](Yin_C_G0563_v1.md#occupation-fourier-fixed-scope) | Existing whole-order spatial correlation and critical occupation positivity; no temporal positive moment assertion is imported. |
| support | [Source and reuse boundary](#source-and-reuse-boundary) | Existing exact counts, new finite deductions, no new source/native work, and the retained actual critical-mean and asymptotic limitations. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T07:49 |
| status | proved |
| reason | Adopt the entire finite temporal moment obstruction after main reading of complete C709 and fresh isolated whole R930. The exact full original counts at times4,5,6 give a negative Gram determinant at every positive exponential scale, excluding the precise positive-real-measure, bounded-selfadjoint and reversible-return representations. The exact relative-error minimum and its two-atom probability are checked for every scale, including the true critical Doob specialization with no mean assumption. This is a finite-time obstruction only; eventual asymptotic models, the actual critical mean and unrestricted Task remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire temporal obstruction](#statement) | TM1--TM10, every lambda>0, all positive finite real measures with finite sixth moment, bounded selfadjoint and reversible scopes, sharp probability control and precise original/critical limitations. |
| argument | [Complete finite proof and consumers](#complete-argument) | Sections1--4, exact original counts, negative temporal Gram/square, optimal relative tolerance and full probability verification, actual Doob telescoping and bounded reversible realization argument. |
| dependency | [Original six-digit count](Yin_C_G0445_v1.md#quartic-center-versus-lower-row-control) | Actual full coefficient feasibility and original weighted p6=9/512; its statement also gives p_N=2^-N for N<=degree(P). No new experiment or coupled-rate theorem is claimed. |
| dependency | [Original five-digit count](Yin_C_G0300_v1.md#quartic-uniform-positive-covariance) | The exact legal returned words0,+P,-P and p5=17/512 under the original digit law. |
| dependency | [Actual critical Doob interface](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Full original core and law, true-R recurrence/range, positive H and exact Q construction; no mean branch or R=beta assertion. |
| dependency | [Exact Doob telescoping](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | Formula9 at every chronological time; its finite-mean limits are not used. |
| support | [Distinct original operator nonnormality](Yin_C_G0203_v1.md#statement) | Existing full-strip norm/nonnormality only, distinguished from the new impossibility of a different scalar selfadjoint moment realization. |
| support | [Spatial positive-definite account](Yin_C_G0563_v1.md#occupation-fourier-fixed-scope) | Existing whole-order spatial correlation and critical occupation positivity; no temporal positive moment assertion is imported. |
| support | [Source and reuse boundary](#source-and-reuse-boundary) | Existing exact counts, new finite deductions, no new source/native work, and the retained actual critical-mean and asymptotic limitations. |
| review | [Fresh independent whole temporal moment finding](../audits/reviews/Yin_R_G0930_v1.md#whole-temporal-moment-finding) | Entire TM1--TM10 statement and proof, original counts and domains, all positive scales, sharp probability attainment, actual true-R and reversible interfaces, and every finite-time/asymptotic limitation. |

