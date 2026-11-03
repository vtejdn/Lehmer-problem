---
author: Yin
---

# A paid finite-precision certificate for exact canonical residual vanishing

Human author Yin.
The characteristic_zero_bridge agent authored the deduction below under the active [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Provenance: project deduction from the accepted original-domain inputs identified below.
Root read the complete candidate and supplied the direct monotonicity and exact-precision clarifications retained below.
Both agents are contributors; this is author work awaiting fresh isolated whole review.
The fixed-input circle bound and its maximum-principle mechanism are credited directly to [C151, Sections2--3](Yin_C_G0151_v1.md#argument), adopted at [its whole-reviewed decision](Yin_C_G0151_v1.md#decision-whole-reviewed-2026-10-15).
The present specialization combines that existing estimate with the actual dyadic coefficient divisibility and the reciprocal trace phase; it does not claim a new circle-supremum theorem.
The exact phase and trace-field degree are the adopted [C153v2 interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
No native mathematical computation, parameter scan, new literature acquisition or uninspected external theorem is used.
Registration fixes the complete PC1--PC14 argument at its explicit open assessment; it supplies no independent review or strategy adoption.

<a id="paid-characteristic-zero-certificate"></a>
## Statement

Let P in Z[z] be monic, irreducible, reciprocal and nontorsion, with constant coefficient1 and full degree N=2D>=2.
Write

    P(z)=z^D T(z+z^(-1)),
    m=log M(P)>0,
    S=max_(|z|=1)|P(z)|.

The actual monic irreducible trace polynomial T has degree D.
No total-reality or Salem hypothesis is imposed.
Use C_0=2, C_1=X and C_(j+1)=X C_j-C_(j-1), so C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X.
Use the SAME actual canonical integer polynomials

    a=rem_T(T(C2))/2,
    b=rem_T(T(C3))/3, c=rem_T(T(C5))/5,
    F=rem_T(2c^2-3a^5),
    X_s=rem_T(b^2-a^3+s(c^3-2b^5)),
    G=rem_T(c^3-2b^5), s in{1,-1}.

The exact integer divisions and all remainders use this one T.
Put

    A_F(S)=2S^2/25+3S^5/32,
    A_X(S)=S^2/9+S^3/8+S^3/125+2S^5/243.          (PC1)

For any integers n_F,n_X>=0, the following separate implications hold:

    F in 2^(n_F) Z[X], F!=0
        => n_F log2 <= log A_F(S)+10m;
    X_s in 2^(n_X) Z[X], X_s!=0
        => n_X log2 <= log A_X(S)+15m.             (PC2)

Consequently divisibility together with the strict reverse inequality forces the corresponding canonical polynomial to be IDENTICALLY zero in characteristic zero.
In particular both exact identities hold if both are divisible by2^n for an integer n>=0 and

    n log2 > max{log A_F(S)+10m,
                  log A_X(S)+15m}.               (PC3)

This tests the actual finite input; it does not require a limiting compatible sequence of coefficient classes.
The sufficient threshold is not asserted necessary, optimal or satisfied by a currently constructed input.

For a fully numerical degree/measure version put

    kappa=61319/243000,
    U(N,m)=m+(9/2)sqrt(N)+(log N)/(2sqrt(N))
           +sqrt(N(2log N+7)(2m+log N+4)), N>=8.  (PC4)

The accepted C151 bound gives log S<=U(N,m).
Thus either nonzero residual under simultaneous2^n divisibility necessarily obeys

    n log2 <= 5U(N,m)+15m+log kappa, N>=8.         (PC5)

The strict reverse inequality forces BOTH exact identities.
For a specified upper bound m<=M0, substitute U(N,M0) and M0 on the right; every displayed term is increasing in the nonnegative measure argument.
For all N>=2 there is also the elementary version

    n log2 > 5N log2+20m+log kappa                 (PC6)

as a sufficient condition for both exact identities.
One convenient sharper integer specialization, valid for every N>=2, is

    0<m<=log2, n>=5N+14,
    F=X_s=0 modulo2^n
        => F=X_s=0 in Z[X].                       (PC7)

The full reciprocal degree N, rather than D or a powered own-field degree, occurs in PC4--PC7.
At fixed measure bound, PC5 is a threshold of order sqrt(N)log N.
Every nonexact irreducible reciprocal lift at bounded total measure therefore has a precise upper bound on its residual precision in terms of its complete original degree.
A sequence with both residuals divisible by2^(n_j), uniformly bounded m(P_j), and n_j/(sqrt(N_j)log N_j) tending to infinity must have both residuals exactly zero for all sufficiently large j when N_j tends to infinity.
Existence of such a sequence is not asserted.

<a id="complete-trace-norm-proof"></a>
## Complete argument

### Reciprocal trace and norm calculation

Choose one root alpha_i from each reciprocal pair of roots of P, with |alpha_i|>=1, and put delta_i=alpha_i+alpha_i^(-1), 1<=i<=D.
These are exactly the D distinct roots of T, with every trace embedding counted once.
This choice is valid for arbitrary complex reciprocal roots; a unit-circle pair has equal modulus1 and either choice is allowed.
Set ell_i=log|alpha_i|>=0.
The complete root definition of Mahler measure gives

    sum_(i=1)^D ell_i=m.                           (PC8)

No real embedding or positive-value assumption is used.
For any polynomial of degree N, the maximum principle in the unit disk, followed outside the disk by its degree-N reversed polynomial, gives

    |P(z)|<=S max{1,|z|^N}.

This is exactly the mechanism already proved in C151 Section3.
At the actual pair representative, the trace identity and commuting trace powers give

    |T(Cp(delta_i))|
      =|alpha_i|^(-pD)|P(alpha_i^p)|
      <=S exp(pD ell_i), p in{2,3,5}.             (PC9)

The same-value canonical remainders have these values divided by p.
Consequently

    |F(delta_i)|
      <=[2S^2/25+3S^5/32] exp(10D ell_i),
    |X_s(delta_i)|
      <=(S^2/9+S^3/8)exp(6D ell_i)
          +(S^3/125+2S^5/243)exp(15D ell_i)
      <=A_X(S)exp(15D ell_i).                    (PC10)

The last inequality uses ell_i>=0; it is valid for both separately fixed signs.
Multiplication over ALL D trace embeddings, with PC8, proves

    |Norm_(Q(delta)/Q) F(delta)|
          <=A_F(S)^D exp(10D m),
    |Norm_(Q(delta)/Q) X_s(delta)|
          <=A_X(S)^D exp(15D m).                 (PC11)

Both bounds remain valid with a zero norm.
They involve the full trace-field norm of degree D, not a smaller field generated by a residual value.

Each canonical polynomial has degree below D.
Since T is the minimal polynomial of delta, a nonzero such polynomial evaluates to a nonzero element of Q(delta).
If F is coefficientwise divisible by2^(n_F), then F(delta)=2^(n_F)u for an algebraic integer u in Z[delta].
When F!=0, the nonzero rational integer Norm(u) has absolute value at least1, whence

    |Norm F(delta)|>=2^(n_F D).

The same argument applies to X_s.
Comparison with PC11, division by the ACTUAL D and logarithms prove PC2.
The argument only needs the corresponding value to belong to2^n O_(Q(delta)); actual coefficient divisibility is a sufficient premise that is already supplied by the finite constructions.
No identification Z[delta]=O_(Q(delta)) is required.
Irreducibility, rather than an unproved coefficient-height bound or finite numerical test, then turns the zero field element into the identically zero canonical polynomial.
This proves PC3.

### Fully paid degree thresholds

C151 Section2 supplies PC4 for N>=8, with the original monic irreducible nontorsion integer polynomial and full measure exactly as required here.
Its source and whole-review limits remain those of the adopted C151 input; no fresh source-proof audit is claimed.
Since S>=M(P)>1, elementary termwise comparison gives

    A_F(S)<=(139/800)S^5,
    A_X(S)<=kappa S^5,
    139/800<kappa,
    kappa=1/9+1/8+1/125+2/243.                     (PC12)

For m>=0, PC2 and PC12 yield the common right side5log S+15m+log kappa.
Substitution of PC4 proves PC5.
The elementary coefficient-free product bound

    S<=product_(P(alpha)=0)(1+|alpha|)
       <=2^N exp(m)

counts all N original roots and proves PC6.
For fixed M0 the displayed PC4 is O_(M0)(sqrt(N)log N); this is the claimed asymptotic scope and no constant is hidden when the explicit formula is used.
At fixed m>=0, U(N,m) is strictly increasing for real N>=8.
Indeed

    d/dN[(9/2)sqrt(N)+(log N)/(2sqrt(N))]
       =(9N+2-log N)/(4N^(3/2))>0.

The remaining radical in PC4 increases because each positive factor N, 2log N+7 and 2m+log N+4 increases there.
This justifies the degree comparison below without replacing the explicit upper bound by an asymptotic label.

For PC7, m<=log2 gives S<=2^(N+1).
The functions in PC1 are increasing for S>0.
Dividing the two exponentiated PC3 thresholds by2^(5N+14) gives respectively

    A_F(2^(N+1)) 2^10 /2^(5N+14)
       =3/16+(2/25)2^(-3N-2)<1,
    A_X(2^(N+1)) 2^15 /2^(5N+14)
       =128/243+(133/1000)2^(4-2N)
                         +(1/9)2^(3-3N)
       <=128/243+133/1000+1/72<1.                 (PC13)

The inequalities hold already at N=2 and become stronger for larger N.
They are strict, so the integer equality n=5N+14 is included in PC7.
The harmless fraction comparison in the second line is less than1 because128/243<8/15,133/1000<2/15 and1/72<1/60, whose sum is41/60<1.
Thus PC3 applies at the claimed integer precision.

<a id="actual-construction-comparison"></a>
## What this resolves for the current finite construction

The adopted [C716 actual simultaneous32 construction](Yin_C_G0716_v1.md#decision-whole-reviewed-2026-10-25) has final trace degree2d, hence reciprocal degree N=4d, with

    d=q(30m_src+degY), q>=131072,
    m_src=Q/4-2, Q>=2^82,
    precision n=5.

All full factors, original q, maximal2q, canonical degree gap and separate synthetic layer remain at C716's stated scope.
Its exact binary G is nonzero, so any integer lift preserving that binary polynomial has nonzero actual canonical G; no equality with the synthetic integer zero-Haar lift follows.
C716 itself supplies no irreducibility or measure bound, so it does not yet meet the entire PC domain.
Even if irreducibility and a bound m<=log2 were supplied without changing the degree, its n=5 would be far below both PC5's explicit sufficient threshold and PC7's5N+14 threshold.
Indeed U(N,m)>=(9/2)sqrt(N), so already the leading explicit term5U/log2 grows with the complete degree; increasing the original q while keeping n fixed makes this certificate less accessible.
The stated actual source costs give m_src>2^79, q>=2^17 and N>30*2^98>2^102.
Hence sqrt(N)>2^51.
Since log2<7/10 and kappa>1/4, the explicit common threshold in PC5 obeys

    [5U(N,m)+15m+log kappa]/log2
       >(225/7)2^51-2>2^56.                       (PC14)

Thus this existing supremum-based sufficient certificate requires an exponent above2^56 even at the smallest displayed original source costs, whereas C716 establishes exponent5.
This is the price of this particular certificate, not a lower bound on the precision required by every possible characteristic-zero argument.
This is a failure to meet a sufficient certificate, not a proof of nonexistence at that precision.

The [C711 Salem construction](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) can impose irreducibility and Salem root location in the same dyadic class, but pays its actual measure log beta.
Its explicit nonzero first residual is compatible with PC2 and PC5; this deduction concerns EVERY irreducible reciprocal lift and does not replace C711's stronger explicit sign estimate for its particular representatives.
For an actual dyadic k>=2, a pure pullback gives P_k(z)=P(z^k) and T_k=T(C_k), multiplying the full degree by k and preserving the full measure.
Every k-th-root fiber over one original root contributes its original log^+ modulus in total, so this measure assertion uses all Nk roots.
For each residual R in{F,X_s}, [C697's exact canonical covariance](Yin_C_G0697_v1.md#statement) gives R(T_k)=R(T)(C_k).
If the nonzero integer polynomial R(T) has exact coefficient2-adic order v, write R(T)=2^v H with Hbar!=0.
Modulo2 one has C_k=X^k, and the substitution Hbar(X)->Hbar(X^k) is injective in F_2[X], because distinct monomial degrees remain distinct.
Thus R(T_k) has EXACTLY the same finite coefficient2-adic order v, not merely at least that order; a zero residual stays zero.
Composition by the nonconstant C_k also preserves nonvanishing over Z.
If P_k remains irreducible, PC5 applies to it with the same m and exact precision but strictly larger U(kN,m) for N>=8.
Thus a pure pullback cannot improve PC5's explicit certificate, with neither precision gain nor degree normalization supplied for free.
If one new precision bit always costs a degree multiplier of at least2, then even a hypothetically bounded-measure iteration has n/(sqrt(N)log N) tending to0; the present certificate cannot certify an exact limit from that schedule.
This statement evaluates that specified schedule only; cheaper future corrections or exact vanishing at an earlier stage remain possible.

The concrete continuing target exposed here is an actual irreducible reciprocal input whose shared residual precision exceeds the explicit PC3 or PC5 threshold while its complete total measure is controlled.
That target can be checked at a finite stage and needs no appeal to an infinite2-adic limit.
It is not proved necessary for Lehmer's conjecture or for arbitrary exact residual solutions.
An exact residual solution alone also does not complete G0001: actual canonical G, its integer Haar data, full norm income and the original-root comparison keep their independent obligations.

## Local reuse and author checking limits

The local reuse pass inspected C711/C717's precise finite-lift and measure boundaries, C604's positivity/interlacing controls, C191v2's actual dyadic norm theorem, C201v2's Salem endpoint/tail theorem, and C646/C674's distinct five-adic questions.
These exclude relabelling an old positivity-only, degree-normalized or finite-gate argument as a new characteristic-zero bridge.
The decisive adequate input was C151's already adopted actual supremum/maximum-principle account, so no external literature search was needed for this deduction.
This is a direct original-domain application of existing norm and supremum mechanisms, with a new explicit finite-precision conclusion and the actual construction comparison; no global novelty assertion is made.
Author checking covered all reciprocal pairs in PC8, the canonical denominator powers, the two radial degrees, the full trace norm exponent, strict versus non-strict thresholds, both signs, nonmaximal trace orders, N=2 in PC13 and the lack of total-reality dependence.
Fresh isolated whole review and a subsequent mathematical acceptance decision remain outstanding.
The fixed registration preserves the entire author argument and its comparison boundaries; it does not import a review of this deduction from its accepted inputs.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision paid-precision-certificate-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T15:46 |
| status | open |
| reason | Register the complete PC1--PC14 finite-precision certificate and its original-construction comparison after contributor checking. The exact canonical trace norm lower bound is compared with the credited C151 supremum estimate at full reciprocal degree and total measure, including both signs, arbitrary complex trace fields, strict thresholds, the explicit 5N+14 specialization, actual C716 threshold expense and pure-pullback limitations. This is author-complete mathematics awaiting fresh isolated whole review; no current input passes the certificate, no characteristic-zero realization or unrestricted Task completion is asserted, and no independent review is claimed by registration. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire paid precision statement](#statement) | PC1--PC7, exact canonical integer domain, all individual and common precision quantifiers, arbitrary complex reciprocal roots, full degree N=2D, total measure, norm integrality, strict sufficient thresholds and bounded-measure asymptotic implication. |
| argument | [Complete norm and degree proof](#complete-argument) | PC8--PC13, all reciprocal pairs and trace embeddings, exact canonical denominators and radial powers, nonmaximal-order-safe norm lower bound, irreducible zero detection, credited supremum application, integer endpoint comparison and explicit U monotonicity. |
| argument | [Actual construction and pullback comparison](#actual-construction-comparison) | PC14 and the complete C716/C711/C697 comparison, all original q/source/full-degree costs, actual G versus synthetic G distinction, exact coefficient2-adic precision under pure pullback and its irreducibility scope, specified doubling-cost schedule and remaining original-realization obligations. These comparisons are not used to prove PC1--PC13. |
| dependency | [Adopted original circle bound](Yin_C_G0151_v1.md#decision-whole-reviewed-2026-10-15) | Sections2--3, explicit U(N,m) at N>=8 and the whole-circle maximum-principle polynomial estimate, with its accepted source and review limits; the new coefficient-divisibility/trace-norm conclusion is proved here. |
| dependency | [Adopted exact reciprocal trace interface](Yin_C_G0153_v2.md#decision-current-endpoint-proof-home) | Exact reciprocal phase, monic irreducible degree-D trace polynomial and degree-two original extension, actual canonical integral quotients and all embedding multiplicities; no total reality is imported into the present general domain. |
| support | [Adopted actual simultaneous32 construction](Yin_C_G0716_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: actual n=5, final trace degree2d and reciprocal degree4d, original q>=131072, full C724 source costs, nonzero binary canonical G and separate synthetic layer; no irreducibility or small-measure premise is inferred. |
| support | [Adopted exact canonical covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 supplies the exact integer F/X_s covariance only for the separate pure-pullback comparison; the new elementary injectivity check preserves exact2-adic coefficient order. It is not a premise of PC1--PC13. |
| support | [Adopted finite Salem lifts and tower](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: genuine Salem realization of a finite dyadic class, its complete positive full measure and particular nonzero first residual, with all tower degree and root-location limits. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T16:04 |
| status | proved |
| reason | Adopt the complete fixed PC1--PC14 deduction after reading the whole claim and fresh isolated whole review R941. The full trace norm, arbitrary complex reciprocal domain, exact canonical divisions, strict sufficient thresholds, N=2 integer endpoint, original-degree supremum cost and exact nonzero precision under pure pullback are supported at the recorded fixed-input and source limits. This is a sufficient certificate and a paid construction comparison, not a necessary precision bound, a currently passing controlled-measure input, an exact characteristic-zero realization or G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire paid precision statement](#statement) | PC1--PC7, exact canonical integer domain, all individual and common precision quantifiers, arbitrary complex reciprocal roots, full degree N=2D, total measure, norm integrality, strict sufficient thresholds and bounded-measure asymptotic implication. |
| argument | [Complete norm and degree proof](#complete-argument) | PC8--PC13, all reciprocal pairs and trace embeddings, exact canonical denominators and radial powers, nonmaximal-order-safe norm lower bound, irreducible zero detection, credited supremum application, integer endpoint comparison and explicit U monotonicity. |
| argument | [Actual construction and pullback comparison](#actual-construction-comparison) | PC14 and the complete C716/C711/C697 comparison, all original q/source/full-degree costs, actual G versus synthetic G distinction, exact coefficient2-adic precision under pure pullback and its irreducibility scope, specified doubling-cost schedule and remaining original-realization obligations. These comparisons are not used to prove PC1--PC13. |
| dependency | [Adopted original circle bound](Yin_C_G0151_v1.md#decision-whole-reviewed-2026-10-15) | Sections2--3, explicit U(N,m) at N>=8 and the whole-circle maximum-principle polynomial estimate, with its accepted source and review limits; the new coefficient-divisibility/trace-norm conclusion is proved here. |
| dependency | [Adopted exact reciprocal trace interface](Yin_C_G0153_v2.md#decision-current-endpoint-proof-home) | Exact reciprocal phase, monic irreducible degree-D trace polynomial and degree-two original extension, actual canonical integral quotients and all embedding multiplicities; no total reality is imported into the present general domain. |
| support | [Adopted actual simultaneous32 construction](Yin_C_G0716_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: actual n=5, final trace degree2d and reciprocal degree4d, original q>=131072, full C724 source costs, nonzero binary canonical G and separate synthetic layer; no irreducibility or small-measure premise is inferred. |
| support | [Adopted exact canonical covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 supplies the exact integer F/X_s covariance only for the separate pure-pullback comparison; the new elementary injectivity check preserves exact2-adic coefficient order. It is not a premise of PC1--PC13. |
| support | [Adopted finite Salem lifts and tower](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: genuine Salem realization of a finite dyadic class, its complete positive full measure and particular nonzero first residual, with all tower degree and root-location limits. |
| review | [Fresh isolated whole review](../audits/reviews/Yin_R_G0941_v1.md#whole-paid-precision-finding) | Independently reviewed entire fixed statement, complete argument and actual-construction comparison, exact initial selection and consumed fixed input interfaces, with accepted deeper proof and source limits retained. |

