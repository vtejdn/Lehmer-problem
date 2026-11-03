---
author: Yin
---

# Actual two-dimensional weighted phase bands and a fixed-enlargement critical-width bound

Human author Yin.
Root proposed using a nondegenerate local two-dimensional phase patch to obtain a complete power-sized band.
Phase_bands checked the exact weighted Hessian, inspected the required new primary-source passages, matched their uniform parameter hypotheses, and completed the cutoff, full-band, original-cost and actual-degree argument.
Both are contributors, not independent reviewers.
The actual polynomial family, original2d window and probability laws are exactly those of adopted C684.
No new family, native scan, unweighted surrogate or two-factor original law is introduced.

## Statement

For integers j>=4K take the exact weighted three-factor C684 family

    K=(product_(p prime,p<=48)p) lcm(1,...,ceil(8^5*5^(5/2))),
    a_j=min{p prime:p>(j+1)K}, L_j=K+a_j+2, M_j=floor(a_j/4),
    n_j=ceil((L_j+1)^(17/8)), ell_j=ceil(log_2(L_j+1)),
    c_j=min{p prime:p>n_j ell_j}, d_j=c_j+L_j-2,
    e=(K,a_j,c_j), w=(1,1,2),
    P_j(x)=[(x^2-1)product_i(x^e_i-1)
       -(x/2)sum_i w_i(x^e_i+1)product_(l!=i)(x^e_l-1)]/(x-1)^2.

The threshold n_j ell_j is an integer product, formed before prime selection.
These are actual monic integral irreducible Salem minimal polynomials of even degree d_j and trace0, with log2<m(P_j)<log4.
Use ALL d_j relation columns and the original2d_j coordinates:

    A_rel,j=[P_j,xP_j,...,x^(d_j-1)P_j],
    G_j=A_rel,j^T A_rel,j, Pi_j=A_rel,j G_j^-1 A_rel,j^T,
    v_n(z)=(1,z,...,z^(n-1))^T,
    h_orig,j=v_(2d_j)^*Pi_j v_(2d_j)/(2d_j),
    f_(j,tau)=(1-h_orig,j/tau)_+.

Fourier coefficients use negative exponentials, all Haar measures have mass1, and W_*(f)=sum_(n!=0)abs(fhat(n)).
All conclusions below concern these actual functions; their finite-input Wiener sums, circle-root value1 and at least1/2 margin for tau<=1 are retained from C684.

Define the SAME weighted torus phase

    R(z,u)=(z^K-1)(u-1), S(z,u)=2(z^K u-1),
    Acal=-(z^2-1)R-zR+zS/2,
    Bcal= (z^2-1)R-zR-zS/2,
    U=Acal/Bcal off common zeros, U=0 at common zeros,
    V(z,u)=U(z^-1,u^-1),
    h(z,u,w)=(1+Re(wV(z,u)))/2, F_tau=(1-h/tau)_+,
    iota_j(z)=(z,z^a_j,z^c_j),
    H_j(gamma)=gamma_0+a_j gamma_1+c_j gamma_2.             (CB1)

### Actual curved patch and an entire finite power band

On an angular neighborhood of x_*=(pi/K,pi) let

    D(t,s)=4sin t+cot(Kt/2)+cot(s/2),
    phi(t,s)=2arctan(D(t,s)/2), U(exp(it),exp(is))=exp(i phi(t,s)).

The actual Hessian satisfies

    det Hess(phi)(x_*)=2sin^2(pi/K)/(1+4sin^2(pi/K))^3>0,
    partial_ss phi(x_*)<0.                              (CB2)

Fix a positive lambda and delta so that the closed Euclidean ball B_(4delta)(x_*) lies inside one smooth angular chart with no cotangent poles, and

    -Hess(phi)(x)>=lambda I on B_(4delta)(x_*).

