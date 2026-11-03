---
author: Yin
---
# Rational almost-positive Gram certificates and arithmetic precision

Date: 2026-10-14T19:50.
Human author Yin.
Continuing F0010-inspired inquiry under the resumed G0001 goal.

## Responsible question

C103 rules out positive rational Gram gain on irreducible circle-root inputs; the signed-trace analysis now retained in C107 identifies the exact costs of one particular all-place construction.
Investigate a genuinely different boundary: rational same-symbol Grams with a controlled negative part.
Can their coefficient denominator, size and negative tolerance be related to a meaningful objective gain, rather than simply requiring exact PSD?
Compare the actual existing rational correction and positivity materials first.
Seek an exact certificate/obstruction or a useful inverse statement; low negative rank, small negative eigenvalues and proximity to the same-symbol PSD fiber must remain distinct.
Every denominator, original degree and coefficient norm must be paid.
Do not assume that the signed trace construction exhausts rational indefinite Grams.

<a id="almost-positive-gram-reuse"></a>
## 1. Reuse, contribution and model distinctions

The f_unitary_scope AI authors every new argument and constant below.
Root supplied the question only.
The author previously authored C103 and C107, which are explicitly identified inputs/ancestry rather than independent review of this work.
No numerical or symbolic program, J or native mathematical run has occurred.

