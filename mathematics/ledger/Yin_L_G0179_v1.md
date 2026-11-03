---
author: Yin
---

# Trinomial eventual positivity and height-one negative phase balance

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit instruction after complete noncontributor reviews of D G0044 and D G0045.
The retaining orbit_research AI authored the trinomial limit and did not author or review the separate height-one negative construction.
The coordinating AI independently reviewed the former; the resultant_research AI independently reviewed the latter and supplied J38.
All contributor and library-dependence disclosures below remain operative.
No unrestricted G0001 conclusion or new Claim decision is asserted.

<a id="phase-sign-boundaries-fixed-scope"></a>
## Adopted paired boundaries

For primitive exponent pairs 0<b<a, gcd(a,b)=1, the complete doubling balance of t^a-t^b-1 converges uniformly to one two-variable constant Delta_infinity>1/250.
Therefore every sufficiently large such pair has Delta>1/500; the remaining sign question has only finitely many possible exceptions.
This argument uses the previously accepted full Lawton theorem including zeros, but supplies no effective degree cutoff.
Its exact sectional integrals and rational lower certificate are retained in the [trinomial proof](#trinomial-eventual-positive-balance).

The separate [height-one construction](#height-one-negative-phase-balance) gives infinitely many monic unit seeds with coefficient height one, no reciprocal or cyclotomic factor and complete balance below log(2/3), using an explicit specialization cutoff.
A varying-copy sequence has balance tending to minus infinity while its seed measure grows.
Irreducibility, three-term support and near-one measure are not established for these seeds.
Thus eventual positivity in the exact primitive trinomial class and negativity in the broader height-one class are compatible.

The negative construction's initial qualitative Lawton proof was replaced before independent review by an elementary quantitative averaging estimate using a torus modulus lower bound.
Lawton is not its current dependency.
J37 and the separately authored J38 retain the actual degree63 certificate and distinct author/reviewer results with their common FLINT/Arb library boundary; no enormous specialized polynomial was expanded.
Full auxiliary factors and leading coefficients are retained in both balances.

The complete original bodies and reviews follow.
Their dated exploratory or pending-review wording preserves the state at writing; this adoption and the appended findings determine the current fixed status.
Only heading depth and relative navigation are relocated, with mathematical prose and formulas unchanged.

<a id="retained-trinomial-limit-argument"></a>
## A universal two-variable limit for primitive trinomial doubling balance

Date: 2026-10-10.
Assigned orbit_research AI for Yin, after fixed retention of the complete seed-boundary results in L175.
This bounded conceptual experiment keeps exactly f_(a,b)=t^a-t^b-1, 0<b<a and gcd(a,b)=1.
It does not enlarge the previous45-row parameter scan.
The proposed discriminator is the two-variable Mahler limit of its full doubling auxiliary and the sign of that one limit.

### Starting observation and intended test

Write u=t^b and v=t^(a-b).
The fixed [L175 formulas](Yin_L_G0175_v1.md#sparse-trinomial-auxiliary) express the seed as F(u,v)=uv-u-1 and its full auxiliary as a single fixed integer polynomial G(u,v).
For coprime b,a-b the relation parameter in the accepted Lawton specialization theorem is max(b,a-b), at least a/2.
Consequently an unbounded coprime family should have one universal full-measure limit, independently of the ratio b/a.
The exact source hypotheses and integral interpretation will be checked before asserting the conclusion.
If its balance is strictly positive, the all-input sign question reduces to finitely many degrees, though the existing non-effective limit need not supply a numerical cutoff.
If it is negative, arbitrarily large primitive trinomial counterexamples follow.
A zero limit requires finer information.

The local reuse screen found and read the exact Lawton interface in [Den09-U002, Theorem14/Example15](../audits/literature/Den09/Yin_U002.md#den09-u002), including polynomials with circle zeros, and the uniform two-variable application in [L50](Yin_L_G0050_v1.md#essential-family-mahler-limit).
The direct argument below proves that the single limiting balance is strictly greater than1/250, so all sufficiently large coprime trinomials have balance greater than1/500.
There is no effective degree cutoff here.
The earlier45 positive discovery decimals are not a premise.
Ongoing general height-one cancellation constructions by the coordinator concern a different seed class and are not pursued here.
No new source theorem or numerical integral is used.

<a id="trinomial-eventual-positive-balance"></a>
### 1. Exact statement and retained source boundary

For integers 0<b<a with gcd(a,b)=1, put

    f_(a,b)(t)=t^a-t^b-1,
    f*_(a,b)(t)=t^a f_(a,b)(1/t),
    G_(a,b)(t)=[(f*_(a,b))^2 f_(a,b)(t^2)
                         +f_(a,b)^2 f*_(a,b)(t^2)]/2,
    Delta_(a,b)=log2+m(G_(a,b))-3m(f_(a,b)).             (1)

Every m here is the full logarithmic Mahler measure, including leading coefficients and all factors.
The seed is not assumed irreducible.
L175 proves G_(a,b)(1)=-1, its exact monomial normalization and the exceptional nonmonic residual at(2,1).
No factor is removed in(1).

There exists a real constant Delta_infinity such that

    Delta_(a,b) -> Delta_infinity uniformly over gcd(a,b)=1,
                  0<b<a, as a -> infinity,
    Delta_infinity > 1/250.                            (2)

Consequently there is an integer A_0 such that

    Delta_(a,b)>1/500 for every a>=A_0,
                   0<b<a and gcd(a,b)=1.              (3)

In particular there are only finitely many pairs in this class with Delta_(a,b)<=0, or even with Delta_(a,b)<=1/500.
This proves neither that this finite exceptional set is empty nor an effective upper bound on its degrees.

The sole non-elementary input is the previously accepted full Lawton specialization statement: for a fixed nonzero Laurent polynomial P in two variables,

    M(P(t^r,t^s)) -> M(P)
    as q(r,s)=min{max(|i|,|j|): (i,j) != (0,0), ir+js=0}
       -> infinity.                                  (4)

Den09-U002 retains this full theorem, including its treatment of zeros, as an external statement; the original Lawton proof was not audited there or here.
The invertible-only determinant approximation elsewhere in that unit would not suffice.
L50 already uses this exact all-vector limit to obtain uniformity over offsets; that method is reused, with the following polynomials and a new direct limiting-integral estimate.
No rate is available from the input used here.

<a id="trinomial-universal-mahler-limit"></a>
### 2. One fixed two-variable polynomial controls every offset

Define

    F(u,v)=uv-u-1,             H(u,v)=1-v-uv,
    G(u,v)=[H(u,v)^2 F(u^2,v^2)+F(u,v)^2 H(u^2,v^2)]/2.

The exact integer expansion retained in L175 is

    G=u^4 v^3-u^4 v^2+u^3 v^4-2u^3 v^2+u^3 v
                         -u^2 v^2+u v^3-2u v^2+u-v^2+v. (5)

Substitution at (u,v)=(t^b,t^(a-b)) gives precisely f_(a,b), f*_(a,b), and G_(a,b).
Both specializations are nonzero for all these inputs.
Since gcd(b,a-b)=1, every integral relation with (b,a-b) is an integer multiple of (a-b,-b).
Therefore

    q(b,a-b)=max(b,a-b)>=a/2.                          (6)

Applying(4) separately to the two fixed polynomials F and G, and taking logarithms of their positive Mahler measures, gives(2)'s convergence with

    Delta_infinity=log2+m(G)-3m(F).                    (7)

It is uniform over the stated offsets: otherwise a sequence of exceptions with a tending to infinity would, by(6), contradict the all-vector limit in(4).
No assumption on convergence of b/a is required.
The following explicit integrals in particular verify positivity and finiteness of M(F),M(G).

On the two-dimensional unit torus, H=uv conjugate(F), so R=H/F has modulus one almost everywhere.
The same exact factorization as in L175 gives, almost everywhere,

    G=[F(u,v)^2 F(u^2,v^2)/2]
                         [R(u,v)^2+R(u^2,v^2)].

The integrability justified below and invariance of torus Haar measure under coordinatewise squaring show that(7) is also the full two-variable phase integral

    Delta_infinity=integral_(T^2)
                    log|R(u,v)^2+R(u^2,v^2)| dmu.     (8)

Thus the limit concerns the complete balance, including all signed phase contributions.
It is not a sum of limits of selected Fourier modes.

<a id="trinomial-quartic-section-integral"></a>
### 3. A rotated reciprocal quartic and its exact Jensen integral

Write u=exp(2i theta), with0<=theta<=pi, and set v=exp(i(phi-theta)).
For fixed theta this is only a rotation of the v circle and preserves its normalized measure.
The divisor u^2 v^2 has unit modulus, and dividing(5) by it gives the real expression

    G/(u^2 v^2)=2cos(2phi)+4cos(3theta)cos(phi)
                           -2cos(4theta)-4cos(2theta)-1. (9)

Put c=cos(theta), A=cos(3theta)=4c^3-3c and D=4c^2-1.
With z=exp(i phi) and x=z+z^(-1), the right side of(9) is

    x^2+2A x-D^2.

Indeed -2cos(4theta)-4cos(2theta)-3=-(4c^2-1)^2.
Its two real trace roots are

    xi_+=-A+sqrt(A^2+D^2),
    xi_-=-A-sqrt(A^2+D^2),
    A^2+D^2=1+c^2(4c^2-1)^2>0.                       (10)

After multiplication by z^2, the section is the monic reciprocal quartic

    (z^2-xi_+ z+1)(z^2-xi_- z+1).

For a real x the logarithmic Mahler measure of z^2-xz+1 is

    J(x)=0 if |x|<=2, and J(x)=arcosh(|x|/2) if |x|>2.

This follows directly from the two roots with product one, including the double-root endpoints.
Hence the inner v integral is I(theta)=J(xi_+)+J(xi_-), which is nonnegative.
Evaluating the trace quadratic at +/-2 gives

    4+4A-D^2=(2c-1)^2(3-4c^2),
    4-4A-D^2=(2c+1)^2(3-4c^2).                        (11)

Since xi_+>=0 and xi_-<=0, both roots lie in[-2,2] when |c|<=sqrt(3)/2.
Equality at c=+/-1/2 merely gives an endpoint trace root and still zero inner measure.
When |c|>sqrt(3)/2, both roots have modulus greater than2.
Replacing c by -c exchanges xi_+ and -xi_-, so I(theta) is unchanged by theta -> pi-theta.

For0<=theta<pi/6, D>2.
The product xi_+(-xi_-) is D^2, while(11) gives

    sqrt((xi_+^2-4)(xi_-^2-4))=D(D-2).

The addition formula for hyperbolic cosine therefore implies

    cosh(I(theta))=[D^2+D(D-2)]/4=D(D-1)/2,
    I(theta)=arcosh((4cos^2(theta)-1)(2cos^2(theta)-1)). (12)

Both sides are nonnegative, so inversion by arcosh is legitimate.
The formula extends continuously to theta=pi/6 with value zero.
It follows that

    m(G)=(2/pi) integral_0^(pi/6)
             arcosh((4cos^2(theta)-1)(2cos^2(theta)-1)) dtheta.
                                                               (13)

No unproved interchange across torus zeros is used.
On T^2 one has |G|<=13 from(5), so its positive logarithmic part is bounded.
For each fixed theta the monic quartic's Jensen integral is I(theta)>=0, hence the inner negative logarithmic integral is at most its positive logarithmic integral, which is at most log13.
Tonelli bounds the full negative part as well.
This proves integrability of log|G| and justifies Fubini and(13).

For F, Jensen in v gives max(0,log|1+u|).
The same positive/negative-part argument, using |F|<=3 and its nonnegative inner integral, proves integrability.
Thus

    m(F)=(2/pi) integral_0^(pi/3) log(2cos(theta)) dtheta. (14)

These facts also justify the integrable identity(8): its last logarithm is the difference of the three integrable polynomial logarithms in the preceding exact factorization, away from their null zero sets.
Coordinatewise squaring preserves normalized Haar measure, so the factor F(u^2,v^2) has the same integral as F.

<a id="positive-trinomial-limit-certificate"></a>
### 4. Two elementary integral estimates give a positive rational margin

The integrand in(13) is decreasing on[0,pi/6], since D decreases from3 to2 and D(D-1)/2 is increasing as a function of D on that range.
At the two exact angles,

    cosh(I(pi/12))=(3+sqrt3)/2 > 17/8=cosh(log4),
    cosh(I(pi/8))=1+sqrt2/2 > 5/3=cosh(log3).

The strict inequalities use only sqrt3>5/4 and sqrt2>4/3.
Integrating the corresponding constant lower bounds on[0,pi/12] and[pi/12,pi/8], and using nonnegativity on the rest, gives

    m(G)>(log4)/6+(log3)/12=log48/12.                 (15)

For the seed, log(2cos(theta)) is concave on[0,pi/3].
Apply its midpoint Jensen bound separately on[0,pi/6] and[pi/6,pi/3].
Since

    (2cos(pi/12))(2cos(pi/4))=1+sqrt3,

equation(14) yields

    3m(F)<=log(1+sqrt3)<log(11/4),                    (16)

where sqrt3<7/4 follows by squaring.
Consequently

    Delta_infinity>log(8/11)+log48/12
                  =(1/12)log(48*8^12/11^12)>1/250.   (17)

Here the last strict inequality has an elementary integer certificate.
Put

    U=48*8^12=3298534883328,
    V=11^12=3138428376721.

For U>V>0, log(U/V)>(U-V)/U.
Moreover

    250(U-V)=40026626651750
        >12U=39582418599936.

Combining these two comparisons proves the last step of(17).
The displayed integer arithmetic was directly checked with exact integers; no numerical quadrature, algebraic-root approximation or Mahler scan is needed.

Choose the error in the uniform convergence(2) to be less than1/500.
Equations(2) and(17) then imply(3).
Finitely many integer a lie below A_0 and each admits finitely many b, proving the stated finiteness of small or nonpositive balances.

### 5. What this changes, and what it leaves open

The exact limiting discriminator is positive.
Consequently an attempted negative family obtained only by sending coprime trinomial exponents to infinity cannot work, regardless of their ratio or oscillation.
The seed-Phi_6 cases from L175 are included: cyclotomic reduction preserves Delta, and their original coprime exponent vectors still satisfy(6).
No universal sign theorem follows for the remaining finite, presently unbounded range of degrees, and the existing45 numerical positives do not close it.
The next useful step is an effective specialization-error bound strong enough to give a concrete finite cutoff, or a direct inequality covering those finite-degree possibilities without such a cutoff.
A blind larger parameter scan is not justified by the present non-effective reduction.

This also does not construct low-measure negative balances in a broader seed class.
The current theorem is specific to the three occupied coefficients and coprime exponents.
The separately retained negative cubic controls have growing height/measure and do not contradict it; the coordinator's broader height-one cancellation experiment is not covered.
The two-variable limit and eventual positivity are useful structure for this precise class, not a near-one Mahler gap, a new Salem-family construction, or a uniform arithmetic-income theorem for G0001.

### Contribution and actual checking

The assigned orbit_research AI supplied the exact relation-parameter application, rotated quartic section, trace-root classification, hyperbolic simplification, two-interval/concavity bounds and finite-exception conclusion in this draft.
The parent selected the precise trinomial-versus-controlled-measure question and supplied no steps of this derivation.
The complete argument has been self-checked; independent review and fixed adoption remain outstanding.
The fixed L175 sparse polynomial and source-scoped Den09-U002/L50 Lawton interface were reused explicitly.
No new source intake, new J computation, enlarged pilot or novelty claim was made.
G0001 remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0078_v1.md#complete-separate-independent-review), with its original inspected scope and relationship.



<a id="retained-height-one-negative-argument"></a>
## Height-one almost anti-reciprocal seeds and the doubling phase balance

Date: 2026-10-10.
Coordinator-developed conceptual and bounded certificate inquiry.
This extends the precise sign-boundary question of [L175](Yin_L_G0175_v1.md#negative-doubling-phase-balance), without changing its fixed statement or the separate three-term investigation.

### Current question and scope

Does coefficient height one alone force the complete balance Delta(f)=log2+m(G_f)-3m(f) to be nonnegative?
The candidate mechanism is an almost anti-reciprocal polynomial f=t^N h-h*+t^((N+deg h)/2), with N>deg h of matching parity.
Then f+f*=2t^((N+deg h)/2), so the numerator G_f has a quadratic sup-norm bound even though f's measure can grow.
No irreducibility, near-one measure or three-term conclusion is assumed.
The next test is a single exact height-one seed h0 with M(h0)^3 greater than a rigorous squared sup-norm bound, followed by separated products and the already accepted Lawton specialization interface.

The finite recursive pair P_0=Q_0=1, P_(j+1)=P_j+t^(2^j)Q_j, Q_(j+1)=P_j-t^(2^j)Q_j has coefficients +/-1 and |P_j|^2+|Q_j|^2=2^(j+1) on the circle, by direct expansion.
P_6 is the initial 64-term candidate.
These displayed recursion facts are proved directly; no external assertion about its Mahler measure is used.
The candidate has now passed the strict certificate below, and the complete consequence is proved here.
The preceding paragraph retains the original question rather than a universal claim.

<a id="height-one-negative-phase-balance"></a>
### The proved scope

There are infinitely many distinct monic integer polynomials f of coefficient height one, constant term-1, with no reciprocal or cyclotomic factor, for which

    Delta(f)=log2+m(G_f)-3m(f)<log(2/3)<0,
    G_f=((f*)^2 f(t^2)+f^2 f*(t^2))/2.

More generally such examples have Delta tending to minus infinity while their measure grows.
They need not be irreducible or three-term, and none is a small-measure or Salem example.
The theorem refutes a nonnegative balance based solely on monicity, unit constant term, coefficient height one and removal of cyclotomic factors.
It leaves the coprime three-term sign question and every small-measure coverage condition open.

### 1. One fixed recursive seed

Let h0 be P_6 multiplied by its leading sign, so it is monic of degree63 with all64 coefficients in{-1,1}.
The recursion above has disjoint coefficient blocks; hence those coefficient assertions hold by induction.
At each doubling, the parallelogram identity gives

    |P_(j+1)(z)|^2+|Q_(j+1)(z)|^2
       =2(|P_j(z)|^2+|Q_j(z)|^2),  |z|=1.

Therefore ||h0||_infinity<=sqrt128.
The [single-input J37 certificate](../computations/programs/Yin_J_G0037/readme.md) checks exact squarefreeness and isolates all63 roots into pairwise disjoint rigorous complex balls.
The product of the31 strictly exterior root moduli is enclosed near6.8505729309192798991 and, using the ball inequalities rather than decimal rounding, proves

    M(h0)>137/20>34/5,
    M(h0)^3>128.                                      (1)

The leading coefficient is one, so the root product is the Mahler measure; the lower bound would remain valid if any unresolved root moduli had merely been omitted.
In the executed certificate every root's comparison with one is decided.
No irreducibility assertion about h0 is needed.

### 2. Products with coefficients still of height one

For any positive integer k set

    h_k(t)=product_(j=0)^(k-1) h0(t^(64^j)),
    D_k=64^k-1,  C_k=128^(k/2).

Every integer in[0,D_k] has a unique base64 expansion with digits in[0,63].
Each coefficient in the product is consequently one product of signs, with no collision or cancellation.
Thus h_k is monic of degree D_k and all coefficients are +/-1.
Multiplicativity and the circle substitution formula give

    M(h_k)=M(h0)^k>(34/5)^k,
    ||h_k||_infinity<=C_k.                            (2)

These are exact all-k assertions.
J37 expands only h0, not these high-degree products.

### 3. Almost anti-reciprocal specializations

Fix k and write h=h_k, D=D_k.
For each positive integer n define

    f_(k,n)(t)=t^(2n+D)h(t)-h*(t)+t^(D+n),
    q=deg f_(k,n)=2(D+n).                             (3)

Here h*=t^D h(t^(-1)) and f*=t^q f(t^(-1)) use their full degrees.
The low block occupies[0,D], the high block[2n+D,2n+2D], and the middle monomial D+n lies strictly between them.
Thus f is monic, has constant term-1 and every coefficient in{-1,0,1}.
Its reciprocal identity is

    f+f*=2t^(D+n).                                   (4)

There is no nonconstant common factor of f and f*: any such factor would divide the right side of(4), whereas f has nonzero constant term.
In particular f has no reciprocal factor and no cyclotomic factor.
This is not an irreducibility claim.
On the unit circle,

    t^(-(D+n)) f(t)=1+t^n h(t)-t^(-n) conjugate(h(t)),

whose real part is one.
Hence f has no unit-circle root.
Also f(1)=1 and

    ||f||_infinity<=2C_k+1=:F_k.                      (5)

### 4. Elementary averaging with an explicit error

Define the Laurent polynomial in two independent variables

    P_k(z,y)=h(z)y^2+y-z^(-D)h*(z).

Then f_(k,n)(t)=t^D P_k(t,t^n).
On the full two-dimensional unit torus,

    P_k(z,y)/y=1+y h(z)-conjugate(y h(z)),
    |P_k(z,y)|>=1.

Thus the real function H(theta,phi)=log|P_k(exp(i theta),exp(i phi))| is continuously differentiable.
Since h has D+1 coefficients of absolute value one,

    |partial_theta H|<=|partial_theta P_k|/|P_k|
       <=2 sum_(r=0)^D r = D(D+1)=:L_D.

Here the second polynomial term involving h* is exactly conjugate(h) on the circle, so its derivative has the same bound.
Splitting the theta integral into n equal intervals, then setting theta=(2pi*j+phi)/n on interval j, gives

    m(f_(k,n))=(1/n) sum_(j=0)^(n-1)
       average_phi H(2pi*j/n+phi/n,phi).

The full torus mean m(P_k) instead equals the same sum with an independent average over psi in[0,2pi] inside the first argument:

    m(P_k)=(1/n) sum_(j=0)^(n-1)
       average_phi average_psi H(2pi*j/n+psi/n,phi).

The Lipschitz bound therefore proves the explicit estimate

    |m(f_(k,n))-m(P_k)|<=2pi D(D+1)/n.               (6)

No theorem controlling logarithmic singularities is needed here, since |P_k|>=1 everywhere on the torus.
All integrals are ordinary finite continuous integrals, and monomial multiplication does not change their value.

For each |z|=1 with h(z)!=0, the one-variable Jensen root formula in y gives

    integral_(|y|=1) log|P_k(z,y)| >= log|h(z)|.

The finite exceptional z with h(z)=0 have measure zero, log|h| is integrable, and log|P_k| is continuous.
Integrating this inequality gives

    m(P_k)>=m(h_k)=k m(h0)>k log(137/20).             (7)

The elementary integral bound log(1+x)>x/(1+x) for x>0 shows log(137/136)>1/137.
If n>=1100D(D+1), equation(6), pi<4 and 8/1100<1/137 show

    m(f_(k,n))>k log(137/20)-1/137>k log(34/5).

For k=4 the sharper sufficient cutoff is n>=320D(D+1): the error is strictly below1/40, whereas4log(137/136)>4/137>1/40.
These explicit integer cutoffs are huge.
No high-degree f has been expanded or tested numerically.

### 5. Complete numerator and its phase cost

For any integer polynomial f, the displayed G_f is integral: modulo2, f(t^2)=f(t)^2 and likewise for f*, so the numerator is zero modulo2.
Put u=f+f*.
Direct expansion, retaining both contributions, gives

    2G_f=-2fu f(t^2)+u^2 f(t^2)+f^2 u(t^2).          (8)

In the present construction |u|=|u(t^2)|=2 on the circle.
Equations(5) and(8) imply

    |G_f|<=3F_k^2+2F_k,
    m(G_f)<=log(3F_k^2+2F_k).                         (9)

G_f is not the zero polynomial, since G_f(1)=1.
In fact this evaluation also shows content(G_f)=1.
All its factors and any leading coefficient are retained in m(G_f); no selected factor is being substituted into Delta.

For clarity the exact full phase identity is

    Delta(f)=integral_(|z|=1)
       log|r(z)^2+r(z^2)|,  r(z)=f*(z)/f(z).

It follows by factoring 2G_f=f(z)^2 f(z^2)(r(z)^2+r(z^2)).
Here f has no unit-circle zero, and the finitely many possible G_f zeros have integrable logarithms.
The identity is the same complete balance used in L175, not a positive-mode truncation.

For k=4 we have C_4=128^2=16384 and F_4=32769.
The exact rational comparison, also checked in J37, is

    2(3*32769^2+2*32769)/(34/5)^12 < 2/3.             (10)

For every n>=320D_4(D_4+1), equations(6)--(10) prove Delta(f_(4,n))<log(2/3).
Distinct n have distinct degrees, giving infinitely many examples with the stated scope.

For the stronger unbounded assertion, C_k>=1 implies F_k<=3C_k and 3F_k^2+2F_k<=33 C_k^2.
Choose, for example, n_k=1100D_k(D_k+1).
Then

    Delta(f_(k,n_k))
       < log66-k log((34/5)^3/128) -> -infinity,      (11)

because (34/5)^3=39304/125>128.
Simultaneously m(f_(k,n_k))>k log(34/5) grows.
Thus the construction changes the height restriction of L175's earlier negative family but supplies no near-one sequence and no irreducible-factor version of the phase inequality.

### Scope, reuse and review

The coordinator for Yin developed all of this argument and wrote/read/executed J37.
The first one-input run certified the weaker sufficient threshold51/10; after deriving the four-copy bound the same input was rerun with34/5 and exact(10), then with137/20 for the effective averaging error.
All three runs succeeded and no larger seed search was conducted.
The native source and successful full root-ball output are retained at J37.
Independent review is pending.

The local reuse screen read the full L175 negative-balance construction and the accepted [Den09-U002 Lawton interface](../audits/literature/Den09/Yin_U002.md#den09-u002), including its Laurent, zeros and relation-parameter boundaries.
The initial draft used that valid fixed-k qualitative limit.
Before independent review it was replaced by the direct quantitative argument in Section4, after observing the torus lower bound |P_k|>=1; Lawton is no longer a proof dependency.
This is a strengthened proof and effective conclusion, not a detected failure of the original limit.

The paired recursion is standard, but only its displayed elementary proof and the newly executed fixed seed certificate are inputs here; no external Mahler-measure claim about recursive polynomials is imported.
This is a scoped internal construction, not an external novelty assertion.
The no-reciprocal-factor conclusion is exact, while irreducibility, sparse support and small measure remain absent.
A useful next test would impose one of those additional restrictions rather than infer its coverage from this example.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0078_v1.md#complete-independent-proof-and-certificate-finding), with its original inspected scope and relationship.




The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0078_v1.md#phase-sign-boundaries-retention-record), with its original inspected scope and relationship.