Such choices exist by(CB2); one may first take lambda to be half the smallest eigenvalue of -Hess(phi)(x_*) and then decrease delta below min{pi/(8K),pi/8}.
Fix the explicit nonzero smooth bump, periodized on T^2,

    chi(x)=exp[-1/(1-abs(x-x_*)^2/delta^2)] if abs(x-x_*)<delta,
    chi(x)=0 otherwise,
    s_chi=||chi||_2^2>0,
    D_phi,l=sup_(B_delta(x_*)) abs(partial_l phi), l=1,2,
    B_der=[sum_(l=1)^2 (||partial_l chi||_2+D_phi,l||chi||_2)^2]^(1/2),
    Delta=partial_t^2+partial_s^2,
    C_chi=||(1-Delta)^2 chi||_1, A_chi=13C_chi.

All these norms are probability-Haar norms in the fixed angular chart.
The proof establishes a finite constant C_osc>=1, depending only on these fixed phase/bump data, such that

    abs((chi U^k)hat(n))<=C_osc/k
         for EVERY integer k>=1 and EVERY n in Z^2.       (CB3)

Its source input is precisely the accepted primary stationary-phase statement and uniform-dependence scope in Tao26-U003, not the earlier first-derivative source units.
The proof below pays its uniformity over all linear-frequency parameters n/k.

Set the following fixed constants, where C_osc may be any finite bound supplied by that proof:

    C_0=ceil(max{2,2B_der/sqrt(s_chi),
                          24sqrt(3)C_osc C_chi/s_chi}),
    B_band=2C_0,
    a_band=s_chi/(2C_osc A_chi)>0.

Then for EVERY integer k>=1 the complete symmetric band satisfies

    sum_(abs(p),abs(q)<=B_band k)abs((U^k)hat(p,q))>=a_band k. (CB4)

The same statement holds for V^k by inversion of both coordinates.
No Fourier cutoff or bump-removal tail is omitted.

### All five original costs and the full selected support

Suppress j in a,c,d,L,M, and retain the original C684 constants

    epsilon_j=(4L-3)/(2d)+[1+pi L(5+2log c)]/(2c),
    E_bal=4(3+3pi), epsilon_j<=E_bal M^(-9/8),
    delta_*=[28(1+60pi)]^-2,
    C_obs=2/delta_*, C_stab=33C_obs+3,
    g_0=abs(Acal)^2+abs(Bcal)^2, g(z,u)=g_0(z^-1,u^-1),
    D_l=||partial_l Acal||_infinity+||partial_l Bcal||_infinity, l=1,2,
    G_K=sqrt(||g||_infinity),
    C_w=6pi[1+10(D_1+D_2)+2(G_K+1)],
    C_s=3pi[18*96^(2/3)(D_1+D_2)+4^(2/3)],
    C_2=512C_w+2C_s,
    B_ret(j,tau)=min{1,(C_stab epsilon_j)^(2/3)}
                                         +C_2 M^-1 tau^(-1/6).

For M>=max{2,C_w} and0<tau<=1/64, C684 proves for EVERY finite Gamma in the closed[-M,M]^3 box

    sum_(gamma in Gamma)
       abs(fhat_(j,tau)(H_j(gamma))-Fhat_tau(gamma))
                        <=5 card(Gamma)^(2/3)B_ret(j,tau). (CB5)

This is its complete original comparison, two regularizations and two smoothings on the original and every translated law, with no missing rho/tau range or coefficient.
Let

    L_tau=floor(1/(4sqrt(tau))),
    Gamma_tau={(p,q,k):1<=k<=L_tau,
                                  abs(p),abs(q)<=B_band k},
    N_tau=sum_(k=1)^(L_tau)(2B_band k+1)^2
                                      <=(2B_band+1)^2 L_tau^3.

When

    B_band L_tau<=M,                                    (CB6)

the whole Gamma_tau lies in the closed-M box, its original images are strictly positive and distinct, and

    sum_(gamma in Gamma_tau)abs(Fhat_tau(gamma))
                            >=C_mass tau^(-1/2),
    C_mass=3a_band/(1024pi)>0.                           (CB7)

Define

    C_err=(5/16)(2B_band+1)^(4/3)
                         max{(C_stab E_bal)^(2/3),C_2},
    H=M^(3/2)tau.

Then under the same finite premises,

    W_*(f_(j,tau))>=tau^(-1/2)
             [C_mass-C_err(H^(-1/2)+H^(-2/3))].          (CB8)

