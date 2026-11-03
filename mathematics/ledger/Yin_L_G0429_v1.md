---
author: Yin
---
# Static phase bands and a quantitative slow contact corridor

Current complete mathematical home: [exact current C](../claims/Yin_C_G0569_v2.md#statement), [full proof](../claims/Yin_C_G0569_v2.md#argument) and [actual current adoption](../claims/Yin_C_G0569_v2.md#decision-complete-current-self-adoption).
The current complete [R752 finding](../audits/reviews/Yin_R_G0752_v1.md#current-g430-complete-self-finding) is constructor SELF.
All original mathematics, source/native/contribution history and mathematical next questions below retain their original dated scope; the current entry does not rebind an old review or create independent evidence.

Date: 2026-10-18T17:59.
Human author Yin.
Root supplied the bounded question of an effective finite Fourier-mass lower bound for the existing C171 phase.
The angular_envelope_review agent authors the new rational-band and finite-support argument below.
No numerical Fourier integral, prime, width or coefficient scan is selected.
At fixation, this was author mathematics awaiting separate review and adoption.
The later [whole R442 review](../audits/reviews/Yin_R_G0442_v1.md#static-phase-whole-independent-finding) and [bounded strategy adoption](../strategies/Yin_S_G0001.md#static-phase-closeout-2026-10-20) retain the unchanged argument and its original limits.

<a id="static-phase-question"></a>
## Question and bounded reuse

Use only the fixed three-torus U of C171 and the accepted finite-band return theorem [L426](Yin_L_G0426_v1.md#moving-band-target).
The local search checked C171's essential noncontinuity and exact rational phase, C172's Fejer moment and L426's support-dependent error.
These provide no effective static l1 growth rate.
A broader term match for cusp/Besov returned unrelated arithmetic sources and supplies no applicable theorem or negative literature conclusion.
The direct rational calculation below is the selected mechanism; no new source theorem is assumed.
The geometric series, quotient differentiation and finite convolution calculations are given explicitly.
Classical Fejer attribution and the exact probability-Haar first-moment interface are reused from C171/C172, without a source-proof upgrade.

C171 exhibits both addition and cancellation of the two cotangent poles near z_0, u=v=1.
Those two paths establish essential noncontinuity but supply no finite partial-sum rate by themselves.
Therefore the proof does not infer a quantitative rate merely from two incompatible pointwise limits or an assumed jump across a hypersurface.
It instead resolves one variable into exact Fourier bands before taking a finite cutoff in the other two.

<a id="static-phase-statement"></a>
## 1. Exact finite coefficient statement

Keep C171's fixed K and exact U=Acal/Bcal off its common-zero set, with U=0 on that measure-zero set.
All Fourier coefficients use normalized Haar measure and exp(-i(p theta+q t+r s)).
Put

    theta_0=pi/K, delta=pi/(4K), C_0=10^4(K+1),
    C_1=2pi C_0+2pi/delta,
    R_0=ceil(max{3^18,(4C_1)^6,64}).                  (1)

For EVERY integer R>=R_0 set J=floor(R^(1/3)) and

    F_R={(p,q,-m): |p|,|q|<=R-1, 2<=m<=J}.

Then

    |F_R|<4 R^(7/3),
    sum_(gamma in F_R)|Uhat(gamma)|>=log R/24.        (2)

The set is explicit and finite, with every coordinate of magnitude at most R.
The constants depend only on the already fixed K, not on a new arithmetic input or a numerical choice.
The proof retains the cost of the entire rectangular set; it makes no sparsity or optimal-support claim.

As a consequence for the SAME actual L402 family, put M_j=floor(a_j/4) as in L426.
If

    tau_j->0, 0<tau_j<=1,
    tau_j (log M_j)^2 ->infinity,                     (3)

then the ACTUAL original2d_j kernel satisfies

    W_*(psi_(tau_j)(k_j))
       >=sqrt(tau_j)log M_j/(12800pi)-o(1)
       ->infinity.                                  (4)

Its actual contact-minus-Haar margin stays at least1/2 by C174.
For example tau_j=1/log M_j for all sufficiently large j gives a lower bound sqrt(log M_j)/(12800pi)-o(1).
This is a new explicitly slow shrinking corridor, not the arbitrary simultaneous shrinking-width theorem.
The original family still has log2<m(P_j)<log4, so there is no near-one counterexample or uniform Mahler-gap conclusion.

<a id="static-phase-geometric-band"></a>
## 2. An exact one-variable geometric expansion

Write C(w)=(w+1)/(w-1) and

    D_0(z)=-2(z-z^-1)+C(z^K), D(z,u)=D_0(z)+C(u).

For regular circle variables these are purely imaginary.
C171's formula U=(-1/2+H)/(-1/2-H), with2H=D+C(v), gives exactly

    U(z,u,v)=[-D v+D-2]/[(D+2)v-D],
    lambda=D/(D+2), |lambda|<1,
    U=-lambda-4/(D+2)^2 sum_(m>=1)lambda^(m-1)v^(-m).
                                                               (5)

For each fixed regular z,u the series converges absolutely and uniformly in v.
Its negative-v coefficient is consequently

    F_m(z,u)=-4 lambda^(m-1)/(D+2)^2,
    |F_m|=(1-|lambda|^2)|lambda|^(m-1)<=1, m>=1.      (6)

Boundedness and iterated integration identify Uhat(p,q,-m) with the two-torus Fourier coefficient of F_m.
The exceptional z,u sets have Haar measure zero; defining F_m there arbitrarily with modulus at most1 does not change this identity.
In particular there is no substitution of a point restriction for a three-torus coefficient.

At z_0=exp(i theta_0), D_0 is finite and purely imaginary.
As u=exp(it) varies with0<t<2pi, C(u)=-i cot(t/2), so Im D ranges over the entire real line.
For each integer m>=2 choose an actual u_m with |D|^2=4(m-1).
Then |lambda|^2=1-1/m and

    |F_m(z_0,u_m)|
       =(1/m)(1-1/m)^((m-1)/2)>=1/(2m).              (7)

For completeness, with q=m-1>=1 the binomial expansion gives(1+1/q)^q<=sum_(k>=0)1/k!<3.
The tail estimate k!>=2^(k-1) for k>=1 proves the last strict bound, with strictness at some k.
Hence the factor in(7) exceeds1/sqrt3>1/2.
The maximizing point need not be calculated or selected by a search.

<a id="static-phase-local-derivatives"></a>
## 3. Local derivatives with a global bounded tail

Take theta in the fixed real interval I=[theta_0-delta,theta_0+delta].
Then K theta lies in[3pi/4,5pi/4], and direct differentiation gives

    |D_0(exp(i theta))|<=5,
    |partial_theta D_0|<=K+4.                        (8)

Indeed |-4i sin theta|<=4, |cot(K theta/2)|<1, and sin^2(K theta/2)>1/2 on this interval.
Set u=exp(it) and eliminate the apparent singularity at u=1:

    L(z,u)=(D_0+3)u-(D_0+1),
    A(z,u)=(D_0+1)u+(1-D_0),
    lambda=A/L,
    Q(z,u)=-4(u-1)^2/L^2,
    F_m=Q lambda^(m-1).                              (9)

These formulas are smooth for every u on the circle and theta in I, including u=1.
Writing D_0=i d with |d|<=5 yields

    |L|>=sqrt(d^2+9)-sqrt(d^2+1)
         =8/[sqrt(d^2+9)+sqrt(d^2+1)]>2/3.

Also |A|<12, |L|<12, |lambda|<=1 and |Q|<=1 there, including the continuous values at u=1.
The last two bounds follow from(6) and continuity, rather than an estimate that loses powers as m grows.
The elementary derivatives satisfy

    |partial_theta L|, |partial_theta A|<=2(K+4),
    |partial_t L|<=8, |partial_t A|<=6.

Quotient differentiation therefore gives

    |partial_theta lambda|<=57(K+4),
    |partial_t lambda|<=225,
    |partial_theta Q|<=216(K+4),
    |partial_t Q|<=900.

Together with |lambda|,|Q|<=1 these explicit inequalities imply

    |partial_theta F_m|+|partial_t F_m|<=C_0 m       (10)

for all theta in I, every u and m>=1.
For m=1 the derivative of lambda^0 is zero, so there is no negative-power exception.
Outside this z interval only the global almost-everywhere bound |F_m|<=1 is used.
No global derivative bound across the original common-zero set is asserted.

<a id="static-phase-finite-support"></a>
## 4. A finite two-variable Fejer cutoff

Let H_R(t)=R^-1|sum_(l=0)^(R-1)exp(ilt)|^2 be the probability-Haar Fejer kernel.
Use its product in the z,u variables and denote the resulting convolution of F_m by P_(R,m).
It is a finite trigonometric polynomial with both frequencies at most R-1 in magnitude, and its coefficient at(p,q) is

    (1-|p|/R)(1-|q|/R) Uhat(p,q,-m)

inside that square, with coefficient0 outside.
Consequently

    |P_(R,m)(z_0,u_m)|
              <=sum_(|p|,|q|<=R-1)|Uhat(p,q,-m)|.     (11)

This uses all those original three-torus coefficients, without any unpriced slice norm.

C172's exact elementary bounds give

    integral |t|H_R(t)dt/(2pi)
                        <=pi(1/2+log R)/R,
    integral_(|t|>delta)H_R(t)dt/(2pi)<=pi/(R delta).

The second follows directly by integrating H_R(t)<=pi^2/(R t^2) on the two tails.
For convolution displacements whose z angle has magnitude at most delta, the connecting z segment lies in I and(10) controls the difference by C_0 m times the sum of the two angular displacements.
On the other displacements use |F_m|<=1 and hence a difference at most2.
Integrating both regions and using the product normalization proves

    |P_(R,m)(z_0,u_m)-F_m(z_0,u_m)|
       <=2pi C_0 m(1+log R)/R+2pi/(R delta)
       <=C_1 m(1+log R)/R.                           (12)

The u displacement may wrap the angle origin; periodic smoothness in(9) permits the shortest circular arc and keeps the same estimate.
No continuity at distant singular points is needed.

For R>=3^18, one has1+log R<=R^(1/6).
To verify this, put x=log R>=18; the function(x+1)exp(-x/6) decreases for x>5 and its value at18 is19/e^3<1, using the positive exponential series e^3>19.
Since m<=R^(1/3) and R>=(4C_1)^6, equation(12) is at most1/(4m).
Together with(7),(11), this yields

    sum_(|p|,|q|<=R-1)|Uhat(p,q,-m)|>=1/(4m),
                      2<=m<=floor(R^(1/3)).           (13)

The negative-v bands are disjoint.
Summing their coefficients gives |F_R|=(2R-1)^2(J-1)<4R^(7/3) and

    sum_(gamma in F_R)|Uhat(gamma)|
       >=(1/4)sum_(m=2)^J 1/m
       >=[log(J+1)-log2]/4
       >=log R/24, R>=64.                            (14)

Here J+1>R^(1/3), and log R/6>=log2.
This proves the complete finite-support assertion(2).

<a id="static-phase-original-return"></a>
## 5. Original schedule, support payment and the slow corridor

Use exactly L426's M_j, epsilon_j, D_K and approximation budget beta_j.
The letter beta_j here denotes that error budget, not an exterior Salem root.
The original schedule gives L_j>a_j^2 and c_j>(L_j+1)^2.
For x>1 the functions(1+log x)/x and(5+2log x)/x are decreasing.
Substitution in L426's explicit epsilon_j formula therefore shows

    epsilon_j=O((1+log L_j)/L_j)
              =O((1+log M_j)/M_j^2),
    beta_j=O_K(((1+log M_j)/M_j)^(1/13)).             (15)

These bounds use only the lower square separations, not an upper bound on the next prime.
The implicit finite constants are independent of j and tau.
The bounds follow directly from the displayed explicit L426 formula and fixed D_K; no unquantified convergence theorem supplies them.

For all sufficiently large j put R_j=floor(M_j^(1/100))>=R_0 and choose E_j=-F_(R_j).
This reflection is required because L426's S(E) uses Uhat(-eta).
Its support lies in the original alias box and

    N_j<4 M_j^(7/300),
    S(E_j)>=log R_j/24>=log M_j/4800.               (16)

The last inequality holds once M_j^(1/100)>=4: floor x>=sqrt x for x>=4, so log R_j>=log M_j/200.
All constants and finite thresholds are fixed before the j limit.

Under(3), eventually tau_j<=1/4 and1/tau_j=o((log M_j)^2).
The coefficient-by-coefficient error from L426 is therefore bounded by

    N_j beta_j/tau_j
       =o(M_j^(-209/3900)(1+log M_j)^(27/13)) ->0.   (17)

The negative exponent is7/300-1/13=-209/3900.
No Bessel improvement or sparsity conjecture is needed to pay this entire support.
Insert(16)--(17) into L426's actual finite first-band bound with c_*=3/(8pi).
This gives(4), since c_*/4800=1/(12800pi) and sqrt(tau_j)log M_j tends to infinity exactly under the positive condition in(3).

The proof concerns a simultaneous shrinking-width sequence and does not exchange C174's fixed-j thin-peak limit with j tending to infinity.
Its new quantitative band estimate supplies the specific missing rate and support payment for this slow corridor only.
Widths with tau_j(log M_j)^2 bounded, or other parts of the arbitrary corridor, remain unclassified by this result.
The actual original Haar margin, original2d_j normalization, phase inversion, both signed Fourier conventions and fixed positive total-measure range are unchanged.

<a id="static-phase-inputs"></a>
## Exact inputs and author limits

| Input | Actual role |
| --- | --- |
| [C171 exact phase](../claims/Yin_C_G0171_v1.md#two-block-torus-phase) | Actual fixed Acal/Bcal and Cayley representation, common-zero domain and modulus1; the one-variable expansion and static quantitative rate are new here. |
| [C171 singularity](../claims/Yin_C_G0171_v1.md#two-block-singular-phase-divergence) | Earlier qualitative non-l1 conclusion and the actual z_0 choice; no pre-existing quantitative lower bound is assumed. |
| [C172 Fejer bounds](../claims/Yin_C_G0172_v1.md#moving-cubic-discrete-fejer) | Probability-Haar kernel bound and first moment with complete elementary derivation; only this exact classical interface is reused. |
| [L426 finite-band theorem](Yin_L_G0426_v1.md#moving-band-target) | Exact original inverse phase, alias box, epsilon/beta budgets and full finite-support error price, including the actual2d normalization. |
| [L426 original error](Yin_L_G0426_v1.md#moving-band-fejer-budget) | Explicit fixed-K budget constants, not a new unknown uniform approximation rate. |
| [L402 actual schedule](Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Same original irreducible Salem polynomials, original degree and square-separated primes, with log2<m<log4. |
| [C174 contact scope](../claims/Yin_C_G0174_v1.md#narrow-contact-fixed-statement) | Finite original Wiener norms and the automatic actual margin; its fixed-input two-limit theorem is not interchanged here. |
| [R417](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding), [R420](../audits/reviews/Yin_R_G0420_v1.md#moving-cubic-whole-independent-finding), [R434](../audits/reviews/Yin_R_G0434_v1.md#narrow-contact-whole-independent-finding), [R439](../audits/reviews/Yin_R_G0439_v1.md#moving-band-whole-independent-finding) | Accepted independent scopes for this author's upstream mathematics; not prospective review of this new static rate. |

The complete original author SELF finding is retained at [R752](../audits/reviews/Yin_R_G0752_v1.md#original-g430-author-self-finding).
No numerical evidence, new source theorem or universal thin-corridor conclusion is claimed.
