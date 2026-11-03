---
author: Yin
---

# Complete signed autocorrelation bundle theorem and actual residual-column coherence bound

The entire [L318](../ledger/Yin_L_G0318_v1.md) weighted resultant/Poisson/cancellation argument and every all-column projection cost are responsible here.
The joint_boundary_research AI authored the local derivations for Yin; original source inspection, whole author checking and original noncontributor review remain separately retained.

<a id="statement"></a>
## Complete statement

Let P∈Z[t] be monic irreducible of ACTUAL degree d, constant ±1, with no root of unity; m=log M(P)>0 is TOTAL.
Retain ALL original conjugates alpha_i=r_i z_i,r_i>0,|z_i|=1, with Σlog⁺r_i=m and Σ|log r_i|=2m.
Reciprocity is NOT required.
For ANY integer T>=0 and real-coefficient F=Σ_(j=0)^T f_j t^j in that fixed actual degree window, permitting zero endpoints, put E_F=Σf_j² and A_h(F)=Σ_(j=0)^(T-h) f_j f_(j+h).
The complete positive unit-mass Poisson-kernel/finite-Fourier/Cauchy--Schwarz proof gives for 0<=r<=1 and EVERY |z|=1,
    |F(rz)|²<=E_F+2Re Σ_(h=1)^T A_h(F)r^h z^h.
Fixed-window reversal F*=t^T F(t^-1) preserves E_F and ALL A_h, so for EVERY original root, t_i=exp(-|log r_i|),
    |F(alpha_i)|²/max(1,r_i)^(2T)<=E_F+2Re Σ A_h(F)t_i^h z_i^h.
No root, leading coefficient, content or endpoint padding is discarded.

Retain EXACT original powered-angular interface
    c0=log2/4,h0=c0 exp(-20),
    b(u)=max(u,sqrt(u/c0)log sqrt(c0/u)),
    epsilon(u)=min(1,15sqrt(b(u))+4u), 0<u<=h0.
It is increasing and tends to zero; every actual frequency1<=h<=T has
    |d^-1 Σ_i t_i^h z_i^h|<=epsilon(u)+2hm/d<=epsilon(u)+2u, u=Tm/d.
Actual Pri11/Dim19 adopted statement/proof-inspection and powered-degree-drop boundaries remain unchanged.

Take ANY finite nonempty integer bundle F_a∈Z[t],deg<=T, EVERY Res(P,F_a)≠0, and positive REAL weights w_a summing1.
Set E=Σw_a E_Fa>0,A_h=Σw_a A_h(F_a),kappa=2Σ_(h=1)^T|A_h|/E,I=Σw_a log|Res(P,F_a)|/d.
When 0<u<=h0,
    I<=log(E)/2+u+log[1+kappa(epsilon(u)+2u)]/2.
This sums signed autocorrelations over auxiliaries BEFORE absolute values and uses only joint log concavity/majorants, with no independence.
Exact complementarity A_h=0 for EVERY h>=1 is equivalent to Σw_a|F_a(e^iθ)|²=E for ALL θ, and gives
    I<=log(E)/2+Tm/d
for EVERY m>0 without a discrepancy or small-u restriction.
No constructed external Golay/filter-bank/arithmetic-coverage theorem is assumed.

Fix C>0,eta>0.
If a class of ACTUAL inputs has such bundles with T<=Cd, actual arithmetic lower income J<=I and J-log(E)/2>=eta, exact complementarity implies m>=eta/C.
For one uniform kappa<=K, choose 0<u*<=h0 with u*+log[1+K(epsilon(u*)+2u*)]/2<eta; then every input with m<=u*/C is excluded.
Along hypothetical m→0, fixed positive surplus is impossible if kappa[epsilon(Cm)+2Cm]→0.
Actual truncated prime-depth J certificates stay with THEIR F_a and EVERY original root; modulus/ramification/repeated-reduction/order hypotheses are inherited intact.
Replacing F_a=c_a G_a changes its income by log|c_a| and energy/autocorrelations by c_a² SIMULTANEOUSLY; independently primitive-normalizing columns with the old weights is invalid.
The missing premise is genuine joint arithmetic AND coherence coverage.