### Sufficient fixed enlargement and actual-degree conclusion

Set

    H_*=max{1,(4C_err/C_mass)^2,(4C_err/C_mass)^(3/2)},
    M_curv=ceil(max{2,C_w,(B_band/4)^4,(64H_*)^(2/3)}),
    j_curv=max{4K,ceil(4M_curv/K)}.

For EVERY actual j with M_j>=M_curv and EVERY width in the entire nonempty strip

    H_* M_j^(-3/2)<=tau<=1/64,                           (CB9)

the full support premise(CB6) holds and

    W_*(f_(j,tau))>=(C_mass/2)tau^(-1/2).                (CB10)

Every j>=j_curv satisfies the actual M threshold.
In particular for every FIXED real H>=H_*, the actual critical width tau_j=H M_j^(-3/2) obeys, eventually,

    W_*(f_(j,tau_j))>=[C_mass/(2sqrt(H))]M_j^(3/4)
                                                 ->infinity. (CB11)

For the genuine minimal-polynomial degree put Z_j=d_j/(1+log d_j).
C684 gives

    M_j^(17/8)/16<Z_j<2^15 M_j^(17/8).

Define D_*=2^(180/17)H_*.
Every positive shrinking sequence tau_j->0 with Z_j^(12/17)tau_j>=D_* eventually satisfies(CB10) eventually and therefore has divergent W_*.
In particular for every fixed h>=D_*, the actual widths tau_j=h Z_j^(-12/17) give

    W_*(f_(j,tau_j))>=[C_mass/(2sqrt(h))]Z_j^(6/17)
                                                 ->infinity. (CB12)

The lower enlargement need only be a sufficiently large fixed constant; no divergence of that enlargement is required.
The constants depend on the fixed actual K and on the specified fixed local bump/source bound, never on j,tau,k or selected frequencies.
No explicit decimal value for the accepted stationary-phase implicit constant is claimed.
The actual logarithm in Z_j, the Mahler interval log2<m(P_j)<log4, and the complete original2d window remain.
No assertion is made for every smaller H>0, an improved power12/17, every degree, a near-one family, optimality or unrestricted G0001 completion.

## Current assessment
[Selected decision](#decision-curved-full-band-open)

## Complete argument

### 1. Actual phase formula and a definite Hessian

The fixed weighted formula of C681, with v=u^-1 and b(t)=4sin t+cot(Kt/2), is

    U=[(1+ib)-(3+ib)v]/[(3-ib)-(1-ib)v].

For u=exp(is) away from u=1, (1+v)/(1-v)=-i cot(s/2).
Dividing numerator and denominator by1-v gives exactly U=(2+iD)/(2-iD), with D as in(CB2), hence the stated local real phase phi.
The point x_* has neither z^K=1 nor u=1, so there is no common zero or pole there.

Write b(t)=4sin t+cot(Kt/2), q(s)=cot(s/2) and f(D)=2arctan(D/2).
Then f'=4/(4+D^2), f''=-8D/(4+D^2)^2, and

    Hess(phi)=f''(b',q')^T(b',q')+f' diag(b'',q'').

At t_*=pi/K, s_*=pi, writing sigma=sin(pi/K)>0,

    b=4sigma, b''=-4sigma, q=0, q'=-1/2, q''=0.

Thus phi_ss=f''/4<0 and

    det Hess(phi)=f'f'' b''(q')^2
       =128sigma^2/(4+16sigma^2)^3
       =2sigma^2/(1+4sigma^2)^3>0.

The real symmetric Hessian is negative definite.
Continuity therefore supplies the fixed lambda,delta in the statement on the entire closed larger ball.
The prescribed delta bound keeps that ball in the interior of the(0,2pi)^2 angular chart and away from all cotangent poles.
The bump chi is smooth, nonzero, supported in the smaller ball, and its extension by zero and periodization are smooth.

### 2. Uniform oscillatory estimate for every linear frequency

For k>=1 and n in Z^2 put q=n/k and phi_q(x)=phi(x)-q dot x.
The probability-Haar coefficient is(2pi)^(-2)integral chi(x)exp(ik phi_q(x))dx over the chart.
The constant q is a vector in this section, distinct from the integer second Fourier coordinate in Gamma_tau.
We prove a uniform O(k^-1) bound for ALL real q, which includes all n/k.