The author read [C34's rational interior and exact correction](Yin_C_G0034_v1.md#statement) and [PP08-U001](../audits/literature/PP08/Yin_U001.md#pp08-u001).
Strict feasibility is essential to their PSD rounding conclusion.
The rounding operation reused in Section4 is that SAME classical affine projection, credited without novelty, but its output here has a paid negative tolerance.
[C103](Yin_C_G0103_v1.md#statement) supplies the exact rational ceiling and actual quartic trace-field Gram; [C107](Yin_C_G0107_v1.md#argument) supplies the preceding signed-place algebra, whose needed two-place congruence is rederived below.
[C23](Yin_C_G0023_v1.md#statement) concerns a different rational-packet capacity and its degree/height convergence cost; its large-window theorem is not substituted for the finite coefficient-Gram problem.
[L10](../ledger/Yin_L_G0010_v1.md#general-reciprocal-necessary-bound) concerns a different orbit matrix and total negative spectrum, not the smallest eigenvalue of an arbitrary same-symbol coefficient Gram.

The finite Gram/Jensen comparison and optimizer come from [L_F5](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp); [L_F7's vector-Jensen proof](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) contains the elementary upper-bound mechanism used in Section3.
[L_F6](../ledger/Yin_L_F0006_v1.md#coefficient-optimizer-degeneration) treats fixed-input regularization rates, whose constants cannot be silently made uniform.
The new elementary sublevel estimate below instead pays its displayed degree exponent and does not assume root separation or coefficient height.
A bounded local search for almost-PSD, negative tolerance, rational correction and same-symbol distance found these interfaces and no retained version of the combined certificate/arithmetic bound below.
No novelty claim follows.

For the recognized quadratic-unit power method, the author directly text-read Keith Conrad, [Pell's Equation, I](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf), actual13-page online PDF: printed/PDF p.2 table's(649,180) entry for13 and p.5 Theorem4.1/Corollary4.2 on multiplication and powers.
This is classical method attribution.
The particular norm identity, recurrence, parity, denominator and approximation bounds used here are proved below; neither general Pell solvability, a fundamental-unit assertion nor a classification of all solutions is a premise.
No source bytes were acquired, canonical source record extended or complete source-proof audit performed.

## Statement

For a real polynomial p of degree d and an integer n>=d, let v_n=(1,z,...,z^n)^T, N=n+1, and let the SAME-SYMBOL condition mean v_n(z)^*Qv_n(z)=|p(z)|^2 for every |z|=1.
Q is a real symmetric matrix, and epsilon is an explicitly supplied nonnegative number with Q+epsilon I>=0.
The negative tolerance controls operator order; negative rank alone does not supply it.
All logarithms are natural and m(p)=log M(p) is the total scalar Mahler measure.

**A. A valid precision-corrected lower certificate.**
For EVERY monic real p of degree d>=1, every same-symbol Q at width n>=d, and epsilon>=0 with Q+epsilon I>=0 and Q00+epsilon>0,

    m(p)>= (1/2)log(Q00+epsilon)
                -3d^2 (N epsilon)^(1/(2d)).          (A)

Consequently, if Q00>=1+gamma with gamma>0 and

    epsilon<=N^-1[log(1+gamma)/(12d^2)]^(2d),          (B)

then m(p)>=log(1+gamma)/4.
Circle roots and repeated roots are allowed.
No coefficient-height or spectral-separation assumption occurs; the cost is the explicit degree-dependent precision requirement.
This is a sufficient certificate, not a statement that such data exist uniformly.

**B. Exact rational affine approximation, with all losses.**
If p is monic integral, let Q_* be the real PSD maximizing Gram at width n.
For each positive integer q there is an exactly same-symbol rational matrix Q_q with qQ_q integral and

    ||Q_q-Q_*||_op<=N(N+1)/(2q),
    (Q_q)00>=M(p)^2-(N-1)/(2q),
    Q_q+[N(N+1)/(2q)]I>=0.                           (C)

This is an existence/construction from the actual optimizer entries, not a coefficient-only efficient optimizer algorithm; q is a clearing denominator, not necessarily the least.
For irreducible circle-root unit inputs with M(p)>1, sufficiently large q gives genuine rational gain with strictly positive but arbitrarily small negative tolerance.
There is no denominator-free positive threshold making such matrices PSD.

**C. Original-root arithmetic precision floor.**
Suppose p is monic irreducible integral of degree d>=2 with p(0)=+/-1, and let c>=1 count ALL its circle roots.
Let H=sum_j p_j^2, Q be rational and same-symbol at width n>=d, q>=1 an integer with qQ integral, and epsilon>0 with Q+epsilon I>=0.
Put L=H+N epsilon.
If at least one integer row polynomial sum_j(qQij)z^j is NOT divisible by p, then

    1<=q^d N^(d/2) L^(d-c) exp(n m(p))
                   [sqrt((L+epsilon)epsilon)+epsilon]^c.    (D)

If additionally epsilon<=1/N, then

    epsilon >= [4(H+2) q^(2d/c) N^(d/c)
                    (H+1)^(2(d-c)/c) exp(2n m(p)/c)]^-1.   (E)

At ORIGINAL width n=d, Q00>1 forces the required nondivisible row.
At padded widths that inference is false, with the exact rank-two counterexample in Section6.
All d original roots, the full resultant, original width, coefficient norm and denominator are retained; (E) is a necessary condition, not a uniform gap.

**D. Fixed quartic with exact denominator, one negative eigenvalue and quadratic precision.**
For the actual p=z^4-z^3-z^2-z+1, there is an explicit sequence of same-symbol rational5-by-5 matrices R_k with actual LEAST common denominator q_k tending to infinity, uniformly bounded operator norm, objective(R_k)00>3/2 and inertia(4 positive,1 negative).
If epsilon_k=-lambda_min(R_k)>0, then

    c_-/q_k^2<=epsilon_k<=c_+/q_k^2,                  (F)

where the fixed positive algebraic constants c_-,c_+ are explicitly defined in Section7.
Their distance to the REAL same-symbol PSD set is O(q_k^-2), but their distance to the RATIONAL same-symbol PSD set is greater than1/2.
The example is a fixed positive-measure polynomial, not a varying near-one family or a counterexample to A.
Its rational tolerance can eventually meet(B), yielding a paid per-input certificate.

## Argument

<a id="monic-circle-sublevel-bound"></a>
## 2. Elementary monic sublevel estimate and uniform degree cost

Let mu be normalized circle arclength.
For every complex center a and radius r>=0,

    mu{z in T:|z-a|<=r}<=min(1,r).                   (1)

For0<r<1, if the set is nonempty choose one of its points z0.
Every other point has chord distance at most2r from z0, so its principal angular distance is at most2arcsin(r).
The resulting arc has normalized length at most2arcsin(r)/pi<=r; the last inequality follows from convexity of arcsin on[0,1] and its endpoint chord.
For r>=1 the bound by1 suffices; for r0 the set has at most one point and measure zero.

Write the monic degree-d polynomial as p(z)=product_(i=1)^d(z-alpha_i), counting repeated roots.
If |p(z)|<=u, at least one factor has modulus at most u^(1/d).
A union bound and(1) therefore give

    mu{|p|<=u}<=min(1,d u^(1/d)), u>=0.              (2)

For tau>0, use the nonnegative level-set integral to write

    E_p(tau):=integral_T log(1+tau/|p|^2) dmu
       =integral_0^infinity
           mu{|p|<sqrt(tau/(exp(v)-1))} dv.

Finitely many circle zeros have measure zero; this equality is justified by nonnegative integration and remains valid with their pointwise infinite values.
Put a=1/(2d).
By(2),

    E_p(tau)<=d tau^a integral_0^infinity(exp(v)-1)^(-a)dv
             <=6d^2 tau^(1/(2d)).                   (3)

Indeed on0<v<=1, exp(v)-1>=v and the integral is at most1/(1-a)<=2.
On v>=1, exp(v)-1>=exp(v)/2, and the integral is at most2^a exp(-a)/a<=2/a=4d.
Their sum is at most2+4d<=6d.
This proves(3), including logarithmic integrability, without a beta-integral formula or root-separation constant.
Set E_p(0)=0.
The bound is deliberately coarse and its exponent deteriorates with d.

<a id="almost-positive-lower-certificate"></a>
## 3. From an almost-positive exact symbol to a true lower certificate

Let B=Q+epsilon I>=0.
Its circle symbol is

    v_n^* B v_n=|p|^2+N epsilon.                    (4)

The factor N is compulsory: every monomial in v_n has unit modulus.
Factor B as a real coefficient Gram, giving an analytic vector polynomial F with ||F(z)||^2 equal to(4) and ||F(0)||^2=B00.
If B00>0, the scalar polynomial g(z)=<F(z),F(0)>/||F(0)|| has g(0)=sqrt(B00) and |g(z)|<=||F(z)||.
The elementary Jensen/root formula, the same upper-bound device as in F0010, gives

    log(B00)<=integral_T log(|p|^2+N epsilon)dmu
              =2m(p)+E_p(N epsilon).                (5)

For epsilon0 this is the ordinary exact Gram bound, with circle zeros handled by logarithmic integrability.
For epsilon>0 the symbol is strictly positive.
The real factorization of the finite matrix is only an analytic proof device, not an arithmetic norm of irrational coefficients.

Combining(3)--(5) proves(A).
If Q00>=1+gamma and(B) holds, the error term3d^2(N epsilon)^(1/(2d)) is at most log(1+gamma)/4, whereas the first term is at least log(1+gamma)/2.
This proves the stated positive lower bound.
Merely printing a floating-point eigenvalue or an approximate symbol is not the hypothesis: both the lag equations and Q+epsilon I>=0 must be actually certified at the supplied tolerance.
An exact rational LDL or another proved matrix inequality may supply the latter when Q,epsilon are rational.

This procedure does not simply call a signed matrix a lower certificate.
It first obtains an upper regularized capacity, then subtracts the complete proven regularization error to recover a lower bound for the ORIGINAL p.
The particular distinction is why an unpriced negative tolerance would be invalid.

<a id="rational-affine-rounding-cost"></a>
## 4. Rational approximation exists, but its negative error is not free

Let p be integral and Q_* a real PSD maximizing Gram of |p|^2 at width n; its existence and value(Q_*)00=M(p)^2 are F0010 inputs.
Round each independent entry to a multiple of1/q, symmetrically, to form Y with entrywise error at most1/(2q).
Its lag residuals

    e_k=c_k-sum_(i=0)^(n-k)Y_(i,i+k)

lie in q^-1 Z because every exact autocorrelation c_k is integral.
Put the correction e0 at(0,0), and e_k at both(0,k),(k,0) for k>=1.
Call the resulting matrix Q_q.
This is exactly C34's one-entry-per-lag affine right inverse, used without a strict positivity claim.
It restores ALL lag coefficients, including padded zero lags, and keeps qQ_q integral.

The residual satisfies |e_k|<=N/(2q).
Thus every entry of Q_q-Q_* has modulus at most(N+1)/(2q), and its operator norm is at most N(N+1)/(2q), proving the first and third inequalities in(C).
For the objective there is a sharper direct cancellation:

    (Q_q)00=c0-sum_(i=1)^n Y_ii,
    |(Q_q)00-(Q_*)00|<=(N-1)/(2q).                  (6)

This proves the second inequality.
No positive-definite interior is available at the intended circle-root input, and none is assumed.
If p is irreducible with a circle root and p(0)=+/-1, C103's rational ceiling shows that any such rounded matrix with objective>1 is genuinely indefinite.
For an individual p with M(p)>1, sufficiently large q makes that objective>1, and the paid tolerance tends to zero.
Thus no fixed positive negative-eigenvalue threshold independent of denominator can upgrade rational feasibility to PSD.

The rounding construction starts from actual real optimizer entries.
It proves existence with a q-grid and explicit losses, but does not provide a polynomial-time method, a solver tolerance guarantee or a new uniform objective gain.
This reuse of C34 is not the new arithmetic obstruction in the next section.

<a id="original-root-precision-floor"></a>
## 5. A field-norm floor for negative tolerance

Let p,Q,q,c,H,N be as in C.
The lag-zero equation gives trace(Q)=H.
If every eigenvalue of Q is at least-epsilon, each positive eigenvalue is at most H+(N-1)epsilon.
All eigenvalue magnitudes are therefore at most L=H+N epsilon, since H>=1 and N>=3.
Hence ||Q||<=L and ||Q+epsilon I||<=L+epsilon.

At a circle root zeta of p, ||v_n(zeta)||^2=N and the exact symbol gives v_n(zeta)^*Qv_n(zeta)=0.
Let B=Q+epsilon I>=0.
Its spectral decomposition gives ||Bv||^2<=||B||v^*Bv.
Consequently

    ||Qv_n(zeta)||
       <=sqrt(N)[sqrt((L+epsilon)epsilon)+epsilon].   (7)

Choose a row i whose integer polynomial f_i(z)=sum_j(qQij)z^j is not divisible by p.
Irreducibility and monicity imply that f_i(alpha) is a NONZERO algebraic integer in the ORIGINAL field Q(alpha), for any root alpha of p.
Its full d-conjugate norm is a nonzero integer, so its absolute value is at least1.
At each of the c circle roots, (7) bounds |f_i| by q times its right side.
At every other original root alpha_j, coefficient Cauchy--Schwarz gives

    |f_i(alpha_j)|<=q L sqrt(N) max(1,|alpha_j|)^n.

Multiplying all d bounds, and using product_j max(1,|alpha_j|)^n=exp(nm(p)), proves(D).
No subset norm, smaller powered field, discarded circle conjugate or irrational coefficient norm has been used.

If0<epsilon<=1/N, then L<=H+1 and

    sqrt((L+epsilon)epsilon)+epsilon
       <=2sqrt(H+2) sqrt(epsilon).

Substitute this and L<=H+1 into(D), then take the2/c power, obtaining exactly(E).
Equivalently(D) supplies an explicit necessary lower bound on q for any proposed precision; the displayed d,c,H,n factors cannot be suppressed.
For a Salem input c=d-2, the exponent2d/c approaches2 as d grows.
This bound is not claimed sharp for each fixed degree or family.

At original width n=d, if EVERY row polynomial were divisible by p, every row coefficient vector would be a scalar multiple of the original coefficient vector a.
Symmetry then forces Q=s aa^T, and its exact circle symbol forces s=1.
Hence Q00=p(0)^2=1.
Contraposition proves the row condition whenever Q00>1.
This argument uses the actual original width, not an arbitrary padded presentation.

For comparison, the generic integral characteristic-polynomial argument gives a weaker kind of bound without circle roots.
If r is the rank of qQ, the product of its r nonzero eigenvalues is a nonzero integer coefficient of its characteristic polynomial.
With ||Q||<=L, every nonzero eigenvalue magnitude of Q is at least1/(q^r L^(r-1)), and therefore any negative tolerance is at least1/(q^N L^(N-1)).
This records the elementary general spectral-separation shortcut; it does not replace the sharper original-root information in(D).

<a id="padding-and-rank-distinction"></a>
## 6. Padding and negative rank: exact controls and a failed implication

The nondivisible-row condition cannot be inferred from gain at padded width.
At width n=d+1 let a be the coefficients of p padded by one zero, and let Sa be the coefficient vector of zp.
For every rational theta>0,

    Q_theta=(1+theta)aa^T-theta(Sa)(Sa)^T             (8)

is rational and represents EXACTLY |p|^2.
Its objective is1+theta, all its rows are coefficient vectors of multiples of p, and a,Sa are independent.
It has inertia(1 positive,1 negative), with remaining zeros, and Q_theta>=-theta H I.
The row field norms in Section5 are all zero, so using their nonzero-integer floor would be invalid.
This is a precise reason the original-width guard in C is necessary; it does not contradict the conditional formula(D).

Low negative rank alone is also cheap at ORIGINAL width.
For rational theta>0 put

    Q=aa^T+theta E00-theta E11.                     (9)

The added diagonal terms have zero circle symbol.
Since d>=2, the vectors a,e0,e1 are independent; (9) has two positive and one negative eigenvalue, objective1+theta, and negative magnitude at most theta.
Thus even one negative direction does not make a raw objective a valid lower certificate.
In this easy construction the gain decreases with the tolerance.
Section7 gives the different, stronger control where gain stays fixed while tolerance tends to zero and the actual denominator is charged.

<a id="quadratic-precision-quartic-family"></a>
## 7. An exact quartic family with one negative eigenvalue and epsilon proportional to q^-2

Fix the ACTUAL polynomial p=z^4-z^3-z^2-z+1 from L8/C103, and let

    t_+=(1+sqrt(13))/2, t_-=(1-sqrt(13))/2,
    T(x)=x^2-x-3, Delta=t_+-t_-=sqrt(13).

For a formal real parameter x let C(z;x)=z^2+(x-1)z+1.
Form the5-by-5 polynomial matrix Gamma(x) from the coefficient outer products of C(z;x)(z-1)^2, C(z;x)(z-1), C(z;x), with weights1,2(x-2),(x-2)^2.
Every entry lies in Z[x].
Reduce each entry modulo the MONIC T to define the explicit INTEGER symmetric matrices A,B by

    Gamma(x) modulo T(x)=A+xB.                      (10)

This is a finite coefficient definition, not an executed symbolic calculation.
At x=t_+ or t_- it equals C103's corresponding actual conjugate Gram.
Both endpoints have the same symbol |p|^2, so subtracting their lag equations gives lag(B)=0 and lag(A)=the autocorrelations of p.
Thus

    R(x)=A+xB represents |p|^2 for EVERY real x,
    R(x)00=4-x.                                     (11)

The second identity follows from Gamma(t)00=(t-1)^2=4-t modulo T.
In particular B is nonzero, with B00=-1.

Define positive integers P_k,Q_k by the explicit powers

    P_k+Q_k sqrt(13)=(649+180sqrt(13))^k, k>=1.

Since649^2-13*180^2=1, direct multiplication proves

    P_k^2-13Q_k^2=1,
    P_(k+1)=649P_k+2340Q_k,
    Q_(k+1)=180P_k+649Q_k.                           (12)

Induction gives P_k odd, Q_k even and positive, with Q_k tending to infinity.
Any common divisor of P_k,Q_k would have square dividing1, so they are coprime.
Put

    x_k=(1+P_k/Q_k)/2,
    q_k=2Q_k,
    R_k=R(x_k).

Then

    t_+<x_k<5/2<3,
    (R_k)00=4-x_k>3/2,
    x_k-t_+=2/[q_k^2(P_k/Q_k+sqrt(13))].             (13)

Indeed sqrt(13)<P_k/Q_k<=sqrt(14)<4.
The objective has numerator7Q_k-P_k over2Q_k, with that numerator odd and coprime to Q_k.
Therefore its reduced denominator is EXACTLY q_k.
All entries of R_k have denominators dividing q_k by(10), so q_k is the actual least COMMON matrix denominator, not just a supplied clearing denominator.
The matrices have norm bounded by ||A||+(5/2)||B||.

### Exact negative rank

Let C_+,C_- be the two actual quadratic quotients and let U be the5-by-5 real coefficient matrix with columns p,C_+,zC_+,C_-,zC_-.
It is invertible by evaluating at the two pairs of distinct roots, as in C107; its nonzero determinant is not assumed to be1.
Put delta_+=t_+-2, delta_-=t_--2 and

    B_+=delta_+ [[t_+,-2],[-2,t_+]],
    B_-=delta_- [[t_-,-2],[-2,t_-]].

For t_+<x<3 set alpha=(x-t_-)/Delta>0, beta=(t_+-x)/Delta<0.
The interpolation identity R(x)=alpha Gamma(t_+)+beta Gamma(t_-) has alpha+beta=1.
Expanding its two three-column forms in the U basis gives top entry1, local blocks alpha B_+, beta B_-, and couplings alpha delta_+ and beta delta_- to the corresponding zC columns.
The invertible-block square completion has scalar

    1-alpha*t_+/(t_++2)-beta*t_-/(t_-+2)
       =2[alpha/(t_++2)+beta/(t_-+2)]
       =2(3-x)/3>0,                                (14)

because t_++t_-=1, t_+t_-=-3 and(t_++2)(t_-+2)=3.
The first local block is positive definite; the second has one positive and one negative eigenvalue.
Thus R(x) has exactly four positive and one negative eigenvalue on this entire open interval.
In particular the negative rank of every R_k is exactly one.

### Matching upper and lower magnitude bounds

Define the fixed nonzero real vector and positive constant

    y=U^(-T)(0,0,0,1,1)^T,
    c_*=2delta_-^2/[Delta ||y||^2]>0.                (15)

Its quadratic value on Gamma(t_+) is zero, while its value on Gamma(t_-) is2delta_-^2.
Consequently the Rayleigh quotient of R(x) at y is -c_*(x-t_+).
On the other hand Gamma(t_+) is PSD and R(x)=Gamma(t_+)+(x-t_+)B.
Thus the magnitude epsilon(x) of the unique negative eigenvalue obeys

    c_*(x-t_+)<=epsilon(x)<=||B||(x-t_+).            (16)

Using(13) and sqrt(13)<P_k/Q_k<=sqrt(14) proves(F) with the explicit fixed algebraic constants

    c_-=2c_*/[sqrt(14)+sqrt(13)],
    c_+=||B||/sqrt(13).                              (17)

These are positive and finite; B00=-1 ensures the upper constant is nonzero.
They depend on this FIXED actual input, not on k or a hypothetical near-one class.
For a rational certified tolerance one may use epsilon=C_B/q_k^2, where C_B=sum_(i,j)|B_ij| is a positive INTEGER.
Since C_B>=||B||>||B||/sqrt(13), equation(16) proves R_k+epsilon I>=0 exactly.

### Which feasible set is close

The real same-symbol PSD Gram Gamma(t_+) satisfies ||R_k-Gamma(t_+)||<=c_+/q_k^2.
Hence the distance to that real feasible set tends to zero at this rate.
C103's minimal-width rational singleton theorem says its rational PSD feasible set consists ONLY of aa^T for the original coefficient vector a.
Therefore

    ||R_k-aa^T||>=|(R_k)00-1|>1/2.                  (18)

Small negative eigenvalue and proximity to a REAL feasible point do not imply proximity to an exact RATIONAL feasible point.
This does not conflict with C107's different signed-trace construction, whose distance to the REAL feasible set was bounded below in a different regime.

For this fixed quartic, choose k large enough that C_B/q_k^2 meets(B) with d4,N5,gamma1/2.
Then A supplies the actual bound m(p)>=log(3/2)/4.
Such a finite k exists by(12); no numerical k or program execution is claimed.
This is a valid per-input almost-positive rational certificate with its actual denominator and precision cost.
It does not change the original polynomial or provide a near-one counterfamily.

<a id="almost-positive-outcome-and-limits"></a>
## 8. What is genuinely available and what remains missing

The exact rational PSD ceiling does NOT mean that fixed objective gain forces a fixed amount of negativity: Section4 permits arbitrary small negative tolerance for each input with a real capacity gain, and the quartic family gives an explicit bounded-norm, negative-rank-one realization with actual epsilon proportional to q^-2.
Conversely small negativity is not free evidence of a Mahler lower bound; A gives a valid correction and the exact degree-dependent precision sufficient for a positive margin.
The root-norm floor C records how coefficient denominator, original width, coefficient norm and every circle/off-circle embedding constrain that precision when a nonzero row resultant is available.

The reusable rational projection is credited to C34/PP08, not repackaged as a new interior theorem.
The new outcomes are its quantitative almost-positive boundary combined with a true regularization-corrected certificate, the original-field precision obstruction, and the explicit exact-denominator family separating negative rank, tolerance and the two feasible-set distances.
The padded all-divisible control prevents an invalid extension of the row resultant argument.

For an unrestricted G0001 advance one would need a family of ACTUAL certificates with a degree-independent positive gamma and a proved feasible negative tolerance meeting(B), while paying every construction/denominator cost, or a sharper valid error mechanism that changes that requirement.
No such universal family is supplied.
The existing arithmetic root-income route remains separate.
No source-level estimate, numerical PSD test or assumption of near-one input existence fills this remaining gap.

<a id="almost-positive-author-freeze"></a>
## Author freeze for independent whole review

Frozen by the f_unitary_scope author at2026-10-14T20:04 after a full self-check of StatementA--D, Sections1--8 and equations(1)--(18).
The checked scope includes the complete monic sublevel/Jensen argument with its factorN, the credited affine rounding loss, the original-field row resultant and padded exception, and the quartic power recurrence, actual least denominator, congruence inertia and both feasible-set distances.
The structural material check passed.
No mathematical program or new numerical run was used.
This is an author freeze, not an independent review or an adopted Claim decision; the source/reuse and contribution boundaries in Section1 remain part of the full original.

## Fixed organization

The entire author-frozen original above is retained, including the uniform paid certificate, rational approximation, exact original-root precision floor and padding boundary, quartic control, source attribution and all limits.
This actual artifact awaits independent whole review; no native mathematical computation is asserted.

## Current assessment

[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:05 |
| status | open |
| reason | Retain the complete almost-positive same-symbol Gram analysis for separate whole review. All degree, coefficient, denominator, width and negative-tolerance costs remain explicit; no uniformly available gap certificate or near-one exclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D with each real/integer/irreducibility/circle-root and width guard. |
| argument | [Entire argument](#argument) | Complete sublevel/Jensen proof, exact rounding, all-root arithmetic bound, padding counterexample and quartic sequence. |
| dependency | [Rational correction](Yin_C_G0034_v1.md#statement) | Existing affine rounding/projection mechanism, used with a paid negative tolerance here. |
| dependency | [Rational ceiling and Salem family](Yin_C_G0103_v1.md#statement) | Actual original-width rational PSD ceiling and explicit quartic coefficient-Gram family. |
| dependency | [Signed-place algebra](Yin_C_G0107_v1.md#argument) | Actual two-place congruence and coefficient-field distinctions, rederived at the new parameter. |
| dependency | [Scalar Gram maximum](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Real optimizer and exact same-symbol capacity at actual finite width. |
| dependency | [Vector Jensen mechanism](../ledger/Yin_L_F0007_v1.md#matrix-finite-gram-capacity) | Existing elementary vector/scalar Jensen upper-bound device; local finite proof given here. |