For ANY integer N>d, let A be the N×(N-d) coefficient matrix of P,tP,...,t^(N-d-1)P and
    Rproj=I_N-A(A^T A)^-1 A^T.
It is a rational rank/trace d symmetric idempotent.
One genuine q>0 clearing denominators of BOTH Rproj and(A^T A)^-1 A^T yields for EVERY0<=j<N the actual integer polynomial
    F_j=q t^j-P U_j, coefficient vector qRproj e_j,deg<=T=N-1.
Every F_j≠0,F_j(alpha_i)=q alpha_i^j,|Res(P,F_j)|=q^d, EACH original p-adic root valuation=v_p(q), and content(F_j) divides q; full contents are retained.
With ALL N columns and weights1/N,
    E=q²d/N, A_h=(q²/N)a_h,
    a_h=Σ_(j=0)^(N-1-h)(Rproj)_(j,j+h),
    kappa_R=(2/d)Σ|a_h|,I=log q,
    I-log(E)/2=log(N/d)/2.
All common scalar, coefficients, matrix/auxiliary counts and original root factors remain paid; no cheap q or runtime bound independent of d is claimed.

EVERY actual projection satisfies
    0<=kappa_R<=sqrt[(N-1)(N-d)/d].
When0<u=(N-1)m/d<=h0 it ALSO satisfies
    kappa_R[epsilon(u)+2u]>=(N/d)exp(-2u)-1.
Both complete proofs retain all Cauchy--Schwarz factors2, full projection trace/diagonal energy and exponentiation directions.
For N=ceil(Cd),C>1 fixed, the universal upper cost is O_C(sqrt d), an actual cancellation improvement over separate O_C(d) coefficient bounds, not a degree-independent bound.
The displayed combination yields its complete finite necessary discriminator.
Within the stated small-u domain, hypothetical m→0 and N/d bounded away from1 force kappa_R→infinity; no near-one family is constructed.
A uniform bound on THESE ACTUAL signed diagonals at bounded degree ratio would imply the conditional gap, but is unproved.
The resulting degree-dependent test is not claimed to improve the best general Mahler bounds.

For ANY single F and complementary filters with positive weights and Σw_a|G_a(z)|²=K>0 on the whole circle, H_a=FG_a has aggregate K|F(z)|².
Its energy and nonconstant autocorrelations both scale by K, so normalized kappa is UNCHANGED; monomial shifts/sign repetitions do not supply cancellation.
Every extra filter degree and complete resultant factor remains charged.
This exact identity does not exclude genuinely different auxiliary directions.

For EVERY actual nontorsion irreducible unit input and positive integer h, the primitive pair1±t^h with equal weights has T=h,E=2,kappa=0,I=log Z_(2h)/(2d),Z_(2h)=|Res(P,t^(2h)-1)|.
It is nonvanishing, and its two COMPLETE resultants multiply with all original roots/leading signs/content retained.
The accepted full original powered-degree cyclic-cost proof gives log Z_(2h)/d=o(1) uniformly for h<=Cd along hypothetical TOTAL m→0.
Thus this whole degree-linear complementary recipe has surplus tending to -log2/2 and cannot supply the missing positive surplus.
It is not a fixed/growing-measure substitute or a prohibition on other bundles.

The complete actual signed bundle theorem, full residual construction, both exact failure mechanisms and all original source/native/negative boundaries are retained.
ABR01 supplies selected classical Poisson METHOD attribution only; all polynomial/reversal/aggregate/arithmetic steps are locally proved.
Root's original selected pages/proofs/visuals, uninspected upstream source dependencies and no-new-program/no-J facts remain exactly disclosed.
The original entire22109-byte2026-10-10T10:37 freeze and R2172026-10-10T10:39 whole noncontributor finding remain original inputs, not current C review.
No bounded actual coherence, covered unrestricted class, near-one existence or unrestricted gap is proved.