Let E_grad=gradient(phi)(closed B_(2delta)(x_*)).
The definite Hessian gives, for x,y in the larger convex ball,

    (gradient(phi)(x)-gradient(phi)(y)) dot(x-y)
                                          <=-lambda abs(x-y)^2,
    abs(gradient(phi)(x)-gradient(phi)(y))>=lambda abs(x-y). (CB13)

For q in E_grad there is a UNIQUE x_q in the closed B_(2delta) with gradient(phi)(x_q)=q.
Uniqueness follows directly from(CB13).
There is no other stationary point on the amplitude support.
At x_q the Hessian determinant is at least lambda^2, and(CB13) supplies a uniform gradient lower bound lambda r outside every ball of radius r about x_q, on the amplitude support.
All x_q lie in a fixed compact set, q is bounded, and every derivative of phi_q needed on the chart is uniformly bounded.
To match the source's Euclidean smooth-phase convention, extend phi_q by a fixed smooth cutoff that equals1 on B_(3delta) and has support inside B_(4delta); this leaves the amplitude, stationary point and all needed gradients unchanged, and its relevant derivative bounds are uniform for these bounded q.

The directly inspected and accepted Tao26 Lemma3.3, N=0 in dimension2, together with its p11 uniform-dependence paragraph, now gives a finite uniform constant C_stat with coefficient magnitude at most C_stat/k for these q and all k>=1.
The determinant, stationary-point uniqueness, derivative bounds, support diameter and gradient lower bound required by that paragraph have each been supplied above.
Other stationary points of the extended phase outside the amplitude support do not violate the stated source hypotheses.
The(2pi)^(-2) normalization is included in C_stat.
This use asserts neither a specific numerical source constant nor a source-proof audit.

For q outside E_grad, minimize the smooth strongly convex function -phi(x)+q dot x on the closed B_(2delta).
A minimizer x_q^bd exists by compactness and lies on its boundary, since an interior minimum would give q in E_grad.
Its one-sided variational inequality and the Hessian lower bound imply for x in B_delta

    (gradient(-phi+q dot x)(x)) dot(x-x_q^bd)
                                           >=lambda abs(x-x_q^bd)^2.

Indeed subtract the gradient at x_q^bd, use strong monotonicity, and add the nonnegative first-order boundary term.
Since abs(x-x_q^bd)>=delta, this proves

    abs(gradient(phi_q)(x))>=lambda delta=:g_*>0.        (CB14)

This bound is uniform even for unbounded q.
Let B_H=sup_(B_delta)||Hess(phi)||_op and v_q=gradient(phi_q)/abs(gradient(phi_q))^2 near the support.
Then abs(v_q)<=g_*^-1 and abs(div v_q)<=6B_H/g_*^2; the latter follows by differentiating the quotient, with trace bound2B_H and quadratic-form bound B_H.
There is no boundary term because chi is smooth and compactly supported.
The identity v_q dot gradient(exp(ik phi_q))=ik exp(ik phi_q) and one integration by parts give coefficient bound

    (1/k)[||gradient chi||_1/g_*+6B_H||chi||_1/g_*^2].

The norms here already use probability-Haar normalization.
This is a direct proof of the nonstationary bound, not an uninspected uniform-parameter invocation of a source lemma.
Take C_osc>=1 to dominate this fixed constant and C_stat.
The two parameter cases prove(CB3) for every k,n, including all small k and all signed frequencies.

### 3. Parseval mass, finite truncation and full cutoff-removal expense

Let g_k=chi U^k, extended smoothly by zero outside the patch.
Then ||g_k||_2^2=s_chi and the product rule gives

    [sum_l||partial_l g_k||_2^2]^(1/2)<=k B_der.

For each fixed k, smooth periodicity and integration by parts with(1-Delta)^2 make its Fourier series absolutely summable in two dimensions.
The same is true for its derivatives of the finite orders used here.
The positive product kernels from C637 approximate these smooth functions uniformly by their moment bound; therefore the absolutely convergent Fourier series equals the function.
Finite orthogonality followed by the uniform limit proves Parseval, while finite derivative Bessel alone bounds the required tail.
This supplies the used two-dimensional equalities without an unproved completeness step.

