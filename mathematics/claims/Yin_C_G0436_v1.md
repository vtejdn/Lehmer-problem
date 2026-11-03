---
author: Yin
---
# Complete return-space covariance and constrained triangular collision bounds

The complete original L256 theorem and all20 original formulas, exact controls and scope qualifications are retained here with adequate existing inputs.
L256 preserves substantive investigation, both original requested clarifications/refreezes, source/acquisition limits and fixed old review inputs.
No Task/E execution resumes.

## Statement

Let alpha be ANY nonzero algebraic integer with its actual monic minimal polynomial P of degree d>=1 and m=log M(P)>=0, allowing nonunits and torsion.
For every N>=1 use ORIGINAL independent digits eta_j with probabilities1/4,1/2,1/4 on-1,0,1 and p_N=Pr(sum_(j<N)eta_j alpha^j=0)>0, the fair-binary collision probability.
For N<=d, p_N=2^-N exactly.
For N>d set k=N-d, let V be the d-by-N integer remainder matrix of1,t,...,t^(N-1) modulo P, and B the N-by-k FULL coefficient matrix of P,tP,...,t^(k-1)P, with G=B^T B.
The real and integral kernels are exactly im_R B and B Z^k, respectively; on return eta=B h has a UNIQUE integral quotient h.

The complementary rational orthogonal projection is Pi=BG^-1B^T=I-V^T(VV^T)^-1V.
For every real r in R^N and u in R^k,

    E[exp(r^T eta)|V eta=0]
       <=inf_v product_(j<N)cosh(r_j+(V^T v)_j)
       <=exp(||Pi r||^2/2),
    Cov(eta|return)<=Pi,
    E[exp(u^T h)|return]<=exp(u^T G^-1u/2),
    Cov(h|return)<=G^-1.

These are joint proxies, not covariance identities or conditional independence.
The least coefficient norm for any representative with B^T r=u is u^T G^-1u.
The complementary residual diagonals in2 give only the stated arithmetic/probability connection, with no automatic extra resultant margin or exponential probability deficit.

For g_i=(G^-1)_ii and every real H>=0,

    Pr(ht(h)>H|return)
       <=min{1,2sum_(i<k)exp[-(floor(H)+1)^2/(2g_i)]}.

For epsilon in(0,1), H_epsilon=ceil sqrt(2max_i(g_i)log(2k/epsilon)) retains at least1-epsilon of the SAME chronological original p_N.
For GENERAL nonzero algebraic integers define b_N^H as ORIGINAL return-WORD mass restricted by ht(E/P)<=H.
Only for UNITS does the established integral chronological quotient recurrence identify it with a boxed path entry.
The cutoff formula uses actual rational G without root derivatives, but retains all k/G^-1/input and enumeration costs.
If tr G^-1<1, integrality gives2^-N<=p_N<=2^-N/(1-tr G^-1); that finite-window trace hypothesis is not asserted uniformly.

The ENTIRE exact Gaussian partition is

    p_N=2^-N sum_(h in Z^k:||B h||_infinity<=1)
                                      exp[-(log2)h^T G h].

Retaining the last k coefficient inequalities and eliminating in their stated triangular order gives, with D_j=det Gram(P,...,t^(j-1)P), D_0=1 and delta_j=D_j/D_(j-1)>=exp(2m),

    p_N<=2^-N product_(j=1)^(N-d)(1+2^(1-delta_j))
       <=2^-d exp[-(N-d)g(m)]   (N>d),
    g(m)=log[2/(1+2^(1-exp(2m)))],
    p_N<=exp[-N g(m)] for EVERY N>=1, h_2(alpha)>=g(m).

The local three-consecutive-integer Gaussian maximum12 is valid for every real shift and a>=log2, with full nearest-integer and tail proof.
No unrestricted lattice theta sum replaces the actual constrained return words.
All original expanding conjugates enter through M(P).
The expansion g(m)=(log2)m+[log2-(log2)^2/2]m^2+O(m^3) improves the particular previous general B(m)/2 comparison for sufficiently small positive m, but does not dominate every retained bound; the specified one-expanding-place comparison remains stronger in its own regime.

