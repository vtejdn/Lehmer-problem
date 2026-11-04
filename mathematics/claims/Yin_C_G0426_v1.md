---
author: Yin
---

# Complete unrestricted reciprocal derivative-multiplicity and critical-value constraints

This retains the complete necessary mathematical argument from [the entire original L376 unrestricted critical account](../ledger/Yin_L_G0376_v1.md#nonreal-critical-reuse-and-source).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion of actual degree d=2s>=4 and constant coefficient1, and let P(z)=z^s Q(z+z^(-1)), with Q monic irreducible integral of degree s.
Its trace roots x_j are distinct, may be nonreal, and avoid+/-2; no actual circle conjugate is required.
Choose one member alpha_j=exp(ell_j+i theta_j), ell_j>=0, from every original inverse pair, so total m=log M(P)=sum_j ell_j>0.
Let beta_1,...,beta_(s-1) be all roots of Qprime with multiplicities, and r_max the largest such multiplicity.
Every beta is the positive barycenter sum_j x_j/|beta-x_j|² divided by sum_j1/|beta-x_j|².
In particular |x_j|,|beta_j|<=R=2cosh(m), sum_j|Im x_j|<=2sinh(m), and projection y_j=clamp(Re beta_j,-2,2) satisfies |beta_j-y_j|<=4sinh(m); the projection is only a positive comparison measure.

With p_k=sum x_j^k and pprime_k=sum beta_j^k, the finite formal identities and bounds hold for every integer k>=1:

    pprime_k=p_k-k[t^k]log(1+sum_(j>=1)(p_j/s)t^j),
    |pprime_k-p_k|<=(2^k-1)R^k,
    |pprime_k/(s-1)-p_k/s|<=(2R)^k/(s-1).

Let C_0=2,C_1=x,C_(k+1)=xC_k-C_(k-1), and a_k=d^(-1)sum_(i=1)^d(alpha_i/|alpha_i|)^k over all original conjugate labels.
For0<m<=1 the complete normalized Chebyshev transfer, projection and radial bounds are respectively2*16^k/(s-1),2k8^k sinh(m), and2|a_k|+2sinh(km)/s as in(5)--(7).
All multiplicities and the s versus s-1 normalization are retained.

Use the accepted increasing angular error from the exact original-powered-label interface L229:

    c_ang=log(2)/4, h_0=c_ang exp(-20),
    b(h)=max(h,sqrt(h/c_ang)log(sqrt(c_ang/h))),
    epsilon(h)=min(1,15sqrt(b(h))+4h), 0<h<=h_0.

For any integer L>=2 with0<m<=1 and h=(L-1)m/d<=h_0 define

    B_L=2epsilon(h)+2sinh((L-1)m)/s
       +2*16^(L-1)/(s-1)+2(L-1)8^(L-1)sinh(m).

Then every real or nonreal actual derivative-root multiplicity obeys

    r_max/(s-1)<=min(1,2/L+((L-1)/L)B_L)
                <=min(1,2/L+(L-1)B_L).

The exact positive symmetrized projected Fejer law counts all repeated roots and endpoint atoms.
If L=floor((1/2)min(log(s-1)/log(16),log(1/m)/log(8)))>=2 and the same h-domain holds, the sharper fully paid refinement is

    r_max/(s-1)<=2/L+2epsilon(h)+2Lm cosh(1)/s
                     +2/sqrt(s-1)+2L cosh(1)sqrt(m).

Outside those explicit growing-test guards use an actually permitted fixed L.
Along any hypothetical sequence of actual inputs in this full domain with m(P)->0, fixed-degree finiteness gives s->infinity and the fixed-L-first argument yields r_max/(s-1)->0.
Equivalently, each eta>0 has a positive small-total-measure threshold excluding r_max>=eta(s-1); no such sequence is constructed and no uniform numeric threshold is supplied.

For the original phase phi=arccos(2Q(2cos(theta))²/H²-1), H=sum|p_j|, let M be its canceled first-derivative order and r the multiplicity of a real root of Qprime, with r=0 when Qprime does not vanish.
Its complete local orders are: interior simple Qzero, M=0; interior nonzero Q with Q²<H², M=r; interior H² maximum, M=(r-1)/2 with r+1 even; endpoint+/-2 with Q²<H², M=2r+1; endpoint H² value, M=r.
These include one-sided cusp cases, and2M is the multiplicity of the actual gcd-canceled squared derivative.
Every actual order satisfies M<=2r_max+1, hence max M/d->0 on the hypothetical near-one sequences, with the separate no-critical-root branch preserved.
No fixed positive oscillatory exponent follows from sublinear M.

The complete primitive factorization Qprime=g product_j R_j^(r_j), with positive integer content g, primitive positive-leading a_j, and e_j=deg R_j, satisfies sum r_j e_j=s-1 and g product a_j^(r_j)=s.
Thus a_j^(r_j)<=s and r_j>log(s)/log(2) forces a_j=1.
The full critical-value polynomial is

    Delta_Q(Y)=Res_x(Q(x)-Y,Qprime(x))
              =s^s product_(Qprime(beta)=0)(Q(beta)-Y),
    deg Delta_Q=s-1, lead Delta_Q=(-1)^(s-1)s^s,
    0!=Delta_Q(0)=g^s product_j Res(Q,R_j)^(r_j).

For beta a root of primitive R of degree e/multiplicity r/leading a_R, v=Q(beta)!=0, f=[Q(v):Q], and primitive integer minimal polynomial V of v with positive leading a_V, one has f divides e,

    V^(r e/f) divides Delta_Q in Z[Y],
    Res(Q,R)=(-1)^(s e)a_R^s[(-1)^f V(0)/a_V]^(e/f),
    (r+1)e/f<=s.

All field fibers, signs, denominators and coincident values remain charged.
The complete height bounds are M(Q)<=2^s exp(m), ||Q||_1<=3^s exp(m), ||Qprime||_1<=s3^s exp(m), sum r_j log M(R_j)<=log(s)+s log(3)+m-log(g), and ||Delta_Q||_1<=s^s(1+(4cosh(m))^s)^(s-1).
An unevaluated nonzero integer critical-value resultant supplies no positive original income.

If c_NR>0 is the even number of nonreal trace roots, the full polynomial discriminant satisfies

    1<=|disc Q|<=(4s)^s exp(2(s-1)m)(2sm/c_NR)^(c_NR).

For0<m<=1 this gives m>=(c_NR/(2s))(4s)^(-s/c_NR)exp(-2(s-1)/c_NR).
Every real critical point of multiplicity r has r<=c_NR+1 by multiplicity-counted Rolle, and for r>=2 it consequently obeys

    m>=((r-1)/(2s))(4s)^(-s/(r-1))exp(-2(s-1)/(r-1)).

These are degree-paid bounds on actual nonreal pairs and real critical points, not a reduction to all-real trace roots.
Finally, if s>=3 and one derivative root has multiplicity s-1, it is an integer a, Q=(x-a)^s+c_0 with nonzero integer c_0, and total m>=log(2), M(P)>=2.
The s>=3 rational-denominator guard is essential.

The entire derivation preserves original degree, total measure, all inverse pairs and powered multiplicities, full original phase/gcd factors, all finite-frequency/radial/coefficient errors and source-proof boundaries.
Hou16 supplies checked Gauss--Lucas attribution with the supporting-line boundary guard; the complete barycenter proof is local.
No near-one family, absolute multiplicity bound, fixed exponent, uniform conditioning, useful degree-linear cutoff, original norm surplus, native computation or unrestricted Mahler gap is established.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:15 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact irreducible reciprocal trace domain](Yin_C_G0243_v1.md#statement) | Only unique monic integral irreducible trace Q of actual degree s, distinct full inverse pairs and endpoint exclusion; no total-reality or powered-degree-preservation assumption. |
| dependency | [Exact original canceled-phase interface](Yin_C_G0398_v1.md#exact-phase-critical-cancellation) | Only original phase/gcd and positive finite Fejer mechanism; every arbitrary-nonreal-trace local order and new finite derivative transfer is proved here, with the no-critical branch preserved. |
| dependency | [Exact actual-powered-label angular bound](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Only the explicitly stated increasing epsilon(h), h<=h0 and all original powered multiplicities, with Pri11/Dim19 accepted versions/proof-inspection limits; no recursive new source audit. |
| dependency | [Measure conventions and finite degree](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only total multiplicative/logarithmic measure, original degree and elementary monic-integer bounded-degree finiteness, not a new finite scan. |
| support | [Complete discriminant method comparison](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Only classical full-polynomial Vandermonde/Hadamard mechanism and degree costs; all new trace-pair columns and bounds are derived locally without field-discriminant substitution or omitted degree logarithm. |
| support | [Exact selected Gauss Lucas attribution](../audits/literature/Hou16/Yin_U001.md#hou16-u001) | Only checked slides25–26 statement/mechanism with the supporting-line boundary guard and exact original reading depth; full barycenter confinement is proved locally without an unseen source premise. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:19 |
| status | proved |
| reason | Adopt after actual entire current SELF inspection of all original inverse-pair total measure, repeated-root confinement, full finite Newton/Chebyshev/projection and angular transfer, fixed/growing-test quantifiers, full canceled-phase orders, primitive critical-value/resultant/field/height arithmetic, degree-paid nonreal discriminant and maximal-degeneracy log2 argument. Preserve all source-depth, no-uniformity and no-execution boundaries; original R204 whole author-check exposure remains SELF without enlarging its history. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#statement) | Only unique monic integral irreducible trace Q of actual degree s, distinct full inverse pairs and endpoint exclusion; no total-reality or powered-degree-preservation assumption. |
| dependency | [Exact accepted input](Yin_C_G0398_v1.md#exact-phase-critical-cancellation) | Only original phase/gcd and positive finite Fejer mechanism; every arbitrary-nonreal-trace local order and new finite derivative transfer is proved here, with the no-critical branch preserved. |
| dependency | [Exact accepted input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Only the explicitly stated increasing epsilon(h), h<=h0 and all original powered multiplicities, with Pri11/Dim19 accepted versions/proof-inspection limits; no recursive new source audit. |
| dependency | [Exact accepted input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only total multiplicative/logarithmic measure, original degree and elementary monic-integer bounded-degree finiteness, not a new finite scan. |
| support | [Exact support](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Only classical full-polynomial Vandermonde/Hadamard mechanism and degree costs; all new trace-pair columns and bounds are derived locally without field-discriminant substitution or omitted degree logarithm. |
| support | [Exact support](../audits/literature/Hou16/Yin_U001.md#hou16-u001) | Only checked slides25–26 statement/mechanism with the supporting-line boundary guard and exact original reading depth; full barycenter confinement is proved locally without an unseen source premise. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0628_v1.md#current-unrestricted-critical-whole-finding) | Entire precise current unrestricted reciprocal-unit Statement and complete necessary original Sections1–9/equations(1)–(20), explicit growing-L refinement, all original root multiplicities and finite/degree/source/normalization/cost guards. Actual whole relationship is self-reviewed, with original full author check and original R204 actual SELF separately retained. |

## Complete retained argument

<a id="argument"></a>
<a id="unrestricted-reciprocal-critical-constraints"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="nonreal-critical-reuse-and-source"></a>
## 1. Exact reuse, changed result and classical attribution

The complete [L368 canceled-phase certificate and broad obstruction](../ledger/Yin_L_G0368_v1.md#exact-phase-critical-cancellation) and [L369 Salem interlacing specialization](../ledger/Yin_L_G0369_v1.md#salem-interlacing-critical-orders) were read.
L368's broad P_n=(1+z)^(2n)+z^n is squarefree and reciprocal but has no near-one or irreducibility assertion.
L369 exhausts critical orders only when all trace roots are real.
The present argument retains ACTUAL irreducibility and arbitrary nonreal trace roots and does not adopt either broader implication.
[L366](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) was searched/read at its exact complex-outside-root separation interface; no uniform critical multiplicity follows from its paid distances.
[Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) supplies measure conventions and elementary fixed-degree finiteness.
[Smy08-U003](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation) supplies the existing discriminant/cofactor mechanism and its degree subtraction.
[L229](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) is the actual accepted small-height/angular input, with all original powered multiplicities and its Pri11/Dim19 proof-inspection limits retained.

The changed conclusion proved below is a necessary unrestricted-core obstruction: along ANY hypothetical sequence of these actual inputs with total m(P)->0, the largest multiplicity of ANY root of the actual Q' is o(deg Q), and the largest actual canceled phase multiplicity is o(deg P).
This still permits unbounded multiplicities and does not give a fixed positive oscillatory exponent.
An explicit finite bound, a degree-paid nonreal-discriminant bound and a complete arithmetic critical-value diagnostic are retained.
A separate maximal-degeneracy argument gives M(P)>=2 for a single real critical point of multiplicity s-1 when s>=3.

The classical convex-hull mechanism is Gauss--Lucas.
A bounded primary search located Bob Hough, *Math141: Lecture12, The Fundamental Theorem of Algebra and properties of polynomials*, explicitly dated17October2016,26pages, [author-hosted primary PDF](https://www.math.stonybrook.edu/~rdhough/mat141-fall16/lectures/lecture12.pdf).
Its statement and proof on printed/PDFpp.25--26 were directly text-read; the title/date are explicit in the PDF, not inferred from its path.
The complete local barycenter proof needed below is supplied, so the source provides checked classical attribution rather than an uninspected mathematical premise.
No visual or whole-lecture audit is claimed.
Root coordinates canonical source registration/locators; the acquired selected source is now recorded at [Hou16-U001](../audits/literature/Hou16/Yin_U001.md#hou16-u001).
The Fejer kernel is the already checked exact elementary input in L368/Smy08, not a new external theorem.
The finite derivative-moment algebra is proved directly below; no priority claim is made for Gauss--Lucas, Newton identities, critical values or equidistribution.

<a id="actual-total-measure-trace-confinement"></a>
## 2. Actual inverse pairs and every derivative root, with total costs

Use the exact [L66 reciprocal trace domain](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain).
Let P be monic irreducible reciprocal nontorsion in Z[z], actual degree d=2s>=4, with constant coefficient1.
Write

    P(z)=z^s Q(z+z^-1), Q monic irreducible in Z[x], deg Q=s.

The actual trace roots x_1,...,x_s are distinct; Q(2)Q(-2)!=0, since an original endpoint root would contradict irreducible nontorsion P.
For each ORIGINAL inverse pair choose alpha_j=exp(ell_j+i theta_j), ell_j>=0, and its inverse.
Then

    m=log M(P)=sum_(j=1)^s ell_j>0,
    x_j=2cosh(ell_j)cos(theta_j)
                       +2i sinh(ell_j)sin(theta_j),
    |x_j|<=2cosh m,
    sum_j |Im x_j|<=2sinh m.                       (1)

The last inequality uses sum sinh(ell_j)<=sinh(sum ell_j), proved repeatedly from sinh(a+b)>=sinh a+sinh b for nonnegative a,b.
Thus small TOTAL measure pays the sum of all inverse-pair displacements; no average height replaces m.
No x_j is assumed real or in[-2,2], and no original circle conjugate is assumed to exist.

Let beta_1,...,beta_(s-1) be ALL roots of Q', counted with their actual multiplicities.
Since Q is squarefree, Q(beta)!=0 for any such beta.
Its logarithmic derivative gives sum_j1/(beta-x_j)=0.
Taking conjugates and using positive weights w_j=1/|beta-x_j|^2 proves

    beta=(sum_j w_j x_j)/(sum_j w_j).

Consequently every beta, repeated or not, lies in the convex hull of the trace roots.
In particular

    |beta|<=R:=2cosh m,
    |Re beta|<=2cosh m, |Im beta|<=2sinh m.          (2)

Project each beta to y=clamp(Re beta,-2,2).
This projection is used ONLY as a positive-measure comparison device; it does not replace an algebraic root in a norm or polynomial identity.
Equations(1)--(2) give

    y in[-2,2], |beta-y|<=4sinh m.                  (3)

Indeed the horizontal excess is at most2(cosh m-1)<=2sinh m and the vertical excess at most2sinh m.
No separation between beta and a trace root, no reality of Q' and no multiplicity-free derivative hypothesis is needed.

<a id="finite-derivative-moment-transfer"></a>
## 3. Complete finite moment transfer from Q to Q'

For k>=1 put p_k=sum_j x_j^k and p'_k=sum_j beta_j^k, retaining all multiplicities.
A formal expansion at infinity gives

    Q'(z)/s = [Q(z)/z] [1+sum_(k>=1) (p_k/s)z^-k],
    p'_k=p_k-k[t^k]log[1+sum_(j>=1)(p_j/s)t^j].

This is a finite coefficient identity at each k, obtained from Q'/Q=s/z+sum p_k z^(-k-1) and the factorizations of the two monic polynomials.
It involves no convergence or interchange of infinite input limits.
Since |p_j/s|<=R^j, the coefficient of the rth power contributes at most binom(k-1,r-1)R^k.
Therefore

    |p'_k-p_k|<=k R^k sum_(r=1)^k binom(k-1,r-1)/r
                 =(2^k-1)R^k,
    |p'_k/(s-1)-p_k/s|<=(2R)^k/(s-1).            (4)

The sum identity follows from binom(k-1,r-1)/r=binom(k,r)/k.
Normalization by s-1 rather than s is explicitly paid in the second line.

Let C_0=2,C_1=x,C_(k+1)=x C_k-C_(k-1), so C_k(z+z^-1)=z^k+z^-k.
The elementary coefficient l1 norm obeys ||C_k||_1<=2^(k+1) by this recurrence.
For 0<m<=1 we have2<=R<4.
Apply(4) coefficient by coefficient, with the constant-term normalized difference zero, to obtain

    |(s-1)^-1 sum_j C_k(beta_j)-s^-1 sum_j C_k(x_j)|
                              <=2*16^k/(s-1).      (5)

Along the segment between beta_j and its projection y_j, all moduli are at most4.
Polynomial differentiation and(3) give

    |C_k(beta_j)-C_k(y_j)|
       <=4sinh m * k*2^(k+1)*4^(k-1)
       =2k8^k sinh m.                             (6)

These are conservative explicit degree/height costs.
A large finite k is not free: the16^k/(s-1) and8^k sinh m terms remain charged.
In particular no derivative-root equidistribution theorem with an unproved quantitative constant is invoked.

For the original angular moment a_k=d^-1 sum_(i=1)^d (alpha_i/|alpha_i|)^k, direct inverse-pair comparison gives

    |s^-1 sum_j C_k(x_j)|
       <=2|a_k|+2sinh(km)/s.                       (7)

For each pair the discrepancy from2cos(k theta_j) has modulus at most2sinh(k ell_j); summing uses the SAME total m in(1).
All original angular labels occur, even if powering lowers degree or no roots lie exactly on the circle.

<a id="unrestricted-critical-atom-bound"></a>
## 4. Explicit multiplicity obstruction without all-real trace roots

Fix an integer L>=2, assume0<m<=1 and

    h=(L-1)m/d<=h_0,
    B_L=2epsilon(h)+2sinh((L-1)m)/s
          +2*16^(L-1)/(s-1)
          +2(L-1)8^(L-1)sinh m.                   (8)

L229 bounds every original |a_k| by epsilon(h) for1<=k<L.
Combining(5)--(7) bounds every normalized projected derivative Chebyshev moment by B_L.
Write y_j=2cos psi_j with psi_j in[0,pi], and let nu be the probability measure assigning mass1/[2(s-1)] to each of+psi_j and-psi_j, with repetitions counted.
Then |nu_hat(k)|<=B_L/2 for1<=k<L.

Use the exact positive Fejer polynomial

    F_L(t)=L^-1|sum_(j=0)^(L-1)exp(i j t)|^2
          =1+2sum_(k=1)^(L-1)(1-k/L)cos(k t).

It has F_L(0)=L and is nonnegative everywhere.
A root beta of Q' of multiplicity r projects to one y and one angle psi; nu assigns at least r/[2(s-1)] to that angle.
This lower atom bound also holds at psi=0,pi, where symmetrized masses coincide and the actual atom is larger.
Therefore

    Lr/[2(s-1)]<=integral F_L(psi-t)dnu(t)
       <=1+B_L sum_(k=1)^(L-1)(1-k/L)
       =1+(L-1)B_L/2.

Consequently the maximum multiplicity r_max of ANY actual root of Q', real or nonreal, satisfies

    r_max/(s-1)<=min{1,2/L+[(L-1)/L]B_L}
                 <=min{1,2/L+(L-1)B_L}.           (9)

The stronger first form follows from the exact sum; the second looser form is retained for a simple comparison gate.
The atom argument uses positivity after the actual finite moment transfer, and no independent random-phase model or original circle-root assumption.

One explicit growing-test choice is available without suppressing its costs.
If

    L=floor[(1/2)min{log(s-1)/log16,log(1/m)/log8}]>=2

and h in(8) is in the accepted domain, then16^L/(s-1)<=(s-1)^-1/2 and8^L m<=sqrt(m).
Also Lm<=m log(1/m)/(2log8)<1, so sinh((L-1)m)<=L m cosh1 and sinh m<=m cosh1.
The stronger form of(9) gives the fully explicit bound

    r_max/(s-1)<=2/L+2epsilon(h)
          +2L m cosh1/s+2/sqrt(s-1)+2L cosh1 sqrt(m).

This is an input-dependent logarithmic quantitative refinement, not an arbitrary growing-frequency limit exchange.
Outside its L>=2 or h<=h_0 conditions use(9) at an actually permitted fixed L.
Neither form gives a fixed absolute multiplicity bound.

Now suppose a sequence of ACTUAL inputs in this domain has m(P)->0.
Elementary fixed-degree finiteness forces s->infinity: bounded degree and M(P)<2 leave finitely many monic integer coefficient lists, and their positive measures have a positive minimum.
For each fixed L, h->0 and EVERY term of B_L tends to zero.
The accepted epsilon tends to zero.
Taking limsup in(9) for a fixed L gives at most2/L, and letting that chosen integer L increase afterward proves

    r_max/(s-1)->0.                                (10)

This sequence of quantifiers does not exchange a growing-frequency estimate with an input limit.
Equivalently, for every eta>0 there is an actual small-total-measure threshold excluding r_max>=eta(s-1) in this entire irreducible reciprocal-unit domain.
Its existence uses fixed-degree finiteness for the bounded s left by the explicit finite bound.
No small-total-measure family is constructed or assumed to exist.

<a id="general-canceled-phase-orders"></a>
## 5. Exact general phase orders and what the new bound does not prove

Use L368's ACTUAL original phase, H=sum|P_j| and

    phi(theta)=arccos(2Q(2cos theta)^2/H^2-1).

Let r be the multiplicity of a real root x of Q', with r=0 when Q'(x)!=0.
Q has only simple roots and no roots at+/-2.
The same explicit local expansions as L368 give the complete order account without real-root interlacing:

- At an interior circle angle where Q(x)=0, Q'(x) and x' are nonzero; the cusp is linear and its canceled order is M=0.
- At an interior critical x in(-2,2) with Q(x)!=0 and Q(x)^2<H^2, the phase change has exact order r+1, so M=r.
- At an interior Q(x)^2=H^2 maximum, r+1 must be even by real nonnegativity; the phase has order(r+1)/2 and M=(r-1)/2.
- At either angular endpoint x=+/-2 with Q(x)^2<H^2, x-x_0 has order2, so M=2r+1.
- At either angular endpoint with Q(x)^2=H^2, the phase has order r+1, so M=r.

All other interior points have nonzero derivative and M=0.
These are one-sided phase orders where appropriate, and twice M is the multiplicity of the exact gcd-canceled squared derivative.
No smooth passage through a cusp is assumed.
Thus every actual canceled circle-phase order obeys

    M<=2r_max+1,
    max M/d->0 along the hypothetical near-one sequences in(10). (11)

If there are no canceled phase zeros, L368's separate no-critical-root branch applies instead.
Sublinear M is NOT a uniform upper bound for M: it is consistent with M growing, for example at square-root order.
Hence no fixed positive exponent1/(M+1), uniform K_P, useful degree-linear moment cutoff or unrestricted gap follows from(9)--(11).
All of L368's canceled polynomial, leading factor, off-circle factors, separations and full coefficient constant remain paid.
L369's fixed quarter exponent on all-real genuine Salem traces remains a different, stronger conclusion within its smaller domain.

<a id="critical-factor-and-value-account"></a>
## 6. Repeated factors and critical values: full arithmetic diagnostics

Factor the ACTUAL derivative over Z[x] as

    Q'=g product_j R_j^(r_j),
    g>0 the integer content,
    R_j primitive irreducible with positive leading a_j,
    e_j=deg R_j,
    sum_j r_j e_j=s-1, g product_j a_j^(r_j)=s.     (12)

These are exact Gauss-lemma/leading-coefficient identities, not monic-factor assumptions.
In particular a_j^(r_j)<=s; a repeated factor with r_j>log(s)/log2 must be monic.
A real phase-critical point of multiplicity r has all conjugates repeated to that same order, and r deg(R)<=s-1.
A large multiplicity is therefore not an independent free local parameter.

Define the complete critical-value polynomial

    Delta_Q(Y)=Res_x(Q(x)-Y,Q'(x)) in Z[Y]
              =s^s product_(Q'(beta)=0) (Q(beta)-Y),
    deg Delta_Q=s-1,
    lead Delta_Q=(-1)^(s-1)s^s,
    Delta_Q(0)=Res(Q,Q')!=0.                       (13)

All derivative roots and multiplicities occur.
The product formula has no sign from swapping the two resultant arguments because s(s-1) is even.
Delta_Q(0) is the signed polynomial-discriminant value, not a number-field discriminant or a selected original norm.
The exact factor product is

    Delta_Q(0)=g^s product_j Res(Q,R_j)^(r_j).

For a root beta of one primitive R, put v=Q(beta)!=0, e=deg R, f=[Q(v):Q], and let V(Y) be the primitive integer minimal polynomial of v with positive leading a_V.
Then f divides e.
Every conjugate critical value has e/f conjugate roots of this R above it, so

    V(Y)^(r e/f) divides Delta_Q(Y) in Z[Y],
    Res(Q,R)=(-1)^(s e) a_R^s
                [(-1)^f V(0)/a_V]^(e/f),
    (r+1)e/f<=s.                                  (14)

The divisibility is at least that multiplicity, since other critical factors may yield the same value.
The norm identity follows first for Res(R,Q)=a_R^s product Q(beta), then swaps arguments with the displayed sign.
For the last inequality, over Q(v) every one of its e/f conjugate beta roots is a root of Q(x)-v of multiplicity r+1; their distinct factors consume that much of the actual degree s.
Thus the full critical-value field and every ramification multiplicity remain visible.
An assertion that a critical value is a unit requires the actual integer norm and leading denominators in(14), not merely a small selected value.

All heights are still paid.
From the actual inverse pairs,

    M(Q)<=2^s exp(m), ||Q||_1<=3^s exp(m),
    ||Q'||_1<=s3^s exp(m),
    sum_j r_j log M(R_j)
                    <=log s+s log3+m-log g.         (15)

Indeed max(1,|x_j|)<=2exp(ell_j), and1+|x_j|<=1+2cosh ell_j<=3exp(ell_j).
Expand the product defining Q for the coefficient bound, then use M(Q')<=||Q'||_1 and exact multiplicativity with the retained content g.
For every critical beta, (2) gives |Q(beta)|<=[4cosh m]^s.
Accordingly

    ||Delta_Q||_1<=s^s(1+[4cosh m]^s)^(s-1).

These exponential-in-degree costs prevent treating a small original m as a small trace-polynomial or critical-value height.
Nonzero integer resultants in(13)--(14) may equal units; merely raising them to r does not create positive original arithmetic income.
No critical-value resultant has been evaluated here, and none replaces the complete original norm or L368's conditioning constant.

<a id="nonreal-trace-discriminant-cost"></a>
## 7. A degree-paid nonreal-trace obstruction

Let c>0 be the number of NONREAL roots of Q, counted once because Q is squarefree; c is even.
Write them in c/2 conjugate pairs.
The paired inverse radial parameters are equal, and the sum of one ell from each such pair is at most m/2.

Use the monic integer polynomial basis1,C_1,...,C_(s-1) for its Vandermonde evaluation matrix.
Its determinant squared has modulus |disc Q|.
A column at x_j has norm at most2sqrt(s)exp((s-1)ell_j).
For each nonreal pair replace the column at conjugate x by its difference from the column at x.
The jth difference satisfies

    |C_j(x)-C_j(conjugate x)|
       <=4sinh(j ell)<=4j ell exp(j ell).

Hence its column norm is at most4s sqrt(s)ell exp((s-1)ell).
Hadamard, including the unchanged leading-basis determinant and all other columns, gives

    1<=|disc Q|
      <=(4s)^s exp(2(s-1)m) (2s m/c)^c.           (16)

The last product bound is arithmetic/geometric mean on the c/2 positive ell values.
The integer lower bound uses the actual squarefree monic integer Q.
This is a changed trace-paired cofactor bound in the same elementary mechanism already checked at Smy08-U003, not an uncharged root-separation premise.
For0<m<=1 it implies

    m>=(c/(2s))(4s)^(-s/c)exp[-2(s-1)/c].           (17)

For a real critical point of multiplicity r, ordinary Rolle gives at least one distinct derivative root in every gap of the s-c real simple roots.
Counting these gaps with the selected repeated point yields r<=c+1, including s-c=0,1 by the total-degree bound.
Therefore if r>=2, the increasing function t exp[-A/t], A=s log(4s)+2(s-1), gives the necessary bound

    m>=((r-1)/(2s))(4s)^[-s/(r-1)]
                             exp[-2(s-1)/(r-1)].   (18)

This is explicitly degree-dependent.
Its degree logarithm cannot be discarded, and it does not make all near-one trace roots real or imply a bounded r.
It supplies an exact finite discriminator and explains why a bare nonzero discriminant cannot settle the original uniform question.
The stronger asymptotic restriction(10) comes from actual angular information, not from falsely replacing (17) by a uniform positive constant.

<a id="maximal-critical-degeneracy-cost"></a>
## 8. The maximal single-critical-point mechanism costs at least log two

Suppose s>=3 and Q' has a root of multiplicity s-1.
It is the only derivative root and is real because Q' has real coefficients.
Write it a=p/q in lowest terms: it is rational because its minimal polynomial degree times s-1 is at most s-1.
Equation(12) makes q^(s-1) divide s.
Since2^(s-1)>s for s>=3, q=1 and a is an integer.
Integrating the monic derivative gives

    Q(x)=(x-a)^s+c_0, c_0=Q(a) in Z, c_0!=0.       (19)

The trace roots are the regular s-gon a+rho exp(i theta_j), rho=|c_0|^(1/s)>=1.
For s>=4 there is a vertex within angular distance pi/s<=pi/4 of the imaginary axis, so some root has |Im x_j|>=1/sqrt2.
For s=3, the two possible real rotations from real nonzero c_0 have maximal imaginary coordinate at least sqrt3/2.
In every case the selected nonreal root and its distinct conjugate have the same inverse-pair ell, and (1) gives

    ell>=asinh[1/(2sqrt2)]=(log2)/2,
    m(P)>=2ell>=log2, M(P)>=2.                    (20)

This is an ACTUAL total-measure obstruction, not a degree-normalized statement, and it does not require Q to have all real roots or any original circle roots.
The degree guard s>=3 is essential: a quadratic derivative may have a half-integral critical point, so this argument is not applied there.
It rules out the maximal critical multiplicity mechanism of L368's trace Q=(x+2)^s+1 from the near-one M(P)<2 regime, even though it supplies no broader irreducibility claim for that family.
It does not rule out other unbounded but sublinear multiplicities compatible with(10).

## 9. Outcome, retained costs and next test

The changed main result is the finite unrestricted derivative-atom estimate(9), and its near-one consequence(10)--(11), for ACTUAL irreducible reciprocal nontorsion integer units with arbitrary trace root configuration.
The exact critical-factor/value accounting, the degree-paid discriminant inequality and the maximal-degeneracy log2 obstruction provide separate finite discriminators.
No new near-one family, all-real reduction, existence of circle conjugates or bounded absolute critical order is asserted.

The full original d=2s, total m, all inverse pairs and all powered labels remain in every estimate.
The moment cutoff L in(8)--(9) is an explicitly chosen analytic test degree, not the original polynomial degree or an executed scan.
Increasing it incurs16^(L-1)/(s-1),8^(L-1)sinh m, the original epsilon(h) and the complete radial sinh((L-1)m)/s.
The critical-value field degrees, primitive leading coefficients, derivative content and original discriminant signs are not erased.
Source-proof boundaries from L229 remain exactly its accepted ones.

The next useful theoretical gate is whether the sublinear maximum can be strengthened to an ABSOLUTE bound, or whether some actual irreducible small-total-measure family can have growing sublinear critical multiplicity.
Such a family would require actual irreducibility, measure and phase-cancellation proofs; the old broad family and high degree alone do not supply it.
Alternatively a signed Chebyshev tail may remain useful despite growing M, but its actual constants and sign structure must be handled in their own responsible proof.
No program, J, root scan, factor enumeration, moment evaluation or native computation was used or proposed here.
