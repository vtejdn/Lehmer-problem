---
author: Yin
---
# Complete original endpoint-conditioned Gaussian bounds and full-state costs

This retains all original L251 mathematical conclusions and necessary arguments, with the consumed exact quotient/height mechanisms explicit below.
Original exploration, author checking and old R150 inputs remain fixed; no research Task or execution resumes.

## Statement

For every integer d>=1, N>=1, a_j in Z^d, independent digits eta_j with probabilities1/4,1/2,1/4 on-1,0,1, S=sum_(j<N)eta_j a_j, p_N=Pr(S=0)>0, every real r_j,t and z in Z^d,

    E[exp(t sum_j r_j eta_j)1_(S=z)]
          <=p_N product_j cosh(t r_j)
          <=p_N exp[(t^2/2)sum_j r_j^2].

At S=0 this gives the complete conditional moment/tail bound of equations2--3, with variance proxy sum r_j^2 and the zero-variance case treated separately.
For a real linear functional L, the complete point-mass profile is equation4; for actual power-basis columns of any nonzero algebraic integer and all q=r_0+2s_0 neutral real coordinates it is equation5 with kappa=r_0+s_0, including q0 and degenerate projections.

For every actual Salem minimal polynomial P of degree d=2s+2, s>=1, its real expanding/contracting roots beta,beta^-1 and all neutral pairs define the full derivative constants C_0,C_1 in equation6.
For every N>=2 and epsilon in(0,1), the original exact-return-conditioned quotient E/P obeys both the complete union cutoff9 and dyadic cutoff12; in particular

    H_dyad=C_0+2C_1 sqrt(2N)
       [(2+sqrt2)sqrt(log(4s/epsilon))+B_*],
    B_*=sqrt[(1+1/sqrt2)log2](2+sqrt2)^(3/2),
    Pr(ht(E/P)>H_dyad | S=0)<=epsilon.

N1 has only the zero return and quotient height zero.
Every coefficient, time prefix, neutral pair and initial/terminal padding is included.
For any integer retained height H at least a justified cutoff, the original killed-box return b_(N,H) satisfies (1-epsilon)p_N<=b_(N,H)<=p_N at the same chronological N.
No positive-theta law is substituted.

For every algebraic unit alpha, including torsion, use O=Z[alpha], the actual zero-to-zero original core D_act, complex counting-measure l2(D_act), and

    (K_act f)(x)=sum_eta mu(eta)1_(D_act)(alpha x+eta)
                                                f(alpha x+eta).

With all real places counted once and one representative of each complex pair, let R_v be1/(|v(alpha)|-1) at expanding places and1/(1-|v(alpha)|) at contracting places, and set

    C_non=product_(real nonneutral v)(2R_v+2)
          product_(complex nonneutral v)(2sqrt2 R_v+2)^2,
    D_N=C_non[2+sqrt(2pi kappa N)]^r_0
                   [2+sqrt(4pi kappa N)]^(2s_0)

when q>0, and D_N=C_non when q=0.
For every N>=1 and integer n>=0,

    p_N<=||K_act^N||<=D_N p_N, ||K_act||<=1,
    p_n<=min{1,(D_N p_N)^floor(n/N)},
    0<=-log p_N/N-h_2(alpha)
            <=[log D_alpha+(q/2)log N]/N,
    D_alpha=C_non[2+sqrt(2pi kappa)]^r_0
                       [2+sqrt(4pi kappa)]^(2s_0)

with D_alpha=C_non when q=0.
All constants and dimensions remain input dependent.
Combining a genuinely epsilon-relative retained entry with this full-state norm gives A_cert=D_N b_(N,H)/(1-epsilon), the all-time bound18 and h_2>=-log A_cert/N when A_cert<1; the required retained entry and cutoff are not assumed computed for new inputs.

For the actual quartic P=t^4-t^3-t^2-t+1, reusing the complete original p64=121338835637214357477/2^121 and rational beta bracket gives

    p_n<=2^[-39 floor(n/64)] for every integer n>=0,
    h_2(beta)>=39log2/64.

The exact finite-map variance countercontrol and actual irreducible dyadic-cyclotomic norm sharpness control in Section7 retain their complete original laws.
No conditioned independence/martingale, positive-theta counterpart, improved all-unit neutral exponent, optimized finite constants, degree-uniform near-one bound, critical-mean conclusion or unrestricted Mahler gap is asserted.

<a id="argument"></a>
## Complete argument

### Exact consumed integer quotient interface

The following is the complete original L247 integer-basis/reversal calculation used to identify a killed quotient box with the same original returned-word event.
Its original equations keep their local numbering within this subsection.

Let alpha be any algebraic unit, with actual monic irreducible polynomial

    P(t)=sum_(i=0)^d p_i t^i, p_d=1, p_0 in{-1,1},
    O=Z[alpha], mu(0)=1/2, mu(1)=mu(-1)=1/4.

Use chronological quotient states q=(q_0,...,q_(d-1))=(h_(j-d)...,h_(j-1)) and the EXACT L235 update

    h_j=p_0(e-sum_(i=1)^d p_i h_(j-i)),
    S_e(q)=(q_1,...,q_(d-1),h_j), e in{-1,0,1}.       (1)