Put R_k=C_0 k, an integer.
The union of the two coordinate tails satisfies

    sum_(max(abs(n_1),abs(n_2))>R_k)abs(ghat_k(n))^2
          <=R_k^-2 sum_l||partial_l g_k||_2^2<=s_chi/4.

Hence the full closed square has squared mass at least3s_chi/4.
Since EVERY coefficient is at most C_osc/k by(CB3),

    sum_(abs(n_1),abs(n_2)<=R_k)abs(ghat_k(n))
                                        >=3s_chi k/(4C_osc). (CB15)

For chi itself, integration by parts gives

    abs(chihat(r))<=C_chi/(1+abs(r)^2)^2.

Also C_chi>=integral chi>0 because the integral of every derivative term in(1-Delta)^2 chi is zero.

The number of integer points with sup norm exactly h>=1 is8h.
Thus sum_r abs(chihat(r))<=C_chi[1+8sum_(h>=1)h^-3]<=13C_chi=A_chi.
The same shell count and an integral comparison give for R>=1

    sum_(max(abs(r_1),abs(r_2))>R)abs(chihat(r))^2
        <=8C_chi^2 sum_(h>R)h^-7
        <=(4/3)C_chi^2 R^-6.                            (CB16)

Absolute convergence of chi's Fourier series justifies

    ghat_k(n)=sum_m chihat(n-m)(U^k)hat(m).

Finite Bessel for the bounded function U^k, of modulus1 off its finite common-zero set, gives sum_m abs((U^k)hat(m))^2<=1.
This upper bound needs no full Fourier expansion of the possibly nonsmooth global phase.
For n in the closed R_k square and m outside the closed2R_k square, the difference n-m has sup norm greater than R_k.
By Cauchy--Schwarz and(CB16), the TOTAL contribution of those exterior m to the entire sum in(CB15) is at most

    (2R_k+1)^2*(2/sqrt(3))C_chi R_k^-3
       <=6sqrt(3)C_chi/R_k
       <=s_chi k/(4C_osc).                              (CB17)

The last inequality follows from C_0>=24sqrt(3)C_osc C_chi/s_chi and k>=1.
The interior convolution contribution is at most

    A_chi sum_(abs(m_1),abs(m_2)<=2R_k)abs((U^k)hat(m)).

Subtract(CB17) from(CB15) and divide by A_chi to obtain(CB4), because2R_k=B_band k.
This pays both the energy truncation and the whole two-dimensional cutoff-removal tail.
Inversion of both torus coordinates negates the coefficient indices and preserves the symmetric band, proving the V^k assertion.

### 4. Exact original family, five-cost interface and scalar harmonics

The actual family and every original quantity in the statement coincide with adopted C684.
Its original law includes all d relation columns and the full inverse Gram, and its comparison includes the cyclic missing sample, genuine Gram pole and local observability absorption.
Its source/killer, weighted parity, exact(x-1)^2 removal, Salem minimality, positive measure interval and degree are unchanged.
No new source or actual-family reconstruction is required because no parameter has changed.

For clarity, its complete finite budget(CB5) is obtained from the original strong3/2 error min{1,(C_stab epsilon)^(2/3)}, TWO regularizations costing256sqrt(rho)tau^(-1/6) each, and TWO smoothings costing C_s M^-1 tau^(-1/6) each, with rho=(C_w/M)^2.
The translated laws are the actual pushforwards z to t*iota_j(z) for EVERY t in T^3.
Its joint shell estimates cover all s>=rho, including s>1 and rho/tau>1.
The finite weak Fourier lemma returns the ENTIRE Gamma with cost5 card(Gamma)^(2/3); neither sparse selection nor an independent uniform w coordinate under the original law is substituted.
Its strict a>2M and c>a^2>2M(1+a) prove no alias on the punctured CLOSED2M box, including every difference needed here.
These facts are used at precisely their adopted scopes.

