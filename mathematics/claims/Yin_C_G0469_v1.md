---
author: Yin
---
# Complete Gaussian block loss with arbitrary couplings and every fixed inverse lag

All original seven sections and22equations, full original-law normalization, conditional-law distinction and saturation/lag costs are retained.
L267 keeps its meaningful proof development, contribution/caution/source boundaries and original fixed review input; no Task/E resumes.

The [complete historical comparison](../audits/reviews/Yin_R_G0682_v1.md#l267-and-r166) retains the original R166 whole UNKNOWN, its actual 2026-10-10T01:59 completion and every source/control/contribution limit.
The [original complete author SELF](../audits/reviews/Yin_R_G0677_v1.md#arbitrary-coupling-original-author-finding) keeps its actual day precision.

## Statement

Put a0=log2. For EVERY real A>=a0 define

    kappa(A)=min{sqrt(pi/A)*exp(-pi^2/a0),
                 exp(-25A/16)*(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,K(A)=2+4A^2/gamma(A),
    u(A)=exp(-A)/2,
    Delta_A(t)=u(A)*gamma(A)*t^2/
                      [2*(K(A)*gamma(A)*t^2+log2)].

For a in[a0,A], let F_a(y)=sum_(e=-1)^1 exp[-a(e+y)^2], c_a=1+2exp(-a), pi_a(e)=exp(-a*e^2)/c_a.
The COMPLETE logarithmic loss satisfies d_a(y)=log(c_a/F_a(y))>=gamma(A)*y^2 for EVERY real y, including both branch endpoints and unbounded shifts.

Let b>=1 be ANY integer, C ANY real unit upper triangular b-by-b matrix, x ANY vector in R^b, and a_i ANY exponents in[a0,A].
For EVERY e in{-1,0,1}^b set

    y_i=x_i+sum_(j>i)C_(i,j)e_j,
    E(e)=sum_i a_i(e_i+y_i)^2,Z=sum_e exp[-E(e)],
    P_C,x(e)=exp[-E(e)]/Z,Pi(e)=product_i pi_(a_i)(e_i),
    G=log[(product_i c_(a_i))/Z].

All laws are strictly positive on their finite domains, and all logarithms and KL divergences use natural units.
For the ACTUAL reverse conditionals p_i under P_C,x given ALL later digits and the DISTINCT scalar tilts q_i(e|future)=exp[-a_i(e+y_i)^2]/F_(a_i)(y_i),

    G=sum_i E_P D(p_i||q_i)+sum_i E_P d_(a_i)(y_i)>=0,
    sum_i E_P D(p_i||q_i)<=G,
    sum_i E_P y_i^2<=G/gamma(A),D(P_C,x||Pi)<=K(A)*G.

The actual p_i need not equal q_i; earlier energy terms can affect them.
For ANY one strict-upper entry t=C_(i,j), i<j,

    Z<=product_l c_(a_l)*exp[-Delta_A(t)]

UNIFORMLY over ALL shifts and every other real entry, with no coefficient/matrix-norm/smallness restriction or factors3^b/2^b.
Delta_A is continuous/even, zero at0, strictly increasing with abs(t)>0 and bounded with limit u(A)/(2K(A)); t0 is treated without division.
Only one loss per COMPLETE block is justified; overlapping entry losses cannot be summed.
The product comparison law is an analytic device and never replaces the original digit or return-conditioned law.

For the ACTUAL monic minimal polynomial P=sum_(j=0)^d p_j t^j of ANY nonzero algebraic integer alpha, d>=1, put TOTAL m=log M(P), W=sum_j p_j^2.
Keep ORIGINAL independent difference digits mu(0)=1/2,mu(+1)=mu(-1)=1/4 and

    p_N=Pr(sum_(j=0)^(N-1)eta_j alpha^j=0),
    h2=lim_N[-log p_N]/N.

The collision-rate limit exists by blockwise equality/concatenation, including nonunits.
For EVERY integer1<=N<=d, p_N=2^(-N).
For N>d put k=N-d and B_N=[P,tP,...,t^(k-1)P] in ALL N coefficient rows.
The full constrained original probability is

    p_N=2^(-N)sum_(h in Z^k:norminf(B_Nh)<=1)
                          exp[-(log2)*norm2(B_Nh)^2].

Dropping ONLY the first d inequalities gives the integral unit-upper substitution e=Uh over the entire three-point cube, with U_(i,j)=p_(d+i-j), actual Gram--Schmidt expansion R and T=R*U^-1.
The complete upper sum has energy sum_i a_i(e_i+sum_(j>i)T_(i,j)e_j)^2, a_i=(log2)*delta_(i+1), exp(2m)<=delta_j<=W.
For ANY collection of pairwise DISJOINT consecutive blocks I in0,...,k-1, ANY one strict-upper principal-block entry t_I and ANY A_I>=a0 bounding its exponents,

    p_N<=U_N*exp[-sum_I Delta_(A_I)(t_I)],
    U_N=2^(-N)*product_(j=1)^k(1+2^(1-delta_j)).

The empty collection is allowed; A_I=Wlog2 always suffices.
Every outside tail is retained, each digit/square is paid once, and actual finite matrices/pivots are rational.
This is a finite computable certificate without a uniform onset claim or reported computation; no unit-only state or kernel theorem is extended to nonunits.

For m>0 use the ACTUAL exterior-root Blaschke product Bcal normalized Bcal(0)=s=exp(-m), with ALL exterior multiplicities and both members of nonreal pairs, and H=s/Bcal=sum_(ell>=0)h_ell*z^ell,h0=1.
The series is formal at0 or analytic near0, without analyticity throughout the unit disk.
The exact limits a_i->a_infinity=(log2)exp(2m) and T_(i,i+ell)->h_ell hold at EACH fixed ell, also when original unit-circle roots occur.
For ANY fixed ell>=1 with h_ell!=0, ANY A>a_infinity and0<epsilon<abs(h_ell), an INPUT-DEPENDENT all-future onset i0(P,ell,A,epsilon)>=0 supplies the exponent and corner bounds at every later index.
With g(m)=log[2/(1+2^(1-exp(2m)))], the complete finite statement for EVERY N>d is

    p_N<=2^(-d)*exp[-(N-d)*g(m)]
         *exp[-Delta_A(abs(h_ell)-epsilon)
                    *max{0,floor((N-d-i0)/(ell+1))}].

Taking N->infinity FIRST, then epsilon->0 and A->a_infinity, gives

    h2>=g(m)+Delta_(a_infinity)(h_ell)/(ell+1),
    h2>=g(m)+sup_(ell>=1)Delta_(a_infinity)(h_ell)/(ell+1).

This is a supremum of separately established scalar lag bounds, not an overlapping sum, growing-lag/finite-N exchange or uniformly bounded onset.
ALL shorter entries may be nonzero and arbitrarily large.
A genuine nonremovable interior inverse pole makes the coefficients unbounded along a subsequence, so SOME finite ell has abs(h_ell)>=1, without an effective first useful lag.
The direct Blaschke square-sum budget is not applied to this inverse.

For C=I+tE_(0,b-1),b>=2,x0 and every a_i=a>=log2, the exact ratio Z/c_a^b is always>=1/c_a and tends to1/c_a as abs(t)->infinity, so full log loss tends to log c_a independently of span b.
This arbitrary-real-matrix control is not asserted to be an actual polynomial orbit or an optimal constant.
The ACTUAL irreducible golden radicals P_r=t^(2r)-t^r-1,r=2^v,v>=1, have degree2r and FIXED total measure log phi,phi=(1+sqrt5)/2, and

    H_r=(1-phi^-1*z^r)/(1-phi*z^r),
    h_(nr)=phi^(n-1),h_j=0 if r does not divide j.

For EVERY fixed n>=2, the theorem applies at ell=nr despite nonzero shorter multiples of r, with complete finite onset and

    h2>=g(log phi)+Delta_(phi^2log2)(phi^(n-1))/(nr+1).

These inputs are nonreciprocal/fixed-positive-measure controls, not near-one coverage.
Their exact original residue product can give a stronger rate without1/r division; that is not silently substituted into this generic bound.
Bounded Delta makes THIS certificate tend to0 as n grows with r fixed.
For EVERY real M>0 the positive compact minimum D_M=min_(log2<=A<=exp(2M)log2)Delta_A(1)>0 gives h2>=g(m)+D_M/(ell+1) at an ACTUALLY detected abs(h_ell)>=1 and0<m<=M, uniformly in other entries/amplitude but NOT lag, degree or onset.
No unfinished D135 result is a premise, and no source theorem, program/numerical experiment, uniform near-one entropy floor, optimized rate, unrestricted gap or Task completion follows.

<a id="argument"></a>
## Complete retained argument

The dated author argument below retains its original question/source/contribution disclosures and limits; current adoption belongs only to the selected decision.

<a id="robust-block-loss-reuse-and-domain"></a>
### 1. Reuse, exact scope and the changed mechanism

Date: 2026-10-10.
The original argument introduces no numerical experiment or source acquisition.

The needed conclusion is a Gaussian block loss from a LARGE actual inverse coefficient while ALL intervening couplings remain unrestricted.
[L263](Yin_C_G0459_v1.md#argument) already supplies the original digit-coordinate partition, all fixed-diagonal limits and qualitative positive-measure coverage.
Its perturbative block estimate pays both a factor3^b and a factor2^b, and requires the other entries to be small.
[L264](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) proves that the relevant INVERSE coefficients are unbounded along a subsequence; its direct square-sum budget does not constrain them.
Neither result alone converts a large later coefficient into a loss in the presence of arbitrary middle couplings.

A local reuse screen by Gaussian shifts, relative-entropy chain/variational inequalities and finite-law mean bounds found sufficient ingredients: [L259's quantitative single-triple deficit](Yin_C_G0445_v1.md#quantitative-three-point-center-loss), [L102's relative-entropy variational calculation](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy), and [C531's elementary total-variation/relative-entropy bound](Yin_C_G0531_v1.md#stationary-neutral-concentration-cost).
The last gives TV(p,q)<=sqrt(D(p||q)/2), with its binary-partition proof retained there.
The finite entropy chain and finite exponential-tilt identities below are direct expansions of these already used notions; their general forms are not claimed as new results.
No new external theorem, source-proof audit or literature-priority claim is made.
L259's theta input remains at its accepted Nat26 formula scope.

The new contribution is the following use of these ingredients: a small TOTAL block loss forces the whole normalized block law close in relative entropy to the independent centered-triple law, with a constant independent of block length and every matrix entry.
Under that product comparison law a large entry cannot have small center displacement with high probability.
This yields a positive relative block deficit that depends on the entry and exponent bound only.
The product comparison law is an analytical device; it is not the original return-conditioned law and does not replace any original digit probability.

The coordinator supplied the broad missing-bridge question.
During author work it reported a separate unfinished D135 singular-value/lag-detection route.
That report is not a premise, and no part of its proof is imported below.
After Sections1--4 had been written, it requested particular care about the full conditional law versus its local exponential tilt and about unbounded shifts; those verification cautions added no derivation and are already addressed explicitly in Sections2--3.
All new block inequalities, their original-law assembly and controls in this draft are by structural_research for Yin.
The current author also authored L259/L263; those earlier proofs and their separate reviews retain their recorded roles.

Put a_0=log2.
For A>=a_0 define the already retained constant and two new explicit constants

    kappa(A)=min{sqrt(pi/A) exp(-pi^2/a_0),
                 exp(-25A/16)(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,
    K(A)=2+4A^2/gamma(A),   u(A)=exp(-A)/2.             (1)

In particular0<kappa(A)<1.
For a in[a_0,A] set

    F_a(y)=sum_(e=-1)^1 exp[-a(e+y)^2],
    c_a=F_a(0)=1+2exp(-a),
    pi_a(e)=exp(-a e^2)/c_a.                           (2)

All logarithms and relative entropies use natural units.
For strictly positive probability vectors p,q on a finite set, D(p||q)=sum p log(p/q); TV(p,q)=(1/2)sum|p-q|.
Every law used below is strictly positive on its finite domain, so no limiting support convention is needed.

<a id="quadratic-logarithmic-shift-deficit"></a>
### 2. The complete logarithmic shift loss is quadratic

L259 gives, for EVERY real y and a in[a_0,A],

    c_a-F_a(y)>=kappa(A) min{y^2,1},  F_a(y)<=c_a<=2.

We need a global quadratic estimate for its LOGARITHM, rather than a bounded quadratic deficit:

    d_a(y):=log(c_a/F_a(y))>=gamma(A)y^2
                   for every y in R and a in[a_0,A].  (3)

If |y|<=4, the inequality -log(1-v)>=v for0<=v<1 gives

    d_a(y)>=(c_a-F_a(y))/c_a
            >=(kappa(A)/2)min{y^2,1}
            >=kappa(A)y^2/32.

This includes y=0.
If |y|>=4, each |e+y|>=|y|-1, so

    F_a(y)<=3exp[-a(|y|-1)^2],
    d_a(y)>=a(|y|-1)^2-log3
             >=[(9log2-log3)/16]y^2.

Here (|y|-1)^2>=9y^2/16 and log3<=y^2 log3/16.
The last coefficient is larger than1/32: 9log2-log3=log(512/3)>log2>1/2, where the final strict inequality follows by integrating1/t on[1,2].
Since kappa(A)<1, this proves(3) with precisely the constant in(1).
There is no bounded-shift or bounded-tail restriction.

<a id="finite-block-entropy-loss-identity"></a>
### 3. Small block loss controls its entire normalized law

Let b>=1, let C be ANY real unit upper triangular b-by-b matrix, and let x in R^b be arbitrary.
Choose a_i in[a_0,A] for0<=i<b.
For e in{-1,0,1}^b write

    y_i(e)=x_i+sum_(j>i) C_(i,j)e_j,
    E(e)=sum_(i=0)^(b-1) a_i(e_i+y_i(e))^2,
    Z=sum_e exp[-E(e)],
    P_C,x(e)=exp[-E(e)]/Z,
    Pi(e)=product_i pi_(a_i)(e_i),
    G=log[(product_i c_(a_i))/Z].                     (4)

The notation P_C,x is an auxiliary finite probability law on all3^b retained digit vectors, not the original polynomial or original returned-word law.
Until Section5 there is no algebraicity hypothesis.
The key identity is

    G=sum_i E_(P_C,x) D(p_i(.|e_>i)||q_i(.|e_>i))
           +sum_i E_(P_C,x) d_(a_i)(y_i),             (5)

where p_i is the ACTUAL reverse conditional law of coordinate i under P_C,x, given all its later coordinates, and

    q_i(e|e_>i)=exp[-a_i(e+y_i)^2]/F_(a_i)(y_i).

These conditionals are generally different: earlier energy terms can influence p_i.
In particular(5) does not identify P_C,x with the inhomogeneous chain having conditionals q_i.

For a direct verification, the finite entropy chain gives H(P_C,x)=sum_i E H(p_i).
Expanding each conditional divergence gives

    sum_i E D(p_i||q_i)
       =-H(P_C,x)+E E(e)+sum_i E log F_(a_i)(y_i)
       =-log Z+sum_i E log F_(a_i)(y_i).

In the second line H(P_C,x)=E E(e)+log Z is the defining normalized-exponential identity.
Rearrangement proves(5).
Each term is nonnegative, hence G>=0.
By(3),

    sum_i E D(p_i||q_i)<=G,
    sum_i E y_i^2<=G/gamma(A).                       (6)

We claim the following dimension-independent comparison of WHOLE laws:

    D(P_C,x||Pi)<=K(A)G.                             (7)

To prove it, first fix one future and put pi=pi_(a_i), q=q_i, p=p_i and t=-2a_i y_i.
Completing the scalar square shows

    q(e)=pi(e)exp(te)/M(t),
    M(t)=sum_e pi(e)exp(te), L(t)=log M(t).

Thus L''(t) is the variance of e under the tilted three-point law, and0<=L''(t)<=1.
Direct differentiation and integration give

    D(q||pi)=tL'(t)-L(t)=integral_0^t v L''(v)dv
                         <=t^2/2.                   (8)

This holds also for t<0, because reversing the integral changes its sign while v is negative; L(0)=0.
The accepted finite TV bound gives

    |E_p e-E_q e|<=2TV(p,q)<=sqrt(2D(p||q)).

Expanding the logarithmic density ratio through q and using |t|sqrt(2D)<=D+t^2/2 now yields

    D(p||pi)=D(p||q)+t(E_p e-E_q e)+D(q||pi)
             <=2D(p||q)+t^2
             <=2D(p||q)+4A^2 y_i^2.                 (9)

Finally the relative-entropy chain against the PRODUCT law Pi is exactly

    D(P_C,x||Pi)=sum_i E D(p_i||pi_(a_i)).

Sum(9), then use(6).
The safe constant K(A)=2+4A^2/gamma(A) gives(7).
No matrix norm, coefficient bound, b-dependent error, moment of an infinite law or approximation of the other couplings appears.
The finite comparison remains valid when Z is arbitrarily small or the outside shifts are arbitrarily large.

<a id="arbitrary-middle-coupling-block-deficit"></a>
### 4. A large entry forces a loss despite arbitrary intervening entries

For t in R define

    Delta_A(t)=u(A)gamma(A)t^2 /
                  [2(K(A)gamma(A)t^2+log2)].          (10)

It is continuous, even, zero at0, strictly increasing in |t| for |t|>0, and tends to u(A)/(2K(A)) as |t| tends to infinity.
For ANY strict upper entry t=C_(i,j), i<j, the full block obeys

    Z<=product_l c_(a_l) exp[-Delta_A(t)]
                         uniformly over x in R^b.   (11)

All other entries of C can be arbitrary real numbers of arbitrary size.
One can select an entry of maximum absolute value and apply the same formula; multiplying losses from several entries in the SAME block is not claimed.

The case t=0 follows from G>=0.
Suppose t!=0 and let E_t={|y_i|>=|t|}.
Under Pi, condition on every coordinate other than e_j.
The value y_i then has the form z+t e_j.
At least one of |z+t| and |z-t| is at least |t|.
Each of the corresponding sign probabilities is

    pi_(a_j)(+1)=pi_(a_j)(-1)
                  =exp(-a_j)/c_(a_j)>=exp(-A)/2=u(A).

Consequently Pi(E_t)>=u(A), irrespective of all other coefficients and x.
Under P_C,x, (6) instead gives

    P_C,x(E_t)<=E y_i^2/t^2<=G/(gamma(A)t^2).         (12)

Use the finite relative-entropy variational inequality with the test function -(log2)1_(E_t).
In this finite setting it is simply nonnegativity of divergence from the normalized density proportional to exp[-(log2)1_(E_t)]Pi.
Its exact normalization is1-Pi(E_t)/2.
Therefore

    D(P_C,x||Pi)
       >=-(log2)P_C,x(E_t)-log[1-Pi(E_t)/2]
       >=u(A)/2-(log2)G/(gamma(A)t^2).                (13)

Combine(7) and(13), collect the G terms and divide by the positive denominator.
This gives G>=Delta_A(t), exactly(10)--(11).
All events use the weak inequality >=, so the case |z+t|=|t| or |z-t|=|t| is included.
There is no typical-set omission or tail truncation.

Unlike the prior perturbation estimate, (11) has NO factor3^b, NO factor2^b and NO smallness condition on the intervening entries.
It still bounds one complete block, not one original time step.
The chronological density expense when blocks are used repeatedly is retained next.

<a id="original-law-unrestricted-block-assembly"></a>
### 5. Complete finite original-law bound and every-lag rate interface

Let P(t)=sum_(j=0)^d p_j t^j be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha, p_d=1, d>=1, and put m=log M(P), W=sum p_j^2.
Keep the original independent difference law

    mu(0)=1/2, mu(+1)=mu(-1)=1/4,
    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0),
    h_2(alpha)=lim_(N->infinity) -log(p_N)/N.

The retained concatenation interface gives the limit.
For N<=d the exact value is p_N=2^(-N).
For N>d set k=N-d.
The exact full coefficient-matrix identity and its digit-coordinate upper bound, proved in L256 and L263, are

    B_N=[P,tP,...,t^(k-1)P] in all N coefficient rows,
    p_N=2^(-N) sum_(h in Z^k: ||B_N h||_infinity<=1)
                           exp[-(log2)||B_N h||_2^2],
    p_N<=2^(-N) sum_(e in{-1,0,1}^k)
             exp[-sum_(i=0)^(k-1) a_i
                    (e_i+sum_(j>i) T_(i,j)e_j)^2].     (14)

Here R is the Gram--Schmidt expansion matrix of the actual shifts of P, U_(i,j)=p_(d+i-j) is integral unit upper triangular, T=R U^(-1), and a_i=(log2)delta_(i+1).
Coefficients p_j outside0,...,d are zero, and all these matrices are restricted to indices0,...,k-1.
The pivots obey exp(2m)<=delta_j<=W.
The substitution e=Uh is a bijection of the retained integer points with the entire three-point cube.
Only the FIRST d original coefficient constraints have been dropped in the last line.
No replacement of mu, multiplicity loss, parity relaxation or finite-alphabet assumption about the original quotient h is made.
The auxiliary probability law in Section3 exists only to estimate the finite sum in this last line; it is not inserted into the definition of p_N.

Choose any collection of pairwise disjoint consecutive blocks I inside{0,...,k-1}.
In each block I choose ANY one strict-upper entry t_I of its principal matrix T_I.
Let A_I>=log2 bound all a_i in that block.
Then

    p_N<=U_N exp[-sum_I Delta_(A_I)(t_I)],
    U_N=2^(-N) product_(j=1)^k (1+2^(1-delta_j)).      (15)

The empty collection is permitted.
A_I=W log2 always suffices; sharper actual pivot bounds can be used.
To prove(15), eliminate retained digits in increasing chronological index.
At a chosen block, every later digit is fixed, giving an arbitrary real shift vector x.
Equation(11) bounds the sum over that whole block uniformly in this x.
Squares at strictly later indices do not depend on eliminated earlier digits.
At each unselected index use the single-triple maximum c_(a_i).
The same argument applies successively to every block, giving exactly(15).
Gaps between blocks cost their original maxima; no digit or square is charged twice.
Every finite outside tail remains in the calculation.
There is no geometric-series truncation or exceptional event.

The matrices R,U,T and all delta_j in a specified finite(15) are rational, determined by the actual polynomial and the indicated shifts.
The real functions in(1)/(10) are explicit.
Thus(15) is a finite computable certificate with full original normalization; its correctness is independent of an unproved uniform convergence time.
No computation is reported here.

Now assume m>0 and let r be the number of exterior roots, with all multiplicities and both members of each nonreal conjugate pair included.
Write s=exp(-m) and use the normalized actual exterior-root Blaschke product Bcal from L263, Bcal(0)=s.
Put

    H(z)=s/Bcal(z)=sum_(ell>=0) h_ell z^ell,
    h_0=1,  a_infinity=(log2)exp(2m).

The exact consumed L263 limits, including possible unit-circle original roots, are

    a_i -> a_infinity,
    T_(i,i+ell) -> h_ell for EACH fixed ell>=1.         (16)

The reciprocal series is formal at0, or analytic near0; no analyticity in the whole unit disk is required.
Unlike L263's first-nonzero-lag application, the following statement permits ANY lag ell with h_ell!=0, even if EVERY shorter lag is nonzero and large.

Fix such an ell, set b=ell+1, choose A>a_infinity, and choose0<epsilon<|h_ell|.
By(16) there is an integer i_0=i_0(P,ell,A,epsilon)>=0 such that simultaneously

    a_j<=A for every j>=i_0,
    |T_(i,i+ell)|>=|h_ell|-epsilon for every i>=i_0.
                                                               (17)

No estimate for any other entry is needed.
Use the consecutive b-blocks beginning at i_0,i_0+b,... in(15).
Since Delta_A is increasing in the absolute entry and U_N<=2^(-d)exp[-(N-d)g(m)], this proves, for EVERY N>d,

    p_N<=2^(-d)exp[-(N-d)g(m)]
          exp[-Delta_A(|h_ell|-epsilon)
                   max{0,floor((N-d-i_0)/(ell+1))}],
    g(m)=log[2/(1+2^(1-exp(2m)))].                    (18)

Taking -log, dividing by N and passing to the retained rate limit gives

    h_2(alpha)>=g(m)+Delta_A(|h_ell|-epsilon)/(ell+1).

For this fixed ell the right side is continuous as epsilon decreases to0 and A decreases to a_infinity.
The constant kappa is the minimum of two continuous positive functions.
Consequently

    h_2(alpha)>=g(m)+Delta_(a_infinity)(h_ell)/(ell+1),
    h_2(alpha)>=g(m)+sup_(ell>=1)
                         Delta_(a_infinity)(h_ell)/(ell+1).
                                                               (19)

The second line is the supremum of already proved scalar bounds for one fixed input, not an addition of overlapping losses, an exchange of growing lag with finite N, or a claim that their onsets are uniformly bounded.
Formula(18), with explicit A and epsilon and its actual i_0, remains the finite-time statement.

By L264 the inverse has a genuine pole inside the disk and its coefficients are unbounded along a subsequence.
In particular some finite ell has |h_ell|>=1.
Equation(19) then gives at least Delta_(a_infinity)(1)/(ell+1) beyond g(m), WITHOUT any condition on the smaller lags.
This connects genuinely large inverse coefficients to the complete original-law Gaussian loss, which the prior first-nonzero perturbation theorem could not do.
The existing first-nonzero theorem remains valid and may have a preferable short block on a particular input; the new result does not depend on it for qualitative coverage.

All conclusions of(14)--(19) are valid for general nonzero algebraic integers, including nonunits, at the original word-mass scope.
No chronological state kernel on an integer order, no actual-core equality and no unit-only norm theorem are extended to nonunits.

<a id="large-entry-saturation-and-actual-control"></a>
### 6. Complete controls and the unavoidable costs of this certificate

First consider a purely Gaussian control: fix a>=log2, b>=2, C=I+t E_(0,b-1), and x=0.
All middle coordinates factor, so

    Z_C(0)=c_a^(b-2)
               sum_(e,f=-1)^1 exp[-a(e+t f)^2-a f^2].

The f=0 contribution is c_a.
Every term with f=+/-1 tends to0 as |t| tends to infinity, because |e|<=1.
Therefore

    Z_C(0)/c_a^b -> 1/c_a,
    log[c_a^b/Z_C(0)] -> log c_a.                    (20)

In fact the ratio is at least1/c_a at every t, since the f=0 contribution is always present.
Thus a universal one-entry lower bound on the logarithmic loss cannot grow without limit as |t| grows, nor grow proportionally with b merely because the selected entry spans b coordinates.
The saturation of(10) is qualitatively compatible with this exact control.
It does not assert optimality of its small constant.
This matrix control is not asserted to come from an actual algebraic minimal polynomial; it limits the stated arbitrary-matrix theorem, not the original entropy or an arithmetic refinement.

For an ACTUAL control with nonzero middle couplings, use the retained irreducible golden radical family

    P_r(t)=t^(2r)-t^r-1,  r=2^v, v>=1,
    degree(P_r)=2r,  m(P_r)=log phi,
    phi=(1+sqrt5)/2.

L231 supplies its actual irreducibility and exact original-law residue decomposition, and L263/L264 supply the directly checked inverse coefficients

    H_r(z)=(1-phi^(-1)z^r)/(1-phi z^r),
    h_(nr)=phi^(n-1) for n>=1,
    h_j=0 when r does not divide j.                  (21)

Apply(18) with ANY fixed n>=2, ell=nr, A>phi^2 log2 and0<epsilon<phi^(n-1).
This gives a complete all-N original-law bound after i_0(P_r,nr,A,epsilon), and(19) yields

    h_2(alpha)>=g(log phi)
          +Delta_(phi^2 log2)(phi^(n-1))/(nr+1).      (22)

Inside these longer blocks the limiting entries at shorter positive multiples of r are nonzero, including h_r=1.
Hence they do not meet the old sufficient condition that all non-corner entries become arbitrarily small.
The new estimate still applies, and no cost depending exponentially on nr is incurred.
This is a genuine actual-input test of the changed hypothesis, proved symbolically from the retained exact formulas; no numerical experiment is claimed.

The family has FIXED positive total measure log phi, is nonreciprocal, and is not a sequence approaching measure one.
Its stronger exact residue decomposition from L231/L259 still avoids a1/r loss for its true rate; (22) is a new generic certificate, not a claimed best bound for this family.
Letting n grow without charging nr+1 would contradict the displayed finite block count.
Since Delta is bounded, this particular longer-lag certificate tends back to zero as n tends to infinity with r fixed.

There is also a near-one quantitative boundary internal to the new mechanism.
For any fixed M>0, a_infinity lies in[log2,exp(2M)log2] when0<m<=M.
Continuity and positivity in(1)/(10) give

    D_M:=min_(log2<=A<=exp(2M)log2) Delta_A(1)>0.

If an actual input in this range has a detected lag ell with |h_ell|>=1, then(19) gives h_2>=g(m)+D_M/(ell+1).
This is uniform in the coefficient amplitude and all middle couplings at that DETECTED lag.
It is not uniform in lag or degree.
An additional theorem bounding the first useful lag in terms of m,r or d would immediately give a correspondingly charged comparison, but no such theorem is invoked in this draft.
Even a bound growing like(r/m)log(r/m) would leave the reciprocal chronological expense; it would not by itself give a uniform positive entropy floor.
That conditional arithmetic expression is an illustration of cost accounting, not acceptance of the coordinator's unfinished D135 claim.

<a id="robust-block-loss-limits-and-selfcheck"></a>
### 7. Limits and the next discriminating question

The established gain is a relative bound on the COMPLETE translated finite cube.
It removes both exponential block factors in the old sufficient perturbation test, allows every intervening coefficient without restriction, and transfers to every fixed actual inverse lag through the full original probability partition.
It retains the total measure m, degree boundary d, actual exponents, all-future onset i_0, outside-tail uniformity and disjoint chronological density1/(ell+1).
It uses no uncontrolled conditional independence, no finite p_N lower bound for its limiting exponent and no typical-return truncation.

What remains open is not qualitative nonzero-lag coverage, which L263 already settled.
It is a useful varying-input rate after detecting LARGE inverse coefficients and paying the lag density and actual onset.
Several entries in one block cannot be counted separately by(11), because the same whole-law relative entropy controls them.
The exact control(20) shows why a merely longer isolated coupling cannot give a loss proportional to its span.
A changed next test should retain joint constraints that force many independent losses, exploit actual coefficient arithmetic or the discarded first d rows, or establish an actual reordering/residue decomposition with its full law and density.
It should distinguish these from optimizing the small constant in(10).

[L30's one-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) remains stronger at the leading near-one scale than the baseline g(m)~(log2)m.
The new bound is not asserted to overtake it uniformly; its detected lag can increase with the input.
The direct coefficient energy restriction of L264 still does not apply to H, while the large inverse amplitude still pays time.
The unrestricted mathematical problem remains unresolved; no unrestricted Mahler gap or Task/E execution is asserted.



### Actual whole checking and preserved limits

The maintaining agent read the only actual L267 version and ENTIRE R166, compared C445's full scalar proof, C459's complete word/strong-limit mechanisms and C461's entire inverse-pole section, then read C297/L220/C280/C212/C235 at their exact finite-entropy/rate/radical/comparison interfaces.
The finite Pinsker step uses only grouping positive/negative mass differences, log-sum and binary second derivative1/[u(1-u)]>=4; its surrounding stationary unit-chain theorem is not imported.
The complete logarithmic quadratic deficit, reverse-conditionals/scalar-tilt distinction, both tilt signs, whole-law entropy chain, exact weak-event/Delta constants and arbitrary other entries/shifts were checked without a matrix-size/truncation error.
Original mu/degree/first-d constraints/actual T order, complete chronological finite blocks/all-future onset, N-first continuity and scalar supremum were checked without adding overlapping losses.
All saturation and actual radical/full degree/measure/shorter-coupling/density controls and compact D_M guard were checked; unfinished D135 supplies no premise.
R166's shared history/generic brief does not establish its exact initial target context or ordering; upstream author/review roles alone establish neither target contribution nor isolation.
Its ENTIRE original finding remains UNKNOWN with exact scope/date/verdict; original author whole SELF is recorded only at its actual day precision.
Nat26-U003 is reused without expanding source depth or occurrence; GMR18's direct-derivative source is outside the inverse-pole step.
No program/J/native rerun, numerical simulation, source passage/PDF/proof reading, producer or Task/E execution occurred.
Current whole SELF is not fresh isolation or a uniform near-one/gap result.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:17 |
| status | open |
| reason | Retain the complete original all-real logarithmic/full-law-KL/arbitrary-coupling proof, exact original-law finite blocks/every-fixed-lag/onset/density and saturation/actual-radical/source/negative limits. Existing scalar/coordinate/inverse/finite-entropy mechanisms were compared without substituting their separate statements for this whole proof; no new source proof/program/research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole arbitrary-coupling theorem](#statement) | Every finite real triangular block/all shifts/exponent bounds/full-law KL/one-entry loss, every nonzero algebraic integer/nonunit word bound, all fixed inverse lags/onsets/disjoint density and every saturation/radical/cost/negative limit. |
| argument | [Entire original proof](#argument) | Complete Sections1--7/equations1--22, log deficit/actual conditionals/tilt/whole-law KL/all constants/weak-event endpoints, original weights/finite blocks/ordered limits and all controls/source/contribution boundaries. |
| dependency | [Complete scalar shift deficit](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | Full exact kappa(A) theta/paired-tail proof at every real shift/parameter/endpoint; no adjacent-nonzero restriction. |
| dependency | [Actual word coordinates and fixed limits](Yin_C_G0459_v1.md#argument) | Entire original mu/monic quotient/first-d discarded constraints/actual T=R U^-1/pivots and strong fixed-diagonal limits incl circle roots; old small-other-entry theorem is comparison. |
| dependency | [Exact inverse-pole separation](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Direct rational noncancellation/interior-pole/radius/unbounded-subsequence proof and actual radical coefficients, not a direct-l2 or GMR18 derivative theorem. |
| dependency | [Finite variational proof](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only complete bounded-test exponential-tilt/nonnegative-divergence derivation on finite positive laws; no smoothing geometry/source premise. |
| dependency | [Finite binary Pinsker proof](../ledger/Yin_L_G0220_v1.md#stationary-neutral-concentration-cost) | Only log-sum/two-set partition/binary second derivative>=4 proves TV<=sqrt(D/2); no unit-only stationary/neutral-concentration theorem extends to nonunits. |
| dependency | [Collision-rate existence](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | Only blockwise-equality collision supermultiplicativity/subadditivity/Fekete for any endomorphism; no external concentration or injectivity assumption. |
| dependency | [Actual radical degree and product law](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic tower/degree2r/relative degree r and actual residue-stream product at fixed r, no varying-r uniform limit or source gap theorem. |
| support | [Stronger one-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Exact original stronger parameter-dependent rate squeeze, comparison only, no new source proof/near-one sequence/uniform horizon. |
| support | [Existing theta reading](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 author/reviewer formula/notation/principal-root and original403/noartifact/book-proof-depth boundaries; no new source occurrence/read. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:19 |
| status | proved |
| reason | Adopt after actual complete C469/R677 SELF checking of all original Sections1--7/equations1--22 and every exact scalar/log-deficit/full-law-KL/conditionals/tilt/event constant, original mu/degree/T/finite-block/onset/disjoint-density/ordered-limit/every-lag and saturation/actual-radical/source/negative boundary. Adequate existing direct mechanisms were actually compared; R166 retains its ENTIRE original UNKNOWN scope and original author day-precision SELF. No program/native/source proof/PDF/new research/Task execution or fresh isolation is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole arbitrary-coupling theorem](#statement) | Every finite real triangular block/all shifts/exponent bounds/full-law KL/one-entry loss, every nonzero algebraic integer/nonunit word bound, all fixed inverse lags/onsets/disjoint density and every saturation/radical/cost/negative limit. |
| argument | [Entire original proof](#argument) | Complete Sections1--7/equations1--22, log deficit/actual conditionals/tilt/whole-law KL/all constants/weak-event endpoints, original weights/finite blocks/ordered limits and all controls/source/contribution boundaries. |
| dependency | [Complete scalar shift deficit](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | Full exact kappa(A) theta/paired-tail proof at every real shift/parameter/endpoint; no adjacent-nonzero restriction. |
| dependency | [Actual word coordinates and fixed limits](Yin_C_G0459_v1.md#argument) | Entire original mu/monic quotient/first-d discarded constraints/actual T=R U^-1/pivots and strong fixed-diagonal limits incl circle roots; old small-other-entry theorem is comparison. |
| dependency | [Exact inverse-pole separation](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Direct rational noncancellation/interior-pole/radius/unbounded-subsequence proof and actual radical coefficients, not a direct-l2 or GMR18 derivative theorem. |
| dependency | [Finite variational proof](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only complete bounded-test exponential-tilt/nonnegative-divergence derivation on finite positive laws; no smoothing geometry/source premise. |
| dependency | [Finite binary Pinsker proof](../ledger/Yin_L_G0220_v1.md#stationary-neutral-concentration-cost) | Only log-sum/two-set partition/binary second derivative>=4 proves TV<=sqrt(D/2); no unit-only stationary/neutral-concentration theorem extends to nonunits. |
| dependency | [Collision-rate existence](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | Only blockwise-equality collision supermultiplicativity/subadditivity/Fekete for any endomorphism; no external concentration or injectivity assumption. |
| dependency | [Actual radical degree and product law](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic tower/degree2r/relative degree r and actual residue-stream product at fixed r, no varying-r uniform limit or source gap theorem. |
| support | [Stronger one-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Exact original stronger parameter-dependent rate squeeze, comparison only, no new source proof/near-one sequence/uniform horizon. |
| support | [Existing theta reading](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 author/reviewer formula/notation/principal-root and original403/noartifact/book-proof-depth boundaries; no new source occurrence/read. |
| review | [Actual complete whole SELF](../audits/reviews/Yin_R_G0677_v1.md#arbitrary-coupling-whole-self-finding) | ENTIRE exact statement/argument/selected inputs, every arbitrary finite real block/shift/other-entry/actual conditional/original-law/nonunit/fixed-lag/onset/density/limit/control/source/negative scope; no fresh isolated review or uniform near-one gap. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:48 |
| status | proved |
| reason | Adopt the new isolated whole C469 finding after complete coordinator reading of R682, covering every scalar/KL/reverse-conditional/tilt/event/whole-block theorem and every original nonunit-law/lag/onset/limit/saturation/radical/source/cost interface. Initial mathematical conclusions preceded target R comparisons; necessary upstream fixed mathematics and its acceptance scopes were directly inspected. Preserve the entire original R166 UNKNOWN/author SELF and R677 SELF without retrospective change, and no effective lag, uniform entropy or actual polynomial coverage is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every finite real triangular block/all shifts/exponent bounds/full-law KL/one-entry loss, every nonzero algebraic integer/nonunit word bound, all fixed inverse lags/onsets/disjoint density and every saturation/radical/cost/negative limit. |
| argument | [Exact argument](#argument) | Complete Sections1--7/equations1--22, log deficit/actual conditionals/tilt/whole-law KL/all constants/weak-event endpoints, original weights/finite blocks/ordered limits and all controls/source/contribution boundaries. |
| dependency | [Exact dependency](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | Full exact kappa(A) theta/paired-tail proof at every real shift/parameter/endpoint; no adjacent-nonzero restriction. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#argument) | Entire original mu/monic quotient/first-d discarded constraints/actual T=R U^-1/pivots and strong fixed-diagonal limits incl circle roots; old small-other-entry theorem is comparison. |
| dependency | [Exact dependency](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Direct rational noncancellation/interior-pole/radius/unbounded-subsequence proof and actual radical coefficients, not a direct-l2 or GMR18 derivative theorem. |
| dependency | [Exact dependency](Yin_C_G0297_v1.md#disjoint-smoothing-relative-entropy) | Only complete bounded-test exponential-tilt/nonnegative-divergence derivation on finite positive laws; no smoothing geometry/source premise. |
| dependency | [Exact dependency](Yin_C_G0531_v1.md#stationary-neutral-concentration-cost) | Only log-sum/two-set partition/binary second derivative>=4 proves TV<=sqrt(D/2); no unit-only stationary/neutral-concentration theorem extends to nonunits. |
| dependency | [Exact dependency](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | Only blockwise-equality collision supermultiplicativity/subadditivity/Fekete for any endomorphism; no external concentration or injectivity assumption. |
| dependency | [Exact dependency](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one dyadic tower/degree2r/relative degree r and actual residue-stream product at fixed r, no varying-r uniform limit or source gap theorem. |
| support | [Exact support](Yin_C_G0235_v1.md#one-expanding-comparison) | Exact original stronger parameter-dependent rate squeeze, comparison only, no new source proof/near-one sequence/uniform horizon. |
| support | [Exact support](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Original10/10 DLMF1.2.8 author/reviewer formula/notation/principal-root and original403/noartifact/book-proof-depth boundaries; no new source occurrence/read. |
| review | [Exact review](../audits/reviews/Yin_R_G0682_v1.md#gaussian-block-isolated-whole) | Entire exact C469 Statement and complete Sections1--7/equations1--22 Argument, every whole-law conditional/finite/lag/limit/control/source/negative and nonunit boundary. |

