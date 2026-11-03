---
author: Yin
---

# Actual stationary residue entropy, neutral energy and probability escape

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="stationary-geometry-fixed-scope"></a>
## Current adopted scope

The complete independently reviewed proof adopts actual stationary path-information constraints for every algebraic unit and every finite quotient, with explicit Renyi and finite-support bounds.
For Salem inputs it also proves the full neutral second-moment cost and a separate high-probability escape conclusion from mod2 Shannon entropy and actual norm isolation.
The stronger full-support scale is not claimed as a median scale.
No full-strip sufficiency premise or new external theorem is used; no conflicting upper bound or uniform positive gap is obtained.

The complete D78 author proof and review follow without abridgment.
Historical pending-review or pending-adoption sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.
G0001 remains active and unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Coupled actual characters and stationary information

Date: 2026-10-10.
Starting question: Build beyond finite-quotient Fourier false positives.
Couple actual expanding or neutral characters to residues or other actual-law constraints; seek a quantitative stationary/tightness interface, constructive certificate, or precisely informative obstruction, keeping original probabilities and all degree/near-one costs.

Current author result: genuinely stationary low-information laws obey explicit all-q residue-entropy and finite-support bounds.
Coupling those constraints to actual Salem geometry gives support-radius costs.
A further stationary neutral-energy identity strengthens the radius cost and bounds the full second moment; an actual norm-isolation ball and the sharper mod2 Shannon bound also give high-probability neutral escape along a hypothetical near-one sequence.
The distinctions between support, moment and concentration are retained.
This proof-only work is self-checked and ready for a separately organized noncontributor review.
The unrestricted Task remains active and unresolved.

### Reuse and the new constraint