## Complete argument

<a id="argument"></a>

<a id="simultaneous-coherence-reuse"></a>
### 1. Changed mechanism and actual reused premises

This contribution is by the joint_boundary_research AI for Yin.
Root supplied only the broad question, source coordination and review arrangement.
The [L315 selected primitive-pivot theorem](Yin_C_G0597_v1.md#statement) supplies the point of departure, not a new assumption of bounded selected height.
[L229's powered angular estimate](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) and its [whole resultant calculation](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) are the actual analytic premises.
Their accepted Pri11/Dim19 statement and proof-inspection boundaries remain unchanged.
[L237's exact monomial residual](Yin_C_G0570_v1.md#monomial-projection-uniform-margin) supplies the already proved rational projection construction and [its primitive-content accounting](Yin_C_G0570_v1.md#projection-content-and-exact-root-depths).
Projection existence and positive scalar surplus are not claimed anew.
[L241's joint determinant optimum](Yin_C_G0570_v1.md#joint-auxiliary-determinant-fixed-scope) concerns a different determinant functional; it supplies no signed diagonal-sum estimate used here.

The new mechanism combines ALL actual residual columns before discarding Fourier signs.
A finite weighted bundle of integer auxiliaries has an aggregate autocorrelation which can be much smaller than the separate coefficient absolute sums.
A direct Poisson majorant handles expanding and contracting original roots without destroying this cancellation.
On the actual projection bundle a complete elementary bound reduces the coefficient coherence cost from order d to order sqrt(d) at a fixed degree-linear window.
The resulting estimate still does not give a uniform gap; it supplies a changed finite discriminator and a conditional coverage target stated precisely below.

A bounded local screen of the responsible ledgers, audits and bibliography did not locate this particular Poisson/autocorrelation bundle bound.
The first shell search supplied wildcard path arguments unsupported by Windows rg and returned no mathematical evidence; corrected directory/glob searches were used.
Searches also returned unrelated free-Poisson and theta-Poisson records, which are not analytic inputs.
Root completed one bounded primary-source check for classical disk Poisson representation; Section7 records its exact attribution.
A self-contained proof in the required polynomial normalization is given below.
No new mathematical program, numerical experiment, J or class-of-input scan is used.

Let P be monic irreducible in Z[t], with actual degree d, constant term +/-1, and no root of unity.
Retain every original complex conjugate alpha_i=r_i z_i, where r_i>0 and |z_i|=1, and put m=log M(P)>0.
The unit normalization gives

    sum_i log^+ r_i=m,  sum_i |log r_i|=2m.          (1)

Reciprocity is not needed for the new theorem.
It includes the actual reciprocal inputs in L315, with no degree replacement by a trace degree or by the degree of a power.

<a id="polynomial-poisson-majorant"></a>
### 2. A polynomial square majorant retaining Fourier signs

Write F(t)=sum_(j=0)^T f_j t^j with real coefficients, permitting zero endpoints in this fixed degree window.
Set

    E_F=sum_j f_j^2,
    A_h(F)=sum_(j=0)^(T-h) f_j f_(j+h), 1<=h<=T.

For0<=r<=1 and |z|=1,

    |F(rz)|^2 <= E_F+2 Re sum_(h=1)^T A_h(F) r^h z^h.
                                                               (2)

Here is a complete elementary proof.
When0<=r<1, use the positive kernel

    K_r(theta)=(1-r^2)/|1-r exp(i theta)|^2
             =sum_(h in Z) r^|h| exp(i h theta).

The series follows by multiplying the two convergent geometric series; its constant term is1, so its normalized circle integral is1.
Convolution with this kernel sends exp(i j theta) to r^|j| exp(i j theta).
Consequently its average of F on the circle is F(rz), while its average of |F|^2 is the right side of(2), because the Fourier coefficients of |F|^2 are E_F and A_h(F).
Cauchy--Schwarz with respect to this positive probability density proves(2).
At r=1 it is the exact Fourier identity, also obtained by continuity.
This proves the required majorant without invoking a general theorem about subharmonic functions.

Define the fixed-window reverse F^*(t)=t^T F(t^-1).
Real coefficients imply |F^*(z)|=|F(z)| on the unit circle, so its E and all its A_h equal those of F.
If an original root has r_i>=1, then

    r_i^(-T)|F(r_i z_i)|=|F^*(r_i^-1 z_i)|.

Indeed F^*(r^-1 z)=r^-T z^T F(r z^-1), whose modulus equals r^-T|F(rz)| by real coefficients.
Apply(2) to F for r_i<=1 and to F^* for r_i>=1.
With t_i=exp(-|log r_i|), one obtains

    |F(alpha_i)|^2 / max(1,r_i)^(2T)
       <= E_F+2 Re sum_(h=1)^T A_h(F) t_i^h z_i^h.    (3)

All factors in this inequality are for the original roots, including roots on the unit circle.
The fixed T is an actual common degree bound; reversing a polynomial of smaller degree introduces only its actual zero coefficients.
No leading coefficient or nonzero root of F is discarded.

Put u=Tm/d.
The retained L229 function is

    c_0=log(2)/4, h_0=c_0 exp(-20),
    b(u)=max{u,sqrt(u/c_0) log sqrt(c_0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u}, 0<u<=h_0.

It is increasing, tends to zero, and bounds every actual angular moment with1<=h<=T.
By(1) and1-exp(-x)<=x,

    |d^-1 sum_i t_i^h z_i^h|
      <=epsilon(u)+d^-1 sum_i(1-t_i^h)
      <=epsilon(u)+2hm/d<=epsilon(u)+2u.             (4)

Thus radial damping preserves a bound on the AGGREGATE signed Fourier coefficients.
It does not introduce an error involving the separate coefficient l1 norms.

<a id="weighted-integral-bundle-bound"></a>
### 3. Complete simultaneous integer-auxiliary inequality

Take a finite nonempty family F_1,...,F_r in Z[t], each of degree at most T, with every Res(P,F_a) nonzero.
Let weights w_a>0 sum to1.
Real weights are allowed in the inequality; a proposed exact arithmetic construction can use rational weights.
Define

    E=sum_a w_a E_(F_a)>0,
    A_h=sum_a w_a A_h(F_a),
    kappa=2 sum_(h=1)^T |A_h|/E,
    I=sum_a w_a log|Res(P,F_a)|/d.                   (5)

Each resultant here contains all d original labels and the complete integer auxiliary.
One does not add several incomes and then charge only one polynomial's coefficients: the weighted average and its combined energy are both explicit.

**Theorem 1.** Whenever0<u=Tm/d<=h_0,

    I <= log(E)/2+u
             +log[1+kappa(epsilon(u)+2u)]/2.          (6)

If A_h=0 for every h>=1, the sharper bound

    I <= log(E)/2+Tm/d                              (7)

holds for EVERY m>0, without any discrepancy hypothesis or restriction u<=h_0.

*Proof.* Set B_(a,i)=F_a(alpha_i)/max(1,r_i)^T.
By nonvanishing all are nonzero, and the exact resultant identity and(1) give

    I=u+sum_a w_a d^-1 sum_i log|B_(a,i)|.

Concavity of log, first or jointly over the weights w_a/d, gives an upper bound of u+(1/2)log[d^-1 sum_i sum_a w_a |B_(a,i)|^2].
Equations(3)--(4), AFTER summing the signed coefficients over a, bound this last average by E+2(epsilon(u)+2u)sum_h|A_h|.
This proves(6).
When all A_h vanish, summing(3) gives sum_a w_a|B_(a,i)|^2<=E separately for each original i, proving(7) with no use of(4).

This proves the entire theorem for arbitrary signs, arbitrary auxiliary contents, arbitrary coefficient heights and arbitrary finite r.
It does not assume independence between different roots, different frequencies, different primes or different auxiliary polynomials.

An equivalent description of the exact cancellation condition in(7) is

    sum_a w_a |F_a(exp(i theta))|^2=E
                         for every real theta.       (8)

This follows from uniqueness of the finite Fourier coefficients.
It is the precise meaning of a complementary bundle here; no imported construction of such integer polynomials with the required arithmetic income is asserted.

**Fully charged conditional gap.** Fix C>0 and eta>0.
Suppose a class of actual inputs admits bundles above with T<=Cd, arithmetic lower income J<=I, and J-log(E)/2>=eta.
If the bundle is exactly complementary, (7) gives m>=eta/C.
More generally if kappa<=K for one uniform K, choose u_*>0 with u_*<=h_0 and u_*+(1/2)log[1+K(epsilon(u_*)+2u_*)]<eta.
Then no input has m<=u_*/C, by(6) and monotonicity.
Along a hypothetical sequence with m tending to zero, positive uniform surplus is likewise impossible when kappa(epsilon(Cm)+2Cm) tends to zero.
Individual supports, individual effective supports and the number of auxiliaries need not be bounded.
The missing coverage is the existence of bundles satisfying the joint arithmetic AND coherence requirements on those actual inputs.

For example J may be the weighted sum of the L229 actual truncated prime-depth certificates for each F_a separately.
A certificate s_(a,p,i) gives J=sum_a w_a sum_p(log p)sum_i s_(a,p,i)/d.
Every certificate must refer to its own F_a and original roots.
This combines inequalities; it is not the resultant of an imaginary common polynomial.
Modulus truncation, ramification, repeated reduction and actual-order hypotheses remain exactly as in L229.
If F_a=c_a G_a, its income changes by log c_a and its energy and autocorrelations by c_a^2.
All those changes must be made simultaneously; separate primitive normalizations do not preserve(5) with the old weights and energy.

<a id="all-residual-columns-signed-diagonal-coherence"></a>
### 4. An actual all-column construction with a square-root dimension cost

Choose an integer N>d and let A be the N-by-(N-d) coefficient matrix whose columns are P,tP,...,t^(N-d-1)P in the full degree window0,...,N-1.
Its columns are independent because P is monic.
Put

    R=I_N-A(A^T A)^(-1)A^T.                         (9)

This is the rational orthogonal projection onto the orthogonal complement of the actual polynomial multiples.
Its rank and trace are d, and R^2=R=R^T.
This is the exact L237 construction extended from N=2d by the same displayed matrix identity, not an assertion of a new existence principle.

Take one positive integer q clearing the denominators of R and of(A^T A)^(-1)A^T.
For EVERY0<=j<N, let F_j have coefficient vector q R e_j.
Then for an actual integral polynomial U_j,

    F_j=q t^j-P U_j,
    F_j(alpha_i)=q alpha_i^j,
    |Res(P,F_j)|=q^d.                               (10)

The actual unit norm has absolute value1; no equality of powered degree with d is assumed.
Each F_j is nonzero because alpha_i is nonzero.
Every original p-adic root has valuation exactly v_p(q).
These are actual simultaneous integer auxiliaries on the SAME P, degree at most T=N-1, with one genuine common scalar.
Their individual contents divide q by L237's exact actual-order argument.
We retain those contents in(10) and charge their entire coefficients; making all columns individually primitive while keeping the old bundle weights would be invalid.

Use all N polynomials with weights1/N.
Projection multiplication gives the exact aggregate quantities

    E=q^2 d/N,
    A_h=(q^2/N) a_h,
    a_h=sum_(j=0)^(N-1-h) R_(j,j+h),
    kappa_R=(2/d) sum_(h=1)^(N-1)|a_h|,
    I=log q, I-log(E)/2=log(N/d)/2.                (11)

For the autocorrelation equality, sum over the column index in R_(j,k)R_(j+h,k) equals(R^2)_(j,j+h)=R_(j,j+h).
Thus all cancellations are in the signed diagonal sums of the actual projection, not in unrelated freely chosen directions.
The full scalar q cancels in the normalized surplus and in kappa_R; its magnitude and all actual coefficients remain paid in I and E.

**Theorem 2.** Every actual residual projection(9) satisfies

    0<=kappa_R<=sqrt[(N-1)(N-d)/d].                  (12)

Whenever0<u=(N-1)m/d<=h_0 it additionally satisfies

    kappa_R[epsilon(u)+2u]>=(N/d) exp(-2u)-1.        (13)

*Proof of(12).* On each upper diagonal use Cauchy--Schwarz, then use it across the diagonals:

    sum_h |a_h|
      <=sum_h sqrt[(N-h) sum_j R_(j,j+h)^2]
      <=sqrt[(N(N-1)/2) sum_(j<k) R_(j,k)^2].

Since R is a symmetric projection, sum_(j,k)R_(j,k)^2=trace R=d, whence sum_(j<k)R_(j,k)^2=(d-sum_jR_(j,j)^2)/2.
Its diagonal squares sum to at least d^2/N because their sum is d.
Substitution and multiplication by2/d yield exactly(12).
All inequalities hold for the actual rational matrix, without a generic-matrix or random-sign assumption.

*Proof of(13).* Insert(11) in(6), subtract log q, and exponentiate.
The result is exp(-2u)<=(d/N)[1+kappa_R(epsilon(u)+2u)], which is equivalent to(13).

For N=ceil(Cd) with any fixed C>1, (12) is O_C(sqrt d), whereas bounding the individual effective supports only gives O_C(d).
This is a genuine cancellation gain obtained on a fully specified integer auxiliary bundle for EVERY original input.
It does not bound kappa_R independently of d.
The direct finite necessary test is

    (N/d) exp(-2u)-1
      <=sqrt[(N-1)(N-d)/d] [epsilon(u)+2u].          (14)

If m tends to zero along any hypothetical sequence and N/d stays above1 by a fixed positive amount, (13) forces kappa_R to diverge.
Thus exact or uniformly bounded aggregate cancellation is excluded on that hypothetical sequence; it cannot be presumed from averaging the columns.
Conversely a uniform bound for these ACTUAL signed diagonal sums would imply a gap by Theorem1, with surplus log(N/d)/2 and T/d bounded.
The question has moved to a concrete signed projection quantity; no such uniform bound is proved here.
Formula(14) is a weaker degree-dependent constraint than strong established general Mahler estimates and is not presented as a new optimal degree bound.

Every original scalar, polynomial leading coefficient, primitive content and root factor is retained in(10)--(11).
The original measure m is TOTAL and u=(N-1)m/d, with N proportional to actual d.
The number of bundled polynomials is N and the matrix dimension is N; no running-time bound independent of d or cheap common denominator is claimed.
The companion/cover constructions of the separate structural route play no role in this arithmetic statement.

<a id="common-filter-cancellation-obstruction"></a>
### 5. An exact obstruction to a superficial complementary construction

One tempting recipe is to keep a single expensive auxiliary F and multiply it by a complementary family of filters G_a.
Suppose positive weights sum to1 and

    sum_a w_a |G_a(z)|^2=K>0 for every |z|=1.

Then the bundle H_a=F G_a has aggregate circle square exactly K|F(z)|^2.
Its energy is K E_F and its nonconstant aggregate Fourier coefficients are K A_h(F), so its normalized kappa is exactly the original single-polynomial value2sum_h|A_h(F)|/E_F.
Therefore such multiplication does not improve the signed coherence at all.
In particular monomial shifts and sign repetitions do not create a new cancellation mechanism.
The full degree cost increases by the actual filter degrees, and every resultant obeys Res(P,F G_a)=Res(P,F)Res(P,G_a); those additional norms cannot be assigned for free.

This obstruction is a complete polynomial identity, not an unsuccessful bounded search.
General mixtures of genuinely different auxiliary directions are not covered by it.
The all-column construction in Section4 uses different actual monomial residues and therefore has its own aggregate matrix identity(11), rather than being declared successful through common-filter cancellation.
More general integer polynomial matrix transformations would require their actual circle identity, arithmetic income and degree costs to be checked separately.

There is also an exact ALL-INPUT control showing that complementarity by itself does not create the missing arithmetic surplus.
For any positive integer h take the two primitive polynomials F_+=1+t^h and F_-=1-t^h with equal weights.
They are nonvanishing on every nontorsion irreducible input P, have T=h, and satisfy

    (|F_+(z)|^2+|F_-(z)|^2)/2=2 for |z|=1,
    E=2, kappa=0,
    I=log Z_(2h)/(2d),
    Z_(2h)=|Res(P,t^(2h)-1)|.                       (15)

The resultant equality is multiplication of the two COMPLETE resultants, because F_+ F_-=1-t^(2h), and all original roots remain present.
The leading signs have modulus1 and both polynomials have content1; their actual coefficient norms, degrees and both cyclic factors are paid.
The [L168 uniform original cyclic cost](Yin_C_G0391_v1.md#bounded-power-degree-escape), with its retained powered-degree and source boundaries, gives log Z_(2h)/d=o(1) uniformly for h<=Cd along any hypothetical positive-total-m sequence tending to zero.
Thus the surplus in this perfectly complementary family tends to -log(2)/2.
This rules out that entire degree-linear binomial-pair recipe as a positive-surplus near-one construction; it is not a control with fixed or growing positive measure, nor a refutation of genuinely different complementary arithmetic bundles.

<a id="simultaneous-coherence-scope-self-check"></a>
### 6. Scope, failures and complete self-check

An initial possibility was to extend L315's pivot inequality to arbitrary row-space seeds.
That would mainly restate a necessary growth conclusion without changing the coefficient/conjugate mechanism, so it was not developed as a result.
The changed step here is the Poisson majorant with signed aggregate autocorrelation, followed by the actual all-column identity and square-root dimension bound.
The common-filter recipe's precise failure is retained in Section5.
No claim of exact complementary arithmetic coverage, uniform kappa_R, near-one input existence or unrestricted gap is made.
The unrestricted Task remains unresolved; its current execution is paused.


The original complete author checking account is retained at [R785](../audits/reviews/Yin_R_G0785_v1.md#original-bundle-projection-author-self), on the original Sections1–7/equations1–15, with its separate checking minute unrecorded.

<a id="simultaneous-coherence-source-freeze"></a>
### 7. Source attribution and freeze disposition

The new attribution is [ABR01's selected Poisson inspection](../audits/literature/ABR01/readme.md#selected-poisson-attribution): Axler--Bourdon--Ramey, Harmonic Function Theory, second edition(2001), retained author PDF bearing17July2020.
Root read printed pp.12--15/PDF20--23, formulas1.15--1.16, Theorem1.17, Proposition1.20 and Theorem1.21 with their displayed arguments, and visually checked PDF20,22,23.
The exact disk specialization supplies positivity, unit mass and harmonic reproduction.
Root did not recursively audit the cited maximum principle or earlier mean-value inputs, and no whole-book audit is claimed.
This author read that canonical inspection record, not a fresh PDF copy.
Its role is classical-method attribution; the polynomial square estimate, real-coefficient reversal, signed aggregate bounds and actual arithmetic construction are proved locally in full.
No uninspected general subharmonic theorem or external arithmetic projection theorem is a mathematical premise.
The elementary complementary identity(8) is defined and proved by finite Fourier expansion, and no Golay, filter-bank or other external construction theorem is imported.

The author completed the entire self-check and froze Sections1--7, equations(1)--(15), all conditional statements, failed recipes and source limitations at2026-10-10T10:37.
The original subsequent whole noncontributor finding is retained in [R785](../audits/reviews/Yin_R_G0785_v1.md#simultaneous-coherence-complete-independent-review), on that exact author freeze.
No unresolved mathematical step or source identification remains at this local scope; fixed adoption and the unrestricted Task are distinct subsequent matters.
The material check verifies repository form and links only and is not mathematical proof evidence.




## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:32 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete accepted original-root angular/energy/projection interfaces](Yin_C_G0570_v1.md#statement) | Exact source epsilon/frequency domain, original root/prime/content accounting and actual rational monomial projection only; determinant optimum is a separate functional. |
| dependency | [Full actual cyclic-cost proof](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear window cyclic norm decay with actual powered-degree escape and adopted source boundaries, for the complete binomial-pair negative recipe. |
| support | [Selected-pivot predecessor](Yin_C_G0597_v1.md#statement) | Necessary actual TOTAL-small-measure pivot growth only; no bounded coefficients or generic coverage used as premise. |
| support | [Original complete author input](../ledger/Yin_L_G0318_v1.md#complete-retained-proof-and-review) | Entire signed bundle/projection/failed-recipe proof and real source/author/freeze history. |
| support | [Original full finding](../audits/reviews/Yin_R_G0785_v1.md#simultaneous-coherence-complete-independent-review) | Exact22109-byte2026-10-10T10:37 original input checked2026-10-10T10:39, with original relationship limits; not a finding on this C. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:37 |
| status | proved |
| reason | Actual ENTIRE current Statement and COMPLETE original Argument have been read and checked in current whole SELF, preserving all real original inputs, repairs, source/native/negative limits and conditional rather than achieved coverage; no historical independent finding is expanded to this physical C. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete accepted original-root angular/energy/projection interfaces](Yin_C_G0570_v1.md#statement) | Exact source epsilon/frequency domain, original root/prime/content accounting and actual rational monomial projection only; determinant optimum is a separate functional. |
| dependency | [Full actual cyclic-cost proof](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear window cyclic norm decay with actual powered-degree escape and adopted source boundaries, for the complete binomial-pair negative recipe. |
| support | [Selected-pivot predecessor](Yin_C_G0597_v1.md#statement) | Necessary actual TOTAL-small-measure pivot growth only; no bounded coefficients or generic coverage used as premise. |
| support | [Original complete author input](../ledger/Yin_L_G0318_v1.md#complete-retained-proof-and-review) | Entire signed bundle/projection/failed-recipe proof and real source/author/freeze history. |
| support | [Original full finding](../audits/reviews/Yin_R_G0785_v1.md#simultaneous-coherence-complete-independent-review) | Exact22109-byte2026-10-10T10:37 original input checked2026-10-10T10:39, with original relationship limits; not a finding on this C. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0767_v1.md#whole-signed-bundles-projection-self) | Every actual original-degree unit/root/weight/window domain, exact small-u versus all-m complementary theorem, FULL original Sections1--7/equations1--15, all projection/scalar/prime/content/coherence/conditional-gap costs and BOTH complete negative recipes, exact source/freeze/author limits. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete accepted original-root angular/energy/projection interfaces](Yin_C_G0570_v1.md#statement) | Exact source epsilon/frequency domain, original root/prime/content accounting and actual rational monomial projection only; determinant optimum is a separate functional. |
| dependency | [Full actual cyclic-cost proof](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear window cyclic norm decay with actual powered-degree escape and adopted source boundaries, for the complete binomial-pair negative recipe. |
| support | [Selected-pivot predecessor](Yin_C_G0597_v1.md#statement) | Necessary actual TOTAL-small-measure pivot growth only; no bounded coefficients or generic coverage used as premise. |
| support | [Original complete author input](../ledger/Yin_L_G0318_v1.md#complete-retained-proof-and-review) | Entire signed bundle/projection/failed-recipe proof and real source/author/freeze history. |
| support | [Original full finding](../audits/reviews/Yin_R_G0785_v1.md#simultaneous-coherence-complete-independent-review) | Exact22109-byte2026-10-10T10:37 original input checked2026-10-10T10:39, with original relationship limits; not a finding on this C. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0785_v1.md#signed-bundle-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R785. |