Let Q_act be the set of integer states lying on finite zero-to-zero words under(1), and D_act the original core for x -> alpha*x+eta.
Both include zero.
To compare these actual domains, define

    ell_j=-sum_(k=0)^j p_(d-k) alpha^(j-k+1),
                          0<=j<=d-1,
    Phi(q)=sum_(j=0)^(d-1) ell_j q_j,
    Psi(q)=alpha^(-1) Phi(q).                         (2)

By P(alpha)=0, ell_(d-1)=p_0.
For j<d-1, ell_j is -alpha^(j+1) plus integer lower positive powers.
Relative to the integer basis alpha,...,alpha^(d-1),1, the ell_j therefore have triangular change-of-basis determinant +/-1.
This assertion includes d=1, when the sole basis element is p_0.
Multiplication by alpha^(-1) also preserves O bijectively because alpha is a unit.
Thus Phi and Psi are genuine Z-module isomorphisms from Z^d onto O; there is no enlarged fractional module or omitted coset.

The identities

    alpha^(-1) ell_0=-1,
    alpha^(-1) ell_j=ell_(j-1)-p_(d-j) for1<=j<=d-1,
    p_0 ell_(d-1)=1

give directly, coordinate by coordinate in(1),

    Phi(S_e q)=alpha^(-1)Phi(q)+e,
    alpha Psi(S_e q)-e=Psi(q).                       (3)

Consequently a quotient edge q -> S_e q corresponds to the REVERSED original edge Psi(S_e q) -> Psi(q), with original digit -e.
Reversing an entire zero-to-zero word and negating its digits preserves the alphabet and is a bijection of closed words.
Equation(2) therefore restricts to a bijection Q_act -> D_act.
The quotient zero-digit companion has inverse-root orientation; assuming it has eigenvalues alpha rather than alpha^(-1) would be incorrect for general units.
Reciprocity was not needed for(2)--(3).

For a zero-to-zero quotient word of length n, all coordinates appearing during that word are precisely quotient coefficients, together with initial and terminal zero padding.
Thus the maximum of |q_i| over the full state path is the height of E/P for E(t)=sum_(j=0)^(n-1)e_j t^j.
Our tail below concerns this MAXIMUM OVER THE ENTIRE RETURN WORD, not a terminal state (which is zero), a single midpoint, or an occupation distribution.

### Complete consumed Salem partial-fraction height interface

The following is the complete original L235 deterministic coefficient calculation.
Its local equation numbers17--18 belong to this subsection; the subsequent original Sections1--7 retain their own equations1--21.