The author reread [L208](Yin_L_G0208_v1.md#stationary-fourier-fixed-scope) and [L201](Yin_L_G0201_v1.md#actual-stationary-information-variational-interface).
L208's original-row finite-character lifts are not stationary probabilities on the actual state space.
Here full actual stationarity is an essential premise throughout: it allows the original d-step quotient convolution to be compared with a stationary endpoint flow at a cost of exactly d I(Q).
This produces a family of actual residue-entropy constraints and, after coupling to the necessary real strips and the algebraic-integer norm grid, a degree/near-one lower cost for finite stationary supports.
The prior cosine rate is not optimized.

The bounded local screen found no retained hypercontractive quotient/support statement.
The proof below derives the needed elementary finite-norm inequality and tensorization, rather than adopting an external hypercontractivity theorem.
Fourier diagonalization, convexity and tensorization are classical mechanisms; no novelty claim is made for them.
The original probabilities remain p_0=1/2 and p_+=p_-=1/4.
The coordinator supplied the research question and allocation coordination, not the deductions.
No program or new source is needed for this proof-only round.

<a id="stationary-quotient-path-information"></a>
### 1. Genuine stationarity and the exact d-step residue law

Let alpha be any algebraic unit of degree d, including torsion, O=Z[alpha], and D its actual original return core.
Let Q be an admissible positive recurrent irreducible auxiliary law on a subset of D containing0, with stationary probability pi, as in L201.
It uses only edges x -> alpha x+eta with eta in{-1,0,1}.
Its original-law information is

    I=I(Q)=sum_x pi(x) D(q_x||p),       0<=I<=log4.

No finite entropy of pi is assumed.
Starting in pi, the relative entropy of the length-d Q path relative to the original iid-digit path from the same initial distribution is exactly dI, by the chain rule and stationarity.
All original digit probabilities are positive.
The expected absolute one-step log likelihood is at most log3+log4, by the three-point entropy bound and min p=1/4, so the finite path rearrangement is integrable.
This comparison uses the full original process, not a normalized killed law.

Fix an integer q>=2, write F_q=O/qO, M=q^d and nu=pi mod qO.
Since the minimal polynomial is monic of degree d, the actual power basis1,alpha,...,alpha^(d-1) identifies F_q with (Z/qZ)^d.
After d original steps,

    X_d=alpha^d X_0+sum_(j=0)^(d-1) eta_(d-j) alpha^j. (1)

The noise coefficients in this basis are independent copies of the original ternary law modulo q.
Multiplication by alpha^d is a permutation because alpha is a unit.
Denote this original finite-quotient transition by P_q^(d).
Data processing on the pair of initial and final residues gives

    D(J || nu P_q^(d)) <= dI,                        (2)

where J is the Q joint law of the two residues and both its marginals are nu.
The projected Q process need not be Markov; (2) needs only the actual stationary endpoint flow.
This is the premise absent from L208's zero-cost false positives.

For q=2, each ternary digit has even/odd probabilities1/2,1/2.
Hence the d-step original residue is exactly uniform independently of the actual initial state.
Retaining that actual initial state in data processing gives the sharper identity and bound

    D(nu||Unif(F_2))
      +MI_Q(X_0; X_d mod2O) <= dI,
    H(nu) >= d(log2-I).                              (3)

The decomposition is valid even for infinite-entropy pi: the second variable has only2^d values and the conditional relative entropies are bounded by d log2.
In particular any finite actual stationary support has at least exp[d(log2-I)] states.
Section3 strengthens this for low I by allowing q to grow.

<a id="cyclic-noise-tensor-contraction"></a>
### 2. An elementary norm contraction for the actual cyclic noise

All norms in this section use normalized uniform measure.
Let C_q act on real functions on Z/qZ by

    C_q f(x)=(2f(x)+f(x-1)+f(x+1))/4.

Its Fourier eigenvalues are cos^2(pi_number k/q),0<=k<q.
Set

    gamma_q=cos^2(pi_number/q),
    delta_q=1-gamma_q^2,
    epsilon_q=delta_q/(2+log q),
    p_q=2-epsilon_q,    a_q=p_q/2.                    (4)

Here pi_number is the circle constant, distinct from the stationary probability pi.
We have0<epsilon_q<1/2 and1<p_q<2.
The exact contraction to be proved is

    ||C_q f||_2 <= ||f||_(p_q) for every f>=0.         (5)

First, for any finite probability space,1<p<=2 and f>=0, put m=Ef and h=f-m.
Then

    ||f||_p^2 >= m^2+(p-1)||h||_p^2.                 (6)

If m=0 the assertion is trivial.
Otherwise u_t=m+t h is positive for0<=t<1.
For S_t=E u_t^p and F(t)=S_t^(2/p), direct differentiation gives

    F''(t)=2(2-p)S_t^(2/p-2)(E u_t^(p-1)h)^2
             +2(p-1)S_t^(2/p-1)E u_t^(p-2)h^2.

Holder's inequality, applied to

    |h|^p=(u_t^(p-2)h^2)^(p/2) u_t^(p(2-p)/2),

shows S_t^(2/p-1)E u_t^(p-2)h^2>=||h||_p^2.
Thus F''>=2(p-1)||h||_p^2, while F(0)=m^2 and F'(0)=0.
Integrating up to t<1 and passing continuously to1 proves(6), including zeros of f at the endpoint.

On q equally weighted points, ordinary finite-sum norm comparison gives

    ||h||_p^2 >= q^(1-2/p)||h||_2^2.

Fourier diagonalization gives

    ||C_q f||_2^2 <= m^2+gamma_q^2||h||_2^2.

It therefore suffices that (p_q-1)q^(1-2/p_q)>=gamma_q^2.
Write epsilon=epsilon_q.
Using -log(1-epsilon)<=2epsilon and epsilon/(2-epsilon)<=epsilon, valid for0<=epsilon<1/2, gives

    log[(p_q-1)q^(1-2/p_q)]
      =log(1-epsilon)-epsilon log q/(2-epsilon)
      >=-epsilon(2+log q)=-delta_q.

Since exp(-delta_q)>=1-delta_q=gamma_q^2, (5) follows.
The case q=2, where gamma_q=0, is included.

The contraction tensorizes without a dimensional constant:

    ||C_q^(tensor d) f||_2 <= ||f||_(p_q), f>=0.       (7)

For two coordinates, apply(5) in one variable, exchange the mixed norms by Minkowski's integral inequality

    ||g||_(L^2_y L^p_x) <= ||g||_(L^p_x L^2_y), p<=2,

and then apply(5) in the other variable.
This proves(7) for two factors; induction gives d factors.
All intermediate functions remain nonnegative.
Equivalently the displayed mixed-norm inequality follows by applying the triangle inequality in L^(2/p) to |g|^p; it introduces no unproved independence of the argument f.
In(1), the extra multiplication-by-alpha^d permutation preserves every normalized L^p norm.
Consequently

    ||P_q^(d) f||_2 <= ||f||_(p_q), f>=0.             (8)

The tensor product is the actual d-step quotient law, not a substitute independent process on actual states.

<a id="actual-stationary-residue-renyi-bound"></a>
### 3. Residue entropy and actual finite support at low information cost

For a stationary endpoint flow J on F_q with marginal nu, define

    Z=sum_(x,y) sqrt(nu(x)nu(y)) P_q^(d)(x,y).

This is positive because J has at least one supported edge.
Stationarity cancels the finite log nu coboundary on its nonzero support, so the log-sum inequality gives

    D(J||nu P_q^(d))
      =D(J || [sqrt(nu(x)nu(y))P_q^(d)(x,y)]_(x,y))
      >=-log Z.                                     (9)

The middle reference array is not a probability; explicitly its divergence equals D(J||W/Z)-log Z.
There is no assertion of full-state entropy finiteness here: nu is a finite distribution and its zero entries carry no J mass.

Put f(x)=sqrt(M nu(x)), so ||f||_2=1 in normalized uniform measure.
Cauchy--Schwarz and(8) imply

    Z=<f,P_q^(d)f> <= ||f||_2 ||P_q^(d)f||_2
                   <= ||f||_(p_q).

For0<a<1 define H_a(nu)=(1-a)^(-1)log sum_x nu(x)^a.
Direct calculation gives

    -log||f||_(p_q)
       =epsilon_q/(2p_q) [d log q-H_(a_q)(nu)].

Together with(2),(9), this proves the exact all-q bound

    H_(a_q)(pi mod qO)
      >=d log q-(2p_q/epsilon_q)d I.                 (10)

The constants can be simplified without dependence on alpha or d.
Since sin(pi_number/q)>=2/q for q>=2,

    delta_q=1-cos^4(pi_number/q)>=sin^2(pi_number/q)>=4/q^2,
    2p_q/epsilon_q <= q^2(2+log q).

Thus

    H_(a_q)(pi mod qO) >=d[log q-q^2(2+log q)I].      (11)

If pi has finite actual support of cardinality V, its residue support has at most V elements and every Renyi entropy is at most log V.
Therefore

    V >= exp{d[log q-q^2(2+log q)I]} for every q>=2.  (12)

This concerns a genuinely stationary law on the actual core.
It is not a restatement of L208's nonstationary uniform-residue construction.

For an explicit low-I version suppose0<I<=exp(-6), let L=log(1/I), and choose

    q=floor[(4IL)^(-1/2)].

The bracket is at least2, so q>=1/(4sqrt(IL)) and q>=2.
Also log q<=L/2, whence

    q^2(2+log q)I <=1/8+1/(2L)<=5/24<1/4.

Equation(12) yields

    V >= [exp(-1/4)/(4sqrt(I log(1/I)))]^d.           (13)

All constants are explicit, and the original d-step cost is included.
The lower bound can be less than one outside the useful low-I range; no meaningful gain is claimed there.
An I=0 finite support would contradict(12) as q tends to infinity, but no unattained zero-cost law is inserted into(13).

<a id="low-information-neutral-radius-cost"></a>
### 4. Coupling to actual real strips: a varying-input neutral radius cost

Now let alpha=beta>1 be Salem of degree d>=4 and m=log beta.
This section requires only the universally necessary real strips of actual returning states,

    |x_+|<B=1/(beta-1),    |x_-|<S=beta/(beta-1).

It does not require the sufficient full-strip theorem or a complete compact-termination certificate for this input.
Let rho^2=sum_j |sigma_j(x)|^2 over one root from each neutral pair.
If a stationary support lies entirely within rho<=R, the integer norm gives the explicit state-count bound

    V <= (2B+2)(2S+2)(2sqrt(2)R+2)^(d-2).            (14)

Indeed, partition each real embedding coordinate into half-open unit intervals and each real/imaginary neutral coordinate into intervals of length1/sqrt(2).
Two different algebraic integers in a common product cell have all real conjugate differences of absolute value less than1 and all complex conjugate differences of modulus less than1, contradicting their nonzero integer norm.
The bounded intervals intersect at most the displayed numbers of cells.
This is the fixed L91 norm-grid mechanism applied to the actual strip; no maximal-order assumption, discriminant constant or unknown lattice-packing constant is omitted.

Combining(12),(14) gives, for every q>=2,

    2sqrt(2)R+2
       >=[(q exp(-q^2(2+log q)I))^d
                            /((2B+2)(2S+2))]^(1/(d-2)). (15)

This lower bound is a support-radius requirement, not an upper bound on any return time or a probability estimate.
A support bounded in rho is automatically finite by(14), so no separate finiteness hypothesis is hidden in this application.

The near-one cost can be uniform in degree.
Suppose d>=6,

    0<m<=exp(-6)/2,    0<I<=2m,
    c_1=exp(-1/4)/(4sqrt(2)).

The function u log(1/u) is increasing up to exp(-1), so I log(1/I)<=2m log(1/m).
Since B<=1/m and S=B+1, we also have(2B+2)(2S+2)<=24/m^2.
Equation(13) then implies the sharper degree-dependent form

    2sqrt(2)R+2 >=24^(-1/(d-2)) c_1^(d/(d-2))
        *m^(-(d-4)/(2(d-2)))
        *[log(1/m)]^(-d/(2(d-2))).                  (16)

In particular, uniformly over every such d>=6,

    2sqrt(2)R+2 >= C_* m^(-1/4)[log(1/m)]^(-3/4),
    C_*=24^(-1/4)c_1^(3/2)>0.                       (17)

The comparison uses d/(d-2)<=3/2 and(d-4)/(2(d-2))>=1/4, with m<1 and log(1/m)>1.
Its right side tends to infinity as m decreases to zero.
Thus every finite supported actual stationary law with information at most2m must escape every fixed neutral support radius along any hypothetical such near-one Salem sequence, with a stated degree-uniform necessary rate.
This does not construct a near-one sequence or disprove one.

L201 ensures finite admissible laws with information arbitrarily close to h_2(beta)<=m, so I<=2m is a relevant nonvacuous approximation condition at every fixed input in the displayed range, if such an input exists.
The result gives a required state-space cost of those approximations; it gives neither an upper radius nor a uniform lower information gap.
The d=4 formula(16) has no negative power of m and is not included in the uniform divergence assertion.

Section5 below gives a stronger radius requirement on the same Salem finite supports by adding the genuine stationary neutral-energy equation.
Equations(10)--(13) retain a separate all-unit support-cardinality and residue-entropy conclusion; the weaker radius consequence(17) is not presented as the strongest final bound.

<a id="stationary-neutral-energy-information"></a>
### 5. Actual stationary neutral energy forces a stronger second-moment cost

Continue with a Salem input and s=(d-2)/2 selected neutral pairs.
For an actual state x write z=(sigma_1(x)...,sigma_s(x)), A=diag(zeta_1,...,zeta_s), and rho=||z||.
The chronological neutral update is exactly

    z -> Az+eta e,    e=(1,...,1).

Define the two actual Q row moments

    b_x=E_Q(eta|x),    c_x=E_Q(eta^2|x).

The information controls both, with explicit original-law constants:

    E_pi b_x^2 <= I,
    E_pi c_x >= 1/2-sqrt(I/2).                       (18)

For the first, the original moment generating function is E_p exp(t eta)=cosh^2(t/2)<=exp(t^2/4).
The inequality log cosh u<=u^2/2 follows by integrating tanh u<=u for u>=0 and using symmetry.
The elementary relative-entropy variational inequality therefore gives D(q_x||p)>=t b_x-t^2/4 for every real t; choosing t=2b_x proves D(q_x||p)>=b_x^2.
For the second, mapping eta to eta^2 and using log-sum gives

    D(q_x||p)>=c_x log(2c_x)+(1-c_x)log(2(1-c_x))
                 >=2(c_x-1/2)^2.

The last inequality follows by differentiating twice, or the g''>=1 calculation in the retained L92 binary divergence interface.
Averaging and Cauchy--Schwarz prove(18).
Thus no replacement of the original digit variance by an auxiliary iid variance has occurred.

Suppose first that M_2=E_pi rho^2 is finite.
Full stationarity of Q gives the exact integrated energy equation

    0=2 E_pi[b_x Re sum_j zeta_j z_j]+s E_pi c_x.      (19)

The cross term is integrable because |Re sum_j zeta_j z_j|<=sqrt(s)rho, |b_x|<=1 and M_2<infinity.
Consequently(18) and Cauchy--Schwarz yield, for I>0,

    M_2 >= s(1/2-sqrt(I/2))_+^2/(4I).               (20)

If M_2 is infinite, this extended-real lower bound holds automatically; no energy cancellation is performed in that case.
For0<I<=1/32 it simplifies to

    E_pi rho^2 >=9s/(256 I).                         (21)

In particular any actual stationary support contained in rho<=R satisfies

    R >= (3/16)sqrt(s/I).

Under0<I<=2m and m<=1/64, the degree/near-one form is

    R >= (3/32)sqrt((d-2)/m),
    E_pi rho^2 >=9(d-2)/(1024 m).                    (22)

These conclusions use every neutral coordinate and no phase spacing or root separation.
They apply to any genuinely stationary admissible law, regardless of whether a full-strip sufficiency theorem has been proved.
The radius assertion is for its full support; the moment assertion allows infinite supports and infinite moments.
The energy argument is stronger than Section4's radius consequence, but does not replace its actual residue entropy and support-size information.
It also does not give an upper moment or a uniform entropy gap.

<a id="mod-two-isolation-quantile-escape"></a>
### 6. A genuine concentration consequence, without a second-moment assumption

The sharper mod2 Shannon statement(3) also bounds every individual residue mass.
For t=nu(r) and u=2^(-d), log-sum onto{r},its complement gives

    dI>=D(nu||Unif)>=t d log2-H_binary(t)
                         >=t d log2-log2.

Thus, for every residue r in O/2O,

    pi(r+2O) <= I/log2+1/d,
    pi(0) <= I/log2+1/d.                             (23)

The mass on the single state0 is bounded by its residue-class mass.
This conclusion applies to all admissible stationary laws, including infinite-support and infinite-variance laws.
If a critical information minimizer exists, its I=h_2<=m gives the same inequality with I replaced by m; no existence or attainment is inferred.

There is a useful actual Salem isolation radius with a degree-only lower bound.
Since P is irreducible and noncyclotomic, P(1) is a nonzero integer.
Factoring over its conjugates gives

    1<=|P(1)|=(beta-1)^2/beta *product_j |1-zeta_j|^2,
    BS=beta/(beta-1)^2 <=product_j |1-zeta_j|^2<=4^s. (24)

For any nonzero actual returning state x, the strict necessary real strips and arithmetic-geometric mean give

    1<=|N(x)|<BS product_j|z_j|^2
                    <=BS(rho^2/s)^s.

Consequently rho>J_beta=sqrt(s)(BS)^(-1/(2s))>=sqrt(s)/2.
This is an application of the actual norm-isolation mechanism, not replacement by a larger module.
In particular the closed neutral ball rho<=sqrt(s)/2 contains only0 from the actual core.
Combining with(23),

    pi{rho<=sqrt(s)/2} <= I/log2+1/d.                (25)

Along any hypothetical Salem sequence with m tending to zero and actual stationary laws with I<=2m, (24) forces s and d to infinity because BS tends to infinity.
Hence the right side of(25) tends to zero and the radius sqrt(s)/2 tends to infinity.
The distributions of the scalar neutral radius therefore escape every fixed bounded interval in probability, including for infinite-variance stationary laws.
This is a true concentration conclusion, not an inference from the large moment in(20).

For an explicit m-dependent threshold, (24) gives s>=log(BS)/log4 and d>=2+log(BS)/log2.
Whenever BS>1,

    pi{rho<=(1/2)sqrt(log(BS)/log4)}
       <=2m/log2+1/[2+log(BS)/log2]                 (26)

under I<=2m.
This radius is of order sqrt(log(1/m)) as m tends to zero.
It is weaker than the full-support scale in(22).
We do not upgrade it to a high-probability radius of order sqrt(d/m), because a large second moment alone permits rare large tails.

<a id="stationary-neutral-concentration-boundary"></a>
### 7. General-q concentration and its remaining boundary

For a possibly infinite actual stationary law, let A_R={x in D: rho(x)<=R}, t=pi(A_R), and let N_R denote the right side of(14).
Put

    b_R=min(1,N_R/q^d),
    p=p_q,    a=p/2.

If t>=b_R, the actual concentration is constrained by

    exp(-p d I)
      <= b_R^(1-a)t^a+(1-b_R)^(1-a)(1-t)^a.           (27)

To prove this, let E be the residue image of A_R, b=|E|/q^d<=b_R, and v=nu(E)>=t.
Concavity of z^a and maximization within E and its complement give

    ||sqrt(q^d nu)||_p^p
      <=b^(1-a)v^a+(1-b)^(1-a)(1-v)^a.

For v>=b the right side decreases in v, and for b<=v it increases in b, as direct differentiation shows.
Thus v>=t>=b_R>=b gives the right side of(27).
The endpoint conventions are by continuity.
Equations(2),(9) and the norm bound give exp(-p dI)<=||sqrt(q^d nu)||_p^p, proving(27).
For t=1 it recovers the support constraint with the exact p-dependent constant.
If t<b_R, no extra assertion is needed.

Unlike the support bound, (27) visibly retains dI in its exponential.
The Renyi inequality alone does not justify the stronger scale in(22) for a median neutral radius; the valid concentration conclusion in(25)--(26) uses additional Shannon and actual norm information.
Here is a precise algebraic warning at the finite quotient level, not a counterexample made from an actual stationary law.
On a set of M=q^d points fix0<epsilon<1 and define

    nu_M=(1-epsilon)delta_0+epsilon Unif_M.

For fixed q and its a=a_q<1, direct summation gives

    H_a(nu_M)=log M+[a/(1-a)]log epsilon+o(1)
                as d tends to infinity.

The per-degree Renyi deficit tends to zero, while nu_M(0) tends to1-epsilon.
Therefore a lower Renyi entropy per degree near log q is compatible, by itself, with a large atom.
No claim is made that this example satisfies all actual path, stationary or infinite-family quotient constraints.
It identifies the missing step in inferring full tightness from(10) alone.
A stronger Shannon, multiscale or path-coupled argument may improve this boundary; it has not been proved here.

### 8. Self-check and continuing scope

The author self-check covers the genuine stationary path KL and projected non-Markov endpoint flow; actual power-basis independence modulo every integer q; q=2 digit merging and the actual-initial-state mutual information; cyclic Fourier eigenvalues; endpoint zeros in the elementary Lp convexity argument; the direction of the mixed-norm inequality and its tensorization; the finite marginal coboundary in(9), with no full-state entropy assumption; every constant in(11)--(17); the norm-grid count in the original order; original-law row mean/variance costs and integrability of(19); all constants in(20)--(22); the residue-versus-state distinction in(23); the P(1) product and strict norm-isolation ball; the separate support, moment and concentration conclusions; and the nonstationary scope of the final finite-quotient warning.

The outcome is a genuinely stationary, degree-explicit family of arithmetic character constraints, a near-one cost for finite approximating supports and full neutral second moments, and a distinct high-probability neutral escape consequence from mod2 entropy and norm isolation.
The stationary energy computation extends the familiar positive iid neutral drift by charging the actual state-dependent compensating bias in relative entropy; it does not assume the original iid law is stationary.
The elementary binary divergence used in(18) was locally checked in [L92](Yin_L_G0092_v1.md#binary-increment-js-divergence); the actual-order [norm-grid](Yin_L_G0091_v1.md#norm-grid-support-bound) and [norm-isolation](Yin_L_G0187_v1.md#ideal-zero-class-isolation-scale) mechanisms are the retained L91/L187 interfaces with the displayed constants and P(1) consequence proved here.
L187's narrow-domain constant is not copied to the full strip: the factor BS and strict inequalities are explicitly rederived in Section6.

These results do not repeat a closed L153 seed/window test or produce only a weaker entropy-rate constant.
They also do not complete a gap mechanism: there is no conflicting uniform upper support/moment bound, and(27) retains the stated obstacle to promoting the strong full-support scale to a matching quantile statement.
No new computation or external theorem is a proof premise, no fixed source or route was modified, and no unrestricted G0001 completion is asserted.
A separately organized full noncontributor review remains to be arranged after the author freezes this proof.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0107_v1.md#independent-review-stationary-geometry), with its original inspected scope and relationship.