The finite product is exactly sharp at the actual irreducible input P=t^d+1,d=2^r,r>=0,N=2d: G=2I and p_(2d)=(3/8)^d.
There the actual conditional quotient variance is1/3, below its proxy1/2, with MGF(2+cosh u)/3.
At N=d+1, if any coefficient of P has modulus>1, p_N=2^-N; otherwise p_N=2^-N(1+2^(1-w)), with w the number of nonzero coefficients, another equality in the finite product.
All original digit weights and discarded lower-constraint losses remain.
No practical universal cutoff cost, positive-theta law, uniform extra arithmetic loss, positive entropy floor or unrestricted gap follows because g(m) tends to zero.

<a id="argument"></a>
## Complete argument

### Adequate existing exact finite law, source and comparison inputs

Original Sections1--7/equations1--20 follow completely, including the FINAL original unit-only state identification and d=2^r irreducible torsion qualification.
The original author self-check, both requested scope clarifications/refreezes, source-access failures and old full R155 inputs remain in L256.
The active-task/prospective language in the original work describes2026-10-10 history; no Task/E, mathematical scan or source-proof reading resumes here.

The complete [C419 finite endpoint inequality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) applies to every integer matrix V and all real observables with the original independent three-point law.
It does not require a unit or a state-space realization; its exact-return specialization supplies the entire probability input for3.
C419's [complete argument](Yin_C_G0419_v1.md#argument) also supplies the precise genuine integer quotient/reversed-original-core identification ONLY for a unit constant coefficient+/-1, with every quotient coefficient and zero initial/terminal padding.
No such chronological kernel is asserted for a nonunit.

The finite monic residual/Jensen mechanism used for each positive pivot is fully retained in [C287](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy), including real monic multipliers and integrable circle zeros; its full needed argument is repeated in Section6 below.
C287's [specific prior B(m) comparison](Yin_C_G0287_v1.md#explicit-mahler-binary-comparison) is used only for the stated small-m comparison, not to prove the new triangular product.
The actual L237/L249 arithmetic interpretation of complementary residuals is read at its own recorded domains; it adds no automatic arithmetic margin to the all-nonzero-integer probability theorem.