For0<tau<=1/64 let g_tau(x)=(1-(1+Re x)/(2tau))_+ on the circle.
Its directly computed scalar harmonic obeys

    abs(ghat_tau(k))>=3sqrt(tau)/(8pi), 1<=k<=L_tau.

Indeed on x=exp(i(pi+y)), abs(y)<=sqrt(tau), the cap is at least3/4 and cos(ky)>=1/2.
The cosine is nonnegative on the entire cap support because2k arcsin(sqrt(tau))<=pi/4 in this range, so the rest cannot cancel that central contribution.
Conditioning on the w coordinate under PRODUCT HAAR gives the exact single-coefficient identity

    Fhat_tau(p,q,k)=ghat_tau(k)(V^k)hat(p,q), k>=1.       (CB18)

At a common zero the first factor in w is constant and every positive w coefficient vanishes, agreeing with V=0.
No infinite scalar Fourier expansion is required.

### 5. Every band coefficient, positivity, count and the complete cost

Combining(CB4) and(CB18), the torus mass of the ENTIRE Gamma_tau is at least

    [3a_band sqrt(tau)/(8pi)]sum_(k=1)^(L_tau)k
       >=[3a_band sqrt(tau)/(16pi)]L_tau^2.

Since1/(4sqrt(tau))>=2, its floor satisfies L_tau>=1/(8sqrt(tau)), giving exactly(CB7).
Different k give disjoint triples and all coordinate endpoints are retained.
For each k>=1, (2B_band k+1)^2<=(2B_band+1)^2 k^2.
Also sum_(k=1)^L k^2=L(L+1)(2L+1)/6<=L^3 for every integer L>=1.
Thus the displayed N_tau bound holds for the full set.

Under(CB6), all three coordinates lie in the closed-M box because B_band>=1.
For every selected triple,

    H_j(p,q,k)>=c_j-M(1+a_j)>0.

The closed2M result makes these original frequencies pairwise distinct.
Consequently their sum is a subsum of W_*, and(CB5) returns the ENTIRE torus mass minus the full error.

The count yields

    N_tau^(2/3)<=(2B_band+1)^(4/3)L_tau^2
                              <=(2B_band+1)^(4/3)/(16tau).

Since epsilon_j<=E_bal M^-9/8, the full returned error is at most

    (5/16)(2B_band+1)^(4/3)
      *[(C_stab E_bal)^(2/3)M^(-3/4)tau^-1
                                      +C_2 M^-1 tau^(-7/6)]. (CB19)

Factoring out tau^-1/2, these two relative costs are respectively

    M^-3/4 tau^-1/2=(M^(3/2)tau)^-1/2=H^-1/2,
    M^-1 tau^-2/3=(M^(3/2)tau)^-2/3=H^-2/3.

This proves(CB8); no logarithm or cutoff expense is hidden at critical equality.

### 6. Fixed enlargement, explicit support threshold and genuine degree

For H>=H_* the two relative error terms times C_err are each at most C_mass/4.
Under(CB9), L_tau<=M^(3/4)/(4sqrt(H))<=M^(3/4)/4.
The condition M>=(B_band/4)^4 therefore gives B_band L_tau<=M, with exact floor endpoints included.
The other components of M_curv ensure M>=max{2,C_w} and H_* M^-3/2<=1/64, so the stated strip is nonempty.
The earlier finite argument now gives(CB10) uniformly throughout that strip.
As before, j>=j_curv implies a_j>(j+1)K>4M_curv and hence M_j>=M_curv.

For a fixed H>=H_*, tau_j=H M_j^-3/2 tends to zero, and eventually enters that strip.
Substitution into(CB10) proves(CB11), with no limit H->infinity.
This is the new fixed-enlargement endpoint at the existing critical power, not an improved power.

For Z_j=d_j/(1+log d_j), the actual C684 bounds imply

    16^(-12/17)M_j^(3/2)<Z_j^(12/17)
                                   <2^(180/17)M_j^(3/2).

