---
author: Yin
---

# Analytic damping and a uniform gap for reciprocal cyclotomic three-block measures

This project deduction concerns the three-block construction explored for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
The complete argument is retained here; the selected assessment below owns adoption at its exact scope.
The checks described in the contribution account are author-side development checks, not independent review or a claim of literature priority.

## Statement

Put

    gamma=(sqrt(5)-2)^2/50=(9-4sqrt(5))/50>0.

Use normalized Haar measure on the unit circle T and all tori.
For a nonzero Laurent polynomial, m denotes its total logarithmic Mahler measure, with no division by degree.
For g in L1(T), its Poisson integral at |z|<1 is

    P[g](z)=integral_T (1-|z|^2)/|zeta-z|^2 g(zeta) dmu(zeta).

### Analytic-majorant first-energy assertion

Let f be holomorphic on the open unit disk, with convergent Taylor series

    f(z)=sum_(j>=0)c_j z^j,       c_j in Z,       c_0=1.

Suppose g>=0 is integrable on T, epsilon=integral_T g, and

    log|f(z)|<=log2+P[g](z)       for every |z|<1,             (AM1)

where log0=-infinity is allowed.
If some finite coefficient prefix has square energy at least5, then

    epsilon>=gamma.                                         (AM2)

Equivalently, epsilon<gamma forces f to be an integer polynomial with total coefficient square energy at most4.
No boundary H2 hypothesis on f is required.

### Reciprocal cyclotomic three-block assertion

Let A0 and B0 be monic reciprocal products of cyclotomic polynomials with constant coefficient1 and even degrees 2a and 2b.
The empty product1 is allowed, multiplicities and degrees are unrestricted, and the factor x is not included in a cyclotomic product.
Set

    A(x)=x^(-a)A0(x),       B(x)=x^(-b)B0(x),
    F(x,y)=A(x)(y+y^(-1))-B(x),       f(z)=B0(z)/A0(z).

Define the real function

    phi(t)=0                       if |t|<=2,
    phi(t)=arcosh(|t|/2)           if |t|>2.

The logarithm of F is integrable on T^2, including its torus zeros, and

    epsilon:=m_2(F)=integral_T phi(B/A)>=0.                   (CG1)

The finitely many undefined quotient values on T are irrelevant to this integral.
The cost has a uniform alternative

    epsilon=0  or  epsilon>=gamma.                           (CG2)

Its zero cases are exactly

    B0=A0,
    or B0=A0(1+x^(2h)) for an integer h>=1.                  (CG3)

The constant in CG2 is not asserted to be optimal.

For each fixed pair A0,B0 and every integer N>max(0,b-a), the polynomial

    P_N(t)=t^(2N)A0(t)+A0(t)-t^(N+a-b)B0(t)                 (CG4)

is monic reciprocal and integral, has constant coefficient1 and actual degree2(N+a), and satisfies

    m(P_N)->m_2(F)       as N->infinity.                      (CG5)

For a fixed pair outside CG3, sufficiently large N therefore have m(P_N)>=gamma/2.
The delay cutoff may depend on the entire pair.
There is no effective or pair-uniform cutoff, no assertion of a positive lower bound for arbitrary varying-pair finite delays, and no reduction of an arbitrary original G0001 input to this family.

<a id="source-and-scope"></a>
## Sources, scope and contribution