The adequate [Nat26 original Gaussian readings](../audits/literature/Nat26/Yin_U003.md#nat26-u003) retain the original author20.2.3/20.7.32 and distinct reviewer20.1/formula occurrences at actual statement/formula depth and version1.2.8, with the three actual403 acquisition failures/no-local-bytes boundary.
They supply only the classical theta series/transformation conventions used in Section5; the three-point truncation and constrained integer elimination are proved here.
No historical book proof or new source inspection is claimed.

<a id="return-projection-reuse-and-scope"></a>
### 1. Reuse, conventions and the changed question

The coordinator develops this argument directly.
It reuses [L94's coefficient Gram and monic residual identities](../ledger/Yin_L_G0094_v1.md), [L237's actual arithmetic coefficient projection](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin), [L249's centered specialization](../ledger/Yin_L_G0249_v1.md#centered-column-fixed-scope), [L235's complete integer quotient law](../ledger/Yin_L_G0235_v1.md), and [L251's original endpoint exponential moments](../ledger/Yin_L_G0251_v1.md#original-endpoint-conditioned-exponential-moments).
L94 averages binary posterior means over all endpoint fibers; the return-conditioned difference law below is a different object.
L251's conditional estimate, rather than that averaged covariance inequality, is the probability input.
A bounded G-ledger search for conditional projection, quotient covariance, inverse Gram, and Gaussian partition/three-point estimates did not locate the following assembly.
No exhaustive novelty claim follows.

Let P be the monic minimal polynomial of a nonzero algebraic integer alpha, of degree d>=1, and m=log M(P)>=0.
The theorem below permits nonunits and torsion; its intended unresolved application is to nontorsion units.
Let eta_0,...,eta_(N-1) be the ORIGINAL independent digits with probabilities1/4,1/2,1/4 on-1,0,1.
Write

    E(t)=sum_(j<N) eta_j t^j,
    p_N=Pr(E(alpha)=0)>0.

This is precisely the collision probability of the fair binary sum of length N.
Its logarithmic collision entropy rate h_2 exists by the [retained concatenation/subadditivity argument](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison).
No positive-theta law or renormalized finite box is used.

For N>d put k=N-d.
Let V be the d-by-N integer matrix of remainders of1,t,...,t^(N-1) modulo P in the usual power basis.
Its first d columns are the identity.
Let B be the N-by-k matrix with columns P,tP,...,t^(k-1)P in FULL coefficient coordinates, and put G=B^T B.
Monicity gives independent columns; monic division gives

    ker_R V=im_R B,
    ker_Z V=B Z^k,                                   (1)

with no saturation or order-index loss.
Thus on return there is a unique integral quotient h with eta=B h.
If N<=d, return forces the all-zero word and p_N=2^(-N); all quotient statements below are only needed for k>0.

A further classical input used in Section5 is the Gaussian theta transformation, inspected at statement/formula depth in [Nat26, DLMF20.2.3 and20.7.32](https://dlmf.nist.gov/20.7.E32), version1.2.8 released2026-09-15.
The [supplemental source note](../audits/literature/Nat26/readme.md#gaussian-theta-attribution-20261010) records this exact scope.
The source's historical book proofs were not audited.
The local three-point truncation and integer elimination are proved here rather than attributed to that reference.

<a id="optimized-return-conditioned-coefficient-projection"></a>
### 2. Optimizing an observable on the exact return space

Define the rational orthogonal projection

    Pi=B G^(-1) B^T
       =I-V^T(V V^T)^(-1)V.                          (2)

Both expressions are symmetric idempotents with the image in(1), so they agree.
Fix r in R^N.
Since V eta=0 on return, for every v in R^d the observable r^T eta is unchanged by replacing r with r+V^T v.
Apply L251's exact-return inequality to each such replacement:

    E[exp(r^T eta) | V eta=0]
       <=inf_v product_(j<N) cosh(r_j+(V^T v)_j)
       <=exp((1/2)||Pi r||_2^2).                     (3)

For the second inequality choose v=-(VV^T)^(-1)V r and use log cosh u<=u^2/2.
The infimum inequality itself does not assert attainment or a quadratic approximation to the product.
Sign reversal gives conditional mean zero.
In particular

    Cov(eta | V eta=0) <= Pi                         (4)

as quadratic forms: apply(3) to t r and compare the quadratic terms at t=0.
Every conditional sum is finite, so this differentiation needs no limiting-tail assumption.

Given u in R^k, take r=B G^(-1)u.
Then B^T r=u, Pi r=r and ||r||^2=u^T G^(-1)u.
Consequently

    E[exp(u^T h) | V eta=0]
          <=exp((1/2)u^T G^(-1)u),
    Cov(h | V eta=0)<=G^(-1).                        (5)

This is a jointly valid matrix proxy on the genuine integral quotients.
It asserts neither independent coordinates nor equality with their covariance.
Every representative with B^T r=u has squared norm at least u^T G^(-1)u, since its difference from B G^(-1)u lies in (im B)^perp.

The connection to the arithmetic columns is exact.
For a coefficient vector e_j, the rational residual R_j=(I-Pi)e_j has squared norm l_j=1-Pi_jj.
L237/L249 clear and normalize this residual to obtain an actual arithmetic polynomial.
On the probability side(4) only gives E(eta_j^2|return)<=1-l_j.
These are complementary diagonals of the SAME projection.
An arithmetic resultant margin is not thereby a new exponential probability deficit; no such transfer is used.

<a id="derivative-free-finite-quotient-cutoff"></a>
### 3. A coefficient-only complete height cutoff and an integral control

Let g_i=(G^(-1))_ii>0 and g_* be their maximum.
Chernoff's bound from(5) gives, for a>0,

    Pr(|h_i|>=a | return)<=2 exp(-a^2/(2g_i)).
                                                               (6)

Thus at any real H>=0 one may bound the omitted return fraction by

    Pr(ht(h)>H | return)
       <=min(1, 2 sum_(i<k) exp[-(floor(H)+1)^2/(2g_i)]).
                                                               (7)

Integrality justifies the floor-plus-one.
A convenient sufficient integer cutoff for0<epsilon<1 is

    H_epsilon=ceil sqrt(2 g_* log(2k/epsilon)).          (8)

It retains at least1-epsilon of the ACTUAL p_N at this SAME chronological N.
Define b_N^H here to be the ORIGINAL return-word mass restricted by ht(E/P)<=H; then (1-epsilon)p_N<=b_N^H<=p_N.
For a unit input, all initial and terminal quotient padding is zero and the already retained integer quotient recurrence identifies this mass with its boxed return entry, bounding every coordinate of that state path.
For a nonunit input only the defined word-mass statement is asserted; no p_0=+/-1 chronological integer recurrence is imported.
No enumeration of that mass, full-state norm bound, or practical state-count assertion is supplied by(8).

The finite rational matrix G is constructed from the actual integer coefficients, so(7)--(8) require no root derivative, root separation or off-circle denominator.
This removes those quantities from the FORMULA, not from the possible input dependence: G^(-1) can be large, and the number k of quotient coordinates remains.
It also does not contradict fixed-box escape at an infinite-core input.

There is a separate useful integrality test.
On a nonzero integral h, ||h||_2^2>=1, while(5) gives E||h||_2^2<=tr G^(-1).
Therefore, if delta=tr G^(-1)<1, the conditional probability of h=0 is at least1-delta.
The all-zero original word has probability2^(-N), exactly, so

    2^(-N)<=p_N<=2^(-N)/(1-tr G^(-1))   if tr G^(-1)<1.
                                                               (9)

This is a conditional finite-window criterion; the trace hypothesis is not proved at a degree-linear window on all near-one inputs.
In particular simply tracing(4) gives rank k, which by itself supplies no such criterion.

<a id="exact-return-integral-gaussian-partition"></a>
### 4. The exact constrained integer Gaussian sum

On every admissible return word, eta_j^2=|eta_j|, so its complete product probability is

    2^(-N-wt(eta))=2^(-N) exp[-(log2) h^T G h].

Equation(1) is a bijection, hence exactly

    p_N=2^(-N) sum_(h in Z^k: ||B h||_infinity<=1)
                              exp[-(log2)h^T G h].      (10)

This is not an auxiliary Gaussian law.
The cube restriction is essential: dropping ALL its constraints loses the calibrated bound below.
Retain just the last k of its N coefficient inequalities.
Write P=sum_(a=0)^d p_a t^a, p_d=1.
For i=0,...,k-1, the coefficient in row d+i is

    (B h)_(d+i)=h_i+sum_(j=i+1)^(k-1) p_(d+i-j) h_j,  (11)

where coefficients of P outside0,...,d are zero.
For fixed later h_j, condition(11) allows precisely THREE consecutive integral values of h_i.
The remaining constraints(11) for indices greater than i involve no h_i.
The retained upper triangular system has exactly3^k integral solutions, by choosing h backwards; thus all sums to be bounded are finite.
Discarding the first d inequalities only enlarges(10).

<a id="three-point-gaussian-maximum"></a>
### 5. A fully charged three-point Gaussian bound

For any a>=log2, x in R and any three consecutive integers c-1,c,c+1,

    sum_(j=c-1)^(c+1) exp[-a(j-x)^2] <=1+2 exp(-a).    (12)

Here is a direct reduction to the accepted classical theta formula, including the truncation step.
Among all consecutive triples the sum is largest when c is an integer nearest x: the change from c to c+1 is exp[-a(c+2-x)^2]-exp[-a(c-1-x)^2], whose sign is that of x-c-1/2.
Translation therefore reduces to c=0 and |x|<=1/2.

Nat26's formulas, with tau=i a/pi and z=i a x, give

    Theta_a(x):=sum_(n in Z) exp[-a(n-x)^2]
       =sqrt(pi/a) [1+2 sum_(n>=1)
                            exp(-pi^2 n^2/a) cos(2pi n x)]
       <=Theta_a(0).                                  (13)

Indeed Theta_a(x)=exp(-a x^2) theta_3(i a x | i a/pi); under20.7.32, tau'=i pi/a and z tau'=-pi x.
The principal square root is sqrt(a/pi), the exponential factor is exp(a x^2), and theta_3 is even by20.2.3.
All Fourier coefficients on the right of(13) are nonnegative and both Gaussian series converge absolutely.

For f(y)=exp(-a y^2), f''(y)=2a(2a y^2-1)exp(-a y^2)>=0 whenever y>=3/2: a>=log2>2/9.
Thus for n>=2 and |x|<=1/2, convexity gives f(n-x)+f(n+x)>=2f(n).
Summing the absolutely convergent nonnegative tail shows that the omitted terms with |n|>=2 at x are at least the omitted tail at0.
Subtract this tail inequality from(13).
The three terms remaining give(12).
This proves the estimate for all shifts, including half-integer ties, rather than only for a centered or unshifted Gaussian.

<a id="triangular-gram-collision-bound"></a>
### 6. Sequential elimination and a general Mahler-to-collision comparison

For j>=1 let D_j be the determinant of the j-by-j Gram matrix of P,tP,...,t^(j-1)P; put D_0=1 and

    delta_j=D_j/D_(j-1)>0,
    c_j=1+2^(1-delta_j).                               (14)

All leading principal blocks of G are these Gram matrices.
Successively complete the square and eliminate variables h_0,h_1,...,h_(k-1).
At step i the quadratic coefficient of h_i in the Schur complement is delta_(i+1).
To verify this pivot convention, Gaussian elimination of the first i rows/columns preserves determinant by multiplication by the successive positive pivots; the next leading determinant quotient is D_(i+1)/D_i.
The square's center is a real linear function of later variables; no integrality of that center is assumed.

The monic residual argument in L94, also repeated here, gives delta_j>=M(P)^2.
The Gram-Schmidt residual of t^(j-1)P against its previous shifts is P Q with Q a real monic polynomial of degree j-1.
Its squared coefficient norm is delta_j.
Parseval and the integrable logarithmic mean on the circle imply ||P Q||_2>=M(P Q)=M(P)M(Q)>=M(P).
This covers zeros on the unit circle.
Consequently (log2)delta_j>=log2, as required in(12).

At each step, fix the later integer variables and sum the Gaussian over the three values allowed by(11).
Bound that factor by c_(i+1) using(12), independently of those later values.
Only the constraints(11) with index greater than i remain, and they do not involve the eliminated variable.
Induction therefore gives the complete finite estimate

    p_N<=2^(-N) product_(j=1)^(N-d) (1+2^(1-delta_j))
         <=2^(-d) exp[-(N-d) g(m)],       N>d,          (15)

where

    g(m)=log[2/(1+2^(1-exp(2m)))] >=0.                  (16)

No infinite-state operator cost, root separation, first-return estimate or unproved convergence of D_j/D_(j-1) enters(15).
For N<=d use the exact all-zero value.
Since0<=g(m)<=log2, both ranges imply

    p_N<=exp[-N g(m)] for EVERY N>=1,
    h_2(alpha)>=g(m).                                 (17)

This comparison holds for every nonzero algebraic integer and its full minimal polynomial, in particular with ANY number of expanding conjugates.
It uses the sum of their positive logarithms through M(P), not just the largest modulus.
The stronger first inequality of(15) retains all finite rational pivots and may be used when they are available.

Near zero, elementary Taylor expansion in(16) gives

    g(m)=(log2)m+[(log2)-(log2)^2/2]m^2+O(m^3).         (18)

Thus the general lower comparison here has leading coefficient log2.
L94 together with L89 gives the general bound h_2>=B(m)/2 with leading coefficient1/2; (17) improves that particular comparison for all sufficiently small positive m.
This is not asserted to dominate every previously retained bound or to be new in the literature.
For one-expanding-place inputs, L30 already gives h_2/m ->1 along a hypothetical near-one sequence, which is stronger in that regime.
Most importantly, g(m)->0, so(17) cannot itself exclude such a sequence or solve G0001.

<a id="coefficient-gram-controls-and-next-obstruction"></a>
### 7. Exact controls, costs and the remaining opportunity

The construction is exactly sharp at a concrete finite torsion window.
Take d=2^r for an integer r>=0, P=t^d+1, the actual irreducible cyclotomic input already used in L251, and N=2d.
The columns of B have disjoint two-point supports, so G=2I_d, delta_j=2 and

    p_(2d)=(3/8)^d
           =2^(-2d) product_(j=1)^d(1+2^(1-2)).        (19)

Both copies of each coefficient must be the same quotient digit.
The two zero digits have probability1/4 and the two choices of equal nonzero digits have total probability1/8.
Different pairs are independent.
All discarded lower constraints duplicate the upper ones, and the square centers are zero, proving equality in the first part of(15).
Since this input has m=0, its positive finite collision entropy is not a positive asymptotic gap.

The projected covariance proxy need not be exact even in this control: each conditioned h_i takes0 with probability2/3 and+/-1 with probability1/6 each, so its variance is1/3 whereas (G^(-1))_ii=1/2.
Its exact MGF is(2+cosh u)/3.
This checks the direction and scale of(5) and warns against calling G^(-1) the actual covariance.

For arbitrary monic P and N=d+1, the sole quotient coefficient h is integral and the leading coefficient forces h in{-1,0,1}.
If any coefficient of P has modulus greater than1, only h=0 is admissible, so p_N=2^(-N).
Otherwise let w be the number of nonzero coefficients of P.
Then G=[w] and

    p_N=2^(-N)(1+2^(1-w)),                            (20)

again equality in(15).
Thus omitted lower constraints can matter already at the first nontrivial quotient, and(15) does not claim to recover them for large coefficients.

The changed useful interface is now explicit: actual polynomial coefficient geometry supplies both a return-conditioned covariance/height control and a direct original collision estimate by triangular integer elimination.
To improve this into a positive gap one would need arithmetic information giving additional loss beyond g(m), for example by retaining coupled discarded constraints or proving a suitable excess in the actual pivots at the necessary windows, with its complete costs and entropy direction.
A finite positive surplus at one torsion-compatible window is insufficient; no such uniform arithmetic excess is proved here.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-r800-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:49 |
| status | open |
| reason | Retain all original projection/covariance/height/trace and constrained Gaussian/three-point/pivot/entropy arguments on the actual nonzero-integer domain, with exact unit-only state and dyadic irreducibility qualifications, both sharp controls and every source/cost/negative boundary for whole checking. No new math/source/J execution or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact theorem](#statement) | Every nonzero algebraic integer/d/N, original law and genuine integral quotient; all real observables/shifts, floor/trace/cutoff conditions, full finite pivots/all-time g(m), both exact controls and all unit/nonunit/cost boundaries. |
| argument | [Entire proof](#argument) | Adequate exact finite-law/unit-only/source/comparison interfaces and full original Sections1--7/equations1--20, all monic kernels/projections, original constraints, theta/truncation/pivot/Jensen and finite/entropy/negative limits. |
| dependency | [Exact original finite endpoint law](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Every integer coefficient matrix and real observable under the actual1/4,1/2,1/4 digits; no unit/state-kernel premise for the finite lemma. |
| dependency | [Unit-only integer state identification](Yin_C_G0419_v1.md#argument) | Exact monic constant+/-1 quotient recurrence, reversed original core and all coefficient/padding heights only for units; general nonunit b_N^H remains defined word mass. |
| dependency | [Original Gaussian theta formulas](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Classical20.2.3/20.7.32 and20.1 nome/upper-half-plane/principal-root conventions at the actual original statement/formula depth; no source-book proof or project truncation attributed to the source. |
| support | [Existing finite real-monic Jensen interface](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact coefficient residual/pivot>=M(P)^2, real monic multipliers and circle-log integrability; full needed derivation is repeated here. |
| support | [Specific prior general entropy comparison](Yin_C_G0287_v1.md#explicit-mahler-binary-comparison) | Only the existing B(m)/2 small-m comparison and its scope; no global domination, novelty or new positive gap is inferred. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:54 |
| status | proved |
| reason | Adopt after the actual whole C436/R638 SELF check of the complete real/integral quotient, optimized proxies/height/trace, original constrained Gaussian partition, every shifted three-point/theta/tail/pivot/Jensen step, all-time general-nonzero-integer entropy comparison and both exact controls. The existing original L89 rate argument is now linked to its adequate C280 home; no mathematical mechanism or domain changed. Nat26-U003 preserves distinct actual original formula readings and403/no-bytes limits. Original R155 whole UNKNOWN and its two historical final qualifications remain; no isolation, new scan/source proof or Task/E resumption is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact theorem](#statement) | Every nonzero algebraic integer/d/N, original law and genuine integral quotient; all real observables/shifts, floor/trace/cutoff conditions, full finite pivots/all-time g(m), both exact controls and all unit/nonunit/cost boundaries. |
| argument | [Entire proof](#argument) | Adequate exact finite-law/unit-only/source/comparison interfaces and full original Sections1--7/equations1--20, all monic kernels/projections, original constraints, theta/truncation/pivot/Jensen and finite/entropy/negative limits. |
| dependency | [Exact original finite endpoint law](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Every integer coefficient matrix and real observable under the actual1/4,1/2,1/4 digits; no unit/state-kernel premise for the finite lemma. |
| dependency | [Unit-only integer state identification](Yin_C_G0419_v1.md#argument) | Exact monic constant+/-1 quotient recurrence, reversed original core and all coefficient/padding heights only for units; general nonunit b_N^H remains defined word mass. |
| dependency | [Original Gaussian theta formulas](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Classical20.2.3/20.7.32 and20.1 nome/upper-half-plane/principal-root conventions at the actual original statement/formula depth; no source-book proof or project truncation attributed to the source. |
| support | [Existing finite real-monic Jensen interface](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact coefficient residual/pivot>=M(P)^2, real monic multipliers and circle-log integrability; full needed derivation is repeated here. |
| support | [Specific prior general entropy comparison](Yin_C_G0287_v1.md#explicit-mahler-binary-comparison) | Only the existing B(m)/2 small-m comparison and its scope; no global domination, novelty or new positive gap is inferred. |
| dependency | [Exact general collision-rate existence](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | The unchanged original L89 independent-block/Fekete interface for arbitrary abelian endomorphisms, including nonunit multiplication; no BV20 or extra source theorem. |
| review | [Actual complete SELF finding](../audits/reviews/Yin_R_G0638_v1.md#return-projection-whole-self-finding) | Whole exact statement/argument/finite-law/unit-only/source/comparison/rate inputs, every original1--20 formula, shift/constraint/finite/entropy/control and domain/cost boundary. |


### Decision complete-isolated-whole-r800-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:59 |
| status | proved |
| reason | Adopt the new complete isolated whole finding after full coordinator reading of its exact mathematics, old whole/negative/source/native comparisons and truthful date/context limits; no target proof repair and no retrospective change to original UNKNOWN or SELF relationships. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every nonzero algebraic integer/d/N, original law and genuine integral quotient; all real observables/shifts, floor/trace/cutoff conditions, full finite pivots/all-time g(m), both exact controls and all unit/nonunit/cost boundaries. |
| argument | [Complete selected argument](#argument) | Adequate exact finite-law/unit-only/source/comparison interfaces and full original Sections1--7/equations1--20, all monic kernels/projections, original constraints, theta/truncation/pivot/Jensen and finite/entropy/negative limits. |
| dependency | [Exact accepted input](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Every integer coefficient matrix and real observable under the actual1/4,1/2,1/4 digits; no unit/state-kernel premise for the finite lemma. |
| dependency | [Exact accepted input](Yin_C_G0419_v1.md#argument) | Exact monic constant+/-1 quotient recurrence, reversed original core and all coefficient/padding heights only for units; general nonunit b_N^H remains defined word mass. |
| dependency | [Exact accepted input](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Classical20.2.3/20.7.32 and20.1 nome/upper-half-plane/principal-root conventions at the actual original statement/formula depth; no source-book proof or project truncation attributed to the source. |
| support | [Exact support](Yin_C_G0287_v1.md#endpoint-gram-mahler-entropy) | Exact coefficient residual/pivot>=M(P)^2, real monic multipliers and circle-log integrability; full needed derivation is repeated here. |
| support | [Exact support](Yin_C_G0287_v1.md#explicit-mahler-binary-comparison) | Only the existing B(m)/2 small-m comparison and its scope; no global domination, novelty or new positive gap is inferred. |
| dependency | [Exact accepted input](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | The unchanged original L89 independent-block/Fekete interface for arbitrary abelian endomorphisms, including nonunit multiplication; no BV20 or extra source theorem. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0653_v1.md#return-projection-isolated-whole) | Whole exact original-law/projection/quotient/cutoff/trace/constrained Gaussian/all-N entropy theorem, both final scope clarifications and all source/control/domain costs. |