Thus Z_j^(12/17)tau_j>=D_* implies M_j^(3/2)tau_j>H_*.
For any positive shrinking sequence with that eventual condition, M_j eventually meets M_curv and tau_j eventually meets1/64, so(CB10) applies eventually.
Its lower bound tends to infinity because tau_j tends to zero.
For fixed h>=D_*, the widths h Z_j^-12/17 satisfy that condition and give(CB12) directly.
Sequence-entry times may depend on the sequence; no universal entry time is asserted beyond the finite strip theorem.

## Source, reuse and scope boundary

The Hessian calculation and all support, tail, deconvolution, cardinality and critical-cost arguments are local deductions for the exact weighted phase.
The only new external input is the primary multidimensional stationary-phase bound and its parameter-uniformity interface actually read from the retained Tao26 PDFpp9--12 and preserved in Tao26-U003.
The source theorem is accepted at its checked statement/applicability depth, with its original proof not fully audited and its numerical leading coefficient not used.
Old Tao26-U001/U002 do not acquire broader coverage.
The full linear-frequency applicability check, including unbounded parameters outside the gradient image, is supplied in Section2.
C637 supplies the already checked positive finite kernel/approximate-identity facts; the two-dimensional finite Fourier manipulations are explicit above.
C681 supplies the exact weighted phase formula and scalar coefficient mechanism only; its moving thin-contact frequency-band proof is not substituted for the new curvature band.
C684 supplies precisely the unchanged actual family, its full original2d/cyclic/Gram/translated-law interfaces, all five errors, closed aliases and actual degree.
The distinct two-factor C714 family and its original laws play no role.
The constants may be large and the sufficiently large fixed enlargement threshold is not claimed sharp.
The actual positive Mahler interval and unresolved small-enlargement, improved-power, near-one and unrestricted Task boundaries remain explicit.

## Assessment history

### Decision curved-full-band-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:52 |
| status | open |
| reason | Register the complete actual weighted Hessian and uniform two-dimensional oscillatory bound, full finite power band with both tails paid, and its exact unchanged-family five-cost consumer. The entire selected support yields a polynomial lower bound at every sufficiently large fixed critical enlargement, with explicit thresholds in the fixed phase/source constants and the genuine degree/logarithm conversion. The author-checked result awaits fresh independent whole review; source-proof depth, positive Mahler interval, smaller enlargements, improved powers and unrestricted realization remain limited as stated. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual curvature and fixed-enlargement theorem](#statement) | CB1--CB12: unchanged actual family/full original window, explicit nondegenerate weighted patch, all-frequency local estimate, entire finite power band, complete original five-cost/support estimate, uniform critical strip and actual-degree fixed-height consequences. |
| argument | [Complete actual-band and return proof](#complete-argument) | Sections1--6/CB13--CB19: actual Hessian, uniform source applicability for every linear parameter, energy and convolution tails, complete scalar mass/cardinality/positivity, every original expense and threshold/sequence conversion. |
| dependency | [New inspected stationary-phase source unit](../audits/literature/Tao26/Yin_U003.md#tao26-u003) | Actual retained PDF Lemma3.3 and p11 uniform-dependence paragraph, N=0 in dimension2, accepted at primary-statement/applicability depth; original full proof and exact numerical leading coefficient not adopted. |
| dependency | [Unchanged adopted weighted actual family](Yin_C_G0684_v1.md#decision-whole-reviewed-2026-10-24) | Exact17/8-log actual prime schedule and Salem polynomial, full original2d raw/cyclic/sample/Gram/pole/observability and every translated law, all five WL7--WL8 costs, closed2M aliases, degree and positive measure interval. |
| dependency | [Exact weighted torus phase and scalar harmonics](Yin_C_G0681_v1.md#decision-whole-reviewed-2026-10-24) | Actual weighted Mobius formula and product-Haar scalar coefficient mechanism; its prior thin-contact band is not used in place of the new full curvature band. |
| dependency | [Positive finite kernel](Yin_C_G0637_v1.md#complete-argument) | Existing squared-Fejer probability normalization, closed support, first moment and resulting smooth approximate-identity mechanism. |
| support | [Source and scope boundary](#source-reuse-and-scope-boundary) | New actual primary reading versus old units, complete local uniformity/tail expenses, unchanged original family and positive Mahler interval, and no smaller-height or unrestricted conclusion. |