The construction, integer-prefix exploration and complete original-degree return were developed in [L133 v3](../ledger/Yin_L_G0133_v3.md#three-block-integral).
[L133 v4](../ledger/Yin_L_G0133_v4.md#exact-fourier-escape) identified persistent boundary-log separation after local coefficient stabilization.
Those are provenance and comparison references here: all necessary Jensen, Poisson, short-polynomial and return arguments for the present statement are included below, rather than left in an unreviewed L proof body.

[BM05 U001](../audits/literature/BM05/Yin_U001.md#source-quadratic-families) records the reciprocal quadratic Jensen mechanism in the inspected journal edition, Section2 formulas (2-2),(2-5) and Section3 formulas (3-1),(3-2).
Its [finite-cover comparison](../audits/literature/BM05/Yin_U001.md#finite-cover-and-exact-control) identifies actual source subfamilies within the present construction.
This is an established source mechanism, not a new cyclotomic quadratic family claimed here.
The recorded [scope boundary](../audits/literature/BM05/Yin_U001.md#numerical-scope-and-prefix-boundary) does not supply the unrestricted-pair gap CG2.
No additional BM05 source-proof audit, numerical reproduction or literature-priority claim is made.

[C224](Yin_C_G0224_v1.md#statement) treats specific alternating kernels, exact restricted bounds and their joint Lawton reductions.
The unrestricted cyclotomic pair and analytic-majorant assertion here are a different core result, not a replacement for those restricted exact conclusions.
The local positive Poisson and coefficient-norm mechanisms already occur in [C10 v2](Yin_C_G0010_v2.md#argument) and [C296](Yin_C_G0296_v1.md#endpoint-row-hardy-closure).
The needed particular calculations are supplied completely here.

Only CG5 uses an accepted external theorem: the full fixed-Laurent-polynomial Lawton statement, including torus zeros, recorded for Theorem14 and Example15 of arXiv:0905.0604v1 in [Den09 U002](../audits/literature/Den09/Yin_U002.md#den09-u002).
Its original proof is not newly audited.
The uniform gap CG2 itself does not use Lawton, Smyth's theorem or a boundary-compactness assumption.

The coordinating agent proposed the three-block object and earlier prefix calculation, and then the first-crossing strengthening that removes every frequency and degree cost.
The assigned three_block agent introduced the analytic exponential damping in the preceding finite-prefix test, checked the first-crossing argument and completed this proof.
The global_synthesis agent made a further rapid development check of the truncation and short-polynomial steps.
These checks are contributions to the argument and are not independent mathematical review.

<a id="argument"></a>
## Complete argument

<a id="analytic-damping"></a>
### 1. Analytic damping from a nonnegative majorant

Assume AM1 and define, for |z|<1,

    H(z)=integral_T (zeta+z)/(zeta-z) g(zeta) dmu(zeta),
    q(z)=exp(-H(z)),       b(z)=f(z)q(z).

The kernel has a uniformly convergent power series on each compact subdisk, so H is analytic there and hence throughout the disk.
Its real part is P[g](z), because

    Re((zeta+z)/(zeta-z))=(1-|z|^2)/|zeta-z|^2
    for |zeta|=1.

Thus Re H>=0 and H(0)=epsilon.
It follows that

    |q(z)|<=1,       q(0)=exp(-epsilon),       |b(z)|<=2.     (1)

The last inequality follows directly from AM1, including any zeros of f.
Neither a boundary value of q at every point nor an H2 boundary value for f has been assumed.

For an analytic function u(z)=sum u_j z^j, define ||u||_H2^2=sum |u_j|^2, allowing infinity.
On each circle of radius r<1, the Taylor series and circle orthogonality give

    integral_T |u(rzeta)|^2 dmu=sum_(j>=0)|u_j|^2 r^(2j).

Letting r increase to1 in the nonnegative sum proves from (1) that

    ||q||_H2<=1,       ||b||_H2<=2.

Since q(0)=exp(-epsilon) is real,

    ||1-q||_H2^2
      =1+||q||_H2^2-2exp(-epsilon)
      <=2(1-exp(-epsilon))<=2epsilon.                       (2)

These are coefficient-norm statements obtained from interior circles, so possible boundary poles of the original f cause no difficulty.
For a finite polynomial P with coefficient absolute sum L(P), the same radial-circle calculation gives

    ||P(1-q)||_H2<=L(P)||1-q||_H2.                           (3)

Indeed |P(rzeta)|<=L(P) for every r<=1, and both sides pass to their coefficient-norm limits.
This proves all multiplier estimates used below without a boundary factorization theorem.

<a id="first-energy-crossing"></a>
### 2. The first integral energy crossing

Suppose a coefficient prefix has square energy at least5, and let N be the least such index.
Write

    s=sum_(j<N)c_j^2,       c=|c_N|,       P=S_N f,
    S_N u=sum_(j=0)^N u_j z^j.

Then N>=1, 1<=s<=4, c>=1 and s+c^2>=5.
Every nonzero coefficient before N has absolute value1: a coefficient of absolute value at least2, together with c_0=1, would already have crossed energy5.
Therefore

    ||P||_H2=sqrt(s+c^2),       L(P)=s+c.                    (4)

Since f-P vanishes to order at least N+1 and q is analytic,

    S_N b=S_N(Pq),       P-S_N b=S_N(P(1-q)).                (5)

These are exact finite Taylor identities.
In particular they do not require f, its full tail or the product of that tail with q to belong to H2.

The operator S_N is an orthogonal coordinate truncation in H2 and hence is contractive there.
It is used only on b and P(1-q), which are in H2 by (1)-(3).
Consequently (2)-(5) give

    sqrt(s+c^2)
      <=||S_N b||_H2+||S_N(P(1-q))||_H2
      <=2+(s+c)sqrt(2epsilon).                             (6)

It remains to check an entirely finite integer minimization:

    (sqrt(s+c^2)-2)/(s+c)>=(sqrt(5)-2)/5
    for 1<=s<=4, c>=1, s+c^2>=5.                           (7)

If c=1, necessarily s=4 and equality holds.
If c=2 and s=1, the ratio is (sqrt(5)-2)/3.
If c=2 and 2<=s<=4, it is at least (sqrt(6)-2)/6>1/15.
If c>=3, it is at least (c-2)/(c+4)>=1/7.
Finally (sqrt(5)-2)/5<1/20, since sqrt(5)<9/4, so every stated lower comparison proves (7).
Combining (6)-(7) gives epsilon>=gamma, proving AM2.

If no such N exists, the infinite coefficient square sum is at most4.
Integer coefficients then leave only finitely many nonzero terms, so f is a polynomial of that energy.
This proves the equivalent form of the analytic-majorant assertion.

<a id="quadratic-cost-integrability"></a>
### 3. The complete quadratic Jensen cost

Now impose the cyclotomic hypotheses in the statement.
Reciprocity and real coefficients imply that A and B are real on T.
Since A0(0)=B0(0)=1, the quotient f is analytic and nonzero in the open disk and has Taylor coefficients in Z with c_0=1.
The integrality follows recursively from A0 f=B0 and the constant coefficient1 of A0.

For a point x away from the finitely many zeros of A0 on T, put t=B(x)/A(x).
Then t is real, |t|=|f(x)|, and

    F(x,y)=A(x)y^(-1)(y^2-t y+1).

The two roots of the quadratic have product1.
For |t|<=2 both lie on T, while for |t|>2 their larger modulus is exp(phi(t)).
Its y-circle logarithmic mean is therefore phi(t).

Here is the absolute-integrability justification for the iterated logarithm.
For any complex lambda, |y-lambda| on T is max(1,|lambda|) times a rotated factor |1-r y| or |1-r y^(-1)| with 0<=r<=1.
The logarithm of each normalized factor has mean0, positive part at most log2 and L1 norm at most2log2.
For r<1 the mean follows from the absolutely convergent logarithm series, and r=1 follows by the radial L1 estimate in the next subsection.
Applying this to the two quadratic roots gives

    integral_T |log|y^2-t y+1|| dmu(y)<=phi(t)+4log2.

Also

    phi(t)<=log^+|t|<=log^+|B0(x)|+log^-|A0(x)|.

The right side is integrable: the finitely many logarithmic root singularities of A0 and B0 are integrable on T.
The same is true of log|A(x)|.
Thus log|F| is absolutely integrable on T^2, with its exceptional fibers forming a null set.
Fubini gives

    m_2(F)=integral_T log|A|+integral_T phi(B/A)
          =integral_T phi(B/A),

since every cyclotomic factor has logarithmic measure0.
This proves CG1, including common roots, repeated factors, poles of the quotient and zeros of F on the torus.

<a id="boundary-log-poisson"></a>
### 4. The exact Poisson majorant for the cyclotomic quotient

A polynomial with constant coefficient1 and all roots on T has a factorization into factors 1-zeta^(-1)z, with multiplicity.
Consequently log|f| on T is a finite signed sum of the boundary functions log|1-zeta^(-1)x|.

For one such factor, replace x by rho x with rho<1.
The logarithm series is then absolutely convergent, and convolution with the positive Poisson kernel multiplies its kth Fourier mode by r^|k|.
As rho increases to1 the boundary logarithms converge in L1.
Their positive parts are bounded by log2.
After rotation of the one singular point, their negative parts are dominated by a constant plus |log|theta||: for rho>=1/2 and |theta|<=pi,

    |1-rho exp(i theta)|>=sqrt(2)|theta|/pi.

This follows by squaring and using 1-cos(theta)>=2theta^2/pi^2.
Dominated convergence therefore proves the L1 assertion.
The bounded Poisson kernel at any fixed interior point passes through that limit, giving exactly the harmonic value log|1-zeta^(-1)z|.
The finite signed sum proves

    log|f(z)|=P[log|f||_T](z).                              (8)

Off the exceptional boundary set, |f|=|B/A| and

    log|f|<=log2+phi(B/A).                                  (9)

For |B/A|<=2 this is immediate.
Otherwise |B/A|=2cosh(phi(B/A))<=2exp(phi(B/A)).
The Poisson kernel is positive and has normalized mass1, so (8)-(9) prove AM1 with g=phi(B/A) and epsilon=m_2(F).
All hypotheses of the analytic-majorant assertion now hold.

<a id="short-polynomial-completion"></a>
### 5. Complete treatment below the first energy crossing

If epsilon<gamma, AM2 forces f to be a polynomial with total coefficient square energy at most4.
Because A0 f=B0, that polynomial is monic, has constant coefficient1 and even degree, and is reciprocal.
For the reciprocity statement, take reversals in the polynomial identity and cancel the nonzero reciprocal factor A0.
These facts are obtained after polynomiality, not by an unsupported boundary limit.
All its remaining roots are cyclotomic as well.

Energy1 gives f=1.
Energy2 gives f=1+z^(2h), with h>=1.
If the energy is3, monicity and reciprocity force

    f=1+sigma z^h+z^(2h),       sigma in {1,-1}, h>=1.

Its modulus on T is |2cos(h theta)+sigma|.
The set sigma cos(h theta)>=sqrt(3)/2 has normalized measure1/6, and on it |f|>=1+sqrt(3)>5/2.
Since arcosh(5/4)=log2, CG1 gives

    epsilon>=log2/6.                                       (10)

For energy4, all four nonzero coefficients have absolute value1.
Put X=|f|^2-4 on T.
Then E X=0 and -4<=X<=12, because |f|<=4.
The two extreme nonconstant Fourier coefficients of |f|^2 have modulus1, from its constant and leading coefficients.
Circle orthogonality therefore gives E X^2>=2.
Writing X_+=max(X,0) and X_-=max(-X,0), one has E X_+=E X_- and

    2<=E X^2<=12 E X_++4 E X_-=16 E X_+.

On X>0, |f|=|B/A|>2 and

    phi(B/A)>=log(|f|/2)
             =(1/2)log(1+X/4)>=X/32.

The last step uses log(1+u)>=u/(1+u) and 0<u<=3.
Integration in CG1 proves

    epsilon>=1/256.                                        (11)

Both (10) and (11) exceed gamma.
Indeed sqrt(5)-2<1/4 gives gamma<1/800<1/256, while log2>1/2 gives log2/6>1/12.
Thus epsilon<gamma leaves only f=1 or f=1+z^(2h).

In the first case F=A y^(-1)(y^2-y+1).
In the second case B=A(x^h+x^(-h)) and

    F=A y^(-1)(y-x^h)(y-x^(-h)).

Both factorizations have logarithmic measure0, also directly from CG1.
This proves that epsilon<gamma implies epsilon=0, establishes CG2, and identifies precisely CG3.
Conversely the same factorizations prove that every input in CG3 has epsilon=0.
No degree, support-size or multiplicity bound was imposed on A0 or B0.

<a id="fixed-pair-specialization-return"></a>
### 6. Original-polynomial return and the boundary of the conclusion

For a fixed input pair and N>max(0,b-a), multiplication by the monomial t^(N+a) gives exactly

    t^(N+a)F(t,t^N)
      =t^(2N)A0(t)+A0(t)-t^(N+a-b)B0(t)=P_N(t).

The middle block begins at positive degree and ends below2(N+a).
The two A0 blocks are exchanged by reflection about degree N+a, while that reflection preserves the shifted B0 block.
It follows that P_N has all the properties in CG4, using the actual input degrees even when the blocks have common cyclotomic factors.
Monomial multiplication leaves its logarithmic measure unchanged.

For the fixed Laurent polynomial F, the least sup norm of a nonzero integer relation on (1,N) is N.
The accepted Lawton statement therefore gives CG5 for the complete polynomial, including all torus zeros.
For a fixed positive-cost pair the limit is at least gamma, so its sufficiently late specializations have measure at least gamma/2.
No rate or cutoff uniform over changing pairs follows from this use.

A pointwise assertion for every permitted finite N would already be false for positive-cost pairs.
For example A0=1+t^2 and B0=1 lies outside CG3, but N=1 gives P_N=t^4+t^2+1, a cyclotomic product of measure0.
Thus the theorem concerns the full two-variable cost and its fixed-pair limits, not every finite delay.

If positive costs epsilon_j tending to zero in this family existed, one could choose a separate sufficiently large N_j for each complete pair, above its actual degree threshold, with

    |m(P_(N_j))-epsilon_j|<epsilon_j/2.

This would give genuine integral reciprocal unit polynomials with positive measures tending to zero and degrees2(N_j+a_j).
CG2 rules out precisely that premise, so this counterexample construction by vanishing two-variable costs is closed.
It does not control sequences whose blocks and finite delays vary together without such a small two-variable cost.
No irreducibility, bound on a chosen noncyclotomic factor, or Task-specific all-power property is obtained from the construction.
In particular the result neither supplies a uniform bound for every original G0001 polynomial nor completes the unrestricted Task.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T18:10 |
| status | proved |
| reason | Adopt the complete analytic-majorant first-crossing assertion and reciprocal cyclotomic three-block gap after the independent whole-proof finding R1091. The positive cost is at least (sqrt(5)-2)^2/50 with no degree, frequency, support or multiplicity restriction on the stated family. The exact zero cases and fixed-pair Lawton return are included. No pair-uniform delay cutoff, arbitrary original-input reduction or unrestricted G0001 gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | AM1-AM2 and CG1-CG5, the exact zero classification, total-measure normalization and all stated domain and return limitations. |
| argument | [Complete proof](#argument) | All six sections: analytic damping, the exact first finite energy crossing, integrability and Poisson passage, complete short-polynomial cases and fixed-pair return. |
| dependency | [Lawton statement](../audits/literature/Den09/Yin_U002.md#den09-u002) | Only the accepted fixed-Laurent-polynomial Theorem14/Example15 interface of arXiv:0905.0604v1 for CG5, including torus zeros; no new audit of the original theorem proof. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_G1091_v1.md#whole-proof-finding) | Complete exact statement and argument, all local analytic and integer steps, source application and original-target boundary; no substantive repair supplied by the reviewer. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