Now assume P is a Salem minimal polynomial of degree d=2s+2, s>=1, with distinct conjugates beta>1, beta^(-1), and the s conjugate pairs zeta_l,bar zeta_l on the unit circle.
Define finite constants from the ACTUAL polynomial by

    C_0=1/(|P'(beta)|(beta-1))
          +1/(|P'(beta^(-1))|(1-beta^(-1))),
    C_1=2 sum_(l=1)^s 1/|P'(zeta_l)|.              (17)

These constants are positive and can grow with the input; no uniform root-separation or derivative lower bound is assumed.

For a digit word E of length n which returns exactly, let H=E/P and write, for j>=0,

    M_(j,l)=sum_(k=0)^j e_k zeta_l^k.

Partial fractions at every simple root gamma of P give the formal expansion

    1/P(t)=-sum_(P(gamma)=0) sum_(a>=0)
                          t^a/(P'(gamma)gamma^(a+1)).

Hence the actual coefficient h_j is the sum, over all roots, of

    -gamma^(-(j+1))/P'(gamma) sum_(k=0)^j e_k gamma^k.

The expanding-root term is at most1/(|P'(beta)|(beta-1)), since |e_k|<=1.
For the contracting root use the EXACT return E(beta^(-1))=0 to replace the prefix by the negative suffix; the geometric sum then bounds that term by1/(|P'(beta^(-1))|(1-beta^(-1))).
Each unit-circle pair contributes at most2|M_(j,l)|/|P'(zeta_l)|.
Therefore, on every actual return path,

    ht(H)<=C_0+C_1 max_(0<=j<n,1<=l<=s)|M_(j,l)|. (18)

The contracting estimate uses the endpoint condition; it is not an unconditional bounded-state assertion.
Formula(18) includes every quotient coefficient, both real places and all neutral conjugates.
It neither assumes a finite return core nor discards large coefficients.

### Exact dyadic-cyclotomic binomial input for the sharpness control

For d a power of two, t^d+1 is irreducible: d1 is immediate, and for d>=2 its translate by one is Eisenstein at2, with constant2 and all nonleading binomial coefficients even.
Its powers update the d actual integer coordinates cyclically with signs.
Independence between disjoint exponent residue classes and symmetry of the original digits therefore give, for N=d ell+s and0<=s<d,

    p_N=b_ell^(d-s)b_(ell+1)^s,
    b_j=binom(2j,j)/4^j, b_0=1.

Indeed in one residue class the difference of two fair-binomial sums has zero mass4^(-j)sum_k binom(j,k)^2, and comparison of the coefficient of t^j in(1+t)^(2j) gives the displayed central-binomial value.
The exact ratio b_(j+1)/b_j=(2j+1)/(2j+2) proves1/(2sqrt j)<=b_j<=1/sqrt(j+1) for j>=1 by induction: the squared comparisons reduce respectively to(2j+1)^2>=4j(j+1) and(2j+1)^2(j+2)<=4(j+1)^3.
Thus p_N is comparable to N^(-d/2) for every fixed d, with its finitely many N<d included in fixed positive constants.
This is the exact already retained L206/L228 control, without a new source theorem, enumeration or degree-uniform claim.

<a id="conditional-fourier-gaussian-reuse"></a>
### Reuse and changed mechanism

Read [L228's typical neutral lower mass](../ledger/Yin_L_G0228_v1.md#typical-minkowski-collision-lower-bound), [L239's complete normalized auxiliary law and absolute tails](../ledger/Yin_L_G0239_v1.md#normalized-quotient-tail-fixed-scope), [L243's exact quartic finite experiment](../ledger/Yin_L_G0243_v1.md#finite-box-salem-experiment-fixed-scope), and [L247's relative fixed-box escape and charged block theorem](../ledger/Yin_L_G0247_v1.md#return-tail-block-fixed-scope).
Also screened [L248](../ledger/Yin_L_G0248_v1.md#mixed-dual-overlap-fixed-scope) to avoid duplicating its mixed Abel convolution.
None of those inputs asserts the conditional exponential-moment inequality established below.
No external theorem or novelty claim is adopted.

The changed mechanism uses the special ORIGINAL probabilities mu(0)=1/2, mu(+/-1)=1/4 twice: their Fourier polynomial is a square of a cosine, and setting any specified set of digits to zero costs exactly2 to the power minus its size.
Their combination bounds an exponential moment AFTER an exact integer endpoint constraint without dividing by an exponentially small rough return estimate.
The same identity gives a Gaussian spatial profile relative to the actual zero atom.
This will both control complete return-word heights and improve the full-state neutral norm expense.
It is not inferred from unconditioned diffusion or from a stationary auxiliary law.

All new derivations here are by structural_research for Yin.
Root supplied the broad question, receives progress checkpoints and manages the shared execution gate; it supplied no step of this argument.
Root's simultaneous critical-joint-law work is not an input.
The required elementary Fourier orthogonality and cosine identities are proved/applied directly below; no new J or source acquisition is required.
The work remains author self-review pending complete separate review.

<a id="original-endpoint-conditioned-exponential-moments"></a>
### 1. An exact original-law conditional exponential-moment inequality

Fix integer vectors a_0,...,a_(N-1) in Z^d, with N>=1.
Let eta_j be INDEPENDENT original digits with probabilities(1/4,1/2,1/4) on(-1,0,1).
Put

    S=sum_j eta_j a_j, mu_N(z)=Pr(S=z), p_N=mu_N(0)>0.

No spanning, algebraicity, non-torsion or degree hypothesis is imposed on this finite lemma.
Given any real coefficients r_j and real t, the assertion is

    E[exp(t sum_j r_j eta_j) 1_(S=z)]
            <=p_N product_j cosh(t r_j)
            <=p_N exp((t^2/2) sum_j r_j^2), z in Z^d.     (1)

Every constant is independent of the vectors a_j and of their integer relations.
This is a bound for the ORIGINAL iid digits with an endpoint event, not for L239's state-dependent positive-theta law.

For a direct proof, integrate over theta in[0,1]^d with Lebesgue probability.
Orthogonality of integer characters follows by multiplying the elementary one-variable integrals.
Independence and the finite digit sums give exactly

    E[exp(t sum_j r_j eta_j) 1_(S=z)]
      =integral exp(-2pi i theta dot z)
        product_j cos^2(pi theta dot a_j-i t r_j/2) dtheta.

For real x,y,

    |cos^2(x-i y)|=cos^2 x+sinh^2 y.

The left side of(1) is real and nonnegative, so taking absolute values inside this finite integral bounds it by the integral of the product of these nonnegative expressions.
Expand over subsets J of the positions where the sinh term was selected.
If p_(J^c) is the zero-return probability using just the positions outside J, the term is

    p_(J^c) product_(j in J) sinh^2(t r_j/2).

There is an actual event contributing to p_N in which every digit in J is zero and the other positions return.
Therefore

    p_N>=2^(-|J|)p_(J^c).

This remains true for J equal to all positions, with the empty return probability one.
Bound every nonnegative term by this inequality and sum the product expansion.
The result is

    p_N product_j[1+2sinh^2(t r_j/2)]
          =p_N product_j cosh(t r_j).

Finally log cosh u<=u^2/2 follows by differentiating for u>=0, using tanh u<=u, and symmetry.
This completes(1) without a conditional independence assertion or a change of law.

At z=0 division by the ACTUAL positive p_N yields

    E[exp(t sum_j r_j eta_j) | S=0]
                      <=exp((t^2/2)sum_j r_j^2).          (2)

The conditional mean is zero by simultaneous digit-sign reversal, also consistent with(2).
Chernoff's elementary optimization consequently gives, for A>0 and V=sum_j r_j^2>0,

    Pr(|sum_j r_j eta_j|>=A | S=0)
                      <=2 exp(-A^2/(2V)).                (3)

If V=0 the sum is identically zero.
The coefficients can select ANY interval or subset of the raw digits; no adaptively chosen coefficient sequence is asserted.
In particular(2) does not say the conditioned digit process is independent or a martingale.
Its variance proxy is twice the unconditional one, a distinction illustrated in Section7.

<a id="original-relative-gaussian-atom-profile"></a>
### 2. A Gaussian profile relative to the complete zero atom

For a real linear functional L on R^d, put r_j=L(a_j).
On S=z the sum in(1) is identically L(z).
Hence, when V_L=sum_j L(a_j)^2>0, optimizing t gives

    mu_N(z)<=p_N exp(-L(z)^2/(2V_L)).                       (4)

When V_L=0, all actual displacements have L(z)=0; points violating that equality have probability zero.
Thus degenerate projected covariance causes no omitted support.
Unlike an absolute Gaussian tail divided by a return lower bound, formula(4) keeps the SAME actual p_N as its factor.

Now take a_j to be the integer power-basis columns of alpha^j for an actual algebraic integer alpha.
Let tau_0(x) consist of the real neutral embeddings and the real/imaginary coordinates of one representative of each nonreal neutral pair.
Write r_0,s_0 for their respective numbers,

    q=r_0+2s_0, kappa=r_0+s_0.

At a neutral real place |sigma(alpha)|=1; at a neutral complex pair the squared sum of real and imaginary coordinates of sigma(alpha)^j is1.
Consequently

    ||tau_0(alpha^j)||_2^2=kappa.

For any real vector v on this q-dimensional coordinate space,

    sum_(j<N) (v dot tau_0(alpha^j))^2
                              <=kappa N ||v||_2^2.

Apply(1) with these coefficients.
Choosing v in the direction tau_0(z), or optimizing the vector parameter directly, proves for q>0

    mu_N(z)<=p_N exp(-||tau_0(z)||_2^2/(2 kappa N)).         (5)

This includes every neutral coordinate, allows arbitrary dependencies among the phases, and does not presume phase equidistribution.
A sharper covariance matrix may replace kappa N I if its full positive-semidefinite form is explicitly controlled, but no such uncharged estimate is used here.
When q=0 there is no neutral Gaussian factor; the original maximum-atom bound mu_N(z)<=p_N is enough.

<a id="salem-growing-relative-return-height"></a>
### 3. Genuine growing-height tails for actual Salem returned words

Assume P is an actual Salem minimal polynomial of degree d=2s+2, with real roots beta,beta^(-1) and the s nonreal pairs zeta_l,bar zeta_l.
Use L235/L243's exact returned-word quotient E=P H and its full constants

    C_0=1/(|P'(beta)|(beta-1))
           +1/(|P'(beta^(-1))|(1-beta^(-1))),
    C_1=2 sum_(l=1)^s 1/|P'(zeta_l)|,
    ht(H)<=C_0+C_1 max_(k,l)|M_(k,l)|,
    M_(k,l)=sum_(j=0)^(k-1) eta_j zeta_l^j.                (6)

All probabilities in this section condition the original iid difference word of length N on its EXACT integer/algebraic return.
The quotient coefficients and all their initial/terminal padding are those of L247's actual Z-order core map.
No fractional module or parity relaxation enters.
For k=0,N the neutral sum is zero on return.
For1<=k<N it equals the negative complementary suffix, so either representation can be used in(2).
Its real and imaginary coefficients have squared sum at most min(k,N-k) separately.
If |M_(k,l)|>=R, one Cartesian coordinate has magnitude at least R/sqrt2.
Formula(3) and a union bound give

    Pr(|M_(k,l)|>=R | S=0)
       <=4 exp[-R^2/(4 min(k,N-k))]
       <=4 exp[-R^2/(2N)].                                (7)

Therefore for N>=2 and H_*>C_0,

    Pr(ht(H)>H_* | S=0)
       <=min{1,4s(N-1)
           exp[-(H_*-C_0)^2/(2N C_1^2)]}.                 (8)

The parameter H_* may be real; an integer retained box can round it upward.
In particular, for any0<epsilon<1, the cutoff

    H_*=C_0+C_1 sqrt(2N log(4s(N-1)/epsilon))              (9)

makes the complete omitted returned mass at most epsilon times p_N.
This is a relative estimate at the SAME chronological N and the SAME law.
It has no factor exp(Nm), unknown entropy, density assumption, unproved local limit, or hidden p_N lower-bound denominator.
C_0,C_1, s and N remain explicit.
At N=1 the only returned digit is zero and ht(H)=0, treated separately.

If b_(N,H) is the exactly computed original killed-box return and an integer H>=H_* is used, then

    (1-epsilon)p_N<=b_(N,H)<=p_N,
    p_N<=b_(N,H)/(1-epsilon).                              (10)

This provides a full original-law upper certificate from a retained entry and the proved relative error.
Computing b_(N,H) is still a genuine finite lattice problem, and its state count is not assumed cheap.
Formula(10) is not asserted for the positive-theta chain: its conditional Fourier product is different, and the original proof of(1) does not apply to its state-dependent digits.

Fixed epsilon and fixed input yield the square-root N log N cutoff in(9), which already improves the deterministic linear returned-height envelope for sufficiently large N.
A dyadic use of the SAME conditional moment lemma removes the logarithm in N, as proved next.
Neither statement conflicts with L247: a fixed height still loses nearly every sufficiently long returned word on an infinite core, while these retained heights grow with time.


<a id="dyadic-full-return-height-bound"></a>
### 4. A complete square-root-time relative bound without a martingale premise

The conditional process need not be a martingale, so its maximal estimate is proved by finite dyadic decomposition instead.
Fix0<epsilon<1 and let M=2^L be the smallest power of two at least N; thus M<2N unless N=1, and always M<=2N.
Pad the raw increment sequence with deterministic zeros at positions N,...,M-1.
For each of the q=2s real neutral coordinates, every dyadic interval I of length M*2^(-ell) has a sum satisfying(3) with V at most that length, under the SAME full length-N return condition.
This follows by choosing r_j equal to the relevant real/imaginary phase on I and zero elsewhere.
No independence between intervals is used.

At level ell=0,...,L there are2^ell such intervals.
Put

    u=log(2q/epsilon),
    a_ell=sqrt{2M*2^(-ell)[u+(2ell+1)log2]}.

The total conditional probability that any coordinate sum on any of these intervals exceeds a_ell in absolute value is at most

    sum_(ell=0)^L 2q*2^ell
                   exp[-u-(2ell+1)log2]
       =epsilon sum_(ell=0)^L 2^(-ell-1)<epsilon.          (11)

A zero-variance interval is identically zero and causes no exception.
Every initial interval[0,k) with0<=k<=M is a disjoint union of at most one aligned dyadic interval at each level.
On the complementary event, the absolute value of each real coordinate of every prefix is therefore at most sum_ell a_ell.

Here are explicit constants independent of N, P and s:

    r=1/sqrt2,
    A_*=1/(1-r)=2+sqrt2,
    B_*=sqrt((1+r)log2) A_*^(3/2).

By sqrt(x+y)<=sqrt x+sqrt y and Cauchy--Schwarz for nonnegative series,

    sum_(ell>=0) r^ell sqrt(2ell+1)
       <=sqrt{[sum r^ell][sum(2ell+1)r^ell]}
       =sqrt(1+r) A_*^(3/2).

Consequently

    sum_(ell=0)^L a_ell
       <=sqrt(2M)[A_* sqrt u+B_*]
       <=2sqrt N[A_* sqrt u+B_*].

A complex coordinate has modulus at most sqrt2 times its two-coordinate maximum.
Combining with(6) proves the full original RETURN-CONDITIONED estimate

    Pr(ht(H)>H_dyad(N,epsilon) | S=0)<=epsilon,
    H_dyad=C_0+2 C_1 sqrt(2N)
                    [A_* sqrt(log(4s/epsilon))+B_*].       (12)

Thus at each fixed Salem input and fixed epsilon, an O(sqrt N) growing quotient-height box retains at least1-epsilon of the ORIGINAL returned mass, for every N.
All neutral pairs, both real derivative terms, the union over coordinates and the time maximum are present.
This is a proved relative statement, not an assertion of a Gaussian conditioned local limit or independence.
The finite number of integer states in such a box is at most(2 ceil(H_dyad)+1)^d, which is O(N^(d/2)) only with input and epsilon fixed.
The degree exponent and all constants must be retained when inputs vary.

The numerical constants in(12) are deliberately conservative.
At a given finite N one can use the smallest of this cutoff, the valid union cutoff(9), and L243's deterministic complete-height cutoff, checking the hypotheses of the selected bound.
The asymptotic square-root scale does not claim that(12) improves the J52 height7 or12 certificate at N=64.
No new finite computation or optimized cutoff is asserted.

<a id="gaussian-full-state-norm-sandwich"></a>
### 5. A sharper full-state norm expense, with the complete lattice sum

Now let alpha be any actual algebraic UNIT and let D_act be its original actual return core.
Use the same complex counting-measure Hilbert space and actual original operator, now fully retained in [C405](Yin_C_G0405_v1.md#collision-operator-fixed-scope),

    (K_act f)(x)=sum_eta mu(eta)1_(D_act)(alpha*x+eta)
                                              f(alpha*x+eta).

Every actual core state has |v(x)|<R_v at each nonneutral place, where

    R_v=1/(|v(alpha)|-1) for |v(alpha)|>1,
    R_v=1/(1-|v(alpha)|) for |v(alpha)|<1.

These are L173's finite past/future bounds and do not require equality of the core with a full strip.
Count real places once and complex places by one representative per pair.
Define the NONNEUTRAL constant

    C_non=product_(real nonneutral v)(2R_v+2)
           product_(complex nonneutral v)(2sqrt2 R_v+2)^2. (13)

The neutral quantities r_0,s_0,q,kappa are those of Section2.
For N>=1 and q>0 put

    D_N=C_non [2+sqrt(2pi kappa N)]^r_0
                   [2+sqrt(4pi kappa N)]^(2s_0).

When q=0 put D_N=C_non.
Then the sharpened complete-state estimate is

    p_N<=||K_act^N||_(2->2)<=D_N p_N,
    ||K_act||_(2->2)<=1.                                (14)

The new growth factor is O(N^(q/2)) at each fixed input, replacing L173's O(N^q).
Here is the full geometric argument, including translated centers.

Use the fixed product grid in the entire real Minkowski embedding: side length1 in each real coordinate and1/sqrt2 in each Cartesian coordinate of a complex place.
Each half-open product cell contains at most one algebraic integer.
Indeed, a nonzero difference in one cell would have every real conjugate of absolute value<1 and every complex conjugate of modulus<1, contradicting its nonzero integral norm.
This is the already retained norm-grid injection, not a claim that individual coordinates are integers.
The nonneutral bounds above permit at most C_non choices of nonneutral cells.
The count follows from at most2R+2 intervals in a real direction and at most(2sqrt2 R+2)^2 Cartesian cells for a complex disk, independently of the neutral coordinates.

We need a weighted count in the unbounded neutral directions.
For any grid length h>0, center c in R, and sigma>0, the one-dimensional Gaussian satisfies

    sum_(k in Z) sup_(x in[kh,(k+1)h))
                     exp[-(x-c)^2/(2sigma^2)]
          <=2+sqrt(2pi) sigma/h.                       (15)

For clarity, this includes arbitrary alignment with the grid.
On each interval the upper value minus the average is at most the variation of the Gaussian on that interval.
Summing these differences costs at most its total variation2: it rises from0 to1 and then falls to0.
The sum of the interval averages is h^(-1) times the Gaussian integral sqrt(2pi)sigma.
This proves(15), with all sums finite or obtained as increasing limits of nonnegative sums; Gaussian decay gives convergence.
No lattice-shape constant is omitted.

Fix a core state x.
For every possible endpoint y, the original displacement is z=y-alpha^N x, and K_act^N(x,y)<=mu_N(z).
Original iid index reversal permits the ascending power convention used in Section2.
Formula(5) gives

    K_act^N(x,y)<=p_N
       exp[-||tau_0(y)-O_N tau_0(x)||_2^2/(2 kappa N)],

where O_N is multiplication by alpha^N on the neutral coordinates.
It is orthogonal: a sign on each neutral real place and a rotation on each complex pair.
Count nonneutral grid cells by(13), and for each neutral cell bound its Gaussian weight by its supremum.
The exponential factors into its Cartesian coordinates.
Apply(15) with sigma=sqrt(kappa N), h=1 at real neutral coordinates and h=1/sqrt2 at each of the two complex coordinates.
At most one point lies in a complete cell.
The resulting sum of the row is at most D_N p_N, uniformly in the possibly unbounded center O_N tau_0(x).

For a fixed y, orthogonality gives

    ||tau_0(y)-O_N tau_0(x)||_2
       =||O_N^(-1)tau_0(y)-tau_0(x)||_2.

Every predecessor x is a core state and obeys the same fixed nonneutral bounds.
Thus the identical weighted grid sum bounds every COLUMN by D_N p_N too.
Both directions preserve all core states and complete paths.
In the q=0 case the core lies in a bounded full Minkowski region; the same grid and maximum-atom bound give both counts C_non directly.

Finally, for a finitely supported function f, weighted Cauchy--Schwarz followed by the column bound gives

    sum_x |sum_y K_act^N(x,y)f(y)|^2
                    <=(D_N p_N)^2 sum_y |f(y)|^2.

Density extends this to the stated Hilbert space.
The coefficient at zero is exactly p_N, which proves the lower bound.
Each original one-step row and column sum is at most1, since a digit gives one successor and one predecessor; the same estimate proves the contraction.
This completes(14) without any finite core, absolute tail remainder, conditioned independence, critical stationary law, or auxiliary-kernel radius assumption.

For an explicit fixed-input form, define

    D_alpha=C_non[2+sqrt(2pi kappa)]^r_0
                     [2+sqrt(4pi kappa)]^(2s_0)

when q>0, and D_alpha=C_non when q=0.
For N>=1,

    D_N<=D_alpha N^(q/2),
    0<=-log p_N/N-h_2(alpha)
           <=[log D_alpha+(q/2)log N]/N.             (16)

The last conclusion uses the SAME full-space submultiplicativity as L247: for n=kN+r,0<=r<N,

    p_n<=min{1,(D_N p_N)^floor(n/N)}.                (17)

The reverse finite-rate inequality follows from concatenating actual zero-to-zero words, p_(kN)>=p_N^k.
Bare p_N still has only the upper-entropy direction; the lower direction pays D_N.
At positive theta there is no corresponding claimed estimate, because the Fourier/product and zero-digit-removal steps establishing(1) are not available for that state-dependent law.

<a id="relative-truncation-complete-original-block-certificate"></a>
### 6. A complete computed-box interface and an exact quartic improvement

For a fixed Salem input, combine the valid same-time relative estimate(10) or(12) with(17).
If an exactly evaluated retained entry b_(N,H) uses an integer H meeting one of those epsilon-relative cutoffs, define

    A_cert=D_N b_(N,H)/(1-epsilon).

Then all original times obey

    p_n<=min{1,A_cert^floor(n/N)},
    h_2(alpha)>=-log A_cert/N when A_cert<1.          (18)

This pays both the full relative omitted mass and the full-state seam.
The finite state enumeration itself remains to be carried out for any new proposed input; the theorem does not assert that an arbitrary retained box satisfies the hypothesis.
In particular L247's strict fixed-box pressure gap has not been bypassed by silently holding H constant as N grows.

There is an exact useful application needing no new enumeration.
For the L243 quartic P=t^4-t^3-t^2-t+1, q=2, s_0=kappa=1 and r_0=0.
Its accepted rational beta bracket and the integer calculation in L247 give

    C_non=(2/(beta-1)+2)(2beta/(beta-1)+2)<259/8.

Consequently, using only pi<4,

    D_64=C_non[2+sqrt(256pi)]^2
          <(259/8)*34^2=74851/2.                    (19)

The exact COMPLETE original return value is reused from J52/L243:

    p_64=121338835637214357477/2^121,
    121338835637214357477<7*2^64.

Multiplication of these exact inequalities yields

    D_64 p_64<523957/2^58<2^(-39),
    523957<524288=2^19.

Therefore for EVERY integer n>=0 the actual original quartic satisfies

    p_n<=2^[-39 floor(n/64)],
    h_2(beta)>=39 log2/64.                           (20)

This improves the earlier fully charged34/64 exponent by five binary powers per length64 block, using the SAME complete p_64 and a smaller proved full-state expense.
Neither a new original return computation nor a positive-theta conversion is involved.
The elementary displayed arithmetic is the entire new numerical application; no author or reviewer J52 file was edited or rerun.
The finite experiment's complete support/certificate and original review remain precisely the retained L243 evidence, at their actual recorded relationship and scope.
No best-known or literature-priority assertion is made.

The relative tail estimates also apply unconditionally to this actual quartic at every longer N, with the same proved C_0<6/5,C_1<11/30 from L243 if desired.
Their conservative constants need not outperform the exact short-time support at N=64.
These analytic and numerical roles remain separate.

<a id="conditional-gaussian-cost-controls-and-limits"></a>
### 7. Controls, all varying-input costs and the next genuine gate

The factor-of-two variance proxy in(2) must not be reduced to the original unconditioned proxy without further proof.
As a finite integer-map control, take two original digits, endpoint S=eta_1-eta_2, and R=eta_1+eta_2.
Given S=0 the probabilities of R=0,2,-2 are2/3,1/6,1/6.
Hence its variance is4/3, whereas the unconditioned proxy(1/2)sum r_j^2 equals1.
Thus a purported universal return-conditioned bound with the original unconditioned variance would already fail.
The proved proxy sum r_j^2=2 is consistent.
This control has its full original probabilities and is not substituted for a nontorsion Salem input; it checks the abstract finite lemma's constants.

The N^(q/2) norm expense cannot be decreased to a smaller power uniformly over ALL actual algebraic units, even allowing a separate finite constant at each input.
Use the actual cyclotomic family alpha with minimal polynomial t^d+1, d a power of two, retained in L228.
All d real Minkowski dimensions are neutral, so q=d.
Multiplication by alpha is a signed permutation of its power basis.
Every integer coefficient vector is reachable: choose sufficiently many occurrences in each exponent class modulo d and prescribe digits with the signs needed to add its integer coefficients, filling other positions with zero.
Taking sufficiently large word length divisible by2d also permits a displacement canceling any given state.
Therefore the actual core is the whole Z[alpha].

For every fixed N, let f_T be the indicator of the coefficient cube[-T,T]^d.
Multiplication by alpha^N preserves this cube, and every N-step displacement has every coefficient of magnitude at most N.
For x in[-T+N,T-N]^d all such successors lie in the larger cube.
Thus K_act^N f_T(x)=1 there, and

    ||K_act^N f_T||_2^2/||f_T||_2^2
         >=[(2(T-N)+1)/(2T+1)]^d ->1.

Together with contraction this gives ||K_act^N||=1.
L228's exact residue-class central-binomial formula supplies p_N comparable to N^(-d/2) at each fixed d.
Hence a bound ||K_act^N||<=C_alpha N^gamma p_N with gamma<q/2 would be impossible.
This is a full actual torsion control, not an obstruction to a stronger estimate in a separately specified nontorsion Salem class.

For Salem degree d=2s+2, the new precise norm expense is

    D_N=(2/(beta-1)+2)(2beta/(beta-1)+2)
                             [2+sqrt(4pi s N)]^(2s).       (21)

The leading logarithmic-in-N expense is now(d-2)log N/2, with the additional degree factor and beta-dependent constant displayed.
The relative-height bounds retain C_0 and C_1 built from ALL actual root derivatives, as well as s and epsilon.
Neither derivative control nor bounded state-enumeration complexity as degree grows is assumed.
Combining(18) on varying inputs therefore requires an actual retained entry small enough AFTER division by1-epsilon and multiplication by(21).
The unrestricted near-one gap is not supplied by the analytic Gaussian bounds, the fixed quartic improvement, or a hidden assertion that those costs are uniform.

This result changes a specific prior missing premise: the ORIGINAL exactly returned words do have the displayed full-time relative square-root-height control, by a finite Fourier identity rather than an unconditioned Gaussian assumption.
It leaves open sharper covariance constants for a particular input, effective retained-entry evaluation at useful growing heights, degree-uniform structure overcoming the charged expense, and an analogous justified interface for the positive-theta law.
No critical-mean conclusion or replacement of the original law follows.
The unrestricted G0001 conclusion remains unresolved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:03 |
| status | open |
| reason | Retain the full original conditional Fourier/dyadic/Gaussian-grid theorem, all21 formulas, exact quotient/height/binomial inputs, finite countercontrol and every input-dependent cost for an actual whole check. No source proof or native computation is newly adopted beyond its exact recorded input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full statement](#statement) | All finite integer maps, all actual fixed Salem inputs, all algebraic units including torsion, full original digit law, complete cutoffs/norm costs/all-time quartic and sharpness limits. |
| argument | [Entire proof](#argument) | Complete consumed quotient/partial-fraction/binomial interfaces and all original Sections1--7/equations1--21, including every sign, degenerate case, translated row/column Gaussian grid, all-time norm/entropy direction, controls and nonuniformity. |
| dependency | [Actual-core and entropy convention](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Existing proved general-unit actual core/counting-l2 kernel, complete original displacement and positive entropy-limit/contraction conventions; the sharper Gaussian estimate is proved here. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Only the actual quartic polynomial, exact beta/derivative constants, deterministic complete n64 H12 original theta0 entry p64 and relevant H4/H7 comparison; no new J52 run or whole975-field rereview. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/result.json`; this target locates its run account. |
| support | [Original complete finite proof](../ledger/Yin_L_G0243_v1.md#finite-box-salem-experiment-fixed-scope) | Accepted complete-height12 interpretation, exact rational quartic bracket and full original p64, without replacing it by a truncated/positive-theta value or claiming a new finite computation. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:05 |
| status | proved |
| reason | Adopt after the actual complete C419/R621 whole self-check of the original conditional Fourier inequality, all exact quotient/height/binomial interfaces, dyadic full-time relative cutoff, translated Gaussian row/column sums, same-space norm/block/entropy directions, all original quartic arithmetic and variance/torsion controls. Every real/complex multiplicity, zero-variance/q0/N1 case and input-dependent cost remains explicit. Reuse C405 and the exact original finite p64 at their existing scopes; no J52 execution, new source theorem, independent-coverage claim or Task/E resumption is supplied. Original R150 remains whole UNKNOWN. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full statement](#statement) | All finite integer maps, all actual fixed Salem inputs, all algebraic units including torsion, full original digit law, complete cutoffs/norm costs/all-time quartic and sharpness limits. |
| argument | [Entire proof](#argument) | Complete consumed quotient/partial-fraction/binomial interfaces and all original Sections1--7/equations1--21, including every sign, degenerate case, translated row/column Gaussian grid, all-time norm/entropy direction, controls and nonuniformity. |
| dependency | [Actual-core and entropy convention](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Existing proved general-unit actual core/counting-l2 kernel, complete original displacement, strictly positive p_N, existence of the possibly zero entropy limit and contraction conventions; the sharper Gaussian estimate is proved here. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Only the actual quartic polynomial, exact beta/derivative constants, deterministic complete n64 H12 original theta0 entry p64 and relevant H4/H7 comparison; no new J52 run or whole975-field rereview. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/result.json`; this target locates its run account. |
| support | [Original complete finite proof](../ledger/Yin_L_G0243_v1.md#finite-box-salem-experiment-fixed-scope) | Accepted complete-height12 interpretation, exact rational quartic bracket and full original p64, without replacing it by a truncated/positive-theta value or claiming a new finite computation. |
| review | [Actual complete self finding](../audits/reviews/Yin_R_G0621_v1.md#conditional-gaussian-whole-self-finding) | Exact full statement and entire argument with all declared input interfaces, degenerate/control/native-scope and degree/uniformity/law distinctions; current SELF does not replace original UNKNOWN coverage. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:01 |
| status | proved |
| reason | Adopt the actual new isolated whole finding after complete reading of its fixed current proof and full original whole/input comparison. Preserve all original UNKNOWN/SELF, precise source/native boundaries and actual historical dates; no old finding retirement or Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All finite integer maps, all actual fixed Salem inputs, all algebraic units including torsion, full original digit law, complete cutoffs/norm costs/all-time quartic and sharpness limits. |
| argument | [Complete selected argument](#argument) | Complete consumed quotient/partial-fraction/binomial interfaces and all original Sections1--7/equations1--21, including every sign, degenerate case, translated row/column Gaussian grid, all-time norm/entropy direction, controls and nonuniformity. |
| dependency | [Exact accepted input](Yin_C_G0405_v1.md#collision-operator-fixed-scope) | Existing proved general-unit actual core/counting-l2 kernel, complete original displacement, strictly positive p_N, existence of the possibly zero entropy limit and contraction conventions; the sharper Gaussian estimate is proved here. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0052/readme.md#recorded-runs) | Only the actual quartic polynomial, exact beta/derivative constants, deterministic complete n64 H12 original theta0 entry p64 and relevant H4/H7 comparison; no new J52 run or whole975-field rereview. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0052/result.json`; this target locates its run account. |
| support | [Exact support](Yin_C_G0559_v1.md#finite-box-salem-experiment-fixed-scope) | Accepted complete-height12 interpretation, exact rational quartic bracket and full original p64, without replacing it by a truncated/positive-theta value or claiming a new finite computation. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0639_v1.md#isolated-conditional-gaussian-whole-finding) | Entire exact current Statement and Argument and corresponding original whole mathematical scope, all original binding interfaces, negative/useful boundary findings and actual finite/source limits. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0052](../computations/programs/Yin_J_G0052/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
